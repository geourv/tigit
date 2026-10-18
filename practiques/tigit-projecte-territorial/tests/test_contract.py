"""Resource preparation must preserve inputs and refuse ambiguous/changed trees."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace


spec = importlib.util.spec_from_file_location("tigit_prepare", Path(__file__).resolve().parents[1] / "preparar.py")
prepare = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prepare)


class ResourceFixture:
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="tigit-contract-", dir="/tmp/opencode")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.input = self.source / "data/raw/example.csv"
        self.input.parent.mkdir(parents=True)
        self.data = b"code,value\n001,4\n"
        self.input.write_bytes(self.data)
        self.destination = self.root / "snapshot"
        self.manifest = {"source_commit": "a" * 40, "files": [{"path": "data/raw/example.csv", "sha256": prepare.sha256(self.data), "bytes": len(self.data)}]}
        self.digest = "b" * 64


class ResourceContractTests(ResourceFixture, unittest.TestCase):
    def create(self):
        return prepare.prepare_snapshot(self.destination, self.manifest, self.digest, source=self.source)

    def test_copy_and_independent_readonly_check(self):
        self.assertTrue(self.create()["ok"])
        self.assertEqual(self.input.read_bytes(), self.data)
        copied = self.destination / "data/raw/example.csv"
        self.assertEqual(copied.read_bytes(), self.data)
        before = {p: p.read_bytes() for p in self.destination.rglob("*") if p.is_file()}
        self.assertTrue(prepare.check_snapshot(self.destination, self.manifest, self.digest)["ok"])
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_existing_snapshot_is_never_overwritten(self):
        self.create()
        with self.assertRaises(FileExistsError):
            self.create()

    def test_changed_input_fails_before_output_is_created(self):
        self.input.write_bytes(b"code,value\n001,9\n")
        with self.assertRaisesRegex(ValueError, "differs"):
            self.create()
        self.assertFalse(self.destination.exists())

    def test_traversal_and_alias_paths_are_refused(self):
        for value in ("../escape", "/absolute", "data/../escape", "data//raw/x", "data/./raw/x", "data\\x"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                prepare.relative_path(value)

    def test_symlink_input_is_refused(self):
        self.input.unlink()
        original = self.root / "elsewhere.csv"
        original.write_bytes(self.data)
        self.input.symlink_to(original)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            self.create()
        self.assertFalse(self.destination.exists())

    def test_missing_or_extra_snapshot_file_is_refused(self):
        self.create()
        extra = self.destination / "unexpected.csv"
        extra.write_bytes(b"unexpected")
        with self.assertRaisesRegex(ValueError, "undeclared"):
            prepare.check_snapshot(self.destination, self.manifest, self.digest)
        extra.unlink()
        (self.destination / "data/raw/example.csv").unlink()
        with self.assertRaisesRegex(ValueError, "missing"):
            prepare.check_snapshot(self.destination, self.manifest, self.digest)

    def test_altered_snapshot_and_manifest_are_refused(self):
        self.create()
        (self.destination / "data/raw/example.csv").write_bytes(b"different")
        with self.assertRaisesRegex(ValueError, "differs"):
            prepare.check_snapshot(self.destination, self.manifest, self.digest)
        with self.assertRaisesRegex(ValueError, "different resource manifest"):
            prepare.check_snapshot(self.destination, self.manifest, "c" * 64)

    def test_repository_manifest_preserves_twenty_data_inputs_and_one_audit_pdf(self):
        manifest, digest = prepare.load_manifest(Path(__file__).resolve().parents[1] / "recursos.yml")
        self.assertEqual(sum(row["path"].startswith("data/") for row in manifest["files"]), 20)
        self.assertEqual([row["path"] for row in manifest["files"] if not row["path"].startswith("data/")], ["outputs/figures/non-principal-housing-tarragones-2021.pdf"])
        self.assertEqual(len(digest), 64)


class QgisInputTests(ResourceFixture, unittest.TestCase):
    def setUp(self):
        super().setUp()
        prepare.prepare_snapshot(self.destination, self.manifest, self.digest, source=self.source)
        self.manifest["snapshot"] = "snapshot"
        self.authored = self.root / "authored"
        (self.authored / "activities").mkdir(parents=True)
        self.model = b"raise RuntimeError('The preparation must never execute this model')\n"
        (self.authored / "activities/model.py").write_bytes(self.model)
        self.request = {
            "schema_version": 2,
            "kind": "qgis-practice-request-v2",
            "script": "activities/model.py",
            "inputs": [{"id": "table", "path": "data/raw/example.csv", "sha256": prepare.sha256(self.data)}],
        }
        self.write_request()
        self.packet = self.root / "packet"

    def write_request(self):
        (self.authored / "activity-qgis.json").write_text(json.dumps(self.request), encoding="utf-8")

    def prepare_packet(self):
        return prepare.prepare_qgis_inputs(self.root, self.authored, self.packet, self.manifest, self.digest)

    def test_packet_preserves_source_bytes_and_only_declared_inputs(self):
        result = self.prepare_packet()
        self.assertTrue(result["ok"])
        self.assertEqual((self.packet / "activity-qgis.json").read_bytes(), (self.authored / "activity-qgis.json").read_bytes())
        self.assertEqual((self.packet / "activities/model.py").read_bytes(), self.model)
        self.assertEqual((self.packet / "data/raw/example.csv").read_bytes(), self.data)
        self.assertEqual({p.relative_to(self.packet).as_posix() for p in self.packet.rglob("*") if p.is_file()},
                         {"activity-qgis.json", "activities/model.py", "data/raw/example.csv", "origin.json"})
        with self.assertRaises(FileExistsError):
            self.prepare_packet()

    def test_request_cannot_silently_select_a_different_input_hash(self):
        self.request["inputs"][0]["sha256"] = "f" * 64
        self.write_request()
        with self.assertRaisesRegex(ValueError, "not bound"):
            self.prepare_packet()
        self.assertFalse(self.packet.exists())

    def test_request_cannot_escape_the_authored_source_root(self):
        self.request["script"] = "../outside.py"
        self.write_request()
        with self.assertRaises(ValueError):
            self.prepare_packet()
        self.assertFalse(self.packet.exists())

    def test_modified_resource_snapshot_prevents_packet_creation(self):
        (self.destination / "data/raw/example.csv").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "differs"):
            self.prepare_packet()
        self.assertFalse(self.packet.exists())


class WorkbookInputTests(ResourceFixture, unittest.TestCase):
    def setUp(self):
        super().setUp()
        processed = self.source / "data/processed/derived.csv"
        processed.parent.mkdir(parents=True)
        processed.write_bytes(b"derived\n")
        self.manifest["files"].append({"path": "data/processed/derived.csv", "sha256": prepare.sha256(b"derived\n"), "bytes": 8})
        prepare.prepare_snapshot(self.destination, self.manifest, self.digest, source=self.source)
        self.manifest["snapshot"] = "snapshot"
        self.authored = self.root / "authored"
        (self.authored / "scripts").mkdir(parents=True)
        (self.authored / "preparar.py").write_bytes(b"# source only\n")
        (self.authored / "scripts/requirements.txt").write_bytes(b"openpyxl==3.1.5\n")
        (self.authored / "scripts/model.py").write_bytes(b"raise RuntimeError('must not execute')\n")
        self.run = self.root / prepare.WORKBOOK_ROOT / "run01"
        module_spec = importlib.util.spec_from_file_location("tigit_paths", Path(__file__).resolve().parents[1] / "scripts/practice_paths.py")
        self.paths = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(self.paths)

    def create(self):
        return prepare.prepare_workbook_inputs(self.root, self.authored, self.run, self.manifest, self.digest)

    def selected_run(self):
        return patch.dict(self.paths.os.environ, {"TIGIT_PRACTICE_RUN": self.run.relative_to(self.root).as_posix(), "MCP_CONSUMER_WORKSPACE": str(self.root)})

    def test_copies_only_raw_inputs_and_keeps_the_resource_snapshot_immutable(self):
        self.assertEqual(self.create()["inputs"], 1)
        self.assertEqual({p.relative_to(self.run).as_posix() for p in self.run.rglob("*") if p.is_file()}, {"data/raw/example.csv", "run-inputs.json"})
        (self.run / "data/raw/example.csv").write_bytes(b"run-only edit")
        self.assertTrue(prepare.check_snapshot(self.destination, self.manifest, self.digest)["ok"])
        with self.assertRaises(FileExistsError):
            self.create()

    def test_source_changes_require_a_new_run(self):
        self.create()
        with self.selected_run(), patch.object(self.paths, "WORKSPACE", self.root), patch.object(self.paths.subprocess, "run", return_value=SimpleNamespace(returncode=0)):
            self.assertEqual(self.paths.project_root(), self.run)
            (self.authored / "scripts/model.py").write_bytes(b"changed source")
            with self.assertRaisesRegex(ValueError, "sources changed"):
                self.paths.project_root()

    def test_run_and_explicit_output_cannot_escape_sandbox(self):
        self.create()
        with self.selected_run(), patch.object(self.paths, "WORKSPACE", self.root), patch.object(self.paths.subprocess, "run", return_value=SimpleNamespace(returncode=0)):
            with self.assertRaises(ValueError):
                self.paths.run_path(self.authored / "outside.xlsx")
            with self.assertRaises(FileExistsError):
                self.paths.require_new_output(self.run / "data/raw/example.csv")
            for value in ("_practices/old/run", self.manifest["snapshot"], str(self.run), prepare.WORKBOOK_ROOT + "/../escape"):
                with self.subTest(value=value), patch.dict(self.paths.os.environ, {"TIGIT_PRACTICE_RUN": value}), self.assertRaises(ValueError):
                    self.paths.project_root()

    def test_altered_raw_copy_cannot_be_used_for_pinned_reproduction(self):
        self.create()
        (self.run / "data/raw/example.csv").write_bytes(b"changed observations")
        with self.selected_run(), patch.object(self.paths, "WORKSPACE", self.root):
            with self.assertRaisesRegex(ValueError, "input changed"):
                self.paths.project_root()

    def test_symlinks_and_unignored_runs_are_refused(self):
        self.create()
        with self.selected_run(), patch.object(self.paths, "WORKSPACE", self.root), patch.object(self.paths.subprocess, "run", return_value=SimpleNamespace(returncode=1)):
            with self.assertRaisesRegex(ValueError, "ignored"):
                self.paths.project_root()
            (self.run / "escape").symlink_to(self.source, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "Symlink"):
                self.paths.project_root()

    def test_live_acquisition_requires_explicit_opt_in(self):
        with patch.dict(self.paths.os.environ, {"TIGIT_FETCH_TEACHING_DATA": "0"}):
            with self.assertRaisesRegex(ValueError, "opt-in"):
                self.paths.require_network()


if __name__ == "__main__":
    unittest.main()
