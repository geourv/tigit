---
layout: manual-chapter
title: Cartografia temàtica
description: Mètodes de representació temàtica, normalització, coropletes, mapes dasimètrics, símbols proporcionals, cartogrames, classificació i mapa municipal amb QGIS.
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

>>>>> En acabar el capítol, cal poder convertir un indicador municipal verificat en un mapa temàtic coherent, comparable i revisable.
>>>>>
>>>>> - Relacionar la pregunta, el tipus de dada i la unitat espacial amb un mètode cartogràfic adequat.
>>>>> - Distingir recomptes absoluts, percentatges, ràtios, densitats, zeros i absències abans de simbolitzar-los.
>>>>> - Comparar classificacions quantitatives mitjançant una alternativa controlada i editable.
>>>>> - Construir una coropleta i, quan aporti una lectura complementària, un mapa de símbols proporcionals escalats per àrea.
>>>>> - Reutilitzar el mapa de context i el registre cromàtic sense alterar el significat de les dades.
>>>>> - Validar camps, classes, llegendes, contrast, llegibilitat i exportació vectorial a la mida d'ús.

## Escollir el mètode abans que la paleta

La primera decisió consisteix a determinar quina relació territorial es vol representar; la paleta només es pot triar després d'haver establert què codificarà cada signe.

>>>>> Aquesta fase relaciona el fenomen, la dada i la geometria amb el mètode que en permet una lectura defensable.
>>>>>
>>>>> - Identificar la unitat espacial i el nivell d'agregació de cada variable.
>>>>> - Seleccionar coropletes per a intensitats comparables i símbols proporcionals per a magnituds absolutes.
>>>>> - Interpretar els límits de les unitats municipals sense atribuir el valor agregat a cada punt o persona.
>>>>> - Justificar el mètode abans de definir colors, classes o elements decoratius.

### El fenomen i la unitat espacial

Un mapa temàtic parteix d'una relació entre una dada i una geometria. El projecte comarcal utilitza municipis, de manera que cada registre representa una unitat administrativa amb una forma, una superfície i uns veïns. Aquesta estructura és adequada per comparar indicadors municipals, però no descriu la distribució interna del fenomen dins de cada municipi. Un valor alt en una coropleta municipal no indica que tot el terme municipal tingui aquell mateix comportament.

Aquest límit té dues conseqüències importants. La primera és el **problema de la unitat espacial modificable**: un patró pot canviar si les mateixes observacions s'agrupen per municipis, barris, seccions censals o comarques. La segona és la **fal·làcia ecològica**: un resultat agregat no autoritza a atribuir el mateix comportament a cada persona, establiment o carrer. Monmonier insisteix que els mapes de dades estan plens de decisions d'unitat, classificació i simbolització que poden orientar la interpretació encara que les dades siguin certes {% cite monmonierHowLieMaps2018 longleyGeographicInformationScience2015 %}.

>>>> **Una coropleta municipal no parla de cada punt del municipi.** El mapa pot dir que un indicador municipal és alt, baix o intermedi, però no demostra que totes les urbanitzacions, platges, polígons, carrers o persones comparteixin aquell valor. Quan la pregunta demani distribució interna, caldrà una altra unitat espacial, informació auxiliar o una explicació clara del límit.

El mètode s'ha de decidir abans de la paleta. Un **mapa de coropletes** representa valors associats a unitats territorials mitjançant classes ordenades de color o valor, i és adequat per a percentatges, ràtios o densitats comparables. En un **mapa de símbols proporcionals**, la mida dels símbols varia amb una magnitud i pot representar quantitats absolutes. Les categories qualitatives exigeixen símbols distingibles que no suggereixin un ordre inexistent.

En termes de semiologia gràfica, cada mètode combina un tipus de marca amb una variable visual dominant. Una coropleta utilitza marques superficials i les ordena amb valor o color seqüencial; els símbols proporcionals utilitzen marques puntuals i codifiquen la magnitud amb la mida; un mapa de fluxos treballa amb marques lineals i pot variar amplada, direcció o valor; i una isolínia confia sobretot en la posició i la separació entre línies. Aquesta traducció ajuda a veure per què la paleta no pot decidir-se sola: abans cal saber quin signe farà la feina principal.

La figura següent permet veure que una coropleta pot combinar més d'una decisió visual. El blau fosc identifica els països on l'espanyol té estatus de llengua oficial; aquesta és una distinció qualitativa. En canvi, els estats dels Estats Units es classifiquen segons el percentatge de població que parla espanyol i es representen amb una progressió de blaus més o menys intensos. Per tant, el mapa no només "pinta territoris": utilitza color per separar tipus de situació i valor o intensitat per ordenar classes percentuals. La llegenda és imprescindible per saber on canvia la variable representada i quins intervals de classe s'han triat.

