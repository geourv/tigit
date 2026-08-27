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
>>>>> - Relacionar el model de la Terra, les coordenades, la projecció i el CRS que permeten situar i mesurar una dada.
>>>>> - Interpretar coordenades geogràfiques i UTM amb l'ordre dels eixos, les unitats i el sistema de referència corresponents.
>>>>> - Distingir l'assignació d'un CRS de la reprojecció i seleccionar una representació vectorial o ràster adequada al fenomen.
>>>>> - Preparar i validar una base espacial municipal a QGIS sense sobreescriure la font original.

## Forma terrestre, moviments i il·luminació solar

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

Per expressar una posició o una altura cal distingir la superfície física del planeta dels models regulars que permeten calcular-la.

>>>>> Aquesta fase diferencia els models físics i matemàtics que permeten expressar posicions i altures sobre la Terra.
>>>>>
>>>>> - Distingir la superfície real, el geoide, l'el·lipsoide i l'esferoide per la seva funció de referència.
>>>>> - Relacionar l'altura el·lipsoidal, l'altura ortomètrica i l'ondulació del geoide mitjançant $h = H + N$.
>>>>> - Explicar per què un el·lipsoide regional i un de global poden ajustar-se de manera diferent al territori.
>>>>> - Diferenciar un dàtum geodèsic del marc que el materialitza i de la referència vertical de les altures.

### Geoide, el·lipsoide i esferoide

La forma física de la Terra, el model matemàtic utilitzat per calcular coordenades i la superfície de referència de les altures no són exactament el mateix. Aquesta distinció és important perquè una capa pot estar ben situada en planta i, alhora, expressar l'altura amb una referència inadequada. En cartografia digital, aquests conceptes apareixen dins dels sistemes de referència, però no són simples codis: indiquen quina superfície s'ha triat per mesurar, projectar o comparar.

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

#### Vèrtexs geodèsics i control sobre el terreny

Un marc de referència no queda materialitzat només perquè existeixi una definició matemàtica. Calen estacions i senyals estables amb coordenades determinades mitjançant observacions, ajustos i controls comuns. Un **vèrtex geodèsic** és un d'aquests punts de control: pot adoptar la forma d'un pilar visible sobre un cim, una marca metàl·lica fixada a la roca o una estació GNSS permanent. En aquest context, *vèrtex* no significa un node qualsevol d'un polígon digital, sinó un punt físic documentat que forma part d'una xarxa geodèsica.

Històricament, els vèrtexs situats en llocs intervisibles permetien construir xarxes de triangulació: a partir d'una base i de mesures angulars es propagaven posicions sobre el territori. La topografia de detall s'hi podia enllaçar ocupant un punt conegut, orientant l'instrument cap a un altre i mesurant angles, distàncies i desnivells fins als elements locals. Avui les observacions GNSS, les estacions permanents i els serveis de correcció en temps real han reduït la dependència de la intervisibilitat, però no han eliminat el principi: un aixecament ha de quedar vinculat a un marc conegut i s'ha de poder comprovar amb punts de control {% cite vanSickleBasicGISCoordinates2017 %}.

