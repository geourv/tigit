PYTHON ?= python3
VENV ?= .venv
VENV_PYTHON := $(VENV)/bin/python
VENV_PIP := $(VENV)/bin/pip
VENV_STAMP := $(VENV)/.ready

STARTER := data/processed/tigit-01-preparacio-dades.xlsx
TEACHING := data/processed/tigit-01-preparacio-dades-teaching.xlsx
TEACHING_02 := data/processed/tigit-02-indicadors-territorials-teaching.xlsx
TEACHING_03 := data/processed/tigit-03-semiologia-visualitzacio-teaching.xlsx
TEACHING_07 := data/processed/tigit-07-teoria-color-teaching.xlsx
POPULATION_SERIES := data/raw/poblacio-vila-seca-2000-2022.csv
POPULATION_PYRAMID := data/raw/poblacio-vila-seca-edat-sexe-2021.csv
STUDENT_ZIP := ../../assets/downloads/tigit-01-preparacio-dades-student.zip
TEACHING_ZIP := dist/course-packages/tigit-practiques-teaching.zip

.PHONY: all chapter-01-starter chapter-01 chapter-02 chapter-03 chapter-03-exports chapter-07 chapter-07-exports snapshots point-data spatial-data qgis-transfer packages check libreoffice-check

all: chapter-02 packages check

$(VENV_STAMP): scripts/requirements.txt
	$(PYTHON) -m venv "$(VENV)"
	$(VENV_PIP) install -r scripts/requirements.txt
	touch "$(VENV_STAMP)"

chapter-01-starter: $(STARTER)

$(STARTER): scripts/create_chapter_01_workbook.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/create_chapter_01_workbook.py --force

chapter-01: $(TEACHING)

$(TEACHING): $(STARTER) scripts/prepare_chapter_01.py scripts/create_calc_pivots.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/prepare_chapter_01.py
	$(PYTHON) scripts/create_calc_pivots.py "$(TEACHING)" --county

chapter-02: $(TEACHING_02)

$(TEACHING_02): $(TEACHING) scripts/prepare_chapter_02.py scripts/create_calc_pivots.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/prepare_chapter_02.py
	$(PYTHON) scripts/create_calc_pivots.py "$(TEACHING_02)" --county

chapter-03: $(TEACHING_03)

$(POPULATION_SERIES): scripts/prepare_population_series.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/prepare_population_series.py

$(POPULATION_PYRAMID): scripts/prepare_population_pyramid.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/prepare_population_pyramid.py

$(TEACHING_03): $(TEACHING_02) $(POPULATION_SERIES) $(POPULATION_PYRAMID) scripts/prepare_chapter_03.py scripts/create_calc_pivots.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/prepare_chapter_03.py
	$(PYTHON) scripts/create_calc_pivots.py "$(TEACHING_03)" --county --population

chapter-03-exports: $(TEACHING_03) scripts/export_chapter_03_figures.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/export_chapter_03_figures.py

chapter-07: $(TEACHING_07)

$(TEACHING_07): $(TEACHING_03) scripts/prepare_chapter_07.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/prepare_chapter_07.py

chapter-07-exports: $(TEACHING_07) scripts/export_chapter_07_figures.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/export_chapter_07_figures.py

point-data: scripts/prepare_point_data.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/prepare_point_data.py

spatial-data: scripts/prepare_spatial_data.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/prepare_spatial_data.py

qgis-transfer: $(TEACHING_02) scripts/prepare_qgis_transfer.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/prepare_qgis_transfer.py

snapshots: $(STARTER) $(TEACHING) $(TEACHING_02) $(TEACHING_03) $(TEACHING_07) scripts/publish_snapshots.py | $(VENV_STAMP)
	$(VENV_PYTHON) scripts/publish_snapshots.py

packages: snapshots scripts/build_packages.py
	$(VENV_PYTHON) scripts/build_packages.py

check: $(TEACHING_07) scripts/check_chapter_01.py scripts/check_chapter_02.py scripts/check_chapter_03.py scripts/check_chapter_07.py
	$(VENV_PYTHON) scripts/check_chapter_01.py
	$(VENV_PYTHON) scripts/check_chapter_02.py
	$(VENV_PYTHON) scripts/check_chapter_03.py
	$(VENV_PYTHON) scripts/check_chapter_07.py

libreoffice-check: $(TEACHING) $(TEACHING_02) $(TEACHING_03)
	mkdir -p ../../tmp/libreoffice-check
	libreoffice --headless --convert-to xlsx --outdir ../../tmp/libreoffice-check "$(TEACHING)"
	libreoffice --headless --convert-to xlsx --outdir ../../tmp/libreoffice-check "$(TEACHING_02)"
	libreoffice --headless --convert-to xlsx --outdir ../../tmp/libreoffice-check "$(TEACHING_03)"
