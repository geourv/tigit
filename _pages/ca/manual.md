---
layout: manual-home
title: Tècniques d'informació geogràfica i turística
description: >
  L'assignatura combina la preparació de dades, la visualització, el color, la cartografia i l'ús bàsic dels sistemes d'informació geogràfica. Es treballarà amb dades oficials i obertes relacionades amb població, allotjament turístic, límits administratius i altres variables territorials d'interès. A partir d'aquestes fonts, l'estudiant aprendrà a construir indicadors simples que permetin descriure la distribució espacial de l'activitat turística, la seva intensitat relativa i la seva relació amb la població resident i amb el territori.
lang: ca
ref: home
profiles: [unaltremanual]
content_status: draft
permalink: /ca/
nav: false
show_chapter_index: false
cover_image: /assets/img/manual-cover-cat.png
cover_alt: Manual de Tècniques d'informació geogràfica i turística
figure_captions: true
---

## Orientació del curs

Aquest és el punt de partida de l'assignatura. Presenta els aprenentatges previstos, la relació entre les sessions de teoria i de pràctiques, el paper d'Excel, QGIS i Inkscape, i les evidències que permetran comprovar el progrés.

La idea central és senzilla. L'assignatura no tracta només d'aprendre a fer gràfics o mapes, sinó d'utilitzar dades territorials i turístiques per construir una interpretació visual raonada. Els indicadors resultants poden servir per divulgar una realitat, comparar territoris, seguir objectius, orientar decisions o formular noves preguntes. Això demana eines, però també criteri: entendre què mesura un indicador, quan una comparació és legítima, quin sistema de referència s'està utilitzant, quin tipus de mapa ajuda a llegir una distribució i com es comunica el resultat sense exagerar-lo.

## Recorregut de l'assignatura

El curs parteix de dades territorials i turístiques i acaba amb una interpretació visual argumentada. Entre aquests dos extrems caldrà localitzar fonts fiables, preparar taules, construir indicadors, elaborar gràfics, entendre el color, llegir les bases cartogràfiques, treballar amb QGIS, dissenyar mapes temàtics i integrar els resultats en una infografia.

L'ordre del manual no separa teoria i laboratori en blocs independents. Primer es construeix la base de dades i indicadors; després s'estudia com es codifiquen visualment les dades i per què el color és una decisió transversal que afecta gràfics, mapes, accessibilitat i composició. A continuació s'introdueixen la Terra, les coordenades i el llenguatge cartogràfic. QGIS pot aparèixer abans com a demostració curta per veure una capa, una escala o una composició, però el bloc sistemàtic de SIG arriba quan l'estudiant ja sap què vol representar i quins errors ha d'evitar. La cartografia temàtica aplicada queda després de la integració SIG perquè necessita unir dades i geometries abans de classificar i simbolitzar.

>>>> **Figures i drets d'ús.** El manual és una versió de treball. Algunes figures provenen de recursos oberts o de captures documentades i incorporen autoria, font i condicions d'ús al peu; altres són esquemes propis construïts per substituir materials antics de les diapositives. Quan una imatge de suport encara no ofereix garanties suficients de font, llicència o adequació, no s'ha d'entendre com a material reutilitzable fora del context docent fins que el peu n'indiqui explícitament l'origen i les condicions. Aquesta cautela no canvia el criteri de lectura: cada figura s'ha d'interpretar pel concepte que ajuda a entendre, no com una decoració ni com una autorització genèrica de reproducció.

### Un cicle de descobriment de coneixement territorial

Aquest recorregut s'inspira en el procés de **descobriment de coneixement en bases de dades**, conegut per les sigles KDD. [Fayyad, Piatetsky-Shapiro i Smyth](https://dblp.org/rec/journals/aim/FayyadPS96) van distingir cinc grans fases: selecció, preprocessament, transformació, mineria de dades i interpretació o avaluació. Aquestes fases formen part d'un procés interactiu que també depèn del coneixement del domini, dels objectius i de l'ús posterior dels resultats. La mineria de dades n'és una fase possible, no un sinònim de tot el procés.

