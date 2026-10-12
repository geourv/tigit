# Pla del recorregut pràctic acumulatiu

## Direcció docent i estat de preparació

Direcció de l'autor registrada el 9 d'octubre de 2026, en la coordinació gaContExt #32 i la tasca TIGIT #12. La part pràctica ha de permetre analitzar un municipi i la seva comarca amb dades preparades d'Idescat i ICGC. Ha de tenir entitat pròpia després de la teoria i culminar en una infografia SVG que reutilitzi mapes i gràfics. La microactivitat `tigit-unio-municipal` només és una prova tècnica del circuit de producció.

Aquest document és context de planificació, no una lectura publicable ni un certificat d'execució. Les lectures catalanes es preparen a `_practices/tigit-projecte-territorial/readings/ca/LLEGIU-ME-estudiant.md` i `LLEGIU-ME-professorat.md`, amb `content_status: draft`. El seu mapping al circuit comú de PDF i ZIP s'ha de validar amb la interfície que lliuri el coordinador; aquí no es defineix un descriptor GIS alternatiu.

L'assignatura és Tècniques d'informació geogràfica i turística, de la Universitat Rovira i Virgili. El codi `21224102` correspon al Grau en Gestió en Turisme i Hoteleria; el manual també conserva el codi `21234003` de Geografia. La llengua de treball és el català. La [guia docent oficial de Turisme 2026/2027](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&any_academic=2026_27) s'ha contrastat durant l'intake. No s'afegeixen calendaris ni criteris d'avaluació nous.

## Criteri territorial

- Cas de demostració del professorat: els 22 municipis del Tarragonès.
- Municipi de control i detall de la demostració: Vila-seca, codi `431711`.
- Cada equip treballa el parell comarca–municipi assignat. El cas docent no és automàticament el seu territori de treball; fora del Tarragonès cal preparar i verificar les entrades equivalents.
- Període estadístic principal: població i habitatge de 2021.
- Les fonts posteriors, com centres educatius 2025/2026 o geometria ICGC 2026, s'han de presentar com a context temporal posterior, no com si fossin observacions simultànies.

## Seqüència pedagògica

La teoria manté el recorregut fonts, indicadors, gràfics, color, dades espacials, SIG, llenguatge cartogràfic, cartografia temàtica i síntesi. La part «Pràctiques» se situarà després d'aquests continguts i abans de la bibliografia. Es proposen tres capítols substancials: laboratori QGIS de projecte, dades i relacions; laboratori cartogràfic de representació i composició; i taller de síntesi territorial SVG. Els pesos `101`, `102` i `103` permeten aquesta ubicació entre la síntesi teòrica (`100`) i la bibliografia (`110`). Aquesta reorganització encara no s'ha aplicat als capítols.

Les activitats finals dels capítols 4, 5, 6, 8 i 9 alimentaran aquests laboratoris mitjançant una revisió selectiva. La teoria conservarà les explicacions conceptuals i enllaçarà els procediments; no es copiaran íntegrament en dos llocs. Caldrà revisar la frase del capítol 8 que limita el projecte als símbols proporcionals: la direcció actual incorpora els graduats i n'explica la diferència.

Els prefixos dels llibres i projectes QGIS són identificadors tècnics estables de les fites originals. Es conserven els noms i la genealogia: `tigit-07-teoria-color.xlsx` precedeix `tigit-05-integracio-sig.xlsx`, que en deriva `map_export`. Els fitxers intermedis docents de `data/processed` porten el sufix `-teaching`; els snapshots de `dist/teaching/chapter-NN` tenen el nom docent de lliurament sense aquest sufix.

## Programa de vuit pràctiques

Cada pràctica relaciona una decisió amb la teoria precedent, una operació observable i un control. El professorat de teoria explica la variable, la unitat espacial, el denominador o la decisió visual; el de laboratori comprova que l'operació a QGIS conserva aquest significat. Les lectures estudiant/docent comparteixen els vuit blocs: la primera planteja el treball i la segona aporta els valors de control i els criteris d'intervenció.

### 1. QGIS, fonts de dades i formats

