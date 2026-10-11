---
title: "Pràctiques QGIS i síntesi territorial: LLEGIU-ME del professorat"
lang: ca
ref: tigit-practiques-professorat
content_status: draft
---

# Guia del professorat per al recorregut QGIS i SVG

El laboratori de TIGIT desenvolupa una lectura municipal i comarcal mitjançant un projecte acumulatiu. La preparació de dades pot arribar resolta perquè el temps de pràctica se centri en l'organització del SIG, la unió, la representació i la comunicació. El control docent ha de distingir una operació que s'ha executat correctament d'una interpretació que les dades permeten sostenir.

El cas de demostració és Tarragonès–Vila-seca. Els equips adapten el procediment al seu parell assignat; els recomptes d'aquesta guia no s'imposen a altres comarques. El codi de l'assignatura al Grau en Gestió en Turisme i Hoteleria és `21224102`; el manual comparteix docència amb Geografia, codi `21234003`.

La teoria precedent és la dels capítols de dades espacials, SIG, llenguatge cartogràfic, semiologia, color, cartografia temàtica i síntesi. El professorat de teoria fixa el significat de les variables i dels mètodes; el de laboratori comprova com es materialitzen al projecte. El registre de la pràctica ha de permetre a tots dos reconstruir la decisió.

## Preparar la demostració

Cal identificar la versió de QGIS, l'idioma real de la interfície i les versions dels connectors que s'utilitzin. Les captures han de mostrar aquesta interfície, amb els recursos i els diàlegs necessaris per entendre una decisió. Els mapes i gràfics s'avaluen en les seves exportacions, no mitjançant captures del llenç.

Les rutes següents són relatives a l'arrel del projecte pràctic. `data/processed/tarragones-boundaries-icgc-20260120.gpkg` conté cinc capes locals en EPSG:25831: 22 municipis, una comarca, una província, Vila-seca a 1:50.000 i 22 capitals municipals. `catalonia-counties-icgc-20260120.gpkg` hi afegeix les 43 comarques per al context de Catalunya.

La taula `municipal-indicators-tarragones-2021.csv` conté onze camps i 22 registres; el `.csvt` corresponent en declara els tipus. La procedència es conserva als originals d'Idescat i al llibre `tigit-05-integracio-sig-teaching.xlsx`, amb fonts, diccionari, fórmules, paleta i `map_export`. El llibre és la referència per revisar una discrepància; no s'ha de corregir el CSV com una font independent.

Els indicadors de 2021 es relacionen amb geometries de 2026. Cal documentar que les unitats territorials són compatibles abans d'interpretar la unió. Una coincidència exacta de codis és necessària, però no prova per si sola que no hi hagi hagut canvis de límits.

## 1. QGIS, gestor de fonts i formats

L'objectiu és que es pugui explicar què es desa al projecte i què continua en fitxers externs. Cal mostrar el llenç, els panells i la barra d'estat a partir d'una tasca concreta: carregar i identificar la base municipal. Una visita descontextualitzada a tots els menús aporta menys que una càrrega seguida de la inspecció de propietats.

La comparació de formats utilitza la mateixa geometria i una selecció documentada de camps. El Shapefile docent ha de conservar almenys la clau, el nom i el codi comarcal, amb els seus auxiliars; el GeoPackage conserva la font preparada. La revisió ha d'incloure recomptes, codis, accents, CRS i equivalència geomètrica. Les limitacions de longitud dels noms de camp i de tipus no es poden interpretar com una correcció de la font.

La fita és `qgis/tigit-04-dades-espacials.qgz`. Cal provar-ne la reobertura en una altra ubicació, amb les dades relatives disponibles. Un projecte que només funciona a la carpeta original no supera el control.

La captura del gestor de fonts ha de permetre identificar la subcapa carregada. La de propietats ha de mostrar geometria i CRS. Si una capa apareix desplaçada, cal diagnosticar coordenades, unitats i definició de CRS; no provar codis fins que sembli encaixar.

## 2. Atributs i unió d'Idescat

La demostració comença diferenciant ordenació, selecció i filtre. Després es carrega la taula sense geometria, amb `mun_code` com a text, i es compten claus úniques als dos costats. La relació documentada és `CODIMUNI` amb `mun_code`; el prefix dels camps units s'ha d'anotar perquè les expressions es puguin reconstruir.

Els controls alfanumèrics de les entrades locals són:

- 22 files al CSV i 22 codis municipals únics.
- 22 entitats a `municipalities_250k` i 22 `CODIMUNI` únics.
- Coincidència dels conjunts de claus, sense files sobrants.
- `county_code = 36`, `year = 2021` i `indicator_status = ok` a totes les files.

