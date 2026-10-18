---
title: "Primers mapes amb QGIS: LLEGIU-ME del professorat"
lang: ca
ref: tigit-practica-04-qgis-docent
content_status: draft
recipient: docent
subject: "Tècniques d'informació geogràfica i turística"
subject_code: "21224102"
---

El primer bloc QGIS connecta els indicadors del llibre amb la geometria municipal i amb una representació cartogràfica defensable. La demostració treballa el Tarragonès i Vila-seca; cada equip manté el seu territori assignat. El professorat de teoria explica unitats, CRS, escala i normalització, mentre el laboratori comprova com es conserven aquestes decisions al projecte.

El material de consulta inclou projectes inicials i resolts, dades locals, captures i exportacions de base. Les lectures i les composicions requereixen criteri docent: un control tècnic correcte no substitueix la revisió de llegenda, escala, etiquetes o interpretació.

# Preparació de la sessió

La sessió introdueix QGIS a primer curs. Es pressuposa QGIS instal·lat, els equips i territoris assignats, el llibre de continuïtat revisat i una base ICGC identificada per al territori de cada equip. No es pressuposa experiència prèvia amb projectes, capes o unions. Cal començar amb una obertura guiada i alternar dins de l'equip qui opera, qui verifica taules i qui documenta.

| Component | Durada orientativa |
| --- | --- |
| Aula, base, unió i primera coropleta | 180–240 min |
| Treball autònom per estudiant, treballant en equip | 90–150 min |
| Preparació docent | 45–60 min |

Table: Estimació de la pràctica 04 amb taula validada i base territorial disponible.

Són estimacions no mesurades amb alumnat. Es poden repartir en tres blocs; no inclouen instal·lació, preparació de geometries inexistents, incidències de fonts ni totes les ampliacions de composició i símbols. Si la taula anterior encara té errors, cal reservar temps per resoldre'ls abans de la unió.

La preparació docent comprova la base de cada territori, el CSV/CSVT, les claus i el CRS. Cal obrir una còpia del projecte inicial i dels projectes resolts del Tarragonès, revisar els controls i provar la reobertura amb totes les dependències. Les captures de la guia mostren QGIS 3.44.11; cal identificar a classe qualsevol diferència d'interfície. Disposar del cas resolt no acredita que ja estiguin preparats els materials dels altres equips.

| Aturada | Comprovació | Pregunta de discussió |
| --- | --- | --- |
| Base carregada | Subcapa, CRS, codi i cobertura | Què es desa al GeoPackage i què es desa al projecte? |
| Unió executada | Coincidències, absències, files i tres valors | Com es detecta una clau duplicada si el mapa sembla correcte? |
| Simbologia | Camp, mètode, límits i recomptes | Un municipi que canvia de color ha canviat de valor? |
| Còpia reoberta | Fonts locals resoltes i estils conservats | Què faltaria si només s'hagués enviat el fitxer qgz? |

Table: Comprovacions que connecten dades, representació i persistència.

Els errors habituals són assignar un CRS per fer coincidir visualment les capes, importar codis com a nombres, unir per nom, dividir una altra vegada un percentatge i confondre el llenç amb una composició final. També cal discutir per què una capa temporal o una ruta personal pot funcionar en un ordinador i fallar en una còpia traslladada.

# Encaix de la qualificació

La [guia docent URV 2026/27 de TIGIT, 21224102](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&fitxa_apartat=61&any_academic=2026_27) assigna un 5% global al conjunt d'activitats TIC d'aula, 30% a presentacions/síntesi, 5% al seguiment, 30% a proves mixtes i 30% a proves pràctiques. El 70–20–10 d'aquesta Tasca distribueix els seus 10 punts interns. No modifica aquells pesos ni implica que cada pràctica valgui un 5% del curs.

El professorat concreta a Moodle el pes i els obligatoris respectant els mínims de la guia. La selecció ha de conservar la unió, el projecte i les dades necessàries per continuar la cartografia i la síntesi. Els projectes de consulta ofereixen més variants que les que cal avaluar en aquest primer contacte. La lectura de població i habitatge no acredita per si sola la distribució de l'oferta turística.

