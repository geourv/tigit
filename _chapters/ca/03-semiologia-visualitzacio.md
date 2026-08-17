---
layout: manual-chapter
title: Semiologia gràfica i visualització de dades
description: Variables visuals, tipus de dades, gràfics, retolació, jerarquia i lectura crítica de representacions.
lang: ca
ref: manual-graphic-semiology
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/semiologia-visualitzacio/
weight: 40
part: Continguts
manual_references: true
---

Representar dades significa codificar-les visualment. Aquest capítol introdueix la semiologia gràfica a partir de taules i gràfics, abans d'aplicar-la al mapa. El color apareixerà com una variable visual, però el seu desenvolupament sistemàtic quedarà per al capítol de teoria del color, perquè és una decisió transversal que afecta gràfics, mapes, accessibilitat i infografia. La classificació cartogràfica es treballarà més endavant, un cop introduït el llenguatge propi del mapa i la integració amb QGIS. La idea d'un sistema de signes visuals parteix de la semiologia de Bertin i es pot connectar amb una introducció contemporània i aplicada a la visualització de dades {% cite bertinSemiologyGraphics2010 wilkeFundamentalsDataVisualization2019 %}.

>>>>> En acabar el capítol, cal poder seleccionar, construir, revisar i exportar figures que responguin una pregunta territorial sense deformar les dades.
>>>>>
>>>>> - Explicar com les marques i les variables visuals codifiquen dades qualitatives, ordinals i quantitatives.
>>>>> - Distingir tasques de comparació, composició, distribució, relació, evolució, flux i localització.
>>>>> - Justificar un tipus de gràfic segons la pregunta, les dades, el públic, el suport i la mida final.
>>>>> - Construir al full `charts` figures editables i vinculades als indicadors d'origen.
>>>>> - Interpretar patrons i associacions sense convertir-los en causes o previsions no demostrades.
>>>>> - Validar proporcions, escales, retolació, absències i integritat vectorial, i exportar dues o tres figures candidates en PDF.

## Codificació visual de les dades

### Dades qualitatives, ordinals i quantitatives

El tipus de dada condiciona les operacions de comparació possibles i la variable visual que convé utilitzar. Una dada **qualitativa** diferencia categories sense establir-ne necessàriament un ordre, com el tipus d'habitatge. Una dada **ordinal** forma categories ordenades, encara que la distància entre elles no sigui mesurable. Una dada **quantitativa** expressa magnituds sobre les quals tenen sentit determinades operacions numèriques. Distingir, ordenar i quantificar no són la mateixa tasca.

### Marques: punts, línies i àrees

Una representació es construeix amb **marques gràfiques**, elements visibles com punts, línies o àrees. En un gràfic poden ser una barra o un punt; en un mapa poden correspondre a un municipi, una carretera o una comarca. Les propietats que varien per codificar informació, com la posició, la mida, la forma, l'orientació, el valor, la textura o el color, s'anomenen **variables visuals**. Aquest llenguatge serà compartit després pels gràfics i pels mapes.

La figura següent resumeix aquesta relació. No s'ha de llegir com una recepta automàtica, sinó com una taula de decisions: primer cal saber si la marca és puntual, lineal o superficial; després cal decidir quina variable visual ajuda el lector a distingir categories, reconèixer un ordre, estimar una magnitud o localitzar un patró. Aquesta mateixa matriu tornarà a aparèixer en cartografia quan una carretera sigui una línia, un municipi sigui una superfície i un allotjament o un nucli es representi amb un símbol puntual.

![Matriu de variables visuals aplicada a marques puntuals, lineals i superficials: posició, mida, forma, orientació, valor, textura i to]({{ site.baseurl }}/assets/img/data-visualization/visual-variables-matrix.svg "Les marques són esquemàtiques: la tria final depèn de les dades, del suport, de la tasca de lectura i de la mida final de lectura. Figura d'elaboració pròpia a partir del vocabulari de la semiologia gràfica de Bertin, 17 d'agost de 2026."){: data-figure-width="54rem"}

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

### Selectors de gràfics per comparar alternatives