- Objectiu i teoria: distingir projecte, capa i format; reprendre models vectorials, CRS i escala del capítol 4 i l'organització d'un SIG del 5.
- Entrades: GeoPackage ICGC compacte i les seves cinc subcapes. El productor generarà un Shapefile docent de la capa municipal, amb selecció documentada de camps; encara no existeix.
- Procediment: reconèixer llenç, panell de capes, navegador i barra d'estat; carregar dades amb el gestor de fonts; inspeccionar subcapes; comparar GeoPackage amb `.shp`, `.shx`, `.dbf`, `.prj` i `.cpg`; desar i reobrir amb rutes relatives.
- Producte: projecte base `qgis/tigit-04-dades-espacials.qgz`, amb municipi de detall i context comarcal.
- Controls: 22 municipis, claus úniques, EPSG:25831, accents i atributs conservats; equivalència entre formats i reobertura en una ubicació diferent.
- Captures reals: espai de treball, gestor de fonts/subcapes i propietats de geometria/CRS. La lectura docent explicarà la pèrdua potencial de noms de camp, precisió i codificació en canviar de format.

### 2. Atributs, unió d'Idescat i comparació territorial

- Objectiu i teoria: relacionar entitat, fila, camp, tipus i clau; recuperar preparació de dades del capítol 1, denominadors del 2 i unions del 5.
- Entrades: `municipalities_250k`, CSV/CSVT d'indicadors i llibre acumulatiu amb `map_export`.
- Procediment: inspeccionar i consultar la taula; carregar el CSV sense geometria; comprovar unicitat i compatibilitat temporal; unir `CODIMUNI` amb `mun_code`; consultar un municipi i un llindar; contrastar el municipi amb l'agregat comarcal calculat amb sumes.
- Productes: `qgis/tigit-05-integracio-sig.qgz`, resultat materialitzat quan calgui compartir-lo, i informe d'unió. La unió del projecte i la materialització es comproven per separat.
- Controls: 22 coincidències, cap duplicat, cap clau sobrant; consulta de Vila-seca i sis codis amb habitatge no principal superior al 50%. Els percentatges comarcals són ràtios de sumes, no mitjanes municipals.
- Captures reals: taula/camps, configuració d'unió i consulta amb recompte. La lectura docent inclou els tres casos de control del registre numèric següent.
- Exercici auxiliar ja previst: importar els 17 centres de Vila-seca amb UTM i longitud/latitud; comprovar-ne la coincidència amb una tolerància justificada per la precisió de les coordenades. Els 183 centres del Tarragonès són l'ampliació. No es barregen amb els indicadors censals de 2021.

### 3. Mapa de referència i etiquetes

- Objectiu i teoria: orientar el lector i decidir què és llegible, a partir d'escala, generalització i retolació del capítol 6.
- Entrades: projecte amb unió comprovada, municipis, comarca, província, capitals i geometria municipal de detall; les 43 comarques aporten context de Catalunya.
- Procediment: diferenciar el municipi, la comarca i l'entorn; ordenar capes i gruixos; configurar etiquetes i prioritats; comparar la lectura a escala municipal i comarcal.
- Producte: base de referència de `qgis/tigit-06-llenguatge-cartografic.qgz`, reutilitzada en les composicions. Els PDF de context previstos s'exporten quan el dissenyador s'hagi revisat a la pràctica 6.
- Controls: territori destacat correcte, topònims associats sense ambigüitat, absència de col·lisions rellevants i detall compatible amb l'escala. Les capes locals no s'han de presentar com si incloguessin una xarxa de carrers.
- Captures reals: propietats d'etiquetatge i comparació d'escales. La lectura docent recull quins topònims tenen prioritat i quins ajustos requereixen criteri humà.

### 4. Coropletes i classificacions comparables

- Objectiu i teoria: representar una intensitat amb denominador justificat; recuperar semiologia del capítol 3, color del 7 i normalització/classificació del 8.
- Entrades: unió municipal, `housing_non_main_pct`, `indicator_status`, totals de control i registre `palette`.
- Procediment: validar el percentatge; configurar una paleta seqüencial; comparar dos mètodes de classificació amb nombre de classes, dades, extensió, paleta i mida constants; conservar l'alternativa editable.
- Producte: coropleta comarcal amb el municipi destacat, dins de `qgis/tigit-08-cartografia-tematica.qgz`.
- Controls: intervals sense buits ni solapaments, recomptes que sumen 22, nuls separats de zeros i percentatges sense doble normalització. No es desagrega fictíciament un valor municipal a carrers o persones.
- Captura real: simbologia amb camp, mètode i punts de tall visibles. La lectura docent compara la decisió interpretativa, no només el contrast dels colors.

