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

Representar dades significa codificar-les visualment; llegir un gràfic exigeix reconstruir aquesta correspondència. Aquest capítol parteix de la semiologia de Jacques Bertin i la relaciona amb la gramàtica de gràfics de Leland Wilkinson i amb els estudis de percepció visual. Aquests marcs ajuden a explicar què representa cada marca, com es llegeixen els eixos i quina taula fa possible la figura. La pregunta i la definició de les dades orienten decisions que es poden aplicar directament a Calc o Excel {% cite bertinSemiologyGraphics2010 wilkinsonGrammarGraphics2005 munznerVisualizationAnalysisDesign2014 wilkeFundamentalsDataVisualization2019 %}.

El color apareixerà com un canal visual, però el seu desenvolupament sistemàtic quedarà per al capítol de teoria del color, perquè afecta gràfics, mapes, accessibilitat i infografia. La classificació cartogràfica es treballarà més endavant, un cop introduït el llenguatge propi del mapa i la integració amb QGIS.

>>>>> En acabar el capítol, cal poder seleccionar, construir, revisar i exportar figures que responguin una pregunta territorial sense deformar les dades.
>>>>>
>>>>> - Identificar la unitat d'observació i proposar les files i columnes necessàries per construir un gràfic.
>>>>> - Explicar com les marques i les variables visuals codifiquen dades qualitatives, ordinals i quantitatives.
>>>>> - Construir figures editables i vinculades als indicadors d'origen, adequades al públic, al suport i a la mida final.
>>>>> - Llegir escales i unitats, contrastar valors amb la taula i justificar què permet concloure cada figura.

## La pregunta visual orienta la representació

El llibre ja conté numeradors, denominadors i indicadors revisats. Ara el problema no és calcular un percentatge, sinó decidir quina representació permet comparar-lo sense perdre el municipi, el període, la unitat o el denominador que li donen sentit. L'elecció d'un gràfic exigeix identificar què representa cada fila, quina funció compleix cada camp i quina operació haurà de fer el lector.

La tria de la geometria també exigeix declarar si la figura serveix per **explorar**, **analitzar** o **explicar**. L'exploració conserva alternatives i obre preguntes; l'anàlisi busca patrons, relacions i excepcions; l'explicació selecciona l'evidència necessària per comunicar un resultat a un públic. Una figura útil per descobrir un patró no és automàticament la figura final: pot necessitar menys sèries, més context i una jerarquia més explícita per convertir-se en una explicació {% cite generalitatGuiaVisualitzacioDades2018 %}.

### Unitat d'observació i estructura de la taula

Una **unitat d'observació** és l'entitat descrita per una fila. A `municipal`, cada fila representa un municipi del Tarragonès; a la sèrie temporal de Vila-seca, cada fila representa un any; a la taula d'edat i sexe, cada fila representa una combinació d'edat i sexe. La mateixa columna no pot canviar de significat entre files sense trencar la comparació.

La unitat d'observació determina què serà una marca. En les barres d'habitatge no principal, una barra representa un municipi. En la dispersió, un punt representa el mateix municipi situat segons dos indicadors. En la línia temporal, cada punt representa un any i l'ordre cronològic justifica unir-los. Aquesta distinció explica per què els punts municipals d'una dispersió no s'uneixen: l'ordre de les files no descriu cap trajectòria.

### Tipus i funcions de les variables

Una variable **nominal** distingeix categories sense ordre, com municipi, sexe, titularitat o tipus d'allotjament. Només permet afirmar igualtat o diferència; ordenar alfabèticament ajuda a localitzar un nom, però no crea una jerarquia substantiva. Una variable **ordinal** conté categories ordenades, com baix, mitjà i alt o una categoria d'allotjament expressada en estrelles, però la distància entre nivells consecutius no és necessàriament constant.

Una variable **quantitativa** expressa una magnitud. Els recomptes, com població o habitatges, són discrets; superfície, densitat, percentatge o una coordenada poden tenir decimals. El fet que un camp contingui números no el converteix automàticament en quantitatiu: el codi `431711` identifica Vila-seca, però sumar-lo o calcular-ne la mitjana no té sentit.

El temps i l'espai poden actuar com a estructures de comparació. L'any ordena observacions i permet estudiar canvi; les coordenades situen objectes; el codi municipal relaciona taules; i la geometria conserva localització i veïnatge. Per tant, representar exigeix alguna cosa més que saber si una columna és text o número: cal conèixer quina funció compleix dins de la pregunta.

::: table "Camps del projecte i funció analítica"
| Camp | Tipus i funció | Operació amb sentit | Pregunta visual possible |
| --- | --- | --- | --- |
| `municipality_name` | Nominal, identificador llegible | Filtrar, etiquetar o agrupar | Quin municipi correspon a cada marca? |
| `municipality_code` | Identificador textual | Comprovar igualtat, unicitat i correspondència | Les dues variables pertanyen al mateix municipi? |
| `housing_non_main_pct` | Quantitativa relativa | Ordenar, comparar diferències i resumir distribució | On té més pes l'habitatge no principal? |
| `population_total` | Quantitativa absoluta | Sumar i comparar volums | Quins municipis concentren més població? |
| `age_group` | Ordinal | Ordenar grups i comparar composició | Com canvia l'estructura d'edats? |
| `year` | Temporal | Ordenar i calcular canvis | Com evoluciona la població de Vila-seca? |
| `sex` | Nominal binària en aquesta font | Separar sèries comparables | Quina forma presenta la piràmide per sexe? |
:::

### Unitats, denominadors i absències

Valors absoluts, percentatges, ràtios, densitats i índexs no són intercanviables. `49,9%` d'habitatge no principal a Vila-seca necessita el total d'habitatges com a denominador; `17.417 habitatges` és un volum; i `habitants/km²` relaciona població i superfície. Títol, eix i nota han de conservar aquesta unitat.

Una base petita també canvia la lectura: dos municipis poden tenir el mateix percentatge sobre totals molt diferents. Quan aquest contrast sigui rellevant, el gràfic pot necessitar una anotació, una taula auxiliar o una figura complementària de volums. Una absència no es converteix en zero; es deixa fora del càlcul que no pot realitzar-se i se'n conserva l'estat.

## Semiologia i gramàtica de la representació

Tots els gràfics del capítol, encara que tinguin noms diferents, combinen dades i decisions visuals. Bertin proporciona el vocabulari semiològic de marques i variables visuals. Wilkinson formalitza una gramàtica més àmplia que combina dades, transformacions, escales, elements geomètrics, coordenades i guies. Munzner relaciona atributs de les dades i tasques amb marques i canals perceptius. El manual utilitza aquests marcs per analitzar figures, però no els presenta com si fossin una sola teoria indistinta {% cite bertinSemiologyGraphics2010 wilkinsonGrammarGraphics2005 munznerVisualizationAnalysisDesign2014 %}.

En aquest manual, **camp** designa una columna concreta del llibre o de la taula; en termes analítics, aquell camp implementa una variable o atribut. El camp `housing_non_main_pct` és la columna; el percentatge d'habitatge no principal és la variable; la longitud d'una barra és el canal que la representa. Aquesta distinció evita atribuir al programari una teoria que pertany a la relació entre dades i representació.

### Elements bàsics d'un gràfic

Per revisar les figures del curs, s'utilitza una **pauta didàctica de sis components**: dades, marques, canals visuals, escales, sistema de coordenades i guies de lectura. És una síntesi operativa inspirada en els marcs anteriors, no una citació literal d'un únic autor. Serveix tant per construir una figura a partir d'una taula com per analitzar una figura ja acabada.

