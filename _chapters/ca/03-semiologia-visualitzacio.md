---
layout: manual-chapter
title: Semiologia gràfica i visualització de dades
description: Variables visuals, tipus de dades, gràfics, jerarquia i lectura crítica de representacions.
lang: ca
ref: manual-graphic-semiology
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/semiologia-visualitzacio/
weight: 40
part: Continguts
manual_references: true
---

Representar dades significa codificar-les visualment. Aquest capítol introdueix la semiologia gràfica a partir de taules i gràfics, abans d'aplicar-la al mapa. El color apareixerà com una variable visual, però el seu desenvolupament sistemàtic quedarà per al capítol de cartografia temàtica, un cop introduït el llenguatge propi del mapa. La idea d'un sistema de signes visuals parteix de la semiologia de Bertin i es pot connectar amb una introducció contemporània i aplicada a la visualització de dades {% cite bertinSemiologyGraphics2010 wilkeFundamentalsDataVisualization2019 %}.

## Codificació visual de les dades

### Dades qualitatives, ordinals i quantitatives

El tipus de dada condiciona les operacions de comparació possibles i la variable visual que convé utilitzar. Una dada **qualitativa** diferencia categories sense establir-ne necessàriament un ordre, com el tipus d'habitatge. Una dada **ordinal** forma categories ordenades, encara que la distància entre elles no sigui mesurable. Una dada **quantitativa** expressa magnituds sobre les quals tenen sentit determinades operacions numèriques. Distingir, ordenar i quantificar no són la mateixa tasca.

### Marques: punts, línies i àrees

Una representació es construeix amb **marques gràfiques**, elements visibles com punts, línies o àrees. En un gràfic poden ser una barra o un punt; en un mapa poden correspondre a un municipi, una carretera o una comarca. Les propietats que varien per codificar informació, com la posició, la mida, la forma, l'orientació, el valor, la textura o el color, s'anomenen **variables visuals**. Aquest llenguatge serà compartit després pels gràfics i pels mapes.

## Variables visuals

### Posició, longitud i mida

La posició i la longitud solen permetre comparacions quantitatives precises. La mida també pot expressar magnitud, però exigeix més esforç perceptiu.

### Forma, orientació i textura

Aquestes variables ajuden a diferenciar categories o patrons, però tenen limitacions per representar ordre o quantitat.

### Valor i color

La lluminositat i el color poden separar categories o suggerir intensitat. En aquest punt se n'introduirà la funció; les paletes i els models cromàtics es treballaran després sobre gràfics i mapes.

::: table "Tipus de dada, tasca de lectura i variables visuals"
| Tipus de dada | Tasca principal | Variables especialment adequades | Precaució |
| --- | --- | --- | --- |
| Qualitativa | Distingir categories | To, forma i, amb moderació, textura | No suggerir una jerarquia que les dades no tenen |
| Ordinal | Reconèixer un ordre | Posició ordenada, mida o lluminositat progressiva | L'ordre visual ha de coincidir amb l'ordre conceptual |
| Quantitativa | Comparar magnituds | Posició sobre una escala comuna, longitud i mida proporcional | Posició i longitud solen permetre estimacions més precises que l'àrea o una progressió de lluminositat; el to no expressa magnitud |
:::

La geometria de la marca també importa. Comparar dues barres alineades sobre el mateix origen és més directe que comparar l'àrea de dos cercles o dos sectors. Per això la representació més espectacular no és necessàriament la que permet respondre millor la pregunta.

### El principi de proporcionalitat de tinta

Quan una magnitud es representa mitjançant una superfície acolorida, la part visible d'aquesta superfície ha de variar en proporció amb la dada. Wilke anomena aquest criteri **principi de proporcionalitat de tinta**: una barra, un rectangle o una àrea ombrejada no només té un extrem situat sobre una escala, sinó també una extensió que el lector interpreta com a quantitat {% cite wilkeFundamentalsDataVisualization2019 %}. Si totes les barres comencen en un valor arbitrari, l'extrem pot coincidir amb la dada mentre que la longitud comunica una diferència exagerada.

