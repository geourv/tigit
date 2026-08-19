#!/usr/bin/env python3
"""Export selected chapter 7 color proofs to PDF and SVG."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from openpyxl import load_workbook


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PROJECT_ROOT.parents[1]
SOURCE = PROJECT_ROOT / "data" / "processed" / "tigit-07-teoria-color-teaching.xlsx"
TMP_DIR = REPOSITORY_ROOT / "tmp" / "chapter-07-exports"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "figures"
DIST_DIR = PROJECT_ROOT / "dist" / "teaching" / "chapter-07" / "figures"

EXPORTS = {
    "chart_01_age_structure": "palette-proof-age-structure-tarragones-2021",
    "chart_02_nonprincipal": "palette-proof-non-principal-housing-tarragones-2021",
    "chart_06_population_pyramid": "palette-proof-population-pyramid-vila-seca-2021",
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
        output_svg = OUTPUT_DIR / f"{stem}.svg"
        shutil.copyfile(temporary_pdf, output_pdf)
        subprocess.run(["inkscape", str(output_pdf), "--pdf-poppler", "--export-filename", str(output_svg)], check=True)
        shutil.copyfile(output_pdf, DIST_DIR / output_pdf.name)
        shutil.copyfile(output_svg, DIST_DIR / output_svg.name)
    print(DIST_DIR)


if __name__ == "__main__":
    main()
