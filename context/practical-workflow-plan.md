# Pla del recorregut pràctic acumulatiu

## Criteri territorial

- Escala principal: els 22 municipis del Tarragonès.
- Municipi de control i detall: Vila-seca, codi `431711`.
- Període estadístic principal: població i habitatge de 2021.
- Les fonts posteriors, com centres educatius 2025/2026 o geometria ICGC 2026, s'han de presentar com a context temporal posterior, no com si fossin observacions simultànies.

## Dades tabulars

El llibre distingeix quatre nivells:

1. `data/raw`: fitxers i respostes originals sense modificar.
2. `source_*`: estructura importada amb els camps i categories de la font.
3. `prepared_*`: camps tipats, normalitzats i documentats pel projecte.
4. `municipal`, `indicators_*` i `charts_*`: integració, càlcul i representació.

Els fulls `source_*` no reben noms de camp propis del projecte. Les transformacions han de quedar visibles en el pas cap a `prepared_*`.

## Calc i gràfics

La fita del capítol 3 crearà:

- `charts_data`: rangs vinculats i controls de suma;
- `chart_00_audit`: versió inicial i revisada d'un mateix gràfic;
- `chart_01_age_structure`: barres horitzontals apilades al 100%;
- `chart_02_nonprincipal`: barres horitzontals ordenades del percentatge d'habitatge no principal;
- `chart_03_scatter`: dispersió entre població de 65+ i habitatge no principal, amb Vila-seca identificada;
- `chart_04_housing_donut`: anell de composició del parc d'habitatges;
- `chart_05_population_time`: línia de població anual de Vila-seca, 2000–2022;
- `chart_06_population_pyramid`: piràmide per edat i sexe de Vila-seca, 2021;
- `chart_07_housing_histogram`: distribució municipal de l'habitatge no principal;
- `palette`: registre cromàtic que s'afegirà al capítol 7.

Les figures candidates s'exportaran en PDF vectorial. El PDF s'obrirà a Inkscape per comprovar objectes, textos, fonts i proporcions. Les captures mínimes seran el diàleg de rangs o sèries de Calc i una comprovació vectorial a Inkscape.

## Dades puntuals

### Capa XY principal

Font: Directori anual de centres docents de la Generalitat, conjunt `kvmv-ahh4`.

- API: `https://analisi.transparenciacatalunya.cat/resource/kvmv-ahh4.json`
- CSV: `https://analisi.transparenciacatalunya.cat/resource/kvmv-ahh4.csv`
- Camps útils: codi i nom del centre, titularitat, adreça, codi municipal de sis dígits, UTM X/Y, longitud/latitud i geometria.
- CRS UTM declarat: ETRS89 / UTM 31N, `EPSG:25831`.
- Subconjunt inicial: 17 centres de Vila-seca del curs 2025/2026.
- Ampliació: 183 centres del Tarragonès.

Al final del capítol 4, després d'explicar coordenades i CRS, la taula s'inspeccionarà encara en Calc o Excel: ordre X/Y, graus, metres, absències i duplicats. Al capítol 5 s'importarà primer X/Y UTM i després longitud/latitud per comparar `EPSG:25831` i `EPSG:4326`. El punt representa l'entrada del centre, no tota la parcel·la ni la seva capacitat.

### Geocodificació

Font: Establiments d'allotjament turístic inscrits al Registre de Turisme de Catalunya, conjunt `t2h3-cgys`.

- API: `https://analisi.transparenciacatalunya.cat/resource/t2h3-cgys.json`
- CSV: `https://analisi.transparenciacatalunya.cat/resource/t2h3-cgys.csv`
- Subconjunt inicial: allotjaments convencionals de Vila-seca, excloent habitatges d'ús turístic i llars compartides.
- Geocodificador: ICGC, `https://eines.icgc.cat/geocodificador/`.

Es conservaran l'adreça original, el text retornat, els codis territorials, les coordenades, l'estat d'èxit o ambigüitat i la revisió manual. El registre mesura oferta inscrita, no obertura, disponibilitat, ocupació ni pernoctacions.

## Geometria i QGIS

Font principal: Divisions administratives ICGC v2.2, gener de 2026, CC BY 4.0.

- Descàrrega GeoPackage: `https://datacloud.icgc.cat/datacloud/divisions-administratives/gpkg/divisions-administratives-v2r2-20260120.zip`
- Escala 1:250.000 per al mapa comarcal.
- Escala 1:50.000 per al control de Vila-seca.
- Escala generalitzada per al requadre provincial.

El GeoPackage s'introduirà com un contenidor de capes comparable a un llibre amb fulls. No s'introduiran SQL, triggers ni administració de bases de dades. Les fites seran `tigit-04-dades-espacials.qgz`, `tigit-05-integracio-sig.qgz`, `tigit-06-llenguatge-cartografic.qgz` i `tigit-08-cartografia-tematica.qgz`.

Natural Earth s'utilitzarà només si cal un localitzador d'Europa o del món. No substituirà les geometries oficials de municipis, comarca o província.

## Mapes

- Capítol 6: mapa de context del Tarragonès i requadre provincial, amb versions d'etiquetatge automàtic i revisat.
- Capítol 8: coropleta del percentatge d'habitatge no principal.
- Capítol 8: mapa separat de símbols proporcionals amb habitatges totals.
- Les classificacions final i alternativa conservaran extensió, mida, paleta i context; només canviarà una decisió controlada.
- Els punts de tall, recomptes per classe i colors es conservaran en un registre llegible per màquina.

## Color i infografia

El capítol 7 aplicarà un color neutre a totes les barres i un accent redundant a Vila-seca; la rampa seqüencial per a la coropleta es provarà com a mostres, sense fixar encara els intervals. La prova s'exportarà en SVG i PDF.

El producte final serà A3 vertical, `297 × 420 mm`, amb marges de `15 mm`, sis columnes i separacions de `6 mm`. Orientacions inicials:

- títol: 30–34 pt;
- entrada: 15–17 pt;
- mètrica principal: 24–30 pt;
- cos: 11,5–13 pt;
- etiquetes de mapes i gràfics: 10,5–12 pt;
- fonts i notes: 9–10 pt com a mínim.

Si cal una versió A4, es redissenyarà; no es reduirà automàticament l'A3. PowerPoint es pot utilitzar per a un wireframe A3 ràpid, però el màster final serà SVG d'Inkscape.

## Captures pendents

- Calc: importació delimitada i codi com a text.
- Calc: rangs o sèries vinculats del gràfic ordenat.
- Calc o Excel 365: configuració del full de gràfic i exportació PDF/SVG utilitzada pel grup.
- QGIS: selecció de subcapes del GeoPackage i CRS.
- QGIS: importació XY amb X, Y i CRS d'origen.
- QGIS: configuració i comprovació de la unió municipal.
- QGIS: etiquetatge automàtic i revisat.
- QGIS/Inkscape: prova tipogràfica amb família, variants i caràcters del projecte a mida final.
- QGIS: classificació graduada i assistent de mida proporcional.
- Inkscape: objecte vectorial seleccionat i codi de color visible.
- Inkscape: document A3 amb guies, marges i capes.

Les captures mostraran decisions d'interfície, no substituiran els gràfics, mapes o documents exportats.
