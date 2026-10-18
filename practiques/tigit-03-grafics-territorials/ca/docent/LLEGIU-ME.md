---
title: "Gràfics a partir de les dades: LLEGIU-ME del professorat"
lang: ca
ref: tigit-practica-03-docent
content_status: draft
recipient: docent
subject: "Tècniques d'informació geogràfica i turística"
subject_code: "21224102"
---

La pràctica relaciona una pregunta amb una taula, una geometria i una comprovació de lectura. El professorat de teoria explicita què codifica cada marca; al laboratori es contrasten rangs, eixos, ordre, denominadors i exportació. El cas docent continua amb població i habitatge del Tarragonès i les ampliacions municipals de Vila-seca.

L'alumnat parteix del seu llibre 02 i construeix la continuació 03. La solució docent permet comprovar resultats i diagnosticar incidències; no ha de substituir aquest procés. El [capítol de semiologia i visualització](https://geourv.github.io/tigit/ca/chapters/semiologia-visualitzacio/) diferencia el nucli guiat de les ampliacions opcionals.

# Preparació de la sessió

Per a primer curs convé començar amb una pregunta de comparació i un gràfic vinculat, abans d'obrir el repertori de representacions. Es pressuposa el llibre 02 validat, el mateix equip i territori, Excel o Calc disponible i una comarca d'unes poques desenes de municipis. Cal alternar qui construeix, qui contrasta les dades i qui explica la lectura del gràfic.

| Component | Durada orientativa |
| --- | --- |
| Aula, dues representacions i auditoria | 120–150 min |
| Treball autònom per estudiant, treballant en equip | 90–150 min |
| Preparació docent | 30–45 min |

Table: Estimació de la pràctica 03 amb indicadors i rangs ja comprovats.

Són estimacions no mesurades amb alumnat. Inclouen dues figures seleccionades, la seva auditoria i exportació; no inclouen instal·lacions, noves sèries de dades ni ampliacions. La preparació docent comprova els llibres 02/03, els rangs, el PDF històric d'auditoria i els exports corregits. Cal provar la via d'exportació amb l'aplicació que s'utilitzarà a l'aula.

| Aturada | Comprovació | Pregunta de discussió |
| --- | --- | --- |
| Rang vinculat | Codi, nom i valor es mouen junts | Com es detecta que només s'ha ordenat una columna? |
| Figura editable | Tres casos coincideixen amb la taula; eixos i unitats correctes | La figura compara quantitats, composicions o una relació entre variables? |
| PDF a mida final | Etiquetes, llegenda, fonts i àrea exportada llegibles | Què es pot afirmar mirant el gràfic, i què exigiria altres dades? |

Table: Punts de comprovació de la representació gràfica.

Els errors habituals són incloure un total com si fos un municipi, separar noms i valors, intercanviar eixos, truncar l'origen de barres i confondre un recompte amb un percentatge. La figura històrica permet discutir-los sense alterar els originals. Cal demanar a un membre diferent del que ha fet el gràfic que n'expliqui la variable i la base de comparació.

# Encaix de la qualificació

La [guia docent URV 2026/27 de TIGIT, 21224102](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&fitxa_apartat=61&any_academic=2026_27) diferencia activitats TIC d'aula, 5% global; presentacions/síntesi, 30%; seguiment, 5%; proves mixtes, 30%; i proves pràctiques, 30%. El 70–20–10 d'aquesta activitat distribueix els seus 10 punts interns. No converteix cada Tasca en un 5% de l'assignatura ni substitueix la qualificació posterior de la síntesi.

El professorat anuncia els gràfics i apartats obligatoris i en configura el pes a Moodle respectant la guia. La qualitat tècnica del gràfic es valora al bloc bàsic o a l'ampliació; la llegibilitat, les atribucions i l'organització es valoren al 10%, sense repetir una mateixa millora. Les figures de població i habitatge aporten context territorial, no una estimació d'activitat turística.