### 5. Símbols graduats i proporcionals

- Objectiu i teoria: representar volum i distingir classes de mida d'una escala contínua, a partir dels capítols 3 i 8.
- Entrades: `housing_total`, geometria municipal i punts interiors derivats i comprovats pel productor.
- Procediment: construir classes de mida documentades; comparar-les amb la variant de símbols proporcionals; mantenir clara la diferència entre volum d'habitatges i percentatge no principal.
- Productes: mapa de símbols graduats i variant proporcional editable. El nom existent `simbols_habitatges_totals_tarragones_2021.svg` continua identificant la variant proporcional; el producte graduat tindrà un nom diferenciat en el descriptor comú.
- Controls: un punt per municipi, localització interior, 22 registres, classes/valors coherents amb la llegenda, solapaments revisats i àrea proporcional al valor en la variant contínua.
- Captures reals: classes de mida i assistent de proporcionalitat. La lectura docent contrastarà la lectura d'una classe amb la d'un valor exacte.

### 6. Temes i dissenyador de composicions

- Objectiu i teoria: construir una pàgina cartogràfica que orienti i compari, a partir de jerarquia/composició del capítol 6 i representacions del 8.
- Entrades: mapes de referència, coropleta, símbols i context local de província/Catalunya.
- Procediment: conservar temes amb noms semàntics; crear mapa principal i localitzador petit en la mateixa composició; assignar un tema a cada marc; fixar-ne extensió, escala i orientació per separat; afegir llegendes, fonts i escala.
- Productes: composicions editables i SVG/PDF vectorials. El tema conserva capes i estils; l'extensió i escala pertanyen a cada marc, no al tema.
- Controls: canviar el llenç no altera accidentalment els mapes de la composició; temes, marcs, estils i recursos persisteixen en reobrir; escala, llegendes i textos són llegibles a mida final.
- Captures reals: selector de temes, propietats dels dos marcs i dissenyador. La lectura docent inclou una revisió de llegibilitat i de persistència del projecte.
- Ajust d'autor acceptat: si l'acabat no es pot automatitzar, lliurar una base operativa editable amb els elements realment disponibles i un inventari d'ajustos. No simular un mapa acabat ni substituir el projecte per un ràster. Si el productor no admet temes o layouts, cal declarar aquest requisit pendent, no ampliar informalment el perfil.

### 7. Fons ICGC, Open ICGC i WFS

- Objectiu i teoria: distingir fitxer, servei d'imatge i servei d'objectes, reprenent fonts i serveis del capítol 5.
- Entrades: catàleg oficial d'Open ICGC i connexions WMS/WFS documentades a la secció de serveis. És un recorregut en línia separat del projecte base offline.
- Procediment: afegir un fons; identificar el tipus de servei; consultar capa, CRS i esquema WFS; preparar una descàrrega acotada; documentar la data i verificar el resultat local. No donar per fet que els noms de camp remots coincideixen amb els del GeoPackage conservat.
- Productes: explicació i captura de la via real suportada; una descàrrega només entra a la closure local després de ser materialitzada i comprovada pel productor.
- Controls: paginació i límits de consulta, recompte, clau, CRS, llicència i reobertura local sense xarxa. Una capa WMS amagada continua sent una dependència remota.
- Captures reals: connexió i selecció de capa, plugin si la versió fixada funciona i acció de descàrrega/exportació efectivament disponible.

### 8. Síntesi territorial en SVG

