---
layout: manual-chapter
title: Cartografia temàtica
description: Mètodes de representació temàtica, normalització, coropletes, símbols proporcionals, mapes dasimètrics, cartogrames, productes turístics i mapa municipal amb QGIS.
lang: ca
ref: manual-thematic-cartography
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/cartografia-tematica/
weight: 90
part: Continguts
manual_references: true
---

La cartografia temàtica converteix una variable en una lectura espacial. A diferència d'un **mapa de referència**, que prioritza localitzar elements, un **mapa temàtic** vol mostrar com es distribueix un fenomen, com varia entre territoris o quines connexions presenta. La decisió central no és quin color agrada més, sinó quin mètode cartogràfic correspon al tipus de dada, a la pregunta i a l'escala de lectura.

Aquest capítol aplica els principis de semiologia gràfica, llenguatge cartogràfic i color als mapes municipals del projecte. La seqüència és deliberada: primer es decideix què es mesura i quin mètode ho pot representar; després es normalitza quan cal; a continuació es classifica la distribució; finalment s'aplica una paleta coherent i es comprova la composició. Les referències de Brewer, Slocum, Wilke i Monmonier ajuden a entendre que classificar i simbolitzar també són decisions interpretatives {% cite brewerDesigningBetterMaps2005 slocumThematicCartography2009 wilkeFundamentalsDataVisualization2019 monmonierHowLieMaps2018 %}.

>>>>> En acabar el capítol, cal poder convertir un indicador municipal verificat en un mapa temàtic coherent, comparable i revisable.
>>>>>
>>>>> - Relacionar la pregunta, el tipus de dada i la unitat espacial amb un mètode cartogràfic adequat.
>>>>> - Distingir representacions isomòrfiques i anamòrfiques, i justificar quan la geometria territorial pot convertir-se en una marca quantitativa.
>>>>> - Construir una alternativa controlada que mantingui constants les dades, el context i la paleta.
>>>>> - Validar camps, classes, llegendes, absències, contrast i llegibilitat a la mida final.
>>>>> - Avaluar un mapa turístic acabat segons la funció editorial, el públic i el suport de consulta.

## Mètode cartogràfic i codificació cromàtica

Escollir el mètode significa decidir quina operació de lectura ha de poder fer el mapa. Una magnitud absoluta demana comparar quantitats; un percentatge o una densitat, comparar intensitats relatives; una categoria, distingir tipus; i un fenomen continu, seguir gradients o valors iguals. Cada operació exigeix una implantació i una variable visual capaces de sostenir-la. La paleta només es pot triar després d'haver establert què codificarà cada signe.

Si aquesta decisió s'ajorna, el color pot dissimular una incompatibilitat entre la dada i el mètode: un recompte pot semblar una intensitat perquè omple municipis, o unes categories poden semblar ordenades perquè formen una progressió cromàtica. El criteri no és quin mapa produeix més contrast, sinó quin conserva el significat de la variable, la unitat espacial i els límits de la comparació.

>>>>> Aquesta fase relaciona el fenomen, la dada i la geometria amb el mètode que en permet una lectura defensable.
>>>>>
>>>>> - Identificar la unitat espacial i el nivell d'agregació de cada variable.
>>>>> - Seleccionar coropletes per a intensitats comparables i símbols proporcionals per a magnituds absolutes.
>>>>> - Interpretar els límits de les unitats municipals sense atribuir el valor agregat a cada punt o persona.
>>>>> - Fer dependre els colors, les classes i els elements decoratius d'un mètode justificat.

### El fenomen i la unitat espacial

Un mapa temàtic parteix d'una relació entre una dada i una geometria. El projecte comarcal utilitza municipis, de manera que cada registre representa una unitat administrativa amb una forma, una superfície i uns veïns. Aquesta estructura és adequada per comparar indicadors municipals, però no descriu la distribució interna del fenomen dins de cada municipi. Un valor alt en una coropleta municipal no indica que tot el terme municipal tingui aquell mateix comportament.

Aquest límit té dues conseqüències importants. La primera és el **problema de la unitat espacial modificable**: un patró pot canviar si les mateixes observacions s'agrupen per municipis, barris, seccions censals o comarques. La segona és la **fal·làcia ecològica**: un resultat agregat no autoritza a atribuir el mateix comportament a cada persona, establiment o carrer. Monmonier insisteix que els mapes de dades estan plens de decisions d'unitat, classificació i simbolització que poden orientar la interpretació encara que les dades siguin certes {% cite monmonierHowLieMaps2018 longleyGeographicInformationScience2015 %}.

>>>> **Una coropleta municipal no parla de cada punt del municipi.** El mapa pot dir que un indicador municipal és alt, baix o intermedi, però no demostra que totes les urbanitzacions, platges, polígons, carrers o persones comparteixin aquell valor. Quan la pregunta demani distribució interna, caldrà una altra unitat espacial, informació auxiliar o una explicació clara del límit.

La tria de la paleta depèn del mètode. Un **mapa de coropletes** representa valors associats a unitats territorials mitjançant classes ordenades de color o valor, i és adequat per a percentatges, ràtios o densitats comparables. En un **mapa de símbols proporcionals**, la mida dels símbols varia amb una magnitud i pot representar quantitats absolutes. Les categories qualitatives exigeixen símbols distingibles que no suggereixin un ordre inexistent.

En termes de semiologia gràfica, cada mètode combina un tipus de marca amb una variable visual dominant. Una coropleta utilitza marques superficials i les ordena amb valor o color seqüencial; els símbols proporcionals utilitzen marques puntuals i codifiquen la magnitud amb la mida; un mapa de fluxos treballa amb marques lineals i pot variar amplada, direcció o valor; i una isolínia confia sobretot en la posició i la separació entre línies. Aquesta traducció ajuda a veure per què la paleta no pot decidir-se sola: cal saber quin signe farà la feina principal.

### Implantació cartogràfica i variables visuals