::: table "Elements bàsics d'un gràfic i funció que tenen en la lectura"
| Element | Què aporta | Exemple del projecte |
| --- | --- | --- |
| Dades (unitat d'observació, variables) | Defineix què es compara i amb quina unitat | El municipi com a fila i el seu percentatge com a valor |
| Marca (punt, línia, barra, sector, àrea) | Representa cada observació visiblement | Una barra per municipi |
| Canal visual (posició, longitud, forma, to) | Tradueix la dada en una propietat de la marca | La longitud de la barra codifica el percentatge |
| Escala (lineal, logarítmica, ordinal, de colors) | Assigna valors a posicions, mides o colors | Eix de percentatges amb origen zero |
| Coordenades (cartesianes o polars) | Ordenen les marques en el pla | Barres horitzontals ordenades de més alta a més baixa |
| Guies (títol, eixos, unitats, llegenda, font) | Expliquen com interpretar la figura | Títol que indica territori, període i unitat |
:::

### Eixos visibles i coordenades ocultes

Un **sistema de coordenades** organitza les marques dins del pla. Una **escala** estableix la correspondència entre dades i posicions; l'**eix** en fa llegible la direcció mitjançant graduacions i etiquetes. Ocultar-ne la línia o els números no elimina necessàriament l'escala. Per interpretar el gràfic cal esbrinar què significa desplaçar-se cap a la dreta, cap amunt o al voltant d'un centre, encara que aquestes guies no es dibuixin.

En coordenades **cartesianes**, l'eix horitzontal és el d'**abscisses**, habitualment $x$, i el vertical és el d'**ordenades**, habitualment $y$. Aquests noms indiquen orientació, no el paper de la variable ni una relació de causa i efecte. En les barres horitzontals del percentatge d'habitatge no principal, l'abscissa mesura percentatges i l'ordenada identifica municipis. En una dispersió, en canvi, tots dos eixos poden mesurar percentatges de variables diferents.

La primera distinció és entre una **escala de categories** i una escala quantitativa. A les barres municipals, pujar una fila significa canviar de municipi; la separació regular entre noms no mesura distància geogràfica ni diferència de població. Desplaçar-se deu punts sobre l'eix percentual sí que té una magnitud interpretable. En un histograma aquesta lectura canvia: l'eix horitzontal conté intervals numèrics i el vertical compta municipis, no identifica els seus noms.

També cal mirar les graduacions. En una escala **lineal**, distàncies iguals representen diferències iguals: el tram de 10 a 20 ocupa el mateix espai que el de 40 a 50. En una escala **logarítmica**, distàncies iguals representen factors iguals, com els trams de 10 a 100 i de 100 a 1.000. Llegir-los com si fossin increments constants falsejaria la comparació. El rang, l'origen, el sentit creixent i la unitat s'han d'identificar abans d'atribuir significat a la forma.

En coordenades **polars**, una posició es descriu mitjançant l'angle respecte d'una direcció inicial i la distància al centre o radi. Un gràfic circular es pot construir en aquest sistema: cada sector ocupa un interval angular i s'estén des del centre fins a un radi exterior comú. En l'anell també és comú el radi del buit interior. La volta completa representa el total; el radi exterior no varia entre sectors i no codifica una segona variable. La magnitud de cada part es tradueix en un angle, que es pot comprovar amb una regla de tres.

Les **barres radials** fan una assignació diferent: poden repartir categories en angles iguals i representar cada valor amb una distància al centre. Com a prova, es poden dibuixar dos sectors d'angle igual amb radis de 2 i 4 cm. El segon radi és el doble, però l'àrea és quatre vegades més gran. Cal decidir si es vol comparar longitud o superfície; els angles iguals no indiquen aquí quantitats iguals ni parts iguals d'un total.

Canviar de coordenades transforma la geometria i també la comparació perceptiva. Una barra cartesiana facilita comparar extrems sobre una escala comuna; quan es plega en un cercle, la mateixa magnitud es pot llegir com a angle, arc, radi o àrea segons el disseny. Interpretar una figura exigeix identificar on és l'origen, en quina direcció augmenta cada escala, quina unitat utilitza i quina propietat visible (posició, longitud, angle o àrea) porta realment la dada. Els elements que no varien, com el radi constant d'un anell, formen part de la disposició i no s'han d'interpretar com una variable.

Una lectura concreta consisteix a triar una marca i projectar-la mentalment sobre l'eix corresponent. Per a una barra, es llegeix l'extrem; per a un punt de dispersió, cal llegir les dues coordenades de la mateixa observació. Després es compara amb una segona marca i s'expressa la diferència amb la unitat adequada. Passar del 20% al 30% són deu punts percentuals, no un augment relatiu del 10%.

Les guies han de retolar l'eix amb la variable i la unitat necessàries, sense repetir el títol sencer. Si aquest ja identifica l'habitatge no principal, el territori i el període, l'eix pot indicar-ne breument el percentatge. A la dispersió, però, escriure només `%` als dos eixos seria insuficient: cal distingir el percentatge de població de 65 anys o més del percentatge d'habitatge no principal.

L'ordre anterior tampoc és un algorisme inflexible. Normalment es comença per dades i tasca, es prova una marca i uns canals i després s'ajusten escala, coordenades i guies. La revisió pot obligar a tornar enrere: una etiqueta il·legible pot exigir barres horitzontals; una escala inadequada pot fer canviar de barres a punts; i una absència pot requerir revisar la taula d'origen del gràfic.

### Dades, codificació i presentació

A Calc o Excel convé distingir tres decisions: quin rang de cel·les alimenta el gràfic, quin camp controla cada propietat visible i com es presenta el resultat. Si els valors estan mal aparellats, cal revisar les dades; si una barra exagera una diferència, cal revisar l'escala. Canviar tipografia, fons o quadrícula pot millorar la llegibilitat, però no corregeix cap d'aquests dos problemes.

### Marques i unitats representades

Les **marques** són els objectes visibles que representen observacions: punts, línies, barres, sectors o àrees. Aquest vocabulari deriva de la semiologia gràfica i és utilitzat també en marcs contemporanis de visualització. Una barra té forma rectangular, però la dada quantitativa es llegeix principalment mitjançant la longitud; un punt de dispersió es llegeix per posició; una línia temporal connecta posicions consecutives; i un municipi en un mapa és una marca superficial {% cite bertinSemiologyGraphics2010 munznerVisualizationAnalysisDesign2014 %}.

La marca ha de correspondre a la unitat. Si una barra representa un municipi, el lector ha de poder associar-la amb un únic codi i un únic valor. Si una línia representa una sèrie, els punts han de compartir definició, periodicitat i ordre. Si un cercle representa una magnitud, és la seva àrea i no el radi allò que s'ha d'escalar.

### Canals visuals i tasques de lectura

Un **canal visual** és una propietat de la marca que varia: posició, longitud, àrea, forma, orientació, textura, lluminositat o to. Bertin parlava de variables visuals; la terminologia de marques i canals és habitual en la literatura contemporània. Els canals no tenen la mateixa capacitat: posició i longitud alineades permeten comparar valors pròxims amb més precisió que àrea, angle o color, una diferència recolzada també per experiments de percepció gràfica {% cite bertinSemiologyGraphics2010 clevelandMcGillGraphicalPerception1984 munznerVisualizationAnalysisDesign2014 %}.

::: table "Canals visuals, lectures i exemples"
| Canal | Lectura principal | Exemple del projecte | Límit |
| --- | --- | --- | --- |
| Posició en escala comuna | Ordenar i estimar magnitud | Punts de dispersió i línia temporal | Necessita eixos, unitats i correspondència correcta |
| Longitud | Comparar magnituds | Barres d'habitatge no principal | Les barres quantitatives han de compartir origen |
| Àrea o mida | Estimar volum aproximat | Símbols proporcionals del capítol 8 | Es compara pitjor que una longitud i s'ha d'escalar per àrea |
| Forma | Identificar categories | Tipus de recurs en una dispersió | No expressa bé ordre ni quantitat |
| Orientació | Distingir direcció o patró | Trames o símbols lineals | Massa orientacions es confonen |
| Textura | Separar superfícies o reforçar absències | Patró de sense dades | Pot produir soroll en àrees petites |
| Lluminositat | Reconèixer ordre | Rampa clara-fosca d'una coropleta | Cal comprovar que la progressió sigui perceptible |
| To | Identificar categories | Sèries d'edat o tipus d'allotjament | Un arc de colors no expressa magnitud per si sol |
:::

La figura següent resumeix compatibilitats entre canals i marques. S'ha d'utilitzar com a repertori crític, no com una recepta: la pregunta, la mida i el suport poden descartar una combinació formalment possible.

![Matriu de variables visuals aplicada a marques puntuals, lineals i superficials: posició, mida, forma, orientació, valor, textura i to]({{ site.baseurl }}/assets/img/data-visualization/visual-variables-matrix.svg "La matriu ajuda a formular candidats; la decisió final depèn de la tasca, les dades i la mida. Figura d'elaboració pròpia a partir de Bertin."){: data-figure-width="54rem"}

### Identificar, ordenar i estimar magnitud

Els canals han de correspondre a l'operació mental. Per **identificar**, cal distingir categories sense suggerir superioritat: forma o to poden funcionar. Per **ordenar**, la posició, la mida o una progressió de lluminositat han de seguir el mateix sentit que la dada. Per **estimar magnitud**, posició i longitud solen ser preferibles. Utilitzar una paleta qualitativa per a valors quantitatius o sectors circulars per comparar diferències petites dificulta una tasca que una escala comuna resoldria millor.

La **codificació redundant** combina dos senyals compatibles. Vila-seca pot destacar-se amb color i amb una etiqueta directa; una absència pot utilitzar gris i trama. Aquesta redundància ajuda l'accessibilitat sempre que no introdueixi un segon significat contradictori.

### Proporcionalitat, origen i superfície visible

Quan una magnitud es representa mitjançant una superfície acolorida, la superfície visible també comunica quantitat. Wilke anomena aquest criteri **principi de proporcionalitat de tinta** {% cite wilkeFundamentalsDataVisualization2019 %}. Una barra truncada pot situar correctament l'extrem sobre l'eix i, alhora, exagerar la diferència perquè la longitud visible ja no és proporcional.

::: subfigures a+b "Efecte de l'origen de l'eix sobre la proporcionalitat d'un gràfic de barres. Figures de Claus O. Wilke, CC BY-NC-ND 4.0."
![Gràfic de barres amb eix truncat]({{ site.baseurl }}/assets/img/data-visualization/wilke-proportional-ink-truncated-axis.png "Gràfic de barres amb eix truncat: la longitud exagera la diferència.")
![Mateixes dades amb origen zero]({{ site.baseurl }}/assets/img/data-visualization/wilke-proportional-ink-zero-axis.png "Gràfic de barres amb origen zero: aquest origen conserva la proporcionalitat.")
:::

Les barres quantitatives en escala lineal han de començar ordinàriament a zero. Un punt o una línia codifiquen principalment per posició i poden ampliar un interval justificat. Quan la mida d'un cercle representa $X$, l'àrea ha de ser proporcional; el diàmetre varia amb l'arrel quadrada:

$$
D_2 = D_1\sqrt{\frac{X_2}{X_1}}
$$

La regla de tres és útil quan hi ha una **proporcionalitat declarada**. S'aplica a longituds de barres amb origen zero, a angles de sectors d'un mateix cercle, a àrees de símbols proporcionals o a gruixos de bandes. No s'aplica directament al radi d'una bombolla, al color d'una categoria ni a una posició sobre una escala logarítmica. Abans de mesurar cal identificar quina propietat porta la dada i quina és la seva referència.

## Famílies bàsiques de representació

Hi ha molts tipus de gràfics, però no són un catàleg d'efectes. Tots intenten assignar marques i canals a una estructura de dades perquè el lector consulti, compari, segueixi, distribueixi o relacioni valors. El nom del gràfic és secundari davant la correspondència entre pregunta, unitat, marca i canal.

### Consultar valors: taula, gràfic o mapa

Una taula és adequada quan cal recuperar xifres exactes, codis o definicions. Les barres acceleren la comparació; un histograma resumeix la distribució; i un mapa conserva localització i veïnatge. Cap opció domina sempre. Si l'espai no forma part de la pregunta, ordenar les barres sol permetre comparar millor que acolorir polígons; si cal saber on apareixen valors alts, el mapa aporta una relació que la barra ha eliminat.

::: table "Pregunta, estructura i família bàsica"
| Tasca | Estructura mínima | Família principal | Control imprescindible |
| --- | --- | --- | --- |
| Consultar | Identificador i camps | Taula | Unitats, font i capçalera única |
| Comparar magnituds | Categoria + valor | Barres o punts alineats | Ordre funcional i origen coherent |
| Comparar composicions | Parts del mateix total | Barres apilades al 100% o anell | Les parts reconstrueixen el total |
| Seguir evolució | Temps + valor comparable | Línia | Ordre, periodicitat i canvis de definició |
| Examinar distribució | Conjunt de valors comparables | Histograma o caixa | Intervals, cobertura i valors extrems |
| Explorar relació | Dues variables per observació | Dispersió | Aparellament per codi i absències |
| Conservar localització | Valor + geometria | Mapa | Escala, unitat territorial i mètode cartogràfic |
:::

### Comparar magnituds: barres i punts alineats

Una barra representa una categoria amb una longitud. L'ordre descendent facilita trobar màxims i mínims; l'ordre cronològic o geogràfic serveix altres preguntes. Amb noms municipals llargs, les barres horitzontals permeten llegir etiquetes sense girar-les. La llegenda és redundant quan només hi ha una sèrie i el títol ja n'indica la variable.

Les barres agrupades són útils quan hi ha poques sèries i cal comparar cada subcategoria dins de cada categoria i també entre categories. Si l'acumulació de grups dificulta seguir una sèrie, convé passar a petits múltiples. Quan els panells mostren la mateixa magnitud, han de conservar el mateix rang d'eix, ordre de categories i criteri cromàtic; si les escales canvien, una forma semblant pot amagar magnituds molt diferents {% cite generalitatGuiaVisualitzacioDades2018 %}.

La mateixa taula pot produir variants que responen preguntes diferents. La comparació següent conserva els habitatges principals i no principals d'Altafulla, Roda de Berà, Salou, Torredembarra i Vila-seca, els cinc municipis litorals del Tarragonès, i només canvia la disposició de les barres. Així es pot atribuir la diferència de lectura a la geometria i a la normalització, no a un canvi de dades.

![Barres agrupades d'habitatges principals i no principals als cinc municipis litorals del Tarragonès]({{ site.baseurl }}/assets/img/data-visualization/housing-bars-grouped-tarragones-2021.svg "Barres agrupades: cada municipi té dues barres sobre el mateix origen, de manera que es poden comparar tant els habitatges principals com els no principals. Font: Idescat, habitatges per tipus d'habitatge, 2021."){: data-figure-width-web="43rem" data-figure-width-pdf="100%"}

![Barres apilades en valors absoluts d'habitatges principals i no principals als cinc municipis litorals del Tarragonès]({{ site.baseurl }}/assets/img/data-visualization/housing-bars-stacked-tarragones-2021.svg "Barres apilades absolutes: la longitud completa representa el parc d'habitatges municipal i els dos segments en reconstrueixen el total. Font: Idescat, habitatges per tipus d'habitatge, 2021."){: data-figure-width-web="43rem" data-figure-width-pdf="100%"}

![Barres apilades al 100% d'habitatges principals i no principals als cinc municipis litorals del Tarragonès]({{ site.baseurl }}/assets/img/data-visualization/housing-bars-percent-tarragones-2021.svg "Barres apilades al 100%: totes tenen la mateixa longitud i només comparen la composició percentual del parc d'habitatges. Font: Idescat, habitatges per tipus d'habitatge, 2021."){: data-figure-width-web="43rem" data-figure-width-pdf="100%"}

En la versió agrupada, totes dues sèries comencen a zero i es poden comparar amb precisió, però el total municipal s'ha de sumar mentalment. En l'apilada absoluta, la longitud completa mostra que Salou té el parc més gran dels cinc, però només el segment principal comparteix origen; comparar els segments no principals exigeix estimar longituds que comencen en posicions diferents. En la versió al 100%, Salou i Roda de Berà destaquen pel pes de l'habitatge no principal, però desapareix la diferència entre 31.523 habitatges a Salou i 4.851 a Altafulla. La normalització no millora el mateix gràfic: canvia la pregunta que es pot respondre.

::: subfigures a+b "Comparació de barres i punts sobre línies fines per a la mateixa variable i el mateix ordre municipal."
![Barres ordenades del percentatge d'habitatge no principal als municipis del Tarragonès]({{ site.baseurl }}/assets/visualizations/data-visualization/non-principal-housing-ordered-bars.vl.json "Gràfic de barres ordenades: cada barra és un municipi; la longitud codifica un percentatge de 2021. L'ordre descendent facilita trobar els valors més alts i més baixos."){: data-figure-width="54rem"}
![Punts al final de línia del percentatge d'habitatge no principal dels municipis del Tarragonès]({{ site.baseurl }}/assets/quarto/data-visualization/non-principal-housing-dot-plot.qmd "Gràfic de punts sobre línies fines: la línia fina uneix l'origen amb el valor i el punt marca l'extrem. Amb 22 municipis, aquest disseny redueix la tinta de la barra sense perdre la posició ordenada del valor."){: data-figure-width="54rem"}
:::

El **diagrama de punts** sobre línia fina estalvia tinta: la barra ocupa una superfície que només serveix per unir l'origen amb el valor, i aquesta unió es pot dibuixar amb una línia prima i un punt. Wilke el recomana quan la pregunta no necessita la metàfora de volum de la barra {% cite wilkeFundamentalsDataVisualization2019 %}. La línia ha de començar a l'origen coherent amb la resta del gràfic, i l'altura de traç no ha de convertir-se en una àrea que distorsioni la percepció.

La figura permet veure el rànquing, però no on és cada municipi ni quants habitatges formen el denominador. Aquestes limitacions justifiquen un mapa i una mètrica absoluta complementaris, no una sobrecàrrega del mateix gràfic.

Per llegir un cas, es localitza Vila-seca a l'eix de categories i se segueix la barra o el punt fins a l'escala percentual: el valor és aproximadament 49,9%. Roda de Berà se situa en 64,7%, uns 14,8 punts percentuals més. La seva barra més llarga indica un pes relatiu superior, però Vila-seca té més habitatges no principals en nombres absoluts. El rang que alimenta el gràfic ha de conservar municipi i percentatge aparellats; els recomptes permeten comprovar què hi ha darrere d'aquesta diferència.

::: table "Tres files de control de la taula municipal d'habitatge, 2021" {: data-caption-source="Font: Idescat, habitatges per tipus d'habitatge. Percentatges mostrats amb un decimal."}
| Codi | Municipi | Habitatges totals | No principals | No principals (%) |
| --- | --- | ---: | ---: | ---: |
| `431310` | Roda de Berà | 8.762 | 5.673 | 64,7 |
| `431711` | Vila-seca | 17.417 | 8.692 | 49,9 |
| `431093` | la Pobla de Mafumet | 1.615 | 195 | 12,1 |
:::

Aquestes tres files són un fragment de la taula de 22 municipis, no el conjunt comarcal. Cada percentatge es calcula dividint els no principals pel total de la mateixa fila i multiplicant per 100; el full conserva la precisió del càlcul. Ordenar totes les files pel resultat canvia la disposició del gràfic, però no modifica les dades. Ordenar només la columna percentual separaria els valors dels municipis i produiria una figura incorrecta.

Per comprovar barres simples i punts alineats es pot preparar un esbós amb els valors simulats 20, 40 i 60 sobre una escala de 0 a 100 que mesuri 10 cm. Els extrems han de quedar a 2, 4 i 6 cm de l'origen. Substituir les barres per punts sobre línies fines conserva aquestes posicions; canviar el gruix dels punts no ha de suggerir una nova quantitat.

Les variants agrupada, apilada absoluta i apilada al 100% es poden construir amb dos casos simulats: 60 habitatges principals i 40 no principals en un cas, i 90 principals i 60 no principals en l'altre. Cal comprovar que les apilades absolutes sumin 100 i 150, mentre que les percentuals coincideixin en un repartiment 60/40. A les agrupades, cadascuna de les dues barres parteix de zero; a les apilades, la segona part es llegeix restant els seus dos extrems. La mateixa taula produeix comparacions diferents sense canviar cap recompte.

### Comparar composicions: barres apilades i anells

Una **composició** només existeix quan les parts comparteixen un total. Els grups 0–14, 15–64 i 65+ reconstrueixen la població mostrada de cada municipi i es poden comparar amb barres apilades al 100%. Percentatges d'ocupació de municipis diferents no són parts del mateix total i no s'han d'apilar.

En una barra apilada, la longitud total es compara sobre un origen comú, però només el primer segment comparteix també una base comuna. Els segments interiors comencen en posicions diferents i es comparen amb menys precisió. Si la pregunta se centra en una part concreta o en diferències petites, convé situar-la sempre en el mateix extrem, separar les parts en barres alineades o utilitzar petits múltiples {% cite generalitatGuiaVisualitzacioDades2018 %}.

Un circular o un anell pot resumir poques parts d'un únic total, com habitatges principals i no principals del conjunt comarcal. La seva construcció exigeix respondre «100% de què?» i mantenir visibles les categories absents o desconegudes. Per comparar molts municipis, les barres apilades són més eficients que una col·lecció de cercles.

![Anell de la composició del parc d'habitatges del Tarragonès (2021): principals i no principals]({{ site.baseurl }}/assets/quarto/data-visualization/housing-donut-tarragones.qmd "L'anell mostra les parts d'habitatges principals i no principals d'un únic total: 169.179 habitatges del Tarragonès el 2021. El buit central no porta cap dada; les etiquetes amb percentatge i magnitud eviten dependre només de l'angle. Font: Idescat, habitatges per tipus d'habitatge, 2021."){: data-figure-width="40rem"}

Per llegir aquest anell cal començar pel total de 169.179 habitatges, seguir la volta completa com una escala del 0 al 100% i associar cada interval angular amb la categoria indicada pel color i l'etiqueta. El buit central i el gruix constant de l'anell no representen dades. Aquesta reconstrucció de l'eix ocult permet distingir la codificació quantitativa de les decisions de composició.

La taula que alimenta l'anell té dues files, una per tipus d'habitatge, amb 103.074 principals i 66.105 no principals. S'obté sumant els recomptes dels 22 municipis i després calculant les proporcions sobre el total comarcal. Fer la mitjana dels 22 percentatges municipals respondria una altra pregunta. El to identifica el tipus i la fracció de volta en representa el pes; l'ordre dels sectors no és una jerarquia addicional.

#### Construir sectors i comprovar-los amb una regla de tres {#sectors-regla-de-tres}

En un circular pla, el 100% correspon a una volta de **360°**. Si una categoria conté $n_i$ observacions d'un total $N$ i representa un percentatge $p_i$, l'angle del sector ha de complir aquesta correspondència:

$$
\frac{\theta_i}{360^\circ}=\frac{n_i}{N}=\frac{p_i}{100},
\qquad
\theta_i=\frac{p_i}{100}\,360^\circ
\label{eq:pie-sector-angle}
$$

Per exemple, el 50% necessita 180°, el 25% necessita 90° i el 30% necessita $30\times360/100=108^\circ$. La comprovació inversa recupera el percentatge a partir d'un angle mesurat: $p_i=100\,\theta_i/360^\circ$. Un sector de 90° representa, per tant, el 25%, sigui quina sigui l'etiqueta que s'hi hagi escrit.

Com que tots els sectors comparteixen radi, angle, longitud d'arc i àrea representen la mateixa fracció del cercle. En un anell de radis interior i exterior constants també es conserva aquesta proporció angular. La comprovació deixa de ser directa si es deforma el cercle fins a convertir-lo en una el·lipse, s'utilitzen radis diferents o s'afegeix perspectiva tridimensional. La mida de la lletra i el color identifiquen i retolen les parts, però no validen la quantitat.

Al full de càlcul cal distingir valor i format: una cel·la que conté `0,30` i es mostra com a `30%` es multiplica directament per 360. Si s'hi ha escrit el nombre `30`, primer s'ha de dividir per 100. Confondre aquestes dues representacions multiplica l'angle per cent.

#### Exercici: etiquetes correctes i sectors incoherents {#auditoria-sectors-circulars}

La taula següent conté **100 respostes simulades**, amb una única elecció de mitjà principal per resposta. No descriu una enquesta real. Els recomptes són el punt de partida que cal conservar mentre es comprova el dibuix.

::: table "Dades simulades per comprovar un gràfic circular"
| Codi | Mitjà principal | Respostes | Percentatge |
| --- | --- | ---: | ---: |
| A | Vehicle privat | 50 | 50% |
| B | Transport públic | 30 | 30% |
| C | Altres mitjans | 20 | 20% |
| Total | | 100 | 100% |
:::

La figura incorpora errors geomètrics intencionats. Les etiquetes concorden amb la taula i sumen 100%, però això encara no prova que els sectors siguin proporcionals.

![Circular deliberadament incorrecte: A està etiquetat com a 50% però ocupa un quart de cercle; B diu 30% però ocupa mitja volta; C diu 20% i ocupa l'altre quart]({{ site.baseurl }}/assets/img/data-visualization/pie-sector-audit-incorrect.svg "Circular per auditar: cal contrastar els percentatges escrits amb els angles centrals. Dades simulades i error intencional per a l'exercici."){: data-figure-width-web="36rem" data-figure-width-pdf="75%"}

1. Calcular l'angle que correspon a cada percentatge de la taula. Quin sector hauria d'ocupar exactament mitja volta?
2. Mesurar els angles de la figura amb un transportador o reconèixer-hi els quarts i la mitja volta. La figura ha de conservar la proporció circular en imprimir-la o ampliar-la.
3. Fer la regla de tres inversa i escriure quin percentatge representa realment cada sector dibuixat.
4. Explicar per què sumar 100% a les etiquetes i 360° als sectors són controls necessaris però insuficients.
5. Reconstruir el gràfic a partir dels recomptes de la taula. Si aquests recomptes són els correctes, canviar les etiquetes per adaptar-les al dibuix no és una correcció vàlida.

La comprovació raonada separa les dues correspondències. En aquesta figura els angles mesurats són 90°, 180° i 90°: el dibuix representa un repartiment 25/50/25, diferent del 50/30/20 declarat.

::: table "Comprovació dels angles i dels percentatges de l'exercici"
| Sector | Percentatge escrit | Angle necessari | Angle dibuixat | Percentatge dibuixat |
| --- | ---: | ---: | ---: | ---: |
| A | 50% | 180° | 90° | 25% |
| B | 30% | 108° | 180° | 50% |
| C | 20% | 72° | 90° | 25% |
| Total | 100% | 360° | 360° | 100% |
:::

![Circular corregit amb A al 50%, B al 30% i C al 20%, representats per sectors de 180, 108 i 72 graus]({{ site.baseurl }}/assets/img/data-visualization/pie-sector-audit-correct.svg "Correcció geomètrica de les mateixes dades simulades. Es mantenen radi, colors, ordre i etiquetes; canvien els angles dels sectors."){: data-figure-width-web="36rem" data-figure-width-pdf="75%"}

Com a darrer control, es pot transformar el cercle corregit en un anell mantenint les mateixes divisions angulars. Obrir un buit central igual per a totes les parts no ha de canviar el repartiment. Una tolerància petita de mesura o arrodoniment és raonable, però no explica diferències com escriure 50% sobre un quart de cercle.

Un gràfic circular pot quedar-se en una codificació mínima o evolucionar cap a una representació més llegible sense deixar de ser un gràfic de composició. Un títol descriptiu, un total central, etiquetes externes i pictogrames redundants poden reduir l'ambigüitat sense afegir una conclusió narrativa ni una segona representació de les dades. La comparació següent permet auditar aquesta progressió sense assumir que més elaboració sempre significa més claredat o més evidència.

::: subfigures a+b/c "Evolució docent d'un gràfic circular insuficient a un gràfic en anell documentat. Elaboracions pròpies; dades d'ocupació del sòl del CREAF, 2005."
![Gràfic circular amb quatre percentatges, però sense títol, categories, període, total ni font]({{ site.baseurl }}/assets/img/data-visualization/pie-chart-audit.svg "Els sectors sumen 100%, però els percentatges sols no permeten saber què es mesura ni què representa cada color.")
![Gràfic circular de l'ocupació del sòl de Catalunya el 2005, amb categories i etiquetes directes]({{ site.baseurl }}/assets/img/data-visualization/chart-catalonia-landuse-2005.png "El títol, el territori, l'any, les categories i els percentatges converteixen els sectors en una composició interpretable. Elaboració pròpia a partir de dades del CREAF.")
![Gràfic en anell de l'ocupació del sòl de Catalunya el 2005, amb total central, etiquetes externes i pictogrames]({{ site.baseurl }}/assets/img/data-visualization/landuse-catalonia-2005-infographic.svg "L'anell centra el total i separa les quatre categories amb colors contrastats. Els percentatges, els noms i els pictogrames queden fora dels sectors per evitar solapaments i no dependre només del color. Elaboració pròpia a partir de dades del CREAF."){: data-figure-width-web="43.5rem" data-figure-width-pdf="100%"}
:::

La subfigura `a` ja falla per un problema més bàsic que la comparació dels angles: quatre percentatges i quatre colors no identifiquen la variable ni les categories, i tampoc no permeten verificar el total o la procedència. La subfigura `b` resol aquesta mancança amb un títol, un àmbit, un any i etiquetes directes. Encara conserva els límits del circular: el sector de les aigües continentals és difícil d'estimar i una barra ordenada facilitaria comparar diferències petites.

La subfigura `c` reprèn exactament les dades de `b`, però converteix el cercle en un anell, situa el total al centre i trasllada els percentatges i els noms fora dels sectors. Els pictogrames de bosc, cultiu, ciutat i aigua reforcen les categories sense substituir-ne els noms, i els separadors blancs ajuden a distingir els dos sectors més petits. La millora prové de l'espai, el contrast i la redundància gràfica, no d'afegir una barra, una conclusió nova o més dades.

![Estructura d'edats per grans grups dels municipis del Tarragonès, 2021]({{ site.baseurl }}/assets/quarto/data-visualization/age-structure-tarragones.qmd "Gràfic de barres apilades al 100%: cada barra representa un municipi i equival al 100% de la seva població. La longitud de cada segment codifica el percentatge d'un grup d'edat i el color l'identifica; l'ordenació per pes relatiu dels 65+ facilita comparar perfils."){: data-figure-width="54rem"}

En aquestes barres d'edat, la posició identifica el municipi i cada color identifica un grup; la longitud del segment expressa la seva proporció. Per llegir un segment interior cal restar-ne els dos límits: si ocupa el tram del 15% al 80%, representa un 65%, no un 80%. La taula necessita els recomptes de cada grup d'edat per municipi i el total utilitzat com a denominador. La normalització permet comparar perfils, però les barres igualment llargues no indiquen poblacions iguals.

### Representar el temps: evolució, esdeveniments i durades

El temps acostuma a situar-se a l'eix d'abscisses perquè l'esquerra-dreta ofereix una direcció de lectura estable i permet reservar l'eix d'ordenades per a una magnitud. És una convenció molt estesa, no una propietat natural del temps: una cronologia pot ser vertical i un calendari pot organitzar-se com una matriu. El criteri essencial és que la direcció, l'interval i les absències siguin recognoscibles i que posicions igualment separades només representin intervals iguals quan l'escala ho garanteix.

#### Seguir una magnitud amb una línia

Una línia connecta observacions perquè l'ordre temporal és part de la dada. La sèrie de població de Vila-seca utilitza una definició anual comparable del Padró entre 2000 i 2022. Cada punt és un any; la línia ajuda a seguir canvis de ritme, però no demostra quina causa els ha produït ni autoritza a extrapolar-los.

![Evolució anual de la població de Vila-seca entre 2000 i 2022]({{ site.baseurl }}/assets/quarto/data-visualization/population-vila-seca-series-line.qmd "Gràfic de línia temporal: la posició vertical codifica la població i la posició horitzontal ordena els anys. Font: Idescat, a partir del Padró continu de l'INE."){: data-figure-width="52rem"}

La **relació d'aspecte**, el rang vertical i la selecció d'anys poden fer semblar el mateix canvi més brusc o més suau. Cal mostrar període i unitat, revisar ruptures metodològiques i descriure el passat com a canvi observat, no com a previsió.

La taula mínima té una fila per any i dues columnes, any i població, amb territori i definició documentats. Un punt es llegeix creuant l'any amb el nombre d'habitants; un tram es llegeix comparant els dos extrems i el temps transcorregut. La línia entre dos recomptes anuals no aporta observacions mensuals. Si faltés un any, caldria conservar l'absència i comprovar que el programa no converteix els anys restants en categories equidistants.

Un exercici de construcció consisteix a representar una sèrie simulada amb valors 100, 120 i 180 als anys 2020, 2021 i 2024. El segon interval horitzontal ha de ser tres vegades més llarg que el primer. Els increments són 20 i 60, però tots dos equivalen a un augment mitjà de 20 unitats per any. Cal comprovar què passaria si el programa espaiés els tres anys com a categories equidistants: la forma canviaria tot i conservar els nombres. Els anys intermedis continuen sense observació.

#### Ordenar fites i planificar durades

Una **cronologia** selecciona fites i en fa visible l'ordre. Pot utilitzar una escala temporal proporcional, però també pot repartir els esdeveniments amb separacions regulars només per facilitar-ne la lectura. En aquest segon cas, la posició indica «abans» i «després», però la distància gràfica no mesura quant temps ha passat. Alternar les etiquetes per damunt i per sota de la línia acostuma a ser una decisió de composició, no una segona variable.

![Cronologia conceptual de la traça d'una figura, des de la font fins a la publicació]({{ site.baseurl }}/assets/diagrams/data-visualization/mermaid-timeline.mmd "Cronologia conceptual: la posició horitzontal ordena quatre fites, però la separació entre elles no representa una durada mesurada. Figura d'elaboració pròpia."){: data-figure-width="54rem"}

Un **diagrama de Gantt** representa intervals: cada barra comença i acaba en una posició temporal i cada fila identifica una tasca o un grup. La longitud informa de la durada; la superposició mostra simultaneïtat; i una barra que comença quan n'acaba una altra pot expressar una seqüència planificada. Aquesta coincidència no demostra per si sola una dependència: si una tasca no pot començar fins que una altra acabi, el diagrama o el text ho ha d'indicar explícitament.

![Diagrama de Gantt esquemàtic del cicle breu d'una figura reproduïble]({{ site.baseurl }}/assets/diagrams/data-visualization/mermaid-gantt.mmd "Diagrama de Gantt docent: l'eix horitzontal és una escala de calendari, les files separen fases i la longitud de cada barra mostra la durada. Les dates són esquemàtiques i no constitueixen el calendari del curs. Figura d'elaboració pròpia."){: data-figure-width="48rem"}

Per construir aquest Gantt caldria una fila per tasca i camps per al nom, l'inici i el final —o l'inici i la durada—, més les dependències si n'hi ha. La posició vertical separa tasques; la posició inicial i la longitud de la barra codifiquen temps. A la cronologia conceptual anterior n'hi ha prou amb fita, ordre i descripció: afegir-hi una distància temporal sense dates conegudes inventaria una precisió que la taula no conté.

Per comprovar la diferència, es pot dibuixar una cronologia de quatre fites sense dates i variar-ne les separacions: només se n'ha de conservar l'ordre. En un Gantt simulat, en canvi, una tasca que comença al dia 0 i dura dos dies ocupa l'interval 0–2; una altra que comença al dia 1 i dura tres dies ocupa l'interval 1–4. Amb una escala d'1 cm per dia, les barres mesuren 2 i 3 cm i se superposen durant un dia. Aquí canviar les distàncies sí que canviaria les dades representades.

#### Llegir el temps quan l'eix no es dibuixa

No totes les representacions temporals necessiten una línia contínua ni un eix graduat visible. A [*Based on a True True Story?*](https://informationisbeautiful.net/visualizations/based-on-a-true-true-story/), cada pel·lícula es converteix en una franja que avança de l'inici al final. Les escenes ocupen intervals obtinguts a partir dels minuts d'inici i final, i el color les classifica com a certes, aproximades, falses o desconegudes segons el criteri editorial seleccionat. L'eix temporal queda ocult perquè no es dibuixen marques ni minuts, però l'ordre i l'amplada dels segments permeten seguir la successió i la durada relativa de les escenes. L'eix vertical només separa pel·lícules; no representa una segona magnitud.

![Captura de «Based on a True True Story?», amb quatre pel·lícules descompostes en intervals temporals acolorits segons el grau de veracitat atribuït a cada escena]({{ site.baseurl }}/assets/img/data-visualization/based-on-true-true-story-information-is-beautiful-2022.png "«Based on a True True Story?», publicada el 2016 i actualitzada el 2022. Disseny i concepte: David McCandless; recerca: Stephanie Starling i David McCandless; codi: Omid Kashan. © Information is Beautiful. Reproducció segons el permís gratuït per a usos educatius no comercials; aquest recurs queda exclòs de la llicència Creative Commons del manual."){: data-figure-width-web="58rem" data-figure-width-pdf="78%"}

La lectura és ràpida perquè combina dos canals separats: la posició i l'amplada expliquen quan passa cada escena i quant dura, mentre que el to n'identifica la categoria. Les franges tenen la mateixa amplada total i normalitzen pel·lícules de durades diferents; per tant, permeten comparar-ne la composició relativa, no alinear el mateix minut entre títols. El percentatge resumeix la classificació seleccionada, però no substitueix la seqüència: dues pel·lícules poden obtenir una proporció semblant i distribuir les escenes falses en moments molt diferents. La [visualització interactiva](https://informationisbeautiful.net/visualizations/based-on-a-true-true-story/) permet consultar cada interval i les [dades publicades pels autors](https://docs.google.com/spreadsheets/d/1sJDpzYH_sMYuYHqkmZeJGIq_TEXGDjboYdSoew7UjZ8/edit#gid=1961296402) en documenten l'inici, el final, la classificació i les fonts.

Una hipòtesi de taula seria una fila per escena, amb identificador de pel·lícula, inici, final i categoria de veracitat. La durada es calcula restant final i inici; dividir-la per la durada de la pel·lícula permet obtenir l'amplada relativa. Una taula amb només pel·lícula i percentatge final podria reproduir el resum, però no la successió de segments. Reconèixer aquesta informació perduda és part de la lectura del gràfic.

La normalització es pot comprovar amb dues durades hipotètiques de 90 i 180 minuts. Un segment que ocupi el 10% de cada franja equival a 9 i 18 minuts, respectivament. Cal esbossar les dues franges amb la mateixa amplada i justificar per què segments iguals no representen el mateix nombre de minuts. Per reconstruir temps absoluts cal conservar la durada total de cada pel·lícula.

### Examinar una distribució: histograma i diagrama de caixa

Un histograma agrupa valors quantitatius en intervals i compta observacions. No mostra municipis individuals ni categories preexistents. Amb només 22 municipis, canviar l'amplada o l'origen dels intervals pot modificar molt la forma percebuda; per això s'han de publicar els límits i comprovar que les freqüències sumen 22.

![Histograma municipal del percentatge d'habitatge no principal al Tarragonès]({{ site.baseurl }}/assets/quarto/data-visualization/housing-histogram-tarragones.qmd "Histograma: cada barra compta municipis dins d'un interval percentual. Els intervals són una decisió analítica, no categories de la font."){: data-figure-width="50rem"}

Aquí «40» a l'eix horitzontal designa un percentatge d'habitatge, mentre que «4» a l'eix vertical designaria quatre municipis. L'altura no indica el percentatge mitjà de la barra. La taula original continua tenint una fila per municipi; la taula resum té una fila per interval, amb límit inferior, límit superior i freqüència. Cal declarar a quin interval pertany un valor situat exactament en un límit. Amb intervals d'igual amplada, comparar altures permet comparar freqüències; els límits no es poden canviar sense recalcular-les.

Es pot construir un histograma de prova amb sis percentatges simulats: 12, 18, 20, 27, 35 i 42. Amb intervals $[10,20)$, $[20,30)$, $[30,40)$ i $[40,50)$, les freqüències han de ser 2, 2, 1 i 1, i sumar sis. El valor 20 pertany al segon interval. Si s'uneixen els dos primers intervals, cal recalcular el recompte; no n'hi ha prou amb ampliar una barra. Amb amplades desiguals, l'altura ha de representar la freqüència dividida per l'amplada perquè sigui l'àrea, i no l'altura sola, la que conservi la freqüència.

Un diagrama de caixa resumeix mediana, quartils i possibles valors extrems. La **mediana** deixa la meitat de les observacions a cada costat; el primer i el tercer **quartil** delimiten el 50% central, que forma la caixa. Els bigotis estenen el resum segons la regla declarada i els punts que en queden fora es mostren com a possibles valors extrems. És compacte per comparar distribucions, però amaga part de la forma i la localització. Un valor extrem és una observació per revisar, no un error automàtic.

::: subfigures a+b "Ús del diagrama de caixa per descriure i comparar distribucions."
![Diagrama de caixa del percentatge d'habitatge no principal dels municipis del Tarragonès (2021)]({{ site.baseurl }}/assets/quarto/data-visualization/boxplot-non-main-housing-tarragones.qmd "Diagrama de caixa d'una distribució: la caixa abasta els quartils i la línia central marca la mediana; els punts superposats mostren els 22 municipis. Amb la regla d'1,5 vegades el rang interquartílic, cap observació queda fora dels bigotis."){: data-figure-width="48rem"}
![Diagrama de caixa de la longitud del sèpal per a tres espècies d'iris, on cada caixa descriu una distribució i les caixes es comparen entre si]({{ site.baseurl }}/assets/quarto/data-visualization/boxplot-species-iris.qmd "Diagrama de caixa per categories: cada caixa resumeix una espècie; comparar els centres, les dispersions i els possibles extrems permet dir ràpidament si els grups se superposen o si una espècie n'ocupa una part extrema. Dades del conjunt de Fisher de 1936."){: data-figure-width="48rem"}
:::

En la caixa municipal, el percentatge es llegeix sobre l'eix horitzontal. La mediana és aproximadament el 31,0% i el 50% central queda entre el 21,3% i el 51,6%. Els bigotis arriben als valors observats més allunyats que encara queden dins del marge d'1,5 vegades el rang interquartílic respecte de la caixa. En aquest conjunt abasten del 12,1% al 64,7%: hi ha valors alts, però cap observació fora dels bigotis. El petit desplaçament vertical dels punts en facilita la visibilitat; no representa una segona variable.

La funció comparativa es veu millor amb les tres espècies d'iris. Cal localitzar les medianes sobre l'escala comuna i comparar l'extensió de les caixes i els bigotis, sense prendre la superfície dels rectangles com un recompte de flors. Així es pot discutir quins grups se superposen o mostren més variabilitat, conservant la distinció entre observacions individuals i resums.

La caixa exigeix llegir primer quin eix porta la magnitud i quines posicions corresponen a mediana, quartils i bigotis. La seva amplada habitualment no compta observacions. Per recalcular-la calen els valors individuals —municipi i percentatge, o flor, espècie i longitud—, no només una fila amb el valor mitjà. A partir dels quartils dibuixats no es pot recuperar una única taula original: conjunts diferents poden compartir el mateix resum.

Una prova manual pot utilitzar els valors simulats 10, 20, 30, 40 i 90, amb mediana 30 i quartils inclusius 20 i 40. Cal dibuixar la caixa, calcular el rang interquartílic de 20 i els llindars de −10 i 70, i situar els bigotis als valors observats admesos: 10 i 40. El 90 queda com a punt exterior. Aquesta prova permet comprovar que els bigotis no arriben necessàriament al mínim i al màxim, ni s'aturen automàticament als llindars calculats. El criteri de quartils s'ha de mantenir explícit quan es compara amb el resultat del full.

### Explorar una relació: dispersió

En una dispersió, cada punt representa una unitat amb dos valors. El codi municipal ha de garantir que `x` i `y` pertanyen al mateix municipi; emparellar per número de fila després d'ordenar una sola taula pot crear punts falsos. La posició permet llegir direcció, forma, intensitat aparent i excepcions.

::: subfigures a+b "Comparació de dispersions amb intensitats d'associació molt diferents."
![Dispersió entre la població de 65 anys o més i l'habitatge no principal als municipis del Tarragonès]({{ site.baseurl }}/assets/quarto/data-visualization/ageing-housing-scatter-tarragones.qmd "Gràfic de dispersió amb línia d'ajust: cada punt és un municipi identificat pel mateix codi a les dues variables. La línia d'ajust resumeix una associació aparent, però no demostra causalitat."){: data-figure-width="48rem"}
![Dispersió entre el total d'habitatges i la població total, amb l'equació d'ajust lineal i el coeficient de determinació]({{ site.baseurl }}/assets/quarto/data-visualization/housing-population-scatter-tarragones.qmd "Gràfic de dispersió amb ajust lineal: cada punt és un municipi. La recta és l'ajust de mínims quadrats: l'equació escrita a la figura permet llegir-hi un pendent aproximat, i el R² en percentatge quantifica com de prop queden els punts de la línia."){: data-figure-width="48rem"}
:::

Els punts municipals no s'uneixen amb línies perquè no formen una seqüència. Amb observacions superposades es pot utilitzar transparència; qualsevol desplaçament artificial s'ha de documentar. Una línia d'ajust resumeix una associació, però no converteix habitatge no principal en causa d'envelliment ni a l'inrevés.

En la primera dispersió, el punt de Vila-seca es llegeix aproximadament com el parell 14,5% de població de 65 anys o més i 49,9% d'habitatge no principal. Són dues variables amb denominadors diferents, encara que comparteixin el símbol `%`. La taula necessita una fila per municipi i les dues columnes aparellades pel codi. Si s'afegeixen bombolles, cal una tercera columna amb la població total; canviar-ne l'àrea no ha de moure les coordenades.

Per comprovar la posició es pot fer un esbós amb un eix horitzontal de 0–25% i un de vertical de 0–100%, tots dos de 10 cm. Amb els valors arrodonits de Vila-seca, el punt queda a 5,8 cm de l'origen horitzontal i a 4,99 cm del vertical. Cal repetir-ho amb un segon municipi i contrastar cada parell amb la mateixa fila de la taula. Canviar l'ordre de les files no ha de moure cap punt; ordenar una sola columna pot trencar l'aparellament.

La comparació entre les dues dispersions fa evident un fet: la mateixa tècnica d'ajust pot resumir una relació laxa (a) i una relació molt estreta (b). La recta de **mínims quadrats** és la que minimitza la suma dels quadrats de les distàncies verticals entre els punts observats i els valors ajustats. El **coeficient de determinació** o R² resumeix quina part de la variació observada queda descrita per aquesta recta dins del conjunt analitzat; no mesura causalitat ni garanteix una predicció fora d'aquest conjunt. A la segona dispersió, els punts queden molt a prop de la recta i el R² del 93% s'explica, en part, perquè habitatges i persones mesuren la mateixa realitat de fons —un territori gran tendeix a tenir molts habitatges i molta gent—. Consignar l'equació i el R² és un exercici de transparència: el lector veu quin resum concret s'ofereix i pot jutjar si la recta és una descripció fidel o una simplificació.

L'acceptació d'una recta exigeix inspeccionar també la forma del núvol de punts. Una relació corba, uns pocs casos influents o un nombre reduït d'observacions poden fer inadequat l'ajust lineal encara que el programa calculi una equació i un R². En aquest capítol, tots dos descriuen només els municipis observats i s'han d'acompanyar de la dispersió visible; no són una prova causal ni una predicció per a altres territoris.

La dispersió també admet una tercera variable si un canal addicional ho permet. Quan aquesta variable és quantitativa, dimensionar els punts produeix un **gràfic de bombolles**. En l'exemple següent es mantenen als eixos el percentatge de població de 65 anys o més i el percentatge d'habitatge no principal, mentre que l'àrea de cada cercle representa la població total del municipi:

![Gràfic de bombolles dels municipis del Tarragonès: envelliment i habitatge no principal per posició, i població total per àrea]({{ site.baseurl }}/assets/img/data-visualization/project-ageing-housing-population-bubbles-tarragones-2021.svg "Cada municipi ocupa la mateixa posició que en la dispersió bivariant, però l'àrea de la bombolla és proporcional a la població total. Tarragona domina en volum sense tenir els percentatges més alts dels altres dos indicadors. Font: Idescat, 2021."){: data-figure-width-web="52rem" data-figure-width-pdf="100%"}

La mida aporta context de volum i fa visible que Tarragona, Salou i Vila-seca no tenen el mateix pes demogràfic que els municipis petits. Tanmateix, l'àrea es compara amb menys precisió que una longitud i les bombolles grans poden tapar-ne d'altres. Per això l'àrea, no el radi, ha de ser proporcional al valor, la llegenda ha d'incloure cercles de referència i una barra continua sent preferible si cal ordenar poblacions exactes.

L'exercici de mides pot prendre dos valors de referència de 1.000 i 4.000 habitants. Si el primer cercle té un diàmetre de 10 mm, el segon n'ha de tenir 20: quadruplica l'àrea quan duplica el diàmetre. Un diàmetre de 40 mm multiplicaria l'àrea per setze. Cal comprovar aquesta relació amb les àrees dels cercles i mantenir intactes les posicions dels punts, que continuen codificant els altres dos indicadors.

Quan la tercera variable és nominal, el to i la forma dels punts poden identificar una categoria sense moure cap posició. Amb dades d'observacions individuals classificades per una espècie o un tipus, aquests dos canals es poden utilitzar de manera redundant:

![Dispersió de la longitud del pètal i del sèpal per a tres espècies d'iris, amb to i forma com a canals identificadors]({{ site.baseurl }}/assets/quarto/data-visualization/iris-flower-scatter.qmd "Gràfic de dispersió amb to i forma: cada punt combina dues variables per posició i una categoria per to i forma. Els tres grups formen nuvols separats que es poden llegir per posició, però to i forma els identifiquen i els reforcen sense dependre d'un únic canal."){: data-figure-width="50rem"}

La redundància de canals (el mateix grup dibuixat amb to i amb forma) millora l'accessibilitat i evita que la lectura depengui d'un sol senyal. Els canals redundants han de ser consistents: si to i forma contradiguessin el grup, el lector hauria de desfer una confusió que el gràfic mateix ha creat.

En la dispersió d'iris, la comprovació consisteix a identificar dues flors de la mateixa espècie i relacionar el seu to i la seva forma amb la llegenda. Després es pot imaginar la figura en grisos: la forma ha de continuar identificant l'espècie. Hi ha dos camps quantitatius per a la posició i un camp categòric representat de dues maneres; tenir quatre canals visibles no implica tenir quatre variables de dades.

La lectura d'una dispersió acabada també es pot fer en sentit invers: de les marques visibles cap a la taula que les hauria de fer possibles. [*Best in Show: The Ultimate Data Dog*](https://informationisbeautiful.net/visualizations/best-in-show-whats-the-top-data-dog/) és una dispersió en què els punts s'han substituït per siluetes de races de gos. La lectura s'inicia formulant una hipòtesi sobre l'estructura de la base, que després es contrastarà amb les dades:

1. Quina és la unitat d'observació i quantes files aproximades hi hauria?
2. Quins camps calen per situar, acolorir, orientar, dimensionar i retolar cada marca?
3. Quins camps semblen observacions de partida i quin sembla un indicador derivat?
4. Si la popularitat original és un rànquing, com s'hauria de transformar o invertir perquè «més amunt» signifiqui «més popular»?

![«Best in Show: The Ultimate Data Dog», dispersió multivariable que compara la puntuació composta i la popularitat de diverses races de gos]({{ site.baseurl }}/assets/img/data-visualization/best-in-show-data-dog-information-is-beautiful-2014.png "«Best in Show: The Ultimate Data Dog», publicada el 2014. Concepte i disseny: David McCandless; recerca: Miriam Quick; il·lustracions de gossos: Andrew Park. © Information is Beautiful. Reproducció de la imatge original segons el permís gratuït per a usos educatius no comercials; aquest recurs queda exclòs de la llicència Creative Commons del manual."){: data-figure-width-web="58rem" data-figure-width-pdf="88%"}

La hipòtesi mínima és una fila per raça i camps per al nom, la popularitat, la puntuació composta, la talla, el grup i la intel·ligència. La posició horitzontal codifica la puntuació creada pels autors a partir d'intel·ligència, costos, longevitat, cures, afeccions i gana; la vertical ordena la popularitat; el to separa grups de races; la mida de la silueta indica la talla; l'orientació distingeix els dos extrems de la classificació d'intel·ligència; i el text identifica la raça. La forma pictòrica ajuda a reconèixer-la, però també ocupa més espai i produeix més solapaments que un punt geomètric.

Reconstruir aquesta correspondència no valida automàticament l'índex. Encara cal obrir les [dades publicades](https://docs.google.com/spreadsheets/d/1l_HfF5EaN-QgnLc2UYdCc7L2CVrk0p3VdGB1godOyhk/edit), comprovar les definicions, les fonts, els sentits de les escales i la manera com s'han combinat els components. La figura és útil perquè mostra que una dispersió pot incorporar molts canals, però també perquè obliga a distingir dades observades, categories, transformacions i decisions editorials.

### Comparar perfils d'edat: piràmide de població

La piràmide és una **barra divergent**. Les edats formen l'eix ordinal; homes i dones comparteixen escala i origen. Els valors masculins s'emmagatzemen temporalment amb signe negatiu per situar-los a l'esquerra, però la població no és negativa. Les etiquetes o el format de l'eix han d'evitar aquesta interpretació literal.

![Piràmide de població de Vila-seca per grups quinquennals i sexe, 2021]({{ site.baseurl }}/assets/quarto/data-visualization/population-pyramid-vila-seca.qmd "Piràmide de població: les edats simples s'agrupen en intervals de cinc anys; la longitud compara recomptes a banda i banda d'un origen comú, amb homes i dones que comparteixen escala."){: data-figure-width="50rem"}

La piràmide pot treballar amb recomptes per descriure el municipi o amb percentatges per comparar territoris de grandàries diferents. La versió utilitzada ha d'indicar-ho. Grups d'edat, sexe, any i font formen part de la definició de la figura.

La lectura parteix del zero central i compara longituds cap als dos costats dins del mateix grup d'edat. Pujar a la fila següent significa passar a una altra franja, no afegir una quantitat de persones. La taula preparada pot tenir una fila per grup d'edat i dues columnes de recomptes, homes i dones, o una fila per combinació de grup i sexe. El signe negatiu és una transformació de presentació que s'ha de distingir del recompte original.

Es pot comprovar una fila amb una població simulada de 1.000 persones en què una franja conté 60 homes i 40 dones. Sobre el total municipal, les dues barres representen el 6% i el 4% i sumen el 10%, no el 100%. Sobre el total d'aquella franja, en canvi, serien el 60% i el 40%. Cal dibuixar la fila de piràmide amb un origen i una escala comuns, conservar els recomptes positius a la taula i indicar quin denominador s'ha utilitzat.

La mateixa font censal permet afegir el **lloc de naixement** a l'anàlisi. Aquesta variable no identifica la nacionalitat actual, l'any d'arribada ni una immigració recent: una persona nascuda a l'estranger pot tenir nacionalitat espanyola i haver residit al municipi durant dècades. Per això les categories de la figura següent s'anomenen «nascuda a Espanya» i «nascuda a l'estranger». La primera agrega Catalunya i la resta de l'Estat perquè totes dues parts reconstrueixin el total de cada grup d'edat.

Quan la pregunta és quina proporció representa la població nascuda a l'estranger, apilar aquesta variable dins d'una piràmide de longituds diferents dificultaria la comparació. Les barres al 100% mantenen un denominador comú, situen sempre el segment d'interès al mateix extrem i n'escriuen el percentatge al costat del límit. Així es pot comparar la composició per edat sense confondre-la amb el nombre total de persones de cada franja.

::: subfigures a+b "Lloc de naixement per grup d'edat a Vila-seca i Salou, 2021. Font: Idescat, a partir del Cens de població i habitatges de l'INE."
![Proporció de població nascuda a Espanya i a l'estranger per grup d'edat a Vila-seca]({{ site.baseurl }}/assets/img/data-visualization/foreign-born-share-by-age-vila-seca-2021.svg "Vila-seca: proporció nascuda a Espanya i a l'estranger dins de cada grup d'edat.")
![Proporció de població nascuda a Espanya i a l'estranger per grup d'edat a Salou]({{ site.baseurl }}/assets/img/data-visualization/foreign-born-share-by-age-salou-2021.svg "Salou: proporció nascuda a Espanya i a l'estranger dins de cada grup d'edat.")
:::

La diferència entre els municipis no es limita al total: la població nascuda a l'estranger representa el 18,7% de Vila-seca i el 38,6% de Salou, però el pes canvia molt segons l'edat. A Vila-seca arriba al 31,1% entre 25 i 29 anys; a Salou supera el 50% entre 25 i 44 anys i assoleix el 59,2% entre 25 i 29. Aquest perfil descriu una composició censal, no explica per si sol les causes laborals, residencials o turístiques de la diferència.

Per comparar la forma de les dues estructures per sexe cal fer una normalització diferent. Cada barra de les piràmides següents expressa el percentatge que representa una combinació d'edat i sexe sobre tota la població del municipi. Les dues bandes d'una piràmide sumen, per tant, el 100% municipal, i l'escala simètrica comuna de 0 a 6% permet comparar longituds entre panells. La taula conjunta disponible agrupa totes les edats de 85 anys o més en una sola categoria, que s'ha de mantenir igual als dos municipis.

::: subfigures a+b "Piràmides percentuals de Vila-seca i Salou per grup d'edat i sexe, 2021. Font: Idescat, a partir del Cens de població i habitatges de l'INE."
![Piràmide percentual de Vila-seca, amb els homes a l'esquerra i les dones a la dreta]({{ site.baseurl }}/assets/img/data-visualization/population-pyramid-vila-seca-percent-2021.svg "Vila-seca: percentatge de la població municipal per grup quinquennal i sexe.")
![Piràmide percentual de Salou, amb els homes a l'esquerra i les dones a la dreta]({{ site.baseurl }}/assets/img/data-visualization/population-pyramid-salou-percent-2021.svg "Salou: percentatge de la població municipal per grup quinquennal i sexe.")
:::

La normalització elimina la diferència de volum entre 22.781 habitants a Vila-seca i 28.314 a Salou, però no elimina les diferències de forma. Salou presenta més pes relatiu entre 20 i 59 anys, mentre que a Vila-seca destaquen especialment els grups de 35 a 49 anys. Aquesta lectura complementa les barres d'origen: una figura compara l'estructura relativa per edat i sexe; l'altra compara la composició per lloc de naixement dins de cada edat.

Les famílies d'aquesta secció permeten comparar quantitats, composicions, evolucions, distribucions, relacions i perfils, però, en organitzar les observacions per valors o categories, no conserven necessàriament la posició, el veïnatge, la litoralitat o les agrupacions espacials. Quan aquestes relacions formen part de la pregunta, cal un mapa: no és una versió més avançada del gràfic, sinó una representació amb una tasca diferent. Les barres ordenades continuen responent millor al rànquing; la coropleta del capítol 8 mostrarà on apareixen els valors i com es distribueixen territorialment. La mateixa variable pot necessitar totes dues peces perquè resolen preguntes complementàries.

### Exercici: reconstruir la taula que permet dibuixar un gràfic {#reconstruir-taula-grafic}

L'exercici parteix d'una figura ja acabada. Cal proposar quines dades i decisions la fan possible abans de consultar-ne la font o obrir l'assistent de gràfics. No es tracta de copiar-ne l'aspecte, sinó de justificar una correspondència que una altra persona podria reconstruir al full de càlcul.

1. Identificar què representa una marca i quina seria la unitat de cada fila de la taula.
2. Relacionar cada canal que varia —posició, longitud, àrea, to o forma— amb un camp. Distingir els canals que codifiquen dades dels que només destaquen un cas o organitzen l'espai.
3. Explicar els eixos, inclosos els implícits: categories o magnituds, unitats, sentit, origen, rang i normalització. Llegir dues marques i formular una comparació amb unitats.
4. Dibuixar les capçaleres d'una taula possible i completar dues o tres files amb valors consultats a la font. Si només es poden estimar de la imatge, cal marcar-los com a aproximats i deixar explícits els camps desconeguts.
5. Indicar quins càlculs o agrupacions falten entre la taula de partida i la figura: percentatges, sumes, recomptes per interval, ordenació o canvi de signe. Contrastar la proposta amb les dades publicades.
6. Fer un esbós amb una escala declarada i comprovar-ne almenys una correspondència: longitud, posició, angle, àrea, gruix, freqüència o connexió segons la família. Justificar per què aquest control és pertinent i què no permet comprovar.

Per començar es poden comparar les barres municipals, la dispersió i l'histograma d'habitatge. Les barres i la dispersió conserven municipis identificables, però l'histograma els agrupa i en perd els noms. Les barres agrupades, apilades i al 100% permeten una segona prova: es parteix dels mateixos recomptes, es canvia la disposició o el denominador i s'explica com canvia la pregunta.

::: table "Taules possibles i transformacions que cal explicar"
| Exemple | Una fila de la taula de partida | Camps necessaris | Operació per obtenir la figura |
| --- | --- | --- | --- |
| Barres municipals | Municipi i any | Codi, nom, no principals i total d'habitatges | Calcular el percentatge i ordenar files completes |
| Anell comarcal | Municipi i any | Habitatges principals i no principals | Sumar cada tipus i calcular-ne el pes sobre el total comarcal |
| Línia de població | Any d'un mateix municipi | Any i població | Ordenar cronològicament i conservar absències |
| Histograma | Municipi | Codi i percentatge | Definir intervals i comptar municipis, una sola vegada cadascun |
| Dispersió amb bombolles | Municipi i any | Dos indicadors i població total | Aparellar per codi; assignar posició als indicadors i àrea al volum |
| Piràmide | Grup d'edat i sexe d'un territori i any | Grup, sexe i recompte | Agrupar edats i preparar les dues bandes sobre la mateixa escala |
:::

La proposta és coherent quan permet explicar cada marca, cada categoria de la llegenda i cada unitat dels eixos. No sempre és possible recuperar les dades originals: una composició percentual pot ocultar el volum, un histograma agrupa valors i una caixa en resumeix la distribució. Assenyalar què falta és una resposta més precisa que inventar una taula aparentment exacta. La mateixa pauta es pot aplicar als exemples de l'ampliació següent.

Per a cada família es pot conservar una fitxa breu amb l'esbós, la correspondència entre camps i canals, la taula necessària i el control efectuat. Els exercicis de comprensió poden fer-se al paper o amb el full de càlcul; no impliquen dominar totes les eines de les galeries ni incorporar tots els tipus de gràfic a la infografia final.

## Ampliació: altres estructures visuals

Els repertoris externs, com el [Financial Times Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary), [From Data to Viz](https://www.data-to-viz.com/) o les galeries de [R](https://r-graph-gallery.com/) i [Python](https://python-graph-gallery.com/), són útils per generar alternatives, no per copiar formes. La [galeria de RAWGraphs](https://www.rawgraphs.io/gallery) amplia aquest repertori amb estructures que es poden construir a partir de dades tabulars i exportar com a SVG, mentre que [Tableau Public](https://public.tableau.com/app/discover) permet explorar visualitzacions i quadres de comandament interactius publicats per la seva comunitat.

Aquests recursos mostren possibilitats que van més enllà dels gràfics disponibles a Calc o Excel, però no formen part del programari que cal dominar en el curs. Les galeries d'R i Python tampoc no pressuposen que calgui programar: serveixen per reconèixer alternatives i entendre què podria aportar un flux reproduïble basat en codi. En tots els casos, la pregunta, l'estructura de les dades i la tasca de lectura han de precedir l'eina; si s'utilitza una plataforma de publicació, també cal revisar què es fa públic i sota quines condicions.

Els gràfics de pendents, els gràfics d'intensitat de colors, els diagrames de rectangles, els diagrames de Sankey, els núvols de paraules, els climogrames, els radars i les xarxes només s'utilitzaran quan la pregunta i l'estructura de les dades ho exigeixin.

::: table "Repertori opcional"
| Estructura | Pregunta adequada | Risc principal |
| --- | --- | --- |
| Gràfic de pendents | Com canvien els valors i l'ordre entre dos moments? | Confondre canvi absolut, canvi relatiu i posició al rànquing |
| Gràfic d'intensitat de colors | On apareix un patró en una matriu ordenada? | Fer dependre valors exactes només del color |
| Diagrama de rectangles | Com es reparteixen poques parts dins d'un total, amb jerarquia opcional? | Comparació imprecisa d'àrees |
| Diagrama de Sankey o al·luvial | Com circula un volum entre estats? | Dibuixar flux sense quantitat coherent |
| Núvol de paraules | Quins termes apareixen amb més freqüència en un corpus? | Fer interpretar la posició o comparar mides amb una precisió que no tenen |
| Climograma ombrotèrmic | Quin ritme mensual tenen temperatura i precipitació i quins mesos compleixen un criteri de sequedat? | Ajustar arbitràriament els dos eixos o ometre la regla que els relaciona |
| Radar | Com es comparen pocs perfils sobre una escala comuna? | Àrea i ordre dels eixos distorsionen la lectura |
| Xarxa | Què connecta amb què? | Perdre posició territorial o saturar arestes |
:::

Una forma opcional només s'utilitzarà si una justificació escrita identifica quina pregunta respon millor que una taula, una barra, una línia, una dispersió o un mapa, i quin camp controla cada canal visual.

### Gràfic de pendents: comparar dos moments

Un **gràfic de pendents** situa dues observacions de cada unitat en dues columnes i les uneix amb una línia. Les columnes identifiquen els moments; la posició vertical utilitza una escala comuna de la variable. La inclinació permet reconèixer augment, disminució o estabilitat, i els encreuaments poden mostrar canvis d'ordre. La taula mínima té identificador, valor inicial i valor final. Si l'eix representa posicions d'un rànquing en lloc de magnituds, cal declarar-ho: passar de tercer a primer no informa de quantes unitats ha canviat el valor.

L'exercici pot comparar tres sèries simulades: A passa de 10 a 20, B de 30 a 35 i C de 25 a 15. Cal esbossar-les sobre la mateixa escala i distingir tres preguntes: qui augmenta més en unitats, qui augmenta més en proporció i qui acaba amb el valor més alt. A augmenta 10 unitats i un 100%; B augmenta 5 unitats i aproximadament un 16,7%, però conserva el valor final més alt. Els segments només connecten dos moments observats; no documenten el recorregut intermedi.

### Matriu acolorida: localitzar valors per fila i columna

Un **gràfic d'intensitat de colors** pot representar una matriu en què cada cel·la correspon a una combinació de dues categories, com establiment i mes. La fila i la columna localitzen l'observació; el color en codifica el valor segons una llegenda comuna. Les cel·les poden tenir totes la mateixa àrea perquè la quantitat no s'hi representa per mida. Per construir-lo calen els dos identificadors i el valor de cada combinació, en una taula llarga o en una matriu equivalent.

Es pot provar amb pernoctacions simulades de dos establiments en tres mesos: A té 10, 20 i 40, i B té 20, 20 i 10. Cal acolorir les sis cel·les amb una mateixa escala de 0 a 40 i comprovar que tots els valors 20 tinguin el mateix color. Si cada fila utilitzés el seu propi màxim, el 20 de B rebria el color més intens i el d'A no. També cal substituir una cel·la per una absència i diferenciar-la del zero. La intensitat ajuda a reconèixer patrons; si es necessita una xifra exacta, convé conservar l'etiqueta o consultar la taula.

Quan la intensitat se superposa a un mapa o a una imatge, com en el seguiment de la mirada, les posicions tenen un altre referent: coordenades territorials o punts de l'estímul. Cal explicar què agrega el color —recompte, durada o densitat— i no traslladar automàticament la lectura de files i columnes categòriques a aquella superfície.

### Xarxes: representar relacions entre unitats

Una **xarxa** utilitza nodes per representar unitats i arestes per representar relacions. Pot ser dirigida, si la relació té sentit d'origen a destinació, i ponderada, si incorpora una quantitat com freqüència o cost. Necessita una taula de nodes amb identificadors i una d'arestes amb els dos extrems; els pesos i les direccions són camps addicionals. La proximitat del dibuix no representa necessàriament proximitat geogràfica, durada ni intensitat: sovint és el resultat d'organitzar els nodes perquè els enllaços es puguin veure.

Per comprovar-ne el funcionament es poden esbossar tres nodes ficticis —Estació, Museu i Platja— i dues connexions no dirigides: Estació–Museu i Estació–Platja. Cal dibuixar dues disposicions diferents i verificar que totes dues conservin tres nodes, dues arestes i les mateixes connexions. L'Estació té dues connexions directes; els altres nodes, una cadascun. Sense un camp de distància o temps no es pot concloure quin trajecte és més curt a partir de la longitud de les línies.

### Núvol de paraules: freqüència sense posició quantitativa

Un **núvol de paraules** dimensiona termes segons la freqüència o un altre pes calculat. Pot servir per explorar ràpidament quins mots dominen un corpus i per formular preguntes, però no conserva l'ordre de les frases, el context, la negació ni la relació entre termes. La posició dins del núvol només resol la composició: una paraula a prop d'una altra no és necessàriament més semblant ni hi apareix conjuntament.

L'exemple utilitza els noms públics dels 17 allotjaments convencionals de Vila-seca inclosos en la instantània local del Registre de Turisme. Els noms es passen a minúscules, se separen en unitats alfanumèriques i se n'eliminen paraules funcionals breus com `de`, `la` o `by`. El núvol conserva tots els termes resultants: els que es repeteixen apareixen en blau i negreta, i els que només apareixen una vegada, en gris. Cada aparició compta una vegada; no es pondera per places, categoria, ocupació ni valoració.

El corpus és petit i no representa tot el llenguatge de la destinació ni les preferències dels visitants. Només permet descriure el vocabulari d'aquests 17 noms registrats. La prominència de `hotel`, `portaventura` i `world` reflecteix paraules genèriques i una marca repetida en diversos establiments, no el pes territorial, econòmic o turístic de cada allotjament.

![Núvol de paraules dels noms públics de 17 allotjaments convencionals registrats a Vila-seca]({{ site.baseurl }}/assets/img/data-visualization/word-cloud-accommodation-names-vila-seca.svg "La mida tipogràfica representa el nombre d'aparicions després de normalitzar els noms i eliminar paraules funcionals breus. El blau i la negreta identifiquen termes repetits; el gris, termes que només apareixen una vegada. La posició no codifica cap variable."){: data-figure-width-web="51rem" data-figure-width-pdf="100%"}

La mateixa taula de freqüències es pot ordenar en barres. El núvol mostra el vocabulari complet, mentre que la barra concentra la consulta en els sis termes que es repeteixen: `hotel` i `portaventura` apareixen cinc vegades, `world` quatre i `gran`, `palas` i `pineda` dues. La comparació també fa visible una limitació: la majoria dels termes només apareixen una vegada i no formen un patró quantitatiu robust.

Cal distingir dues taules: la font té una fila per establiment i el seu nom; el resum té una fila per terme i el nombre d'aparicions. La mida tipogràfica i el to del núvol es deriven d'aquest recompte. No cal una columna de longitud o latitud, perquè les posicions no representen localització ni una magnitud. En les barres, el mateix recompte passa a una longitud mesurable sobre l'eix d'aparicions.

La comprovació pot comparar `hotel` i `portaventura`: tots dos apareixen cinc vegades i utilitzen la mateixa mida tipogràfica, però la paraula més llarga ocupa més espai. No es pot recuperar la freqüència aplicant una regla de tres a l'àrea de la paraula. En aquest núvol, la mida de la font es gradua entre límits llegibles i no és una escala d'àrees proporcionals. Per contrastar recomptes exactes cal reconstruir la taula terme–freqüència i comprovar-los a les barres.

![Barres ordenades dels sis termes repetits en els noms públics dels allotjaments registrats a Vila-seca]({{ site.baseurl }}/assets/img/data-visualization/word-frequency-bars-accommodation-names-vila-seca.svg "Les barres mostren els termes amb més d'una aparició i permeten consultar sobre una escala comuna els recomptes que controlen la mida del núvol."){: data-figure-width-web="43rem" data-figure-width-pdf="100%"}

### Climograma: coordinar dues sèries mensuals

Un **climograma** combina el ritme anual de la temperatura i la precipitació. Els dotze mesos comparteixen ordre i posició horitzontal, però les dues variables no comparteixen unitat: els graus Celsius descriuen temperatura i els mil·límetres, precipitació acumulada. Superposar-les amb dos eixos Y només és comparable si la relació entre les escales es fixa a priori.

El **criteri de Gaussen** estableix aquesta relació: 10 °C han d'ocupar la mateixa altura que 20 mm, de manera que la temperatura es dibuixa a l'escala de precipitació com $2T$. Un mes es considera sec quan $P < 2T$. L'eix esquerre de la figura va de 0 a 100 mm i el dret de 0 a 50 °C; no s'han ajustat perquè les corbes coincideixin. Si es comparen localitats o períodes, cal conservar tant aquesta relació 2:1 com els mateixos límits verticals quan també es vulguin comparar magnituds absolutes.

![Diagrama ombrotèrmic de Vila-seca amb precipitació i temperatura superposades segons el criteri de Gaussen, 1991-2020]({{ site.baseurl }}/assets/quarto/data-visualization/climograph-vila-seca.qmd "Les barres mostren la precipitació mitjana mensual en mil·límetres i la línia, la temperatura mitjana mensual sobre un eix secundari fixat a la meitat de l'escala principal. El fons destaca juny, juliol i agost, quan P és inferior a 2T. Font: Servei Meteorològic de Catalunya, Atles Climàtic de mitjanes per municipi 1991-2020."){: data-figure-width-web="43rem" data-figure-width-pdf="100%"}

La regla identifica juny, juliol i agost com a mesos secs: les precipitacions respectives de 23,5, 14,3 i 40,2 mm queden per sota de $2T$, que equival a 46,0, 50,8 i 51,4 mm. La precipitació arriba a 78,4 mm tant al setembre com a l'octubre i la suma anual publicada és de 531,2 mm; la temperatura mitjana passa dels 10,3 °C de gener als 25,7 °C d'agost i té una mitjana anual de 17,4 °C. La figura resumeix mitjanes climàtiques mensuals del període 1991-2020: no descriu episodis concrets ni permet afirmar que cada dia d'aquests mesos sigui sec.

La taula té dotze files i camps per al mes, la precipitació i la temperatura. Per llegir juliol, l'altura de la barra es consulta a l'eix de mil·límetres i la posició de la línia, al de graus Celsius: 14,3 mm i 25,4 °C. No es resten directament aquestes dues xifres. La columna auxiliar $2T$ permet aplicar la convenció de Gaussen i justificar el ressaltat del mes.

L'Atles Climàtic assigna aquests valors al punt del **cap de municipi de Vila-seca**. No són observacions d'una estació identificada ni una mitjana espacial de tot el terme. Aquesta precisió territorial forma part de la font i s'ha de conservar al títol, al peu o a les metadades quan la figura es reutilitzi.

L'exercici de comprovació pot reprendre juliol: calcular $2\times25,4=50,8$ i comparar aquest llindar amb els 14,3 mm de precipitació. Cal esbossar les dues marques amb les escales 0–100 mm i 0–50 °C i verificar que el mes compleixi $P<2T$. Després es pot provar un cas hipotètic amb $P=2T$: la igualtat no compleix el criteri estricte de mes sec. La relació 2:1 és una convenció del mètode, no una conversió física entre graus i mil·límetres.

### Radar: construir i comparar perfils

Un gràfic de **radar** assigna una variable a cada eix radial, situa el valor a una distància del centre i uneix els punts seguint un ordre fix. Només és comparable si tots els eixos comparteixen una escala interpretable. Quan les variables ja són percentatges amb el mateix denominador, com en l'exemple d'edats, es poden representar directament. Si combinen unitats diferents, cal definir límits substantius $L_j$ i $U_j$ per a cada variable i transformar cada valor a una escala comuna, per exemple $z_{ij} = 100(x_{ij} - L_j)/(U_j - L_j)$. Els límits, la direcció de cada indicador i els valors originals s'han de conservar; utilitzar només el mínim i el màxim de la mostra pot convertir diferències petites en extrems 0–100 i fer que el perfil canviï quan s'afegeix un territori.

La figura següent agrupa la població de 2021 en cinc franges que sumen el 100% de cada municipi. L'ordre dels eixos segueix el cicle d'edat i els tres panells mantenen una escala radial comuna de 0–40%. Separar els municipis evita que els polígons se solapin, però obliga a desplaçar la mirada entre panells; aquesta és una decisió més llegible que afegir moltes línies sobre el mateix radar {% cite generalitatGuiaVisualitzacioDades2018 %}.

![Radars dels percentatges de població en cinc grups d'edat a la Pobla de Mafumet, Vila-seca i Creixell]({{ site.baseurl }}/assets/quarto/data-visualization/radar-age-profiles-tarragones.qmd "Cada panell comparteix la mateixa escala percentual i conserva l'ordre cronològic dels grups. La forma ajuda a reconèixer el perfil general, però l'àrea del polígon no és una estadística i no s'ha d'utilitzar per estimar diferències exactes."){: data-figure-width="56rem"}

La lectura comença en un eix concret, no en l'àrea total: la Pobla de Mafumet presenta un pes relatiu més baix de la població de 65 anys o més, Creixell el més alt i Vila-seca una situació intermèdia. Després es pot seguir el contorn per veure en quines franges canvia el perfil. Les diferències exactes continuen sent més fàcils d'estimar amb barres o punts alineats, perquè el radar obliga a comparar distàncies amb orientacions diferents.

Per reconstruir-lo caldria una fila per municipi i una columna percentual per cadascun dels cinc grups d'edat, amb el denominador documentat. L'angle identifica el grup; la distància al centre en mesura el percentatge. Moure un eix radial a una altra posició canvia la forma del polígon sense canviar cap cel·la. El control és comparar el mateix grup sobre la mateixa escala als tres panells.

La forma i l'àrea tenen límits importants. Reordenar els mateixos eixos modifica el polígon sense canviar cap dada; augmentar un radi fa créixer l'àrea de manera no lineal; i una superfície gran no equival ni a una suma ni a una mitjana. Massa variables produeixen formes anguloses difícils de recordar, i massa perfils generen interseccions. Per això cal mantenir pocs eixos, començar al centre amb zero, fer visible l'escala, fixar un ordre amb significat i utilitzar el radar per reconèixer configuracions globals, no per substituir una comparació precisa.

Es pot construir un perfil simulat de cinc parts amb valors 10%, 20%, 30%, 25% i 15%. Si l'escala radial de 0–40% mesura 4 cm, els punts han de quedar a 1, 2, 3, 2,5 i 1,5 cm del centre. Els cinc eixos poden separar-se angularment per igual, però aquests angles no codifiquen els percentatges. Cal reordenar dos eixos i comprovar que canviï la forma sense canviar cap valor: la regla de tres s'aplica a cada radi, no a l'àrea del polígon complet.

### Diagrama al·luvial: seguir fluxos successius

El diagrama al·luvial il·lustra la geometria de fluxos successius sense respondre cap pregunta concreta del Tarragonès: serveix per veure com es descompon successivament un volum quan cada columna és una variable i l'ample de cada flux és proporcional al recompte.

![Diagrama al·luvial de les persones a bord del Titanic per classe, sexe i supervivència]({{ site.baseurl }}/assets/quarto/data-visualization/alluvial-titanic-survival.qmd "Diagrama al·luvial: cada columna és una variable —classe, sexe i supervivència— i l'ample de cada flux codifica el recompte de persones. Aquesta geometria permet seguir de quina combinació de classe i sexe sortia cada grup de supervivents."){: data-figure-width="50rem"}

El pas del total per classe, després per sexe i finalment per supervivència permet comprovar sense cercar dades que la majoria de les víctimes provenien de la tercera classe i de la tripulació, mentre que a les primeres classes la proporció de supervivents és més gran. Aquesta mena de gràfic seria l'apropiat si en algun moment del projecte es disposés de dades de fluxos turístics reals, com procedència, mitjà d'arribada o tipus d'allotjament.

En aquest cas, una taula agregada pot tenir una fila per combinació de classe, sexe i supervivència, amb una columna de recompte. Les tres posicions horitzontals són variables successives del dibuix, no tres dates; les bandes relacionen classificacions de les mateixes persones. Una taula amb només els totals separats de cada variable no permetria reconstruir aquestes correspondències.

Una prova curta pot partir de 100 registres simulats, classificats en dos camps: A/B i X/Y, amb 50 registres a cada categoria de cada camp. Cal construir dos repartiments conjunts possibles: un amb 50 A–X i 50 B–Y, i un altre amb 50 A–Y i 50 B–X. Els totals de cada columna són idèntics, però les bandes connecten categories diferents. La comprovació ha de conservar tant les quantitats com les correspondències; els totals separats no determinen l'al·luvial.

### Diagrama de Sankey: comprovar un balanç

Un **diagrama de Sankey** respon millor una pregunta de balanç: quina quantitat entra, per quines branques es reparteix i si aquestes branques conserven el total. En lloc de repetir el cas del Titanic, la figura següent aplica aquesta estructura a les 9.985 places dels 17 allotjaments convencionals de Vila-seca inclosos en la instantània del [Registre de Turisme de Catalunya](https://analisi.transparenciacatalunya.cat/Turisme/Establiments-d-allotjament-tur-stic-inscrits-al-Re/t2h3-cgys/about_data). El primer repartiment diferencia tipus d'establiment i el segon, categories registrals; les categories hoteleres residuals s'agrupen perquè continuïn sent llegibles.

![Diagrama de Sankey de les places d'allotjament convencional registrades a Vila-seca, des del total municipal fins al tipus d'establiment i la categoria registral]({{ site.baseurl }}/assets/quarto/data-visualization/sankey-allotjament-vilaseca.qmd "Diagrama de Sankey d'un balanç territorial: el gruix de cada flux codifica places registrades i el total de 9.985 es conserva entre el municipi, els tipus d'establiment i les categories agrupades. La figura representa capacitat administrativa, no ocupació ni mobilitat turística."){: data-figure-width="54rem"}

La branca hotelera concentra 8.611 places, el 86,2 % del total registrat, i les categories de quatre estrelles i quatre estrelles superior n'apleguen 8.145. Aquesta lectura descriu l'estructura administrativa de l'oferta: les bandes no són trajectes de persones i no permeten inferir ocupació, pernoctacions, obertura efectiva ni demanda. El control essencial del diagrama de Sankey és aritmètic: a cada columna les branques han de continuar sumant 9.985 places.

La font necessita una fila per establiment amb tipus, categoria i places. En agrupar-la, cada connexió es pot descriure amb origen, destinació i quantitat; aquest últim camp controla el gruix. La distància horitzontal entre columnes no mesura quilòmetres ni temps. Llegir una banda consisteix a seguir-ne les dues categories i comprovar el volum que connecta.

Per construir un esbós proporcional, es pot representar el total de 9.985 places amb un gruix de 20 mm al costat del node inicial. La branca hotelera de 8.611 places necessita aproximadament 17,25 mm i la resta, 2,75 mm. Cal aplicar la regla de tres al gruix, no a la longitud del recorregut, i comprovar que els fills de cada repartiment reconstrueixin la quantitat del pare. La mesura es fa als trams rectes propers als nodes, on la comparació és més clara.

### Diagrama de rectangles: repartir un total per àrea

El **diagrama de rectangles** (*treemap*) és una altra estructura opcional que encaixa quan la pregunta és «com es reparteix un total entre poques parts identificables». No requereix necessàriament diversos nivells jeràrquics, però sí un total comú i una regla d'agrupació explícita. En aquest exemple, les 9.985 places d'allotjament convencional registrades al municipi de Vila-seca es reparteixen entre els cinc establiments amb més capacitat i un grup que agrega els altres dotze. Així es pot llegir la concentració sense forçar etiquetes dins de rectangles residuals:

![Diagrama de rectangles de les places registrades als allotjaments convencionals del municipi de Vila-seca, amb els cinc establiments de més capacitat i els altres dotze agregats]({{ site.baseurl }}/assets/quarto/data-visualization/treemap-allotjament-vilaseca.qmd "Diagrama de rectangles d'una composició: l'àrea codifica places registrades, no ocupació ni pernoctacions. Els cinc establiments amb més capacitat sumen 6.616 places, el 66,3 %; els altres dotze en sumen 3.369, el 33,7 %."){: data-figure-width="54rem"}

La taula preparada té sis files: els cinc establiments i l'agregat restant, cadascun amb etiqueta i places. Cada rectangle es llegeix per la seva àrea dins del total; amplada i altura no codifiquen dues variables independents. La disposició omple l'espai i no situa els establiments sobre el territori. Per conèixer-ne la localització caldrien altres camps i una representació cartogràfica.

El diagrama de rectangles té un límit seriós: comparar magnituds per superfície és menys precís que per longitud o posició alineada. És adequat per veure de cop com es reparteix un total i per destacar quina part domina, però no és la millor opció quan cal estimar ràtios o diferències petites entre parts. Si la jerarquia té molts nivells, la llegibilitat cau de pressa. Com amb el diagrama al·luvial, només s'ha d'escollir si una justificació explicita quina pregunta concreta respon i quin camp controla cada rectangle.

La comprovació es pot fer sobre un esbós en què la zona ocupada pels rectangles mesuri 10 × 10 cm. El grup agregat dels altres dotze establiments, amb aproximadament el 33,7% de les places, ha d'ocupar uns 33,7 cm². Cal mesurar amplada per altura i sumar les àrees de les parts, excloent marges, títols i espais auxiliars. Dos rectangles amb la mateixa amplada poden representar quantitats diferents si tenen altures diferents.

## Construir jerarquia i context

Una figura no reparteix l'atenció de manera neutral. La posició, la mida, el pes tipogràfic, el contrast, l'alineació, la proximitat i l'espai en blanc indiquen per on començar i què és secundari. La dada principal ha de dominar; els eixos, quadrícules, vores i llegendes només han d'aportar l'estructura necessària per interpretar-la.

La jerarquia no consisteix a fer gran qualsevol element important. Un títol pot orientar sense competir amb les barres; una anotació pot destacar Vila-seca sense convertir la resta en soroll; i una font pot quedar en un nivell discret sense arribar a ser il·legible. Quan tots els elements tenen color intens, negreta, contorn o mida gran, la jerarquia desapareix perquè res no queda subordinat.

>>>>> La jerarquia visual permet orientar l'atenció i mantenir recuperable el context que sosté la comparació.
>>>>>
>>>>> - Construir una jerarquia entre dades, títol, etiquetes, unitats, font i elements auxiliars.
>>>>> - Utilitzar prominència, agrupació i espai per diferenciar evidència principal, context i informació auxiliar.
>>>>> - Organitzar un recorregut de lectura adequat a la tasca sense presentar-lo com una seqüència culturalment universal.
>>>>> - Retolar títols, eixos, unitats, etiquetes, anotacions, llegendes i fonts amb una prioritat coherent.

### Prominència i jerarquia visual

La **prominència visual** descriu la capacitat d'un element per captar atenció per contrast, mida, color, aïllament o posició. La **jerarquia visual** assigna aquesta força d'acord amb una funció comunicativa. Una taca vermella pot ser molt prominent i, tanmateix, destacar una dada secundària; una jerarquia correcta fa coincidir el primer nivell amb la pregunta o l'evidència principal, reserva un segon nivell per al context i manté fonts i controls en un tercer nivell llegible. La semiologia de Bertin ajuda a jutjar com les variables visuals codifiquen dades, però no constitueix per si sola una teoria completa de composició, atenció o ordre ocular {% cite bertinSemiologyGraphics2010 maceachrenHowMapsWork1995 %}.

La proximitat, l'alineació i la regió comuna també agrupen elements. Una xifra i la seva etiqueta es perceben com una unitat si comparteixen espai, mentre que una caixa o un fons comú pot separar un bloc metodològic de la conclusió. Aquest recurs no s'ha d'utilitzar per envoltar-ho tot: si cada fragment té una caixa, el nombre de fronteres creix i les relacions principals deixen de ser evidents. La regió comuna és un principi d'agrupació perceptiva, no una ordre de decorar cada element amb un contenidor {% cite palmerCommonRegion1992 %}.

![La mateixa informació resolta com una composició plana, una jerarquia coherent i una composició saturada]({{ site.baseurl }}/assets/img/data-visualization/visual-hierarchy-comparison.svg "Els tres panells conserven títol, mètrica, gràfic, anotació i font. La versió plana no estableix prioritats; la versió coherent diferencia entrada, evidència i context; la versió saturada fa competir colors, vores i negretes. Figura d'elaboració pròpia."){: data-figure-width="54rem"}

Una prova ràpida consisteix a observar la peça durant pocs segons, retirar-la i formular tres preguntes: quin era el tema, quina dada dominava i quin element aportava el límit o el context? La resposta no converteix la percepció en una mètrica universal, però ajuda a detectar si la jerarquia prevista coincideix amb la lectura real. Després cal tornar a la mida final i comprovar que el tercer nivell continua sent recuperable: subordinat no significa invisible.

### Ampliació: atenció visual i seguiment de la mirada

El **seguiment de la mirada** estima on dirigeix la mirada una persona mentre observa una figura. Una **fixació** és un interval relativament estable durant el qual la mirada es manté en una zona; un **moviment sacàdic** és el moviment ràpid que connecta dues fixacions. La durada, el nombre i l'ordre de les fixacions poden ajudar a estudiar quins elements s'han consultat i quin recorregut s'ha produït, però depenen de l'aparell, el calibratge, el mostreig, els llindars de detecció, la tasca i la persona. L'atenció també pot operar fora del punt exacte de mirada. Per això mirar una marca no demostra haver-la entès, acceptat ni recordat {% cite orquinThreatsValidityEyeMovement2018 %}.

Les dades de la mirada es poden representar de diverses maneres. Un **recorregut de la mirada** conserva una seqüència individual mitjançant cercles i connexions; un gràfic d'intensitat de colors agrega densitat o durada sobre l'estímul; i una línia temporal permet comparar quan s'ha consultat cada àrea d'interès. Cada resum respon una pregunta diferent. El gràfic d'intensitat de colors és útil per localitzar concentracions, però elimina l'ordre temporal i pot ocultar que persones diferents han seguit recorreguts oposats. Superposar totes les trajectòries, en canvi, conserva més moviment però pot generar una trama impossible de llegir {% cite blascheckVisualizationEyeTracking2017 %}.

![Fixacions i moviments sacàdics, recorregut temporal individual i gràfic d'intensitat de colors agregat aplicats al mateix estímul infogràfic]({{ site.baseurl }}/assets/img/data-visualization/eye-tracking-reading.svg "Fixacions, recorregut individual i intensitat agregada sobre un mateix estímul, amb dades simulades. Elaboració docent pròpia."){: data-figure-width="54rem"}

En una prova de lectura del projecte, aquestes mesures només tindrien sentit si la prova parteix d'una tasca definida: trobar el municipi amb el valor més alt, explicar una tendència o identificar la limitació de l'indicador. Sense una pregunta observable, acumular fixacions no permet saber si la composició funciona. La comprovació més directa continua sent demanar a la persona què ha entès, quina evidència ha utilitzat i què no ha pogut resoldre; el seguiment de la mirada pot complementar aquesta resposta, no substituir-la.

### Ordre de lectura, cultura i seqüència

La disposició crea probabilitats de recorregut, no una ruta obligatòria. En una pàgina escrita en català, començar a la part superior i avançar d'esquerra a dreta és una expectativa raonable perquè coincideix amb l'aprenentatge de l'escriptura llatina. Altres sistemes d'escriptura entren a la pàgina des d'altres direccions, i fins i tot dins d'una mateixa cultura la tasca, el dispositiu, l'experiència i la prominència dels elements poden canviar el punt d'entrada. La recerca mostra que la direcció habitual de lectura pot modular l'atenció visuoespacial; no autoritza a convertir un recorregut esquerra-dreta en una llei universal del disseny {% cite rinaldiReadingDirectionAttention2014 %}.

![Direccions de lectura com a convencions culturals i diferència entre una agrupació ambigua i una seqüència explícita]({{ site.baseurl }}/assets/img/data-visualization/reading-directions-sequence.svg "La part superior compara expectatives apreses de direcció sense presentar-les com a universals. La part inferior mostra que la proximitat pot suggerir un ordre, però només la numeració i els connectors fan inequívoca una seqüència obligatòria. Figura d'elaboració pròpia."){: data-figure-width="54rem"}

Patrons anomenats `F`, `Z` o `V` poden servir per formular hipòtesis sobre pàgines concretes, però no garanteixen que totes les persones recorrin qualsevol gràfic o infografia d'aquella manera. Si l'ordre és només preferent, la jerarquia, l'alineació i l'espai poden suggerir-lo. Si és necessari per entendre un procés, una ruta o una comparació abans/després, cal fer-lo explícit amb números, fletxes, línies o encapçalaments. La proximitat entre dues caixes no demostra que la segona sigui conseqüència de la primera.

### Retolació de gràfics: títol, eixos, etiquetes i font

Un gràfic ha de poder-se interpretar sense reconstruir la taula original. El títol ha d'identificar la pregunta o la troballa sense afirmar més del que mostren les dades; el subtítol o una anotació poden aportar el context imprescindible. Les unitats, el període, el territori i la font han de ser visibles, i la precisió numèrica ha de correspondre a la qualitat de les dades i a la necessitat del lector. Les etiquetes directes redueixen el trajecte entre marca i llegenda quan l'espai ho permet. Aquests criteris també es poden revisar amb els [principis bàsics de visualització de dades](https://policyviz.com/2018/08/07/dataviz-cheatsheet/) i la [llista de comprovació de visualització de dades](https://web.archive.org/web/20190918015742/https://datavizchecklist.stephanieevergreen.com/assets/DataVizChecklist_Feb2018.pdf).

La **retolació** d'un gràfic inclou tots els textos que guien la lectura: títol, subtítol, eixos, unitats, etiquetes directes, anotacions, llegenda, font i notes sobre transformacions. La seva funció és reduir l'ambigüitat sense repetir la taula sencera. Un gràfic sense prou text obliga el lector a endevinar què compara; un gràfic amb massa text converteix la figura en un full de càlcul il·lustrat. La decisió correcta depèn de la pregunta, de la mida final i del públic.

La retolació de gràfics comparteix criteris amb la retolació que es treballarà a la fase de llenguatge cartogràfic. En tots dos casos cal associar cada text amb l'element corresponent, establir jerarquia, evitar col·lisions i comprovar la llegibilitat final. La diferència és que un gràfic pot reorganitzar categories o situar etiquetes directament al final d'una línia, mentre que un mapa ha de respectar la posició territorial dels elements.

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

## Llegir i revisar críticament

La revisió crítica reconstrueix la correspondència entre dades i forma com a condició per acceptar el missatge d'una figura. Primer cal comprovar què representa cada marca, amb quina unitat i quin denominador; després, si la geometria, les escales i les proporcions permeten la comparació declarada; finalment, si el títol, les absències, la font i el context sostenen la interpretació. Aquest ordre permet distingir un error de dades d'una decisió visual que exagera una diferència o en dificulta la comprovació.

### Eixos truncats, tres dimensions i soroll visual

S'analitzaran recursos que exageren diferències, dificulten la comparació o amaguen el context, inclosos els gràfics tridimensionals i l'excés de categories. La lectura crítica no consisteix només a detectar una falsedat explícita: també ha de reconèixer decisions que orienten l'atenció o fan més difícil comprovar una comparació {% cite jonesHowLieCharts2018 tufteVisualDisplay2001 wilkeFundamentalsDataVisualization2019 %}.

![El mateix gràfic circular del 25% i el 75% vist des de quatre angles; la perspectiva altera l'àrea aparent dels sectors]({{ site.baseurl }}/assets/img/data-visualization/wilke-rotated-pie-3d.png "Gràfic circular tridimensional: la tercera dimensió decorativa no representa cap dada i la perspectiva fa que un mateix sector sembli canviar de mida. Figura 26.1 de Claus O. Wilke, «Fundamentals of Data Visualization», original sense modificar, CC BY-NC-ND 4.0."){: data-figure-width="32rem"}

La tercera dimensió és especialment problemàtica quan només converteix sectors, barres o línies en objectes amb volum. La figura es projecta igualment sobre una pàgina o pantalla plana, de manera que la perspectiva deforma longituds i àrees i pot ocultar marques situades al darrere. Si una tercera variable és necessària, sovint es pot representar amb petits múltiples, posició en un segon gràfic, mida, forma o color sense perdre la possibilitat de comparar sobre un pla comú.

La prova amb els quatre circulars consisteix a calcular quins angles tindrien les parts del 25% i el 75% en una vista plana: 90° i 270°. Cal identificar què canvia en girar la representació tridimensional i què es conserva a les dades. Un transportador sobre la imatge en perspectiva no recupera directament aquells angles centrals; la comprovació s'ha de fer sobre la geometria plana o sobre les dades d'origen.

L'ús de 3D pot estar justificat quan l'objecte estudiat és realment tridimensional, com un relleu, i la forma espacial és part de la pregunta. Encara així, una vista estàtica pot amagar pendents o elements; una visualització interactiva, diverses perspectives o una alternativa amb corbes de nivell poden aportar controls de lectura. La precaució no consisteix a prohibir qualsevol 3D, sinó a exigir que la tercera dimensió comuniqui una dada necessària i no una decoració.

Una figura pot orientar la lectura sense inventar cap número. Aquest és el nucli de la lectura crítica que Jones formula per als gràfics i que Tufte i Wilke desenvolupen des de criteris de claredat, proporció i integritat visual {% cite jonesHowLieCharts2018 tufteVisualDisplay2001 wilkeFundamentalsDataVisualization2019 %}. L'error no sempre és una mentida directa; sovint és una decisió que fa molt fàcil una conclusió i molt difícil comprovar-ne els límits.

Un cas habitual és el **doble eix vertical sense una transformació definida**. Pot semblar una solució compacta quan dues sèries comparteixen període però no unitat, però també permet escollir rangs diferents fins que dues línies semblen moure's alhora. La coincidència visual pot sortir de l'escala, no d'una relació substancial entre les variables. Si l'objectiu és comparar evolucions, és més honest separar les sèries en petits múltiples, indexar-les respecte d'un any base o representar directament la diferència que es vol discutir. El diagrama de Gaussen és una excepció metodològica perquè fixa a priori $P = 2T$ per aplicar un criteri explícit; no ajusta els eixos després de veure la forma de les sèries.

::: subfigures a+b "Efecte del disseny de l'escala en dues representacions temporals de la mateixa informació. Elaboració pròpia, 15 d'agost de 2026."
![Gràfic problemàtic amb ocupació i preu mitjà dibuixats sobre dos eixos verticals que fan coincidir els pendents]({{ site.baseurl }}/assets/img/data-visualization/dual-axis-misleading.svg "Gràfic de línies amb doble eix vertical: la semblança visual depèn dels rangs escollits.")
![Versió revisada amb dos petits múltiples, unitats explícites i la mateixa seqüència temporal]({{ site.baseurl }}/assets/img/data-visualization/dual-axis-reviewed.svg "Petits múltiples: cada variable conserva la seva escala")
:::

>>>> **Una figura millorable no s'ha de maquillar al final.** Si el problema és l'escala, la geometria, el denominador o la unitat, corregir colors i tipografia no resol l'error. La revisió ha de tornar a la pregunta, a les dades i al tipus de comparació.

::: table "Errors típics en gràfics i revisió corresponent"
| Decisió problemàtica | Efecte sobre la lectura | Revisió preferent |
| --- | --- | --- |
| Barres amb eix truncat | Exagera diferències perquè la longitud deixa de ser proporcional | Fer començar les barres a zero o canviar a punts/línies si cal ampliar un rang |
| Doble eix vertical sense relació fixa | Pot fabricar paral·lelismes entre sèries amb unitats diferents | Usar petits múltiples, índex base 100 o una transformació definida a priori, com $P = 2T$ en un diagrama de Gaussen |
| 3D decoratiu | Deforma angles, àrees i posicions sense afegir cap variable | Tornar a una geometria plana o justificar una tercera dimensió real |
| Cercles escalats pel radi | Exagera les diferències d'àrea percebuda | Fer proporcional l'àrea i incloure una llegenda de mides |
| Categories sense ordre funcional | Amaga màxims, mínims o patrons de comparació | Ordenar per magnitud, cronologia, geografia o criteri analític explícit |
| Percentatges tractats com a composició | Fa sumar taxes independents que no comparteixen total | Verificar numerador, denominador i total com a condició per apilar o fer sectors |
| Títol massa concloent | Presenta com a resultat allò que només és una lectura possible | Formular el missatge amb període, unitat, territori i limitació |
| Absències convertides en zero | Desplaça marques i pot crear una classe o una barra falsa | Representar o documentar l'absència separadament |
:::

La relació d'aspecte també orienta la lectura. En una sèrie temporal, la mateixa diferència vertical pot semblar una pujada brusca o una variació suau segons l'altura i l'amplada del marc. No hi ha una proporció universalment correcta, però el criteri ha de ser defensable: conservar el rang rellevant, indicar unitats i període, i evitar que la forma del marc substitueixi l'anàlisi de la magnitud real del canvi.

![Tres gràfics de línia amb la mateixa sèrie temporal i el mateix rang numèric, però amb marcs alt, equilibrat i pla que modifiquen la sensació de pendent]({{ site.baseurl }}/assets/img/data-visualization/aspect-ratio-trend.svg "Efecte de la relació d'aspecte sobre una mateixa sèrie temporal esquemàtica, 2021-2025. Elaboració pròpia, 17 d'agost de 2026."){: data-figure-width="54rem"}

Per comprovar el doble eix cal llegir cada sèrie amb la seva unitat i reconstruir-la en un panell propi, conservant les dates. La coincidència de dues línies sobre el paper no prova que els valors siguin iguals. En la prova de relació d'aspecte es pot duplicar només l'altura del marc: creix el pendent visual, però es conserven les diferències entre valors i el temps transcorregut. L'angle d'una línia temporal no té la mateixa funció que l'angle d'un sector circular.

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
2. seleccionar als fulls `indicators_*` els municipis, el període, la variable i la unitat corresponents;
3. comprovar que no s'hi han barrejat totals comarcals, files auxiliars ni valors absents convertits en zero;
4. escollir una geometria adequada a la comparació i ordenar les categories amb un criteri explícit;
5. construir almenys una alternativa que mantingui constants les dades i la pregunta;
6. evitar dobles eixos sense una transformació definida, efectes 3D, àrees mal escalades o altres recursos que dificultin comprovar la comparació;
7. revisar el títol, els eixos, les etiquetes, la llegenda, el color i la font a la mida prevista;
8. contrastar almenys dos valors representats amb les cel·les d'origen;
9. conservar el gràfic editable al llibre i generar l'exportació vectorial a partir d'aquesta versió.

## Formats de sortida per a les figures

Una figura es pot exportar com una **imatge ràster** o com un **document vectorial**. La diferència és important perquè els gràfics produïts a Calc o Excel s'integraran i s'acabaran d'editar a [Inkscape](https://inkscape.org/), un editor lliure de gràfics vectorials que permet seleccionar i ajustar formes i textos sense convertir-los en píxels {% cite wilkeFundamentalsDataVisualization2019 %}.

::: table "Formats habituals per exportar figures"
| Família | Formats | Propietats | Ús en el curs |
| --- | --- | --- | --- |
| Ràster | PNG, JPEG, TIFF | Graella de píxels; depèn de la resolució; el text deixa de ser text editable | Previsualitzacions, captures o fotografies, no màster dels gràfics |
| Vectorial | PDF, SVG, EPS | Formes geomètriques escalables; pot conservar línies, text i colors editables | Màster de gràfics i mapes per editar i compondre |
| Mixt | PDF o SVG amb imatges incrustades | Pot combinar vectors amb elements ràster | Cal inspeccionar el contingut, no només l'extensió |
:::

JPEG és inadequat per a gràfics amb text i línies perquè introdueix artefactes de compressió. PNG manté les vores netes però continua sent ràster. PDF serà el format vectorial d'intercanvi principal perquè Excel i LibreOffice Calc el poden generar i Inkscape el pot importar. SVG també és adequat quan la versió del programa permet exportar-lo correctament.

>>>> **Una extensió `.pdf` no garanteix que tot sigui vectorial.** Una captura de pantalla inserida dins d'un PDF continua sent una imatge de píxels. La figura s'ha de revisar ampliant-la molt o obrint-la a Inkscape i comprovant que barres, línies i textos es poden seleccionar com a objectes.

La interfície varia entre versions, però el procediment general és estable:

>> **Primer contacte amb Inkscape.** Abans de revisar una figura cal distingir la pàgina dels objectes que conté, utilitzar l'eina de selecció, reconèixer si diversos elements formen un grup i bloquejar la proporció abans de redimensionar. El panell d'emplenat i traç permet comprovar color, contorn i transparència; `Desa una còpia` en SVG conserva el document editable. En aquesta fase només s'inspecciona i s'anota l'exportació: les dades, l'ordre, els eixos i la geometria es corregeixen al full de càlcul i es tornen a exportar.

1. revisar títol, eixos, unitats, llegenda, font i mida final del gràfic;
2. col·locar el gràfic en un full propi o definir una àrea d'impressió que només contingui la figura;
3. exportar o imprimir la selecció directament com a PDF, sense cap captura intermèdia;
4. obrir el PDF a Inkscape i comprovar formes, textos, tipografies i colors;
5. conservar la figura exportada i el llibre que permet regenerar-la.

Les figures són resultats intermedis i s'emmagatzemaran a `outputs/figures`. El document o infografia final que les integri s'exportarà més endavant a `dist`. Aquesta separació evita confondre una peça analítica amb el producte final de síntesi.

## Activitat: construir el conjunt de figures comarcals

Cada figura haurà de respondre una pregunta sobre les diferències entre municipis o sobre el conjunt de la comarca. No es tracta de decorar la mateixa dada de moltes maneres, sinó de comprovar què permet veure cada geometria.

>>>>> L'activitat converteix els indicadors revisats en un conjunt de gràfics editables i en dues o tres figures candidates per a la síntesi comarcal.
>>>>>
>>>>> - Construir als fulls `chart_*` gràfics vinculats als rangs controlats de `charts_data`.
>>>>> - Justificar per a cada figura la pregunta, la geometria, les marques, les variables visuals i l'ordre.
>>>>> - Interpretar comparacions i associacions com a patrons, i explicitar què no permeten concloure sobre les causes.
>>>>> - Validar marques, totals, unitats, absències, retolació i valors representats contra les cel·les d'origen.
>>>>> - Exportar exactament dues o tres figures candidates en PDF vectorial i registrar-les a `README.md`.

### Dades d'entrada, gràfics guiats i PDFs candidats

L'entrada és el mateix llibre acumulatiu, amb els camps de població per grans grups d'edat a `municipal` i els sis càlculs municipals revisats a `indicators_demography` i `indicators_housing`. `tigit-02-indicadors-territorials.xlsx` es conservarà intacte com a fita de partida i el treball es farà en una còpia nova anomenada `tigit-03-semiologia-visualitzacio.xlsx`. `charts_data` contindrà rangs vinculats mitjançant fórmules; `chart_00_audit` conservarà una versió inicial i una de revisada; i cada altre full allotjarà una figura editable.

La sèrie temporal i la piràmide necessiten dues entrades addicionals que no es poden deduir de `municipal`: població anual de Vila-seca entre 2000 i 2022, i població de 2021 per edat simple i sexe. Els fitxers originals es conservaran a `data/raw`, es registraran a `sources` amb definició, període, selecció i URL, i s'importaran als fulls `source_population_time` i `source_population_pyramid`. Les transformacions quedaran a `prepared_population_time` i `prepared_population_pyramid`, i els recomptes, absències i cobertura es documentaran a `checks`. Si aquestes fonts no s'han preparat, la línia i la piràmide es tractaran com a demostracions docents i no com a figures construïdes per l'estudiant.

El nucli que construirà tot el grup conté barres ordenades, agrupades, apilades absolutes i apilades al 100%, i, quan la pregunta ho justifiqui, dispersió. El llibre docent incorpora també anell, sèrie temporal, piràmide i histograma perquè el professorat pugui demostrar altres famílies o assignar-ne una com a ampliació. El gràfic de bombolles, el núvol de paraules i el climograma serveixen per explicar canals i estructures addicionals, però no s'exigirà exportar totes les figures ni presentar-les totes a la infografia.

La línia temporal utilitzarà la població de Vila-seca entre 2000 i 2022, amb el canvi anual i el percentatge calculats per referència a la fila anterior. La piràmide partirà d'edat simple i sexe de 2021: `pivot_population_age_sex` permetrà explorar els recomptes amb una taula dinàmica, mentre `SUMIFS`, introduïda a la preparació de les edats, sumarà els valors que compleixen diverses condicions per agrupar-los en intervals de cinc anys i situar els homes amb valors negatius i les dones amb valors positius. `COUNTIFS` aplica la mateixa lògica als recomptes: compta les files que compleixen totes les parelles de rang i criteri, i servirà per obtenir quants municipis queden en cada interval d'habitatge no principal. Python comprovarà els resultats, però les transformacions que s'expliquen a classe quedaran com a fórmules o taules dinàmiques del llibre.

### Figures guiades i alternatives opcionals

::: table "Figures que es poden construir o analitzar"
| Figura | Dades adequades | Pregunta possible | Abast |
| --- | --- | --- | --- |
| Barres simples ordenades | Percentatge d'habitatge no principal per municipi | Quins municipis presenten els valors més alts i més baixos? | Demostració guiada |
| Barres agrupades | Habitatges principals i no principals en valors absoluts | Com es compara cada tipus entre municipis sobre un origen comú? | Demostració guiada |
| Barres apilades absolutes | Habitatges principals i no principals en valors absoluts | Quin volum total té el parc i com es reparteix? | Demostració guiada |
| Barres apilades al 100% | Percentatges de població de 0–14, 15–64 i 65+ | Com varia l'estructura per edats entre municipis? | Demostració guiada |
| Dispersió | Percentatge de 65+ i percentatge d'habitatge no principal | Hi ha una associació visible entre tots dos indicadors? | Demostració guiada quan la pregunta i les dades la justifiquen |
| Bombolles | Dos indicadors municipals i població total | Com canvia la relació quan el volum de cada municipi es codifica per àrea? | Anàlisi opcional* |
| Línia temporal | Població anual de Vila-seca, 2000–2022 | Com evoluciona la població i quins canvis anuals s'hi observen? | Ampliació guiada de sèrie temporal i referències entre files |
| Piràmide de població | Edat simple i sexe de Vila-seca, 2021 | Com es distribueixen homes i dones per grups d'edat? | Ampliació guiada de barres divergents i `SUMIFS` |
| Gràfic de pendents | Mateixa variable en dos moments | Quins municipis han pujat o baixat de posició? | Anàlisi opcional* |
| Circular | Habitatges principals i no principals del total comarcal | Quina composició té el conjunt de la comarca? | Anàlisi opcional* |
| Anell | Habitatges principals i no principals del total comarcal | Quina composició té el parc i què aporta el buit central? | Ampliació guiada per comparar amb el gràfic circular |
| Histograma | Percentatge d'habitatge no principal dels 22 municipis | Com es distribueixen els municipis entre intervals percentuals? | Ampliació guiada de distribució i `COUNTIFS` |
| Diagrama de caixa | Un indicador per a tots els municipis de la comarca | Quin és el centre, la dispersió i els possibles casos extrems? | Anàlisi opcional* |
| Gràfic d'intensitat de colors | Matriu de mesos i municipis, o dies i hores | Quan es concentren els valors més alts i més baixos? | Anàlisi opcional* |
| Diagrama de rectangles | Parts d'un total, amb jerarquia opcional | Com es concentren les places entre establiments o grups? | Anàlisi opcional* |
| Diagrama al·luvial o de Sankey | Fluxos, transicions o repartiments successius | D'on venen els visitants, on van o com canvien de categoria? | Anàlisi opcional* |
| Núvol de paraules | Textos tokenitzats amb una regla i un recompte explícits | Quins termes apareixen amb més freqüència i què es perd sense context? | Anàlisi opcional* |
| Climograma de Gaussen | Temperatura i precipitació mensual | Quin ritme climàtic condiciona l'activitat turística i quins mesos compleixen $P < 2T$? | Anàlisi opcional* |
:::

\* Les files d'anàlisi opcional només es construiran quan existeixin les dades que requereixen i la pregunta les faci pertinents; si no, es podran estudiar com a exemples. El gràfic circular i el d'anell poden representar intencionadament la mateixa composició per permetre'n una comparació crítica. El diagrama de caixa resumeix la distribució municipal, però no identifica per si sol la posició geogràfica dels valors.

### Selecció de dues o tres figures candidates

La sèrie completa serveix per aprendre i comparar, mentre que el repertori restant continua sent opcional i analític. S'exportaran exactament dues o tres figures candidates que expliquin aspectes complementaris. El capítol 9 farà la selecció final de dues o tres peces visuals en total, comptant també els mapes. Per a la demostració del Tarragonès, una combinació coherent de candidates seria:

1. barres apilades al 100% per comparar l'estructura d'edats;
2. barres ordenades del percentatge d'habitatge no principal;
3. dispersió entre envelliment i habitatge no principal.

La dispersió només es construirà quan la pregunta i les dades justifiquin explorar una associació. Que no mostri una relació interpretable és un resultat que es documentarà i pot motivar que es descarti de la selecció; si l'associació no era una pregunta pertinent d'entrada, se'n justificarà la substitució o l'omissió.

Els punts de la dispersió no s'uniran amb línies: cada municipi és una observació independent i no existeix una seqüència territorial o temporal entre files consecutives. Una línia de tendència, si s'afegeix, es distingirà de la sèrie i s'interpretarà només com a resum exploratori.

### Carpeta i noms dels PDFs candidats

Cada figura candidata exportada tindrà un nom semàntic i una versió vectorial PDF. Una possible estructura és:

::: listing "Noms dels fitxers PDF de les figures candidates"
```filetree
outputs/figures/
  age-structure-tarragones-2021.pdf
  non-principal-housing-tarragones-2021.pdf
  ageing-vs-non-principal-housing-tarragones-2021.pdf
```
:::

L'any i el territori s'adaptaran a les dades reals. No s'utilitzaran noms com `grafico1.pdf` o `final.pdf`. Si una figura es revisa, s'ha de poder regenerar des del llibre de treball; no s'ha de corregir únicament el PDF i perdre la relació amb les dades.

### Validació de les figures i de l'exportació

Per acceptar una figura cal comprovar que el nombre de marques correspon als municipis o categories previstos, que les unitats coincideixen amb el diccionari del llibre i que els valors absents no han passat a ser zeros. En el gràfic apilat al 100% de l'estructura d'edats, el denominador de cada municipi serà la suma dels tres grups mostrats: població de 0–14, de 15–64 i de 65 anys o més. Si aquesta suma difereix del total de població publicat, la discrepància es conservarà i es registrarà a `checks`; no es modificarà manualment cap grup per forçar la coincidència. Les altres composicions percentuals també han de reconstruir el seu total explícit dins del marge d'arrodoniment, i les barres basades en longitud han de començar ordinàriament a zero; qualsevol excepció requeriria una altra geometria o una justificació explícita. En sèries temporals, també es revisarà si la relació d'aspecte, el rang de l'eix i les anotacions fan semblar inevitable una tendència que només s'ha observat en aquell període.

La revisió també es farà a la mida final. El text, els símbols i els traços han de continuar sent llegibles fora de la interfície del full de càlcul. La figura ha de conservar un fons opac adequat quan s'ampliï o s'insereixi en un altre document; la transparència interna dels punts pot mantenir la seva funció sobre aquest fons. Després de l'exportació, el PDF s'obrirà a Inkscape per verificar que les formes i els textos continuen sent objectes vectorials seleccionables.

### Exportar des de LibreOffice Calc o Microsoft Excel 365

El llibre conserva els gràfics vinculats a les dades, però Inkscape necessita un fitxer vectorial independent. No es copiarà el gràfic a Word per imprimir-lo: aquest pas pot canviar les fonts, alterar la mida o convertir el contingut en una imatge. La ruta preferent és exportar directament des de l'aplicació de full de càlcul.

L'evidència del procés mostrarà el diàleg de rangs o sèries del gràfic d'habitatge, amb els noms municipals i el percentatge vinculats a `charts_data`, i la configuració de pàgina o exportació de l'aplicació utilitzada, Calc o Excel 365. No caldrà duplicar la mateixa captura en totes dues eines. La comprovació posterior a Inkscape es documentarà amb un objecte vectorial i un text seleccionables.

#### LibreOffice Calc

Per obtenir un PDF controlable, convé que cada figura ocupi un full propi, com `chart_02_nonprincipal`. Primer se selecciona el marc exterior del gràfic, no un element intern; després s'ajusten la mida i l'orientació a `Format > Estil de pàgina` i es defineix l'àrea d'impressió perquè no inclogui cel·les buides. `Fitxer > Exporta com a > Exporta com a PDF` generarà el PDF del full o de la selecció indicada. Si l'opció de selecció no produeix només el gràfic, s'utilitzarà el full dedicat com a àrea d'exportació.

Calc també pot oferir `Exporta com a imatge` al menú contextual del gràfic. Si la llista de formats inclou SVG, es pot crear una còpia vectorial directa. Com que el filtre SVG i el tractament de textos poden variar entre versions, el procediment més robust per al curs serà `Calc → PDF vectorial → Inkscape → SVG`.

#### Microsoft Excel 365

En Excel 365, la via més estable és moure o copiar el gràfic a un full de gràfic propi mitjançant `Disseny de gràfic > Mou el gràfic > Full nou`. Després es pot utilitzar `Fitxer > Exporta > Crea un document PDF/XPS` o `Anomena i desa` amb format PDF. A `Opcions`, quan aparegui, s'ha de publicar el full actiu o la selecció i no tot el llibre. En macOS, els noms poden aparèixer com `Fitxer > Desa com a` o `Fitxer > Imprimeix > PDF`; la pàgina resultant sempre s'ha de sotmetre a una comprovació final.

Per obtenir SVG, Excel 365 permet habitualment seleccionar el gràfic, fer clic amb el botó dret i utilitzar `Desa com a imatge`, triant SVG. Si aquella instal·lació no ofereix SVG o el resultat altera els textos, s'exportarà primer a PDF i es desarà després com a SVG des d'Inkscape. Copiar el gràfic a PowerPoint pot servir per preparar una maqueta, però no substituirà el gràfic vinculat del llibre ni serà la ruta canònica d'exportació.

#### Comprovació a Inkscape

El PDF s'importarà a Inkscape amb la proporció bloquejada. S'ampliarà el gràfic i se seleccionaran una marca i un text: si continuen sent objectes vectorials, es podran editar sense pixelació. També es revisaran accents, substitució de fonts, etiquetes tallades, gruixos, llegenda i mida final. Les correccions que afectin dades, ordre, eixos o geometria es faran a Calc o Excel i es tornarà a exportar; Inkscape es reservarà per a color, anotació i composició.

### Evidències de la visualització comarcal

::: table "Evidències de la visualització comarcal"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/processed` | `tigit-03-semiologia-visualitzacio.xlsx` | `charts_data`, auditoria i un full editable per cada gràfic candidat |
| `data/processed` | Fonts addicionals, quan l'estudiant construeixi la sèrie temporal o la piràmide | `source_population_time` o `source_population_pyramid`, transformació `prepared_*` i registre corresponent a `sources` i `checks` |
| `data/processed` | Taules dinàmiques i fórmules | `pivot_county_control` i referències revisables; `pivot_population_age_sex`, `prepared_population_time`, `pyramid_data` o `histogram_data` només per a les ampliacions que s'hagin construït |
| `outputs/figures` | PDFs vectorials | Dos o tres PDFs candidats, un per cada pregunta considerada, amb títol, unitat, període i font |
| `data/processed` | Auditoria guiada | Una figura inicial i la seva versió revisada, conservades com a demostració del mètode |
| `README.md` | Registre de figures | Fitxer, pregunta, tipus de dada, marca, variable visual, condició de candidata i limitació principal |
| `captures` | Exportació utilitzada | Aplicació i versió, full o selecció exportada, mida de pàgina i comprovació vectorial a Inkscape |
:::

L'activitat deixarà un conjunt de gràfics revisats i exactament dues o tres figures candidates per a la mateixa infografia territorial, cadascuna associada a una pregunta i a un indicador. Per a cada figura es podrà explicar quines variables visuals utilitza, què permet veure i quins límits conserva. Després de desenvolupar el color, els components espacials, la integració SIG, el llenguatge cartogràfic i la cartografia temàtica, la fase final de síntesi seleccionarà dues o tres peces visuals en total entre aquestes figures i els mapes disponibles.