- Objectiu i teoria: sostenir una explicació amb evidències complementàries, després de la teoria d'infografia del capítol 9.
- Entrades: mapes QGIS vectorials, gràfics de les pràctiques de full de càlcul, mètriques municipals/comarcals i fonts.
- Procediment: formular pregunta, resultat i limitació; seleccionar dues o tres peces visuals en total; compondre-les en una base A3 editable; mantenir proporcions; fer una prova de lectura i registrar els ajustos.
- Productes: màster `outputs/infographics/infografia_<comarca>-<municipi>_<periode>.svg` i PDF de revisió, amb la genealogia de cada peça. Els PDF/ZIP finals segueixen el circuit comú i l'autorització de l'edició.
- Controls: valors i períodes compatibles, mapes i gràfics vectorials editables, recursos incrustats o locals, fonts disponibles, escala i símbols sense deformació i limitacions visibles.
- Base materialitzada: `_practices/tigit-projecte-territorial/templates/infografia-a3.svg`, A3 vertical, marges de 15 mm, sis columnes de 39,5 mm i separacions de 6 mm. Inclou capes de paper, títol/pregunta, mapa principal, localitzador, gràfic, lectura/limitació, fonts i guies. Els camps per emplenar no representen cap anàlisi executada. La figura `assets/img/infographics/grid-wireframe-composition.svg` es conserva com a explicació del disseny.
- Dependència separada: no hi ha eina de captures d'Inkscape en aquest circuit. Es poden preparar la font SVG i el recorregut textual, però no fabricar ni certificar captures. Aquesta manca no bloqueja els materials QGIS.

## Dades tabulars

El llibre distingeix quatre nivells:

1. `data/raw`: fitxers i respostes originals sense modificar.
2. `source_*`: estructura importada amb els camps i categories de la font.
3. `prepared_*`: camps tipats, normalitzats i documentats pel projecte.
4. `municipal`, `indicators_*` i `charts_*`: integració, càlcul i representació.

Els fulls `source_*` no reben noms de camp propis del projecte. Les transformacions han de quedar visibles en el pas cap a `prepared_*`.

## Calc i gràfics

La fita de semiologia i visualització crearà:

- `charts_data`: rangs vinculats i controls de suma;
- `chart_00_audit`: versió inicial i revisada d'un mateix gràfic;
- `chart_01_age_structure`: barres horitzontals apilades al 100%;
- `chart_02_nonprincipal`: barres horitzontals ordenades del percentatge d'habitatge no principal;
- `chart_03_scatter`: dispersió entre població de 65+ i habitatge no principal, amb Vila-seca identificada;
- `chart_04_housing_donut`: anell de composició del parc d'habitatges;
- `chart_05_population_time`: línia de població anual de Vila-seca, 2000–2022;
- `chart_06_population_pyramid`: piràmide per edat i sexe de Vila-seca, 2021;
- `chart_07_housing_histogram`: distribució municipal de l'habitatge no principal;
- `palette`: registre cromàtic que s'afegirà a la fase de color.

Les figures candidates s'exportaran en PDF/SVG vectorial. La revisió a Inkscape comprovarà objectes, textos, fonts i proporcions. La captura real del diàleg de rangs o sèries de Calc i la comprovació visual d'Inkscape són evidències diferents; la captura d'Inkscape continua com a dependència separada.

## Color

La fase de color aplicarà un color neutre a totes les barres i un accent redundant a Vila-seca; la rampa seqüencial per a la coropleta es provarà com a mostres, sense fixar encara els intervals. La prova s'exportarà en SVG i PDF abans de preparar la transferència cap a QGIS.

## Dades puntuals

### Capa XY principal

Font: Directori anual de centres docents de la Generalitat, conjunt `kvmv-ahh4`.

- API: `https://analisi.transparenciacatalunya.cat/resource/kvmv-ahh4.json`
- CSV: `https://analisi.transparenciacatalunya.cat/resource/kvmv-ahh4.csv`
- Camps útils: codi i nom del centre, titularitat, adreça, codi municipal de sis dígits, UTM X/Y, longitud/latitud i geometria.
- CRS UTM declarat: ETRS89 / UTM 31N, `EPSG:25831`.
- Subconjunt inicial: 17 centres de Vila-seca del curs 2025/2026.
- Ampliació: 183 centres del Tarragonès.

Al final de la fase de dades espacials, després d'explicar coordenades i CRS, la taula s'inspeccionarà encara en Calc o Excel: ordre X/Y, graus, metres, absències i duplicats. A la fase d'integració SIG s'importarà primer X/Y UTM i després longitud/latitud per comparar `EPSG:25831` i `EPSG:4326`. El punt representa l'entrada del centre, no tota la parcel·la ni la seva capacitat.

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

