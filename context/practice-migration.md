# Migració de les pràctiques al contracte d'unaltraweb

Estat del 18 d'octubre de 2026: 104 de les 118 retirades executades, les 24 fonts útils reubicades, eixos corregits i vuit PDFs 0.2.0 amb distribució de treball autoritzada per l'autor. El build i el control editorial de publicació passen; la carpeta Moodle està preparada. Resten els 13 inputs de figures públiques i el ZIP inicial enllaçat pel manual, pendents del contracte compartit per retirar-los. Aquest fitxer és context tècnic; la confirmació humana i les proves de publicació es detallen al final.

## Decisió i reserva

L'autor prefereix adoptar el contracte nou completament: fonts editables a `practiques/`, dades i execucions a `sandbox/practiques/`, i edicions de lliurament a `dist/practiques/<slug>/<versio>/<idioma>/`. El codi, les configuracions i les plantilles útils s'han de moure o adaptar; els empaquetadors, snapshots i instruccions substituïts s'han de retirar de l'arbre actiu.

La reserva exacta és al [comentari de proposta de TIGIT #14](https://github.com/geourv/tigit/issues/14#issuecomment-6154076902): 118 retirades, 32 destinacions noves i 82 paths de revisió. L'autor l'ha acceptada explícitament, amb [constància a la issue](https://github.com/geourv/tigit/issues/14#issuecomment-6154879170). Empremta de la llista ordenada de base/remove/create/update: `1b46615465fdb9230e431836eda9536374a0d7dda43a99b1fe318707dece8af2`.

Checkout únic `/home/benizar/git/tigit`, branca `content/14-spreadsheet-practice-01`, base `715944fcbf5463e6dd48ade7696a251c94e8c2fd`. Aquesta decisió substitueix la instrucció anterior de conservar el llegat actiu sense modificacions. Es manté la revisió humana abans de commit o publicació.

## Dependències inventariades

L'inventari inicial de `_practices/` al commit base conté 113 fitxers versionats, 18.294.454 bytes. Inclou 29 fitxers a data, 27 a dist, 21 a outputs i 24 a scripts, a més de configuració, model QGIS, lectures i plantilla. La reserva també retira el ZIP públic antic, la configuració de probes QGIS antiga i tres documents de planificació/retenció que s'han de consolidar en el nou circuit.

Hi ha 24 fonts de codi/configuració/plantilla identificades per adaptar a `practiques/tigit-projecte-territorial/`. Les dades, els llibres calculats i els ZIPs no es traslladaran a una altra carpeta versionada com si fossin codi.

La migració afecta també figures del manual: 13 inputs de l'arbre antic són dependències de 23 fonts Quarto —22 R i una Python— i d'una visualització Vega. Els locks declaren 32 outputs de Quarto; amb el SVG de Vega són 33 figures. Cal actualitzar les fonts i regenerar els outputs/locks amb el productor corresponent; no s'han d'editar els rebuts a mà ni eliminar les declaracions de dependències per superar els controls.

## Preparació de recursos implementada

S'han creat aquestes fonts dins de la reserva:

- `practiques/tigit-projecte-territorial/recursos.yml`: 20 inputs de dades i un PDF històric d'auditoria, amb paths, mides, SHA-256 i origen Git immutable. El fitxer usa el subconjunt JSON de YAML perquè la preparació només necessiti la biblioteca estàndard de Python.
- `practiques/tigit-projecte-territorial/preparar.py`: operacions `resources`, `check-resources`, `qgis-inputs` i `workbook-inputs`. Prepara les entrades; els llibres els executen els scripts de domini reubicats, i GIS/PDF/edicions continuen a càrrec dels proveïdors.
- `practiques/tigit-projecte-territorial/tests/test_contract.py`: proves de preservació dels inputs, no-sobreescriptura, integritat, inventari complet, symlinks, paths fora de l'arrel, preparació del packet QGIS sense executar el model i confinament dels runs de fulls.

L'origen dels bytes és el commit públic `715944fcbf5463e6dd48ade7696a251c94e8c2fd` del mateix repositori. Inclou tant extractes com derivats ja existents: no és una consulta nova a Idescat/ICGC ni modifica períodes o valors. La procedència estadística original i els límits C07/C14 continuen vigents. Aquest origen immutable permet recuperar els inputs quan la carpeta antiga ja no existeixi al checkout actiu.

El manifest no inclou llibres XLSX ni ZIPs; només conserva com a figura històrica el PDF declarat de l'exercici d'auditoria. La preparació verifica tots els inputs abans d'escriure, exigeix una destinació nova ignorada, refusa paths amb traversal o symlinks, i conserva un intent incomplet en lloc de sobreescriure'l. `resources.json` és un inventari del cas TIGIT, no un bundle ni un rebut atribuït a unaltracaptura/unaltraweb.

Comandes del primer lot, amb el manifest de vint inputs; es conserven com a registre històric, no com a instruccions per reutilitzar el llegat retirat:

```bash
python3 -B -m unittest discover -s practiques/tigit-projecte-territorial/tests -v
python3 -B practiques/tigit-projecte-territorial/preparar.py resources --from-local _practices/tigit-projecte-territorial
python3 -B practiques/tigit-projecte-territorial/preparar.py check-resources
python3 -B practiques/tigit-projecte-territorial/preparar.py resources --fetch --output sandbox/practiques/tigit-projecte-territorial/recursos/2026-10-13-fetch-check-01
python3 -B practiques/tigit-projecte-territorial/preparar.py check-resources --output sandbox/practiques/tigit-projecte-territorial/recursos/2026-10-13-fetch-check-01
```

Resultat vigent: divuit proves passen —vuit de recursos, quatre del packet QGIS i sis de preparació/confinament dels fulls. Les dues preparacions inicials van verificar 20 fitxers i 7.735.602 bytes; el lot vigent del dia 14 en verifica 21 i 7.759.191 bytes, inclòs el PDF d'auditoria. Cap d'aquestes operacions de preparació executa models, crea un PDF o compon una edició.

| Font o evidència | SHA-256 |
| --- | --- |
| `preparar.py` | `14b64c48f7f6e27f9a987c756c9475af61b2b47e70626fb71871a6a6f70b5b68` |
| `recursos.yml` | `255e6a1f29ba26208ea5ca681199562b75f82430ebe9283ae24af06e7f500cdc` |
| `tests/test_contract.py` | `9e030fd7a5fde0958ddb9e459b2a71dd888f1c7f9670609a575395ab1e23623d` |
| `scripts/practice_paths.py` | `44b438d3dedbe70b67bc89ef03c921873c1b77e1bbb582895c78d0c5484d3cc9` |
| `sandbox/practiques/tigit-projecte-territorial/recursos/2026-10-13/resources.json` | `d57491109f4cf2098a387e7eba49769d2925c419e31ba4659dbba8e763ed37ee` |
| `sandbox/practiques/tigit-projecte-territorial/recursos/2026-10-13-fetch-check-01/resources.json` | `8bffff8ed74fc832d98169333b458f7e9145450a4dd61c1164761c6dbdadefeb` |

La ruta per defecte és ara `sandbox/practiques/tigit-projecte-territorial/recursos/2026-10-14/`. Els dos directoris del dia 13 són evidència històrica amb el manifest anterior conservat separadament.

## Reproducció dels fulls des del contracte nou

S'han completat les 24 correspondències de fonts acordades: request/model QGIS, vint scripts Python, `requirements.txt` i plantilla A3. La plantilla conserva el SHA `2a998051b7699daefd77cad4e173b2be16fbdbecedbdb3adcaf40594e6a47c9a`. També s'han creat els dos README, el Makefile i el helper de paths reservats. El nou Makefile separa preparació, generació, exportació i comprovació; `check` i `check-figures` no tenen dependències generadores. No crea snapshots a dist ni ZIPs.

`workbook-inputs` copia les deu taules raw a un run nou sota `sandbox/practiques/tigit-projecte-territorial/fulls/`, amb el directori de resultats inicialment buit. `run-inputs.json` registra els hashes de deu inputs i 23 fonts de reproducció. Els scripts refusen fonts o inputs canviats, paths fora del run, symlinks i outputs de llibre preexistents. El lector de població utilitza el CSV retingut i conserva els valors numèrics, incloses les representacions decimals com `40.0`; no torna a consultar l'API.

El primer run complet va ser `sandbox/practiques/tigit-projecte-territorial/fulls/run02-contract-20261014/`, amb `run-inputs.json` SHA `91e4670f87cfd0c65ed4382db641d4c58cff9cf51f8f70016f7e57697a43b0c7`. El vigent és `fulls/run04-eixos-20261014/`, amb manifest d'entrades SHA `de619f1a329323fffc6a76c3213c6759bb60adc1e114772f41429950a93c5d57`. Run01 és la prova anterior al control de hashes raw; run03 conserva un intent interromput pel límit agregat de 300 segons de la comanda, amb llibres complets però exports parcials. La repetició en run04, amb fases separades i temps suficient, ha acabat. Entorn propi ignorat `sandbox/practiques/tigit-projecte-territorial/venv-fulls-20261014/`, openpyxl 3.1.5, LibreOffice 24.2.7.2 i Inkscape 1.2.2. Calc usa un perfil dins del run i una connexió UNO de nom únic.

Han passat `workbooks`, els cinc comprovadors de llibres, `figures` i `check-figures`: sis XLSX reconstruïts, deu PDF i set SVG. La comparació readonly amb el cas retingut confirma fulls/fórmules/gràfics/pivots, absència de solucions a la plantilla inicial, C07/C14 preservats i els mateixos valors als 22 municipis. El CSV i el CSVT de transferència coincideixen byte a byte amb els inputs fixats, SHA `d762d55fbbfb085493fe3af39c9ae8e458c1422f41a4467a2f37202cc5f1baac` i `b2ac06038a8d40fa24e7cb9b53bdded5a96b402f56d839551a77d56c2a1373b1`. Els sis llibres antics conserven els SHA originals. La taula de hashes nous és a `context/spreadsheet-practice-audit.md`.

Els scripts d'adquisició en viu s'han reubicat amb opt-in explícit `TIGIT_FETCH_TEACHING_DATA=1`; no s'han executat com a part d'aquesta reproducció. La correcció dels eixos d'habitatge i composició d'edats s'ha fet a `prepare_chapter_03.py`: en BarChart, `x_axis` és l'eix categòric també quan les barres són horitzontals. Els comprovadors 03/07 validen els títols i els PDF exportats mostren municipis a les categories i percentatges als valors. La figura històrica de la lectura 03 conserva els seus bytes i el seu error com a exercici.

Els set SVG del primer lot havien retornat `UW-IMAGE-TRANSPARENT`; el mostreig directe de la prova d'habitatge 07 del run04 torna a donar alpha mínim 0. La decisió sobre els fons continua pendent i no s'han pintat els outputs. La correcció tècnica dels eixos no concedeix aprovació visual a tots els gràfics.

`prose_check` refusa els dos README tècnics perquè no són targets editorials de lectura pública (`files_checked: 0`); no s'ha registrat aquest resultat com una revisió reeixida. Les lectures docents 01–03 s'han actualitzat als noms/rutes canònics i totes tres passen `prose_check` amb cobertura d'un fitxer. La revisió line de 03 s'ha preparat amb digest `f555a208b6c0a3ec9678323f4a2a065a1259b19238981e46cad5f32d8ac3ba9b`, sense aprovació editorial.

## Procés QGIS des de les fonts reubicades

S'han mogut byte a byte `activity-qgis.json` i `activities/qgis-territorial.py` de l'arbre antic a `practiques/tigit-projecte-territorial/`. La comparació amb `git show HEAD:<path antic>` confirma els SHA originals `6154464971d829dc1396230f9064482f9f1ffe003ee96125e67c07ded7374aaf` i `dcd4240755b7780dc18b0255c3e0c1c825683abe70217f1bdb020cfd695c620c`. Són les dues primeres retirades de les 118 aprovades.

`qgis-inputs` verifica el snapshot, el request v2 i els hashes dels quatre inputs declarats. Prepara una còpia confinada de request, model i dades, amb `origin.json`; el productor QGIS rep aquest packet i conserva la responsabilitat d'executar el model i verificar els productes.

```bash
python3 -B practiques/tigit-projecte-territorial/preparar.py qgis-inputs \
  --output sandbox/practiques/tigit-projecte-territorial/entrades-qgis/2026-10-14-01
```

El SHA d'`origin.json` és `ee716e96c9885a0dc1688ff162d5e5ee7380d48398736b3f43e01731ca7030ed`. L'execució nativa posterior ha generat `sandbox/practiques/tigit-projecte-territorial/0.1.0/ca/run05-contract-20261014/`, bundle `8719b839d1071be858deed94fcce0e32e61f01f575d29c2b4f5e2d0ce5704eac`: 123 fitxers, 10 projectes, 10 grups de captures, 8 exports i 40 controls. La reobertura offline dels deu projectes i la selecció conjunta de cinc productes amb 17 dependències passen.

Les receptes de la pràctica 04 consumeixen aquest run05 i desen les tres captures a `sandbox/practiques/tigit-04-qgis-mapes/run03/`. Els PDFs `contract-20261014-01` i `migracio-20261014-01`, de cinc pàgines i bytes PDF idèntics però vinculats a configuracions diferents, es conserven com a històrics. El lot vigent de lectures és 0.2.0, descrit més avall. Paths, hashes i límits de revisió són a `context/qgis-practice-plan.md`.

## Incident MCP i reparació del 14 d'octubre

El 13 d'octubre la configuració local declarava unaltraweb enabled i el desplegament `522f9eadf0d6f110a38d66e107d98fa028dcc6e69bcc9a9aac4b0f8c615739d1`, però la sessió Web constava exited des de `2026-10-13T06:38:30.332440+00:00`. El connected global del pla de control corresponia a les altres connexions. Un intent de reconnectar la mateixa selecció retornava `Connection closed`.

El diagnòstic directe del llançador i de l'inventari de gaContExt va concretar el bloqueig: la instal·lació Web `796ad34e4fdc5b0dfd0eefac73a8ac60d4d285d322d80bf24a7ddbe20b771121` retornava `installation-modified`, amb el missatge `installed files, links, modes or resource closure changed`. Els tres manuals seleccionaven aquell mateix ID. No s'ha determinat quin canvi concret va invalidar-ne el manifest; la instal·lació antiga i el seu rebut es conserven com a evidència, sense reescriure'n el segell.

El menú development de gaContExt mostrava, separadament, un conflicte entre el Diavisuals 0.5.0 exigit per Web 0.7.2 i el checkout local de Diavisuals 0.7.0. La reparació dels manuals utilitza les instal·lacions de release acordades, amb Diavisuals 0.5.0.

### Instal·lació nova amb els mateixos artefactes publicats

S'han utilitzat exclusivament les operacions públiques del hub immutable `da91db4a34963ec733551e38184127aed7bd6ad1e5fe4fe52ae421bea1115ed2`: `mcp-prepare.py seed`, `mcp-runtime.py prepare-profile --offline`, selecció i activació amb CAS. Els deu artefactes de la preparació, 2.201.360.930 bytes, s'han transferit de la memòria cau anterior amb verificació completa. No s'ha canviat de versió ni reconstruït cap imatge.

- Store nou: `/home/benizar/.local/share/gacontext/prepared-web-0.7.2-repair-20261014`.
- Spec publicat: `a779db0f654caed1f8ea1c7ad22e62c542ff59685d8f195f18df5aeaeedb08f4`.
- Job de preparació: `bc5e17c0a83b4ad989de5fa272643c04`.
- Rebut H2A: `ac2b683e4e207fad16be6f38cda94b18b0e5543dfe1ae20b8c4c3996f658b4a0`.
- Instal·lació Web nova: `b223d80b68822dd94516d7f2ba27f1d76cc6528509378e4c1b81aafea075078a`.

La verificació nativa de la preparació passa també després de connectar-la i fer-hi crides MCP. La imatge Web continua sent `sha256:576dcd772f2c345fa2021745f975f8392568d8d2783f7a66ba41a3521b3bd546`, el PDF `sha256:618163d3f924439792b2306617bd9612f566c5881166102fa544b4e782d569fa` i el verificador QGIS `sha256:1fe4a54a42cbac4a6eea596be73425985ab3bca5f28f5871d2fa66d7c0a05f8b`.

### Selecció comuna i connexions reals

Els tres consumidors passen a revisió 2 i comparteixen exactament els quatre IDs següents:

| MCP | Versió | Instal·lació |
| --- | --- | --- |
| unaltraweb | 0.7.2 | `b223d80b68822dd94516d7f2ba27f1d76cc6528509378e4c1b81aafea075078a` |
| unaltracaptura-qgis | 0.6.0 | `01e54cf65014d95af7d1f30e27690bdff34e7f2f72473805a012147ab30b3235` |
| vegavisuals | 0.5.1 | `9673f0bea562fa3465384233f2a389e0cb3850b7f104b293f2111c6ecfcbe4bf` |
| diavisuals | 0.5.0 | `dc381380a28d0b1aca44bae069f6504d53c6afc5775707f70ecdcaf3dd2732fe` |

| Consumidor | Desplegament nou |
| --- | --- |
| TIG | `290fdcccfa368782d68b2714de5950e318bfd71b0e51dc3dd7b05cbe4759c372` |
| TIGIT | `453299819774033e17bdfd578c2469217cd9c29b410dddd58fb8aebdf2eaa64e` |
| Geodisseny | `09233acf2862a3e6f248d9a6a47530d1bb5144f12d9fe7ff89ab98601a4e9f38` |

La reconnexió s'ha fet servidor per servidor amb l'operació `mcp.add` anunciada per l'OpenAPI del client existent, aplicant la configuració del desplegament que acabava de generar gaContExt. S'han comprovat l'arrel exacta, les referències, l'absència de peticions MCP actives i l'estat idle dels altres manuals. No s'ha utilitzat la recuperació global d'instància que el helper refusa per a OpenCode 1.19.0. Les consultes de sessions abans/després conserven els IDs retornats pel backend; són observacions acotades, no una auditoria completa de l'historial.

Comprovació al final de la reparació inicial: 12 connexions vives, quatre per manual, totes `connected` i vinculades al seu desplegament actual. Els tres `status` retornen `configuration_matches: true`, `activation_required: false` i `reconnect_required: false`. Les observacions natives de Web/QGIS/Vega passen la verificació del supervisor; Diavisuals 0.5.0 manté la identitat parcial del contracte original. Aquesta observació precedeix l'incident de resposta llarga descrit a continuació.

A TIGIT s'han fet crides reals a `runtime_identity`, `language_policy`, `site_context` i al dry-run de `manual_practice_pdf_build`. Web retorna versió 0.7.2, binding TIGIT, `drift: false` i instància `82c4cf7ba1b2437c88831788d546ba11`. El PDF 01 d'alumnat retorna `state: current`, amb el rebut `dd2b2b3e04750f45707e816055855f7ee35da8af9fd0d8bfbe1f022b0e8da83b` i el PDF `5f196b4791e6950d444a27b1da39c1a76df2cb93d482e740b16b419dabc2f141` originals. No s'ha tornat a renderitzar.

També s'han tornat a cridar les eines reals dels tres helpers a TIGIT després de reconnectar-los. Les imatges locals de càlcul R/Python del projecte continuen disponibles amb els IDs anteriors; els workers opcionals no declarats en aquesta preparació comuna no s'han adquirit. L'actualització dels controls del lloc 0.7.1→0.7.2 continua ajornada per la decisió anterior; el seu conflicte de scaffold no és una fallada de la connexió MCP reparada.

### Timeout posterior i recuperació del resultat

La crida `manual_pdf_preview_prepare` del manual complet va superar el temps de resposta MCP; posteriorment, `manual_pdf_status` retornava `Connection closed`. El supervisor registra la sessió Web `25a418823f9a4837b2500d9caa374baa` acabada el `2026-10-14T19:55:49.983638+00:00`, codi 1 i `busy_requests: 1`. La verificació nativa de la instal·lació nova continuava passant: no s'ha reproduït `installation-modified` ni s'ha tornat a instal·lar.

S'ha reconnectat només Web TIGIT amb la mateixa selecció gestionada. Les crides reals del 14 d'octubre a partir de les 20:09 UTC confirmen instància `b9ce41cee5c9427caebec7275122e3f2`, sessió `3f2558d02ac244b696a5055c91c1ae00`, binding TIGIT, versió 0.7.2, `drift: false` i cap operació activa en aquella observació. El contenidor de la sessió anterior ja no existeix; no s'ha fet neteja manual.

El PDF sí que s'havia acabat: `manual_pdf_status` retorna manifest i artefactes vàlids, `fresh: true`. `tmp/manual-pdf/ca/tigit-ca.pdf` té 398 pàgines, 56.926.430 bytes i SHA `f18e804a555e3cfa8a33ee4e5757eb12fdb8e52993bc2ff0f3034ec956b53f14`. La preparació repetida després de comprovar l'estat ha reutilitzat el PDF, amb `built_languages: []`, `publishes: false` i rebut de preview `e6b8334d26592ae9e909eca3f6876a4145a15e027de57daf6638a19438e47fdf`. La còpia a `assets/pdf/tigit-ca.pdf` és local i ignorada; `published_current` en aquest comprovador no acredita cap desplegament públic.

`site_check` passa. La crida posterior a `build_site` també ha superat el temps de resposta MCP; una observació Docker immediata mostrava el procés Jekyll encara treballant. En acabar, es va repetir `Connection closed`. S'ha reconnectat només Web amb la mateixa configuració gestionada, sense repetir el build mentre era actiu. La web generada té 57 HTML amb mtime nou i la nota ONU incorporada. L'auditoria HTML passa sense findings estructurals; la cobertura d'opacitat avisa que `assets/plotly/demo.html` supera el límit d'inspecció. Això no acredita opacitat de totes les imatges.

El problema de les operacions llargues està retornat al propietari a [gaContExt #30](https://github.com/dosquartsdedocs/gacontext/issues/30#issuecomment-6178010364); la causa encara no està determinada. La sessió Web posterior `b7bbbb99d1224cdf8ebf2336033b2840` conserva el preview gestionat a `http://127.0.0.1:32768/tigit/ca/`. S'han comprovat des del host HTTP 200 a la portada, al capítol `terra-dades-espacials` i a la petició HEAD del PDF de 56.926.430 bytes. El `http_check` del controller retorna `Network is unreachable` quan intenta la IP interna del preview amb el seu mode network none; no s'ha ampliat la xarxa per esquivar-ho. La revisió humana queda pendent.

### Build després de retirar el llegat substituït

S'ha eliminat el mapping privat antic d'`_config.yml`; les vuit lectures canòniques es resolen sense aquest alias. La CI de fonts selecciona `practiques/` i manté `_practices/.../data` com a arrel de dades transitòria. La configuració té SHA `3742ac1b21b3753daf9e2e846739bd1190554766caba19cbfc73d51f028a0303`.

El canvi de configuració invalida la reutilització dels jobs privats anteriors: el dry-run del 01 alumnat ho refusa amb `Existing practice run has different inputs`. S'han creat, serialment, els vuit jobs `migracio-20261014-01`, tots `built` i `publishes: false`, amb 197 artefactes i 36 referències d'entrada verificats. Els tres PDFs docents modificats s'han obert i revisat; els altres cinc conserven els bytes de les versions anteriors. No hi ha Overfull, errors LaTeX ni caràcters perduts als logs.

Després de `site_check: ok`, s'ha executat el target del consumidor amb la mateixa imatge immutable ja seleccionada, sense canviar pins:

```bash
MCP_IMAGE=sha256:576dcd772f2c345fa2021745f975f8392568d8d2783f7a66ba41a3521b3bd546 make build
```

La crida CLI ha acabat correctament, inclosa la preparació nativa del PDF i Jekyll; la fase Jekyll informa 216,95 segons. El PDF complet actual té SHA `6abf17cec51eec3e971a7d06b5342f69e94efa1b21ceecfca4d50f271abcc357` i 56.926.430 bytes. `manual_pdf_preview_prepare` posterior el reutilitza sense construir idiomes; receipt de preview `445d0f76bb59a3a3453b852338d062edcab954b331898a1ae93ebd7bd44b5011`. L'auditoria dels 57 HTML no té findings estructurals; continua l'avís de cobertura d'imatges. La connexió MCP no s'ha hagut de reconnectar durant aquest build CLI. El preview anterior s'ha aturat amb l'eina del propietari; el vigent és `http://127.0.0.1:32769/tigit/ca/`, amb HTTP 200 comprovat des del host a portada, capítol 04 i HEAD del PDF després d'acabar l'arrencada.

## Continuació de guies docents i Moodle del 15 d'octubre

La [reserva exacta de continuació](https://github.com/geourv/tigit/issues/14#issuecomment-6200474177) inclou `context/writing-profile.md`, `practiques/README.md`, les vuit lectures 01–04 i els tres informes actuals. L'única ampliació de paths és el perfil de redacció, demanat explícitament per l'autor. Es manté el checkout i la branca de la reserva original; el preflight assenyala únicament el dirty-checkout de la feina pròpia. TIG s'ha consultat readonly.

El perfil incorpora el patró durador de preparació docent, durades amb supòsits, conducció de la classe, configuració de Tasca Moodle, enunciat autònom, obligatoris seleccionats amb continuïtat, dues ampliacions controlades i qualificació interna 7/2/1. Les vuit lectures estan adaptades a primer de Gestió en Turisme i Hoteleria, TIGIT 21224102, amb els mateixos equips i territoris assignats. Es diferencia el 70–20–10 dels pesos globals de la guia oficial 2026/27 i s'explica que bàsic/documentació complets poden arribar a 8/10 sense ampliacions.

L'índex [practiques/README.md](../practiques/README.md) identifica les fonts, els vuit PDFs locals vigents i els materials de demostració. Les versions de pràctica són independents de les del manual i els productors. Patró dels jobs: `sandbox/practiques/<slug>/lectura-0.2.0-ca-<destinatari>-<run>/`; PDF a `outputs/LLEGIU-ME.pdf`, rebut a `receipt.json`.

| Pràctica | Run alumnat | Pàgines alumnat/docent | Run docent |
| --- | --- | --- | --- |
| 01 | `moodle-20261015-01` | 6 / 8 | `moodle-20261015-01` |
| 02 | `moodle-20261015-02` | 5 / 7 | `moodle-20261015-01` |
| 03 | `moodle-20261015-03` | 5 / 9 | `moodle-20261015-01` |
| 04 | `moodle-20261015-02` | 7 / 9 | `moodle-20261015-01` |

Les fonts/PDFs/receipts exactes consten a `context/spreadsheet-practice-audit.md`, i els de 04 també al pla QGIS. El productor natiu retorna `built` i `publishes: false`, amb el mateix worker immutable PDF. S'han verificat els 197 artefactes i les 36 referències d'entrada contra fonts/configuració/imatges actuals. Passen els vuit `prose_check` individuals, el control A4 apaïsat/ESBORRANY, la inspecció de logs i el confinament del text dins de les pàgines. La revisió visual cobreix pàgines 3–5 dels quatre docents i la darrera pàgina dels quatre PDFs d'alumnat. Els ajustos de paginació s'han fet a les fonts i en runs nous.

Les lectures continuen `draft`. L'aplicació efectiva de les Tasques correspon al professorat a Moodle; el lot no acredita configuració d'un curs remot ni aprovació editorial. Les demostracions provenen dels llibres run04, bundle QGIS run05 i captures run03 ja conservats. Els jobs 0.1.0 i els intents 0.2.0 previs són evidència històrica, amb rebuts intactes; no s'han de comprovar com si descrivissin les fonts actuals. Aquesta unitat no resol les 14 retirades pendents ni el contracte tabular de composició.

### Comprovació final i revisió local

La verificació de l'índex confirma els 21 enllaços locals, els vuit PDFs sense duplicats, les pàgines anunciades, les vuit fonts `draft` en català amb codi 21224102 i els 30 lligams de hash transcrits als dos informes. SHA del perfil de redacció: `ab95b1fe66cd125388211e089ba53d0a1980a1f9423698e1b8994c20d4e595ff`; SHA de l'índex: `3e24ae24a494150e7f6a08b08e0e971049c820e4a94360f1e7691fb0036b3767`.

Després de `site_check: ok`, s'ha repetit `make build` amb l'override immutable MCP ja documentat, amb resultat correcte; Jekyll ha acabat en 165,667 segons. La preparació nativa de preview ha reutilitzat el PDF complet existent, `built_languages: []`, sense regenerar-lo. Font i còpia local del PDF mantenen el SHA `6abf17cec51eec3e971a7d06b5342f69e94efa1b21ceecfca4d50f271abcc357`, 56.926.430 bytes. El rebut de preview final `.cache/unaltraweb/manual-pdf-preview.json` té SHA `d642104c43849a300be731c5e3af6e6836730a56048b23bbab5f11b1206db053`.

L'auditoria dels 57 HTML retorna zero findings estructurals. Es mantenen els 63 avisos de dimensions del manual, avisos d'imatges transparents o no verificables —inclòs el límit de pressupost d'inspecció— i el límit de cobertura HTML a `assets/plotly/demo.html`; no són una certificació global d'opacitat. `site_doctor` continua assenyalant el pin MCP 0.7.1 i el conflicte de scaffold `.gitignore`, ajornats anteriorment. El build usa explícitament el runtime immutable seleccionat 0.7.2.

El preview gestionat s'ha aturat durant el build i s'ha reiniciat al mateix port: `http://127.0.0.1:32769/tigit/ca/`. Des del host, la portada, el capítol de Terra i la petició HEAD del PDF retornen HTTP 200; el PDF anuncia `application/pdf` i la mida correcta. Els PDFs privats de pràctiques es revisen des de l'índex local, perquè `practiques/` i `sandbox/` estan exclosos de Jekyll. El resultat queda disponible per a la revisió humana acordada, amb l'índex Git buit.

## Nota cartogràfica addicional

La reserva del capítol `_chapters/ca/04-terra-dades-espacials.md` està [acceptada separadament](https://github.com/geourv/tigit/issues/14#issuecomment-6175406315). La nota sobre *Correct the map* explica la votació de l'Assemblea General del 4 de setembre de 2026 —164 vots favorables, un contrari i sis abstencions— i la recomanació no vinculant d'Equal Earth i altres projeccions equivalents. No afirma una prohibició de Mercator ni una substitució universal als centres educatius.

Les fonts són el comunicat `press.un.org/en/2026/ga12779.doc.htm`, UN News i la documentació PROJ d'Equal Earth. La font catalana té SHA `1b813373d436285ef70ace9f56bc43cb097063f4df8ddeef74aba39cfa9406d1`; `prose_check` passa i s'ha preparat la revisió d'evidència, sense concedir aprovació editorial. La revisió humana del resultat continua pendent.

## Preparació en la publicació pendent de contracte compartit

El workflow de publicació reutilitzat per TIGIT, `site-deploy.yml@3332e0b93933f12317e05f1ce8d38ce80046feab`, comprova freshness de càlculs i Vega i sincronitza PDF abans d'executar `build-command`. Aquest darrer input arriba massa tard per preparar dades que aquells controls ja necessiten.

S'ha traslladat la dependència al propietari a [unaltraweb #98](https://github.com/dosquartsdedocs/unaltraweb/issues/98#issuecomment-6155003975): confirmar la via nativa de preparació abans dels controls o ampliar la interfície compartida. La prova local de `resources --fetch` proporciona una preparació concreta dels inputs, però encara no l'integra al workflow compartit. No s'ha modificat el workflow ni desactivat cap checker.

El [retorn del 14 d'octubre](https://github.com/dosquartsdedocs/unaltraweb/issues/98#issuecomment-6178087168) aporta les 24 fonts reubicades, les 18 proves i la reproducció real dels sis llibres amb CSV/CSVT idèntics; manté explícits els dos bloqueigs de contracte i el fet que la revisió local encara disposa de les dades de llegat.

La CI de fonts 0.7.2 permet retirar dades antigues i no necessita dades privades per revisar fonts. Això no acredita una construcció o publicació amb els inputs disponibles. El cas tabular també manté la limitació del schema de composició 0.7.2, que exigeix `gis`; no es prepararà un descriptor GIS fictici per als fulls de càlcul.

## Per reprendre

### Retenció consolidada del llegat

La continuació tècnica sense revisió intermèdia de l'autor conserva els 118 fitxers de la reserva en `sandbox/practiques/tigit-projecte-territorial/llegat-715944f-20261014.tar`, generat amb `git archive` del commit base. SHA de l'arxiu: `dfe882b23fc2c664e810242840d3e011df09df32e017b4b883249e3e601174ab`. S'han contrastat el conjunt exacte de membres, els bytes dels 118 blobs i el permís d'execució amb Git. Només conté fitxers regulars i directoris; no s'ha extret com un altre checkout.

Aquest arxiu és una còpia local de conservació, no un bundle de productor ni un backup durable independent. `durable_backup_verified` continua sent false. Els originals també es poden recuperar pel seu path al commit base, sense reescriure l'historial. Els tres documents antics es conserven íntegres dins de l'arxiu i a Git:

| Document històric | SHA-256 |
| --- | --- |
| `context/practical-workflow-plan.md` | `660214cd41916c3af284db92c49667355898a99a50b0926793614e0fe35f985b` |
| `context/practice-retention-index.json` | `4e72f09bffd164d64e2eb4c73b3503f916373505b66165e0900ff82dca9192ea` |
| `context/practice-tools-handoff.md` | `24c51a3b9e11175d126b19f4111c289cf6528ef00380f1ebcc51220239ce5682` |

El pla docent encara pertinent es consolida a `context/qgis-practice-plan.md`; les identitats de candidats i les observacions de connexió del dia 9 són històriques. L'índex antic no s'ha de llegir com l'estat del runtime 0.7.2 actual. El seu inventari complet dels 40 fitxers de captures continua recuperable dins del handoff arxivat.

Continuen retinguts els arbres sencers `run02-core`, `run03-cartography`, `run04-practice14-20261013` i `run05-contract-20261014`, amb els seus `bundle.json`, descriptors, recursos i controls natius. Els seus segells consten al pla QGIS. La restauració ha de conservar l'arbre complet i verificar-lo amb `practice-check`; una selecció de productes no substitueix el bundle original. Una reobertura offline nova és una operació de productor diferent de la verificació readonly.

Es conserven igualment `sandbox/practiques/tigit-projecte-territorial/0.1.0/ca/probes01`, `sandbox/qgis-practice-jobs`, `tmp/tigit-12-qgis-rc2`, `tmp/tigit-12-render-review-20261009-01` i `tmp/tigit-12-svg-preview`, sense executar cap neteja. El probe modal interromput és `.unaltracaptura-qgis/jobs/tigit-ui-probes-formats-2343a3e572.fe8ufb62`; el seu índex històric de sis fitxers i la comprovació original d'absència del contenidor són al JSON arxivat. Aquesta conservació no és una afirmació nova que tots els directoris temporals siguin un backup durable.

El manifest anterior de vint inputs es conserva separadament a `sandbox/practiques/tigit-projecte-territorial/manifest-recursos-2026-10-13.yml`, amb el SHA original `c0ef0092f45176d27e6aa2e63ac1fa65c5f4cb44114aac4fd9331a214f0f0b88`. Els arbres de recursos del dia 13 no reben cap fitxer addicional. El manifest nou incorpora el PDF d'auditoria i materialitza 21 fitxers, 7.759.191 bytes, sota `recursos/2026-10-14/`; SHA de `recursos.yml`: `255e6a1f29ba26208ea5ca681199562b75f82430ebe9283ae24af06e7f500cdc`. La recuperació real per xarxa i la comprovació readonly passen.

### Continuació pendent

1. Amb l'accés als MCP ja restablert, resoldre el punt de preparació d'inputs abans dels controls del workflow compartit. La reserva de fonts del consumidor ja està acceptada; una modificació addicional de controls o del proveïdor requerirà el seu circuit corresponent.
2. Revisar els llibres i exports reconstruïts, especialment acabat visual i fons, i la selecció de dades per destinatari. Els eixos ja estan corregits i les eines de llegat substituïdes ja s'han retirat.
3. Actualitzar els 23 Quarto, Vega, capítols i lectures per consumir els recursos preparats; regenerar figures, locks i PDFs amb els propietaris. Incorporar la figura d'auditoria necessària com a recurs explícit de la lectura, sense convertir-ne l'error d'eixos en un model validat.
4. Completar les 14 retirades restants: els 13 inputs exactes que encara declaren Quarto/Vega i `assets/downloads/tigit-01-preparacio-dades-student.zip`. La resta dels 118 paths ja està retirada i contrastada amb l'arxiu verificat. Els bundles segellats existents no s'han modificat.
5. Executar les comprovacions natives, `make build` i la previsualització; esperar la revisió humana abans de commit/publicació. Les edicions a dist continuen subjectes al contracte del productor i a la selecció de contingut.

En aquest punt s'han completat 104 retirades, preparat 21 recursos, corregit els gràfics i validat els llibres, les lectures, el procés QGIS i el build local. La continuació tècnica no ha requerit revisió intermèdia de l'autor. La publicació encara depèn del contracte compartit i de la revisió final acordada; el build local disposa dels 13 inputs transitoris i no acredita que ja es puguin eliminar.

## Publicació de la versió de treball — 18 d'octubre

L'autor ha confirmat la revisió del manual al preview i dels PDF amb «Sí, publica aquesta versió», autoritzant commit, push, PR, fusió a main i desplegament a Pages. La [confirmació queda registrada a TIGIT #14](https://github.com/geourv/tigit/issues/14#issuecomment-6253802016). Es manté l'estat `draft` i la indicació ESBORRANY de l'edició de treball. Aquesta autorització permet publicar l'estat actual amb els tretze inputs públics i el ZIP inicial encara conservats; les dependències de contracte bloquegen la seva retirada final, no aquesta publicació amb dades presents.

El control editorial de l'HTML detectava la demo no referenciada `assets/plotly/demo.html`, massa gran per a la lectura acotada. `exclude` no la retirava: el lector d'assets de tema de Jekyll 4.4.1 no aplica aquella llista. S'ha usat la configuració nativa de `StaticFile`, amb un default `published: false` per a aquest únic path. La comprovació Ruby confirma que es preserven els set defaults del core fixat i que aquest és l'únic asset del tema que deixa d'escriure's. El SHA final d'`_config.yml` és `d70e5c43e2f7706d0f8ec31b651115f3868dc4dbef56d8d091e5f4b40f02cdd0`.

`site_check` passa i s'ha completat `MCP_IMAGE=sha256:576dcd772f2c345fa2021745f975f8392568d8d2783f7a66ba41a3521b3bd546 make build`; la fase Jekyll ha acabat en 287,647 segons. `editorial_publication_check` amb `_site` passa, sense errors; conserva tres avisos de repetició i els indicis de longitud. L'auditoria de 56 HTML retorna zero findings estructurals. La inspecció d'imatges ja no s'atura a la demo, però conserva avisos de transparència i límits de pressupost; no s'han pintat fons ni declarat totes les imatges opaques. El PDF complet té 398 pàgines, 56.926.430 bytes i SHA `9fed0764784942294c32a0611f15d91d3c4edd1797d2612c6986368fc88800b8`; el rebut local de preview és `6af1cc21ffcb327e87ec5fe8f49bb17feef4a0a4af257a7fde8ce52ee8a72b2f`.

Les vuit lectures s'han reconstruït amb el productor natiu en run `pages-20261018-02` i versió 0.2.0: 197 artefactes i 36 referències d'entrada verificats contra l'estat final. Els vuit PDF són byte-idèntics als revisats per l'autor; els rebuts nous consten a l'auditoria de fulls. La carpeta local `sandbox/practiques/moodle-2026-10-18/` conté 138 còpies verificades, el manifest i `OBRE-AQUI.html`, i s'ha obert amb `xdg-open`. A `PER-PUJAR-A-MOODLE` hi ha quatre PDF i la plantilla XLSX; a `PROFESSORAT`, les guies, cinc llibres resolts i el bundle QGIS complet. La còpia del bundle passa el verificador natiu amb el segell original.

`translation_plan` confirma que només hi ha català configurat i cap traducció pendent o prematura. Les divuit proves de reproducció passen; la conservació dels 104 paths retirats continua vinculada a l'arxiu del commit base. Els fitxers locals ignorats i els PDF generats no s'inclouran al commit. El commit, la PR i el resultat efectiu del workflow manual de Pages s'identificaran al retorn de #14; la migració restant continua oberta.

## Correcció de la publicació Vega — 19 d'octubre

La [PR #18](https://github.com/geourv/tigit/pull/18) s'ha fusionat a `1e44a042b829cf36ec26b34e8f380eb06769f546`, amb el mateix arbre revisat `7c566a99b7186ab178cf93beebda56ba58891861`; la CI de fonts ha passat. El [primer desplegament](https://github.com/geourv/tigit/actions/runs/39160736953) s'ha aturat abans de publicar, al control de frescor de Vega. Les comprovacions de procedència del worker PDF, càlculs i captures havien passat.

Els logs confirmen els mateixos hashes de font, CSV i SVG. El desajust és entre el lock amb selecció explícita de la imatge local i el mode portable de perfil que usa el workflow. El productor 0.5.1 afegeix `renderer_image_id` al fingerprint només en el mode explícit; el mode normal conserva la portabilitat entre reconstruccions compatibles del perfil. La manca d'imatge a CI no exigeix renderitzar-hi la figura per validar-ne les fonts i l'artefacte en aquest segon mode.

L'autor ha acceptat la reserva atòmica de vuit paths de [TIGIT #19](https://github.com/geourv/tigit/issues/19) amb «Sí, corregeix i publica». A la branca `fix/19-vega-publication-profile`, el `render-all` natiu 0.5.1 en mode de perfil ha executat el worker immutable `sha256:46aaea98bb22103cc01d7c85e2230ed04137c2d5c34a5aae6d58cd64dd61e29e`, amb xarxa `none` i `pull never`. El contracte continua `28bd331ce12ca101b2b1326328b5bd5c8e89a5ecae6f478160ecbbf3c70ed800`, perfil `vl-convert-1.9.0` i família `benizar`.

L'SVG resultant és **byte-idèntic** al revisat: 39.503 bytes, SHA `496de7e896a4e4d0ee2dc9eca43ae7af15633d3dd559a3278935b4c48536dbfe`. El productor ha escrit el fingerprint portable `c778ac7d284fef032af496c66b5673c55509f06f59e4e40e6b8d1fa9d4d0a46f` al lock. `check` retorna `fresh: 1` i reemet el rebut, també amb bytes idèntics. No s'han editat fingerprints manualment.

Una consulta readonly `status` amb Docker deliberadament inaccessible també retorna `fresh: 1` i `renderer.available: false`, reproduint la condició de la CI sense emetre un rebut en aquella prova. Els checks de publicació utilitzen la CLI en mode de perfil, sense `VEGAVISUALS_RENDERER_IMAGE_ID`; la connexió MCP amb selecció explícita és un altre context de fingerprint i no s'ha reconfigurat globalment. Cal preservar aquesta distinció en futures regeneracions.

El 19 d'octubre el client no exposa l'MCP Web. S'han repetit `site-check` i `manual-pdf-status` amb la CLI de la mateixa imatge immutable Web 0.7.2, en un contenidor efímer sense xarxa i amb el checkout readonly. Tots dos passen i el PDF complet continua `fresh`, amb manifest i artefactes vàlids. La correcció només canvia el lock generat i aquest informe; les fonts, les dades, les figures i els PDF revisats es mantenen. El resultat efectiu del nou desplegament es registrarà a #19 i #14.