# Preparar Moodle

1. Crear o configurar una **Tasca** anomenada **TIGIT 03 · Gràfics i lectura crítica del territori**.
2. Copiar a **Descripció** el bloc següent, de «Pregunta i punt de partida» fins al final de «Qualificació». Enumerar els codis B i les representacions obligatòries comunicades a classe. Indicar quines comparacions queden com a ampliació.
3. Mantenir el llibre i els indicadors de continuïtat cap a QGIS. La selecció ha de produir dues o tres figures candidates, però no obliga a construir tots els exemples de la guia.
4. Adjuntar a **Fitxers addicionals** el PDF d'alumnat «Gràfics a partir de les dades». Si s'ofereix la figura defectuosa, etiquetar-la com a cas d'auditoria. Els llibres docents, la figura històrica, els exports corregits i els valors de control serveixen per preparar la demostració.
5. Revisar tramesa en grup, agrupament, formats, mida i dates. Configurar màxim 10 amb criteris de 7, 2 i 1 i el pes global corresponent. Demanar fitxer editable i evidències de lectura, no només imatges de pantalla.
6. Revisar la **vista d'estudiant**, el PDF, la selecció de gràfics i la separació entre exemple resolt i treball del territori assignat.

## Enunciat per copiar a la descripció

### Pregunta i punt de partida

Quines representacions permeten comparar els municipis de la comarca sense desfigurar les dades? Cada equip continua el seu llibre 02 i conserva el parell comarca–municipi assignat. Cal desar `tigit-03-semiologia-visualitzacio.xlsx`, mantenint indicadors, components i controls. Els gràfics del Tarragonès són exemples; el resultat propi ha de correspondre a les dades de l'equip.

### Treball bàsic —70%

El professor comunica a classe els apartats i gràfics obligatoris i els enumera en aquesta Tasca. El recorregut disponible és:

- **B1. Rangs:** preparar blocs vinculats a les dades, amb codi, nom i valors de cada municipi, sense transcriure'ls a mà.
- **B2. Comparació municipal:** construir les barres ordenades d'habitatge no principal i comprovar marques, ordre, origen i unitats.
- **B3. Segona lectura:** construir la representació complementària seleccionada pel professorat, indicant si mostra volum, composició o relació entre variables.
- **B4. Auditoria i continuïtat:** conservar una versió inicial i una de revisada, justificar les decisions i exportar dues o tres figures candidates. El llibre ha de mantenir les claus, els components i els indicadors que després s'incorporaran a QGIS.

### Ampliacions —20%

Es pot desenvolupar una comparació controlada com aquestes, si supera el treball seleccionat:

- **A1. Volum i composició residencial.** Pregunta: quins contrastos es veuen o s'amaguen en passar de barres apilades absolutes a barres al 100%? Es varia la normalització, mantenint municipis, ordre, categories i colors. La referència són els habitatges principals, no principals i totals del llibre. Cal comprovar sumes, denominadors positius i que cada barra relativa representa el 100%. La interpretació diferencia mida del parc i composició, sense deduir-ne ús turístic.
- **A2. Intervals d'un histograma.** Pregunta: com canvia la lectura de la distribució amb intervals de 10 o 20 punts percentuals? Es varia només l'amplada dels intervals d'habitatge no principal, sobre el mateix domini de 0 a 100. La referència és la taula de valors validats. Cal comprovar límits sense buits ni solapaments, inclusió del 100 al darrer interval i suma igual al nombre de municipis vàlids. La interpretació explica detall, agrupació i límits d'una mostra petita; les absències es compten separadament.

Una comparació ja obligatòria no torna a puntuar com a ampliació. Una pregunta ben contrastada pot justificar el bloc; acumular figures o canviar colors sense analitzar l'efecte no garanteix més nota.

### Productes, controls i documentació

