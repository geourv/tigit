# Projecte territorial TIGIT

Projecte pràctic acumulatiu per preparar una infografia territorial a partir de dades oficials, indicadors, gràfics i mapes. El cas inicial utilitza municipis del Tarragonès i dades de població i habitatge de 2021, però la identitat del projecte no depèn d'aquest territori ni d'aquest període.

## Estructura

```text
data/raw/       Descàrregues originals sense modificar
data/processed/ Llibres, CSV i capes derivades
qgis/           Projectes, composicions i estils de QGIS
outputs/        Resultats intermedis regenerables
captures/       Captures netes de les decisions d'interfície
scripts/        Automatització, comprovacions i empaquetat
sandbox/        Proves temporals pròpies de la pràctica
dist/           Lliurables finals i paquets reproduïbles
```

## Estats acumulatius

| Fitxer | Resultat docent |
| --- | --- |
| `data/processed/tigit-01-preparacio-dades.xlsx` | Fonts, imports, controls i taula municipal preparada |
| `data/processed/tigit-02-indicadors-territorials.xlsx` | Indicadors i agregats afegits al llibre anterior |
| `data/processed/tigit-03-semiologia-visualitzacio.xlsx` | Taules auxiliars i gràfics editables afegits al llibre anterior |
| `qgis/tigit-04-dades-espacials.qgz` | Base espacial inspeccionada i validada |
| `qgis/tigit-05-integracio-sig.qgz` | Indicadors units i consultes comprovades |
| `data/processed/tigit-05-integracio-sig.xlsx` | Llibre acumulatiu amb `map_export` preparat per a QGIS |
| `qgis/tigit-06-llenguatge-cartografic.qgz` | Mapa de context i retolació revisada |
| `data/processed/tigit-07-teoria-color.xlsx` | Registre cromàtic i prova sobre un gràfic |
| `qgis/tigit-08-cartografia-tematica.qgz` | Mapa temàtic i alternativa controlada |
| `outputs/infographics/infografia_tarragones_2021.svg` | Màster editable de la infografia |

Els sufixos no són números de versió arbitraris. Identifiquen una fita docent i permeten comparar què s'ha incorporat en cada capítol. Git conserva, a més, l'historial de canvis de cada fita.

## Reproducció per capítols

El `Makefile` local explicita l'ordre de les operacions:

```bash
make chapter-01-starter
make chapter-01
make chapter-02
make point-data
make spatial-data
make qgis-transfer
make packages
make check
make libreoffice-check
```

`chapter-01-starter` genera el llibre buit de l'estudiant. `chapter-01` crea la versió docent de preparació de dades i `chapter-02` hi afegeix els indicadors. `point-data`, `spatial-data` i `qgis-transfer` preparen les entrades dels capítols SIG. `packages` reconstrueix els ZIP i `check` comprova dimensions, files, fórmules i integritat.

La preparació tabular utilitza Python perquè la lectura de CSV i JSON-stat és directa i auditable. LibreOffice s'utilitza com a aplicació final del llibre i com a motor de compatibilitat mitjançant la línia d'ordres. L'API UNO es reservarà per a operacions pròpies de Calc, com taules dinàmiques o gràfics, quan aporti un resultat que no convingui simular amb una biblioteca externa.

## Resultats exportats

Els resultats incorporen fenomen, territori i període, per exemple:

```text
outputs/figures/age-structure-tarragones-2021.pdf
outputs/figures/non-principal-housing-tarragones-2021.pdf
outputs/maps/context_tarragones.pdf
outputs/maps/coropleta_no_principal_tarragones_2021.svg
outputs/infographics/infografia_tarragones_2021_review.pdf
dist/infografia_tarragones_2021.pdf
```

Els fitxers d'`outputs/` són intermedis o editables. `dist/` conservarà el PDF final i el ZIP reproduïble que l'estudiant lliurarà; el màster SVG continuarà a `outputs/` com a font editable.

## Registre cromàtic

El full `palette` del llibre acumulatiu conserva els codis, l'origen i la funció de cada color. El fons i els textos utilitzen neutres; el gràfic ordenat reserva `#D55E00` com a accent redundant de Vila-seca; els grups d'edat utilitzen una seqüència discreta YlGnBu amb límits foscos; i la piràmide separa les categories nominals de sexe amb una parella equilibrada. BuGn és la candidata seqüencial per a la coropleta, mentre que RdBu només s'utilitzarà amb una referència central explícita.

El mateix full registra el gris equivalent i les simulacions completes de protanopia, deuteranopia i tritanopia calculades amb les [matrius de Machado, Oliveira i Fernandes (2009)](https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html). La revisió confirma l'ordre clar-fosc de YlGnBu i BuGn; també documenta que la parella nominal, l'accent i la rampa divergent necessiten l'etiqueta, la posició, el patró o la llegenda previstos i no poden dependre només del color. Els controls executables rebutgen qualsevol color definit que conservi una prova pendent. La inspecció humana de les tres proves PDF/SVG a mida final es farà abans de publicar el lot.

## Cobertura actual

| Capítol | Estat executable |
| --- | --- |
| 1. Preparació de dades | Complet: llibre inicial, versió docent, fonts i controls |
| 2. Indicadors territorials | Complet: sis indicadors, agregats i comprovacions |
| 3. Semiologia i visualització | Complet: llibre progressiu, auditoria, tres gràfics i exportacions PDF/SVG |
| 4. Dades espacials | GeoPackage compacte preparat; projecte QGIS pendent |
| 5. Integració SIG | CSV, CSVT i punts preparats; unió QGIS pendent |
| 6. Llenguatge cartogràfic | Activitat definida; layouts i exports pendents |
| 7. Teoria del color | Executable complet: registre, contrast i simulacions; inspecció humana a mida final pendent |
| 8. Cartografia temàtica | Activitat definida; classificacions i mapes pendents |
| 9. Infografia | Format i mockup definits; màster i lliurables pendents |

## Regla de correcció

Una dada no es corregeix directament en un fitxer de `data/raw` ni en una exportació. La regla s'aplica al llibre o projecte editable que correspongui, es registra a `checks` o en aquest document i es regenera el resultat dependent.

## Paquets distribuïbles

`scripts/build_packages.py` genera dos ZIP diferenciats. El paquet inicial de l'estudiant es publica a `assets/downloads`; el paquet docent queda a `dist/course-packages`. El ZIP reproduïble que elaborarà l'estudiant al final serà un altre lliurable i es desarà a `dist/` juntament amb la infografia final.
