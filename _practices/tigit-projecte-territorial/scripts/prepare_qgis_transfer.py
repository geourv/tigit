#!/usr/bin/env python3
"""Recalculate the workbook in Calc and export its QGIS transfer table."""

from __future__ import annotations

import csv
import shutil
import subprocess
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PROJECT_ROOT.parents[1]
SOURCE = PROJECT_ROOT / "data" / "processed" / "tigit-07-teoria-color-teaching.xlsx"
OUTPUT = PROJECT_ROOT / "data" / "processed" / "tigit-05-integracio-sig-teaching.xlsx"
TMP_DIR = REPOSITORY_ROOT / "tmp" / "qgis-transfer"
RECALCULATED = TMP_DIR / SOURCE.name
CSV_OUTPUT = PROJECT_ROOT / "data" / "processed" / "municipal-indicators-tarragones-2021.csv"
CSVT_OUTPUT = CSV_OUTPUT.with_suffix(".csvt")

HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
HEADER_FONT = Font(color="FFFFFF", bold=True)


def main() -> None:
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    if RECALCULATED.exists():
        RECALCULATED.unlink()
    subprocess.run([
        "libreoffice", "--headless", "--convert-to", "xlsx", "--outdir", str(TMP_DIR), str(SOURCE)
    ], check=True)

    calculated = load_workbook(RECALCULATED, data_only=True)
    municipal = calculated["municipal"]
    demography = calculated["indicators_demography"]
    housing = calculated["indicators_housing"]
    headers = [
        "mun_code", "municipality", "county_code", "year", "population_total",
        "population_65_plus", "population_65_plus_pct", "housing_total",
        "housing_non_main", "housing_non_main_pct", "indicator_status",
    ]
    rows = []
    for row in range(2, 24):
        values = [
            municipal.cell(row, 1).value, municipal.cell(row, 2).value, municipal.cell(row, 3).value,
            2021, municipal.cell(row, 5).value, municipal.cell(row, 8).value,
            demography.cell(row, 8).value, municipal.cell(row, 9).value,
            municipal.cell(row, 11).value, housing.cell(row, 7).value,
        ]
        status = "ok" if all(value is not None for value in values[4:]) else "missing_component"
        rows.append(values + [status])
    if len(rows) != 22 or len({row[0] for row in rows}) != 22:
        raise ValueError("QGIS transfer table must contain 22 unique municipalities")
    if not any(row[0] == "431711" and row[1] == "Vila-seca" for row in rows):
        raise ValueError("Vila-seca control row is missing")

    shutil.copyfile(SOURCE, OUTPUT)
    workbook = load_workbook(OUTPUT)
    project = workbook["project"]
    project_rows = {project.cell(row, 1).value: row for row in range(2, project.max_row + 1)}
    project.cell(project_rows["chapter_snapshot"], 2, "05")
    if "map_export" in workbook.sheetnames:
        del workbook["map_export"]
    map_export = workbook.create_sheet("map_export")
    map_export.append(headers)
    for source_row in range(2, 24):
        output_row = map_export.max_row + 1
        map_export.append([
            f"=municipal!A{source_row}",
            f"=municipal!B{source_row}",
            f"=municipal!C{source_row}",
            2021,
            f"=municipal!E{source_row}",
            f"=municipal!H{source_row}",
            f"=indicators_demography!H{source_row}",
            f"=municipal!I{source_row}",
            f"=municipal!K{source_row}",
            f"=indicators_housing!G{source_row}",
            f'=IF(COUNT(E{output_row}:J{output_row})=6,"ok","missing_component")',
        ])
    for cell in map_export[1]:
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(wrap_text=True)
    map_export.freeze_panes = "A2"
    map_export.auto_filter.ref = map_export.dimensions
    for column in range(1, map_export.max_column + 1):
        map_export.column_dimensions[get_column_letter(column)].width = 22
    workbook.calculation.fullCalcOnLoad = True
    workbook.calculation.forceFullCalc = True
    workbook.save(OUTPUT)

    with CSV_OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(rows)
    CSVT_OUTPUT.write_text(
        '"String","String","String","Integer","Integer","Integer","Real","Integer","Integer","Real","String"\n',
        encoding="ascii",
    )
    print(OUTPUT)
    print(CSV_OUTPUT)


if __name__ == "__main__":
    main()
