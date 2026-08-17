---
layout: manual-chapter
title: Introducció als sistemes d'informació geogràfica
description: Conceptes bàsics de SIG, capes, taules d'atributs, importació, unions i control de qualitat amb QGIS.
lang: ca
ref: manual-gis-data-integration
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/integracio-sig/
weight: 80
part: Continguts
manual_references: true
---

Un sistema d'informació geogràfica relaciona geometries, atributs i operacions per respondre preguntes sobre el territori. En aquesta assignatura se'n farà una introducció aplicada que continua el treball iniciat amb coordenades, capes i llenguatge cartogràfic: QGIS serà sobretot l'espai on la taula municipal preparada al llibre únic es vincula amb els límits municipals de la comarca i es converteix en informació territorial consultable. Aquesta visió evita reduir el SIG a un programa o a una eina per fer mapes: també hi intervenen les dades, els procediments, la infraestructura, les preguntes i les persones que produeixen, analitzen i utilitzen la informació {% cite longleyGeographicInformationScience2015 nunesDiccionariSIG2012 %}.

Les operacions de QGIS dels capítols anteriors formen part del mateix flux acumulatiu, però no substitueixen aquest bloc d'integració. Aquí es formalitza el procediment: importar dades, revisar atributs, unir taules, diagnosticar errors i deixar el projecte preparat perquè la cartografia temàtica posterior no sigui només una captura acolorida.

>>>>> En acabar el capítol, cal poder integrar una taula d'indicadors amb geometries municipals a QGIS i conservar un resultat territorial consultable, validat i reproduïble.
>>>>>
>>>>> - Distingir un SIG del programari QGIS, del projecte `.qgz` i de les sortides cartogràfiques o tabulars.
>>>>> - Formular una pregunta espacial i vincular-la amb les dades, les operacions i els controls necessaris.
>>>>> - Organitzar un flux de treball des de les fonts i les entrades fins a una consulta o sortida revisable.
>>>>> - Importar un CSV UTF-8 preservant codis territorials, tipus numèrics, absències i nombre de registres.
>>>>> - Construir una unió municipal d'un a un amb claus documentades i normalitzades sense sobreescriure els camps originals.
>>>>> - Executar consultes alfanumèriques a QGIS i interpretar-ne els resultats com a seleccions descriptives.
>>>>> - Validar la unió amb recomptes, duplicats, coincidències, absències, contrastos manuals i comprovació espacial.

## De la cartografia automatitzada als SIG actuals

Els mapes, els censos i els inventaris territorials són molt anteriors als ordinadors. El canvi que va donar lloc als SIG no va consistir només a dibuixar mapes amb una màquina, sinó a representar la localització i els atributs de manera que es poguessin consultar, combinar i analitzar. Durant les dècades de 1950 i 1960, la geografia quantitativa, l'anàlisi espacial i els primers ordinadors van crear aquest entorn conceptual. El *Canada Geographic Information System*, desenvolupat per gestionar l'inventari de terres del Canadà durant els anys seixanta, se sol considerar una de les primeres implementacions de SIG a gran escala {% cite longleyGeographicInformationScience2015 %}.

Durant els anys setanta i vuitanta, les millores en bases de dades, emmagatzematge, teledetecció i algoritmes espacials van permetre separar millor les dades de les representacions cartogràfiques. Als anys noranta, els ordinadors personals i les interfícies gràfiques van estendre els SIG d'escriptori més enllà de grans administracions i centres de recerca. Des de l'inici del segle XXI, la navegació per satèl·lit d'ús civil, internet, els estàndards geoespacials, el programari lliure, els telèfons mòbils i els serveis al núvol han fet que consultar o produir informació geogràfica formi part de moltes activitats quotidianes. [QGIS](https://www.qgis.org/project/overview/) s'inscriu en aquesta etapa: integra edició, anàlisi, automatització, composició cartogràfica i publicació interoperable, no només visualització.

![Cronologia sintètica de l'evolució dels SIG, des de l'anàlisi espacial i els primers sistemes institucionals fins als SIG web, mòbils i connectats]({{ site.baseurl }}/assets/img/gis/gis-history-timeline.svg "La història dels SIG combina avenços conceptuals, dades, bases de dades, informàtica, observació de la Terra, posicionament per satèl·lit, xarxes i comunitats de programari. Cronologia sintètica: les etapes se superposen i no substitueixen completament les tecnologies anteriors. Esquema docent d'elaboració pròpia."){: data-figure-width="58rem"}

