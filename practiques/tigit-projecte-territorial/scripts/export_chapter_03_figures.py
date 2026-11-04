#!/usr/bin/env python3
"""Export chapter 3 chart sheets to vector PDF and editable SVG."""

from __future__ import annotations

import shutil
import subprocess

from openpyxl import load_workbook


from practice_paths import libreoffice_command, project_root, require_new_output

PROJECT_ROOT = project_root()
SOURCE = PROJECT_ROOT / "data" / "processed" / "tigit-03-semiologia-visualitzacio-teaching.xlsx"
TMP_DIR = PROJECT_ROOT / "cache" / "chapter-03-exports"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "figures" / "chapter-03"

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
    for stem in EXPORTS.values():
        require_new_output(OUTPUT_DIR / f"{stem}.pdf")
        require_new_output(OUTPUT_DIR / f"{stem}.svg")
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for sheet_name, stem in EXPORTS.items():
        workbook = load_workbook(SOURCE)
        for sheet in workbook.worksheets:
            sheet.sheet_state = "visible" if sheet.title == sheet_name else "hidden"
        temporary_book = TMP_DIR / f"{stem}.xlsx"
        temporary_pdf = TMP_DIR / f"{stem}.pdf"
        if temporary_pdf.exists():
            temporary_pdf.unlink()
        workbook.save(temporary_book)
        subprocess.run([*libreoffice_command(), "--convert-to", "pdf", "--outdir", str(TMP_DIR), str(temporary_book)], check=True, timeout=180)
        output_pdf = OUTPUT_DIR / f"{stem}.pdf"
        shutil.copyfile(temporary_pdf, output_pdf)

        if stem in {"age-structure-tarragones-2021", "non-principal-housing-tarragones-2021", "population-vila-seca-2000-2022", "population-pyramid-vila-seca-2021"}:
            output_svg = OUTPUT_DIR / f"{stem}.svg"
            subprocess.run([
                "inkscape", str(output_pdf), "--pdf-poppler", "--export-filename", str(output_svg)
            ], check=True, timeout=180)
    print(OUTPUT_DIR)


if __name__ == "__main__":
    main()
