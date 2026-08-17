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

## Modelar la forma de la Terra

### Geoide, el·lipsoide i esferoide

La forma física de la Terra, el model matemàtic utilitzat per calcular coordenades i la superfície de referència de les altures no són exactament el mateix. Aquesta distinció és important perquè una capa pot estar ben situada en planta i, alhora, expressar l'altura amb una referència inadequada. En cartografia digital, aquests conceptes apareixen dins dels sistemes de referència, però no són simples codis: indiquen quina superfície s'ha triat per mesurar, projectar o comparar.

La superfície real de la Terra és el relleu: continents, fons oceànics, gel, aigua i formes canviants. El **geoide** no és aquesta superfície real. És una superfície física vinculada al camp de gravetat terrestre, propera al nivell mitjà del mar i prolongada conceptualment sota els continents. Serveix per entendre altures perquè segueix una condició gravimètrica: tots els punts del geoide comparteixen el mateix potencial de gravetat. Per això és una referència natural per a altures físiques, però no és una superfície regular ni còmoda per calcular coordenades horitzontals.

L'**el·lipsoide de referència** és un model matemàtic regular que aproxima la forma general de la Terra i permet definir latituds, longituds, normals, distàncies i projeccions amb fórmules manejables. En molts textos també es parla d'**esferoide**. En aquest context, un esferoide és un el·lipsoide de revolució, és a dir, una el·lipse que gira al voltant del seu eix menor. La paraula recorda que el model s'assembla a una esfera lleugerament aplanada, però el terme tècnic més habitual en geodèsia i cartografia digital és el·lipsoide.

En una secció meridiana, l'el·lipsoide es pot descriure mitjançant el semieix major equatorial $a$ i el semieix menor polar $b$. La diferència real entre tots dos és molt petita respecte de la mida de la Terra; la subfigura b exagera l'aplanament per fer visibles els eixos. En fer girar aquesta secció al voltant de l'eix polar s'obté l'el·lipsoide de revolució utilitzat com a model de referència.

Els el·lipsoides es poden ajustar per a territoris, èpoques i finalitats diferents. Alguns models històrics o regionals buscaven encaixar molt bé amb una part concreta del món; altres, com els que s'utilitzen en marcs globals contemporanis, busquen una coherència planetària. Això explica que un canvi de dàtum pugui desplaçar una capa encara que la projecció sembli la mateixa: no només canvia la manera de dibuixar sobre el pla, sinó també la manera d'ancorar el model a la Terra.

