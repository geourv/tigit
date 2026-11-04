# Reproducció del cas docent Tarragonès–Vila-seca

Aquest directori conté les fonts del cas docent: preparació de recursos, llibres de càlcul, request/model QGIS i plantilla A3 editable. Les lectures són a les carpetes de les pràctiques 01–04. La migració de les dependències públiques del manual continua documentada a `context/practice-migration.md`.

## Recursos fixats

`recursos.yml` declara vint inputs de dades i un PDF històric d'auditoria, amb mida i SHA-256, recuperables del commit `715944fcbf5463e6dd48ade7696a251c94e8c2fd`. Inclou extractes i derivats ja existents. Aquesta recuperació no és una consulta nova a Idescat/ICGC i no canvia els períodes dels materials.

Les comandes s'executen des de l'arrel de TIGIT. La primera descàrrega és explícita; quan el snapshot ja existeix, només cal comprovar-lo:

```bash
python3 -B practiques/tigit-projecte-territorial/preparar.py resources --fetch
python3 -B practiques/tigit-projecte-territorial/preparar.py check-resources
```

El snapshot canònic és `sandbox/practiques/tigit-projecte-territorial/recursos/2026-10-14/`. La preparació verifica tots els bytes abans d'escriure i refusa sobreescriure una destinació existent. Una operació interrompuda es conserva i cal escollir una destinació nova. Els snapshots del dia 13 continuen com a evidència amb el manifest anterior.

La població i l'habitatge són de 2021; la superfície publicada el 2025 conserva els controls pendents C07/C14. La geometria ICGC de 2026 necessita justificació de compatibilitat amb les estadístiques. L'habitatge no principal no identifica habitatges turístics, i residents per habitatge principal no és la grandària oficial de la llar.

La font cartogràfica és Divisions administratives ICGC v2.2, data territorial 20/01/2026, llicència CC BY 4.0 i EPSG:25831. El [ZIP original](https://datacloud.icgc.cat/datacloud/divisions-administratives/gpkg/divisions-administratives-v2r2-20260120.zip) té SHA `563fb7d81e143509d88569a9e8fe86d7c44ae9ce9e96c75b888379a7f0554162`; els dos GeoPackages compactes tenen els seus hashes propis al manifest. Les URL de les consultes estadístiques es conserven a les taules i als scripts de domini. Cal contrastar les condicions de reutilització de cada font abans de distribuir-ne una selecció.

## Llibres en un run aïllat

Cal Python 3.10 o posterior amb `openpyxl==3.1.5`, LibreOffice Calc i un Python amb el mòdul UNO. `PYTHON` selecciona l'entorn amb openpyxl i `CALC_PYTHON` el Python d'UNO. La instal·lació d'aquestes dependències és explícita; el Makefile no instal·la programari.

```bash
make -f practiques/tigit-projecte-territorial/Makefile test
make -f practiques/tigit-projecte-territorial/Makefile workbook-inputs \
  RUN=sandbox/practiques/tigit-projecte-territorial/fulls/revisio-01
make -f practiques/tigit-projecte-territorial/Makefile workbooks \
  RUN=sandbox/practiques/tigit-projecte-territorial/fulls/revisio-01
make -f practiques/tigit-projecte-territorial/Makefile check \
  RUN=sandbox/practiques/tigit-projecte-territorial/fulls/revisio-01
```

`workbook-inputs` copia només les taules raw fixades, registra els hashes de les fonts a `run-inputs.json` i crea `data/processed/` buit. No copia els llibres resolts del llegat. `workbooks` reconstrueix la plantilla d'alumnat i els llibres docents 01, 02, 03, 07 i 05; utilitza les dades locals i no fa consultes estadístiques noves. Els scripts de reproducció refusen fonts o inputs raw canviats i outputs de llibre preexistents: cal un run nou per reproduir una versió nova.

Els llibres, caches i exports romanen dins del run. Calc usa un perfil propi del run i una connexió UNO de nom únic; les operacions es fan serialment. `check` és readonly i no té dependències que regenerin dades o llibres. Les proves amb Calc no acrediten automàticament la compatibilitat visual amb Excel.

Els scripts d'adquisició de dades es conserven com a fonts de procedència. Fer-hi consultes noves exigeix `TIGIT_FETCH_TEACHING_DATA=1` i modifica exclusivament la còpia de treball seleccionada amb `TIGIT_PRACTICE_RUN`. No formen part de la reproducció fixada. Els resultats nous necessiten revisió de dates, metadades i manifest abans d'adoptar-los.

## Exports de gràfics

Amb Inkscape disponible, `figures RUN=...` exporta els gràfics del cas i `check-figures RUN=...` exigeix els PDF/SVG declarats. Es desen a `outputs/figures/chapter-03/` i `chapter-07/` dins del run, sense copiar-los a dist. Les figures públiques Quarto/Vega del manual tenen productors, fonts i locks propis.

Els gràfics d'habitatge i composició d'edats assignen els municipis a l'eix categòric i el percentatge a l'eix de valors, també quan les barres són horitzontals. Els comprovadors de 03 i 07 verifiquen els títols d'aquests eixos. La figura històrica amb els títols intercanviats continua al snapshot de recursos per a l'exercici d'auditoria de la lectura docent 03. Els SVG de prova requereixen encara una decisió sobre el fons i revisió visual abans del lliurament.

## QGIS, captures i PDFs

`activity-qgis.json` i `activities/qgis-territorial.py` són fonts de domini per al productor unaltracaptura-qgis 0.6.0. Cal preparar un packet nou amb els inputs declarats:

```bash
python3 -B practiques/tigit-projecte-territorial/preparar.py qgis-inputs \
  --output sandbox/practiques/tigit-projecte-territorial/entrades-qgis/revisio-01
```

El `practice-run` natiu rep el request d'aquell packet i una destinació nova. El seu `practice-check` verifica el bundle i calcula les dependències dels productes seleccionats. El preparador TIGIT no interpreta ni fabrica aquests segells. Les receptes de captura de la pràctica 04 són a `practiques/tigit-04-qgis-mapes/captures/` i la configuració és `.unaltracaptura-qgis-practice-04.yml`.

Els PDFs privats s'obtenen amb `manual_practice_pdf_build`, indicant la lectura, una versió i un run nou. El compositor d'edicions, quan contingut i seleccions estiguin confirmats, és `manual_practice_compose`. Encara queda pendent el contracte de composició sense GIS per als materials exclusivament tabulars. Aquest Makefile no genera ZIPs ni substitueix els productors GIS/PDF.