# Preparar Moodle

1. Crear o configurar una **Tasca** anomenada **TIGIT 04 · Unió de dades i primers mapes amb QGIS**.
2. Copiar a **Descripció** l'enunciat següent, de «Pregunta i punt de partida» fins al final de «Qualificació». Enumerar els codis B obligatoris indicats a classe i el camp que es representarà; declarar si alguna comparació de classificació forma part del bàsic.
3. Preservar la cadena llibre–CSV–unió–projecte. Si s'acota un pas necessari, indicar quina preparació identificada del mateix territori permet reprendre'l; no substituir el territori assignat pel cas resolt.
4. Adjuntar a **Fitxers addicionals** el PDF d'alumnat «Primers mapes amb QGIS» i la base geogràfica inicial verificada per als equips, amb metadades i auxiliars necessaris. Cada equip aporta la seva taula validada. Un paquet o un projecte d'exemple només s'ofereix després de comprovar-ne l'inventari i les dependències.
5. Conservar per a la preparació docent el PDF del professorat, el projecte inicial del Tarragonès, els projectes d'unió/referència/temàtic, les dades, les captures i els controls. Si es comparteix un resolt, etiquetar-lo com a exemple de Tarragonès–Vila-seca.
6. Revisar grups, tramesa completa, dates, formats i mida; configurar màxim 10 amb criteris de 7, 2 i 1 i el pes global corresponent. El lliurament ha de poder reobrir-se, no limitar-se a captures.
7. Comprovar la **vista d'estudiant**, els adjunts, el territori, els obligatoris i la instrucció de conservar totes les dependències locals.

## Enunciat per copiar a la descripció

### Pregunta i punt de partida

On se situen els contrastos municipals que s'han calculat al llibre i com es poden representar sense alterar-ne el significat? Cada equip manté el seu parell comarca–municipi, el llibre 03 i els indicadors validats. Cal disposar de la base territorial ICGC identificada per al seu àmbit i preparar una taula de transferència amb codi municipal textual, components i indicador. Tarragonès–Vila-seca és la demostració, no la resposta dels altres equips.

### Treball bàsic —70%

El professor selecciona a classe els apartats obligatoris i els enumera en aquesta Tasca. El recorregut disponible és:

- **B1. Base espacial:** identificar GeoPackage, subcapes, geometria, CRS, codis i cobertura; desar una primera fita del projecte amb dades locals.
- **B2. Transferència i unió:** exportar la taula des del llibre, comprovar tipus i unicitat de claus, unir per codi i contrastar recompte i valors. No unir per ordre de files.
- **B3. Referència i coropleta:** representar el municipi dins de la comarca i l'indicador relatiu seleccionat, amb camp, mètode, classes i rampa justificats. Un percentatge calculat sobre 100 no es torna a normalitzar.
- **B4. Persistència i continuïtat:** conservar fites de projecte, dades, taules i controls; reobrir una còpia en una altra carpeta i verificar fonts i estils. Aquesta base alimentarà les composicions i la síntesi posteriors.

### Ampliacions —20%

Es pot estudiar una d'aquestes preguntes si la comparació no forma part dels obligatoris:

- **A1. Efecte del mètode de classificació.** Pregunta: quins municipis canvien de classe amb quantils o intervals iguals? Es varia només el mètode, mantenint dada, nombre de classes, rampa, extensió i mida. La referència és la coropleta bàsica validada. Cal registrar límits, recomptes i codis que canvien, comprovar que la suma cobreix tots els municipis vàlids i separar nuls. La interpretació explica per què canvia la lectura del mapa sense que canviïn els valors.
- **A2. Efecte del nombre de classes.** Pregunta: quin detall afegeix passar de tres a cinc classes amb el mateix mètode? Es varia només el nombre de classes i es manté la resta. La referència és la classificació bàsica; si hi ha pocs valors diferents, s'acorda una parella admissible, com dues i tres. Cal comprovar classes efectives, límits, recomptes i casos de frontera. La interpretació valora llegibilitat i detall; més classes no signifiquen més precisió de les dades.