La pàgina [*Data Visualization Reference Guides*](https://coolinfographics.com/dataviz-guides), curada per Randy Krum, forma part de *Cool Infographics*, el lloc que acompanya i promociona el seu llibre *Cool Infographics: Effective Communication with Data Visualization and Design* {% cite krumCoolInfographics2013 %}. El llibre desenvolupa el procés de disseny, la narració visual i la integració de dades, text i il·lustracions; el web n'ofereix informació, un capítol de mostra i figures, i amplia aquest entorn amb un directori posterior de selectors de gràfics, vocabularis visuals, catàlegs, matrius i llistes de comprovació.

El valor del directori no consisteix a proporcionar una resposta automàtica, sinó a mostrar que una mateixa taula pot admetre diverses representacions i que cada alternativa facilita unes lectures i en dificulta unes altres. Cal citar la pàgina quan s'utilitza aquesta selecció actualitzada de recursos i el llibre quan es treballa el plantejament general de la infografia; els pòsters i les guies externes conserven, a més, l'autoria i les condicions de cada productor.

![Capçalera del directori Data Visualization Reference Guides i primers recursos sobre principis, catàlegs i percentatges]({{ site.baseurl }}/assets/img/data-visualization/cool-infographics-dataviz-guides-2026-08-12.png "Fragment de «Data Visualization Reference Guides», Cool Infographics, directori curat per Randy Krum. Captura pròpia del 12 d'agost de 2026 per a comentari i docència. Avís del lloc: © 2023 Randy Krum, InfoNewt LLC; les miniatures incrustades pertanyen als titulars respectius."){: data-figure-width="44rem"}

Les guies del repertori parteixen de perspectives complementàries. El [*Chart Chooser*](https://extremepresentation.com/design/7-charts/) d'Andrew Abela comença per allò que es vol mostrar; el [*Financial Times Visual Vocabulary*](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary) agrupa formes segons relacions com desviació, correlació, ordre, distribució, canvi, composició, magnitud, espai i flux; i [*From Data to Viz*](https://www.data-to-viz.com/) comença per l'estructura de les variables i condueix cap a diverses possibilitats, cadascuna amb advertiments. Cap d'aquests marcs substitueix el coneixement de les dades ni converteix una geometria en universalment correcta.

La selecció es pot entendre com un procés de sis decisions:

1. formular la pregunta i la comparació que haurà de fer el lector;
2. identificar si les dades són qualitatives, ordinals, quantitatives, temporals, espacials, jeràrquiques o relacionals;
3. distingir recomptes, percentatges, ràtios, densitats, índexs i canvis, amb els seus denominadors i unitats;
4. decidir si cal consultar valors exactes, comparar magnituds, observar una distribució, seguir una evolució, explorar una associació, explicar una composició o reconèixer un patró espacial o un flux;
5. considerar el públic, el suport, la mida final, l'accessibilitat i el context que necessita la lectura;
6. construir més d'una alternativa i comprovar quina respon millor a la pregunta sense deformar ni ocultar les dades.

Un selector de gràfics genera **candidats**, no un veredicte. Una taula pot ser preferible quan cal recuperar valors exactes; un gràfic ordenat facilita comparar municipis; i un mapa només és necessari quan la localització, la proximitat o el patró espacial formen part de la pregunta. Sovint mapa i gràfic es complementen: el primer conserva el context territorial i el segon permet una comparació més precisa.

>>>>> La tria d'un gràfic parteix de la pregunta de lectura i es comprova comparant alternatives sobre les mateixes dades.
>>>>>
>>>>> - Formular la comparació, el patró o el valor que el lector haurà de localitzar.
>>>>> - Distingir quan convé una taula, un gràfic o un mapa segons la funció de l'espai i la precisió necessària.
>>>>> - Justificar la geometria i les variables visuals a partir del tipus de dada, la unitat i el denominador.
>>>>> - Construir i comparar alternatives que mantinguin constants la pregunta i les dades abans de seleccionar una candidata.

![Vuit famílies de representació visual vinculades a preguntes de comparació, evolució, composició, distribució, relació, xarxa, flux i espai]({{ site.baseurl }}/assets/img/data-visualization/chart-type-repertoire.svg "La pregunta orienta el tipus de gràfic: comparar magnituds, seguir un canvi, explicar una composició, observar una distribució, explorar una relació, mostrar una xarxa, representar un flux o conservar el patró espacial. El repertori és orientatiu: la dada, la pregunta i la mida final condicionen la representació. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="54rem"}

### Repertori ordenat per tasca de lectura

Els noms dels gràfics són útils només si ajuden a formular una decisió. Un *treemap*, un alluvial, un climograma o un radar no són formes més avançades que una barra; són respostes a preguntes diferents. Per això el repertori del curs s'ha d'ordenar per allò que el lector ha de fer: comparar, seguir un canvi, examinar una distribució, explorar una relació, entendre una jerarquia, veure un flux, llegir una pauta estacional o comparar un perfil multivariant.

![Set tipus específics de gràfics: dispersió, alluvial, treemap, climograma, mapa de calor, slopegraph i radar]({{ site.baseurl }}/assets/img/data-visualization/specialized-chart-types.svg "Alguns gràfics específics responen a tasques de lectura concretes: associació entre variables, flux entre categories, jerarquia dins d'un total, ritme climàtic mensual, matriu de valors, canvi entre dos moments o perfil multivariant. Dades esquemàtiques. Figura d'elaboració pròpia, 16 d'agost de 2026."){: data-figure-width="54rem"}

::: table "Tipus de gràfics ordenats per pregunta"
| Tasca de lectura | Tipus de gràfic | Exemple territorial o turístic | Precaució principal |
| --- | --- | --- | --- |
| Consultar valors exactes | Taula, taula destacada o taula amb barres internes | Places d'allotjament per municipi amb font i any | Una taula no mostra patrons amb la mateixa rapidesa que una figura |
| Comparar magnituds | Barres, columnes, punts alineats o *dot plot* | Percentatge d'habitatge no principal per municipi | Ordenar amb criteri i no truncar barres quantitatives |
| Comparar rànquings o canvis entre dos moments | *Slopegraph* o gràfic de pendents | Canvi de posició dels municipis segons densitat turística entre dos anys | Amb molts municipis, les línies es creuen i cal filtrar o agrupar |
| Seguir una evolució temporal | Línia, àrea, petits múltiples o índex base 100 | Evolució mensual de pernoctacions o visitants | No barrejar unitats incompatibles en un doble eix sense justificació |
| Mostrar una composició d'un total | Barres apilades al 100%, circular, anell o mosaic | Distribució de pernoctacions comarcals per tipus d'allotjament | Les parts han de sumar un total comú i no ser taxes independents |
| Mostrar jerarquia i pes intern | *Treemap* o *sunburst* | Repartiment de places per municipi i subtipus d'allotjament | L'àrea és difícil de comparar amb precisió i les etiquetes petites desapareixen |
| Examinar una distribució | Histograma, boxplot, violí, densitat o *ridgeline* | Distribució municipal d'un indicador de renda, edat o habitatge | El resum no identifica per si sol la localització dels casos |
| Explorar relació entre dues variables | Dispersió, línia d'ajust o matriu de dispersió | Envelliment municipal i habitatge no principal | Associació visual no equival a causalitat |
| Afegir una tercera variable aproximada | Bombolles o dispersió codificada amb color o forma | Relació entre envelliment i habitatge no principal, amb població total com a mida | La mida s'ha d'escalar per àrea i pot ocultar punts |
| Representar fluxos o transicions | Sankey, alluvial o diagrama de flux | Canvi de categoria d'un establiment, origen-destinació de visitants o pas entre fases del projecte | Necessita valors compatibles entre etapes; l'amplada suggereix volum |
| Llegir una matriu o un calendari | Mapa de calor, calendari de calor o matriu ordenada | Ocupació hotelera per mes i municipi, o demanda per hora i dia | El color ha de tenir escala comprensible i no substituir valors necessaris |
| Sintetitzar ritmes climàtics | Climograma | Temperatura i precipitació mensual d'una destinació turística | Combina variables diferents; cal indicar unitats i evitar una coincidència visual forçada |
| Comparar perfils multivariants | Radar, aranya o coordenades paral·leles | Perfil de destinacions segons accessibilitat, allotjament, estacionalitat, preu i oferta cultural | Totes les dimensions han de compartir una escala comparable; la forma i l'àrea poden exagerar diferències |
| Conservar la localització | Mapa, cartodiagrama o cartograma | Distribució municipal d'un indicador turístic | Si la localització no importa, un gràfic ordenat pot comparar millor |
:::

En un **diagrama de dispersió**, cada punt representa una unitat d'observació, com un municipi, situada segons dues variables. És adequat quan la pregunta demana si dos indicadors tendeixen a variar conjuntament o si hi ha casos allunyats del patró. En el projecte comarcal podria comparar percentatge de població de 65 anys o més i percentatge d'habitatge no principal. La lectura ha de separar direcció, intensitat aparent i excepcions, i ha de recordar que el gràfic no demostra per si sol una causa.

Un **alluvial** o un **Sankey** fa visible com un volum es reparteix entre categories o com passa d'un estat a un altre. Pot servir per explicar origen i destinació de visitants, canvis de categoria d'establiments, fluxos de dades entre font, full de càlcul, QGIS i sortida final, o repartiments successius d'una magnitud turística. La condició és que l'amplada de cada flux representi una quantitat coherent. Si només es vol mostrar una seqüència d'operacions sense volum, un diagrama de flux ordinari és més honest.

Un **treemap** divideix un rectangle en parts jeràrquiques i fa que l'àrea de cada part representi una magnitud. Pot resumir, per exemple, places d'allotjament per municipi i per tipus. La seva força és mostrar pesos relatius dins d'un total ocupant poc espai; el seu límit és que comparar àrees semblants és difícil, i que les categories petites poden quedar sense etiqueta. Per això convé reservar-lo per a una jerarquia clara i acompanyar-lo de valors o d'una taula quan la precisió sigui important.

Un **climograma** és un gràfic específic perquè combina el ritme mensual de precipitació i temperatura. En geografia turística pot ajudar a explicar estacionalitat climàtica, confort, sequera estival o oportunitat d'activitats a l'aire lliure. Com que barreja variables amb unitats diferents, s'ha de llegir com una convenció gràfica documentada, no com una prova automàtica de relació entre pluja i temperatura. Les unitats, l'estació o font meteorològica i el període de referència han d'aparèixer de manera visible.

Un **mapa de calor** no és un mapa geogràfic, sinó una matriu acolorida. Funciona quan la pregunta combina dues dimensions ordenades, com mesos i municipis, dies i hores, o grups d'edat i tipus de recurs. La decisió principal és ordenar files i columnes amb un criteri interpretable; si l'ordre és arbitrari, el patró pot desaparèixer o aparèixer per casualitat. Quan cal comparar valors exactes, el color pot necessitar etiquetes o una taula complementària.

Un **diagrama de radar** representa diverses dimensions al voltant d'un centre i uneix els valors d'una mateixa observació en un polígon. Pot ajudar a comparar perfils quan totes les variables s'han transformat a una escala comuna, per exemple de 0 a 100, i quan el nombre de dimensions és reduït. En turisme pot servir per discutir si dues destinacions tenen perfils diferents d'accessibilitat, oferta, preu, estacionalitat o serveis. El seu risc principal és que el lector pot interpretar l'àrea o la forma del polígon com si fos una magnitud exacta, i l'ordre dels eixos pot fer que el mateix conjunt de valors sembli més o menys equilibrat. Si cal comparar molts casos o valors precisos, una taula normalitzada, barres agrupades o coordenades paral·leles poden ser més transparents.

>>> **Del nom del gràfic a la decisió.** Si un grup proposa fer un alluvial, un treemap, un climograma o un radar, primer ha d'escriure la pregunta que aquest tipus de gràfic respon millor que una barra, una línia o un mapa. Després ha d'indicar quina variable controla la posició, la longitud, l'àrea, el color, l'amplada del flux o la distància a cada eix radial. Si aquesta correspondència no és clara, la forma encara no està justificada.

Les galeries de codi també poden servir com a repertori quan es llegeixen amb criteri. [*The R Graph Gallery*](https://r-graph-gallery.com/) i [*The Python Graph Gallery*](https://python-graph-gallery.com/) agrupen exemples per famílies de gràfics i mostren codi reproduïble; el llibre en línia de `ggplot2` explica com una visualització es construeix combinant dades, variables estètiques, geometries, escales i facetes {% cite wickhamGgplot2Book2026 %}. Aquests recursos no s'han d'utilitzar per copiar una forma atractiva sense entendre-la. Són útils quan permeten formular alternatives i comprovar quina geometria respon millor a la pregunta.

### Comparar magnituds

Els gràfics de barres i altres representacions basades en posició o longitud permeten comparar territoris i categories quan l'ordenació i les unitats són clares.

Una barra és adequada quan cada municipi o categoria té un valor comparable i el lector ha de discriminar diferències. L'ordre pot seguir la magnitud, la posició geogràfica, una jerarquia conceptual o una classificació prèvia, però ha de tenir una funció. Si l'objectiu és veure qui té més i qui té menys, l'ordre descendent sol facilitar la lectura; si l'objectiu és reconèixer un recorregut territorial o una sèrie temporal, un altre ordre pot ser més coherent.

Les barres no formen una sola família rígida. Poden orientar-se verticalment o horitzontalment, agrupar-se per comparar dues sèries, apilar-se quan les parts comparteixen un total, o obrir-se a banda i banda d'una referència en un gràfic divergent. Una piràmide de població és una aplicació especial d'aquesta lògica: dues sèries comparables es disposen a esquerra i dreta d'un eix central per mostrar l'estructura per edat i sexe. Un *tornado plot* utilitza una disposició semblant per comparar escenaris, sensibilitats o diferències positives i negatives.

![Sis variants de gràfics de barres: barres verticals, horitzontals ordenades, agrupades, apilades al 100%, tornado plot i piràmide de població]({{ site.baseurl }}/assets/img/data-visualization/bar-chart-variants.svg "Les barres comparen longituds sobre una base comuna, però l'orientació i l'organització canvien la pregunta de lectura: magnitud, ordre, comparació entre sèries, composició o diferència respecte d'una referència. Les barres apilades al 100% només són adequades si les parts comparteixen un total. Dades esquemàtiques. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="54rem"}

### Composició, relació i distribució

La composició, la relació entre variables i la distribució d'un indicador demanen estructures gràfiques diferents. La tria ha de respondre a la pregunta, no a l'efecte visual més atractiu. Una sèrie temporal requeriria una estructura específica, però el projecte comarcal treballa principalment una comparació municipal per a un mateix període.

Una figura de composició només és pertinent quan les parts comparteixen un total; una figura de relació només és pertinent quan dues variables es poden comparar observació per observació; i una figura de distribució només és pertinent quan interessa el conjunt de valors, no un municipi concret. Aquesta distinció evita tres errors habituals: fer sumar percentatges independents, suggerir una causalitat a partir d'una dispersió i substituir un mapa per un resum estadístic quan la localització és part de la pregunta.

#### Composició

Una composició mostra com es reparteix un total entre parts compatibles. Les barres apilades al 100% permeten comparar diversos municipis sobre una mateixa escala, mentre que un gràfic circular només resulta manejable amb poques parts i un únic total. Abans de representar cal comprovar que les categories no se solapen i que, amb els arrodoniments admesos, reconstrueixen el total.

No qualsevol conjunt de percentatges forma una composició. El percentatge d'ocupació de diversos municipis conté taxes independents amb denominadors diferents i no ha de sumar 100%. En canvi, el repartiment de les pernoctacions comarcals per municipi sí que descriu parts d'un mateix total. També cal distingir un augment de 40% a 50%, que equival a 10 punts percentuals, d'un augment relatiu del 25% respecte del valor inicial.

>>>> **Un gràfic circular ha de respondre "100% de què?".** Si falta una categoria desconeguda, si s'han retirat valors petits o si els percentatges provenen de denominadors diferents, el cercle deixa de representar un total complet. En aquests casos és preferible una barra al 100% amb la categoria d'absència visible, una taula curta o una altra comparació que no faci veure una composició tancada {% cite jonesHowLieCharts2018 %}.

Quan una magnitud es representa amb cercles o bombolles, és l'àrea i no el radi o el diàmetre el que ha de ser proporcional a la dada. Si un valor de referència $X_1$ es representa amb un diàmetre $D_1$, el diàmetre corresponent a $X_2$ és:

$$
D_2 = D_1\sqrt{\frac{X_2}{X_1}}
$$

Quadruplicar una dada només duplica el diàmetre, perquè així l'àrea es quadruplica. Fer el diàmetre directament proporcional al valor exageraria les diferències, com mostra la guia sobre [l'escalat de cercles en visualització de dades](https://infonewt.com/circles/). Encara que l'escalat sigui correcte, l'àrea es compara amb menys precisió que una longitud alineada; per això els cercles són adequats per mostrar magnituds aproximades o patrons espacials, però necessiten una llegenda de mides o etiquetes quan cal llegir valors concrets.

#### Relació entre dues variables

Un diagrama de dispersió situa cada municipi segons dos indicadors. La lectura ha de considerar la direcció, la forma i la intensitat aparent de l'associació, així com els casos que s'allunyen del patró general. Només s'hi poden incloure observacions amb tots dos valors disponibles, i una associació visual no demostra causalitat.

Quan diverses observacions comparteixen valors o queden molt pròximes, els punts es poden ocultar entre si. La transparència parcial permet detectar concentracions i un desplaçament aleatori molt petit pot separar coincidències exactes, però aquest desplaçament modifica la posició representada i s'ha de limitar i documentar. Amb conjunts molt grans pot ser preferible resumir la densitat en cel·les o corbes de nivell en lloc de dibuixar tots els punts {% cite wilkeFundamentalsDataVisualization2019 %}.

#### Distribució

Un diagrama de caixa resumeix la mediana, els quartils, la dispersió i els possibles valors extrems d'un indicador. Facilita una visió conjunta, però no mostra on es localitza cada municipi. Un valor assenyalat com a extrem no és automàticament un error: cal revisar la dada, el denominador i les característiques territorials abans d'interpretar-lo.

### Unitats i context dels indicadors territorials

Valors absoluts, percentatges, ràtios i densitats necessiten títols, unitats i context suficients perquè no es confonguin entre si.

### Relacions, fluxos i grafs

No totes les visualitzacions comparen magnituds, distribucions o composicions. En alguns casos la pregunta se centra en les **relacions**: quines fonts alimenten un indicador, quins municipis comparteixen un flux, quins equipaments formen una xarxa, quins passos depenen d'una comprovació prèvia o com circula una decisió dins d'un procés. Un **graf** representa aquesta estructura mitjançant nodes i arestes. Els nodes són els elements i les arestes indiquen vincles, dependències, connexions o fluxos; poden tenir direcció, pes o categoria segons la pregunta.

Els grafs no substitueixen els mapes. Un mapa conserva posició, distància i veïnatge territorial; un graf pot reordenar els nodes per fer llegibles les relacions. Aquesta llibertat és útil quan el problema no és saber on és cada element, sinó entendre què connecta amb què. Un esquema de procés del projecte, una xarxa de fonts i fitxers, un flux de dades entre full de càlcul, QGIS i Inkscape, o una xarxa de mobilitat turística poden tenir forma de graf, encara que només alguns d'aquests casos siguin estrictament espacials.

[Mermaid.js](https://mermaid.js.org/) permet escriure diagrames i gràfics mitjançant una sintaxi textual que després es renderitza com a figura. El codi es pot provar en un editor en línia com [Mermaid Live Editor](https://mermaid.live/) i després conservar-lo dins del projecte, de manera que la figura no depengui només d'una captura o d'una composició manual. Aquesta propietat és especialment útil en un context amb models de llenguatge grans, perquè un LLM pot ajudar a esbossar una sintaxi inicial a partir d'una descripció verbal. El resultat, però, s'ha de verificar com qualsevol altra figura: una fletxa pot suggerir una dependència que no existeix, un node pot barrejar dues operacions diferents i una xarxa massa densa pot semblar precisa mentre oculta el criteri de selecció.

Mermaid no és un tipus únic de graf, sinó una família de notacions. Un diagrama de flux ajuda a explicar dependències entre passos; una seqüència mostra interaccions ordenades entre agents o eines; un diagrama d'estats documenta canvis de situació; un esquema entitat-relació és útil per pensar taules i claus; un Gantt situa tasques en el temps; i una línia del temps conserva la traça narrativa d'una figura o d'un projecte.

::: subfigures a+b+c/d+e+f "Sis notacions Mermaid per representar relacions diferents en un projecte de dades territorials. Les subfigures comparteixen una sintaxi textual reproduïble, però cada tipus fa visible una estructura distinta: dependències, interaccions, estats, relacions entre taules, planificació temporal i traça de publicació. Figures d'elaboració pròpia amb Mermaid i `diavisuals`, 15 d'agost de 2026."
![Flux de treball]({{ site.baseurl }}/assets/diagrams/data-visualization/mermaid-flowchart.mmd "Diagrama de flux: dependències entre passos")
![Seqüència]({{ site.baseurl }}/assets/diagrams/data-visualization/mermaid-sequence.mmd "Diagrama de seqüència: interaccions entre estudiant, portal, full de càlcul i QGIS")
![Estats]({{ site.baseurl }}/assets/diagrams/data-visualization/mermaid-state.mmd "Diagrama d'estats: pas d'esborrany a publicació")
![Entitat-relació]({{ site.baseurl }}/assets/diagrams/data-visualization/mermaid-er.mmd "Diagrama entitat-relació: municipis, indicadors i fonts")
![Gantt]({{ site.baseurl }}/assets/diagrams/data-visualization/mermaid-gantt.mmd "Diagrama de Gantt: fases temporals d'una figura reproduïble")
![Línia del temps]({{ site.baseurl }}/assets/diagrams/data-visualization/mermaid-timeline.mmd "Línia del temps: traça de font, taula, visualització i publicació")
:::

![Esquema que mostra com un flux de treball es pot formular com a codi Mermaid i llegir com a xarxa de nodes i arestes]({{ site.baseurl }}/assets/img/data-visualization/graph-mermaid-workflow.svg "Un graf és adequat quan la pregunta se centra en dependències, connexions o fluxos; el codi textual identifica nodes, arestes i direcció i facilita revisar-ne l'estructura abans d'exportar-la. Les fletxes indiquen dependència, no causalitat demostrada; cada node ha de correspondre a un element revisable i cal conservar el codi font. Un LLM pot proposar l'esborrany, però se n'han de comprovar la lògica i les fonts. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="48rem"}

En el projecte comarcal, un diagrama d'aquest tipus pot servir per documentar el flux de treball, però no comptarà com a substitut dels gràfics estadístics principals. Si s'inclou en una memòria o presentació, haurà d'indicar què representa cada node, què significa cada aresta i quins elements s'han deixat fora. Una bona xarxa no és la que conté tots els noms possibles, sinó la que permet entendre una relació concreta sense perdre la traçabilitat. La reproductibilitat no eximeix de revisar el significat: conservar el codi Mermaid permet regenerar la figura, però la responsabilitat sobre la relació representada continua sent de l'autor.

## Jerarquia i lectura crítica

### Retolació de gràfics: títol, eixos, etiquetes i font

Un gràfic ha de poder-se interpretar sense reconstruir la taula original. El títol ha d'identificar la pregunta o la troballa sense afirmar més del que mostren les dades; el subtítol o una anotació poden aportar el context imprescindible. Les unitats, el període, el territori i la font han de ser visibles, i la precisió numèrica ha de correspondre a la qualitat de les dades i a la necessitat del lector. Les etiquetes directes redueixen el trajecte entre marca i llegenda quan l'espai ho permet. Aquests criteris també es poden revisar amb els [principis bàsics de visualització de dades](https://policyviz.com/2018/08/07/dataviz-cheatsheet/) i la [llista de comprovació de visualització de dades](https://web.archive.org/web/20190918015742/https://datavizchecklist.stephanieevergreen.com/assets/DataVizChecklist_Feb2018.pdf).

La **retolació** d'un gràfic inclou tots els textos que guien la lectura: títol, subtítol, eixos, unitats, etiquetes directes, anotacions, llegenda, font i notes sobre transformacions. La seva funció és reduir l'ambigüitat sense repetir la taula sencera. Un gràfic sense prou text obliga el lector a endevinar què compara; un gràfic amb massa text converteix la figura en un full de càlcul il·lustrat. La decisió correcta depèn de la pregunta, de la mida final i del públic.

La retolació de gràfics comparteix criteris amb la retolació cartogràfica que es treballarà al capítol 6. En tots dos casos cal associar cada text amb l'element corresponent, establir jerarquia, evitar col·lisions i comprovar la llegibilitat final. La diferència és que un gràfic pot reorganitzar categories o situar etiquetes directament al final d'una línia, mentre que un mapa ha de respectar la posició territorial dels elements.

>>>>> La jerarquia visual i la lectura crítica permeten orientar l'atenció sense ocultar les condicions que sostenen la comparació.
>>>>>
>>>>> - Construir una jerarquia entre dades, títol, etiquetes, unitats, font i elements auxiliars.
>>>>> - Distingir decisions que faciliten la lectura de recursos que exageren, oculten o fabriquen comparacions.
>>>>> - Interpretar tendències, associacions i valors extrems com a patrons observats, no com a causes o previsions automàtiques.
>>>>> - Validar origen dels eixos, proporcionalitat, ordre, denominadors, absències, llegibilitat i context abans d'acceptar una figura.

::: table "Decisions habituals de retolació en gràfics"
| Element textual | Funció | Criteri de revisió |
| --- | --- | --- |
| Títol | Identificar la pregunta o el missatge principal | No exagerar una conclusió ni repetir literalment el nom del camp |
| Subtítol | Afegir territori, període, unitat o condició de lectura | Incloure només el context que evita una interpretació errònia |
| Eixos i unitats | Fer visible l'escala de mesura | Indicar percentatges, persones, habitatges, densitats o índexs sense abreviatures ambigües |
| Etiquetes directes | Associar valors o categories a marques concretes | Etiquetar els valors necessaris, no totes les marques si això satura la figura |
| Anotacions | Assenyalar un cas, un canvi o una excepció | Explicar per què s'assenyala, no decorar amb comentaris redundants |
| Llegenda | Descodificar colors, formes o sèries | Substituir-la per etiquetes directes quan redueix el moviment ocular i no crea conflictes |
| Font i notes | Documentar procedència, període, transformacions i absències | Fer-les recuperables sense donar-los més pes que a les dades |
:::

En un gràfic de barres, etiquetar tots els valors pot ser útil amb poques categories, però pot fer perdre la comparació si cada barra incorpora números llargs. En una sèrie temporal, sovint és més llegible etiquetar la línia al final que obligar a anar i tornar entre línia i llegenda. En una dispersió, no s'han d'etiquetar tots els punts si això crea una massa de noms; pot ser millor assenyalar només municipis extrems, casos rellevants o observacions que el text comentarà explícitament. Les anotacions s'han de justificar per la lectura, no per omplir l'espai buit.

Els elements auxiliars han d'explicar la comparació i no competir amb les dades. Les línies de quadrícula, els eixos, les marques i les vores poden ajudar a estimar valors o separar panells, però han de quedar en segon pla. El color necessita una funció definida, com agrupar, ordenar o destacar, i no ha de ser l'únic recurs per distingir informació essencial. El capítol de teoria del color desenvoluparà les paletes i les comprovacions d'accessibilitat.

### Eixos truncats, tres dimensions i soroll visual

S'analitzaran recursos que exageren diferències, dificulten la comparació o amaguen el context, inclosos els gràfics tridimensionals i l'excés de categories. La lectura crítica no consisteix només a detectar una falsedat explícita: també ha de reconèixer decisions que orienten l'atenció o fan més difícil comprovar una comparació {% cite jonesHowLieCharts2018 tufteVisualDisplay2001 wilkeFundamentalsDataVisualization2019 %}.

![El mateix gràfic circular del 25% i el 75% vist des de quatre angles; la perspectiva altera l'àrea aparent dels sectors]({{ site.baseurl }}/assets/img/data-visualization/wilke-rotated-pie-3d.png "La tercera dimensió decorativa no representa cap dada i la perspectiva fa que un mateix sector sembli canviar de mida. Figura 26.1 de Claus O. Wilke, «Fundamentals of Data Visualization», original sense modificar, CC BY-NC-ND 4.0."){: data-figure-width="32rem"}

La tercera dimensió és especialment problemàtica quan només converteix sectors, barres o línies en objectes amb volum. La figura es projecta igualment sobre una pàgina o pantalla plana, de manera que la perspectiva deforma longituds i àrees i pot ocultar marques situades al darrere. Si una tercera variable és necessària, sovint es pot representar amb petits múltiples, posició en un segon gràfic, mida, forma o color sense perdre la possibilitat de comparar sobre un pla comú.

L'ús de 3D pot estar justificat quan l'objecte estudiat és realment tridimensional, com un relleu, i la forma espacial és part de la pregunta. Encara així, una vista estàtica pot amagar pendents o elements; una visualització interactiva, diverses perspectives o una alternativa amb corbes de nivell poden aportar controls de lectura. La precaució no consisteix a prohibir qualsevol 3D, sinó a exigir que la tercera dimensió comuniqui una dada necessària i no una decoració.

Una figura pot orientar la lectura sense inventar cap número. Aquest és el nucli de la lectura crítica que Jones formula per als gràfics i que Tufte i Wilke desenvolupen des de criteris de claredat, proporció i integritat visual {% cite jonesHowLieCharts2018 tufteVisualDisplay2001 wilkeFundamentalsDataVisualization2019 %}. L'error no sempre és una mentida directa; sovint és una decisió que fa molt fàcil una conclusió i molt difícil comprovar-ne els límits.

Un cas habitual és el **doble eix vertical**. Pot semblar una solució compacta quan dues sèries comparteixen període però no unitat, però també permet escollir rangs diferents fins que dues línies semblen moure's alhora. La coincidència visual pot sortir de l'escala, no d'una relació substancial entre les variables. Si l'objectiu és comparar evolucions, és més honest separar les sèries en petits múltiples, indexar-les respecte d'un any base o representar directament la diferència que es vol discutir.

::: subfigures a+b "La mateixa informació pot suggerir una relació artificial o conservar la comparació sense fabricar-la. La subfigura a utilitza dos eixos verticals ajustats perquè ocupació i preu mitjà comparteixin pendent aparent; la subfigura b separa les unitats i deixa que la interpretació causal quedi fora del gràfic. Figures d'elaboració pròpia, 15 d'agost de 2026."
![Gràfic problemàtic amb ocupació i preu mitjà dibuixats sobre dos eixos verticals que fan coincidir els pendents]({{ site.baseurl }}/assets/img/data-visualization/dual-axis-misleading.svg "Doble eix: la semblança visual depèn dels rangs escollits")
![Versió revisada amb dos petits múltiples, unitats explícites i la mateixa seqüència temporal]({{ site.baseurl }}/assets/img/data-visualization/dual-axis-reviewed.svg "Petits múltiples: cada variable conserva la seva escala")
:::

>>>> **Una figura millorable no s'ha de maquillar al final.** Si el problema és l'escala, la geometria, el denominador o la unitat, corregir colors i tipografia no resol l'error. La revisió ha de tornar a la pregunta, a les dades i al tipus de comparació.

::: table "Errors típics en gràfics i revisió corresponent"
| Decisió problemàtica | Efecte sobre la lectura | Revisió preferent |
| --- | --- | --- |
| Barres amb eix truncat | Exagera diferències perquè la longitud deixa de ser proporcional | Fer començar les barres a zero o canviar a punts/línies si cal ampliar un rang |
| Doble eix vertical | Pot fabricar paral·lelismes entre sèries amb unitats diferents | Usar petits múltiples, índex base 100 o gràfics separats amb unitats visibles |
| 3D decoratiu | Deforma angles, àrees i posicions sense afegir cap variable | Tornar a una geometria plana o justificar una tercera dimensió real |
| Cercles escalats pel radi | Exagera les diferències d'àrea percebuda | Fer proporcional l'àrea i incloure una llegenda de mides |
| Categories sense ordre funcional | Amaga màxims, mínims o patrons de comparació | Ordenar per magnitud, cronologia, geografia o criteri analític explícit |
| Percentatges tractats com a composició | Fa sumar taxes independents que no comparteixen total | Verificar numerador, denominador i total abans d'apilar o fer sectors |
| Títol massa concloent | Presenta com a resultat allò que només és una lectura possible | Formular el missatge amb període, unitat, territori i limitació |
| Absències convertides en zero | Desplaça marques i pot crear una classe o una barra falsa | Representar o documentar l'absència separadament |
:::

La relació d'aspecte també orienta la lectura. En una sèrie temporal, la mateixa diferència vertical pot semblar una pujada brusca o una variació suau segons l'altura i l'amplada del marc. No hi ha una proporció universalment correcta, però el criteri ha de ser defensable: conservar el rang rellevant, indicar unitats i període, i evitar que la forma del marc substitueixi l'anàlisi de la magnitud real del canvi.

![Tres gràfics de línia amb la mateixa sèrie temporal i el mateix rang numèric, però amb marcs alt, equilibrat i pla que modifiquen la sensació de pendent]({{ site.baseurl }}/assets/img/data-visualization/aspect-ratio-trend.svg "La mateixa sèrie de 2021 a 2025, representada sempre amb el rang 0-20, pot semblar més o menys dramàtica segons la relació entre amplada i altura del marc. En comparar alternatives cal mantenir visibles el rang, el període i el motiu de la proporció triada. Dades esquemàtiques: 8,2; 9,7; 10,8; 12,4; 13,8. Figura d'elaboració pròpia, 17 d'agost de 2026."){: data-figure-width="54rem"}

>>>> **Una tendència visual no és una previsió.** Unir punts amb una línia ajuda a llegir evolució, però extrapolar-la cap al futur exigeix una hipòtesi sobre el procés que genera les dades. Si el text diu que un indicador "continuarà pujant", cal aportar model, període, incertesa i justificació; si només es descriu el passat, és millor parlar d'augment observat, canvi de ritme o variació entre anys.

### Criteris per seleccionar i revisar visualitzacions

Les guies de visualització, com [*From Data to Viz*](https://www.data-to-viz.com/), el [*Financial Times Visual Vocabulary*](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary), els [*Core Principles of Data Visualization*](https://policyviz.com/2018/08/07/dataviz-cheatsheet/) i la [*Data Visualization Checklist*](https://web.archive.org/web/20190918015742/https://datavizchecklist.stephanieevergreen.com/assets/DataVizChecklist_Feb2018.pdf), coincideixen en molts criteris de claredat i integritat, però les recomanacions depenen de la marca, la tasca i el suport. Convertir-les en prohibicions absolutes produiria errors nous: l'origen zero és essencial per comparar longituds de barres, però no per a qualsevol gràfic de línies; una quadrícula pot ser útil per estimar valors si queda en segon pla; i una llegenda continua sent necessària quan les etiquetes directes saturarien un mapa.

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
| Donar funció al color | Utilitzar-lo per agrupar, ordenar o destacar i combinar-lo amb altres senyals | Cal comprovar contrast, mida final i visió cromàtica; el capítol de teoria del color ho desenvolupa |
| Evitar comparacions ambigües | Mantenir escales comunes i separar mesures quan una doble escala vertical podria suggerir una relació artificial | Els panells coordinats o els petits múltiples solen fer explícites les unitats |
| Utilitzar mapes quan l'espai importa | Representar localització, proximitat, direcció o patrons territorials | Un gràfic ordenat és millor quan només cal comparar valors amb precisió |
| Conservar context i precisió adequats | Indicar període, territori, unitat, font, transformacions i absències | Més decimals i més dades no impliquen necessàriament més informació útil |
| Comparar alternatives | Mantenir constants la pregunta i les dades mentre canvia una decisió visual | La versió més atractiva no és necessàriament la més interpretable |
:::

### Auditoria i revisió de figures millorables

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

Com a pràctica guiada del mètode d'auditoria, es conservarà una figura inicial i una de revisada. S'hi identificaran almenys tres decisions problemàtiques i es construirà la versió alternativa amb el full de càlcul. La comparació entre l'original i la revisió es justificarà amb criteris perceptius, no amb preferències com “queda més bonic”.

### Construir i revisar gràfics al full de càlcul

Excel i Calc permeten produir gràfics ràpidament, però el resultat automàtic s'ha de revisar. El procediment es manté estable encara que canviï la interfície:

1. formular la pregunta territorial que haurà de respondre la figura;
2. seleccionar al full `indicators` els municipis, el període, la variable i la unitat corresponents;
3. comprovar que no s'hi han barrejat totals comarcals, files auxiliars ni valors absents convertits en zero;
4. escollir una geometria adequada a la comparació i ordenar les categories amb un criteri explícit;
5. construir almenys una alternativa que mantingui constants les dades i la pregunta;
6. evitar dobles eixos, efectes 3D, àrees mal escalades o altres recursos que dificultin comprovar la comparació;
7. revisar el títol, els eixos, les etiquetes, la llegenda, el color i la font a la mida prevista;
8. contrastar almenys dos valors representats amb les cel·les d'origen;
9. conservar el gràfic editable al llibre abans de generar-ne l'exportació vectorial.

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

### Dades d'entrada, gràfics guiats i PDFs candidats

L'entrada és el mateix llibre acumulatiu, amb els camps de població per grans grups d'edat a `municipal` i els sis càlculs municipals revisats a `indicators`. La demostració guiada construeix al full `charts` unes barres apilades al 100% de l'estructura d'edats i unes barres ordenades del percentatge d'habitatge no principal. També construeix una dispersió entre envelliment i habitatge no principal quan la pregunta acordada i les dades compatibles justifiquen explorar-ne l'associació; en cas contrari, se'n justificarà la substitució per una figura pertinent o l'omissió. Tots els gràfics construïts que es considerin candidats es conservaran editables i vinculats a les cel·les d'origen a `charts`. Com a demostració del mètode d'auditoria, una figura conservarà una versió inicial i una de revisada. S'exportaran exactament dues o tres figures candidates en PDF vectorial a `outputs/figures` i es registraran a `README.md`.

Cada figura haurà de respondre una pregunta sobre les diferències entre municipis o sobre el conjunt de la comarca. No es tracta de decorar la mateixa dada de moltes maneres, sinó de comprovar què permet veure cada geometria.

>>>>> L'activitat converteix els indicadors revisats en un conjunt de gràfics editables i en dues o tres figures candidates per a la síntesi comarcal.
>>>>>
>>>>> - Construir al full `charts` gràfics vinculats als camps compatibles de `municipal` i `indicators`.
>>>>> - Justificar per a cada figura la pregunta, la geometria, les marques, les variables visuals i l'ordre.
>>>>> - Interpretar comparacions i associacions com a patrons, i explicitar què no permeten concloure sobre les causes.
>>>>> - Validar marques, totals, unitats, absències, retolació i valors representats contra les cel·les d'origen.
>>>>> - Exportar exactament dues o tres figures candidates en PDF vectorial i registrar-les a `README.md`.

### Figures guiades i alternatives opcionals

::: table "Figures que es poden construir o analitzar"
| Figura | Dades adequades | Pregunta possible | Abast |
| --- | --- | --- | --- |
| Barres simples ordenades | Percentatge d'habitatge no principal per municipi | Quins municipis presenten els valors més alts i més baixos? | Demostració guiada |
| Barres apilades al 100% | Percentatges de població de 0–14, 15–64 i 65+ | Com varia l'estructura per edats entre municipis? | Demostració guiada |
| Dispersió | Percentatge de 65+ i percentatge d'habitatge no principal | Hi ha una associació visible entre tots dos indicadors? | Demostració guiada quan la pregunta i les dades la justifiquen |
| Barres en paral·lel | Habitatges principals i no principals en valors absoluts | Com canvien el volum i la composició del parc residencial? | Anàlisi opcional* |
| Línia temporal | Valors comparables repetits en el temps | Com evoluciona un indicador mensual o anual? | Anàlisi opcional* |
| Slopegraph | Mateixa variable en dos moments | Quins municipis han pujat o baixat de posició? | Anàlisi opcional* |
| Circular | Habitatges principals i no principals del total comarcal | Quina composició té el conjunt de la comarca? | Anàlisi opcional* |
| Anell | La mateixa composició que el circular | El buit central aporta informació o només decoració? | Anàlisi opcional* |
| Boxplot | Un indicador per a tots els municipis de la comarca | Quin és el centre, la dispersió i els possibles casos extrems? | Anàlisi opcional* |
| Mapa de calor | Matriu de mesos i municipis, o dies i hores | Quan es concentren els valors més alts i més baixos? | Anàlisi opcional* |
| Treemap | Parts jeràrquiques d'un total | Com es reparteixen places o pernoctacions per municipi i tipus? | Anàlisi opcional* |
| Alluvial o Sankey | Fluxos, transicions o repartiments successius | D'on venen els visitants, on van o com canvien de categoria? | Anàlisi opcional* |
| Climograma | Temperatura i precipitació mensual | Quin ritme climàtic condiciona l'activitat turística d'una destinació? | Anàlisi opcional* |
:::

\* Les files d'anàlisi opcional només es construiran quan existeixin les dades que requereixen i la pregunta les faci pertinents; si no, es podran estudiar com a exemples. El gràfic circular i el d'anell poden representar intencionadament la mateixa composició per permetre'n una comparació crítica. El boxplot resumeix la distribució municipal, però no identifica per si sol la posició geogràfica dels valors.

### Selecció de dues o tres figures candidates

La sèrie completa serveix per aprendre i comparar, mentre que el repertori restant continua sent opcional i analític. S'exportaran exactament dues o tres figures candidates que expliquin aspectes complementaris. El capítol 9 farà la selecció final de dues o tres peces visuals en total, comptant també els mapes. Per a la demostració del Tarragonès, una combinació coherent de candidates seria:

1. barres apilades al 100% per comparar l'estructura d'edats;
2. barres ordenades del percentatge d'habitatge no principal;
3. dispersió entre envelliment i habitatge no principal.

La dispersió només es construirà quan la pregunta i les dades justifiquin explorar una associació. Que no mostri una relació interpretable és un resultat que es documentarà i pot motivar que es descarti de la selecció; si l'associació no era una pregunta pertinent d'entrada, se'n justificarà la substitució o l'omissió.

### Carpeta i noms dels PDFs candidats

Cada figura candidata exportada tindrà un nom semàntic i una versió vectorial PDF. Una possible estructura és:

```text
outputs/figures/
  age_structure_tarragones_2021.pdf
  non_principal_housing_tarragones_2021.pdf
  ageing_vs_non_principal_housing_tarragones_2021.pdf
```

L'any i el territori s'adaptaran a les dades reals. No s'utilitzaran noms com `grafico1.pdf` o `final.pdf`. Si una figura es revisa, s'ha de poder regenerar des del llibre de treball; no s'ha de corregir únicament el PDF i perdre la relació amb les dades.

### Control de qualitat abans d'exportar

Abans d'acceptar una figura cal comprovar que el nombre de marques correspon als municipis o categories previstos, que les unitats coincideixen amb el diccionari del llibre i que els valors absents no han passat a ser zeros. En el gràfic apilat al 100% de l'estructura d'edats, el denominador de cada municipi serà la suma dels tres grups mostrats: població de 0–14, de 15–64 i de 65 anys o més. Si aquesta suma difereix del total de població publicat, la discrepància es conservarà i es registrarà a `checks`; no es modificarà manualment cap grup per forçar la coincidència. Les altres composicions percentuals també han de reconstruir el seu total explícit dins del marge d'arrodoniment, i les barres basades en longitud han de començar ordinàriament a zero; qualsevol excepció requeriria una altra geometria o una justificació explícita. En sèries temporals, també es revisarà si la relació d'aspecte, el rang de l'eix i les anotacions fan semblar inevitable una tendència que només s'ha observat en aquell període.

La revisió també es farà a la mida final. El text, els símbols i els traços han de continuar sent llegibles fora de la interfície del full de càlcul. Després de l'exportació, el PDF s'obrirà a Inkscape per verificar que les formes i els textos continuen sent objectes vectorials seleccionables.

### Evidències de la visualització comarcal

::: table "Evidències de la visualització comarcal"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/processed` | El mateix llibre de treball | Taules, indicadors i tots els gràfics candidats editables al full `charts` |
| `outputs/figures` | PDFs vectorials | Dos o tres PDFs candidats, un per cada pregunta considerada, amb títol, unitat, període i font |
| `data/processed` | Auditoria guiada | Una figura inicial i la seva versió revisada, conservades com a demostració del mètode |
| `README.md` | Registre de figures | Fitxer, pregunta, tipus de dada, marca, variable visual, condició de candidata i limitació principal |
:::

L'activitat deixarà un conjunt de gràfics revisats i exactament dues o tres figures candidates per a la mateixa miniinfografia comarcal, cadascuna associada a una pregunta i a un indicador. Per a cada figura es podrà explicar quines variables visuals utilitza, què permet veure i quins límits conserva. Després de desenvolupar el color, els components espacials, el llenguatge cartogràfic, el SIG i la cartografia temàtica, el capítol 9 seleccionarà dues o tres peces visuals finals en total entre aquestes figures i els mapes disponibles.
