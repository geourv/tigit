#!/usr/bin/env python3
"""Build deterministic student and teaching ZIP packages."""

from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = "tigit-projecte-territorial"
FIXED_TIME = (2026, 8, 18, 0, 0, 0)

STUDENT_OUTPUT = REPOSITORY_ROOT / "assets" / "downloads" / "tigit-01-preparacio-dades-student.zip"
TEACHING_OUTPUT = PROJECT_ROOT / "dist" / "course-packages" / "tigit-practiques-teaching.zip"


def add_bytes(archive: ZipFile, archive_path: str, content: bytes) -> None:
    info = ZipInfo(archive_path, FIXED_TIME)
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, content)


def add_file(archive: ZipFile, source: Path, archive_path: str) -> None:
    add_bytes(archive, archive_path, source.read_bytes())


def add_directory(archive: ZipFile, archive_path: str) -> None:
    info = ZipInfo(archive_path.rstrip("/") + "/", FIXED_TIME)
    info.external_attr = 0o40755 << 16
    archive.writestr(info, b"")


def build_student_package() -> None:
    workbook = PROJECT_ROOT / "dist" / "student" / "chapter-01" / "tigit-01-preparacio-dades.xlsx"
    readme = PROJECT_ROOT / "scripts" / "student-package-README.md"
    raw_readme = PROJECT_ROOT / "data" / "raw" / "README.md"

    STUDENT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(STUDENT_OUTPUT, "w") as archive:
        add_file(archive, readme, f"{PACKAGE_ROOT}/README.md")
        add_file(archive, raw_readme, f"{PACKAGE_ROOT}/data/raw/README.md")
        add_file(archive, workbook, f"{PACKAGE_ROOT}/data/processed/tigit-01-preparacio-dades.xlsx")
        for directory in (
            "qgis",
            "outputs/figures",
            "outputs/maps",
            "outputs/infographics",
            "captures",
            "sandbox",
            "dist",
        ):
            add_directory(archive, f"{PACKAGE_ROOT}/{directory}")