- Llenguatge cartogràfic: mapa de context del Tarragonès i requadre provincial, amb una composició inicial completa i una versió revisada.
- Cartografia temàtica: coropleta del percentatge d'habitatge no principal.
- Cartografia temàtica: mapa de símbols graduats amb classes de mida explícites.
- Cartografia temàtica: mapa separat de símbols proporcionals amb habitatges totals.
- Les classificacions final i alternativa conservaran extensió, mida, paleta i context; només canviarà una decisió controlada.
- Els punts de tall, recomptes per classe i colors es conservaran en un registre llegible per màquina.

## Infografia

La demostració del taller serà A3 vertical, `297 × 420 mm`, amb marges de `15 mm`, sis columnes i separacions de `6 mm`. El format avaluable concret serà el que indiqui Moodle. Orientacions inicials per a la demostració:

- títol: 30–34 pt;
- entrada: 15–17 pt;
- mètrica principal: 24–30 pt;
- cos: 11,5–13 pt;
- etiquetes de mapes i gràfics: 10,5–12 pt;
- fonts i notes: 9–10 pt com a mínim.

Si cal una versió A4, es redissenyarà; no es reduirà automàticament l'A3. PowerPoint es pot utilitzar per a un wireframe A3 ràpid, però el màster final serà SVG d'Inkscape.

El tancament conservarà també el PDF de revisió, el PDF final autoritzat després d'una prova de lectura i un ZIP reproduïble amb el llibre, el projecte QGIS, les dades redistribuïbles, el màster SVG, els recursos i el `README.md`. El ZIP s'haurà d'extreure en una carpeta nova i reobrir abans del lliurament.

## Bloquejos d'aprovació

- La guia docent 2026_27 exigeix allotjament turístic municipal i indicadors d'intensitat, densitat i composició de l'oferta; el llibre executable actual només integra població i habitatge a escala municipal.
- El subconjunt d'allotjaments de Vila-seca serveix per practicar geocodificació, però no substitueix una taula municipal comparable per als 22 municipis ni per als territoris assignats als trios.
- Els quatre projectes QGIS, les composicions, les exportacions cartogràfiques, el màster SVG, el PDF final i el ZIP reproduïble encara no existeixen com a artefactes aprovats.

## Captures pendents

- Calc: importació delimitada i codi com a text.
- Calc: rangs o sèries vinculats del gràfic ordenat.
- Calc o Excel 365: configuració del full de gràfic i exportació PDF/SVG utilitzada pel grup.
- QGIS: selecció de subcapes del GeoPackage i CRS.
- QGIS: importació XY amb X, Y i CRS d'origen.
- QGIS: configuració i comprovació de la unió municipal.
- QGIS: composició inicial i revisada de l'etiquetatge.
- QGIS/Inkscape: prova tipogràfica amb família, variants i caràcters del projecte a mida final.
- QGIS: classificació graduada i assistent de mida proporcional.
- Inkscape: objecte vectorial seleccionat i codi de color visible.
- Inkscape: document A3 amb guies, marges i capes.

Les captures mostraran decisions d'interfície, no substituiran els gràfics, mapes o documents exportats.

## Inputs locals, procedència i mapping

En aquesta secció, `P` designa `_practices/tigit-projecte-territorial`. Les mides i recomptes corresponen a la inspecció readonly del 8–9 d'octubre de 2026; no són resultats d'una execució QGIS.

| Font existent | Observació | Destinació pedagògica |
| --- | --- | --- |
| `P/data/processed/tarragones-boundaries-icgc-20260120.gpkg` | 598.016 B; `municipalities_250k` (22), `comarca_250k` (1), `province_1000k` (1), `vila_seca_50k` (1), `municipality_seats` (22); EPSG:25831 | Base espacial, etiquetes, mapes i localització |
| `P/data/processed/catalonia-counties-icgc-20260120.gpkg` | 1.851.392 B; `counties_250k` (43), EPSG:25831 | Context de Catalunya |
| `P/data/processed/municipal-indicators-tarragones-2021.csv` | 2.032 B; 22 files i 22 claus úniques | Unió i indicadors |
| `P/data/processed/municipal-indicators-tarragones-2021.csvt` | 100 B; tipus de les onze columnes | Importació tipada, inclòs el codi com a text |
| `P/data/processed/tigit-05-integracio-sig-teaching.xlsx` | 517.721 B; llibre amb `map_export` | Procedència, fórmules i contrast docent |
| `P/data/processed/education-centres-vila-seca-2025.csv` | 5.928 B; 17 files | Exercici XY de detall |
| `P/data/processed/education-centres-tarragones-2025.csv` | 61.765 B; 183 files | Ampliació XY comarcal |
| `P/outputs/figures/non-principal-housing-tarragones-2021.svg` | Gràfic existent, amb PDF company | Comparació municipal a la síntesi |
| `P/outputs/figures/age-structure-tarragones-2021.svg` | Gràfic existent, amb PDF company | Figura candidata, segons l'argument |
| `P/outputs/figures/population-pyramid-vila-seca-2021.svg` | Gràfic existent, amb PDF company | Figura municipal candidata |