::: subfigures a+b "Efecte de l'origen de l'eix sobre la proporcionalitat de les barres. Figures 17.1 i 17.2 de Claus O. Wilke, «Fundamentals of Data Visualization», originals sense modificar, CC BY-NC-ND 4.0."
![Gràfic de barres en què l'eix vertical comença a 50.000 dòlars i exagera les diferències d'ingressos entre comtats de Hawaii]({{ site.baseurl }}/assets/img/data-visualization/wilke-proportional-ink-truncated-axis.png "L'eix truncat exagera les diferències")
![Gràfic de barres amb les mateixes dades d'ingressos i un eix vertical que comença a zero]({{ site.baseurl }}/assets/img/data-visualization/wilke-proportional-ink-zero-axis.png "L'origen zero conserva la proporcionalitat")
:::

En una escala lineal, les barres que representen quantitats han de començar a zero. Aquesta regla no obliga que qualsevol eix comenci sempre a zero. Un gràfic de punts o una línia codifiquen el valor principalment mitjançant la posició i poden ampliar un interval per examinar una variació petita, sempre que l'escala sigui visible i no s'hi afegeixi una àrea ombrejada que converteixi la distància a l'origen en part del missatge. Si la pregunta demana comparar canvis, també es poden representar directament les diferències positives i negatives respecte d'una referència explícita.

## Gràfics segons la pregunta

### Un repertori per explorar alternatives

La pàgina [*Data Visualization Reference Guides*](https://coolinfographics.com/dataviz-guides), curada per Randy Krum, forma part de *Cool Infographics*, el lloc que acompanya i promociona el seu llibre *Cool Infographics: Effective Communication with Data Visualization and Design* {% cite krumCoolInfographics2013 krumDataVisualizationReferenceGuides2026 %}. El llibre desenvolupa el procés de disseny, la narració visual i la integració de dades, text i il·lustracions; el web n'ofereix informació, un capítol de mostra i figures, i amplia aquest entorn amb un directori posterior de selectors de gràfics, vocabularis visuals, catàlegs, matrius i llistes de comprovació.

El valor del directori no consisteix a proporcionar una resposta automàtica, sinó a mostrar que una mateixa taula pot admetre diverses representacions i que cada alternativa facilita unes lectures i en dificulta unes altres. Cal citar la pàgina quan s'utilitza aquesta selecció actualitzada de recursos i el llibre quan es treballa el plantejament general de la infografia; els pòsters i les guies externes conserven, a més, l'autoria i les condicions de cada productor.

![Capçalera del directori Data Visualization Reference Guides i primers recursos sobre principis, catàlegs i percentatges]({{ site.baseurl }}/assets/img/data-visualization/cool-infographics-dataviz-guides-2026-08-12.png "Fragment de «Data Visualization Reference Guides», Cool Infographics, directori curat per Randy Krum. Captura pròpia del 12 d'agost de 2026 per a comentari i docència. Avís del lloc: © 2023 Randy Krum, InfoNewt LLC; les miniatures incrustades pertanyen als titulars respectius."){: data-figure-width="44rem"}

Les guies del repertori parteixen de perspectives complementàries. El *Chart Chooser* d'Andrew Abela comença per allò que es vol mostrar; el *Financial Times Visual Vocabulary* agrupa formes segons relacions com desviació, correlació, ordre, distribució, canvi, composició, magnitud, espai i flux; i *From Data to Viz* comença per l'estructura de les variables i condueix cap a diverses possibilitats, cadascuna amb advertiments {% cite abelaChartSuggestions2006 financialTimesVisualVocabulary2018 holtzFromDataViz2018 %}. Cap d'aquests marcs substitueix el coneixement de les dades ni converteix una geometria en universalment correcta.

La selecció es pot entendre com un procés de sis decisions:

1. formular la pregunta i la comparació que haurà de fer el lector;
2. identificar si les dades són qualitatives, ordinals, quantitatives, temporals, espacials, jeràrquiques o relacionals;
3. distingir recomptes, percentatges, ràtios, densitats, índexs i canvis, amb els seus denominadors i unitats;
4. decidir si cal consultar valors exactes, comparar magnituds, observar una distribució, seguir una evolució, explorar una associació, explicar una composició o reconèixer un patró espacial o un flux;
5. considerar el públic, el suport, la mida final, l'accessibilitat i el context que necessita la lectura;
6. construir més d'una alternativa i comprovar quina respon millor a la pregunta sense deformar ni ocultar les dades.

Un selector de gràfics genera **candidats**, no un veredicte. Una taula pot ser preferible quan cal recuperar valors exactes; un gràfic ordenat facilita comparar municipis; i un mapa només és necessari quan la localització, la proximitat o el patró espacial formen part de la pregunta. Sovint mapa i gràfic es complementen: el primer conserva el context territorial i el segon permet una comparació més precisa.

### Comparar magnituds

Els gràfics de barres i altres representacions basades en posició o longitud permeten comparar territoris i categories quan l'ordenació i les unitats són clares.

### Composició, relació i distribució

La composició, la relació entre variables i la distribució d'un indicador demanen estructures gràfiques diferents. La tria ha de respondre a la pregunta, no a l'efecte visual més atractiu. Una sèrie temporal requeriria una estructura específica, però el projecte comarcal treballa principalment una comparació municipal per a un mateix període.

#### Composició

Una composició mostra com es reparteix un total entre parts compatibles. Les barres apilades al 100% permeten comparar diversos municipis sobre una mateixa escala, mentre que un gràfic circular només resulta manejable amb poques parts i un únic total. Abans de representar cal comprovar que les categories no se solapen i que, amb els arrodoniments admesos, reconstrueixen el total.

No qualsevol conjunt de percentatges forma una composició. El percentatge d'ocupació de diversos municipis conté taxes independents amb denominadors diferents i no ha de sumar 100%. En canvi, el repartiment de les pernoctacions comarcals per municipi sí que descriu parts d'un mateix total. També cal distingir un augment de 40% a 50%, que equival a 10 punts percentuals, d'un augment relatiu del 25% respecte del valor inicial.

Quan una magnitud es representa amb cercles o bombolles, és l'àrea i no el radi o el diàmetre el que ha de ser proporcional a la dada. Si un valor de referència $X_1$ es representa amb un diàmetre $D_1$, el diàmetre corresponent a $X_2$ és:

$$
D_2 = D_1\sqrt{\frac{X_2}{X_1}}
$$

Quadruplicar una dada només duplica el diàmetre, perquè així l'àrea es quadruplica. Fer el diàmetre directament proporcional al valor exageraria les diferències. Encara que l'escalat sigui correcte, l'àrea es compara amb menys precisió que una longitud alineada; per això els cercles són adequats per mostrar magnituds aproximades o patrons espacials, però necessiten una llegenda de mides o etiquetes quan cal llegir valors concrets {% cite krumSizingCircles2021 %}.

#### Relació entre dues variables

Un diagrama de dispersió situa cada municipi segons dos indicadors. La lectura ha de considerar la direcció, la forma i la intensitat aparent de l'associació, així com els casos que s'allunyen del patró general. Només s'hi poden incloure observacions amb tots dos valors disponibles, i una associació visual no demostra causalitat.

Quan diverses observacions comparteixen valors o queden molt pròximes, els punts es poden ocultar entre si. La transparència parcial permet detectar concentracions i un desplaçament aleatori molt petit pot separar coincidències exactes, però aquest desplaçament modifica la posició representada i s'ha de limitar i documentar. Amb conjunts molt grans pot ser preferible resumir la densitat en cel·les o corbes de nivell en lloc de dibuixar tots els punts {% cite wilkeFundamentalsDataVisualization2019 %}.

#### Distribució

Un diagrama de caixa resumeix la mediana, els quartils, la dispersió i els possibles valors extrems d'un indicador. Facilita una visió conjunta, però no mostra on es localitza cada municipi. Un valor assenyalat com a extrem no és automàticament un error: cal revisar la dada, el denominador i les característiques territorials abans d'interpretar-lo.

### Representar indicadors territorials

Valors absoluts, percentatges, ràtios i densitats necessiten títols, unitats i context suficients perquè no es confonguin entre si.

## Jerarquia i lectura crítica

### Títol, eixos, etiquetes i font

Un gràfic ha de poder-se interpretar sense reconstruir la taula original. El títol ha d'identificar la pregunta o la troballa sense afirmar més del que mostren les dades; el subtítol o una anotació poden aportar el context imprescindible. Les unitats, el període, el territori i la font han de ser visibles, i la precisió numèrica ha de correspondre a la qualitat de les dades i a la necessitat del lector. Les etiquetes directes redueixen el trajecte entre marca i llegenda quan l'espai ho permet {% cite schwabishCorePrinciples2018 evergreenDataVisualizationChecklist2018 %}.

Els elements auxiliars han d'explicar la comparació i no competir amb les dades. Les línies de quadrícula, els eixos, les marques i les vores poden ajudar a estimar valors o separar panells, però han de quedar en segon pla. El color necessita una funció definida, com agrupar, ordenar o destacar, i no ha de ser l'únic recurs per distingir informació essencial. El capítol 7 desenvoluparà les paletes i les comprovacions d'accessibilitat.

### Eixos truncats, tres dimensions i soroll visual

S'analitzaran recursos que exageren diferències, dificulten la comparació o amaguen el context, inclosos els gràfics tridimensionals i l'excés de categories. La lectura crítica no consisteix només a detectar una falsedat explícita: també ha de reconèixer decisions que orienten l'atenció o fan més difícil comprovar una comparació {% cite jonesHowLieCharts2000 tufteVisualDisplay2001 wilkeFundamentalsDataVisualization2019 %}.

![El mateix gràfic circular del 25% i el 75% vist des de quatre angles; la perspectiva altera l'àrea aparent dels sectors]({{ site.baseurl }}/assets/img/data-visualization/wilke-rotated-pie-3d.png "La tercera dimensió decorativa no representa cap dada i la perspectiva fa que un mateix sector sembli canviar de mida. Figura 26.1 de Claus O. Wilke, «Fundamentals of Data Visualization», original sense modificar, CC BY-NC-ND 4.0."){: data-figure-width="32rem"}

La tercera dimensió és especialment problemàtica quan només converteix sectors, barres o línies en objectes amb volum. La figura es projecta igualment sobre una pàgina o pantalla plana, de manera que la perspectiva deforma longituds i àrees i pot ocultar marques situades al darrere. Si una tercera variable és necessària, sovint es pot representar amb petits múltiples, posició en un segon gràfic, mida, forma o color sense perdre la possibilitat de comparar sobre un pla comú.

L'ús de 3D pot estar justificat quan l'objecte estudiat és realment tridimensional, com un relleu, i la forma espacial és part de la pregunta. Encara així, una vista estàtica pot amagar pendents o elements; una visualització interactiva, diverses perspectives o una alternativa amb corbes de nivell poden aportar controls de lectura. La precaució no consisteix a prohibir qualsevol 3D, sinó a exigir que la tercera dimensió comuniqui una dada necessària i no una decoració.

### Principis orientadors, no receptes

Les guies de visualització coincideixen en molts criteris de claredat i integritat, però les recomanacions depenen de la marca, la tasca i el suport. Convertir-les en prohibicions absolutes produiria errors nous: l'origen zero és essencial per comparar longituds de barres, però no per a qualsevol gràfic de línies; una quadrícula pot ser útil per estimar valors si queda en segon pla; i una llegenda continua sent necessària quan les etiquetes directes saturarien un mapa {% cite schwabishCorePrinciples2018 evergreenDataVisualizationChecklist2018 financialTimesVisualVocabulary2018 holtzFromDataViz2018 %}.

::: table "Principis per seleccionar i revisar una visualització"
| Principi | Aplicació | Matisació necessària |
| --- | --- | --- |
| Començar per la pregunta | Definir la comparació, el patró o el valor que el lector ha de trobar | El programa no decideix la pregunta ni la importància territorial |
| Respectar l'estructura de les dades | Distingir quantitats, categories, temps, espai, jerarquies i fluxos | Una mateixa estructura admet diverses geometries segons l'objectiu |
| Prioritzar comparacions precises | Preferir posició sobre una escala comuna i longitud quan cal discriminar valors pròxims | Àrea, angle i color poden servir per a patrons aproximats o altres tasques |
| Mantenir proporcions honestes | Fer que longituds, àrees i intervals representin correctament les dades | Les barres comencen a zero; punts i línies poden ampliar un rang justificat |
| Ordenar amb un criteri | Utilitzar magnitud, cronologia, grup, geografia o una seqüència conceptual | L'ordre alfabètic només és útil per localitzar, no sempre per comparar |
| Integrar text i gràfic | Fer coherents títol, anotacions, etiquetes, unitats i font amb el missatge | Etiquetar directament quan millora la lectura, sense omplir totes les marques |
| Subordinar l'estructura auxiliar | Reduir vores, quadrícules, marques i llegendes que competeixen amb les dades | No s'han d'eliminar els elements necessaris per estimar valors o separar panells |
| Donar funció al color | Utilitzar-lo per agrupar, ordenar o destacar i combinar-lo amb altres senyals | Cal comprovar contrast, mida final i visió cromàtica; el capítol 7 ho desenvolupa |
| Evitar comparacions ambigües | Mantenir escales comunes i separar mesures quan una doble escala vertical podria suggerir una relació artificial | Els panells coordinats o els petits múltiples solen fer explícites les unitats |
| Utilitzar mapes quan l'espai importa | Representar localització, proximitat, direcció o patrons territorials | Un gràfic ordenat és millor quan només cal comparar valors amb precisió |
| Conservar context i precisió adequats | Indicar període, territori, unitat, font, transformacions i absències | Més decimals i més dades no impliquen necessàriament més informació útil |
| Comparar alternatives | Mantenir constants la pregunta i les dades mentre canvia una decisió visual | La versió més atractiva no és necessàriament la més interpretable |
:::

### El laboratori de figures millorables

La comparació de gràfics circulars, radials, de barres, de línies, de dispersió i de bombolles no ha de servir per memoritzar un catàleg de formes. El seu valor consisteix a identificar què facilita i què dificulta cada geometria quan es manté una mateixa pregunta i una mateixa taula de partida.

::: table "Auditoria d'una figura millorable"
| Element | Pregunta |
| --- | --- |
| Pregunta | Quina comparació ha de poder fer el lector? |
| Dades | El tipus de variable, la unitat i el denominador són compatibles amb la geometria? |
| Tipus de gràfic | La geometria escollida permet fer aquesta comparació amb precisió? |
| Ordre | Les categories segueixen un criteri útil o només l'ordre original de la taula? |
| Escala | L'eix i el punt d'origen representen honestament les diferències? |
| Color | Codifica informació o només decora? |
| Text | El títol, les etiquetes i la precisió numèrica orienten la lectura sense repetir informació? |
| Context | Hi consten unitat, període, territori, font, transformacions i limitacions rellevants? |
| Accessibilitat | La mida, el contrast i la codificació continuen funcionant sense dependre només del color? |
| Soroll | Hi ha relleus, tres dimensions, icones o llegendes que dificulten la lectura? |
:::

Cada projecte partirà d'una figura funcional però millorable, identificarà almenys tres decisions problemàtiques i en construirà una versió alternativa amb el full de càlcul. La comparació entre l'original i la revisió haurà de justificar-se amb criteris perceptius, no amb preferències com “queda més bonic”.

### Procediment de construcció i revisió

Excel i Calc permeten produir gràfics ràpidament, però el resultat automàtic s'ha de revisar. El procediment es manté estable encara que canviï la interfície:

1. formular la pregunta territorial que haurà de respondre la figura;
2. seleccionar al full `indicators` els municipis, el període, la variable i la unitat corresponents;
3. comprovar que no s'hi han barrejat totals comarcals, files auxiliars ni valors absents convertits en zero;
4. escollir una geometria adequada a la comparació i ordenar les categories amb un criteri explícit;
5. construir almenys una alternativa que mantingui constants les dades i la pregunta;
6. revisar el títol, els eixos, les etiquetes, la llegenda, el color i la font a la mida prevista;
7. contrastar almenys dos valors representats amb les cel·les d'origen;
8. conservar el gràfic editable al llibre abans de generar-ne l'exportació vectorial.

## Formats de sortida per a les figures

Una figura es pot exportar com una imatge ràster o com un document vectorial. La diferència és important perquè els gràfics produïts al full de càlcul s'integraran i s'acabaran d'editar fora d'Excel {% cite wilkeFundamentalsDataVisualization2019 %}.

::: table "Formats habituals per exportar figures"
| Família | Formats | Propietats | Ús en el curs |
| --- | --- | --- | --- |
| Ràster | PNG, JPEG, TIFF | Graella de píxels; depèn de la resolució; el text deixa de ser text editable | Previsualitzacions, captures o fotografies, no màster dels gràfics |
| Vectorial | PDF, SVG, EPS | Formes geomètriques escalables; pot conservar línies, text i colors editables | Màster de gràfics i mapes per editar i compondre |
| Mixt | PDF o SVG amb imatges incrustades | Pot combinar vectors amb elements ràster | Cal inspeccionar el contingut, no només l'extensió |
:::

JPEG és inadequat per a gràfics amb text i línies perquè introdueix artefactes de compressió. PNG manté les vores netes però continua sent ràster. PDF serà el format vectorial d'intercanvi principal perquè Excel i LibreOffice Calc el poden generar i Inkscape el pot importar. SVG també és adequat quan la versió del programa permet exportar-lo correctament.

>>>> **Una extensió `.pdf` no garanteix que tot sigui vectorial.** Una captura de pantalla inserida dins d'un PDF continua sent una imatge de píxels. La figura s'ha de revisar ampliant-la molt o obrint-la a Inkscape i comprovant que barres, línies i textos es poden seleccionar com a objectes.

### Exportar des del full de càlcul

La interfície varia entre versions, però el procediment general és estable:

1. revisar títol, eixos, unitats, llegenda, font i mida final del gràfic;
2. col·locar el gràfic en un full propi o definir una àrea d'impressió que només contingui la figura;
3. exportar o imprimir la selecció com a PDF, sense convertir-la abans en captura;
4. obrir el PDF a Inkscape i comprovar formes, textos, tipografies i colors;
5. conservar la figura exportada i el llibre que permet regenerar-la.

Les figures són resultats intermedis i s'emmagatzemaran a `outputs/figures`. El document o infografia final que les integri s'exportarà més endavant a `dist`. Aquesta separació evita confondre una peça analítica amb el producte final de síntesi.

## Activitat: construir el conjunt de figures comarcals

La sessió pràctica partirà del full `indicators` del llibre comarcal. Els gràfics es crearan al full `charts` i continuaran vinculats a les cel·les d'origen. Cada figura haurà de respondre una pregunta sobre les diferències entre municipis o sobre el conjunt de la comarca. No es tracta de decorar la mateixa dada de moltes maneres, sinó de comprovar què permet veure cada geometria.

### Sèrie de gràfics bàsics

::: table "Figures que es construiran amb Excel o Calc"
| Figura | Dades adequades | Pregunta possible |
| --- | --- | --- |
| Barres simples ordenades | Percentatge d'habitatge no principal per municipi | Quins municipis presenten els valors més alts i més baixos? |
| Barres en paral·lel | Habitatges principals i no principals en valors absoluts | Com canvien el volum i la composició del parc residencial? |
| Barres apilades al 100% | Percentatges de població de 0–14, 15–64 i 65+ | Com varia l'estructura per edats entre municipis? |
| Circular | Habitatges principals i no principals del total comarcal | Quina composició té el conjunt de la comarca? |
| Anell | La mateixa composició que el circular | El buit central aporta informació o només decoració? |
| Dispersió | Percentatge de 65+ i percentatge d'habitatge no principal | Hi ha una associació visible entre tots dos indicadors? |
| Boxplot | Un indicador per a tots els municipis de la comarca | Quin és el centre, la dispersió i els possibles casos extrems? |
:::

El gràfic circular i el d'anell representaran intencionadament la mateixa composició per permetre'n una comparació crítica. No caldrà incorporar-los a la infografia final si una barra comunica millor la diferència. El boxplot resumeix la distribució municipal, però no identifica per si sol la posició geogràfica dels valors.

### Selecció de dues o tres figures

La sèrie completa serveix per aprendre i comparar. La miniinfografia només seleccionarà dues o tres figures que expliquin aspectes complementaris. Per a la demostració del Tarragonès, una combinació coherent seria:

1. barres apilades al 100% per comparar l'estructura d'edats;
2. barres ordenades del percentatge d'habitatge no principal;
3. dispersió entre envelliment i habitatge no principal, només si la relació aporta una lectura interpretable.

La tercera figura no és obligatòria si repeteix el mapa o no aporta una pregunta nova. Seleccionar també significa descartar.

### Organització i noms

Cada figura tindrà un nom semàntic i una versió vectorial PDF. Una possible estructura és:

```text
outputs/figures/
  age_structure_tarragones_2021.pdf
  non_principal_housing_tarragones_2021.pdf
  ageing_vs_non_principal_housing_tarragones_2021.pdf
```

L'any i el territori s'adaptaran a les dades reals. No s'utilitzaran noms com `grafico1.pdf` o `final.pdf`. Si una figura es revisa, s'ha de poder regenerar des del llibre de treball; no s'ha de corregir únicament el PDF i perdre la relació amb les dades.

### Control de qualitat abans d'exportar

Abans d'acceptar una figura cal comprovar que el nombre de marques correspon als municipis o categories previstos, que les unitats coincideixen amb el diccionari del llibre i que els valors absents no han passat a ser zeros. Les composicions percentuals han de reconstruir el total dins del marge d'arrodoniment, i les barres basades en longitud han de començar ordinàriament a zero; qualsevol excepció requeriria una altra geometria o una justificació explícita.

La revisió també es farà a la mida final. El text, els símbols i els traços han de continuar sent llegibles fora de la interfície del full de càlcul. Després de l'exportació, el PDF s'obrirà a Inkscape per verificar que les formes i els textos continuen sent objectes vectorials seleccionables.

### Evidències que s'han de conservar

::: table "Evidències de la visualització comarcal"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/processed` | El mateix llibre de treball | Taules, indicadors i gràfics editables al full `charts` |
| `outputs/figures` | PDFs vectorials | Una figura per pregunta, amb títol, unitat, període i font |
| `outputs/figures` | Alternatives comparables | Circular/anell o figura inicial/revisada quan ho requereixi l'activitat |
| `README.md` | Registre de figures | Fitxer, pregunta, tipus de dada, marca, variable visual, decisió de selecció i limitació principal |
:::

El resultat serà un conjunt de gràfics revisats i dues o tres figures candidates per a la mateixa miniinfografia comarcal, cadascuna associada a una pregunta i a un indicador. S'haurà de poder explicar quines variables visuals utilitza, què permet veure i quins límits conserva. Els capítols 4–7 desenvoluparan els components espacials abans d'integrar-los amb aquestes figures a la composició final.