def build_teaching_package() -> None:
    included_files = (
        (PROJECT_ROOT / "README.md", "README.md"),
        (PROJECT_ROOT / "Makefile", "Makefile"),
        (PROJECT_ROOT / "dist" / "course-packages" / "TEACHING-GUIDE.md", "TEACHING-GUIDE.md"),
        (PROJECT_ROOT / "data" / "raw" / "README.md", "data/raw/README.md"),
        (PROJECT_ROOT / "data" / "raw" / "mpiscatalunya.csv", "data/raw/mpiscatalunya.csv"),
        (PROJECT_ROOT / "data" / "raw" / "t30mun.csv", "data/raw/t30mun.csv"),
        (PROJECT_ROOT / "data" / "raw" / "t396mun.csv", "data/raw/t396mun.csv"),
        (PROJECT_ROOT / "data" / "raw" / "poblacio-edat-tarragones-2021.csv", "data/raw/poblacio-edat-tarragones-2021.csv"),
        (PROJECT_ROOT / "data" / "raw" / "poblacio-vila-seca-2000-2022.csv", "data/raw/poblacio-vila-seca-2000-2022.csv"),
        (PROJECT_ROOT / "data" / "raw" / "poblacio-vila-seca-edat-sexe-2021.csv", "data/raw/poblacio-vila-seca-edat-sexe-2021.csv"),
        (PROJECT_ROOT / "data" / "raw" / "centres-educatius-tarragones.csv", "data/raw/centres-educatius-tarragones.csv"),
        (PROJECT_ROOT / "data" / "raw" / "allotjaments-vila-seca-convencionals.csv", "data/raw/allotjaments-vila-seca-convencionals.csv"),
        (PROJECT_ROOT / "data" / "raw" / "icgc" / "README.md", "data/raw/icgc/README.md"),
        (PROJECT_ROOT / "data" / "processed" / "README.md", "data/processed/README.md"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-01" / "tigit-01-preparacio-dades.xlsx", "dist/teaching/chapter-01/tigit-01-preparacio-dades.xlsx"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-02" / "tigit-02-indicadors-territorials.xlsx", "dist/teaching/chapter-02/tigit-02-indicadors-territorials.xlsx"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "tigit-03-semiologia-visualitzacio.xlsx", "dist/teaching/chapter-03/tigit-03-semiologia-visualitzacio.xlsx"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-07" / "tigit-07-teoria-color.xlsx", "dist/teaching/chapter-07/tigit-07-teoria-color.xlsx"),
        (PROJECT_ROOT / "dist" / "snapshot-manifest.csv", "dist/snapshot-manifest.csv"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "age-structure-tarragones-2021.pdf", "dist/teaching/chapter-03/figures/age-structure-tarragones-2021.pdf"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "age-structure-tarragones-2021.svg", "dist/teaching/chapter-03/figures/age-structure-tarragones-2021.svg"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "non-principal-housing-tarragones-2021.pdf", "dist/teaching/chapter-03/figures/non-principal-housing-tarragones-2021.pdf"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "non-principal-housing-tarragones-2021.svg", "dist/teaching/chapter-03/figures/non-principal-housing-tarragones-2021.svg"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "ageing-vs-non-principal-housing-tarragones-2021.pdf", "dist/teaching/chapter-03/figures/ageing-vs-non-principal-housing-tarragones-2021.pdf"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "housing-composition-tarragones-2021.pdf", "dist/teaching/chapter-03/figures/housing-composition-tarragones-2021.pdf"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "population-vila-seca-2000-2022.pdf", "dist/teaching/chapter-03/figures/population-vila-seca-2000-2022.pdf"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "population-vila-seca-2000-2022.svg", "dist/teaching/chapter-03/figures/population-vila-seca-2000-2022.svg"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "population-pyramid-vila-seca-2021.pdf", "dist/teaching/chapter-03/figures/population-pyramid-vila-seca-2021.pdf"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "population-pyramid-vila-seca-2021.svg", "dist/teaching/chapter-03/figures/population-pyramid-vila-seca-2021.svg"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-03" / "figures" / "housing-non-main-histogram-tarragones-2021.pdf", "dist/teaching/chapter-03/figures/housing-non-main-histogram-tarragones-2021.pdf"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-07" / "figures" / "palette-proof-age-structure-tarragones-2021.pdf", "dist/teaching/chapter-07/figures/palette-proof-age-structure-tarragones-2021.pdf"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-07" / "figures" / "palette-proof-age-structure-tarragones-2021.svg", "dist/teaching/chapter-07/figures/palette-proof-age-structure-tarragones-2021.svg"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-07" / "figures" / "palette-proof-non-principal-housing-tarragones-2021.pdf", "dist/teaching/chapter-07/figures/palette-proof-non-principal-housing-tarragones-2021.pdf"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-07" / "figures" / "palette-proof-non-principal-housing-tarragones-2021.svg", "dist/teaching/chapter-07/figures/palette-proof-non-principal-housing-tarragones-2021.svg"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-07" / "figures" / "palette-proof-population-pyramid-vila-seca-2021.pdf", "dist/teaching/chapter-07/figures/palette-proof-population-pyramid-vila-seca-2021.pdf"),
        (PROJECT_ROOT / "dist" / "teaching" / "chapter-07" / "figures" / "palette-proof-population-pyramid-vila-seca-2021.svg", "dist/teaching/chapter-07/figures/palette-proof-population-pyramid-vila-seca-2021.svg"),
        (PROJECT_ROOT / "data" / "processed" / "tarragones-boundaries-icgc-20260120.gpkg", "data/processed/tarragones-boundaries-icgc-20260120.gpkg"),
        (PROJECT_ROOT / "data" / "processed" / "education-centres-tarragones-2025.csv", "data/processed/education-centres-tarragones-2025.csv"),
        (PROJECT_ROOT / "data" / "processed" / "education-centres-vila-seca-2025.csv", "data/processed/education-centres-vila-seca-2025.csv"),
        (PROJECT_ROOT / "data" / "processed" / "education-centres-tarragones-series.csv", "data/processed/education-centres-tarragones-series.csv"),
        (PROJECT_ROOT / "data" / "processed" / "tourism-accommodation-vila-seca-geocoding.csv", "data/processed/tourism-accommodation-vila-seca-geocoding.csv"),
        (PROJECT_ROOT / "data" / "processed" / "municipal-indicators-tarragones-2021.csv", "data/processed/municipal-indicators-tarragones-2021.csv"),
        (PROJECT_ROOT / "data" / "processed" / "municipal-indicators-tarragones-2021.csvt", "data/processed/municipal-indicators-tarragones-2021.csvt"),
        (PROJECT_ROOT / "qgis" / "README.md", "qgis/README.md"),
        (PROJECT_ROOT / "outputs" / "README.md", "outputs/README.md"),
        (PROJECT_ROOT / "captures" / "README.md", "captures/README.md"),
        (PROJECT_ROOT / "scripts" / "requirements.txt", "scripts/requirements.txt"),
        (PROJECT_ROOT / "scripts" / "create_chapter_01_workbook.py", "scripts/create_chapter_01_workbook.py"),
        (PROJECT_ROOT / "scripts" / "prepare_chapter_01.py", "scripts/prepare_chapter_01.py"),
        (PROJECT_ROOT / "scripts" / "check_chapter_01.py", "scripts/check_chapter_01.py"),
        (PROJECT_ROOT / "scripts" / "prepare_chapter_02.py", "scripts/prepare_chapter_02.py"),
        (PROJECT_ROOT / "scripts" / "check_chapter_02.py", "scripts/check_chapter_02.py"),
        (PROJECT_ROOT / "scripts" / "prepare_point_data.py", "scripts/prepare_point_data.py"),
        (PROJECT_ROOT / "scripts" / "prepare_spatial_data.py", "scripts/prepare_spatial_data.py"),
        (PROJECT_ROOT / "scripts" / "prepare_qgis_transfer.py", "scripts/prepare_qgis_transfer.py"),
        (PROJECT_ROOT / "scripts" / "publish_snapshots.py", "scripts/publish_snapshots.py"),
        (PROJECT_ROOT / "scripts" / "prepare_chapter_03.py", "scripts/prepare_chapter_03.py"),
        (PROJECT_ROOT / "scripts" / "export_chapter_03_figures.py", "scripts/export_chapter_03_figures.py"),
        (PROJECT_ROOT / "scripts" / "check_chapter_03.py", "scripts/check_chapter_03.py"),
        (PROJECT_ROOT / "scripts" / "create_calc_pivots.py", "scripts/create_calc_pivots.py"),
        (PROJECT_ROOT / "scripts" / "prepare_population_series.py", "scripts/prepare_population_series.py"),
        (PROJECT_ROOT / "scripts" / "prepare_population_pyramid.py", "scripts/prepare_population_pyramid.py"),
        (PROJECT_ROOT / "scripts" / "prepare_chapter_07.py", "scripts/prepare_chapter_07.py"),
        (PROJECT_ROOT / "scripts" / "export_chapter_07_figures.py", "scripts/export_chapter_07_figures.py"),
        (PROJECT_ROOT / "scripts" / "check_chapter_07.py", "scripts/check_chapter_07.py"),
        (PROJECT_ROOT / "scripts" / "build_packages.py", "scripts/build_packages.py"),
    )

    TEACHING_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(TEACHING_OUTPUT, "w") as archive:
        for source, relative_path in included_files:
            add_file(archive, source, f"{PACKAGE_ROOT}/{relative_path}")
        for directory in ("outputs/figures", "outputs/maps", "outputs/infographics", "sandbox", "dist"):
            add_directory(archive, f"{PACKAGE_ROOT}/{directory}")


if __name__ == "__main__":
    build_student_package()
    build_teaching_package()
    print(STUDENT_OUTPUT)
    print(TEACHING_OUTPUT)
