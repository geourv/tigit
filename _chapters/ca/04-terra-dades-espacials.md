---
layout: manual-chapter
title: Representació de la Terra i dades espacials
description: Forma de la Terra, coordenades, projeccions, sistemes de referència i geometries espacials.
lang: ca
ref: manual-earth-spatial-data
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/terra-dades-espacials/
weight: 60
part: Continguts
manual_references: true
---

La posició geogràfica introdueix una condició que no apareix en una taula o en un gràfic convencional: les dades han d'estar relacionades amb un model de la Terra. Aquest capítol presenta els conceptes necessaris per entendre com una posició, una distància o una superfície depenen d'una forma de referència, d'unes coordenades i d'una projecció.

El vocabulari cartogràfic clàssic ajuda a entendre la representació, però el treball amb capes digitals exigeix fixar també la terminologia dels sistemes de referència, les geometries i les dades espacials. El capítol combina una lectura cartogràfica general, una introducció específica als sistemes de coordenades i una referència terminològica en català {% cite jolyCartografia1982 vanSickleBasicGISCoordinates2017 nunesDiccionariSIG2012 %}.

>>>>> En acabar el capítol, cal poder interpretar com es modela i es representa la Terra, triar un sistema de referència adequat i preparar una base espacial municipal validada a QGIS.
>>>>>
>>>>> - Distingir la superfície terrestre, el geoide, l'el·lipsoide, el dàtum i el marc de referència segons la funció que compleixen.
>>>>> - Interpretar coordenades geogràfiques i UTM amb l'ordre dels eixos, les unitats, el fus, l'hemisferi i el CRS corresponents.
>>>>> - Comparar projeccions segons les propietats que conserven, les distorsions que introdueixen i l'operació territorial prevista.
>>>>> - Justificar l'assignació d'un CRS o la reprojecció d'una geometria sense confondre-les amb la reprojecció al vol del projecte.
>>>>> - Seleccionar un model vectorial o ràster i una geometria de punt, línia o polígon d'acord amb el fenomen i l'escala.
>>>>> - Preparar a QGIS, quan calgui, una capa municipal de treball en `EPSG:25831` sense sobreescriure la font original.
>>>>> - Validar procedència, geometria, codis, CRS, extensió i mesures abans d'utilitzar una capa en una anàlisi.

## De la Terra percebuda a la Terra mesurada

### Forma, evidència i mesura

La pregunta per la forma de la Terra neix d'una experiència molt concreta: a escala humana, el terreny sembla pla, l'horitzó amaga la curvatura i els desplaçaments quotidians ocupen una part mínima del planeta. Per això moltes representacions antigues van imaginar el món com una superfície plana, sovint organitzada al voltant d'un centre polític, religiós o cultural. El mapa babilònic del món, per exemple, situava Babilònia dins d'un disc envoltat d'aigua i combinava geografia coneguda, poder imperial i imaginari mític. Aquestes formes de representar no eren simples errors: expressaven quina part del món es coneixia, quina part s'imaginava i quin lloc ocupava cada societat dins del seu relat.

La idea d'una Terra esfèrica es va consolidar amb observacions repetibles. Quan un vaixell s'allunya, desapareix primer el buc i després les parts més altes; aquesta seqüència és coherent amb una superfície corba. Durant un eclipsi de Lluna, l'ombra de la Terra projectada sobre la Lluna és circular; aquesta observació era un argument especialment fort en la tradició aristotèlica, perquè una esfera projecta una ombra circular des de qualsevol orientació. També canvia l'altura aparent de les estrelles quan canvia la latitud: constel·lacions visibles en un lloc poden quedar baixes o desaparèixer de l'horitzó en un altre.

Eratòstenes va convertir aquesta geometria en una mesura. Al voltant del solstici d'estiu, a Siene, prop de l'actual Assuan, el Sol podia arribar gairebé al zenit i il·luminar el fons d'un pou; a Alexandria, al mateix moment, una vara vertical projectava ombra. L'angle mesurat a Alexandria era d'uns 7,2°, és a dir, una cinquantena part d'una circumferència. Si la distància entre les dues ciutats representava aquell arc, multiplicar-la per cinquanta donava una estimació de la circumferència terrestre. El valor depèn de la unitat exacta d'estadi emprada, però el procediment és el més important per al curs: una observació local, una distància territorial i un model geomètric permeten estimar una magnitud planetària.

Altres evidències van reforçar aquesta imatge a mesura que milloraven els instruments i els viatges. Les circumnavegacions demostraven la continuïtat de la superfície terrestre; les xarxes geodèsiques mesuraven arcs de meridià i revelaven que la Terra s'aproxima millor a un el·lipsoide que a una esfera perfecta; la fotografia aèria i els satèl·lits van fer visible una superfície que abans s'havia deduït mitjançant ombres, angles i desplaçaments. El vídeo de l'ICGC [*La mesura de la Terra*](https://www.icgc.cat/ca/LICGC/Sobre-lICGC/Videos/La-mesura-de-la-Terra) recorre aquesta història des de les primeres representacions fins a la cartografia quotidiana actual.

Per al curs, aquesta seqüència històrica serveix per entendre que mesurar la Terra sempre implica un model. Una esfera és suficient per explicar una primera estimació del radi; un el·lipsoide és millor per calcular coordenades; el geoide és necessari per parlar d'altures físiques; i un sistema de referència fa explícit com s'ancora tot això a observacions mesurables.

>>>> **Evidències convergents.** Les imatges de satèl·lit fan visible la forma general de la Terra, i les observacions clàssiques mostren com aquesta forma es podia deduir abans de poder fotografiar-la des de l'espai. Quan s'avalua una afirmació territorial cal preguntar-se quines observacions independents la sostenen, quin model geomètric utilitza i quines prediccions permet comprovar.

### Moviments, eclíptica i latitud climàtica

La Terra rota sobre el seu eix i es desplaça al voltant del Sol. El pla d'aquest moviment orbital s'anomena **eclíptica**. El terme no vol dir el mateix que **el·líptica**: *eclíptica* designa el pla de l'òrbita terrestre i el camí aparent del Sol sobre l'esfera celeste; *el·líptica* descriu una forma geomètrica, l'el·lipse. Els dos conceptes es troben en aquesta explicació perquè l'òrbita terrestre és lleugerament el·líptica, però el nom *eclíptica* prové de la relació d'aquest pla amb els eclipsis: només es produeixen quan la Lluna se situa molt a prop d'aquest pla. L'eix de rotació terrestre no és perpendicular a l'eclíptica: està inclinat aproximadament 23,5°. Aquesta obliqüitat explica que la insolació canviï durant l'any, que hi hagi solsticis i equinoccis, i que els tròpics i els cercles polars apareguin com a paral·lels significatius a la xarxa geogràfica. A escala anual, el contrast estacional prové sobretot de la combinació entre obliqüitat, durada del dia i angle d'incidència de la radiació.

La latitud expressa una relació geomètrica amb la radiació solar. A latituds baixes, els raigs solars poden arribar amb angles més propers a la vertical i concentrar energia sobre una superfície menor. A latituds altes, la mateixa energia es reparteix sobre una superfície més gran i travessa més atmosfera. Aquesta geometria és la base astronòmica de molts contrastos climàtics, i es completa amb altitud, relleu, distància al mar, corrents oceànics i circulació atmosfèrica.

