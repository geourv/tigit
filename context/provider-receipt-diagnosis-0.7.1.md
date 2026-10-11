# Diagnòstic de rebuts de proveïdor — Web 0.7.1

Observació del 9 d'octubre de 2026 a `/home/benizar/git/tigit`, branca `integration/unaltraweb/12-practical-readiness`, HEAD `aa6d000a7176d24bb07da1ad14f5ccc1a9678b7c`. Continuació autoritzada de TIGIT #12 / gaContExt #32. Els canvis de controls i fonts docents de la fase anterior es preserven sense commit.

## Contracte efectivament contrastat

`unaltraweb_runtime_identity` acredita Web 0.7.1 instal·lat, sense drift, amb binding de consumidor i projecte efectiu a TIGIT. Instància: `f723bf4a486d4d3195091bbaa29e35fc`.

`distribution_doctor(check_docker=false)` retorna `ok: true` per la distribució i els pins del consumidor. Aquest resultat no acredita les connexions dels helpers: el contracte selecciona Diavisuals 0.5.0 i Vegavisuals 0.5.1.

S'ha contrastat `companion_compatibility.py` del core immutable `3332e0b93933f12317e05f1ce8d38ce80046feab`. El seu SHA-256, `ee103d6076a4dee0f5fc8a78bd011c6453e5e90de29db8cdb86c8560678f9f20`, coincideix amb el fitxer declarat per la identitat del Web viu. Admet exactament el parell de versió/release seleccionat i, com a punt legacy, `0.4.0 / v0.4.0` per a tots dos proveïdors. No admet `0.3.1 / v0.3.1`; tampoc admet un rebut Diavisuals `0.6.0 / v0.6.0` amb aquesta selecció.

## Identitats anteriors dels rebuts

| Path | SHA-256 del fitxer abans del diagnòstic | Versió/release |
| --- | --- | --- |
| `.unaltraweb/receipts/vegavisuals.json` | `8f6ed6a0e46b2fbcfc7fc046f9370b2b79bb770db2ad6c27bb1396646be61864` | `0.3.1 / v0.3.1` |
| `.unaltraweb/receipts/diavisuals.json` | `06c2b0f0c492731d1fe7429fc8073c0cd1939307142f663aadb61ce1a144332e` | `0.3.1 / v0.3.1` |

Vega declara una sortida i request `47c02bbeae56098d42d64a47b7aa67072dcf3d8ef6b02ccedd0300895b02d267`. Diavisuals declara 23 sortides i request `c6c5a396d5169df2e6bb143c058da12922235207637f5f70d0938b5ee38b5570`.

Els dos paths s'han reservat, però no s'han editat ni renovat: les condicions per executar els checks emissors de rebuts no s'han satisfet.

## Vegavisuals

- Eines natives executades: `runtime_identity`, `compatibility_status`, `factory_manifest` i `visualization_status(manifest_path=".vegavisuals.yml")`.
- Instància: `9dc45c2d4d7242ba80ba3bde963b70e3`; binding `/home/benizar/git/tigit`, coincident amb l'arrencada.
- Versió carregada: **0.5.1**, admissible pel contracte Web, però en mode development/editable.
- Identitat `ok: false`: `source-revision-changed`, de `9788de7129e704fc9028d536008a28d629cdd506` a `6173589720358182e8709fe3ee6af142b69ef794`. El digest dels fitxers de paquet observats es manté igual: `9d6901b203e17595488fa362881246cb1fcf8706006f6f924b7030636d774540`. No s'ha interpretat el canvi de HEAD com una modificació demostrada de tots aquests fitxers.
- Perfil natiu: `vl-convert-1.9.0`, disponible. Contracte de renderer actual i del lock: `28bd331ce12ca101b2b1326328b5bd5c8e89a5ecae6f478160ecbbf3c70ed800`.

### Bloqueig concret de frescor

`visualization_status` ha retornat la visualització `non-principal-housing-ordered-bars` en estat **`stale`**, amb `managed: true`. L'`ok: true` de la resposta indica que la consulta s'ha pogut fer; no significa que la visualització sigui fresca.

| Identitat | Lock conservat | Selecció actual |
| --- | --- | --- |
| Imatge del renderer | `sha256:695125943d0fbc3aa7c877babb9a11a6501bbc7ac265b0975bb5657c60439d98` | `sha256:46aaea98bb22103cc01d7c85e2230ed04137c2d5c34a5aae6d58cd64dd61e29e` |
| Fingerprint | `2899808fdfe499b4d30e2b3574c2b26a0727f04d51d824c0d5ebbc5163257459` | `c778ac7d284fef032af496c66b5673c55509f06f59e4e40e6b8d1fa9d4d0a46f` |