La unió executada ha de mantenir les 22 geometries i els valors estadístics. Cal aturar el procediment si apareixen duplicats, nuls inesperats o multiplicació de registres. Els noms geogràfics poden ajudar a diagnosticar, però no substitueixen la clau: per exemple, l'ordre de l'article pot diferir entre fonts.

### Casos de contrast

Vila-seca, codi `431711`, té 17.417 habitatges totals i 8.692 no principals. El percentatge del CSV és `49.9052649710053`, és a dir, aproximadament 49,91%. No entra a la consulta estricta de valors superiors a 50.

Roda de Berà, `431310`, aporta el contrast alt: 8.762 habitatges totals, 5.673 no principals i `64.7454918968272`%. La Pobla de Mafumet, `431093`, aporta el contrast baix: 1.615 totals, 195 no principals i `12.0743034055728`%.

La consulta sobre `housing_non_main_pct > 50`, aplicada al camp efectiu de la unió, ha de donar sis codis: `430120`, `430509`, `431310`, `431536`, `431649` i `439057`. Cal conservar l'expressió, el recompte i els codis, no només una imatge amb municipis ressaltats.

La suma dels 22 registres proporciona 169.179 habitatges totals i 66.105 no principals. El percentatge agregat és `39.07399854591882`%. La població suma 262.868 residents, dels quals 45.352 tenen 65 anys o més; el percentatge agregat és `17.252765646636334`%. Aquests valors són controls calculats a partir del CSV local, no una nova taula oficial descarregada.

La fita `qgis/tigit-05-integracio-sig.qgz` conserva la unió i les consultes. Si es materialitza una capa per compartir-la, cal comprovar-la de nou i mantenir la procedència de la taula. La captura ha de mostrar les claus i els camps incorporats, amb el recompte final recuperable.

### Exercici auxiliar XY

El CSV de centres educatius de Vila-seca té 17 files, i l'ampliació del Tarragonès en té 183. La importació UTM utilitza EPSG:25831; la geogràfica utilitza EPSG:4326. Cal justificar una tolerància de comparació segons la precisió i l'arrodoniment de la font, no exigir igualtat binària de coordenades transformades.

La lectura ha de conservar que els punts representen entrades de centres del curs 2025/2026. No es poden interpretar com a oferta turística ni sumar-los als indicadors censals de 2021. La captura pertinent és el diàleg d'importació amb camps X/Y, CRS i tipus visibles.

## 3. Referència territorial i etiquetatge

La lectura de la comarca necessita un context que expliqui la localització del municipi. Cal distingir el contorn comarcal, els límits municipals i la marca del municipi de referència amb una jerarquia controlada. El canvi entre escala municipal i comarcal permet observar quines etiquetes deixen de ser llegibles i per què cal generalitzar.

La base local ofereix límits administratius i capitals; no s'ha de descriure com una cartografia detallada de carrers. El GeoPackage de comarques permet situar el Tarragonès dins de Catalunya, mentre que la geometria provincial facilita un context més proper. El fons més adequat depèn de la pregunta i del públic, no de quina capa omple més espai.

La fita és `qgis/tigit-06-llenguatge-cartografic.qgz`. Cal conservar els criteris de prioritat dels topònims i els estils que es reutilitzaran en les composicions. La revisió docent comprova associació inequívoca, col·lisions i llegibilitat a mida final. Les captures de propietats d'etiquetatge han de correspondre a aquests criteris.

## 4. Coropletes i alternativa controlada

La coropleta de la demostració utilitza `housing_non_main_pct`. El numerador és `housing_non_main`, el denominador és `housing_total` i la unitat és el percentatge. Cal comprovar que el camp ja està normalitzat i que no s'aplica una segona divisió.

Per comparar classificacions, es mantenen les mateixes dades, paleta, extensió, mida i nombre de classes. Només canvia el mètode de tall. El registre ha d'incloure els talls exactes, els recomptes i qualsevol classe buida; els casos classificats han de sumar els 22 municipis amb dades. No hi ha un únic mètode correcte al marge de la pregunta i la distribució.

La revisió ha de separar un canvi de classificació d'un canvi de paleta. La primera alternativa queda editable; la prova cromàtica es fa amb els talls fixats. La captura mostrarà el camp i els intervals, i l'exportació permetrà revisar llegenda, contrast i mida del text.

El resultat forma part de `qgis/tigit-08-cartografia-tematica.qgz`. El nom previst per a l'exportació principal és `outputs/maps/coropleta_no_principal_tarragones_2021.svg`. La interpretació ha d'explicar que habitatge no principal inclou situacions residencials diferents i no és un indicador directe d'habitatge turístic.

## 5. Símbols graduats i variant proporcional

