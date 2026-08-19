#!/usr/bin/env python3
"""Export chapter 3 chart sheets to vector PDF and editable SVG."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from openpyxl import load_workbook


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PROJECT_ROOT.parents[1]
SOURCE = PROJECT_ROOT / "data" / "processed" / "tigit-03-semiologia-visualitzacio-teaching.xlsx"
TMP_DIR = REPOSITORY_ROOT / "tmp" / "chapter-03-exports"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "figures"
DIST_DIR = PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures"

EXPORTS = {
    "chart_01_age_structure": "age-structure-tarragones-2021",
    "chart_02_nonprincipal": "non-principal-housing-tarragones-2021",
    "chart_03_scatter": "ageing-vs-non-principal-housing-tarragones-2021",
    "chart_04_housing_donut": "housing-composition-tarragones-2021",
    "chart_05_population_time": "population-vila-seca-2000-2022",
    "chart_06_population_pyramid": "population-pyramid-vila-seca-2021",
    "chart_07_housing_histogram": "housing-non-main-histogram-tarragones-2021",
}


def main() -> None:
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    for sheet_name, stem in EXPORTS.items():
        workbook = load_workbook(SOURCE)
        for sheet in workbook.worksheets:
            sheet.sheet_state = "visible" if sheet.title == sheet_name else "hidden"
        temporary_book = TMP_DIR / f"{stem}.xlsx"
        temporary_pdf = TMP_DIR / f"{stem}.pdf"
        if temporary_pdf.exists():
            temporary_pdf.unlink()
        workbook.save(temporary_book)
        subprocess.run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(TMP_DIR), str(temporary_book)], check=True)
        output_pdf = OUTPUT_DIR / f"{stem}.pdf"
        shutil.copyfile(temporary_pdf, output_pdf)
        shutil.copyfile(output_pdf, DIST_DIR / output_pdf.name)

        if stem in {"age-structure-tarragones-2021", "non-principal-housing-tarragones-2021", "population-vila-seca-2000-2022", "population-pyramid-vila-seca-2021"}:
            output_svg = OUTPUT_DIR / f"{stem}.svg"
            subprocess.run([
                "inkscape", str(output_pdf), "--pdf-poppler", "--export-filename", str(output_svg)
            ], check=True)
            shutil.copyfile(output_svg, DIST_DIR / output_svg.name)
    print(OUTPUT_DIR)


if __name__ == "__main__":
    main()
