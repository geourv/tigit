# TIGIT · retorn de les eines a l'autor

9 d'octubre de 2026 · gaContExt #32 / [TIGIT #12](https://github.com/geourv/tigit/issues/12). L'encàrrec de completar les vuit pràctiques queda substituït pel retorn d'eines. Aquest document és context de treball, no aprovació del curs.

## Estat per reprendre

- Checkout comprovat: `/home/benizar/git/tigit`; branca `integration/unaltraweb/12-practical-readiness`; HEAD `aa6d000a7176d24bb07da1ad14f5ccc1a9678b7c`. El preflight només assenyala el `dirty-checkout` conegut. Índex Git buit; cap commit/push nou.
- **QGIS CLI provada:** els bundles `run02-core` i `run03-cartography` passen `practice-check`, perfil `qgis-practice-v2`. No s'ha repetit el càlcul ni la reobertura: s'han verificat els segells i les evidències retingudes.
- **Prova Web temporal anterior:** va acreditar el fingerprint exacte, binding TIGIT, `drift:false`, controller i PDF worker `matched`. Aquella connexió es va drenar i tancar; `session-status` va confirmar `stopped`, `resources_released:true`.
- **Registre local activat:** `opencode.json`, només `$schema` i `mcp.unaltraweb`, tipus `local`, ordre array, `enabled:true`. Validació completa contra `https://opencode.ai/config.json`: correcta. Esquema consultat SHA `e8cb6e287a3852ee3403f4803be5ad6b19db94948037eaa9672125c333427922`. Exclusió local exacta `/opencode.json` a `.git/info/exclude`; cap altra entrada/model/permís ni configuració global modificats. El coordinador confirma la recàrrega scoped amb el nou host adapter `2c9b0c21…`: OpenCode 1.18.35, un POST HTTP 200/true i event `disposed` observat; tots els IDs d'historial i el mateix model/agent preservats.
- **MCP REAL comprovat el 2026-10-09 a les 21:55 UTC:** una crida `unaltraweb.runtime_identity` des de la connexió d'aquesta sessió, `ok:true`, `observation:live-serving-process`. Instància `f174d482832e4c6e9a95b511c3a1d815`, sessió `ff42180dc2f5d82d8981f9bad9747527`, inici `2026-10-09T21:53:26.088156+00:00`, contenidor `5e6241e38e59953c8b0afd43f9af8e8f2ef887bde658bdcfd24655cf47c3a2c9`. Aquesta és l'observació posterior a la recàrrega del nou adapter.
- **Identitats reals coincidents:** image seleccionada/esperada/observada `sha256:17ef0d24e8611a6802b3c01ff440e6e552eac728343733198056fdbc6cdf379e`; fingerprint carregat i actual `sha256:5b8de154fc10665f71056b2887959d41a2a6f5fb5726611d1ee3482c7d7b3d36`; `drift:false`. Tots els bindings apunten a `/home/benizar/git/tigit`, project ID `71d5b0c667697959`. PDF esperat/observat `sha256:618163d3f924439792b2306617bd9612f566c5881166102fa544b4e782d569fa`, `state:matched`, referència i productor fixats més avall. La metadata Python continua 0.7.1; els hashes identifiquen candidate-04.
- **Inventari MCP real a les 21:55 UTC:** `manual_practice_pdf_build(source, version, run?, dry_run?)` i `manual_practice_compose(config, dry_run?)` consten exposades en aquesta sessió, amb noms d'eina `unaltraweb_manual_practice_pdf_build` i `unaltraweb_manual_practice_compose`. Disponibilitat comprovada a l'inventari, sense executar-les ni repetir cap render/dry-run.
- **Connexió usable i idle:** `lifecycle.state:connected`, `active_operation:null`, `queued_operations:0`, `resources_released:false`, `diagnostics:[]`, xarxa `none`. La connexió actual es conserva oberta; no s'ha drenat.

