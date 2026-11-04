---
title: "Primers mapes amb QGIS: LLEGIU-ME de l'alumnat"
lang: ca
ref: tigit-practica-04-qgis-alumnat
content_status: draft
recipient: alumnat
subject: "Tècniques d'informació geogràfica i turística"
subject_code: "21224102"
---

Els indicadors del llibre descriuen els municipis; QGIS permet relacionar-los amb la seva localització i representar-ne els contrastos. Aquest primer recorregut prepara un projecte de capes locals, comprova la unió amb la taula estadística i construeix un mapa de referència i una coropleta.

Cal treballar el territori assignat. Les captures d'aquesta guia mostren Tarragonès–Vila-seca, el cas docent, i no substitueixen les dades dels altres equips. El [capítol d'integració SIG](https://geourv.github.io/tigit/ca/chapters/integracio-sig/) explica les relacions entre capes i taules; el de [cartografia temàtica](https://geourv.github.io/tigit/ca/chapters/cartografia-tematica/) desenvolupa la representació dels indicadors.

>>>>> - Distingir projecte QGIS, dades i representació.
>>>>> - Comprovar CRS, unitat territorial, tipus i claus abans d'unir.
>>>>> - Construir una base de referència i una coropleta amb decisions explícites.
>>>>> - Conservar projectes, recursos, controls i captures que permetin reprendre el procés.

# Selecció del treball i organització de l'equip

El professor comunica a classe els apartats obligatoris i els enumera a Moodle. Els blocs són **B1, base espacial; B2, transferència i unió; B3, referència i coropleta; i B4, persistència i continuïtat**. La guia i els projectes d'exemple poden oferir més variants que les seleccionades per avaluar.

Es mantenen l'equip i el parell comarca–municipi assignats. Convé alternar qui opera QGIS, qui comprova taules i qui documenta; cada membre ha de poder explicar una font, la clau d'unió i una decisió de representació. La continuïtat exigeix conservar taula, dades, projectes i controls reobribles. Si s'acota un pas necessari, el professorat ha d'indicar com es completarà o quina preparació identificada del mateix territori s'utilitzarà.

Amb QGIS instal·lat, llibre revisat i base territorial disponible, s'estimen **180–240 minuts d'aula i 90–150 de treball autònom per estudiant treballant en equip**. Són estimacions no mesurades amb alumnat i es poden repartir en diversos blocs. No inclouen instal·lació, preparació de geometries inexistents, incidències de fonts ni totes les ampliacions. Moodle fixa sessions i terminis.

# Material i projecte

Cal disposar de la base territorial del territori assignat i de la taula d'indicadors validada. Si el professorat facilita un paquet inicial, el seu inventari ha d'identificar projecte, dades i dependències. Cal extreure'l completament i conservar-ne l'estructura; el fitxer `.qgz` no incorpora automàticament les capes que consulta.

| Element | Funció i comprovació |
| --- | --- |
| GeoPackage | Pot contenir diverses capes; cal identificar la subcapa, el CRS, els camps i el nombre d'entitats. |
| CSV i, quan es faciliti, CSVT | Taula sense geometria i declaració de tipus; la clau municipal ha de conservar-se com a text. |
| Projecte QGIS | Organització, estils, etiquetes, temes i referències a les dades. |
| Registre de treball | Fonts, versions, períodes, correspondències, decisions i incidències. |

Table: Components del primer projecte cartogràfic.

El projecte es desa dins de `qgis`, amb rutes relatives quan el material sigui local i portable. En la demostració s'utilitza ETRS89 / UTM 31N, `EPSG:25831`. El CRS del projecte i el de les capes s'han de comprovar per separat; que una capa aparegui a la pantalla no acredita per si sol que estigui ben georeferenciada.

# Carregar i inspeccionar la base

1. Cal obrir el gestor de fonts o l'Explorador de QGIS i identificar les subcapes del GeoPackage.
2. Es carrega la capa municipal i es comproven el tipus de geometria, el CRS, el codi territorial i la cobertura.
3. S'afegeixen el contorn comarcal i el detall del municipi de referència, si estan disponibles i són pertinents a l'escala de treball.
4. Es revisen l'ordre i la visibilitat al panell de capes; una capa carregada pot estar amagada o tapada per una altra.
5. Es desa una primera fita i es torna a obrir per comprovar que es localitzen totes les dades.

![Finestra real de QGIS amb la base municipal del Tarragonès i el panell de capes destacat](sandbox/practiques/tigit-04-qgis-mapes/run03/captures/tigit-04-mapa-base/mapa-base.png "Mapa de referència de la demostració. La captura real mostra les capes locals, les etiquetes i el CRS del projecte; el requadre identifica el panell de capes. QGIS 3.44.11, interfície catalana.")

La geometria de la demostració prové de l'ICGC, edició del 20 de gener de 2026, mentre les estadístiques corresponen a 2021. Aquesta diferència s'ha de documentar i valorar. Una coincidència de codis no demostra tota sola l'equivalència territorial entre dues edicions.

# Incorporar els indicadors

La taula de transferència ha de ser rectangular, amb una fila per municipi, noms de camp estables i tipus explícits. Cal exportar-la des del llibre revisat i contrastar que els valors i els codis es conserven. Els percentatges calculats sobre 100 no s'han de tornar a normalitzar.

En la demostració, la clau de la geometria és `CODIMUNI` i la del CSV és `mun_code`. Els noms efectius del projecte propi poden ser diferents, però han d'identificar el mateix sistema de codis i la mateixa unitat territorial. Abans de la unió cal comprovar longitud, tipus textual, unicitat i cobertura als dos costats.

La unió es configura amb les claus, mai amb l'ordre de les files. Després cal comptar coincidències i absències, revisar que no s'hagin duplicat municipis i contrastar valors de control amb el llibre. Si es materialitza una capa nova per compartir-la, es conserva també la documentació de l'operació; la taula original no s'ha de substituir per una còpia corregida a mà.

# Mapa de referència

El mapa de referència ha de permetre reconèixer el municipi dins de la comarca. Cal establir una jerarquia de contorns, fons i etiquetes, i revisar-la a l'escala de lectura prevista. La geometria generalitzada que funciona per a una comarca no es converteix en cartografia de detall pel fet d'ampliar-la.

Convé conservar un tema amb un nom descriptiu per recuperar les capes i els estils de la vista. Un tema no substitueix el projecte ni fixa per si sol totes les propietats d'un futur marc de composició.

# Coropleta de l'indicador

La primera coropleta utilitza un indicador relatiu amb denominador justificat. En la demostració és `housing_non_main_pct`, el percentatge d'habitatge no principal. Una magnitud absoluta, com el nombre total d'habitatges, demana una decisió de representació diferent.

1. Cal seleccionar la capa amb els indicadors comprovats i obrir el panell d'estils o la simbologia.
2. Es tria el camp, el mètode de classificació, el nombre de classes i una rampa seqüencial adequada.
3. Es comproven els intervals, els nuls i el nombre de municipis de cada classe. La llegenda arrodonida no ha de substituir els límits numèrics originals.
4. Si el professor selecciona la comparació d'una alternativa, es mantenen dades, extensió, mida i rampa perquè només canviï la decisió que s'estudia. Si no és obligatòria, es pot desenvolupar com a ampliació.
5. Es conserva la decisió i la seva justificació al registre del projecte.

Cal contrastar el mètode indicat per la interfície amb els intervals realment conservats. Un nom de capa o de tema no garanteix que el desplegable del mètode estigui configurat com s'espera. La comparació ha de descriure què canvia en la lectura i no atribuir automàticament una causa turística al patró residencial.

# Ampliacions controlades

Una comparació seleccionada com a bàsica es valora només en aquell bloc. Per al 20% cal una aportació pròpia amb pregunta, referència, controls i interpretació; no basta duplicar una capa amb altres colors.

## A1. Comparar mètodes de classificació

La pregunta és quins municipis canvien de classe entre quantils i intervals iguals. Es varia només el mètode; es mantenen indicador, nombre de classes, rampa, extensió i mida de lectura. La referència és la coropleta bàsica validada.

Cal registrar límits, recomptes i codis que canvien de classe. La suma ha de cobrir tots els municipis vàlids i els nuls s'han de distingir dels zeros. La interpretació explica per què canvia la lectura del mapa sense que canviïn els valors. Si no s'observen diferències, cal documentar les dades i les condicions que ho expliquen.

## A2. Comparar nombres de classes

La pregunta és quin detall afegeix passar de tres a cinc classes amb el mateix mètode. Es varia només el nombre de classes; la referència és la classificació bàsica i es mantenen dades, rampa i enquadrament. Amb pocs valors diferents cal acordar una parella admissible, com dues i tres, en lloc de forçar cinc classes.

Es comproven classes efectives, límits, recomptes i municipis als extrems o a les fronteres dels intervals. La interpretació compara llegibilitat i detall i explica per què més classes no donen més precisió a les dades. Les dues alternatives es conserven al projecte i es documenten amb captures o mapes comparables.

# Resultats i continuació

Cal conservar el projecte inicial, el projecte amb unió i la continuació cartogràfica, juntament amb les dades i les dependències. Les captures han de mostrar decisions identificables: capes i CRS, camps de la unió o configuració de la simbologia. No substitueixen els projectes editables ni les comprovacions.

La composició final afegirà, segons la finalitat del mapa, títol, llegenda, fonts, escala i localitzador. Una captura del llenç encara no és aquesta pàgina cartogràfica final. El projecte ha de poder reobrir-se des d'una altra ubicació amb les dades locals disponibles abans de preparar el lliurament.

# Lliurament i qualificació interna

El lliurament prepara els projectes i totes les dependències locals, juntament amb uns apunts breus en PDF sobre fonts, períodes, transferència, unió, simbologia, controls i contribucions de l'equip. Moodle concreta el conjunt, els mapes exportats que calgui adjuntar i el format de tramesa. Cal conservar també el llibre i les fites anteriors; no s'envia un qgz aïllat com si incorporés automàticament les dades.

| Bloc | Màxim | Què es valora |
| --- | ---: | --- |
| Bàsic, 70% | 7 punts | Dades, unió, representació i persistència dels apartats seleccionats. |
| Ampliacions, 20% | 2 punts | Pregunta, comparació controlada i interpretació. |
| Documentació, 10% | 1 punt | Apunts clars, captures significatives, mapes llegibles, atribucions i organització. |

Table: Qualificació interna de la pràctica QGIS sobre 10.

Els màxims no són automàtics. Bàsic i documentació complets poden arribar a 8/10 sense ampliacions. Aquestes no substitueixen obligatoris i acumular capes o fitxers no garanteix punts. Cada aportació tècnica es valora al bàsic o a l'ampliació; el 10% valora comunicació i organització, sense duplicar-la. El 70–20–10 és intern; Moodle concreta el pes global i els requisits de superació d'acord amb la [guia docent de TIGIT, 21224102](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&fitxa_apartat=61&any_academic=2026_27).
