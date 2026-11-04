PYTHON ?= python3
CALC_PYTHON ?= /usr/bin/python3
PRACTICE := $(patsubst %/,%,$(dir $(lastword $(MAKEFILE_LIST))))
SCRIPTS := $(PRACTICE)/scripts
RUN ?=
QGIS_INPUTS ?=
export TIGIT_PRACTICE_RUN := $(RUN)
export PYTHONDONTWRITEBYTECODE := 1
.DEFAULT_GOAL := help
.NOTPARALLEL:

.PHONY: help test resources check-resources require-run workbook-inputs workbooks check figures check-figures qgis-inputs

help:
	@printf '%s\n' 'Executar des de l’arrel de TIGIT amb make -f practiques/tigit-projecte-territorial/Makefile TARGET.' 'resources: descarregar els inputs fixats; check-resources: verificar-los sense escriure.' 'workbook-inputs RUN=sandbox/practiques/tigit-projecte-territorial/fulls/NOM: preparar un run nou.' 'workbooks RUN=...: construir els sis llibres amb Python/openpyxl i Calc/UNO.' 'check RUN=...: comprovar llibres i CSV, sense generar-los.' 'figures RUN=...: exportar els gràfics amb Calc i Inkscape; check-figures RUN=...: verificar-los.' 'qgis-inputs QGIS_INPUTS=sandbox/practiques/tigit-projecte-territorial/entrades-qgis/NOM: preparar el request natiu.' 'test: comprovar el contracte de preparació. GIS, PDFs i edicions es processen amb els proveïdors natius.'

test:
	$(PYTHON) -B -m unittest discover -s $(PRACTICE)/tests -v

resources:
	$(PYTHON) -B $(PRACTICE)/preparar.py resources --fetch

check-resources:
	$(PYTHON) -B $(PRACTICE)/preparar.py check-resources

require-run:
	@test -n "$(RUN)" || { printf '%s\n' 'Cal indicar RUN amb una destinació de fulls dins de sandbox.' >&2; exit 1; }

workbook-inputs: require-run
	$(PYTHON) -B $(PRACTICE)/preparar.py workbook-inputs --output "$(RUN)"

workbooks: require-run
	$(PYTHON) -B $(SCRIPTS)/create_chapter_01_workbook.py
	$(PYTHON) -B $(SCRIPTS)/prepare_chapter_01.py
	$(CALC_PYTHON) -B $(SCRIPTS)/create_calc_pivots.py "$(RUN)/data/processed/tigit-01-preparacio-dades-teaching.xlsx" --county
	$(PYTHON) -B $(SCRIPTS)/prepare_chapter_02.py
	$(CALC_PYTHON) -B $(SCRIPTS)/create_calc_pivots.py "$(RUN)/data/processed/tigit-02-indicadors-territorials-teaching.xlsx" --county
	$(PYTHON) -B $(SCRIPTS)/prepare_chapter_03.py
	$(CALC_PYTHON) -B $(SCRIPTS)/create_calc_pivots.py "$(RUN)/data/processed/tigit-03-semiologia-visualitzacio-teaching.xlsx" --county --population
	$(PYTHON) -B $(SCRIPTS)/prepare_chapter_07.py
	$(PYTHON) -B $(SCRIPTS)/prepare_qgis_transfer.py

check: require-run
	$(PYTHON) -B $(SCRIPTS)/check_chapter_01.py
	$(PYTHON) -B $(SCRIPTS)/check_chapter_02.py
	$(PYTHON) -B $(SCRIPTS)/check_chapter_03.py
	$(PYTHON) -B $(SCRIPTS)/check_chapter_07.py
	$(PYTHON) -B $(SCRIPTS)/check_chapter_05.py

figures: require-run
	$(PYTHON) -B $(SCRIPTS)/export_chapter_03_figures.py
	$(PYTHON) -B $(SCRIPTS)/export_chapter_07_figures.py

check-figures: require-run
	$(PYTHON) -B $(SCRIPTS)/check_chapter_03.py --figures
	$(PYTHON) -B $(SCRIPTS)/check_chapter_07.py --figures

qgis-inputs:
	@test -n "$(QGIS_INPUTS)" || { printf '%s\n' 'Cal indicar QGIS_INPUTS amb una destinació nova.' >&2; exit 1; }
	$(PYTHON) -B $(PRACTICE)/preparar.py qgis-inputs --output "$(QGIS_INPUTS)"