SHA actual de `opencode.json`: `1cb43f4fa41ccd02b634247ebefabab1fbd45793f1b055ff02fea68f6739302a`. Baseline anterior comprovat: `70537c065ded62bd99d35f91477d48098f1e9801cc7aaab5a6672c3f1f86cccc`; únic delta: `mcp.unaltraweb.command[0]`, l'executable host. La resta de bytes de configuració es conserva exactament. SHA de `.git/info/exclude`: `6c3f352a4d8377de80579f90c7a3bc92cf58c454b7c9b120791934a60e1bfd6c`.

## Selecció comuna i ordres

Guia: `/tmp/opencode/practice32-final-cohort.md`, SHA `6455db67fee9f13da172be810b6ea29d60b05ba2fba9d5f84038c1a47f95e7a2`.
Contracte Web: `/tmp/opencode/practice32-web-candidate04/CONTRACT.md`; `ready.json` SHA `ba9fbdb6170a0f51086bad310a636e8c3d2f93ea4317c106d313ab32f509718b`. Els quatre hashes del payload del contracte s'han contrastat. No cal obrir el factory.

### Adapter host corregit: recarregat

Executable nou: `/tmp/opencode/practice32-web-adapter-2c9b0c21cbdf7f226a76fd792b9a8fe31e51a525ad0e14398aa052b7a89e7a2a/venv/bin/unaltraweb-mcp-docker`. Pin del wheel host: `2c9b0c21cbdf7f226a76fd792b9a8fe31e51a525ad0e14398aa052b7a89e7a2a`; `ready.json` del mateix directori públic SHA `7c7f98fb11f0aaab827644c201a6b8527079ec8b26a96da3f346dbf861c2f9ec`. `USAGE.md` i `manifest.json` revisats i hashes comprovats: `eaf206b0d678239b2e44175c06a83a0ffe1b3cbf5b922c4e8c248950b3c0f044` i `0cc8e3735c960924e4698909367d01cf711d536eebda5fe068835d519b94f554`.

La correcció tracta l'ordre dels mounts al reaper. La identitat host `2c9b0c21…` és independent del fingerprint del controller: image `17ef0d24…`, fingerprint `5b8de154…` i PDF `618163d3…` es mantenen. El coordinador ha recarregat el registre amb el nou executable; la crida REAL de les 21:55 UTC acredita el controller, el consumidor i el worker esperats. No s'ha repetit la verificació del paquet host ni cap prova Docker/render/dry-run. La connexió actual continua oberta, sense drain. L'adapter vell i el contracte original romanen intactes. Als exemples one-shot, `CLIENT` apunta a la `venv` nova.

### QGIS: comprovació readonly copiable

Client compartit existent, sense instal·lació nova: `unaltracaptura-qgis 0.6.0rc2`, revision `sha256:5922d3dc411c14c7c3c2d9257a78b4d42f42fb1aae8451bcf245ca44a0e91992`; wheel `1a7456c0b81e0a4729b702b60d9340456efea9a88b9f5c21b97c8ff4823d09bf`; schema v2 `528c8be229c72c346f134ffaa60094f94224094a25b6fb11bcc87802ddc7fffb`. `ready.json` del client SHA `6a51f1f9c77a0a333623e8332b886651ea497895b1736165404e79d8905983bd`.

