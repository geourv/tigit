# Pla d'ampliació a partir del material antic

Aquest document és una eina editorial. No forma part del cos publicable del manual i pot contenir notes de treball, figures pendents i decisions sobre materials que no s'han de reproduir directament.

## Criteri general

Els `homework`, les diapositives i les imatges de `sandbox/geoteaching-tigit-90437e4c4ce3/` s'utilitzen com a pedrera de preguntes, seqüències didàctiques, exemples i guions visuals. Les imatges antigues no s'han d'incorporar al manual mentre no tinguin autoria, origen, llicència i funció didàctica verificables. Quan la idea visual sigui bona però la imatge no sigui publicable, la sortida preferent és una figura pròpia, una captura documentada d'un recurs consultat de nou, o un recurs obert amb registre complet.

El cos del manual ha de continuar sent publicable. Per tant, els placeholders editorials no s'han d'inserir en cap capítol ni pàgina mentre unaltraweb no tingui un mode explícit de revisió que els separi de la publicació web i PDF. De moment, les figures pendents es registren a `context/figure-plan.md` i en aquest document.

### Criteri provisional de revisió visual

El 14 d'agost de 2026 s'ha introduït una excepció de treball per aprofundir els capítols 2-9: quan encara no existeixi la figura ideal, es pot incorporar una imatge de les diapositives antigues o un placeholder visual amb una descripció precisa. Les imatges procedents de `sandbox/geoteaching-tigit-90437e4c4ce3/` han d'indicar explícitament al peu que la font, autoria o llicència estan pendents, i la posició de la llicència ha d'incloure el text literal `Referencia pendiente`. Aquest criteri serveix per a revisió docent i no elimina la necessitat de substituir o verificar cada recurs abans d'aprovar el contingut.

## Fonts locals revisades

| Tipus | Fitxers principals | Ús editorial |
| --- | --- | --- |
| Diapositives | `0-presentacio-de-la-assignatura-cat.slides.md`, `1-presentacio-de-la-informacio-cat.slides.md`, `2-representacio-de-la-terra-cat.slides.md`, `3-el-llenguatge-cartografic-cat.slides.md`, `4-mapes-tematics-cat.slides.md`, `5-gps-i-sig-cat.slides.md` | Guió visual, repertori de conceptes i exemples per redibuixar |
| Homework conceptual | `1-4-la-teoria-del-color-cat.homework.md`, `2-1-treball-amb-coordenades-cat.homework.md`, `2-3-el-reticle-utm-cat.homework.md`, `3-treball-amb-escales-cat.homework.md`, `3-toponimia-cat.homework.md`, `3-mapa-topografic-nacional-espanyol-cat.homework.md`, `3-us-de-color-als-mapes-cat.homework.md`, `5-1-breu-historia-de-la-cartografia-cat.homework.md` | Activitats d'autoaprenentatge que es poden convertir en exemples resolts, criteris de revisió o bancs d'exercicis |
| Proves pràctiques | `2018-12-20-segona-prova-practica-qgis-cat.homework.md`, `2019-01-21-segona-prova-practica-excel-cat.homework.md`, `2019-01-21-segona-prova-practica-cat.homework.md` | Patrons d'avaluació pràctica, no calendari ni dades antigues |
| Imatges antigues | `src/images/png/*.png`, `src/images/mmd/*.uml` | Només diagnosi visual; cada reutilització necessita decisió individual |
| Dades antigues | `src/data/*.xls`, `*.xlsx`, `*.shp`, `*.kml` | Models de problemes de dades; les dades s'han d'actualitzar o substituir abans de publicar-les |

## Oportunitats per capítol

