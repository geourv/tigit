---
title: "Preparació de dades territorials: LLEGIU-ME del professorat"
lang: ca
ref: tigit-practica-01-docent
content_status: draft
recipient: docent
subject: "Tècniques d'informació geogràfica i turística"
subject_code: "21224102"
---

Aquesta pràctica inicia el llibre acumulatiu de TIGIT. La demostració del professorat treballa els 22 municipis del Tarragonès i utilitza Vila-seca com a cas de control. Cada equip aplica el mateix procediment al parell comarca–municipi assignat. La finalitat és obtenir una taula municipal traçable, no reproduir de memòria la posició dels botons d'una aplicació.

El professorat de teoria situa la pregunta, les fonts, la unitat d'observació, els tipus de dades i la compatibilitat temporal. Al laboratori es comprova com aquestes decisions es materialitzen en la importació, el filtratge, les referències i els controls. La [guia de preparació de dades del manual](https://geourv.github.io/tigit/ca/chapters/fonts-preparacio-dades/) és la referència conceptual compartida amb l'alumnat.

>>>>> - Fer visible la traça entre original, importació, transformació i taula municipal.
>>>>> - Distingir una incidència de format d'una absència o d'una incompatibilitat conceptual.
>>>>> - Comprovar codis, cobertura i resultats amb casos de referència.
>>>>> - Deixar les limitacions documentades abans de reutilitzar les dades en indicadors.

# Preparació de la sessió

La sessió s'adreça a primer de Gestió en Turisme i Hoteleria. Es parteix dels equips i territoris ja assignats, d'un full de càlcul instal·lat i d'una comarca d'unes poques desenes de municipis. Cal mostrar una importació completa abans de demanar que es repeteixi amb altres fonts. Dins de cada equip convé alternar qui opera, qui verifica i qui documenta; tots els membres han de poder explicar el procediment.

| Component | Durada orientativa |
| --- | --- |
| Aula, importació i taula municipal | 150–180 min |
| Treball autònom per estudiant, treballant en equip | 90–150 min |
| Preparació docent | 45–60 min |

Table: Estimació de la pràctica 01 amb quatre fonts i plantilla buida.

Són estimacions no mesurades amb alumnat. La dedicació inclou lectura de metadades i controls; no inclou instal·lacions, esperes prolongades dels portals ni ampliacions. Es pot repartir l'aula en dos blocs. Una comarca molt extensa o una descàrrega que necessiti assistència requereix ajustar l'estimació.

Abans de classe cal obrir el PDF d'alumnat i la plantilla buida, provar les quatre vies d'accés d'Idescat i comprovar el recàlcul del llibre docent. La demostració s'ha de preparar en una còpia amb els originals del Tarragonès i els controls descrits més avall. Si un portal falla, es registra la incidència i es prepara una via de continuació del territori assignat, sense substituir-lo silenciosament pel cas docent.

| Aturada | Comprovació | Pregunta de discussió |
| --- | --- | --- |
| Primera importació | Codi textual, delimitador, decimals i capçalera | Quina informació es perd si un identificador es tracta com un nombre? |
| Taules relacionades | Una fila per municipi; coincidències i absències | Com es distingiria una unió incompleta d'una unió que duplica files? |
| Taula final reoberta | Components, fórmules i incidències visibles | Per què no es pot sumar TOTAL amb les edats ni convertir una absència en zero? |

Table: Punts de comprovació de la conducció docent.

Els errors habituals són unir per nom o posició, incloure notes com a dades, sumar `TOTAL` dues vegades i perdre zeros inicials. Cal demanar que es localitzi el pas on apareix l'error, en lloc de corregir directament el número final. El bloc de diagnòstics conserva els exemples i la incidència temporal `C07`.

# Encaix de la qualificació

La [guia docent URV 2026/27 de TIGIT, 21224102](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&fitxa_apartat=61&any_academic=2026_27) assigna un 5% global al conjunt d'activitats TIC d'aula, un 30% a presentacions/síntesi, un 5% al seguiment, un 30% a proves mixtes i un 30% a proves pràctiques. El 70–20–10 d'aquesta Tasca és una distribució interna sobre 10; la guia no prescriu aquest repartiment intern. No s'ha d'assignar un 5% a cadascuna de les quatre pràctiques ni pressuposar un repartiment igual entre elles.