```bash
WORKSPACE=/home/benizar/git/tigit
CLIENT=/tmp/opencode/practice32-qgis-client-1a7456c0b81e/env/bin/python
test "$(pwd -P)" = "$WORKSPACE" && test "$(git rev-parse --show-toplevel)" = "$WORKSPACE" || exit 1
env -u DOCKER_CONTEXT -u DOCKER_TLS_VERIFY -u DOCKER_CERT_PATH -u DOCKER_API_VERSION \
  -u UNALTRACAPTURA_QGIS_PROJECT_ID -u UNALTRACAPTURA_QGIS_JOB_REGISTRY \
  -u UNALTRACAPTURA_QGIS_JOB_REGISTRY_HOST -u UNALTRACAPTURA_QGIS_JOB_GRANT \
  DOCKER_HOST=unix:///var/run/docker.sock MCP_CONSUMER_WORKSPACE="$WORKSPACE" \
  UNALTRACAPTURA_QGIS_WORKSPACE="$WORKSPACE" UNALTRACAPTURA_QGIS_HOST_WORKSPACE="$WORKSPACE" \
  UNALTRACAPTURA_QGIS_HOST_UID="$(id -u)" UNALTRACAPTURA_QGIS_HOST_GID="$(id -g)" \
  "$CLIENT" -I -B -m veure_qgis_mcp.cli practice-check --workspace "$WORKSPACE" \
  --path sandbox/practiques/tigit-projecte-territorial/0.1.0/ca/run02-core/bundle.json \
  --sha256 78d8a824ec96119a105ffdcc79b478fa626fb3304ec6eba6a4f60d882a6f6e19 \
  --select initial-project
```

El mateix prefix serveix per a `practice-schema --profile qgis-practice-v2`, `practice-run` i `practice-reopen`, segons `USAGE.md` del client. Un run/reopen nou necessita destinació create-only i decisió expressa de reprendre'l. Engine preparat: `sha256:1003721d96abe9607d8337b36851f9b29f84c2f8f92b377d1a73ff03c9d15cd2`; daemon local comprovat `OFGT:YV5X:2GIS:4KWP:ZPIT:HO2R:FHDY:B7SD:KK3W:5OLQ:YX5P:Q2NK`.

### Web: dry-run copiable amb retirada exacta

Controller `sha256:17ef0d24e8611a6802b3c01ff440e6e552eac728343733198056fdbc6cdf379e`; fingerprint carregat `sha256:5b8de154fc10665f71056b2887959d41a2a6f5fb5726611d1ee3482c7d7b3d36`. Worker PDF observat `sha256:618163d3f924439792b2306617bd9612f566c5881166102fa544b4e782d569fa`; productor `b7ec1d7a139c65b3b0b88699cdbeb19080f13be1`.

```bash
PROJECT=/home/benizar/git/tigit
CLIENT=/tmp/opencode/practice32-web-adapter-2c9b0c21cbdf7f226a76fd792b9a8fe31e51a525ad0e14398aa052b7a89e7a2a/venv
IMAGE=sha256:17ef0d24e8611a6802b3c01ff440e6e552eac728343733198056fdbc6cdf379e
PDF_IMAGE=ghcr.io/dosquartsdedocs/unaltraweb-manual-pdf@sha256:1bb3f2dafd741e96c28639ec1cc8ccaeb81cbaa73e649f787c0b4ef59997bd4b
test "$(pwd -P)" = "$PROJECT" && test "$(git rev-parse --show-toplevel)" = "$PROJECT" || exit 1
PROFILE="$("$CLIENT/bin/unaltraweb-mcp-docker" path)"
PROJECT_ID="$(/bin/sh "$PROFILE/scripts/unaltraweb-mcp-project-id.sh" "$PROJECT")"
SESSION="$(od -An -N16 -tx1 /dev/urandom | tr -d ' \n')"
PM="$(/bin/sh "$PROFILE/scripts/unaltraweb-docker-mount.sh" "$PROJECT" "$PROJECT")"
SOCKET="$(realpath /var/run/docker.sock)"
SM="$(/bin/sh "$PROFILE/scripts/unaltraweb-docker-mount.sh" "$SOCKET" /var/run/docker.sock)"
CID="$(docker --context default create --pull never --network none --init \
  --name "unaltraweb-stdio-$SESSION" --cpus 2 --memory 4g --pids-limit 512 \
  --label io.context.mcp-factory=unaltraweb --label io.context.mcp-role=stdio \
  --label "io.context.mcp-project=$PROJECT_ID" --label "io.context.mcp-session=$SESSION" \
  --user "$(id -u):$(id -g)" --group-add "$(stat -c %g "$SOCKET")" \
  --mount "$PM" --mount "$SM" -e HOME=/tmp \
  -e "MCP_CONSUMER_WORKSPACE=$PROJECT" -e "UNALTRAWEB_DOCKER_ROOT=$PROJECT" \
  -e "UNALTRAWEB_RUNTIME_SESSION=$SESSION" -e "MANUAL_PDF_IMAGE=$PDF_IMAGE" \
  --entrypoint unaltraweb-mcp "$IMAGE" --project "$PROJECT" \
  mcp manual-practice-pdf-build \
  --source _practices/tigit-projecte-territorial/readings/ca/LLEGIU-ME-estudiant.md \
  --version 0.1.0 --dry-run)" || exit 1
declare -p CID SESSION
STATUS=0
docker --context default start --attach "$CID" || STATUS=$?
DOCKER_CONTEXT=default "$CLIENT/bin/unaltraweb-mcp-docker" reap-session \
  --project "$PROJECT" --session-id "$SESSION" --container-id "$CID" && test "$STATUS" -eq 0
```

