#!/usr/bin/env python3
"""Download ICGC divisions and build a compact Tarragones GeoPackage."""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path
from urllib.request import Request, urlopen
from zipfile import ZipFile


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PROJECT_ROOT.parents[1]
CACHE_DIR = REPOSITORY_ROOT / "tmp"
EXTRACT_DIR = CACHE_DIR / "spatial-source"
ZIP_PATH = CACHE_DIR / "divisions-administratives-v2r2-20260120.zip"
SOURCE_GPKG = EXTRACT_DIR / "divisions-administratives-v2r2-20260120.gpkg"
OUTPUT_GPKG = PROJECT_ROOT / "data" / "processed" / "tarragones-boundaries-icgc-20260120.gpkg"

URL = "https://datacloud.icgc.cat/datacloud/divisions-administratives/gpkg/divisions-administratives-v2r2-20260120.zip"
SHA256 = "563fb7d81e143509d88569a9e8fe86d7c44ae9ce9e96c75b888379a7f0554162"


def download() -> None:
    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)
    if not ZIP_PATH.exists():
        request = Request(URL, headers={"User-Agent": "TIGIT teaching material preparation"})
        with urlopen(request, timeout=180) as response:
            ZIP_PATH.write_bytes(response.read())
    digest = hashlib.sha256(ZIP_PATH.read_bytes()).hexdigest()
    if digest != SHA256:
        raise ValueError(f"Unexpected ICGC checksum: {digest}")
    if not SOURCE_GPKG.exists():
        with ZipFile(ZIP_PATH) as archive:
            archive.extractall(EXTRACT_DIR)


def ogr2ogr(*arguments: str) -> None:
    subprocess.run(["ogr2ogr", *arguments], check=True)


def build() -> None:
    OUTPUT_GPKG.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT_GPKG.exists():
        OUTPUT_GPKG.unlink()
    ogr2ogr("-f", "GPKG", str(OUTPUT_GPKG), str(SOURCE_GPKG), "_64_municipis-250000", "-where", "CODICOMAR = '36'", "-nln", "municipalities_250k")
    layers = (
        ("_54_comarques-250000", "CODICOMAR = '36'", "comarca_250k"),
        ("_36_provincies-1000000", "CODIPROV = '43'", "province_1000k"),
        ("_62_municipis-50000", "CODIMUNI = '431711'", "vila_seca_50k"),
        ("_10_caps-municipi", "CODICOMAR = '36'", "municipality_seats"),
    )
    for source_layer, where, target_layer in layers:
        ogr2ogr("-update", "-append", str(OUTPUT_GPKG), str(SOURCE_GPKG), source_layer, "-where", where, "-nln", target_layer)


if __name__ == "__main__":
    download()
    build()
    print(OUTPUT_GPKG)
