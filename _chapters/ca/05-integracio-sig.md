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

Un sistema d'informació geogràfica relaciona geometries, atributs i operacions. En aquesta assignatura se'n farà una introducció aplicada després d'haver treballat semiologia, color, coordenades i llenguatge cartogràfic: QGIS serà sobretot l'espai on la taula municipal preparada al llibre únic es vincula amb els límits municipals de la comarca i es converteix en informació territorial consultable. Aquesta visió evita reduir el SIG a un programa: també hi intervenen les dades, els procediments, les preguntes i les persones que prenen decisions {% cite longleyGeographicInformationScience2015 nunesDiccionariSIG2012 %}.

Les demostracions breus de QGIS que hagin aparegut en capítols anteriors no substitueixen aquest bloc. Servien per veure una capa, una escala, una composició o una paleta en context. Aquí es formalitza el procediment: importar dades, revisar atributs, unir taules, diagnosticar errors i deixar el projecte preparat perquè la cartografia temàtica posterior no sigui només una captura acolorida.

La informació **georeferenciada** combina un component temàtic, que descriu què és o quin valor té una entitat, i un component espacial, que indica on es troba. Un SIG integra dades, eines, persones i mètodes per gestionar i analitzar aquesta relació i respondre problemes territorials.

![Esquema històric de fases d'un projecte SIG, utilitzat com a suport provisional per distingir dades, tractament, anàlisi i presentació]({{ site.baseurl }}/assets/img/legacy/gis-phases.png "Un projecte SIG no comença en el mapa final: necessita definir el problema, preparar dades, executar operacions, verificar resultats i comunicar-los. Imatge procedent de les diapositives antigues del curs; font i autoria pendents de verificació. Llicència: Referencia pendiente."){: data-figure-width="48rem"}

## Del programa al mètode de treball

Un SIG universitari no s'aprèn només localitzant menús. El programa és necessari, però el criteri principal és saber construir una cadena de treball revisable. Abans d'una unió, cal saber quina taula aporta els indicadors, quina capa aporta les geometries i quin camp permet relacionar-les. Després de la unió, cal comprovar si el nombre d'entitats, les claus i els valors continuen tenint sentit. Entre una captura vistosa i un resultat defensable hi ha una diferència metodològica: la segona opció permet reconstruir com s'ha arribat al mapa.

El projecte comarcal es pot entendre com quatre capes de responsabilitat. La primera és **documental**: conservar fonts, llicències, dates i definicions. La segona és **estructural**: mantenir una fila per municipi, camps amb tipus adequats i codis territorials coherents. La tercera és **espacial**: revisar CRS, geometria, extensió, escala i correspondència territorial. La quarta és **comunicativa**: decidir quines consultes, mapes i exportacions expliquen el resultat sense ocultar errors o absències. Si una d'aquestes capes falla, el mapa pot aparèixer igualment a la pantalla, però la interpretació quedarà debilitada.

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

En el laboratori es podrà utilitzar el connector **Open ICGC** de QGIS com a accés ràpid a la geoinformació de l'Institut Cartogràfic i Geològic de Catalunya. El connector incorpora una barra d'eines per carregar capes de referència, cercar topònims i adreces, consultar ortofotos, afegir fons cartogràfics i descarregar productes vectorials o ràster quan cal treballar sense connexió {% cite icgcOpenICGCQgisConnector2026 qgisOpenICGCPluginRepository2026 %}. Aquesta comoditat no substitueix la lectura de metadades: abans d'utilitzar una capa com a geometria d'anàlisi cal identificar productor, data, escala, CRS, llicència i si el recurs és una imatge de fons, un servei de visualització o una capa vectorial amb atributs.

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

El full `map_export` del llibre contindrà una taula plana amb una fila per municipi, el codi municipal i només els camps necessaris. S'exportarà com a CSV UTF-8 amb noms de camp breus i comprensibles. Aquesta exportació és una còpia de transferència: si canvia una fórmula, s'ha de regenerar des del mateix llibre, no corregir el CSV a mà.

La primera fila contindrà una única capçalera. No s'hi inclouran cel·les combinades, subtotals, notes de presentació, gràfics ni files comarcals barrejades amb els municipis. Els codis han de conservar la longitud i els zeros inicials; els valors absents es distingiran dels zeros; i els indicadors calculats s'exportaran amb el valor resultant. El CSV no substitueix les fórmules ni el diccionari conservats al llibre.

Un CSV no conserva per si sol el tipus de cada camp. En importar-lo a QGIS, el codi s'ha de declarar o interpretar explícitament com a text i verificar-se abans de la unió. El delimitador de camps i el separador decimal s'escolliran de manera que la importació sigui inequívoca. Després de l'exportació s'ha de tornar a importar o inspeccionar una mostra per confirmar que el nombre de columnes, els accents, els decimals i els identificadors es mantenen correctament.

### Importar i comprovar

La importació no acaba quan la taula apareix al projecte. Cal revisar caràcters, separadors, camps, files i interpretació dels valors. El nombre de registres ha de coincidir amb les files municipals de `map_export`, els codis s'han de conservar com a text quan l'esquema ho requereixi i els indicadors han de continuar sent numèrics.

Abans d'unir, almenys dos municipis i dos indicadors es contrastaran amb el full `indicators`. Aquesta comprovació separa els errors d'exportació dels errors que es puguin produir després durant la unió.

### Coordenades a punts

Algunes fonts no arriben com una capa de municipis, sinó com una taula amb coordenades. Pot passar amb equipaments turístics, punts d'informació, allotjaments, recursos patrimonials o adreces geocodificades. En aquest cas, QGIS pot carregar el CSV com a capa de text delimitat i crear geometries puntuals a partir dels camps X i Y. La decisió crítica és indicar el CRS correcte de les coordenades originals: longitud i latitud en graus solen correspondre a `EPSG:4326`, mentre que coordenades UTM del projecte haurien d'estar en metres i documentar-se com `EPSG:25831`.

![Espai de treball per documentar la importació d'un CSV, la unió amb límits municipals i la creació de punts a partir de coordenades]({{ site.baseurl }}/assets/img/placeholders/qgis-data-operations-placeholder.svg "QGIS: diàleg d'importació de text delimitat, configuració de la unió i conversió de camps X/Y en punts."){: data-figure-width="44rem"}

Crear punts no és el mateix que unir indicadors municipals. Una unió mitjançant codi territorial transfereix atributs a una geometria administrativa existent; una capa de punts crea entitats noves a partir de posicions. Si després cal resumir punts per municipi, caldrà una operació espacial específica i una comprovació diferent, perquè el resultat dependrà de la precisió de les coordenades i dels límits utilitzats.

## Unions mitjançant codis territorials

### Clau de la capa i clau de la taula

Una unió necessita camps compatibles i una correspondència clara entre registres. Els noms geogràfics només s'utilitzaran quan no hi hagi un identificador més robust.

Els dos camps originals s'han de conservar encara que no comparteixin longitud, prefix o tipus. Si cal adaptar-los, es crearan camps normalitzats nous amb noms explícits, com `mun_code_norm`. Retallar espais, completar zeros o eliminar un prefix només és legítim quan l'esquema territorial documenta la transformació.

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

Quan calgui conservar un resultat estable o compartir-lo fora del projecte, es podrà exportar una capa derivada a GeoPackage amb els camps ja units. Aquesta materialització facilita la portabilitat, però no converteix la capa en la font mestra dels indicadors: qualsevol correcció s'ha de fer al llibre, regenerar a `map_export` i repetir de manera controlada.

## Preguntes territorials que permet formular el SIG

Les aplicacions SIG es poden organitzar com a preguntes: què hi ha en aquest lloc, on es compleixen unes condicions, què ha canviat, quin patró es pot observar o quin recorregut respon a un criteri. En aquest curs es prioritzaran les dues primeres perquè es poden resoldre amb consultes, filtres i unions senzilles.

Localització directa
: Consulta que parteix d'una posició o una entitat i pregunta quins objectes o atributs hi ha associats.

Localització condicionada
: Cerca de les parts del territori que compleixen una o diverses condicions temàtiques o espacials.

Patró espacial
: Regularitat, concentració o associació observable en la distribució territorial d'un fenomen. Reconèixer un patró no demostra per si mateix una relació causal.

## Activitat: unir els indicadors de la comarca

La pràctica unirà `map_export` amb la capa municipal del capítol 4. La capa i la taula representen els mateixos municipis, però els codis poden tenir prefixos, longituds o tipus diferents. Abans de normalitzar-los, caldrà comptar valors únics, detectar duplicats i establir una correspondència d'una fila d'indicadors per municipi.

### Comprovar les entrades

El projecte QGIS del capítol 4, la capa comarcal validada, el llibre únic i el CSV regenerat constitueixen les entrades. Abans de la unió s'anotaran el nombre d'entitats, el nombre de files, les claus úniques i els possibles duplicats. La clau territorial es triarà a partir de la documentació, no només perquè dos camps mostrin valors semblants.

### Preparar les claus i executar la unió

Si els camps no són compatibles, els codis normalitzats es calcularan sense sobreescriure els originals. La unió utilitzarà els camps resultants i només incorporarà els indicadors necessaris per a les consultes i els mapes posteriors. Els noms i les unitats han de continuar coincidint amb el diccionari del llibre.

### Verificar coincidències i absències

Després de la unió es repetiran els recomptes. Tots els municipis previstos han de tenir una correspondència o una absència explicada. Es contrastaran manualment almenys tres municipis, inclosos un valor habitual i un cas extrem, i es comprovarà que el nombre de geometries no ha canviat.

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
| `data/processed` | Llibre únic actualitzat | Fulls `indicators` i `map_export` coherents |
| `data/processed` | CSV de transferència | UTF-8, una fila per municipi, codis preservats i camps necessaris |
| `qgis` | Projecte QGIS continuat | Capa municipal, taula importada, unió, grups i rutes relatives |
| `qgis` | Capa de punts, si s'utilitzen coordenades | Camps X/Y, CRS d'origen, punts creats i comprovació espacial |
| `data/processed` o `qgis` | Capa materialitzada, si cal | Geometries i indicadors units en un GeoPackage derivat |
| `README.md` | Informe de la unió | Claus, normalització, cardinalitat, recomptes, absències i casos contrastats |
:::