El professorat concreta a Moodle el pes de cada Tasca dins del bloc corresponent i respecta els mínims i requisits de la guia. Les estimacions d'aquestes lectures són parcials respecte de les 22 hores d'aula i 20 de treball autònom que la planificació oficial orienta a pràctiques TIC. Població i habitatge són una base de treball; no substitueixen la futura informació d'oferta turística municipal.

# Preparar Moodle

1. Crear o configurar una **Tasca** anomenada **TIGIT 01 · Preparació de dades del territori assignat**.
2. Copiar a **Descripció** el bloc següent, de «Pregunta i punt de partida» fins al final de «Qualificació». Afegir-hi una llista explícita dels codis B i subapartats obligatoris indicats a classe. La lectura completa no és tota obligatòria per defecte.
3. Comprovar que la selecció produeix la taula municipal necessària per a 02. Si s'acota un pas, preveure com es completarà o quina preparació identificada del mateix territori permetrà continuar.
4. Adjuntar a **Fitxers addicionals** el PDF d'alumnat «Preparació de dades territorials» i el paquet inicial amb la plantilla buida. La guia docent, la solució `-teaching` i els controls del Tarragonès són material de preparació del professorat.
5. Revisar equips, agrupament i tramesa en grup. Fixar a Moodle dates, formats admesos i límit de mida; configurar el màxim de 10 punts amb criteris de 7, 2 i 1 i el pes global que correspongui.
6. Revisar la **vista d'estudiant**: descripció completa, llista d'obligatoris, territori, obertura del PDF i plantilla sense solució. Si es comparteix un cas resolt, identificar-lo com a exemple del Tarragonès–Vila-seca.

## Enunciat per copiar a la descripció

### Pregunta i punt de partida

Com es distribueixen la població i els habitatges entre els municipis de la comarca assignada, i com es pot preparar una taula fiable per estudiar-los? Cada equip manté el seu parell comarca–municipi i parteix de la plantilla buida adjunta. Cal obtenir d'Idescat els codis territorials, la població per edat de 2021, l'habitatge de 2021 i la superfície amb el seu període real. Tarragonès–Vila-seca és l'exemple de classe, no la resposta dels altres equips.

### Treball bàsic —70%

El professor indica a classe els apartats obligatoris i els enumera en aquesta Tasca. El recorregut disponible és:

- **B1. Fonts:** conservar els originals i registrar productor, selecció, període, URL, accés i condicions d'ús a `sources`.
- **B2. Preparació:** importar a `source_*`, conservar codis textuals i magnituds numèriques, i documentar transformacions a `prepared_*` i `dictionary`.
- **B3. Integració:** construir `municipal` amb una fila per municipi, claus comprovades i components de població, habitatge i superfície vinculats a l'origen.
- **B4. Control i continuïtat:** comprovar cobertura, duplicats, absències i sumes; registrar incidències i reobrir el llibre. La base que passarà a 02 ha de conservar components, procedència i limitacions, encara que la selecció avaluada sigui més curta que la guia.

### Ampliacions —20%

Es pot desenvolupar una d'aquestes propostes més enllà del treball seleccionat:

- **A1. Auditoria d'importació.** Pregunta: què altera l'obertura automàtica d'un CSV respecte d'una importació controlada? Es varia només el procediment d'importació, sobre còpies del mateix original. La referència és el CSV conservat. Es contrasten recompte, codis, accents, tipus i tres valors amb decimals o separadors; si no hi ha diferències, també es documenta. La interpretació explica quines opcions preserven el significat i en quines condicions.
- **A2. Prova dels controls.** Pregunta: els controls detecten un duplicat i una absència? En dues còpies de prova identificades s'introdueix, separadament, una fila duplicada i l'omissió d'un municipi. La referència és la taula validada. Cal predir i contrastar files, claus úniques, correspondències i efecte en una suma. La interpretació explica per què comptar files no és suficient. Les còpies de prova no substitueixen la taula real ni passen a 02.

Una ampliació ja inclosa als obligatoris es puntua al bloc bàsic, una sola vegada. No cal acumular proves: la pregunta, el contrast, els controls i la interpretació determinen la qualitat de l'aportació.