![Mapa mundial sobre la presència de l'espanyol, amb països on té estatus oficial i estats dels Estats Units classificats segons percentatge de població que parla espanyol]({{ site.baseurl }}/assets/img/legacy/spanish-speakers-choropleth-map.png "Exemple de coropleta que combina una categoria qualitativa amb classes percentuals ordenades. Llicència: pendent de revisar."){: data-figure-width="54rem"}

Altres mètodes responen a estructures diferents. Un mapa de punts assigna una quantitat constant a cada punt; un mapa de fluxos representa moviments o connexions mitjançant línies; i una isolínia uneix posicions amb el mateix valor d'un fenomen considerat continu, interpolat o modelat. Les corbes de nivell o isohipses només en són el cas més conegut: també hi ha isòbares de pressió atmosfèrica, isotermes de temperatura, isohietes de precipitació, isòbates de profunditat o isòcrones de temps de desplaçament. No tots aquests mètodes s'aplicaran al projecte comarcal, però ajuden a entendre que la forma del fenomen precedeix la selecció de la simbologia.

![Sis esquemes de mapes temàtics: coropleta, símbols proporcionals, punts, fluxos, isolínies i cartodiagrama]({{ site.baseurl }}/assets/img/thematic-cartography/thematic-map-types.svg "El mètode cartogràfic ha de respondre al tipus de dada: intensitat, volum, presència, moviment, continuïtat o composició localitzada. Les geometries són esquemàtiques i no representen cap comarca real. Figura d'elaboració pròpia."){: data-figure-width="54rem"}

### Pregunta, dada i mètode

En una coropleta, les unitats territorials extenses ocupen més superfície visual amb qualsevol indicador. El problema específic dels recomptes absoluts és diferent: combinen el fenomen amb la grandària de la població, del parc residencial o d'una altra població exposada. Per això no permeten comparar directament la intensitat municipal. La normalització no elimina l'efecte visual de la mida dels polígons, però defineix una quantitat comparable entre territoris i evita que una superfície ombrejada s'interpreti com si representés directament un recompte {% cite wilkeFundamentalsDataVisualization2019 %}.

::: table "Pregunta, dada i mètode cartogràfic"
| Dada o pregunta | Representació adequada | Precaució principal |
| --- | --- | --- |
| Quantitat absoluta per municipi | Símbols proporcionals | La magnitud s'ha de codificar amb l'àrea del símbol, no amb el radi |
| Percentatge, ràtio o densitat municipal | Coropleta | El denominador, la unitat i la comparabilitat han d'estar justificats |
| Categoria nominal | Colors o símbols qualitatius | No suggerir un ordre inexistent |
| Moviment entre llocs | Fluxos | Explicar direcció, amplada i unitat de les connexions |
| Fenomen continu, interpolat o modelat | Isolínies o superfícies contínues | Justificar què significa la igualtat representada i d'on surt la interpolació |
:::

La cartografia temàtica inclou més famílies que les que s'aplicaran al projecte comarcal. Conèixer-les evita forçar qualsevol dada dins d'una coropleta.

::: table "Famílies de mapes temàtics i criteri d'ús"
| Família | Què prioritza | Quan pot ser útil | Risc principal |
| --- | --- | --- | --- |
| Coropleta | Intensitat en unitats territorials | Percentatges, ràtios i densitats municipals | Fer servir recomptes absoluts o classes poc justificades |
| Símbols proporcionals o graduats | Magnitud localitzada | Població, places o altres quantitats absolutes | Escalar el radi en lloc de l'àrea o ocultar el fons |
| Punts | Distribució d'una quantitat constant | Fenòmens amb localització aproximada i molts casos | Suggerir una precisió espacial que no existeix |
| Fluxos o vectors | Direcció i connexió | Mobilitat, rutes, intercanvis o desplaçaments | Saturar el mapa o confondre connexió amb volum |
| Isopletes o superfícies contínues | Gradients espacials | Altitud, pressió atmosfèrica, temperatura, precipitació, profunditat o temps d'accés modelat | Interpolar variables que no són contínues o no documentar el model |
| Cartodiagrama | Gràfics localitzats | Comparar composicions en pocs llocs | Barrejar massa variables i perdre llegibilitat |
| Dasimètric | Redistribució dins d'àrees plausibles | Densitats quan es disposa d'informació auxiliar | Fer veure una precisió no documentada |
| Cartograma o anamòrfic | Pes d'una magnitud en la forma del mapa | Mostrar desigualtat de població, economia o turisme | Perdre forma, distància i reconeixement territorial |
| Pictòric o turístic | Reconeixement, orientació i atracció | Comunicació pública o orientació de visitants | Substituir l'anàlisi per promoció o il·lustració |
:::

### Errors típics en mapes temàtics

La lectura crítica dels mapes parteix d'una idea incòmoda però necessària: un mapa sempre selecciona, simplifica i codifica el territori. Monmonier ho formula de manera provocadora perquè obliga a mirar les decisions invisibles del mapa: projecció, escala, extensió, classificació, símbols, llegenda i absències {% cite monmonierHowLieMaps2018 %}. En el projecte del curs, aquesta lectura crítica no ha de conduir a desconfiar de qualsevol mapa, sinó a preguntar quina decisió concreta podria estar desviant la interpretació.

Molts errors cartogràfics són versions espacials d'errors de gràfics. Una coropleta basada en recomptes absoluts fa que una àrea territorial sembli intensitat; una classificació massa dramàtica pot fabricar contrast; una llegenda automàtica pot ocultar unitats, decimals o valors absents; i una paleta atractiva pot suggerir un ordre que les dades no tenen. El mapa continua semblant tècnic perquè surt de QGIS, però el problema és anterior a l'exportació.

::: subfigures a+b "Comparació amb dades esquemàtiques entre una coropleta problemàtica i una versió revisada. La subfigura a pinta recomptes absoluts de places turístiques sobre municipis, tot i que una coropleta requereix una unitat comparable i un denominador justificat, i confon una absència amb la classe més baixa; la subfigura b representa un indicador normalitzat, separa els valors sense dades i fa explícita la unitat de lectura. Figures d'elaboració pròpia."
![Mapa de coropletes problemàtic que usa recomptes absoluts, una llegenda automàtica i cap tractament visible dels valors absents]({{ site.baseurl }}/assets/img/thematic-cartography/choropleth-absolute-counts-bad.svg "Coropleta problemàtica: recompte absolut, llegenda automàtica i absència amagada")
![Mapa de coropletes revisat que usa places per mil residents, una paleta seqüencial i una classe separada per als valors sense dades]({{ site.baseurl }}/assets/img/thematic-cartography/choropleth-normalized-reviewed.svg "Coropleta revisada: indicador normalitzat, unitat explícita i absències separades")
:::

>>>> **Una coropleta no és adequada només perquè el camp sigui numèric.** Abans de pintar municipis cal decidir si la dada expressa intensitat comparable. Si el camp és un recompte absolut, cal normalitzar-lo o utilitzar símbols proporcionals; si el valor falta, s'ha de separar del zero.

::: table "Errors típics en mapes i revisió corresponent"
| Decisió problemàtica | Efecte sobre la lectura | Revisió preferent |
| --- | --- | --- |
| Recompte absolut en coropleta | Confón volum amb intensitat territorial | Normalitzar amb un denominador justificat o usar símbols proporcionals |
| Normalització automàtica sense revisar fórmula | Pot dividir per un camp inadequat o duplicar una ràtio ja calculada | Escriure i documentar numerador, denominador i unitat |
| Nuls representats com a zero | Incorpora absències a la classe baixa | Crear una categoria separada de sense dades o no aplicable |
| Classes escollides per maximitzar contrast | Fa semblar forts patrons febles o invisibilitza valors extrems | Comparar mètodes amb la mateixa paleta, extensió i nombre de classes |
| Paleta qualitativa en una dada ordenada | Trenca la lectura d'intensitat | Usar una progressió seqüencial o divergent segons la pregunta |
| Símbols proporcionals escalats pel radi | Exagera la magnitud percebuda | Escalar l'àrea i afegir valors de referència a la llegenda |
| Fons o relleu massa dominant | Competeix amb la variable principal | Simplificar el context i revisar jerarquia a mida final |
| Llegenda automàtica sense unitats ni font | Obliga el lector a endevinar què mesura el mapa | Reescriure títol, classes, unitat, període, font i tractament d'absències |
:::

### Mapes dasimètrics

El límit principal d'una coropleta no és només estadístic; també és espacial. Quan un municipi queda pintat amb una classe, el lector pot imaginar que el fenomen ocupa tota la superfície de manera homogènia, encara que la població, els habitatges, els establiments turístics o les places d'allotjament es concentrin en nuclis urbans, urbanitzacions, càmpings, fronts litorals o eixos de comunicació. El terme català habitual és **mapa dasimètric**. Rabella el presenta, dins del recurs de l'ICGC sobre el [mapa de coropletes](https://www.icgc.cat/en/node/19259), com una resposta al problema de les coropletes: subdividir àrees estadístiques heterogènies en àrees més petites i relativament homogènies amb l'ajuda d'informació complementària, i aplicar-hi després un tractament de tipus coroplètic {% cite slocumThematicCartography2009 %}.

Un mapa dasimètric no descobreix automàticament on és cada cas individual. Si només es disposa d'un total municipal, no es pot saber en quin carrer o parcel·la es troba el fenomen; sí que es pot restringir o redistribuir la lectura cap a zones on la presència és plausible. Una capa de cobertes del sòl, el sòl urbà, el cadastre, les edificacions, la xarxa viària o una classificació d'usos pot funcionar com a informació auxiliar, sempre que la relació amb la variable estigui justificada. Per exemple, una densitat de població representada sobre tot el terme municipal pot fer semblar habitat un espai agrícola o forestal; una versió dasimètrica pot limitar la lectura a les àrees residencials o urbanitzades, deixant clar quin criteri s'ha utilitzat.

En el projecte comarcal, el mapa dasimètric és sobretot una eina per pensar què amaga la unitat municipal. Pot ajudar a discutir per què una densitat turística per quilòmetre quadrat municipal no significa el mateix en un municipi compacte que en un terme amb grans espais no urbanitzats. Si es construeix una versió dasimètrica, cal documentar la capa auxiliar, explicar per què serveix de suport al fenomen, conservar els totals quan es redistribueixen dades agregades i evitar una aparença de precisió parcel·lària que les fonts no garanteixen. La millora respecte de la coropleta no és fer el mapa més detallat, sinó fer més explícita la hipòtesi espacial que abans quedava amagada.

### Símbols proporcionals i àrea

Els símbols proporcionals són adequats quan interessa mostrar una quantitat absoluta associada a una localització o a una unitat territorial. La regla perceptiva és la mateixa que en els cercles dels gràfics: si el símbol és un cercle, l'àrea ha de ser proporcional al valor, no el radi. Si un valor de referència $X_1$ es representa amb un diàmetre $D_1$, el diàmetre corresponent a $X_2$ és:

$$
D_2 = D_1\sqrt{\frac{X_2}{X_1}}
$$

Quadruplicar una dada només duplica el diàmetre. Si el diàmetre creixés directament amb el valor, les diferències d'àrea quedarien exagerades. En un mapa, a més, cal comprovar que els cercles no ocultin la geometria de base, que no suggereixin una precisió espacial falsa i que la llegenda de mides permeti llegir ordres de magnitud.

## Isolínies i superfícies contínues

### Valors iguals, no només relleu

Una **isolínia** és una línia que uneix punts amb el mateix valor d'una variable. La corba de nivell o **isohipsa** uneix punts amb la mateixa altitud, però el mateix principi s'utilitza per a moltes altres lectures geogràfiques. Una **isòbara** uneix punts amb la mateixa pressió atmosfèrica; una **isoterma**, punts amb la mateixa temperatura; una **isohieta**, punts amb la mateixa precipitació acumulada; una **isòbata**, punts amb la mateixa profunditat; i una **isòcrona**, punts que comparteixen el mateix temps d'accés segons un model de mobilitat. En tots els casos la pregunta no és només com es dibuixa la línia, sinó què vol dir que dos punts tinguin "el mateix valor".

El cas de les isòbares ajuda a separar el vocabulari del relleu. En un mapa de superfície meteorològica, les línies no representen muntanyes ni pendents del terreny, sinó pressió atmosfèrica reduïda al nivell del mar. La distància entre isòbares suggereix el gradient de pressió: quan estan molt juntes, el canvi de pressió és més intens i pot associar-se a vents més forts. L'[anàlisi de superfície del Weather Prediction Center del 28 d'abril de 2002](https://commons.wikimedia.org/wiki/File:2002-04-28_2100_UTC_WPC_surface_analysis.jpg) mostra centres d'alta i baixa pressió, fronts i altres límits atmosfèrics; els productes del National Weather Service són de domini públic si no indiquen el contrari, segons l'[avís legal del National Weather Service](https://www.weather.gov/disclaimer/).

![Mapa de superfície del Weather Prediction Center amb isòbares, centres d'alta i baixa pressió i fronts]({{ site.baseurl }}/assets/img/thematic-cartography/wpc-surface-analysis-isobars-2002-04-28.jpg "Les isòbares uneixen punts amb la mateixa pressió atmosfèrica, no punts amb la mateixa altitud. Weather Prediction Center, anàlisi de superfície del 28 d'abril de 2002 a les 21 UTC, producte NWS de domini públic als Estats Units; fitxer incorporat des de Wikimedia Commons sense modificacions."){: data-figure-width="46rem"}

Les isolínies només són defensables si el fenomen admet una lectura contínua o si el model que n'ha produït la continuïtat està explicat. L'altitud canvia de manera contínua sobre una superfície; la pressió o la temperatura també es poden estimar entre estacions, amb incertesa. En canvi, no té sentit interpolar directament categories municipals com "municipi costaner" o recomptes administratius sense una hipòtesi espacial. En una isòcrona, la continuïtat no surt del territori com una superfície física, sinó d'un model de xarxa, velocitats, modes de transport i barreres. Per això la llegenda ha d'identificar la variable, la unitat, l'interval entre línies, la font de les observacions i el procediment d'interpolació o càlcul.

## Cartogrames i mapes anamòrfics

### Canviar l'espai per mostrar pes

Un **cartograma** o mapa anamòrfic modifica la mida o la forma dels territoris per fer que la superfície representada respongui a una magnitud, com població, PIB, places turístiques o pernoctacions. És un cas cartogràfic particular del **principi de proporcionalitat de tinta**: la quantitat d'àrea impresa o acolorida que veu el lector ha de mantenir una relació proporcional amb la dada. Si $x_i$ és el valor d'un territori, $X$ és la suma de tots els valors i $A$ és l'àrea total del cartograma, el criteri ideal és:

$$
\frac{A_i}{A} = \frac{x_i}{X}
$$

Aquesta igualtat no diu que el territori sigui físicament més gran, sinó que el mapa ha reassignat l'espai visual. En un mapa convencional, una comarca extensa ocupa molt espai encara que tingui poca població; en un cartograma poblacional, la seva mida visual disminueix i les àrees més poblades guanyen pes. L'operació pot fer visible una desigualtat que el mapa territorial oculta, però el preu és perdre distàncies, formes, angles i part del reconeixement espacial.

La clau matemàtica és distingir propietats **geomètriques** i propietats **topològiques**. La geometria mesura distàncies, angles, posicions, formes i àrees; la topologia descriu relacions que poden continuar sent vàlides encara que l'espai es deformi, sobretot el veïnatge: què toca amb què, quines unitats continuen connectades i quin ordre relacional es manté. Un cartograma contigu intenta conservar aquesta topologia d'adjacències mentre deforma els polígons per ajustar-ne l'àrea a la magnitud representada. Un cartograma no contigu permet separar-los o canviar-los de mida sense mantenir totes les vores; un cartograma de cercles substitueix territoris per cercles o altres formes proporcionals. Cap d'aquestes variants és una versió més "real" del mapa: totes canvien la propietat que el lector ha d'observar.

![Comparació entre un mapa territorial convencional, un cartograma contigu esquemàtic i un cartograma de cercles en què la mida respon a una magnitud]({{ site.baseurl }}/assets/img/thematic-cartography/cartogram-anamorphic-principle.svg "Els cartogrames fan visible el pes d'una magnitud sacrificant part de la forma, la distància o la familiaritat territorial. És un esquema conceptual sense dades reals ni geometries administratives. Figura d'elaboració pròpia."){: data-figure-width="54rem"}

El cartograma següent aplica aquest principi a la població europea de 2018. Cada quadrat representa `500.000` persones, de manera que Alemanya, França, el Regne Unit, Itàlia, Espanya, Polònia, Ucraïna o la part europea de Rússia ocupen una presència visual molt diferent de la que tindrien en un mapa territorial convencional. La forma encara conserva prou referències per reconèixer Europa, però la lectura ja no és de distància ni de superfície real: és una lectura del pes demogràfic.

![Cartograma de la població europea de 2018 en què cada quadrat representa 500.000 persones i la mida dels països respon al volum de població]({{ site.baseurl }}/assets/img/thematic-cartography/cartogram-europe-population-2018.png "Europe's Population in 2018. Max Roser per a Our World in Data; dades de població de la UN Population Division; versió 1, setembre de 2018; llicència CC-BY-SA indicada a la mateixa imatge."){: data-figure-width="60rem"}

Un exemple directament turístic és el cartograma de HowMuch [*Mapping the Tourism Industry Around the World*](https://howmuch.net/articles/worlds-top-tourist-destinations-money-spent), publicat el 16 de setembre de 2019. La peça representa els ingressos o rebuts del turisme internacional de 2018 en dòlars: cada país canvia de mida segons el valor d'aquests rebuts, de manera que els Estats Units, Espanya, França o Tailàndia guanyen una presència visual que no correspon a la seva superfície territorial, sinó al pes econòmic de la variable. La pàgina de l'article enllaça també una [pàgina de fonts i dades preparades](https://howmuch.net/sources/worlds-top-tourist-destinations-money-spent), identificada com a `Data: Table 1.1`, que convé citar juntament amb el cartograma quan s'utilitza l'exemple.

Els mapes de metro permeten introduir una altra forma d'anamorfosi, més esquemàtica que estadística. Un plànol de xarxa no acostuma a fer proporcional l'àrea a una magnitud, com faria un cartograma de població, sinó que deforma distàncies, angles i posicions per fer llegible l'ordre de les estacions, les línies i les correspondències. Per això és una bona peça per preguntar què sacrifica una representació i què guanya a canvi: el viatger no necessita mesurar la distància real entre dues parades, sinó entendre quina línia ha d'agafar, on ha de canviar i en quin ordre trobarà les estacions. L'exemple següent és un [diagrama del metro de Washington](https://commons.wikimedia.org/wiki/File:Washington_DC_Metro_Map.svg) publicat a Wikimedia Commons amb dedicació CC0.

![Diagrama del metro de Washington amb línies acolorides, estacions i correspondències]({{ site.baseurl }}/assets/img/thematic-cartography/washington-dc-metro-map-2012.svg "Un mapa de metro reorganitza l'espai per prioritzar connectivitat, ordre i correspondències per sobre de distància i forma territorial exactes. Washington DC Metro Map, VeggieGarden, 14 de gener de 2012, Wikimedia Commons, CC0 1.0; fitxer incorporat sense modificacions."){: data-figure-width="46rem"}

En turisme, un cartograma podria mostrar el pes de les pernoctacions o de les places d'allotjament respecte d'una base territorial. Seria útil per comunicar concentracions fortes, però no substituiria el mapa convencional quan calgui entendre proximitat, litoralitat, accessos o continuïtats territorials. En el projecte comarcal no es demanarà construir-ne un de complet, però sí reconèixer quan una representació anamòrfica està canviant la pregunta de lectura.

## Normalitzar abans de simbolitzar

La normalització prepara una comparació territorial només quan relaciona un numerador amb un denominador pertinent i documentat.

>>>>> Aquesta fase comprova si la variable ja és comparable o si necessita una transformació abans de representar-la.
>>>>>
>>>>> - Classificar cada camp com a recompte, percentatge, ràtio o densitat.
>>>>> - Formular i documentar el numerador, el denominador i la unitat d'un indicador normalitzat.
>>>>> - Verificar la comparabilitat de l'indicador amb el diccionari del llibre i amb casos municipals coneguts.
>>>>> - Separar els zeros, les absències i els casos no aplicables abans de calcular classes.

### Volum, intensitat i denominador

La classificació no corregeix un indicador inadequat. Primer s'ha de decidir què es mesura i després com s'agrupen els valors. El percentatge d'habitatge no principal ja relaciona una part amb el parc total de cada municipi; no s'ha de tornar a dividir perquè QGIS ofereixi una opció anomenada normalització.

Un nombre absolut d'habitatges no és equivalent al percentatge. Aplicar els mateixos colors als recomptes faria que els municipis amb més volum tendissin a dominar la lectura, encara que el pes relatiu fos moderat. El nom del camp, la fórmula i la unitat s'han de contrastar amb el diccionari del llibre abans de simbolitzar.

### Zero, absència i no aplicable

Els territoris sense dades necessiten un tractament diferent dels valors zero. El zero és una observació possible dins de l'escala de l'indicador; l'absència indica que no es disposa d'un valor calculable o comparable. Un tercer cas, el **no aplicable**, apareix quan la pregunta no correspon a aquella unitat. La llegenda i la simbologia han de mantenir aquestes diferències.

Convertir nuls en zero pot alterar tant la classificació com la interpretació. Si un municipi queda sense correspondència després d'una unió, no s'ha d'incorporar a la classe més baixa; primer cal diagnosticar si falta una dada, si hi ha un codi mal unit o si realment el valor és zero.

## Classificar dades quantitatives

Classificar significa agrupar una distribució ja validada; per això cal observar-ne la forma i controlar què canvia entre alternatives.

>>>>> Aquesta fase compara criteris de tall sense confondre l'efecte de la classificació amb altres decisions visuals.
>>>>>
>>>>> - Examinar mínims, màxims, mediana, repeticions, absències i valors extrems abans de crear classes.
>>>>> - Aplicar i comparar almenys dos mètodes mantenint constants l'indicador, el territori, la paleta i la composició.
>>>>> - Registrar punts de tall, observacions per classe, classes buides i efectes dels casos extrems.
>>>>> - Seleccionar una classificació segons la pregunta i la distribució, no segons el contrast que produeix.
>>>>> - Comprovar que els intervals i les etiquetes de la llegenda no se solapen ni deixen valors sense assignar.

### Examinar la distribució abans de classificar

Abans d'escollir un mètode s'han de revisar el mínim, el màxim, la mediana, els valors repetits, les absències i els casos extrems. Una llista ordenada, un histograma o el diagrama de caixa construït al capítol 3 permeten observar si la distribució és uniforme, asimètrica o dominada per pocs municipis.

La classificació agrupa valors que ja existeixen; no corregeix errors ni crea comparabilitat. Si un municipi té un valor excepcional, primer s'ha de comprovar el numerador, el denominador i la font. Si és correcte, cal decidir com afecta les classes i explicar-ho, no eliminar-lo perquè dificulta el mapa.

![Comparació entre intervals iguals, quantils, intervals arrodonits, desviacions estàndard i trencaments naturals sobre una mateixa distribució sintètica de valors municipals]({{ site.baseurl }}/assets/img/thematic-cartography/classification-methods.svg "Distribució sintètica de dotze observacions: intervals iguals, quantils, intervals arrodonits, desviacions estàndard i trencaments naturals il·lustren criteris diferents, no una recomanació automàtica. Figura d'elaboració pròpia."){: data-figure-width="54rem"}

::: subfigures a+b+c/d+e "Comparació de cinc classificacions cartogràfiques sobre un mateix conjunt de dades. Llicència: pendent de revisar."
![Mapa de coropletes classificat amb intervals iguals, on els punts de tall mantenen la mateixa amplitud numèrica]({{ site.baseurl }}/assets/img/legacy/iqual-intervals-choropleth-map.png "Els intervals iguals conserven amplituds constants, però poden deixar classes poc poblades")
![Mapa de coropletes classificat amb quantils, on les classes tendeixen a contenir un nombre semblant d'unitats territorials]({{ site.baseurl }}/assets/img/legacy/quantile-choropleth-map.png "Els quantils reparteixen observacions entre classes, però poden generar intervals numèrics desiguals")
![Mapa de coropletes classificat amb intervals arrodonits, útil per observar la llegibilitat de la llegenda i possibles classes buides]({{ site.baseurl }}/assets/img/legacy/pretty-breaks-choropleth-map.png "Els intervals arrodonits poden facilitar la lectura, però s'han de justificar i documentar")
![Mapa de coropletes classificat per desviacions estàndard respecte de la mitjana, amb classes per sota i per sobre del centre]({{ site.baseurl }}/assets/img/legacy/standard-deviations-map.png "Les desviacions estàndard mostren distàncies respecte de la mitjana i són més útils quan aquest centre té sentit analític")
![Mapa de coropletes classificat amb trencaments naturals de Jenks, on els punts de tall responen a agrupacions internes de la distribució]({{ site.baseurl }}/assets/img/legacy/natural-breaks-jenks-choropleth-map.png "Jenks busca classes internament homogènies, però depèn del conjunt concret de dades")
:::

La comparació visual només és útil si les alternatives estan controlades. En una prova de classificacions, el territori, l'indicador, la paleta, la mida del mapa i la llegenda general s'han de mantenir estables; només canvia el mètode de tall. Si alhora es modifica l'extensió, el nombre de classes, la rampa cromàtica i la presència d'etiquetes, ja no es pot saber quina decisió ha produït el canvi de lectura.

Aquest control no imposa cap mètode. Els quantils poden ser adequats quan es vol comparar territoris repartits en grups de mida semblant; els intervals iguals faciliten explicar distàncies numèriques; els intervals arrodonits poden fer més llegible una llegenda; les desviacions estàndard destaquen distàncies respecte d'una mitjana; els trencaments màxims situen talls en salts forts entre valors consecutius; i Jenks pot ressaltar agrupacions pròpies d'una distribució. La justificació ha d'explicar quina lectura es prioritza i quin cost s'assumeix. Per exemple, un mapa amb quantils pot mostrar contrast territorial fins i tot quan els valors reals són molt pròxims, mentre que un mapa amb intervals iguals pot deixar una classe quasi buida si hi ha un valor extrem. Aquesta diferència no és un error tècnic: és una conseqüència de la pregunta i del criteri de classificació.

La taula següent resumeix aquesta decisió de manera orientativa. No ordena els mètodes com si un fos sempre millor que els altres: relaciona cada opció amb el tipus de lectura que facilita, el cost que introdueix i el risc d'aplicar-la a dades que ja són categories ordinals. Si el programa utilitzat ofereix noms diferents, cal escriure el nom exacte del mètode i revisar què fa sobre la llista ordenada de valors.

::: table "Criteris per triar un mètode de classificació"
| Mètode | Quan ajuda més | Cost principal | Dades ordinals |
| --- | --- | --- | --- |
| Intervals iguals | Quan interessa mantenir amplituds numèriques constants i explicar fàcilment la llegenda | Pot ignorar la forma de la distribució i deixar classes buides amb valors extrems | No recomanable; les categories ordinals ja tenen talls propis |
| Quantils | Quan es vol comparar grups territorials amb un nombre semblant d'observacions | Pot separar valors molt semblants i crear intervals numèrics desiguals | Només acceptable si l'ordre es reagrupa amb una justificació explícita |
| Intervals arrodonits | Quan la llegenda necessita talls memorables i els valors admeten aproximació | Pot imposar talls més llegibles que analítics o ampliar el rang més enllà de les dades | Poc recomanable, tret que els talls respectin categories definides prèviament |
| Desviacions estàndard | Quan la pregunta és identificar valors per sota o per sobre d'un centre significatiu | Depèn de la mitjana i funciona malament si la distribució és molt asimètrica | No recomanable; pressuposa distàncies numèriques interpretables |
| Trencaments màxims | Quan la llista ordenada mostra salts clars entre grups de valors | Pot produir llegendes irregulars i molt dependents d'un buit concret | No recomanable; converteix l'ordre en distàncies que potser no existeixen |
| Trencaments naturals | Quan hi ha agrupacions visibles i es vol ajustar la llegenda a la distribució | Dificulta comparar períodes o territoris perquè els talls canvien amb el conjunt | No recomanable si les categories originals ja tenen sentit |
| Trencaments naturals de Jenks | Quan es busca minimitzar la variació interna de cada classe en una distribució quantitativa | Pot semblar objectiu, però depèn de les dades, del nombre de classes i de l'algorisme | No recomanable; és un mètode per a magnituds quantitatives |
:::

>>>> **Cap classificació és neutral.** Canviar els punts de tall pot fer aparèixer una frontera visual, suavitzar un cas extrem o repartir contrastos que numèricament són petits. La bona pràctica no és buscar la classificació que "queda millor", sinó documentar quin mètode s'ha provat, què fa visible i quines diferències deixa en segon pla.

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

### Intervals arrodonits o pretty breaks

Els **intervals arrodonits** busquen punts de tall fàcils de llegir, com múltiples de 5, 10 o 25, en lloc de conservar exactament una amplitud calculada o el mateix nombre d'observacions per classe. Són útils quan la llegenda ha de comunicar-se ràpidament i els valors admeten una lectura aproximada. La regla no és purament estadística: parteix del rang de dades, tria una amplitud llegible $b$ i construeix talls del tipus:

$$
c_j = a + jb
$$

on $a$ és un inici arrodonit igual o inferior al mínim i $j=1,2,\ldots,k-1$. Aquest mètode pot millorar la llegibilitat, però també pot crear classes buides, ampliar el rang més enllà de les dades o desplaçar un tall just al costat d'un grup important de valors. Per això s'ha de documentar com qualsevol altra classificació.

### Desviacions estàndard

La classificació per **desviacions estàndard** organitza els valors segons la distància respecte d'una mitjana. Si $\bar{x}$ és la mitjana i $s$ la desviació estàndard, una frontera típica es pot expressar com:

$$
c_j = \bar{x} + js
$$

amb $j$ prenent valors negatius i positius segons les classes situades per sota o per sobre de la mitjana. Aquest sistema és útil quan la pregunta és identificar territoris clarament per sota o per sobre d'un centre analític, però pot ser poc adequat en distribucions molt asimètriques o quan la mitjana no representa bé el conjunt. En una llegenda, el centre i les unitats de desviació han de quedar explícits.

### Trencaments màxims

Els **trencaments màxims** ordenen els valors i busquen els salts més grans entre observacions consecutives. Si entre un grup de municipis i el següent hi ha un buit numèric clar, situar-hi un tall pot separar agrupacions que la distribució ja suggereix. Aquest criteri pot ser útil en una exploració, però s'ha de revisar amb prudència: un sol valor extrem pot crear un salt molt gran, i un canvi petit en les dades pot moure els punts de tall. La llegenda resultant pot ser menys intuïtiva que amb intervals iguals o arrodonits perquè les amplades de classe no segueixen una pauta regular.

### Trencaments naturals de Jenks

Els **trencaments naturals** són una família de criteris que busquen classes internament homogènies i separades entre elles. En molts entorns, l'opció anomenada trencaments naturals correspon als **trencaments naturals de Jenks**, que minimitzen la suma de desviacions quadràtiques dins de cada classe:

$$
\min \sum_{c=1}^{k}\sum_{i\in c}(x_i-\bar{x}_c)^2
$$

Aquest criteri s'adapta bé a distribucions amb agrupacions visibles, però els punts de tall depenen fortament del conjunt concret de dades. Si s'afegeix o s'elimina un municipi, o si canvia el període, la classificació pot variar i dificultar la comparació temporal o territorial. Jenks no és una garantia d'objectivitat; és un criteri algorítmic que cal interpretar.

### Nombre de classes i etiquetes

Cada mètode de classificació destaca unes diferències i n'oculta unes altres. Els intervals iguals faciliten comparar amplades numèriques, però poden deixar classes buides. Els quantils reparteixen observacions entre classes, però poden donar amplituds molt diferents. Els intervals arrodonits faciliten llegendes netes, però poden imposar talls més retòrics que analítics. Les desviacions estàndard mostren distàncies respecte de la mitjana, però depenen de la forma de la distribució. Els trencaments màxims i Jenks s'adapten a discontinuïtats o agrupacions de la distribució concreta, però els punts de tall poden canviar quan canvien les dades.

La selecció es basarà en una lectura conjunta de la distribució, el nombre d'observacions per classe, l'amplada dels intervals i la pregunta territorial. Un cop escollida la classificació, se'n registraran els punts de tall exactes perquè el mapa es pugui reconstruir i comparar.

Les etiquetes de la llegenda no han de mostrar més decimals dels que es poden interpretar ni deixar buits o solapaments. Els límits de classe han de seguir un criteri consistent, especialment quan els indicadors poden prendre valors exactament iguals a un punt de tall. Una formulació com `10,0-19,9` i `20,0-29,9` pot ser llegible si les dades s'arrodoneixen a una decimal; una notació matemàtica com `[10, 20)` i `[20, 30]` és més precisa, però pot ser menys adequada per al públic general. La solució ha de conservar exactitud i comprensibilitat.

### Casos extrems i absència de dades

Els valors extrems poden concentrar la resta d'observacions en poques classes. Es pot revisar el nombre de classes, comparar un mètode diferent o mostrar el valor de manera explícita, però qualsevol decisió ha de conservar la dada i quedar documentada. Un extrem pot ser un error, una base petita o un resultat territorial important; només la revisió del numerador, denominador i context permet distingir-ho.

## Activitat: construir i comparar el mapa temàtic

La demostració guiada reprèn la unió municipal, el registre cromàtic i el mapa de context per convertir un indicador verificat en una lectura espacial. Sempre produeix una coropleta i una alternativa controlada en què només canvia la classificació o la paleta; aquesta alternativa es conserva editable dins del projecte QGIS com a evidència de comparació i permet justificar la versió escollida sense confondre l'efecte de diverses decisions simultànies.

>>>>> L'activitat integra les decisions estadístiques, cartogràfiques i gràfiques en un mapa temàtic preparat per a la síntesi final.
>>>>>
>>>>> - Verificar el camp, la unitat, la unió i les absències abans d'aplicar la simbologia.
>>>>> - Produir una coropleta i conservar una alternativa controlada editable dins del projecte QGIS.
>>>>> - Construir símbols proporcionals només quan una magnitud absoluta aporti una lectura complementària.
>>>>> - Aplicar el registre cromàtic i reutilitzar el mapa de context amb una jerarquia visual coherent.
>>>>> - Revisar la llegenda, les fonts, l'accessibilitat i l'SVG a la mida prevista per a la miniinfografia.

### Materials i resultats de treball

Per començar es disposa del projecte QGIS compartit amb la unió municipal verificada al capítol 5, del `## Registre cromàtic` del capítol 7 i del mapa de context construït al capítol 6. Els resultats de treball són la coropleta final, la comparació controlada de classificació o paleta i el registre al `README.md` de la classificació i les comprovacions d'accessibilitat. El mapa de context es reutilitza o s'incorpora a la composició, sense reconstruir-lo com una peça independent.

En el cas del Tarragonès, els noms semàntics poden ser `outputs/maps/mapa_coropleta_tarragones_habitatge_no_principal.svg` i, si aporta una lectura complementària, un nom adaptat al camp absolut seleccionat, per exemple `outputs/maps/mapa_simbols_tarragones_poblacio_total.svg`. Si cal comparar-la fora de QGIS, l'alternativa també es pot exportar com `outputs/maps/mapa_coropleta_tarragones_habitatge_no_principal_alternativa.svg`. Els noms s'adapten al territori, l'indicador i el camp de cada projecte.

La pràctica compararà mapes municipals del mateix indicador construïts amb classificacions i paletes diferents. La demostració representarà el **percentatge d'habitatge no principal** al Tarragonès. Cada projecte podrà mantenir aquest indicador o justificar l'ús del percentatge de població de 65 anys o més.

La **coropleta** representarà un indicador relatiu, com un percentatge o una densitat, mitjançant classes de color. Quan una magnitud absoluta aporti una lectura complementària, es produirà també un **mapa de símbols proporcionals** amb la població total o els habitatges totals disponibles i mides escalades per àrea. El mapa de context ja construït situarà el territori d'estudi i es podrà incorporar a una de les composicions o reutilitzar com a peça separada, però no s'haurà de duplicar. Totes les peces compartiran fonts, criteris de retolació i una jerarquia visual coherent.

### Verificar l'indicador unit a la capa

Es continuarà el projecte QGIS del capítol de SIG. Abans de simbolitzar, es revisaran el camp seleccionat, el tipus numèric, la unitat, el mínim, el màxim, els nuls i almenys tres municipis contrastats amb el llibre. L'informe de la unió ha de demostrar que no hi ha codis duplicats o municipis sense correspondència inexplicada.

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

La primera comparació mantindrà una mateixa paleta seqüencial i aplicarà almenys dos mètodes de classificació entre intervals iguals, quantils, intervals arrodonits, desviacions estàndard, trencaments màxims si l'eina els ofereix i Jenks. Per a cada alternativa s'anotaran el nombre d'observacions per classe, els punts de tall, les classes buides i l'efecte dels valors extrems. L'objectiu no és trobar el mapa que produeix més contrast, sinó el que respon millor a la distribució i a la pregunta.

#### Comparar paletes

La segona comparació mantindrà els punts de tall seleccionats i provarà paletes compatibles amb una dada ordenada. Es revisaran la progressió de lluminositat i el contrast amb límits i etiquetes. Els modes de previsualització del llenç de QGIS, quan estiguin disponibles, permetran comprovar l'escala de grisos i simular deficiències de visió cromàtica; alternativament, s'aplicarà la mateixa prova a una exportació. La versió final conservarà els valors HEX o RGB exactes i una nota dels problemes detectats i dels ajustos aplicats.

#### Justificar la versió final

La decisió registrarà què s'ha mantingut constant, què ha canviat, quin patró es fa més o menys visible i quines limitacions conserva. Una alternativa descartada es mantindrà sempre editable dins del projecte QGIS com a evidència de comparació; no s'ha de presentar com un error si representa les dades correctament però respon pitjor al propòsit. Només caldrà exportar-la com un SVG independent si la comparació s'ha de consultar fora de QGIS.

El mapa principal serà una coropleta perquè representa un percentatge. No s'hi aplicaran els colors al nombre absolut d'habitatges. Si es produeix un mapa de símbols proporcionals, utilitzarà la població total o el total d'habitatges disponible i aportarà una lectura complementària. Si se superposen els símbols i la coropleta, els símbols conservaran una llegenda clara i no ocultaran el patró de la coropleta.

### Construir símbols proporcionals

Quan aporti aquesta lectura complementària, el mapa de símbols proporcionals treballarà amb un recompte o una magnitud absoluta disponible. QGIS pot generar mides a partir d'un camp numèric, però cal revisar si l'assistent està escalant l'àrea del símbol o només el radi. La llegenda mostrarà dos o tres valors de referència, i els símbols no taparan completament els límits, les etiquetes o els punts que el mapa necessita per orientar-se.

En alguns casos serà millor separar la coropleta i els símbols proporcionals en dos mapes. Superposar-los pot ser útil quan les dues lectures es reforcen, per exemple percentatge d'habitatge no principal i nombre total d'habitatges, però pot saturar la peça si les classes de color, els cercles, els límits i les etiquetes competeixen. La decisió s'ha de prendre mirant la composició final, no només la pantalla de QGIS.

### Mapa de referència i layouts

El mapa de referència del capítol 6 no és una versió simplificada del mapa temàtic. La seva funció és localitzar: pot utilitzar un fons gris o simplificat, límits administratius, topònims seleccionats, xarxa viària principal o una ortofoto quan el context físic sigui necessari. En aquesta activitat es reutilitzarà o s'incorporarà a la composició sense reconstruir-lo com una tercera peça independent. El connector Open ICGC pot facilitar l'accés a aquests fons i divisions, però el mapa final ha de mantenir la mateixa exigència de fonts i crèdits que la resta de capes.

En el disseny d'impressió de QGIS es podrà preparar una composició amb el mapa temàtic principal i un petit mapa de referència, o bé una sèrie de layouts separats per comparar coropleta, símbols proporcionals i context. Si es fan diverses composicions, s'han de conservar l'escala de lectura, la mida relativa dels textos, el sistema de fonts i la manera d'indicar període, unitat i productor. Canviar de layout no ha de canviar la interpretació de les dades.

![Espai de treball per documentar la simbologia graduada, els símbols proporcionals i una composició amb mapa de referència a QGIS]({{ site.baseurl }}/assets/img/placeholders/qgis-thematic-layout-placeholder.svg "QGIS: simbologia graduada per a coropleta, símbols proporcionals i layout amb mapa principal, mapa de referència, llegenda i fonts."){: data-figure-width="44rem"}

### Completar la composició i la llegenda

El mapa temàtic reutilitzarà l'extensió, la jerarquia territorial i els criteris de retolació del mapa de context. La llegenda indicarà l'indicador, la unitat, les classes i el tractament de les absències amb etiquetes comprensibles. Quan hi hagi símbols proporcionals, la llegenda de mides s'haurà de llegir sense confondre-la amb les classes de color. Les fonts distingiran les dades estadístiques, la geometria municipal i els fons cartogràfics.

La composició es revisarà a la mida que ocuparà a la miniinfografia. Els mapes finals s'exportaran en format vectorial a `outputs/maps`; l'alternativa controlada només s'exportarà separadament si cal consultar la comparació fora de QGIS. Els estils, les classificacions, les llegendes, la versió final i l'alternativa controlada editables es conservaran al projecte QGIS.

### Comprovacions de qualitat

Abans d'acceptar el mapa cal verificar que:

1. el camp, la fórmula i la unitat coincideixen amb el diccionari del capítol 2;
2. el mètode cartogràfic correspon al tipus de dada i no converteix recomptes absoluts en intensitats;
3. la unió no presenta duplicats ni absències inexplicades;
4. els punts de tall estan ordenats, no se solapen i coincideixen amb la llegenda;
5. les classes buides, els valors repetits i els casos extrems s'han revisat;
6. el zero i l'absència de dades tenen significats i símbols diferents;
7. la paleta conserva un ordre perceptible i contrast suficient;
8. els límits, les etiquetes i qualsevol símbol proporcional continuen sent llegibles;
9. el mapa de referència orienta sense competir amb la variable principal;
10. les llegendes de color i de mida no es confonen entre si;
11. la interpretació no atribueix a carrers, persones o establiments allò que només s'ha calculat per municipi;
12. l'SVG conserva les geometries, els textos i els colors previstos.

### Evidències que s'han de conservar

::: table "Evidències de la cartografia temàtica"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `qgis` | Projecte QGIS continuat | Unió verificada, estils, classificacions, versió final i alternativa controlada editables |
| `qgis` | Estil reutilitzable, si cal | Camp, classes, punts de tall, colors i símbol d'absència |
| `outputs/maps` | Mapa temàtic final | `mapa_coropleta_tarragones_habitatge_no_principal.svg`, amb llegenda, fonts, període i absències |
| `outputs/maps` | Mapa de símbols proporcionals, si aporta una lectura complementària | Nom adaptat al camp absolut seleccionat, per exemple `mapa_simbols_tarragones_poblacio_total.svg`; població total o habitatges totals disponibles, escala de mides, valors de referència i fonts |
| `outputs/maps` | Alternativa controlada, només si cal consultar-la fora de QGIS | `mapa_coropleta_tarragones_habitatge_no_principal_alternativa.svg`, amb el mateix indicador, extensió i mida i una sola variació controlada |
| Capítol 6 / composició | Mapa de context reutilitzat | Peça existent incorporada o referenciada, sense exigir-ne una reconstrucció independent |
| `README.md` | Registre de classificació | Camp, unitat, mètode, classes, punts de tall, paleta i justificació |
| `README.md` | Control d'accessibilitat | Escala de grisos, simulació cromàtica, contrast i ajustos aplicats |
:::
