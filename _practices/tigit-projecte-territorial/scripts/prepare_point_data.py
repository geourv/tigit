#!/usr/bin/env python3
"""Prepare official point-data subsets for the QGIS activities."""

from __future__ import annotations

import csv
import io
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

EDUCATION_BASE = "https://analisi.transparenciacatalunya.cat/resource/kvmv-ahh4.csv"
TOURISM_BASE = "https://analisi.transparenciacatalunya.cat/resource/t2h3-cgys.csv"


def fetch_csv(url: str, destination: Path):
    request = Request(url, headers={"User-Agent": "TIGIT teaching material preparation"})
    with urlopen(request, timeout=120) as response:
        content = response.read()
    destination.write_bytes(content)
    return list(csv.DictReader(io.StringIO(content.decode("utf-8-sig"))))


def write_csv(path: Path, headers, rows) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def prepare_education() -> None:
    query = urlencode({
        "$where": "nom_comarca='Tarragonès'",
        "$limit": 50000,
        "$order": "any,codi_municipi_6,codi_centre",
    })
    url = f"{EDUCATION_BASE}?{query}"
    series_records = fetch_csv(url, RAW_DIR / "centres-educatius-tarragones.csv")
    records = [record for record in series_records if record.get("any") == "2025"]
    if len(records) != 183:
        raise ValueError(f"Expected 183 education records for 2025, found {len(records)}")

    headers = [
        "year", "centre_code", "centre_name", "ownership", "address", "postal_code",
        "municipality_code", "municipality", "county", "utm_x", "utm_y",
        "longitude", "latitude", "source_url",
    ]
    prepared = []
    for record in records:
        prepared.append({
            "year": record.get("any"),
            "centre_code": record.get("codi_centre"),
            "centre_name": record.get("denominaci_completa"),
            "ownership": record.get("nom_titularitat") or record.get("nom_naturalesa"),
            "address": record.get("adre_a"),
            "postal_code": record.get("codi_postal"),
            "municipality_code": record.get("codi_municipi_6"),
            "municipality": record.get("nom_municipi"),
            "county": record.get("nom_comarca"),
            "utm_x": record.get("coordenades_utm_x"),
            "utm_y": record.get("coordenades_utm_y"),
            "longitude": record.get("coordenades_geo_x"),
            "latitude": record.get("coordenades_geo_y"),
            "source_url": url,
        })
    write_csv(PROCESSED_DIR / "education-centres-tarragones-2025.csv", headers, prepared)

    vila_seca = [row for row in prepared if row["municipality_code"] == "431711"]
    if len(vila_seca) != 17:
        raise ValueError(f"Expected 17 Vila-seca education records, found {len(vila_seca)}")
    write_csv(PROCESSED_DIR / "education-centres-vila-seca-2025.csv", headers, vila_seca)

    series_headers = ["course", "year", "centre_code", "centre_name", "nature", "municipality_code", "municipality", "county"]
    series = [{
        "course": record.get("curs"),
        "year": record.get("any"),
        "centre_code": record.get("codi_centre"),
        "centre_name": record.get("denominaci_completa"),
        "nature": record.get("nom_naturalesa"),
        "municipality_code": record.get("codi_municipi_6"),
        "municipality": record.get("nom_municipi"),
        "county": record.get("nom_comarca"),
    } for record in series_records]
    write_csv(PROCESSED_DIR / "education-centres-tarragones-series.csv", series_headers, series)


def prepare_tourism() -> None:
    where = (
        "municipi='Vila-seca' AND tipus_establiment NOT IN "
        "('Habitatges d''ús turístic','Llars compartides')"
    )
    query = urlencode({"$where": where, "$limit": 50000, "$order": "tipus_establiment,n_mero_inscripci"})
    url = f"{TOURISM_BASE}?{query}"
    records = fetch_csv(url, RAW_DIR / "allotjaments-vila-seca-convencionals.csv")
    if not records:
        raise ValueError("Tourism Register query returned no records")

    headers = [
        "registration_number", "establishment_type", "public_name", "address_input",
        "postal_code", "municipality_code", "municipality", "county_code", "county",
        "category", "registered_places", "geocode_status", "matched_address",
        "longitude", "latitude", "utm_x", "utm_y", "source_url",
    ]
    prepared = []
    for record in records:
        address_parts = [
            record.get("tipus_de_via"), record.get("nom_de_la_via"), record.get("numero"),
            record.get("codi_postal"), record.get("municipi"),
        ]
        prepared.append({
            "registration_number": record.get("n_mero_inscripci"),
            "establishment_type": record.get("tipus_establiment"),
            "public_name": record.get("r_tol"),
            "address_input": " ".join(str(value).strip() for value in address_parts if value),
            "postal_code": record.get("codi_postal"),
            "municipality_code": record.get("codi_municipi_idescat"),
            "municipality": record.get("municipi"),
            "county_code": record.get("codi_comarca_idescat"),
            "county": record.get("comarca"),
            "category": record.get("categoria"),
            "registered_places": record.get("total_places"),
            "geocode_status": "PENDING",
            "matched_address": "",
            "longitude": "",
            "latitude": "",
            "utm_x": "",
            "utm_y": "",
            "source_url": url,
        })
    write_csv(PROCESSED_DIR / "tourism-accommodation-vila-seca-geocoding.csv", headers, prepared)


if __name__ == "__main__":
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    prepare_education()
    prepare_tourism()
    print("Point-data subsets prepared")
