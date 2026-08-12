---
layout: manual-chapter
title: Representació de la Terra i dades espacials
description: Forma de la Terra, coordenades, projeccions, sistemes de referència i geometries espacials.
lang: ca
ref: manual-earth-spatial-data
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/terra-dades-espacials/
weight: 50
part: Continguts
manual_references: true
---

La posició geogràfica introdueix una condició que no apareix en una taula o en un gràfic convencional: les dades han d'estar relacionades amb un model de la Terra. Aquest capítol presenta els conceptes necessaris per començar a treballar amb capes a QGIS sense convertir els sistemes de referència en codis opacs.

El vocabulari cartogràfic clàssic ajuda a entendre la representació, però per treballar amb capes digitals cal fixar també la terminologia dels sistemes d'informació geogràfica. El capítol combina una lectura cartogràfica general, una introducció específica als sistemes de coordenades i una referència terminològica en català {% cite jolyCartografia1982 vanSickleBasicGISCoordinates2017 nunesDiccionariSIG2012 %}.

## Modelar la forma de la Terra

### Geoide i el·lipsoide

La forma física de la Terra i el model matemàtic utilitzat per descriure-la no són exactament el mateix. Aquesta distinció ajuda a entendre per què existeixen diferents sistemes de referència. El **geoide** és una superfície vinculada al camp de gravetat que s'aproxima al nivell mitjà del mar i serveix de referència per a les altituds. L'**el·lipsoide de referència** és una superfície matemàtica regular que aproxima la forma terrestre i facilita els càlculs horitzontals.

En una secció meridiana, l'el·lipsoide es pot descriure mitjançant el semieix major equatorial $a$ i el semieix menor polar $b$. La diferència real entre tots dos és molt petita respecte de la mida de la Terra; la figura exagera l'aplanament per fer visibles els eixos. En fer girar aquesta secció al voltant de l'eix polar s'obté l'el·lipsoide de revolució utilitzat com a model de referència.

![Secció el·líptica amb el semieix major equatorial a i el semieix menor polar b]({{ site.baseurl }}/assets/img/coordinate-systems/ellipse-semi-axes.svg "Els semieixos a i b descriuen la secció d'un el·lipsoide de revolució; l'aplanament està exagerat. Adaptació de M. W. Toews, «Ellipse semi-major and minor axes», Wikimedia Commons, CC0 1.0."){: data-figure-width="25rem"}

### Dàtum i marc de referència

Les coordenades només tenen sentit quan es coneix respecte de quin model i marc s'han definit. El geoide descriu una superfície física; l'el·lipsoide n'ofereix una aproximació matemàtica; el **dàtum geodèsic** defineix com aquest model es relaciona amb la Terra; i el marc de referència en materialitza la realització mitjançant punts, coordenades i convencions de mesura. El **sistema de referència espacial** estableix com s'expressen i s'interpreten les posicions. Quan aquestes posicions es projecten sobre un pla, les coordenades passen a tenir unitats i propietats adequades per a determinades operacions.

Aquesta cadena explica per què dos parells de nombres no es poden comparar només per l'aparença. Una posició sense sistema de referència és incompleta, i un codi EPSG sense entendre les unitats i l'àrea d'ús tampoc no garanteix una operació correcta.

## Localitzar i mesurar

### Coordenades geogràfiques

La latitud i la longitud expressen posicions mitjançant unitats angulars. Valors com `1.1478406, 41.1026664` descriuen la posició de la Facultat de Turisme i Geografia amb l'ordre longitud–latitud. L'ordre no s'ha de deduir per intuïció: alguns formats i serveis utilitzen longitud–latitud, mentre que altres convencions mostren latitud–longitud.

![Dos globus mostren els paral·lels que determinen la latitud i els meridians que determinen la longitud]({{ site.baseurl }}/assets/img/coordinate-systems/latitude-longitude-earth.svg "La xarxa geogràfica permet expressar la latitud respecte de l'equador i la longitud respecte del meridià d'origen. Font: Djexplo, «Latitude and Longitude of the Earth», Wikimedia Commons, CC0 1.0.")

### Reticle UTM i coordenades projectades