El camp `housing_total` permet representar una magnitud absoluta sense convertir el recompte en una falsa intensitat superficial. La pràctica ha de fer explícita la diferència entre unes classes de mida i una escala contínua. Convé demanar què es pot inferir d'un símbol de cada variant i quina informació s'ha agrupat.

Els punts interiors municipals han de conservar una clau única i els atributs de les 22 entitats. Cal verificar-ne la posició i evitar que un centroide exterior es presenti com una localització correcta del símbol. Les classes graduades han de coincidir amb la llegenda i amb el nombre de casos registrats.

En la variant proporcional, quadruplicar la dada duplica el diàmetre del cercle. Aquest control ajuda a detectar una escala aplicada erròniament al radi. La revisió també ha de comprovar que els símbols no ocultin tota la base ni suggereixin una localització interna del parc residencial que la font no proporciona.

`outputs/maps/simbols_habitatges_totals_tarragones_2021.svg` identifica la variant proporcional del recorregut existent. La versió graduada s'ha d'identificar de manera diferenciada. Les captures documenten la classificació de mides i l'assistent de proporcionalitat; les dues variants continuen editables al projecte.

## 6. Temes, mapes i composicions editables

Els temes permeten recuperar combinacions de capes i estils per a referència, coropleta, símbols i localització. No substitueixen la definició d'extensió i escala dels marcs del dissenyador. Aquesta distinció és central quan una mateixa composició conté un mapa principal i un localitzador petit.

La demostració ha de conservar un tema adequat per a cada marc i definir-ne la mida i orientació. La llegenda principal ha de correspondre a l'indicador; el localitzador necessita un context simplificat i una marca inequívoca de l'àrea d'estudi. Cal comprovar escala, unitats, fonts i crèdits després d'estabilitzar els mapes.

La prova tècnica consisteix a canviar la visibilitat del llenç, desar, reobrir en una altra ubicació i revisar la composició sense xarxa. S'han de conservar mapes, temes, estils i recursos. La prova visual revisa les etiquetes, l'espai de les llegendes i la jerarquia a la mida prevista per a la infografia.

Una base operativa pot deixar ajustos de posició, retolació o distribució per al professorat, sempre que aquests elements siguin editables i els controls incomplets estiguin identificats al registre de treball. L'exportació només es considera acabada després d'aquesta revisió. Una captura o un mapa rasteritzat no pot substituir el projecte font.

Els mapes de context mantenen els noms `outputs/maps/context_tarragones_initial.pdf` i `context_tarragones.pdf` per distingir la composició inicial i la revisada. Les peces temàtiques s'exporten en vector des de les seves composicions. Les captures mostren l'assignació de temes i les propietats dels dos marcs.

## 7. Serveis ICGC i descàrrega

