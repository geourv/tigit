---
layout: manual-chapter
title: Cartografia temàtica
description: Mètodes de representació temàtica, normalització, coropletes, símbols proporcionals, cartogrames, classificació i mapa municipal amb QGIS.
lang: ca
ref: manual-thematic-cartography
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/cartografia-tematica/
weight: 90
part: Continguts
manual_references: true
---

La cartografia temàtica converteix una variable en una lectura espacial. A diferència d'un mapa de referència, que prioritza localitzar elements, un mapa temàtic vol mostrar com es distribueix un fenomen, com varia entre territoris o quines connexions presenta. La decisió central no és quin color agrada més, sinó quin mètode cartogràfic correspon al tipus de dada, a la pregunta i a l'escala de lectura.

Aquest capítol aplica els principis de semiologia gràfica, llenguatge cartogràfic i color als mapes municipals del projecte. La seqüència és deliberada: primer es decideix què es mesura i quin mètode ho pot representar; després es normalitza quan cal; a continuació es classifica la distribució; finalment s'aplica una paleta coherent i es comprova la composició. Les referències de Brewer, Slocum, Wilke i Monmonier ajuden a entendre que classificar i simbolitzar també són decisions interpretatives {% cite brewerDesigningBetterMaps2005 slocumThematicCartography2009 wilkeFundamentalsDataVisualization2019 monmonierHowLieMaps2018 %}.

## Escollir el mètode abans que la paleta

### El fenomen i la unitat espacial

Un mapa temàtic parteix d'una relació entre una dada i una geometria. El projecte comarcal utilitza municipis, de manera que cada registre representa una unitat administrativa amb una forma, una superfície i uns veïns. Aquesta estructura és adequada per comparar indicadors municipals, però no descriu la distribució interna del fenomen dins de cada municipi. Un valor alt en una coropleta municipal no indica que tot el terme municipal tingui aquell mateix comportament.

El mètode s'ha de decidir abans de la paleta. Un **mapa de coropletes** representa valors associats a unitats territorials mitjançant classes ordenades de color o valor, i és adequat per a percentatges, ràtios o densitats comparables. En un **mapa de símbols proporcionals**, la mida dels símbols varia amb una magnitud i pot representar quantitats absolutes. Les categories qualitatives exigeixen símbols distingibles que no suggereixin un ordre inexistent.

Altres mètodes responen a estructures diferents. Un mapa de punts assigna una quantitat constant a cada punt; un mapa de fluxos representa moviments o connexions mitjançant línies; i una isolínia uneix posicions amb el mateix valor d'un fenomen considerat continu. No tots s'aplicaran al projecte comarcal, però ajuden a entendre que la forma del fenomen precedeix la selecció de la simbologia.