Els sistemes projectats transformen la superfície terrestre en un pla i permeten treballar habitualment amb unitats mètriques. El sistema UTM divideix el món en seixanta zones de 6° de longitud. Catalunya es treballa habitualment dins de la zona 31N, compresa entre 0° i 6° E. En `ETRS89 / UTM zona 31N` (`EPSG:25831`), els eixos són **est** (*easting*, E) i **nord** (*northing*, N), en aquest ordre, i la unitat és el metre {% cite epsg25831 usgsUtmCoordinates2026 %}.

La coordenada UTM necessita més informació que els dos nombres. `EPSG:25831 · E 344.469 m · N 4.551.807 m` identifica el CRS, la component est i la component nord de la Facultat. El meridià central de la zona, 3° E, rep un **fals est** de 500.000 m; per això una E inferior a 500.000 situa el punt a l'oest del meridià central sense emprar valors negatius. A l'hemisferi nord, la N es compta des de l'equador amb un fals nord de 0 m. La lletra `N` de `31N` indica l'hemisferi i no s'ha de confondre amb les bandes de l'MGRS, un altre sistema de referència per quadrícula.

::: subfigures a+b "De la zona UTM al reticle local de Vila-seca. Esquemes propis basats en la definició d'ETRS89 / UTM zona 31N de l'EPSG i en conversions executades amb PROJ 9.4.0."
![Zona UTM 31N entre zero i sis graus est, amb el meridià central de tres graus est i Vila-seca a l'oest]({{ site.baseurl }}/assets/img/coordinate-systems/utm-zone-31n.svg "La zona 31N i el fals est de 500.000 m")
![Reticle UTM quilomètric amb tres llocs reals de Vila-seca i les seves coordenades est i nord]({{ site.baseurl }}/assets/img/coordinate-systems/utm-grid-vila-seca.svg "El reticle es llegeix primer cap a l'est i després cap al nord")
:::

::: table "Tres llocs de Vila-seca en coordenades geogràfiques i UTM"
| Lloc | Longitud, latitud (`EPSG:4326`) | E, N (`EPSG:25831`) |
| --- | --- | --- |
| Facultat de Turisme i Geografia | `1.1478406, 41.1026664` | `344469 m E, 4551807 m N` |
| Castell de Vila-seca | `1.1475084, 41.1146813` | `344469 m E, 4553142 m N` |
| Torre d'en Dolça | `1.1599211, 41.0989127` | `345474 m E, 4551369 m N` |
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

QGIS pot mostrar conjuntament capes amb sistemes diferents mitjançant una transformació temporal de visualització. Aquesta capacitat facilita l'exploració, però no canvia els fitxers d'origen ni resol automàticament quin sistema convé per mesurar o exportar. El CRS del projecte i el de cada capa s'han de revisar explícitament.

### Escala de treball

Els mapes municipals, comarcals i regionals requereixen nivells de detall i fonts cartogràfiques diferents. La capa més detallada no és sempre la més adequada: pot alentir el projecte i introduir formes impossibles de percebre a la mida final.

## Models de dades espacials

### Vector i ràster

El model vectorial representa entitats diferenciables mitjançant geometries i atributs. És adequat per a municipis, allotjaments, carreteres o itineraris. El model ràster divideix l'espai en cel·les i és habitual en ortofotos, models d'elevació, temperatura o cobertes derivades d'imatges. La resolució de la cel·la condiciona el detall observable i les operacions possibles.

El projecte comarcal utilitza polígons vectorials perquè cada municipi necessita una geometria vinculada a un codi i a una fila d'indicadors. Les ortofotos o altres ràsters poden aportar context, però no substitueixen els límits administratius necessaris per a la unió.

### Punts, línies i polígons

Els models vectorials representen objectes geogràfics mitjançant geometries. Un allotjament es pot representar com un punt; una ruta, com una línia; i un municipi, com un polígon. El tipus ha de correspondre al fenomen i a l'escala: convertir qualsevol objecte en un punt o una àrea pot ocultar propietats rellevants.

### Geometria i atributs

Cada entitat espacial combina una forma i un registre alfanumèric. Aquesta relació serà la base de les taules d'atributs i de les unions del capítol següent.

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

## Resultat del capítol

El resultat serà un únic projecte QGIS inicial amb la capa municipal de Catalunya, la comarca de treball identificada, sistemes de referència comprovats i una explicació breu de per què les dades espacials són adequades. El llibre de càlcul no es modificarà ni es duplicarà en aquesta fase. El capítol 5 reutilitzarà la clau municipal validada per unir-hi `map_export`; els indicadors no s'han de copiar manualment dins de la font espacial.
