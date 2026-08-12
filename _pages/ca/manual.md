---
layout: manual-home
title: Tècniques d'informació geogràfica i turística
description: >
  L'assignatura combina la representació gràfica de dades, la cartografia temàtica i l'ús bàsic dels sistemes d'informació geogràfica. Es treballarà amb dades oficials i obertes relacionades amb població, allotjament turístic, límits administratius i altres variables territorials d'interès. A partir d'aquestes fonts, l'estudiant aprendrà a construir indicadors simples que permetin descriure la distribució espacial de l'activitat turística, la seva intensitat relativa i la seva relació amb la població resident i amb el territori.
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

El curs parteix de dades territorials i turístiques i acaba amb una interpretació visual argumentada. Entre aquests dos extrems caldrà localitzar fonts fiables, preparar taules, construir indicadors, elaborar gràfics, entendre les dades espacials, unir informació a QGIS, dissenyar mapes temàtics i integrar els resultats en una infografia.

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
| Dades espacials i SIG | Límits municipals documentats i unió controlada amb la taula del llibre |
| Llenguatge cartogràfic | Mapa de localització de la comarca i base municipal llegible |
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

La guia docent 2026_27 defineix una avaluació continuada amb activitats de laboratori, presentació o exposició, atenció personalitzada, prova de continguts i prova pràctica. El manual explica com aquestes evidències es connecten amb el treball del curs, però les condicions exactes i les instruccions de lliurament s'han de consultar a Moodle.

::: table "Blocs d'avaluació indicats a la guia docent 2026_27"
| Activitat | Pes |
| --- | --- |
| Pràctiques a través de TIC en aules informàtiques | 5% |
| Presentacions / exposicions | 30% |
| Atenció personalitzada | 5% |
| Proves mixtes | 30% |
| Proves pràctiques | 30% |
:::

Aquest repartiment combina seguiment, comprensió conceptual, resolució pràctica i un producte de síntesi. No n'hi ha prou amb obtenir un mapa visualment agradable: cal poder justificar les dades utilitzades, els indicadors calculats, les unions realitzades, la classificació cartogràfica i la interpretació territorial proposada.

### Prova de continguts

La prova mixta comprovarà la comprensió dels conceptes i la capacitat d'aplicar criteris: interpretar indicadors, llegir gràfics, detectar problemes visuals, entendre sistemes de referència i valorar decisions cartogràfiques.

### Prova pràctica

La prova pràctica serà individual i comprovarà la resolució d'operacions essencials del flux de treball, des de la preparació d'una taula i el càlcul d'un indicador fins a la unió i simbolització de dades a QGIS.

### Infografia territorial

La infografia serà el producte de síntesi. Haurà d'integrar dades traçables, indicadors justificats, dues o tres figures, un o dos mapes i una interpretació breu dins d'una composició coherent elaborada amb Inkscape. La guia docent permet que aquest producte sigui individual o en grup segons indiqui el professorat, però no fixa una mida de grup. La composició dels equips, el format i les condicions concretes de la presentació es publicaran a Moodle.