Cal separar aquesta demostració en línia del projecte base local. Les fonts de consulta són el [catàleg Open ICGC](https://plugins.qgis.org/plugins/OpenICGC/), la [documentació del connector](https://www.icgc.cat/ca/Eines-i-visors/Eines/Connector-QGIS-Open-ICGC) i el [servei de mapa base](https://www.icgc.cat/ca/Geoinformacio-i-mapes/Servei-de-Mapa-Base). La versió instal·lada i els controls disponibles s'han de registrar abans de descriure'n el procediment de classe.

Les connexions de referència són:

- WMS: `https://geoserveis.icgc.cat/servei/catalunya/mapa-base/wms`.
- WFS: `https://geoserveis.icgc.cat/servei/catalunya/divisions-administratives/wfs`.

Les capacitats WFS consultades anuncien `divisions_administratives_wfs:divisions_administratives_municipis_250000` amb EPSG:25831. Cal tornar a comprovar el catàleg i l'esquema en la sessió de treball, perquè un servei pot canviar sense modificar l'adreça. No s'han de copiar expressions sobre camps locals assumint que tenen el mateix nom al servei.

La demostració de descàrrega ha de revisar selecció territorial, paginació, límits i recompte. Després d'exportar, cal validar clau, geometria, CRS, font, data i condicions de reutilització. La capa local només pot substituir la dependència remota després d'aquests controls; amagar un WMS o confiar en la memòria cau no acredita funcionament offline.

La captura documentarà la connexió i l'acció real de descàrrega o exportació. Si el connector no funciona en la versió seleccionada, la demostració ha d'explicar el resultat de la prova i emprar una via nativa verificada, sense reconstruir una interfície fictícia.

## 8. Síntesi SVG i prova de lectura

La infografia ha de respondre una pregunta amb dues o tres peces visuals complementàries, comptant conjuntament gràfics i mapes. Els requadres integrats en un mapa no formen un panell independent. Aquesta selecció evita convertir l'inventari de pràctiques en una làmina saturada de resultats.

La base A3 vertical, de 297 × 420 mm, utilitza marges de 15 mm, sis columnes i separacions de 6 mm. El màster SVG ha de conservar grups o capes per als recursos visuals, mètriques, interpretació i fonts. Els mapes i gràfics s'importen com a peces vectorials identificables, sense deformar-ne la proporció ni transcriure valors.

La [plantilla de treball `templates/infografia-a3.svg`](../../templates/infografia-a3.svg) concreta aquesta retícula amb columnes de 39,5 mm. Ofereix dos espais visuals principals, mapa i gràfic, amb un localitzador dins del mapa i una columna de lectura de resultats. Els camps entre claudàtors són instruccions d'emplenament, no exemples de resultats. La figura conceptual del manual sobre retícula i composició continua tenint una funció explicativa diferent.

La revisió docent ha de seguir la procedència de cada peça: full i rang o sèrie per als gràfics; projecte, composició, capa i camp per als mapes. Una incoherència es corregeix a la font corresponent i es torna a exportar. Cal distingir període estadístic, data de la geometria i any d'edició del document.

La prova de lectura demana a una persona aliena a la composició que identifiqui pregunta, resultat, evidència i limitació. Les respostes han de justificar canvis observables en el document. La comprovació tècnica revisa objectes editables, fonts, recursos i obertura des d'una ubicació nova.

La captura real d'una operació d'Inkscape, quan es demani, és una evidència diferent de la verificació del màster. La docència pot explicar la retícula, la importació i la jerarquia amb recursos SVG editables; cap recreació de la interfície s'ha de presentar com una captura executada.

### Criteris de valoració formativa de la composició

La valoració ha d'observar si les decisions editorials conserven el significat de les dades. Els criteris següents orienten el retorn docent i els ajustos de la peça:

- **Argument i evidència:** pregunta concreta, resultat sostingut pel mapa i el gràfic, i limitació que acota la interpretació. Les dues peces han d'aportar lectures complementàries; el localitzador ha d'orientar.
- **Integritat de la representació:** proporcions conservades, símbols i llegendes coherents, unitats visibles i escala cartogràfica revisada després de qualsevol canvi de mida. Una escala numèrica impresa requereix exportar el mapa a la mida pertinent.
- **Jerarquia i llegibilitat:** mapa principal dominant, localitzador subordinat i textos llegibles a la mida final. Cal reordenar o simplificar abans de reduir tipografia per encabir contingut.
- **Editabilitat:** capes amb noms semàntics, mapes i gràfics importats com a vectors i textos del màster editables. Cal comprovar grups i objectes, no només l'aparença de la previsualització.
- **Fonts i períodes:** atribucions completes, llicències, separació entre any estadístic i data de la geometria, i correspondència de cada peça amb el registre de procedència.
- **Tancament de la plantilla:** camps i marcs de treball substituïts, capa de guies oculta, metadades actualitzades i recursos accessibles després de moure la carpeta del projecte.

El professorat o l'autor pot acabar la composició ajustant l'amplada del títol, els salts de línia, l'espai de la llegenda, la posició del localitzador i la distribució del bloc de fonts. Si la composició QGIS ja inclou el localitzador, cal retirar el camp separat de la plantilla. Incorporar una tercera evidència implica revisar la retícula, no reduir indiscriminadament els tres panells. Els canvis que afectin classificació, geometria, escala declarada o contingut d'una etiqueta cartogràfica han de tornar a QGIS.

La plantilla usa DejaVu Sans i conserva un fons de paper opac de color `#fffdf8`. Una substitució tipogràfica ha de ser explícita i s'ha de revisar amb els topònims reals; un altre color de paper és possible si manté opacitat i contrast. La previsualització rasteritzada de la plantilla serveix per revisar la distribució, però l'avaluació de l'editabilitat es fa sobre l'SVG i els documents font.

El paper té 1 mm de sagnat per cobrir també els marges de mostreig en rasteritzar. Cal verificar que s'exporta l'àrea de pàgina A3 i no la totalitat del dibuix. El sagnat no modifica ni el `viewBox` de 297 × 420 ni els marges útils de 15 mm.

## Revisions del conjunt

Cada equip ha de poder explicar una decisió sobre dades, una sobre representació i una sobre comunicació, amb evidències recuperables. Els errors de fitxer, de càlcul i d'interpretació requereixen correccions diferents. El registre final conservarà els controls superats i els ajustos fets al projecte i a la síntesi.

El cas d'habitatge permet aprendre aquest circuit, però no substitueix la taula municipal d'oferta turística i els seus indicadors quan l'activitat del curs els requereixi. Les dades d'allotjaments geocodificats de Vila-seca són una ampliació puntual, no una cobertura equivalent dels 22 municipis. Qualsevol adaptació a un altre territori ha de repetir les comprovacions amb les seves fonts i recomptes.