### Productes, controls i documentació

Cal conservar el llibre `tigit-01-preparacio-dades.xlsx`, els originals i el registre de fonts, diccionari i incidències. El `README.md` explica territori, decisions i contribucions dels membres. Per al lliurament, cal preparar el llibre i uns apunts breus en PDF amb captures llegibles d'una importació i d'un control; els originals o el paquet complet s'adjunten segons el que indiqui la Tasca. Tot el conjunt es conserva per continuar.

Els controls exigeixen un codi únic per municipi, cobertura documentada, correspondències comptades i components d'edat contrastats amb el total. Les absències no són zeros; la superfície posterior a 2021 manté la limitació temporal. No s'han de forçar els recomptes perquè coincideixin amb els 22 municipis del cas docent.

### Qualificació

**Bàsic: fins a 7 punts**, per correcció, traça i comprovació dels apartats seleccionats. **Ampliacions: fins a 2 punts**, per una pregunta delimitada, contrast controlat i interpretació. **Documentació: fins a 1 punt**, per claredat dels apunts, captures significatives, atribucions i organització. Els màxims no són automàtics i acumular fitxers no garanteix més nota.

La documentació suma també sense ampliacions: bàsic i documentació complets poden arribar a 8/10. La correcció tècnica es valora al bàsic o a l'ampliació; el 10% valora com es comunica i s'organitza, sense puntuar dues vegades la mateixa aportació. Les ampliacions no substitueixen els obligatoris. Aquesta és la nota interna de la Tasca; el seu pes global i els requisits de superació són els de Moodle i la guia docent.

# Material de la demostració

El projecte docent conserva diverses fases del curs en una execució identificada. Per a aquesta pràctica s'utilitzen el llibre de la fita 01 i les quatre fonts següents. Les altres solucions no formen part del punt de partida de l'alumnat, que rep la plantilla buida i fa la descàrrega guiada del seu territori.

| Fitxer dins del projecte pràctic | Paper en la demostració |
| --- | --- |
| `tigit-01-preparacio-dades-teaching.xlsx` | Solució a `data/processed`: 14 fulls, dades importades, transformacions, 264 fórmules i taula dinàmica de control. |
| `data/raw/mpiscatalunya.csv` | Correspondència de 947 municipis amb les comarques a la descàrrega conservada. |
| `data/raw/t30mun.csv` | Categories d'habitatge municipal de 2021. |
| `data/raw/t396mun.csv` | Superfície municipal; la còpia conservada identifica una publicació de 2025. |
| `data/raw/poblacio-edat-tarragones-2021.csv` | Extracte documentat de població: 2.244 files, 22 municipis i 102 categories d'edat, amb sexe total i any 2021. |

Table: Material que s'utilitza en la primera pràctica.

La plantilla d'alumnat és un llibre diferent de la solució docent: té 13 fulls i no conté dades als blocs `source_*`, `prepared_*` o `municipal`. Cal comprovar que es distribueix aquesta versió i no una còpia del llibre resolt. La plantilla porta exemples del Tarragonès a `project` i `sources`; la primera intervenció docent ha d'assegurar que cada equip els adapta al territori assignat.

El llibre docent s'ha reconstruït amb els inputs fixats i s'ha contrastat estructuralment amb el cas de consulta. Les proves amb LibreOffice Calc 24.2.7.2 conserven fórmules, codis textuals i taula dinàmica. La preparació de l'aula ha d'incloure també una obertura amb la versió d'Excel que s'utilitzi, si escau. La comprovació del format XLSX no substitueix l'observació de l'aplicació ni el control del recàlcul.

# Conducció del laboratori

La demostració pot seguir un únic municipi abans d'ampliar-se a la comarca. Cal mostrar com es localitza Vila-seca a les quatre fonts i com el codi `431711` evita dependre de l'ordre o de la grafia del nom. A continuació, el codi comarcal `36` permet obtenir el conjunt de 22 municipis.