Resultat observat: `ok:false`, `publishes:false`, `timed_out:false`, returncode 2, **`Standalone practice PDF cannot retain local file links without an explicit portable edition context`**. La lectura enllaça `../../templates/infografia-a3.svg`: falta l'edició portable que autoritzi el recurs. No s'ha eliminat l'enllaç ni retocat la lectura per forçar un pass. `edition.json` encara no existeix ni s'ha indexat; no s'han produït PDFs de lectura ni ZIPs d'aquesta edició.

El mapping privat ja és explícit a `_config.yml → unaltraweb.practices.readings`: slug `tigit-projecte-territorial`, `lang:ca`, fonts estudiant/professorat amb recipients `alumnat`/`docent`. `_practices/`, `practiques/`, `sandbox/` i `dist/` queden exclosos del web; això no converteix els fitxers Git en privats. Per reprendre la composició, la plantilla ha de conservar-se com a recurs de la futura edició:

```yaml
resources:
  - path: _practices/tigit-projecte-territorial/templates/infografia-a3.svg
    sha256: 2a998051b7699daefd77cad4e173b2be16fbdbecedbdb3adcaf40594e6a47c9a
    destination: resources/infografia-a3.svg
    role: editable-infographic
    recipients: [alumnat, docent]
    dependencies: []
```

Aquest fragment és preparació, no una edició validada. Cal afegir bundle real, seleccions/closure, lectures i hashes a la configuració completa, reservar/indexar el fitxer quan s'autoritzi i usar `mcp manual-practice-compose --config _practices/tigit-projecte-territorial/edition.json --dry-run` amb el mateix controller. El schema és `/tmp/opencode/practice32-web-candidate04/practice-edition-v1.schema.json`, SHA `06707a0d847715f85576fd2f3118d132808c8cf5dbd522333bbabf4759bd867d`. `approved_sha256` fixa bytes; les lectures continuen `draft`.

Identitat no és un subcommand CLI d'aquest candidat: `mcp runtime-identity` retorna `invalid choice`. Cal cridar el tool `runtime_identity` per stdio. La prova temporal anterior es va fer amb l'adapter; després de la recàrrega del coordinador, la connexió REAL d'OpenCode també ha acreditat la identitat indicada a l'inici del handoff.

## Pràctica ja executada i evidències

Arrel comuna `S = sandbox/practiques/tigit-projecte-territorial/0.1.0/ca/`:

| Evidència relativa a S | SHA-256 |
| --- | --- |
| `run02-core/bundle.json` | `78d8a824ec96119a105ffdcc79b478fa626fb3304ec6eba6a4f60d882a6f6e19` |
| `run02-core/payload/practice.json` | `04020bd62d57c24bc03a9e422e6bb4f5e2fb2e9aa7c3aeb339182b5c8a65e3cc` |
| `run02-core/payload/controls/offline-reopen.json` | `2e7c288465a254caba3820521c348c44df6f9a0472675aec901fabe1f608a1bd` |
| `run03-cartography/bundle.json` | `9ca86916de5918805e23107ca93a3f48537c289c3dfa7ebe72569da95d5429ed` |
| `run03-cartography/payload/practice.json` | `8118fae9bc06f6d9eb8d59c7e8027dbcad97e4f3fe28e22143f0f44a6ab7ab25` |
| `run03-cartography/payload/controls/offline-reopen.json` | `24feab2cd8eb0a3d7c9eba289c1d6446907205f7a36eef1398f26201f044574c` |