| Capítol actual | Material antic útil | Ampliació recomanada | Figura o suport visual |
| --- | --- | --- | --- |
| Fonts i preparació de dades | Taules turístiques antigues, claus incompatibles i exercicis Excel | Afegir un cas narratiu de taula imperfecta: font, metadades, codis, tipus de dada, files buides i camp calculat | Figura pròpia del full `sources` + `dictionary`, i captura Calc/Excel quan el llibre docent estigui estabilitzat |
| Indicadors territorials i turístics | Gràfics antics d'establiments, places i pernoctacions | Reforçar valors absoluts, percentatges, ràtios, densitats i denominadors amb un mateix indicador turístic | Sèrie pròpia amb la mateixa comarca: recompte, taxa per 1.000 habitants, densitat i composició |
| Semiologia i visualització | `1-presentacio-de-la-informacio-cat.slides.md`; repertori de gràfics i infografies saturades | Convertir el contrast text/taula/gràfic/mapa/infografia en una decisió de lectura, no en una galeria de tipus | Figura pròpia "mateixa pregunta, quatre formes de representació"; auditoria d'una infografia com a exemple textual o figura recreada |
| Color | `1-4-la-teoria-del-color-cat.homework.md`; `3-us-de-color-als-mapes-cat.homework.md` | Desenvolupar paletes segons tipus de dada, contrast simultani i diferència entre provar colors a la llegenda i provar-los al mapa | Figures pròpies de paletes seqüencials, divergents, qualitatives i binàries; mostra mapa/llegenda reconstruïda |
| Terra i dades espacials | Coordenades, UTM, geoide, el·lipsoide, dàtum i mapa resolt de geolocalització | Afegir activitats curtes de lectura de coordenades i diferència entre retícula angular i quadrícula mètrica | Esquema propi de coordenades i exercici resolt sobre mapa obert; no reutilitzar el mapa antic |
| Llenguatge cartogràfic | Escales, MTN, toponímia, generalització, retolació i llegenda | Separar bloc conceptual d'escala de banc d'exercicis; afegir retolació/toponímia amb nomenclàtors actuals | Figures pròpies de generalització a tres escales, retolació abans/després i composició de mapa |
| SIG | Proves QGIS, diagrames UML i diapositives de components/mètodes | Convertir "fer dos mapes" en flux traçable: preparar CSV, importar, unir, validar i simbolitzar | Diagrama reproduïble del flux SIG; captures QGIS actuals amb dades de demostració |
| Cartografia temàtica | `4-mapes-tematics-cat.slides.md`; classificacions i tipus de mapa | Reforçar la comparació controlada: mateixa geometria, mateix indicador, només canvia classificació, paleta o tècnica | Sèrie pròpia amb intervals iguals, quantils, Jenks, coropleta, símbols proporcionals i, si cal, fluxos/cartogrames com ampliació |
| Infografia i síntesi | Infografies antigues i idea de conservar rastre Excel/QGIS/Inkscape | Fer visible la decisió de síntesi: pregunta, selecció d'evidències, retícula, jerarquia, fonts i exportació | Comparació pròpia entre composició saturada i composició revisada; captura Inkscape només per operacions de maquetació |

## Figures candidates

| ID provisional | Capítol | Inspiració local | Decisió | Producció prevista |
| --- | --- | --- | --- | --- |
| `fig-03-representation-forms` | Semiologia | `chart-catalonia-landuse.png`, `map-middle-earth.png`, repertori de gràfics | Recrear | Una mateixa dada turística explicada com a text breu, taula, gràfic i mapa esquemàtic |
| `fig-03-chart-audit` | Semiologia | `infographics-tourism.png`, repertori de gràfics | Recrear | Auditoria d'una peça densa amb criteris de pregunta, unitat, font, jerarquia i soroll visual |
| `fig-04-map-vs-legend-color` | Color | `map-colors-perception.png`, `maps-color-perception-legend.png` | Recrear | Mostra controlada on el mateix color es llegeix diferent segons fons, mida del polígon i llegenda |
| `fig-04-palette-families` | Color | `sequential-*`, `divergent-*`, `qualitative-*`, `binary-colors-map.png` | Recrear | Paletes i minivisualitzacions amb una mateixa geometria o graella sintètica |
| `fig-05-coordinate-exercise` | Terra i dades espacials | `geolocation-exercice-world-map*.png` | Recrear | Mapa obert o esquema propi per practicar latitud, longitud i hemisferis |
| `fig-05-ed50-etrs89` | Terra i dades espacials | `datum-distortions.png`, capes antigues ED50 | Recrear | Mateixa entitat interpretada amb CRS correcte i incorrecte, amb desplaçament mesurat |
| `fig-06-mtn-sheet-system` | Llenguatge cartogràfic | `3-mapa-topografic-nacional-espanyol-cat.homework.md` | Proposada | Esquema propi de full 1:50.000 i subdivisió a escales més detallades |
| `fig-06-toponymy-labels` | Llenguatge cartogràfic | `3-toponimia-cat.homework.md`, `map-labels-eg-*` | Recrear | Retolació amb prioritats, topònims oficials i conflictes resolts |
| `fig-06-generalization-three-scales` | Llenguatge cartogràfic | `map-generalization-three-scales.png` | Recrear | Mateix territori a tres escales amb selecció, simplificació i canvi de jerarquia |
| `fig-07-gis-workflow` | SIG | `qgis-exercise-setup.uml`, `qgis-join-attributes.uml`, `qgis-visual-analysis.uml` | Recrear | Diagrama únic de preparació, importació, unió, validació i exportació |
| `fig-08-classification-series` | Cartografia temàtica | `quantile-choropleth-map.png`, `iqual-intervals-choropleth-map.png`, `natural-breaks-jenks-choropleth-map.png` | Recrear | Mateix indicador municipal amb intervals iguals, quantils i Jenks, punts de tall visibles |
| `fig-08-technique-choice` | Cartografia temàtica | cartodiagrames, coropletes, fluxos, dasimètrics i cartogrames antics | Recrear | Matriu de tècnica cartogràfica segons tipus de dada i pregunta |
| `fig-09-synthesis-before-after` | Infografia | `infographics-tourism.png`, gràfics turístics antics | Recrear | Comparació entre peça saturada i versió amb una pregunta territorial explícita |

