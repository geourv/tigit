# Pla editorial de figures

Aquest document converteix les figures de les diapositives antigues, els llibres de consulta i els recursos oberts en decisions editorials verificables. No forma part del cos publicable del manual. Una figura només passa a `assets/` quan se'n poden documentar autoria, origen, llicència, funció didàctica, peu i text alternatiu.

## Estats

| Estat | Decisió |
| --- | --- |
| Incorporada | Recurs obert verificat, desat a `assets/` i citat al manual |
| Preparada | Recurs obert verificat que encara no cal inserir |
| Proposada | Recurs o captura pendent de produir; encara no s'ha d'inserir al cos publicable |
| Recrear | La idea és útil, però cal una figura pròpia amb un disseny i unes dades independents |
| Captura documentada | La interfície o el resultat web és l'objecte d'estudi; cal registrar URL, data, versió i condicions d'ús |
| No reutilitzar | No hi ha una procedència o una llicència suficient, o la figura ha perdut el context necessari |

## Auditoria de les figures prioritàries de les diapositives

| Capítol | Fitxer antic | Evidència de procedència | Decisió | Substitució prevista |
| --- | --- | --- | --- | --- |
| 3 | `visual-variables.png` | Captura d'una taula impresa en català, sense autor, obra, pàgina ni llicència; apareix dues vegades a `3-el-llenguatge-cartografic-cat.slides.md` | No reutilitzar | Matriu pròpia de marques, variables visuals i tasques de lectura, fonamentada en Bertin i contrastada amb Longley |
| 4 | `parallels-meridians.png` | Coincidència visual amb `Latitude and Longitude of the Earth.svg`, obra pròpia de Djexplo publicada a Wikimedia Commons sota CC0 1.0 | Incorporada | S'ha substituït la còpia rasteritzada per l'SVG original a `assets/img/coordinate-systems/latitude-longitude-earth.svg` |
| 4 | `earth-geoid-ellipsoid.png` | Diagrama rasteritzat en castellà, sense autor, font ni llicència | No reutilitzar | Tall propi i simplificat de superfície terrestre, geoide i el·lipsoide, amb separacions explícitament exagerades |
| 4 | `ellipsoid-definition.png` | Escaneig probable d'un llibre en castellà, sense obra, pàgina ni llicència | No reutilitzar | Esquema vectorial propi amb semieix major `a`, semieix menor `b`, equador, pols i eix de rotació |
| 4 | `ellipsoids.png` | Diagrama rasteritzat en castellà, sense autor, obra, pàgina ni llicència | No reutilitzar | Substituït per `assets/img/coordinate-systems/ellipsoid-local-fit.svg`, esquema propi d'ajust local i global d'el·lipsoides |
| 4 | `datum-distortions.png` | Fragment d'un mapa imprès sense llegenda, autoria ni context suficient per interpretar les zones numerades | No reutilitzar | Comparació reproduïble d'una mateixa posició o capa en ED50 / UTM 31N i ETRS89 / UTM 31N |

La llicència GPL del repositori antic no demostra que els recursos externs incorporats a les diapositives fossin GPL. Per tant, no s'utilitza com a prova de permís sobre les imatges individuals.

## Recursos oberts verificats

