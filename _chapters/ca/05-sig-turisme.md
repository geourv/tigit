---
layout: manual-chapter
title: Sistemes d'informació geogràfica aplicats al turisme
description: Ús de QGIS per integrar dades, capes, unions, simbologia i síntesi visual en l'anàlisi turística.
lang: ca
ref: manual-gis-tourism
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/sig-turisme/
weight: 60
part: Continguts
manual_references: false
---

El bloc final del temari porta les dades i els criteris cartogràfics a un entorn SIG. QGIS permet treballar amb capes vectorials, taules d'atributs, serveis cartogràfics i unions de dades. En aquest curs, el SIG no és només una eina per fer mapes: és l'espai on es connecten dades turístiques, territoris administratius i decisions de representació.

El flux de treball començarà amb capes de límits administratius i taules externes preparades en el full de càlcul. La unió entre aquests dos mons es farà mitjançant codis territorials. Quan la unió funciona, cada municipi o comarca pot incorporar indicadors calculats prèviament i aquests indicadors poden simbolitzar-se cartogràficament.

Aquest capítol tanca el recorregut del manual perquè obliga a connectar totes les fases anteriors. Les dades no es poden unir si els codis no s'han preparat bé; els indicadors no es poden simbolitzar si no tenen sentit territorial; els mapes no es poden interpretar si el sistema de referència o la classificació són dubtosos. QGIS funciona aquí com un entorn d'integració, no com una solució automàtica.

## Capes, taules i unions

Les capes vectorials poden representar punts, línies o polígons. En el treball del curs, els polígons municipals o comarcals seran especialment importants perquè permeten representar indicadors agregats territorialment. Les taules externes aportaran dades estadístiques o turístiques que no tenen geometria pròpia, però que es poden vincular a una capa mitjançant un camp comú.

La taula d'atributs és el lloc on es pot comprovar si la unió ha funcionat. No n'hi ha prou amb veure que el mapa canvia de color: cal revisar quants registres han rebut valors, si hi ha camps nuls inesperats, si els tipus de dada són correctes i si els territoris sense informació tenen una explicació. Aquesta revisió és una pràctica de control de qualitat, no un tràmit.

::: table "Comprovacions bàsiques abans i després d'una unió a QGIS"
| Moment | Comprovació |
| --- | --- |
| Abans de la unió | El camp clau existeix a la taula i a la capa |
| Abans de la unió | Els codis tenen el mateix format i conserven zeros inicials |
| Després de la unió | No hi ha territoris esperats sense valor |
| Després de la unió | Els indicadors apareixen amb tipus numèric quan cal simbolitzar-los |
| Després de la unió | Una revisió visual confirma que el patró és plausible |
:::

## Simbolització i exportació

Un cop les dades estan incorporades a la capa, QGIS permet simbolitzar-les amb diferents estratègies: coropletes, símbols proporcionals, categories o altres formes segons el tipus de variable. Aquesta decisió ha de recuperar els criteris del capítol de cartografia temàtica. No es tracta de provar estils fins que un mapa sembli bonic, sinó de triar una representació coherent amb l'indicador.

L'exportació del mapa tampoc és un pas mecànic. El mapa ha de sortir amb mida, resolució, llegenda, títol, font i composició adequades per integrar-se en una infografia o document de síntesi. El producte final haurà de combinar mapes, gràfics i text breu per comunicar una interpretació territorial.

El projecte QGIS ha de conservar una organització llegible. Capes originals, capes transformades, taules unides i composicions finals han de tenir noms que permetin reconstruir el procés. Quan el projecte es desordena, és fàcil repetir càlculs, simbolitzar un camp antic o exportar una versió que ja no correspon a la interpretació final. La disciplina d'arxiu forma part de la competència SIG.

::: table "Rastre mínim del projecte SIG"
| Element | Què ha de permetre revisar |
| --- | --- |
| Capes originals | Font, sistema de referència i geometria inicial |
| Taules preparades | Camps clau, indicadors i unitats |
| Capes amb unions | Correspondència entre territori i dades |
| Estils o simbologia | Variable representada, classes i paleta |
| Composicions exportades | Mida, font, llegenda i versió final |
:::

## Síntesi visual

La síntesi visual és el moment en què l'estudiant ha de demostrar que entén el flux complet. Les dades han d'estar preparades, els indicadors han de ser interpretables, els mapes han de ser cartogràficament coherents i el text ha d'explicar el resultat sense exagerar-lo.

El criteri de qualitat no serà només visual. Un bon producte final ha de deixar rastre del procés: fonts utilitzades, decisions de càlcul, unions, sistemes de referència, classificació cartogràfica i justificació del missatge principal.

La síntesi final hauria de funcionar com una resposta a una pregunta territorial, no com una col·lecció de peces independents. Un mapa pot mostrar el patró espacial, un gràfic pot reforçar una comparació i un text breu pot formular la interpretació. Quan aquests tres elements expliquen coses diferents, el producte perd força. Quan es coordinen, l'estudiant demostra que sap convertir dades en una lectura turística del territori.

També cal deixar espai per a la incertesa. Les dades poden tenir limitacions, alguns territoris poden requerir cautela i una classificació alternativa podria matisar el resultat. Reconèixer aquests límits no debilita el treball; el fa més sòlid. En un ús professional de la informació geogràfica, una conclusió prudent i ben documentada és més valuosa que una afirmació contundent basada en un mapa poc revisat.