La font ICGC, la llicència CC BY 4.0 i el checksum de la descàrrega original es conserven a `P/data/raw/icgc/README.md`. Les dades estadístiques es remunten a `P/data/raw/t30mun.csv`, `poblacio-edat-tarragones-2021.csv` i `mpiscatalunya.csv`, i als fulls `sources` i `dictionary`. Les transformacions existents es documenten a `prepare_spatial_data.py` i `prepare_qgis_transfer.py`; no cal executar-les per tornar a obtenir inputs ja presents.

Les figures conceptuals `assets/quarto/cartographic-language/locator-map-vila-seca.qmd`, `assets/quarto/thematic-cartography/thematic-methods-tarragones.qmd` i `assets/quarto/thematic-cartography/proportional-symbols-housing-total.qmd` mantenen la seva autoria computacional. Els seus SVG són exemples de teoria, no captures ni evidències d'execució QGIS.

L'ortofoto `P/data/processed/vila-seca-orthophoto-icgc-2025.jpg` (637.230 B) és un recurs local de la figura R, que li assigna una extensió explícita. No s'ha acreditat com a ràster GIS autònom georeferenciat. Afegir-la al paquet GIS exigiria metadades espacials verificades i suport de ràster declarat pel productor. Natural Earth queda com a context mundial opcional, no com a substitut dels límits oficials.

### Registre numèric de control de la demostració

La inspecció alfanumèrica confirma coincidència exacta dels 22 codis del CSV amb `CODIMUNI` del GeoPackage. SQLite informa integritat `ok`; la validesa geomètrica i la unió executada encara requereixen el productor QGIS. La coincidència de codis no demostra per si sola equivalència territorial entre 2021 i 2026.

| Control | Valor dels inputs locals |
| --- | --- |
| Vila-seca, `431711` | 17.417 habitatges totals; 8.692 no principals; 49,9052649710053% |
| Roda de Berà, `431310` | 8.762 totals; 5.673 no principals; 64,7454918968272% |
| La Pobla de Mafumet, `431093` | 1.615 totals; 195 no principals; 12,0743034055728% |
| Comarca, suma de 22 files | 169.179 habitatges totals; 66.105 no principals; 39,07399854591882% |
| Població comarcal del CSV | 262.868 residents; 45.352 de 65+; 17,252765646636334% |
| Consulta `housing_non_main_pct > 50` | 6 codis: `430120`, `430509`, `431310`, `431536`, `431649`, `439057` |

### Lectures i lliuraments diferenciats

Les fonts `P/readings/ca/LLEGIU-ME-estudiant.md` i `P/readings/ca/LLEGIU-ME-professorat.md` són text de domini. La primera explica procediments, criteris i evidències; la segona afegeix controls, respostes i diagnòstics. El mapping a destinataris i als noms natius de les lectures del circuit comú s'ha de validar abans de compilar. No s'assumeix que aquests paths siguin auto-descoberts per l'MCP actual.

La prova del 9 d'octubre amb Web 0.7.1 confirma un límit addicional: `prose_check` rebutja totes dues lectures amb `files_checked: 0` i `Editorial target must be reader-facing content or public metadata`; `editorial_review_prepare` també rebutja el target de la lectura estudiant. La revisió local de text i referències no es presentarà com un check editorial MCP superat. El circuit comú necessita admetre les fonts de lectures o un mapping explícit suportat, sense copiar-les en una col·lecció pública per eludir el límit.

