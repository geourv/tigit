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

Representar dades significa codificar-les visualment. Aquest capítol parteix de la semiologia de Jacques Bertin, que estudia com punts, línies, àrees i variables visuals construeixen diagrames, xarxes i mapes. La connecta, amb cautela, amb la gramàtica de gràfics de Leland Wilkinson i amb la seva implementació per capes a `ggplot2`: són marcs complementaris, no llistes de regles que garanteixin per si soles una figura correcta. La pregunta, la definició de les dades i la tasca del lector continuen precedint la sintaxi gràfica {% cite bertinSemiologyGraphics2010 wilkinsonGrammarGraphics2005 wickhamGgplot2Book2026 munznerVisualizationAnalysisDesign2014 wilkeFundamentalsDataVisualization2019 %}.

El color apareixerà com un canal visual, però el seu desenvolupament sistemàtic quedarà per al capítol de teoria del color, perquè afecta gràfics, mapes, accessibilitat i infografia. La classificació cartogràfica es treballarà més endavant, un cop introduït el llenguatge propi del mapa i la integració amb QGIS.

>>>>> En acabar el capítol, cal poder seleccionar, construir, revisar i exportar figures que responguin una pregunta territorial sense deformar les dades.
>>>>>
>>>>> - Explicar com les marques i les variables visuals codifiquen dades qualitatives, ordinals i quantitatives.
>>>>> - Distingir tasques de comparació, composició, distribució, relació, evolució, flux i localització.
>>>>> - Justificar un tipus de gràfic segons la pregunta, les dades, el públic, el suport i la mida final.
>>>>> - Construir `charts_data` i fulls `chart_*` editables i vinculats als indicadors d'origen.
>>>>> - Interpretar patrons i associacions sense convertir-los en causes o previsions no demostrades.
>>>>> - Validar proporcions, escales, retolació, absències i integritat vectorial, i exportar dues o tres figures candidates en PDF.

## De l'indicador a la pregunta visual

El llibre ja conté numeradors, denominadors i indicadors revisats. Ara el problema no és calcular un percentatge, sinó decidir quina representació permet comparar-lo sense perdre el municipi, el període, la unitat o el denominador que li donen sentit. Abans d'escollir un gràfic cal identificar què representa cada fila, quina funció compleix cada camp i quina operació haurà de fer el lector.

### Unitat d'observació i estructura de la taula

Una **unitat d'observació** és l'entitat descrita per una fila. A `municipal`, cada fila representa un municipi del Tarragonès; a la sèrie temporal de Vila-seca, cada fila representa un any; a la taula d'edat i sexe, cada fila representa una combinació d'edat i sexe. La mateixa columna no pot canviar de significat entre files sense trencar la comparació.

La unitat d'observació determina què serà una marca. En les barres d'habitatge no principal, una barra representa un municipi. En la dispersió, un punt representa el mateix municipi situat segons dos indicadors. En la línia temporal, cada punt representa un any i l'ordre cronològic justifica unir-los. Aquesta distinció explica per què els punts municipals d'una dispersió no s'uneixen: l'ordre de les files no descriu cap trajectòria.

### Tipus i funcions de les variables

Una variable **nominal** distingeix categories sense ordre, com municipi, sexe, titularitat o tipus d'allotjament. Només permet afirmar igualtat o diferència; ordenar alfabèticament ajuda a localitzar un nom, però no crea una jerarquia substantiva. Una variable **ordinal** conté categories ordenades, com baix, mitjà i alt o una categoria d'allotjament expressada en estrelles, però la distància entre nivells consecutius no és necessàriament constant.

Una variable **quantitativa** expressa una magnitud. Els recomptes, com població o habitatges, són discrets; superfície, densitat, percentatge o una coordenada poden tenir decimals. El fet que un camp contingui números no el converteix automàticament en quantitatiu: el codi `431711` identifica Vila-seca, però sumar-lo o calcular-ne la mitjana no té sentit.

El temps i l'espai poden actuar com a estructures de comparació. L'any ordena observacions i permet estudiar canvi; les coordenades situen objectes; el codi municipal relaciona taules; i la geometria conserva localització i veïnatge. Per tant, abans de representar no n'hi ha prou amb preguntar si una columna és text o número: cal saber quina funció compleix dins de la pregunta.

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

Per revisar les figures del curs, adoptarem una **pauta didàctica de sis components**: dades, marques, canals visuals, escales, sistema de coordenades i guies de lectura. Aquesta enumeració és una síntesi operativa del manual, inspirada en els marcs anteriors; no és una citació literal ni la descomposició única proposada per Bertin, Wilkinson o Wickham. Serveix per no oblidar cap decisió quan es passa d'una columna del llibre a una figura.