### GPS, GNSS i dades de posició

El **GNSS** és el conjunt de sistemes globals de navegació per satèl·lit. GPS és el sistema dels Estats Units; Galileo, GLONASS i BeiDou són altres constel·lacions globals. En el llenguatge quotidià es diu sovint «GPS» per referir-se al receptor o a qualsevol posicionament per satèl·lit, però la distinció ajuda a entendre que un telèfon pot combinar senyals de sistemes diferents.

El receptor estima la distància als satèl·lits a partir del temps de propagació dels senyals. Per obtenir una posició tridimensional i corregir el desajust del rellotge del receptor necessita, en condicions ordinàries, observacions d'almenys quatre satèl·lits. El resultat depèn de la geometria dels satèl·lits visibles, l'atmosfera, els obstacles, els reflexos del senyal, el receptor i el mètode de correcció. Una coordenada obtinguda al carrer, per tant, no és una veritat exacta: ha d'anar acompanyada del sistema de referència, el moment de l'observació i una estimació de qualitat adequada a l'ús {% cite vanSickleBasicGISCoordinates2017 %}.

GPS i SIG no són sinònims. Un receptor GNSS produeix posicions, tracks i marques temporals; un SIG les pot integrar amb carrers, municipis, allotjaments, relleu o indicadors per consultar-les i analitzar-les. Registrar la posició d'un recurs turístic és una operació de captura. Comprovar en quin municipi es troba, calcular-ne l'accessibilitat, detectar concentracions o combinar-lo amb dades de demanda són operacions SIG.

## Què és un SIG

La informació **georeferenciada** combina un component temàtic, que descriu què és o quin valor té una entitat, i un component espacial, que indica on es troba, quina forma té i quines relacions manté amb altres entitats. Un SIG és un sistema sociotècnic que permet capturar, emmagatzemar, gestionar, consultar, analitzar i comunicar aquesta informació per abordar preguntes de base territorial {% cite longleyGeographicInformationScience2015 nunesDiccionariSIG2012 %}.

Aquesta definició diferencia tres nivells. **QGIS** és una aplicació informàtica; el **projecte QGIS** registra capes, estils, unions, consultes i composicions; el **SIG** inclou, a més, les fonts, la infraestructura, les persones, els procediments i el context institucional que fan possible interpretar i mantenir el resultat. Instal·lar un programa no crea per si sol un SIG, de la mateixa manera que obrir un full de càlcul no garanteix una base de dades correcta.

>>>>> Aquesta fase delimita què constitueix un SIG i quin paper hi tenen les dades, les persones, els mètodes, la infraestructura i el programari.
>>>>>
>>>>> - Descompondre una informació georeferenciada en component temàtic i component espacial.
>>>>> - Distingir el sistema SIG, l'aplicació QGIS, el projecte QGIS i una sortida com un mapa, una taula o una capa derivada.
>>>>> - Relacionar persones, dades, mètodes, programari i infraestructura amb una pregunta territorial concreta.
>>>>> - Identificar quin component o procediment cal revisar quan un resultat territorial és incomplet o enganyós.

![Components d'un sistema d'informació geogràfica: persones, dades, mètodes, programari i infraestructura connectats per una pregunta territorial]({{ site.baseurl }}/assets/img/gis/gis-components.svg "Cap component funciona aïlladament: la pregunta orienta el sistema i el control de qualitat relaciona persones, dades, mètodes, programari i infraestructura. Esquema docent d'elaboració pròpia."){: data-figure-width="52rem"}

Les **persones** formulen la pregunta, decideixen els criteris i interpreten els resultats. Les **dades** aporten geometries, atributs, temps i metadades. Els **mètodes** defineixen com es capturen, transformen, relacionen i validen. El **programari** implementa les operacions, des de QGIS fins a una base de dades o un servei web. La **infraestructura** inclou ordinadors, receptors, servidors, xarxes i emmagatzematge. El control de qualitat travessa tots cinc components: un algoritme correcte aplicat a una dada inadequada, o una dada precisa interpretada amb un criteri erroni, pot produir un resultat enganyós.

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

En el projecte del curs es prioritzaran la consulta, la localització condicionada, les unions i la lectura de patrons. Les rutes, la modelització i l'estadística espacial mostren l'abast professional dels SIG, però no s'han d'aplicar sense dades i coneixements metodològics suficients.