Una comparació ja seleccionada al bàsic es puntua una sola vegada. Una ampliació petita amb controls i interpretació pot justificar el bloc; acumular mapes amb colors diferents no garanteix punts.

### Productes, controls i documentació

Cal conservar el llibre, el CSV/CSVT, les dades geogràfiques i les fites de projecte dins de l'estructura de treball. El lliurament prepara els projectes amb totes les dependències locals i uns apunts breus en PDF amb fonts, períodes, unió, simbologia, controls i contribucions de l'equip. Les captures mostren configuracions i resultats identificables; els mapes exportats que es demanin han d'incloure els elements de lectura necessaris. Moodle concreta el conjunt i el format de tramesa.

La comprovació exigeix una clau única, coincidències i absències documentades, tres valors contrastats amb el llibre i reobertura de la còpia. S'han de separar el CRS de la capa i el del projecte i declarar les diferències temporals. Una captura del llenç no substitueix una composició ni un projecte editable; el patró d'habitatge no principal no identifica automàticament activitat turística.

### Qualificació

**Bàsic: fins a 7 punts**, per dades, unió, representació i persistència dels apartats seleccionats. **Ampliacions: fins a 2 punts**, per pregunta, comparació controlada i interpretació. **Documentació: fins a 1 punt**, per apunts clars, captures significatives, mapes llegibles, atribucions i organització. Els màxims no són automàtics i el nombre de capes o fitxers no dona punts per si sol.

La documentació suma també sense ampliacions: bàsic i documentació complets poden arribar a 8/10. La correcció tècnica es valora al bàsic o a l'ampliació; la comunicació i l'organització es valoren al 10%, sense duplicar la mateixa aportació. Les ampliacions no substitueixen els obligatoris. La nota és interna de la Tasca; el pes global i els requisits de superació són els de Moodle i la guia docent.

# Recursos del cas docent

| Recurs | Contingut i control |
| --- | --- |
| Base ICGC local | Municipis del Tarragonès: 22; comarca: 1; detall de Vila-seca: 1; capes complementàries de província i capitals. CRS `EPSG:25831`. |
| Context de Catalunya | 43 comarques a l'edició ICGC conservada. |
| CSV/CSVT d'indicadors | 22 municipis; `mun_code` textual i indicadors numèrics. |
| Resultat de la unió | 22 coincidències, cap absència i geometria municipal conservada en els controls del cas. |
| Punts de símbols | 22 punts interiors, un per municipi. |

Table: Recursos i comprovacions de la demostració.

Les estadístiques són de 2021 i la geometria ICGC és del 20 de gener de 2026. La compatibilitat territorial s'ha de justificar; els recomptes i les claus no són una prova completa d'equivalència temporal. Les dades d'altres comarques s'han de preparar i verificar separadament.

El projecte inicial permet estudiar formats i taules; el projecte amb unió conserva els indicadors relacionats; el de referència treballa contorns i etiquetes; i el temàtic conserva variants de coropleta i símbols. Els noms tècnics de les fites són estables, però no imposen el calendari de classe.

# Conducció de la unió i del mapa base

Cal començar mostrant la diferència entre un GeoPackage, una capa del contenidor i un projecte QGIS. El panell de capes mostra què forma part del projecte; l'Explorador permet consultar recursos i connexions. La demostració ha de comprovar CRS, identificador, camps i cobertura abans de triar una representació.

La geometria municipal utilitza `CODIMUNI`; el CSV utilitza `mun_code`. S'ha de contrastar la unicitat de les dues claus abans d'executar o materialitzar la unió. Vila-seca, Roda de Berà i la Pobla de Mafumet permeten seguir la mateixa dada al llibre, al CSV i a la capa resultant.

| Municipi | Habitatges totals | No principals | Percentatge |
| --- | ---: | ---: | ---: |
| Vila-seca | 17.417 | 8.692 | 49,9053% |
| Roda de Berà | 8.762 | 5.673 | 64,7455% |
| La Pobla de Mafumet | 1.615 | 195 | 12,0743% |

