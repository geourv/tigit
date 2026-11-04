---
title: "Preparació de dades territorials: LLEGIU-ME de l'alumnat"
lang: ca
ref: tigit-practica-01-alumnat
content_status: draft
recipient: alumnat
subject: "Tècniques d'informació geogràfica i turística"
subject_code: "21224102"
---

La primera pràctica construeix la base que alimentarà els indicadors, els gràfics i els mapes del projecte territorial. La pregunta de partida és com es distribueixen la població i el parc d'habitatges entre els municipis de la comarca assignada. El resultat serà una taula `municipal` amb una fila per municipi i un rastre comprovable de les fonts i les transformacions.

El parell Tarragonès–Vila-seca és la demostració del professorat. Cada equip treballa el parell comarca–municipi assignat; els noms, els codis, les seleccions i els recomptes s'han d'adaptar a aquest territori. Aquesta guia acompanya l'[activitat de preparació de dades del manual](https://geourv.github.io/tigit/ca/chapters/fonts-preparacio-dades/), on es desenvolupen les explicacions i els exemples de fórmules.

>>>>> - Conservar i documentar els originals d'Idescat.
>>>>> - Importar codis, nombres i categories sense alterar-ne el significat.
>>>>> - Relacionar les fonts pel codi municipal i obtenir una fila per municipi.
>>>>> - Comprovar la cobertura, les absències, les sumes i la compatibilitat temporal.

# Selecció del treball i organització de l'equip

El professor indica a classe els apartats obligatoris i els enumera explícitament a la Tasca de Moodle. Aquesta guia ofereix el recorregut complet; no tots els exemples es converteixen automàticament en requisits avaluats. Els blocs identificables són **B1, fonts; B2, importació i preparació; B3, taula municipal; i B4, controls i continuïtat**.

Cada equip conserva el parell comarca–municipi assignat i registra les contribucions dels membres. Convé alternar qui opera, qui contrasta les dades i qui documenta; tots els membres han de poder explicar una font, una transformació i un control. Tarragonès–Vila-seca continua sent una demostració.

Per passar a 02 cal conservar la taula municipal amb claus, components de població i habitatge, superfície amb període declarat, procedència i incidències. Si s'acota algun pas, el professorat ha d'indicar com es completarà o quina preparació identificada del mateix territori permet continuar. La selecció avaluada no justifica perdre una dependència necessària.

Amb plantilla buida, programa instal·lat i una comarca d'unes poques desenes de municipis, s'estimen **150–180 minuts d'aula i 90–150 de treball autònom per estudiant treballant en equip**. Són orientacions no mesurades amb alumnat; no inclouen instal·lacions, esperes prolongades dels portals ni ampliacions. Moodle concreta les sessions i els terminis.

# Material i preparació