El manual adapta aquest marc a un curs introductori d'informació territorial. La selecció crítica de fonts, la depuració del llibre, la construcció d'indicadors, les unions espacials, els gràfics, els mapes i la infografia formen un cicle que produeix representacions i resultats interpretables. No totes les activitats constitueixen mineria de dades ni produeixen un descobriment científic nou. El valor del marc és recordar que un resultat útil depèn de tot el procés i que una incoherència detectada al final pot obligar a revisar la pregunta, la font o la preparació inicial.

### Una pregunta territorial com a fil conductor

Les eines no s'aprendran com una col·lecció de funcions independents. Cada operació haurà de respondre una pregunta: quina comparació es vol fer, quina dada la permet, quin indicador és adequat i quina representació ajuda a comunicar el resultat sense exagerar-lo.

El manual desenvoluparà una diagnosi de **població i habitatge d'una comarca tarragonina**. La demostració comuna utilitzarà els municipis del Tarragonès i dades de l'Idescat de 2021. El projecte començarà amb una pregunta, continuarà amb un únic llibre de càlcul i acabarà amb una miniinfografia formada per tres o quatre mètriques, dues o tres figures, un mapa de context, un mapa temàtic i una interpretació breu.

::: table "Fil acumulatiu del projecte comarcal"
| Fase | Resultat que es reutilitza |
| --- | --- |
| Fonts i preparació | Un llibre amb dades originals importades, diccionari, comprovacions i una fila per municipi |
| Indicadors | Percentatges, ràtios i densitats calculats al mateix llibre |
| Gràfics | Sèrie de figures editables i selecció de dues o tres exportacions vectorials |
| Color | Registre cromàtic amb funcions, paletes, codis i proves d'accessibilitat |
| Dades espacials i llenguatge cartogràfic | Límits municipals documentats, escala, retolació i mapa de localització llegible |
| SIG | Projecte QGIS amb capes, taula importada, unió controlada i comprovacions |
| Cartografia temàtica | Mapa d'un indicador normalitzat, amb classificació i paleta justificades |
| Síntesi | Miniinfografia, fitxers de treball i explicació oral quan correspongui |
:::

### Cicle de treball del manual

![Cicle de treball del manual]({{ site.baseurl }}/assets/diagrams/manual-flow.mmd "Cicle adaptat de descobriment de coneixement territorial: de la pregunta i les dades a la interpretació i la comunicació")

## Metodologia de treball

### Teoria i pràctica en un mateix recorregut

Les sessions teòriques introduiran conceptes i criteris de decisió. Les pràctiques permetran aplicar-los amb dades i eines concretes. No formen dos cursos paral·lels: una fórmula d'Excel, una unió a QGIS o una decisió d'Inkscape només tenen sentit si es poden relacionar amb el problema explicat a teoria.

### Manual, Moodle i treball autònom

El manual és el text de treball estable del curs. Moodle continuarà sent l'espai viu de gestió docent: allí hi haurà els avisos, les dates concretes, els lliuraments, les qualificacions i qualsevol ajust que depengui del calendari. El manual explica què s'ha de fer, per què es fa, quin criteri tècnic hi ha darrere de cada decisió i com es reconeix un resultat ben resolt.

Cada capítol es pot llegir com una peça d'un procés. Abans de la sessió, el text ajuda a situar el problema. Durant el laboratori, serveix per tornar al procediment i als criteris. Després de treballar amb les dades, permet revisar si el resultat és coherent amb la decisió que s'havia de prendre.

Per al professorat, el manual té una funció de coordinació. Cada capítol ha de fer visible quin concepte correspon treballar en teoria, quina acció toca supervisar al laboratori i quina evidència es pot revisar després. La teoria i la pràctica no s'han de duplicar: s'han d'alinear.

## Marc de la guia docent