Run02, job `practice-719e8a2656e14a45bf490fd6c450f7b1`: **40 controls, 22 coincidències, 0 absències**, claus úniques i geometries conservades. Sis municipis superen estrictament el 50%; Vila-seca dona 49,9052649710053%; comarca 66.105 / 169.179 = 39,07399854591882%. Reobertura retinguda `ok:true`, `network:none`, absència de contenidors verificada, projectes inicial i unió. Captura inicial real però massa allunyada.

Run03, job `practice-b845310438844475b4af4d1bcb0f5490`: els mateixos 40 controls; quatre QGZ sota `payload/projects/`, fites `tigit-04-dades-espacials.qgz`, `tigit-05-integracio-sig.qgz`, `tigit-06-llenguatge-cartografic.qgz`, `tigit-08-cartografia-tematica.qgz`. Reobertura offline dels quatre: correcta. Vuit exports sota `payload/figures/`: `context-base`, `coropleta-base`, `simbols-graduats`, `simbols-proporcionals`, cadascun SVG/PDF. El descriptor segella tots els hashes, dades, fonts, auxiliars, temes i marcs. Preservar el bundle sencer.

Captures provades en QGIS 3.44.11, català: vista inicial, taula d'unió i simbologia al bundle; gestor GeoPackage amb cinc subcapes, atributs Shapefile, diàleg `native:joinattributestable`, etiquetatge i selector de temes als probes. `open_toolbutton_menu text=temes` funciona. `project-menu` i `layouts-menu` són captures de menús, **no del dissenyador**.

## Punts a reprendre per l'autor

1. Revisar les dues lectures catalanes i adaptar les rutes antigues `data/qgis/outputs` a les reals `payload/data`, `payload/projects`, `payload/figures`. Els tres nous capítols 10–12 encara no s'han creat; la reorganització de teoria queda pendent. Els contextos anteriors contenen estats històrics; aquest handoff fixa l'estat actual.
2. El model de domini actual corregeix el mètode de classificació del renderer i compacta la taula. **No s'ha reexecutat**: run03 encara mostra el combo de classificació per defecte malgrat contenir talls quantils. La petició actual amplia a deu projectes/captures i queda draft; `run04-teaching` no s'ha llançat. Cal validar-la amb el productor quan es reprengui, sense substituir runs segellats.
3. El layout és una base editable amb dos marcs independents; llegenda automàtica i barra d'escala requereixen acabat d'autor. La variant proporcional usa mides estàtiques pels valors observats, no una expressió activa: dades noves exigeixen recomputació. Cal revisar fonts, col·lisions i mida final.
4. Captures **no acreditades**: dissenyador/propietats dels marcs, propietats de capa modal, assistent proporcional, serveis/plugin en línia i GUI Inkscape. El matcher de `Projecte > Dissenys` confon `Gestor de dissenys...`; `trigger_action` pel nom del layout no funciona. `mActionLayerProperties` va quedar modal; no s'ha insistit. Les captures de taula i diàleg d'unió sí que es van obtenir després. El render Inkscape de la plantilla no és una captura GUI.
5. Completar selecció/bindings/resources de l'edició quan interessi a l'autor. Les dades 2021 i geometries 2026 necessiten justificació temporal; el cas d'habitatge no substitueix tota l'oferta turística del curs. Ni els bundles ni aquesta prova certifiquen les vuit pràctiques acabades.

## Fonts, preservació i hashes