## El mapa és una sortida, no tot el sistema

Un mapa és una de les sortides possibles d'un SIG, juntament amb una taula, una capa derivada, una mesura, un informe, una base de dades o un servei web. La cartografia fa visible una selecció del resultat, però no conserva necessàriament totes les dades, consultes i decisions que l'han produït. Per això el projecte editable, les capes i la documentació continuen sent necessaris encara que la peça final sigui un PDF.

QGIS ofereix eines de simbolització i composició suficients per produir mapes complets. Si la integració amb altres gràfics o textos exigeix un acabat més controlat, el mapa es pot exportar en PDF o SVG vectorial i obrir a Inkscape. És legítim ajustar la disposició a la pàgina, la jerarquia tipogràfica, els espais, els crèdits o elements decoratius, sempre que el mapa continuï representant el mateix resultat i mantingui llegibilitat, escala i atribució.

>>>> **El retoc gràfic no pot corregir ni reescriure l'anàlisi espacial.** No s'han de moure municipis, punts o límits per fer-los encaixar; estirar el mapa; redibuixar geometries; canviar classes o valors; eliminar absències; alterar proporcions de símbols; ni conservar una escala gràfica després d'haver deformat la peça. Si cal modificar l'extensió, la projecció, la classificació, la simbologia, les etiquetes vinculades a dades o qualsevol geometria, la correcció s'ha de fer al projecte QGIS i s'ha de tornar a exportar. Inkscape serveix per compondre i acabar, no per trencar la correspondència entre dada i espai.

## Del programa al mètode de treball

Un SIG universitari no s'aprèn només localitzant menús. El programa és necessari, però el criteri principal és saber construir una cadena de treball revisable. Abans d'una unió, cal saber quina taula aporta els indicadors, quina capa aporta les geometries i quin camp permet relacionar-les. Després de la unió, cal comprovar si el nombre d'entitats, les claus i els valors continuen tenint sentit. Entre una captura vistosa i un resultat defensable hi ha una diferència metodològica: la segona opció permet reconstruir com s'ha arribat al mapa.

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

![Espai de treball per documentar el connector Open ICGC dins de QGIS, amb accés a fons de mapa, ortofoto i límits administratius]({{ site.baseurl }}/assets/img/placeholders/qgis-open-icgc-placeholder.svg "QGIS i Open ICGC: selecció d'un fons de mapa i localització de límits administratius o divisions territorials."){: data-figure-width="44rem"}

Els fons de mapa de l'ICGC són molt útils per orientar el lector, comprovar si una capa cau on toca i construir un mapa de referència. En canvi, una unió d'indicadors municipals necessita una capa vectorial de límits amb camps identificadors. Si el connector ofereix diverses vies per arribar a un límit administratiu, s'ha de triar la que permeti conservar la geometria i els atributs necessaris, no només la que es veu millor al llenç.

### Fitxers i serveis de dades

Les capes descarregables permeten conservar una versió local, inspeccionar-ne l'esquema i processar-la sense dependre permanentment del servidor. Els serveis d'objectes poden proporcionar geometries i atributs consultables, mentre que els serveis de mapes o imatges estan orientats principalment a la visualització. Que QGIS pugui mostrar un recurs no significa que aquest es pugui editar, analitzar o distribuir de la mateixa manera.

La procedència i les metadades s'han de conservar en tots els casos. Un servei pot canviar mantenint la mateixa adreça, i una capa local pot quedar descontextualitzada si se'n perd la data, la llicència o el sistema de referència. La base municipal validada al capítol 4 continuarà sent la geometria de treball del projecte.

## Taules d'atributs

### Entitats, camps i tipus de dada

La taula d'atributs connecta cada **geometria**, la representació espacial d'una entitat, amb els seus **atributs**, els valors alfanumèrics que la descriuen. Els camps de text, enters i decimals tenen comportaments diferents en filtres, càlculs i unions.

### Seleccionar, ordenar i filtrar

Abans de representar una variable cal saber inspeccionar els registres i localitzar casos concrets o valors absents.

La selecció respon una condició temporal dins del projecte; no modifica necessàriament les dades. Un filtre limita quines entitats es mostren o es processen, i una exportació crea un resultat nou. Cal distingir aquestes operacions per no confondre una vista parcial amb una capa que només conté la comarca.

## Transferir la taula a QGIS

### Preparar la taula externa