El productor QGIS únic prepararà dades derivades, projectes inicial/resolt, estils, temes, composicions, recursos i captures dins del perfil que realment admeti. El descriptor versionat d'aquest productor serà l'única font de selecció GIS per a Web. Web hi afegirà la lectura i el PDF de cada destinatari i crearà dues edicions ZIP. Els antics `scripts/build_packages.py` i ZIP de preparació de dades conserven la seva finalitat; no es reutilitzen com a motor del nou circuit.

La destinació proposada és `dist/practiques/tigit-projecte-territorial/<version>/ca/`, amb staging per execució a `tmp/practiques/tigit-projecte-territorial/<version>/ca/<run-id>/`. Cada nom d'edició i execució ha de ser nou; cal reservar els fitxers exactes declarats pel productor abans de generar-los. No s'han creat aquestes sortides.

La closure local inclourà només les dependències requerides, amb hashes i paths relatius; no copiarà indiscriminadament l'arbre `_practices`. Els noms dels quatre projectes acumulatius es preserven. El projecte inicial d'una pràctica correspon a la fita precedent; el resolt n'és la continuació, amb les operacions i els controls d'aquella pràctica.

`_practices` és públic al repositori encara que no s'inclogui al web. Cal excloure explícitament el nou `dist/practiques` de Jekyll i comprovar que `_site` no contingui dades, lectures docents ni ZIP no destinats al web. La configuració base inspeccionada exclou `tmp`, però no `dist`; aquesta revisió necessita reserva pròpia d'`_config.yml`. L'exclusió web no permet guardar materials confidencials en un repositori públic.

## Serveis ICGC: evidència i límits

