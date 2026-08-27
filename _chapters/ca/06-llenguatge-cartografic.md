---
layout: manual-chapter
title: Llenguatge cartogràfic
description: Productes cartogràfics, escala, generalització, fotografia aèria, ortofotos, orientació, llegenda, retolació, jerarquia i composició del mapa.
lang: ca
ref: manual-cartographic-language
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/llenguatge-cartografic/
weight: 80
part: Continguts
manual_references: true
---

Un mapa no és una taula acolorida ni un gràfic col·locat sobre un territori. La posició de les entitats ve determinada per la geografia, i l'escala, la selecció i la generalització condicionen què pot mostrar-se. Aquest capítol aplica al mapa els criteris de semiologia i color treballats abans, continua el projecte QGIS que ja conté la base espacial i la unió municipal validades i prepara la cartografia temàtica. Les decisions cartogràfiques no són neutres: seleccionar, ometre, projectar, classificar i jerarquitzar condiciona el missatge que rep el lector {% cite jolyCartografia1982 monmonierHowLieMaps2018 %}.

>>>>> En acabar el capítol, cal poder construir i revisar un mapa de context que comuniqui la localització del territori amb una escala, una generalització i una composició justificades.
>>>>>
>>>>> - Distingir una imatge útil per observar el territori d'un producte adequat per mesurar o cartografiar.
>>>>> - Justificar l'escala, el detall i la generalització segons la funció i la mida final del mapa.
>>>>> - Organitzar símbols, retolació, llegenda, orientació, fonts de dades i crèdits amb una jerarquia llegible.
>>>>> - Construir i revisar a QGIS un mapa de context, i documentar els canvis entre la versió inicial i la final.

## Productes cartogràfics i funció del mapa

### Posició geogràfica i relacions espacials

La proximitat, la continuïtat, la forma i el veïnatge tenen significat territorial. No es poden reorganitzar lliurement com les categories d'un gràfic.

En un gràfic de barres, els municipis es poden ordenar de més a menys per facilitar una comparació. En un mapa, cada municipi ha de mantenir la posició, la forma i el contacte amb els veïns. Aquesta restricció redueix la precisió d'algunes comparacions quantitatives, però permet observar continuïtats, agrupacions i contrastos territorials que la taula no mostra.

### Mapes de referència, temàtics i turístics

Cada producte cartogràfic selecciona informació diferent. Un mapa turístic pot orientar, localitzar recursos o comunicar una anàlisi, i aquestes funcions no exigeixen la mateixa composició. Abans de discutir escala, relleu, llegenda o retolació, cal saber quin paper tindrà el mapa dins del treball.

::: table "Funció del mapa i informació prioritària"
| Tipus | Pregunta principal | Informació prioritària | Risc habitual |
| --- | --- | --- | --- |
| Referència | On és cada element? | Xarxa, poblament, relleu, límits i topònims | Acumular més detall del que permet l'escala |
| Temàtic | Com es distribueix una variable? | Patró de l'indicador, unitats territorials i llegenda | Fer que el context competeixi amb la variable |
| Localització | On se situa el territori d'estudi? | Extensió, entorn i jerarquia territorial | Convertir el requadre en un segon mapa complex |
| Turístic d'orientació | Com s'arriba als recursos i serveis? | Itineraris, accessos, punts d'interès i referències útils | Confondre promoció, orientació i anàlisi |
:::

## Productes d'imatge per observar i cartografiar el territori

Una imatge presa des de l'aire pot mostrar el territori amb molt detall sense tenir encara la geometria d'un mapa. La direcció de la càmera, la perspectiva, el relleu, la inclinació de la plataforma i el processament posterior condicionen què es pot identificar i què es pot mesurar. Aquesta distinció és necessària quan s'utilitzen fotografies històriques per estudiar l'evolució urbana i litoral, o una ortofoto actual com a fons per localitzar allotjaments, accessos i equipaments.

>>>>> Aquesta fase passa de la lectura visual d'una imatge a la valoració del seu ús com a font cartogràfica.
>>>>>
>>>>> - Diferenciar preses obliqües, fotogrames verticals, imatges georeferenciades i ortofotos a partir de la perspectiva i la correcció geomètrica.
>>>>> - Explicar per què georeferenciar una imatge no equival a ortorectificar-la.
>>>>> - Triar entre fotografia aèria, ortofoto i imatge de satèl·lit segons l'extensió, el detall i la pregunta territorial.
>>>>> - Verificar data, CRS, resolució, precisió, productor i condicions de reutilització abans de mesurar o comparar.

### Preses obliqües i verticals