![Sis esquemes de mapes temàtics: coropleta, símbols proporcionals, punts, fluxos, isolínies i cartodiagrama]({{ site.baseurl }}/assets/img/thematic-cartography/thematic-map-types.svg "El mètode cartogràfic ha de respondre al tipus de dada: intensitat, volum, presència, moviment, continuïtat o composició localitzada. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="54rem"}

### Pregunta, dada i mètode

En una coropleta, les unitats territorials extenses ocupen més superfície visual amb qualsevol indicador. El problema específic dels recomptes absoluts és diferent: combinen el fenomen amb la grandària de la població, del parc residencial o d'una altra població exposada. Per això no permeten comparar directament la intensitat municipal. La normalització no elimina l'efecte visual de la mida dels polígons, però defineix una quantitat comparable entre territoris i evita que una superfície ombrejada s'interpreti com si representés directament un recompte {% cite wilkeFundamentalsDataVisualization2019 %}.

::: table "Pregunta, dada i mètode cartogràfic"
| Dada o pregunta | Representació adequada | Precaució principal |
| --- | --- | --- |
| Quantitat absoluta per municipi | Símbols proporcionals | La magnitud s'ha de codificar amb l'àrea del símbol, no amb el radi |
| Percentatge, ràtio o densitat municipal | Coropleta | El denominador, la unitat i la comparabilitat han d'estar justificats |
| Categoria nominal | Colors o símbols qualitatius | No suggerir un ordre inexistent |
| Moviment entre llocs | Fluxos | Explicar direcció, amplada i unitat de les connexions |
| Fenomen continu | Isolínies o superfícies contínues | Justificar les observacions i la interpolació |
:::

La cartografia temàtica inclou més famílies que les que s'aplicaran al projecte comarcal. Conèixer-les evita forçar qualsevol dada dins d'una coropleta.

::: table "Famílies de mapes temàtics i criteri d'ús"
| Família | Què prioritza | Quan pot ser útil | Risc principal |
| --- | --- | --- | --- |
| Coropleta | Intensitat en unitats territorials | Percentatges, ràtios i densitats municipals | Fer servir recomptes absoluts o classes poc justificades |
| Símbols proporcionals o graduats | Magnitud localitzada | Població, places o altres quantitats absolutes | Escalar el radi en lloc de l'àrea o ocultar el fons |
| Punts | Distribució d'una quantitat constant | Fenòmens amb localització aproximada i molts casos | Suggerir una precisió espacial que no existeix |
| Fluxos o vectors | Direcció i connexió | Mobilitat, rutes, intercanvis o desplaçaments | Saturar el mapa o confondre connexió amb volum |
| Isopletes o superfícies contínues | Gradients espacials | Altitud, temperatura, pressió o interpolacions justificades | Interpolar variables que no són contínues |
| Cartodiagrama | Gràfics localitzats | Comparar composicions en pocs llocs | Barrejar massa variables i perdre llegibilitat |
| Dasimètric | Redistribució dins d'àrees plausibles | Densitats quan es disposa d'informació auxiliar | Fer veure una precisió no documentada |
| Cartograma o anamòrfic | Pes d'una magnitud en la forma del mapa | Mostrar desigualtat de població, economia o turisme | Perdre forma, distància i reconeixement territorial |
| Pictòric o turístic | Reconeixement, orientació i atracció | Comunicació pública o orientació de visitants | Substituir l'anàlisi per promoció o il·lustració |
:::

### Símbols proporcionals i àrea

Els símbols proporcionals són adequats quan interessa mostrar una quantitat absoluta associada a una localització o a una unitat territorial. La regla perceptiva és la mateixa que en els cercles dels gràfics: si el símbol és un cercle, l'àrea ha de ser proporcional al valor, no el radi. Si un valor de referència $X_1$ es representa amb un diàmetre $D_1$, el diàmetre corresponent a $X_2$ és:

$$
D_2 = D_1\sqrt{\frac{X_2}{X_1}}
$$

Quadruplicar una dada només duplica el diàmetre. Si el diàmetre creixés directament amb el valor, les diferències d'àrea quedarien exagerades. En un mapa, a més, cal comprovar que els cercles no ocultin la geometria de base, que no suggereixin una precisió espacial falsa i que la llegenda de mides permeti llegir ordres de magnitud.

## Cartogrames i mapes anamòrfics

### Canviar l'espai per mostrar pes

Un **cartograma** o mapa anamòrfic modifica la mida o la forma dels territoris per fer que la superfície representada respongui a una magnitud, com població, PIB, places turístiques o pernoctacions. En un mapa convencional, una comarca extensa ocupa molt espai encara que tingui poca població; en un cartograma poblacional, la seva mida visual disminueix i les àrees més poblades guanyen pes. Aquesta operació pot fer visible una desigualtat que el mapa territorial oculta, però el preu és perdre distàncies, formes i part del reconeixement espacial.

Hi ha diverses solucions. Un cartograma contigu intenta conservar veïnatges mentre deforma els polígons; un cartograma no contigu permet separar-los o canviar-los de mida sense mantenir totes les vores; un cartograma de cercles substitueix territoris per cercles o altres formes proporcionals. Cap d'aquestes variants és una versió més "real" del mapa: totes canvien la propietat que el lector ha d'observar.

![Comparació entre un mapa territorial convencional, un cartograma contigu esquemàtic i un cartograma de cercles en què la mida respon a una magnitud]({{ site.baseurl }}/assets/img/thematic-cartography/cartogram-anamorphic-principle.svg "Els cartogrames fan visible el pes d'una magnitud sacrificant part de la forma, la distància o la familiaritat territorial. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="54rem"}

En turisme, un cartograma podria mostrar el pes de les pernoctacions o de les places d'allotjament respecte d'una base territorial. Seria útil per comunicar concentracions fortes, però no substituiria el mapa convencional quan calgui entendre proximitat, litoralitat, accessos o continuïtats territorials. En el projecte comarcal no es demanarà construir-ne un de complet, però sí reconèixer quan una representació anamòrfica està canviant la pregunta de lectura.

## Normalitzar abans de simbolitzar

### Volum, intensitat i denominador

La classificació no corregeix un indicador inadequat. Primer s'ha de decidir què es mesura i després com s'agrupen els valors. El percentatge d'habitatge no principal ja relaciona una part amb el parc total de cada municipi; no s'ha de tornar a dividir perquè QGIS ofereixi una opció anomenada normalització.

Un nombre absolut d'habitatges no és equivalent al percentatge. Aplicar els mateixos colors als recomptes faria que els municipis amb més volum tendissin a dominar la lectura, encara que el pes relatiu fos moderat. El nom del camp, la fórmula i la unitat s'han de contrastar amb el diccionari del llibre abans de simbolitzar.

### Zero, absència i no aplicable

Els territoris sense dades necessiten un tractament diferent dels valors zero. El zero és una observació possible dins de l'escala de l'indicador; l'absència indica que no es disposa d'un valor calculable o comparable. Un tercer cas, el **no aplicable**, apareix quan la pregunta no correspon a aquella unitat. La llegenda i la simbologia han de mantenir aquestes diferències.

Convertir nuls en zero pot alterar tant la classificació com la interpretació. Si un municipi queda sense correspondència després d'una unió, no s'ha d'incorporar a la classe més baixa; primer cal diagnosticar si falta una dada, si hi ha un codi mal unit o si realment el valor és zero.

## Classificar dades quantitatives

### Examinar la distribució abans de classificar

Abans d'escollir un mètode s'han de revisar el mínim, el màxim, la mediana, els valors repetits, les absències i els casos extrems. Una llista ordenada, un histograma o el diagrama de caixa construït al capítol 3 permeten observar si la distribució és uniforme, asimètrica o dominada per pocs municipis.

La classificació agrupa valors que ja existeixen; no corregeix errors ni crea comparabilitat. Si un municipi té un valor excepcional, primer s'ha de comprovar el numerador, el denominador i la font. Si és correcte, cal decidir com afecta les classes i explicar-ho, no eliminar-lo perquè dificulta el mapa.

![Comparació entre intervals iguals, quantils i trencaments naturals sobre una mateixa distribució sintètica de valors municipals]({{ site.baseurl }}/assets/img/thematic-cartography/classification-methods.svg "Classificar és decidir quins valors es llegiran com a semblants; intervals iguals, quantils i trencaments naturals responen a criteris diferents. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="54rem"}

### Intervals iguals

Els **intervals iguals** divideixen el rang numèric en classes amb la mateixa amplitud. Si $x_{min}$ és el valor mínim, $x_{max}$ el valor màxim i $k$ el nombre de classes, l'amplada és:

$$
w = \frac{x_{max} - x_{min}}{k}
$$

Els punts de tall es poden escriure com $x_{min}+jw$ per a $j=1,2,\ldots,k-1$. Aquest mètode facilita explicar la llegenda perquè totes les classes cobreixen el mateix rang numèric, però pot generar classes buides o concentrar moltes observacions en una sola classe si la distribució és asimètrica.

### Quantils

Els **quantils** distribueixen aproximadament el mateix nombre d'observacions a cada classe. Si hi ha $n$ observacions i $k$ classes, cada classe conté al voltant de $n/k$ casos. Els punts de tall s'associen a posicions ordenades de la distribució, de manera aproximada:

$$
p_j = \frac{j}{k}\quad j=1,2,\ldots,k-1
$$

El mètode fa que totes les classes apareguin representades quan hi ha prou observacions, però les amplituds numèriques poden ser molt diferents. També pot separar valors iguals o gairebé iguals en classes diferents si la distribució conté empats o grups compactes. Per això la llegenda ha de mostrar els talls exactes i el recompte per classe s'ha de revisar.

### Trencaments naturals de Jenks

Els **trencaments naturals** busquen classes internament homogènies i separades entre elles. La formulació habitual minimitza la suma de desviacions quadràtiques dins de cada classe:

$$
\min \sum_{c=1}^{k}\sum_{i\in c}(x_i-\bar{x}_c)^2
$$

Aquest criteri s'adapta bé a distribucions amb agrupacions visibles, però els punts de tall depenen fortament del conjunt concret de dades. Si s'afegeix o s'elimina un municipi, o si canvia el període, la classificació pot variar i dificultar la comparació temporal o territorial. Jenks no és una garantia d'objectivitat; és un criteri algorítmic que cal interpretar.

### Nombre de classes i etiquetes

Cada mètode de classificació destaca unes diferències i n'oculta unes altres. Els intervals iguals faciliten comparar amplades numèriques, però poden deixar classes buides. Els quantils reparteixen observacions entre classes, però poden donar amplituds molt diferents. Jenks s'adapta a l'agrupació de la distribució concreta, però els punts de tall poden canviar quan canvien les dades.

La selecció es basarà en una lectura conjunta de la distribució, el nombre d'observacions per classe, l'amplada dels intervals i la pregunta territorial. Un cop escollida la classificació, se'n registraran els punts de tall exactes perquè el mapa es pugui reconstruir i comparar.

Les etiquetes de la llegenda no han de mostrar més decimals dels que es poden interpretar ni deixar buits o solapaments. Els límits de classe han de seguir un criteri consistent, especialment quan els indicadors poden prendre valors exactament iguals a un punt de tall. Una formulació com `10,0-19,9` i `20,0-29,9` pot ser llegible si les dades s'arrodoneixen a una decimal; una notació matemàtica com `[10, 20)` i `[20, 30]` és més precisa, però pot ser menys adequada per al públic general. La solució ha de conservar exactitud i comprensibilitat.

### Casos extrems i absència de dades

Els valors extrems poden concentrar la resta d'observacions en poques classes. Es pot revisar el nombre de classes, comparar un mètode diferent o mostrar el valor de manera explícita, però qualsevol decisió ha de conservar la dada i quedar documentada. Un extrem pot ser un error, una base petita o un resultat territorial important; només la revisió del numerador, denominador i context permet distingir-ho.

## Activitat: construir i comparar el mapa temàtic

La pràctica compararà mapes municipals del mateix indicador construïts amb classificacions i paletes diferents. La demostració representarà el **percentatge d'habitatge no principal** al Tarragonès. Cada projecte podrà mantenir aquest indicador o justificar l'ús del percentatge de població de 65 anys o més.

### Verificar l'indicador unit a la capa

Es continuarà el projecte QGIS del capítol 5. Abans de simbolitzar, es revisaran el camp seleccionat, el tipus numèric, la unitat, el mínim, el màxim, els nuls i almenys tres municipis contrastats amb el llibre. L'informe de la unió ha de demostrar que no hi ha codis duplicats o municipis sense correspondència inexplicada.

La construcció seguirà un procediment estable:

1. configurar una simbologia graduada sobre el camp numèric verificat;
2. separar els valors nuls abans de calcular les classes perquè no s'interpretin com a zero;
3. aplicar un primer mètode i registrar el nombre de classes, els punts de tall i les observacions de cada classe;
4. duplicar l'estil o la capa només per crear una alternativa controlada, sense duplicar les dades d'origen;
5. mantenir la mateixa extensió i composició mentre es comparen classificacions;
6. fixar els punts de tall seleccionats i comparar després les paletes preparades al capítol 7;
7. desar l'estil final al projecte i, si cal reutilitzar-lo, en un fitxer d'estil al costat del projecte.

### Construir alternatives controlades

La comparació mantindrà constants el territori, l'indicador i la mida del mapa. Només canviaran el mètode de classificació o la paleta. Així es podrà atribuir la diferència de lectura a una decisió concreta i no a una acumulació de canvis simultanis.

#### Comparar classificacions

La primera comparació mantindrà una mateixa paleta seqüencial i aplicarà almenys dos mètodes de classificació. Per a cada alternativa s'anotaran el nombre d'observacions per classe, els punts de tall, les classes buides i l'efecte dels valors extrems. L'objectiu no és trobar el mapa que produeix més contrast, sinó el que respon millor a la distribució i a la pregunta.

#### Comparar paletes

La segona comparació mantindrà els punts de tall seleccionats i provarà paletes compatibles amb una dada ordenada. Es revisaran la progressió de lluminositat i el contrast amb límits i etiquetes. Els modes de previsualització del llenç de QGIS, quan estiguin disponibles, permetran comprovar l'escala de grisos i simular deficiències de visió cromàtica; alternativament, s'aplicarà la mateixa prova a una exportació. La versió final conservarà els valors HEX o RGB exactes i una nota dels problemes detectats i dels ajustos aplicats.

#### Justificar la versió final

La decisió registrarà què s'ha mantingut constant, què ha canviat, quin patró es fa més o menys visible i quines limitacions conserva. Una alternativa descartada es mantindrà com a evidència; no s'ha de presentar com un error si representa les dades correctament però respon pitjor al propòsit.

El mapa principal serà una coropleta perquè representa un percentatge. No s'hi aplicaran els colors al nombre absolut d'habitatges. Si una segona capa de símbols proporcionals representa la població total, haurà d'aportar una lectura complementària, conservar una llegenda clara i no ocultar el patró de la coropleta.

### Completar la composició i la llegenda

El mapa temàtic reutilitzarà l'extensió, la jerarquia territorial i els criteris de retolació del mapa de context. La llegenda indicarà l'indicador, la unitat, les classes i el tractament de les absències amb etiquetes comprensibles. Les fonts distingiran les dades estadístiques de la geometria municipal.

La composició es revisarà a la mida que ocuparà a la miniinfografia. El mapa s'exportarà en format vectorial a `outputs/maps`, i l'estil, la classificació i la composició editable es conservaran al projecte QGIS.

### Comprovacions de qualitat

Abans d'acceptar el mapa cal verificar que:

1. el camp, la fórmula i la unitat coincideixen amb el diccionari del capítol 2;
2. la unió no presenta duplicats ni absències inexplicades;
3. els punts de tall estan ordenats, no se solapen i coincideixen amb la llegenda;
4. les classes buides, els valors repetits i els casos extrems s'han revisat;
5. el zero i l'absència de dades tenen significats i símbols diferents;
6. la paleta conserva un ordre perceptible i contrast suficient;
7. els límits, les etiquetes i qualsevol símbol proporcional continuen sent llegibles;
8. el PDF conserva les geometries, els textos i els colors previstos.

### Evidències que s'han de conservar

::: table "Evidències de la cartografia temàtica"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `qgis` | Projecte QGIS continuat | Unió verificada, estils, classificacions i composició editable |
| `qgis` | Estil reutilitzable, si cal | Camp, classes, punts de tall, colors i símbol d'absència |
| `outputs/maps` | Mapa temàtic final | Coropleta vectorial amb llegenda, fonts, període i absències |
| `outputs/maps` | Alternativa descartada | Mateix indicador, extensió i mida amb una variació controlada |
| `README.md` | Registre de classificació | Camp, unitat, mètode, classes, punts de tall, paleta i justificació |
| `README.md` | Control d'accessibilitat | Escala de grisos, simulació cromàtica, contrast i ajustos aplicats |
:::