L'SVG conserva el SHA-256 `496de7e896a4e4d0ee2dc9eca43ae7af15633d3dd559a3278935b4c48536dbfe`, igual que el lock. El CSV conserva `d762d55fbbfb085493fe3af39c9ae8e458c1422f41a4467a2f37202cc5f1baac`. La diferència observada d'identitat del renderer requereix resolució de procedència; no justifica tocar l'SVG ni actualitzar el lock a mà.

La inspecció Docker readonly confirma que la imatge històrica `695125…39d98` encara existeix localment, amb tag `diapora-composer/vega-proof:0.4.0` i sense registry digest. Aquest tag no s'ha adoptat ni modificat.

**Pas mínim per al coordinador/owner Vega:** establir una connexió de la versió acceptada amb identitat coherent i seleccionar explícitament, mitjançant el mecanisme suportat pel proveïdor, el renderer històric si es vol verificar aquesta procedència. Repetir `visualization_status`; només si retorna `fresh`, executar `visualization_check` per emetre el rebut natiu. Si el fingerprint continua diferint, l'owner ha de determinar-ne la causa i la via de migració. No s'ha re-renderitzat ni preparat un runtime nou.

`visualization_check` no s'ha executat perquè la comprovació prèvia nativa ja identifica una sortida obsoleta respecte de la selecció actual; no hi ha cap rebut nou d'èxit.

## Diavisuals

- Eines natives executades: `server_identity`, `compatibility_status` i `factory_manifest`.
- Instància: `1ccddd2b9ab346148f8b4feb8be76c24`; binding fix de consumidor i runtime efectiu `/home/benizar/git/tigit`.
- Versió carregada: **0.6.0**, mode development. Queda fora dels punts de rebut acceptats pel Web 0.7.1 seleccionat.
- Revisió carregada dels objectes de codi: `sha256:cb2aad166a3441200c511a85968b083aa0d25daed90be5e3f66843a94fcea8f1`.
- `current_disk.drift: true`; metadades de distribució actuals no disponibles; `metadata_matches_loaded_version: false`; `pinned_runtime_ready: false`. L'`ok: true` superior de l'eina d'identitat no elimina aquests findings.
- Perfil del renderer: `mermaid-11.16.0-plantuml-1.2026.1`, reportat com a suportat, sense drift del perfil. Imatge observada: `sha256:5a6887b372a0e1c386a7b54981d11ae1910215baeb6a12dfd0706b3e85ef0846`.

**Pas mínim per al coordinador/owner Diavisuals:** proporcionar una connexió coherent, fixada i vinculada a TIGIT, d'una versió seleccionada pel contracte vigent, amb evidència d'identitat/binding. Si l'owner necessita 0.6.0, correspon a Web i al coordinador provar i autoritzar aquella compatibilitat en una tasca de proveïdor; aquesta sessió no canvia pins ni allowlists. Després cal executar el `project_check` natiu sobre els outputs existents, sense render, i només retenir el rebut que realment produeixi.

`project_check` no s'ha executat amb aquesta connexió: no seria legítim substituir el rebut amb una versió que Web no accepta ni ignorar el drift. El fet que el check Web identifiqui els 23 diagrames com a `fresh` no equival a aquesta verificació nativa pendent.

## Gate i preservació

`site_check` s'ha repetit després del diagnòstic i continua amb `ok: false`: els apartats `visualizations` i `diagrams` rebutgen les metadades dels dos rebuts conservats. No s'ha desbloquejat el gate.

El baseline de preservació es desa a `tmp/tigit-12-svg-preview/baseline.json`. Protegeix 441 fitxers (96.875.155 bytes) d'`assets`, `_chapters`, `_documentation` i `_practices`, excepte els dos LLEGIU-ME autoritzats i la nova plantilla. El digest de l'inventari és `df0a49d28d0f34472e277819a8f2f8219f2a5a43d0f0ce2adbc6c78f5d80da2b`. Es calcula ordenant els paths Git versionats i no ignorats, i concatenant per fitxer `path + NUL + sha256(contingut) + LF`; els enllaços simbòlics es representen pel seu destí textual. També conserva els hashes dels dos rebuts, dels cinc controls d'update, de `.gitignore` i dels controls Vega.

El registre és una evidència de diagnòstic, no un rebut de proveïdor. Els checks emissors, la renovació dels rebuts i una eventual modificació de la selecció corresponen als passos acotats anteriors.

La comprovació posterior a la creació de la plantilla confirma els mateixos 441 fitxers, bytes i digest d'inventari. També coincideixen els deu hashes fixos del baseline i el HEAD. Això inclou els dos rebuts, els controls Vega i la figura conceptual `assets/img/infographics/grid-wireframe-composition.svg`; no s'han regenerat ni modificat els artefactes antics.