Cal conservar els llibres 02/03, els gràfics editables, els rangs, l'auditoria i les figures exportades a `outputs/figures`. El lliurament prepara el llibre 03, els PDF seleccionats i uns apunts breus en PDF amb pregunta, tres decisions justificades, controls i limitacions. Moodle concreta el conjunt que s'ha de trametre. El registre d'equip identifica contribucions i fonts.

Cal contrastar tres municipis, comprovar que cada marca correspon a la seva dada i llegir el PDF a mida final. Una captura no substitueix el gràfic editable. Les magnituds absolutes i relatives s'etiqueten amb les seves unitats; una associació entre variables no demostra una causa turística.

### Qualificació

**Bàsic: fins a 7 punts**, per construcció, vinculació, controls i justificació dels gràfics seleccionats. **Ampliacions: fins a 2 punts**, per pregunta, comparació i interpretació pròpies. **Documentació: fins a 1 punt**, per claredat dels apunts, captures útils, gràfics llegibles, atribucions i organització. Els màxims no són automàtics ni depenen de quants fitxers s'entreguen.

La documentació pot sumar sense ampliacions: bàsic i documentació complets poden arribar a 8/10. La correcció tècnica es puntua al bloc que correspon i no es torna a comptar com a qualitat comunicativa. Les ampliacions no substitueixen els obligatoris. Aquesta és una qualificació interna; Moodle i la guia docent fixen el pes global i els requisits de superació.

# Inventari de la fita docent

El llibre `tigit-03-semiologia-visualitzacio-teaching.xlsx` es troba a `data/processed` de l'execució del projecte pràctic. Té 33 fulls, 1.080 fórmules, nou objectes de gràfic i dues taules dinàmiques. `chart_00_audit` conté dos gràfics; cadascun dels set fulls `chart_01` a `chart_07` en conté un.

| Full o bloc | Funció |
| --- | --- |
| `charts_data` | Blocs vinculats de composició d'edats, habitatge ordenat i parelles de dispersió. |
| `chart_00_audit` | Comparació d'una presentació inicial i una de revisada. |
| `chart_01_age_structure` | Composició per grans grups d'edat. |
| `chart_02_nonprincipal` | Comparació municipal d'habitatge no principal. |
| `chart_03_scatter` | Associació descriptiva entre envelliment i habitatge no principal. |
| `chart_04_housing_donut` | Composició del parc d'habitatges comarcal. |
| `chart_05_population_time` | Sèrie del Padró de Vila-seca, 2000–2022. |
| `chart_06_population_pyramid` | Edat i sexe del Cens de 2021. |
| `chart_07_housing_histogram` | Distribució dels 22 municipis per interval percentual. |

Table: Components de consulta de la fita de visualització.

Les barres agrupades i apilades absolutes del nucli pedagògic s'han de construir o demostrar a partir dels components d'habitatge: no disposen d'un full específic entre aquests nou objectes. El recompte de gràfics del comprovador no acredita que totes les variants del manual estiguin materialitzades ni que la retolació sigui correcta.

# Auditoria d'una exportació real

La figura següent és una exportació històrica del llibre, conservada per treballar la revisió crítica. Els valors i els noms municipals permeten reconstruir la comparació, però els títols dels eixos estan intercanviats: «Municipi» apareix sota l'eix numèric i la unitat percentual al costat de les categories. L'exercici consisteix a corregir-los al gràfic editable i tornar a exportar.

![Barres horitzontals dels municipis del Tarragonès amb els títols dels eixos intercanviats](sandbox/practiques/tigit-projecte-territorial/recursos/2026-10-14/outputs/figures/non-principal-housing-tarragones-2021.pdf "Exportació històrica per a l'auditoria. Les categories són municipis i l'eix numèric expressa percentatge d'habitatge no principal; els títols d'aquesta figura estan intercanviats. Dades: Idescat, 2021.")

La solució de consulta situa «Municipi» a l'eix categòric i «% sobre el total d'habitatges» a l'eix de valors. Cal comparar aquesta correspondència en el gràfic editable i en el PDF exportat: canviar l'orientació de les barres no canvia la funció dels dos eixos.

