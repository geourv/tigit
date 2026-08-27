---
layout: manual-chapter
title: Introducció als sistemes d'informació geogràfica
description: Introducció als SIG, el seu ecosistema i la seva evolució, amb capes, taules d'atributs, importació, unions i control de qualitat a QGIS.
lang: ca
ref: manual-gis-data-integration
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/integracio-sig/
weight: 70
part: Continguts
manual_references: true
---

Moltes decisions territorials exigeixen relacionar què passa amb on passa. Comparar l'oferta turística entre municipis, estudiar l'accés a un equipament, delimitar una àrea exposada o examinar els canvis d'ús del sòl requereix combinar localitzacions, atributs, temps i criteris d'anàlisi. Una taula o un mapa aïllats poden mostrar una part del problema, però no organitzen necessàriament les dades, les operacions i les comprovacions que permeten respondre'l.

Un **sistema d'informació geogràfica** (SIG) relaciona dades georeferenciades, persones, mètodes, programari i infraestructura per capturar, gestionar, consultar, analitzar i comunicar informació sobre el territori. Aquest capítol presenta primer el concepte, els components, l'evolució i les principals famílies d'aplicacions dels SIG. A continuació, aquest marc general es trasllada al projecte del curs mitjançant una unió entre indicadors municipals i geometries, consultes espacials i controls de qualitat {% cite longleyGeographicInformationScience2015 nunesDiccionariSIG2012 %}.

>>>>> En acabar el capítol, cal poder explicar com funciona un SIG i aplicar-ne els criteris per obtenir un resultat territorial consultable, validat i reproduïble.
>>>>>
>>>>> - Explicar un SIG com un sistema de persones, dades, mètodes, programari i infraestructura que treballa per capes per respondre preguntes territorials.
>>>>> - Distingir la captura d'una posició amb GNSS de la seva documentació, integració i anàlisi posterior en un SIG.
>>>>> - Formular una pregunta espacial i relacionar-la amb les dades, l'operació i els controls de qualitat necessaris.
>>>>> - Integrar una taula d'indicadors amb una capa municipal sense perdre codis, absències ni fonts originals.
>>>>> - Comprovar consultes i unions amb recomptes, contrastos manuals i documentació suficient per reconstruir el resultat.

El capítol presenta noms de tecnologies per reconèixer quina funció compleixen dins d'un sistema, no perquè s'hagin de memoritzar o instal·lar totes. La pràctica se centra en QGIS i en la integració de dades municipals; les biblioteques, les bases de dades i els servidors només ajuden a entendre que una aplicació d'escriptori no és tot el SIG.

## Què és un SIG

La informació **georeferenciada** combina un **component temàtic**, que descriu què és o quin valor té una entitat, i un **component espacial**, que indica on es troba, quina forma té i quines relacions manté amb altres entitats. Un SIG organitza aquests components perquè la localització no sigui només una etiqueta, sinó una dimensió que es pot consultar, mesurar, relacionar i analitzar.

Un SIG comprèn diversos nivells relacionats. Una **aplicació SIG** implementa operacions sobre dades geogràfiques; un **projecte editable** registra capes, estils, unions, consultes i composicions; i una **sortida** comunica una part del resultat mitjançant un mapa, una taula, una capa derivada, una ruta, una alerta o un servei web. El sistema complet incorpora també les fonts, les persones, els procediments, la infraestructura i el context institucional que permeten interpretar i mantenir aquests resultats. Per això una aplicació o un mapa representen peces del SIG, no el sistema sencer.

>>>>> En acabar aquesta fase, cal poder anomenar els cinc components d'un SIG, explicar per què tots són essencials i relacionar-los amb un exemple territorial concret.
>>>>>
>>>>> - Descompondre una informació georeferenciada en component temàtic i component espacial.
>>>>> - Distingir el sistema SIG, una aplicació d'escriptori, un projecte editable i una sortida com un mapa, una taula o una capa derivada.
>>>>> - Explicar la funció de persones, dades, mètodes, programari i infraestructura, amb almenys un exemple de cada component.
>>>>> - Identificar quin component o procediment cal revisar quan un resultat territorial és incomplet o enganyós.

Els serveis cartogràfics quotidians permeten reconèixer algunes d'aquestes capacitats. [Google Maps](https://support.google.com/maps/answer/144349?hl=ca), els navegadors de vehicle, els visors turístics i moltes aplicacions de mobilitat localitzen llocs, combinen informació, calculen rutes i mostren bases cartogràfiques. Són serveis geoespacials especialitzats que resolen consultes delimitades amb una interfície preparada per al consum. Un entorn SIG generalista, en canvi, permet definir les capes, els camps, els sistemes de referència, les unions, els models d'anàlisi i les regles de publicació d'un procés propi.

### Separar el territori en capes per poder-lo relacionar

Una **capa geogràfica** agrupa entitats o valors que comparteixen un significat i una forma de localització: municipis, carreteres, allotjaments, cursos d'aigua, pendents o zones inundables, per exemple. Separar-los evita barrejar en una sola representació dades amb unitats, dates i qualitats diferents. Alhora, la georeferenciació permet alinear les capes i preguntar quines entitats coincideixen, queden dins d'una zona, es troben a prop d'una xarxa o compleixen diversos criteris alhora.

La superposició té antecedents anteriors als SIG digitals. Una manera de comparar factors consistia a representar cada tema sobre un full transparent amb la mateixa base geogràfica i superposar els fulls per observar coincidències. Ian L. McHarg no va inventar aquesta tècnica ni els SIG, però la va sistematitzar i difondre en la planificació ecològica, especialment amb *Design with Nature*, publicat el 1969. La transició digital va convertir aquella combinació òptica de mapes en operacions reproduïbles sobre geometries i atributs {% cite mchargDesignNature1969 goodchildTowardsGeodesign2010 %}.

![Tres capes alineades del mateix territori representen el relleu, la inundabilitat i els accessos; una operació de superposició aplica criteris explícits i delimita una àrea candidata]({{ site.baseurl }}/assets/img/gis/gis-layer-overlay.svg "El precedent dels fulls transparents ajuda a entendre la lògica de les capes, però una operació SIG exigeix definir la pregunta, les regles, el sistema de referència i els controls de qualitat. L'àrea candidata és un resultat derivat, no una realitat observada directament. Esquema docent d'elaboració pròpia basat en McHarg i Goodchild."){: data-figure-width-web="62rem" data-figure-width-pdf="100%"}

La figura planteja una localització hipotètica: el relleu limita els pendents admissibles, la inundabilitat exclou àrees de risc i la xarxa condiciona l'accés. La zona verda només és candidata segons aquestes regles; no demostra que sigui el lloc adequat. Encara caldria justificar els llindars, comprovar l'escala, la data, el sistema de referència i la precisió de cada capa, incorporar els factors omesos i contrastar el resultat sobre el terreny. Treballar per capes facilita, precisament, identificar quina entrada o quina regla s'ha de revisar quan la síntesi és incompleta o enganyosa.

### Un ecosistema de peces especialitzades

Un **SIG d'escriptori** s'executa en un ordinador i ofereix una interfície per obrir capes, editar geometries, consultar atributs, analitzar, simbolitzar i preparar sortides. QGIS i ArcGIS Pro són exemples d'aquesta categoria, però cap aplicació constitueix per si sola tot el sistema d'informació.

