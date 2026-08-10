---
layout: manual-chapter
title: Llenguatge cartogràfic i cartografia temàtica
description: Elements del mapa, variables visuals, classificació de dades i criteris per construir cartografia temàtica.
lang: ca
ref: manual-thematic-cartography
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/cartografia-tematica/
weight: 50
part: Continguts
manual_references: false
---

Un mapa temàtic és una argumentació visual sobre el territori. No mostra només on són les coses; mostra una manera de classificar, comparar i interpretar una variable. Per això el llenguatge cartogràfic és una part central del curs. Escala, orientació, llegenda, retolació, color, classificació i normalització no són detalls de presentació: són decisions que afecten la lectura.

En turisme, la cartografia temàtica pot ajudar a veure concentracions d'oferta, intensitats relatives, contrastos entre municipis, distribucions comarcals o relacions entre població resident i allotjament. Però també pot exagerar diferències, amagar denominadors o suggerir patrons que depenen més de la classificació que de la dada.

Aquest capítol recupera decisions preses abans. L'indicador calculat al full de càlcul, el criteri visual treballat amb gràfics i el sistema de referència de les capes condicionen la qualitat del mapa. La cartografia temàtica no és una fase separada del procés: és el lloc on totes aquestes decisions es fan visibles alhora.

## Elements del mapa

Cada mapa ha de permetre que el lector entengui què mira, on ho mira i amb quin criteri s'ha representat. La llegenda ha d'explicar la variable i les classes; l'escala ha de ser adequada al territori; la retolació ha de donar context sense saturar; i l'orientació, la font i altres elements auxiliars han de reforçar la lectura, no carregar la composició.

El títol hauria d'expressar la variable, el territori i, quan calgui, el període o la unitat de mesura. Una llegenda amb intervals poc clars o amb unitats absents obliga el lector a endevinar. Una font mal indicada impedeix revisar l'origen de la informació. Aquests elements poden semblar secundaris mentre es treballa a QGIS, però són els que permeten que el mapa circuli fora del projecte i continuï sent comprensible.

::: table "Elements cartogràfics i funció comunicativa"
| Element | Funció |
| --- | --- |
| Títol | Presentar la variable i el territori representat |
| Llegenda | Explicar classes, símbols i unitats |
| Escala | Situar distàncies i nivell de detall |
| Retolació | Identificar llocs sense ocultar la variable principal |
| Font | Fer visible l'origen de les dades |
:::

## Classificació i color

La classificació de dades quantitatives és una de les decisions més delicades en cartografia temàtica. Canviar el nombre de classes, el mètode de tall o la paleta pot modificar la lectura del mapa. Per això cal distingir entre valors absoluts i valors normalitzats, i cal justificar quan s'utilitzen coropletes, símbols proporcionals o altres formes de representació.

Les paletes seqüencials són adequades per representar intensitat o densitat; les divergents, per mostrar desviacions respecte d'un valor de referència; i les qualitatives, per distingir categories. El criteri visual ha d'estar subordinat al criteri territorial: el mapa ha de fer llegible la dada, no només produir una imatge atractiva.

La tria entre coropletes i símbols proporcionals mereix una atenció especial. Les coropletes funcionen bé amb ràtios, percentatges o densitats associades a àrees; en canvi, poden ser enganyoses per representar volums totals, perquè la mida del territori influeix molt en la percepció. Els símbols proporcionals poden representar quantitats absolutes, però necessiten una escala visual llegible i una col·locació que no amagui el territori.

::: table "Representació cartogràfica segons el tipus de variable"
| Tipus de dada | Forma habitual | Risc que cal controlar |
| --- | --- | --- |
| Valor absolut | Símbols proporcionals o punts agregats | Domini visual dels territoris amb més volum |
| Percentatge o ràtio | Coropleta seqüencial | Interpretar intensitat com si fos volum |
| Desviació respecte d'un valor | Coropleta divergent | Amagar quin és el punt de referència |
| Categoria | Paleta qualitativa | Fer servir massa colors o categories |
:::

## Composició i jerarquia

La composició final del mapa ha de conduir la mirada. El territori i la variable representada han de tenir prioritat visual; la resta d'elements han d'ajudar a interpretar-los. Això implica controlar marges, mida de la llegenda, jerarquia tipogràfica, pes de les línies, retolació i relació entre mapa principal i elements de context.

Quan el mapa s'integra en una infografia o en un document de síntesi, la composició ha de dialogar amb gràfics i text. Inkscape o una altra eina de composició poden servir per ajustar aquesta relació, però el disseny no ha de tapar la decisió cartogràfica. Un bon resultat no és el que acumula més recursos visuals, sinó el que fa visible el patró territorial amb menys ambigüitat.

## Lectura crítica

La cartografia temàtica aplicada al turisme ha de ser especialment prudent amb les comparacions. Un municipi petit pot aparèixer molt intens si es calcula una ràtio determinada; un municipi gran pot dominar un mapa de valors absoluts; i una classificació massa agressiva pot convertir diferències petites en contrastos visuals excessius.

L'estudiant haurà d'aprendre a preguntar què mesura exactament el mapa, quin denominador utilitza, quins territoris són comparables i quines limitacions cal mencionar abans d'interpretar el patró espacial.

La lectura crítica també inclou explicar allò que el mapa no pot demostrar. Un patró espacial pot suggerir una relació amb accessibilitat, litoralitat, concentració hotelera o dimensió urbana, però el mapa no converteix aquesta relació en causalitat. El text que acompanya el mapa ha de formular interpretacions prudents i assenyalar quines dades addicionals caldrien per confirmar-les.