També cal revisar l'ordre visible, el títol amb l'any i la llegenda d'una única sèrie. L'exercici pot demanar una versió amb els valors més alts a dalt, una unitat correcta a l'eix horitzontal i una font llegible. No s'ha de presentar aquesta exportació conservada com una versió final validada.

# Controls de dades i sèries

Les barres d'habitatge han de representar 22 municipis. El màxim del cas docent és Roda de Berà, 64,7455%; el segueixen Salou, 63,0778%, i Creixell, 59,8172%. Vila-seca presenta 49,9053% i la Pobla de Mafumet, 12,0743%. Aquests valors permeten detectar una ordenació parcial que hagi separat noms i magnituds.

La dispersió vincula X a `population_65_plus_pct` i Y a `housing_non_main_pct`. Per a Vila-seca, la parella és aproximadament `(14,4858; 49,9053)`. Hi ha d'haver un punt per municipi, sense segments que uneixin observacions independents. Una línia d'ajust eventual és descriptiva i no acredita causalitat.

L'anell utilitza 103.074 habitatges principals i 66.105 no principals, amb total 169.179. Les barres d'edats han de mantenir els tres grups i explicitar la base de normalització. En les dades conservades, els grups reconstrueixen el total; per a un altre territori s'ha de tornar a comprovar aquesta propietat.

| Interval d'habitatge no principal | Municipis |
| --- | ---: |
| De 0 a menys de 10% | 0 |
| De 10 a menys de 20% | 4 |
| De 20 a menys de 30% | 7 |
| De 30 a menys de 40% | 3 |
| De 40 a menys de 50% | 2 |
| De 50 a menys de 60% | 4 |
| De 60 a menys de 70% | 2 |

Table: Recompte de l'histograma de la demostració; els intervals sumen 22 municipis.

Els límits són decisions analítiques. El cas actual no té valors iguals o superiors a 70%, però una altra selecció podria necessitar ampliar-los. No s'ha de reutilitzar el mateix rang sense revisar-ne la cobertura.

# Sèrie temporal i piràmide

La sèrie del Padró té 23 observacions anuals, de 13.133 residents el 2000 a 22.681 el 2022. El 2021 hi figuren 22.522 residents. La piràmide censal de 2021 suma 11.443 homes i 11.338 dones, és a dir, 22.781 persones.

>>>> Padró i Cens són operacions diferents. Que tots dos fitxers continguin l'any 2021 no obliga les xifres a coincidir. No s'ha de substituir el valor de la sèrie ni alterar la piràmide per eliminar aquesta diferència.

La piràmide conserva 18 grups, de `0–4` a `85+`. Els signes negatius dels homes s'utilitzen per construir la representació; la lectura del recompte s'ha d'explicar amb valors absoluts. Les etiquetes buides d'alguns anys de la sèrie són intencionades per espaiar la retolació i no equivalen a dades de població absents.

# Revisió i exportació

Cal revisar cada gràfic amb les cel·les d'origen obertes: municipi, valor, unitat i nombre de marques. Després es comproven eixos, ordre, llegibilitat i rang de pàgina. Una estructura XLSX correcta o un PDF que s'obre no garanteixen que els textos i les escales comuniquin la variable adequada.

Les exportacions de consulta són a `outputs/figures/chapter-03` dins de l'execució del projecte. El procés exporta fulls de Calc a PDF i, per a quatre figures, deriva un SVG amb Inkscape. És una exportació vectorial, no una captura de la interfície. Les evidències docents de diàlegs de rangs i d'exportació s'han d'obtenir de la interfície real quan es documenti aquesta operació.

Cada equip conservarà una auditoria inicial/revisada i dues o tres figures candidates. La correcció ha de valorar la traçabilitat i la justificació de les decisions. La fase de color completarà els codis cromàtics; després, QGIS afegirà els mapes que la síntesi territorial necessiti.
