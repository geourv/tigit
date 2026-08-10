---
layout: manual-chapter
title: Presentació
description: Orientació general del curs, ús del manual, guia docent, estructura, avaluació i bibliografia.
lang: ca
ref: manual-orientation
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/presentacio/
weight: 10
part: Orientació
manual_references: false
---

Aquest primer capítol explica com s'ha de llegir el manual i quin lloc ocupa dins de l'assignatura. No desenvolupa encara els continguts tècnics del curs. La seva funció és deixar clar el marc de treball: què diu la guia docent, com s'organitzen els capítols, quin paper té Moodle, quines dades i eines apareixeran al llarg del quadrimestre, com s'avaluarà el procés i on es concentra la bibliografia general.

La idea central és senzilla. L'assignatura no tracta només d'aprendre a fer gràfics o mapes, sinó d'utilitzar dades territorials i turístiques per construir una interpretació visual raonada. Això demana eines, però també criteri: entendre què mesura un indicador, quan una comparació és legítima, quin sistema de referència s'està utilitzant, quin tipus de mapa ajuda a llegir una distribució i com es comunica el resultat sense exagerar-lo.

## Com usar aquest manual

El manual és el text de treball estable del curs. Moodle continuarà sent l'espai viu de gestió docent: allí hi haurà els avisos, les dates concretes, els lliuraments, les qualificacions i qualsevol ajust que depengui del calendari. El manual, en canvi, ha d'explicar què s'ha de fer, per què es fa, quin criteri tècnic hi ha darrere de cada decisió i com es pot reconèixer un resultat ben resolt.

L'estudiant hauria de llegir cada capítol com una peça d'un procés. Abans de la sessió, el text ajuda a situar el problema. Durant el laboratori, serveix per tornar al procediment i als criteris. Després de treballar amb les dades o amb QGIS, permet revisar si el resultat és coherent amb la decisió que s'havia de prendre. Aquesta manera de llegir evita que el curs es converteixi en una successió de receptes de programari.

Per al professorat, el manual té una funció de coordinació. Cada capítol hauria de fer visible quin concepte correspon treballar en teoria, quina acció toca supervisar al laboratori i quina evidència pot revisar-se després. La teoria i la pràctica no s'han de duplicar: s'han d'alinear.

## Guia docent 2026_27

La guia docent oficial és la referència normativa de l'assignatura. Aquest manual la desplega en forma de materials, explicacions i criteris de treball, però no la substitueix. Si hi ha discrepàncies sobre dates, percentatges, condicions d'avaluació o instruccions administratives, preval la guia docent i les indicacions publicades a Moodle.

::: table "Dades identificatives de la guia docent 2026_27"
| Camp | Valor |
| --- | --- |
| Assignatura | Tècniques d'informació geogràfica i turística |
| Codi | 21224102 |
| Ensenyament | Grau en Gestió en Turisme i Hoteleria |
| Curs | Primer |
| Període | 1Q |
| Crèdits | 6 ECTS |
| Departament | Geografia |
:::

La descripció general de la guia situa el curs en la representació gràfica de dades, la cartografia temàtica i l'ús bàsic dels sistemes d'informació geogràfica. També concreta que es treballarà amb dades oficials i obertes sobre població, allotjament turístic, límits administratius i altres variables territorials. Aquesta orientació encaixa amb un flux progressiu: preparar dades, calcular indicadors, unir taules amb capes cartogràfiques, elaborar mapes i construir una síntesi visual.

## Estructura del temari

Els noms dels capítols principals segueixen el temari de la guia docent 2026_27. El tema 0 és aquesta presentació; els temes 1 a 5 despleguen els continguts tècnics i conceptuals del curs.

