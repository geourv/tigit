---
layout: manual-chapter
title: Llenguatge cartogràfic
description: Fotografia aèria, ortofotos, escala, orientació, llegenda, retolació, generalització, jerarquia i composició del mapa.
lang: ca
ref: manual-cartographic-language
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/llenguatge-cartografic/
weight: 70
part: Continguts
manual_references: true
---

Un mapa no és una taula acolorida ni un gràfic col·locat sobre un territori. La posició de les entitats ve determinada per la geografia, i l'escala, la selecció i la generalització condicionen què pot mostrar-se. Aquest capítol introdueix la gramàtica pròpia del mapa abans d'entrar en el color i la cartografia temàtica. Les decisions cartogràfiques no són neutres: seleccionar, ometre, projectar, classificar i jerarquitzar condiciona el missatge que rep el lector {% cite jolyCartografia1982 monmonierHowLieMaps2018 %}.

## Què fa que una representació sigui un mapa

### Posició geogràfica i relacions espacials

La proximitat, la continuïtat, la forma i el veïnatge tenen significat territorial. No es poden reorganitzar lliurement com les categories d'un gràfic.

En un gràfic de barres, els municipis es poden ordenar de més a menys per facilitar una comparació. En un mapa, cada municipi ha de mantenir la posició, la forma i el contacte amb els veïns. Aquesta restricció redueix la precisió d'algunes comparacions quantitatives, però permet observar continuïtats, agrupacions i contrastos territorials que la taula no mostra.

### Planimetria i altimetria

La **planimetria** representa elements en posició horitzontal, com límits, nuclis, carreteres, costa o hidrografia. L'**altimetria** descriu el relleu mitjançant cotes, corbes de nivell, ombrejat o tintes hipsomètriques. Totes dues poden proporcionar context, però el seu nivell de detall ha de respondre al propòsit del mapa.

En el mapa comarcal, els límits i alguns topònims ajuden a localitzar els municipis. Un relleu detallat o una xarxa viària completa podrien competir amb aquesta funció. Només s'incorporaran si aporten una referència necessària per interpretar la localització; altrament, s'ometran com a part de la generalització.

El relleu és especialment delicat perquè pot donar molta estructura visual sense formar part de la variable principal. Les cotes aporten valors puntuals; les corbes de nivell mostren forma i pendent; l'ombrejat fa intuïtiu el volum, però pot semblar una font de llum real; i les tintes hipsomètriques ordenen rangs d'altura, però introdueixen una paleta que pot competir amb una coropleta. En un mapa temàtic municipal, l'altimetria només s'ha d'afegir si ajuda a explicar un patró territorial, com una diferència entre litoral i interior, i no només perquè el mapa sembli més complet.