::: table "Elements bàsics d'un gràfic i funció que tenen en la lectura"
| Element | Què aporta | Exemple del projecte |
| --- | --- | --- |
| Dades (unitat d'observació, variables) | Defineix què es compara i amb quina unitat | El municipi com a fila i el seu percentatge com a valor |
| Marca (punt, línia, barra, sector, àrea) | Representa cada observació visiblement | Una barra per municipi |
| Canal visual (posició, longitud, forma, to) | Tradueix la dada en una propietat de la marca | La longitud de la barra codifica el percentatge |
| Escala (lineal, logarítmica, ordinal, de colors) | Assigna valors a posicions, mides o colors | Eix de percentatges amb origen zero |
| Coordenades (cartesians, polars, divergents) | Ordenen les marques en el pla | Barres horitzontals ordenades de més alta a més baixa |
| Guies (títol, eixos, unitats, llegenda, font) | Expliquen com interpretar la figura | Títol que indica territori, període i unitat |
:::

En coordenades cartesianes, els dos eixos tenen noms propis. L'eix **horitzontal** és l'eix d'**abscisses** i se sol referir com a $x$; l'eix **vertical** és l'eix d'**ordenades** i se sol referir com a $y$. Cada eix és una escala que assigna una posició a un valor: a l'abscissa hi sol anar la variable que ordena les observacions (categories, anys, un percentatge) i a l'ordenada la magnitud que es compara, tot i que la decisió pot girar-se quan convé llegir etiquetes llargues. El nom de l'eix no depèn del contingut, sinó de l'orientació: en un gràfic de barres horitzontals, el percentatge continua sent el valor, però es llegeix sobre l'abscissa en lloc de sobre l'ordenada.

Les guies han de retolar l'eix amb la unitat, no repetir sencerament el títol. Si el títol ja diu «Habitatge no principal als municipis del Tarragonès (2021)», l'etiqueta de l'eix pot quedar en «Percentatge» i les marques de l'escala poden afegir el símbol `%`; tornificar el mateix enunciat al títol i a l'eix satura la lectura sense aportar informació. El títol respon a «què és aquesta figura?»; els eixos responen a «sobre quina escala vull llegir cada valor?».

L'ordre anterior tampoc és un algoritme inflexible. Normalment es comença per dades i tasca, es prova una marca i uns canals i després s'ajusten escala, coordenades i guies. La revisió pot obligar a tornar enrere: una etiqueta il·legible pot exigir barres horitzontals; una escala inadequada pot fer canviar de barres a punts; i una absència pot requerir revisar la taula abans del gràfic.

### Capes i components a `ggplot2`

La gramàtica per capes de `ggplot2` fa operativa una part d'aquest raonament. Una figura combina un conjunt de **dades**, un mapatge d'atributs a propietats estètiques amb `aes()`, una o més geometries `geom_*`, transformacions estadístiques, escales, un sistema de coordenades i, si cal, facetes. El **tema** controla elements no vinculats directament a les dades, com tipografia, fons, quadrícula o posició de la llegenda {% cite wickhamGgplot2Book2026 %}.

Separar capes ajuda a diagnosticar. Si el problema és que `x` i `y` estan intercanviats, no es resol canviant el tema. Si les barres no comencen a zero, cal revisar l'escala o la geometria. Si una categoria no és distingible, cal revisar el mapatge i l'escala de color. `ggplot2` és una implementació especialment explícita, però les mateixes preguntes es poden fer davant d'un gràfic de Calc o Excel encara que la interfície no mostri les capes amb aquests noms.

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

La codificació redundant combina dos senyals compatibles. Vila-seca pot destacar-se amb color i amb una etiqueta directa; una absència pot utilitzar gris i trama. Aquesta redundància ajuda l'accessibilitat sempre que no introdueixi un segon significat contradictori.

### Proporcionalitat, origen i superfície visible

Quan una magnitud es representa mitjançant una superfície acolorida, la superfície visible també comunica quantitat. Wilke anomena aquest criteri **principi de proporcionalitat de tinta** {% cite wilkeFundamentalsDataVisualization2019 %}. Una barra truncada pot situar correctament l'extrem sobre l'eix i, alhora, exagerar la diferència perquè la longitud visible ja no és proporcional.

::: subfigures a+b "Efecte de l'origen de l'eix sobre la proporcionalitat de les barres. Figures de Claus O. Wilke, CC BY-NC-ND 4.0."
![Gràfic de barres amb eix truncat]({{ site.baseurl }}/assets/img/data-visualization/wilke-proportional-ink-truncated-axis.png "La longitud exagera la diferència")
![Mateixes dades amb origen zero]({{ site.baseurl }}/assets/img/data-visualization/wilke-proportional-ink-zero-axis.png "L'origen zero conserva la proporcionalitat")
:::

Les barres quantitatives en escala lineal han de començar ordinàriament a zero. Un punt o una línia codifiquen principalment per posició i poden ampliar un interval justificat. Quan la mida d'un cercle representa $X$, l'àrea ha de ser proporcional; el diàmetre varia amb l'arrel quadrada:

$$
D_2 = D_1\sqrt{\frac{X_2}{X_1}}
$$

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

::: subfigures a+b "La mateixa variable com a barres (a) i com a punts sobre línies fines (b), amb el mateix ordre municipal."
![Barres ordenades del percentatge d'habitatge no principal als municipis del Tarragonès]({{ site.baseurl }}/assets/quarto/data-visualization/non-principal-housing-ordered-bars.qmd "Cada barra és un municipi; la longitud codifica un percentatge de 2021. L'ordre descendent facilita trobar els valors més alts i més baixos."){: data-figure-width="54rem"}
![Punts al final de línia del percentatge d'habitatge no principal dels municipis del Tarragonès]({{ site.baseurl }}/assets/quarto/data-visualization/non-principal-housing-dot-plot.qmd "La línia fina uneix l'origen amb el valor i el punt marca l'extrem. Amb 22 municipis, redueix la tinta de la barra sense perdre la posició ordenada del valor."){: data-figure-width="54rem"}
:::

La versió de punts sobre línia fina (dot-plot) estalvia tinta: la barra ocupa una superfície que només serveix per unir l'origen amb el valor, i aquesta unió es pot dibuixar amb una línia prima i un punt. Wilke la recomana quan la pregunta no necessita la metàfora de volum de la barra {% cite wilkeFundamentalsDataVisualization2019 %}. La línia ha de començar a l'origen coherent amb la resta del gràfic, i l'altura de traç no ha de convertir-se en una àrea que distorsioni la percepció.

La figura permet veure el rànquing, però no on és cada municipi ni quants habitatges formen el denominador. Aquestes limitacions justifiquen un mapa i una mètrica absoluta complementaris, no una sobrecàrrega del mateix gràfic.

### Comparar composicions: barres apilades i anells

Una composició només existeix quan les parts comparteixen un total. Els grups 0–14, 15–64 i 65+ reconstrueixen la població mostrada de cada municipi i es poden comparar amb barres apilades al 100%. Percentatges d'ocupació de municipis diferents no són parts del mateix total i no s'han d'apilar.

Un circular o un anell pot resumir poques parts d'un únic total, com habitatges principals i no principals del conjunt comarcal. Abans de construir-lo cal respondre «100% de què?» i mantenir visibles les categories absents o desconegudes. Per comparar molts municipis, les barres apilades són més eficients que una col·lecció de cercles.

![Anell de la composició del parc d'habitatges del Tarragonès (2021): principals i no principals]({{ site.baseurl }}/assets/quarto/data-visualization/housing-donut-tarragones.qmd "L'anell mostra la part principals i no principals d'un únic total: 169.179 habitatges del Tarragonès el 2021. El buit central no porta cap dada; les etiquetes amb percentatge i magnitud eviten dependre només de l'angle. Font: Idescat, habitatges per tipus d'habitatge, 2021."){: data-figure-width="40rem"}

![Estructura d'edats per grans grups dels municipis del Tarragonès, 2021]({{ site.baseurl }}/assets/quarto/data-visualization/age-structure-tarragones.qmd "Cada barra representa un municipi i equival al 100% de la seva població. La longitud de cada segment codifica el percentatge d'un grup d'edat i el color l'identifica; l'ordenació per pes relatiu dels 65+ facilita comparar perfils."){: data-figure-width="54rem"}

La sèrie del Tarragonès evidencia perfils molt diferents entre municipis: en uns quants el pes relatiu dels 65+ supera clarament la mitjana de la comarca, mentre que en d'altres domina la franja 15–64. Coses com aquesta expliquen que la composició sigui una de les famílies més útils quan la pregunta és comparar «com és» cada territori, no «quant val» l'indicador.

### Seguir una evolució: línies

Una línia connecta observacions perquè l'ordre temporal és part de la dada. La sèrie de població de Vila-seca utilitza una definició anual comparable del Padró entre 2000 i 2022. Cada punt és un any; la línia ajuda a seguir canvis de ritme, però no demostra quina causa els ha produït ni autoritza a extrapolar-los.

![Evolució anual de la població de Vila-seca entre 2000 i 2022]({{ site.baseurl }}/assets/quarto/data-visualization/population-vila-seca-series-line.qmd "La posició vertical codifica la població i la posició horitzontal ordena els anys. Font: Idescat, a partir del Padró continu de l'INE."){: data-figure-width="52rem"}

La relació d'aspecte, el rang vertical i la selecció d'anys poden fer semblar el mateix canvi més brusc o més suau. Cal mostrar període i unitat, revisar ruptures metodològiques i descriure el passat com a canvi observat, no com a previsió.

### Examinar una distribució: histograma i diagrama de caixa

Un histograma agrupa valors quantitatius en intervals i compta observacions. No mostra municipis individuals ni categories preexistents. Amb només 22 municipis, canviar l'amplada o l'origen dels intervals pot modificar molt la forma percebuda; per això s'han de publicar els límits i comprovar que les freqüències sumen 22.

![Histograma municipal del percentatge d'habitatge no principal al Tarragonès]({{ site.baseurl }}/assets/quarto/data-visualization/housing-histogram-tarragones.qmd "Cada barra compta municipis dins d'un interval percentual. Els intervals són una decisió analítica, no categories de la font."){: data-figure-width="50rem"}

Un diagrama de caixa resumeix mediana, quartils i possibles valors extrems. És compacte per comparar distribucions, però amaga part de la forma i la localització. Un valor extrem és una observació per revisar, no un error automàtic.

::: subfigures a+b "El diagrama de caixa pot descriure una sola distribució (a) o comparar diverses distribucions alineades en categories (b)."
![Boxplot del percentatge d'habitatge no principal dels municipis del Tarragonès (2021)]({{ site.baseurl }}/assets/quarto/data-visualization/boxplot-non-main-housing-tarragones.qmd "La caixa abasta els quartils i la línia central marca la mediana; els punts superposats mostren cada municipi. Els casos més alts se surten dels bigotis i visualitzen la cua asimètrica de la distribució."){: data-figure-width="48rem"}
![Boxplot de la longitud del sèpal per a tres espècies d'iris, on cada caixa descriu una distribució i les caixes es comparen entre si]({{ site.baseurl }}/assets/quarto/data-visualization/boxplot-species-iris.qmd "Cada caixa resumeix una espècie; comparar els centres, les dispersions i els possibles extrems permet dir ràpidament si els grups se superposen o si una espècie n'ocupa una part extrema. Dades del dataset de Fisher de 1936."){: data-figure-width="48rem"}
:::

La distribució municipal no principal és clarament asimètrica: la majoria de municipis se situen per sota del 35%, mentre que uns quants casos superen amb claredat el valor de la mediana i apareixen com a valors extrems o bé punts alts dels bigotis. La funció comparativa de la caixa es veu millor quan hi ha més d'una categoria: amb les espècies d'iris, col·locar les tres caixes sobre una mateixa escala converteix un punt de cada caixa en una pregunta de comparació (quins grups queden separats, quins se sobreposen, quin mostra més variabilitat) que una llista de resums numèrics no deixa veure tan directa.

### Explorar una relació: dispersió

En una dispersió, cada punt representa una unitat amb dos valors. El codi municipal ha de garantir que `x` i `y` pertanyen al mateix municipi; emparellar per número de fila després d'ordenar una sola taula pot crear punts falsos. La posició permet llegir direcció, forma, intensitat aparent i excepcions.

::: subfigures a+b "Dues dispersions amb intensitats molt diferents: una associació aparent però dispersa (a) i una associació molt estreta i gairebé lineal (b)."
![Dispersió entre la població de 65 anys o més i l'habitatge no principal als municipis del Tarragonès]({{ site.baseurl }}/assets/quarto/data-visualization/ageing-housing-scatter-tarragones.qmd "Cada punt és un municipi identificat pel mateix codi a les dues variables. La línia d'ajust resumeix una associació aparent, però no demostra causalitat."){: data-figure-width="48rem"}
![Dispersió entre el total d'habitatges i la població total, amb l'equació d'ajust lineal i el coeficient de determinació]({{ site.baseurl }}/assets/quarto/data-visualization/housing-population-scatter-tarragones.qmd "Cada punt és un municipi. La recta és l'ajust de mínims quadrats: l'equació escrita a la figura permet llegir-hi un pendent aproximat, i el R² en percentatge quantifica com de prop queden els punts de la línia."){: data-figure-width="48rem"}
:::

Els punts municipals no s'uneixen amb línies perquè no formen una seqüència. Amb observacions superposades es pot utilitzar transparència; qualsevol desplaçament artificial s'ha de documentar. Una línia d'ajust resumeix una associació, però no converteix habitatge no principal en causa d'envelliment ni a l'inrevés.

La comparació entre les dues dispersions fa evident un fet: la mateixa tècnica d'ajust pot resumir una relació laxa (a) i una relació molt estreta (b). A la segona, els punts queden molt a prop de la recta i el R² del 93% s'explica, en part, perquè habitatges i persones mesuren la mateixa realitat de fons —un territori gran tendeix a tenir molts habitatges i molta gent—; per això un bon ajust no implica causalitat. Consignar l'equació i el R² és un exercici de transparència: el lector veu quin resum concret s'ofereix i pot jutjar si la recta és una descripció fidel o una simplificació.

La dispersió també admet una tercera variable si un canal addicional ho permet. Amb dades d'observacions individuals classificades per una espècie o un tipus, el to i la forma dels punts poden identificar la categoria sense moure cap posició:

![Dispersió de la longitud del pètal i del sèpal per a tres espècies d'iris, amb to i forma com a canals identificadors]({{ site.baseurl }}/assets/quarto/data-visualization/iris-flower-scatter.qmd "Cada punt combina dues variables per posició i una categoria per to i forma. Els tres grups formen nuvols separats que es poden llegir per posició, però to i forma els identifiquen i els reforcen sense dependre d'un únic canal."){: data-figure-width="50rem"}

La redundància de canals (el mateix grup dibuixat amb to i amb forma) millora l'accessibilitat i evita que la lectura depengui d'un sol senyal. Els canals redundants han de ser consistents: si to i forma contradiguessin el grup, el lector hauria de desfer una confusió que el gràfic mateix ha creat.

### Comparar perfils d'edat: piràmide de població

La piràmide és una barra divergent. Les edats formen l'eix ordinal; homes i dones comparteixen escala i origen. Els valors masculins s'emmagatzemen temporalment amb signe negatiu per situar-los a l'esquerra, però la població no és negativa. Les etiquetes o el format de l'eix han d'evitar aquesta interpretació literal.

![Piràmide de població de Vila-seca per grups quinquennals i sexe, 2021]({{ site.baseurl }}/assets/quarto/data-visualization/population-pyramid-vila-seca.qmd "Les edats simples s'agrupen en intervals de cinc anys; la longitud compara recomptes a banda i banda d'un origen comú, amb homes i dones que comparteixen escala."){: data-figure-width="50rem"}

La piràmide pot treballar amb recomptes per descriure el municipi o amb percentatges per comparar territoris de grandàries diferents. La versió utilitzada ha d'indicar-ho. Grups d'edat, sexe, any i font formen part de la definició de la figura.

### Conservar la localització: transició cap al mapa

Un mapa és necessari quan interessa la posició, el veïnatge, la litoralitat o una agrupació espacial. No és una versió més avançada del gràfic. Les barres ordenades responen millor al rànquing; la coropleta del capítol 8 respondrà on apareixen els valors i com es distribueixen territorialment. La mateixa variable pot necessitar les dues peces perquè resolen preguntes diferents.

## Ampliació: altres estructures visuals

Els repertoris externs, com el [Financial Times Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary), [From Data to Viz](https://www.data-to-viz.com/) o les galeries de [R](https://r-graph-gallery.com/) i [Python](https://python-graph-gallery.com/), són útils per generar alternatives, no per copiar formes. Slopegraphs, mapes de calor, treemaps, Sankey, climogrames, radars i xarxes només s'utilitzaran quan la pregunta i l'estructura de les dades ho exigeixin.

::: table "Repertori opcional"
| Estructura | Pregunta adequada | Risc principal |
| --- | --- | --- |
| Slopegraph | Com canvia el rànquing entre dos moments? | Encreuaments amb massa categories |
| Mapa de calor | On apareix un patró en una matriu ordenada? | Fer dependre valors exactes només del color |
| Treemap | Com es reparteix una jerarquia dins d'un total? | Comparació imprecisa d'àrees |
| Sankey o alluvial | Com circula un volum entre estats? | Dibuixar flux sense quantitat coherent |
| Climograma | Quin ritme mensual tenen temperatura i precipitació? | Confondre dues unitats o una coincidència visual |
| Radar | Com es comparen pocs perfils sobre una escala comuna? | Àrea i ordre dels eixos distorsionen la lectura |
| Xarxa | Què connecta amb què? | Perdre posició territorial o saturar arestes |
:::

Abans d'utilitzar una forma opcional cal escriure quina pregunta respon millor que una taula, una barra, una línia, una dispersió o un mapa, i indicar quin camp controla cada canal visual.

L'alluvial il·lustra la geometria de fluxos successius sense respondre cap pregunta concreta del Tarragonès: serveix per veure com es descompon successivament un volum quan cada columna és una variable i l'ample de cada flux és proporcional al recompte.

![Alluvial del passatge del Titanic per classe, sexe i supervivència]({{ site.baseurl }}/assets/quarto/data-visualization/alluvial-titanic-survival.qmd "Cada columna és una variable: classe, sexe i supervivència. L'ample de cada flux codifica el recompte de persones i permet seguir de quina combinació de classe i sexe sortia cada grup de supervivents."){: data-figure-width="50rem"}

El pas del total per classe, després per sexe i finalment per supervivència permet comprovar sense cercar dades que la majoria de les víctimes provenien de la tercera classe i de la tripulació, mentre que a les primeres classes la proporció de supervivents és més gran. Aquesta mena de gràfic seria l'apropiat si en algun moment del projecte es disposés de dades de fluxos turístics reals, com procedència, mitjà d'arribada o tipus d'allotjament.

Una variant visualment semblant és el **Sankey**. La diferència aproximada és que l'alluvial manté les barreres verticals (els estrats) com a columnes que conserven l'ordre de cada variable, mentre que en un Sankey els fluxos se solen disposar de manera que es puguin seguir com a bandes corbes entre nodes. El mateix conjunt de dades permet veure com canvia la lectura d'un estil a l'altre, sense que cap dels dos sigui automàticament superior:

![Diagrama de flux de tipus Sankey del passatge del Titanic per classe, sexe i supervivència]({{ site.baseurl }}/assets/quarto/data-visualization/sankey-titanic-survival.qmd "Amb geom_flow de ggalluvial els fluxos connecten els estrats com a bandes corbes i l'ample comunica el recompte; visualment s'acosta a un Sankey. La diferència respecte de la versió alluvial és principalment de disposició dels fluxos, no del volum de dades representades."){: data-figure-width="50rem"}

El **treemap** és una altra estructura opcional que encaixa quan la pregunta és «com es reparteix un total entre poques parts identificables». Requereix una jerarquia o, si més no, un conjunt de parts que sumin un àmbit definit. Amb les places d'allotjament convencional de la costa de Vila-seca es pot veure com hotels, càmpings, apartaments turístics i autocaravanes comparteixen el total de places; la superfície de cada rectangle és proporcional al recompte:

![Treemap de les places d'allotjament per tipus d'establiment a Vila-seca, amb àrea proporcional als recomptes]({{ site.baseurl }}/assets/quarto/data-visualization/treemap-allotjament-vilaseca.qmd "L'àrea de cada rectangle és proporcional al total de places d'una tipologia. Els rectangles s'ordenen per ocupar el quadre d'una manera compacta; la comparació de magnituds per superfície és menys precisa que per longitud o posició, però el format compacte comunica ràpidament com es reparteix un total entre parts."){: data-figure-width="46rem"}

El treemap té un límit seriós: comparar magnituds per superfície és menys precís que per longitud o posició alineada. És adequat per veure de cop com es reparteix un total i per destacar quina part domina, però no és la millor opció quan cal estimar ràtios o diferències petites entre parts. Si la jerarquia té molts nivells, la llegibilitat cau de pressa. Com amb l'alluvial, abans de decidir-ne l'ús cal escriure quina pregunta concreta respon i quin camp controla cada rectangle.

## Construir jerarquia i context

Una figura no reparteix l'atenció de manera neutral. La posició, la mida, el pes tipogràfic, el contrast, l'alineació, la proximitat i l'espai en blanc indiquen per on començar i què és secundari. La dada principal ha de dominar; els eixos, quadrícules, vores i llegendes només han d'aportar l'estructura necessària per interpretar-la.

La jerarquia no consisteix a fer gran qualsevol element important. Un títol pot orientar sense competir amb les barres; una anotació pot destacar Vila-seca sense convertir la resta en soroll; i una font pot quedar en un nivell discret sense arribar a ser il·legible. Quan tots els elements tenen color intens, negreta, contorn o mida gran, la jerarquia desapareix perquè res no queda subordinat.

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

## Llegir i revisar críticament

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
2. seleccionar als fulls `indicators_*` els municipis, el període, la variable i la unitat corresponents;
3. comprovar que no s'hi han barrejat totals comarcals, files auxiliars ni valors absents convertits en zero;
4. escollir una geometria adequada a la comparació i ordenar les categories amb un criteri explícit;
5. construir almenys una alternativa que mantingui constants les dades i la pregunta;
6. evitar dobles eixos, efectes 3D, àrees mal escalades o altres recursos que dificultin comprovar la comparació;
7. revisar el títol, els eixos, les etiquetes, la llegenda, el color i la font a la mida prevista;
8. contrastar almenys dos valors representats amb les cel·les d'origen;
9. conservar el gràfic editable al llibre abans de generar-ne l'exportació vectorial.

## Formats de sortida per a les figures

Una figura es pot exportar com una imatge ràster o com un document vectorial. La diferència és important perquè els gràfics produïts a Calc o Excel s'integraran i s'acabaran d'editar a Inkscape {% cite wilkeFundamentalsDataVisualization2019 %}.

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

L'entrada és el mateix llibre acumulatiu, amb els camps de població per grans grups d'edat a `municipal` i els sis càlculs municipals revisats a `indicators_demography` i `indicators_housing`. Abans de començar es conservarà `tigit-02-indicadors-territorials.xlsx` i es crearà `tigit-03-semiologia-visualitzacio.xlsx`. `charts_data` contindrà rangs vinculats mitjançant fórmules; `chart_00_audit` conservarà una versió inicial i una de revisada; i cada altre full allotjarà una figura editable.

El nucli que construirà tot el grup conté barres ordenades, barres apilades al 100% i, quan la pregunta ho justifiqui, dispersió. El llibre docent incorpora també anell, sèrie temporal, piràmide i histograma perquè el professorat pugui demostrar altres famílies o assignar-ne una com a ampliació. No s'exigirà exportar totes les figures ni presentar-les totes a la infografia.

La línia temporal utilitzarà la població de Vila-seca entre 2000 i 2022, amb el canvi anual i el percentatge calculats per referència a la fila anterior. La piràmide partirà d'edat simple i sexe de 2021: `pivot_population_age_sex` permetrà explorar els recomptes amb una taula dinàmica, mentre `SUMIFS` els agruparà en intervals de cinc anys i situarà els homes amb valors negatius i les dones amb valors positius. L'histograma utilitzarà `COUNTIFS` per comptar quants municipis queden en cada interval d'habitatge no principal. Python comprovarà els resultats, però les transformacions que s'expliquen a classe quedaran com a fórmules o taules dinàmiques del llibre.

Cada figura haurà de respondre una pregunta sobre les diferències entre municipis o sobre el conjunt de la comarca. No es tracta de decorar la mateixa dada de moltes maneres, sinó de comprovar què permet veure cada geometria.

>>>>> L'activitat converteix els indicadors revisats en un conjunt de gràfics editables i en dues o tres figures candidates per a la síntesi comarcal.
>>>>>
>>>>> - Construir als fulls `chart_*` gràfics vinculats als rangs controlats de `charts_data`.
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
| Línia temporal | Població anual de Vila-seca, 2000–2022 | Com evoluciona la població i quins canvis anuals s'hi observen? | Ampliació guiada de sèrie temporal i referències entre files |
| Piràmide de població | Edat simple i sexe de Vila-seca, 2021 | Com es distribueixen homes i dones per grups d'edat? | Ampliació guiada de barres divergents i `SUMIFS` |
| Slopegraph | Mateixa variable en dos moments | Quins municipis han pujat o baixat de posició? | Anàlisi opcional* |
| Circular | Habitatges principals i no principals del total comarcal | Quina composició té el conjunt de la comarca? | Anàlisi opcional* |
| Anell | Habitatges principals i no principals del total comarcal | Quina composició té el parc i què aporta el buit central? | Ampliació guiada per comparar amb el gràfic circular |
| Histograma | Percentatge d'habitatge no principal dels 22 municipis | Com es distribueixen els municipis entre intervals percentuals? | Ampliació guiada de distribució i `COUNTIFS` |
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

Els punts de la dispersió no s'uniran amb línies: cada municipi és una observació independent i no existeix una seqüència territorial o temporal entre files consecutives. Una línia de tendència, si s'afegeix, es distingirà de la sèrie i s'interpretarà només com a resum exploratori.

### Carpeta i noms dels PDFs candidats

Cada figura candidata exportada tindrà un nom semàntic i una versió vectorial PDF. Una possible estructura és:

```text
outputs/figures/
  age-structure-tarragones-2021.pdf
  non-principal-housing-tarragones-2021.pdf
  ageing-vs-non-principal-housing-tarragones-2021.pdf
```

L'any i el territori s'adaptaran a les dades reals. No s'utilitzaran noms com `grafico1.pdf` o `final.pdf`. Si una figura es revisa, s'ha de poder regenerar des del llibre de treball; no s'ha de corregir únicament el PDF i perdre la relació amb les dades.

### Control de qualitat abans d'exportar

Abans d'acceptar una figura cal comprovar que el nombre de marques correspon als municipis o categories previstos, que les unitats coincideixen amb el diccionari del llibre i que els valors absents no han passat a ser zeros. En el gràfic apilat al 100% de l'estructura d'edats, el denominador de cada municipi serà la suma dels tres grups mostrats: població de 0–14, de 15–64 i de 65 anys o més. Si aquesta suma difereix del total de població publicat, la discrepància es conservarà i es registrarà a `checks`; no es modificarà manualment cap grup per forçar la coincidència. Les altres composicions percentuals també han de reconstruir el seu total explícit dins del marge d'arrodoniment, i les barres basades en longitud han de començar ordinàriament a zero; qualsevol excepció requeriria una altra geometria o una justificació explícita. En sèries temporals, també es revisarà si la relació d'aspecte, el rang de l'eix i les anotacions fan semblar inevitable una tendència que només s'ha observat en aquell període.

La revisió també es farà a la mida final. El text, els símbols i els traços han de continuar sent llegibles fora de la interfície del full de càlcul. Després de l'exportació, el PDF s'obrirà a Inkscape per verificar que les formes i els textos continuen sent objectes vectorials seleccionables.

### Exportar des de LibreOffice Calc o Microsoft Excel 365

El llibre conserva els gràfics vinculats a les dades, però Inkscape necessita un fitxer vectorial independent. No es copiarà el gràfic a Word per imprimir-lo: aquest pas pot canviar les fonts, alterar la mida o convertir el contingut en una imatge. La ruta preferent és exportar directament des de l'aplicació de full de càlcul.

#### LibreOffice Calc

Per obtenir un PDF controlable, convé que cada figura ocupi un full propi, com `chart_02_nonprincipal`. Primer se selecciona el marc exterior del gràfic, no un element intern; després s'ajusten la mida i l'orientació a `Format > Estil de pàgina` i es defineix l'àrea d'impressió perquè no inclogui cel·les buides. `Fitxer > Exporta com a > Exporta com a PDF` generarà el PDF del full o de la selecció indicada. Si l'opció de selecció no produeix només el gràfic, s'utilitzarà el full dedicat com a àrea d'exportació.

Calc també pot oferir `Exporta com a imatge` al menú contextual del gràfic. Si la llista de formats inclou SVG, es pot crear una còpia vectorial directa. Com que el filtre SVG i el tractament de textos poden variar entre versions, el procediment més robust per al curs serà `Calc → PDF vectorial → Inkscape → SVG`.

#### Microsoft Excel 365

En Excel 365, la via més estable és moure o copiar el gràfic a un full de gràfic propi mitjançant `Disseny de gràfic > Mou el gràfic > Full nou`. Després es pot utilitzar `Fitxer > Exporta > Crea un document PDF/XPS` o `Anomena i desa` amb format PDF. A `Opcions`, quan aparegui, s'ha de publicar el full actiu o la selecció i no tot el llibre. En macOS, els noms poden aparèixer com `Fitxer > Desa com a` o `Fitxer > Imprimeix > PDF`; cal comprovar sempre la pàgina resultant abans de donar-la per bona.

Per obtenir SVG, Excel 365 permet habitualment seleccionar el gràfic, fer clic amb el botó dret i utilitzar `Desa com a imatge`, triant SVG. Si aquella instal·lació no ofereix SVG o el resultat altera els textos, s'exportarà primer a PDF i es desarà després com a SVG des d'Inkscape. Copiar el gràfic a PowerPoint pot servir per preparar un mockup, però no substituirà el gràfic vinculat del llibre ni serà la ruta canònica d'exportació.

#### Comprovació a Inkscape

El PDF s'importarà a Inkscape amb la proporció bloquejada. S'ampliarà el gràfic i se seleccionaran una marca i un text: si continuen sent objectes vectorials, es podran editar sense pixelació. També es revisaran accents, substitució de fonts, etiquetes tallades, gruixos, llegenda i mida final. Les correccions que afectin dades, ordre, eixos o geometria es faran a Calc o Excel i es tornarà a exportar; Inkscape es reservarà per a color, anotació i composició.

La captura d'interfície necessària mostrarà el diàleg de rangs o sèries del gràfic d'habitatge, amb els noms municipals i el percentatge vinculats a `charts_data`. Una segona captura mostrarà la configuració de pàgina o exportació de l'aplicació utilitzada, Calc o Excel 365, sense exigir duplicar la mateixa evidència en totes dues. La comprovació a Inkscape es documentarà amb un objecte vectorial i un text seleccionables.

### Evidències de la visualització comarcal

::: table "Evidències de la visualització comarcal"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/processed` | `tigit-03-semiologia-visualitzacio.xlsx` | `charts_data`, auditoria i un full editable per cada gràfic candidat |
| `data/processed` | Taules dinàmiques i fórmules | `pivot_county_control`, `pivot_population_age_sex`, `prepared_population_time`, `pyramid_data`, `histogram_data` i referències revisables |
| `outputs/figures` | PDFs vectorials | Dos o tres PDFs candidats, un per cada pregunta considerada, amb títol, unitat, període i font |
| `data/processed` | Auditoria guiada | Una figura inicial i la seva versió revisada, conservades com a demostració del mètode |
| `README.md` | Registre de figures | Fitxer, pregunta, tipus de dada, marca, variable visual, condició de candidata i limitació principal |
| `captures` | Exportació utilitzada | Aplicació i versió, full o selecció exportada, mida de pàgina i comprovació vectorial a Inkscape |
:::

L'activitat deixarà un conjunt de gràfics revisats i exactament dues o tres figures candidates per a la mateixa miniinfografia comarcal, cadascuna associada a una pregunta i a un indicador. Per a cada figura es podrà explicar quines variables visuals utilitza, què permet veure i quins límits conserva. Després de desenvolupar el color, els components espacials, el llenguatge cartogràfic, el SIG i la cartografia temàtica, el capítol 9 seleccionarà dues o tres peces visuals finals en total entre aquestes figures i els mapes disponibles.