Durant aquest capítol es crearà o regenerarà el full `map_export` a partir dels fulls coherents `municipal` i `indicators`. Contindrà una taula plana amb una fila per municipi i només els camps necessaris per al flux guiat: codi i nom municipals, l'indicador relatiu seleccionat, la població total i/o el total d'habitatges que després permetran demostrar els símbols proporcionals. S'exportarà com a CSV UTF-8 amb noms de camp breus i comprensibles. Aquesta exportació és una còpia de transferència: si canvia una fórmula, s'ha de regenerar des del mateix llibre, no corregir el CSV a mà.

La primera fila contindrà una única capçalera. No s'hi inclouran cel·les combinades, subtotals, notes de presentació, gràfics ni files comarcals barrejades amb els municipis. Els codis han de conservar la longitud i els zeros inicials; els valors absents es distingiran dels zeros; i els indicadors calculats s'exportaran amb el valor resultant. El CSV no substitueix les fórmules ni el diccionari conservats al llibre.

Un CSV no conserva per si sol el tipus de cada camp. En importar-lo a QGIS, el codi s'ha de declarar o interpretar explícitament com a text i verificar-se abans de la unió. El delimitador de camps i el separador decimal s'escolliran de manera que la importació sigui inequívoca. Després de l'exportació s'ha de tornar a importar o inspeccionar una mostra per confirmar que el nombre de columnes, els accents, els decimals i els identificadors es mantenen correctament.

### Importar i comprovar

La importació no acaba quan la taula apareix al projecte. Cal revisar caràcters, separadors, camps, files i interpretació dels valors. El nombre de registres ha de coincidir amb les files municipals de `map_export`, els codis s'han de conservar com a text quan l'esquema ho requereixi i els indicadors han de continuar sent numèrics.

Abans d'unir, almenys dos municipis i dos indicadors es contrastaran amb el full `indicators`. Aquesta comprovació separa els errors d'exportació dels errors que es puguin produir després durant la unió.

### Coordenades a punts

Algunes fonts no arriben com una capa de municipis, sinó com una taula amb coordenades. Pot passar amb equipaments turístics, punts d'informació, allotjaments, recursos patrimonials o adreces geocodificades. En aquest cas, QGIS pot carregar el CSV com a capa de text delimitat i crear geometries puntuals a partir dels camps X i Y. La decisió crítica és indicar el CRS correcte de les coordenades originals: longitud i latitud en graus solen correspondre a `EPSG:4326`, mentre que coordenades UTM del projecte haurien d'estar en metres i documentar-se com `EPSG:25831`.

La capa de punts és opcional i només es crearà si l'activitat utilitza efectivament una taula amb coordenades. No forma part del resultat obligatori de la unió municipal.