La guia docent oficial és la referència normativa de l'assignatura. Aquest manual la desplega en forma de materials, explicacions i criteris de treball, però no la substitueix. Si hi ha discrepàncies sobre dates, percentatges, condicions d'avaluació o instruccions administratives, preval la guia docent i les indicacions publicades a Moodle.

::: table "Dades identificatives de les guies docents 2026_27"
| Camp | Valor |
| --- | --- |
| Assignatura | Tècniques d'informació geogràfica i turística |
| Guia docent | [Grau en Geografia, Anàlisi Territorial i Sostenibilitat](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2123&assignatura=21234003&any_academic=2026_27) |
| Codi | 21234003 |
| Guia docent | [Grau en Gestió en Turisme i Hoteleria](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&any_academic=2026_27) |
| Codi | 21224102 |
| Curs | Primer |
| Període | 1Q |
| Crèdits | 6 ECTS |
| Departament | Geografia |
:::

## Eines i organització del treball

Cal familiaritzar-se amb el sistema de fitxers de l'ordinador: crear carpetes, reconèixer una ruta, moure i copiar fitxers, identificar una extensió i saber en quin dispositiu o servei està desat un document. Aquestes operacions formen part del treball acadèmic, encara que les aplicacions mòbils i els serveis al núvol sovint les ocultin.

::: table "Eines principals i paper dins del curs"
| Eina | Paper dins del curs |
| --- | --- |
| Full de càlcul | Depurar dades, tractar codis territorials, calcular indicadors i preparar gràfics |
| QGIS | Unir taules i capes, simbolitzar indicadors i elaborar mapes temàtics |
| Inkscape | Compondre la infografia i coordinar mapes, gràfics, textos i jerarquia visual |
| Fonts oficials de dades | Proporcionar població, habitatges, codis territorials, superfícies i límits administratius |
| Moodle | Gestionar avisos, terminis, lliuraments, qualificacions i instruccions operatives |
:::

### Fulls de càlcul recomanats

A les pràctiques es pot utilitzar qualsevol full de càlcul que permeti assolir els objectius i conservar un llibre interoperable. Es recomana **LibreOffice Calc** quan es vol treballar localment amb programari lliure. Quan cal editar al núvol o simultàniament, es recomana **Excel per al web dins de Microsoft 365** perquè la URV proporciona aquest entorn a la comunitat universitària.

