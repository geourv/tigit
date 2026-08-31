#!/usr/bin/env python3
"""Prepare 2021 age, sex, and birthplace data for Vila-seca and Salou."""

from __future__ import annotations

import csv
import json
from itertools import product
from pathlib import Path
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CACHE = PROJECT_ROOT / "sandbox" / "cache" / "poblacio-vila-seca-salou-edat-sexe-naixement-2021.json"
OUTPUT = PROJECT_ROOT / "data" / "raw" / "poblacio-vila-seca-salou-edat-sexe-naixement-2021.csv"
URL = "https://api.idescat.cat/taules/v2/censph/535/562/mun/data?lang=ca&YEAR=2021&MUN=431711,439057"
EXPECTED_TOTALS = {"431711": 22781, "439057": 28314}


def main() -> None:
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    request = Request(URL, headers={"User-Agent": "TIGIT teaching material preparation"})
    with urlopen(request, timeout=120) as response:
        CACHE.write_bytes(response.read())
    dataset = json.loads(CACHE.read_text(encoding="utf-8"))

    dimensions = dataset["id"]
    if dimensions != ["YEAR", "MUN", "AGE", "PBIRTH", "SEX", "CONCEPT"]:
        raise ValueError(f"Unexpected dimensions: {dimensions}")

    dimension_data = dataset["dimension"]
    categories = [dimension_data[dimension]["category"]["index"] for dimension in dimensions]
    rows = []
    for coordinates, value in zip(product(*categories), dataset["value"], strict=True):
        if value is None:
            raise ValueError(f"Missing value at {coordinates}")
        record = dict(zip(dimensions, coordinates, strict=True))
        rows.append({
            "year": int(record["YEAR"]),
            "municipality_code": record["MUN"],
            "municipality": dimension_data["MUN"]["category"]["label"][record["MUN"]],
            "age_code": record["AGE"],
            "age_label": dimension_data["AGE"]["category"]["label"][record["AGE"]],
            "age_order": categories[2].index(record["AGE"]),
            "birthplace_code": record["PBIRTH"],
            "birthplace_label": dimension_data["PBIRTH"]["category"]["label"][record["PBIRTH"]],
            "sex_code": record["SEX"],
            "sex_label": dimension_data["SEX"]["category"]["label"][record["SEX"]],
            "population": int(value),
            "status": "",
            "source": dataset["source"],
            "source_updated": dataset["updated"],
            "source_url": URL,
        })

    if len(rows) != 456:
        raise ValueError(f"Expected 456 observations, found {len(rows)}")

    lookup = {
        (row["municipality_code"], row["age_code"], row["sex_code"], row["birthplace_code"]): row["population"]
        for row in rows
    }
    for municipality_code in EXPECTED_TOTALS:
        for age_code in categories[2]:
            for sex_code in categories[4]:
                components = sum(
                    lookup[(municipality_code, age_code, sex_code, birthplace_code)]
                    for birthplace_code in ("CA09", "RES", "ESTR")
                )
                total = lookup[(municipality_code, age_code, sex_code, "TOTAL")]
                if components != total:
                    raise ValueError(
                        f"Birthplace components do not sum to total for {municipality_code}, {age_code}, {sex_code}"
                    )
        observed_total = lookup[(municipality_code, "TOTAL", "TOTAL", "TOTAL")]
        if observed_total != EXPECTED_TOTALS[municipality_code]:
            raise ValueError(f"Unexpected total for {municipality_code}: {observed_total}")

    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(OUTPUT)


if __name__ == "__main__":
    main()
