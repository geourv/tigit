---
layout: manual-chapter
title: La representació de la Terra i els sistemes de referència
description: Geoide, el·lipsoide, coordenades, projeccions i sistemes de referència en el treball amb SIG.
lang: ca
ref: manual-earth-reference-systems
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/sistemes-referencia/
weight: 40
part: Continguts
manual_references: false
---

Quan treballem amb mapes digitals, la posició no és una dada neutra. Una coordenada només té sentit dins d'un sistema de referència, i una projecció cartogràfica sempre implica alguna forma de transformació. Aquest capítol introdueix els conceptes mínims perquè l'estudiant pugui entendre per què una capa apareix al lloc correcte, per què una altra pot aparèixer desplaçada i per què no és indiferent treballar amb un EPSG o amb un altre.

La Terra no és una esfera perfecta. Per representar-la en un pla cal utilitzar models i projeccions. En un curs aplicat al turisme no cal convertir aquesta qüestió en un tractat de geodèsia, però sí entendre'n les conseqüències pràctiques: distorsions, unitats de mesura, coordenades geogràfiques, coordenades projectades i coherència entre capes.

Aquest capítol fa de pont entre la visualització de dades i la cartografia. Fins ara hem parlat de taules, indicadors i gràfics; a partir d'aquí, la posició espacial entra com una condició tècnica. Un mapa digital només és fiable si les capes comparteixen un marc de referència coherent. Quan aquest marc falla, el problema no és estètic: afecta mesures, unions espacials, superposicions i interpretacions territorials.

## Coordenades i projeccions

Les coordenades geogràfiques expressen posicions mitjançant latitud i longitud. Són útils per localitzar punts en un sistema global, però no sempre són la millor opció per mesurar distàncies, superfícies o treballar amb cartografia local. En canvi, els sistemes projectats, com UTM, transformen la superfície terrestre en un pla i permeten treballar amb unitats mètriques.

La diferència entre localitzar i mesurar és important. Una coordenada en latitud i longitud pot situar un allotjament o un equipament turístic, però si el treball demana calcular superfícies, distàncies o densitats, cal revisar si el sistema de referència utilitzat és adequat. En cartografia temàtica, aquesta decisió es torna especialment sensible quan es combinen capes de procedència diferent.

::: table "Conceptes que cal distingir"
| Concepte | Paper en el treball cartogràfic |
| --- | --- |
| Geoide | Forma física aproximada de la Terra |
| El·lipsoide | Model matemàtic utilitzat per representar la Terra |
| Coordenades geogràfiques | Posició expressada en latitud i longitud |
| Projecció | Transformació de la superfície terrestre a un pla |
| EPSG | Codi que identifica un sistema de referència espacial |
:::

## Implicacions per a QGIS

QGIS pot mostrar capes amb sistemes de referència diferents, però això no elimina la necessitat d'entendre què està passant. Si una capa no té sistema assignat, si se li assigna un sistema incorrecte o si les coordenades s'han importat amb l'ordre canviat, el resultat pot ser aparentment misteriós: punts que apareixen lluny del territori esperat, capes que no encaixen o mesures incoherents.

>>>> Si els punts apareixen al Golf de Guinea, gairebé sempre hi ha un problema d'ordre X/Y o d'assignació del sistema de coordenades.

En el context de Catalunya, el treball cartogràfic habitual es farà amb ETRS89 / UTM zone 31N, identificat com EPSG:25831. Aquest criteri haurà de comprovar-se amb cada font de dades i amb cada capa utilitzada.

Cal distingir dues accions que sovint es confonen. Assignar un sistema de referència vol dir indicar a QGIS com ha d'interpretar unes coordenades que ja existeixen. Transformar o reprojetar una capa vol dir crear una nova geometria expressada en un altre sistema. Si s'assigna un EPSG incorrecte per "fer encaixar" una capa, el projecte pot semblar resolt a primera vista però quedar tècnicament contaminat.

::: table "Decisions habituals amb sistemes de referència"
| Situació | Decisió prudent |
| --- | --- |
| La capa té metadades clares d'EPSG | Respectar el sistema indicat i comprovar l'encaix visual |
| La capa no declara sistema de referència | Identificar-lo a la font abans d'assignar-lo |
| Les capes encaixen però les unitats no són mètriques | Valorar una reprojecció per a càlculs de distància o superfície |
| Els punts apareixen desplaçats | Revisar ordre de coordenades, separadors decimals i EPSG |
:::

El resultat esperat d'aquest bloc és que l'estudiant deixi de veure l'EPSG com un codi opac i comenci a entendre'l com una decisió de treball. Aquesta comprensió permet detectar errors abans que arribin a la fase de mapa temàtic, on una capa mal interpretada pot donar lloc a una conclusió territorial equivocada.