::: table "Temari oficial i funció dins del manual"
| Tema | Títol | Funció dins del manual |
| --- | --- | --- |
| 0 | Presentació | Situar guia docent, ús del manual, organització, avaluació i bibliografia general |
| 1 | Dades territorials, informació turística i indicadors | Preparar fonts de dades, codis territorials, depuració i indicadors |
| 2 | Representació de la informació: gràfics, color i lectura visual de dades | Triar gràfics, variables visuals, color i criteris de llegibilitat |
| 3 | La representació de la Terra i els sistemes de referència | Entendre geoide, el·lipsoide, coordenades, projeccions i EPSG |
| 4 | Llenguatge cartogràfic i cartografia temàtica | Construir mapes temàtics llegibles i honestos |
| 5 | Sistemes d'informació geogràfica aplicats al turisme | Integrar taules, capes, unions, simbologia i síntesi visual en QGIS |
:::

![Flux de treball del curs]({{ site.baseurl }}/assets/diagrams/manual-flow.mmd "Flux de treball del curs: de les dades territorials i turístiques a la síntesi visual")

## Dades, eines i organització del treball

El curs treballarà amb dades reals. Això vol dir que una part de l'aprenentatge consistirà a conviure amb codis, formats, taules incompletes, camps que no encaixen a la primera i decisions de normalització que condicionen la lectura final. El full de càlcul servirà per preparar i revisar dades; QGIS, per vincular-les espacialment i simbolitzar-les; i les eines de composició visual, per donar forma al producte final.

::: table "Eines principals i paper dins del curs"
| Eina | Paper dins del curs |
| --- | --- |
| Full de càlcul | Depurar dades, tractar codis territorials, calcular indicadors i preparar gràfics |
| QGIS | Unir taules i capes, simbolitzar indicadors i elaborar mapes temàtics |
| Fonts oficials de dades | Proporcionar població, allotjament turístic, límits administratius i variables territorials |
| Programari de composició | Integrar mapes, gràfics i text breu en una síntesi visual |
| Moodle | Gestionar avisos, terminis, lliuraments, qualificacions i instruccions operatives |
:::

L'organització dels fitxers forma part del treball tècnic. Un projecte GIS mal ordenat és difícil de revisar i encara més difícil de corregir. Per això convé mantenir una estructura mínima i estable des del primer exercici.

![Estructura recomanada de carpetes]({{ site.baseurl }}/assets/diagrams/project-folders.puml "Estructura recomanada de carpetes per al treball del curs")

## Avaluació i seguiment

La guia docent 2026_27 defineix una avaluació continuada amb activitats de laboratori, presentació o exposició, atenció personalitzada, prova de continguts i prova pràctica. El manual pot explicar quina mena d'evidències s'esperen i com es connecten amb el treball del curs, però les condicions exactes i les instruccions de lliurament s'han de consultar a Moodle.

::: table "Blocs d'avaluació indicats a la guia docent 2026_27"
| Activitat | Pes |
| --- | --- |
| Pràctiques a través de TIC en aules informàtiques | 5% |
| Presentacions / exposicions | 30% |
| Atenció personalitzada | 5% |
| Proves mixtes | 30% |
| Proves pràctiques | 30% |
:::

Aquest repartiment mostra que el curs combina seguiment, productes aplicats, comprensió conceptual i resolució pràctica. No n'hi ha prou amb obtenir un mapa visualment agradable: l'estudiant ha de poder justificar les dades utilitzades, els indicadors calculats, les unions realitzades, la classificació cartogràfica i la interpretació territorial que proposa.

## Bibliografia general

La guia docent inclou bibliografia bàsica i complementària sobre cartografia, lectura de mapes, visualització de dades, color, gràfics i sistemes d'informació geogràfica. En aquest manual, la bibliografia general es mantindrà en una pàgina pròpia perquè les cites es puguin gestionar amb BibTeX i perquè cada capítol pugui activar només les referències que necessita.

El criteri és que les lectures no apareguin com una llista decorativa. Quan una idea del manual depengui d'una font, la cita ha d'aparèixer prop del fragment que la necessita. La pàgina de bibliografia servirà com a índex general de lectures, però els capítols han de mostrar per què una lectura és útil en aquell punt del procés.

## Estat editorial

La versió catalana és la font de treball principal. Les versions en altres idiomes es prepararan quan el contingut català estigui revisat i marcat com `content_status: approved`. Aquesta norma evita multiplicar esborranys inconsistents mentre el curs encara està prenent forma.