Una **fotografia aèria obliqua** es pren amb l'eix òptic de la càmera inclinat respecte de la vertical. Ofereix una perspectiva semblant a la visió humana i fa visibles façanes, vessants i volums, però l'escala varia fortament entre el primer terme i el fons. En la classificació internacional utilitzada aquí, l'**obliqua baixa** no inclou l'horitzó i l'**obliqua alta** sí que l'inclou. La primera pot facilitar la identificació de formes i la segona proporciona una visió territorial més extensa, però cap de les dues no admet mesures planimètriques directes com un mapa {% cite baumannAerialPhotography2019 %}. El [catàleg de fotogrames aeris individuals de l'USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-aerial-photography-aerial-photo-single-frames) permet consultar aquest tipus de recurs.

Una **fotografia aèria vertical** es pren amb la càmera orientada tan a prop del nadir com permet la plataforma. Aquesta orientació facilita la fotogrametria i la cobertura sistemàtica, però la imatge continua sent una **projecció central**. Els elements elevats es desplacen radialment respecte del centre i poden mostrar part dels seus costats; la inclinació de la càmera i les diferències de relleu també alteren la posició i l'escala. Per tant, «vista des de dalt», «vertical», «georeferenciada» i «ortorectificada» no són sinònims.

El tema [*Aerial Photography: History and Georeferencing*](https://doi.org/10.22224/gistbok/2019.2.5) del GIS&T Body of Knowledge desenvolupa aquesta seqüència mitjançant definicions, història, ortorectificació, fotografia digital, resultats d'aprenentatge i temes relacionats. El DOI és l'enllaç estable; la plataforma actual també permet cercar altres temes, consultar-ne les connexions en un mapa de coneixement i obtenir una versió d'impressió.

![Capçalera, citació i definicions inicials del tema sobre fotografia aèria al GIS&T Body of Knowledge]({{ site.baseurl }}/assets/img/aerial-photography/gistbok-aerial-photography-2026-08-12.png "Consulta del tema DC-02-010, amb etiquetes, citació, DOI i definicions de fotogrametria, ortorectificació i georeferenciació. Captura pròpia de la interfície del GIS&T Body of Knowledge, UCGIS, 12 d'agost de 2026; fragment reproduït per a comentari docent. El contingut pertany a UCGIS i als autors del tema."){: data-figure-width="48rem"}

### Georeferenciació i ortorectificació d'imatges aèries

Un **fotograma** és una captura individual d'un vol fotogramètric abans de l'ortorectificació. Les passades es planifiquen amb solapament longitudinal i transversal perquè una part del territori aparegui en diverses imatges. Aquest recobriment evita buits, permet la visió estereoscòpica i contribueix a estimar el relleu i a construir mosaics.

La **georeferenciació** relaciona la imatge amb un sistema de coordenades mitjançant la posició de la càmera, punts de control o altres paràmetres. Permet situar-la aproximadament sobre altres capes, però no elimina per si sola els desplaçaments interns de la perspectiva. L'**ortorectificació** corregeix geomètricament la inclinació, la perspectiva i l'efecte del relleu mitjançant l'orientació de la càmera, punts de control i un model d'elevacions. El resultat, descrit amb més detall a la [documentació del PNOA sobre la generació d'ortofotos](https://pnoa.ign.es/web/portal/pnoa-imagen/generacion-de-ortofotos), és una imatge en projecció ortogonal amb una escala espacial controlada, apta per comparar posicions i efectuar mesures dins de la precisió declarada.

::: table "Fotografies aèries i productes derivats"
| Tipus o producte | Com s'obté | Tret de lectura | Ús i límit principal |
| --- | --- | --- | --- |
| Obliqua baixa | Càmera inclinada, sense horitzó visible | Perspectiva i laterals dels objectes | Identificar formes i volums; l'escala no és uniforme |
| Obliqua alta | Càmera inclinada, amb horitzó visible | Gran extensió des del primer terme fins al fons | Il·lustrar el paisatge i el context; no permet mesura planimètrica directa |
| Fotograma vertical | Càmera orientada aproximadament al nadir | Captura individual amb perspectiva central | Fotointerpretació i fotogrametria; conserva desplaçaments per relleu i inclinació |
| Fotograma georeferenciat | Fotograma associat a coordenades o punts de control | Se superposa aproximadament a altres capes | Localitzar i comparar; georeferenciar no equival a ortorectificar |
| Ortoimatge | Qualsevol imatge corregida a projecció ortogonal | Posició planimètrica i escala espacial controlades | Mesurar dins de la resolució i precisió documentades; pot procedir d'un avió, un satèl·lit o un altre sensor |
| Mosaic d'imatges de satèl·lit | Imatges de sensors orbitals processades i combinades | Cobertura territorial extensa i resolució més moderada | Observar formes, cobertes i dinàmiques ambientals; no confondre'l amb el detall d'una ortofoto aèria |
| Ortofoto o ortofotografia | Fotografia aèria ortorectificada | Detall fotogràfic amb geometria cartogràfica | Mesurar, digitalitzar i usar com a fons; continua necessitant data, resolució, CRS i precisió |
| Ortofotomosaic | Unió ajustada de diverses ortofotos | Cobertura contínua més gran que un fotograma | Consultar un territori extens; les peces poden correspondre a dates diferents |
| Ortofotomapa | Ortofoto o ortofotomosaic amb topònims, xarxes, límits o símbols cartogràfics | La imatge aporta el fons i les capes afegides en faciliten l'orientació | Comunicar i navegar; cal distingir la data de la imatge de la de les capes superposades |
:::

>>>> **Una fotografia vertical no es converteix en ortofoto només perquè encaixi aproximadament sobre un mapa.** La georeferenciació pot situar alguns punts correctament mentre altres continuen desplaçats. Per interpretar una mesura cal conèixer el processament, el CRS, la resolució, la precisió i la data de captació.

### Imatges de satèl·lit com a producte cartogràfic

Una imatge de satèl·lit també pot funcionar com a producte cartogràfic quan ha estat corregida, georeferenciada i distribuïda amb metadades. La diferència amb una ortofoto aèria no és només la plataforma, sinó el tipus de sensor, la resolució espacial, la freqüència de revisita, les bandes espectrals i el nivell de processament. Una ortofoto permet llegir voreres, edificis, camins o parcel·les amb molt detall; un mosaic Sentinel-2 pot mostrar de manera més sintètica formes litorals, aigües, arrossars, zones urbanes, camps i grans contrastos de coberta.

El delta de l'Ebre és un bon exemple perquè la forma del territori i els usos del sòl es reconeixen sense necessitat d'un zoom urbà: el riu, les badies, les barres litorals, les llacunes, la xarxa de canals i les parcel·les d'arròs formen un conjunt que es llegeix millor a escala regional. La figura següent prové d'una petició WMS a la capa `s2cloudless` d'[EOxCloudless](https://cloudless.eox.at/documentation/usage). És un mosaic sense núvols basat en dades Sentinel-2 de 2016, publicat sota CC BY 4.0 segons les [condicions de reutilització d'EOxCloudless](https://cloudless.eox.at/pricing) i la [llicència de dades Sentinel de Copernicus](https://cds.climate.copernicus.eu/licences/ec-sentinel), i no s'ha d'interpretar com una imatge d'última actualitat ni com una ortofoto de 25 o 50 cm.

![Imatge Sentinel-2 cloudless del delta de l'Ebre, amb el riu, les badies, les barres litorals, arrossars i zones urbanes principals]({{ site.baseurl }}/assets/img/aerial-photography/sentinel2-cloudless-delta-ebre-eox-2016.jpg "Imatge Sentinel-2 cloudless del delta de l'Ebre obtinguda mitjançant WMS. Font: EOxCloudless, EOX IT Services GmbH; conté dades Copernicus Sentinel modificades de 2016; llicència CC BY 4.0. Retall: 0,45-0,98° E i 40,52-40,86° N; consulta i incorporació: 17 d'agost de 2026."){: data-figure-width="48rem"}

La lectura ha de separar tres nivells. Primer s'identifica el marc tècnic: data, extensió, sensor, resolució i composició de bandes. Després es descriu allò que és visible (tons, textures, formes, vores i patrons) sense assignar-hi encara una causa. Finalment, aquestes evidències es contrasten amb cartografia, treball de camp o fonts temàtiques abans d'interpretar-les com a aigua, arrossars, teixit urbà o una transformació. Un color aparentment familiar orienta una hipòtesi, però no demostra per si sol una coberta ni un ús del sòl.

La mateixa lògica s'ha d'aplicar quan la consulta es fa des de QGIS: cal conservar la URL base del servei, la capa, el sistema de referència, l'extensió, la mida de sortida, el format i la data de consulta. Un WMS retorna una imatge generada pel servidor, no totes les bandes originals ni els valors radiomètrics necessaris per calcular índexs com l'índex de vegetació de diferència normalitzada (NDVI). Si la pregunta demana només lectura territorial i context visual, la imatge generada pot ser suficient; si demana anàlisi espectral, classificació de cobertes o mesures temporals, caldrà descarregar productes Sentinel amb el nivell de processament i les bandes adequades.

### Consultar una fototeca històrica

La [Fototeca Digital del CNIG](https://fototeca.cnig.es/) permet cercar una localització, seleccionar vols històrics i PNOA en una cronologia, mostrar els fotocentres, obrir fotogrames, regular-ne l'opacitat, comparar-los amb ortofotos i consultar o descarregar els productes disponibles. El CNIG conserva i distribueix el material, però cada vol pot tenir un productor i unes condicions d'atribució propis.

La captura mostra una consulta sobre Vila-seca, Salou i Tarragona. S'ha seleccionat el vol Americà B de 1956–1957 i el fotograma `PNOA-H_AMS_1956-57_33k_ES_comp_PAN_21mic_etrs89_UTM-hu31_H50_0472_fot_16089`, que apareix sobre l'ortofoto disponible com a fons el dia de la consulta. Els punts blaus representen fotocentres. La costa, els camins i les edificacions visibles al fotograma històric es poden contrastar amb el fons, però els contorns no coincideixen necessàriament: la [Fototeca Digital del CNIG adverteix](https://fototeca.cnig.es/) que els fotogrames històrics poden tenir una orientació aproximada i que, encara que estiguin georeferenciats, no són ortofotos.

::: subfigures a+b "Comparació de la mateixa extensió a la Fototeca Digital del CNIG. El fotograma històric es pot situar sobre l'ortofoto de fons, però conserva la geometria d'una fotografia en perspectiva. Captures pròpies, 12 d'agost de 2026. Vol Americà B, Ministeri de Defensa, CEGET, distribuït per IGN/CNIG; dades geogràfiques sota CC BY 4.0."
![Fotograma històric superposat a l'ortofoto de fons]({{ site.baseurl }}/assets/img/aerial-photography/fototeca-cnig-vila-seca-fotograma-1956-1957.png "Fotograma de 1956–1957 visible sobre el fons")
![Mateix enquadrament de Vila-seca, Salou i Tarragona amb el fotograma històric ocult]({{ site.baseurl }}/assets/img/aerial-photography/fototeca-cnig-vila-seca-ortofoto-2026-08-12.png "Mateix enquadrament amb l'ortofoto de fons")
:::

La consulta es pot reproduir cercant `Vila-seca`, activant **Fotogrames**, seleccionant **1956–1957 Americà B** i obrint un dels fotocentres pròxims. Abans d'utilitzar-ne el resultat s'han d'anotar el vol, l'identificador complet del fotograma, la data o interval, el productor, la resolució o escala, el sistema de referència, la llicència i la data de consulta. Una captura del visor documenta l'operació, però per analitzar o mesurar cal treballar amb el fitxer i les metadades corresponents.

### Google Maps i la vista d'imatges

[Google Maps](https://support.google.com/maps/answer/3092439?hl=ca&co=GENIE.Platform%3DDesktop) distingeix oficialment entre **Mapa**, que mostra vies, llocs i punts de referència, i **Satèl·lit**, que mostra imatges aèries. Aquesta etiqueta comercial no identifica el sensor ni garanteix per si sola que cada peça visible sigui una ortofoto amb resolució, data i precisió conegudes. Amb les etiquetes desactivades, es pot parlar de **vista d'imatges**; si s'hi superposen vies, topònims, límits i punts d'interès, és una **vista híbrida**. Només s'hauria d'anomenar ortofotomapa si la imatge de base és una ortofoto documentada i les capes cartogràfiques incorporades també es poden identificar. Una vista inclinada o un entorn 3D torna a introduir perspectiva i tampoc no és un ortofotomapa planimètric.

Per tant, el nom depèn del producte que es veu i de les capes actives, però també de la informació tècnica disponible. En una exploració quotidiana es pot parlar de vista d'imatges o vista híbrida. En un treball acadèmic, una mesura o una font de dades, cal preferir una ortofoto oficial amb data, CRS, resolució, precisió i condicions de reutilització documentades. Google Maps no és una font de dades obertes: la reproducció i la reutilització del contingut estan subjectes als límits de les [directrius geogràfiques de Google](https://about.google/brand-resource-center/products-and-services/geo-guidelines/) i exigeixen mantenir l'atribució a Google i, si escau, als proveïdors de dades; les directrius admeten alguns usos i en restringeixen d'altres.

### Street View i el paisatge vist des del carrer

Google Street View no és fotografia aèria: registra panorames des del nivell del carrer i, per tant, mostra façanes, voreres, arbrat, mobiliari, rètols, accessos i relacions entre l'espai públic i els edificis. Aquesta perspectiva complementa l'ortofoto. La vista zenital ajuda a reconèixer l'extensió i la forma del teixit urbà; la vista de carrer permet observar com aquest teixit es materialitza i com es percep a escala humana.

En alguns punts, l'opció de Street View [**Mostra més dates**](https://support.google.com/maps/answer/3093484?hl=ca&co=GENIE.Platform%3DDesktop) permet recuperar panorames d'anys diferents. La comparació pot revelar una nova urbanització, la reforma d'un carrer, el creixement dels arbres, canvis d'usos o transformacions d'un paisatge turístic. No obstant això, l'historial no està disponible a tot arreu, els intervals són irregulars i una diferència d'estació, hora, trànsit o posició de la càmera pot semblar un canvi territorial sense ser-ho.

Una exploració guiada pot partir d'aquest [panorama de l'entorn sud-est del nucli de Vila-seca](https://www.google.com/maps/@41.1074631,1.1453166,3a,75y,30.7h,90t/data=!3m6!1e1!3m4!1scbGZ8h5wToZfvBH_5i8XtA!2e0!7i16384!8i8192?hl=ca). Si la interfície ofereix **Mostra més dates**, se seleccionaran dos anys prou separats i es mantindran la mateixa posició, orientació i ampliació. El registre indicarà les dues dates i distingirà els canvis permanents, com l'edificació o la secció del carrer, dels elements conjunturals, com vehicles, obres provisionals, ombres o vegetació estacional.

Pel que fa específicament a Street View, les [directrius geogràfiques de Google](https://about.google/brand-resource-center/products-and-services/geo-guidelines/) permeten enllaçar o incrustar els panorames mitjançant les eines proporcionades, però no autoritzen captures fixes de Street View, la seva reproducció en llibres o manuals ni l'extracció de dades per digitalització o anàlisi automatitzada. Aquestes restriccions afecten les imatges de Street View i no s'han de generalitzar a tots els productes cartogràfics de Google, que tenen condicions pròpies. Per això el manual enllaça el panorama viu i no reprodueix una parella de captures. Les observacions serviran per formular hipòtesis qualitatives, que s'hauran de contrastar amb ortofotos oficials, cartografia, planejament o treball de camp abans d'afirmar un canvi.

## Escala i generalització

L'escala relaciona la mida del mapa amb el territori, mentre que la generalització adapta el detall a aquesta relació i a la funció de la peça. Les dues decisions s'han de comprovar conjuntament en la mida final.

>>>>> Aquesta fase converteix l'escala i el suport final en criteris per calcular, seleccionar i simplificar la informació.
>>>>>
>>>>> - Interpretar escales numèriques, gràfiques i verbals sense confondre escales grans i petites.
>>>>> - Calcular distàncies, superfícies i equivalències entre fulls després d'unificar les unitats.
>>>>> - Distingir coordenades angulars i unitats mètriques abans d'interpretar mesures o barres d'escala.
>>>>> - Aplicar selecció, simplificació, agregació, desplaçament o exageració segons la funció i l'escala.
>>>>> - Validar la llegibilitat i l'àrea mínima cartografiable a la mida d'exportació.

### Escala numèrica i gràfica

L'**escala cartogràfica** relaciona una distància representada al mapa amb la distància corresponent al territori i limita el detall que es pot llegir. A escala `1:100 000`, una unitat al mapa representa cent mil unitats al territori: un centímetre equival a un quilòmetre. Aquesta relació només és interpretable quan es coneixen la mida i el suport finals.

>> **Gran i petita descriuen la fracció.** Una escala `1:5 000` és més gran que `1:100 000` perquè la fracció `1/5 000` té més valor que `1/100 000`. En cartografia, «gran» no descriu ni el denominador ni l'extensió del territori, sinó la relació entre mapa i realitat: com més gran és l'escala, més detall pot mantenir el mapa en una mateixa mida final.

La mida final d'exportació forma part de la decisió. Ampliar el zoom de QGIS no augmenta l'espai disponible a la pàgina, i reduir posteriorment un mapa pot fer il·legibles etiquetes, traços i símbols. L'escala s'ha de comprovar dins de la composició, a la mida de publicació.

L'**escala gràfica** manté la relació visual quan el document es redimensiona proporcionalment; l'**escala numèrica** deixa de ser certa si la pàgina s'amplia o es redueix. En tots dos casos, el marc de mapa i el CRS del projecte han de permetre interpretar les distàncies correctament.

Una **escala verbal** expressa la relació amb paraules, per exemple «un centímetre representa un quilòmetre». En canvi, «mapa de detall municipal» o «mapa de context provincial» descriuen l'abast o la funció de la peça, no una escala. La forma verbal no substitueix l'escala numèrica o gràfica quan s'han de comprovar distàncies. En el treball del curs, l'escala s'ha de registrar juntament amb la mida final de la peça, perquè la mateixa composició exportada a una pàgina A4 o a una diapositiva no ofereix la mateixa lectura.

### Escales mètriques i escales en graus

Les equivalències d'una escala només són segures quan les unitats que es comparen són compatibles. En una composició projectada en metres, com ETRS89 / UTM 31N per a Catalunya, la barra d'escala pot expressar quilòmetres o metres perquè el sistema de coordenades ja treballa amb unitats lineals. En un sistema geogràfic, en canvi, les coordenades s'expressen en graus de latitud i longitud; un grau és una obertura angular sobre l'el·lipsoide, no una distància fixa sobre el mapa.

El recordatori geomètric és important. Les línies de latitud són **paral·lels** perquè envolten la Terra en plans paral·lels a l'equador i no s'intersequen entre elles. Les línies de longitud són **meridians**: uneixen els dos pols i tots coincideixen en aquests punts. Per això un grau de latitud es mesura com un arc nord-sud sobre un meridià, mentre que un grau de longitud es mesura com un arc est-oest sobre un paral·lel. Com més petit és el paral·lel, més curta és la distància corresponent al mateix angle de longitud.

La latitud i la longitud tampoc no es comporten igual. Un grau de latitud no val exactament sempre el mateix, perquè depèn de l'el·lipsoide i de la latitud, però la variació és petita: se situa al voltant de 111 km i pot usar-se com a aproximació docent. Un grau de longitud, en canvi, s'escurça molt cap als pols: prop de l'equador s'aproxima als 111 km, a la latitud del Camp de Tarragona, al voltant de 41° N, baixa a uns 84 km, i a 60° N és d'uns 56 km. Per això una retícula en graus no pot llegir-se com una regla mètrica uniforme. Si el mapa necessita mesurar recorreguts, àrees o zones d'influència, cal treballar amb un CRS projectat adequat a l'àrea i a l'ús, o documentar explícitament el mètode geodèsic emprat {% cite snyderMapProjections1987 vanSickleBasicGISCoordinates2017 %}.

![Esquema que compara escala numèrica, verbal i gràfica, i recorda que els graus de latitud es mesuren sobre meridians mentre que els graus de longitud es mesuren sobre paral·lels cada vegada més curts cap als pols]({{ site.baseurl }}/assets/img/cartographic-language/scale-types-and-degree-units.svg "Les formes habituals de l'escala poden ser equivalents en un mapa mètric, però una retícula en graus no és una regla uniforme: els paral·lels no s'intersequen, els meridians convergeixen als pols i la distància associada a un grau de longitud depèn de la latitud. Abans d'interpretar una barra d'escala, cal revisar la mida final, el CRS, les unitats i el mètode de mesura. Figura d'elaboració pròpia, 17 d'agost de 2026."){: data-figure-width="54rem"}

>>>> **Una escala en graus no és una escala en metres.** Si una capa o una captura mostra coordenades en graus, no s'han de calcular distàncies multiplicant graus per metres sense revisar la latitud, la projecció i el mètode de mesura. En QGIS, abans de confiar en una barra d'escala o en una mesura directa, cal comprovar el CRS del projecte i de les capes; per a treballs locals a Catalunya, un CRS projectat en metres acostuma a ser més adequat que una visualització en latitud i longitud.

### Càlculs d'escala

Els càlculs d'escala són una manera de comprovar si el mapa representa les magnituds amb coherència i si la composició final és viable. No són un exercici separat de la cartografia: permeten saber quina distància real correspon a una mesura sobre el paper, quina mida tindrà un element real en una pàgina, quina escala té una imatge quan es coneix una distància de referència i quants fulls a una escala més gran calen per cobrir l'extensió d'un full més general.

En una escala $1:n$, una unitat mesurada al mapa representa $n$ unitats al territori. La regla només funciona si les dues magnituds estan en la mateixa unitat abans d'operar. Si $D_m$ és la distància al mapa, $D_r$ la distància real i $n$ el denominador de l'escala, les relacions bàsiques són:

$$
D_r = D_m \cdot n
$$

$$
D_m = \frac{D_r}{n}
$$

$$
n = \frac{D_r}{D_m}
$$

Per calcular la distància real, es planteja la proporció entre una unitat al mapa i les unitats corresponents a la realitat. Per exemple, $2\cm$ en un mapa $1:50\,000$ representen $1\km$:

$$
\frac{1\cm}{50\,000\cm} = \frac{2\cm}{X\cm}
$$

$$
\frac{\cancel{1\cm}\cdot X\cm}{50\,000\cm}
=
\frac{2\cm\cdot\cancel{X\cm}}{\cancel{X\cm}}
$$

$$
\frac{X\cm\cdot\cancel{50\,000\cm}}{\cancel{50\,000\cm}}
=
2\cm\cdot50\,000
=
100\,000\cm
=
1\km
$$

En sentit invers, primer cal convertir la distància real a la unitat del mapa i després aïllar $X$. Una distància màxima de $728\m$ en un camp de golf, representada a $1:30\,000$, ocuparia $2{,}43\cm$ sobre el mapa:

$$
\frac{1\cm}{30\,000\cm}
=
\frac{X\cm}{728\m}
=
\frac{X\cm}{72\,800\cm}
$$

$$
\frac{\cancel{1\cm}\cdot72\,800\cm}{30\,000\cm}
=
\frac{X\cm\cdot\cancel{72\,800\cm}}{\cancel{72\,800\cm}}
$$

$$
X\cm
=
\frac{72\,800\cm}{30\,000}
=
2{,}43\cm
$$

Quan es desconeix l'escala, es construeix la fracció amb la mesura del mapa i la mesura real expressades en la mateixa unitat. Si $40\mm$ al mapa corresponen a $200\m$ reals, la relació es redueix a $1:5\,000$:

$$
\frac{40\mm}{200\m}
=
\frac{4\cm}{20\,000\cm}
=
\frac{\cancelto{1}{4\cm/4\cm}}{20\,000\cm/4\cm}
=
\frac{1\cancel{\cm}}{5\,000\cancel{\cm}}
$$

La mateixa operació permet detectar captures o reproduccions redimensionades: una escala numèrica impresa deixa de ser vàlida si la imatge s'ha ampliat o reduït sense recalcular-la.

Les superfícies segueixen la mateixa lògica, però amb el **quadrat de l'escala**. Si $A_m$ és l'àrea al mapa i $A_r$ l'àrea real, llavors:

$$
A_r = A_m \cdot n^2
$$

$$
A_m = \frac{A_r}{n^2}
$$

A escala $1:50\,000$, $18\cms$ al mapa no es resolen multiplicant una sola vegada pel denominador, sinó elevant-lo al quadrat; el canvi de dimensió és el punt important del càlcul:

$$
\frac{1\cms}{\left(50\,000\cm\right)^2}
=
\frac{18\cms}{X\cms}
$$

$$
X\cms
=
18\cms\cdot(50\,000)^2
=
45\,000\,000\,000\cms
=
4{,}5\squarekilometre
$$

Per passar d'una superfície real a una superfície sobre el mapa, es divideix pel quadrat del denominador. Així, $150\squarekilometre$ a $1:100\,000$ ocupen $150\cms$ al mapa:

$$
150\squarekilometre
=
1\,500\,000\,000\,000\cms
$$

$$
X\cms
=
\frac{1\,500\,000\,000\,000\cms}{(100\,000)^2}
=
150\cms
$$

El nombre de fulls també depèn del quadrat de la relació entre escales. Si un full a una escala $1:n_1$ es vol cobrir amb fulls del mateix format a una escala més gran $1:n_2$, el nombre ideal de fulls és:

$$
N = \left(\frac{n_1}{n_2}\right)^2
$$

Un full $1:50\,000$ genera quatre fulls $1:25\,000$, perquè cada costat es divideix en dues parts i la superfície total queda dividida en quatre. Amb el mateix criteri, un full $1:200\,000$ genera setze fulls $1:50\,000$:

$$
\frac{200\,000^2}{50\,000^2}
=
\left(\frac{200\,000}{50\,000}\right)^2
=
4^2
=
16
$$

En sèries cartogràfiques oficials poden existir talls, solapaments o convencions pròpies, però el càlcul mostra la relació geomètrica bàsica.

![Quatre esquemes de càlcul d'escala: distància del mapa a la realitat, distància real sobre el mapa, superfície calculada amb el quadrat del denominador i divisió d'un full en quatre fulls a escala més gran]({{ site.baseurl }}/assets/img/cartographic-language/scale-calculations.svg "Els càlculs d'escala permeten controlar distàncies, superfícies i equivalències entre fulls. En els tres primers panells, n és el denominador de l'escala 1:n: els panells 1 i 3 treballen a 1:50.000 i el panell 2, a 1:25.000; en el quart, n₁ i n₂ són els denominadors comparats i N és el nombre de fulls. Els marcs de realitat s'han exagerat respecte dels marcs de mapa per diferenciar-los i no guarden una proporció gràfica. El segon panell representa una distància recta entre dos punts, no un itinerari sinuós ni una deformació causada per la projecció. Figura d'elaboració pròpia, revisada el 23 d'agost de 2026."){: data-figure-width="54rem"}

::: table "Càlculs d'escala que s'han de dominar"
| Tipus de càlcul | Operació | Resultat de control |
| --- | --- | --- |
| Distància real a partir del mapa | $5\cm$ a $1:50\,000$ | $5\cm\cdot50\,000=250\,000\cm=2{,}5\km$ |
| Distància real a partir del mapa | $20\cm$ a $1:30\,000$ | $20\cm\cdot30\,000=600\,000\cm=6\,000\m$ |
| Distància al mapa a partir de la realitat | $650\km$ a $1:1\,000\,000$ | $\frac{65\,000\,000\cm}{1\,000\,000}=65\cm$ |
| Distància al mapa a partir de la realitat | $728\m$ a $1:30\,000$ | $\frac{72\,800\cm}{30\,000}=2{,}43\cm$ |
| Escala desconeguda | $24\cm$ al plànol i $156\m$ reals | $\frac{24\cm}{15\,600\cm}=\frac{1}{650}$ |
| Escala gràfica | $10\cm$ representen $10\,000\m$ | $\frac{10\cm}{1\,000\,000\cm}=\frac{1}{100\,000}$ |
| Superfície real | $18\cms$ a $1:50\,000$ | $18\cms\cdot50\,000^2=4{,}5\squarekilometre$ |
| Superfície al mapa | $150\squarekilometre$ a $1:100\,000$ | $\frac{1\,500\,000\,000\,000\cms}{100\,000^2}=150\cms$ |
| Fulls equivalents | De $1:200\,000$ a $1:50\,000$ | $\left(\frac{200\,000}{50\,000}\right)^2=16$ fulls |
| Fulls equivalents | De $1:500\,000$ a $1:25\,000$ | $\left(\frac{500\,000}{25\,000}\right)^2=400$ fulls |
:::

>>>> **No es barregen unitats dins d'una regla de tres.** Abans de calcular cal convertir metres, quilòmetres, mil·límetres o hectàrees a una unitat coherent. En distàncies es treballa amb unitats lineals; en superfícies, amb unitats quadrades. També cal recordar que les mesures calculades sobre un mapa només són fiables dins de les condicions del producte: projecció, escala, resolució, precisió i mida final.

### Seleccionar, simplificar i jerarquitzar

La **generalització cartogràfica** adapta la informació a l'escala i al propòsit del mapa mitjançant selecció, simplificació, combinació, desplaçament o exageració. Generalitzar no és eliminar informació arbitràriament, sinó conservar-ne el sentit essencial a la mida prevista.

#### Comparar diverses escales

Una mateixa geometria municipal es pot observar en una composició provincial, comarcal o local. A l'escala provincial interessa la forma general i la situació de la comarca; a l'escala comarcal es poden distingir els municipis; a una escala local pot ser necessari incorporar carreteres, nuclis o altres elements. Mostrar el mateix detall en els tres casos produeix soroll o una falsa sensació de precisió.

El canvi d'escala no és només reduir una imatge. Si tres mapes ocupen la mateixa mida de paper o de pantalla, el mapa d'escala més petita cobreix molt més territori dins del mateix marc. Això comprimeix carrers, parcel·les, topònims i petits polígons fins que deixen de ser llegibles. La generalització comença aquí: abans de decidir quina operació concreta s'aplica, cal entendre quina informació encara pot funcionar a la nova escala.

![Tres mapes de la mateixa mida final a escala local, comarcal i regional, amb menys detall i més simbolització a mesura que l'extensió representada creix]({{ site.baseurl }}/assets/img/cartographic-language/generalization-three-scales.svg "La generalització és una resposta al canvi d'escala: amb la mateixa mida de sortida, cada marc cobreix una extensió real diferent i obliga a seleccionar, simplificar, agregar o simbolitzar el detall. Figura d'elaboració pròpia, 17 d'agost de 2026."){: data-figure-width="54rem"}

#### Decidir què es conserva

La generalització pot seleccionar els elements necessaris, simplificar formes massa detallades, combinar categories, desplaçar símbols que se superposen o exagerar elements que desapareixerien. Cada operació ha de conservar la funció territorial del mapa. En l'esquema següent, la font es mostra a una escala més gran i en un marc més ampli que les sortides generalitzades. Els punts buits dels panells de desplaçament i exageració indiquen la posició original; les línies de crida permeten veure que el símbol s'ha acostat deliberadament a la carretera. En el mapa de context del projecte, els municipis i la comarca són essencials; una xarxa viària exhaustiva o una ortofoto detallada no ho són.

![Operacions principals de generalització cartogràfica comparades entre una font detallada gran i cinc sortides més petites]({{ site.baseurl }}/assets/img/cartographic-language/generalization-operations.svg "La font detallada es presenta en un marc gran a 1:10.000, mentre que les cinc sortides ocupen marcs més petits a 1:20.000: el canvi d'escala redueix l'espai disponible per al detall. La selecció omet elements; la simplificació redueix vèrtexs; l'agregació crea un polígon envoltant a partir dels habitatges; i el desplaçament i l'exageració acosten símbols a la carretera, amb una línia de crida fins a la posició original. L'esquema docent no deriva d'una capa real. Figura d'elaboració pròpia, revisada el 23 d'agost de 2026."){: data-figure-width="54rem"}

#### Automatitzar sense renunciar al criteri

La generalització pot incorporar un component artístic o experimental quan s'exploren formes, jerarquies i graus d'exageració per comunicar millor un territori. Aquest marge no significa que totes les decisions hagin de ser manuals o intuïtives. Una part del procés es pot automatitzar amb regles geomètriques reproduïbles, sempre que el paràmetre, l'escala de sortida i els elements que s'han de conservar continuïn responent a la funció del mapa. La caixa d'eines de processos de QGIS inclou operacions per simplificar geometries, calcular envolupants, suavitzar, dissoldre, agregar o eliminar detalls; el nom concret i les opcions poden variar segons la versió i el proveïdor de l'algorisme.

L'algorisme de **Douglas-Peucker** simplifica una línia a partir d'una tolerància. Primer uneix els dos extrems amb un segment i busca el vèrtex intermedi amb la distància perpendicular màxima. Si aquesta distància supera la tolerància, conserva el vèrtex i repeteix el test als dos fragments; si no la supera, elimina els vèrtexs intermedis. La tolerància s'expressa en les unitats de la capa, de manera que cal conèixer el CRS i treballar amb una unitat adequada abans d'interpretar-la com metres. Un valor més gran produeix menys vèrtexs, però també pot deformar revolts, desplaçar límits o crear problemes de continuïtat entre geometries veïnes.

L'**envolupant convexa** resol una operació diferent: calcula el polígon convex més petit que conté tots els objectes seleccionats. Pot proporcionar una agregació exterior ràpida d'un conjunt d'habitatges, però no reconstrueix el teixit urbà ni detecta buits interns; el polígon també pot incloure espais sense edificis. La figura següent aplica les dues operacions a geometries didàctiques i fa visible què aporta cada algorisme i què encara ha de decidir la persona que construeix el mapa.

![Douglas-Peucker i envolupant convexa com a exemples d'operacions automatitzables de generalització cartogràfica]({{ site.baseurl }}/assets/img/cartographic-language/generalization-algorithms.svg "Douglas-Peucker conserva els vèrtexs que superen una tolerància de distància, mentre que l'envolupant convexa calcula el polígon convex mínim que conté els habitatges. Cap dels dos resultats es pot acceptar sense considerar l'escala, la funció, la topologia i la mida final. Geometries sintètiques i figura d'elaboració pròpia."){: data-figure-width="54rem"}

#### Comprovar el suport final

La generalització s'ha de revisar primer al 100% de la mida d'exportació, és a dir, amb la pàgina, la imatge o la diapositiva a la mida en què la rebrà el lector. Aquesta vista permet comprovar si la jerarquia funciona, si els símbols es poden distingir i si les etiquetes es llegeixen sense ampliar. Si un detall només es percep fent molt de zoom, no forma part efectiva del mapa publicat. Abans de reduir totes les etiquetes o tots els traços, convé retirar informació secundària.

El zoom compleix una altra funció: serveix per diagnosticar problemes que la vista normal oculta. En una exportació ràster, dos trams separats per un sol píxel poden semblar units al 100% a causa de la mida del traç, l'antialiàsing i la percepció visual. Quan s'amplia la quadrícula de píxels, la separació es fa evident. En un PDF o un SVG vectorial no hi ha una quadrícula de píxels fixa, però l'ampliació també permet inspeccionar els extrems i comprovar si les geometries coincideixen realment.

![Comparació entre dues línies que semblen unides a la mida final i un zoom de diagnosi que mostra un píxel buit entre els extrems]({{ site.baseurl }}/assets/img/cartographic-language/final-output-inspection.svg "La lectura al 100% i el zoom de diagnosi responen a preguntes diferents. A la mida final, els dos trams de l'exemple semblen formar una línia contínua; a l'ampliació de la mateixa exportació ràster, un píxel buit demostra que els extrems no coincideixen. Si els trams han de formar una xarxa, cal ajustar la geometria i validar-ne la topologia; si només formen part de la composició, la decisió de llegibilitat s'ha de prendre a la mida de publicació. Figura d'elaboració pròpia, 23 d'agost de 2026."){: data-figure-width="54rem"}

L'aparença, per tant, no substitueix la comprovació geomètrica. Si els dos trams representen una carretera, un itinerari o una xarxa que ha de ser contínua per a l'anàlisi, els extrems han de coincidir i cal validar la topologia o l'ajustament de QGIS. El zoom localitza el defecte; la vista al 100% permet decidir si la correcció, la simplificació o la retirada de detall produeix un mapa final clar.

#### Àrea mínima cartografiable

L'**àrea mínima cartografiable** és la superfície més petita que es pot representar de manera llegible i significativa a una escala i una mida de sortida determinades. També pot aparèixer com a **unitat mínima cartogràfica** o, en anglès, *minimum mapping unit* (**MMU**). No és una propietat absoluta de la font, sinó una relació entre detall, suport i funció. Una capa pot contenir polígons petits perfectament reals, però si a la composició final ocupen una taca imperceptible, el lector no els podrà distingir ni interpretar. L'AMC no diu que l'element no existeixi; diu que aquest mapa concret no el pot mostrar com una unitat superficial independent sense enganyar la lectura.

El llindar perceptiu és una pista important, però no és tota la decisió. En condicions ideals, l'ull humà pot separar detalls molt petits; en cartografia, però, no es tracta només de detectar una ratlla, sinó de reconèixer una forma, distingir-la del contorn veí, associar-la a una llegenda i llegir-la dins d'una composició carregada. Les guies de dimensions mínimes cartogràfiques acostumen a moure's al voltant de $0{,}2\mm$ per a separacions o traços bàsics a una distància de lectura d'uns $30\cm$, i recomanen valors més grans quan cal discriminar símbols, colors, textos o àrees. Un valor com $0{,}02\mm$ és massa petit per decidir l'AMC d'un mapa publicat: pot tenir sentit com a ordre de reproducció tècnica o de resolució instrumental, però no com a criteri docent de llegibilitat cartogràfica {% cite ledermannMinimumDimensionsCartographic2023 %}.

El càlcul comença sempre en la mida final del mapa. Si s'adopta una dimensió mínima $d_m$ en mil·límetres sobre el paper o sobre l'exportació, i l'escala és $1:n$, la dimensió real equivalent és:

$$
D_r = \frac{d_m \cdot n}{1\,000}
$$

on $D_r$ queda expressada en metres. Si el criteri és un quadrat mínim de costat $d_m$, l'àrea real equivalent és:

$$
A_r = \left(\frac{d_m \cdot n}{1\,000}\right)^2
$$

Si el criteri ja es defineix com una superfície mínima sobre el mapa, $a_m$, expressada en $\mm^2$, la conversió directa a hectàrees és:

$$
A_{r,ha} = \frac{a_m \cdot n^2}{10^{10}}
$$

La diferència entre un llindar gràfic i una AMC realista es veu de seguida. A escala $1:50\,000$, una separació de $0{,}2\mm$ equival a $10\m$ sobre el terreny, però això només indica una mida perceptiva elemental. Si es vol que un polígon temàtic tingui una taca prou clara, un criteri de $5\mm \times 5\mm$ equival a $250\m \times 250\m$, és a dir, $6{,}25\hectare$. Amb $6\mm \times 6\mm$, l'AMC puja a $9\hectare$.

::: table "De la mida gràfica a l'àrea mínima sobre el terreny"
| Criteri sobre el mapa final | Lectura prudent | A $1:50\,000$ | A $1:100\,000$ |
| --- | --- | --- | --- |
| $0{,}2\mm \times 0{,}2\mm$ | Llindar gràfic elemental; no és una AMC per a polígons | $10\m$ de costat; $0{,}01\hectare$ | $20\m$ de costat; $0{,}04\hectare$ |
| $1\mm \times 1\mm$ | Taca molt petita, útil només si el mapa és net i l'element és simple | $50\m$ de costat; $0{,}25\hectare$ | $100\m$ de costat; $1\hectare$ |
| $5\mm \times 5\mm$ | Criteri conservador per a polígons temàtics llegibles | $250\m$ de costat; $6{,}25\hectare$ | $500\m$ de costat; $25\hectare$ |
| $6\mm \times 6\mm$ | Criteri encara més prudent quan cal delinear bé taques petites | $300\m$ de costat; $9\hectare$ | $600\m$ de costat; $36\hectare$ |
:::

En cartografia professional, aquesta decisió acostuma a quedar fixada en les especificacions del producte o en les metadades: escala de publicació, mida de sortida, tipus de lector, densitat d'informació, contrast, símbols i AMC adoptada. Després es treballa sobre una capa de sortida, sense destruir la font detallada. Els polígons per sota del llindar es poden eliminar si són secundaris, dissoldre amb unitats veïnes, agregar dins d'una classe més general, simplificar si el problema és només l'excés de vèrtexs, o substituir per un símbol puntual si són essencials per al missatge. En un mapa digital amb diversos nivells de zoom, no hi ha una sola AMC per a tot el visor: cada nivell d'escala necessita la seva pròpia regla de visibilitat i generalització.

La decisió, per tant, pot resoldre's de tres maneres principals. Si l'element és secundari, s'omet. Si forma part d'una categoria més gran, s'agrupa. Si és essencial per al missatge, es pot exagerar o representar amb un símbol, però llavors cal acceptar que la mida ja no correspon exactament a la superfície real. En tots els casos, la generalització ha d'estar justificada per la lectura final i no per la comoditat del programa.

La figura següent aplica un criteri docent de $5\mm \times 5\mm$ a una sortida comarcal a escala $1:250\,000$. El quadrat equival a $1\,250\m$ de costat i a $156{,}25\hectare$. Les divisions municipals de l'ICGC contenen sis components més petits que aquest llindar: tres de Perafort, dos del Morell i un del Catllar. La sortida no afirma que aquests fragments hagin desaparegut ni que sempre es puguin eliminar; els substitueix per símbols perquè continuïn sent visibles en un mapa comarcal. Si la funció és consultar-ne el límit administratiu exacte, la solució correcta és una ampliació o una escala més gran.

![Aplicació de l'àrea mínima cartografiable a sis components municipals petits del Tarragonès]({{ site.baseurl }}/assets/img/cartographic-language/minimum-mapping-unit-tarragones.svg "La font conserva sis components de Perafort, el Morell i el Catllar per sota de 156,25 ha. En la sortida a 1:250.000 es canvia la marca superficial per un símbol puntual visible; no s'elimina l'existència del territori. Si cal consultar-ne la forma exacta, cal ampliar el mapa. Dades: divisions administratives de l'ICGC de 20 de gener de 2026, CC BY 4.0."){: data-figure-width-web="38rem" data-figure-width-pdf="90%"}

## Informació de base i relleu

### Planimetria i altimetria

Un cop fixada la funció del mapa i l'escala de treball, es pot decidir quina informació de base ajuda a llegir el territori. La **planimetria** representa elements en posició horitzontal, com límits, nuclis, carreteres, costa o hidrografia. L'**altimetria** descriu el relleu mitjançant cotes, corbes de nivell, ombrejat o tintes hipsomètriques. Totes dues poden proporcionar context, però el seu nivell de detall ha de respondre al propòsit del mapa.

En el mapa comarcal, els límits i alguns topònims ajuden a localitzar els municipis. Un relleu detallat o una xarxa viària completa podrien competir amb aquesta funció. Només s'incorporaran si aporten una referència necessària per interpretar la localització; altrament, s'ometran com a part de la generalització.

El relleu és especialment delicat perquè pot donar molta estructura visual sense formar part de la variable principal. Les cotes aporten valors puntuals; les corbes de nivell mostren forma i pendent; l'ombrejat fa intuïtiu el volum, però pot semblar una font de llum real; i les tintes hipsomètriques ordenen rangs d'altura, però introdueixen una paleta que pot competir amb una coropleta. Per comparar aquests recursos sense atribuir les diferències a terrenys distints, la figura següent aplica cotes, tintes i ombrejat a `volcano`, un petit conjunt de dades d'exemple inclòs amb el llenguatge R que representa una malla d'altituds de Maunga Whau. S'utilitza perquè permet mantenir el terreny constant, no perquè l'estudiant hagi de treballar amb R ni perquè sigui una font adequada per mesurar el volcà. En un mapa temàtic municipal, l'altimetria només s'ha d'afegir si ajuda a explicar un patró territorial, com una diferència entre litoral i interior, i no només perquè el mapa sembli més complet.

![Tres representacions del mateix model d'altituds de Maunga Whau: cotes puntuals, tintes hipsomètriques i ombrejat del relleu]({{ site.baseurl }}/assets/img/cartographic-language/terrain-relief-volcano.svg "Les cotes donen valors en punts concrets; les tintes hipsomètriques codifiquen l'altitud amb una rampa ordenada; i l'ombrejat simula una il·luminació amb azimut 315° i altura 40°, però no proporciona una altura exacta. Dades: conjunt volcano de Maunga Whau, una malla de 10 m digitalitzada per Ross Ihaka i no apta per a mesures precises."){: data-figure-width="54rem"}

### Corbes de nivell i formes del relleu

Una **corba de nivell** uneix punts que tenen la mateixa altitud. En un mapa topogràfic, aquestes línies acostumen a dibuixar-se en color sèpia o marró perquè el relleu quedi diferenciat de la hidrografia, la vegetació, els camins i la retolació. Les **corbes mestres** apareixen més gruixudes i sovint etiquetades amb la cota; serveixen per no perdre el recompte vertical. Entre dues corbes mestres hi ha corbes normals o intermèdies, separades per una **equidistància** constant que cal llegir a la llegenda del mapa. Si l'equidistància és de 10 m, cada corba normal representa un canvi de 10 m d'altitud; si és de 20 m, el salt és de 20 m. La distància visual entre línies, en canvi, no és l'equidistància: quan les corbes estan molt juntes el pendent és més fort, i quan s'allunyen el pendent és més suau.

La figura següent separa aquestes dues distàncies. L'equidistància és el salt vertical constant entre corbes; l'espai dibuixat entre línies correspon a una distància horitzontal i varia amb el pendent. El model esglaonat de l'esquerra mostra els talls horitzontals d'un mateix relleu, i la vista zenital de la dreta en conserva la forma com a línies sobre el mapa.

![Formació i lectura de les corbes de nivell a partir de talls horitzontals d'un relleu]({{ site.baseurl }}/assets/img/cartographic-language/contour-lines-reading-guide.svg "Els talls horitzontals, separats per una equidistància de 20 m, es projecten com a corbes de nivell sobre el mapa. La separació gràfica entre corbes és més gran al vessant suau i més petita al vessant fort. Elaboració pròpia."){: data-figure-width-web="54rem" data-figure-width-pdf="100%"}

La forma de les corbes també informa sobre el drenatge. En un barranc o una vall, les corbes tendeixen a entrar cap amunt en forma de `V` o de `U`: el terreny és **còncau** i el flux d'aigua es concentra cap a l'eix de la depressió. En una cresta o un esperó, la forma s'obre cap avall i el terreny és **convex**: l'aigua es dispersa cap als dos vessants. Aquesta lectura no substitueix una xarxa hidrogràfica ni un model digital d'elevacions, però permet reconèixer lògiques bàsiques del relleu abans d'afegir més capes.

Un **perfil topogràfic** trasllada a una vista lateral les altituds recorregudes per un transsecte dibuixat sobre el mapa. Cada vegada que la línia `A–A′` talla una corba de nivell, el perfil passa per aquella mateixa cota; entre interseccions, la forma depèn de les altituds disponibles i del mètode d'interpolació. En l'exemple calculat, els punts marrons marquen els creuaments amb intervals de 10 m. Els eixos horitzontal i vertical no comparteixen la mateixa escala gràfica, de manera que el perfil exagera visualment l'altura i no s'ha d'interpretar com una secció amb proporció `1:1`.

![Corbes de nivell de Maunga Whau amb un transsecte A–A′ i el perfil topogràfic calculat sobre la mateixa línia]({{ site.baseurl }}/assets/img/cartographic-language/contour-profile-volcano.svg "El mapa utilitza una equidistància de 10 m i reforça com a mestres les corbes cada 50 m. A la dreta, el perfil recorre el mateix transsecte i assenyala les interseccions amb cada cota; l'escala vertical està exagerada respecte de l'horitzontal. Dades: conjunt volcano de Maunga Whau, digitalitzat per Ross Ihaka i no apte per a mesures precises."){: data-figure-width="54rem"}

El retall següent mostra l'entorn de l'Estany de Montcortès en la [cartografia topogràfica del Servei de Mapa Base de l'ICGC](https://www.icgc.cat/ca/Geoinformacio-i-mapes/Servei-de-Mapa-Base). La convenció cromàtica ajuda a separar les corbes de nivell sèpia, la hidrografia blava, les masses de vegetació verdes, les vies grises i els topònims.

![Retall topogràfic de l'Estany de Montcortès amb corbes de nivell, cotes, hidrografia, vegetació i topònims]({{ site.baseurl }}/assets/img/cartographic-language/contour-lines-montcortes.png "Retall topogràfic de l'entorn de l'Estany de Montcortès. Font cartogràfica: Institut Cartogràfic i Geològic de Catalunya, cartografia topogràfica de Catalunya. Llicència: pendent de revisar."){: data-figure-width="54rem"}

>>> **Estimar l'altitud de l'Estany de Montcortès.** Per llegir l'altitud de l'estany no n'hi ha prou amb mirar el color blau de l'aigua. Primer cal identificar una corba mestra propera, com la de `1.050 m`, deduir l'equidistància entre corbes i comptar cap a la riba. Si la làmina d'aigua queda entre dues corbes consecutives, el mapa només permet afirmar un interval: l'altitud és més alta que la corba inferior i més baixa que la corba superior. Un valor com `1.030 m` pot ser una estimació raonada si la lectura de les corbes porta a aquest entorn, però no s'ha de presentar com una dada exacta obtinguda del mapa. L'altitud que el mapa declara directament, sempre dins de la precisió de la font, només correspon a una cota puntual, una consulta altimètrica documentada o els punts pels quals passa una corba de nivell concreta; entre dues corbes, el relleu s'interpreta dins d'un rang.

## Símbols, textos i elements auxiliars del mapa

Els elements auxiliars i la retolació només aporten informació quan responen a la funció, l'orientació i la jerarquia de la composició. Aquesta fase prepara una revisió sistemàtica abans de maquetar el mapa de context.

>>>>> Aquesta fase organitza els signes, textos i elements auxiliars perquè el lector pugui localitzar, descodificar i verificar el mapa.
>>>>>
>>>>> - Relacionar símbols puntuals, lineals i superficials amb el fenomen representat i la variable visual adequada.
>>>>> - Redactar un títol i una llegenda que identifiquin el territori, la funció i els codis necessaris sense redundàncies.
>>>>> - Decidir si calen escala gràfica i indicació del nord segons les mesures, la rotació i les referències disponibles.
>>>>> - Jerarquitzar i col·locar topònims sense col·lisions ni associacions territorials ambigües.
>>>>> - Comprovar fonts, període, autoria, CRS, crèdits i llegibilitat en la mida final.

### Títol i subtítol

El títol ha d'identificar el propòsit, la variable o el territori i, quan sigui necessari, el període o la unitat. No ha de repetir literalment tota la llegenda. En un mapa de context pot ser suficient «El Tarragonès dins de la província de Tarragona»; en un mapa temàtic caldrà identificar també l'indicador i l'any.

### Símbols cartogràfics i convencions

Els símbols cartogràfics apliquen les variables visuals sobre tres formes d'implantació: **puntual**, **lineal** i **superficial**. Un allotjament, un museu o una estació poden aparèixer com a símbols puntuals; una carretera, un itinerari o un riu, com a símbols lineals; i un municipi, una zona urbana o una coberta del sòl, com a símbols superficials. Aquesta implantació no és només una qüestió geomètrica: condiciona quina variable visual serà llegible. La mida funciona d'una manera en un cercle puntual, d'una altra en l'amplada d'una línia i d'una altra en una àrea de color.

La relació entre el signe i el fenomen també pot variar. Un símbol **arbitrari** no s'assembla al que representa i necessita una llegenda clara. Un símbol **associatiu** aprofita algun tret recognoscible, com una forma, un color o una textura que evoca el fenomen. Un símbol **convencional** depèn d'un acord compartit, sovint repetit en sèries cartogràfiques, institucions o pràctiques professionals. En la pràctica, molts símbols combinen aquestes tres dimensions: el blau d'un riu és associatiu perquè recorda l'aigua, però també és convencional perquè el lector l'ha après en molts mapes.

![Esquema de símbols cartogràfics arbitraris, associatius i convencionals aplicats a implantació puntual, lineal i superficial]({{ site.baseurl }}/assets/img/cartographic-language/map-symbols-relationships.svg "Els exemples són esquemàtics: el bosc s'associa a la vegetació mitjançant un color verd pla, els fruiters utilitzen una retícula agrícola regular i la pedrera, el símbol de martell i pic. Els signes poden combinar semblança, convenció i decisió gràfica, i funcionar de manera diferent segons si la implantació és puntual, lineal o superficial. Figura d'elaboració pròpia, revisada el 23 d'agost de 2026."){: data-figure-width="54rem"}

### Llegenda

La **llegenda** explica el significat dels símbols, les classes i les unitats utilitzades. Només ha d'incloure els elements que necessiten descodificació i que apareixen realment al mapa. L'ordre ha de seguir la lògica visual o conceptual de la simbologia, i les etiquetes automàtiques s'han de substituir per expressions comprensibles.

Un límit municipal evident pot no necessitar una entrada de llegenda si el títol i la composició ja n'aclareixen la funció. En canvi, una diferència entre comarca d'estudi, resta de la província i territoris exteriors necessita una explicació si no es pot deduir amb seguretat.

La posició de la llegenda forma part de la lectura. Situar-la fora del marc conserva íntegra la geografia, però consumeix pàgina i pot allunyar-la dels símbols. Col·locar-la dins del mapa redueix aquest recorregut si aprofita un espai realment buit, com una zona de mar sense informació o un marge intern. L'espai negatiu no és automàticament espai disponible: pot contenir una illa petita, una ruta, un topònim, una absència significativa o el context necessari per entendre la costa. Abans de superposar-hi la llegenda cal inspeccionar totes les capes i la mida final {% cite tynerPrinciplesMapDesign2010 brewerDesigningBetterMaps2005 %}.

![Tres ubicacions d'una llegenda cartogràfica: fora del marc, dins d'un espai de mar buit i sobre informació territorial rellevant]({{ site.baseurl }}/assets/img/cartographic-language/map-legend-placement.svg "La llegenda exterior preserva el mapa però ocupa pàgina; la llegenda interior pot aprofitar espai negatiu verificat; la col·locació problemàtica tapa entitats i altera la lectura. Els tres mapes utilitzen geometria i simbologia sintètiques. Figura d'elaboració pròpia."){: data-figure-width="54rem"}

La llegenda s'ha de llegir en relació amb el mapa, no com una taula independent. Una rampa seqüencial ha de mantenir el mateix sentit clar-fosc que les classes cartografiades; els símbols proporcionals necessiten valors de referència; i els casos sense dades o no aplicables han de quedar separats del zero. Si la llegenda exigeix una explicació llarga per desfer abreviatures, decimals o noms de camps del programari, primer cal reescriure'n les etiquetes i simplificar la simbologia.

### Orientació, escala, fonts i crèdits

Els elements auxiliars s'inclouran quan compleixin una funció. Una fletxa del nord pot ser redundant en un mapa convencional orientat al nord i sense rotació. Una escala gràfica és útil quan cal estimar distàncies o quan el document es pot redimensionar. Cap element s'ha d'afegir només perquè aparegui entre les opcions de QGIS.

La font de dades, el període o versió, l'autoria i, quan sigui rellevant, el CRS són necessaris per interpretar i revisar el producte. Cal distingir la font de les geometries de la font dels indicadors: aquest capítol utilitza principalment la base espacial, mentre que el mapa temàtic incorporarà també les dades estadístiques.

#### Per què ens «orientem»?

La paraula **orientar-se** recorda que la referència històrica no era el nord, sinó l'**orient** o llevant. *Orient* prové del llatí *oriens*, «que neix o s'aixeca», en referència al Sol. El [*Diccionari català-valencià-balear* defineix *orient*](https://dcvb.iec.cat/results.asp?word=orient) com el punt de l'horitzó per on surt el Sol i explica *orientar* com situar una cosa o una persona respecte dels punts cardinals. Orientar-se era, doncs, trobar primer la direcció de l'orient; un cop establert l'eix est-oest, es podien deduir el nord i el sud. El punt exacte de la sortida del Sol varia al llarg de l'any i només se situa aproximadament a l'est al voltant dels equinoccis, però el llevant proporcionava una referència observable per donar nom a l'operació. El significat es va ampliar fins a l'ús actual: reconèixer on som i en quina direcció queden els llocs, encara que utilitzem el nord, una brúixola, una quadrícula o una fita del paisatge com a referència.

#### Nord geogràfic, magnètic i de quadrícula

L'orientació no és només una fletxa decorativa perquè hi ha diverses direccions que anomenem «nord» i no sempre coincideixen. El **nord geogràfic** o nord vertader és la direcció del meridià local cap al pol Nord geogràfic, definit per l'eix de rotació de la Terra. És la referència que utilitzen els meridians i la que acostuma a representar una fletxa del nord en un mapa general.

El **nord magnètic** és la direcció que segueix, sobre el pla horitzontal, una brúixola lliure d'interferències locals. L'agulla s'alinea amb la component horitzontal del camp magnètic terrestre en aquell lloc; no apunta simplement en línia recta cap a un únic punt fix. El camp varia sobre la superfície i canvia amb el temps, i els pols magnètics es desplacen. L'angle entre el nord magnètic i el geogràfic s'anomena **declinació magnètica**: s'expressa cap a l'est o cap a l'oest i necessita una localització i una data. Per exemple, una declinació de `4° E` indica que la direcció marcada com a nord per la brúixola queda quatre graus a l'est del nord geogràfic. La [informació geomagnètica de la NOAA](https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions) explica també que les roques, les estructures metàl·liques i altres camps pròxims poden alterar una lectura local.

El **nord de quadrícula** segueix les línies verticals d'un sistema de coordenades projectades. La projecció obliga a representar en un pla uns meridians que convergeixen cap als pols; per això les línies de quadrícula i el meridià local poden formar un angle, anomenat **convergència de meridians** o de quadrícula. En un mapa comarcal ordinari aquestes diferències solen ser petites per a la lectura general. En navegació, treball de camp o cartografia tècnica, en canvi, cal indicar quin nord s'utilitza i aplicar, quan correspongui, la declinació magnètica o la convergència de quadrícula.

#### Orientar el mapa segons la tasca

Un mapa pot estar rotat per aprofitar millor el suport, seguir una costa, adaptar-se a un recorregut turístic o encaixar en una composició. Aquesta decisió és legítima si no desorienta el lector. Com més s'allunyi la composició de l'orientació convencional al nord, més necessari serà indicar l'orientació i proporcionar referències suficients. En canvi, repetir una rosa dels vents en cada mapa petit d'una infografia pot afegir soroll si tots els marcs comparteixen una orientació evident.

El nord a dalt és una convenció cartogràfica estesa, no una propietat necessària del territori. Un mapa de corredor pot girar-se perquè la costa o l'itinerari aprofitin millor el suport; un plànol de visita pot alinear-se amb la direcció en què mira la persona situada davant del panell. En els mapes «sou aquí», aquesta correspondència entre el document i l'entorn pot reduir la rotació mental, sempre que el punt de situació, la direcció de mirada i el nord quedin indicats sense ambigüitat. Una orientació egocèntrica útil en un plafó fix no s'ha de copiar automàticament a un mapa general que es consultarà des de posicions diferents {% cite levinePlacementYouAreHere1984 maceachrenHowMapsWork1995 %}.

![El mateix territori sintètic orientat al nord, girat per seguir un corredor litoral i alineat amb la mirada en un mapa «sou aquí»]({{ site.baseurl }}/assets/img/cartographic-language/map-orientation-comparison.svg "Els tres panells conserven els mateixos llocs i recorreguts. Canvia l'orientació del marc segons la tasca, però tots incorporen un senyal inequívoc de nord o de posició i mirada. Figura d'elaboració pròpia."){: data-figure-width="54rem"}

::: subfigures a+b/c+d "Orientar un mapa és una decisió de llenguatge cartogràfic. La subfigura a mostra la diferència entre nord geogràfic, nord de quadrícula i nord magnètic; la subfigura b recorda que una fletxa del nord també és un símbol gràfic que cal triar amb contenció; la subfigura c mostra un mapa de Catalunya sense fletxa explícita, però amb retícula, coordenades i una convenció nord-amunt prou clares; la subfigura d capgira deliberadament el mapamundi convencional i, per això, necessita fer visible l'orientació. Llicència: pendent de revisar."
![Esquema tècnic amb nord geogràfic, nord de quadrícula, nord magnètic, convergència i declinació]({{ site.baseurl }}/assets/img/cartographic-language/north-types.png "Tipus de nord en un full cartogràfic tècnic")
![Diverses formes gràfiques de fletxes del nord i roses dels vents]({{ site.baseurl }}/assets/img/cartographic-language/graphic-north-types.png "Repertori gràfic de símbols d'orientació")
![Mapa de Catalunya sense fletxa del nord explícita, però amb retícula i coordenades]({{ site.baseurl }}/assets/img/cartographic-language/catalonia-without-north.png "Mapa de Catalunya sense fletxa del nord")
![Mapamundi de McArthur amb orientació sud-amunt i rosa dels vents visible]({{ site.baseurl }}/assets/img/cartographic-language/mcarthur-corrective-projection.png "Mapamundi de McArthur amb orientació sud-amunt")
:::

>>>> **Absència de fletxa no significa absència d'orientació.** En un mapa nord-amunt, sense rotació i amb retícula, costa, topònims o marc territorial fàcilment recognoscibles, ometre la fletxa pot ser una decisió correcta. En un mapa rotat, en una ruta, en una composició turística poc convencional o en un producte que serveixi per orientar-se físicament sobre el terreny, cal indicar l'orientació de manera explícita. Si el treball depèn d'una brúixola, d'una quadrícula o de navegació, també cal precisar quin nord s'està utilitzant.

### Retolació

La **retolació** selecciona, jerarquitza i col·loca noms i altres textos perquè identifiquin elements geogràfics sense ambigüitat. Inclou topònims, valors puntuals, anotacions, unitats, textos de llegenda i crèdits breus. No és una capa decorativa que s'afegeix al final: forma part del llenguatge del mapa i pot confirmar o desfer la jerarquia construïda amb símbols i colors. Les etiquetes no han de competir amb la variable principal. Tipografia, mida, posició, espaiament, contrast i ús d'halo formen part de la decisió; per això la retolació s'ha de revisar en la mida final i no només dins de la interfície de QGIS {% cite brewerDesigningBetterMaps2005 %}.

#### Famílies, variants, pesos i estils

Una **família tipogràfica** és un sistema de signes relacionats, com Roboto, Noto Sans, Liberation Sans o DejaVu Serif. Dins d'una mateixa família poden existir variants de pes, amplada i estil: regular, negreta, lleugera, condensada, cursiva o negreta cursiva. La **cursiva** no és una família independent, sinó una variant dissenyada per canviar el ritme i la forma de les lletres. Tampoc no s'ha de confondre el pes amb la mida: un text de `10 pt` pot ser regular o negreta i ocupar la mateixa alçada nominal, però tenir una presència visual i un consum de tinta diferents.

Les famílies **amb serifa** incorporen petits acabaments als traços; les **de pal sec** prescindeixen d'aquests remats; les **monoespaiades** assignen una amplada semblant a cada caràcter; i les famílies **per a titulars** estan pensades per a títols o usos de gran mida, no necessàriament per a etiquetes petites. Aquestes categories ajuden a descriure una font, però no determinen automàticament el suport correcte. Una família de pal sec mediocre pot funcionar pitjor en pantalla que una família amb serifa ben dibuixada, i una serifa massa fina pot perdre's en un mapa imprès. La decisió s'ha de provar amb els cossos, accents, xifres, topònims i fons reals del projecte.

Comparar sempre el mateix topònim permet atribuir les diferències a la tipografia i no al contingut. A la fila superior de la figura següent, `Vila-seca` conserva la mida nominal però canvia de família; a la fila inferior es manté DejaVu Sans i només canvia la variant. La negreta guanya presència, la cursiva modifica el ritme i la monoespaiada ocupa l'espai d'una manera diferent. Aquestes diferències poden construir jerarquia, però també poden dificultar l'encaix o la lectura si s'apliquen sense criteri.

![El topònim Vila-seca comparat en famílies de pal sec, amb serifa i monoespaiada, i en variants regular, negreta, cursiva i negreta cursiva]({{ site.baseurl }}/assets/img/cartographic-language/typographic-specimens.svg "El mateix topònim canvia d'amplada, ritme, densitat i presència visual segons la família i la variant. Les mostres mantenen la mateixa mida nominal perquè es puguin comparar; abans de triar una font cal repetir la prova amb la mida final, els accents, les xifres i el fons reals del mapa. Figura d'elaboració pròpia."){: data-figure-width-web="29rem" data-figure-width-pdf="69%"}

::: table "Famílies i variants tipogràfiques"
| Recurs | Funció possible | Risc que cal comprovar |
| --- | --- | --- |
| Amb serifa | Text narratiu, notes o identitat editorial | Serifes massa fines o confusió en cossos petits |
| De pal sec | Etiquetes, llegendes, gràfics i interfícies | Uniformitat excessiva si no hi ha jerarquia de pes i mida |
| Monoespaiada | Codis, coordenades o fragments tècnics breus | Amplada excessiva i aspecte de codi en text ordinari |
| Negreta | Prioritat, municipi destacat o títol | Convertir massa elements en prioritaris |
| Cursiva | Convenció per a hidrografia, relleu o èmfasi puntual | Pèrdua de llegibilitat o ús merament decoratiu |
| Condensada | Etiquetes amb poc espai, si la família la proporciona | Comprimir artificialment una font o ajuntar massa les lletres |
:::

No s'utilitzaran negretes o cursives simulades si existeix la variant real. Un programa pot inclinar o engruixir artificialment una font que no disposa d'aquell estil, però el resultat pot deformar els caràcters i variar entre Calc, QGIS, Inkscape i el PDF. Per construir jerarquia és preferible treballar amb una família que ofereixi regular, negreta i cursiva reals, i limitar el nombre de variants.

#### Tipografies instal·lades, llicència i portabilitat

Els programes no porten necessàriament totes les tipografies dins del document. Calc, Excel, QGIS i Inkscape consulten les tipografies instal·lades al sistema operatiu; per això un fitxer pot canviar d'aspecte quan s'obre en un altre ordinador. Windows, Linux i macOS inclouen repertoris diferents, i una família disponible a l'aula pot no existir a l'ordinador on es revisa o imprimeix el treball. Abans d'adoptar una família cal comprovar que conté accents catalans, ela geminada, signes matemàtics, percentatges i les xifres necessàries.

Si el repertori instal·lat no és suficient, se'n poden afegir fonts noves. A Windows es poden instal·lar des del fitxer de font o mitjançant la configuració del sistema, seguint les instruccions de [Microsoft per afegir fonts](https://support.microsoft.com/office/add-a-font-b7c5f17c-4426-4b53-967f-455339c564c1). En Linux, el procediment depèn de la distribució i de l'entorn d'escriptori: es pot utilitzar el gestor de fonts o instal·lar-les per a l'usuari, habitualment dins de `~/.local/share/fonts`, i actualitzar la memòria cau amb `fc-cache`. Instal·lar una font requereix permisos adequats i reiniciar les aplicacions que ja estaven obertes.

[Roboto](https://fonts.google.com/specimen/Roboto) és una candidata habitual, però no és obligatòria ni està instal·lada en tots els equips. Noto Sans, Liberation Sans i DejaVu Sans són alternatives lliures amb bona cobertura; Liberation Sans, a més, pot facilitar la compatibilitat mètrica amb documents que esperen Arial. La selecció final registrarà família, variant, procedència i llicència. Descarregar un fitxer de font d'una web desconeguda pot introduir problemes de llicència o seguretat; cal utilitzar repositoris oficials o reconeguts.

En exportar, el PDF ha d'incrustar les tipografies o aplicar una substitució deliberada. Convertir text a traçats evita algunes substitucions, però augmenta la mida, impedeix editar i cercar el text i empitjora l'accessibilitat; no serà l'opció predeterminada. L'estudiant comprovarà el fitxer en un segon visor o equip. Quan el professorat prepari el material de demostració, també podrà usar `pdffonts`, una utilitat de línia d'ordres que enumera les tipografies d'un PDF; aquesta comprovació tècnica no forma part de les competències exigides a l'estudiant.

#### Tipografia i consum de tinta o tòner

Algunes fonts i variants utilitzen traços més fins o menys superfície impresa i poden reduir tinta o tòner a la mateixa mida. També existeixen fonts amb perforacions internes pensades perquè els buits desapareguin visualment en cossos petits. Tanmateix, no hi ha una font universalment més sostenible en qualsevol document. Una família ampla pot consumir menys tinta per caràcter però necessitar més línies o pàgines; una variant massa lleugera pot obligar a augmentar la mida; i una font perforada pot perdre qualitat segons la impressora i el cos.

La prova adequada combina llegibilitat i recursos: mateix text, mateixa mida aparent, mateix suport i configuració d'impressió. També influeixen més en el consum total la impressió a doble cara, el mode esborrany, la quantitat de superfícies fosques, el nombre de còpies i la simplificació del document. En mapes i infografies, reduir grans fons saturats o trames innecessàries acostuma a ser més rellevant que substituir una sola família tipogràfica. No es sacrificarà la llegibilitat ni l'accessibilitat per obtenir una reducció de tinta no mesurada.

>> **Prova tipogràfica del projecte.** Abans de fixar la família, cal preparar una mostra amb `Tarragonès`, `Vila-seca`, `l'Espluga de Francolí`, `10,5%`, `EPSG:25831`, una coordenada UTM i una línia de font o crèdit. Cal comparar regular, negreta i cursiva a la mida final, tant en pantalla com en PDF, i registrar la família escollida i una alternativa disponible per si falla la incrustació.

La jerarquia tipogràfica es pot entendre abans de mirar cap mapa. Un rètol comercial de carrer, per exemple, no reparteix l'atenció de manera neutral: una paraula domina per mida, color, pes i contrast; altres línies expliquen la condició de l'oferta, la marca o el detall secundari; i alguns textos queden deliberadament en un nivell molt baix. El mecanisme és el mateix que després cal disciplinar en cartografia. El lector no llegeix totes les paraules alhora, sinó que entra per un nivell dominant i continua per nivells més petits si necessita més informació.

![Rètol comercial de carrer amb una jerarquia tipogràfica molt marcada per mida, pes, color, posició i contrast]({{ site.baseurl }}/assets/img/cartographic-language/typographic-hierarchy.png "La jerarquia tipogràfica guia l'ordre de lectura: mida, pes, color, majúscules, posició i contrast indiquen què s'ha de veure primer i què queda com a informació secundària. Llicència: pendent de revisar."){: data-figure-width="44rem"}

En un mapa, aquesta força s'ha d'utilitzar amb més contenció. Una etiqueta massa gran pot fer semblar més important una població, un accident geogràfic o un país; una cursiva pot suggerir hidrografia o relleu; un color blau pot associar-se a aigua; una majúscula espaiada pot fer llegir un mar, una serralada o una regió com una superfície. Cap d'aquests recursos és innocent. Quan es combinen bé, permeten que mars i oceans, estats, regions, ciutats, accidents físics i elements puntuals formin una jerarquia llegible sense necessitat d'explicar cada nivell amb una llegenda.

#### Topònims i formes oficials

Els topònims són dades lingüístiques i territorials. Abans de retolar un mapa cal decidir quina forma del nom s'utilitzarà, amb quina llengua, amb quina capitalització i amb quina font de validació. En un mapa acadèmic ordinari convé respectar els nomenclàtors i les formes oficials quan existeixen. Si s'utilitza un exònim o una forma traduïda perquè és la forma habitual en el text, la decisió ha de ser coherent amb la resta del document i no pot barrejar variants sense criteri.

Els noms també informen sobre el territori. Poden indicar relleu, hidrografia, vegetació, usos, història o llengua. Aquesta funció no obliga a explicar l'etimologia dins del mapa, però sí a tractar el topònim com una part rellevant de la informació. Escriure un nom incorrecte, retallar-lo sense criteri o col·locar-lo sobre una entitat veïna és un error cartogràfic, no només ortogràfic.

#### Prioritat dels topònims

No tots els noms tenen la mateixa funció. El nom de la comarca, els municipis del territori d'estudi, els municipis veïns, els rius, les vies principals i les referències externes poden formar nivells jeràrquics diferents. La prioritat s'ha de definir abans de reduir la tipografia: quan no hi ha espai, primer s'eliminen o se simplifiquen els noms secundaris. Una jerarquia clara pot combinar mida, pes, estil, color i espaiament, però no ha d'utilitzar tots aquests recursos alhora.

La jerarquia no s'ha de confondre amb una simple llista de cossos de lletra. En un mapa de referència a escala regional, els nivells poden començar pels grans espais marins o continentals, continuar pels països o unitats polítiques principals, baixar a illes, regions i ciutats destacades, i acabar en localitats menors, caps, badies, relleu, carreteres o cotes. La pregunta de revisió és doble: quin nivell ha de percebre el lector primer, i quin recurs tipogràfic fa possible aquesta prioritat sense tapar els altres?

![Fragment de mapa de Xipre i el Mediterrani oriental amb diversos nivells de retolació: mar, illa, països, ciutats, caps, badies, relleu i xarxa viària]({{ site.baseurl }}/assets/img/cartographic-language/map-labels-eg-2.png "El fragment permet analitzar com mida, majúscules, minúscules, cursiva, color, pes, espaiament, orientació i posició creen nivells de lectura en la retolació cartogràfica. Llicència: pendent de revisar."){: data-figure-width="48rem"}

>>> **Analitzar la jerarquia de la retolació.** Sobre el mapa anterior, cal ordenar els nivells de retolació de més a menys presència visual, començant pels grans espais, com mars i oceans, i continuant amb països, illes, ciutats, elements costaners, relleu, vies o altres categories recognoscibles. Per a cada nivell, cal descriure què fa que destaqui més o menys: mida, majúscules, pes, color, cursiva, espaiament, orientació, halo, proximitat a l'element o relació amb el fons. La resposta no ha de ser només una llista de noms; ha d'explicar quin sistema de prioritats construeix el mapa.

::: table "Criteris de retolació cartogràfica"
| Element | Criteri principal | Risc habitual |
| --- | --- | --- |
| Punt o símbol puntual | Etiqueta pròxima, desplaçada sempre amb el mateix criteri i sense tapar el símbol | Que el lector no sàpiga a quin punt pertany el nom |
| Línia o recorregut | Text orientat segons el sentit de la línia, amb separació suficient i repetició només quan ajuda | Fer seguir el text per corbes massa tancades o invertir-ne la lectura |
| Àrea o municipi | Nom dins o associat clarament a l'àrea, amb mida proporcional a la jerarquia i no a la superfície | Confondre el nom amb una àrea veïna o fer-lo desaparèixer en polígons petits |
| Element d'aigua o relleu | Estil coherent amb la convenció adoptada i contrast suficient amb el fons | Utilitzar cursiva, blau o efectes sense funció o amb poca llegibilitat |
| Referència externa | Tractament secundari respecte del territori d'estudi | Donar més pes visual al context que al mapa principal |
:::

#### Posició, sentit i espaiament

La posició de l'etiqueta ha de fer visible l'associació amb l'element. En elements puntuals, la proximitat i un desplaçament coherent resolen la relació. En elements lineals, el text ha de seguir el recorregut sense obligar a girar excessivament el cap ni trencar paraules. En àrees, el nom ha de quedar dins de l'entitat o vinculat de manera inequívoca; si l'àrea és massa petita, pot caldre una línia de crida, una etiqueta exterior o una decisió de generalització.

L'espaiament també comunica escala i jerarquia. Un topònim zonal pot ocupar més espai perquè representa una àrea; un nom puntual ha de quedar més contingut. Les lletres massa separades poden semblar elegants però dificultar la lectura, especialment en pantalles petites o exportacions reduïdes. Abans d'abaixar tots els cossos, cal comprovar si hi ha massa etiquetes per a l'escala disponible.

#### Conflictes i ambigüitats

Una etiqueta no ha de tapar una altra, sortir de la seva entitat sense una relació clara ni confondre's amb un municipi veí. La posició, l'halo, el contrast i les línies de crida poden resoldre casos concrets, però una acumulació de recursos correctius sol indicar que hi ha massa noms per a l'escala disponible. El mapa de context del projecte no necessita demostrar que QGIS pot etiquetar tots els objectes: necessita mostrar els noms que permeten entendre el territori d'estudi.

![Criteris de col·locació d'etiquetes per a punts, línies i àrees, amb candidats, conflictes i línies de crida]({{ site.baseurl }}/assets/img/cartographic-language/map-label-placement.svg "Els punts admeten diverses posicions candidates; els textos lineals han de seguir recorreguts llegibles; els noms d'àrea han de conservar una associació inequívoca. Quan una etiqueta puntual es desplaça, la línia de crida manté visible l'ancoratge. Geometries i topònims sintètics; figura d'elaboració pròpia."){: data-figure-width="54rem"}

#### Retolació automàtica i versió revisada

Els principis clàssics de retolació defineixen posicions preferents segons si l'element és puntual, lineal o superficial i penalitzen l'ambigüitat, les col·lisions i les interrupcions de trets importants {% cite imhofPositioningNamesMaps1975 %}. En un sistema automàtic, cada entitat pot generar diversos candidats amb costos diferents; el problema consisteix a seleccionar una combinació que mantingui el màxim d'etiquetes útils sense solapaments. Amb molts punts, les combinacions possibles creixen de pressa i els algorismes pràctics necessiten heurístiques, prioritats i límits de temps. «Automàtic» significa que el programa resol un problema formal segons unes regles, no que conegui la intenció territorial del mapa {% cite christensenLabelPlacementAlgorithms1995 %}.

La retolació es pot revisar amb una parella en què escala, extensió, geometria, estil i composició es mantinguin constants: la primera versió conserva la configuració automàtica i la segona aplica prioritats, resolució de conflictes, formes oficials i jerarquia. Aquesta comparació controlada permet atribuir els canvis a l'etiquetatge. En l'activitat final del capítol també es revisaran escala, detall, orientació i composició; per això els dos PDF s'anomenaran **inicial** i **revisat**, no automàtic i revisat.

## Jerarquia i composició

### Mapa principal i context

El territori d'estudi ha de dominar la composició. Els límits, fons i elements de localització han d'acompanyar-lo sense desplaçar-lo visualment.

Un requadre de situació és útil quan el públic no pot localitzar fàcilment la comarca en un marc més ampli. No és obligatori si el títol, l'extensió i les referències existents ja resolen la localització. Si s'incorpora, ha de compartir una jerarquia coherent amb el mapa principal i indicar sense ambigüitat quina àrea s'hi amplia.

### Equilibri, marges i recorregut de lectura

La distribució dels elements ha de conduir la mirada des del missatge principal cap a la informació de suport.

L'equilibri no obliga a centrar-ho tot ni a omplir qualsevol espai buit. Els marges separen grups, l'alineació fa visibles les relacions i l'espai en blanc evita que el mapa, el títol, la llegenda i els crèdits competeixin. Una costa, un llac o un buit entre agrupacions poden allotjar informació auxiliar només després de comprovar que no contenen dades, relacions o referències necessàries. La composició s'ha de valorar com una pàgina completa, no com una suma de peces independents {% cite tynerPrinciplesMapDesign2010 %}.

## Activitat: construir el mapa de context

La pràctica construirà el **mapa de context** de la miniinfografia, encara sense aprofundir en la classificació temàtica. Mostrarà on se situa la comarca dins de la província de Tarragona i identificarà els seus municipis amb una jerarquia llegible. L'objectiu serà controlar escala, extensió, retolació, fonts i exportació; no convertir el mapa de localització en un segon mapa temàtic.

L'activitat aplicarà aquests criteris a una composició de QGIS i conservarà una versió inicial i una de revisada. Les seccions següents concreten el projecte de partida, els noms dels fitxers, les comprovacions i les evidències; són passos del procediment, no objectius addicionals que calgui memoritzar.

### Entrades i mapes de context resultants

Per al Tarragonès s'obrirà `qgis/tigit-05-integracio-sig.qgz` i es desarà la continuació com `qgis/tigit-06-llenguatge-cartografic.qgz`. El GeoPackage multiescala de l'ICGC proporcionarà municipis, comarca i província sense recrear ni tornar a descarregar les geometries, i la unió municipal validada es conservarà dins del projecte encara que el mapa de context no la simbolitzi temàticament. Natural Earth només s'afegirà si el producte necessita un localitzador europeu o mundial: no substituirà les divisions oficials del Tarragonès ni de Tarragona. Abans d'obrir la composició es fixaran i registraran l'amplada, l'altura, l'orientació, l'escala i l'espai que el mapa ocuparà a la infografia.

Es generaran dos PDF vectorials a `outputs/maps`: `context_tarragones_initial.pdf`, amb la primera composició completa, i `context_tarragones.pdf`, amb la versió revisada. El `README.md` en compararà els canvis a la mateixa mida final i registrarà per separat el període 2021 dels indicadors del projecte i la versió ICGC de 2026 de la geometria. El mapa revisat serà una entrada explícita del mapa temàtic del capítol 8 i de la miniinfografia del capítol 9.

### Dades i projecte de partida

Es continuarà el projecte QGIS validat a la fase d'integració SIG. La font municipal oficial completa, de la qual s'obté o es deriva el context provincial, la capa comarcal filtrada, la unió, el CRS, les rutes i els codis ja validats no s'han de substituir ni recrear a partir d'una descàrrega nova. Abans de maquetar es registraran la mida del mapa exportat, l'orientació de la pàgina, l'escala i l'espai que la peça ocuparà a la miniinfografia.

El procediment general serà aquest:

1. crear una composició dins del projecte QGIS i definir-ne la mida i l'orientació finals;
2. afegir un marc principal amb l'extensió de la comarca i comprovar-ne l'escala;
3. ordenar i estilitzar les capes perquè la comarca domini i el context quedi en segon terme;
4. preparar la prova tipogràfica, registrar la família i configurar l'etiquetatge municipal amb variants reals;
5. afegir un segon marc provincial només si millora la localització;
6. completar títol, escala, orientació, fonts i crèdits després d'estabilitzar els marcs;
7. exportar la versió inicial, obrir-la fora de QGIS i corregir la composició editable abans de generar la versió revisada.

### Construir el mapa principal

El mapa principal mostrarà els límits municipals de la comarca. L'extensió deixarà un marge suficient al voltant del territori sense reduir-lo innecessàriament, i la jerarquia dels traços distingirà el límit comarcal dels municipals. Els fons o territoris veïns tindran un tractament secundari.

Els municipis s'etiquetaran segons prioritats. Només es conservaran els noms que es puguin associar sense ambigüitat i llegir a la mida final. Si la composició no admet tots els topònims, la solució preferent serà reduir-ne el nombre o ajustar-ne la disposició, no fer-los tots igualment petits.

### Construir el requadre de situació

Un requadre més petit podrà mostrar la comarca destacada dins de la província de Tarragona. La seva extensió, simbologia i títol han de deixar clar que compleix una funció de localització. No incorporarà detalls municipals, llegendes o fons que no contribueixin a aquesta funció.

### Completar i exportar la composició

El títol, la llegenda si és necessària, l'escala, l'orientació, les fonts i els crèdits s'afegiran després d'estabilitzar el mapa. El CRS del projecte es comprovarà abans de confiar en la barra d'escala. La fletxa del nord només s'incorporarà si resol una ambigüitat: si el mapa principal i el requadre comparteixen una orientació convencional i evident, l'omissió també s'haurà de poder justificar. La composició es revisarà a mida real. Primer s'exportarà `context_tarragones_initial.pdf`; després de revisar retolació, escala, detall, orientació i composició, s'exportarà `context_tarragones.pdf`, sense substituir el projecte ni la composició editable.

### Validar el mapa de context

Abans d'acceptar el mapa cal verificar que:

1. hi apareixen totes les geometries municipals previstes i cap territori exterior es confon amb la comarca; només s'etiqueten els topònims llegibles i necessaris;
2. el CRS, l'extensió i la barra d'escala són coherents, i cap coordenada en graus es presenta com una mesura mètrica directa;
3. els límits municipals es poden seguir sense dominar visualment la pàgina;
4. l'orientació és evident o està indicada amb un símbol discret i coherent;
5. les etiquetes no presenten col·lisions ni associacions ambigües;
6. el requadre de situació aporta una localització que el mapa principal no resol per si sol;
7. la font, la versió, l'autoria i els crèdits es poden recuperar;
8. els textos i traços continuen sent llegibles a la mida final;
9. el PDF conserva vectors, tipografies i proporcions quan s'obre fora de QGIS; en obrir-lo a Inkscape, els límits i textos vectorials es poden ampliar sense pixelació i seleccionar com a objectes.
10. la família escollida, les variants, la llicència i l'alternativa estan registrades, i les fonts queden incrustades o substituïdes de manera deliberada.

### Evidències del mapa de context

::: table "Evidències del mapa de context"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `qgis` | Projecte QGIS continuat | Font municipal oficial completa i context provincial obtingut o derivat d'aquesta font, capa filtrada del Tarragonès, CRS, estils, etiquetes i composició editable |
| `outputs/maps` | `context_tarragones_initial.pdf` | Composició inicial completa, a la mida final i en format vectorial |
| `outputs/maps` | `context_tarragones.pdf` | Versió revisada amb extensió final, topònims, escala funcional, fonts i crèdits en format vectorial |
| `README.md` | Comparació i registre cartogràfic | Comparació dels dos PDF a la mateixa mida, escala, detall omès, prioritats de retolació, orientació i decisió sobre el requadre |
| `README.md` | Registre tipogràfic | Família, regular/negreta/cursiva, procedència, llicència, alternativa, caràcters comprovats i resultat de la incrustació al PDF |
| `captures` | Prova tipogràfica | Mostra a mida final amb topònims, xifres, percentatge, coordenada i crèdit; no cal capturar el procés d'instal·lació de la font |
:::

La fita `tigit-06-llenguatge-cartografic.qgz` conserva així la unió del capítol anterior i hi afegeix una composició de context revisada. El capítol de cartografia temàtica reutilitzarà aquest mateix projecte: mantindrà el context estable i incorporarà l'indicador, la classificació i la paleta com a decisions noves i controlables.