`P = _practices/tigit-projecte-territorial/`. Hashes al retorn, sense cap canvi posterior de contingut:

| Font | SHA-256 |
| --- | --- |
| `P/readings/ca/LLEGIU-ME-estudiant.md` | `a60fe7b98e6d25c6c1c02f682487c7bbb916a27c926f9b2f8a3f788eb1ca2403` |
| `P/readings/ca/LLEGIU-ME-professorat.md` | `f39d5dba152545ed443fdc482f5fa7fdacbc12db9ca7c25117c2f3f8b223f3d2` |
| `P/activity-qgis.json` | `6154464971d829dc1396230f9064482f9f1ffe003ee96125e67c07ded7374aaf` |
| `P/activities/qgis-territorial.py` | `dcd4240755b7780dc18b0255c3e0c1c825683abe70217f1bdb020cfd695c620c` |
| `P/captures/qgis-ui-probes.yml` | `4a405b5d1ed3b78277002aeefc9f171d98e222c4cc4724f20754d24d3ce6a6de` |
| `P/templates/infografia-a3.svg` | `2a998051b7699daefd77cad4e173b2be16fbdbecedbdb3adcaf40594e6a47c9a` |
| `unaltracaptura-qgis.yml` | `f3b1c95ea8b7c8bf70a69a0197c3082abdcfcbcecd5097c30c04e4358ec54a23` |
| `_config.yml` | `eec4e1f94a11e70fb058dc2e0b1c21d3485318b371b08c08f1a807063cfb0cd0` |
| `context/practical-workflow-plan.md` | `660214cd41916c3af284db92c49667355898a99a50b0926793614e0fe35f985b` |
| `context/provider-receipt-diagnosis-0.7.1.md` (històric) | `1193e7ba32999e5d3b307a6362df0fa28235b6883c4fb824c779a6cafb97b36f` |

AGENTS preservat: SHA `5dc6913c3b9c7347a9fa76a2682a6e90a6eb64980e8f3c956365cf7ead13e410`. Les 24 sortides regenerades i les còpies anteriors es conserven; dossier `tmp/tigit-12-render-review-20261009-01/`, `verification-final.json` SHA `4a6943429b23333575febe8776eca62c8649d596cafe5dfd339bc9df3f64b196`. Rebuts preservats: Diavisuals `abee6b55e69ed1be7d2973741d7bd02d3a3346dfaaa734e6e9d849bb78d459b6`; Vega `850d6d53e62216c4fc1c028146143935cd5a50d2fde87049a52b8c36fa2abb21`. No regeneració/build/pull/retag nou.

Previsualització de la plantilla: `tmp/tigit-12-svg-preview/infografia-a3.png`, SHA `bafc0835751be1ce7f15a3e31bd7ea61dbd0dad7cf44a9d5048847c6a8b4252c`. Logs GIS i diagnòstics: `tmp/tigit-12-qgis-rc2/`; staging natiu `sandbox/qgis-practice-jobs/`. Es preserva també l'estat del probe interromput a `.unaltracaptura-qgis/`, actualment no versionat; no s'ha netejat ni afegit a Git.

<details>
<summary>Inventari SHA-256 de totes les captures noves (paths relatius a S)</summary>

