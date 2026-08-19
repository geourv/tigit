#!/usr/bin/env python3
"""Prepare a consistent 2000-2022 population series for Vila-seca."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = PROJECT_ROOT / "sandbox" / "cache"
OUTPUT = PROJECT_ROOT / "data" / "raw" / "poblacio-vila-seca-2000-2022.csv"

QUERIES = (
    (
        "1063",
        "https://api.idescat.cat/taules/v2/pmh/1180/1063/mun/data?lang=ca&MUN=431711&SEX=TOTAL&AGE=TOTAL",
    ),
    (
        "8078",
        "https://api.idescat.cat/taules/v2/pmh/1180/8078/mun/data?lang=ca&MUN=431711&SEX=TOTAL&AGE=TOTAL",
    ),
)


def fetch(table_id: str, url: str):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache = CACHE_DIR / f"pmh-1180-{table_id}-vila-seca.json"
    request = Request(url, headers={"User-Agent": "TIGIT teaching material preparation"})
    with urlopen(request, timeout=120) as response:
        cache.write_bytes(response.read())
    return json.loads(cache.read_text(encoding="utf-8"))


def main() -> None:
    rows = []
    for table_id, url in QUERIES:
        dataset = fetch(table_id, url)
        years = dataset["dimension"]["YEAR"]["category"]["index"]
        for year, value in zip(years, dataset["value"]):
            rows.append({
                "year": int(year),
                "municipality_code": "431711",
                "municipality": "Vila-seca",
                "population": value,
                "table_id": table_id,
                "source": dataset["source"],
                "source_url": url,
            })
    rows.sort(key=lambda row: row["year"])
    if [row["year"] for row in rows] != list(range(2000, 2023)):
        raise ValueError("Population series is not continuous from 2000 to 2022")
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(OUTPUT)


if __name__ == "__main__":
    main()