La [fitxa oficial d'Open ICGC](https://plugins.qgis.org/plugins/OpenICGC/) anuncia la versió estable 1.2.3 en la consulta del 9 d'octubre de 2026. La [pàgina de l'ICGC](https://www.icgc.cat/ca/Eines-i-visors/Eines/Connector-QGIS-Open-ICGC) confirma accés a fons i descàrregues, però el seu apartat d'actualització encara esmenta 1.1.20. S'ha de fixar i provar la versió instal·lada en el runtime escollit; no es certifica compatibilitat a partir d'aquestes fitxes.

- WMS mapa base: `https://geoserveis.icgc.cat/servei/catalunya/mapa-base/wms`. `GetCapabilities` ha respost amb WMS 1.1.1, EPSG:25831 i capes com `topografic`, `topografic-gris`, `simplificat` i `orto`.
- WFS divisions: `https://geoserveis.icgc.cat/servei/catalunya/divisions-administratives/wfs`. `GetCapabilities` ha respost amb WFS 2.0.0, EPSG:25831, paginació i `divisions_administratives_wfs:divisions_administratives_municipis_250000`.
- `DescribeFeatureType` ha fallat amb error de transport. No s'han descarregat entitats ni provat el servei dins del runtime QGIS d'aquesta sessió.

Aquestes consultes només acrediten el servei i les capacitats anunciades. Les captures de connexió, la descàrrega real, l'esquema i els controls de completitud són treball posterior. Els serveis remots es documenten separadament de la base portable; no s'introdueix un WMS en el projecte offline per millorar-ne l'aparença.

## Requisits del productor i criteris d'acceptació

1. Carregar i verificar GeoPackage multicap, CSV/CSVT i Shapefile amb auxiliars; conservar codis, tipus, codificació i CRS.
2. Executar i comprovar unió, seleccions i punts interiors, amb paràmetres, recomptes i resultats conservats. Cap prova alfanumèrica externa substitueix aquesta execució GIS.
3. Conservar coropletes, símbols graduats/proporcionals, alternatives i etiquetes en el projecte editable.
4. Conservar temes i enllaços de capes/estils; configurar separadament l'extensió, escala i orientació dels marcs del layout.
5. Reobrir projectes, temes i composicions en una ubicació nova i amb xarxa desactivada. Verificar també fonts i símbols externs, no només les capes visibles.
6. Produir captures reals de l'estat configurat, amb PNG original, anotació derivada i metadata de runtime/idioma. Els noms de controls s'han de contrastar amb la UI observada.
7. Exportar vectors i conservar el projecte font. Si l'autor ha d'ajustar la composició, identificar exactament els elements editables i els controls encara no superats.
8. Consumir el descriptor GIS únic des de Web, afegir dues lectures/PDF i verificar per separat les dues edicions ZIP.

El coordinador ha comunicat el candidat QGIS 0.6.0rc1 i un candidat PDF verificat. La seva selecció immutable i la interfície de packaging/suport docent encara s'han de lliurar a aquesta sessió. No es dedueix que el runtime carregat inclogui aquests candidats ni que el seu perfil admeti layouts, map themes o ràsters. Qualsevol manca es retorna al productor; no es crea un wrapper, un parser QGZ ni un empaquetador local.

La base SVG de síntesi és una font editable de docència a `P/templates/infografia-a3.svg`, amb capes, guies i espais per a peces reals. Té `width="297mm"`, `height="420mm"`, `viewBox="0 0 297 420"` i un fons opac `#fffdf8`. Els dos panells principals són mapa i gràfic; el localitzador s'integra al mapa. No conté scripts, imatges ni referències externes a recursos. Les lectures expliquen com inserir vectors, conservar proporcions i tipografies, substituir camps i revisar crèdits.

La previsualització real s'ha exportat amb l'Inkscape 1.2.2 disponible, mitjançant CLI, a `tmp/tigit-12-svg-preview/infografia-a3.png`. És un render del document, no una captura de la interfície ni una prova d'interacció GUI. Les captures d'Inkscape i la validació de la infografia emplenada continuen com a dependències explícites. La revisió humana del layout i de la síntesi no és substituïble per un segell de bundle.

La comprovació `image_background_check` de la primera plantilla detectava alpha al mostreig del viewport malgrat el fons opac i el PNG d'Inkscape opac. S'ha afegit 1 mm de sagnat només al rectangle de paper de la plantilla nova, mantenint pàgina, proporcions i color. La segona comprovació informa `state: opaque`, `alpha_min: 255` i cap avís al seu mostreig de 1087 × 1536 píxels; això no certifica totes les escales possibles. La previsualització s'exporta amb `--export-area-page`.

Validació local de la plantilla del 9 d'octubre de 2026: XML correcte, IDs únics, dimensions i retícula comprovades, vuit capes semàntiques, 28 objectes de text editables i cap recurs extern ni script. La consulta nativa `inkscape --query-all` situa tots els textos dins dels marges útils; el cos mínim és de 9,07 pt. El PNG de 1123 × 1588 píxels té alpha 255 a tots els píxels i s'ha inspeccionat visualment. SHA-256 de l'SVG: `2a998051b7699daefd77cad4e173b2be16fbdbecedbdb3adcaf40594e6a47c9a`; del PNG: `bafc0835751be1ce7f15a3e31bd7ea61dbd0dad7cf44a9d5048847c6a8b4252c`. Aquesta validació no és una aprovació editorial ni una execució del recorregut QGIS.

## Estat verificat de preparació

- Executat: inspecció readonly de fonts, mides, esquemes, claus, recomptes i agregats; consultes de capacitats WMS/WFS; registre del programa i redacció de les dues lectures; creació de la plantilla SVG, validació XML/estructura i render CLI de la previsualització.
- Existents: llibres, CSV/CSVT, GeoPackages, gràfics de full de càlcul i plantilla A3 editable amb camps per emplenar. Les figures Quarto/R continuen sent exemples del manual.
- Pendents d'execució comuna: Shapefile docent, quatre projectes QGIS, temes, composicions, captures, mapes exportats, PDFs de lectures, dues edicions ZIP i reobertura offline.
- Pendents d'ajust d'autor: composició cartogràfica quan la base operativa ho requereixi, selecció final d'evidències i infografia SVG.
- Pendents de dades/criteri: compatibilitat territorial 2021–2026, inputs per a altres parells assignats i oferta turística municipal requerida per a completar el projecte del curs.
- Pendent de compatibilitat editorial: acceptació dels paths de lectures pel checker del circuit comú; els intents amb les eines del Web 0.7.1 carregat no han inspeccionat la prosa d'aquests fitxers.

L'estat és preparació de fonts docents; no és `practice-ready`. La revisió renderitzada i l'aprovació de l'autor precediran qualsevol publicació.