```text
51339407d00d53850661c0ae5ddee3c2da7f7fcea7825b38dc9e7a4a6e733206  run02-core/payload/captures/initial-project/overview.annotations.svg
c78395407f6d40b9cf2b7b911ecc8cb91618a26507202c2ca660b29c6dba266f  run02-core/payload/captures/initial-project/overview.manifest.json
b16b63d0ba26bfccf2deaba625423e62c9b49832076334715335a39034e0e15d  run02-core/payload/captures/initial-project/overview.original.png
31209ff7d31f678cbefd3d830199512f6844f60345597469a07f350ae8a9c53a  run02-core/payload/captures/initial-project/overview.png
a13d51c019264536e849ebda233477aca4d467b1f56df13813436933b2d21fdb  run03-cartography/payload/captures/initial-project/overview.annotations.svg
e2026097e732bf17f613b544560857744536af48044c7e861ba06a399d7be4b2  run03-cartography/payload/captures/initial-project/overview.manifest.json
798ec8cd8007d9c09f3662a47b0adea1009ec57910e1b2296e110bb0ff6f92c2  run03-cartography/payload/captures/initial-project/overview.original.png
a0b79d852f5127e1ac4b022e9d918dc91915812a8f1d8f989a289d2007607514  run03-cartography/payload/captures/initial-project/overview.png
e78210a5962be867b47ced5fa7fa86a3a96615fbba8ac100e10c1811086d900a  run03-cartography/payload/captures/joined-project/attributes.annotations.svg
4bfd95c8ba3098668b6720f3970f6be2b367fa8d38392de8baa5b8ae0d3c0037  run03-cartography/payload/captures/joined-project/attributes.manifest.json
c128c68ea6b5ed3cf43df038cf32830b0962e9842c87520a7f445ba4aaa72b7f  run03-cartography/payload/captures/joined-project/attributes.original.png
c128c68ea6b5ed3cf43df038cf32830b0962e9842c87520a7f445ba4aaa72b7f  run03-cartography/payload/captures/joined-project/attributes.png
5c5688934ecf576fea9cead64207916bbfc940aab4870d1e36d1268cc6422622  run03-cartography/payload/captures/resolved-project/symbology.annotations.svg
a6b672e5d1383651e874ecb2ebf6faeae05e5e9d3c32de1bd7e7e5bce90a39f9  run03-cartography/payload/captures/resolved-project/symbology.manifest.json
d7bab2cb411c6e3d72a294100f37b0f3056c1ce8aab93aa66e8ece141fcdcbb1  run03-cartography/payload/captures/resolved-project/symbology.original.png
d7bab2cb411c6e3d72a294100f37b0f3056c1ce8aab93aa66e8ece141fcdcbb1  run03-cartography/payload/captures/resolved-project/symbology.png
96229cf01b9368c33203f84e11fced9b1406650229bf2534cd5190a4f99631e5  probes01/captures/tigit-ui-probes/formats.annotations.svg
a739c769618639e7e18f2293d75d3f2bebca420ecd2d69f537423624661ebc0e  probes01/captures/tigit-ui-probes/formats.manifest.yml
93c112c3bd68bda2e46cffd51cb2e7c7a4efbe774a832d0187a42f92ff2a01bd  probes01/captures/tigit-ui-probes/formats.png
8d11227df31ced6c268deea6270de63429729b32fb80692eb9b1985b8a0dd364  probes01/captures/tigit-ui-probes/join.annotations.svg
f1bd23e6b657a542a224cca473dd740aba4388338d7ff9ab958620acde8765c2  probes01/captures/tigit-ui-probes/join.manifest.yml
af8bb4b98783566029f7b26e395b81df64ad3eded8c26bc4c9ed8e48b7420811  probes01/captures/tigit-ui-probes/join.png
22808cf45f7fc9b104756510aaadb9765edc211f60f1e65594097fa5c154d24e  probes01/captures/tigit-ui-probes/labeling.annotations.svg
8f74fc6d2a465c4ff6637da960624e2b32ce023848efd8b8d1fc074a27f3ddf9  probes01/captures/tigit-ui-probes/labeling.manifest.yml
9d1d43ad0d9cc786d0d4b5212b7912d845ab5111272e7f5551286243a0bb62e0  probes01/captures/tigit-ui-probes/labeling.png
8cd5b5b6b2e12b35737aae15975f6c34590866fb62f45d4b94ab8a6807bb1f81  probes01/captures/tigit-ui-probes/layouts-menu.annotations.svg
f17a56b0799025f58faffcdd16b8d9e4526b061095df24ed3b20834f85e7a5c6  probes01/captures/tigit-ui-probes/layouts-menu.manifest.yml
65a7f5a631516a2599a5d8d06d2a1854706c38cff2fe1dd821b9cc496ffe771d  probes01/captures/tigit-ui-probes/layouts-menu.png
9df01422b5b105b541232a300ca375619f80041d85b703773b59ff3346288f8a  probes01/captures/tigit-ui-probes/project-menu.annotations.svg
e3d3f164bb099f3808a7600f62d2d519bc2aa289cd0bbcc6abb1634b5a64cbef  probes01/captures/tigit-ui-probes/project-menu.manifest.yml
229dd45b9a14677dd3ac348f15d20c3159eb2bef5d784fd11d8a55b1b1e58fa6  probes01/captures/tigit-ui-probes/project-menu.png
9cdf48629568ea13bc1eccb7c7cb78928479d69e78c34ea7021304750afc0442  probes01/captures/tigit-ui-probes/sources.annotations.svg
0a36a3868efc0e2bc0eacdbe76fadbdc8d6c82b629ac9730ac71521e785b3445  probes01/captures/tigit-ui-probes/sources.manifest.yml
5026f941a3c8432abd7033a3b12a1b947e1f362c5ec9663dbd6359be9432903b  probes01/captures/tigit-ui-probes/sources.png
5e81cb61afe2488a55c02a57e6697fc305144ab3edea27ff179e576653f92b12  probes01/captures/tigit-ui-probes/themes-menu.annotations.svg
6e96be3a4d06eec5a987302a5cd805d2bdbf5294937c83c041da486de302486f  probes01/captures/tigit-ui-probes/themes-menu.manifest.yml
3cdc99898a4764b12521d78ebcb235b7a79ffefc80045b94f480f49f3cce23c8  probes01/captures/tigit-ui-probes/themes-menu.png
38289d3a99c71e129abd3e1f3247d73a93821ff0990f36997fb3d538c06c2eeb  probes01/captures/tigit-ui-probes/themes-overview.annotations.svg
f2270b3696a8d14c733a54ae84cf41105333614a3ac90a1ee319e9af92efd542  probes01/captures/tigit-ui-probes/themes-overview.manifest.yml
b91932abf0347fcbd8b95d5af5288dfec7cf5dfb7ddbb0d829b361ab49ad8c0a  probes01/captures/tigit-ui-probes/themes-overview.png
```