La figura resumeix dos efectes físics que convé separar. El primer és geomètric: si $E_0$ és la irradiància rebuda sobre una superfície perpendicular als raigs solars, una superfície horitzontal rep aproximadament $E = E_0 \cos z = E_0 \sin h$, on $z$ és l'angle zenital i $h$ és l'altura del Sol sobre l'horitzó. Aquesta relació, coneguda com a llei del cosinus de Lambert i formulada dins de la fotometria del segle XVIII, explica per què la mateixa radiació queda més concentrada quan el Sol és alt i més repartida quan arriba obliquament. El segon efecte és atmosfèric: la radiació directa es debilita quan travessa aire, vapor d'aigua, aerosols i gasos absorbents. Una forma simplificada de la [llei de Bouguer-Lambert-Beer](https://www.termcat.cat/ca/cercaterm/fitxa/Mzg5NjU2NA%3D%3D) és $I = I_0 e^{-\tau m}$, o bé $I = I_0 p^m$ en la formulació clàssica de la transparència, on $m$ és la massa òptica o camí atmosfèric relatiu, que creix quan el Sol és baix. Bouguer i Lambert van estudiar aquesta pèrdua d'intensitat com un problema de fotometria: com mesurar la gradació de la llum quan un feix travessa un medi. En una atmosfera real, l'atenuació també depèn que la pressió i la densitat de l'aire disminueixen amb l'altura; la llei baromètrica associada a Laplace ho expressa, de manera simplificada, com $p(z)=p_0 e^{-z/H}$ en una atmosfera isoterma. Per això, quan el Sol és baix, la radiació no només es reparteix sobre una superfície més gran: també recorre un camí atmosfèric més llarg abans d'arribar al sòl {% cite gilOlcinaOlcinaClimatologiaGeneral1997 bouguerEssaiOptique1729 lambertPhotometria1760 laplaceMecaniqueCeleste1805 %}.

::: subfigures a+b/c+d "Translació, rotació, eclíptica i incidència solar, ordenades de l'escala orbital al detall terrestre. La subfigura a situa solsticis, equinoccis, periheli i afeli; la subfigura b mostra la il·luminació de la Terra durant la translació anual; la subfigura c aïlla la rotació, l'eix terrestre i la divisió entre hemisferi il·luminat i hemisferi nocturn; la subfigura d centra la lectura en l'obliqüitat i en el repartiment de la radiació segons la latitud. Llicència: pendent de revisar."
![Esquema de l'òrbita terrestre amb solsticis, equinoccis, periheli i afeli]({{ site.baseurl }}/assets/img/coordinate-systems/earth-plane-seasons.png "L'òrbita terrestre és lleugerament el·líptica: el periheli se situa a principis de gener i l'afeli a principis de juliol, mentre que solsticis i equinoccis responen sobretot a l'obliqüitat de l'eix.")
![Esquema de la translació terrestre al voltant del Sol amb la il·luminació canviant durant l'any]({{ site.baseurl }}/assets/img/coordinate-systems/earth-translation-illumination.png "La translació al voltant del Sol fa visible la successió estacional; l'òrbita i les mides dels cossos es representen de manera esquemàtica i no a escala.")
![Esquema de la rotació terrestre amb l'eix inclinat, els raigs solars i el límit entre la part il·luminada i la part nocturna]({{ site.baseurl }}/assets/img/coordinate-systems/earth-rotation-illumination.png "La rotació terrestre explica l'alternança entre dia i nit, mentre que l'eix inclinat i els paral·lels principals permeten relacionar la il·luminació amb latitud, tròpics i cercles polars.")
![Esquema de la inclinació de l'eix terrestre i de la diferent incidència de la radiació solar segons la latitud]({{ site.baseurl }}/assets/img/coordinate-systems/earth-axial-tilt-climate.png "La inclinació de l'eix terrestre respecte del pla de l'eclíptica fa visibles els tròpics, els cercles polars i la diferència d'incidència solar entre latituds.")
:::

La resposta climàtica presenta diferències clares entre hemisferis. L'hemisferi sud té molta menys superfície continental i molta més superfície oceànica que l'hemisferi nord; com que l'oceà acumula i allibera calor més lentament que la terra ferma, tendeix a amortir i retardar part del contrast estacional. Per això la geometria solar és una base necessària per entendre les estacions, però el clima real exigeix afegir la distribució de continents i oceans, la circulació atmosfèrica i oceànica, el relleu i l'albedo.

Aquestes idees connecten la representació de la Terra amb problemes que apareixeran després al mapa. La xarxa de paral·lels i meridians relaciona posició, moviment planetari, mesura angular, hores, estacions i condicions ambientals. Quan més endavant es treballi amb projeccions, sistemes de referència i capes digitals, aquesta base evita tractar les coordenades com si fossin simples nombres en una taula.

## Modelar la forma de la Terra

### Geoide, el·lipsoide i esferoide

La forma física de la Terra, el model matemàtic utilitzat per calcular coordenades i la superfície de referència de les altures no són exactament el mateix. Aquesta distinció és important perquè una capa pot estar ben situada en planta i, alhora, expressar l'altura amb una referència inadequada. En cartografia digital, aquests conceptes apareixen dins dels sistemes de referència, però no són simples codis: indiquen quina superfície s'ha triat per mesurar, projectar o comparar.

>>>>> Aquesta fase diferencia els models físics i matemàtics que permeten expressar posicions i altures sobre la Terra.
>>>>>
>>>>> - Distingir la superfície real, el geoide, l'el·lipsoide i l'esferoide per la seva funció de referència.
>>>>> - Relacionar l'altura el·lipsoidal, l'altura ortomètrica i l'ondulació del geoide mitjançant $h = H + N$.
>>>>> - Explicar per què un el·lipsoide regional i un de global poden ajustar-se de manera diferent al territori.
>>>>> - Diferenciar un dàtum geodèsic del marc que el materialitza i de la referència vertical de les altures.

La superfície real de la Terra és el relleu: continents, fons oceànics, gel, aigua i formes canviants. El **geoide** no és aquesta superfície real. És una superfície física vinculada al camp de gravetat terrestre, propera al nivell mitjà del mar i prolongada conceptualment sota els continents. Serveix per entendre altures perquè segueix una condició gravimètrica: tots els punts del geoide comparteixen el mateix potencial de gravetat. Per això és una referència natural per a altures físiques, però no és una superfície regular ni còmoda per calcular coordenades horitzontals.

L'**el·lipsoide de referència** és un model matemàtic regular que aproxima la forma general de la Terra i permet definir latituds, longituds, normals, distàncies i projeccions amb fórmules manejables. En molts textos també es parla d'**esferoide**. En aquest context, un esferoide és un el·lipsoide de revolució, és a dir, una el·lipse que gira al voltant del seu eix menor. La paraula recorda que el model s'assembla a una esfera lleugerament aplanada, però el terme tècnic més habitual en geodèsia i cartografia digital és el·lipsoide.

En una secció meridiana, l'el·lipsoide es pot descriure mitjançant el semieix major equatorial $a$ i el semieix menor polar $b$. La diferència real entre tots dos és molt petita respecte de la mida de la Terra; la subfigura b exagera l'aplanament per fer visibles els eixos. En fer girar aquesta secció al voltant de l'eix polar s'obté l'el·lipsoide de revolució utilitzat com a model de referència.

Els el·lipsoides es poden ajustar per a territoris, èpoques i finalitats diferents. Alguns models històrics o regionals buscaven encaixar molt bé amb una part concreta del món; altres, com els que s'utilitzen en marcs globals contemporanis, busquen una coherència planetària. Això explica que un canvi de dàtum pugui desplaçar una capa encara que la projecció sembli la mateixa: no només canvia la manera de dibuixar sobre el pla, sinó també la manera d'ancorar el model a la Terra.

::: subfigures a+b/c "Geoide i el·lipsoide com a models de referència complementaris. El geoide descriu una superfície física vinculada a la gravetat; l'el·lipsoide és una superfície matemàtica regular que pot ajustar-se globalment o prioritzar una regió."
![Visualització global del geoide GOCO06s amb colors blaus i vermells que indiquen l'altura del geoide respecte d'un el·lipsoide de referència]({{ site.baseurl }}/assets/img/coordinate-systems/nasa-geoid-goco06s-2026.png "Geoide GOCO06s, amb l'altura exagerada 10.000 vegades. Visualització de Mark SubbaRao, NASA/GSFC, basada en el model gravitatori GOCO06s")
![Secció el·líptica amb el semieix major equatorial a i el semieix menor polar b]({{ site.baseurl }}/assets/img/coordinate-systems/ellipse-semi-axes.svg "Semieixos a i b d'un el·lipsoide de revolució; adaptació de M. W. Toews, Wikimedia Commons, CC0 1.0")
![Esquema amb un el·lipsoide global i dos el·lipsoides locals que s'ajusten millor a Amèrica del Nord o a Europa]({{ site.baseurl }}/assets/img/coordinate-systems/ellipsoid-local-fit.svg "Esquema propi, no a escala: les formes, els desplaçaments i les separacions estan exagerats per mostrar com un el·lipsoide local pot encaixar millor amb una regió, mentre que l'el·lipsoide global reparteix l'encaix a escala planetària")
:::

La subfigura a és útil justament perquè exagera allò que a escala planetària gairebé no veuríem. La mateixa [fitxa de la NASA](https://svs.gsfc.nasa.gov/5660) avisa que hi ha una versió a escala en què les variacions no són perceptibles, i una versió exagerada per fer-les visibles. Aquesta és una bona advertència cartogràfica: una figura del geoide no mostra muntanyes ni fondàries oceàniques, sinó diferències de potencial gravimètric respecte d'un el·lipsoide. La subfigura c també és un esquema exagerat: no representa les dimensions reals dels el·lipsoides, sinó la idea que l'encaix d'un model depèn de l'àrea d'ús i del dàtum que el materialitza.

>>>> **Ni el geoide ni l'el·lipsoide són «la forma real de la Terra».** El relleu real és irregular i inclou la superfície topogràfica i batimètrica. El geoide és una superfície física de referència gravimètrica; l'el·lipsoide és una superfície matemàtica regular. Cada model respon a una pregunta diferent i tots dos simplifiquen la realitat.

### Altures el·lipsoidals i altures gravimètriques

La distinció entre geoide i el·lipsoide es fa especialment visible quan es parla d'altures. Un receptor GNSS calcula habitualment una **altura el·lipsoidal** $h$, mesurada respecte de l'el·lipsoide i al llarg de la normal a aquest el·lipsoide. Aquesta altura és coherent amb el sistema geodèsic de posicionament, però no respon directament a la pregunta quotidiana de quants metres hi ha sobre el nivell del mar.

Les altures que utilitza la cartografia topogràfica acostumen a ser altures físiques o gravimètriques. En el cas més habitual d'aquesta explicació, l'**altura ortomètrica** $H$ es mesura respecte del geoide i segueix la direcció de la gravetat. La diferència entre el geoide i l'el·lipsoide en un punt és l'**ondulació del geoide** $N$. De manera simplificada, la relació es pot escriure com $h = H + N$: si es coneixen dues de les magnituds, es pot obtenir la tercera mitjançant un model de geoide adequat.

![Relació entre l'altura el·lipsoidal, l'altura ortomètrica i l'ondulació del geoide]({{ site.baseurl }}/assets/img/coordinate-systems/ellipsoidal-orthometric-geoid-height.svg "La figura diferencia l'altura el·lipsoidal h, l'altura ortomètrica H i l'ondulació del geoide N. Original de Javiersanp, «Altitudes.svg», Wikimedia Commons, CC BY-SA 4.0 i altres llicències compatibles."){: data-figure-width="36rem"}

En alguns països i sistemes verticals s'utilitzen altures normals i quasi-geoides en lloc d'altures ortomètriques i geoides estrictes. El curs no necessita desenvolupar ara aquesta distinció, però sí conservar la idea principal: la coordenada horitzontal i l'altura poden dependre de superfícies i models diferents. Per això, quan es combinen punts GNSS, models digitals d'elevacions, capes municipals i mapes topogràfics, cal revisar tant el sistema de referència horitzontal com la referència vertical.

### Dàtum i marc de referència

Les coordenades només tenen sentit quan es coneix respecte de quin model i marc s'han definit. El **dàtum geodèsic** defineix com l'el·lipsoide i el sistema de coordenades es relacionen amb la Terra: origen, orientació, escala, el·lipsoide adoptat i, segons el cas, convencions de mesura i època. El **marc de referència** materialitza aquest dàtum amb una xarxa de punts, coordenades, observacions i procediments que permeten obtenir posicions consistents. En sistemes moderns, el marc també ha de tenir en compte que les plaques tectòniques es mouen i que les coordenades poden estar associades a una època.

També hi ha dàtums verticals. Un dàtum horitzontal permet expressar posicions en latitud, longitud o coordenades projectades; un dàtum vertical defineix de què depèn l'altura. En termes docents, l'el·lipsoide resol sobretot el problema geomètric de situar punts sobre una superfície regular, mentre que el geoide i els models gravimètrics resolen el problema físic de comparar altures. Aquesta separació no és absoluta, però ajuda a entendre per què el treball amb capes pot necessitar informació diferent per a planta i per a elevació.

El **sistema de referència espacial** estableix com s'expressen i s'interpreten les posicions. Quan aquestes posicions es projecten sobre un pla, les coordenades passen a tenir unitats i propietats adequades per a determinades operacions. Per exemple, `ETRS89 / UTM zona 31N` (`EPSG:25831`) combina un marc geodèsic europeu amb una projecció UTM concreta; `ED50 / UTM zona 31N` utilitza una projecció semblant, però un dàtum diferent. Aquesta diferència és suficient per produir desplaçaments apreciables si una capa s'assigna o es transforma malament.

Aquesta cadena explica per què dos parells de nombres no es poden comparar només per l'aparença. Una posició sense sistema de referència és incompleta, i un codi EPSG sense entendre les unitats i l'àrea d'ús tampoc no garanteix una operació correcta.

## Localitzar i mesurar

### Coordenades geogràfiques

La latitud i la longitud expressen posicions mitjançant unitats angulars. Valors com `1.1478406, 41.1026664` descriuen la posició de la Facultat de Turisme i Geografia amb l'ordre longitud–latitud. L'ordre no s'ha de deduir per intuïció: alguns formats i serveis utilitzen longitud–latitud, mentre que altres convencions mostren latitud–longitud.

>>>>> Aquesta fase aplica coordenades i projeccions a la localització, la comparació i la mesura de posicions territorials.
>>>>>
>>>>> - Localitzar posicions amb latitud i longitud a partir de meridians, paral·lels, hemisferis i ordre d'eixos.
>>>>> - Calcular antecs, periecs i antípodes normalitzant signes, hemisferis i longituds.
>>>>> - Interpretar coordenades UTM amb el fus, l'hemisferi, els eixos E/N, el fals est i les unitats mètriques.
>>>>> - Comparar projeccions conformes, equivalents i equidistants segons la propietat necessària per a la tasca.
>>>>> - Detectar mesures o posicions incoherents contrastant CRS, unitats, àrea d'ús i extensió.

![Dos globus mostren els paral·lels que determinen la latitud i els meridians que determinen la longitud]({{ site.baseurl }}/assets/img/coordinate-systems/latitude-longitude-earth.svg "La xarxa geogràfica permet expressar la latitud respecte de l'equador i la longitud respecte del meridià d'origen. Font: Djexplo, «Latitude and Longitude of the Earth», Wikimedia Commons, CC0 1.0.")

#### Localitzar coordenades sobre un mapamundi

Un mapamundi amb reticle permet practicar la lectura de coordenades abans d'entrar en un SIG. La tasca no consisteix a endevinar topònims, sinó a relacionar meridians, paral·lels, hemisferis i ordre d'eixos. En la xarxa geogràfica de la figura, els paral·lels i els meridians apareixen traçats a intervals angulars regulars: cada línia representa el mateix salt en graus que la línia veïna, encara que aquesta regularitat no equivalgui a distàncies terrestres idèntiques. Aquesta equidistància angular permet interpolar una posició entre dues línies i entendre el reticle com una xarxa de latituds i longituds.

Per orientar aquesta lectura cal reconèixer algunes línies principals. L'equador és el paral·lel de `0°` i separa l'hemisferi nord de l'hemisferi sud. El meridià de Greenwich és el meridià de `0°` i serveix d'origen per comptar les longituds cap a l'est i cap a l'oest. A l'altra banda del globus, l'antimeridià correspon a `180°` i marca el límit on les longituds est i oest es troben. Si el mapa no etiqueta totes les línies, primer cal localitzar aquests eixos de referència i després deduir l'interval del reticle. En els exemples següents les xifres s'interpreten com a graus decimals; si una font utilitza graus i minuts, els minuts han d'estar entre `0'` i `59'`.

::: subfigures a+b "Lectura de coordenades geogràfiques sobre un mapamundi. La subfigura a funciona com a mapa mut per localitzar punts a partir del reticle; la subfigura b mostra una solució amb les línies numerades i els punts identificats. Projecció Robinson. Llicència: pendent de revisar."
![Mapamundi mut amb reticle de meridians i paral·lels per practicar la localització de coordenades]({{ site.baseurl }}/assets/img/coordinate-systems/geolocation-exercise-world-map.png "Mapa mut per localitzar coordenades geogràfiques")
![Mapamundi amb reticle numerat i sis punts resolts sobre Califòrnia, Alaska, Kamtxatka, el Japó i Hawaii]({{ site.baseurl }}/assets/img/coordinate-systems/geolocation-exercise-world-map-solved.png "Mapa resolt amb punts de coordenades localitzats")
:::

La versió resolta serveix per comprovar el procediment. Un punt com `122,47° O · 37,84° N` cau a Califòrnia, a l'entorn de la badia de San Francisco; `149,54° O · 61,13° N` cau a Alaska, prop d'Anchorage; `158,58° E · 52,83° N` situa la península de Kamtxatka; `139,81° E · 35,64° N` correspon a l'àrea de Tòquio; i `155,60° O · 19,53° N` situa l'illa de Hawaii. Aquesta comprovació és aproximada perquè el mapa és petit i el reticle és general, però obliga a fer explícits hemisferi, longitud i latitud abans de donar un lloc per bo.

#### Antípodes, antecs i periecs

El mateix sistema angular permet calcular punts relacionats geomètricament. L'**antípoda** d'un lloc és el punt oposat del globus: canvia l'hemisferi de la latitud i desplaça la longitud 180°. El punt **antec** conserva la longitud i canvia només l'hemisferi de la latitud; queda al mateix meridià, però a l'altra banda de l'equador. El punt **periec** conserva la latitud i desplaça la longitud 180°; queda al mateix paral·lel, però a l'altra banda del globus.

![Esquema didàctic dels punts antec, periec i antípoda respecte d'una posició inicial sobre el globus]({{ site.baseurl }}/assets/img/coordinate-systems/antipodes-antec-periec.png "Relació entre antecs, periecs i antípodes. Llicència: pendent de revisar."){: data-figure-width="22rem"}

Per calcular aquests punts amb coordenades, la latitud només canvia de signe: `40° N` passa a `40° S`, i `26° S` passa a `26° N`. La longitud oposada s'obté sumant o restant `180°` i normalitzant el resultat dins de l'interval `180° O` a `180° E`; en notació est-oest, això equival a canviar d'hemisferi longitudinal i restar la longitud inicial a `180°`.

Per comprovar el procediment sobre un mapa, es pot utilitzar aquest [mapa interactiu d'antípodes, antecs i periecs](https://www.herramientas-online.com/antipodes/mapa-antipodas.php). Permet seleccionar un punt, alternar entre els tres càlculs i veure les coordenades resultants sobre un segon mapa. És una bona ajuda per detectar errors de signe o d'hemisferi, però el resultat s'ha de poder explicar igualment amb la regla de latitud i longitud anterior.

::: table "Exemples de càlcul d'antecs, periecs i antípodes"
| Punt inicial | Antec | Periec | Antípoda |
| --- | --- | --- | --- |
| `40° N · 37° O` | `40° S · 37° O` | `40° N · 143° E` | `40° S · 143° E` |
| `40° N · 1° E` | `40° S · 1° E` | `40° N · 179° O` | `40° S · 179° O` |
| `49° S · 69° E` | `49° N · 69° E` | `49° S · 111° O` | `49° N · 111° O` |
| `26° S · 80° O` | `26° N · 80° O` | `26° S · 100° E` | `26° N · 100° E` |
:::

### Reticle UTM i coordenades projectades

Els sistemes projectats transformen la superfície terrestre en un pla i permeten treballar habitualment amb unitats mètriques. El [sistema UTM](https://www.usgs.gov/faqs/what-does-term-utm-mean-utm-better-or-more-accurate-latitudelongitude) divideix el món, entre 80° S i 84° N, en seixanta fusos longitudinals de 6°. Els mapes generals del reticle també mostren bandes latitudinals de 8° que s'utilitzen en referències de quadrícula: Catalunya queda al fus 31 i a la banda T. Per això una referència MGRS catalana pot començar per `31T`, com en les [quadrícules UTM de l'ICGC](https://www.icgc.cat/es/Geoinformacion-y-mapas/Datos-y-productos/Geoinformacion-cartografica/Cuadriculas-UTM). En canvi, quan parlem del CRS `ETRS89 / UTM zona 31N` ([`EPSG:25831`](https://epsg.org/crs_25831/ETRS89-UTM-zone-31N.html)), la `N` indica l'hemisferi nord, no la banda latitudinal. En aquest sistema, els eixos són **est** (*easting*, E) i **nord** (*northing*, N), en aquest ordre, i la unitat és el metre {% cite icgcQuadriculesUtmEspecificacions2026 %}.

La coordenada UTM necessita més informació que els dos nombres. `ETRS89 / UTM zona 31N · EPSG:25831 · E 344.469 m · N 4.551.807 m` identifica el CRS, el fus i l'hemisferi, la component est i la component nord de la Facultat. El meridià central del fus 31, 3° E, rep un **fals est** de 500.000 m; per això una E inferior a 500.000 situa el punt a l'oest del meridià central sense emprar valors negatius. A l'hemisferi nord, la N es compta des de l'equador amb un fals nord de 0 m. Escriure només `344469, 4551807` deixaria oberta la zona, l'hemisferi, el dàtum i fins i tot l'ordre dels eixos.

Quan la mateixa lògica s'aplica a una quadrícula, el parell E/N ja no descriu necessàriament un punt d'interès, sinó el punt d'origen que dona nom a un quadrat. Les especificacions de les quadrícules UTM de l'ICGC creen polígons d'1 km o 10 km a partir d'un origen UTM ETRS89 i els assignen una [nomenclatura MGRS](https://www.icgc.cat/es/Ayuda/Preguntas-frecuentes/Coordenadas-de-tipo-31TCG213911), per exemple `31T CG 61 13`. Això vol dir que el codi representa tota la cel·la de la quadrícula; la coordenada associada serveix per indexar-la i localitzar-ne la cantonada de referència, no per substituir el polígon per un punt central {% cite icgcQuadriculesUtmEspecificacions2026 %}.

::: subfigures a+b/c+d "Del reticle UTM global al reticle local de Vila-seca. La subfigura a mostra els fusos i bandes UTM del planeta; la subfigura b situa el fus 31 dins del CRS 31N; la subfigura c explica el funcionament intern del fus, amb meridià central, fals est i eixos E/N; la subfigura d aplica aquesta lectura a tres llocs de Vila-seca. Les subfigures b, c i d són esquemes propis basats en definicions EPSG i conversions executades amb PROJ 9.4.0."
![Reticle mundial de fusos UTM i bandes latitudinals; Catalunya se situa al fus 31 i a la banda T, mentre que EPSG:25831 usa 31N per indicar el fus 31 de l'hemisferi nord]({{ site.baseurl }}/assets/img/coordinate-systems/utm-zones-world.jpg "Fusos longitudinals i bandes latitudinals del reticle UTM. Font: Jan Krymmel, Wikimedia Commons, a partir de NASA Visible Earth; domini públic, CC BY-SA 3.0 i GFDL.")
![Fus UTM 31 dins del CRS 31N, entre els meridians 0° E i 6° E, amb el meridià central a 3° E i Vila-seca situada a l'oest d'aquest meridià]({{ site.baseurl }}/assets/img/coordinate-systems/utm-zone-31n.svg "El fus 31 és una franja de 6° de longitud; dins del CRS 31N, la N indica l'hemisferi nord. El meridià central rep E = 500.000 m i permet interpretar per què Vila-seca té una coordenada est inferior a 500.000 m. Figura d'elaboració pròpia, 14 d'agost de 2026.")
![Esquema del funcionament intern d'un fus UTM: límits longitudinals, meridià central, fals est, coordenada est i coordenada nord]({{ site.baseurl }}/assets/img/coordinate-systems/utm-zone-internal-coordinates.svg "Dins d'un fus UTM, les coordenades són metres sobre un sistema cartesià local: E augmenta cap a l'est, N cap al nord i el fals est de 500.000 m evita valors negatius a prop del meridià central. Esquema didàctic d'elaboració pròpia, no a escala respecte de la deformació UTM, 14 d'agost de 2026.")
![Reticle UTM quilomètric amb tres llocs reals de Vila-seca i les seves coordenades est i nord]({{ site.baseurl }}/assets/img/coordinate-systems/utm-grid-vila-seca.svg "El reticle es llegeix primer cap a l'est i després cap al nord; a l'hemisferi nord, el valor N es compta des de l'equador")
:::

::: table "Tres llocs de Vila-seca en coordenades geogràfiques i UTM"
| Lloc | Longitud, latitud (`EPSG:4326`) | UTM ETRS89 / zona 31N (`EPSG:25831`) |
| --- | --- | --- |
| Facultat de Turisme i Geografia | `1.1478406, 41.1026664` | `zona 31N · E 344469 m · N 4551807 m` |
| Castell de Vila-seca | `1.1475084, 41.1146813` | `zona 31N · E 344469 m · N 4553142 m` |
| Torre d'en Dolça | `1.1599211, 41.0989127` | `zona 31N · E 345474 m · N 4551369 m` |
:::

Les posicions geogràfiques de la taula provenen d'OpenStreetMap i s'han transformat amb PROJ 9.4.0; la pàgina de [drets d'autor i atribució d'OpenStreetMap](https://www.openstreetmap.org/copyright) n'estableix les condicions d'ús i l'atribució, però no verifica directament aquestes coordenades. Els resultats s'han arrodonit al metre i no representen un aixecament topogràfic. La lectura relativa és immediata: la Facultat i el Castell tenen gairebé la mateixa E, però el Castell és aproximadament 1,3 km més al nord; la Torre d'en Dolça queda aproximadament 1 km més a l'est de tots dos. En un reticle d'1 km, la [lectura de coordenades UTM](https://www.usgs.gov/faqs/how-are-utm-coordinates-measured-usgs-topographic-maps) comença identificant la línia d'est situada a l'esquerra del punt i després la línia de nord situada per sota; els dígits addicionals precisen la posició dins del quadrat.

>>>> **Un parell de coordenades no identifica per si sol un lloc.** Interpretar metres com si fossin graus, invertir els eixos o assignar un EPSG només perquè la capa aparegui prop del territori esperat pot ocultar l'error. Primer s'han de revisar la font, les unitats, l'ordre dels eixos i l'extensió; després es decideix l'operació adequada.

### Projeccions i distorsions

Una **projecció cartogràfica** transforma matemàticament posicions d'una superfície corba per representar-les sobre un pla. Cap projecció conserva alhora formes, àrees, distàncies i direccions. La selecció depèn del territori, l'escala i l'operació prevista.

Una manera clàssica d'introduir les projeccions és imaginar una superfície auxiliar que rep la informació del globus i després es desplega: un **pla** en les projeccions azimutals o zenitals, un **con** en les projeccions còniques i un **cilindre** en les projeccions cilíndriques. Aquesta imatge ajuda a entendre per què una projecció pot ajustar-se millor a unes zones que a unes altres. Si la superfície toca el globus, parlem d'una posició tangent; si el talla, de posició secant. També pot canviar l'orientació: normal, transversa o obliqua, segons quin eix o franja del territori es vulgui privilegiar.

![Esquema de tres superfícies auxiliars de projecció: un pla azimutal o zenital, un con i un cilindre al voltant del globus]({{ site.baseurl }}/assets/img/coordinate-systems/projection-surfaces.svg "Les projeccions azimutals projecten sobre un pla, les còniques sobre un con i les cilíndriques sobre un cilindre. La superfície pot ser tangent o secant i pot orientar-se de manera normal, transversa o obliqua. És un esquema de famílies de projecció, no una projecció òptica literal: moltes projeccions reals es defineixen directament amb fórmules. Elaboració pròpia inspirada en el repertori docent clàssic de projeccions."){: data-figure-width="54rem"}

L'esquema no s'ha de llegir com si totes les projeccions fossin una projecció òptica literal. Moltes projeccions cartogràfiques es defineixen directament amb fórmules, i algunes combinen o modifiquen aquestes famílies bàsiques. La utilitat de la classificació és donar una intuïció inicial: la distorsió tendeix a ser menor a prop de les línies o punts de contacte i creix quan el mapa s'allunya de la zona per a la qual ha estat pensat.

Projecció conforme
: Preserva localment els angles i, per tant, les formes petites, però no conserva necessàriament les àrees.

Projecció equivalent
: Conserva les proporcions d'àrea, una propietat especialment rellevant quan la superfície de les regions participa en la lectura del mapa.

Projecció equidistant
: Conserva determinades distàncies definides pel disseny de la projecció, però no totes les distàncies possibles del mapa.

Les **indicatrius de Tissot** parteixen de cercles iguals i molt petits sobre la superfície terrestre i mostren com els transforma una projecció. En la projecció conforme de Mercator continuen sent circulars, però augmenten d'àrea cap als pols. En la projecció equivalent de Mollweide conserven l'àrea relativa i canvien de forma. La comparació permet observar que conservar una propietat implica deformar-ne d'altres.

::: subfigures a+b "Indicatrius de Tissot en una projecció conforme i una d'equivalent. Figures originals sense modificar de Justin Kunimune, amb costa de Natural Earth; Wikimedia Commons, CC BY-SA 4.0."
![En el mapamundi de Mercator, les indicatrius són circulars i augmenten de mida cap als pols]({{ site.baseurl }}/assets/img/coordinate-systems/mercator-tissot.svg "Mercator conserva localment els angles, però deforma les àrees")
![En el mapamundi de Mollweide, les indicatrius mantenen l'àrea i es deformen en forma d'el·lipse]({{ site.baseurl }}/assets/img/coordinate-systems/mollweide-tissot.svg "Mollweide conserva les àrees, però deforma les formes")
:::

Els dos mapes es poden consultar a les fitxes de Wikimedia Commons de [Mercator](https://commons.wikimedia.org/wiki/File:Mercator_with_Tissot%27s_Indicatrices_of_Distortion.svg) i [Mollweide](https://commons.wikimedia.org/wiki/File:Mollweide_with_Tissot%27s_Indicatrices_of_Distortion.svg), i es distribueixen sota la llicència [Creative Commons Reconeixement-CompartirIgual 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.ca).

No cal memoritzar una galeria extensa de projeccions. La comparació d'una projecció conforme, una d'equivalent i la Mercator transversa que estructura UTM permet formular una pregunta més útil: quina propietat cal preservar per a l'operació prevista? Localitzar municipis, mesurar distàncies, calcular superfícies o construir un mapa regional no imposen exactament les mateixes condicions.

Una capa pot semblar ben situada i, tanmateix, no ser adequada per calcular àrees o distàncies. La comprovació ha d'incloure el sistema de referència, les unitats i l'àrea d'ús, no només la coincidència visual amb un mapa de fons.

### Explorar com es construeix una projecció

El [GITTA Map Projector](https://gevian.github.io/GITTA-MP/) de Magnus Heitzler permet passar d'una definició abstracta a una construcció manipulable. El mode **Advanced** separa la superfície de projecció, la seva orientació, el centre de projecció i les capes de fronteres, retícula i indicatrius de Tissot. També permet aplanar un cilindre o un con i observar com una funció d'escalat modifica el resultat. El recurs va ser desenvolupat per a la plataforma GITTA a l'ETH Zürich i el [repositori original](https://github.com/gevian/GITTA-MP) es distribueix sota GPL v3.

![Mode avançat del GITTA Map Projector amb una projecció de Mercator aplanada, la funció d'escalat i les indicatrius de Tissot]({{ site.baseurl }}/assets/img/coordinate-systems/gitta-map-projector-mercator-advanced-2026-08-12.png "Construcció de Mercator a partir d'una projecció cilíndrica central aplanada i escalada. S'hi mostren fronteres, retícula, indicatrius de Tissot, paràmetres geomètrics i funció d'escalat. Captura pròpia del mode Advanced, 12 d'agost de 2026. GITTA Map Projector, Magnus Heitzler, Institute of Cartography and Geoinformation, ETH Zürich, 2019, GPL v3."){: data-figure-width="54rem"}

Una exploració breu pot començar a **Projection Surfaces** per construir un pla, un con i un cilindre; continuar a **Map Distortion Basics** activant les indicatrius; i acabar a **The Mercator Projection** amb la seqüència **Central Cylindrical Projection**, **flatten** i **Scale Central Cylindrical to Mercator**. El model ajuda a entendre propietats i transformacions, però no implica que totes les projeccions cartogràfiques siguin projeccions geomètriques de llum sobre una superfície: moltes es defineixen directament mitjançant fórmules.

### Les projeccions ens enganyen?

Una projecció no és una fotografia defectuosa del globus, sinó una transformació matemàtica. Com que una superfície corba no es pot desplegar sobre un pla sense deformar-la, qualsevol mapamundi altera les àrees, les formes, les distàncies o les direccions. La distorsió és inevitable i es pot mesurar; el problema comunicatiu apareix quan s'utilitza una projecció inadequada per a la pregunta o s'oculten les propietats que no conserva {% cite snyderMapProjections1987 %}.

Mercator va presentar el 1569 una projecció destinada explícitament a la navegació. És conforme: conserva els angles locals i converteix les **loxodròmies**, els trajectes de rumb constant, en rectes. Aquesta propietat facilitava traçar rumbs de brúixola, encara que una loxodròmia no sigui generalment la ruta més curta. El cost és que l'escala i les àrees augmenten ràpidament amb la latitud i els pols no es poden representar; per això Mercator no és adequada per comparar la superfície de països o continents en un mapamundi {% cite snyderMapProjections1987 %}.

La projecció coneguda com a **Gall-Peters** respon a un altre propòsit. James Gall ja havia presentat el 1855 una construcció matemàticament equivalent i la va publicar el 1885; Arno Peters la va popularitzar a partir de 1973 com una alternativa més equitativa als mapamundis de Mercator. Gall-Peters és una [projecció cilíndrica equivalent](https://proj.org/en/stable/operations/projections/cea.html): un territori que té el doble d'àrea que un altre ocupa el doble de superfície al mapa. No elimina la distorsió, sinó que la redistribueix: deforma les formes, els angles, les distàncies i les direccions, amb escala correcta als paral·lels de 45° N i 45° S {% cite gallCylindricalProjections1885 robinsonArnoPeters1985 %}.

L'eina [*The True Size Of…*](https://thetruesize.com/) permet cercar un país i arrossegar-ne el contorn per diferents latituds sobre un fons Mercator. El territori no canvia d'àrea real durant el desplaçament, però la mida necessària per encaixar amb el mapa varia: Groenlàndia deixa de semblar comparable amb Àfrica quan s'acosta a l'equador. L'activitat fa visible el patró de distorsió, però no converteix el fons del visor en una superfície adequada per mesurar; serveix per formular una comparació que després es pot contrastar amb dades d'àrea.

![Captura de The True Size Of amb Groenlàndia seleccionada sobre un mapa Mercator]({{ site.baseurl }}/assets/img/coordinate-systems/the-true-size-greenland-mercator-2026-08-13.png "Captura pròpia de The True Size Of, 13 d'agost de 2026, amb Groenlàndia seleccionada sobre el mapa interactiu. Recurs creat per James Talmage i Damon Maneice; mapa base de Google. La funció docent és observar com el visor permet desplaçar un territori per comparar-ne l'àrea aparent en Mercator."){: data-figure-width="54rem"}

La campanya de Peters va assenyalar un efecte comunicatiu real: un mapamundi Mercator dona més pes visual a Europa i a altres territoris de latituds altes que a regions tropicals molt més extenses. Tanmateix, la fórmula amplia segons la latitud i ho fa simètricament als dos hemisferis; no codifica continents, pobles ni un meridià central concret. Analitzar l'eurocentrisme o el llegat colonial d'un mapa exigeix estudiar també qui el produeix, quina projecció i centrament escull, on talla el món, quina orientació adopta, quines fronteres i topònims mostra i en quin context circula {% cite harleyDeconstructingMap1989 monmonierHowLieMaps2018 %}.

>>>> **Mercator no és «falsa» i Gall-Peters no és «la realitat».** Mercator és útil per a determinats problemes de navegació i inadequada per comparar àrees globals; Gall-Peters conserva les àrees, però ofereix formes molt deformades. Tampoc no és l'única projecció equivalent. La pregunta cartogràfica no és quina projecció és universalment millor, sinó quina propietat necessita conservar el mapa, quines distorsions pot assumir i com les farà comprensibles al lector.

## Sistemes de referència espacial

### Identificadors EPSG

Un codi EPSG és un identificador curt per referir-se a una definició geodèsica llarga. L'acrònim prové de l'antic **European Petroleum Survey Group**; avui el conjunt de dades EPSG és publicat a [epsg.org](https://epsg.org/) i mantingut per la subcomissió de geodèsia del comitè de geomàtica de l'IOGP. En la pràctica, el registre funciona com un vocabulari tècnic compartit: en lloc d'escriure cada vegada el dàtum, l'el·lipsoide, la projecció, les unitats, els eixos i l'àrea d'ús, molts programes poden identificar aquesta definició mitjançant un número.

A QGIS, seleccionar el CRS d'una capa o del projecte sovint vol dir triar una d'aquestes definicions. `EPSG:4326` identifica el sistema geogràfic WGS 84, expressat habitualment en longitud i latitud en graus. `EPSG:25831` identifica `ETRS89 / UTM zona 31N`, un sistema projectat en metres adequat per al treball regional a Catalunya. La diferència no és cosmètica: si una taula amb longituds i latituds en graus s'importa com si fossin metres UTM, o si una capa UTM es declara com a WGS 84, QGIS pot situar els punts en un lloc absurd o permetre mesures que semblen precises però no tenen sentit.

El codi facilita l'intercanvi i evita moltes ambigüitats, però no substitueix la lectura crítica de la font. Abans d'acceptar un EPSG cal comprovar que el nom del CRS, les unitats, l'ordre dels eixos, l'àrea d'ús i l'operació prevista concorden amb les coordenades disponibles. Configurar bé QGIS no consisteix a trobar un número que faci encaixar visualment una capa, sinó a declarar el sistema real de les coordenades i, si cal, transformar-les després amb una reprojecció documentada.

>>>>> Aquesta fase converteix la definició d'un sistema de referència espacial en decisions explícites sobre capes, projectes i transformacions.
>>>>>
>>>>> - Interpretar un identificador EPSG a partir del dàtum, la projecció, els eixos, les unitats i l'àrea d'ús.
>>>>> - Contrastar `EPSG:4326`, `EPSG:25831` i un CRS ED50 segons les coordenades i el territori que descriuen.
>>>>> - Assignar un CRS només quan les coordenades ja pertanyen al sistema conegut i en falta la definició correcta.
>>>>> - Reprojectar una geometria quan cal calcular coordenades noves en un CRS de destinació justificat.
>>>>> - Verificar per separat el CRS de cada capa, el CRS del projecte i el CRS del fitxer exportat.

### Assignar i reprojeccionar

Assignar un sistema indica com s'han d'interpretar unes coordenades; reprojeccionar transforma la geometria. Confondre aquestes operacions pot produir capes aparentment encaixades però tècnicament incorrectes.

#### Assignar un sistema de referència

L'assignació modifica la descripció de les coordenades, no els nombres que formen la geometria. Només és adequada quan el sistema correcte es coneix per la font o per documentació fiable i la capa l'ha perdut o el declara erròniament. No s'ha d'utilitzar com un procediment de prova fins que la capa coincideixi visualment.

#### Reprojectar una geometria

La reprojecció calcula coordenades noves que representen les mateixes posicions en un altre sistema. És adequada quan el sistema d'origen està ben definit i cal obtenir una capa de treball amb un altre CRS. La capa original s'ha de preservar, i el fitxer derivat ha d'identificar el sistema de destinació.

#### Reprojecció al vol

El programari cartogràfic pot mostrar conjuntament capes amb sistemes diferents mitjançant una transformació temporal de visualització. Aquesta capacitat facilita l'exploració, però no canvia els fitxers d'origen ni resol automàticament quin sistema convé per mesurar o exportar. El sistema de referència del projecte i el de cada capa s'han de revisar explícitament.

### Escala de treball

Els mapes municipals, comarcals i regionals requereixen nivells de detall i fonts cartogràfiques diferents. La capa més detallada no és sempre la més adequada: pot alentir el projecte i introduir formes impossibles de percebre a la mida final.

## Models de dades espacials

### Vector i ràster

El model vectorial representa entitats diferenciables mitjançant geometries i atributs. És adequat per a municipis, allotjaments, carreteres o itineraris. El model ràster divideix l'espai en cel·les i és habitual en ortofotos, models d'elevació, temperatura o cobertes derivades d'imatges. La resolució de la cel·la condiciona el detall observable i les operacions possibles.

El projecte comarcal utilitza polígons vectorials perquè cada municipi necessita una geometria vinculada a un codi i a una fila d'indicadors. Les ortofotos o altres ràsters poden aportar context, però no substitueixen els límits administratius necessaris per a la unió.

### Punts, línies i polígons

Els models vectorials representen objectes geogràfics mitjançant geometries. Un allotjament es pot representar com un punt; una ruta, com una línia; i un municipi, com un polígon. El tipus ha de correspondre al fenomen i a l'escala: convertir qualsevol objecte en un punt o una àrea pot ocultar propietats rellevants.

### Geometria i atributs

Cada entitat espacial combina una forma i un registre alfanumèric. Aquesta relació serà la base de les taules d'atributs i de les unions del capítol de SIG.

Una entitat municipal pot estar formada per una geometria multipart si inclou fragments territorials separats. També pot contenir errors geomètrics o un nivell de detall inadequat per a l'escala del mapa. La validesa de la forma, la presència d'un identificador i la data territorial són controls diferents: una geometria pot ser tècnicament vàlida i, alhora, correspondre a una delimitació antiga.

## Activitat: preparar la base espacial de la comarca

L'activitat prepara una base espacial municipal fiable per continuar el projecte: abans de representar indicadors, cal comprovar la procedència, la geometria, els codis territorials i el sistema de referència de la capa, i distingir una assignació de CRS d'una reprojecció.

>>>>> L'activitat produeix una base municipal traçable i validada que es conservarà en el projecte QGIS dels capítols següents.
>>>>>
>>>>> - Documentar al `README.md` la procedència, la data territorial, la llicència, la geometria, els camps clau i el CRS de la font municipal.
>>>>> - Inspeccionar a QGIS l'esquema, l'extensió, les unitats, el nombre d'entitats i almenys un municipi conegut.
>>>>> - Seleccionar la comarca amb una clau territorial documentada i comprovar la presència i la unicitat dels codis municipals.
>>>>> - Diagnosticar el desplaçament ED50–ETRS89 i justificar si correspon assignar informació absent o reprojeccionar coordenades definides.
>>>>> - Desar, quan calgui, `data/processed/municipis_tarragones_epsg25831.gpkg` en `EPSG:25831` sense modificar la font original.
>>>>> - Verificar geometria, CRS, extensió, recomptes, codis i ordres de magnitud abans de continuar el projecte.

### Materials i resultats de treball

Per al Tarragonès s'utilitzaran la capa oficial completa de límits municipals identificada al `README.md`, el projecte `qgis/tigit_tarragones.qgz` i, quan calgui filtrar o reprojeccionar, la capa derivada `data/processed/municipis_tarragones_epsg25831.gpkg`. La parella diagnòstica ED50/ETRS89 serà proporcionada pel professorat: no se'n pressuposen els noms de fitxer, però el `README.md` n'identificarà cada fitxer, el tipus de geometria i el CRS. Els noms territorials dels fitxers s'adaptaran a la comarca del projecte.

El mateix projecte QGIS continuarà als capítols següents. La font municipal oficial completa es conservarà sense modificacions dins del projecte i servirà per obtenir o derivar el context provincial; l'auditoria espacial i la diagnosi de CRS quedaran documentades al `README.md`.

### Documentar i carregar la font

La capa de límits municipals ha d'estar acompanyada del productor, l'URL de descàrrega, la data d'accés, la versió o data territorial, la llicència, el nivell de detall i el sistema de referència. Ser oficial no elimina la necessitat de comprovar si la delimitació i l'escala són adequades per al projecte.

La capa municipal oficial de Catalunya permetrà identificar els municipis de la comarca seleccionada; el Tarragonès serà el cas de demostració. Encara no s'hi representaran els indicadors: primer es comprovaran la font, la data, el codi municipal, la geometria i el sistema de referència.

### Inspeccionar l'esquema i l'extensió

La inspecció inicial registrarà el tipus de geometria, el nombre d'entitats, els noms i tipus dels camps, el CRS, les unitats i l'extensió de coordenades. També es verificarà manualment almenys un municipi conegut. Una capa carregada sense avisos no es considera validada fins que aquests elements siguin coherents.

### Identificar la comarca i la clau municipal

La selecció de la comarca s'ha de basar en un codi o camp territorial documentat. Cal comptar els municipis seleccionats, comprovar que els identificadors municipals són presents i revisar si són únics. La llista obtinguda es contrastarà amb els codis territorials preservats al llibre del capítol 1.

### Diagnosticar desplaçaments i mesures incoherents

Quan una capa apareix lluny del territori esperat o produeix mesures inversemblants, es revisaran coordenades, ordre X/Y, unitats i EPSG abans de modificar-la.

Una pràctica de diagnosi combinarà deliberadament una capa antiga en ED50 / UTM 31N amb una capa actual en ETRS89 / UTM 31N. Caldrà identificar els sistemes, explicar el desplaçament i decidir si s'ha d'assignar informació que falta o reprojeccionar una geometria que ja està correctament definida.

La resolució haurà d'identificar els dos CRS, descriure el desplaçament observat, distingir si falta la definició o si les coordenades pertanyen realment a sistemes diferents, justificar l'assignació o la reprojecció i verificar el resultat després de l'operació. Fer coincidir les capes visualment sense conservar aquest raonament no completa la diagnosi.

### Preparar la capa de treball

Quan sigui necessari filtrar o reprojeccionar, la selecció del Tarragonès es desarà a la ubicació canònica `data/processed/municipis_tarragones_epsg25831.gpkg`. La font original continuarà a `data/raw`, i el projecte utilitzarà rutes relatives perquè la carpeta es pugui moure sense perdre les capes.

### Comprovacions de qualitat

Abans de continuar s'han de comprovar aquests punts:

1. l'extensió cobreix el territori esperat i les unitats concorden amb el CRS;
2. el nombre de municipis de la comarca és plausible i queda registrat;
3. el codi municipal és present i no conté duplicats inesperats;
4. la geometria és poligonal i adequada per representar unitats municipals;
5. almenys un municipi, una coordenada i una mesura tenen un ordre de magnitud coherent;
6. la data territorial, la font i la llicència es poden recuperar;
7. els fitxers originals no s'han sobreescrit.

### Evidències que s'han de conservar

::: table "Evidències de la preparació espacial"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/raw` | Capa municipal original | Fitxers complets sense modificar i documentació de procedència |
| `qgis` | `tigit_tarragones.qgz` | Font municipal oficial completa, context provincial que proporciona o se'n deriva, CRS, rutes relatives i selecció comprovada |
| `data/processed` | `municipis_tarragones_epsg25831.gpkg`, si cal | Municipis seleccionats, codi territorial preservat i `EPSG:25831` explícit |
| `README.md` | Auditoria de la capa | Productor, versió, llicència, geometria, entitats, camps clau, CRS, unitats i extensió |
| `README.md` | Diagnosi ED50–ETRS89 | Cada fitxer identificat amb nom, geometria i CRS; desplaçament, operació justificada i comprovació posterior |
:::
