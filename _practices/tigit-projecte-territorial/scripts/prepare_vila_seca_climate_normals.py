#!/usr/bin/env python3
"""Prepare Vila-seca monthly climate normals for 1991-2020."""

from __future__ import annotations

import csv
import io
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CACHE = PROJECT_ROOT / "sandbox" / "cache" / "clima-vila-seca-mitjanes-1991-2020.csv"
OUTPUT = PROJECT_ROOT / "data" / "raw" / "clima-vila-seca-mitjanes-1991-2020.csv"
ENDPOINT = "https://analisi.transparenciacatalunya.cat/resource/9ehv-pmf5.csv"
ABOUT_URL = "https://analisi.transparenciacatalunya.cat/Medi-Ambient/Atles-Clim-tic-de-mitjanes-per-municipi/9ehv-pmf5/about_data"
LICENSE_URL = "https://gencat.cat/ca/generalitat/dades-indicadors/dades-obertes/llicencies"
MONTHS = (
    ("gener", "Gener"),
    ("febrer", "Febrer"),
    ("marc", "Març"),
    ("abril", "Abril"),
    ("maig", "Maig"),
    ("juny", "Juny"),
    ("juliol", "Juliol"),
    ("agost", "Agost"),
    ("setembre", "Setembre"),
    ("octubre", "Octubre"),
    ("novembre", "Novembre"),
    ("desembre", "Desembre"),
)


def main() -> None:
    fields = [
        "codi_municipi",
        "cap_municipi",
        "nom_municipi",
        "variable",
        "unitat",
        *(key for key, _ in MONTHS),
        "anual",
    ]
    query = urlencode({
        "$select": ",".join(fields),
        "$where": "codi_municipi='431711'",
    })
    url = f"{ENDPOINT}?{query}"
    request = Request(url, headers={"User-Agent": "TIGIT teaching material preparation"})
    with urlopen(request, timeout=120) as response:
        content = response.read()

    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_bytes(content)
    source_rows = list(csv.DictReader(io.StringIO(content.decode("utf-8-sig"))))
    by_variable = {row["variable"]: row for row in source_rows}
    required = {"Temperatura mitjana", "Precipitació mitjana"}
    if not required.issubset(by_variable):
        raise ValueError(f"Missing climate variables: {sorted(required - set(by_variable))}")

    temperature = by_variable["Temperatura mitjana"]
    precipitation = by_variable["Precipitació mitjana"]
    rows = []
    for month_number, (month_key, month_label) in enumerate(MONTHS, start=1):
        rows.append({
            "municipality_code": "431711",
            "municipality": "Vila-seca",
            "reference_point": "Cap de municipi de Vila-seca",
            "period": "1991-2020",
            "month_number": month_number,
            "month": month_label,
            "mean_temperature_c": float(temperature[month_key]),
            "mean_precipitation_mm": float(precipitation[month_key]),
            "annual_mean_temperature_c": float(temperature["anual"]),
            "annual_precipitation_mm": float(precipitation["anual"]),
            "source": "Servei Meteorològic de Catalunya, Atles Climàtic de mitjanes per municipi",
            "source_updated": "2026-06-15",
            "source_url": ABOUT_URL,
            "license_url": LICENSE_URL,
        })

    if abs(sum(row["mean_precipitation_mm"] for row in rows) - rows[0]["annual_precipitation_mm"]) > 0.2:
        raise ValueError("Monthly precipitation does not match the published annual value")
    if abs(sum(row["mean_temperature_c"] for row in rows) / 12 - rows[0]["annual_mean_temperature_c"]) > 0.1:
        raise ValueError("Monthly temperatures do not match the published annual mean")

    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(OUTPUT)


if __name__ == "__main__":
    main()