Una **biblioteca geoespacial** és codi que altres programes reutilitzen per fer una feina concreta. [GDAL](https://gdal.org/en/stable/about.html), per exemple, llegeix, escriu i transforma molts formats de dades ràster i vectorials; el nom **OGR** encara apareix en documentació i ordres per referir-se a la part vectorial històrica del mateix projecte. QGIS pot aprofitar GDAL quan obre o converteix fitxers, però l'estudiant no necessita programar la biblioteca ni executar-ne les ordres per entendre aquesta funció.

Una **base de dades espacial** compleix una funció diferent: conserva taules i geometries i permet consultar-les de manera coordinada. [PostGIS](https://postgis.net/documentation/) no és una biblioteca equivalent a GDAL, sinó una extensió que afegeix tipus geomètrics i operacions espacials a la base de dades PostgreSQL. És útil quan moltes persones o aplicacions han de consultar i actualitzar un conjunt de dades compartit; administrar-la queda fora de la pràctica introductòria del curs.

Un **servidor geoespacial**, com [GeoServer](https://geoserver.org/about/) o QGIS Server, publica capes, mapes o operacions perquè altres aplicacions les consumeixin. Un **WebGIS** és el conjunt que el lector utilitza al navegador i sol combinar una interfície web, serveis, dades i regles d'accés. Per tant, GeoServer no és per si sol tota l'aplicació web, igual que QGIS Desktop no és tot el sistema d'informació. Els estàndards de l'[Open Geospatial Consortium](https://www.ogc.org/standards/) permeten que peces de fabricants diferents intercanviïn mapes i objectes geogràfics.

::: table "Peces habituals de l'ecosistema SIG"
| Peça | Funció i límit | Exemples orientatius |
| --- | --- | --- |
| Servei o aplicació especialitzada | Resol consultes o tasques delimitades, però no ofereix necessàriament control general sobre les dades i els mètodes | Google Maps, un visor turístic o una aplicació de treball de camp |
| SIG d'escriptori | Permet explorar, editar, analitzar i compondre dades; el programa no inclou per si sol les persones, les dades i els criteris de tot el sistema | QGIS, de codi obert; ArcGIS Pro, propietari |
| Biblioteca geoespacial | Proporciona funcions reutilitzables a altres programes; no és una aplicació completa amb una interfície pròpia de treball | [GDAL](https://gdal.org/en/stable/about.html), per llegir i transformar formats; [PROJ](https://proj.org/), per transformar coordenades |
| Base de dades espacial | Emmagatzema taules i geometries i permet fer consultes compartides | PostgreSQL amb l'extensió PostGIS |
| Servidor geoespacial | Publica dades i mapes perquè els utilitzin altres programes o pàgines web | GeoServer o QGIS Server, de codi obert |
| Aplicació WebGIS o plataforma gestionada | Combina la interfície del navegador amb dades, serveis, permisos i manteniment | Un visor institucional; ArcGIS Online o Google Maps Platform com a serveis comercials |
:::

**Programari lliure i de codi obert** significa que la llicència permet estudiar, modificar i redistribuir el codi segons unes condicions. **Programari propietari** limita aquest accés i depèn de les condicions del titular. **Comercial** descriu un model de negoci, no necessàriament una llicència tancada: un projecte de codi obert pot tenir desenvolupament o suport professional de pagament, i un servei propietari pot oferir un nivell d'accés gratuït. L'elecció s'ha de basar en el control sobre les dades, la interoperabilitat, la continuïtat, el suport, els costos totals, el coneixement disponible i la dependència del proveïdor {% cite steinigerOverviewCurrentFree2009 %}.

![Components d'un sistema d'informació geogràfica: persones, dades, mètodes, programari i infraestructura connectats per una pregunta territorial]({{ site.baseurl }}/assets/img/gis/gis-components.svg "Cap component funciona aïlladament: la pregunta orienta el sistema i el control de qualitat relaciona persones, dades, mètodes, programari i infraestructura. Esquema docent d'elaboració pròpia."){: data-figure-width="52rem"}

Aquest esquema no és una seqüència temporal. La pregunta ocupa el centre perquè organitza el sistema, i els cinc components que l'envolten s'han d'interpretar com a parts interdependents. Les connexions expressen relació; el contorn exterior del control de qualitat indica una responsabilitat transversal que afecta tots els components.

Cap dels cinc components és decoratiu o substituïble per la resta. Les **persones** formulen la pregunta, assumeixen responsabilitats, decideixen els criteris i interpreten els resultats. Les **dades** aporten geometries, atributs, temps i metadades: sense dades adequades no hi ha evidència territorial. Els **mètodes** defineixen com es captura, transforma, relaciona, analitza i valida la informació: prémer un botó no justifica l'operació. El **programari** implementa aquestes operacions i ajuda a conservar-ne el procés. La **infraestructura** inclou ordinadors, receptors, servidors, xarxes, emmagatzematge i còpies de seguretat: sense ella el sistema no es pot executar, compartir ni mantenir. El control de qualitat travessa tots cinc components.

::: table "Els components d'un SIG en un projecte territorial"
| Component | Exemple en un projecte territorial | Pregunta que cal poder respondre |
| --- | --- | --- |
| Persones | Qui prepara les dades, qui valida la integració i qui utilitzarà el resultat | Qui defineix la pregunta i qui respon del resultat? |
| Dades | Límits municipals, indicadors, codis, dates, CRS i metadades | Les fonts representen el territori, el període i les entitats necessàries? |
| Mètodes | Importació, normalització de claus, unió, selecció i comprovacions | Per què aquesta operació respon la pregunta i com se n'ha verificat el resultat? |
| Programari | Full de càlcul, SIG d'escriptori i serveis de dades | Quina peça executa cada operació i què queda registrat al projecte? |
| Infraestructura | Ordinador, emmagatzematge, xarxa, GNSS i còpies de seguretat quan siguin necessaris | On es processen i es conserven les dades, i com se'n garanteix l'accés? |
:::

Un algorisme correcte aplicat a una dada inadequada pot produir un resultat enganyós; una dada precisa sense un mètode justificat tampoc no resol la pregunta; i un projecte ben construït que ningú no pot interpretar o mantenir no constitueix un sistema complet. Al final del curs no caldrà memoritzar totes les tecnologies de l'ecosistema, però sí reconèixer aquests cinc components i explicar com es relacionen en un cas concret.

## Història i evolució dels sistemes d'informació geogràfica

Els mapes, els censos i els inventaris territorials són molt anteriors als ordinadors. El canvi que va donar lloc als SIG no va consistir només a dibuixar mapes amb una màquina, sinó a codificar la localització i els atributs de manera que es poguessin consultar, combinar, mesurar i actualitzar. Durant les dècades de 1950 i 1960, la geografia quantitativa, la cartografia temàtica, la gestió de recursos i els primers ordinadors van confluir en diversos projectes. El debat sobre què podia aportar l'ordinador al raonament geogràfic ja apareixia explícitament en textos com *The Computer and the Geographer*, de Torsten Hägerstrand {% cite hagerstrandComputerGeographer1967 goodchildReimaginingHistoryGIS2018 %}.

Un dels episodis fundacionals més citats és el **Canada Geographic Information System** (CGIS), desenvolupat durant els anys seixanta per donar suport al [**Canada Land Inventory**](https://sis.agr.gc.ca/cansis/nsdb/cli/index.html). L'inventari federal havia de combinar informació sobre capacitat agrícola, boscos, fauna, lleure i usos del sòl en més de 2,5 milions de quilòmetres quadrats de territori rural i aigua, i va arribar a produir més de mil fulls a escala 1:250.000. Informatitzar les capes permetia superposar classificacions, calcular superfícies i obtenir síntesis per a la planificació sense repetir manualment tota la cartografia. [Roger Tomlinson](https://www.gg.ca/en/honours/recipients/146-7529) va concebre i va dirigir una part decisiva d'aquest treball; per això és reconegut convencionalment com el «pare dels SIG» i el CGIS sovint es presenta com el primer SIG operatiu. La fórmula resumeix una contribució central, però no ha d'ocultar que el sistema va ser una obra col·laborativa de responsables públics, especialistes en recursos, geògrafs i informàtics {% cite tomlinsonIntroductionGeoInformationSystem1967 stundenBowerToolsRationalDevelopment2018 %}.

La relació inicial entre SIG, inventari i recursos naturals no és accidental. En un país extens com el Canadà, reunir cartografia dispersa, mantenir classificacions comparables i calcular aptituds del sòl per a grans àrees feia especialment visible el cost dels procediments manuals. Necessitats semblants van impulsar sistemes de planificació forestal, ambiental i territorial als Estats Units i en altres administracions. Això no significa que la superfície d'un país produeixi automàticament un SIG: al mateix temps hi havia recerca universitària, cartografia censal i aplicacions urbanes en territoris de dimensions molt diferents. La necessitat institucional, les dades disponibles, els mètodes i la capacitat informàtica expliquen conjuntament cada desenvolupament {% cite goodchildReimaginingHistoryGIS2018 longleyGeographicInformationScience2015 %}.

També van aparèixer programes més especialitzats. **SYMAP**, desenvolupat a Harvard durant els anys seixanta, automatitzava mapes estadístics en una època en què la sortida podia dependre d'impressores de línies. **VIEWIT**, documentat el 1975 pel Servei Forestal dels Estats Units, calculava visibilitat, pendent i orientació per donar suport a la planificació d'usos del sòl. Aquests programes mostren que la cartografia per ordinador i l'anàlisi del relleu avançaven en paral·lel, però no oferien necessàriament l'entorn generalista, interactiu i interoperable que avui s'espera d'un SIG {% cite robertsonSYMAPProgrammeComputer1967 travisVIEWITComputationSeen1975 %}.

Durant els anys setanta i vuitanta, les millores en bases de dades, emmagatzematge, teledetecció i algorismes espacials van permetre separar millor les dades de la seva representació cartogràfica. A començament dels anys noranta, productes com ArcView van portar capes, consultes i mapes a interfícies gràfiques d'ordinadors personals. Els SIG d'escriptori van deixar d'estar restringits a grans centres de càlcul i van arribar a administracions locals, empreses, universitats i consultories, encara que les llicències, el maquinari i l'obtenció de dades continuaven sent barreres importants.

L'inici del segle XXI va reduir algunes d'aquestes barreres. L'any 2000, els Estats Units van [desactivar la degradació intencionada del senyal GPS civil](https://clintonwhitehouse4.archives.gov/WH/EOP/OSTP/html/0053_2.html), cosa que en va millorar substancialment la precisió d'ús públic. El projecte QGIS va començar el 2002 i es va incorporar a una comunitat creixent de programari geoespacial lliure i de codi obert. Els estàndards web, les infraestructures de dades espacials, OpenStreetMap, els portals de dades obertes i els telèfons amb GNSS van multiplicar tant les eines com les fonts disponibles {% cite steinigerOverviewCurrentFree2009 %}.

Les interfícies d'ArcView 1 i de la versió 0.0.5-alpha de QGIS permeten observar què va canviar i què es va conservar durant el pas cap als SIG d'escriptori. La resolució, els controls i l'organització visual pertanyen a dues èpoques diferents, però totes dues interfícies ja articulen la feina al voltant d'un visor cartogràfic, una llista de capes, eines d'interacció i controls sobre la representació.

::: subfigures a+b "Dues interfícies històriques de SIG d'escriptori. La subfigura a mostra ArcView 1 (1991), amb el visor, la llegenda de capes i una paleta d'eines; la subfigura b mostra QGIS 0.0.5-alpha (2002), amb el panell de capes, el visor, la barra d'eines i el diàleg de propietats d'una capa. Les captures no mostren totes les funcions disponibles i s'utilitzen com a fragments per a comentari històric i docent. Captures conservades al material docent TIGIT anterior. ArcView és programari d'Esri; QGIS és programari lliure distribuït sota la GNU GPL."
![Interfície d'ArcView 1 amb una llegenda de capes, un visor cartogràfic i una paleta vertical d'eines]({{ site.baseurl }}/assets/img/gis/arcview-1-1991.png "ArcView 1, 1991. Captura de la interfície del programari d'Esri conservada al material docent TIGIT anterior.")
![Interfície de QGIS 0.0.5-alpha amb el panell de capes, el visor, una barra d'eines i el diàleg de simbologia]({{ site.baseurl }}/assets/img/gis/qgis-0.0.5-2002.png "QGIS 0.0.5-alpha, compilació del 20 d'agost de 2002. Captura de la interfície del programari QGIS conservada al material docent TIGIT anterior.")
:::

La comparació es completa al laboratori amb la versió actual de QGIS. Cal localitzar-hi el llenç o visor, el panell de capes que també funciona com a llegenda de treball, les barres d'eines, les propietats de simbologia i la taula d'atributs, encara que aquesta darrera no aparegui oberta a les captures. L'objectiu no és trobar botons idèntics, sinó reconèixer operacions persistents: activar i ordenar capes, inspeccionar entitats i atributs, canviar-ne la representació, navegar pel mapa i conservar el resultat en un projecte. Tres dècades d'evolució han ampliat molt els formats, les anàlisis i les formes de publicació, però no han eliminat aquesta estructura bàsica de treball.

Avui no hi ha una única cadena de treball ni una sola família de proveïdors. Conviuen SIG d'escriptori, bases de dades espacials, biblioteques de programació, servidors de mapes, aplicacions mòbils, plataformes comercials, serveis públics interoperables i entorns d'anàlisi al núvol. Aquesta abundància permet abordar volums i escales abans inassolibles, però no elimina els límits de llicència, cobertura, qualitat, representativitat o capacitat tècnica. Des de la dècada de 2020, l'aprenentatge automàtic, la IA geoespacial i els assistents generatius assenyalen un canvi cap a fluxos més automatitzats de classificació, predicció i consulta. Aquest canvi amplia l'ecosistema, però no substitueix la pregunta, la documentació, la validació ni la interpretació territorial.

![Cronologia per etapes dels SIG: fonaments als anys cinquanta, primers SIG als seixanta, dades i algorismes entre els setanta i els vuitanta, escriptori als noranta, web, GNSS i codi obert als dos mil, SIG connectats als anys deu i canvi cap a la IA geoespacial des dels anys vint]({{ site.baseurl }}/assets/img/gis/gis-history-timeline.svg?v=2 "Set etapes àmplies de l'evolució dels SIG, des de la geografia quantitativa i els primers ordinadors fins als entorns connectats dels anys deu i la incorporació progressiva de la IA geoespacial des dels anys vint. Les etapes se solapen i acumulen capacitats; no representen una substitució completa de les tecnologies anteriors. Esquema docent d'elaboració pròpia a partir de les fonts citades al text."){: data-figure-width-web="39.5rem" data-figure-width-pdf="93%"}

La cronologia agrupa processos en etapes temporals perquè el canvi principal és l'eixamplament progressiu de l'ecosistema. Els sistemes institucionals van continuar després de l'arribada dels ordinadors personals; els serveis web no van fer innecessari l'escriptori; i el programari lliure no va fer desaparèixer les plataformes propietàries. Cada etapa va ampliar les dades, els usuaris i les formes de captura, anàlisi i publicació, però també va afegir decisions sobre interoperabilitat, manteniment, privacitat i dependència d'un proveïdor.

## Sistemes de posicionament, GPS i GNSS

La possibilitat d'obtenir coordenades fora d'un laboratori va transformar la producció d'informació geogràfica. Un inventari turístic, una incidència, una fotografia de camp o el recorregut d'una ruta es poden registrar directament al lloc on s'observen i integrar després amb límits, xarxes, relleu i indicadors. Aquesta disponibilitat no prové només d'un satèl·lit o d'una aplicació: depèn d'una infraestructura orbital i terrestre, dels receptors, dels sistemes de referència, de les comunicacions i dels procediments que converteixen una observació en una dada utilitzable.

>> **GPS i GNSS no són sinònims exactes.** En l'ús quotidià, *GPS* s'empra sovint com a nom genèric de qualsevol posicionament per satèl·lit. Tècnicament, **GPS** (*Global Positioning System*, sistema de posicionament global) és el sistema operat pels Estats Units, mentre que **GNSS** (*Global Navigation Satellite System*, sistema global de navegació per satèl·lit) designa la família de sistemes d'abast global. Per això, el manual usa *GPS* quan es refereix al sistema nord-americà i *GNSS* quan parla de la família o de receptors que combinen diverses constel·lacions.

### Posicionar no és només rebre GPS

El GPS és una tecnologia de posicionament, però no és el nom de totes les maneres d'estimar una posició. Molts sistemes sí que observen **senyals de ràdio**: els GNSS reben emissions de satèl·lits; la telefonia i el Wi-Fi poden relacionar el dispositiu amb transmissors o bases de dades de referència; i les balises Bluetooth o els ancoratges de banda ultraampla (UWB) poden resoldre posicions locals. Totes aquestes opcions necessiten conèixer o estimar alguna propietat dels emissors, del temps de propagació, de la direcció o de la potència rebuda, però difereixen en cobertura, infraestructura i exactitud.

Una classificació publicada l'any 2010 ajuda a veure aquesta diversitat perquè combina dues preguntes: quin **abast aproximat** tenia cada sistema i en quina fase de **maduresa tecnològica** se situava aleshores. La posició vertical representa l'ordre de magnitud de la cobertura o l'abast del sistema, no l'exactitud amb què calculava una coordenada. La posició horitzontal tampoc no és una propietat permanent: «consolidat», «en desenvolupament» o «experimental» descriuen una valoració històrica que depenia del país i de l'aplicació {% cite baskerJammingClearPresent2010 %}.

![Matriu històrica dels sistemes de posicionament per ràdio segons l'abast aproximat i la maduresa que se'ls atribuïa l'any 2010]({{ site.baseurl }}/assets/img/gis/radio-positioning-reach-maturity-2010.svg "El GNSS apareixia consolidat i amb abast global, però coexistia amb sistemes terrestres regionals, telefonia, infraestructura aeronàutica i tecnologies de proximitat. La fletxa entre Loran-C i eLoran representa una evolució proposada. Redibuix interpretatiu propi de la figura «Range and lifecycles of current radio systems», atribuïda a Paul Groves i publicada per Sally Basker a GPS World l'abril de 2010."){: data-figure-width-web="47.5rem" data-figure-width-pdf="100%"}

La comparació no s'ha de llegir com un catàleg vigent. El Bluetooth, el Wi-Fi i l'UWB s'han consolidat en molts usos de localització; la telefonia ha evolucionat amb LTE, 5G i mètodes híbrids; Galileo i BeiDou han canviat el paisatge multiconstel·lació; i sistemes com eLoran, VOR/DME o ILS mantenen trajectòries diferents segons les polítiques i els sectors. El valor de la figura és mostrar que el GNSS ocupa una regió concreta dins d'un ecosistema de tecnologies amb escales i cicles de vida diferents.

Altres mètodes no utilitzen ràdio. Els acceleròmetres i giroscopis estimen canvis de moviment i orientació; l'odometria mesura el desplaçament de rodes o passos; una càmera pot reconèixer fites; el LiDAR observa l'entorn amb llum làser; i els sistemes acústics poden emprar so o ultrasons. Aquestes observacions poden mantenir la continuïtat quan el GNSS queda ocult, però sovint produeixen una posició relativa o acumulen deriva. L'ajust a una xarxa viària o a un plànol conegut tampoc no és un senyal: és una restricció de model que ajuda a corregir o descartar solucions incompatibles {% cite grovesPrinciplesGNSSInertial2013 zafariSurveyIndoorLocalization2019 %}.

![Famílies d'observacions per al posicionament: senyals de ràdio, sensors de moviment i observacions o models de l'entorn convergeixen en una solució fusionada]({{ site.baseurl }}/assets/img/gis/positioning-systems-overview.svg?v=2 "GPS i la resta de GNSS formen part dels mètodes basats en ràdio. Els sensors inercials, l'odometria, la visió, el LiDAR, l'acústica i l'ajust a mapes aporten informació diferent. Els sistemes pràctics poden fusionar diverses fonts i han d'expressar la incertesa i el sistema de referència. Esquema docent d'elaboració pròpia basat en Groves i Zafari et al."){: data-figure-width-web="58rem" data-figure-width-pdf="100%"}

Un telèfon, un vehicle o un robot acostumen a **fusionar observacions** en lloc de confiar sempre en una única font. El GNSS pot aportar una referència global a l'exterior; els sensors inercials poden descriure el moviment entre dues solucions; el Wi-Fi o les balises poden ajudar en interiors; i un mapa pot restringir la posició a recorreguts plausibles. La combinació no elimina els errors: cal conservar una estimació d'incertesa, identificar el sistema de referència i entendre quines fonts estaven disponibles en cada moment.

Un **sistema global de navegació per satèl·lit** (GNSS, de l'anglès *Global Navigation Satellite System*) utilitza una constel·lació per prestar serveis globals de posicionament, navegació i temps. **GPS** és el sistema dels Estats Units; **Galileo**, el de la Unió Europea; **GLONASS**, el de Rússia; i **BeiDou**, el de la Xina. Tots ofereixen serveis civils, encara que la governança i els serveis restringits siguin diferents. GNSS no és una cinquena constel·lació ni un sinònim tècnic de GPS, sinó el nom de la família. Molts receptors actuals combinen observacions de diversos sistemes, fet que augmenta el nombre de satèl·lits potencialment visibles i pot millorar la disponibilitat i la geometria de la solució {% cite euspaWhatGNSS2026 %}.

![Visualització de la Terra envoltada per les òrbites dels satèl·lits de les constel·lacions mundials de navegació GNSS]({{ site.baseurl }}/assets/img/gis/gnss-satellite-fleet-nasa-2026.jpg "Visualització de la flota mundial de satèl·lits GNSS el 2026. Els colors diferencien els operadors de les constel·lacions i fan visible que el posicionament global depèn d'una infraestructura formada per nombrosos satèl·lits i plans orbitals; la imatge no representa la qualitat del senyal en un lloc concret. NASA Scientific Visualization Studio, Science and Technology Corporation i Kel Elkins; font original: NASA SVS 5627; Wikimedia Commons; domini públic als Estats Units."){: data-figure-width-web="48rem" data-figure-width-pdf="100%"}

### Origen militar i obertura del GPS civil

Els antecedents tècnics del GPS inclouen sistemes de navegació per satèl·lit com Transit i programes d'experimentació temporal com Timation. L'any 1973, el Departament de Defensa dels Estats Units va integrar línies de desenvolupament prèvies en el programa Navstar GPS. El sistema es va concebre sota control militar, però la seva evolució va incorporar un ús civil global. Després que el vol civil KAL 007 fos abatut l'any 1983, l'administració de Ronald Reagan va anunciar que, quan el GPS fos operatiu, es posaria a disposició de l'aviació civil. La decisió no va crear immediatament un servei complet, però va establir un compromís polític explícit d'accés civil {% cite nationalResearchCouncilGlobalPositioning1995 speakesCivilGPSAccess1983 %}.

La capacitat operativa inicial es va declarar el 1993 i la capacitat operativa completa, el 1995. Durant els anys noranta, però, la **disponibilitat selectiva** degradava intencionadament la precisió del servei civil estàndard. La seva desactivació el maig de 2000 va reduir de manera immediata aquesta font d'error i va afavorir usos civils i comercials més exigents. El GPS civil ja existia abans de l'any 2000; el canvi va consistir a deixar d'empitjorar-ne deliberadament el senyal obert, no a inaugurar el posicionament civil en aquella data {% cite gpsDirectorateInitialOperationalCapability2014 clintonStopDegradingGPS2000 gpsGovAccuracy2026 %}.

### Els segments espacial, de control i d'usuari

El funcionament del GPS s'organitza en tres segments relacionats. El **segment espacial** inclou els satèl·lits i els senyals que transmeten informació orbital i temporal. El **segment de control** observa les òrbites i els rellotges, avalua l'estat dels satèl·lits i hi carrega dades de navegació actualitzades. El **segment d'usuari** està format pels receptors: equips topogràfics, navegadors, sensors, telèfons o altres dispositius que reben els senyals i calculen posició, velocitat o temps. Les altres constel·lacions tenen arquitectures equivalents, encara que les organitzacions, les estacions i els serveis siguin propis de cada sistema {% cite gpsGovGPSOverview2026 %}.

![Esquema dels tres segments GNSS: satèl·lits, antenes de la xarxa de control i un telèfon com a receptor d'usuari]({{ site.baseurl }}/assets/img/gis/gnss-three-segments.svg?v=3 "Els satèl·lits emeten senyals unidireccionals amb dades orbitals i temporals cap als receptors. La xarxa de control rep telemetria i dades de seguiment, i envia ordres i dades de navegació actualitzades als satèl·lits; les dues fletxes taronges representen aquesta comunicació d'anada i tornada. Els receptors calculen la seva solució sense enviar la posició als satèl·lits. Composició docent pròpia basada en la descripció institucional de GPS.gov; pictogrames adaptats de Lucide, llicències ISC i MIT."){: data-figure-width-web="37rem" data-figure-width-pdf="88%"}

Un receptor convencional és **passiu respecte dels satèl·lits**: escolta els senyals, però no els respon ni els comunica automàticament on es troba. Un telèfon pot transmetre la posició calculada a una aplicació o un servidor mitjançant la xarxa mòbil o una connexió sense fil; aquesta comunicació posterior no forma part del càlcul orbital. La distinció és important per separar el posicionament GNSS de l'ús, l'emmagatzematge o la difusió de la localització per part d'un servei digital.

### El càlcul de la posició

Cada satèl·lit transmet codis i un missatge de navegació associats a una escala temporal molt precisa. El receptor compara el codi rebut amb una rèplica pròpia, estima quant ha trigat el senyal a arribar i multiplica aquest temps per la velocitat de la llum. El resultat s'anomena **pseudodistància** perquè no és la distància geomètrica exacta: també incorpora els desajustos dels rellotges, els retards atmosfèrics, els efectes instrumentals, els senyals reflectits i el soroll del receptor {% cite sanzGNSSBasicObservables2011 %}.

Per obtenir una posició tridimensional, el receptor ha de resoldre quatre incògnites principals: les coordenades `x`, `y` i `z`, i el desajust del seu rellotge respecte del temps del sistema. Els satèl·lits disposen de rellotges atòmics; els receptors de consum utilitzen rellotges molt menys estables. Per això, en condicions ordinàries, calen observacions simultànies d'almenys **quatre satèl·lits**. La quarta observació no es limita a comprovar les altres tres: permet estimar l'error del rellotge del receptor juntament amb la posició. Observar-ne més aporta redundància i pot millorar la geometria, però no garanteix per si sol una posició exacta {% cite vanSickleBasicGISCoordinates2017 %}.

![Quatre satèl·lits envien observacions a un telèfon que representa el receptor i que estima tres coordenades i el desajust del rellotge]({{ site.baseurl }}/assets/img/gis/gnss-four-observations.svg?v=4 "Cada temps de propagació produeix una pseudodistància. Quatre observacions permeten resoldre les tres coordenades de la posició i el desajust temporal del receptor; satèl·lits addicionals aporten redundància i una geometria potencialment més favorable. Composició docent pròpia basada en Van Sickle i Navipedia; pictogrames adaptats de Lucide, llicències ISC i MIT."){: data-figure-width-web="32.5rem" data-figure-width-pdf="77%"}

El missatge de navegació inclou **efemèrides**, que descriuen amb precisió l'òrbita i la correcció de rellotge d'un satèl·lit durant un període relativament curt. L'**almanac** resumeix de manera menys precisa l'estat i les òrbites de la constel·lació durant un període més llarg i ajuda el receptor a preveure quins satèl·lits pot cercar. En posicionament assistit, la xarxa pot facilitar temps aproximat, òrbites o altres dades perquè el receptor adquireixi els senyals més ràpidament; la posició continua depenent de les observacions i del mètode de càlcul, no només de descarregar un almanac {% cite vanSickleBasicGISCoordinates2017 djuknicGeolocationAssistedGPS2001 %}.

La **planificació de la missió** continua sent rellevant quan la qualitat exigida és alta. Abans d'un aixecament convé anticipar obstacles, hores d'observació, geometria de les constel·lacions, durada, punts de control i mètode de correcció. Els receptors multiconstel·lació han reduït els intervals amb pocs satèl·lits, però no eliminen edificis, arbres, relleu, interferències ni una antena mal situada.

>> **Recurs recomanat: [Trimble GNSS Planning](https://www.gnssplanning.com).** Aquesta aplicació web permet fixar el lloc, la data, l'interval temporal, l'angle de tall i les constel·lacions, i després explorar la disponibilitat prevista mitjançant gràfics, un diagrama del cel i una vista mundial. Convé provar la localització d'una pràctica de camp i comparar què canvia en modificar l'hora, l'angle de tall o els sistemes activats. La predicció ajuda a planificar i a entendre la geometria dels satèl·lits, però no incorpora tots els obstacles i errors locals ni garanteix l'exactitud que s'obtindrà.

### Qualitat de la posició i fonts d'error

La qualitat d'una posició no es pot resumir amb una xifra universal. GPS.gov ofereix com a exemple una exactitud típica d'uns 4,9 m de radi per a un telèfon sota cel obert, però adverteix que empitjora prop d'edificis, ponts i arbres. Altres proves amb telèfons han obtingut errors horitzontals medians de diversos metres en condicions exteriors i resultats pitjors a l'interior. Aquestes xifres descriuen equips, llocs i procediments concrets; no són una garantia aplicable a qualsevol observació {% cite gpsGovAccuracy2026 zandbergenPositionalAccuracyAssisted2011 %}.

::: table "Factors que condicionen una observació GNSS"
| Factor | Com afecta el resultat | Control possible |
| --- | --- | --- |
| Geometria dels satèl·lits | Satèl·lits concentrats en una mateixa part del cel amplifiquen la incertesa | Observar més constel·lacions, revisar indicadors de geometria i canviar l'hora si l'ús exigeix més control |
| Atmosfera | La ionosfera i la troposfera alteren el temps de propagació | Utilitzar més d'una freqüència, models o serveis de correcció quan l'objectiu ho requereixi |
| Obstacles i multitrajecte | Edificis, relleu i vegetació bloquegen senyals o en produeixen reflexos que recorren un camí més llarg | Buscar cel obert, separar-se de parets i repetir o contrastar observacions |
| Receptor, antena i mètode | El disseny, el soroll, la posició de l'antena, la durada i les correccions condicionen la solució | Documentar l'equip i el mètode, estabilitzar l'antena i aplicar controls adequats a l'escala |
| Referència i sortida | Una altura, un CRS o una marca temporal mal interpretats poden desplaçar o invalidar la dada | Conservar sistema de referència, tipus d'altura, data, hora, unitats i estimadors de qualitat |
:::

![Efecte de multitrajecte en una vall: els senyals directes arriben al receptor per un camí curt i els reflectits recorren un camí més llarg]({{ site.baseurl }}/assets/img/gis/gnss-multipath-commons.png "El verd representa el trajecte directe del senyal i el vermell, trajectes reflectits per les parets del relleu. L'esquema utilitza satèl·lits GPS, però el mateix problema de propagació afecta altres senyals GNSS. Obra derivada de Javiersanp, a partir de Vaughan Weather, NASA i Realbrvhrt; Wikimedia Commons, 9 d'abril de 2010, CC BY-SA 3.0."){: data-figure-width-web="34rem" data-figure-width-pdf="64%"}

El multitrajecte explica per què un nombre alt de satèl·lits visibles no garanteix una bona solució. En un carrer estret, un receptor pot utilitzar senyals directes, bloquejats i reflectits alhora; la geometria aparent és abundant, però algunes pseudodistàncies representen camins més llargs que la línia directa. També cal diferenciar **exactitud**, que compara la posició amb una referència, de **repetibilitat**, que descriu fins a quin punt diverses mesures s'agrupen. Un conjunt de punts molt agrupats pot continuar desplaçat respecte de la posició real.

### La generalització del posicionament mòbil

Durant els anys noranta, els receptors dedicats es van abaratir i es van estendre en navegació, topografia, logística i treball de camp. La generalització social va augmentar a partir de finals dels anys dos mil, quan els telèfons intel·ligents van integrar receptors GNSS, connexió mòbil, mapes, càmera, rellotge, sensors de moviment i aplicacions en un mateix dispositiu. Això va permetre georeferenciar fotografies, formularis, incidències, activitats esportives i trajectes sense portar un equip específic per a cada tasca.

La posició que mostra un telèfon no sempre procedeix d'una observació GNSS autònoma. El **GNSS assistit** pot obtenir per xarxa una estimació inicial de temps i lloc, dades orbitals o informació que redueix el temps d'adquisició. El sistema operatiu també pot combinar GNSS amb xarxes Wi-Fi, antenes de telefonia i sensors inercials. Els dispositius moderns poden observar GPS, Galileo, GLONASS i BeiDou, i alguns incorporen més d'una freqüència; aquestes capacitats poden millorar la disponibilitat i reduir alguns errors, però no converteixen qualsevol telèfon en un receptor centimètric. Els resultats d'alta precisió exigeixen condicions favorables, observacions adequades, correccions i processament especialitzat {% cite djuknicGeolocationAssistedGPS2001 robustelliAssessmentDualFrequency2019 %}.

L'accés massiu ha multiplicat les dades georeferenciades disponibles: traces aportades a projectes col·laboratius, fotografies amb coordenades, registres de mobilitat, formularis de camp i observacions ciutadanes. El volum no elimina els biaixos. Hi ha més dades on hi ha més dispositius, cobertura, aplicacions o persones disposades a contribuir, i una trajectòria pot revelar domicilis, llocs de treball o hàbits. La qualitat, la representativitat, la finalitat i la privacitat s'han d'avaluar amb els criteris de fonts i protecció de dades del [capítol 1]({{ site.baseurl }}/ca/chapters/fonts-preparacio-dades/) {% cite goodchildCitizensSensors2007 %}.

### Integració de les observacions GNSS en un SIG

Un receptor pot produir una posició puntual, una successió temporal de posicions o mesures més detallades del senyal. Per incorporar el resultat a un SIG no n'hi ha prou amb conservar dos nombres. Cal registrar com a mínim la data i l'hora, el sistema de referència, el tipus d'altura si s'utilitza, el dispositiu o mètode, una estimació de qualitat i el significat de l'objecte observat. El GPS treballa vinculat a WGS 84, però una aplicació pot transformar o presentar les coordenades en altres referències; l'altura el·lipsoidal tampoc no equival automàticament a una cota sobre el nivell del mar, tal com s'explica al [capítol 4]({{ site.baseurl }}/ca/chapters/terra-dades-espacials/).

::: table "De l'observació del receptor a una capa"
| Observació | Representació habitual al SIG | Metadades i controls mínims |
| --- | --- | --- |
| Posició d'un recurs o incidència | Punt amb atributs | Data i hora, CRS, altura si escau, dispositiu, qualitat estimada i identificador de l'objecte |
| Successió de posicions | Línia o traça temporal | Ordre i interval de mostreig, buits, velocitats, aturades i regla de simplificació |
| Fotografia o formulari de camp | Punt o geometria vinculada a documents i atributs | Autoria, finalitat, correspondència entre registre i lloc, llicència i dades personals |
:::

Registrar la posició d'un recurs turístic és una operació de **captura**. Comprovar en quin municipi es troba, relacionar-lo amb una xarxa, calcular-ne l'accessibilitat, detectar concentracions o combinar-lo amb dades de demanda són operacions **SIG**. Més endavant, el capítol crearà punts des d'una taula de coordenades i comprovarà el CRS abans d'interpretar-los. Aquesta separació entre observació, dada documentada i anàlisi evita atribuir al receptor decisions que corresponen al sistema d'informació i al mètode de treball.

## Aplicacions i preguntes espacials

Les aplicacions dels SIG es poden entendre millor com a famílies de preguntes que no pas com una llista de botons. Una mateixa base pot servir per consultar, seleccionar, mesurar, relacionar, modelitzar o comunicar, però cada operació necessita dades i controls diferents.

::: table "Preguntes que pot abordar un SIG"
| Pregunta | Operació habitual | Exemple territorial o turístic | Precaució |
| --- | --- | --- | --- |
| Què hi ha aquí? | Identificació i consulta d'atributs | Consultar la categoria i la capacitat d'un allotjament seleccionat | La posició i els atributs han de representar la mateixa entitat i data |
| On es compleixen unes condicions? | Filtre alfanumèric, selecció espacial, superposició o àrea d'influència | Localitzar recursos accessibles prop d'una estació i dins d'un municipi | La distància en línia recta no equival necessàriament a accessibilitat real |
| Què ha canviat? | Comparació temporal i detecció de canvis | Mesurar l'expansió urbana o els canvis d'ús del sòl en una destinació | Les fonts i classificacions de les dues dates han de ser comparables |
| Quin recorregut respon al criteri? | Anàlisi de xarxes i rutes | Calcular un itinerari segons temps, pendent o mode de transport | La ruta depèn de la xarxa, les restriccions i els costos definits |
| Quin patró espacial s'observa? | Densitats, veïnatges, agrupacions i estadística espacial | Examinar si l'oferta turística es concentra al litoral o al voltant de nodes | Un patró espacial no demostra per si sol una causa |
| Què podria passar? | Modelització i simulació d'escenaris | Estimar àrees exposades a inundació o canvis en temps d'accés | Un model simplifica la realitat i ha d'explicitar supòsits i incertesa |
:::

### Selecció espacial, proximitat i superposició

Una consulta alfanumèrica selecciona entitats a partir dels atributs: per exemple, allotjaments amb una capacitat superior a un llindar o municipis amb un percentatge determinat. Una **selecció espacial** aplica una relació entre geometries: punts dins d'un municipi, equipaments que intersequen una zona inundable, parcel·les que toquen una via o recursos situats a una distància definida d'una estació. Les condicions temàtiques i espacials es poden combinar, però no són equivalents. Que un establiment compleixi una condició d'atributs no indica on és; que caigui dins d'un polígon no garanteix que la seva informació sigui completa o actual.

La relació s'ha de formular amb precisió. «Dins de», «interseca», «toca», «se superposa» i «és a menys de» poden retornar conjunts diferents, especialment quan una entitat queda sobre un límit o quan les geometries tenen errors. La selecció és un estat temporal dins del projecte; si cal conservar-la, s'ha d'exportar com una capa derivada amb la consulta, la data i el recompte documentats. Aquesta distinció evita confondre les entitats ressaltades a la pantalla amb una nova font de dades.

Les àrees d'influència o *buffers* representen una distància al voltant d'una geometria. Són útils per fer una primera aproximació a la proximitat, però un radi de 500 m no equival automàticament a cinc minuts a peu: pot travessar vies sense pas, pendents, rius o recintes tancats. La **superposició espacial** combina capes per identificar interseccions, inclusions o parts comunes. Permet preguntar quina oferta queda dins d'una àrea protegida o quines seccions d'una ruta travessen una zona de risc, però exigeix geometries, escala, data i CRS compatibles. El resultat hereta els límits i les incerteses de totes les entrades {% cite longleyGeographicInformationScience2015 %}.

### Xarxes, rutes i costos acumulats

Una xarxa representa connexions mitjançant **nodes** i **arcs**. Els arcs poden tenir un pes de distància, temps, desnivell, tarifa o una combinació documentada. La ruta «més curta» només és la de menor longitud si aquest és exactament el pes adoptat; una ruta de menor temps pot ser més llarga en metres, i una ruta accessible pot excloure escales o aplicar una penalització al pendent. També cal modelar sentits de circulació, girs prohibits, horaris, transbordaments i trams temporalment tancats quan siguin rellevants.

L'algorisme de Dijkstra calcula un camí de cost mínim en una xarxa amb pesos no negatius. Parteix de l'origen amb cost zero, actualitza el millor cost conegut dels nodes veïns i fixa successivament el node pendent amb menor cost acumulat fins a arribar a la destinació {% cite dijkstraNoteTwoProblems1959 %}. El procediment garanteix el mínim respecte dels pesos proporcionats, no respecte d'una realitat que no s'hagi codificat. Una xarxa incompleta o uns temps mal assignats poden produir un resultat matemàticament correcte i territorialment inútil.

### Accessibilitat i càlcul d'isòcrones

Una ruta respon com arribar d'un origen a una destinació; una **isòcrona** delimita fins on es pot arribar des d'un origen amb un mateix cost acumulat, normalment temps. Les corbes o polígons de 10, 20 i 30 minuts no són circumferències: segueixen la connectivitat de la xarxa i s'estenen més pels corredors ràpids que pels carrers lents, els pendents o les barreres. En turisme poden comparar l'accés a platges, allotjaments, estacions o equipaments; en planificació pública poden mostrar quina població queda coberta per un servei {% cite osullivanDesktopGISIsochrone2000 %}.

El càlcul necessita una xarxa connectada i costos adequats al mode de transport. En una isòcrona a peu cal considerar passos, escales, pendents i trams no transitables; en transport públic, itineraris, parades, freqüències, temps d'espera i transbordament; i en vehicle privat, sentits, girs, velocitats i, si la pregunta ho exigeix, congestió segons l'hora. La mateixa ubicació pot generar àrees diferents segons el moment de sortida, el perfil de mobilitat i si el cost representa només moviment o també espera.

Una isòcrona modela **accessibilitat potencial**, no ús efectiu. Que un recurs quedi dins dels 20 minuts no demostra que sigui conegut, assequible, obert o adequat per a tothom. Cal indicar origen, llindars, mode, data de la xarxa, regla de cost i qualsevol exclusió. Comparar una isòcrona amb un *buffer* circular és una prova didàctica útil perquè mostra quina part de la resposta depèn de la xarxa i no només de la distància euclidiana.

### Geomàrqueting i localització de serveis

El **geomàrqueting** relaciona la distribució espacial de la demanda, l'oferta i la competència per donar suport a decisions de localització, cobertura i comunicació. Un establiment turístic pot estudiar d'on procedeixen les reserves; una oficina d'informació, quines àrees queden mal cobertes; i una xarxa comercial, si una nova obertura amplia el mercat o redistribueix clients entre punts existents. Les operacions habituals combinen geocodificació, àrees de mercat, isòcrones, matrius origen-destinació, perfils territorials i models de localització-assignació {% cite cliquetGeomarketing2006 %}.

La unitat d'anàlisi condiciona la decisió. Les dades de residents, visitants, despesa, mobilitat i oferta poden referir-se a domicilis, seccions censals, zones estadístiques, cel·les o punts de venda, amb períodes i cobertures diferents. Assignar a cada persona el valor mitjà del seu barri produeix una inferència ecològica injustificada; comparar polígons de mida desigual pot crear patrons artificials; i utilitzar només transaccions pròpies descriu la clientela observada, no tot el mercat potencial.

La localització comercial tampoc no anul·la les obligacions ètiques i legals. Les traces individuals, adreces i perfils de consum poden ser dades personals o permetre reidentificació quan es combinen. Cal treballar amb la mínima informació necessària, agregacions i llindars de recompte adequats, accés controlat i una finalitat explícita. Un mapa de segments és una construcció analítica per a una decisió concreta, no una descripció completa de les persones que viuen o circulen en un lloc.

### Epidemiologia espacial i salut pública

L'**epidemiologia espacial** estudia com es distribueixen esdeveniments de salut, poblacions exposades, possibles fonts i serveis sanitaris. Un SIG pot ajudar a geocodificar casos, calcular taxes per població en risc, detectar concentracions espaciotemporals, estimar accessibilitat assistencial o explorar relacions amb exposicions ambientals. Els recomptes bruts no basten: una zona amb més casos pot tenir simplement més població, una estructura d'edat diferent o una detecció més intensa.

La investigació de John Snow sobre el brot de còlera de Broad Street a Londres el 1854 és un precedent clàssic. El [mapa de defuncions i bombes d'aigua](https://commons.wikimedia.org/wiki/File:Snow-cholera-map-1.jpg) va fer visible una concentració al voltant d'una bomba, però l'argument no va sortir del mapa tot sol. Snow va combinar localització de morts, entrevistes, coneixement de l'abastiment d'aigua i comparacions entre poblacions. Presentar el cas només com un patró de punts que va revelar automàticament una causa simplifica tant el mètode com la història {% cite brodyMapMakingMythMaking2000 %}.

En dades actuals, la posició d'un cas pot correspondre al domicili, al lloc d'exposició, al diagnòstic o al centre assistencial, i cada opció respon una pregunta diferent. També cal controlar període, definició de cas, denominador, mobilitat, retard de notificació i qualitat de geocodificació. Com que la informació sanitària és especialment sensible, la cartografia pública ha d'evitar punts identificables i agregacions amb recomptes petits. Un patró espacial pot orientar una investigació, però no demostra per si sol transmissió ni causalitat.

### Densitats, interpolació i patrons espacials

Quan hi ha molts punts, una densitat pot resumir on es concentren esdeveniments com incidències, visites o accidents. El resultat depèn de la mida de cel·la, el radi de cerca, el nucli i, si escau, el pes assignat a cada punt. Una superfície suau no converteix automàticament observacions discretes en un fenomen continu: pot mostrar intensitat d'esdeveniments, intensitat per població exposada o només cobertura desigual de la font, segons les dades utilitzades.

La interpolació estima valors en llocs sense observació a partir d'una hipòtesi de continuïtat espacial. És defensable per a variables com elevació, temperatura o contaminació quan el procés, el mostreig i el mètode ho permeten; no ho és per omplir mecànicament categories administratives o preferències individuals. Les agrupacions i els valors atípics espacials també necessiten una hipòtesi nul·la, una escala de veïnatge i control de proves múltiples. Visualitzar un patró és el començament de l'anàlisi, no la seva explicació {% cite longleyGeographicInformationScience2015 %}.

### Relleu, visibilitat i superfícies contínues

Un model digital d'elevacions permet derivar pendent, orientació, ombrejat, perfils, drenatge o visibilitat. Una **conca visual** classifica quines cel·les mantenen línia de visió amb un observador. El càlcul necessita l'altitud de cada cel·la, la posició i l'altura de l'observador i, segons l'escala, l'altura de l'objectiu, la curvatura terrestre i la refracció. Si el ràster representa només el terreny, no hi apareixen necessàriament arbres, edificis o altres obstacles. Per tant, una conca visual és el resultat d'un model i no una fotografia de tot allò que es veu realment.

![Ruta de cost mínim calculada sobre una xarxa amb pesos en minuts i conca visual amb l'observador prop d'un extrem del model d'elevacions]({{ site.baseurl }}/assets/img/gis/gis-analysis-examples.svg?v=2 "El panell esquerre modela una xarxa sintètica amb temps de recorregut i aplica Dijkstra per obtenir la ruta A–B–D–G–I, de cost total 11 minuts. El panell dret situa l'observador prop del marge dret i calcula una conca visual: el relleu deixa cel·les visibles al mateix vessant, mentre que la muntanya oculta bona part del vessant oposat. El conjunt docent `volcano` representa Maunga Whau i no s'ha de considerar un aixecament precís. Figura d'elaboració pròpia."){: data-figure-width="58rem"}

La figura comparteix una idea metodològica: abans d'escollir l'algorisme cal representar el problema. La ruta necessita una xarxa i una definició de cost; la conca visual necessita un ràster d'elevacions i una definició de l'observador. En el panell dret, el punt se situa gairebé al límit del model. El groc s'estén sobretot pel mateix costat de la muntanya, mentre que el vessant que queda més enllà del relleu no manté línia de visió. La frontera irregular no és un radi de distància: resulta de comparar l'angle vertical de cada cel·la amb els obstacles intermedis.

Canviar una entrada pot modificar la resposta encara que el codi sigui idèntic. Desplaçar l'observador, elevar-lo, afegir edificis o utilitzar un model de superfície en lloc d'un model del terreny altera la conca visual. Altres operacions segueixen la mateixa lògica: una isòcrona depèn de la xarxa i del cost, una densitat depèn del radi o nucli, una interpolació depèn de les observacions i del model de continuïtat, i una simulació depèn dels supòsits que converteixen processos territorials en regles calculables.

En el projecte del curs es prioritzaran la consulta, la selecció espacial, la localització condicionada, les unions i la lectura de patrons. Les isòcrones, el geomàrqueting, l'epidemiologia espacial, la modelització del relleu, la interpolació i l'estadística espacial mostren l'abast professional dels SIG, però no s'han d'aplicar sense dades i coneixements metodològics suficients. Reconèixer què podria fer un SIG no implica que qualsevol eina avançada sigui adequada per a la pregunta o avaluable en aquest curs.

## El SIG d'escriptori del manual

Les categories i els components anteriors permeten situar l'eina escollida per al curs. En aquest manual s'utilitzarà [**QGIS Desktop**](https://www.qgis.org/project/overview/) perquè és programari lliure i de codi obert, funciona als principals sistemes operatius i permet inspeccionar, editar, analitzar i representar dades geogràfiques dins d'un projecte revisable. També pot llegir formats i serveis geoespacials habituals, de manera que resulta adequat per relacionar fonts estadístiques i cartogràfiques sense vincular l'aprenentatge a una llicència propietària.

QGIS és una peça d'un projecte geoespacial més ampli que també inclou opcions de servidor, aplicacions mòbils relacionades, complements i serveis professionals. El curs se centrarà en l'aplicació d'escriptori: la taula municipal preparada al llibre de càlcul es vincularà amb els límits de la comarca, es consultaran els atributs i es conservarà el projecte editable que documenta la integració. Les capes i els mapes exportats podran alimentar una publicació posterior, mentre que el desplegament d'un WebGIS complet i la programació de biblioteques geoespacials queden fora de l'abast pràctic d'aquest manual.

La instal·lació recomanada i les versions de referència de QGIS, LibreOffice i Inkscape es recullen al [capítol 0]({{ site.baseurl }}/ca/#installacio-programari). Abans d'iniciar les activitats pràctiques de SIG cal comprovar que QGIS s'obre correctament, que permet crear un projecte i que es coneix la carpeta on es desaran les dades. La tria del programa concreta l'entorn de treball, però els criteris sobre fonts, mètodes, components i qualitat continuen sent aplicables a altres SIG.

## El mapa és una sortida, no tot el sistema

Un mapa és una de les sortides possibles d'un SIG, juntament amb una taula, una capa derivada, una mesura, un informe, una base de dades o un servei web. La cartografia fa visible una selecció del resultat, però no conserva necessàriament totes les dades, consultes i decisions que l'han produït. Per això el projecte editable, les capes i la documentació continuen sent necessaris encara que la peça final sigui un PDF.

QGIS ofereix eines de simbolització i composició suficients per produir mapes complets. Si la integració amb altres gràfics o textos exigeix un acabat més controlat, el mapa es pot exportar en PDF o SVG vectorial i obrir a Inkscape. És legítim ajustar la disposició a la pàgina, la jerarquia tipogràfica, els espais, els crèdits o elements decoratius, sempre que el mapa continuï representant el mateix resultat i mantingui llegibilitat, escala i atribució.

>>>> **El retoc gràfic no pot corregir ni reescriure l'anàlisi espacial.** No s'han de moure municipis, punts o límits per fer-los encaixar; estirar el mapa; redibuixar geometries; canviar classes o valors; eliminar absències; alterar proporcions de símbols; ni conservar una escala gràfica després d'haver deformat la peça. Si cal modificar l'extensió, la projecció, la classificació, la simbologia, les etiquetes vinculades a dades o qualsevol geometria, la correcció s'ha de fer al projecte QGIS i s'ha de tornar a exportar. Inkscape serveix per compondre i acabar, no per trencar la correspondència entre dada i espai.

## Flux de treball SIG revisable

Aprendre a treballar amb un SIG en un context universitari exigeix construir una cadena de treball revisable. Localitzar menús és només una part de la tasca. Abans d'una unió, cal saber quina taula aporta els indicadors, quina capa aporta les geometries i quin camp permet relacionar-les. Després de la unió, cal comprovar si el nombre d'entitats, les claus i els valors continuen tenint sentit. Entre una captura vistosa i un resultat defensable hi ha una diferència metodològica: la segona opció permet reconstruir com s'ha arribat al mapa.

El projecte comarcal es pot entendre com quatre capes de responsabilitat. La primera és **documental**: conservar fonts, llicències, dates i definicions. La segona és **estructural**: mantenir una fila per municipi, camps amb tipus adequats i codis territorials coherents. La tercera és **espacial**: revisar CRS, geometria, extensió, escala i correspondència territorial. La quarta és **comunicativa**: decidir quines consultes, mapes i exportacions expliquen el resultat sense ocultar errors o absències. Si una d'aquestes capes falla, el mapa pot aparèixer igualment a la pantalla, però la interpretació quedarà debilitada.

>>>>> Aquesta fase transforma l'ús de QGIS en un flux de treball territorial que es pot reconstruir i revisar.
>>>>>
>>>>> - Formular la pregunta, el territori, el període i la unitat d'observació abans d'escollir una operació.
>>>>> - Identificar per a cada entrada la font, la data, la llicència, el CRS, els camps clau i el nombre de registres.
>>>>> - Ordenar les fases de preparació, unió, consulta i sortida amb un control explícit a cada pas.
>>>>> - Preservar originals i documentar transformacions perquè el resultat es pugui reproduir.
>>>>> - Diferenciar el sistema de treball, el projecte editable i la sortida que comunica una part del resultat.

::: table "De la pregunta territorial a una sortida SIG revisable"
| Fase | Decisió principal | Control mínim |
| --- | --- | --- |
| Pregunta | Quina relació territorial es vol observar? | Fenomen, territori, període i unitat d'observació explícits |
| Entrades | Quina geometria i quina taula s'utilitzen? | Font, data, llicència, CRS, camps clau i nombre de registres |
| Preparació | Quines transformacions són necessàries? | Camps nous documentats, originals preservats i valors contrastats |
| Unió | Com es relacionen geometries i indicadors? | Cardinalitat, duplicats, coincidències, absències i nuls |
| Consulta | Què es pot preguntar al resultat unit? | Filtres i seleccions descrits sense convertir-los en conclusions causals |
| Sortida | Quin mapa, taula o fitxer es conservarà? | Format, estil, escala, fonts i ruta dins del projecte |
:::

Aquest esquema també ajuda a repartir responsabilitats entre teoria i laboratori. La teoria dona el vocabulari per parlar de georeferenciació, geometria, atribut, sistema de referència, escala i patró espacial. El laboratori converteix aquest vocabulari en comprovacions concretes: obrir propietats de capa, revisar una taula, normalitzar una clau, filtrar municipis, executar una unió i registrar el resultat. Cap de les dues parts funciona sola; sense criteri conceptual, QGIS es redueix a recepta, i sense pràctica, els conceptes no arriben a una decisió operativa.

## Fonts cartogràfiques i serveis geogràfics

### Capes oficials de límits administratius

Les geometries han de provenir de fonts documentades, tenir una escala adequada i conservar informació sobre el sistema de referència i la data.

En el laboratori es podrà utilitzar el connector [**Open ICGC**](https://www.icgc.cat/en/Tools-and-viewers/Tools/Connector-QGIS-Open-ICGC) de QGIS com a accés ràpid a la geoinformació de l'Institut Cartogràfic i Geològic de Catalunya. El connector, disponible també al [repositori de connectors de QGIS](https://plugins.qgis.org/plugins/OpenICGC/), incorpora una barra d'eines per carregar capes de referència, cercar topònims i adreces, consultar ortofotos, afegir fons cartogràfics i descarregar productes vectorials o ràster quan cal treballar sense connexió. Aquesta comoditat no substitueix la lectura de metadades: abans d'utilitzar una capa com a geometria d'anàlisi cal identificar productor, data, escala, CRS, llicència i si el recurs és una imatge de fons, un servei de visualització o una capa vectorial amb atributs.

![Espai de treball per documentar el connector Open ICGC dins de QGIS, amb accés a fons de mapa, ortofoto i límits administratius]({{ site.baseurl }}/assets/img/placeholders/qgis-open-icgc-placeholder.svg "QGIS i Open ICGC: selecció d'un fons de mapa i localització de límits administratius o divisions territorials."){: data-figure-width-web="41.5rem" data-figure-width-pdf="99%"}

Els fons de mapa de l'ICGC són molt útils per orientar el lector, comprovar si una capa cau on toca i construir un mapa de referència. En canvi, una unió d'indicadors municipals necessita una capa vectorial de límits amb camps identificadors. Si el connector ofereix diverses vies per arribar a un límit administratiu, s'ha de triar la que permeti conservar la geometria i els atributs necessaris, no només la que es veu millor al llenç.

### Fitxers i serveis de dades

Les capes descarregables permeten conservar una versió local, inspeccionar-ne l'esquema i processar-la sense dependre permanentment del servidor. Els serveis d'objectes poden proporcionar geometries i atributs consultables, mentre que els serveis de mapes o imatges estan orientats principalment a la visualització. Que QGIS pugui mostrar un recurs no significa que aquest es pugui editar, analitzar o distribuir de la mateixa manera.

La procedència i les metadades s'han de conservar en tots els casos. Un servei pot canviar mantenint la mateixa adreça, i una capa local pot quedar descontextualitzada si se'n perd la data, la llicència o el sistema de referència. La base municipal validada al capítol 4 continuarà sent la geometria de treball del projecte.

## Estructura i consulta de les taules d'atributs

### Entitats, camps i tipus de dada

La taula d'atributs connecta cada **geometria**, la representació espacial d'una entitat, amb els seus **atributs**, els valors alfanumèrics que la descriuen. Els camps de text, enters i decimals tenen comportaments diferents en filtres, càlculs i unions.

### Seleccionar, ordenar i filtrar

Abans de representar una variable cal saber inspeccionar els registres i localitzar casos concrets o valors absents.

La selecció respon una condició temporal dins del projecte; no modifica necessàriament les dades. Un filtre limita quines entitats es mostren o es processen, i una exportació crea un resultat nou. Cal distingir aquestes operacions per no confondre una vista parcial amb una capa que només conté la comarca.

## Importació de taules i creació de punts a QGIS

### Preparar la taula externa

Durant aquest capítol es crearà o regenerarà el full `map_export`. L'esquema canònic de la demostració tindrà una fila per municipi i agruparà aquests camps:

- fulls d'entrada: `municipal`, `indicators_demography` i `indicators_housing`;
- identificació: `mun_code`, `municipality`, `county_code` i `year`;
- demografia: `population_total`, `population_65_plus` i `population_65_plus_pct`;
- habitatge: `housing_total`, `housing_non_main` i `housing_non_main_pct`;
- control: `indicator_status`.

Un resultat no calculable s'exportarà com a nul amb un estat explicatiu, mai com a zero o com el text `#N/A`. El CSV UTF-8 és una còpia de transferència: si canvia una fórmula, s'ha de regenerar des del llibre, no corregir-lo a mà.

La primera fila contindrà una única capçalera. No s'hi inclouran cel·les combinades, subtotals, notes de presentació, gràfics ni files comarcals barrejades amb els municipis. Els codis han de conservar la longitud i els zeros inicials; els valors absents es distingiran dels zeros; i els indicadors calculats s'exportaran amb el valor resultant. El CSV no substitueix les fórmules ni el diccionari conservats al llibre.

Un CSV no conserva per si sol el tipus de cada camp. En importar-lo a QGIS, el codi s'ha de declarar o interpretar explícitament com a text i verificar-se abans de la unió. El delimitador de camps i el separador decimal s'escolliran de manera que la importació sigui inequívoca. Després de l'exportació s'ha de tornar a importar o inspeccionar una mostra per confirmar que el nombre de columnes, els accents, els decimals i els identificadors es mantenen correctament.

### Importar i comprovar

La importació no acaba quan la taula apareix al projecte. Cal revisar caràcters, separadors, camps, files i interpretació dels valors. El nombre de registres ha de coincidir amb les files municipals de `map_export`, els codis s'han de conservar com a text quan l'esquema ho requereixi i els indicadors han de continuar sent numèrics.

Abans d'unir, almenys dos municipis i dos indicadors es contrastaran amb `indicators_demography` i `indicators_housing`. Aquesta comprovació separa els errors d'exportació dels errors que es puguin produir després durant la unió.

### Demostració obligatòria: coordenades a punts

Algunes fonts no arriben com una capa de municipis, sinó com una taula amb coordenades. Pot passar amb equipaments turístics, punts d'informació, allotjaments, recursos patrimonials o adreces geocodificades. En aquest cas, QGIS pot carregar el CSV com a capa de text delimitat i crear geometries puntuals a partir dels camps X i Y. La decisió crítica és indicar el **CRS declarat per la font**, no deduir-lo només perquè els valors semblin graus o metres. En aquesta demostració, la font identifica les coordenades geogràfiques com a WGS84 i per això s'importen amb `EPSG:4326`; també declara les coordenades UTM com a ETRS89 / UTM 31N, corresponents a `EPSG:25831`.

La demostració de coordenades utilitzarà el Directori anual de centres docents de la Generalitat del curs 2025/2026. Primer es filtraran els centres de Vila-seca per obtenir un conjunt petit i comprovable; després es podrà ampliar al Tarragonès per resumir recomptes municipals. La font conté coordenades ETRS89 / UTM 31N, longitud i latitud, adreça i codi municipal de sis dígits. El punt representa l'entrada del centre, no tota la parcel·la, la capacitat ni la població atesa. Aquesta capa és una demostració auxiliar de creació de punts i no s'ha de presentar com si compartís el període 2021 dels indicadors censals.

La mateixa taula es carregarà una vegada amb X/Y UTM i `EPSG:25831` i una altra amb longitud/latitud i `EPSG:4326`. Les dues capes han de coincidir després que QGIS les reprojecti dinàmicament al sistema de referència del projecte. La captura conservarà el diàleg de text delimitat amb els camps X i Y, el CRS d'origen i la previsualització de tipus; no cal capturar la capa ja carregada si el mapa exportat mostra millor el resultat.

Les coordenades UTM d'una taula poden identificar un punt o formar part de la referència d'una quadrícula. Quan la font identifica una cel·la, com les [quadrícules UTM de l'ICGC](https://www.icgc.cat/es/Geoinformacion-y-mapas/Datos-y-productos/Geoinformacion-cartografica/Cuadriculas-UTM) amb [codis MGRS del tipus `31TCG213911`](https://www.icgc.cat/es/Ayuda/Preguntas-frecuentes/Coordenadas-de-tipo-31TCG213911), el parell E/N associat permet situar la cantonada de referència del quadrat i dona nom al polígon, però no descriu per si sol el centre ni un objecte puntual. En aquests casos convé carregar o construir la capa poligonal de quadrícula i, només si l'objectiu cartogràfic ho justifica, derivar-ne un punt auxiliar documentat {% cite icgcQuadriculesUtmEspecificacions2026 %}.

![Espai de treball per documentar la importació d'un CSV, la unió amb límits municipals i la creació de punts a partir de coordenades]({{ site.baseurl }}/assets/img/placeholders/qgis-data-operations-placeholder.svg "QGIS: diàleg d'importació de text delimitat, configuració de la unió i conversió de camps X/Y en punts."){: data-figure-width-web="38rem" data-figure-width-pdf="90%"}

Crear punts i unir indicadors municipals són operacions diferents. Una **unió mitjançant codi territorial** transfereix atributs a una geometria administrativa existent; una **capa de punts** crea entitats noves a partir de posicions. Si després cal resumir punts per municipi, caldrà una operació espacial específica i una comprovació diferent, perquè el resultat dependrà de la precisió de les coordenades i dels límits utilitzats.

### Ampliació opcional: geocodificació

Com a ampliació s'utilitzarà un subconjunt reduït d'allotjaments convencionals de Vila-seca del Registre de Turisme de Catalunya. Es conservaran l'adreça original, el resultat retornat pel geocodificador de l'ICGC, els codis territorials, les coordenades i un estat d'èxit, ambigüitat o revisió manual. No s'inclouran noms de titulars ni altres camps personals que no siguin necessaris. El registre descriu oferta inscrita, no obertura, disponibilitat, ocupació o pernoctacions.

## Unions mitjançant codis territorials

Una unió necessita camps compatibles i una correspondència clara entre registres. Els noms geogràfics només s'utilitzaran quan no hi hagi un identificador més robust.

Els dos camps originals s'han de conservar encara que no comparteixin longitud, prefix o tipus. Si cal adaptar-los, es crearan camps normalitzats nous amb noms explícits, com `mun_code_norm`. Retallar espais, completar zeros o eliminar un prefix només és legítim quan l'esquema territorial documenta la transformació.

>>>>> Aquesta fase relaciona geometries i indicadors mitjançant claus territorials compatibles i controls alfanumèrics i espacials.
>>>>>
>>>>> - Comparar les claus de la capa i de la taula segons el tipus, la longitud, els prefixos, els zeros inicials i la unicitat.
>>>>> - Crear camps normalitzats reproduïbles sense alterar els codis territorials originals.
>>>>> - Confirmar una cardinalitat d'un a un abans d'executar la unió municipal.
>>>>> - Comptar coincidències, absències, duplicats i files no utilitzades sense convertir els nuls en zeros.
>>>>> - Contrastar municipis i valors amb el llibre i amb la seva distribució espacial abans de materialitzar o simbolitzar el resultat.

### Clau de la capa i clau de la taula

#### Cardinalitat esperada

El projecte necessita una fila d'indicadors per cada municipi de la capa comarcal. Aquesta **correspondència d'un a un** exigeix **claus úniques als dos costats**. Si `map_export` conté més d'una fila amb el mateix codi, la unió és ambigua i no s'ha de resoldre escollint una coincidència arbitrària. Primer cal determinar si hi ha un total barrejat, un duplicat o dues unitats d'observació diferents.

#### Normalitzar sense perdre l'original

La normalització es farà de manera explícita i reproduïble. Es conservaran els codis rebuts, s'anotaran les regles aplicades i es compararan manualment diversos parells coneguts. Els noms municipals poden ajudar a diagnosticar, però no substituiran el codi oficial com a clau principal.

### Comprovació alfanumèrica

La taula d'atributs permet revisar quants territoris han rebut dades, quins han quedat sense correspondència i si els indicadors mantenen el tipus correcte.

La validació d'una unió exigeix registrar les entitats de la capa, les files de la taula, les claus úniques, els duplicats, les coincidències, els municipis sense dades i les files de la taula que no s'han utilitzat. Aquest registre aporta l'evidència que falta quan només s'afirma que la unió «ha funcionat». Una absència després de la unió ha de quedar com a nul, no convertir-se en zero.

### Comprovació espacial

La distribució sobre el mapa pot revelar errors que una taula no mostra fàcilment, però una imatge plausible no substitueix el recompte i la revisió dels registres.

La verificació espacial identificarà municipis coneguts i contrastarà els seus valors amb el llibre. També es revisaran mínims, màxims i ordres de magnitud. Un patró territorial versemblant pot haver-se construït amb un camp equivocat o una correspondència incompleta; la inspecció espacial complementa la prova alfanumèrica, però no la reemplaça.

### Unió del projecte i capa materialitzada

Una unió configurada dins del projecte QGIS manté la dependència amb el CSV extern. És útil mentre el llibre i `map_export` continuen canviant, perquè la còpia de transferència es pot regenerar. Tanmateix, si el CSV es mou o canvia l'esquema, la unió es pot trencar.

Només quan calgui compartir el resultat fora del projecte, es podrà exportar una capa derivada a GeoPackage amb els camps ja units. Aquesta materialització és opcional i no converteix la capa en la font mestra dels indicadors: qualsevol correcció s'ha de fer al llibre, regenerar a `map_export` i repetir de manera controlada.

## Activitat: unir els indicadors de la comarca

La pràctica relaciona la geometria municipal validada amb els indicadors del llibre mitjançant un codi territorial. La capa i la taula representen els mateixos municipis, però els codis poden tenir prefixos, longituds o tipus diferents; abans de normalitzar-los, cal comptar valors únics, detectar duplicats i confirmar una correspondència d'una fila d'indicadors per municipi.

El resultat serà un projecte QGIS amb una unió municipal comprovada, dues consultes reproduïbles i un informe de control al `README.md`. Els noms dels fitxers, les comprovacions i les evidències es concreten en les seccions següents perquè funcionen com a procediment de l'activitat, no com a objectius d'aprenentatge independents.

### Entrades i resultats de la unió municipal

Per al Tarragonès s'obrirà, dins de `qgis`, el projecte `tigit-04-dades-espacials.qgz` i es desarà la nova fita com `tigit-05-integracio-sig.qgz`, sense crear un projecte desconnectat. A `data/processed` es mantindrà `tarragones-boundaries-icgc-20260120.gpkg` i es conservarà la fita anterior del llibre abans de crear `tigit-05-integracio-sig.xlsx`. En aquest nou estat del mateix llibre es crearà o regenerarà `map_export` amb l'esquema canònic definit en el capítol. La còpia de transferència serà `municipal-indicators-tarragones-2021.csv`. Els noms s'adaptaran al territori i al període del projecte.

El projecte conservarà la unió entre la capa municipal i el CSV, mentre que el `README.md` recollirà l'informe de la unió. Com a evidència de pràctica es conservaran també tres comprovacions manuals de municipis i dues consultes de QGIS amb els recomptes i els codis resultants.

### Comprovar les entrades

Les entrades són el projecte QGIS del capítol 4, la capa comarcal validada i tres fulls del llibre: `municipal`, `indicators_demography` i `indicators_housing`. Després de crear o regenerar `map_export` i el CSV de transferència, abans de la unió s'anotaran el nombre d'entitats, el nombre de files, les claus úniques i els possibles duplicats. La clau territorial es triarà a partir de la documentació, no només perquè dos camps mostrin valors semblants. També es comprovarà que els codis i les unitats municipals dels indicadors de 2021 continuen corresponent a la geometria ICGC de 2026; si hi ha hagut cap canvi territorial, la unió quedarà aturada fins a documentar-ne el tractament.

### Preparar les claus i executar la unió

El procediment operatiu mínim serà aquest:

1. carregar la capa municipal del GeoPackage i importar el CSV com una **taula sense geometria**;
2. comprovar files, tipus de camp, codis, accents, decimals i valors nuls abans de configurar cap relació;
3. crear, només si cal, camps normalitzats nous amb el calculador de camps, sense sobreescriure les claus originals;
4. configurar a les propietats de la capa municipal una unió d'un a un entre la clau documentada de la geometria i `mun_code`;
5. limitar els camps incorporats als indicadors necessaris i comprovar quines geometries no han rebut correspondència;
6. desar `tigit-05-integracio-sig.qgz` només després de contrastar els recomptes i tres municipis amb el llibre.

Els noms i les unitats dels camps units han de continuar coincidint amb el diccionari del llibre. Si la clau no és única, els tipus no són compatibles o apareixen municipis sense correspondència, no s'ha de continuar cap a la simbolització fins a resoldre i documentar la incidència.

### Verificar coincidències i absències

Després de la unió es repetiran els recomptes. Tots els municipis previstos han de tenir una correspondència o una absència explicada. Per practicar la verificació, es contrastaran manualment tres municipis, inclosos un valor habitual i un cas extrem, i es comprovarà que el nombre de geometries no ha canviat.

També es practicaran i conservaran dues consultes de QGIS: una per identificar un municipi conegut i una altra per seleccionar una condició sobre un indicador. Per a cadascuna, el `README.md` registrarà l'expressió, el recompte obtingut i els codis municipals seleccionats.

::: table "Control de qualitat d'una unió territorial"
| Moment | Comprovació | Evidència |
| --- | --- | --- |
| Abans | La clau és única a la taula que aporta els atributs | Files, valors únics i duplicats |
| Abans | Els dos camps tenen format compatible o una regla de normalització documentada | Camps originals i normalitzats |
| Durant | El nombre de registres de la capa no canvia inesperadament | Recompte anterior i posterior |
| Després | Es compten coincidències, absències i files no utilitzades | Informe de la unió |
| Després | Els camps quantitatius continuen sent numèrics | Tipus i mostra de valors |
| Després | Els valors coincideixen amb el llibre | Municipis i indicadors contrastats |
| Després | La distribució espacial confirma casos concrets | Inspecció territorial documentada |
:::

### Consultar la unió

La unió es posarà a prova amb dues consultes senzilles. La primera identificarà els indicadors d'un municipi conegut. La segona localitzarà els municipis que compleixen una condició documentada, com superar un determinat percentatge d'habitatge no principal. Es podrà afegir una segona condició, però el resultat s'interpretarà com una **selecció descriptiva**, no com una **explicació causal**.

### Organització del projecte QGIS

#### Capes originals, derivades i estils

Els noms i grups de capes han de permetre distingir la font original, la capa comarcal, les transformacions de claus, la unió i els resultats preparats per simbolitzar. La simbologia temàtica encara no substituirà els noms semàntics ni la documentació de les capes.

#### Rutes, carpetes i traçabilitat

El projecte s'ha de poder obrir i revisar sense perdre fitxers. S'obrirà el `.qgz` iniciat al capítol 4 i es desarà la fita `tigit-05-integracio-sig.qgz`, amb rutes relatives dins de la carpeta arrel. El CSV de transferència, la font espacial i qualsevol GeoPackage derivat conservaran ubicacions estables; no es crearà un segon projecte desconnectat per al mapa de context o el mapa temàtic.

### Evidències de la integració SIG

Els fitxers principals d'aquesta fita són:

- llibre acumulatiu: `tigit-05-integracio-sig.xlsx`;
- CSV de transferència: `municipal-indicators-tarragones-2021.csv`;
- projecte QGIS: `tigit-05-integracio-sig.qgz`.

::: table "Evidències de la integració SIG"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/processed` | Llibre acumulatiu | Estat del llibre amb `municipal`, `indicators_demography`, `indicators_housing`, `palette` i `map_export` coherents |
| `data/processed` | CSV de transferència | UTF-8, una fila per municipi, codi i nom, indicador relatiu, totals, nul i estat separats |
| `qgis` | Projecte QGIS continuat | Capa municipal, taula importada, unió, grups i rutes relatives |
| `qgis` | Demostració auxiliar de centres docents de Vila-seca i, si s'amplia, del Tarragonès | Curs 2025/2026, camps X/Y, `EPSG:25831` i `EPSG:4326`, punts coincidents i codi municipal verificat; no forma part de l'evidència censal de 2021 |
| `qgis` | Allotjaments geocodificats, com a ampliació | Adreça d'entrada, resultat, coordenades, codi territorial i estat de revisió, sense camps personals innecessaris |
| `data/processed` o `qgis` | Capa materialitzada, només per compartir | Geometries i indicadors units en un GeoPackage derivat fàcil de transferir |
| `README.md` | Informe i evidència de pràctica | Claus, normalització, cardinalitat, recomptes, absències, tres casos contrastats i dues consultes amb recompte i codis |
:::

La fita `tigit-05-integracio-sig.qgz` deixa una única capa municipal amb la unió comprovada i les entrades auxiliars separades. El capítol següent continuarà aquest mateix projecte per convertir la base espacial i alfanumèrica en un mapa de context amb escala, retolació i composició revisades.
