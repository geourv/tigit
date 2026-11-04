# Primer procés de mapes QGIS — pràctica 04

Continuació de [TIGIT #14](https://github.com/geourv/tigit/issues/14), autoritzada el 13 d'octubre de 2026, amb les fonts reubicades, run05 i captures run03 el dia 14, i guies docents/Moodle 0.2.0 el dia 15. L'autor n'ha revisat i autoritzat el lliurament com a versió de treball el dia 18, mantenint `draft` i ESBORRANY; l'últim apartat identifica els rebuts i la còpia lliurada. Aquest és context tècnic.

## Abast

El primer lot reprèn la base territorial i els indicadors per explicar projecte/capes, CRS, unió per clau, mapa de referència i coropleta. S'han preparat dues lectures amb el format privat d'unaltraweb i tres captures reals amb unaltracaptura-qgis: mapa de referència, llenç de la coropleta i detall del panell de simbologia. Els PDFs vigents 0.2.0 tenen set pàgines d'alumnat i nou de professorat; s'enllacen a [l'índex local](../practiques/README.md).

Tarragonès–Vila-seca continua sent el cas docent. Les captures i els productes conservats d'aquest cas no es convertiran en les dades dels territoris assignats als equips sense preparar i verificar els recursos equivalents.

## Recursos i procedència

El catàleg consultat amb `list_teaching_resources` i els recursos `qgis://teaching/resources` i `qgis://teaching/data-preparation` retorna zero entrades/plans en aquesta instal·lació. No s'han atribuït al catàleg fitxers inexistents ni s'han iniciat descàrregues. Es reutilitzen les dades locals ICGC/Idescat i els projectes ja conservats.

La primera prova de captures (`run01`) es va fer amb aquesta base històrica, que es conserva intacta:

- `sandbox/practiques/tigit-projecte-territorial/0.1.0/ca/run03-cartography/bundle.json`, segell `9ca86916de5918805e23107ca93a3f48537c289c3dfa7ebe72569da95d5429ed`.
- Perfil `qgis-practice-v2`; descriptor `payload/practice.json`, SHA `8118fae9bc06f6d9eb8d59c7e8027dbcad97e4f3fe28e22143f0f44a6ab7ab25`.
- Productor històric `unaltracaptura-qgis 0.6.0rc2`, revisió `sha256:5922d3dc411c14c7c3c2d9257a78b4d42f42fb1aae8451bcf245ca44a0e91992`. El checker i el capturador actuals són 0.6.0; això no reetiqueta el productor dels originals.
- Engine QGIS fixat: `sha256:1003721d96abe9607d8337b36851f9b29f84c2f8f92b377d1a73ff03c9d15cd2`, ja preparat. Locale `ca_ES`, xarxa desactivada i pull prohibit a les receptes.

La inspecció de la interfície d'aquella prova va mostrar una discrepància: la capa conservava intervals de quantils, però el selector del mètode indicava desviació estàndard. La font versionada `activities/qgis-territorial.py` ja contenia la correcció, encara no materialitzada en aquell bundle. S'ha executat aquesta font amb el productor natiu en una destinació nova, sense editar el model ni els originals rc2.

## Execució nativa vigent

La CLI persistent 0.6.0 ha executat `practice-run` amb aquestes entrades i destinació, relatives al consumidor:

- Request font: `practiques/tigit-projecte-territorial/activity-qgis.json`, SHA `6154464971d829dc1396230f9064482f9f1ffe003ee96125e67c07ded7374aaf`.
- Model font: `practiques/tigit-projecte-territorial/activities/qgis-territorial.py`, SHA `dcd4240755b7780dc18b0255c3e0c1c825683abe70217f1bdb020cfd695c620c`.
- Request lliurat a `practice-run`: `sandbox/practiques/tigit-projecte-territorial/entrades-qgis/2026-10-14-01/activity-qgis.json`, còpia byte a byte amb els quatre inputs fixats pel manifest de recursos.
- Destinació: `sandbox/practiques/tigit-projecte-territorial/0.1.0/ca/run05-contract-20261014/`.
- Bundle: `bundle.json`, SHA `8719b839d1071be858deed94fcce0e32e61f01f575d29c2b4f5e2d0ce5704eac`.
- Descriptor: `payload/practice.json`, SHA `3105ec5a8111558c7cfeb20811fe8f811536926b685c4b146fa4032755330d04`.
- Job: `practice-70a6209a5cab4b46911e35f94696989a`.
- Productor: `unaltracaptura-qgis 0.6.0`, revisió `sha256:4dcd2c40bca4836a202c0c5cc400553b0f134925023b7300e0c0ff2fff1d8492`.

L'execució ha retornat `ok: true`: 123 entrades a `bundle.files`, 10 projectes, 10 grups de captures natives, 8 exportacions i 40 controls. A diferència de la relectura dels reports històrics, aquesta és una execució nova del procés QGIS. `payload/controls/offline-reopen.json` acredita reobertura dels deu projectes amb xarxa `none`, `ok: true` i `container_absence_verified: true`; el seu SHA és `99a87198e2597f3182bd1a4848ef31a6c2e4b2d377674417213b0f7c151cb17a`.

Les receptes vigents llegeixen `reference-project` i `resolved-project` d'aquest bundle nou. Els seus SHA són, respectivament, `a132bf2d1d0f01d4d8fc26ff28c5254c698e8ae93bdc2a1bc808ecabbf8c8d42` i `00ae4c3bb7b102161814f264c24ee0d94939a9504e1e13b80b449526088b39de`. Els checkpoints i les captures es desen fora de l'arbre segellat. Run04 queda conservat amb el segell `13f78819fd87cc8772ce54322d07434445f4397ca12e835b810f9b0667023fa0`.

## Fonts de captura

- Configuració: `.unaltracaptura-qgis-practice-04.yml`, a l'arrel del consumidor.
- Recepta de mapa de referència: `practiques/tigit-04-qgis-mapes/captures/mapa-base.yml`.
- Recepta de coropleta: `practiques/tigit-04-qgis-mapes/captures/coropleta.yml`.
- Destinació vigent: `sandbox/practiques/tigit-04-qgis-mapes/run03/`; `run01/` i `run02/` queden com a proves anteriors.

S'ha capturat la finestra real QGIS amb panell de capes i barra d'estat. La vista de referència incorpora una única etiqueta de regió sobre el panell de capes; la coropleta mostra la finestra completa i el detall s'obté directament del widget `QgsRendererPropsDialogBase`. Es conserven originals, representacions i manifests del capturador. La interfície vigent mostra el camp `housing_non_main_pct`, cinc classes, rampa BuGn i mètode `Equal Count (Quantile)`.

El productor resol les declaracions de projecte des de l'arrel de configuració i refusa `..` en projectes/fonts. Per això l'autor ha acceptat moure la configuració nova a l'arrel, amb nom ocult per a Jekyll. La configuració QGIS antiga es conserva. Les claus completes són `tigit-04-mapa-base.mapa-base`, `tigit-04-coropleta.coropleta` i `tigit-04-coropleta.simbologia`; les operacions QGIS es fan serialment perquè la instància admet una sola operació activa. El render de `simbologia` ha produït les dues captures de la seva recepta.

Captures incorporades a les lectures, sota `sandbox/practiques/tigit-04-qgis-mapes/run03/captures/`:

| Path | SHA-256 del PNG |
| --- | --- |
| `tigit-04-mapa-base/mapa-base.png` | `5c8a802c78fd78e06b47765f65666899dcc09ca53ed3d79b3057284d4a23788c` |
| `tigit-04-coropleta/coropleta.png` | `b91932abf0347fcbd8b95d5af5288dfec7cf5dfb7ddbb0d829b361ab49ad8c0a` |
| `tigit-04-coropleta/simbologia.png` | `d0536c0fdd7c84d08df9e343072309b210815327a2f0c945bbcec0ef1baf584a` |

Les tres imatges passen `image_background_check` seleccionades directament: `opaque`, `alpha_min: 255`, sense avisos. El checker de referències sobre la lectura docent resolia el path des de la carpeta Markdown i retornava `unverifiable`; el productor de PDF privat el resol des de l'arrel del consumidor i n'ha verificat el binding i el hash. És un límit de coherència dels dos inspectors, no una imatge absent al PDF. S'han revisat visualment mapa, camp, intervals, mètode i absència de dades personals visibles a les captures.

## Selecció de dades per als futurs paquets

Les seleccions s'han verificat amb `practice-check --select` sobre el segell de run04; totes retornen `ok: true`. En run05 s'ha tornat a comprovar la selecció conjunta dels cinc IDs, amb 17 fitxers i `ok: true`; els recomptes individuals de la taula corresponen a la comprovació conservada de run04. El checker comprova el bundle i els controls enregistrats; aquestes crides no tornen a executar els models.

| Selecció | IDs demanats | Fitxers amb dependències |
| --- | --- | ---: |
| Inicial del cas docent | `initial-project` | 11 |
| Consulta cartogràfica docent | `reference-project`, `resolved-project`, `context-svg`, `choropleth-svg` | 9 |
| Conjunt de les dues seleccions | Els cinc IDs anteriors | 17 |

La selecció inicial inclou `counties-context`, `font-regular`, `indicators-table`, `indicators-types`, `initial-project`, `municipalities-cpg`, `municipalities-dbf`, `municipalities-prj`, `municipalities-shp`, `municipalities-shx` i `territorial-base`. Conserva CSV/CSVT i tots els auxiliars del Shapefile, sense projectes resolts. Les dades continuen sent les de Tarragonès–Vila-seca: és una selecció tècnica del cas docent, no un paquet ja adaptat a cada equip.

La consulta docent inclou `choropleth-svg`, `context-svg`, `counties-context`, `font-regular`, `joined-data`, `reference-project`, `resolved-project`, `symbol-points` i `territorial-base`. Els hashes i les dependències exactes queden al descriptor segellat. Els 17 fitxers de la unió no inclouen automàticament lectures, controls, captures o fonts de reproducció: són la clausura dels cinc productes seleccionats, no el recompte d'un futur ZIP complet.

Les lectures encara no estan aprovades. Per tant, una selecció de productes verificada no equival a una edició ZIP final. El compositor Web s'utilitzarà quan el contingut i les seleccions estiguin confirmats; no es fabricaran hashes d'aprovació ni es canviarà `content_status` per superar-ne el gate.

## Lot històric de lectures i PDFs 0.1.0

Les fonts `practiques/tigit-04-qgis-mapes/ca/{alumnat,docent}/LLEGIU-ME.md` passen `prose_check` individualment després del canvi de paths a run03. La revisió `line` amb digest `c7b5730cce40b94cef73e5ce54c33703de839a3f8351225aab9f9666224dc778` correspon a la font docent anterior; no s'ha enregistrat una aprovació editorial ni s'ha atribuït aquell digest a la font nova.

`manual_practice_pdf_build` ha produït els dos PDFs nous amb el worker immutable `sha256:618163d3f924439792b2306617bd9612f566c5881166102fa544b4e782d569fa`, `state: built` i `publishes: false`. S'han obert el PDF docent nou i les captures; el PDF d'alumnat és byte-idèntic al que ja s'havia revisat. La guia docent manté l'ordre dels intervals que evita una pàgina gairebé buida. Els dos PDFs són A4 apaïsats de cinc pàgines amb peu ESBORRANY.

| Destinatari | SHA font | SHA PDF | SHA receipt |
| --- | --- | --- | --- |
| Alumnat | `eb54d253c8c194fcb5dfca54546e099516b9d2b8bcdc74fd7959fd1f78647cc7` | `cd1cf62fa372c861492241a80fb950dccfe9597372522c33e32bd82f57a10e4c` | `914781ee99aa0d648ed0f59b9fa6ddf492e412d1011bcc7256cd4b4dc31f5290` |
| Professorat | `d643a00c7ccc6e1827c0b2f39d2a39b0139aa4ffec2620b310cbe19e09541ac4` | `a7d5c4e8a8ee95a7723de68cd76100234ee2ce9671cedb4dea62121f2c4ec98f` | `ac3638590c732166e98842ad2f43d9ee2c6256f97fdc5ec7be99ad48bd6f3425` |

Ubicacions d'aquest lot històric:

- `sandbox/practiques/tigit-04-qgis-mapes/lectura-0.1.0-ca-alumnat-migracio-20261014-01/outputs/LLEGIU-ME.pdf`
- `sandbox/practiques/tigit-04-qgis-mapes/lectura-0.1.0-ca-docent-migracio-20261014-01/outputs/LLEGIU-ME.pdf`

La retirada del mapping privat de llegat ha canviat `_config.yml`, que és un input dels PDFs. Per això s'han generat aquests jobs nous encara que les fonts 04 i els bytes PDF siguin idèntics. Els jobs `contract-20261014-01` conserven els seus rebuts anteriors; no s'han sobreescrit. QGIS i les captures no s'han repetit per aquest canvi de metadades.

S'han contrastat els 25/26 artefactes i els 5/6 inputs actuals dels dos receipts. Els logs vigents no contenen `Overfull`, errors LaTeX ni caràcters perduts; mantenen avisos de plantilla sobre codificació TU/T1 i configuracions de captions no utilitzades. Les execucions docents 01/02 es conserven com a proves de maquetació anteriors.

## Comprovació històrica després del reinici del 13 d'octubre

La interrupció va afectar una consulta readonly `project_status`, després de construir i comprovar els PDFs. La instància QGIS nova, `6707be66-18b8-4c46-a67c-ffa8b4359c21`, ha retornat versió 0.6.0, binding al checkout TIGIT, `disk_drift: false`, imatges fixades coincidents i cap operació ni worker actiu de la seva sessió.

Les consultes repetides de mapa base i simbologia retornen `state: fresh`, `action: reuse`. Els fingerprints són `6454890375fe4699af5997377a391a7c977334008de9aa8f91db28ac880e0a44` i `d96f349e940d086d2439e1036ae44aa74aebaeeea298a29dd801bc92b2842ada`. La comprovació del bundle i la selecció conjunta de 17 fitxers també passen després del reinici. No ha calgut repetir els renders.

Els vuit PDFs de les pràctiques 01–04 d'aquella observació coincidien amb els hashes anteriors a la interrupció: 197 artefactes i 36 referències d'entrada verificats contra els receipts. `opencode.json` tenia SHA `43599ff9746f44200c729febab9dbc1fdeda7b220005f657cbf31f46472274a3`. La sessió exposava QGIS, Dia i Vega, però no les eines/recursos d'unaltraweb. La reparació del 14 d'octubre, els renders nous de 04 i el timeout posterior de preview són documentats a `context/practice-migration.md`; aquest apartat conserva l'evidència històrica, no descriu la connexió actual.

## Límits i següent decisió

Les estadístiques de 2021 i la geometria ICGC de 2026 encara exigeixen justificació de compatibilitat territorial. La densitat conserva C07/C14 per la superfície publicada el 2025. Els controls tècnics no concedeixen aprovació a aquestes comparacions.

Les exportacions cartogràfiques són bases editables: la llegenda i l'escala gràfica requereixen acabat i revisió. Les mides proporcionals del cas es fixen per als valors observats i s'han de recalcular quan canvien les dades. Aquest lot acredita les tres captures descrites, no tota la interacció amb diàlegs d'unió, propietats o dissenyador. La inspecció dels checkpoints natius de run05 mostra algunes taules/panells estrets i camps retallats; no s'han declarat tots deu grups natius aprovats visualment.

`run02-core` i `run03-cartography` han tornat a passar el verificador readonly amb els segells originals `78d8a824ec96119a105ffdcc79b478fa626fb3304ec6eba6a4f60d882a6f6e19` i `9ca86916de5918805e23107ca93a3f48537c289c3dfa7ebe72569da95d5429ed`. El seu productor continua sent rc2 i els seus 40 controls són evidència enregistrada, no una execució nova en aquelles carpetes.

Falten revisió de l'autor, selecció final per destinatari i composició dels paquets segons el contracte natiu. Tot el material nou segueix `draft`, amb outputs ignorats i sense commit, publicació ni ZIP nou.

## Continuació docent conservada del pla anterior

El pla històric de TIGIT #12 es conserva íntegrament al commit `715944fcbf5463e6dd48ade7696a251c94e8c2fd` i a l'arxiu de llegat identificat a `context/practice-migration.md`. La migració retira els documents antics de l'arbre actiu, però manté aquestes decisions per a la continuació:

| Bloc | Evidència actual o treball pendent |
| --- | --- |
| Projecte, formats i CRS | Base GeoPackage, Shapefile amb auxiliars i projectes segellats; la lectura 04 tracta els primers passos. |
| Atributs, unió i comparació | CSV/CSVT, unió i controls de 22 municipis; queda ampliar la demostració llegible dels diàlegs i consultes. |
| Mapa de referència i etiquetes | Projecte de referència i captura propis; les col·lisions i prioritats a altres escales requereixen revisió. |
| Coropletes comparables | Quantils, intervals iguals i control de camp/classes; cal continuar la comparació interpretativa mantenint les altres decisions constants. |
| Símbols graduats i proporcionals | Projectes/exports de base disponibles; la variant proporcional usa mides fixades pels valors observats, i l'assistent GUI continua pendent. |
| Temes i composicions | Temes i dos marcs editables conservats; llegenda, escala gràfica i captures del dissenyador necessiten acabat. |
| Serveis ICGC | Recorregut en línia separat de la base portable; no s'han acreditat captures, descàrregues o reobertura del servei al runtime. |
| Síntesi SVG | Plantilla A3 editable disponible; infografia emplenada, captures GUI d'Inkscape i selecció final de peces pendents. |

La proposta anterior de tres laboratoris substancials després de la teoria —projecte/dades/relacions, cartografia/composició i síntesi SVG— continua sent una proposta, no capítols ja creats. La teoria ha de mantenir les explicacions i remetre al procediment sense duplicar-lo íntegrament. Els prefixos tècnics de les fites es conserven: 01 → 02 → 03 → 07 → 05 per als llibres, i 04/05/06/08 per als projectes cartogràfics. No defineixen un calendari de Moodle.

El cas de 2021 no cobreix encara tota l'oferta turística municipal requerida per la guia docent. Els allotjaments convencionals de Vila-seca, procedents de `t2h3-cgys`, són una base de geocodificació, no una taula comparable per als 22 municipis. El registre mesura oferta inscrita, no ocupació o pernoctacions. Els 17 centres docents de Vila-seca i els 183 del Tarragonès, de `kvmv-ahh4`, permeten un exercici XY posterior amb EPSG:25831 i EPSG:4326, separat temporalment dels indicadors censals.

El pla conserva les consultes històriques del 9 d'octubre als serveis `https://geoserveis.icgc.cat/servei/catalunya/mapa-base/wms` i `https://geoserveis.icgc.cat/servei/catalunya/divisions-administratives/wfs`: capacitats WMS 1.1.1 i WFS 2.0.0 anunciades; `DescribeFeatureType` va fallar i no es van descarregar entitats. Open ICGC anunciava 1.2.3 al catàleg, però no s'ha acreditat la versió instal·lada. Aquestes observacions no són una prova nova de compatibilitat del plugin ni autoritzen a afegir una dependència remota al projecte offline.

La plantilla actual `practiques/tigit-projecte-territorial/templates/infografia-a3.svg` conserva A3 vertical, marges de 15 mm, sis columnes de 39,5 mm, separacions de 6 mm i vuit capes. El fons de paper és `#fffdf8`; els camps són per emplenar, no resultats analítics. La comprovació històrica d'Inkscape correspon a un render CLI, no a una captura GUI. La síntesi ha de reutilitzar dues o tres peces complementàries, conservar proporcions, fonts i crèdits, i redissenyar-se si canvia a A4. La base tècnica i els controls de fitxer no substitueixen la revisió de l'argument territorial.

## Guia docent, Moodle i revisió 0.2.0 del 15 d'octubre

La [reserva del 15 d'octubre](https://github.com/geourv/tigit/issues/14#issuecomment-6200474177) completa les guies per a primer de Gestió en Turisme i Hoteleria, TIGIT 21224102. La 04 incorpora preparació, aturades de control, errors habituals, «Preparar Moodle» i l'enunciat autònom de la Tasca. La lectura d'alumnat comparteix els quatre apartats B, les ampliacions, la selecció comunicada a classe/Moodle, els productes i la qualificació interna 7/2/1. La guia oficial 2026/27 es cita i es diferencia del 70–20–10 intern: els pesos globals i els requisits de superació no es redefineixen.

L'estimació és de 180–240 minuts d'aula, 90–150 de treball autònom per estudiant en equip i 45–60 de preparació docent. Pressuposa QGIS instal·lat, taula validada i base geogràfica del territori disponible; exclou instal·lació, preparació de geometries inexistents i el desenvolupament de totes les variants avançades. Són estimacions no mesurades amb alumnat. Les aturades comproven base/CRS, claus/unió, classificació i reobertura de la còpia.

Les dues ampliacions proposen comparar quantils amb intervals iguals, o canviar només el nombre de classes. Es mantenen camp, dades, extensió, dimensions i altres decisions, i es registren límits, recomptes, nuls i municipis que canvien de classe. La interpretació explica el canvi de lectura sense atribuir-lo a un canvi de valors. Una comparació seleccionada com a bàsica es puntua només al 70%; la documentació pot completar 8/10 sense ampliacions.

La preparació de Moodle identifica el PDF d'alumnat i la base inicial verificada per a cada equip, amb la taula pròpia i les dependències locals. Els projectes resolts, captures i controls serveixen per preparar la demostració docent; Tarragonès–Vila-seca continua sent un exemple. La publicació efectiva de la Tasca i dels adjunts és una operació posterior del professorat.

Ubicacions de la revisió del dia 15, cadascuna amb `receipt.json` al directori del job:

- `sandbox/practiques/tigit-04-qgis-mapes/lectura-0.2.0-ca-alumnat-moodle-20261015-02/outputs/LLEGIU-ME.pdf`
- `sandbox/practiques/tigit-04-qgis-mapes/lectura-0.2.0-ca-docent-moodle-20261015-01/outputs/LLEGIU-ME.pdf`

| Destinatari | Pàgines | SHA font | SHA PDF | SHA receipt |
| --- | ---: | --- | --- | --- |
| Alumnat | 7 | `6bdc30fa7f365f9b3c769456e6efd60b59ad8740475690945f4d3732aa5538fd` | `c72ffea82b9a02420de03eb1621dac363b7ba2c03d922292c2346608e5580357` | `9ffb78906fb9c467e5be3c3416d98919007b75f9adb13e6ee4b136f7cac9b9e9` |
| Professorat | 9 | `1e6dd9fc552fa11e6a4e5b6f2289b36c0e4ddd65dfa32889868bee67bf46b951` | `e5049e496e9aa04171b383b05d8724908f3cb8ef9cfe82dc65026f3afa179ffd` | `3dba206eb16d1d777e87d7e91d53a86aa9b1aea49d7895a4293a749b09cb8b21` |

Totes dues fonts passen `prose_check` amb cobertura real. La preparació de revisió `structure` del docent té digest `f82a7cf3581bd92700b0766700d51d26245bcfcccef28baf575ad63f16492332`, vinculada al SHA de font de la taula; no s'ha enregistrat aprovació. El worker PDF és el mateix immutable del lot anterior, amb `state: built` i `publishes: false`.

La verificació readonly comprova 51 artefactes i 11 referències d'entrada entre els dos jobs, incloses les tres captures retingudes de run03. Els PDFs són A4 apaïsats amb ESBORRANY a totes les pàgines, sense Overfull, errors LaTeX ni caràcters perduts, i amb totes les paraules extretes dins de la pàgina. S'han inspeccionat les pàgines 3–5 del docent i la darrera d'alumnat; compactar la font d'alumnat va evitar una pàgina gairebé buida i va donar lloc al run02.

La revisió 0.2.0 reutilitza el bundle run05 i les captures run03; no és una nova execució GIS. Els lots PDF 0.1.0 i els intents de maquetació 0.2.0 anteriors queden conservats com a històrics. Les dependències de dades per equip, els límits temporals, l'acabat cartogràfic i la revisió de l'autor continuen oberts.

## Lliurament de treball autoritzat el 18 d'octubre

L'autor ha revisat i autoritzat la publicació del manual i el lliurament dels PDF de treball, mantenint ESBORRANY; [constància de l'autorització](https://github.com/geourv/tigit/issues/14#issuecomment-6253802016). Els dos jobs vigents usen **`pages-20261018-02`**, amb fonts, pàgines i bytes PDF idèntics als de la taula del dia 15. Rebut d'alumnat: `4a3fd368ee274c3c259f92798bebf0ff8fceed2088bac59c9e6ce138ce3c0704`; rebut docent: `bd8a8815a9f059baf2dba69387a960b8fe701bc7f5a0efafaa2167117170bfd8`. Estan vinculats a la configuració final indicada a l'auditoria de fulls.

La còpia íntegra del bundle és a `sandbox/practiques/moodle-2026-10-18/PROFESSORAT/qgis-cas-tarragones/`. Conserva `bundle.json`, el descriptor i els 123 fitxers declarats. `practice-check` 0.6.0 passa sobre l'original i sobre la còpia amb el segell `8719b839d1071be858deed94fcce0e32e61f01f575d29c2b4f5e2d0ce5704eac`, inclosa la selecció dels cinc productes ja identificats. És verificació de l'arbre i dels controls enregistrats, no una nova execució GIS ni una nova reobertura.

El dry-run de composició amb configuració temporal s'ha refusat amb `Edition configuration must be a versioned, non-ignored consumer source`. No s'ha presentat cap ZIP com a edició nativa: la carpeta de lliurament conté les còpies verificades i el bundle íntegre. L'índex `OBRE-AQUI.html` distingeix el PDF d'alumnat, el material docent i les bases dels altres territoris que encara cal preparar. Els límits temporals i d'acabat cartogràfic continuen documentats.
