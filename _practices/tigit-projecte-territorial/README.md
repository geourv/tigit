# Projecte territorial TIGIT

Projecte pràctic acumulatiu per preparar una infografia territorial a partir de dades oficials, indicadors, gràfics i mapes. El parell Tarragonès–Vila-seca i les dades de població i habitatge de 2021 formen exclusivament el cas de demostració del professorat. Cada trio rebrà un altre parell comarca–municipi i adaptarà les dades, els noms dels fitxers i les sortides al territori i al període assignats.

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

La seqüència de treball és fonts, indicadors, gràfics, color, dades espacials, SIG, llenguatge cartogràfic, cartografia temàtica i síntesi. Els prefixos dels fitxers són identificadors tècnics estables creats amb les fites originals; no indiquen l'ordre actual de lectura. Per això `tigit-07-teoria-color.xlsx` precedeix `tigit-05-integracio-sig.xlsx` i n'és una entrada explícita.

| Fitxer | Resultat docent |
| --- | --- |
| `data/processed/tigit-01-preparacio-dades.xlsx` | Fonts, imports, controls i taula municipal preparada |
| `data/processed/tigit-02-indicadors-territorials.xlsx` | Indicadors i agregats afegits al llibre anterior |
| `data/processed/tigit-03-semiologia-visualitzacio.xlsx` | Taules auxiliars i gràfics editables afegits al llibre anterior |
| `data/processed/tigit-07-teoria-color.xlsx` | Registre cromàtic i prova sobre un gràfic |
| `qgis/tigit-04-dades-espacials.qgz` | Base espacial inspeccionada i validada |
| `qgis/tigit-05-integracio-sig.qgz` | Indicadors units i consultes comprovades |
| `data/processed/tigit-05-integracio-sig.xlsx` | Llibre acumulatiu amb `map_export` preparat per a QGIS |
| `qgis/tigit-06-llenguatge-cartografic.qgz` | Mapa de context i retolació revisada |
| `qgis/tigit-08-cartografia-tematica.qgz` | Mapa temàtic i alternativa controlada |
| `outputs/infographics/infografia_<comarca>-<municipi>_<periode>.svg` | Màster editable de la infografia adaptat al parell assignat |

Els sufixos no són números de versió arbitraris. Identifiquen una fita docent i permeten comparar què s'hi ha incorporat. Git conserva, a més, l'historial de canvis de cada fita.

## Reproducció executable

El `Makefile` local explicita l'ordre de les operacions:

```bash
make chapter-01-starter
make chapter-01
make chapter-02
make chapter-03
make chapter-03-exports
make chapter-07
make chapter-07-exports
make point-data
make spatial-data
make qgis-transfer
make snapshots
make packages
make check
make libreoffice-check
```

`chapter-01-starter` genera el llibre buit de l'estudiant. `chapter-01` crea la versió docent de preparació de dades, `chapter-02` hi afegeix els indicadors, `chapter-03` incorpora els gràfics i `chapter-07` aplica el registre cromàtic. `point-data`, `spatial-data` i `qgis-transfer` preparen després les entrades de les fases SIG; `qgis-transfer` deriva `tigit-05-integracio-sig.xlsx` de `tigit-07-teoria-color.xlsx` i hi afegeix `map_export`. `snapshots` publica aquesta genealogia, `packages` reconstrueix els ZIP i `check` comprova dimensions, files, fórmules i integritat.

La preparació tabular utilitza Python perquè la lectura de CSV i JSON-stat és directa i auditable. LibreOffice s'utilitza com a aplicació final del llibre i com a motor de compatibilitat mitjançant la línia d'ordres. L'API UNO es reservarà per a operacions pròpies de Calc, com taules dinàmiques o gràfics, quan aporti un resultat que no convingui simular amb una biblioteca externa.

## Resultats exportats

Els resultats incorporen fenomen, territori i període, per exemple:

