#!/usr/bin/env python3
"""Prepare the fixed TIGIT teaching inputs; GIS, PDF and editions remain native.

recursos.yml uses the JSON subset of YAML so preparation needs only Python's
standard library. Its Git origin identifies the retained bytes, including
derived tables; it is not a claim of a new download from Idescat or ICGC.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.request import Request, urlopen


SOURCE_ROOT = Path(__file__).resolve().parent
WORKSPACE = SOURCE_ROOT.parents[1]
RESOURCE_ROOT = "sandbox/practiques/tigit-projecte-territorial/recursos"
QGIS_INPUT_ROOT = "sandbox/practiques/tigit-projecte-territorial/entrades-qgis"
WORKBOOK_ROOT = "sandbox/practiques/tigit-projecte-territorial/fulls"
MAX_FILE_BYTES = 16 * 1024 * 1024
MAX_TOTAL_BYTES = 64 * 1024 * 1024


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def relative_path(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"Invalid relative path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or path.as_posix() != value or any(part in {".", ".."} for part in path.parts):
        raise ValueError(f"Invalid relative path: {value!r}")
    return path


def confined(root: Path, value: str) -> Path:
    result = root
    for part in relative_path(value).parts:
        result = result / part
        if result.is_symlink():
            raise ValueError(f"Symlink in resource path: {result}")
    if root.is_symlink() or not result.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Resource path escapes its root: {value}")
    return result


def load_manifest(path: Path) -> tuple[dict, str]:
    raw = path.read_bytes()
    manifest = json.loads(raw)
    keys = {"schema_version", "kind", "version", "source_commit", "source_prefix", "source_url", "snapshot", "files"}
    if set(manifest) != keys or manifest["schema_version"] != 1 or manifest["kind"] != "tigit-teaching-resources":
        raise ValueError("Unsupported TIGIT resource manifest")
    if not re.fullmatch(r"[0-9a-f]{40}", manifest["source_commit"]):
        raise ValueError("The resource source must be an immutable Git commit")
    relative_path(manifest["source_prefix"].rstrip("/"))
    expected_url = f"https://raw.githubusercontent.com/geourv/tigit/{manifest['source_commit']}/{manifest['source_prefix']}"
    if manifest["source_url"] != expected_url or not expected_url.endswith("/"):
        raise ValueError("Unexpected resource source URL")
    snapshot = relative_path(manifest["snapshot"])
    if not snapshot.is_relative_to(RESOURCE_ROOT) or len(snapshot.parts) != 5:
        raise ValueError("Resource snapshots must use one named directory under the TIGIT resource root")
    rows = manifest["files"]
    if not isinstance(rows, list) or not 1 <= len(rows) <= 64:
        raise ValueError("Invalid resource inventory")
    seen = set()
    for row in rows:
        if set(row) != {"path", "sha256", "bytes"}:
            raise ValueError("Invalid resource declaration")
        item = relative_path(row["path"])
        data_input = item.parts[:2] in {("data", "raw"), ("data", "processed")}
        audit_figure = item.parts[:2] == ("outputs", "figures") and item.suffix == ".pdf"
        if len(item.parts) != 3 or not (data_input or audit_figure):
            raise ValueError("Only declared teaching data and historical audit PDFs are supported")
        if row["path"] in seen or not re.fullmatch(r"[0-9a-f]{64}", row["sha256"]):
            raise ValueError("Duplicate resource or invalid SHA-256")
        if type(row["bytes"]) is not int or not 0 < row["bytes"] <= MAX_FILE_BYTES:
            raise ValueError("Invalid resource size")
        seen.add(row["path"])
    if sum(row["bytes"] for row in rows) > MAX_TOTAL_BYTES:
        raise ValueError("Resource snapshot is too large")
    return manifest, sha256(raw)


def check_bytes(data: bytes, row: dict) -> None:
    if len(data) != row["bytes"] or sha256(data) != row["sha256"]:
        raise ValueError(f"Resource differs from its manifest: {row['path']}")


def check_snapshot(root: Path, manifest: dict, manifest_sha: str) -> dict:
    metadata = json.loads(confined(root, "resources.json").read_bytes())
    if metadata["manifest_sha256"] != manifest_sha or metadata["source_commit"] != manifest["source_commit"]:
        raise ValueError("Snapshot belongs to a different resource manifest")
    if metadata["files"] != manifest["files"]:
        raise ValueError("Snapshot inventory differs from its manifest")
    expected = {"resources.json"} | {row["path"] for row in manifest["files"]}
    observed = set()
    for path in root.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Symlink in resource snapshot: {path}")
        if path.is_file():
            observed.add(path.relative_to(root).as_posix())
    if observed != expected:
        raise ValueError("Snapshot has missing or undeclared files")
    for row in manifest["files"]:
        check_bytes(confined(root, row["path"]).read_bytes(), row)
    return {"ok": True, "files": len(manifest["files"]), "bytes": sum(row["bytes"] for row in manifest["files"]), "manifest_sha256": manifest_sha}


def prepare_snapshot(root: Path, manifest: dict, manifest_sha: str, *, source: Path | None = None, fetch: bool = False) -> dict:
    if (source is None) == (not fetch):
        raise ValueError("Select exactly one explicit input mode: local files or fetch")
    if root.exists() or root.is_symlink():
        raise FileExistsError(f"Snapshot already exists; use check-resources: {root}")
    payloads = []
    for row in manifest["files"]:
        if source is not None:
            data = confined(source, row["path"]).read_bytes()
        else:
            request = Request(manifest["source_url"] + row["path"], headers={"User-Agent": "TIGIT resource preparation"})
            with urlopen(request, timeout=120) as response:
                data = response.read(row["bytes"] + 1)
        check_bytes(data, row)
        payloads.append((row, data))
    # Validate every input before creating output. An interrupted write is retained
    # without a success marker; another invocation must not overwrite that attempt.
    root.mkdir(parents=True, exist_ok=False)
    for row, data in payloads:
        destination = confined(root, row["path"])
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("xb") as handle:
            handle.write(data)
    metadata = {"kind": "tigit-resource-snapshot", "manifest_sha256": manifest_sha, "source_commit": manifest["source_commit"], "input_mode": "local" if source else "fetch", "files": manifest["files"]}
    with (root / "resources.json").open("x", encoding="utf-8") as handle:
        json.dump(metadata, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return check_snapshot(root, manifest, manifest_sha)


def prepare_qgis_inputs(workspace: Path, source_root: Path, root: Path, manifest: dict, manifest_sha: str) -> dict:
    """Snapshot this course's authored request/model and its exact declared inputs.

    The resulting request is passed to native practice-run. This operation neither
    executes the model nor interprets QGIS products, projects or dependency closure.
    """
    root = confined(workspace, root.relative_to(workspace).as_posix())
    source_root = confined(workspace, source_root.relative_to(workspace).as_posix())
    if root.exists():
        raise FileExistsError(f"QGIS input packet already exists: {root}")
    snapshot = confined(workspace, manifest["snapshot"])
    check_snapshot(snapshot, manifest, manifest_sha)
    request_raw = confined(source_root, "activity-qgis.json").read_bytes()
    request = json.loads(request_raw)
    if request.get("schema_version") != 2 or request.get("kind") != "qgis-practice-request-v2":
        raise ValueError("The TIGIT model requires the native qgis-practice-request-v2 contract")
    script = relative_path(request["script"]).as_posix()
    if not script.startswith("activities/") or not script.endswith(".py"):
        raise ValueError("The authored QGIS model must be a Python source under activities/")
    script_raw = confined(source_root, script).read_bytes()
    payloads = {"activity-qgis.json": request_raw, script: script_raw}
    available = {row["path"]: row for row in manifest["files"]}
    inputs = request.get("inputs", [])
    if not inputs:
        raise ValueError("The QGIS request declares no teaching inputs")
    ids = set()
    for item in inputs:
        path = relative_path(item["path"]).as_posix()
        if item["id"] in ids or path in payloads:
            raise ValueError("Duplicate QGIS input ID or path")
        ids.add(item["id"])
        row = available.get(path)
        if row is None or item["sha256"] != row["sha256"]:
            raise ValueError(f"QGIS input is not bound to the resource manifest: {path}")
        data = confined(snapshot, path).read_bytes()
        check_bytes(data, row)
        payloads[path] = data
    origin = {
        "kind": "tigit-qgis-input-origin",
        "resource_manifest_sha256": manifest_sha,
        "resource_snapshot": manifest["snapshot"],
        "sources": {
            (source_root / path).relative_to(workspace).as_posix(): sha256(data)
            for path, data in (("activity-qgis.json", request_raw), (script, script_raw))
        },
        "files": {path: sha256(data) for path, data in payloads.items()},
    }
    root.mkdir(parents=True, exist_ok=False)
    for path, data in payloads.items():
        destination = confined(root, path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("xb") as handle:
            handle.write(data)
        if sha256(destination.read_bytes()) != origin["files"][path]:
            raise ValueError(f"QGIS input copy failed its hash check: {path}")
    with (root / "origin.json").open("x", encoding="utf-8") as handle:
        json.dump(origin, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return {
        "ok": True,
        "request": (root / "activity-qgis.json").relative_to(workspace).as_posix(),
        "inputs": len(inputs),
        "source_hashes": origin["sources"],
        "origin_sha256": sha256((root / "origin.json").read_bytes()),
    }


def prepare_workbook_inputs(workspace: Path, source_root: Path, root: Path, manifest: dict, manifest_sha: str) -> dict:
    """Copy pinned raw tables to a new mutable run; never copy legacy workbooks."""
    root = confined(workspace, root.relative_to(workspace).as_posix())
    source_root = confined(workspace, source_root.relative_to(workspace).as_posix())
    if root.exists():
        raise FileExistsError(f"Workbook run already exists: {root}")
    snapshot = confined(workspace, manifest["snapshot"])
    check_snapshot(snapshot, manifest, manifest_sha)
    inputs = [row for row in manifest["files"] if row["path"].startswith("data/raw/")]
    payloads = [(row, confined(snapshot, row["path"]).read_bytes()) for row in inputs]
    for row, data in payloads:
        check_bytes(data, row)
    sources = [source_root / "preparar.py", source_root / "scripts/requirements.txt", *sorted((source_root / "scripts").glob("*.py"))]
    metadata = {
        "kind": "tigit-workbook-inputs",
        "resource_manifest_sha256": manifest_sha,
        "resource_snapshot": manifest["snapshot"],
        "files": {row["path"]: row["sha256"] for row in inputs},
        "sources": {path.relative_to(workspace).as_posix(): sha256(confined(source_root, path.relative_to(source_root).as_posix()).read_bytes()) for path in sources},
    }
    root.mkdir(parents=True, exist_ok=False)
    for row, data in payloads:
        destination = confined(root, row["path"])
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("xb") as handle:
            handle.write(data)
    (root / "data/processed").mkdir(parents=True)
    with (root / "run-inputs.json").open("x", encoding="utf-8") as handle:
        json.dump(metadata, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return {"ok": True, "inputs": len(inputs), "source_count": len(sources), "origin_sha256": sha256((root / "run-inputs.json").read_bytes())}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["resources", "check-resources", "qgis-inputs", "workbook-inputs"])
    origin = parser.add_mutually_exclusive_group()
    origin.add_argument("--from-local", help="Workspace-relative directory containing the declared data tree")
    origin.add_argument("--fetch", action="store_true", help="Explicitly fetch the immutable, hash-pinned resource bytes")
    parser.add_argument("--output", help="Named sandbox path; required for qgis-inputs and workbook-inputs")
    args = parser.parse_args()
    if Path.cwd().resolve() != WORKSPACE or Path(os.environ.get("MCP_CONSUMER_WORKSPACE", WORKSPACE)).resolve() != WORKSPACE:
        parser.error("Run from the authoritative TIGIT checkout root")
    manifest, digest = load_manifest(SOURCE_ROOT / "recursos.yml")
    if args.operation in {"qgis-inputs", "workbook-inputs"} and (not args.output or args.fetch or args.from_local):
        parser.error(args.operation + " requires --output and uses the already verified resource snapshot")
    output = args.output or manifest["snapshot"]
    relative = relative_path(output)
    output_root = {"qgis-inputs": QGIS_INPUT_ROOT, "workbook-inputs": WORKBOOK_ROOT}.get(args.operation, RESOURCE_ROOT)
    if not relative.is_relative_to(output_root) or len(relative.parts) != 5:
        parser.error("Output must be one named directory under " + output_root)
    destination = confined(WORKSPACE, output)
    ignored = subprocess.run(["git", "check-ignore", "--quiet", "--no-index", output + "/resources.json"], cwd=WORKSPACE)
    if ignored.returncode != 0:
        parser.error("Generated resource snapshots must be ignored by Git")
    if args.operation == "qgis-inputs":
        result = prepare_qgis_inputs(WORKSPACE, SOURCE_ROOT, destination, manifest, digest)
    elif args.operation == "workbook-inputs":
        result = prepare_workbook_inputs(WORKSPACE, SOURCE_ROOT, destination, manifest, digest)
    elif args.operation == "check-resources":
        if args.fetch or args.from_local:
            parser.error("check-resources is read-only and accepts no input mode")
        result = check_snapshot(destination, manifest, digest)
    else:
        source = confined(WORKSPACE, args.from_local) if args.from_local else None
        result = prepare_snapshot(destination, manifest, digest, source=source, fetch=args.fetch)
    print(json.dumps({**result, "snapshot": output, "operation": args.operation}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