1. **Verificació de la font.** Cal llegir el títol, les categories, el període i les notes, i completar el registre de `sources` abans de transformar la taula.
2. **Importació.** La previsualització ha de permetre comprovar UTF-8, delimitador, decimals i codis com a text. Els títols i les notes de publicació s'han de separar del bloc de dades.
3. **Preparació.** Cal comparar una fila de `source_*` amb la corresponent de `prepared_*` i explicar quina regla ha canviat el tipus, el nom del camp o l'estructura.
4. **Integració.** Les referències i unions s'han de construir amb les claus municipals. S'han de comptar coincidències i absències abans d'acceptar la taula.
5. **Control.** Cal revisar una selecció de municipis i els totals compatibles, anotar les incidències i tornar a obrir el llibre desat.

La població requereix distingir les 101 categories d'edat simple o oberta de la categoria `TOTAL`. El reagrupament utilitza `0–14`, `15–64` i `65+`; `Y_GE100` s'inclou a l'últim grup. S'ha d'evitar que `TOTAL` es sumi amb les edats o que el grup de 100 anys o més desaparegui de l'agregació.

El professorat pot utilitzar la taula dinàmica per comprovar la cobertura municipal, però convé mantenir visibles les fórmules de la taula analítica. L'alumnat ha de poder explicar d'on surt un valor de `municipal`, no només mostrar que coincideix amb un número de control.

# Valors de control del cas docent

Els valors següents corresponen als fitxers conservats de la demostració. Serveixen per detectar problemes d'importació, referència o suma. No s'apliquen als altres territoris assignats. La població total i els grups d'edat s'expressen en persones; les tres últimes columnes compten habitatges.

| Municipi i codi | Població total | 0–14 | 15–64 | 65+ | Habitatges totals | Principals | No principals |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vila-seca, `431711` | 22.781 | 4.155 | 15.326 | 3.300 | 17.417 | 8.725 | 8.692 |
| Roda de Berà, `431310` | 7.154 | 1.074 | 4.539 | 1.541 | 8.762 | 3.089 | 5.673 |
| La Pobla de Mafumet, `431093` | 4.044 | 867 | 2.845 | 332 | 1.615 | 1.420 | 195 |

Table: Controls de població i habitatge de 2021 per al professorat.

Les 22 files de `municipal` sumen 262.868 residents, 169.179 habitatges totals i 66.105 habitatges no principals. Cal contrastar les sumes amb els components i les definicions conservades. Una coincidència numèrica no acredita per si sola la compatibilitat territorial ni converteix l'habitatge no principal en una mesura del turisme.

# Diagnòstics que cal treballar

Un codi sense zero inicial indica sovint una conversió automàtica a nombre. Cal tornar a la importació i al tipus de columna, no afegir zeros per intuïció. Si la unió produeix menys files o duplica municipis, s'han de revisar longitud, espais, esquema de codis, unicitat i nivell territorial de les dues taules.

Una suma d'edats incorrecta pot provenir de la inclusió de `TOTAL`, d'una interpretació errònia del grup obert o d'un rang de fórmula inadequat. També cal consultar les notes de difusió abans de corregir una discrepància. Les absències i els símbols de confidencialitat no s'han de convertir en zeros per fer quadrar un control.

>>>> El control `C07` del llibre docent continua identificant una diferència temporal: població i habitatge de 2021 davant superfície publicada el 2025. Cal acreditar que no hi ha canvis territorials rellevants o obtenir una font equivalent abans d'acceptar la densitat de la pràctica següent. El recàlcul correcte de la fórmula no resol aquesta qüestió.

Quan s'obre un llibre generat, el recàlcul pot actualitzar els valors desats sense modificar la definició de les fórmules. Cal distingir un error de cel·la d'una cadena buida retornada intencionadament, i comprovar els valors numèrics després del recàlcul. La versió de consulta no s'ha de substituir per una còpia amb fórmules convertides en valors.

# Criteris de tancament

La taula es pot donar per preparada quan cada camp es pot remuntar a una font, cada municipi té una única fila, els tipus i les claus són correctes i les incidències estan explicades. `sources`, `dictionary`, `checks` i el `README.md` han de permetre reprendre el procés sense reconstruir oralment les decisions.

La revisió amb cada equip ha de demanar la justificació del territori, la selecció de fonts i una transformació concreta, a més del fitxer final. Cal conservar la fita 01 abans de començar els indicadors en una còpia de continuació. Les qüestions que afectin denominadors o comparabilitat han de passar explícitament a la pràctica 02; no desapareixen en canviar el nom del llibre.