Els probes són evidències d'interfície conservades amb SVG i manifest; no formen part d'un nou bundle segellat. Els PNG originals separats dels bundles es preserven.

</details>

## Finalització de les proves

- Identitat candidata temporal: instància `a1de22d0ad0c42088a3584fdd6d772d0`, sessió `3e93960e3b12370d1807bcaa41a15714`, contenidor `72fb02178416bd31032afd577980c6525f50b759a1836b696375b28f1a1b6526`; drain, EOF i absència exacta comprovats.
- Dry-run: sessió `58c047f22ce20ba2a494f122a0aba246`, contenidor `6499455d06ea65c4586518d462c04bbfcf11f040109b9c9731dd6cfaccb2cb0d`; `reap-session` correcte, recursos alliberats.
- Intent CLI d'identitat no suportat: sessió `c4cf2977fbd3f9309e51483899e2e4f6`, contenidor `7a171a14c7d7521dcb003eee4f3c27156bb9d240cef0479320cba05895980757`; reaper correcte també en error.
- Probe modal anterior: contenidor propi `819f312eacf232647068c8bb319df59d508440f359bb2c0b89a16a1185bfb3c6`, aturat després de verificar labels, projecte i muntatge del job; retirada i absència exactes comprovades. Cap worker de captura TIGIT queda actiu.

Tancament posterior a la recàrrega scoped: sessió editora idle i connexió REAL del candidat oberta i usable per l'autor. Només s'ha observat la identitat i l'inventari d'eines i actualitzat aquest handoff; la CLI QGIS i el límit de l'enllaç SVG sense edició portable conserven les comprovacions anteriors. Cap nova recàrrega, drain, render/dry-run ni treball docent. Cap seqüència docent completa ni edició final declarada acabada.