No totes les coordenades UTM d'una taula s'han de convertir automàticament en punts. Si la font identifica una quadrícula, com les [quadrícules UTM de l'ICGC](https://www.icgc.cat/es/Geoinformacion-y-mapas/Datos-y-productos/Geoinformacion-cartografica/Cuadriculas-UTM) amb [codis MGRS del tipus `31TCG213911`](https://www.icgc.cat/es/Ayuda/Preguntas-frecuentes/Coordenadas-de-tipo-31TCG213911), la dada representa una cel·la. El parell E/N associat permet situar la cantonada de referència del quadrat i dona nom al polígon, però no descriu per si sol el centre ni un objecte puntual. En aquests casos convé carregar o construir la capa poligonal de quadrícula i, només si l'objectiu cartogràfic ho justifica, derivar-ne un punt auxiliar documentat {% cite icgcQuadriculesUtmEspecificacions2026 %}.

![Espai de treball per documentar la importació d'un CSV, la unió amb límits municipals i la creació de punts a partir de coordenades]({{ site.baseurl }}/assets/img/placeholders/qgis-data-operations-placeholder.svg "QGIS: diàleg d'importació de text delimitat, configuració de la unió i conversió de camps X/Y en punts."){: data-figure-width="44rem"}

Crear punts no és el mateix que unir indicadors municipals. Una unió mitjançant codi territorial transfereix atributs a una geometria administrativa existent; una capa de punts crea entitats noves a partir de posicions. Si després cal resumir punts per municipi, caldrà una operació espacial específica i una comprovació diferent, perquè el resultat dependrà de la precisió de les coordenades i dels límits utilitzats.

## Unions mitjançant codis territorials

### Clau de la capa i clau de la taula

Una unió necessita camps compatibles i una correspondència clara entre registres. Els noms geogràfics només s'utilitzaran quan no hi hagi un identificador més robust.

Els dos camps originals s'han de conservar encara que no comparteixin longitud, prefix o tipus. Si cal adaptar-los, es crearan camps normalitzats nous amb noms explícits, com `mun_code_norm`. Retallar espais, completar zeros o eliminar un prefix només és legítim quan l'esquema territorial documenta la transformació.

>>>>> Aquesta fase relaciona geometries i indicadors mitjançant claus territorials compatibles i controls alfanumèrics i espacials.
>>>>>
>>>>> - Comparar les claus de la capa i de la taula segons el tipus, la longitud, els prefixos, els zeros inicials i la unicitat.
>>>>> - Crear camps normalitzats reproduïbles sense alterar els codis territorials originals.
>>>>> - Confirmar una cardinalitat d'un a un abans d'executar la unió municipal.
>>>>> - Comptar coincidències, absències, duplicats i files no utilitzades sense convertir els nuls en zeros.
>>>>> - Contrastar municipis i valors amb el llibre i amb la seva distribució espacial abans de materialitzar o simbolitzar el resultat.

#### Cardinalitat esperada

El projecte necessita una fila d'indicadors per cada municipi de la capa comarcal. Aquesta correspondència d'un a un exigeix claus úniques als dos costats. Si `map_export` conté més d'una fila amb el mateix codi, la unió és ambigua i no s'ha de resoldre escollint una coincidència arbitrària. Primer cal determinar si hi ha un total barrejat, un duplicat o dues unitats d'observació diferents.

#### Normalitzar sense perdre l'original

La normalització es farà de manera explícita i reproduïble. Es conservaran els codis rebuts, s'anotaran les regles aplicades i es compararan manualment diversos parells coneguts. Els noms municipals poden ajudar a diagnosticar, però no substituiran el codi oficial com a clau principal.

### Comprovació alfanumèrica

La taula d'atributs permet revisar quants territoris han rebut dades, quins han quedat sense correspondència i si els indicadors mantenen el tipus correcte.

No n'hi ha prou amb afirmar que la unió «ha funcionat». Cal registrar les entitats de la capa, les files de la taula, les claus úniques, els duplicats, les coincidències, els municipis sense dades i les files de la taula que no s'han utilitzat. Una absència després de la unió ha de quedar com a nul, no convertir-se en zero.

### Comprovació espacial

La distribució sobre el mapa pot revelar errors que una taula no mostra fàcilment, però una imatge plausible no substitueix el recompte i la revisió dels registres.

La verificació espacial identificarà municipis coneguts i contrastarà els seus valors amb el llibre. També es revisaran mínims, màxims i ordres de magnitud. Un patró territorial versemblant pot haver-se construït amb un camp equivocat o una correspondència incompleta; la inspecció espacial complementa la prova alfanumèrica, però no la reemplaça.

### Unió del projecte i capa materialitzada

Una unió configurada dins del projecte QGIS manté la dependència amb el CSV extern. És útil mentre el llibre i `map_export` continuen canviant, perquè la còpia de transferència es pot regenerar. Tanmateix, si el CSV es mou o canvia l'esquema, la unió es pot trencar.

Només quan calgui compartir el resultat de manera portable fora del projecte, es podrà exportar una capa derivada a GeoPackage amb els camps ja units. Aquesta materialització és opcional i no converteix la capa en la font mestra dels indicadors: qualsevol correcció s'ha de fer al llibre, regenerar a `map_export` i repetir de manera controlada.

## Activitat: unir els indicadors de la comarca

La pràctica relaciona la geometria municipal validada amb els indicadors del llibre mitjançant un codi territorial. La capa i la taula representen els mateixos municipis, però els codis poden tenir prefixos, longituds o tipus diferents; abans de normalitzar-los, cal comptar valors únics, detectar duplicats i confirmar una correspondència d'una fila d'indicadors per municipi.

>>>>> L'activitat deixa el projecte QGIS preparat amb una unió municipal comprovada, dues consultes reproduïbles i un informe de control al `README.md`.
>>>>>
>>>>> - Regenerar `map_export` i `data/processed/municipal_indicators_tarragones_2021.csv` des del llibre sense corregir manualment la còpia de transferència.
>>>>> - Comprovar abans de la unió les entitats, les files, les claus úniques, els duplicats, els tipus de camp i una mostra de valors.
>>>>> - Normalitzar les claus en camps nous i unir només els indicadors necessaris a la capa municipal validada.
>>>>> - Verificar que el nombre de geometries no canvia i registrar coincidències, absències i files no utilitzades.
>>>>> - Contrastar manualment tres municipis, inclosos un valor habitual i un cas extrem, amb els fulls `municipal` i `indicators`.
>>>>> - Conservar dues consultes de QGIS amb l'expressió, el recompte i els codis municipals seleccionats.
>>>>> - Mantenir `qgis/tigit_tarragones.qgz`, el CSV, la capa espacial i qualsevol GeoPackage derivat amb rutes relatives i funcions diferenciades.

### Materials i resultats de treball

Per al Tarragonès es continuarà `qgis/tigit_tarragones.qgz` amb `data/processed/municipis_tarragones_epsg25831.gpkg` quan s'hagi materialitzat al capítol 4 i amb el llibre únic, del qual es crearà o regenerarà `map_export` des dels fulls coherents `municipal` i `indicators`. La còpia de transferència serà `data/processed/municipal_indicators_tarragones_2021.csv` i inclourà codi i nom municipals, l'indicador relatiu seleccionat, població total i/o total d'habitatges. Els noms de comarca i any s'adaptaran al territori i al període del projecte.

El projecte conservarà la unió entre la capa municipal i el CSV, mentre que el `README.md` recollirà l'informe de la unió. Com a evidència de pràctica es conservaran també tres comprovacions manuals de municipis i dues consultes de QGIS amb els recomptes i els codis resultants.

### Comprovar les entrades

El projecte QGIS del capítol 4, la capa comarcal validada i els fulls `municipal` i `indicators` constitueixen les entrades. Després de crear o regenerar `map_export` i el CSV de transferència, abans de la unió s'anotaran el nombre d'entitats, el nombre de files, les claus úniques i els possibles duplicats. La clau territorial es triarà a partir de la documentació, no només perquè dos camps mostrin valors semblants.

### Preparar les claus i executar la unió

Si els camps no són compatibles, els codis normalitzats es calcularan sense sobreescriure els originals. La unió utilitzarà els camps resultants i només incorporarà els indicadors necessaris per a les consultes i els mapes posteriors. Els noms i les unitats han de continuar coincidint amb el diccionari del llibre.

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

La unió es posarà a prova amb dues consultes senzilles. La primera identificarà els indicadors d'un municipi conegut. La segona localitzarà els municipis que compleixen una condició documentada, com superar un determinat percentatge d'habitatge no principal. Es podrà afegir una segona condició, però el resultat s'interpretarà com una selecció descriptiva, no com una explicació causal.

### Organització del projecte QGIS

#### Capes originals, derivades i estils

Els noms i grups de capes han de permetre distingir la font original, la capa comarcal, les transformacions de claus, la unió i els resultats preparats per simbolitzar. La simbologia temàtica encara no substituirà els noms semàntics ni la documentació de les capes.

#### Rutes, carpetes i traçabilitat

El projecte s'ha de poder obrir i revisar sense perdre fitxers. S'utilitzarà el mateix `.qgz` iniciat al capítol 4, amb rutes relatives dins de la carpeta arrel. El CSV de transferència, la font espacial i qualsevol GeoPackage derivat conservaran ubicacions estables; no es crearà un segon projecte desconnectat per al mapa temàtic.

#### Evidències que s'han de conservar

::: table "Evidències de la integració SIG"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/processed` | Llibre únic actualitzat | Fulls `municipal`, `indicators` i `map_export` coherents |
| `data/processed` | `municipal_indicators_tarragones_2021.csv` | UTF-8, una fila per municipi, codi i nom, indicador relatiu i totals necessaris per als símbols proporcionals |
| `qgis` | Projecte QGIS continuat | Capa municipal, taula importada, unió, grups i rutes relatives |
| `qgis` | Capa de punts, si s'utilitzen coordenades | Camps X/Y, CRS d'origen, punts creats i comprovació espacial |
| `data/processed` o `qgis` | Capa materialitzada, només per compartir | Geometries i indicadors units en un GeoPackage derivat portable |
| `README.md` | Informe i evidència de pràctica | Claus, normalització, cardinalitat, recomptes, absències, tres casos contrastats i dues consultes amb recompte i codis |
:::
