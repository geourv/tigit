---
title: "Pràctiques QGIS i síntesi territorial: LLEGIU-ME de l'estudiant"
lang: ca
ref: tigit-practiques-estudiant
content_status: draft
---

# Pràctiques QGIS i síntesi territorial

El treball pràctic de TIGIT relaciona una pregunta territorial amb dades, mapes i una explicació visual. El recorregut comença amb l'organització d'un projecte QGIS, continua amb la incorporació d'indicadors i acaba amb una infografia SVG que combina mapes i gràfics. Cada operació ha de deixar una evidència que permeti entendre què s'ha fet i comprovar si el resultat respon a la pregunta.

El parell Tarragonès–Vila-seca és el cas de demostració del professorat. Cada equip ha d'adaptar noms, codis, recomptes i resultats al municipi i la comarca que tingui assignats. Les dades de població i habitatge de la demostració corresponen a 2021; la geometria ICGC és de gener de 2026. Cal distingir aquestes dates i documentar-ne la compatibilitat territorial.

## Preparar l'espai de treball

Les rutes d'aquesta lectura parteixen de l'arrel del projecte pràctic. Cal extreure completament el material de treball i mantenir juntes les carpetes `data`, `qgis`, `outputs` i `captures`. El registre de treball ha d'identificar el territori, les fonts, el període, la versió de QGIS i la ubicació de cada resultat.

El GeoPackage `data/processed/tarragones-boundaries-icgc-20260120.gpkg` proporciona la base espacial de la demostració. La taula `data/processed/municipal-indicators-tarragones-2021.csv`, amb el seu `.csvt`, aporta indicadors preparats. Les dades d'Idescat es poden facilitar ja descarregades per concentrar el laboratori en la unió i la interpretació. El llibre de càlcul conserva les fórmules i el diccionari: el CSV és una còpia de transferència, no una font independent per corregir a mà.

El nucli del treball utilitza dades locals. La pràctica de serveis ICGC necessita connexió i té un recorregut propi. Si un recurs requerit no figura a l'inventari del material rebut, cal aclarir-ne la disponibilitat amb el professorat abans de continuar aquella operació.

## 1. Reconèixer QGIS i comparar formats