| Concepte | Recurs | Autoria i llicència | Valor didàctic | Decisió |
| --- | --- | --- | --- | --- |
| Latitud i longitud | [Latitude and Longitude of the Earth](https://commons.wikimedia.org/wiki/File:Latitude_and_Longitude_of_the_Earth.svg) | Djexplo; obra pròpia; CC0 1.0 | Separa paral·lels, meridians i els dos angles en un SVG clar | Incorporada al capítol 4; es conserva l'autoria al peu encara que CC0 no l'exigeixi |
| Semieixos d'una el·lipse | [Ellipse semi-major and minor axes](https://commons.wikimedia.org/wiki/File:Ellipse_semi-major_and_minor_axes.svg) | M. W. Toews; obra pròpia; CC0 1.0 | Explica `a` i `b` sense dependència lingüística | Incorporada al capítol 4 amb els focus retirats i etiquetes en català; ara forma part del panell `b` de la figura composta sobre geoide i el·lipsoide |
| Altures i geoide | [Altitudes](https://commons.wikimedia.org/wiki/File:Altitudes.svg) | Javiersanp; obra pròpia; CC BY-SA 4.0 i llicències compatibles | Relaciona altura el·lipsoidal, altura ortomètrica i ondulació del geoide | Incorporada al capítol 4 sense modificacions; es conserva autoria i llicència al peu |
| Visualització global del geoide | [The Geoid](https://svs.gsfc.nasa.gov/5660) | NASA Scientific Visualization Studio; visualització de Mark SubbaRao, NASA/GSFC, basada en GOCO06s | Mostra que el geoide és una superfície gravimètrica i que les variacions s'han d'exagerar per fer-se visibles | Incorporada al capítol 4 com a panell `a` de la figura composta sobre geoide i el·lipsoide; el text avisa de l'exageració 10.000x |
| Xarxa geogràfica i UTM | [Utm-latlon grid en](https://commons.wikimedia.org/wiki/File:Utm-latlon_grid_en.svg) | Javiersanp; obra pròpia; CC BY-SA 3.0 | Compara una retícula angular amb una quadrícula mètrica | No inserir: representa la zona 28N i no es pot convertir en zona 31N canviant només les etiquetes |
| Zones UTM mundials | [Universal Transverse Mercator zones](https://commons.wikimedia.org/wiki/File:Universal_Transverse_Mercator_zones.svg) | cmglee, STyx, Wikialine i Goran tek-en; CC BY-SA 4.0 | Mostra les zones i les excepcions globals | No inserir: la combinació de zones, bandes i excepcions és excessiva per al propòsit del capítol; cal una figura pròpia centrada en 31N |
| Distorsió conforme | [Mercator with Tissot's Indicatrices of Distortion](https://commons.wikimedia.org/wiki/File:Mercator_with_Tissot%27s_Indicatrices_of_Distortion.svg) | Justin Kunimune; obra pròpia amb costa de Natural Earth; CC BY-SA 4.0 | Fa visible l'augment d'àrea cap als pols i la conservació local dels angles | Incorporada sense modificacions al capítol 4 com a panell `a` d'una comparació `a+b` amb Mollweide |
| Distorsió equivalent | [Mollweide with Tissot's Indicatrices of Distortion](https://commons.wikimedia.org/wiki/File:Mollweide_with_Tissot%27s_Indicatrices_of_Distortion.svg) | Justin Kunimune; obra pròpia amb costa de Natural Earth; CC BY-SA 4.0 | Manté l'àrea de les indicatrius i en mostra el canvi de forma | Incorporada sense modificacions al capítol 4 com a panell `b` d'una comparació `a+b` amb Mercator; es conserva la proposta de regenerar la parella més endavant |

Les adaptacions de recursos `CC BY-SA` han d'indicar autoria, llicència i canvis, i s'han de distribuir sota la mateixa llicència. Per reduir barreges de llicències i ajustar les figures al Tarragonès, es prefereixen figures pròpies quan l'alternativa oberta exigeix una adaptació substancial.

## Fonts conceptuals localitzades a Calibre

Els PDF s'utilitzen per estudiar conceptes, localitzar figures canòniques i citar les obres. No se n'extreuen ni se'n tracen les il·lustracions editorials.

| Concepte | Obra i localitzador | Ús previst |
| --- | --- | --- |
| Variables visuals | Jacques Bertin, *Semiology of Graphics*, part I, secció II.C, p. 60–97; taula de propietats a la p. 97 | Fonamentar una matriu pròpia que diferenciï forma, orientació, textura, valor, color i mida sense reproduir la composició de Bertin |
| Variables visuals en SIG | Longley et al., *Geographic Information Science and Systems*, cap. 11, p. 247–251 | Contrastar quines variables són adequades per a punts, línies, àrees i tipus d'atribut |
| Latitud i longitud | Jan Van Sickle, *Basic GIS Coordinates*, 3a ed., cap. 1, p. 11–21 | Revisar la construcció angular i diferenciar latitud geodèsica i geocèntrica quan sigui necessari |
| El·lipsoide i dàtum | Van Sickle, cap. 2, p. 43–65 | Fonamentar la seqüència el·lipsoide, dàtum o marc i coordenades |
| Geoide i altures | Van Sickle, cap. 3, p. 90–104, especialment les figures 3.6, 3.7 i 3.9 | Dissenyar un tall propi que diferenciï superfície, geoide i el·lipsoide i avisi que les separacions no són a escala |
| UTM | Van Sickle, cap. 4, p. 140–145; Longley et al., cap. 4, p. 92–93 | Dissenyar una zona 31N pròpia amb meridià central, fals est, est i nord en metres i límits d'ús |
| Distorsió de projeccions | John R. Jensen i Ryan R. Jensen, *Introductory Geographic Information Systems*, cap. 2, p. 33–48 | Generar indicatrius pròpies en projeccions diferents en lloc de copiar les làmines editorials |
| Generalització | Longley et al., cap. 3, p. 71–75; Mark Monmonier, *How to Lie with Maps*, cap. 3, p. 25–45 | Produir una comparació pròpia del Tarragonès a diverses escales i amb operacions controlades |
| Classificació i color | Jensen i Jensen, cap. 10, p. 306–313; Longley et al., cap. 11, p. 251–254; Monmonier, cap. 5, p. 60–71 | Comparar classificacions i paletes amb les mateixes dades municipals, canviant una sola decisió a cada sèrie |

Rutes locals principals:

- `/home/benizar/MEGA/books/quanti/Jacques Bertin/Semiology of Graphics_ Diagrams, Networks, Maps (5)/Semiology of Graphics_ Diagrams, Networks, - Jacques Bertin.pdf`
- `/home/benizar/MEGA/books/gis/Jan van Sickle/Basic GIS Coordinates, Third Edition (15)/Basic GIS Coordinates, Third Edition - Jan van Sickle.pdf`
- `/home/benizar/MEGA/books/gis/Paul A. Longley/Geographic Information Science and Systems (41)/Geographic Information Science and Systems - Paul A. Longley.pdf`
- `/home/benizar/MEGA/books/gis/John R. Jensen/Introductory Geographic Information Systems (29)/Introductory Geographic Information System - John R. Jensen.pdf`
- `/home/benizar/MEGA/books/quanti/Mark Monmonier/How to Lie With Maps, Third Edition (6)/How to Lie With Maps, Third Edition - Mark Monmonier.epub`

## Recursos de *Fundamentals of Data Visualization*

El manuscrit complet publicat per Claus O. Wilke a [clauswilke.com/dataviz](https://clauswilke.com/dataviz/) declara una llicència [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). El fitxer `LICENSE` del repositori [clauswilke/dataviz](https://github.com/clauswilke/dataviz) conserva, en canvi, la declaració anterior CC BY-NC-ND 3.0 US i no separa el codi R amb una llicència de programari permissiva. L'accés públic al codi permet estudiar com s'han construït les figures, però no autoritza a tractar-lo com si fos MIT, BSD o GPL.

Per al manual s'aplicaran tres vies:

1. les figures seleccionades es poden reproduir íntegres, sense traduir-ne etiquetes, retallar-les, anotar-les ni recombinar-les, amb autoria, títol, font i llicència, sempre que el manual mantingui l'ús no comercial;
2. el codi es pot consultar per verificar dades, escales, llavors aleatòries i decisions gràfiques, però no es modificarà per produir una adaptació publicada mentre la clàusula `ND` sigui aplicable;
3. els principis generals es poden explicar i aplicar a figures pròpies, amb dades del Tarragonès i una implementació independent, citant Wilke com a referència conceptual sense presentar el resultat com una adaptació de la seva figura.

| Capítol de Wilke | Recurs docent | Ús previst a TIGIT | Via |
| --- | --- | --- | --- |
| 17 | Figures 17.1 i 17.2, eix truncat i origen zero | Comparar la mateixa dada i introduir la proporcionalitat de tinta al capítol 3 | Originals sense modificar, agrupats com a subfigures `a+b` |
| 26 | Figura 26.1, sector circular des de quatre angles | Mostrar com la perspectiva 3D altera l'àrea aparent sense afegir dades | Original sense modificar, incorporat |
| 18 | Superposició, transparència, desplaçament i agregació bidimensional | Revisar el diagrama de dispersió municipal i documentar qualsevol desplaçament | Figura pròpia amb dades del projecte |
| 19 | Excés de categories, rampes no monotòniques i simulació de visió cromàtica | Comparar una rampa arc de Sant Martí amb una seqüencial al capítol 7 | Figura pròpia amb mapa del Tarragonès |
| 20 | Codificació redundant i etiquetatge directe | Fer llegibles categories i sèries sense dependre només del color | Figura pròpia amb dades del projecte |
| 15 | Projeccions, capes, coropletes i cartogrames | Connectar àrea visual, normalització i unitats territorials | Referència conceptual; figures cartogràfiques pròpies |
| 21 i 23 | Petits múltiples i equilibri entre dades i context | Construir comparacions controlades de classificacions i paletes | Figura pròpia amb composició constant |
| 27 i 28 | Formats, reproductibilitat i separació entre contingut i disseny | Reforçar el flux PDF/SVG, PNG i Inkscape del capítol 3 | Referència conceptual i demostració pròpia |

Els fitxers incorporats conserven la imatge publicada per l'autor; el redimensionament al navegador és només una modificació tècnica de presentació. El registre d'origen és:

| Fitxer local | Figura original | URL d'origen | Autor i llicència |
| --- | --- | --- | --- |
| `assets/img/data-visualization/wilke-proportional-ink-truncated-axis.png` | 17.1 | `https://clauswilke.com/dataviz/proportional_ink_files/figure-html/hawaii-income-bars-bad-1.png` | Claus O. Wilke, CC BY-NC-ND 4.0 |
| `assets/img/data-visualization/wilke-proportional-ink-zero-axis.png` | 17.2 | `https://clauswilke.com/dataviz/proportional_ink_files/figure-html/hawaii-income-bars-good-1.png` | Claus O. Wilke, CC BY-NC-ND 4.0 |
| `assets/img/data-visualization/wilke-rotated-pie-3d.png` | 26.1 | `https://clauswilke.com/dataviz/no_3d_files/figure-html/rotated-pie-1.png` | Claus O. Wilke, CC BY-NC-ND 4.0 |

## Programa de figures pròpies

| Prioritat | Capítol | Figura | Contingut mínim | Producció prevista |
| --- | --- | --- | --- | --- |
| 1 | 3 | Matriu de variables visuals | Marques puntuals, lineals i superficials; posició, longitud, mida, forma, orientació, textura, valor i to; tasques de distingir, ordenar i quantificar | SVG o chunk reproduïble; exemples gràfics originals i citació de Bertin, Longley i Wilke |
| 2 | 4 | Superfície, geoide i el·lipsoide | Tres superfícies diferenciades, relació conceptual i advertiment d'exageració | Incorporada parcialment com a subfigures `a+b/c`: geoide GOCO06s documentat, semieixos de l'el·lipsoide i esquema propi `ellipsoid-local-fit.svg` d'ajust local/global |
| 3 | 4 | Coordenades geogràfiques i UTM 31N | El mateix punt del Tarragonès en graus i en metres; zona 31N, meridià central de 3° E, fals est de 500.000 m, eixos E/N i `EPSG:25831` | Incorporada com a subfigures pròpies `a+b`; tres posicions OSM transformades amb PROJ 9.4.0 i contrastades amb la definició EPSG |
| 4 | 4 | Assignar i reprojeccionar | Nombres que no canvien en assignar i coordenades que sí que canvien en reprojeccionar | Diagrama propi combinat amb una comprovació reproduïble |
| 5 | 4 | Distorsió cartogràfica | Indicatrius idèntiques sobre una projecció conforme i una d'equivalent, amb dades i estil constants | R o Python; mateixa costa, retícula, posicions i dimensions a tots els panells |
| 6 | 4 | Desplaçament ED50–ETRS89 | Mateixa entitat representada correctament i mal interpretada; CRS d'origen, transformació i magnitud del desplaçament | QGIS o Python amb PROJ i dades obertes de Catalunya |
| 7 | 6 | Escala i generalització | Mateix territori a escala provincial, comarcal i local; detall i retolació adequats a cada mida | QGIS o Python a mida final constant |
| 8 | 6 | Retolació abans i després | Configuració automàtica i versió revisada amb prioritats i conflictes resolts | QGIS; mateixa extensió, mida i geometria |
| 9 | 7 | Paletes segons la dada | Qualitativa, seqüencial i divergent sobre mostres comparables i accessibles | R o Python; colors registrats en HEX i comprovacions de grisos i visió cromàtica |
| 10 | 7 | Classificacions comparades | Mateix indicador del Tarragonès amb intervals iguals, quantils i Jenks; punts de tall i freqüències visibles | R, Python o QGIS amb dades del projecte i una paleta constant |
| 11 | 7 | Coropleta i símbols proporcionals | Percentatge municipal en coropleta i recompte absolut amb símbols proporcionals | QGIS o codi; mateixa geometria i font estadística |
| 12 | 8 | Síntesi territorial | Mapa, gràfic, interpretació, fonts i crèdits integrats en una pàgina amb jerarquia | Inkscape a partir de resultats vectorials reproduïbles |
| 13 | 3 | Superposició en un diagrama municipal | Mateixes observacions sense tractament, amb transparència i, només si cal, amb un desplaçament mínim declarat | Chunk reproduïble amb llavor fixa i dades del projecte; citació conceptual de Wilke |
| 14 | 7 | Rampa no monotònica i rampa seqüencial | Mateix indicador, classificació, geometria i mida; només canvia la rampa, amb una còpia en grisos | QGIS o chunk reproduïble; colors i transformació a grisos registrats |
| 15 | 3 o 7 | Codificació redundant | Categories representades només per color i després per color més forma, patró o etiqueta directa | Figura pròpia reproduïble; comprovació en grisos i simulació cromàtica |

Per a la figura UTM, la referència normativa principal serà [ETRS89 / UTM zone 31N, EPSG:25831](https://epsg.org/crs_25831/ETRS89-UTM-zone-31N.html): sistema cartesià en metres amb eixos est i nord, extensió europea entre 0° E i 6° E i conversió UTM 31N. Els paràmetres de la conversió es verificaran de nou quan es generi la figura.

La figura UTM publicada consta de `assets/img/coordinate-systems/utm-zone-31n.svg` i `assets/img/coordinate-systems/utm-grid-vila-seca.svg`. Les longituds i latituds de la Facultat de Turisme i Geografia, el Castell de Vila-seca i la Torre d'en Dolça provenen de Nominatim/OpenStreetMap, consultat el 12 d'agost de 2026, sota ODbL. Les conversions d'`EPSG:4326` a `EPSG:25831` s'han executat amb `cs2cs` de PROJ 9.4.0 i arrodonit al metre. Els esquemes són docents: el primer no és un mapa a escala i el segon simplifica el context territorial per explicar la lectura de la quadrícula.

## Figures pròpies del capítol 1

| Recurs | Estat | Funció docent | Seguiment |
| --- | --- | --- | --- |
| `assets/img/data-sources/kdd-dikw-cycle.svg` | Incorporada | Relacionar reptes territorials, observacions, dades, informació, anàlisi, coneixement i saviesa pràctica com una escala ascendent, amb les fases del KDD com a accions sobre les fletxes i un retorn inferior cap a noves observacions | SVG propi editable manualment, basat en Fayyad et al. i la discussió DIKW de Rowley; mantenir textos i formes editables en Inkscape |
| `assets/diagrams/data-source-levels.mmd` | Incorporada | Separar pregunta, catàleg, conjunt, distribució, servei, capa i petició abans de parlar d'API, INSPIRE o OGC | Figura conceptual pròpia; regenerar l'SVG si canvia el diagrama |
| `assets/diagrams/data-access-modes.mmd` | Incorporada | Separar dades pròpies, dades publicades formalment i informació visible o documental, i després distingir interfície, fitxer, API, geoservei, extracció web i extracció documental supervisades | Figura conceptual pròpia regenerada el 13 d'agost de 2026; revisar visualment que el nivell de detall sigui llegible |
| `assets/img/data-sources/spreadsheet-parts.svg` | Incorporada | Identificar barra de fórmules, capçaleres, files, cel·la activa, referències i rang rectangular sense dependre d'una interfície concreta | Esquema propi provisionalment suficient; es pot substituir o complementar amb captura Calc/Excel quan existeixi el llibre del curs |
| `assets/img/data-sources/spreadsheet-sum-formula.svg` | Incorporada | Mostrar una fórmula elemental que suma dues cel·les i separar valor mostrat de regla de càlcul | Esquema propi; mantenir-lo encara que més endavant s'afegeixi una captura real perquè és més estable que una interfície |
| `assets/img/data-sources/rectangular-table.svg` | Incorporada | Explicar forma rectangular, una capçalera, una fila per observació i separació de metadades, diccionari i resultats | Esquema propi; revisar visualment a web i PDF |
| `assets/img/data-sources/world-bank-data-2026-08-13.png` | Captura documentada | Mostrar un portal global amb cercador, perfils temàtics i indicadors comparables | Captura pròpia del portal World Bank Open Data, 13 d'agost de 2026; conté bàner de cookies inferior visible i no s'ha retallat |
| `assets/img/data-sources/gisco-geodata-2026-08-13.png` | Captura documentada | Mostrar una font europea de geodades harmonitzades i la necessitat de llegir metadades i condicions | Captura pròpia de GISCO Geodata, 13 d'agost de 2026; conté avís de cookies inferior visible i no s'ha retallat |
| `assets/img/data-sources/inebase-2026-08-13.png` | Captura documentada | Mostrar una entrada estatal a operacions estadístiques oficials per categories temàtiques | Captura pròpia d'INEbase, 13 d'agost de 2026; sense dades personals ni anotacions |
| `assets/img/data-sources/cnig-downloads-2026-08-13.png` | Captura documentada | Mostrar un catàleg estatal de productes geogràfics de referència | Captura pròpia del Centro de Descargas del CNIG, 13 d'agost de 2026; sense dades personals ni anotacions |
| `assets/img/data-sources/generalitat-open-data-tourism-register-2026-08-13.png` | Captura documentada | Mostrar una fitxa catalana de registre administratiu amb productor, actualització i exportació | Captura pròpia de Dades Obertes de la Generalitat, 13 d'agost de 2026; sense dades personals ni anotacions |
| `assets/img/data-sources/mercuri-dipta-2026-08-13.png` | Captura documentada | Mostrar un sistema supramunicipal de síntesi amb dades municipals, indicadors, mapes, gràfics i informes | Captura pròpia de Mercuri, Diputació de Tarragona, 13 d'agost de 2026; sense dades personals ni anotacions |
| Captura d'importació d'un CSV d'Idescat en Calc o Excel | Proposada | Mostrar codificació UTF-8, delimitador `;`, codi municipal com a text i comprovació de decimals abans d'obrir el fitxer | Produir-la quan existeixi el llibre docent `territorial_context_tarragones.xlsx`; no usar dades personals ni rutes locals visibles |
| Captura o subfigura del full `sources` i del full `dictionary` | Proposada | Fer visible que procedència i diccionari són part del resultat, no burocràcia externa | Ajornar fins que el model de llibre estigui estabilitzat; valorar subfigures `a+b` si la comparació ajuda a distingir font i variable |
| Captures de Reus Open Data i TGN Dades | Proposada | Aprofundir en recursos locals i mostrar la diferència entre observatori, portal de dades, quadre de comandament i conjunt descarregable | La captura de Reus Open Data del 13 d'agost de 2026 va retornar timeout i no s'ha incorporat; la captura de TGN Dades va quedar parcialment tapada per un avís de cookies i s'ha descartat |

## Captures web

Una captura només es farà quan calgui analitzar una interfície, un quadre de comandament o una resposta concreta del servei. Per explicar geoide, coordenades, UTM o projeccions és preferible una figura estable i reproduïble a una captura d'una pàgina web.

Cada captura conservarà:

1. URL exacta i títol del recurs;
2. productor, data de consulta i, si consta, versió;
3. llicència o condicions d'ús aplicables;
4. descripció de la selecció, els filtres i l'estat de la interfície;
5. text alternatiu i peu que expliquin què s'ha de llegir;
6. fitxer original sense anotacions i, si escau, una còpia anotada identificada com a adaptació.

No es farà una captura quan un enllaç textual, una taula pròpia o una figura reproduïble comuniquin la mateixa relació amb més claredat i menys dependència temporal.

### GITTA Map Projector

La captura `assets/img/coordinate-systems/gitta-map-projector-mercator-advanced-2026-08-12.png` documenta el mode **Advanced** de l'original [GITTA Map Projector](https://gevian.github.io/GITTA-MP/) i no un *fork*. S'ha obert **The Mercator Projection**, construït **Central Cylindrical Projection**, activat **flatten**, aplicat **Scale Central Cylindrical to Mercator** i mantingut actives les fronteres, la retícula i les indicatrius de Tissot. La càmera s'ha orientat frontalment mitjançant DevTools sense alterar els paràmetres de la projecció.

La captura es va fer el 12 d'agost de 2026 amb Chromium, finestra de 1.920 × 1.080 px i escala 1. El fitxer publicat s'ha retallat a 1.520 × 865 px per eliminar el buit lateral i inferior sense ocultar el títol, els controls, el tutorial, l'autoria ni la llicència visibles. El recurs és de Magnus Heitzler, Institute of Cartography and Geoinformation, ETH Zürich, 2019, i el repositori `gevian/GITTA-MP` declara GPL v3. La funció docent és relacionar superfície, aplanament, escalat i indicatrius, no substituir la interacció amb l'aplicació.

### The True Size Of

La captura `assets/img/coordinate-systems/the-true-size-greenland-mercator-2026-08-13.png` documenta el recurs [*The True Size Of…*](https://thetruesize.com/) com a eina interactiva per observar la distorsió de Mercator. S'ha cercat **Greenland** i s'ha mantingut el contorn seleccionat sobre el mapa, amb la barra lateral, el nom del territori, la superfície, la població i els crèdits visibles. La captura no substitueix l'activitat interactiva: el text del capítol demana arrossegar el contorn cap a altres latituds i contrastar la lectura amb dades d'àrea.

La captura es va fer el 13 d'agost de 2026 amb Chromium, finestra de 1.400 × 900 px i escala 1, sense retall ni anotacions posteriors. El recurs és de James Talmage i Damon Maneice; la interfície mostra avís © 2026 The True Size i mapa base de Google. Com que no consta una llicència oberta per a la interfície, la captura es manté com a fragment documentat per a comentari docent i conserva els crèdits visibles. Si en el futur cal una figura amb reutilització oberta plena, s'haurà de produir una comparació pròpia amb dades d'àrea i una projecció controlada.

### Fotografia aèria i fototeques

Les dues captures incorporades al capítol 6 tenen funcions diferents. La primera documenta com es consulta un tema conceptual i la seva citació estable; la segona registra una operació territorial que només es pot entendre veient simultàniament la interfície, el fotograma, l'ortofoto de fons i la cronologia de vols.

| Camp | GIS&T Body of Knowledge | Fototeca Digital del CNIG |
| --- | --- | --- |
| Fitxer | `assets/img/aerial-photography/gistbok-aerial-photography-2026-08-12.png` | Captura completa conservada a `assets/img/aerial-photography/fototeca-cnig-vila-seca-1956-1957-2026-08-12.png`; comparació publicada com a subfigures `fototeca-cnig-vila-seca-fotograma-1956-1957.png` i `fototeca-cnig-vila-seca-ortofoto-2026-08-12.png` |
| Títol i URL | *Aerial Photography: History and Georeferencing*, `https://gistbok-ltb.ucgis.org/current/concept/DC-02-010`; DOI `10.22224/gistbok/2019.2.5` | *Fototeca Digital*, `https://fototeca.cnig.es/` |
| Responsable | UCGIS; tema de Paul Baumann, 2019 | IGN/CNIG; fotograma del vol Americà B cedit pel Ministeri de Defensa (CEGET) |
| Data | Consulta i captura: 12 d'agost de 2026; tema de 2019 dins de l'edició mestra de 15 d'abril de 2026 | Consulta i captura: 12 d'agost de 2026; vol de 1956–1957 |
| Estat | Vista directa sense mapa de coneixement: títol, etiquetes, autoria, DOI, índex i definicions inicials | Vila-seca, Salou i Tarragona; base d'imatge; pestanya **Fotogrames**; vol **1956–1957 Americà B**; fotograma `PNOA-H_AMS_1956-57_33k_ES_comp_PAN_21mic_etrs89_UTM-hu31_H50_0472_fot_16089`; opacitat 100% al panell `a` i fotograma ocult al panell `b` |
| Captura | Chromium en mode headless, viewport de 1.440 × 1.000 px i escala 1; sense retall ni anotacions | Chromium controlat mitjançant DevTools, viewport de 1.440 × 1.000 px i escala 1; els dos panells comparteixen un retall de 970 × 716 px i no contenen anotacions |
| Funció docent | Mostrar la localització actual del tema, la citació estable i les operacions de consulta disponibles sense reproduir-ne les figures | Mostrar la selecció temporal, els fotocentres, un fotograma històric i la diferència visible respecte de l'ortofoto disponible com a fons |
| Condicions | El programari Living Textbook declara CC BY-NC-ND 4.0; el contingut pertany a UCGIS i als autors. Fragment limitat de la interfície reproduït per a comentari docent | El WMS de la Fototeca i la capa Americà B declaren CC BY 4.0; s'han de mantenir l'atribució al productor i a IGN/CNIG |
| Modificacions | Cap | Cap; la consulta i la selecció del fotograma són pròpies |

La captura de la Fototeca no substitueix el fotograma descarregable ni les metadades. Si es produeix una comparació analítica posterior, es conservaran els fitxers d'origen, els paràmetres de georeferenciació i la llicència, i es construirà una figura independent de la interfície.

La comparació es publica amb `::: subfigures a+b` perquè els dos panells responen a una sola pregunta i comparteixen extensió, mida i estat del visor. No s'agruparan com a subfigures captures que només tractin el mateix tema però exigeixin lectures independents. La composició web és l'objectiu principal; caldrà revisar el resultat del PDF perquè la disposició de subfigures encara no hi és equivalent.

### Street View temporal

No es publicaran captures fixes de Google Street View. Les [directrius geogràfiques de Google](https://about.google/brand-resource-center/products-and-services/geo-guidelines/) prohibeixen expressament les captures de Street View en webs i l'ús d'aquestes imatges en llibres, manuals, revistes i altres suports impresos; també en prohibeixen la descàrrega separada, la digitalització i l'anàlisi automatitzada. Aquesta restricció s'aplica també als projectes acadèmics i no queda resolta mantenint només l'atribució.

El capítol 6 enllaça un panorama viu de Vila-seca i explica com utilitzar **Mostra més dates** dins de Google Maps. L'activitat conservarà fora de les imatges la localització, les dates seleccionades, l'orientació aproximada i una llista breu d'observacions. No es desaran ni es lliuraran captures de Street View. Si cal una evidència visual publicable, s'utilitzaran fotografies pròpies repetides des del mateix punt o un arxiu amb una llicència compatible.

### Data Visualization Reference Guides

La captura `assets/img/data-visualization/cool-infographics-dataviz-guides-2026-08-12.png` presenta el directori [Data Visualization Reference Guides](https://coolinfographics.com/dataviz-guides) com a objecte docent: permet observar que la selecció d'una visualització es pot abordar mitjançant principis, catàlegs, classificacions, arbres de decisió i llistes de comprovació. El directori forma part del lloc que acompanya i promociona el llibre de Randy Krum *Cool Infographics: Effective Communication with Data Visualization and Design* (Wiley, 2013), però conté recursos posteriors i obres de molts productors. Per això no s'utilitza com a font d'una única taxonomia, com a substitut dels recursos primaris ni com si totes les miniatures fossin figures del llibre.

| Camp | Registre |
| --- | --- |
| Títol i URL | *Data Visualization Reference Guides*, `https://coolinfographics.com/dataviz-guides` |
| Responsable | Cool Infographics; directori curat per Randy Krum; avís del lloc © 2023 Randy Krum, InfoNewt LLC |
| Data | Consulta i captura: 12 d'agost de 2026; les metadades del lloc indiquen una modificació el 12 de febrer de 2026 |
| Estat | Capçalera i primers tres recursos: *Core Principles of Data Visualization*, *The Data Visualisation Catalogue* i *Visualizing Percentages & Parts of a Whole* |
| Captura | Chromium en mode headless, viewport de 1.440 × 1.400 px i escala 1; captura del viewport, sense retall posterior |
| Interacció | S'ha tancat el bàner de cookies abans de capturar; no s'han aplicat filtres, zoom, anotacions ni modificacions al contingut |
| Condicions | No consta una llicència oberta per a la pàgina; fragment limitat reproduït per a comentari i docència. Les miniatures pertanyen als creadors i titulars dels recursos enllaçats |
| Peu | Ha d'identificar el títol, Randy Krum, URL, data de captura, finalitat docent i titularitat separada de les miniatures |

Els principis del manual es redacten de manera independent i citen les fonts primàries. No es tradueixen ni es reprodueixen els pòsters complets. Les classificacions s'utilitzen per construir un procés propi basat en pregunta, estructura de dades, tasca de lectura, context territorial, públic, suport i comparació d'alternatives.

## Captures d'aplicacions

Les captures de QGIS, LibreOffice Calc, Microsoft Excel i Inkscape han de mostrar una decisió que l'estudiant necessita localitzar a la interfície. No substituiran els gràfics, els mapes ni els documents exportats, que s'han de publicar com a peces vectorials independents. Es capturaran amb dades de demostració del Tarragonès, sense noms d'usuari, rutes personals, historials recents, notificacions ni altres dades alienes a l'activitat.

| Prioritat | Capítol | Aplicació i captura | Lectura que ha de permetre | Estat i retall previstos |
| --- | --- | --- | --- | --- |
| 1 | 4 | QGIS: propietats d'una capa, apartat d'informació | Localitzar CRS, unitats, extensió, geometria i nombre d'entitats abans d'operar | Capa municipal carregada; retall del panell i una franja del llenç que identifiqui la capa |
| 2 | 4 | QGIS: selector de CRS amb `EPSG:25831` | Distingir nom, codi, àrea d'ús i eixos d'un resultat de cerca | Cerca exacta i resultat seleccionat, sense validar encara el diàleg |
| 3 | 5 | LibreOffice Calc: full `map_export` | Reconèixer una taula plana amb capçalera única, codi textual i camps numèrics | Files inicials i barra de fórmules; codis amb zeros inicials visibles |
| 4 | 5 | QGIS: importació de text delimitat | Comprovar codificació, delimitador, decimal, tipus de camps i vista prèvia abans de carregar el CSV | Diàleg complet amb `mun_code` com a text i indicadors numèrics; anotacions numerades en una còpia derivada |
| 5 | 5 | QGIS: propietats de la unió i taula d'atributs | Relacionar camps de clau, camps units i nuls amb el recompte de coincidències | Comparació en dos panells: configuració de la unió i mostra de tres municipis contrastats |
| 6 | 3 | Calc i Excel: gràfic automàtic i gràfic revisat | Identificar ordre, eix, títol, unitat, font i soroll visual sense confondre una interfície amb el lliurable | Mateixa taula i mida als dos programes; només es duplicarà la captura si una diferència d'interfície és docentment rellevant |
| 7 | 6 | QGIS: disseny d'impressió | Localitzar pàgina, marc de mapa, escala, guies i elements auxiliars abans d'exportar | Composició del mapa de context amb panells laterals mínims i guies visibles |
| 8 | 7 | QGIS: simbologia graduada | Relacionar camp, mètode, nombre de classes, punts de tall, rampa i tractament dels nuls | Mateix indicador en dues captures controlades: canvia només la classificació o només la paleta |
| 9 | 8 | Inkscape: propietats del document i guies | Comprovar mida, orientació, marges, columnes i unitats abans de maquetar | Pàgina sencera amb esquema de blocs i panell de propietats obert |
| 10 | 8 | Inkscape: panell de capes i objectes | Distingir fons, mapes, gràfics, textos i crèdits, i comprovar que les peces importades continuen agrupades | Miniinfografia intermèdia amb noms de capes semàntics i sense dades personals |
| 11 | 8 | Inkscape: inspecció d'un PDF o SVG importat | Verificar que textos, línies i formes són objectes vectorials i que la proporció queda bloquejada | Zoom elevat amb un objecte seleccionat; una segona mostra ràster servirà de contraexemple si és necessària |

Cada sèrie conservarà la versió sense anotacions i una còpia docent anotada. El registre indicarà aplicació i versió, sistema operatiu, idioma de la interfície, data de captura, fitxer o projecte d'origen, dimensions, retall aplicat i modificacions. Les anotacions s'afegiran després de capturar, amb numeració i contrast suficients; no es dibuixaran fletxes a mà sobre l'única còpia disponible.

Les captures de Microsoft Excel o Microsoft 365 s'utilitzaran només quan expliquin una operació institucional o una diferència real respecte de Calc. Per als procediments estables es prioritzarà una captura de Calc i una explicació independent de menús concrets, de manera que una actualització de la interfície no obligui a reconstruir tot el capítol.