Table: Controls que connecten full de càlcul i capa municipal.

La consulta de percentatges superiors al 50% selecciona sis municipis del cas docent. El percentatge comarcal continua sent la ràtio de sumes, 39,0740%, i no la mitjana dels percentatges. Cap d'aquests valors identifica directament habitatge turístic.

# Coropleta i comprovació de la interfície

La capa `Municipis · unió` representa `housing_non_main_pct` amb cinc classes de quantils i rampa BuGn. Les captures següents mostren el llenç real de QGIS i el detall de la simbologia. El contorn taronja identifica Vila-seca; els colors de la coropleta descriuen el percentatge municipal.

![Coropleta real d'habitatge no principal dels municipis del Tarragonès en QGIS](sandbox/practiques/tigit-04-qgis-mapes/run03/captures/tigit-04-coropleta/coropleta.png "Estat cartogràfic del cas docent: percentatge d'habitatge no principal, 2021, amb geometria ICGC de 2026. És una captura del projecte, no una composició final amb tots els elements de mapa.")

![Widget real de simbologia de QGIS amb el camp, els cinc intervals i el mètode de quantils](sandbox/practiques/tigit-04-qgis-mapes/run03/captures/tigit-04-coropleta/simbologia.png "Detall capturat directament del widget de simbologia. El camp és housing_non_main_pct, la classificació conserva cinc classes i el desplegable mostra el mètode de quantils. QGIS 3.44.11.")

Els límits aproximats són 12,0743; 20,3576; 25,9165; 37,8561; 54,6003 i 64,7455. Els valors exactes es conserven al projecte. Cal comprovar el camp, els límits i el mètode, i no deduir-los només del nom de la capa. A la interfície utilitzada, el mètode apareix com `Equal Count (Quantile)`.

La variant d'intervals iguals es conserva en una altra capa del projecte per comparar-la amb la mateixa extensió, dada i rampa. La comparació ha de considerar recomptes per classe, separació de valors i conseqüències de lectura. No es canvien alhora totes les decisions visuals.

# Temes, símbols i composició

Els temes de referència, localització, unió, coropletes i símbols permeten recuperar estats de capes i estils. Cal comprovar-los després de desar i reobrir el projecte. Els marcs de mapa del dissenyador tenen escala i extensió pròpies; un localitzador no ha d'heretar accidentalment l'extensió del mapa principal.

El projecte també conserva símbols graduats i una variant de mides proporcionals. La variant proporcional de la demostració fixa mides per als valors observats: si canvien les dades, cal recalcular-la i revisar-ne la llegenda. No s'ha de presentar com una escala automàtica adequada per a qualsevol taula nova.

Les composicions de base contenen mapa principal, localitzador, títol i fonts. La llegenda i l'escala gràfica s'han de completar i revisar al dissenyador abans d'acceptar el mapa com a producte final. Les exportacions SVG/PDF són bases editables i no substitueixen aquesta revisió.

# Captures i preparació del paquet

La documentació del procés ha de separar tres evidències: un diàleg configurat, una operació executada amb controls i un resultat mostrat al projecte. La captura d'una configuració d'unió no acredita que la unió hagi funcionat; calen recomptes i contrast de valors. Una captura de mapa tampoc no prova per si sola que totes les dependències es puguin traslladar.

El paquet inicial ha de contenir les dades, el projecte inicial i totes les dependències requerides. El docent pot afegir projectes resolts, controls i exportacions. La selecció s'ha de fer amb els IDs i les dependències verificats pel productor, mantenint fonts tipogràfiques i auxiliars de formats com Shapefile. Un sol `.qgz` sense les dades no és un paquet reproduïble.

Abans del lliurament cal revisar el territori, el contingut de cada destinatari, la lectura, els projectes reoberts i la composició final. Les captures d'aquesta guia documenten estats reals de la demostració; l'acceptació docent i la distribució dels materials als equips són decisions posteriors.
