"""Paths for the TIGIT teaching scripts; every mutable run stays in sandbox."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys

SOURCE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE_ROOT))
from preparar import WORKSPACE, WORKBOOK_ROOT, confined, relative_path, sha256


def project_root(*, acquisition: bool = False) -> Path:
    value = os.environ.get("TIGIT_PRACTICE_RUN", "")
    if not value:
        raise ValueError("Set TIGIT_PRACTICE_RUN to a run prepared with preparar.py workbook-inputs")
    path = relative_path(value)
    if not path.is_relative_to(WORKBOOK_ROOT) or len(path.parts) != 5:
        raise ValueError("Workbook runs must be one named directory under " + WORKBOOK_ROOT)
    if Path(os.environ.get("MCP_CONSUMER_WORKSPACE", WORKSPACE)).resolve() != WORKSPACE:
        raise ValueError("The selected consumer is not the authoritative TIGIT checkout")
    root = confined(WORKSPACE, value)
    metadata = json.loads(confined(root, "run-inputs.json").read_bytes())
    if metadata.get("kind") != "tigit-workbook-inputs":
        raise ValueError("Not a prepared TIGIT workbook run")
    if acquisition:
        require_network()
    else:
        for source, digest in metadata["files"].items():
            if sha256(confined(root, source).read_bytes()) != digest:
                raise ValueError("Pinned workbook input changed: " + source)
    for source, digest in metadata["sources"].items():
        if sha256(confined(WORKSPACE, source).read_bytes()) != digest:
            raise ValueError("Authored sources changed; prepare a new workbook run: " + source)
    for item in root.rglob("*"):
        if item.is_symlink():
            raise ValueError("Symlink in workbook run: " + str(item))
    ignored = subprocess.run(["git", "check-ignore", "--quiet", "--no-index", value + "/run-inputs.json"], cwd=WORKSPACE)
    if ignored.returncode != 0:
        raise ValueError("Workbook runs must be ignored by Git")
    return root


def run_path(path: Path) -> Path:
    """Confine an explicit script argument as well as its default output."""
    root = project_root()
    absolute = path if path.is_absolute() else Path.cwd() / path
    return confined(root, absolute.relative_to(root).as_posix())


def require_new_output(path: Path) -> None:
    path = run_path(path)
    if path.exists():
        raise FileExistsError("Output already exists; prepare a new run: " + str(path))


def require_network() -> None:
    if os.environ.get("TIGIT_FETCH_TEACHING_DATA") != "1":
        raise ValueError("Live acquisition is opt-in: TIGIT_FETCH_TEACHING_DATA=1; use pinned resources for reproduction")


def libreoffice_command() -> list[str]:
    profile = confined(project_root(), "cache/libreoffice-profile")
    profile.mkdir(parents=True, exist_ok=True)
    return ["libreoffice", "-env:UserInstallation=" + profile.as_uri(), "--headless", "--nologo", "--nofirststartwizard"]