```text
outputs/figures/age-structure-tarragones-2021.pdf
outputs/figures/non-principal-housing-tarragones-2021.pdf
outputs/maps/context_tarragones.pdf
outputs/maps/coropleta_no_principal_tarragones_2021.svg
outputs/infographics/infografia_tarragones-vila-seca_2021_review.pdf
dist/infografia_tarragones-vila-seca_2021.pdf
dist/projecte_tarragones-vila-seca_2021.zip
```

Els tres darrers noms exemplifiquen la demostració del professorat; cada trio substituirà `tarragones-vila-seca` pel seu parell assignat. Els fitxers d'`outputs/` són intermedis o editables. `dist/` conservarà el PDF final i el ZIP reproduïble que l'estudiant lliurarà; el màster SVG continuarà a `outputs/` com a font editable.

## Registre cromàtic

El full `palette` del llibre acumulatiu conserva els codis, l'origen i la funció de cada color. El fons i els textos utilitzen neutres; el gràfic ordenat reserva `#D55E00` com a accent redundant de Vila-seca; els grups d'edat utilitzen una seqüència discreta YlGnBu amb límits foscos; i la piràmide separa les categories nominals de sexe amb una parella equilibrada. BuGn és la candidata seqüencial per a la coropleta, mentre que RdBu només s'utilitzarà amb una referència central explícita.

El mateix full registra el gris equivalent i les simulacions completes de protanopia, deuteranopia i tritanopia calculades amb les [matrius de Machado, Oliveira i Fernandes (2009)](https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html). La revisió confirma l'ordre clar-fosc de YlGnBu i BuGn; també documenta que la parella nominal, l'accent i la rampa divergent necessiten l'etiqueta, la posició, el patró o la llegenda previstos i no poden dependre només del color. Els controls executables rebutgen qualsevol color definit que conservi una prova pendent. El lot només es publicarà un cop inspeccionades les tres proves PDF/SVG a mida final.

## Cobertura actual

| Fase visible | Identificador tècnic | Estat executable |
| --- | --- | --- |
| Preparació de dades | `01` | Complet: llibre inicial, versió docent, fonts i controls |
| Indicadors territorials | `02` | Complet: sis indicadors, agregats i comprovacions; falta integrar l'oferta turística municipal exigida per la guia docent |
| Semiologia i visualització | `03` | Complet: llibre progressiu, auditoria, tres gràfics i exportacions PDF/SVG |
| Teoria del color | `07` | Executable complet: registre, contrast i simulacions; inspecció humana a mida final pendent |
| Dades espacials | `04` | GeoPackage compacte preparat; projecte QGIS pendent |
| Integració SIG | `05` | CSV, CSVT i punts preparats; unió QGIS pendent |
| Llenguatge cartogràfic | `06` | Activitat definida; composicions i exportacions pendents |
| Cartografia temàtica | `08` | Activitat definida; classificacions i mapes pendents |
| Infografia i síntesi | `09` | Format i maqueta preliminar definits; màster, PDF final i ZIP reproduïble pendents |

La pràctica no es pot considerar completa ni publicable mentre faltin la taula municipal d'allotjament turístic i els seus indicadors, els projectes QGIS comprovats, les exportacions cartogràfiques, el màster SVG, la prova de lectura, el PDF final i l'extracció de control del ZIP reproduïble.

## Regla de correcció

Una dada no es corregeix directament en un fitxer de `data/raw` ni en una exportació. La regla s'aplica al llibre o projecte editable que correspongui, es registra a `checks` o en aquest document i es regenera el resultat dependent.

## Paquets distribuïbles

`scripts/build_packages.py` genera dos ZIP diferenciats. El paquet inicial de l'estudiant es publica a `assets/downloads`; el paquet docent queda a `dist/course-packages`. El ZIP reproduïble que elaborarà l'estudiant al final serà un altre lliurable i es desarà a `dist/` juntament amb la infografia final.