La [matriu general de marques i canals del capítol 3]({{ site.baseurl }}/ca/chapters/semiologia-visualitzacio/#canals-visuals-i-tasques-de-lectura) mostra combinacions formalment possibles. En cartografia, la **implantació** concreta com existeix el fenomen al mapa: un local es pot representar com un punt, un tram de carrer com una línia i un barri com una àrea. Canviar d'implantació no és aplicar un altre estil a la mateixa columna; sovint significa canviar la unitat d'observació, la geometria i la pregunta.

En una **representació isomòrfica**, la variable temàtica no modifica la geometria territorial que serveix de referència. Els municipis conserven la forma, la superfície i la posició que els corresponen a l'escala i la projecció del mapa, i la dada s'hi codifica amb color, valor, textura o símbols superposats. *Isomòrfica* no significa que el mapa sigui geomètricament idèntic al territori: tota projecció i generalització introdueix transformacions. Significa que la variable estadística representada no engrandeix, contrau ni substitueix les unitats geogràfiques.

En una **representació anamòrfica**, en canvi, la magnitud transforma la implantació territorial mateixa. La superfície cartografiada deixa de ser només el suport on es posa un signe i es converteix en la marca quantitativa: una unitat ocupa més o menys espai visual segons el valor que representa. Aquesta distinció separa un mapa de cercles proporcionals d'un cartograma. En el primer, l'àrea dels cercles respecta la proporcionalitat de tinta, però els cercles se superposen a una geografia que es manté fixa; en el segon, és la geografia representada la que canvia d'àrea o de forma per respectar aquella proporcionalitat.

Una taula d'atributs simplificada de locals fa explícita aquesta relació entre registre, geometria i variables. Cada fila descriu un establiment i la columna de geometria en conserva la posició com un punt. Les coordenades de l'exemple són fictícies i només mostren l'estructura WKT (*well-known text*); el CRS s'hauria d'identificar a les metadades de la capa.

::: table "Exemple simplificat d'una taula d'atributs de locals"
| ID | Geometria (WKT) | Tipus | Aforament | Preu mitjà (€) |
| --- | --- | --- | ---: | ---: |
| L01 | `POINT (346120 4551680)` | pub | 200 | 8,50 |
| L02 | `POINT (346540 4551430)` | bar de vins | 50 | 12,00 |
| L03 | `POINT (347010 4551210)` | cocteleria | 450 | 15,50 |
:::

En un GeoPackage, la geometria forma part de cada entitat encara que QGIS no la mostri per defecte com una columna de text a la taula d'atributs. Amb aquesta capa puntual es pot preguntar on és cada local i simbolitzar-ne els atributs: el pictograma pot indicar el tipus, l'àrea del cercle l'aforament i la lluminositat el preu mitjà. No es pot convertir la mateixa fila en un carrer o un barri canviant-ne només l'estil. Per estudiar la mobilitat nocturna cal una altra capa, amb una fila i una geometria lineal per tram i una observació o un model de persones per hora. Per comparar barris cal una capa de polígons, agregar-hi els locals i calcular un indicador comparable, com locals per quilòmetre quadrat.

![Tres implantacions cartogràfiques d'un exemple d'oferta i mobilitat nocturnes: símbols puntuals per als locals, línies d'amplada variable per al flux als carrers i una coropleta de densitat per barris]({{ site.baseurl }}/assets/img/thematic-cartography/visual-variables-nightlife-map.svg "Exemple conceptual amb dades fictícies. Els pictogrames, el mapa esquemàtic i la composició són d'elaboració pròpia. La figura aplica les variables visuals a marques puntuals, lineals i superficials sense reproduir una matriu anterior d'autoria desconeguda."){: data-figure-width-web="58rem" data-figure-width-pdf="90%"}

>>>> **Reflexió: la llegenda com a prova de disseny.** A partir de l'exemple, cal formular una pregunta sobre l'oferta o la mobilitat nocturna i escriure una fila fictícia de la capa necessària. S'han d'indicar la unitat d'observació, la geometria, el camp i la unitat de cada canal visual. Si es vol representar «qualitat», cal definir què significa i com s'observa: una categoria oficial, una valoració mitjana, el nombre de ressenyes o una auditoria no són la mateixa variable. També cal decidir si la pregunta demana localitzar establiments, mesurar fluxos per carrers o comparar una intensitat entre barris; una icona atractiva no resol aquesta decisió.

La llegenda és la prova d'aquest raonament. La forma d'una copa pot identificar un tipus de local, però no expressa bé una magnitud; una icona més gran pot representar aforament si la seva àrea segueix una escala, però comparar mides de pictogrames diferents és menys precís que comparar cercles comuns; i una coropleta no ha d'omplir barris amb el recompte brut si la seva superfície o població fa injusta la comparació. La gamma blau verdosa dona coherència als tres panells, però no té una única unitat compartida: al mapa puntual, la lluminositat ordena el preu; al mapa lineal, el color és constant i només l'amplada i la fletxa representen el pas i el sentit; a la coropleta, la lluminositat ordena classes de densitat. Cada signe ha de correspondre a un camp recuperable de la base i a una operació que el lector pugui explicar.

Els dos mapes següents mantenen un tema comú, la presència de l'espanyol, però no contenen la mateixa mena de dada. Comparar-los inicialment sense llegir-ne l'explicació permet separar el tema representat de l'estructura de la taula que hi ha darrere del color.

::: subfigures a+b "Codificacions qualitativa i quantitativa sobre la presència de l'espanyol. Recreació docent; dades, període i llicència de la font original pendents de revisar."
![Estatus institucional de l'espanyol per territoris, representat amb categories de color]({{ site.baseurl }}/assets/img/thematic-cartography/spanish-speakers-qualitative-map.png "Cada territori pertany a una categoria nominal; el color no expressa una quantitat.")
![Proporció de població que parla espanyol als estats contigus dels Estats Units, agrupada en intervals ordenats]({{ site.baseurl }}/assets/img/thematic-cartography/spanish-speakers-quantitative-map.png "Els colors ordenen intervals percentuals; la llegenda permet comparar intensitats, no només distingir categories.")
:::

>>>> **Reflexió: quina taula hi ha darrere de cada mapa?** Per continuar, cal proposar una fila possible per a cada conjunt de dades i identificar-ne la unitat d'observació, el camp representat, els valors que pot prendre i la funció del color. També cal preguntar si les categories admeten un ordre i si tindria sentit calcular-ne una diferència o una mitjana. La forma del territori no resol cap d'aquestes preguntes: la resposta s'ha de deduir del títol, la llegenda i la definició de la variable.

En el primer mapa, cada territori pertany a una categoria d'estatus institucional. Es tracta d'una **dada qualitativa nominal**: els valors serveixen per distingir situacions, però no expressen una distància numèrica ni un ordre de menys a més. En el segon, cada estat té una proporció de població que parla espanyol i el mapa l'agrupa en intervals. La dada de partida és **quantitativa** i les classes conserven un ordre. Tots dos mapes utilitzen color sobre àrees, però en el primer el to separa categories i en el segon la progressió de lluminositat permet comparar intensitats. La paleta no converteix una dada en qualitativa o quantitativa; només codifica una estructura que ja ha d'estar definida a la taula.

Altres mètodes responen a estructures diferents. Un mapa puntual localitza entitats o observacions; un mapa de fluxos representa moviments o connexions mitjançant línies; una isolínia uneix posicions amb el mateix valor d'un fenomen continu, interpolat o modelat; i un cartodiagrama situa petits gràfics sobre el territori. No tots aquests mètodes s'aplicaran al projecte comarcal, però ajuden a entendre que la forma del fenomen precedeix la selecció de la simbologia.

La comparació següent manté el Tarragonès com a territori comú i canvia la pregunta i la marca principal. La coropleta mostra el percentatge d'habitatge no principal; els cercles proporcionals, el total d'habitatges; el mapa puntual, les 22 capitals municipals; i els cartodiagrames, la composició entre habitatge principal i no principal en quatre municipis. No són quatre estils intercanviables per a una mateixa columna: cada panell respon a una estructura de dades diferent.

![Quatre mètodes de representació temàtica aplicats als municipis del Tarragonès]({{ site.baseurl }}/assets/img/thematic-cartography/thematic-methods-tarragones-2021.svg "La coropleta representa una intensitat relativa; els símbols proporcionals, un volum absolut; el mapa puntual localitza les capitals municipals; i els cartodiagrames comparen una composició. Dades d'habitatge: Idescat, 2021. Divisions i capitals municipals: ICGC, 20 de gener de 2026, CC BY 4.0."){: data-figure-width-web="38rem" data-figure-width-pdf="90%"}

### Pregunta, dada i mètode

En una coropleta, les unitats territorials extenses ocupen més superfície visual amb qualsevol indicador. El problema específic dels recomptes absoluts és diferent: combinen el fenomen amb la grandària de la població, del parc residencial o d'una altra població exposada. Per això no permeten comparar directament la intensitat municipal. La **normalització** no elimina l'efecte visual de la mida dels polígons, però defineix una quantitat comparable entre territoris i evita que una superfície ombrejada s'interpreti com si representés directament un recompte {% cite wilkeFundamentalsDataVisualization2019 %}.

::: table "Pregunta, dada i mètode cartogràfic"
| Dada o pregunta | Representació adequada | Precaució principal |
| --- | --- | --- |
| Quantitat absoluta per municipi | Símbols proporcionals | La magnitud s'ha de codificar amb l'àrea del símbol, no amb el radi |
| Percentatge, ràtio o densitat municipal | Coropleta | El denominador, la unitat i la comparabilitat han d'estar justificats |
| Categoria nominal | Colors o símbols qualitatius | No suggerir un ordre inexistent |
| Moviment entre llocs | Fluxos | Explicar direcció, amplada i unitat de les connexions |
| Fenomen continu, interpolat o modelat | Isolínies o superfícies contínues | Justificar què significa la igualtat representada i d'on surt la interpolació |
:::

La cartografia temàtica inclou més famílies que les que s'aplicaran al projecte comarcal. Conèixer-les evita forçar qualsevol dada dins d'una coropleta. En els símbols **proporcionals**, la mida varia de manera contínua amb el valor; en els **graduats**, els valors s'agrupen abans en unes poques classes de mida. El projecte treballarà amb símbols proporcionals i, per tant, no exigirà classificar-los.

::: table "Famílies de mapes temàtics i criteri d'ús"
| Família | Què prioritza | Quan pot ser útil | Risc principal |
| --- | --- | --- | --- |
| Coropleta | Intensitat en unitats territorials | Percentatges, ràtios i densitats municipals | Fer servir recomptes absoluts o classes poc justificades |
| Símbols proporcionals | Magnitud localitzada en una escala contínua | Població, places o altres quantitats absolutes | Escalar el radi en lloc de l'àrea o ocultar el fons |
| Símbols graduats | Magnitud agrupada en classes de mida | Comparacions en què unes poques classes justificades faciliten la lectura | Confondre una classe amb un valor exacte o triar talls arbitraris |
| Punts | Distribució d'una quantitat constant | Fenòmens amb localització aproximada i molts casos | Suggerir una precisió espacial que no existeix |
| Fluxos o vectors | Direcció i connexió | Mobilitat, rutes, intercanvis o desplaçaments | Saturar el mapa o confondre connexió amb volum |
| Isopletes o superfícies contínues | Gradients espacials | Altitud, pressió atmosfèrica, temperatura, precipitació, profunditat o temps d'accés modelat | Interpolar variables que no són contínues o no documentar el model |
| Cartodiagrama | Gràfics localitzats | Comparar composicions en pocs llocs | Barrejar massa variables i perdre llegibilitat |
| Dasimètric | Redistribució dins d'àrees plausibles | Densitats quan es disposa d'informació auxiliar | Fer veure una precisió no documentada |
| Cartograma o anamòrfic | Pes d'una magnitud en la forma del mapa | Mostrar desigualtat de població, economia o turisme | Perdre forma, distància i reconeixement territorial |
| Pictòric | Reconeixement mitjançant dibuixos i fites visuals | Comunicació pública, paisatge o orientació per referències recognoscibles | Exagerar objectes i ocultar distàncies, escala o jerarquia |
| Turístic d'orientació | Accés a recursos, serveis i itineraris | Preparar o conduir una visita | Confondre selecció promocional amb una anàlisi neutral del territori |
:::

Les dues darreres famílies es reprendran al final del desenvolupament teòric, quan ja es puguin avaluar com a productes acabats. Un mapa turístic pot ser pictòric, però no ho ha de ser, i un mapa pictòric tampoc no és necessàriament turístic.

### Reutilitzar el context territorial

La fase de [llenguatge cartogràfic]({{ site.baseurl }}/ca/chapters/llenguatge-cartografic/#context-territorial-requadre-situacio) ja ha resolt el mapa de context, els salts d'escala i la possible generalització d'una àrea mitjançant un punt en un requadre de situació. La cartografia temàtica no ha de repetir aquesta feina: reutilitza la peça validada i concentra la decisió nova en l'indicador, el mètode, la classificació, la paleta i la llegenda.

### Errors típics en mapes temàtics

La lectura crítica dels mapes parteix d'una idea incòmoda però necessària: un mapa sempre selecciona, simplifica i codifica el territori. Monmonier ho formula de manera provocadora perquè obliga a mirar les decisions invisibles del mapa: projecció, escala, extensió, classificació, símbols, llegenda i absències {% cite monmonierHowLieMaps2018 %}. En el projecte del curs, aquesta lectura crítica no ha de conduir a desconfiar de qualsevol mapa, sinó a preguntar quina decisió concreta podria estar desviant la interpretació.

Molts errors cartogràfics són versions espacials d'errors de gràfics. Una coropleta basada en recomptes absoluts fa que una àrea territorial sembli intensitat; una classificació massa dramàtica pot fabricar contrast; una llegenda automàtica pot ocultar unitats, decimals o valors absents; i una paleta atractiva pot suggerir un ordre que les dades no tenen. El mapa continua semblant tècnic perquè surt de QGIS, però el problema és anterior a l'exportació.

::: subfigures a+b "Comparació crítica de coropletes municipals del Tarragonès amb dades d'habitatge de 2021. Elaboració pròpia a partir de l'Idescat i de l'ICGC."
![Coropleta problemàtica del recompte absolut d'habitatge no principal als municipis del Tarragonès]({{ site.baseurl }}/assets/quarto/thematic-cartography/choropleth-housing-absolute-bad.qmd "Coropleta problemàtica: recompte absolut amb escala contínua automàtica")
![Coropleta revisada del percentatge municipal d'habitatge no principal al Tarragonès]({{ site.baseurl }}/assets/quarto/thematic-cartography/choropleth-housing-normalized-reviewed.qmd "Coropleta revisada: percentatge municipal en cinc classes quantils")
:::

La comparació manté la mateixa extensió i una orientació nord-amunt. Són mapes estadístics pensats per contrastar dues codificacions, no per estimar distàncies ni per localitzar la comarca; per això no incorporen escala, fletxa del nord ni fons de referència. El contorn comarcal dona jerarquia a les divisions municipals, mentre que el mapa de context de la fase de llenguatge cartogràfic resol la localització quan la composició final la necessita.

>>>> **Una coropleta no és adequada només perquè el camp sigui numèric.** Pintar els municipis exigeix haver comprovat si la dada expressa una intensitat comparable. Si el camp és un recompte absolut, cal normalitzar-lo o utilitzar símbols proporcionals; si el valor falta, s'ha de separar del zero.

::: table "Errors típics en mapes i revisió corresponent"
| Decisió problemàtica | Efecte sobre la lectura | Revisió preferent |
| --- | --- | --- |
| Recompte absolut en coropleta | Confon volum amb intensitat territorial | Normalitzar amb un denominador justificat o usar símbols proporcionals |
| Normalització automàtica sense revisar fórmula | Pot dividir per un camp inadequat o duplicar una ràtio ja calculada | Escriure i documentar numerador, denominador i unitat |
| Nuls representats com a zero | Incorpora absències a la classe baixa | Crear una categoria separada de sense dades o no aplicable |
| Classes escollides per maximitzar contrast | Fa semblar forts patrons febles o invisibilitza valors extrems | Comparar mètodes amb la mateixa paleta, extensió i nombre de classes |
| Paleta qualitativa en una dada ordenada | Trenca la lectura d'intensitat | Usar una progressió seqüencial o divergent segons la pregunta |
| Símbols proporcionals escalats pel radi | Exagera la magnitud percebuda | Escalar l'àrea i afegir valors de referència a la llegenda |
| Fons o relleu massa dominant | Competeix amb la variable principal | Simplificar el context i revisar jerarquia a mida final |
| Llegenda automàtica sense unitats ni font | Obliga el lector a endevinar què mesura el mapa | Reescriure títol, classes, unitat, període, font i tractament d'absències |
:::

### Símbols proporcionals i àrea {#simbols-proporcionals-area}

Els símbols proporcionals són adequats quan interessa mostrar una quantitat absoluta associada a una localització o a una unitat territorial. La regla perceptiva és la mateixa que en els cercles dels gràfics: si el símbol és un cercle, **l'àrea ha de ser proporcional al valor, no el radi**. Si un valor de referència $X_1$ es representa amb un diàmetre $D_1$, el diàmetre corresponent a $X_2$ és:

$$
D_2 = D_1\sqrt{\frac{X_2}{X_1}}
$$

Quadruplicar una dada només duplica el diàmetre. Si el diàmetre creixés directament amb el valor, les diferències d'àrea quedarien exagerades. En un mapa, a més, cal comprovar que els cercles no ocultin la geometria de base, que no suggereixin una precisió espacial falsa i que la llegenda de mides permeti llegir ordres de magnitud.

Amb els habitatges totals dels municipis del Tarragonès es pot veure com funciona aquesta regla amb dades reals: cada cercle se situa en un punt interior del seu municipi i la seva àrea és proporcional al recompte. Tarragona, Salou i Vila-seca concentren les superfícies més grans, mentre que la llegenda ofereix valors de referència per llegir-ne la mida sense haver de llegir el recompte exacte de cada municipi:

![Símbols proporcionals dels habitatges totals dels municipis del Tarragonès (2021)]({{ site.baseurl }}/assets/img/thematic-cartography/proportional-symbols-housing-total-tarragones-2021.svg?v=3 "Cada cercle se situa en un punt interior del municipi i la seva àrea és proporcional al nombre d'habitatges totals. La llegenda mostra valors de referència per llegir ordres de magnitud. Font: Idescat, habitatges per tipus d'habitatge, 2021."){: data-figure-width="48rem"}

El mateix principi es pot aplicar a les comarques de Catalunya. El mapa següent conserva les superfícies, les formes i les posicions comarcals, i representa la població estimada amb cercles proporcionals. La llegenda està expressada en habitants i l'àrea de cada cercle, no el radi, respon a la magnitud. És, per tant, una representació isomòrfica: la tinta dels símbols és proporcional a la dada, però la geografia que hi ha a sota no es deforma.

![Població estimada de les comarques de Catalunya representada amb símbols proporcionals, 2025]({{ site.baseurl }}/assets/img/thematic-cartography/population-proportional-symbols-catalonia-2025.svg "L'àrea dels cercles és proporcional a la població estimada, mentre que la geometria comarcal es manté fixa. El mapa isomòrfic prepara la comparació posterior amb el cartograma. Pes demogràfic estimat a partir dels indicadors municipals de superfície i densitat de l'Idescat, 2025. Divisions comarcals: ICGC, 20 de gener de 2026, CC BY 4.0."){: data-figure-width-web="28rem" data-figure-width-pdf="67%"}

## Normalització de la variable

Normalitzar no consisteix a aplicar qualsevol divisió a un camp numèric. Consisteix a construir una comparació territorial en què el numerador es llegeix respecte d'un denominador pertinent i documentat. Canviar el denominador canvia la pregunta: una fórmula pot ser aritmèticament correcta i, tanmateix, produir un indicador que no respon al fenomen estudiat.

Cal resoldre aquesta decisió per simbolitzar, perquè ni les classes ni els colors poden reparar una relació mal definida. També cal comprovar si el camp ja és un percentatge, una ràtio o una densitat: tornar-lo a normalitzar introdueix una segona transformació sense significat. El risc que es vol evitar és comparar municipis amb una unitat aparentment comuna però construïda sobre bases diferents o inadequades.

>>>>> Aquesta fase comprova si la variable ja és comparable o si necessita una transformació per poder-la representar.
>>>>>
>>>>> - Classificar cada camp com a recompte, percentatge, ràtio o densitat.
>>>>> - Formular i documentar el numerador, el denominador i la unitat d'un indicador normalitzat.
>>>>> - Verificar la comparabilitat de l'indicador amb el diccionari del llibre i amb casos municipals coneguts.
>>>>> - Calcular les classes amb els zeros, les absències i els casos no aplicables ja separats.

### Volum, intensitat i denominador

La classificació no corregeix un indicador inadequat. Primer s'ha de decidir què es mesura i després com s'agrupen els valors. El percentatge d'habitatge no principal ja relaciona una part amb el parc total de cada municipi; no s'ha de tornar a dividir perquè QGIS ofereixi una opció anomenada normalització.

En aquest indicador, el numerador és el nombre d'habitatges no principals, `housing_non_main`; el denominador és el total d'habitatges del mateix municipi i període, `housing_total`; i la unitat resultant és el percentatge. El camp `housing_non_main_pct` implementa, per tant, la relació `housing_non_main / housing_total × 100`. El denominador defineix una lectura de la composició del parc residencial, no del volum municipal d'habitatges.

Un nombre absolut d'habitatges no és equivalent al percentatge. Comparar municipis aplicant una coropleta al recompte d'habitatges no principals seria inadequat perquè els municipis amb més volum tendirien a dominar la lectura, encara que el pes relatiu fos moderat. Com a criteri de qualitat, l'indicador ha de poder reconstruir-se amb el numerador i el denominador del mateix municipi i període, i el resultat ha de coincidir amb `housing_non_main_pct` després de l'arrodoniment documentat. Cal contrastar el nom del camp, la fórmula i la unitat amb el diccionari del llibre per poder simbolitzar-lo.

### Zero, absència i no aplicable

Els territoris sense dades necessiten un tractament diferent dels valors zero. El **zero** és una observació possible dins de l'escala de l'indicador; l'**absència** indica que no es disposa d'un valor calculable o comparable. Un tercer cas, el **no aplicable**, apareix quan la pregunta no correspon a aquella unitat. La llegenda i la simbologia han de mantenir aquestes diferències.

En una capa municipal, un zero verificat en un camp indica que el valor observat o calculat és efectivament zero i pot entrar en la classificació. En canvi, si un municipi conserva la geometria però queda sense fila corresponent després de la unió, el nul assenyala una absència que cal contrastar amb l'informe de la unió i amb `indicator_status`: pot faltar un component de l'indicador o pot haver-hi un codi mal unit. El cas no aplicable s'ha de reservar per a una unitat a la qual la definició de l'indicador no correspon, no per tapar una incidència de la unió.

Aquestes situacions també han de ser diferents a la llegenda. El zero pot formar part de l'interval quantitatiu que li correspon; l'absència de dades necessita un símbol neutral o una trama i una etiqueta pròpia; i el no aplicable, si existeix, necessita una altra etiqueta explícita. Convertir un nul en zero l'incorporaria indegudament a la classe més baixa i alteraria tant els punts de tall com la interpretació municipal.

## Classificar dades quantitatives

**Classificar** significa agrupar una distribució ja validada per facilitar-ne una lectura, no corregir-la ni descobrir automàticament una estructura territorial. Per escollir els talls cal decidir si interessa conservar distàncies numèriques, comparar posicions, destacar desviacions respecte d'un centre o identificar agrupacions internes. Cada criteri respon una pregunta diferent i pot fer visibles fronteres que un altre criteri suavitza.

El principal risc és atribuir al territori un contrast produït pels punts de tall. Per separar aquest efecte de la resta del disseny, les alternatives s'han de comparar mantenint constants les dades, el nombre de classes, la paleta, l'extensió i la composició. La decisió final ha de poder explicar tant la lectura que facilita com les diferències que deixa en segon pla.

>>>>> Aquesta fase compara criteris de tall sense confondre l'efecte de la classificació amb altres decisions visuals.
>>>>>
>>>>> - Crear les classes a partir de l'examen dels mínims, els màxims, la mediana, les repeticions, les absències i els valors extrems.
>>>>> - Aplicar i comparar almenys dos mètodes mantenint constants l'indicador, el territori, la paleta i la composició.
>>>>> - Registrar punts de tall, observacions per classe, classes buides i efectes dels casos extrems.
>>>>> - Seleccionar una classificació segons la pregunta i la distribució, no segons el contrast que produeix.
>>>>> - Comprovar que els intervals i les etiquetes de la llegenda no se solapen ni deixen valors sense assignar.

### Diagnosi de la distribució

Per escollir el mètode cal revisar el mínim, el màxim, la mediana, els valors repetits, les absències i els casos extrems. Una llista ordenada, un histograma o el diagrama de caixa construït al capítol 3 permeten observar si la distribució és uniforme, asimètrica o dominada per pocs municipis.

La classificació agrupa valors que ja existeixen; no corregeix errors ni crea comparabilitat. Si un municipi té un valor excepcional, primer s'han de comprovar el numerador, el denominador, la font i la possible influència d'una base petita. L'extrem pot ser un error o un resultat territorial important. Si és correcte, pot concentrar la resta d'observacions en poques classes; es pot revisar el nombre de classes, comparar un altre mètode o mostrar el valor de manera explícita, però la dada s'ha de conservar i la decisió ha de quedar documentada.

![Comparació entre intervals iguals, quantils, intervals arrodonits, desviacions estàndard i trencaments naturals sobre una mateixa distribució sintètica de valors municipals]({{ site.baseurl }}/assets/img/thematic-cartography/classification-methods.svg "Distribució sintètica de dotze observacions: intervals iguals, quantils, intervals arrodonits, desviacions estàndard i trencaments naturals il·lustren criteris diferents, no una recomanació automàtica. Figura d'elaboració pròpia."){: data-figure-width="54rem"}

::: subfigures a+b+c/d+e "Cinc classificacions cartogràfiques aplicades al mateix conjunt de dades. Llicència: pendent de revisar."
![Mapa de coropletes classificat amb intervals iguals, on els punts de tall mantenen la mateixa amplitud numèrica]({{ site.baseurl }}/assets/img/legacy/iqual-intervals-choropleth-map.png "Els intervals iguals conserven amplituds constants, però poden deixar classes poc poblades")
![Mapa de coropletes classificat amb quantils, on les classes tendeixen a contenir un nombre semblant d'unitats territorials]({{ site.baseurl }}/assets/img/legacy/quantile-choropleth-map.png "Els quantils reparteixen observacions entre classes, però poden generar intervals numèrics desiguals")
![Mapa de coropletes classificat amb intervals arrodonits, útil per observar la llegibilitat de la llegenda i possibles classes buides]({{ site.baseurl }}/assets/img/legacy/pretty-breaks-choropleth-map.png "Els intervals arrodonits poden facilitar la lectura, però s'han de justificar i documentar")
![Mapa de coropletes classificat per desviacions estàndard respecte de la mitjana, amb classes per sota i per sobre del centre]({{ site.baseurl }}/assets/img/legacy/standard-deviations-map.png "Les desviacions estàndard mostren distàncies respecte de la mitjana i són més útils quan aquest centre té sentit analític")
![Mapa de coropletes classificat amb trencaments naturals de Jenks, on els punts de tall responen a agrupacions internes de la distribució]({{ site.baseurl }}/assets/img/legacy/natural-breaks-jenks-choropleth-map.png "Jenks busca classes internament homogènies, però depèn del conjunt concret de dades")
:::

La comparació visual només és útil si les alternatives estan controlades. En una prova de classificacions, el territori, l'indicador, la paleta, la mida del mapa i la llegenda general s'han de mantenir estables; només canvia el mètode de tall. Si alhora es modifica l'extensió, el nombre de classes, la rampa cromàtica i la presència d'etiquetes, ja no es pot saber quina decisió ha produït el canvi de lectura.

Aquest control no imposa cap mètode. Els quantils poden ser adequats quan es vol comparar territoris repartits en grups de mida semblant; els intervals iguals faciliten explicar distàncies numèriques; els intervals arrodonits poden fer més llegible una llegenda; les desviacions estàndard destaquen distàncies respecte d'una mitjana; i els trencaments naturals de Jenks poden ressaltar agrupacions pròpies d'una distribució. La justificació ha d'explicar quina lectura es prioritza i quin cost s'assumeix. Per exemple, un mapa amb quantils pot mostrar contrast territorial fins i tot quan els valors reals són molt pròxims, mentre que un mapa amb intervals iguals pot deixar una classe quasi buida si hi ha un valor extrem. Aquesta diferència no és un error tècnic: és una conseqüència de la pregunta i del criteri de classificació.

La taula següent resumeix aquesta decisió de manera orientativa. No ordena els mètodes com si un fos sempre millor que els altres: relaciona cada opció amb el tipus de lectura que facilita, el cost que introdueix i el risc d'aplicar-la a dades que ja són categories ordinals. Si el programa utilitzat ofereix noms diferents, cal escriure el nom exacte del mètode i revisar què fa sobre la llista ordenada de valors.

::: table "Criteris per triar un mètode de classificació"
| Mètode | Quan ajuda més | Cost principal | Dades ordinals |
| --- | --- | --- | --- |
| Intervals iguals | Quan interessa mantenir amplituds numèriques constants i explicar fàcilment la llegenda | Pot ignorar la forma de la distribució i deixar classes buides amb valors extrems | No recomanable; les categories ordinals ja tenen talls propis |
| Quantils | Quan es vol comparar grups territorials amb un nombre semblant d'observacions | Pot separar valors molt semblants i crear intervals numèrics desiguals | Només acceptable si l'ordre es reagrupa amb una justificació explícita |
| Intervals arrodonits | Quan la llegenda necessita talls memorables i els valors admeten aproximació | Pot imposar talls més llegibles que analítics o ampliar el rang més enllà de les dades | Poc recomanable, tret que els talls respectin categories definides prèviament |
| Desviacions estàndard | Quan la pregunta és identificar valors per sota o per sobre d'un centre significatiu | Depèn de la mitjana i funciona malament si la distribució és molt asimètrica | No recomanable; pressuposa distàncies numèriques interpretables |
| Trencaments naturals de Jenks | Quan hi ha agrupacions visibles i es vol minimitzar la variació interna de cada classe | Dificulta comparar períodes o territoris i pot semblar objectiu, però depèn de les dades, del nombre de classes i de l'algorisme | No recomanable; és un mètode per a magnituds quantitatives |
:::

>>>> **Cap classificació és neutral.** Canviar els punts de tall pot fer aparèixer una frontera visual, suavitzar un cas extrem o repartir contrastos que numèricament són petits. La bona pràctica no és buscar la classificació que "queda millor", sinó documentar quin mètode s'ha provat, què fa visible i quines diferències deixa en segon pla.

### Talls per amplitud i posició

Els tres mètodes d'aquest grup situen els talls amb referències diferents. Els intervals iguals divideixen l'eix numèric sense tenir en compte quantes observacions rep cada classe; els quantils parteixen de la posició dels casos ordenats encara que les amplituds resultants siguin desiguals; i els intervals arrodonits prioritzen fronteres fàcils de comunicar. Contrastar-los obliga a decidir si pesa més conservar distàncies, equilibrar el nombre de municipis o simplificar la llegenda, i evita confondre una distribució visualment equilibrada amb una classificació necessàriament adequada.

#### Intervals iguals

Els **intervals iguals** divideixen el rang numèric en classes amb la mateixa amplitud. Si $x_{min}$ és el valor mínim, $x_{max}$ el valor màxim i $k$ el nombre de classes, l'amplada és:

$$
w = \frac{x_{max} - x_{min}}{k}
$$

Els punts de tall es poden escriure com $x_{min}+jw$ per a $j=1,2,\ldots,k-1$. Aquest mètode facilita explicar la llegenda perquè totes les classes cobreixen el mateix rang numèric, però pot generar classes buides o concentrar moltes observacions en una sola classe si la distribució és asimètrica.

#### Quantils

Els **quantils** distribueixen aproximadament el mateix nombre d'observacions a cada classe. Si hi ha $n$ observacions i $k$ classes, cada classe conté al voltant de $n/k$ casos. Els punts de tall s'associen a posicions ordenades de la distribució, de manera aproximada:

$$
p_j = \frac{j}{k}\quad j=1,2,\ldots,k-1
$$

El mètode fa que totes les classes apareguin representades quan hi ha prou observacions, però les amplituds numèriques poden ser molt diferents. També pot separar valors iguals o gairebé iguals en classes diferents si la distribució conté empats o grups compactes. Per això la llegenda ha de mostrar els talls exactes i el recompte per classe s'ha de revisar.

#### Intervals arrodonits o pretty breaks

Els **intervals arrodonits** busquen punts de tall fàcils de llegir, com múltiples de 5, 10 o 25, en lloc de conservar exactament una amplitud calculada o el mateix nombre d'observacions per classe. Són útils quan la llegenda ha de comunicar-se ràpidament i els valors admeten una lectura aproximada. La regla no és purament estadística: parteix del rang de dades, tria una amplitud llegible $b$ i construeix talls del tipus:

$$
c_j = a + jb
$$

on $a$ és un inici arrodonit igual o inferior al mínim i $j=1,2,\ldots,k-1$. Aquest mètode pot millorar la llegibilitat, però també pot crear classes buides, ampliar el rang més enllà de les dades o desplaçar un tall just al costat d'un grup important de valors. Per això s'ha de documentar com qualsevol altra classificació.

### Centre i agrupacions de la distribució

Els mètodes d'aquest grup utilitzen l'estructura de la distribució, però no busquen el mateix. Les desviacions estàndard ordenen els valors per la distància a una mitjana que ha de tenir sentit analític; els trencaments de Jenks busquen agrupacions internament homogènies sense adoptar aquest centre com a referència. El primer facilita parlar de posicions per sota o per sobre de la mitjana, però pateix amb distribucions asimètriques; el segon s'adapta millor al conjunt concret, però en dificulta la comparació amb altres períodes o territoris.

#### Desviacions estàndard

La classificació per **desviacions estàndard** organitza els valors segons la distància respecte d'una mitjana. Si $\bar{x}$ és la mitjana i $s$ la desviació estàndard, una frontera típica es pot expressar com:

$$
c_j = \bar{x} + js
$$

amb $j$ prenent valors negatius i positius segons les classes situades per sota o per sobre de la mitjana. Aquest sistema és útil quan la pregunta és identificar territoris clarament per sota o per sobre d'un centre analític, però pot ser poc adequat en distribucions molt asimètriques o quan la mitjana no representa bé el conjunt. En una llegenda, el centre i les unitats de desviació han de quedar explícits.

#### Trencaments naturals de Jenks

Els **trencaments naturals** són una família de criteris que busquen classes internament homogènies i separades entre elles. En molts entorns, l'opció anomenada trencaments naturals correspon als **trencaments naturals de Jenks**, que minimitzen la suma de desviacions quadràtiques dins de cada classe:

$$
\min \sum_{c=1}^{k}\sum_{i\in c}(x_i-\bar{x}_c)^2
$$

Aquest criteri s'adapta bé a distribucions amb agrupacions visibles, però els punts de tall depenen fortament del conjunt concret de dades. Si s'afegeix o s'elimina un municipi, o si canvia el període, la classificació pot variar i dificultar la comparació temporal o territorial. Jenks no és una garantia d'objectivitat; és un criteri algorítmic que cal interpretar.

### Nombre de classes i etiquetes

No hi ha un nombre de classes universalment adequat. La selecció depèn de la forma de la distribució i del nombre d'observacions: massa classes poden deixar grups amb un sol municipi o separar diferències mínimes, mentre que massa poques poden ocultar un extrem o una agrupació rellevant. Cal revisar conjuntament les observacions per classe, l'amplada dels intervals, els valors repetits i la pregunta territorial, sense adoptar automàticament el valor proposat pel programa.

El suport i la mida final també imposen un límit perceptiu. Les classes només són útils si els colors es poden distingir sobre els polígons reals i si la llegenda es pot llegir sense convertir diferències subtils en categories aparentment precises. Quan diversos mapes han de ser comparables, convé mantenir un criteri comú de nombre de classes i punts de tall sempre que representin la mateixa variable i unitat; recalcular-los independentment pot fer que un mateix color signifiqui rangs diferents. Si una distribució obliga a apartar-se d'aquest criteri comú, el cost per a la comparació s'ha de fer explícit. Un cop escollida la classificació, se'n registraran els punts de tall exactes perquè el mapa es pugui reconstruir i comparar.

Les etiquetes de la llegenda no han de mostrar més decimals dels que es poden interpretar ni deixar buits o solapaments. Els límits de classe han de seguir un criteri consistent, especialment quan els indicadors poden prendre valors exactament iguals a un punt de tall. Una formulació com `10,0-19,9` i `20,0-29,9` pot ser llegible si les dades s'arrodoneixen a una decimal; una notació matemàtica com `[10, 20)` i `[20, 30]` és més precisa, però pot ser menys adequada per al públic general. La solució ha de conservar exactitud i comprensibilitat.

## Repertori complementari de mètodes temàtics

La coropleta i els símbols proporcionals resolen el nucli pràctic del projecte. Els mètodes següents amplien el repertori per a preguntes que exigeixen informació auxiliar, fenòmens continus o una transformació deliberada de l'espai; no substitueixen la normalització ni la classificació ja justificades.

Adoptar-los implica canviar una hipòtesi central de la representació. Un mapa dasimètric restringeix la distribució amb informació auxiliar; una superfície contínua pressuposa continuïtat o un model d'interpolació; i un cartograma converteix l'àrea territorial en una marca quantitativa. El criteri d'elecció és si aquest canvi respon millor a la pregunta i es pot documentar. El risc comú és que el detall, la continuïtat o la deformació facin semblar més precisa una inferència que les dades no sostenen.

### Mapes dasimètrics

El límit principal d'una coropleta no és només estadístic; també és espacial. Quan un municipi queda pintat amb una classe, el lector pot imaginar que el fenomen ocupa tota la superfície de manera homogènia, encara que la població, els habitatges, els establiments turístics o les places d'allotjament es concentrin en nuclis urbans, urbanitzacions, càmpings, fronts litorals o eixos de comunicació. El terme català habitual és **mapa dasimètric**. Rabella el presenta, dins del recurs de l'ICGC sobre el [mapa de coropletes](https://www.icgc.cat/en/node/19259), com una resposta al problema de les coropletes: subdividir àrees estadístiques heterogènies en àrees més petites i relativament homogènies amb l'ajuda d'informació complementària, i aplicar-hi després un tractament de tipus coroplètic {% cite slocumThematicCartography2009 %}.

Un mapa dasimètric no descobreix automàticament on és cada cas individual. Si només es disposa d'un total municipal, no es pot saber en quin carrer o parcel·la es troba el fenomen; sí que es pot restringir o redistribuir la lectura cap a zones on la presència és plausible. Una capa de cobertes del sòl, el sòl urbà, el cadastre, les edificacions, la xarxa viària o una classificació d'usos pot funcionar com a informació auxiliar, sempre que la relació amb la variable estigui justificada. Per exemple, una densitat de població representada sobre tot el terme municipal pot fer semblar habitat un espai agrícola o forestal; una versió dasimètrica pot limitar la lectura a les àrees residencials o urbanitzades, deixant clar quin criteri s'ha utilitzat.

En el projecte comarcal, el mapa dasimètric és sobretot una eina per pensar què amaga la unitat municipal. Pot ajudar a discutir per què una densitat turística per quilòmetre quadrat municipal no significa el mateix en un municipi compacte que en un terme amb grans espais no urbanitzats. Si es construeix una versió dasimètrica, cal documentar la capa auxiliar, explicar per què serveix de suport al fenomen, conservar els totals quan es redistribueixen dades agregades i evitar una aparença de precisió parcel·lària que les fonts no garanteixen. La millora respecte de la coropleta no és fer el mapa més detallat, sinó fer explícita la hipòtesi espacial que la coropleta mantenia amagada.

### Isopletes, isolínies i superfícies contínues

Els noms [**coropleta**](https://www.icgc.cat/ca/Ambits-tematics/Divulgacio/Publicacions/Diccionaris/Mapa-de-coropletes) i [**isopleta**](https://www.icgc.cat/ca/Mapes-i-geoinformacio/Publicacions/Diccionaris/Mapa-disopletes) s'assemblen perquè tots dos designen mapes temàtics quantitatius i el segment *-pleta* al·ludeix a les magnituds representades. La diferència decisiva és espacial. En una coropleta, els límits ja venen donats per unitats de recompte, com municipis o barris, i cada unitat rep un valor agregat. En un mapa d'isopletes, les línies es construeixen unint punts d'igual valor sobre una superfície contínua, observada o modelada, i per això poden travessar les fronteres administratives.

>> **Regla mnemotècnica:** **coro-** remet al grec *chora*, «regió», mentre que **iso-** remet a *ísos*, «igual». Dit curt: **les coropletes omplen territoris; les isopletes uneixen valors iguals**.

Una **isolínia** és cadascuna de les línies que uneixen punts amb el mateix valor d'una variable dins d'un mapa d'isopletes. La paraula que segueix el prefix **iso-** identifica què es manté igual al llarg de la línia. La corba de nivell és, per tant, una isolínia d'altitud i també rep el nom d'**isohipsa**; no és, però, l'únic cas d'aquesta família.

::: table "Vocabulari de les isolínies"
| Terme | Què es manté igual | Exemple d'unitat o model |
| --- | --- | --- |
| Isohipsa o corba de nivell | Altitud | Metres sobre el nivell mitjà del mar |
| Isòbara | Pressió atmosfèrica | Hectopascals reduïts al nivell del mar |
| Isoterma | Temperatura | Graus Celsius en un instant o període definit |
| Isohieta | Precipitació acumulada | Mil·límetres en un període definit |
| Isòbata | Profunditat | Metres respecte d'una referència vertical |
| Isòcrona | Temps de desplaçament o d'accés | Minuts segons una xarxa, un mode i unes velocitats |
:::

El nom no garanteix que la línia sigui vàlida. En tots els casos cal preguntar què vol dir «igual», quines observacions o quin model produeixen la superfície i amb quina incertesa s'han traçat les línies.

El cas de les isòbares ajuda a separar el vocabulari del relleu. En un mapa de superfície meteorològica, les línies no representen muntanyes ni pendents del terreny, sinó pressió atmosfèrica reduïda al nivell del mar. La distància entre isòbares suggereix el gradient de pressió: quan estan molt juntes, el canvi de pressió és més intens i pot associar-se a vents més forts. L'[anàlisi de superfície del Weather Prediction Center del 28 d'abril de 2002](https://commons.wikimedia.org/wiki/File:2002-04-28_2100_UTC_WPC_surface_analysis.jpg) mostra centres d'alta i baixa pressió, fronts i altres límits atmosfèrics; els productes del National Weather Service són de domini públic si no indiquen el contrari, segons l'[avís legal del National Weather Service](https://www.weather.gov/disclaimer/).

![Mapa de superfície del Weather Prediction Center amb isòbares, centres d'alta i baixa pressió i fronts]({{ site.baseurl }}/assets/img/thematic-cartography/wpc-surface-analysis-isobars-2002-04-28.jpg "Les isòbares uneixen punts amb la mateixa pressió atmosfèrica, no punts amb la mateixa altitud. Weather Prediction Center, anàlisi de superfície del 28 d'abril de 2002 a les 21 UTC, producte NWS de domini públic als Estats Units; fitxer incorporat des de Wikimedia Commons sense modificacions."){: data-figure-width="46rem"}

Les isolínies només són defensables si el fenomen **admet una lectura contínua** o si el model que n'ha produït la continuïtat està explicat. L'altitud canvia de manera contínua sobre una superfície; la pressió o la temperatura també es poden estimar entre estacions, amb incertesa. En canvi, no té sentit interpolar directament categories municipals com "municipi costaner" o recomptes administratius sense una hipòtesi espacial. En una isòcrona, la continuïtat no surt del territori com una superfície física, sinó d'un model de xarxa, velocitats, modes de transport i barreres. Per això la llegenda ha d'identificar la variable, la unitat, l'interval entre línies, la font de les observacions i el procediment d'interpolació o càlcul.

### Cartogrames: implantació anamòrfica {#cartogrames-anamorfics}

Un **cartograma** o mapa anamòrfic modifica la mida o la forma dels territoris per fer que la superfície representada respongui a una magnitud, com població, PIB, places turístiques o pernoctacions. No afegeix només un signe quantitatiu damunt d'un mapa fix: converteix la implantació superficial del territori en el signe. És un cas cartogràfic particular del [**principi de proporcionalitat de tinta** explicat al capítol 3]({{ site.baseurl }}/ca/chapters/semiologia-visualitzacio/#proporcionalitat-origen-i-superfície-visible): la quantitat d'àrea impresa o acolorida que veu el lector ha de mantenir una relació proporcional amb la dada.

Per això el cartograma es pot entendre com una representació híbrida, a mig camí entre un gràfic i un mapa. Funciona com un gràfic perquè l'àrea de cada marca territorial es dimensiona segons un valor, de manera semblant a l'àrea d'un cercle proporcional o a la longitud d'una barra. Continua funcionant com un mapa mentre conserva prou identitat geogràfica, posició relativa, veïnatge o correspondència territorial per reconèixer les unitats i interpretar-ne les relacions espacials. Si $x_i$ és el valor d'un territori, $X$ és la suma de tots els valors i $A$ és l'àrea total del cartograma, el criteri ideal és:

$$
\frac{A_i}{A} = \frac{x_i}{X}
$$

Aquesta igualtat no diu que el territori sigui físicament més gran, sinó que el mapa ha reassignat l'espai visual. En un mapa convencional, una comarca extensa ocupa molt espai encara que tingui poca població; en un cartograma poblacional, la seva mida visual disminueix i les àrees més poblades guanyen pes. L'operació pot fer visible una desigualtat que el mapa territorial oculta, però el preu és perdre distàncies, formes, angles i part del reconeixement espacial.

La clau matemàtica és distingir propietats **geomètriques** i propietats **topològiques**. La geometria mesura distàncies, angles, posicions, formes i àrees; la topologia descriu relacions que poden continuar sent vàlides encara que l'espai es deformi, sobretot el veïnatge: què toca amb què, quines unitats continuen connectades i quin ordre relacional es manté. Un cartograma contigu intenta conservar aquesta topologia d'adjacències mentre deforma els polígons per ajustar-ne l'àrea a la magnitud representada. Un cartograma no contigu permet separar-los o canviar-los de mida sense mantenir totes les vores; un cartograma de cercles substitueix territoris per cercles o altres formes proporcionals. Cap d'aquestes variants és una versió més "real" del mapa: totes canvien la propietat que el lector ha d'observar.

#### Cercles de Dorling i mosaics regulars

El **cartograma de Dorling**, atribuït al geògraf Danny Dorling, substitueix cada unitat territorial per un cercle, en modifica l'àrea segons una magnitud i desplaça els cercles fins que no se superposen. La posició relativa es conserva de manera aproximada, però desapareixen les fronteres i es poden alterar distàncies i veïnatges. En l'exemple mundial, l'àrea representa la població estimada de 2019 i el color diferencia continents: la Xina i l'Índia dominen l'espai visual, mentre que els països menys poblats es redueixen a cercles petits. La disposició utilitza la variant de `carto-flow` que prioritza les orientacions entre territoris veïns, però això no converteix els centres dels cercles en localitzacions geogràfiques exactes {% cite nusratStateArtCartograms2016 %}.

Un **cartograma de tessel·les d'àrea igual** substitueix les unitats per peces regulars, sovint quadrats o hexàgons. Quan cada territori rep una sola peça igual, el pes territorial es manté deliberadament constant: l'àrea deixa de privilegiar els territoris físicament extensos, però tampoc varia amb una magnitud estadística. És un cartograma perquè transforma la forma i la disposició geogràfiques, però es distingeix de l'anamorfosi quantitativa d'àrea, en què cada superfície creix o disminueix segons el valor representat. En l'exemple dels Estats Units, cada estat contigu i el districte de Colúmbia ocupen un hexàgon igual, les sigles n'identifiquen la unitat i el color diferencia les quatre regions censals. La forma regular facilita comparar unitats amb el mateix pes visual, a canvi de simplificar-ne la posició, la forma i algunes adjacències.

Els símbols i la disposició de les dues figures següents s'han calculat amb `carto-flow`, un paquet de Python per construir cartogrames; els títols, les etiquetes i les llegendes s'han compost amb Matplotlib. Aquesta distinció documenta què resol l'algorisme i què forma part de l'edició gràfica. Ni Python ni aquests paquets són eines exigides a l'estudiant en l'activitat del capítol.

![Cartograma de Dorling de la població mundial estimada de 2019]({{ site.baseurl }}/assets/img/thematic-cartography/world-population-dorling-cartogram.svg "Cartograma de Dorling de la població mundial estimada de 2019. Generat amb carto-flow 1.1.2 i Matplotlib; conjunt d'exemple amb geometries i dades de Natural Earth, domini públic."){: data-figure-width-web="52rem" data-figure-width-pdf="100%"}

![Mosaic hexagonal dels estats contigus dels Estats Units]({{ site.baseurl }}/assets/img/thematic-cartography/us-states-hex-tile-cartogram.svg "Cada estat contigu i el districte de Colúmbia ocupen un hexàgon igual; el color identifica la regió censal. Generat amb carto-flow 1.1.2 i el dataset d'exemple inclòs al paquet. Geometries i dades: Natural Earth, domini públic."){: data-figure-width-web="48rem" data-figure-width-pdf="92%"}

La comparació obliga a identificar què representa l'àrea per interpretar les figures. En el Dorling, una superfície més gran significa més població; en el mosaic, tots els territoris pesen visualment igual i el color només distingeix una categoria regional. Els dos mètodes eviten el domini visual de les unitats geogràficament grans, però no resolen la mateixa pregunta ni conserven les mateixes relacions espacials.

La comparació amb el [mapa isomòrfic de símbols proporcionals](#simbols-proporcionals-area) és decisiva. En aquell mapa, els cercles canvien d'àrea però els polígons comarcals continuen al mateix lloc i amb la mateixa forma. En un Dorling, els cercles substitueixen les comarques i es desplacen; en un cartograma contigu, són els polígons mateixos els que s'expandeixen o es contrauen. La proporcionalitat de tinta pot ser comuna als tres casos, però només els dos darrers transformen la geografia representada.

#### Llegir i comentar la deformació

Per comentar un cartograma cal comparar la quota de la variable amb la quota de superfície real, no limitar-se a dir que la forma ha canviat. Si $S_i/S$ és la proporció de superfície real d'una comarca, el **factor de deformació** $d_i$ es pot expressar com:

$$
d_i = \frac{x_i/X}{S_i/S}
$$

Una **distorsió positiva** té $d_i>1$: la comarca necessita més superfície visual perquè concentra una quota de població superior a la seva quota de territori. Una **distorsió negativa** té $d_i<1$: la seva quota de població és inferior a la quota territorial i el cartograma la contrau. La distorsió és **neutra** quan $d_i=1$, però aquest valor exacte és poc habitual; per facilitar la lectura, la figura agrupa com a *gairebé neutres* els factors entre `0,8×` i `1,25×`, dos llindars recíprocs que expressen canvis moderats. En un cartograma de població, aquest factor també equival a comparar la densitat de cada comarca amb la densitat mitjana del conjunt.

::: table "Direcció de la deformació en un cartograma"
| Distorsió | Factor ideal | Lectura correcta |
| --- | --- | --- |
| Negativa | $d_i<1$ | La superfície visual es contrau perquè la quota de població és menor que la quota territorial |
| Neutra | $d_i=1$ | La quota de població i la quota territorial coincideixen; la superfície no necessita canviar |
| Positiva | $d_i>1$ | La superfície visual s'expandeix perquè la quota de població supera la quota territorial |
:::

La comparació següent manté les mateixes 43 comarques i el mateix pes demogràfic, però canvia l'espai que ocupa cada unitat. A l'esquerra, el mapa territorial conserva les superfícies reals. A la dreta, el cartograma contigu deforma els polígons perquè l'àrea visual s'aproximi a la quota de població, alhora que intenta conservar els veïnatges. El Barcelonès, gairebé imperceptible en el mapa territorial, presenta una distorsió positiva forta; el Segrià mostra una distorsió negativa, i moltes comarques del Pirineu i de l'interior occidental es contrauen. Aquest comentari no significa que hagin guanyat o perdut població: descriu la relació entre població estimada i superfície dins del mateix període.

Els colors permeten seguir cada comarca entre els dos panells i indiquen la direcció del canvi, no la seva població. La llegenda mostra el factor de deformació: els blaus corresponen a distorsions negatives, el to central a situacions gairebé neutres i els colors càlids a distorsions positives. L'àrea del cartograma és el canal que representa la població. Per interpretar el patró convé observar també si les expansions o contraccions formen concentracions territorials, quins veïnatges es conserven i quines formes o distàncies deixen de ser comparables.

El pes de 2025 és una estimació reproduïble calculada com a superfície municipal multiplicada per la densitat publicada i agregada per comarca. Com que la densitat està arrodonida, el resultat serveix per construir i interpretar la deformació, però no substitueix un recompte oficial exacte de població.

![Comparació de les comarques de Catalunya abans i després d'una deformació contigua proporcional a la població estimada de 2025]({{ site.baseurl }}/assets/img/thematic-cartography/population-cartogram-catalonia-2025.svg "El mapa territorial conserva la superfície real. El cartograma contigu conserva els veïnatges i aproxima l'àrea de cada comarca al seu pes demogràfic: el Barcelonès s'expandeix i el Segrià es contrau. Pes demogràfic estimat a partir dels indicadors municipals de superfície i densitat de l'Idescat, 2025. Divisions comarcals: ICGC, 20 de gener de 2026, CC BY 4.0."){: data-figure-width-web="38rem" data-figure-width-pdf="90%"}

El cartograma següent aplica aquest principi a la població europea de 2018. Cada quadrat representa `500.000` persones, de manera que Alemanya, França, el Regne Unit, Itàlia, Espanya, Polònia, Ucraïna o la part europea de Rússia ocupen una presència visual molt diferent de la que tindrien en un mapa territorial convencional. La forma encara conserva prou referències per reconèixer Europa, però la lectura ja no és de distància ni de superfície real: és una lectura del pes demogràfic.

![Cartograma de la població europea de 2018 en què cada quadrat representa 500.000 persones i la mida dels països respon al volum de població]({{ site.baseurl }}/assets/img/thematic-cartography/cartogram-europe-population-2018.png "Europe's Population in 2018. Max Roser per a Our World in Data; dades de població de la UN Population Division; versió 1, setembre de 2018; llicència CC-BY-SA indicada a la mateixa imatge."){: data-figure-width="60rem"}

Un exemple directament turístic és el cartograma de HowMuch [*Mapping the Tourism Industry Around the World*](https://howmuch.net/articles/worlds-top-tourist-destinations-money-spent), publicat el 16 de setembre de 2019. La peça representa els ingressos o rebuts del turisme internacional de 2018 en dòlars: cada país canvia de mida segons el valor d'aquests rebuts, de manera que els Estats Units, Espanya, França o Tailàndia guanyen una presència visual que no correspon a la seva superfície territorial, sinó al pes econòmic de la variable. La pàgina de l'article enllaça també una [pàgina de fonts i dades preparades](https://howmuch.net/sources/worlds-top-tourist-destinations-money-spent), identificada com a `Data: Table 1.1`, que convé citar juntament amb el cartograma quan s'utilitza l'exemple.

En turisme, un cartograma podria mostrar el pes de les pernoctacions o de les places d'allotjament respecte d'una base territorial. Seria útil per comunicar concentracions fortes, però no substituiria el mapa convencional quan calgui entendre proximitat, litoralitat, accessos o continuïtats territorials. En el projecte comarcal no es demanarà construir-ne un de complet, però sí reconèixer quan una representació anamòrfica està canviant la pregunta de lectura.

### Mapes esquemàtics: deformació no proporcional

Un plànol de xarxa també deforma la geografia, però no és un cartograma ni una representació anamòrfica quantitativa en el sentit adoptat en aquest capítol. No fa proporcional la superfície territorial a una magnitud ni aplica el principi de proporcionalitat de tinta a les unitats geogràfiques. Regularitza distàncies, angles i posicions per fer llegible l'ordre de les estacions, les línies i les correspondències. El resultat se situa a mig camí entre mapa i diagrama de xarxa, no entre mapa i gràfic quantitatiu d'àrees.

La distinció ajuda a preguntar què sacrifica cada transformació i què guanya a canvi. En un cartograma, la deformació permet comparar el pes d'una magnitud. En un plànol ferroviari, permet seguir la connectivitat: el viatger no necessita mesurar la distància real entre dues parades, sinó entendre quina línia ha d'agafar, on ha de canviar i en quin ordre trobarà les estacions.

![Esquema ferroviari del Camp de Tarragona amb línies, estacions i correspondències proposades]({{ site.baseurl }}/assets/img/thematic-cartography/tarragona-railway-proposal-ptp.png "El diagrama reorganitza el Camp de Tarragona per prioritzar la continuïtat de les línies, l'ordre de les estacions i els nodes d'enllaç per sobre de les distàncies, els angles i la forma territorial exactes. Proposta ferroviària de la PTP a partir de les esmenes al PITC, publicada originalment a TRAMvia.org; fitxer incorporat sense modificacions."){: data-figure-width-web="46rem" data-figure-width-pdf="92%"}

L'exemple aplica el llenguatge gràfic d'un mapa de metro a una proposta ferroviària de la PTP per al Camp de Tarragona; per tant, no s'ha d'interpretar com una xarxa existent ni com un plànol a escala. Les línies regularitzen els recorreguts, separen ramals i fan visibles nodes com Tarragona, Reus, Vila-seca, Salou o Cambrils. A canvi d'aquesta claredat topològica, la distància aparent entre dues estacions, l'angle d'un tram i la posició respecte de la costa deixen de ser mesures fiables. La figura és útil precisament perquè permet analitzar una representació pròxima al territori del curs sense confondre connectivitat amb geometria.

## Cartografia turística i suports de publicació {#cartografia-turistica}

Un cop estudiats els mètodes temàtics, les variables visuals, la classificació i les deformacions, es pot revisar un mapa turístic com un producte editorial complet. L'avaluació ja no pregunta només si una dada està ben simbolitzada: també considera què s'ha seleccionat, per a quin públic, amb quina finalitat, en quin suport i amb quines conseqüències per a la lectura del territori.

Un **mapa turístic** és un producte cartogràfic preparat per ajudar un públic visitant a descobrir, seleccionar o recórrer un territori. Pot combinar una base de referència, itineraris, transports, allotjaments, serveis, patrimoni, paisatge, activitats i missatges promocionals. No és una família geomètrica única: pot adoptar la forma d'un plànol urbà, un mapa de carreteres, una il·lustració pictòrica, un visor interactiu o un mapa temàtic. Tampoc s'ha de confondre amb un mapa analític sobre turisme, que podria representar pernoctacions, places o despesa sense estar pensat per orientar una visita.

Seleccionar contingut és una decisió editorial amb efectes territorials. Destacar un mirador, una platja o un itinerari pot concentrar-hi l'atenció; ometre un barri, un accés en transport públic o un recurs menys conegut pot fer-lo invisible per al visitant. Una selecció és inevitable, però ha de respondre al públic i a la tasca, distingir informació de promoció i evitar que els patrocinis o la marca semblin una classificació neutral del territori {% cite monmonierHowLieMaps2018 %}.

Els exemples següents mostren tres operacions diferents. El mapa imprès de Tarragona concentra punts d'interès sobre una trama urbana; el mapa general de Mallorca integra carreteres, poblament, relleu i serveis a escala insular; i el plànol de Murten-Morat associa categories de la llegenda amb àrees, serveis i itineraris d'un esdeveniment. Cap estratègia és completa per si sola: la funció, l'extensió i el públic expliquen quina informació rep més jerarquia.

::: subfigures a+b/c "Mapes turístics a diferents escales amb funcions d'orientació i identitat editorial. Llicència: pendent de revisar."
![Mapa turístic imprès de Tarragona amb trama urbana i punts d'interès numerats]({{ site.baseurl }}/assets/img/legacy/printed-tourist-map.png "Mapa turístic urbà")
![Mapa general de Mallorca amb carreteres, relleu, poblament, serveis i informació turística]({{ site.baseurl }}/assets/img/legacy/base-tourist-map.png "Mapa turístic insular de referència")
![Plànol de Murten-Morat amb una llegenda que diferencia zones d'exposició, esdeveniments, serveis i transports]({{ site.baseurl }}/assets/img/legacy/map-legend.png "Llegenda aplicada a un plànol de visita")
:::

### Mapes pictòrics i pictogrames

Un **mapa pictòric** representa una part rellevant del territori, del relleu o dels llocs mitjançant dibuixos recognoscibles. Pot adoptar una vista obliqua, exagerar edificis o muntanyes i reduir el detall de la xarxa per afavorir la identificació i l'atracció. Aquests trets són freqüents, però no obligatoris: pictòric no significa necessàriament fictici, oblic o sense escala.

També cal distingir un mapa pictòric d'un plànol convencional que només utilitza **pictogrames puntuals**. En aquest segon cas, la base pot conservar carrers, distàncies i orientació, mentre que els dibuixos identifiquen monuments o serveis concrets. La diferència importa perquè una icona gran no conserva automàticament la superfície ni la posició exacta de l'objecte que representa.

::: subfigures a+b+c "Tres intensitats del llenguatge pictòric. Llicències: parcialment pendents de revisar."
![Panorama pictòric de Yellowstone que representa el relleu i les grans formes del paisatge en perspectiva obliqua]({{ site.baseurl }}/assets/img/legacy/pictorial-map.png "Panorama de Yellowstone de Heinrich C. Berann, encarregat pel National Park Service; obra del govern federal dels Estats Units, domini públic")
![Mapa pictòric d'Espanya amb ciutats, edificis i paisatges representats mitjançant dibuixos]({{ site.baseurl }}/assets/img/legacy/pictorial-tourist-map.png "Síntesi territorial pictòrica")
![Plànol d'Almeria amb una base urbana i monuments representats mitjançant pictogrames localitzats]({{ site.baseurl }}/assets/img/legacy/pictorial-point-tourist-map.png "Plànol urbà amb pictogrames")
:::

El llenguatge pictòric pot facilitar el reconeixement d'una fita, donar continuïtat visual a un itinerari o comunicar el caràcter d'una destinació. El cost és que els objectes il·lustrats poden tapar carrers, exagerar unes atraccions respecte d'altres i suggerir una proximitat que no es pot mesurar. La revisió ha de preguntar si la persona necessita reconèixer, orientar-se, estimar una distància o prendre una decisió accessible; una vista atractiva no resol totes aquestes tasques.

### Paper, fitxer digital i mapa interactiu

La pregunta «és millor el mapa digital o el mapa en paper?» no té una resposta universal perquè compara propietats que depenen del producte i de la situació. Un PDF consultat en un telèfon és digital però pot ser tan estàtic com un full imprès. La cerca, el canvi de zoom, la geolocalització, el càlcul de rutes o l'actualització depenen d'una aplicació, de les dades, de la connexió i del dispositiu, no de la paraula *digital*.

Les captures històriques de Salou i Benidorm permeten observar un primer contrast: el mapa turístic gira i selecciona la destinació segons la costa, l'accés o la promoció, mentre que el servei digital utilitza una orientació i una jerarquia pròpies de la plataforma. No s'han d'emprar per navegar avui: les dades, la interfície i els negocis representats poden haver canviat, i una captura fixa no conserva la cerca, el zoom ni l'actualització que definien el servei interactiu.

::: subfigures a+b/c+d "Comparacions històriques de mapes turístics de Salou i Benidorm per analitzar orientació, extensió i selecció. Llicència: pendent de revisar."
![Fragment d'un mapa turístic imprès de Salou, orientat en una franja litoral horitzontal]({{ site.baseurl }}/assets/img/legacy/salou-tourist-map.png "Mapa turístic de Salou")
![Captura històrica de Google Maps centrada a Cambrils i Vilafortuny]({{ site.baseurl }}/assets/img/legacy/salou-google-maps.png "Servei cartogràfic digital a l'entorn de Salou")
![Mapa turístic de Benidorm de 1995 amb quadrícula, itinerari d'accés, punts d'interès, nord i escala]({{ site.baseurl }}/assets/img/legacy/benidorm-tourist-map.png "Mapa turístic de Benidorm")
![Captura històrica de Google Maps de la façana litoral de Benidorm]({{ site.baseurl }}/assets/img/legacy/benidorm-google-maps.png "Servei cartogràfic digital de Benidorm")
:::

::: table "Arguments condicionats per triar el suport d'un mapa turístic"
| Suport | Arguments a favor | Arguments en contra | Contextos en què pot ser adequat |
| --- | --- | --- | --- |
| Paper | Visió conjunta estable; no necessita bateria, cobertura ni compte d'usuari; es pot plegar, anotar i compartir | Extensió i volum d'informació limitats; cerca lenta; actualització i reimpressió costoses; no mostra la posició de l'usuari | Recorregut urbà preparat, plafó fix, visita amb cobertura incerta o còpia de contingència |
| Fitxer digital estàtic | Distribució i descàrrega fàcils; conserva una composició editorial; es pot consultar fora de línia o imprimir | No calcula rutes ni s'actualitza automàticament; pot quedar obsolet sense que el lector ho percebi; la pantalla petita pot obligar a ampliar constantment | Preparació prèvia, dossier de visita, mapa accessible descarregable o versió imprimible |
| Mapa digital interactiu | Cerca, filtres, zoom, geolocalització, rutes i actualitzacions; pot adaptar capes i detall a la consulta | Depèn del dispositiu, l'energia, les dades i sovint la cobertura; pot registrar ubicació; el rànquing comercial i els suggeriments condicionen què es veu | Navegació en moviment, canvi d'itinerari, consulta de serveis actuals o necessitats molt específiques |
:::

La decisió professional pot ser una combinació: un mapa interactiu per cercar i recalcular, un fitxer descarregat per mantenir una referència fora de línia i un plafó o fullet per oferir visió conjunta al lloc. La qualitat no depèn d'oposar tecnologia i paper, sinó d'explicitar el públic, la tasca, les condicions d'ús, les fonts, l'actualització i una alternativa quan falla el suport principal.

### Activitat de debat: defensar un suport segons el context

Durant la sessió, cada grup prepararà una defensa condicionada d'un mapa en paper, un fitxer digital estàtic o un mapa interactiu. El punt de partida serà un context concret, com una visita a peu amb cobertura irregular, la preparació d'un itinerari accessible, l'orientació dins d'un recinte o la consulta d'oferta actual mentre la persona ja es desplaça.

>> **No hi ha un suport guanyador.** L'activitat no premia el paper ni el mapa digital per defecte. Avalua si cada grup relaciona la seva recomanació amb el públic, la tasca, l'accés a energia i cobertura, l'actualització, l'accessibilitat, la privacitat i una alternativa quan falla el suport principal.

1. Identificar el públic, la tasca, el lloc de consulta i les possibles fallades del context assignat.
2. Formular tres arguments a favor del suport defensat i vincular cadascun a una condició observable, no a una preferència personal.
3. Anticipar dos inconvenients i explicar com es podrien mitigar o amb quin suport complementari es resoldrien.
4. Contrastar la proposta amb un altre grup i revisar-la si l'alternativa resol millor una tasca concreta.
5. Tancar amb una recomanació que indiqui suport principal, suport de contingència i informació que s'hauria d'actualitzar.

El debat ha de concloure en quines circumstàncies cada opció conserva millor l'orientació, la visió conjunta, l'actualitat, l'accessibilitat, la privacitat i la capacitat de recuperació. Aquest criteri s'aplicarà tot seguit a la composició temàtica del projecte i, més endavant, a la infografia territorial.

## Activitat: construir i comparar el mapa temàtic

La demostració guiada reprèn la unió municipal, el registre cromàtic i el mapa de context per convertir un indicador verificat en una lectura espacial. Sempre produeix una coropleta i una **alternativa controlada** en què només canvia el mètode de classificació; l'indicador, el nombre de classes, la paleta, l'extensió, la mida i el context es mantenen constants. La prova de paletes es farà després amb els punts de tall ja fixats i no substituirà aquesta alternativa. Així es pot justificar la versió escollida sense confondre l'efecte de diverses decisions simultànies.

>>>>> L'activitat integra les decisions estadístiques, cartogràfiques i gràfiques en un mapa temàtic preparat per a la síntesi final.
>>>>>
>>>>> - Aplicar la simbologia amb el camp, la unitat, la unió i les absències verificats.
>>>>> - Produir una coropleta i conservar una alternativa controlada editable dins del projecte QGIS.
>>>>> - Construir, en la demostració del Tarragonès, un mapa separat de símbols proporcionals amb `housing_total`; en projectes adaptats, justificar la magnitud absoluta equivalent.
>>>>> - Aplicar el registre cromàtic i reutilitzar el mapa de context amb una jerarquia visual coherent.
>>>>> - Revisar la llegenda, les fonts, l'accessibilitat i l'SVG a la mida prevista per a la infografia territorial.

### Entrades i mapes temàtics resultants

Els fitxers d'entrada i continuació són:

::: listing "Fitxers d'entrada de la cartografia temàtica"
```filetree
qgis/
  tigit-06-llenguatge-cartografic.qgz
  tigit-08-cartografia-tematica.qgz
data/processed/
  tigit-05-integracio-sig.xlsx
```
:::

Per començar s'obrirà el primer projecte QGIS, que conserva la unió municipal verificada i el mapa de context, i la continuació es desarà amb el segon nom. Els indicadors de `map_export` i el registre cromàtic es recuperaran del llibre, que conserva el full `palette`; la secció `## Registre cromàtic` del `README.md` n'explicarà les funcions i comprovacions. Els resultats de treball són la coropleta final, el mapa separat de símbols proporcionals, l'alternativa controlada de classificació i el registre de les comprovacions d'accessibilitat. El mapa de context es reutilitza o s'incorpora a la composició, sense reconstruir-lo com una peça independent.

En el cas del Tarragonès, els mapes s'exportaran amb aquests noms semàntics:

::: listing "Noms dels mapes temàtics exportats"
```filetree
outputs/maps/
  coropleta_no_principal_tarragones_2021.svg
  simbols_habitatges_totals_tarragones_2021.svg
  coropleta_alt_no_principal_tarragones_2021.svg
```
:::

Els fitxers corresponen, per ordre, a la coropleta final, els símbols proporcionals i l'alternativa que només cal exportar si s'ha de consultar fora de QGIS.

Els noms s'adaptaran al territori, l'indicador i el període de cada projecte.

La pràctica compararà mapes municipals del mateix indicador construïts amb dues classificacions i una paleta constant. La demostració representarà el **percentatge d'habitatge no principal** al Tarragonès. Cada projecte podrà mantenir aquest indicador o justificar l'ús del percentatge de població de 65 anys o més.

La **coropleta** representarà el percentatge d'habitatge no principal. La lectura complementària utilitzarà **habitatges totals** amb símbols proporcionals, perquè aquesta magnitud és el denominador directe de l'indicador i permet comparar pes relatiu i volum. Els símbols se situaran en un punt interior segur del municipi, no en un centroide que pugui caure fora del polígon, i l'àrea visual serà proporcional a la dada. El mapa de context ja construït situarà el territori d'estudi i es podrà incorporar a una composició, sense reconstruir-lo.

### Verificar l'indicador unit a la capa

Es continuarà el projecte QGIS de la fase de llenguatge cartogràfic. La fase de simbolització comença amb la revisió dels camps canònics de `map_export`:

- `housing_non_main_pct` per a la coropleta;
- `housing_total` per als símbols proporcionals;
- `indicator_status` per diagnosticar resultats no calculables;
- `population_65_plus_pct` com a alternativa d'indicador relatiu quan el projecte la justifiqui.

Es comprovaran el tipus numèric, la unitat, el mínim, el màxim, els nuls i almenys tres municipis contrastats amb el llibre. L'informe de la unió ha de demostrar que no hi ha codis duplicats o municipis sense correspondència inexplicada.

### Construir alternatives controlades

L'alternativa controlada mantindrà constants el territori, l'indicador, el nombre de classes, la paleta, l'extensió, la mida i el context del mapa. Només canviarà el mètode de classificació. Així es podrà atribuir la diferència de lectura a una decisió concreta i no a una acumulació de canvis simultanis.

A partir del camp i de la unió ja verificats, la construcció seguirà un procediment estable:

1. configurar una simbologia graduada sobre el camp numèric verificat;
2. separar els valors nuls del càlcul de les classes perquè no s'interpretin com a zero;
3. aplicar un primer mètode i registrar el nombre de classes, els punts de tall i les observacions de cada classe;
4. duplicar l'estil o la capa només per crear una alternativa de classificació, sense duplicar les dades d'origen;
5. mantenir el mateix indicador, nombre de classes, paleta, extensió i composició mentre es comparen els dos mètodes;
6. fixar els punts de tall seleccionats i comparar després les paletes preparades al capítol de teoria del color;
7. desar l'estil final al projecte i, si cal reutilitzar-lo, en un fitxer d'estil al costat del projecte.

#### Comparar classificacions

La comparació mantindrà una mateixa paleta seqüencial i aplicarà almenys dos mètodes entre intervals iguals, quantils, intervals arrodonits, desviacions estàndard i trencaments naturals de Jenks. Per a cada alternativa s'anotaran el nombre d'observacions per classe, els punts de tall, les classes buides i l'efecte dels valors extrems. L'objectiu no és trobar el mapa que produeix més contrast, sinó el que respon millor a la distribució i a la pregunta.

#### Comparar paletes

Un cop seleccionats i fixats els punts de tall, es provaran paletes compatibles amb una dada ordenada. Aquesta prova cromàtica és una fase de validació separada i no és l'alternativa de classificació que es conservarà per comparar mètodes. Es revisaran la progressió de lluminositat i el contrast amb límits i etiquetes. Els modes de previsualització del llenç de QGIS, quan estiguin disponibles, permetran comprovar l'escala de grisos i simular deficiències de visió cromàtica; alternativament, s'aplicarà la mateixa prova a una exportació. La versió final conservarà els valors HEX o RGB exactes i una nota dels problemes detectats i dels ajustos aplicats.

#### Justificar la versió final

La decisió registrarà què s'ha mantingut constant, què ha canviat, quin patró es fa més o menys visible i quines limitacions conserva. Una alternativa descartada es mantindrà sempre editable dins del projecte QGIS com a evidència de comparació; no s'ha de presentar com un error si representa les dades correctament però respon pitjor al propòsit. Només caldrà exportar-la com un SVG independent si la comparació s'ha de consultar fora de QGIS.

El mapa principal serà una coropleta perquè representa un percentatge. No s'hi aplicaran els colors al nombre absolut d'habitatges. En la demostració del Tarragonès, el mapa separat de símbols proporcionals utilitzarà `housing_total` i aportarà una lectura complementària del volum que serveix de denominador a l'indicador. En un projecte adaptat es podrà triar una altra magnitud absoluta, sempre que el camp, la funció i el nom del fitxer quedin documentats. Si excepcionalment se superposen símbols i coropleta en una composició addicional, els símbols conservaran una llegenda clara i no ocultaran el patró de la coropleta.

### Construir símbols proporcionals

A la demostració del Tarragonès, el mapa de símbols proporcionals treballarà amb `housing_total`; en un projecte adaptat, treballarà amb el recompte o la magnitud absoluta que s'hagi justificat. QGIS pot generar mides a partir d'un camp numèric, però cal revisar si l'assistent està escalant l'àrea del símbol o només el radi. La llegenda mostrarà dos o tres valors de referència, i els símbols no taparan completament els límits, les etiquetes o els punts que el mapa necessita per orientar-se.

En alguns casos serà millor separar la coropleta i els símbols proporcionals en dos mapes. Superposar-los pot ser útil quan les dues lectures es reforcen, per exemple percentatge d'habitatge no principal i nombre total d'habitatges, però pot saturar la peça si les classes de color, els cercles, els límits i les etiquetes competeixen. La decisió s'ha de prendre mirant la composició final, no només la pantalla de QGIS.

### Reutilitzar el mapa de context en les composicions

El mapa de context de la fase de llenguatge cartogràfic no és una versió simplificada del mapa temàtic. La seva funció és localitzar: pot utilitzar un fons gris o simplificat, límits administratius, topònims seleccionats, xarxa viària principal o una ortofoto quan el context físic sigui necessari. En aquesta activitat es reutilitzarà o s'incorporarà a la composició sense reconstruir-lo com una tercera peça independent. El connector Open ICGC pot facilitar l'accés a aquests fons i divisions, però el mapa final ha de mantenir la mateixa exigència de fonts i crèdits que la resta de capes.

En el disseny d'impressió de QGIS es podrà preparar una composició amb el mapa temàtic principal i un petit requadre de situació, o bé una sèrie de composicions separades per comparar coropleta, símbols proporcionals i context. Si se'n fan diverses, s'han de conservar l'escala de lectura, la mida relativa dels textos, el sistema de fonts i la manera d'indicar període, unitat i productor. Canviar de composició no ha de canviar la interpretació de les dades.

![Espai de treball per documentar la simbologia graduada, els símbols proporcionals i una composició amb mapa de context a QGIS]({{ site.baseurl }}/assets/img/placeholders/qgis-thematic-layout-placeholder.svg "QGIS: simbologia graduada per a coropleta, símbols proporcionals i composició amb mapa principal, mapa de context, llegenda i fonts."){: data-figure-width-web="39.5rem" data-figure-width-pdf="94%"}

### Completar la composició i la llegenda

El mapa temàtic reutilitzarà l'extensió, la jerarquia territorial i els criteris de retolació del mapa de context. La llegenda indicarà l'indicador, la unitat, les classes i el tractament de les absències amb etiquetes comprensibles. Quan hi hagi símbols proporcionals, la llegenda de mides s'haurà de llegir sense confondre-la amb les classes de color. Les fonts distingiran les dades estadístiques, la geometria municipal i els fons cartogràfics.

La composició es revisarà a la mida que ocuparà a la infografia territorial. Els mapes finals s'exportaran en format vectorial a `outputs/maps`; l'alternativa controlada només s'exportarà separadament si cal consultar la comparació fora de QGIS. Els estils, les classificacions, les llegendes, la versió final i l'alternativa controlada editables es conservaran al projecte QGIS.

### Validar el mapa temàtic

L'acceptació del mapa exigeix verificar que:

1. el camp, la fórmula i la unitat coincideixen amb el diccionari del capítol 2;
2. el mètode cartogràfic correspon al tipus de dada i no converteix recomptes absoluts en intensitats;
3. la unió no presenta duplicats ni absències inexplicades;
4. els punts de tall estan ordenats, no se solapen i coincideixen amb la llegenda;
5. les classes buides, els valors repetits i els casos extrems s'han revisat;
6. el zero i l'absència de dades tenen significats i símbols diferents;
7. la paleta conserva un ordre perceptible i contrast suficient;
8. els límits, les etiquetes i qualsevol símbol proporcional continuen sent llegibles;
9. el mapa de context orienta sense competir amb la variable principal;
10. les llegendes de color i de mida no es confonen entre si;
11. la interpretació no atribueix a carrers, persones o establiments allò que només s'ha calculat per municipi;
12. l'SVG conserva les geometries, els textos i els colors previstos.

### Evidències de la cartografia temàtica

::: table "Evidències de la cartografia temàtica"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `qgis` | Projecte QGIS temàtic | Continuació de la fita de llenguatge cartogràfic amb unió verificada, estils, classificació final, alternativa controlada i composicions editables |
| `qgis` | Estil reutilitzable, si cal | Camp, classes, punts de tall, colors i símbol d'absència |
| `outputs/maps` | Mapa temàtic final | Coropleta final, camp `housing_non_main_pct`, llegenda, fonts, període i absències |
| `outputs/maps` | Mapa de símbols proporcionals de la demostració | Símbols amb el camp `housing_total`, escala d'àrees, valors de referència i fonts; en projectes adaptats, nom i camp equivalents justificats |
| `outputs/maps` | Alternativa controlada, només si cal consultar-la fora de QGIS | Mateix indicador, nombre de classes, paleta, extensió, mida i context; només canvia el mètode de classificació |
| Composició cartogràfica | Mapa de context reutilitzat | Peça existent incorporada o referenciada, sense exigir-ne una reconstrucció independent |
| `README.md` | Registre de classificació | Camp, unitat, mètode, classes, punts de tall, paleta i justificació |
| `README.md` | Control d'accessibilitat | Escala de grisos, simulació cromàtica, contrast i ajustos aplicats |
| `captures` | Classificació i proporcionalitat | Simbologia graduada amb punts de tall visibles i assistent de mida amb camp, escala i llegenda de referència |
:::

Amb l'indicador, la classificació, la paleta, la llegenda i el mapa de context ja validats, el projecte disposa de peces cartogràfiques comparables amb els gràfics previs. La fase de síntesi decidirà quines dues o tres peces sostenen un únic argument territorial i quines han de quedar només com a evidència de treball.