La [teoria de dades espacials](https://geourv.github.io/tigit/ca/chapters/terra-dades-espacials/) explica geometria, CRS i escala. A QGIS aquests conceptes apareixen en decisions concretes: quina capa s'obre, què representen les coordenades i quin detall pot sostenir el mapa.

El llenç mostra el mapa; el panell de capes en controla l'ordre i la visibilitat; el navegador ajuda a localitzar recursos; i la barra d'estat informa, entre altres elements, de l'escala i el CRS del projecte. El gestor de fonts permet carregar les dades. Cal relacionar cada element amb la seva funció mentre s'observa la interfície de la versió utilitzada.

1. Crear el projecte dins de `qgis` i configurar l'ús de rutes relatives.
2. Obrir el GeoPackage amb el gestor de fonts i identificar les subcapes de municipis, comarca, província, Vila-seca de detall i capitals municipals.
3. Revisar geometria, camps, CRS i nombre d'entitats de `municipalities_250k`.
4. Exportar una còpia docent de la capa municipal a Shapefile, sense substituir el GeoPackage, i tornar-la a carregar.
5. Comparar recomptes, codis i topònims entre les dues capes.
6. Desar `qgis/tigit-04-dades-espacials.qgz`, tancar-lo i reobrir-lo.

Un Shapefile distribueix la informació entre diversos fitxers: `.shp` conté geometria, `.shx` l'índex i `.dbf` els atributs; `.prj` documenta el CRS i `.cpg` pot declarar la codificació. Cal conservar-los junts. Un GeoPackage pot reunir diverses capes en un sol fitxer. El `.qgz` desa la configuració del projecte, però no incorpora automàticament totes les dades que consulta.

La comprovació ha de demostrar que desar el projecte i conservar les dades són responsabilitats diferents. La captura del gestor de fonts ha de mostrar la subcapa seleccionada, i la de propietats ha de permetre identificar-ne el CRS. Un mapa que apareix al lloc esperat encara necessita aquests controls.

## 2. Llegir atributs i unir els indicadors

La [preparació de dades](https://geourv.github.io/tigit/ca/chapters/fonts-preparacio-dades/), els [indicadors](https://geourv.github.io/tigit/ca/chapters/indicadors-territorials/) i les [unions en un SIG](https://geourv.github.io/tigit/ca/chapters/integracio-sig/) expliquen per què una clau territorial és més fiable que una coincidència de noms. Una fila municipal ha d'identificar la mateixa unitat a la geometria i a la taula estadística.

Cal distingir ordenar, seleccionar i filtrar: ordenar canvia la consulta de les files; seleccionar ressalta casos; filtrar limita els registres visibles o disponibles per a una operació. Cap d'aquestes accions justifica modificar els originals.

1. Obrir la taula d'atributs municipal i reconèixer camps de text, enters i decimals.
2. Carregar el CSV com a taula sense geometria i comprovar la interpretació dels tipus. El codi `mun_code` ha de conservar-se com a text.
3. Comptar files i claus úniques als dos costats; revisar duplicats, absències i compatibilitat territorial.
4. Configurar la unió entre `CODIMUNI` i `mun_code`, anotant el prefix amb què QGIS identifica els camps units.
5. Contrastar tres municipis amb el llibre, comptar coincidències i comprovar que no s'han multiplicat les geometries.
6. Desar la continuació com `qgis/tigit-05-integracio-sig.qgz` i registrar les dues consultes següents.

La primera consulta identifica el municipi de referència; la segona selecciona els municipis amb més del 50% d'habitatge no principal. Cal utilitzar el nom efectiu del camp a QGIS, inclòs el prefix de la unió, i conservar expressió, recompte i codis seleccionats. La captura de la configuració ha de permetre recuperar les dues claus; la consulta ha de deixar visible el seu recompte.

Per comparar municipi i comarca, el percentatge comarcal es calcula amb la suma d'habitatges no principals dividida per la suma d'habitatges totals, multiplicada per 100. La mitjana simple dels percentatges municipals respon una altra pregunta perquè dona el mateix pes a municipis amb parcs residencials diferents. Els camps acabats en `_pct` ja expressen percentatges sobre 100.

Com a exercici auxiliar de coordenades, la taula de centres educatius es pot carregar amb `utm_x` i `utm_y` en EPSG:25831 i amb longitud/latitud en EPSG:4326. Cal comparar les dues localitzacions considerant l'arrodoniment de les coordenades. Els punts representen entrades de centres del curs 2025/2026, no dades d'habitatge ni parcel·les completes.

## 3. Preparar el mapa de referència i les etiquetes

El [llenguatge cartogràfic](https://geourv.github.io/tigit/ca/chapters/llenguatge-cartografic/) relaciona escala, generalització i jerarquia. Un mapa de referència ha de permetre localitzar el municipi dins de la comarca i entendre on és la comarca, sense competir amb la informació que s'analitzarà després.

Cal reprendre el projecte amb la unió comprovada i desar-ne la continuació com `qgis/tigit-06-llenguatge-cartografic.qgz`. La capa municipal generalitzada serveix per al conjunt comarcal; la geometria de Vila-seca a 1:50.000 permet una lectura de més detall. Ampliar una capa a 1:250.000 no crea informació de carrers ni precisió addicional.

1. Diferenciar el contorn comarcal, els límits municipals i el municipi de referència amb una jerarquia de traços.
2. Afegir les capitals municipals i els topònims necessaris per orientar-se.
3. Configurar etiquetes segons escala i prioritat, evitant associacions ambigües.
4. Comparar el resultat a escala municipal i comarcal, a la mida prevista d'ús.

L'evidència ha d'explicar quins topònims es prioritzen i per què. La captura de l'etiquetatge mostra la decisió d'interfície; el projecte conserva la configuració real. El mapa de referència s'utilitzarà en les composicions, sense reconstruir-lo cada vegada.

## 4. Representar una intensitat amb coropletes

La [semiologia](https://geourv.github.io/tigit/ca/chapters/semiologia-visualitzacio/), el [color](https://geourv.github.io/tigit/ca/chapters/color/) i la [cartografia temàtica](https://geourv.github.io/tigit/ca/chapters/cartografia-tematica/) ajuden a triar una representació coherent amb la dada. Una coropleta permet comparar intensitats municipals quan el denominador està justificat.

En la demostració, `housing_non_main_pct` relaciona habitatges no principals i habitatges totals del mateix municipi i any. Cal reprendre el projecte de context i desar-ne la continuació com `qgis/tigit-08-cartografia-tematica.qgz`.

1. Comprovar el camp, la unitat, el rang de valors i l'estat dels indicadors units.
2. Aplicar una paleta seqüencial i una primera classificació documentada.
3. Crear una alternativa en què només canviï el mètode de classificació; mantenir dades, nombre de classes, paleta, extensió i mida.
4. Registrar talls, recomptes per classe i possibles classes buides; justificar la versió escollida.
5. Conservar l'alternativa editable dins del projecte.

El total de casos classificats ha de concordar amb els municipis que tenen dades. Un nul no és un zero, i un percentatge ja calculat no s'ha de tornar a normalitzar. La llegenda ha de permetre llegir els intervals, la unitat i les absències. La captura de la simbologia ha de mostrar el camp i els punts de tall.

El percentatge d'habitatge no principal descriu una composició residencial, no identifica directament habitatges turístics. Tampoc informa de la distribució interna per carrers o persones. Aquesta limitació ha d'acompanyar la interpretació del mapa.

## 5. Representar volums amb símbols graduats

El nombre total d'habitatges és una magnitud absoluta. Comparar-lo amb el percentatge de la pràctica anterior permet distingir volum i intensitat: un municipi pot tenir molts habitatges i un pes relatiu moderat d'habitatge no principal.

Cal representar `housing_total` amb símbols situats en un punt interior de cada municipi. Els símbols graduats agrupen els valors en classes de mida; els proporcionals varien contínuament amb el valor. Aquestes dues lectures s'han de conservar amb noms d'estil o capes diferenciats.

1. Obtenir punts interiors municipals i comprovar que mantenen els codis i els atributs corresponents.
2. Definir classes de mida i una llegenda amb els intervals reals.
3. Revisar la superposició dels símbols i la llegibilitat dels límits i topònims.
4. Comparar el mapa graduat amb una variant proporcional contínua.

En la variant proporcional, l'àrea del cercle ha de seguir la magnitud; escalar directament el radi exageraria les diferències. Cal contrastar almenys dos valors amb la llegenda i explicar quina precisió de lectura proporciona cada mètode. Les captures documentaran les classes de mida i la configuració de proporcionalitat, sense substituir els mapes exportats.

## 6. Compondre mapes amb temes i localitzador

La composició converteix les capes i els estils en una peça que es pot llegir fora de QGIS. El mapa principal explica el fenomen; el localitzador petit situa el territori; la llegenda, l'escala i les fonts permeten interpretar-lo. Cal decidir la mida final abans d'ajustar els textos.

1. Desar temes diferenciats per a referència, coropleta, símbols i localització.
2. Crear una composició al dissenyador i afegir-hi el marc principal i el localitzador.
3. Assignar el tema pertinent a cada marc i configurar-ne extensió, escala i orientació.
4. Afegir llegendes, escala, títol, període estadístic, data de la geometria i crèdits.
5. Canviar la visibilitat al llenç, desar i reobrir el projecte per comprovar que la composició conserva la configuració prevista.
6. Exportar en SVG o PDF vectorial i revisar el resultat a la mida final.

Un tema conserva la combinació de capes i estils. L'extensió i l'escala s'han de fixar al marc de la composició. Per això no n'hi ha prou amb desar un tema perquè el mapa principal i el localitzador mantinguin la seva funció.

La composició es revisarà sobre la base editable: cal corregir col·lisions, retallar textos quan convingui i donar espai a la llegenda. Un canvi de valors, classificació o geometria s'ha de fer al projecte QGIS i tornar a exportar. La captura del dissenyador ha de mostrar els dos marcs i la propietat que s'està comprovant.

## 7. Consultar fons i serveis de l'ICGC

Els serveis en línia permeten explorar informació actualitzada, però introdueixen una dependència de connexió i de disponibilitat. La documentació de l'[ICGC](https://www.icgc.cat/ca/Geoinformacio-i-mapes/Geoinformacio-en-linia-Geoserveis) i del connector [Open ICGC](https://plugins.qgis.org/plugins/OpenICGC/) permet distingir els fons de referència i els productes descarregables.

El servei de mapa base WMS té l'adreça `https://geoserveis.icgc.cat/servei/catalunya/mapa-base/wms`. El servei WFS de divisions administratives és `https://geoserveis.icgc.cat/servei/catalunya/divisions-administratives/wfs`. Cal comprovar les capes i capacitats que ofereixen en el moment de l'exercici i utilitzar el connector només amb una versió comprovada pel professorat.

1. Treballar en un projecte d'exploració separat de la base local.
2. Afegir un fons WMS i observar què aporta per orientar-se.
3. Consultar una capa WFS, inspeccionar-ne els camps i identificar-ne el CRS i el nivell de detall.
4. Acotar la consulta o descàrrega segons el territori i revisar límits, paginació i recompte.
5. Si cal conservar el resultat, desar-lo localment amb font, data i condicions d'ús, i provar-ne l'obertura sense connexió.

El WMS proporciona una imatge del mapa; aquesta imatge no substitueix les geometries i els atributs necessaris per a una unió. Una capa remota amagada també continua depenent del servei. Les captures han de mostrar la connexió, la capa seleccionada i l'acció real utilitzada, amb el resultat de la comprovació local.

## 8. Elaborar la síntesi en un SVG editable

La [teoria d'infografia i síntesi](https://geourv.github.io/tigit/ca/chapters/infografia-sintesi/) ajuda a decidir què aporta cada peça. El mapa conserva les relacions espacials; un gràfic pot ordenar millor els municipis; el text explica el resultat i el seu límit. Cal seleccionar dues o tres peces visuals en total que sostinguin un mateix argument, no reunir tots els resultats del laboratori.

La demostració utilitza A3 vertical, de 297 × 420 mm, amb marges de 15 mm, sis columnes i separacions de 6 mm. Aquesta retícula és una base per alinear, no una obligació d'omplir tots els espais. Si el suport canvia, cal redissenyar la composició en lloc de reduir-la automàticament.

La [plantilla editable A3](../../templates/infografia-a3.svg), situada a `templates/infografia-a3.svg`, proporciona aquesta base. Conté dos espais visuals principals, per al mapa i el gràfic, i un localitzador integrat al mapa. Els camps entre claudàtors i els marcs buits indiquen què cal inserir; no representen dades ni una anàlisi resolta. Cal desar-ne una còpia de treball a `outputs/infographics` amb el territori i el període al nom, conservant la plantilla original.

1. Escriure una pregunta territorial, un resultat principal i una limitació específica.
2. Seleccionar els mapes i gràfics que aporten evidències complementàries.
3. Preparar un document SVG amb grups o capes identificables per a peces visuals, mètriques, interpretació i fonts.
4. Importar les peces vectorials i mantenir-ne la proporció; conservar recursos incrustats o accessibles dins del projecte.
5. Revisar valors, topònims, períodes, llegendes i tipografies a mida final.
6. Fer una prova de lectura amb una persona que no hagi participat en la composició i registrar els canvis necessaris.

El màster es desarà a `outputs/infographics` amb territori i període al nom. Les correccions que afectin les dades es faran al llibre o al projecte cartogràfic d'origen. El registre final ha de relacionar cada gràfic amb el seu full o sèrie i cada mapa amb la composició, capa i camp que l'han produït.

La comprovació d'editabilitat es farà sobre els objectes reals d'Inkscape: una imatge de la seva interfície no substitueix el màster SVG. Si es demana una captura, ha de correspondre a l'operació efectivament observada. La reobertura del projecte, dels recursos i de la síntesi des d'una carpeta nova completa el control de portabilitat.

### Inserir les peces a la plantilla

Les capes s'identifiquen en català: paper, títol i pregunta, mapa principal, localitzador, gràfic, lectura dels resultats, fonts i guies. El paper opac està bloquejat per facilitar la selecció dels altres objectes. La capa de guies també està bloquejada i oculta; es pot mostrar per comprovar les sis columnes, però ha de tornar a quedar oculta en l'exportació. Les guies pròpies del document ajuden a alinear i no s'imprimeixen.

El fons de paper incorpora 1 mm de sagnat fora de la pàgina. En exportar cal seleccionar l'àrea de pàgina de 297 × 420 mm, no l'àrea total del dibuix, perquè aquest sagnat no canviï el format final.

1. Obrir la còpia de la plantilla i activar la capa de destí, per exemple «Mapa principal: peça vectorial».
2. Obrir l'SVG exportat de QGIS o del gràfic en un document separat i comprovar que límits, marques, etiquetes i llegenda es conserven com a objectes vectorials. Si la peça arriba en PDF, importar la pàgina pertinent i revisar igualment els objectes i les fonts resultants.
3. Copiar o importar la peça com a contingut vectorial editable, mantenir-la agrupada i inserir-la a la capa corresponent. Un únic objecte d'imatge que no permet accedir als vectors no substitueix aquesta importació.
4. Ajustar-ne la mida amb la proporció bloquejada. Si no encaixa, cal revisar l'espai de la composició o tornar a exportar amb una mida més adequada, no estirar-la en una sola direcció.
5. Eliminar el grup de camp corresponent, identificat com a `camp-mapa-principal`, `camp-localitzador` o `camp-grafic`, quan la peça real ja sigui al lloc. Cal fer-ho sense eliminar el grup importat ni la capa de treball.
6. Substituir pregunta, resultat, limitació, unitats i crèdits pels textos de l'anàlisi. La marca «Plantilla per emplenar» i els altres camps de treball també s'han de substituir en la composició acabada; les metadades de títol i descripció han d'identificar la peça real.

Si l'exportació de QGIS ja conté el mapa principal i el localitzador en una mateixa composició, cal inserir-los com una peça i ocultar o retirar el camp separat de localització de la plantilla. No s'ha de duplicar el requadre. Una tercera peça visual només es justifica si aporta una evidència diferent i la retícula es pot adaptar sense fer il·legibles els textos; no és necessari omplir més espais.

La revisió tipogràfica ha de comprovar accents, topònims, xifres, percentatges i unitats. La plantilla utilitza DejaVu Sans; cal tenir disponible la família utilitzada o acordar-ne una substitució deliberada. Convé conservar el text editable al màster. Si l'importador substitueix una font o rasteritza la peça, cal revisar l'exportació o la importació abans de continuar. Les correccions de valors, classes, etiquetes cartogràfiques o llegendes s'han de fer a l'aplicació d'origen.

Redimensionar un mapa modifica l'escala numèrica que tindria imprès. Per conservar una escala declarada, cal fixar la mida final a QGIS i tornar a exportar; la proporcionalitat visual per si sola no acredita que aquella escala continuï sent correcta. La barra gràfica, les marques i la llegenda s'han de conservar coherents amb el mapa.

El peu de cada peça ha d'identificar variable, unitat, territori i període. El bloc compartit de fonts ha de distingir dades estadístiques, geometria, llicències i autoria. Cal comprovar que cap recurs importat depengui d'una ruta externa a la carpeta de treball i que el màster s'obri complet en una ubicació nova.