![Quatre recursos per representar altimetria: cotes, corbes de nivell, ombrejat i tintes hipsomètriques]({{ site.baseurl }}/assets/img/cartographic-language/relief-representation-methods.svg "El relleu pot orientar la lectura o competir amb la variable principal; cotes, corbes, ombrejat i tintes hipsomètriques no comuniquen exactament la mateixa informació. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="54rem"}

## De la fotografia aèria al mapa

Una imatge presa des de l'aire pot mostrar el territori amb molt detall sense tenir encara la geometria d'un mapa. La direcció de la càmera, la perspectiva, el relleu, la inclinació de la plataforma i el processament posterior condicionen què es pot identificar i què es pot mesurar. Aquesta distinció és necessària quan s'utilitzen fotografies històriques per estudiar l'evolució urbana i litoral, o una ortofoto actual com a fons per localitzar allotjaments, accessos i equipaments.

### Preses obliqües i verticals

Una **fotografia aèria obliqua** es pren amb l'eix òptic de la càmera inclinat respecte de la vertical. Ofereix una perspectiva semblant a la visió humana i fa visibles façanes, vessants i volums, però l'escala varia fortament entre el primer terme i el fons. En la classificació internacional utilitzada aquí, l'**obliqua baixa** no inclou l'horitzó i l'**obliqua alta** sí que l'inclou. La primera pot facilitar la identificació de formes i la segona proporciona una visió territorial més extensa, però cap de les dues no admet mesures planimètriques directes com un mapa {% cite baumannAerialPhotography2019 usgsAerialPhotoSingleFrames2018 %}.

Una **fotografia aèria vertical** es pren amb la càmera orientada tan a prop del nadir com permet la plataforma. Aquesta orientació facilita la fotogrametria i la cobertura sistemàtica, però la imatge continua sent una projecció central. Els elements elevats es desplacen radialment respecte del centre i poden mostrar part dels seus costats; la inclinació de la càmera i les diferències de relleu també alteren la posició i l'escala. Per tant, «vista des de dalt», «vertical», «georeferenciada» i «ortorectificada» no són sinònims.

El tema [*Aerial Photography: History and Georeferencing*](https://doi.org/10.22224/gistbok/2019.2.5) del GIS&T Body of Knowledge desenvolupa aquesta seqüència mitjançant definicions, història, ortorectificació, fotografia digital, resultats d'aprenentatge i temes relacionats. El DOI és l'enllaç estable; la plataforma actual també permet cercar altres temes, consultar-ne les connexions en un mapa de coneixement i obtenir una versió d'impressió.

![Capçalera, citació i definicions inicials del tema sobre fotografia aèria al GIS&T Body of Knowledge]({{ site.baseurl }}/assets/img/aerial-photography/gistbok-aerial-photography-2026-08-12.png "Consulta del tema DC-02-010, amb etiquetes, citació, DOI i definicions de fotogrametria, ortorectificació i georeferenciació. Captura pròpia de la interfície del GIS&T Body of Knowledge, UCGIS, 12 d'agost de 2026; fragment reproduït per a comentari docent. El contingut pertany a UCGIS i als autors del tema."){: data-figure-width="48rem"}

### Del fotograma a l'ortofoto

Un **fotograma** és una captura individual d'un vol fotogramètric abans de l'ortorectificació. Les passades es planifiquen amb solapament longitudinal i transversal perquè una part del territori aparegui en diverses imatges. Aquest recobriment evita buits, permet la visió estereoscòpica i contribueix a estimar el relleu i a construir mosaics.

La **georeferenciació** relaciona la imatge amb un sistema de coordenades mitjançant la posició de la càmera, punts de control o altres paràmetres. Permet situar-la aproximadament sobre altres capes, però no elimina per si sola els desplaçaments interns de la perspectiva. L'**ortorectificació** corregeix geomètricament la inclinació, la perspectiva i l'efecte del relleu mitjançant l'orientació de la càmera, punts de control i un model d'elevacions. El resultat és una imatge en projecció ortogonal amb una escala espacial controlada, apta per comparar posicions i efectuar mesures dins de la precisió declarada {% cite ignPnoaOrthophotoGeneration2026 %}.

::: table "Fotografies aèries i productes derivats"
| Tipus o producte | Com s'obté | Tret de lectura | Ús i límit principal |
| --- | --- | --- | --- |
| Obliqua baixa | Càmera inclinada, sense horitzó visible | Perspectiva i laterals dels objectes | Identificar formes i volums; l'escala no és uniforme |
| Obliqua alta | Càmera inclinada, amb horitzó visible | Gran extensió des del primer terme fins al fons | Il·lustrar el paisatge i el context; no permet mesura planimètrica directa |
| Fotograma vertical | Càmera orientada aproximadament al nadir | Captura individual amb perspectiva central | Fotointerpretació i fotogrametria; conserva desplaçaments per relleu i inclinació |
| Fotograma georeferenciat | Fotograma associat a coordenades o punts de control | Se superposa aproximadament a altres capes | Localitzar i comparar; georeferenciar no equival a ortorectificar |
| Ortoimatge | Qualsevol imatge corregida a projecció ortogonal | Posició planimètrica i escala espacial controlades | Mesurar dins de la resolució i precisió documentades; pot procedir d'un avió, un satèl·lit o un altre sensor |
| Ortofoto o ortofotografia | Fotografia aèria ortorectificada | Detall fotogràfic amb geometria cartogràfica | Mesurar, digitalitzar i usar com a fons; continua necessitant data, resolució, CRS i precisió |
| Ortofotomosaic | Unió ajustada de diverses ortofotos | Cobertura contínua més gran que un fotograma | Consultar un territori extens; les peces poden correspondre a dates diferents |
| Ortofotomapa | Ortofoto o ortofotomosaic amb topònims, xarxes, límits o símbols cartogràfics | La imatge aporta el fons i les capes afegides en faciliten l'orientació | Comunicar i navegar; cal distingir la data de la imatge de la de les capes superposades |
:::

>>>> **Una fotografia vertical no es converteix en ortofoto només perquè encaixi aproximadament sobre un mapa.** La georeferenciació pot situar alguns punts correctament mentre altres continuen desplaçats. Per interpretar una mesura cal conèixer el processament, el CRS, la resolució, la precisió i la data de captació.

### Consultar una fototeca històrica

La [Fototeca Digital del CNIG](https://fototeca.cnig.es/) permet cercar una localització, seleccionar vols històrics i PNOA en una cronologia, mostrar els fotocentres, obrir fotogrames, regular-ne l'opacitat, comparar-los amb ortofotos i consultar o descarregar els productes disponibles. El CNIG conserva i distribueix el material, però cada vol pot tenir un productor i unes condicions d'atribució propis.

La captura mostra una consulta sobre Vila-seca, Salou i Tarragona. S'ha seleccionat el vol Americà B de 1956–1957 i el fotograma `PNOA-H_AMS_1956-57_33k_ES_comp_PAN_21mic_etrs89_UTM-hu31_H50_0472_fot_16089`, que apareix sobre l'ortofoto disponible com a fons el dia de la consulta. Els punts blaus representen fotocentres. La costa, els camins i les edificacions visibles al fotograma històric es poden contrastar amb el fons, però els contorns no coincideixen necessàriament: el servei adverteix que els fotogrames històrics poden tenir una orientació aproximada i que, encara que estiguin georeferenciats, no són ortofotos {% cite cnigFototecaDigital2026 %}.

::: subfigures a+b "Comparació de la mateixa extensió a la Fototeca Digital del CNIG. El fotograma històric es pot situar sobre l'ortofoto de fons, però conserva la geometria d'una fotografia en perspectiva. Captures pròpies, 12 d'agost de 2026. Vol Americà B, Ministeri de Defensa, CEGET, distribuït per IGN/CNIG; dades geogràfiques sota CC BY 4.0."
![Fotograma històric superposat a l'ortofoto de fons]({{ site.baseurl }}/assets/img/aerial-photography/fototeca-cnig-vila-seca-fotograma-1956-1957.png "Fotograma de 1956–1957 visible sobre el fons")
![Mateix enquadrament de Vila-seca, Salou i Tarragona amb el fotograma històric ocult]({{ site.baseurl }}/assets/img/aerial-photography/fototeca-cnig-vila-seca-ortofoto-2026-08-12.png "Mateix enquadrament amb l'ortofoto de fons")
:::

La consulta es pot reproduir cercant `Vila-seca`, activant **Fotogrames**, seleccionant **1956–1957 Americà B** i obrint un dels fotocentres pròxims. Abans d'utilitzar-ne el resultat s'han d'anotar el vol, l'identificador complet del fotograma, la data o interval, el productor, la resolució o escala, el sistema de referència, la llicència i la data de consulta. Una captura del visor documenta l'operació, però per analitzar o mesurar cal treballar amb el fitxer i les metadades corresponents.

### Google Maps i la vista d'imatges

Google Maps distingeix oficialment entre **Mapa**, que mostra vies, llocs i punts de referència, i **Satèl·lit**, que mostra imatges aèries. Aquesta etiqueta comercial no identifica el sensor ni garanteix per si sola que cada peça visible sigui una ortofoto amb resolució, data i precisió conegudes. Amb les etiquetes desactivades, la vista és una base d'imatges georeferenciada; si s'hi superposen vies, topònims, límits i punts d'interès, el resultat funciona visualment com un **ortofotomapa**. En canvi, una vista inclinada o un entorn 3D torna a introduir perspectiva i no s'ha de descriure com un ortofotomapa planimètric.

Per tant, el nom depèn del producte que es veu i de les capes actives, però també de la informació tècnica disponible. En una exploració quotidiana es pot parlar de vista d'imatges o vista híbrida. En un treball acadèmic, una mesura o una font de dades, cal preferir una ortofoto oficial amb data, CRS, resolució, precisió i condicions de reutilització documentades; la consulta pública de Google Maps no autoritza a redistribuir-ne les imatges {% cite googleMapsLayers2026 %}.

### Street View i el paisatge vist des del carrer

Google Street View no és fotografia aèria: registra panorames des del nivell del carrer i, per tant, mostra façanes, voreres, arbrat, mobiliari, rètols, accessos i relacions entre l'espai públic i els edificis. Aquesta perspectiva complementa l'ortofoto. La vista zenital ajuda a reconèixer l'extensió i la forma del teixit urbà; la vista de carrer permet observar com aquest teixit es materialitza i com es percep a escala humana.

En alguns punts, l'opció **Mostra més dates** permet recuperar panorames d'anys diferents. La comparació pot revelar una nova urbanització, la reforma d'un carrer, el creixement dels arbres, canvis d'usos o transformacions d'un paisatge turístic. No obstant això, l'historial no està disponible a tot arreu, els intervals són irregulars i una diferència d'estació, hora, trànsit o posició de la càmera pot semblar un canvi territorial sense ser-ho {% cite googleStreetViewHistorical2026 %}.

Una exploració guiada pot partir d'aquest [panorama de l'entorn sud-est del nucli de Vila-seca](https://www.google.com/maps/@41.1074631,1.1453166,3a,75y,30.7h,90t/data=!3m6!1e1!3m4!1scbGZ8h5wToZfvBH_5i8XtA!2e0!7i16384!8i8192?hl=ca). Si la interfície ofereix **Mostra més dates**, se seleccionaran dos anys prou separats i es mantindran la mateixa posició, orientació i ampliació. El registre indicarà les dues dates i distingirà els canvis permanents, com l'edificació o la secció del carrer, dels elements conjunturals, com vehicles, obres provisionals, ombres o vegetació estacional.

Les directrius de Google permeten consultar i incrustar Street View mitjançant les eines proporcionades, però prohibeixen publicar-ne captures fixes, utilitzar-les en llibres o manuals i extreure'n dades per digitalització o anàlisi automatitzada. Per això el manual enllaça el panorama viu i no reprodueix una parella de captures. Les observacions serviran per formular hipòtesis qualitatives, que s'hauran de contrastar amb ortofotos oficials, cartografia, planejament o treball de camp abans d'afirmar un canvi {% cite googleGeoGuidelines2026 %}.

### Mapes de referència, temàtics i turístics

Cada tipus de mapa selecciona informació diferent. Un mapa turístic pot orientar, localitzar recursos o comunicar una anàlisi, i aquestes funcions no exigeixen la mateixa composició.

::: table "Funció del mapa i informació prioritària"
| Tipus | Pregunta principal | Informació prioritària | Risc habitual |
| --- | --- | --- | --- |
| Referència | On és cada element? | Xarxa, poblament, relleu, límits i topònims | Acumular més detall del que permet l'escala |
| Temàtic | Com es distribueix una variable? | Patró de l'indicador, unitats territorials i llegenda | Fer que el context competeixi amb la variable |
| Localització | On se situa el territori d'estudi? | Extensió, entorn i jerarquia territorial | Convertir el requadre en un segon mapa complex |
| Turístic d'orientació | Com s'arriba als recursos i serveis? | Itineraris, accessos, punts d'interès i referències útils | Confondre promoció, orientació i anàlisi |
:::

## Escala i generalització

### Escala numèrica i gràfica

L'**escala cartogràfica** relaciona una distància representada al mapa amb la distància corresponent al territori i limita el detall que es pot llegir. A escala `1:100 000`, una unitat al mapa representa cent mil unitats al territori: un centímetre equival a un quilòmetre. Aquesta relació només és interpretable quan es coneixen la mida i el suport finals.

La distinció entre **escala gran** i **escala petita** pot resultar contraintuïtiva perquè es refereix al valor de la fracció, no a la mida del territori representat. `1:5 000` és una escala més gran que `1:100 000` perquè una unitat del mapa representa menys unitats del terreny i, per tant, pot mostrar més detall. Un plànol urbà és habitualment de gran escala; un mapa provincial o estatal és de petita escala. Dir que un mapa és “gran” perquè cobreix molta superfície és ambigu i s'ha d'evitar en la justificació cartogràfica.

La mida final d'exportació forma part de la decisió. Ampliar el zoom de QGIS no augmenta l'espai disponible a la pàgina, i reduir posteriorment un mapa pot fer il·legibles etiquetes, traços i símbols. L'escala s'ha de comprovar dins de la composició, a la mida de publicació.

L'escala gràfica manté la relació visual quan el document es redimensiona proporcionalment; l'escala numèrica deixa de ser certa si la pàgina s'amplia o es redueix. En tots dos casos, el marc de mapa i el CRS del projecte han de permetre interpretar les distàncies correctament.

Una escala verbal, com “mapa de detall municipal” o “mapa de context provincial”, pot ajudar el lector general, però no substitueix l'escala numèrica o gràfica quan s'han de comprovar distàncies. En el treball del curs, l'escala s'ha de registrar juntament amb la mida final de la peça, perquè la mateixa composició exportada a una pàgina A4 o a una diapositiva no ofereix la mateixa lectura.

### Seleccionar, simplificar i jerarquitzar

La **generalització cartogràfica** adapta la informació a l'escala i al propòsit del mapa mitjançant selecció, simplificació, combinació, desplaçament o exageració. Generalitzar no és eliminar informació arbitràriament, sinó conservar-ne el sentit essencial a la mida prevista.

#### Comparar diverses escales

Una mateixa geometria municipal es pot observar en una composició provincial, comarcal o local. A l'escala provincial interessa la forma general i la situació de la comarca; a l'escala comarcal es poden distingir els municipis; a una escala local pot ser necessari incorporar carreteres, nuclis o altres elements. Mostrar el mateix detall en els tres casos produeix soroll o una falsa sensació de precisió.

#### Decidir què es conserva

La generalització pot seleccionar els elements necessaris, simplificar formes massa detallades, combinar categories, desplaçar símbols que se superposen o exagerar elements que desapareixerien. Cada operació ha de conservar la funció territorial del mapa. En el mapa de context del projecte, els municipis i la comarca són essencials; una xarxa viària exhaustiva o una ortofoto detallada no ho són.

#### Comprovar el suport final

La decisió s'ha de revisar al 100% de la mida d'exportació. Si un detall només es percep ampliant molt la pantalla, no forma part efectiva del mapa publicat. Abans de reduir totes les etiquetes o tots els traços, convé retirar informació secundària.

#### Àrea mínima cartografiable

L'**àrea mínima cartografiable** és la superfície més petita que es pot representar de manera llegible i significativa a una escala i una mida de sortida determinades. No és una propietat absoluta de la font, sinó una relació entre detall, suport i funció. Una capa pot contenir polígons petits perfectament reals, però si a la composició final ocupen una taca imperceptible, el lector no els podrà distingir ni interpretar.

La decisió pot resoldre's de tres maneres. Si l'element és secundari, s'omet. Si forma part d'una categoria més gran, s'agrupa. Si és essencial per al missatge, es pot exagerar o representar amb un símbol, però llavors cal acceptar que la mida ja no correspon exactament a la superfície real. En tots els casos, la generalització ha d'estar justificada per la lectura final i no per la comoditat del programa.

![Comparació entre una font detallada i un mapa publicat en què els polígons massa petits s'ometen, s'agrupen o s'exageren si són essencials]({{ site.baseurl }}/assets/img/cartographic-language/minimum-mapping-unit.svg "L'àrea mínima cartografiable recorda que un detall pot existir a la font i no ser llegible a la mida final; generalitzar significa decidir com conservar el sentit del mapa. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="54rem"}

## Elements del mapa

### Títol i subtítol

El títol ha d'identificar el propòsit, la variable o el territori i, quan sigui necessari, el període o la unitat. No ha de repetir literalment tota la llegenda. En un mapa de context pot ser suficient «El Tarragonès dins de la província de Tarragona»; en un mapa temàtic caldrà identificar també l'indicador i l'any.

### Llegenda

La **llegenda** explica el significat dels símbols, les classes i les unitats utilitzades. Només ha d'incloure els elements que necessiten descodificació i que apareixen realment al mapa. L'ordre ha de seguir la lògica visual o conceptual de la simbologia, i les etiquetes automàtiques s'han de substituir per expressions comprensibles.

Un límit municipal evident pot no necessitar una entrada de llegenda si el títol i la composició ja n'aclareixen la funció. En canvi, una diferència entre comarca d'estudi, resta de la província i territoris exteriors necessita una explicació si no es pot deduir amb seguretat.

### Orientació, escala, fonts i crèdits

Els elements auxiliars s'inclouran quan compleixin una funció. Una fletxa del nord pot ser redundant en un mapa convencional orientat al nord i sense rotació. Una escala gràfica és útil quan cal estimar distàncies o quan el document es pot redimensionar. Cap element s'ha d'afegir només perquè aparegui entre les opcions de QGIS.

La font de dades, el període o versió, l'autoria i, quan sigui rellevant, el CRS són necessaris per interpretar i revisar el producte. Cal distingir la font de les geometries de la font dels indicadors: el capítol 6 utilitza principalment la base espacial, mentre que el mapa temàtic del capítol 8 incorporarà també les dades estadístiques.

L'orientació no és només una fletxa decorativa. El **nord geogràfic** apunta cap al pol geogràfic, el **nord de quadrícula** segueix les línies verticals del sistema projectat i el **nord magnètic** correspon a la direcció indicada per una brúixola en un lloc i moment concrets. En un mapa comarcal ordinari, aquestes diferències rarament seran decisives per a la lectura general, però convé saber que existeixen. Si es treballa amb navegació, treball de camp o cartografia tècnica, el tipus de nord i la declinació poden esdevenir rellevants.

Un mapa pot estar rotat per aprofitar millor el suport, seguir una costa, adaptar-se a un recorregut turístic o encaixar en una composició. Aquesta decisió és legítima si no desorienta el lector. Com més s'allunyi la composició de l'orientació convencional al nord, més necessari serà indicar l'orientació i proporcionar referències suficients. En canvi, repetir una rosa dels vents en cada mapa petit d'una infografia pot afegir soroll si tots els marcs comparteixen una orientació evident.

### Retolació

La **retolació** selecciona, jerarquitza i col·loca noms i altres textos perquè identifiquin elements geogràfics sense ambigüitat. Les etiquetes no han de competir amb la variable principal. Tipografia, mida, posició i contrast formen part de la jerarquia. La qualitat del mapa depèn tant d'aquestes relacions com de la simbologia principal; per això les decisions de retolació i composició s'han de revisar en la mida final i no només dins de la interfície de QGIS {% cite brewerDesigningBetterMaps2005 %}.

#### Prioritat dels topònims

No tots els noms tenen la mateixa funció. El nom de la comarca, els municipis del territori d'estudi i les referències externes poden formar nivells jeràrquics diferents. La prioritat s'ha de definir abans de reduir la tipografia: quan no hi ha espai, primer s'eliminen o se simplifiquen els noms secundaris.

#### Conflictes i ambigüitats

Una etiqueta no ha de tapar una altra, sortir de la seva entitat sense una relació clara ni confondre's amb un municipi veí. La posició, l'halo, el contrast i les línies de crida poden resoldre casos concrets, però una acumulació de recursos correctius sol indicar que hi ha massa noms per a l'escala disponible.

#### Comparació abans i després

La retolació es revisarà mitjançant una parella construïda sobre el territori d'estudi. La primera versió conservarà una configuració automàtica; la segona aplicarà prioritats, resolució de conflictes i jerarquia. La justificació identificarà canvis observables i no es limitarà a afirmar que el resultat és més atractiu.

## Jerarquia i composició

### Mapa principal i context

El territori d'estudi ha de dominar la composició. Els límits, fons i elements de localització han d'acompanyar-lo sense desplaçar-lo visualment.

Un requadre de situació és útil quan el públic no pot localitzar fàcilment la comarca en un marc més ampli. No és obligatori si el títol, l'extensió i les referències existents ja resolen la localització. Si s'incorpora, ha de compartir una jerarquia coherent amb el mapa principal i indicar sense ambigüitat quina àrea s'hi amplia.

### Equilibri, marges i recorregut de lectura

La distribució dels elements ha de conduir la mirada des del missatge principal cap a la informació de suport.

L'equilibri no obliga a centrar-ho tot ni a omplir qualsevol espai buit. Els marges separen grups, l'alineació fa visibles les relacions i l'espai en blanc evita que el mapa, el títol, la llegenda i els crèdits competeixin. La composició s'ha de valorar com una pàgina completa, no com una suma de peces independents.

## Activitat: construir el mapa de context

La pràctica construirà el **mapa de context** de la miniinfografia, encara sense aprofundir en la classificació temàtica. Mostrarà on se situa la comarca dins de la província de Tarragona i identificarà els seus municipis amb una jerarquia llegible. L'objectiu serà controlar escala, extensió, retolació, fonts i exportació; no convertir el mapa de localització en un segon mapa temàtic.

### Dades i projecte de partida

Es continuarà el mateix projecte QGIS dels capítols 4 i 5. La capa municipal, el CRS, les rutes i els codis ja validats no s'han de substituir per una descàrrega nova sense documentar. Abans de maquetar es fixaran la mida del mapa exportat, l'orientació de la pàgina i l'espai que la peça ocuparà a la miniinfografia.

El procediment general serà aquest:

1. crear una composició dins del projecte QGIS i definir-ne la mida i l'orientació finals;
2. afegir un marc principal amb l'extensió de la comarca i comprovar-ne l'escala;
3. ordenar i estilitzar les capes perquè la comarca domini i el context quedi en segon terme;
4. configurar l'etiquetatge municipal i resoldre els conflictes a la mida final;
5. afegir un segon marc provincial només si millora la localització;
6. completar títol, escala, fonts i crèdits després d'estabilitzar els marcs;
7. exportar una prova, obrir-la fora de QGIS i corregir la composició editable abans de generar la versió conservada.

### Construir el mapa principal

El mapa principal mostrarà els límits municipals de la comarca. L'extensió deixarà un marge suficient al voltant del territori sense reduir-lo innecessàriament, i la jerarquia dels traços distingirà el límit comarcal dels municipals. Els fons o territoris veïns tindran un tractament secundari.

Els municipis s'etiquetaran segons prioritats. Només es conservaran els noms que es puguin associar sense ambigüitat i llegir a la mida final. Si la composició no admet tots els topònims, la solució preferent serà reduir-ne el nombre o ajustar-ne la disposició, no fer-los tots igualment petits.

### Construir el requadre de situació

Un requadre més petit podrà mostrar la comarca destacada dins de la província de Tarragona. La seva extensió, simbologia i títol han de deixar clar que compleix una funció de localització. No incorporarà detalls municipals, llegendes o fons que no contribueixin a aquesta funció.

### Completar i exportar la composició

El títol, la llegenda si és necessària, l'escala, les fonts i els crèdits s'afegiran després d'estabilitzar el mapa. El CRS del projecte es comprovarà abans de confiar en la barra d'escala. La composició es revisarà a mida real i s'exportarà en PDF vectorial a `outputs/maps`, sense substituir el projecte ni la composició editable.

### Comprovacions de qualitat

Abans d'acceptar el mapa cal verificar que:

1. hi apareixen tots els municipis previstos i cap territori exterior es confon amb la comarca;
2. el CRS, l'extensió i la barra d'escala són coherents;
3. els límits municipals es poden seguir sense dominar visualment la pàgina;
4. les etiquetes no presenten col·lisions ni associacions ambigües;
5. el requadre de situació aporta una localització que el mapa principal no resol per si sol;
6. la font, la versió, l'autoria i els crèdits es poden recuperar;
7. els textos i traços continuen sent llegibles a la mida final;
8. el PDF conserva vectors, tipografies i proporcions quan s'obre fora de QGIS; en obrir-lo a Inkscape, els límits i textos vectorials es poden ampliar sense pixelació i seleccionar com a objectes.

### Evidències que s'han de conservar

::: table "Evidències del mapa de context"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `qgis` | Projecte QGIS continuat | Capes, CRS, estils, etiquetes i composició editable |
| `outputs/maps` | Mapa de context vectorial | Extensió final, topònims, escala funcional, fonts i crèdits |
| `outputs/maps` | Comparació de retolació o escala | Alternativa automàtica i versió revisada a la mateixa mida |
| `README.md` | Registre cartogràfic | Escala, mida final, detall omès, prioritats de retolació i decisió sobre el requadre |
:::