El [paquet inicial de pràctiques](https://geourv.github.io/tigit/assets/downloads/tigit-01-preparacio-dades-student.zip) conté la plantilla `data/processed/tigit-01-preparacio-dades.xlsx`, un `README.md` de treball i les carpetes del projecte. Els fulls analítics estan buits: les dades s'obtenen i es documenten durant l'activitat. Es necessita Excel o LibreOffice Calc i connexió a Internet per consultar i descarregar les fonts.

Cal extreure completament el ZIP en una carpeta amb permisos d'escriptura i obrir el llibre des d'aquesta carpeta. Al full `project` s'han d'anotar autoria, aplicació, versió, configuració regional i territori. La plantilla porta `Tarragonès` com a exemple a `case_territory`: cal substituir-lo pel territori assignat i revisar també les seleccions preomplertes de `sources`. El municipi de referència i el seu codi han de quedar identificats al registre del projecte.

Les carpetes anticipen el recorregut del curs. En aquesta pràctica s'utilitzen `data/raw`, `data/processed` i el `README.md`; és normal que les carpetes de mapes i figures encara siguin buides.

| Ubicació | Funció en aquesta pràctica |
| --- | --- |
| `data/raw` | Originals rebuts del productor, sense correccions manuals. |
| `data/processed/tigit-01-preparacio-dades.xlsx` | Importació, preparació, diccionari, comprovacions i taula municipal. |
| `README.md` | Territori, pregunta, fonts, decisions i incidències que permeten reprendre el treball. |

Table: Organització del material de la pràctica.

# Fonts i selecció territorial

La lectura de la pàgina del productor precedeix la descàrrega. Cal comprovar títol, nivell territorial, període, categories, notes i condicions de reutilització. Per a cada recurs s'ha de completar una fila de `sources` amb l'URL, la data d'accés, la selecció aplicada, el format i el nom del fitxer conservat.

| Font d'Idescat | Selecció i comprovació essencial |
| --- | --- |
| [Codis de municipis i comarques](https://www.idescat.cat/codis/?id=50&n=9&lang=ca) | Identificar el codi de la comarca i les claus municipals que li corresponen. |
| [Població per sexe i edat any a any](https://www.idescat.cat/pub/?id=censph&n=10&lang=ca) | Any 2021, municipis assignats, sexe total, edats simples i total publicat. |
| [Habitatges per tipus d'habitatge](https://www.idescat.cat/pub/?id=censph&n=30&lang=ca) | Any 2021 i municipis; conservar les categories i les notes originals. |
| [Superfície, densitat i entitats singulars](https://www.idescat.cat/pub/?id=inddt&n=396&lang=ca) | Nivell municipal; registrar el període real de la superfície descarregada. |

Table: Fonts necessàries per preparar la taula municipal.

El codi de comarca permet seleccionar el conjunt de municipis. El prefix provincial no és suficient per identificar una comarca. Convindrà seguir primer el municipi de referència en les quatre fonts i aplicar després la mateixa comprovació a totes les claus de l'àmbit assignat.

>>>> Població i habitatge corresponen a 2021. Si la superfície procedeix d'una publicació posterior, cal registrar aquesta diferència i comprovar la compatibilitat territorial abans d'utilitzar-la com a denominador. No s'ha de canviar l'etiqueta de l'any per fer coincidir les fonts.

Si la descàrrega de població no conserva la selecció necessària, cal contrastar-la amb el professorat o utilitzar la consulta documentada de l'API d'Idescat. Un fitxer corresponent a una altra comarca no pot substituir les dades del territori assignat.

# Importació i preparació al llibre

Els CSV s'han d'importar amb la codificació i el delimitador que corresponguin al fitxer. Les descàrregues d'Idescat poden utilitzar UTF-8, punt i coma i coma decimal; cal comprovar-ho a la previsualització. Els codis municipals s'han de tractar com a text perquè conservin els sis caràcters i els zeros inicials.

1. Cal conservar el fitxer rebut a `data/raw` i identificar títols, notes i capçalera abans d'importar-lo.
2. Cada taula s'incorpora al seu full `source_*`, mantenint les capçaleres i categories de la font. Els títols i les notes no poden convertir-se en files analítiques.
3. Als fulls `prepared_*` es documenten els noms de camp propis, els tipus i les regles de transformació. Si codi i nom apareixen junts, s'han de separar sense perdre la clau textual.
4. Cal filtrar el territori amb el codi de comarca i relacionar les taules pel codi municipal. No s'han d'unir per la posició de les files ni per una semblança de noms.
5. Les absències, els símbols de confidencialitat i els problemes de correspondència es registren a `checks`; no s'han de convertir en zeros.

La població per edat requereix una transformació concreta. A `prepared_population` cal interpretar l'edat simple com a nombre i construir els grups `0–14`, `15–64` i `65+`. La categoria oberta `Y_GE100` forma part de `65+`; la categoria `TOTAL` es conserva com a control, però no entra en cap dels tres grups. La suma condicionada `SUMIFS` permet agrupar per municipi i interval d'edat, segons l'exemple del manual.

Els noms de les funcions i els separadors poden aparèixer localitzats a Excel o Calc. Cal conservar la lògica de la fórmula i comprovar-ne el resultat amb unes quantes files conegudes. Que una aplicació accepti la sintaxi no demostra que s'hagin triat el rang o les condicions correctes.

# Taula municipal i comprovacions

`municipal` ha de reunir identificació territorial, població total i per grans grups d'edat, habitatges i superfície. Els camps han de referenciar les dades preparades perquè una correcció es pugui seguir fins a l'origen. Cal conservar explícitament la definició de cada categoria d'habitatge: l'habitatge no principal no equival a habitatge turístic.

Abans de donar per acabada la taula, s'han de comprovar aquests punts:

- El nombre de files correspon als municipis de la comarca i cada codi apareix una sola vegada.
- Les unions tenen un recompte de coincidències i absències; cap unió ha multiplicat files.
- Els codis continuen sent text i les magnituds que s'han de sumar són numèriques.
- Els grups d'edat s'han contrastat amb el total publicat. Si hi ha una diferència de difusió o arrodoniment, es conserva i s'explica.
- Les categories, els períodes i les unitats corresponen a les definicions anotades a `dictionary` i `sources`.

Una incidència es tanca quan se'n coneix la causa i es pot comprovar la decisió aplicada. Si encara afecta la interpretació d'un camp, ha de continuar visible al registre; marcar una fila com a correcta no resol per si mateix el problema.

# Ampliacions controlades

Es pot desenvolupar una de les propostes següents si va més enllà dels obligatoris. Si el professor ja ha seleccionat una comparació com a bàsica, es puntua en aquell bloc i no una altra vegada com a ampliació.

## A1. Auditar una importació

La pregunta és què altera l'obertura automàtica d'un CSV respecte d'una importació controlada. Es varia només la manera d'importar còpies del mateix fitxer; la referència és l'original conservat a `data/raw`. Cal comparar recompte, codis textuals, accents, tipus i tres valors amb decimals o separadors.

La interpretació identifica quines opcions preserven les dades i quins errors poden afectar les unions o les sumes. Si les dues importacions coincideixen, es documenta aquesta coincidència i les condicions provades; no s'inventa un error. Es conserven les opcions, una comparació breu i captures significatives.

## A2. Posar a prova els controls

La pregunta és si els controls permeten distingir un duplicat d'una absència. Es preparen dues còpies de prova de la taula validada: en una es duplica una fila i en l'altra s'omet un municipi. La taula real, que no es modifica, és la referència.

Cal predir i comprovar files, claus úniques, correspondències i efecte sobre una suma. La interpretació explica per què un recompte aparentment correcte no garanteix integritat. Les còpies s'identifiquen com a proves i no passen a la pràctica 02; es valora el diagnòstic, no la producció de més fitxers.

# Resultat que cal conservar

El resultat d'aquesta pràctica és el llibre `tigit-01-preparacio-dades.xlsx`, acompanyat dels originals i del registre del projecte. El `README.md` ha d'explicar quin territori s'ha treballat, d'on prové cada font, com s'han preparat les dades i quines limitacions continuen afectant-ne l'ús.

Cal tancar el llibre i tornar-lo a obrir des de la carpeta extreta, comprovar que les fórmules es calculen i revisar els casos de control. El llibre únic, els originals, `sources`, `dictionary` i `checks` han de permetre a una altra persona reconstruir la preparació. Aquesta base alimentarà la pràctica d'indicadors; els percentatges, els gràfics i els mapes es desenvoluparan en les fases següents.

# Lliurament i qualificació interna

El lliurament prepara el llibre i uns apunts breus en PDF amb territori, fonts, decisions, controls i contribucions de l'equip. Una captura d'importació i una d'un control poden acreditar decisions si són llegibles i comentades; no cal capturar cada clic. Moodle indica si s'adjunten també els originals o el conjunt complet. El que no es demani trametre es conserva igualment per continuar.

| Bloc | Màxim | Què es valora |
| --- | ---: | --- |
| Bàsic, 70% | 7 punts | Correcció, traça i comprovació dels apartats seleccionats. |
| Ampliacions, 20% | 2 punts | Pregunta, contrast controlat i interpretació justificats. |
| Documentació, 10% | 1 punt | Apunts clars, captures útils, atribucions i organització. |

Table: Qualificació interna de l'activitat sobre 10.

Els 7 punts són el màxim del bàsic, no una nota automàtica. La documentació també suma sense ampliacions: bàsic i documentació complets poden arribar a 8/10. Les ampliacions no substitueixen els obligatoris i acumular fitxers no garanteix més nota. La correcció tècnica es valora al bàsic o a l'ampliació; el 10% valora la comunicació i l'organització sense tornar a puntuar la mateixa aportació.

Aquesta distribució interna no és el pes de l'activitat dins de l'assignatura. Moodle en concreta l'encaix global d'acord amb la [guia docent vigent de TIGIT, 21224102](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&fitxa_apartat=61&any_academic=2026_27), inclosos els requisits de superació.