La [guia d'Office 365 del CRAI](https://urv.libguides.com/Office365), actualitzada el febrer de 2026, documenta l'accés web a Excel i altres aplicacions, així com la possibilitat d'instal·lar les aplicacions d'escriptori fins a cinc ordinadors personals. La [guia institucional de OneDrive](https://urv.libguides.com/c.php?g=684760&p=4891187) descriu un espai personal URV al núvol, actualment de 1 TB, que permet crear, editar i compartir llibres d'Excel i treballar-hi simultàniament. S'hi accedeix mitjançant els serveis digitals de la URV, inclòs [virtual.urv.cat](https://virtual.urv.cat/). Les quotes, aplicacions i condicions poden canviar, de manera que s'ha de consultar la documentació institucional vigent.

Google Sheets, ONLYOFFICE, Apple Numbers i altres opcions també cobreixen operacions bàsiques, però no seran l'entorn de referència del manual. Si s'utilitzen, cal comprovar que fórmules, tipus, gràfics i exportacions es conserven quan el llibre s'intercanvia amb Calc o Excel.

### Saber on és el fitxer

Una aplicació pot mostrar un llibre sense fer evident on està desat. La llista de fitxers **recents** és només un índex d'accessos: no és una carpeta ni informa necessàriament de quin compte, dispositiu o núvol conté el fitxer. L'Escriptori tampoc no garanteix una ubicació local, perquè el sistema pot sincronitzar-lo amb OneDrive.

::: table "Ubicacions que no s'han de confondre"
| Ubicació | Com reconèixer-la | Risc que cal controlar |
| --- | --- | --- |
| Carpeta local | Té una ruta dins del disc de l'ordinador i es pot obrir amb el gestor de fitxers | Es pot perdre si falla o es canvia el dispositiu i no hi ha còpia |
| OneDrive personal | La sessió correspon a un compte particular | El grup pot dependre d'un compte aliè a la URV i d'un propietari únic |
| OneDrive URV | La sessió correspon al compte institucional i el fitxer apareix al OneDrive de la URV | L'accés depèn del compte institucional i dels permisos compartits |
| Carpeta sincronitzada | Té una ruta local però també un estat de sincronització al núvol | Pot ser només disponible en línia, estar pendent de pujada o generar conflictes |
| Escriptori o Baixades | La ubicació depèn de la configuració del sistema i del navegador | Acumula còpies, noms duplicats i fitxers difícils de tornar a localitzar |
:::

>>>> **“El veig a Recents” no demostra que se sàpiga on és.** Abans de començar cal identificar la ruta local o el compte de OneDrive, obrir la carpeta des del gestor de fitxers i comprovar el nom complet del llibre. Un OneDrive personal i el OneDrive proporcionat per la URV són espais diferents, encara que l'aplicació els mostri junts.

Per treballar amb seguretat, el projecte tindrà una carpeta arrel identificable. Després de la primera sessió s'ha de poder tancar l'aplicació, navegar fins a la carpeta sense usar **Recents** i tornar a obrir el llibre. Si es treballa al núvol, cal comprovar el compte actiu, els permisos de les persones participants i l'estat de sincronització abans d'apagar l'ordinador.

Compartir un enllaç no és el mateix que lliurar un fitxer. Quan Moodle demani un fitxer, s'ha de descarregar o exportar la versió correcta, verificar que s'obre fora de la sessió del navegador i trametre-la en el format indicat. Els enllaços compartits només substituiran el fitxer quan les instruccions ho demanin explícitament.

L'organització dels fitxers forma part del treball tècnic. Un projecte mal ordenat és difícil de revisar i encara més difícil de corregir. Per això convé mantenir una estructura mínima i estable des del primer exercici.

![Estructura recomanada de carpetes]({{ site.baseurl }}/assets/diagrams/reproducible-project-structure.puml "Estructura recomanada de carpetes per al treball del curs")

## Evidències d'aprenentatge

La guia docent 2026_27 defineix una avaluació continuada amb activitats de laboratori, presentació o exposició, atenció personalitzada, prova de continguts i prova pràctica. El manual explica com aquestes evidències es connecten amb el treball del curs, però les dates, els lliuraments concrets, el territori assignat i els enunciats operatius s'han de consultar a Moodle.

::: table "Blocs d'avaluació i desplegament del curs"
| Activitat | Pes | Organització principal |
| --- | --- | --- |
| Pràctiques a través de TIC en aules informàtiques | 5% | Seguiment, exercicis i evidències intermèdies segons Moodle |
| Presentació, exposició o infografia territorial | 30% | Primera convocatòria en trios mixtos de titulació; segona convocatòria individual i de mida reduïda |
| Atenció personalitzada | 5% | Participació, resolució de dubtes i incorporació de correccions |
| Prova mixta de continguts | 30% | Prova individual de comprensió teòrica i criteris d'aplicació |
| Prova pràctica de full de càlcul | 15% | Prova individual sobre preparació de dades, codis i indicadors |
| Prova pràctica de QGIS | 15% | Prova individual sobre unions, simbolització i resolució cartogràfica |
:::

Aquest repartiment combina seguiment, comprensió conceptual, resolució pràctica individual i un producte de síntesi. No n'hi ha prou amb obtenir un mapa visualment agradable: cal poder justificar les dades utilitzades, els indicadors calculats, les unions realitzades, la classificació cartogràfica i la interpretació territorial proposada.

L'avaluació continuada exigeix seguiment regular. Per mantenir l'itinerari ordinari de primera convocatòria cal assistir com a mínim al 80% de les sessions pràctiques, o justificar adequadament les absències, i lliurar les activitats o evidències intermèdies que indiqui Moodle. La manca de seguiment, d'assistència o de participació efectiva pot obligar a una recuperació individual específica en segona convocatòria.

Si l'assistència i el seguiment són suficients, però una activitat principal queda per sota de 4 sobre 10 o la nota mitjana no arriba a l'aprovat, la segona convocatòria se centrarà en les activitats o blocs suspesos. Això permet conservar la feina superada i recuperar només allò que no ha assolit el nivell mínim. Si no hi ha seguiment continuat o el projecte de síntesi no s'ha desenvolupat de manera verificable, la recuperació pot requerir una modalitat individual més completa.

### Prova de continguts

La prova mixta serà individual i comprovarà la comprensió dels conceptes i la capacitat d'aplicar criteris: interpretar indicadors, llegir gràfics, detectar problemes visuals, entendre sistemes de referència i valorar decisions cartogràfiques.

### Proves pràctiques

Les proves pràctiques seran individuals i es distribuiran en dues parts. La prova de full de càlcul comprovarà la preparació d'una taula, la gestió de codis territorials, el tractament de valors absents, el càlcul d'indicadors i la validació dels resultats. La prova de QGIS comprovarà la incorporació de dades, la unió amb capes territorials, la simbolització cartogràfica i la resolució de problemes aplicats.

### Infografia territorial

La infografia serà el producte de síntesi de primera convocatòria. Es farà en **trios** i els equips hauran de combinar estudiants de Geografia i de Turisme: no poden estar formats per tres persones de la mateixa titulació. Aquesta composició busca que el treball integre mirades territorials, turístiques, tècniques i comunicatives, no que cada membre treballe una peça aïllada sense entendre la resta.

La infografia haurà d'integrar dades traçables, indicadors justificats, dues o tres figures, un o dos mapes i una interpretació breu dins d'una composició coherent elaborada amb Inkscape. El treball en equip no elimina la responsabilitat individual: qualsevol membre ha de poder explicar les fonts, els càlculs, les unions, els mapes i les decisions visuals principals.

En segona convocatòria, quan calgui recuperar el projecte de síntesi, la infografia o document equivalent serà **individual** i de mida més reduïda. Moodle indicarà el territori, les dades, el format, el termini i els criteris concrets d'aquesta recuperació.

### Preguntes freqüents

::: table "Dubtes habituals sobre l'avaluació i el treball"
| Pregunta | Resposta curta |
| --- | --- |
| La infografia és individual o en grup? | En primera convocatòria és en trios; en segona convocatòria, si s'ha de recuperar, és individual i més petita. |
| Es pot fer un trio només de Geografia o només de Turisme? | No. Els trios han de combinar estudiants de les dues titulacions i no poden estar formats per tres persones de la mateixa titulació. |
| Les proves pràctiques són en grup? | No. Hi haurà una prova individual de full de càlcul del 15% i una prova individual de QGIS del 15%. |
| Què passa si una part queda per sota de 4? | No es pot compensar automàticament. Si hi ha seguiment suficient, en segona convocatòria es recuperaran les activitats o blocs suspesos. |
| Què passa si la mitjana no arriba a 5? | Si s'ha seguit l'avaluació continuada, es recuperaran les parts necessàries per arribar al nivell mínim. |
| L'assistència a pràctiques és obligatòria? | És necessària per mantenir l'itinerari ordinari d'avaluació continuada: cal arribar al 80% o justificar les absències. |
| Es pot lliurar només l'enllaç a un fitxer compartit? | Només si Moodle ho demana explícitament. Quan es demani un fitxer, cal lliurar la versió correcta i comprovar que s'obre fora de la sessió del navegador. |
| Com es comprova l'autoria d'un llibre de càlcul o projecte QGIS? | Amb originals, fonts, fórmules, comprovacions, versions intermèdies, fitxers de treball i explicacions orals quan calgui; les metadades del fitxer poden ser un indici, però no una prova suficient. |
:::