::: subfigures a+b/c "Geoide i el·lipsoide com a models de referència complementaris. El geoide descriu una superfície física vinculada a la gravetat; l'el·lipsoide és una superfície matemàtica regular que pot ajustar-se globalment o prioritzar una regió."
![Visualització global del geoide GOCO06s amb colors blaus i vermells que indiquen l'altura del geoide respecte d'un el·lipsoide de referència]({{ site.baseurl }}/assets/img/coordinate-systems/nasa-geoid-goco06s-2026.png "Geoide GOCO06s, amb l'altura exagerada 10.000 vegades. Visualització de Mark SubbaRao, NASA/GSFC, basada en el model gravitatori GOCO06s")
![Secció el·líptica amb el semieix major equatorial a i el semieix menor polar b]({{ site.baseurl }}/assets/img/coordinate-systems/ellipse-semi-axes.svg "Semieixos a i b d'un el·lipsoide de revolució; adaptació de M. W. Toews, Wikimedia Commons, CC0 1.0")
![Esquema amb un el·lipsoide global i dos el·lipsoides locals que s'ajusten millor a Amèrica o a Europa]({{ site.baseurl }}/assets/img/coordinate-systems/ellipsoid-local-fit.svg "Esquema propi: un el·lipsoide local pot encaixar millor amb una regió i pitjor amb una altra; l'el·lipsoide global reparteix l'encaix a escala planetària")
:::

La subfigura a és útil justament perquè exagera allò que a escala planetària gairebé no veuríem. La mateixa fitxa de la NASA avisa que hi ha una versió a escala en què les variacions no són perceptibles, i una versió exagerada per fer-les visibles {% cite nasaSvsGeoid2026 %}. Aquesta és una bona advertència cartogràfica: una figura del geoide no mostra muntanyes ni fondàries oceàniques, sinó diferències de potencial gravimètric respecte d'un el·lipsoide. La subfigura c també és un esquema exagerat: no representa les dimensions reals dels el·lipsoides, sinó la idea que l'encaix d'un model depèn de l'àrea d'ús i del dàtum que el materialitza.

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

![Dos globus mostren els paral·lels que determinen la latitud i els meridians que determinen la longitud]({{ site.baseurl }}/assets/img/coordinate-systems/latitude-longitude-earth.svg "La xarxa geogràfica permet expressar la latitud respecte de l'equador i la longitud respecte del meridià d'origen. Font: Djexplo, «Latitude and Longitude of the Earth», Wikimedia Commons, CC0 1.0.")

### Reticle UTM i coordenades projectades

Els sistemes projectats transformen la superfície terrestre en un pla i permeten treballar habitualment amb unitats mètriques. El sistema UTM divideix el món, entre 80° S i 84° N, en seixanta fusos longitudinals de 6°. Els mapes generals del reticle també mostren bandes latitudinals de 8° que s'utilitzen en referències de quadrícula: Catalunya queda al fus 31 i a la banda T. En canvi, quan parlem del CRS `ETRS89 / UTM zona 31N` (`EPSG:25831`), la `N` indica l'hemisferi nord, no la banda latitudinal. En aquest sistema, els eixos són **est** (*easting*, E) i **nord** (*northing*, N), en aquest ordre, i la unitat és el metre {% cite epsg25831 usgsUtmCoordinates2026 %}.

La coordenada UTM necessita més informació que els dos nombres. `ETRS89 / UTM zona 31N · EPSG:25831 · E 344.469 m · N 4.551.807 m` identifica el CRS, el fus i l'hemisferi, la component est i la component nord de la Facultat. El meridià central del fus 31, 3° E, rep un **fals est** de 500.000 m; per això una E inferior a 500.000 situa el punt a l'oest del meridià central sense emprar valors negatius. A l'hemisferi nord, la N es compta des de l'equador amb un fals nord de 0 m. Escriure només `344469, 4551807` deixaria oberta la zona, l'hemisferi, el dàtum i fins i tot l'ordre dels eixos.

::: subfigures a+b/c "Del reticle UTM global al fus 31N i al reticle local de Vila-seca. La subfigura a mostra els fusos i bandes UTM del planeta; les subfigures b i c són esquemes propis basats en conversions executades amb PROJ 9.4.0."
![Reticle mundial de fusos UTM i bandes latitudinals; Catalunya se situa al fus 31 i a la banda T, mentre que EPSG:25831 usa 31N per indicar el fus 31 de l'hemisferi nord]({{ site.baseurl }}/assets/img/coordinate-systems/utm-zones-world.jpg "Fusos longitudinals i bandes latitudinals del reticle UTM. Font: Jan Krymmel, Wikimedia Commons, a partir de NASA Visible Earth; domini públic, CC BY-SA 3.0 i GFDL.")
![Zona UTM 31N entre els meridians 0° E i 6° E, amb el meridià central a 3° E i Vila-seca situada a l'oest d'aquest meridià]({{ site.baseurl }}/assets/img/coordinate-systems/utm-zone-31n.svg "El fus 31N és una franja de 6° de longitud; el meridià central rep E = 500.000 m i permet interpretar per què Vila-seca té una coordenada est inferior a 500.000 m. Figura d'elaboració pròpia, 14 d'agost de 2026.")
![Reticle UTM quilomètric amb tres llocs reals de Vila-seca i les seves coordenades est i nord]({{ site.baseurl }}/assets/img/coordinate-systems/utm-grid-vila-seca.svg "El reticle es llegeix primer cap a l'est i després cap al nord; a l'hemisferi nord, el valor N es compta des de l'equador")
:::

![Esquema del funcionament intern d'un fus UTM: límits longitudinals, meridià central, fals est, coordenada est i coordenada nord]({{ site.baseurl }}/assets/img/coordinate-systems/utm-zone-internal-coordinates.svg "Dins d'un fus UTM, les coordenades són metres sobre un sistema cartesià local: E augmenta cap a l'est, N cap al nord i el fals est de 500.000 m evita valors negatius a prop del meridià central. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="54rem"}

::: table "Tres llocs de Vila-seca en coordenades geogràfiques i UTM"
| Lloc | Longitud, latitud (`EPSG:4326`) | UTM ETRS89 / zona 31N (`EPSG:25831`) |
| --- | --- | --- |
| Facultat de Turisme i Geografia | `1.1478406, 41.1026664` | `zona 31N · E 344469 m · N 4551807 m` |
| Castell de Vila-seca | `1.1475084, 41.1146813` | `zona 31N · E 344469 m · N 4553142 m` |
| Torre d'en Dolça | `1.1599211, 41.0989127` | `zona 31N · E 345474 m · N 4551369 m` |
:::

Les posicions geogràfiques de la taula provenen d'OpenStreetMap i s'han transformat amb PROJ 9.4.0; els resultats s'han arrodonit al metre i no representen un aixecament topogràfic {% cite openStreetMapCopyright2026 %}. La lectura relativa és immediata: la Facultat i el Castell tenen gairebé la mateixa E, però el Castell és aproximadament 1,3 km més al nord; la Torre d'en Dolça queda aproximadament 1 km més a l'est de tots dos. En un reticle d'1 km, primer s'identifica la línia d'est situada a l'esquerra del punt i després la línia de nord situada per sota; els dígits addicionals precisen la posició dins del quadrat {% cite usgsUtmGridReading2026 %}.

>>>> **Un parell de coordenades no identifica per si sol un lloc.** Interpretar metres com si fossin graus, invertir els eixos o assignar un EPSG només perquè la capa aparegui prop del territori esperat pot ocultar l'error. Primer s'han de revisar la font, les unitats, l'ordre dels eixos i l'extensió; després es decideix l'operació adequada.

### Projeccions i distorsions

Una **projecció cartogràfica** transforma matemàticament posicions d'una superfície corba per representar-les sobre un pla. Cap projecció conserva alhora formes, àrees, distàncies i direccions. La selecció depèn del territori, l'escala i l'operació prevista.

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

El [GITTA Map Projector](https://gevian.github.io/GITTA-MP/) de Magnus Heitzler permet passar d'una definició abstracta a una construcció manipulable. El mode **Advanced** separa la superfície de projecció, la seva orientació, el centre de projecció i les capes de fronteres, retícula i indicatrius de Tissot. També permet aplanar un cilindre o un con i observar com una funció d'escalat modifica el resultat. El recurs va ser desenvolupat per a la plataforma GITTA a l'ETH Zürich i el [repositori original](https://github.com/gevian/GITTA-MP) es distribueix sota GPL v3 {% cite heitzlerGittaMapProjector2019 %}.

![Mode avançat del GITTA Map Projector amb una projecció de Mercator aplanada, la funció d'escalat i les indicatrius de Tissot]({{ site.baseurl }}/assets/img/coordinate-systems/gitta-map-projector-mercator-advanced-2026-08-12.png "Construcció de Mercator a partir d'una projecció cilíndrica central aplanada i escalada. S'hi mostren fronteres, retícula, indicatrius de Tissot, paràmetres geomètrics i funció d'escalat. Captura pròpia del mode Advanced, 12 d'agost de 2026. GITTA Map Projector, Magnus Heitzler, Institute of Cartography and Geoinformation, ETH Zürich, 2019, GPL v3."){: data-figure-width="54rem"}

Una exploració breu pot començar a **Projection Surfaces** per construir un pla, un con i un cilindre; continuar a **Map Distortion Basics** activant les indicatrius; i acabar a **The Mercator Projection** amb la seqüència **Central Cylindrical Projection**, **flatten** i **Scale Central Cylindrical to Mercator**. El model ajuda a entendre propietats i transformacions, però no implica que totes les projeccions cartogràfiques siguin projeccions geomètriques de llum sobre una superfície: moltes es defineixen directament mitjançant fórmules.

### Les projeccions ens enganyen?

Una projecció no és una fotografia defectuosa del globus, sinó una transformació matemàtica. Com que una superfície corba no es pot desplegar sobre un pla sense deformar-la, qualsevol mapamundi altera les àrees, les formes, les distàncies o les direccions. La distorsió és inevitable i es pot mesurar; el problema comunicatiu apareix quan s'utilitza una projecció inadequada per a la pregunta o s'oculten les propietats que no conserva {% cite snyderMapProjections1987 %}.

Mercator va presentar el 1569 una projecció destinada explícitament a la navegació. És conforme: conserva els angles locals i converteix les **loxodròmies**, els trajectes de rumb constant, en rectes. Aquesta propietat facilitava traçar rumbs de brúixola, encara que una loxodròmia no sigui generalment la ruta més curta. El cost és que l'escala i les àrees augmenten ràpidament amb la latitud i els pols no es poden representar; per això Mercator no és adequada per comparar la superfície de països o continents en un mapamundi {% cite snyderMapProjections1987 %}.

La projecció coneguda com a **Gall-Peters** respon a un altre propòsit. James Gall ja havia presentat el 1855 una construcció matemàticament equivalent i la va publicar el 1885; Arno Peters la va popularitzar a partir de 1973 com una alternativa més equitativa als mapamundis de Mercator. Gall-Peters és equivalent: un territori que té el doble d'àrea que un altre ocupa el doble de superfície al mapa. No elimina la distorsió, sinó que la redistribueix: deforma les formes, els angles, les distàncies i les direccions, amb escala correcta als paral·lels de 45° N i 45° S {% cite gallCylindricalProjections1885 robinsonArnoPeters1985 projEqualAreaCylindrical2026 %}.

L'eina [*The True Size Of…*](https://thetruesize.com/) permet cercar un país i arrossegar-ne el contorn per diferents latituds sobre un fons Mercator. El territori no canvia d'àrea real durant el desplaçament, però la mida necessària per encaixar amb el mapa varia: Groenlàndia deixa de semblar comparable amb Àfrica quan s'acosta a l'equador. L'activitat fa visible el patró de distorsió, però no converteix el fons del visor en una superfície adequada per mesurar; serveix per formular una comparació que després es pot contrastar amb dades d'àrea {% cite talmageManeiceTrueSize %}.

![Captura de The True Size Of amb Groenlàndia seleccionada sobre un mapa Mercator]({{ site.baseurl }}/assets/img/coordinate-systems/the-true-size-greenland-mercator-2026-08-13.png "Captura pròpia de The True Size Of, 13 d'agost de 2026, amb Groenlàndia seleccionada sobre el mapa interactiu. Recurs creat per James Talmage i Damon Maneice; mapa base de Google. La funció docent és observar com el visor permet desplaçar un territori per comparar-ne l'àrea aparent en Mercator."){: data-figure-width="54rem"}

La campanya de Peters va assenyalar un efecte comunicatiu real: un mapamundi Mercator dona més pes visual a Europa i a altres territoris de latituds altes que a regions tropicals molt més extenses. Tanmateix, la fórmula amplia segons la latitud i ho fa simètricament als dos hemisferis; no codifica continents, pobles ni un meridià central concret. Analitzar l'eurocentrisme o el llegat colonial d'un mapa exigeix estudiar també qui el produeix, quina projecció i centrament escull, on talla el món, quina orientació adopta, quines fronteres i topònims mostra i en quin context circula {% cite harleyDeconstructingMap1989 monmonierHowLieMaps2018 %}.

>>>> **Mercator no és «falsa» i Gall-Peters no és «la realitat».** Mercator és útil per a determinats problemes de navegació i inadequada per comparar àrees globals; Gall-Peters conserva les àrees, però ofereix formes molt deformades. Tampoc no és l'única projecció equivalent. La pregunta cartogràfica no és quina projecció és universalment millor, sinó quina propietat necessita conservar el mapa, quines distorsions pot assumir i com les farà comprensibles al lector.

## Sistemes de referència espacial

### Identificadors EPSG

Els codis EPSG identifiquen definicions completes de sistemes de referència. En el context habitual del curs es prestarà una atenció especial a ETRS89 / UTM zona 31N (`EPSG:25831`), un sistema projectat en metres adequat per al treball regional a Catalunya. El codi facilita l'intercanvi, però no substitueix la comprensió del nom, les unitats, l'àrea d'ús i les operacions previstes.

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

L'activitat iniciarà un únic projecte QGIS que continuarà als capítols següents. La font municipal es conservarà sense modificacions i se'n prepararà una capa de treball només quan calgui filtrar, reprojeccionar o exportar un resultat derivat.

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

Quan sigui necessari, la selecció comarcal es desarà com una capa derivada dins de `data/processed` o de l'espai de treball QGIS definit pel projecte. El nom indicarà el territori i el CRS. La font original continuarà a `data/raw`, i el projecte utilitzarà rutes relatives perquè la carpeta es pugui moure sense perdre les capes.

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
| `qgis` | Projecte QGIS únic | Capes carregades, CRS del projecte, rutes relatives i selecció comprovada |
| `data/processed` o `qgis` | Capa comarcal derivada | Municipis seleccionats, codi territorial preservat i CRS explícit |
| `README.md` | Auditoria de la capa | Productor, versió, llicència, geometria, entitats, camps clau, CRS, unitats i extensió |
| `README.md` | Diagnosi ED50–ETRS89 | Sistemes identificats, desplaçament, operació justificada i comprovació posterior |
:::
