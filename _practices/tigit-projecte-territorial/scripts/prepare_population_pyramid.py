#!/usr/bin/env python3
"""Prepare Vila-seca population by single age and sex for 2021."""

from __future__ import annotations

import csv
import json
from itertools import product
from pathlib import Path
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CACHE = PROJECT_ROOT / "sandbox" / "cache" / "poblacio-vila-seca-edat-sexe-2021.json"
OUTPUT = PROJECT_ROOT / "data" / "raw" / "poblacio-vila-seca-edat-sexe-2021.csv"
URL = "https://api.idescat.cat/taules/v2/censph/10/5975/mun/data?lang=ca&YEAR=2021&MUN=431711&SEX=M,F"


def main() -> None:
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    request = Request(URL, headers={"User-Agent": "TIGIT teaching material preparation"})
    with urlopen(request, timeout=120) as response:
        CACHE.write_bytes(response.read())
    dataset = json.loads(CACHE.read_text(encoding="utf-8"))
    dimensions = dataset["id"]
    categories = [dataset["dimension"][dimension]["category"]["index"] for dimension in dimensions]
    labels = dataset["dimension"]["AGE"]["category"]["label"]
    rows = []
    for coordinates, value in zip(product(*categories), dataset["value"]):
        record = dict(zip(dimensions, coordinates))
        age_code = record["AGE"]
        if age_code == "TOTAL":
            continue
        age_years = 100 if age_code == "Y_GE100" else int(age_code[1:])
        rows.append({
            "year": int(record["YEAR"]),
            "municipality_code": record["MUN"],
            "municipality": "Vila-seca",
            "age_code": age_code,
            "age_label": labels[age_code],
            "age_years": age_years,
            "sex": record["SEX"],
            "population": value,
            "source_url": URL,
        })
    if len(rows) != 202:
        raise ValueError(f"Expected 202 age-sex observations, found {len(rows)}")
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(OUTPUT)


if __name__ == "__main__":
    main()
