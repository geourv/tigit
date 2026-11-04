---
title: "Càlcul d'indicadors territorials: LLEGIU-ME del professorat"
lang: ca
ref: tigit-practica-02-docent
content_status: draft
recipient: docent
subject: "Tècniques d'informació geogràfica i turística"
subject_code: "21224102"
---

La pràctica relaciona la definició d'un indicador amb una operació revisable al llibre. La demostració utilitza els 22 municipis del Tarragonès i segueix Vila-seca, Roda de Berà i la Pobla de Mafumet com a casos de control. L'alumnat continua el seu propi llibre amb el territori assignat.

El professorat de teoria explica la relació entre numerador, denominador i ús de la mesura. Al laboratori es comproven referències, rangs, tipus, absències i agregats. El [capítol d'indicadors](https://geourv.github.io/tigit/ca/chapters/indicadors-territorials/) és la referència comuna; aquesta guia afegeix controls de la demostració i criteris d'intervenció.

# Preparació de la sessió

La sessió pressuposa una fita 01 revisada del mateix equip i territori, un full de càlcul instal·lat i components disponibles per a una comarca d'unes poques desenes de municipis. Per a primer curs convé construir una fórmula completa, comprovar-ne una fila i només després estendre-la. Es mantenen els equips i s'alternen operació, verificació i documentació.

| Component | Durada orientativa |
| --- | --- |
| Aula, indicadors seleccionats i agregació | 120–150 min |
| Treball autònom per estudiant, treballant en equip | 60–90 min |
| Preparació docent | 30–45 min |

Table: Estimació de la pràctica 02 amb la taula municipal ja validada.

Són estimacions no mesurades amb alumnat. Inclouen definició, fórmules, comprovacions i interpretació; no inclouen reconstruir una fita 01 incompleta ni les ampliacions. La preparació docent comprova les versions 01/02, les referències de tres municipis i els agregats; també conserva una còpia separada per mostrar un denominador nul o absent.

| Aturada | Comprovació | Pregunta de discussió |
| --- | --- | --- |
| Primera fórmula | Components, unitat, escala i denominador | Què representa el número 25 abans d'aplicar un format percentual? |
| Fórmula estesa | Claus, rangs, extrems i absències | Quin error pot quedar amagat darrere d'un resultat plausible? |
| Resum comarcal | Mateixa cobertura als dos components | Es vol descriure el parc d'habitatges de la comarca o el municipi mitjà? |

Table: Aturades per diagnosticar els indicadors.

Cal discutir doble multiplicació per 100, referències mal arrossegades, mitjanes no justificades i divisions per bases incompatibles. Una fórmula que es recalcula no resol `C07/C14`. La correcció ha de demanar a diferents membres de l'equip que expliquin numerador, denominador i limitació d'un resultat.

# Encaix de la qualificació

La [guia docent URV 2026/27 de TIGIT, 21224102](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&fitxa_apartat=61&any_academic=2026_27) fixa un 5% global per al conjunt d'activitats TIC d'aula, 30% per a presentacions/síntesi, 5% per al seguiment, 30% per a proves mixtes i 30% per a proves pràctiques. El 70–20–10 és aquí una rúbrica interna sobre 10, no el repartiment global de l'assignatura ni un percentatge de la guia atribuïble a cada Tasca.

Moodle ha d'indicar els apartats seleccionats, el pes concret dins del bloc corresponent i els requisits de superació aplicables. La guia de consulta mostra sis indicadors, però no tots han de ser obligatoris per defecte. La selecció ha de preservar els components i indicadors necessaris per als gràfics i QGIS. El cas de població/habitatge no substitueix els indicadors d'oferta turística que exigeixi el projecte de síntesi.

# Preparar Moodle

1. Crear o configurar una **Tasca** anomenada **TIGIT 02 · Indicadors i comparació territorial**.
2. Copiar a **Descripció** l'enunciat següent, de «Pregunta i punt de partida» fins al final de «Qualificació». Enumerar els codis B i els indicadors obligatoris comunicats a classe; no donar per exigits els sis només perquè apareixen al PDF.
3. Preservar per a 03/04 els components i els percentatges d'habitatge no principal i població de 65+, amb les seves claus. Si s'acota una operació necessària, indicar com es completarà abans de continuar.
4. Adjuntar a **Fitxers addicionals** el PDF d'alumnat «Càlcul d'indicadors territorials». El punt de partida és el llibre 01 propi de l'equip, no la solució 02. Els llibres docents 01/02, els controls municipals i la còpia d'errors són materials de preparació del professorat.
5. Revisar tramesa en grup, agrupament, dates, formats i mida. Configurar màxim 10 amb criteris de 7, 2 i 1 i el pes global corresponent; no duplicar una mateixa comparació al bàsic i a les ampliacions.
6. Comprovar la **vista d'estudiant**, l'adjunt, la selecció d'indicadors i els productes demanats. Si es comparteix la solució del Tarragonès, identificar-la com a exemple.

## Enunciat per copiar a la descripció

### Pregunta i punt de partida

Com es poden comparar municipis de mides diferents sense confondre volum i intensitat? Cal continuar, en el mateix equip i territori comarca–municipi, el llibre 01 validat. Les dades de població i habitatge són de 2021; la superfície conserva el període real i les limitacions documentades. Cal desar una còpia de continuació anomenada `tigit-02-indicadors-territorials.xlsx`.

### Treball bàsic —70%

El professor indica a classe els apartats i indicadors obligatoris i els enumera en aquesta Tasca. La guia completa ofereix un recorregut més ampli:

- **B1. Definició:** identificar pregunta, numerador, denominador, escala, unitat i límit de cada indicador seleccionat.
- **B2. Càlcul:** vincular components a `municipal`, construir fórmules comprovables i estendre-les amb controls de tipus, denominadors i referències.
- **B3. Agregació:** calcular els indicadors comarcals seleccionats a partir de sumes de components amb la mateixa cobertura; conservar aquests components al resum.
- **B4. Interpretació i continuïtat:** contrastar tres municipis, documentar absències i limitacions, reobrir el llibre i explicar què permet afirmar cada resultat. Per continuar calen les claus, els components i els percentatges d'habitatge no principal i població de 65+.

### Ampliacions —20%

Es pot desenvolupar una d'aquestes comparacions més enllà del treball seleccionat:

- **A1. Pes dels municipis en l'agregat.** Pregunta: què canvia entre el municipi mitjà i el conjunt del parc residencial? Es varia la ponderació dels percentatges municipals, mantenint dades i cobertura. La referència és la ràtio de sumes. Cal comparar mitjana simple i mitjana ponderada pels habitatges totals, comprovar que els pesos sumen 1 i que la ponderada coincideix amb la ràtio de sumes. La interpretació identifica quins municipis pesen més i quina pregunta respon cada mesura.
- **A2. Canvi de denominador residencial.** Pregunta: què expressa dividir residents entre tots els habitatges o només entre els principals? Es manté la població i es varia el denominador; la referència és residents per habitatge principal. Cal comprovar components d'habitatge, denominadors positius, unitats i tres municipis. La interpretació explica la diferència i per què cap de les dues ràtios és la grandària oficial de la llar ni una mesura directa d'ocupació turística.

Si una comparació ja és obligatòria, es puntua només al bàsic. Una ampliació ha d'afegir un contrast i una interpretació propis; no n'hi ha prou amb una columna o un indicador addicional sense controls.

### Productes, controls i documentació

Cal conservar els llibres 01 i 02, les fórmules, els components, `sources`, `dictionary`, `checks` i el registre d'equip. Per al lliurament es prepara el llibre 02 i uns apunts breus en PDF amb pregunta, resultats interpretats i captures d'una fórmula i d'un control. Moodle concreta si també cal adjuntar originals o el conjunt complet; les entrades de continuïtat es conserven igualment.

La verificació comprova una fila per municipi, cobertura comuna en numeradors i denominadors, percentatges sense doble conversió i agregats reconstruïbles. Les absències no es converteixen en zeros. La densitat continua condicionada per la compatibilitat temporal; habitatge no principal no significa habitatge turístic.

### Qualificació

**Bàsic: fins a 7 punts**, per definicions, fórmules, controls i interpretació dels apartats seleccionats. **Ampliacions: fins a 2 punts**, per pregunta, comparació controlada i conclusions justificades. **Documentació: fins a 1 punt**, per claredat, captures llegibles, atribucions i organització. Els màxims no són automàtics i el nombre de fitxers o fórmules no dona punts per si sol.

La documentació pot sumar sense ampliacions: bàsic i documentació complets poden arribar a 8/10. La correcció tècnica es valora al bàsic o a l'ampliació; el 10% valora la comunicació i l'organització sense repetir aquella puntuació. Les ampliacions no substitueixen els obligatoris. Aquesta és la nota interna; Moodle i la guia docent determinen el pes global i els requisits de superació.

# Entrades i solució de consulta

El punt de partida docent és la fita 01 resolta. El resultat de consulta és `tigit-02-indicadors-territorials-teaching.xlsx`, dins de la carpeta `data/processed` de l'execució del projecte pràctic. Cal conservar el llibre de la fita anterior per poder comparar què incorpora aquesta continuació.

El llibre 02 té 17 fulls i afegeix `indicators_demography`, `indicators_housing` i `indicators_summary`. Conserva 132 fórmules d'indicadors municipals —sis per cadascun dels 22 municipis— i vuit mesures agregades. Les 682 cel·les amb fórmula del llibre inclouen també els vincles i els càlculs heretats, no només aquests indicadors.

Els camps demogràfics de la demostració situen població total a `C`, població de 0–14 a `D`, població de 65+ a `E` i superfície a `F`. Els resultats ocupen `G:J`. Al full d'habitatge, `C` és població, `D` habitatges totals, `E` principals i `F` no principals; els resultats ocupen `G:H`.

# Seqüència de demostració

Cal començar amb una pregunta i formular què compara el denominador. A continuació es pot construir el pes de la població gran i contrastar-lo amb l'índex d'envelliment: comparteixen numerador, però no mesuren el mateix perquè divideixen per bases diferents.

1. Cal seguir una fila des de `municipal` fins a les cel·les vinculades del full d'indicadors.
2. Es construeix una divisió validada i es contrasta el resultat amb el càlcul dels components.
3. La fórmula s'estén al territori i es revisen claus, cobertura, extrems i denominadors.
4. Es comparen un percentatge municipal, la mitjana dels percentatges i el percentatge comarcal calculat amb sumes.
5. Es registra una interpretació limitada a allò que les dades permeten sostenir.

En una còpia de prova, un denominador zero o un component no numèric permeten observar per què cal distingir un resultat no calculable d'un zero real. No s'han d'introduir aquests casos artificials a la solució de consulta ni modificar els originals.

# Controls municipals

Els valors següents estan arrodonits per a la lectura. El llibre conserva més decimals. «Envelliment» expressa persones de 65+ per cada 100 de 0–14; «residents/principal» expressa residents per habitatge principal.

| Municipi | 0–14 (%) | 65+ (%) | Envelliment | Habitatge no principal (%) | Residents/principal |
| --- | ---: | ---: | ---: | ---: | ---: |
| Vila-seca | 18,2389 | 14,4858 | 79,4224 | 49,9053 | 2,6110 |
| Roda de Berà | 15,0126 | 21,5404 | 143,4823 | 64,7455 | 2,3160 |
| La Pobla de Mafumet | 21,4392 | 8,2097 | 38,2930 | 12,0743 | 2,8479 |

Table: Controls dels indicadors de població i habitatge del cas docent.

La densitat de Vila-seca resulta numèricament de dividir 22.781 residents per 21,64 km²: 1.052,7264 habitants/km². Aquest resultat continua sotmès a la incidència temporal `C07/C14`, perquè la superfície conservada correspon a una publicació de 2025. La comprovació aritmètica no acredita per si mateixa la compatibilitat del denominador.

# Controls comarcals i error d'agregació

| Mesura comarcal | Components | Resultat |
| --- | --- | ---: |
| Població total | Suma de 22 municipis | 262.868 persones |
| Habitatges totals | Suma de 22 municipis | 169.179 habitatges |
| Pes de 0–14 | 41.535 / 262.868 × 100 | 15,8007% |
| Pes de 65+ | 45.352 / 262.868 × 100 | 17,2528% |
| Índex d'envelliment | 45.352 / 41.535 × 100 | 109,1898 |
| Habitatge no principal | 66.105 / 169.179 × 100 | 39,0740% |
| Residents per principal | 262.868 / 103.074 | 2,5503 |

Table: Controls agregats calculats a partir de components compatibles.

La mitjana simple dels 22 percentatges municipals d'habitatge no principal és 35,7612%, diferent del 39,0740% comarcal. Aquest contrast és una demostració directa de l'efecte del denominador. Cal demanar quina pregunta respon cada operació, no presentar una mitjana com a errònia sense precisar-ne l'ús.

La vuitena mesura del resum és la densitat: 262.868 / 319,37 = 823,0829 habitants/km², igualment provisional per la compatibilitat de la superfície. Els altres resultats de població i habitatge no resolen aquesta incidència.

# Diagnòstics i criteris de revisió

Un percentatge aparent de milers pot indicar una doble conversió: la fórmula multiplica per 100 i la cel·la torna a aplicar un format percentual. Un canvi inesperat entre files pot provenir d'una referència mal arrossegada. Un resultat agregat plausible pot ocultar municipis omesos si `SUM` ha ignorat absències o text.

Els controls `C08:C13` documenten estructura, denominadors, components, fórmules, rangs percentuals i agregació. S'han de llegir juntament amb els components reals; els textos de control no substitueixen les comprovacions. `C07` i `C14` continuen visibles i no s'han de marcar com a resolts per haver obert o recalculat el llibre.

Per tancar la revisió cal comprovar un indicador de cada família, la correspondència de codis, la cobertura dels agregats i una interpretació escrita. L'habitatge no principal no és un indicador directe de turisme, i residents per habitatge principal no és la grandària oficial de la llar. La preparació deixa un llibre auditable per construir gràfics, sense atribuir causes que no s'han estudiat.