## Patrons de homework que convé recuperar

El treball d'escales és el patró més madur: enunciat, nota conceptual, preguntes i resolució pas a pas. Al manual convé mantenir la teoria al capítol i portar les vint operacions a un bloc d'activitat o banc de pràctica. Els exemples resolts poden quedar en tres famílies: distància mapa-realitat, superfície i equivalència de fulls.

El treball amb coordenades aporta una situació professional narrativa i una resolució interpretativa. Cal actualitzar la notació, evitar coordenades amb minuts impossibles si no es vol usar-les com a error deliberat, i generar el mapa amb una font oberta o un esquema propi.

El reticle UTM és més un guió de cerca que una explicació final. Pot alimentar un apartat d'activitat autònoma: origen, fusos, zona 31N, fals est, fals nord, coordenades en metres i ús en un full del MTN.

Toponímia és útil per ampliar la retolació: el mapa no només posa noms, també tria formes oficials, exònims i criteris lingüístics. Cal actualitzar exemples sensibles i contrastar-los amb nomenclàtors vigents abans de publicar-los.

Els deures de color ja contenen la seqüència conceptual que el manual necessita. S'han de reescriure amb terminologia actual, corregir possibles simplificacions, citar fonts i substituir imatges antigues per figures pròpies o recursos oberts verificats.

Les proves QGIS antigues s'han de convertir en criteris de pràctica, no en enunciats històrics. El valor no és l'any 2013 ni els intervals fixats, sinó el tipus de tasca: unir dades, triar tècnica, classificar, construir llegenda i exportar un resultat llegible.

## Millora proposada per a unaltraweb i l'MCP

El contracte actual d'unaltraweb és correcte per publicar: `manual_editorial_quality_check` rebutja placeholders en el cos del manual, i `manual_source_quality_check` comprova que les figures tinguin caption. El que falta és un estat intermedi de producció visual.

Proposta de millora:

1. Afegir un manifest opcional, per exemple `context/figure-proposals.yml` o `_data/manual_figures.yml`, amb `id`, `chapter_ref`, `status`, `legacy_trigger`, `rights_status`, `desired_figure`, `production_plan` i `replacement_asset`.
2. Afegir una eina MCP `manual_figure_proposal_inventory` que llegeixi aquest manifest i retorni figures pendents, bloquejades per drets, preparades i incorporades.
3. Afegir una comprovació `manual_asset_provenance_check` que avisi si una imatge publicada al manual no apareix al manifest o no té evidència de font/llicència al peu o al registre.
4. Permetre placeholders només en mode revisió, amb un bloc explícit com `::: figure-proposal id="fig-06-toponymy-labels" :::`, que no s'ha de renderitzar en producció web/PDF o que ha de fer fallar la publicació si continua actiu.
5. Mantenir els placeholders fora del cos publicable per defecte. El mode de producció ha de continuar exigint figures finals, captions i procedència verificable.

Amb aquest flux, una imatge de les diapositives pot inspirar una figura sense entrar a `assets/`, i una figura pendent pot ser visible per a l'equip docent sense convertir-se accidentalment en material publicat.