::: subfigures a+b/c "Materialització de referències geodèsiques i verticals. La subfigura a situa un vèrtex geodèsic en un cim, on l'horitzó obert facilitava la intervisibilitat; la subfigura b mostra el detall d'una placa altimètrica referida al nivell mitjà del Mediterrani a Alacant; la subfigura c relaciona una xarxa de punts coneguts amb un aixecament topogràfic local. Les dues fotografies són exemples de llocs i senyals diferents: la placa altimètrica no és un detall del vèrtex de la primera imatge. El senyal físic no és el dàtum, sinó una materialització que permet usar i verificar una referència sobre el terreny."
![Vèrtex geodèsic de Cabeza Mediana situat en un cim de la serra de Guadarrama]({{ site.baseurl }}/assets/img/coordinate-systems/geodetic-vertex-cabeza-mediana.jpg "Vèrtex geodèsic de Cabeza Mediana, serra de Guadarrama. Fotografia de Miguel303xm, 14 de febrer de 2009; Wikimedia Commons, CC BY 3.0.")
![Placa altimètrica històrica d'Àvila amb una cota referida al nivell mitjà del Mediterrani a Alacant]({{ site.baseurl }}/assets/img/coordinate-systems/vertical-benchmark-avila.jpg "Placa de la Direcció General de l'Institut Geogràfic i Estadístic a Àvila. Fotografia de L. Vadillo - MaLéPhotoSpain, 15 de juny de 2022; Wikimedia Commons, CC BY-SA 4.0. Còpia redimensionada a 1280 píxels sense modificar-ne el contingut.")
![Esquema d'una xarxa geodèsica enllaçada amb un aixecament topogràfic local]({{ site.baseurl }}/assets/img/coordinate-systems/geodetic-reference-network.svg "Els punts de control comparteixen un marc, unes coordenades, una data i una qualitat conegudes. L'aixecament local transfereix aquesta referència a geometries de més detall. Esquema docent d'elaboració pròpia, 25 d'agost de 2026.")
:::

La [fotografia del vèrtex de Cabeza Mediana](https://commons.wikimedia.org/wiki/File:Cabeza_Mediana_cima.JPG) permet reconèixer el pilar dins del paisatge, mentre que la [placa altimètrica d'Àvila](https://commons.wikimedia.org/wiki/File:20220615_AVILA_06-1.jpg) fa explícites una cota i la superfície vertical de referència. La primera forma part d'una xarxa geodèsica; la segona conserva una referència d'altura en un edifici. Llegir-les conjuntament ajuda a distingir la posició d'un punt, la seva materialització física i el significat de l'altura indicada.

El [cercador de vèrtexs geodèsics REGENTE i ROI de l'IGN](https://www.ign.es/web/gds-vertices) permet consultar punts per nom, número, full MTN50, municipi o rang de coordenades. Per a cada vèrtex publica les coordenades geogràfiques i UTM, la data de compensació, les característiques físiques del pilar i una descripció de la situació. Aquesta fitxa és tan important com el monument: abans d'utilitzar un senyal cal comprovar la xarxa, el sistema de referència, la data, l'estat i la precisió, no limitar-se a trobar una estructura sobre el terreny.

També hi ha dàtums verticals. Un dàtum horitzontal permet expressar posicions en latitud, longitud o coordenades projectades; un dàtum vertical defineix de què depèn l'altura. En termes docents, l'el·lipsoide resol sobretot el problema geomètric de situar punts sobre una superfície regular, mentre que el geoide i els models gravimètrics resolen el problema físic de comparar altures. Aquesta separació no és absoluta, però ajuda a entendre per què el treball amb capes pot necessitar informació diferent per a planta i per a elevació.

El **sistema de referència espacial** estableix com s'expressen i s'interpreten les posicions. Quan aquestes posicions es projecten sobre un pla, les coordenades passen a tenir unitats i propietats adequades per a determinades operacions. Per exemple, `ETRS89 / UTM zona 31N` (`EPSG:25831`) combina un marc geodèsic europeu amb una projecció UTM concreta; `ED50 / UTM zona 31N` utilitza una projecció semblant, però un dàtum diferent. Aquesta diferència és suficient per produir desplaçaments apreciables si una capa s'assigna o es transforma malament.

Aquesta cadena explica per què dos parells de nombres no es poden comparar només per l'aparença. Una posició sense sistema de referència és incompleta, i un codi EPSG sense entendre les unitats i l'àrea d'ús tampoc no garanteix una operació correcta.

## Coordenades, projeccions i mesura territorial

Una posició només es pot interpretar i mesurar correctament quan se'n coneixen el tipus de coordenades, les unitats i la projecció.

>>>>> Aquesta fase aplica coordenades i projeccions a la localització, la comparació i la mesura de posicions territorials.
>>>>>
>>>>> - Localitzar posicions amb latitud i longitud a partir de meridians, paral·lels, hemisferis i ordre d'eixos.
>>>>> - Calcular antecs, periecs i antípodes normalitzant signes, hemisferis i longituds.
>>>>> - Interpretar coordenades UTM amb el fus, l'hemisferi, els eixos E/N, el fals est i les unitats mètriques.
>>>>> - Comparar projeccions conformes, equivalents i equidistants segons la propietat necessària per a la tasca.
>>>>> - Detectar mesures o posicions incoherents contrastant CRS, unitats, àrea d'ús i extensió.

### Coordenades geogràfiques

La latitud i la longitud expressen posicions mitjançant unitats angulars. Valors com `1.1478406, 41.1026664` descriuen la posició de la Facultat de Turisme i Geografia amb l'ordre longitud–latitud. L'ordre no s'ha de deduir per intuïció: alguns formats i serveis utilitzen longitud–latitud, mentre que altres convencions mostren latitud–longitud.

![Dos globus mostren els paral·lels que determinen la latitud i els meridians que determinen la longitud]({{ site.baseurl }}/assets/img/coordinate-systems/latitude-longitude-earth.svg "La xarxa geogràfica permet expressar la latitud respecte de l'equador i la longitud respecte del meridià d'origen. Font: Djexplo, «Latitude and Longitude of the Earth», Wikimedia Commons, CC0 1.0.")

#### Localitzar coordenades sobre un mapamundi

Un mapamundi amb reticle permet practicar la lectura de coordenades abans d'entrar en un SIG. La tasca no consisteix a endevinar topònims, sinó a relacionar meridians, paral·lels, hemisferis i ordre d'eixos. En la xarxa geogràfica de la figura, els paral·lels i els meridians apareixen traçats a intervals angulars regulars: cada línia representa el mateix salt en graus que la línia veïna, encara que aquesta regularitat no equivalgui a distàncies terrestres idèntiques. Aquesta equidistància angular permet interpolar una posició entre dues línies i entendre el reticle com una xarxa de latituds i longituds.

Per orientar aquesta lectura cal reconèixer algunes línies principals. L'equador és el paral·lel de `0°` i separa l'hemisferi nord de l'hemisferi sud. El meridià de Greenwich és el meridià de `0°` i serveix d'origen per comptar les longituds cap a l'est i cap a l'oest. A l'altra banda del globus, l'antimeridià correspon a `180°` i marca el límit on les longituds est i oest es troben. Si el mapa no etiqueta totes les línies, primer cal localitzar aquests eixos de referència i després deduir l'interval del reticle. En els exemples següents les xifres s'interpreten com a graus decimals; si una font utilitza graus i minuts, els minuts han d'estar entre `0'` i `59'`.

::: table "Coordenades que cal localitzar al mapamundi"
| Punt | Latitud | Longitud |
| --- | --- | --- |
| A | `50° N` | `120° O` |
| B | `60° N` | `140° O` |
| C | `60° N` | `170° E` |
| D | `40° N` | `140° E` |
| E | `20° N` | `160° O` |
| F | `20° N` | `160° E` |
:::

::: subfigures a/b "Lectura de coordenades geogràfiques sobre un mapamundi. La subfigura a funciona com a mapa mut: el reticle de 10° no està numerat i les posicions s'han de deduir des de l'equador, Greenwich i l'antimeridià. La subfigura b permet comprovar els sis punts. Projecció Robinson; elaboració pròpia a partir de la base mundial del conjunt `maps`."
![Mapamundi mut amb reticle de 10° sense numeració i amb l'equador, Greenwich i l'antimeridià reforçats]({{ site.baseurl }}/assets/img/coordinate-systems/geolocation-exercise-world-map.svg "Mapa mut per localitzar les coordenades A–F a partir dels eixos geogràfics principals.")
![Mapamundi resolt amb els sis punts A–F situats sobre el mateix reticle sense numeració]({{ site.baseurl }}/assets/img/coordinate-systems/geolocation-exercise-world-map-solved.svg "Solució de l'exercici de localització de coordenades geogràfiques.")
:::

La versió resolta serveix per comprovar el procediment, no per substituir-lo. Primer es compten els intervals de latitud des de l'equador i es decideix l'hemisferi nord o sud. Després es compten els intervals de longitud des de Greenwich cap a l'est o cap a l'oest. Per als punts propers a 180° resulta més curt comprovar la distància respecte de l'antimeridià: C, a `170° E`, queda un interval a l'oest del marge dret; E, a `160° O`, queda dos intervals a l'est del marge esquerre; i F, a `160° E`, queda dos intervals a l'oest del marge dret. Aquesta doble comprovació ajuda a evitar que una longitud oriental es col·loqui per error al costat occidental del mapa.

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

#### Longitud, hora solar i hora civil

Els fusos horaris s'entenen millor després de la longitud geogràfica i abans de passar a les coordenades projectades. La Terra completa aproximadament una rotació de `360°` en 24 hores solars mitjanes: `15°` de longitud corresponen a una hora i `1°`, a uns quatre minuts. Per això el migdia solar mitjà no arriba simultàniament a dos llocs situats sobre meridians diferents. Aquesta relació geomètrica explica l'origen dels fusos, però no determina per si sola l'hora que marca el rellotge civil.

La coordinació de ferrocarrils, comunicacions i administracions va exigir substituir moltes hores locals per referències comunes. La Conferència Internacional del Meridià de 1884 va adoptar Greenwich com a origen de les longituds i va definir un dia universal de referència. El model teòric divideix el globus en 24 fusos d'uns `15°`, però els límits civils segueixen sovint fronteres i decisions polítiques, i els desplaçaments respecte d'UTC també poden ser de mitja hora o d'un quart d'hora. Compartir meridià no obliga a compartir hora oficial, i conèixer una longitud no basta per deduir-la {% cite planesasHoraOficialEspana2013 %}.

::: table "Quatre conceptes temporals que no s'han de confondre"
| Concepte | Què representa | Què cal conservar en unes dades |
| --- | --- | --- |
| Hora solar mitjana local | Posició temporal mitjana del Sol respecte del meridià del lloc | Longitud i criteri astronòmic utilitzat |
| UTC | Referència temporal coordinada global | Instant expressat en UTC, sovint amb `Z` |
| Desplaçament UTC | Diferència numèrica en un instant, com `+01:00` o `+02:00` | Data, hora i desplaçament explícit |
| Zona temporal civil | Conjunt històric de regles d'un territori, com `Europe/Madrid` | Identificador de zona i versió de les regles quan sigui rellevant |
:::

A Espanya, l'hora oficial peninsular i balear es va unificar amb la referència de Greenwich a partir de 1901, mentre que les Canàries mantenen una hora menys des de 1922. L'avanç decretat el març de 1940 no es va revertir i va deixar l'hora base peninsular en un desplaçament equivalent avui a UTC+1; quan s'aplica l'horari d'estiu, s'hi afegeix temporalment una altra hora. Planesas adverteix, però, que l'ordre de 1940 no va declarar formalment l'adopció d'un fus amb aquest nom i que la documentació no sosté explicacions simplificades com l'anomenada «hora alemanya». L'hora oficial és una convenció amb història, no una conseqüència automàtica del mapa.

En una base de dades, `2026-04-03T14:30:00+02:00` identifica un instant, però el desplaçament `+02:00` no explica per si sol totes les regles passades o futures del territori. Si cal convertir reserves, arribades, mobilitat o observacions entre llocs i dates, convé conservar l'instant en UTC i també la zona temporal civil d'origen. Així es poden tractar els canvis estacionals i històrics sense deduir-los només de la coordenada.

>> **Lectura recomanada.** [*La hora oficial en España y sus cambios*](https://astronomia.ign.es/rknowsys-theme/images/webAstro/paginas/documentos/Anuario/lahoraoficialenespana.pdf), de Pere Planesas, documenta la formació dels fusos, la unificació horària espanyola i els canvis legals des de 1901. El PDF oficial incorpora també una actualització de gener de 2017 {% cite planesasHoraOficialEspana2013 %}.

### Reticle UTM i coordenades projectades

Els sistemes projectats transformen la superfície terrestre en un pla i permeten treballar habitualment amb unitats mètriques. El [sistema UTM](https://www.usgs.gov/faqs/what-does-term-utm-mean-utm-better-or-more-accurate-latitudelongitude) divideix el món, entre 80° S i 84° N, en seixanta fusos longitudinals de 6°. Els mapes generals del reticle també mostren bandes latitudinals de 8° que s'utilitzen en referències de quadrícula: Catalunya queda al fus 31 i a la banda T. Per això una referència MGRS catalana pot començar per `31T`, com en les [quadrícules UTM de l'ICGC](https://www.icgc.cat/es/Geoinformacion-y-mapas/Datos-y-productos/Geoinformacion-cartografica/Cuadriculas-UTM). En canvi, quan parlem del CRS `ETRS89 / UTM zona 31N` ([`EPSG:25831`](https://epsg.org/crs_25831/ETRS89-UTM-zone-31N.html)), la `N` indica l'hemisferi nord, no la banda latitudinal. En aquest sistema, els eixos són **est** (*easting*, E) i **nord** (*northing*, N), en aquest ordre, i la unitat és el metre {% cite icgcQuadriculesUtmEspecificacions2026 %}.

La coordenada UTM necessita més informació que els dos nombres. `ETRS89 / UTM zona 31N · EPSG:25831 · E 344.469 m · N 4.551.807 m` identifica el CRS, el fus i l'hemisferi, la component est i la component nord de la Facultat. El meridià central del fus 31, 3° E, rep un **fals est** de 500.000 m; per això una E inferior a 500.000 situa el punt a l'oest del meridià central sense emprar valors negatius. A l'hemisferi nord, la N es compta des de l'equador amb un fals nord de 0 m. Escriure només `344469, 4551807` deixaria oberta la zona, l'hemisferi, el dàtum i fins i tot l'ordre dels eixos.

Quan la mateixa lògica s'aplica a una quadrícula, el parell E/N ja no descriu necessàriament un punt d'interès, sinó el punt d'origen que dona nom a un quadrat. Les especificacions de les quadrícules UTM de l'ICGC creen polígons d'1 km o 10 km a partir d'un origen UTM ETRS89 i els assignen una [nomenclatura MGRS](https://www.icgc.cat/es/Ayuda/Preguntas-frecuentes/Coordenadas-de-tipo-31TCG213911), per exemple `31T CG 61 13`. Això vol dir que el codi representa tota la cel·la de la quadrícula; la coordenada associada serveix per indexar-la i localitzar-ne la cantonada de referència, no per substituir el polígon per un punt central {% cite icgcQuadriculesUtmEspecificacions2026 %}.

::: subfigures a+b/c+d "Del reticle UTM global al reticle local de Vila-seca. La subfigura a mostra els fusos i bandes UTM del planeta; la subfigura b segueix el fus 31N des de l'equador fins al límit de 84° N i hi situa Vila-seca; la subfigura c mostra com l'equador i el fals est del meridià central originen les coordenades N i E; la subfigura d amplia un reticle quilomètric local i manté explícit l'equador com a origen de N, tot i que queda fora del mapa. Les subfigures b, c i d són esquemes propis basats en definicions EPSG i transformacions de coordenades."
![Reticle mundial de fusos UTM i bandes latitudinals; Catalunya se situa al fus 31 i a la banda T, mentre que EPSG:25831 usa 31N per indicar el fus 31 de l'hemisferi nord]({{ site.baseurl }}/assets/img/coordinate-systems/utm-zones-world.jpg "Fusos longitudinals i bandes latitudinals del reticle UTM. Font: Jan Krymmel, Wikimedia Commons, a partir de NASA Visible Earth; domini públic, CC BY-SA 3.0 i GFDL.")
![Fus UTM 31N entre l'equador i 84° N, delimitat pels meridians 0° E i 6° E, amb Vila-seca situada a 41,10° N]({{ site.baseurl }}/assets/img/coordinate-systems/utm-zone-31n.svg "El fus 31 és una franja de 6° de longitud. En EPSG:25831, la N selecciona la part situada entre l'equador i 84° N; no identifica una banda MGRS. Figura d'elaboració pròpia, revisada el 25 d'agost de 2026.")
![Esquema de les coordenades UTM E i N amb el fals est de 500.000 m al meridià central i l'origen N igual a zero metres a l'equador]({{ site.baseurl }}/assets/img/coordinate-systems/utm-zone-internal-coordinates.svg "La coordenada E de Vila-seca és inferior a 500.000 m perquè queda a l'oest del meridià central. A l'hemisferi nord, la coordenada N es compta des de l'equador. Esquema conceptual d'elaboració pròpia, no a escala, revisat el 25 d'agost de 2026.")
![Reticle UTM quilomètric de Vila-seca amb tres llocs reals i un recordatori que l'origen de la coordenada N és l'equador, fora del mapa local]({{ site.baseurl }}/assets/img/coordinate-systems/utm-grid-vila-seca.svg "El reticle local es llegeix primer cap a l'est i després cap al nord. Els valors N superiors a 4,5 milions de metres conserven l'equador com a origen encara que no càpiga en aquesta extensió. Figura d'elaboració pròpia, revisada el 25 d'agost de 2026.")
:::

::: table "Tres llocs de Vila-seca en coordenades geogràfiques i UTM"
| Lloc | Longitud, latitud (`EPSG:4326`) | UTM ETRS89 / zona 31N (`EPSG:25831`) |
| --- | --- | --- |
| Facultat de Turisme i Geografia | `1.1478406, 41.1026664` | `zona 31N · E 344469 m · N 4551807 m` |
| Castell de Vila-seca | `1.1475084, 41.1146813` | `zona 31N · E 344469 m · N 4553142 m` |
| Torre d'en Dolça | `1.1599211, 41.0989127` | `zona 31N · E 345474 m · N 4551369 m` |
:::

Les posicions geogràfiques de la taula provenen d'OpenStreetMap i s'han transformat amb [PROJ 9.4.0](https://proj.org/), una biblioteca oberta que utilitzen diversos programes geoespacials per transformar coordenades entre sistemes de referència. El nom documenta com s'ha fet el càlcul; no és una eina que l'estudiant hagi d'executar en aquesta activitat. La pàgina de [drets d'autor i atribució d'OpenStreetMap](https://www.openstreetmap.org/copyright) n'estableix les condicions d'ús i l'atribució, però no verifica directament aquestes coordenades. Els resultats s'han arrodonit al metre i no representen un aixecament topogràfic. La lectura relativa és immediata: la Facultat i el Castell tenen gairebé la mateixa E, però el Castell és aproximadament 1,3 km més al nord; la Torre d'en Dolça queda aproximadament 1 km més a l'est de tots dos. En un reticle d'1 km, la [lectura de coordenades UTM](https://www.usgs.gov/faqs/how-are-utm-coordinates-measured-usgs-topographic-maps) comença identificant la línia d'est situada a l'esquerra del punt i després la línia de nord situada per sota; els dígits addicionals precisen la posició dins del quadrat.

>>>> **Un parell de coordenades no identifica per si sol un lloc.** Interpretar metres com si fossin graus, invertir els eixos o assignar un EPSG només perquè la capa aparegui prop del territori esperat pot ocultar l'error. Primer s'han de revisar la font, les unitats, l'ordre dels eixos i l'extensió; després es decideix l'operació adequada.

### Projeccions i distorsions

Una **projecció cartogràfica** transforma matemàticament posicions d'una superfície corba per representar-les sobre un pla. Cap projecció conserva alhora formes, àrees, distàncies i direccions. La selecció depèn del territori, l'escala i l'operació prevista.

Una manera clàssica d'introduir les projeccions és imaginar una superfície auxiliar que rep la informació del globus i després es desplega: un **pla** en les projeccions azimutals o zenitals, un **con** en les projeccions còniques i un **cilindre** en les projeccions cilíndriques. Aquesta imatge ajuda a entendre per què una projecció pot ajustar-se millor a unes zones que a unes altres. Si la superfície toca el globus, parlem d'una posició **tangent**; si el talla, de posició **secant**. En la figura, el vermell assenyala els punts o paral·lels on l'escala és exacta, el taronja indica expansió de l'escala i el blau, compressió. També pot canviar l'orientació: normal, transversa o obliqua, segons quin eix o franja del territori es vulgui privilegiar.

![Comparació de superfícies cilíndriques, còniques i azimutals en posició tangent i secant]({{ site.baseurl }}/assets/img/coordinate-systems/comparison-cartography-surface-development-ca.svg "La posició tangent produeix un punt o un paral·lel d'escala exacta; la secant en produeix dos, excepte en el cas azimutal, on el contacte és circular. El vermell indica escala exacta, el taronja expansió i el blau compressió. CMG Lee, US government, Clindberg i Palosirkka, «Comparison of cartography surface development», Wikimedia Commons, 12 de desembre de 2019; revisió portuguesa de Vickvvy, 30 de juliol de 2024; adaptació al català del manual TIGIT, 25 d'agost de 2026, CC BY-SA 4.0."){: data-figure-width-web="17.5rem" data-figure-width-pdf="41%"}

En algunes projeccions azimutals perspectives també és determinant la posició del **centre de projecció**, que es pot imaginar com un punt de llum. Els raigs parteixen d'aquest centre, travessen punts de l'esfera i tallen el pla tangent. Si el centre se situa al centre de l'esfera, la projecció és **gnomònica**; si se situa sobre la superfície al punt oposat al contacte amb el pla, és **estereogràfica**; i si s'allunya idealment fins a l'infinit, els raigs esdevenen paral·lels i la projecció és **ortogràfica**. La posició modifica la separació dels punts projectats i les propietats resultants: la gnomònica converteix els grans cercles en rectes, l'estereogràfica és conforme i l'ortogràfica produeix l'aparença d'un globus observat des de molt lluny.

![Comparació del centre de projecció en les projeccions azimutals gnomònica, estereogràfica i ortogràfica]({{ site.baseurl }}/assets/img/coordinate-systems/azimuthal-perspective-centers.svg "La gnomònica situa el centre de projecció al centre de l'esfera; l'estereogràfica, al punt de la superfície oposat al punt de tangència; i l'ortogràfica, a l'infinit, de manera que els raigs són paral·lels. Esquema geomètric d'elaboració pròpia, no a escala, 25 d'agost de 2026."){: data-figure-width="56rem"}

Aquesta construcció no s'ha de llegir com si totes les projeccions fossin una projecció òptica literal. Només descriu una família perspectiva concreta. Moltes projeccions cartogràfiques es defineixen directament amb fórmules, i algunes combinen o modifiquen les famílies bàsiques de superfícies. La utilitat de la classificació és donar una intuïció inicial: la distorsió tendeix a ser menor a prop de les línies o punts de contacte i creix quan el mapa s'allunya de la zona per a la qual ha estat pensat.

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

En cartografia, l'«error» d'una projecció no acostuma a ser un soroll aleatori, sinó una deformació sistemàtica que canvia amb la posició i, sovint, amb la direcció. El factor d'escala pot ser gairebé exacte sobre una línia o prop d'un centre i créixer en allunyar-se'n. Per això no n'hi ha prou amb saber que una projecció és conforme o equivalent: també cal saber on se situa el territori respecte del meridià central, els paral·lels estàndard, el punt de tangència o l'àrea d'ús declarada.

La geometria de la superfície auxiliar orienta aquest patró. Una azimutal concentra habitualment l'ajust al voltant del centre i es degrada cap a la vora; és útil per a regions polars, hemisferis o distàncies i direccions definides des d'un punt, segons la projecció concreta. Una cònica pot ajustar bé territoris de latituds mitjanes estesos d'est a oest, especialment a prop dels paral·lels estàndard. Una cilíndrica normal reparteix el contacte prop de l'equador o de paral·lels escollits i acostuma a deformar més les latituds altes. En posició transversa, la franja de menor deformació gira i segueix un meridià: aquesta és la lògica que permet dividir UTM en fusos estrets.

Algunes parts del món poden quedar no només deformades, sinó excloses. Mercator no representa els pols perquè quedarien a una distància infinita; una ortogràfica mostra només l'hemisferi orientat cap a l'observador; una gnomònica no pot prolongar sense límit els punts propers als 90° del centre; i un CRS UTM està pensat per al seu fus i la seva àrea d'ús, no per a calcular indistintament sobre tot el planeta. Retallar el mapa no elimina aquesta limitació: cal que l'extensió representada i l'operació coincideixin amb la zona on la projecció controla la deformació {% cite snyderMapProjections1987 %}.

::: subfigures a+b/c+d/e+f "Sis projeccions calculades amb la mateixa base mundial i una retícula comparable. Les quatre primeres mostren alternatives globals; l'ortogràfica fa explícit que una vista perspectiva només ensenya un hemisferi; la Mercator transversa mostra una projecció regional que concentra la precisió prop del fus. Figures d'elaboració pròpia a partir de la base mundial del conjunt `maps`."
![Mapamundi de Mercator, conforme, amb l'àrea ampliada cap a les latituds altes i els pols exclosos]({{ site.baseurl }}/assets/img/coordinate-systems/projection-gallery-mercator.svg "Mercator conserva angles locals, però l'escala i l'àrea creixen amb la latitud; la figura es limita a 80° N i 80° S.")
![Mapamundi en projecció cilíndrica equivalent de Lambert, amb àrees conservades i formes comprimides a latituds altes]({{ site.baseurl }}/assets/img/coordinate-systems/projection-gallery-lambert-cylindrical-equal-area.svg "La projecció cilíndrica equivalent de Lambert conserva les àrees relatives, però no els angles ni les formes.")
![Mapamundi de Mollweide, equivalent i de contorn el·líptic]({{ site.baseurl }}/assets/img/coordinate-systems/projection-gallery-mollweide.svg "Mollweide conserva l'àrea mundial i reparteix les deformacions de forma dins d'un contorn el·líptic.")
![Mapamundi de Robinson, de compromís, sense conservació mètrica exacta global]({{ site.baseurl }}/assets/img/coordinate-systems/projection-gallery-robinson.svg "Robinson busca un equilibri visual global, però no conserva exactament àrees, angles o distàncies.")
![Projecció ortogràfica centrada a l'Àfrica que només mostra l'hemisferi visible]({{ site.baseurl }}/assets/img/coordinate-systems/projection-gallery-orthographic-africa.svg "L'ortogràfica simula una vista molt distant: el centre és recognoscible i l'horitzó comprimeix les formes; l'hemisferi posterior no hi apareix.")
![Mercator transversa ETRS89 UTM zona 31N aplicada a Europa occidental]({{ site.baseurl }}/assets/img/coordinate-systems/projection-gallery-transverse-mercator.svg "ETRS89 / UTM zona 31N és conforme i adequada prop del fus 31; l'error d'escala augmenta en allunyar-se del meridià central.")
:::

#### Projeccions especials

Les famílies cilíndrica, cònica i azimutal són una primera classificació útil, però no esgoten les construccions possibles. Algunes projeccions es defineixen amb transformacions matemàtiques que produeixen contorns pseudocilíndrics, quadrats o aparentment tridimensionals. Aquestes formes no són només una curiositat visual: permeten comprovar que el contorn del mapamundi i la propietat geomètrica que conserva són decisions diferents.

Rabella presenta aquesta diversitat com una demostració de l'«impossible art d'aplanar la Terra»: no hi ha una projecció ideal al marge de la finalitat. Entre els exemples inclou la projecció estrellada de **Petermann**, que converteix el mapamundi en una estrella de vuit puntes. La descriu com a parcialment equidistant perquè conserva l'escala al llarg d'una línia concreta que travessa l'hemisferi central, no perquè mantingui totes les distàncies del mapa. La forma espectacular no és, per tant, una propietat mètrica ni un criteri suficient de selecció {% cite rabellaMilProjeccionsMapamundi1990 %}.

La projecció **sinusoïdal**, també anomenada Sanson–Flamsteed, és pseudocilíndrica i equivalent. Els paral·lels són rectes, el meridià central també és recte i la resta de meridians es corben fins a trobar-se als pols. La conservació de l'àrea la fa adequada per comparar superfícies globals, però les formes s'allarguen o s'inclinen progressivament en allunyar-se del meridià central.

La projecció **quincuncial de Peirce** transforma el globus en un quadrat que es pot repetir com una tessel·lació. És conforme excepte en quatre punts singulars de l'equador: lluny d'aquests punts, les indicatrius conserven la forma circular encara que canviïn de mida; a les singularitats, la deformació creix bruscament. La projecció **Armadillo de Raisz** produeix, en canvi, una vista que recorda una perspectiva sobre una superfície corba i permet mostrar més d'un hemisferi. No és conforme ni equivalent; les indicatrius esdevenen el·lipses i canvien de mida segons la posició.

::: subfigures a+b/c "Tres projeccions que amplien les famílies habituals. La subfigura a mostra una projecció sinusoïdal equivalent d'elaboració pròpia. La subfigura b mostra la projecció quincuncial de Peirce amb indicatrius de Tissot. La subfigura c mostra la projecció Armadillo de Raisz i combina la deformació angular i d'àrea en les indicatrius. Les dues darreres figures es conserven sense modificacions des de Wikimedia Commons."
![Mapamundi sinusoïdal equivalent, amb paral·lels rectes i meridians corbats excepte el central]({{ site.baseurl }}/assets/img/coordinate-systems/projection-gallery-sinusoidal.svg "La projecció sinusoïdal conserva les àrees, però deforma progressivament les formes cap als marges. Base mundial: conjunt `maps`.")
![Projecció quincuncial de Peirce en un quadrat, amb indicatrius circulars excepte als quatre punts singulars de l'equador]({{ site.baseurl }}/assets/img/coordinate-systems/projection-special-peirce-quincuncial-tissot.svg "Projecció quincuncial de Peirce amb retícula de 10 graus i indicatrius de Tissot de 1.000 km. Justin Kunimune, Wikimedia Commons, CC0 1.0.")
![Projecció Armadillo de Raisz amb retícula i indicatrius que mostren deformació angular i variació d'àrea]({{ site.baseurl }}/assets/img/coordinate-systems/projection-special-armadillo-tissot.svg "Projecció Armadillo de Raisz amb indicatrius de Tissot; els tons clars indiquen menys deformació, el vermell més deformació angular i el verd més variació d'àrea. Strebe, Wikimedia Commons, CC BY-SA 4.0.")
:::

Les figures originals es poden consultar a les fitxes de Wikimedia Commons de la [projecció quincuncial de Peirce](https://commons.wikimedia.org/wiki/File:Peirce_Quincuncial_with_Tissot%27s_Indicatrices_of_Distortion.svg), publicada per Justin Kunimune sota CC0 1.0, i de la [projecció Armadillo](https://commons.wikimedia.org/wiki/File:Armadillo_projection_Tissot.svg), publicada per Strebe sota CC BY-SA 4.0. En tots tres casos, la forma singular del mapa no substitueix l'avaluació de propietats, àrea d'ús i finalitat: una projecció visualment expressiva no esdevé per això adequada per mesurar distàncies, angles o superfícies.

>> **Lectura recomanada.** [*Mil projeccions per a un mapamundi, o l'impossible art d'aplanar la Terra*](https://raco.cat/index.php/RCG/article/view/119557), de Josep Maria Rabella i Vives, es pot consultar a RACO. La lectura és especialment útil per comparar sinusoïdal, Petermann, Peirce i Armadillo com a respostes diferents a un problema sense solució única; l'accés públic no implica que les figures es puguin redistribuir sense revisar-ne els drets {% cite rabellaMilProjeccionsMapamundi1990 %}.

No cal memoritzar les fórmules de tota la galeria. Cal poder reconèixer quina propietat es prioritza, on es concentra la deformació, quina part del món queda inclosa i si l'extensió és coherent amb la tasca. Localitzar municipis, mesurar distàncies, calcular superfícies o construir un mapamundi no imposen exactament les mateixes condicions.

Una capa pot semblar ben situada i, tanmateix, no ser adequada per calcular àrees o distàncies. La comprovació ha d'incloure el sistema de referència, les unitats i l'àrea d'ús, no només la coincidència visual amb un mapa de fons.

### Explorar com es construeix una projecció

El [GITTA Map Projector](https://gevian.github.io/GITTA-MP/) de Magnus Heitzler permet passar d'una definició abstracta a una construcció manipulable. El mode **Advanced** separa la superfície de projecció, la seva orientació, el centre de projecció i les capes de fronteres, retícula i indicatrius de Tissot. També permet aplanar un cilindre o un con i observar com una funció d'escalat modifica el resultat. El recurs va ser desenvolupat per a la plataforma GITTA a l'ETH Zürich i el [repositori original](https://github.com/gevian/GITTA-MP) es distribueix sota GPL v3.

![Mode avançat del GITTA Map Projector amb una projecció de Mercator aplanada, la funció d'escalat i les indicatrius de Tissot]({{ site.baseurl }}/assets/img/coordinate-systems/gitta-map-projector-mercator-advanced-2026-08-12.png "Construcció de Mercator a partir d'una projecció cilíndrica central aplanada i escalada. S'hi mostren fronteres, retícula, indicatrius de Tissot, paràmetres geomètrics i funció d'escalat. Captura pròpia del mode Advanced, 12 d'agost de 2026. GITTA Map Projector, Magnus Heitzler, Institute of Cartography and Geoinformation, ETH Zürich, 2019, GPL v3."){: data-figure-width="54rem"}

Una exploració breu pot començar a **Projection Surfaces** per construir un pla, un con i un cilindre; continuar a **Map Distortion Basics** activant les indicatrius; i acabar a **The Mercator Projection** amb la seqüència **Central Cylindrical Projection**, **flatten** i **Scale Central Cylindrical to Mercator**. El model ajuda a entendre propietats i transformacions, però no implica que totes les projeccions cartogràfiques siguin projeccions geomètriques de llum sobre una superfície: moltes es defineixen directament mitjançant fórmules.

### Mercator, Gall-Peters i lectura crítica de la distorsió

Una projecció no és una fotografia defectuosa del globus, sinó una transformació matemàtica. Com que una superfície corba no es pot desplegar sobre un pla sense deformar-la, qualsevol mapamundi altera les àrees, les formes, les distàncies o les direccions. La distorsió és inevitable i es pot mesurar; el problema comunicatiu apareix quan s'utilitza una projecció inadequada per a la pregunta o s'oculten les propietats que no conserva {% cite snyderMapProjections1987 %}.

Mercator va presentar el 1569 una projecció destinada explícitament a la navegació. És conforme: conserva els angles locals i converteix les **loxodròmies**, els trajectes de rumb constant, en rectes. Aquesta propietat facilitava traçar rumbs de brúixola, encara que una loxodròmia no sigui generalment la ruta més curta. El cost és que l'escala i les àrees augmenten ràpidament amb la latitud i els pols no es poden representar; per això Mercator no és adequada per comparar la superfície de països o continents en un mapamundi {% cite snyderMapProjections1987 %}.

La projecció coneguda com a **Gall-Peters** respon a un altre propòsit. James Gall ja havia presentat el 1855 una construcció matemàticament equivalent i la va publicar el 1885; Arno Peters la va popularitzar a partir de 1973 com una alternativa més equitativa als mapamundis de Mercator. Gall-Peters és una [projecció cilíndrica equivalent](https://proj.org/en/stable/operations/projections/cea.html): un territori que té el doble d'àrea que un altre ocupa el doble de superfície al mapa. No elimina la distorsió, sinó que la redistribueix: deforma les formes, els angles, les distàncies i les direccions, amb escala correcta als paral·lels de 45° N i 45° S {% cite gallCylindricalProjections1885 robinsonArnoPeters1985 %}.

L'eina [*The True Size Of…*](https://thetruesize.com/) permet cercar un país i arrossegar-ne el contorn per diferents latituds sobre un fons Mercator. El territori no canvia d'àrea real durant el desplaçament, però la mida necessària per encaixar amb el mapa varia: Groenlàndia deixa de semblar comparable amb Àfrica quan s'acosta a l'equador. L'activitat fa visible el patró de distorsió, però no converteix el fons del visor en una superfície adequada per mesurar; serveix per formular una comparació que després es pot contrastar amb dades d'àrea.

![Captura de The True Size Of amb Groenlàndia seleccionada sobre un mapa Mercator]({{ site.baseurl }}/assets/img/coordinate-systems/the-true-size-greenland-mercator-2026-08-13.png "Captura pròpia de The True Size Of, 13 d'agost de 2026, amb Groenlàndia seleccionada sobre el mapa interactiu. Recurs creat per James Talmage i Damon Maneice; mapa base de Google. La funció docent és observar com el visor permet desplaçar un territori per comparar-ne l'àrea aparent en Mercator."){: data-figure-width="54rem"}

La campanya de Peters va assenyalar un efecte comunicatiu real: un mapamundi Mercator dona més pes visual a Europa i a altres territoris de latituds altes que a regions tropicals molt més extenses. Tanmateix, la fórmula amplia segons la latitud i ho fa simètricament als dos hemisferis; no codifica continents, pobles ni un meridià central concret. Analitzar l'eurocentrisme o el llegat colonial d'un mapa exigeix estudiar també qui el produeix, quina projecció i centrament escull, on talla el món, quina orientació adopta, quines fronteres i topònims mostra i en quin context circula {% cite harleyDeconstructingMap1989 monmonierHowLieMaps2018 %}.

>>>> **Mercator no és «falsa» i Gall-Peters no és «la realitat».** Mercator és útil per a determinats problemes de navegació i inadequada per comparar àrees globals; Gall-Peters conserva les àrees, però ofereix formes molt deformades. Tampoc no és l'única projecció equivalent. La pregunta cartogràfica no és quina projecció és universalment millor, sinó quina propietat necessita conservar el mapa, quines distorsions pot assumir i com les farà comprensibles al lector.

## Sistemes de referència espacial

Quan diverses capes s'han de comparar, el sistema de referència converteix la definició geodèsica en decisions explícites sobre coordenades, projectes i transformacions.

>>>>> Aquesta fase converteix la definició d'un sistema de referència espacial en decisions explícites sobre capes, projectes i transformacions.
>>>>>
>>>>> - Interpretar un identificador EPSG a partir del dàtum, la projecció, els eixos, les unitats i l'àrea d'ús.
>>>>> - Contrastar `EPSG:4326`, `EPSG:25831` i un CRS ED50 segons les coordenades i el territori que descriuen.
>>>>> - Assignar un CRS només quan les coordenades ja pertanyen al sistema conegut i en falta la definició correcta.
>>>>> - Reprojectar una geometria quan cal calcular coordenades noves en un CRS de destinació justificat.
>>>>> - Verificar per separat el CRS de cada capa, el CRS del projecte i el CRS del fitxer exportat.

### Identificadors EPSG

Un codi EPSG és un identificador curt per referir-se a una definició geodèsica llarga. L'acrònim prové de l'antic **European Petroleum Survey Group**; avui el conjunt de dades EPSG és publicat a [epsg.org](https://epsg.org/) i mantingut per la subcomissió de geodèsia del comitè de geomàtica de l'IOGP. En la pràctica, el registre funciona com un vocabulari tècnic compartit: en lloc d'escriure cada vegada el dàtum, l'el·lipsoide, la projecció, les unitats, els eixos i l'àrea d'ús, molts programes poden identificar aquesta definició mitjançant un número.

A QGIS, seleccionar el CRS d'una capa o del projecte sovint vol dir triar una d'aquestes definicions. `EPSG:4326` identifica el sistema geogràfic WGS 84, expressat habitualment en longitud i latitud en graus. `EPSG:25831` identifica `ETRS89 / UTM zona 31N`, un sistema projectat en metres adequat per al treball regional a Catalunya. La diferència no és cosmètica: si una taula amb longituds i latituds en graus s'importa com si fossin metres UTM, o si una capa UTM es declara com a WGS 84, QGIS pot situar els punts en un lloc absurd o permetre mesures que semblen precises però no tenen sentit.

El codi facilita l'intercanvi i evita moltes ambigüitats, però no substitueix la lectura crítica de la font. Abans d'acceptar un EPSG cal comprovar que el nom del CRS, les unitats, l'ordre dels eixos, l'àrea d'ús i l'operació prevista concorden amb les coordenades disponibles. Configurar bé QGIS no consisteix a trobar un número que faci encaixar visualment una capa, sinó a declarar el sistema real de les coordenades i, si cal, transformar-les després amb una reprojecció documentada.

### Assignar i reprojeccionar

Assignar un sistema indica com s'han d'interpretar unes coordenades; reprojeccionar transforma la geometria. Confondre aquestes operacions pot produir capes aparentment encaixades però tècnicament incorrectes.

#### Assignar un sistema de referència

L'assignació modifica la descripció de les coordenades, no els nombres que formen la geometria. Només és adequada quan el sistema correcte es coneix per la font o per documentació fiable i la capa l'ha perdut o el declara erròniament. No s'ha d'utilitzar com un procediment de prova fins que la capa coincideixi visualment.

#### Reprojectar una geometria

La reprojecció calcula coordenades noves que representen les mateixes posicions en un altre sistema. És adequada quan el sistema d'origen està ben definit i cal obtenir una capa de treball amb un altre CRS. La capa original s'ha de preservar, i el fitxer derivat ha d'identificar el sistema de destinació.

#### Reprojecció al vol

El programari cartogràfic pot mostrar conjuntament capes amb sistemes diferents mitjançant una transformació temporal de visualització. Aquesta capacitat facilita l'exploració, però no canvia els fitxers d'origen ni resol automàticament quin sistema convé per mesurar o exportar. El sistema de referència del projecte i el de cada capa s'han de revisar explícitament.

### Escala cartogràfica i nivell de detall

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

## Activitat prèvia: llegir coordenades en una taula

Abans d'obrir QGIS, s'inspeccionarà a Calc o Excel el CSV del Directori de centres educatius. Es filtrarà el curs 2025/2026 i el municipi de Vila-seca, codi `431711`, i es compararan quatre camps: coordenada UTM X, coordenada UTM Y, longitud i latitud. La font declara les coordenades UTM en ETRS89 / UTM zona 31N, `EPSG:25831`, i les geogràfiques en longitud i latitud. Aquesta informació forma part de la dada: els nombres no permeten crear punts correctes si s'ignoren l'ordre, les unitats o el CRS.

La inspecció comprovarà que X i Y UTM tenen ordres de magnitud compatibles amb metres a Catalunya, mentre que longitud i latitud s'expressen en graus decimals. Es revisarà una fila coneguda, es comptaran coordenades buides o duplicades i s'anotarà que el punt representa l'entrada del centre, no tota la parcel·la ni la població atesa. Encara no es crearà cap geometria.

>>>>> Aquesta activitat deixa preparada una taula de 17 centres de Vila-seca i una fitxa breu dels camps X/Y, les unitats, el CRS i les incidències detectades.

La captura necessària mostrarà al full de càlcul les columnes de codi, centre, UTM X/Y i longitud/latitud, amb el filtre de Vila-seca visible. El capítol següent reutilitzarà exactament aquests camps al diàleg de text delimitat de QGIS i comprovarà que les dues parelles de coordenades produeixen punts coincidents.

## Activitat: preparar la base espacial de la comarca

L'activitat prepara una base espacial municipal fiable per continuar el projecte: abans de representar indicadors, cal comprovar la procedència, la geometria, els codis territorials i el sistema de referència de la capa, i distingir una assignació de CRS d'una reprojecció.

>>>>> L'activitat produeix una base municipal traçable i validada que es conservarà en el projecte QGIS dels capítols següents.
>>>>>
>>>>> - Documentar la procedència, la data territorial, la llicència, la geometria, els camps clau i el CRS de la font municipal.
>>>>> - Inspeccionar a QGIS l'esquema, l'extensió, les unitats, el nombre d'entitats i almenys un municipi conegut.
>>>>> - Seleccionar la comarca amb una clau territorial documentada i comprovar la presència i la unicitat dels codis municipals.
>>>>> - Diagnosticar el desplaçament ED50–ETRS89 i justificar si correspon assignar informació absent o reprojeccionar coordenades definides.
>>>>> - Desar una capa derivada sense modificar la font original i verificar-ne geometria, CRS, extensió, recomptes, codis i ordres de magnitud.

### Fonts, fitxers i resultats de la preparació espacial

Per al Tarragonès s'utilitzarà el GeoPackage oficial **Divisions administratives v2.2, gener de 2026**, de l'ICGC, amb llicència CC BY 4.0 i CRS `EPSG:25831`. El fitxer conté diverses capes i escales: la demostració utilitzarà municipis a 1:250.000 per al mapa comarcal, una versió generalitzada per al requadre provincial i municipis a 1:50.000 per comprovar Vila-seca. Obrir un GeoPackage no exigeix administrar una base de dades: en aquesta activitat funciona com un contenidor amb diverses capes, semblant a un llibre amb diversos fulls.

El projecte conservarà la fita `qgis/tigit-04-dades-espacials.qgz` i la capa derivada compacta `data/processed/tarragones-boundaries-icgc-20260120.gpkg`. La data de la geometria no es confondrà amb el període 2021 de les dades estadístiques. La parella diagnòstica ED50/ETRS89 continuarà sent un exercici separat i no contaminarà la geometria canònica.

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

La selecció del Tarragonès i les capes de context es desaran a `data/processed/tarragones-boundaries-icgc-20260120.gpkg`. No cal reprojeccionar-les perquè la font ja declara `EPSG:25831`; documentar que no s'ha aplicat cap transformació també és una decisió tècnica. El ZIP original es podrà regenerar a partir de la URL i el checksum documentats, i el projecte utilitzarà rutes relatives.

### Validar la base espacial municipal

Abans de continuar s'han de comprovar aquests punts:

1. l'extensió cobreix el territori esperat i les unitats concorden amb el CRS;
2. el nombre de municipis de la comarca és plausible i queda registrat;
3. el codi municipal és present i no conté duplicats inesperats;
4. la geometria és poligonal i adequada per representar unitats municipals;
5. almenys un municipi, una coordenada i una mesura tenen un ordre de magnitud coherent;
6. la data territorial, la font i la llicència es poden recuperar;
7. els fitxers originals no s'han sobreescrit.

### Evidències de la preparació espacial

::: table "Evidències de la preparació espacial"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/raw` | Capa municipal original | Fitxers complets sense modificar i documentació de procedència |
| `qgis` | `tigit-04-dades-espacials.qgz` | Font oficial, capes multiescala, CRS, rutes relatives i selecció comprovada |
| `data/processed` | `tarragones-boundaries-icgc-20260120.gpkg` | Municipis a 1:250.000, comarca, província, Vila-seca a 1:50.000 i capitals necessàries |
| `README.md` | Auditoria de la capa | Productor, versió, llicència, geometria, entitats, camps clau, CRS, unitats i extensió |
| `README.md` | Diagnosi ED50–ETRS89 | Cada fitxer identificat amb nom, geometria i CRS; desplaçament, operació justificada i comprovació posterior |
| `captures` | Subcapes i propietats espacials | Diàleg de subcapes del GeoPackage i propietats amb geometria, entitats, extensió i `EPSG:25831` visibles |
:::
