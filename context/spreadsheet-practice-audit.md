# Auditoria inicial de les pràctiques de full de càlcul

Inspecció iniciada el 12 d'octubre de 2026, ampliada el 13, amb reproducció des de les fonts migrades el 14 i guies docents/Moodle 0.2.0 el 15, tasca [TIGIT #14](https://github.com/geourv/tigit/issues/14). Aquest document és context editorial i tècnic; no és una lectura de l'alumnat ni una aprovació dels lliuraments. El lot vigent de vuit lectures consta al final i s'enllaça a [l'índex local](../practiques/README.md).

## Decisions de l'autor

El primer lot és la pràctica 01, Preparació de dades. L'alumnat manté la plantilla i la descàrrega guiada del territori assignat; Tarragonès–Vila-seca continua sent la demostració docent. Se n'han preparat dues lectures catalanes `draft` i els seus PDFs amb el format estàndard d'unaltraweb. L'ampliació posterior cobreix indicadors, gràfics i el primer procés QGIS.

L'autor va acceptar inicialment una nova issue/branca i tres fonts: aquest document i les dues lectures 01. El 13 d'octubre va acceptar continuar abans de revisar els PDFs, amb deu paths addicionals. Aquella primera reserva de la branca `content/14-spreadsheet-practice-01` comprenia:

- `context/spreadsheet-practice-audit.md`
- `context/qgis-practice-plan.md`
- `practiques/tigit-01-preparacio-dades/ca/alumnat/LLEGIU-ME.md`
- `practiques/tigit-01-preparacio-dades/ca/docent/LLEGIU-ME.md`
- `practiques/tigit-02-indicadors-territorials/ca/alumnat/LLEGIU-ME.md`
- `practiques/tigit-02-indicadors-territorials/ca/docent/LLEGIU-ME.md`
- `practiques/tigit-03-grafics-territorials/ca/alumnat/LLEGIU-ME.md`
- `practiques/tigit-03-grafics-territorials/ca/docent/LLEGIU-ME.md`
- `practiques/tigit-04-qgis-mapes/ca/alumnat/LLEGIU-ME.md`
- `practiques/tigit-04-qgis-mapes/ca/docent/LLEGIU-ME.md`
- `.unaltracaptura-qgis-practice-04.yml`
- `practiques/tigit-04-qgis-mapes/captures/mapa-base.yml`
- `practiques/tigit-04-qgis-mapes/captures/coropleta.yml`

L'ampliació consta al [comentari de reserva](https://github.com/geourv/tigit/issues/14#issuecomment-6135210888), i el canvi de path de configuració QGIS al [comentari d'ajust](https://github.com/geourv/tigit/issues/14#issuecomment-6138932946). No s'ha autoritzat cap commit ni publicació abans de la revisió. Els resultats de prova es conserven fora de Git; els llibres, dades, figures i ZIPs de llegat no s'han substituït.

La reserva posterior de migració —118 retirades, 32 destinacions noves i 82 revisions— està acceptada a [TIGIT #14](https://github.com/geourv/tigit/issues/14#issuecomment-6154879170) i detallada a `context/practice-migration.md`. El 14 d'octubre s'han reubicat les 24 fonts útils a `practiques/tigit-projecte-territorial/` i s'han reconstruït els llibres en un run nou, sense substituir els XLSX originals de l'inventari següent.

L'actualització dels controls del lloc de 0.7.1 a 0.7.2 s'ha ajornat expressament. El MCP actiu és 0.7.2. `site_context` proposa Makefile, Gemfile, Gemfile.lock i `.unaltraweb/scaffold.json`, amb conflicte a `.gitignore`; no s'ha aplicat el pla. `site_doctor` assenyala el pin antic de Makefile i aquest conflicte. Els controls del lloc s'hauran de revisar en una tasca pròpia abans d'una construcció/publicació que els requereixi.

## Inventari del llegat auditat

En aquesta secció, `P` és `_practices/tigit-projecte-territorial` al commit base `715944fcbf5463e6dd48ade7696a251c94e8c2fd`. Els sis llibres originals de `P/data/processed` coincidien byte a byte amb els seus snapshots a `P/dist`. Després de la retirada autoritzada, aquests originals es conserven a l'arxiu de llegat verificat que identifica `context/practice-migration.md`, a més de l'historial Git.

| Fita | Destinatari del fitxer existent | Fulls | Fórmules | Gràfics | Taules dinàmiques |
| --- | --- | ---: | ---: | ---: | ---: |
| 01 inicial | Alumnat | 13 | 0 | 0 | 0 |
| 01 resolta | Professorat | 14 | 264 | 0 | 1 |
| 02 indicadors | Professorat | 17 | 682 | 0 | 1 |
| 03 visualització | Professorat | 33 | 1.080 | 9 | 2 |
| 07 color | Professorat | 34 | 1.323 | 9 | 2 |
| 05 transferència SIG | Professorat | 35 | 1.543 | 9 | 2 |

La seqüència tècnica és 01 → 02 → 03 → 07 → 05. Els prefixos es conserven i no s'han de confondre amb un calendari docent.

El llibre inicial no conté files de dades a `source_*`, `prepared_*` o `municipal`, ni respostes ocultes. Els sis llibres inspeccionats no tenen fulls ocults, macros VBA ni enllaços a altres llibres. La plantilla conserva `Tarragonès` i seleccions de demostració a les metadades: la nova lectura d'alumnat explica que cal adaptar-les al territori assignat.

## Proves efectuades

S'ha preparat un entorn temporal a `/tmp/opencode/tigit-spreadsheet-audit-20261012-01/venv`, amb Python 3.12 i `openpyxl==3.1.5`, segons `P/scripts/requirements.txt`. Els comprovadors s'han executat directament, sense invocar les dependències de regeneració de Make:

- `check_chapter_01.py`: correcte.
- `check_chapter_02.py`: correcte.
- `check_chapter_03.py`: correcte.
- `check_chapter_07.py`: correcte.
- `check_chapter_05.py`: correcte sobre el llibre i el CSV de transferència; no és una execució GIS.

Els controls existents comproven estructura, fórmules, elements seleccionats dels gràfics i integritat bàsica dels fitxers. No certifiquen totes les interpretacions estadístiques ni la qualitat visual d'una figura.

### Prova real amb LibreOffice Calc

Els sis llibres s'han obert i exportat en format XLSX amb LibreOffice Calc 24.2.7.2. S'ha utilitzat un perfil independent a `/tmp/opencode/tigit-spreadsheet-audit-20261012-01/calc-profile` i una destinació nova `calc-roundtrip` dins del mateix directori. Els originals conserven els SHA indicats més avall.

Les còpies conserven l'ordre i el nombre de fulls, el nombre de fórmules, els nou gràfics de les fites que en tenen i les taules dinàmiques. No hi ha errors de cel·la ni enllaços externs als resultats inspeccionats. No s'ha executat Microsoft Excel ni s'ha fet una revisió visual completa de les còpies: l'equivalència visual dels gràfics i el comportament de la interfície són comprovacions diferents.

Els originals 07 i 05 no tenien resultats de fórmula en memòria cau. Calc els ha recalculat a les còpies. Les 11 cel·les buides de la fita 03 i les 56 de les fites 07/05 són resultats de text buit (`t="str"`), com les etiquetes alternes d'anys o les files de paleta sense codi HEX; no s'han classificat com a errors numèrics. El procés ha informat de l'absència de `javaldx`, però ha completat les sis conversions i les comprovacions descrites.

### Límits de les dades

El cas docent conté 22 municipis, 2.244 registres de població per edat i 947 registres a cadascuna de les taules territorials generals importades. La taula municipal suma 262.868 residents, 169.179 habitatges totals i 66.105 no principals.

El control `C07` continua en revisió per la superfície publicada el 2025 respecte de població de 2021. A partir de la fita 02, `C14` manté la densitat provisional per aquesta mateixa causa. No s'han eliminat aquests avisos ni s'ha inferit compatibilitat només perquè les claus coincideixen. La preparació de població i habitatge tampoc no s'ha presentat com una mesura de l'activitat turística.

## Auditoria dels ZIPs de llegat

| Paquet | Fitxers | Contingut comprovat | Límit |
| --- | ---: | --- | --- |
| `assets/downloads/tigit-01-preparacio-dades-student.zip` | 3, més directoris | Plantilla inicial, README de treball i README de fonts; cap CSV ni solució. | No conté un LLEGIU-ME PDF estàndard. |
| `P/dist/course-packages/tigit-practiques-teaching.zip` | 68, més directoris | Cinc llibres docents, vuit CSV originals, derivats, figures, guies i scripts. | És acumulatiu; no és un paquet acotat a la pràctica 01 ni una edició nativa nova. |

Ambdós ZIPs passen el control CRC. No s'ha executat la regeneració del paquet extret. `scripts/build_packages.py` té destinacions fixes de llegat i obre els ZIPs en mode d'escriptura; `make packages` encadena snapshots i transferència SIG. No són ordres de revisió readonly i no s'han executat.

## LLEGIU-ME estàndard i següent empaquetat

`manual_authoring_capabilities` confirma lectures privades sota `practiques/<slug>/<lang>/<destinatari>/LLEGIU-ME.md` i PDF A4 apaïsat amb tipografia, metadades i logos compartits del manual. Les vuit fonts de les pràctiques 01–04 utilitzen aquesta convenció. Les instruccions d'alumnat acompanyen la plantilla, la descàrrega i la continuació del llibre propi; les lectures docents afegeixen els valors de control, els criteris d'intervenció i els límits del cas resolt.

La construcció d'un PDF de lectura no crea ni aprova una edició ZIP. El compositor `manual_practice_compose` 0.7.2 exigeix actualment una entrada GIS amb bundle, segell i verificador de productor, a més de les lectures aprovades. No es fabricarà un bundle GIS per passar aquesta barrera en una pràctica purament tabular. Abans d'una nova edició tabular normalitzada caldrà confirmar el contracte comú de packaging i la selecció de fitxers; els ZIPs antics continuen identificats com a llegat.

Per al futur paquet docent 01, l'inventari inicial acotat és la lectura docent, la solució 01 i les quatre fonts de la taula de material. Per a l'alumnat es manté la plantilla sense solució i el recorregut de descàrrega guiada. Les pràctiques 02/03 continuen el llibre propi de l'equip, no parteixen dels llibres docents resolts. La selecció definitiva dels paquets tabulars continua pendent; no s'han creat plantilles d'alumnat per a totes les fites ni s'han distribuït les solucions com a punts de partida.

## Hashes dels originals revisats

| Artefacte | SHA-256 |
| --- | --- |
| Llibre 01 inicial | `5a0639ded009dd52db3065f411d6e4fcf595dad25699d9e1579312107f7f69df` |
| Llibre 01 docent | `e046cc07bdc5b7085efd5874215b377bb56846424f0dbca7955f0b29ae9adebf` |
| Llibre 02 docent | `0b39340e29a85efb620d937bc5c39a5883fc967062ac1629350bb6f5fe0b548e` |
| Llibre 03 docent | `9550030f2e058f6f85f2e07ca0648d0adb9a8c79b22b034051a385ba3f1f9e0f` |
| Llibre 07 docent | `051f3e0b143cea5f562954615155ef55c1c551f3f77693a877f258fe910a9de4` |
| Llibre 05 docent | `958160b0dfec93040d1bc04ed9515c2664e0958c8d72c19cc56c1312bbe7d61d` |
| ZIP inicial alumnat | `37a9db86a40813e82239b167c82f63d62147c26c8e61caa4133d00d413fddb53` |
| ZIP docent acumulatiu | `d7a5cedd662d873ee5e88a3a23b8043059dbb851797e8572dd7074c0f7fd5a92` |

Les còpies de recàlcul i els PDFs de revisió no substitueixen aquests originals. Qualsevol aprovació de contingut, paquet o publicació correspon a l'autor després de revisar el resultat.

## Primer lot de lectures i PDFs 01, versió 0.1.0

Les dues lectures del primer lot passen `prose_check` amb `files_checked: 1` cadascuna, sense findings, issues ni warnings. Es mantenen `lang: ca` i `content_status: draft`. Aquelles execucions de `manual_practice_pdf_build` van retornar `ok: true`, `state: built` i `publishes: false`, amb el worker PDF immutable `sha256:618163d3f924439792b2306617bd9612f566c5881166102fa544b4e782d569fa`. El lot posterior a la migració i el vigent 0.2.0 consten als apartats finals d'aquest informe.

Els dos PDFs són A4 apaïsats de quatre pàgines, amb logos, metadades del curs, autoria, versió, numeració i peu «ESBORRANY». S'han inspeccionat les previsualitzacions inicials, el text de totes les pàgines i la taula de controls docent renderitzada. La primera prova duplicava el títol de la plantilla amb un encapçalament del Markdown; s'ha corregit la font, sense editar el PDF o el motor. Les taules de població i habitatge del professorat s'han unificat per comparar cada municipi en una mateixa fila i evitar una capçalera de continuació buida.

La preparació editorial `line` inicial va retornar revisió 0 i aquests lligams de font: alumnat, digest `5d854bfa537b4a818bd18cf3be7eebb64b38eba9473ef04febd98fe761dd38c8`, àncora `63e519c7f3a5831e891acc5a`; docent, digest `49b762a2139316eaf91c458fc5a3c351362c9fde874b3385eecc898cf5ba5071`, àncora `c363e0def8cfed5719e46669`. En tots dos casos, la cita exacta de la línia 8 era `# Preparació de dades territorials`. La duplicació s'ha resolt retirant aquest encapçalament redundant i establint les seccions al primer nivell del cos. Aquests digests descriuen la primera versió; els SHA vigents són els de la taula següent. La revisió d'agent no concedeix aprovació d'autor.

| Destinatari | SHA de la font del primer lot | SHA del PDF del primer lot | SHA del receipt natiu |
| --- | --- | --- | --- |
| Alumnat | `3e473c4951cdd1be85659735b72f5dc75965c035f7eb668ad94de079b691558c` | `5f196b4791e6950d444a27b1da39c1a76df2cb93d482e740b16b419dabc2f141` | `dd2b2b3e04750f45707e816055855f7ee35da8af9fd0d8bfbe1f022b0e8da83b` |
| Professorat | `49976abae0ac3ac93ec48f203d16a364cf24d358779c07fd844dfc7a2f3de688` | `068a10b504b5ecdecbdd0b5d8b5503dc9dc52c091ba4d2596b429378a2cc8c5c` | `adcb2c4f2cb625706981c2166c4ab36dce8893c0b107c0cad12554d65bfa0588` |

Ubicacions del primer lot, retingudes i relatives al repositori:

- `sandbox/practiques/tigit-01-preparacio-dades/lectura-0.1.0-ca-alumnat-alumnat-review-20261012-02/outputs/LLEGIU-ME.pdf`
- `sandbox/practiques/tigit-01-preparacio-dades/lectura-0.1.0-ca-docent-docent-review-20261012-03/outputs/LLEGIU-ME.pdf`

Cada job conserva la font capturada, els recursos, el PDF, la previsualització i el receipt. Les proves anteriors també es conserven, però no representen les fonts vigents. No s'han generat ZIPs nous ni s'ha publicat el lloc. La revisió humana dels dos PDFs i el contracte d'empaquetat tabular continuen sent els passos següents.

## Ampliació 02: indicadors territorials

Les lectures diferencien valor, format percentual i arrodoniment; documenten numerador, denominador, cobertura i absències, i mantenen C07/C14. La guia docent contrasta els indicadors de Vila-seca, Roda de Berà i la Pobla de Mafumet amb els agregats comarcals. El percentatge comarcal d'habitatge no principal és 66.105 / 169.179 × 100 = 39,0740%; la mitjana simple municipal és 35,7612%. La diferència és una qüestió de ponderació i pregunta, no un error automàtic de la mitjana.

La fita docent existent té 17 fulls, 132 fórmules de sis indicadors municipals i vuit mesures agregades, dins de les 682 fórmules totals. Les lectures no alteren el llibre ni eliminen incidències. La lectura d'alumnat explica com continuar la fita 01 pròpia, validar divisions i construir els resums.

## Ampliació 03: gràfics i finding visual

Les lectures cobreixen rangs vinculats, correspondència de codis, geometria, ordre, eixos, normalització, sèrie temporal, piràmide, histograma i exportació vectorial. El recompte de nou objectes del llibre existent no acredita totes les variants del nucli pedagògic: les barres agrupades i les apilades absolutes no tenen un full específic entre aquells objectes. Aquest límit queda explícit a la guia docent.

La inspecció de `P/outputs/figures/non-principal-housing-tarragones-2021.pdf`, SHA `75d45fb79d11a7e03f6f48245ba788e790a5d500cd93335dcf9a0bed427c70bb`, va detectar els títols d'eixos intercanviats. «Municipi» apareix sota l'eix numèric i la unitat percentual al costat de les categories. La figura conservada s'utilitza com a cas d'auditoria, amb peu explícit; no es presenta com a resultat final validat. La correcció no formava part de la reserva inicial de lectures, però s'ha executat en la continuació de la migració descrita més avall. El PDF històric conserva el hash al snapshot de recursos del dia 14.

Els controls de lectura inclouen 22 municipis; histograma amb recomptes 0, 4, 7, 3, 2, 4 i 2 als intervals de deu punts entre 0 i 70%; i parella de dispersió de Vila-seca (14,4858; 49,9053). La sèrie del Padró té 23 anys, 2000–2022, i 22.522 residents el 2021; la piràmide del Cens 2021 suma 22.781. S'explica que són operacions diferents i que no s'han de forçar a coincidir.

`image_background_check` marca el PDF de la figura com a `UW-IMAGE-UNVERIFIABLE` perquè l'inspector ràster no l'identifica. La figura es veu al PDF renderitzat i el productor privat n'ha segellat el binding, però això no és una comprovació automàtica d'opacitat del PDF. Les referències d'imatge de les lectures privades són relatives a l'arrel del consumidor: la primera prova amb `..` va ser refusada pel productor i es va corregir només la font Markdown.

## Primer lot de PDFs de les pràctiques 02/03

Les quatre lectures passen `prose_check` individualment sense findings, issues ni warnings; les dues docents s'han tornat a comprovar després dels darrers retocs. Els quatre PDFs són A4 apaïsats, versió 0.1.0, amb metadades del curs i peu ESBORRANY a totes les pàgines. Els resultats natius són `ok: true`, `state: built`, `publishes: false`.

| Lectura | Pàgines | SHA font | SHA PDF | SHA receipt |
| --- | ---: | --- | --- | --- |
| 02 alumnat | 4 | `404ccee8f9c213f77df75b16ff8956ed00076888ee5fb510d8b4a1807b4b5cf1` | `8926f80d2c79c229950192259d763283705773de81dfe253d3a53817495bfb8e` | `5db5f3036d98902bff2877265629f7762835c8b5221e351fec71d6a5999c7756` |
| 02 docent | 3 | `5785f683c8706913460325751a6f0e772aefe44c76356b93c1ed600dccae3771` | `d3c9de6ac10a9632a0b62c1e16184d8e148da7d8fbae7f5d070d259d591e55e8` | `d672cea7e506d34d44ab13282b129a0904c251abaffe8a2731514e01a5e1eaf5` |
| 03 alumnat | 4 | `f58e2979a7ae832e1ab7b1f27158f15835f6009eac481ba9d1bce68db3369507` | `7c928064663957498b043c9985606ce8afdc9bd2a88f452ce8307882904a736b` | `9758afd4e4d3b30a6ec9a1044853b1fbd6a2972e17fa28278e46929acf2bfa38` |
| 03 docent | 5 | `611a87eef322d3e6505045671051f7acc3172246c57f0c6ba0bed0fc908c8689` | `f9407300cd7983451757152e19bf08c0b8dc136c32e36ceca183a4f2814a2e44` | `fda6364854fd8d0b9d8ccb01bc5bae7b40940ebe1b401680efb0bbe9a7b1af88` |

Ubicacions del primer lot, retingudes i relatives al repositori:

- `sandbox/practiques/tigit-02-indicadors-territorials/lectura-0.1.0-ca-alumnat-alumnat-review-20261013-01/outputs/LLEGIU-ME.pdf`
- `sandbox/practiques/tigit-02-indicadors-territorials/lectura-0.1.0-ca-docent-docent-review-20261013-02/outputs/LLEGIU-ME.pdf`
- `sandbox/practiques/tigit-03-grafics-territorials/lectura-0.1.0-ca-alumnat-alumnat-review-20261013-01/outputs/LLEGIU-ME.pdf`
- `sandbox/practiques/tigit-03-grafics-territorials/lectura-0.1.0-ca-docent-docent-review-20261013-02/outputs/LLEGIU-ME.pdf`

S'han inspeccionat el text de totes les pàgines, les previsualitzacions i la figura d'auditoria. La primera guia docent 02 tenia un `Overfull` per un path inline llarg; separar el nom del llibre i la carpeta a la font l'ha resolt al run02. Els quatre logs vigents no contenen `Overfull`, errors LaTeX ni caràcters perduts; conserven avisos de plantilla TU/T1 i configuracions de captions no utilitzades. La taula d'inventari docent 03 continua entre les pàgines 1 i 2 amb capçalera repetida.

## Consolidació i recuperació de la sessió

Els resultats QGIS, les captures i els dos PDFs 04 consten a `context/qgis-practice-plan.md`. El nou bundle natiu 0.6.0 s'ha executat en una carpeta nova: no s'han convertit els bundles rc2 històrics en resultats d'un productor posterior ni s'han sobreescrit.

Després del reinici del 13 d'octubre es van verificar els vuit receipts d'aquell moment: 197 hashes d'artefactes i 36 referències d'entrada coincidien amb els fitxers. Aquells PDFs mantenien els SHA anteriors a la interrupció i les 13 fonts reservades encara eren noves, amb índex buit i fitxers versionats intactes. Aquesta observació és anterior a la migració. La branca continua basada en `715944fcbf5463e6dd48ade7696a251c94e8c2fd`; el 14 s'han actualitzat les fonts/receipts de 04 i reubicat el codi, tal com descriuen els dos informes de continuació. El preflight readonly informa `dirty-checkout` pel treball propi reservat; no s'ha fet stage per alterar-ne el resultat.

`manual_source_quality_check` manté els 63 avisos de dimensions del manual públic i cap issue; no acredita per si sol les lectures privades, comprovades explícitament. L'última CI de fonts aprovada correspon al HEAD versionat anterior, no a aquestes fonts encara untracked. L'actualització dels controls Web continua ajornada.

La revisió final de l'autor i la selecció d'edició precedeixen l'empaquetat admès pel productor, però no han bloquejat la continuació tècnica autoritzada. La prova nativa d'Excel, l'equivalència visual completa dels gràfics i la compatibilitat temporal C07/C14 continuen pendents. No s'ha concedit aprovació ni generat cap edició ZIP nova.

## Primera reproducció del 14 d'octubre des de les fonts migrades

El primer run complet és `sandbox/practiques/tigit-projecte-territorial/fulls/run02-contract-20261014/`, amb deu inputs raw verificats i 23 hashes de fonts a `run-inputs.json` (`91e4670f87cfd0c65ed4382db641d4c58cff9cf51f8f70016f7e57697a43b0c7`). El venv temporal del 12 d'octubre ja no era disponible; s'ha preparat un entorn propi ignorat `sandbox/practiques/tigit-projecte-territorial/venv-fulls-20261014/`, openpyxl 3.1.5 i et-xmlfile 2.0.0. S'han utilitzat Calc 24.2.7.2, Python d'UNO del sistema i Inkscape 1.2.2.

El Makefile nou s'executa des de l'arrel amb `make -f practiques/tigit-projecte-territorial/Makefile`. Han passat `workbook-inputs`, `workbooks`, `check`, `figures` i `check-figures`, amb RUN apuntant al directori anterior i PYTHON al venv. Les divuit proves de contracte també passen. Els targets de comprovació no regeneren llibres, i cada sessió de Calc utilitza el perfil propi del run. La reproducció no ha fet cap nova consulta estadística.

| Llibre nou a `data/processed/` del run | SHA-256 |
| --- | --- |
| `tigit-01-preparacio-dades.xlsx` | `3c3368f87f86482fa633aa559f85cdb60bc133fd04944c82b472085834445013` |
| `tigit-01-preparacio-dades-teaching.xlsx` | `b9cce19699edc33c0552a423d340157c05036068f45b32d84c2a64f0ba1c13b3` |
| `tigit-02-indicadors-territorials-teaching.xlsx` | `71ce97b5b482d96f21144afaccd1429e5af29ab1b0214ca52650214c8904db05` |
| `tigit-03-semiologia-visualitzacio-teaching.xlsx` | `17398c8727b1ceed15e4044c4acadcf1a62520ac58ecc961b7929431d197d93b` |
| `tigit-07-teoria-color-teaching.xlsx` | `2dc2028b89f7ed2cf745942a567129e6f262ffc37aa10bc299d97f6d745c35d0` |
| `tigit-05-integracio-sig-teaching.xlsx` | `7d6c4d0207c94a931708c3a9656a1dce370c40bcad087ef66ca01af5c7cff9fd` |

La comparació readonly amb l'inventari anterior confirma els mateixos recomptes de fulls, fórmules, gràfics i taules dinàmiques; cap full ocult, VBA o enllaç a llibres externs; plantilla inicial sense dades resoltes; i C07/C14 encara en revisió. Els valors de totes les columnes dels 22 municipis coincideixen amb el CSV retingut. Tant `municipal-indicators-tarragones-2021.csv` com el seu CSVT coincideixen també byte a byte, amb SHA `d762d55fbbfb085493fe3af39c9ae8e458c1422f41a4467a2f37202cc5f1baac` i `b2ac06038a8d40fa24e7cb9b53bdded5a96b402f56d839551a77d56c2a1373b1`. Els XLSX nous no s'han declarat byte-idèntics als originals.

Els exports són deu PDF i set SVG sota `outputs/figures/chapter-03/` i `chapter-07/` del run. Els comprovadors de mida/estructura passen. S'ha obert el PDF nou d'habitatge: conserva els títols d'eixos intercanviats. Els set SVG retornen `UW-IMAGE-TRANSPARENT`, alpha mínim 0, en la inspecció directa. Cal decisió d'autor sobre un fons apropiat i revisió de les fonts dels gràfics abans de considerar-los figures finals; no s'han pintat els outputs ni substituït la figura històrica inclosa a la lectura docent.

## Prioritat dels futurs capturadors Calc i Inkscape

La continuació més recent, amb eixos corregits i PDFs actuals, consta als apartats finals. La proposta de capturadors següent segueix sent treball futur de proveïdor.

Calc és el primer candidat perquè les pràctiques 01–03 depenen de passos que el llibre final no mostra: importació del codi com a text, selecció del rang, introducció i format d'una fórmula, construcció d'una taula dinàmica i configuració dels eixos. Un primer lot útil hauria de capturar aquests estats amb identificadors de llibre/full/rang i objectes UNO, conservar el fitxer natiu i produir PNG original més SVG d'anotacions editable. Els controls de fórmules, valors i caches s'han de distingir de la revisió visual del gràfic.

Inkscape pot seguir amb tres casos: inspecció de capes de la plantilla A3, importació d'un mapa/gràfic vectorial conservant proporcions i tipografies, i alineació/composició amb fonts i crèdits. Convé seleccionar objectes per ID i capes, conservar el SVG autoritatiu i registrar la versió, fonts i paràmetres d'exportació. Les anotacions han de reutilitzar el llenguatge dels capturadors existents.

Les operacions llargues necessiten estat i recuperació consultables, especialment arran dels timeouts observats en Web. La gestió comuna de sessió, recursos i retenció ha de seguir el runtime/SDK compartit de gaContExt quan estigui disponible; no s'ha de copiar un gestor genèric dins de TIGIT o de cada capturador. Aquest és un abast proposat, no una afirmació que els dos MCP ja estiguin implementats.

## Correcció d'eixos i retirada del llegat substituït

L'autor ha demanat continuar sense una revisió intermèdia. S'han corregit els gràfics editables d'habitatge i composició d'edats a `prepare_chapter_03.py`: `x_axis` en BarChart designa l'eix de categories, encara que les barres es dibuixin horitzontals. Els títols dels municipis i dels percentatges s'havien intercanviat en tractar els noms de l'API com a orientacions de pantalla. Els comprovadors 03 i 07 incorporen aquest control i els exports PDF de consulta mostren la correspondència correcta.

El run vigent és `sandbox/practiques/tigit-projecte-territorial/fulls/run04-eixos-20261014/`; `run-inputs.json` té SHA `de619f1a329323fffc6a76c3213c6759bb60adc1e114772f41429950a93c5d57`. Run03 conserva l'intent que va superar el límit agregat de 300 segons de la comanda, amb els llibres acabats i l'última parella PDF/SVG de color pendent. Run04 ha completat totes les fases amb temps suficient, sense sobreescriure l'intent anterior.

| Llibre vigent a `data/processed/` | SHA-256 |
| --- | --- |
| `tigit-01-preparacio-dades.xlsx` | `2b6c436d9f553ce57153d8b64dbebb5797f309df884c23f0a6e0ebe9ea9fdf02` |
| `tigit-01-preparacio-dades-teaching.xlsx` | `b8223030348cb0ef6243279994a2ac9b3323fca067ced2a8bb1165fa9ebc73ba` |
| `tigit-02-indicadors-territorials-teaching.xlsx` | `fa8cbfa038b1e63467b60f94d155ad96864c00edec167f5eb782437aa372bd61` |
| `tigit-03-semiologia-visualitzacio-teaching.xlsx` | `8712dd7345a2c5036da797309f602a76df0171d9186019e831a904ec9d09676d` |
| `tigit-07-teoria-color-teaching.xlsx` | `f7ca99caaf1283fdb90efde31378aadf6361301e57904f8a116ba7df7753febe` |
| `tigit-05-integracio-sig-teaching.xlsx` | `e8a97fbc20e2b28503ed5d4721ce8476f46857c34139cee702a18d41abd1abcd` |

Les divuit proves i els cinc comprovadors passen; s'han contrastat novament els deu inputs, les 23 fonts, els recomptes dels sis llibres i tots els camps dels 22 municipis. Es mantenen C07/C14. Els deu PDF i set SVG d'exportació existeixen i passen els controls; els eixos s'han inspeccionat en els PDF, inclosa la prova cromàtica. El mostreig del SVG cromàtic d'habitatge de run04 continua detectant transparència, alpha mínim 0; no s'ha aplicat cap fons automàtic.

S'han retirat 104 paths de la reserva de 118. Els originals estan conservats byte a byte a l'arxiu `llegat-715944f-20261014.tar` dins del sandbox del projecte, SHA `dfe882b23fc2c664e810242840d3e011df09df32e017b4b883249e3e601174ab`. Resten els 13 inputs de Quarto/Vega i el ZIP inicial públic. El PDF històric d'auditoria és ara un dels 21 recursos fixats i la lectura docent 03 el referencia des de `sandbox/practiques/tigit-projecte-territorial/recursos/2026-10-14/outputs/figures/`, sense canviar-ne els bytes.

## Lot històric 0.1.0 després de migrar rutes i configuració

Les lectures docents 01–03 ja usen els noms `-teaching` dins de `data/processed` de l'execució, en lloc dels snapshots antics a dist. La 03 diferencia l'exportació històrica amb error de la solució de consulta corregida. Totes tres passen `prose_check` amb cobertura real; el pass line de 03 s'ha preparat amb digest `f555a208b6c0a3ec9678323f4a2a065a1259b19238981e46cad5f32d8ac3ba9b`, sense enregistrar aprovació.

En retirar el mapping antic d'`_config.yml`, el productor refusa reutilitzar un run amb aquella configuració anterior. S'han reconstruït les vuit lectures, encara `draft`, amb run `migracio-20261014-01`, versió 0.1.0 i el mateix worker immutable. Patró de path: `sandbox/practiques/<slug>/lectura-0.1.0-ca-<destinatari>-migracio-20261014-01/outputs/LLEGIU-ME.pdf`; cada directori conserva el seu `receipt.json`.

| Pràctica / destinatari | Pàgines | SHA PDF | SHA receipt |
| --- | ---: | --- | --- |
| 01 alumnat | 4 | `5f196b4791e6950d444a27b1da39c1a76df2cb93d482e740b16b419dabc2f141` | `f3677aec0621283a517653fba3b17f6703ff6e129f731fbd2a7f8f9a7ef1e65c` |
| 01 docent | 4 | `ad5d70eb99a078d91a8efb290498f3e793eb0f52252612e2caa7c8da68b0ccde` | `6c757f3e5dbb3b9808bd9ece6a9d4908841b4ca12d467e3f30df1a513d1765cb` |
| 02 alumnat | 4 | `8926f80d2c79c229950192259d763283705773de81dfe253d3a53817495bfb8e` | `d019fb169fbd805aedcaa2a87f815b3cd96f4ec40c7d54e6f00213ad5d0707e7` |
| 02 docent | 3 | `34cefd2937b233fdca143d00380d8307fb713f90c0fcb86ae9b958de7d4c4d52` | `5cfd3ca472a2d50ef4ff633aed76c17a593ebe3b61b195767a1de38a8ccdb5df` |
| 03 alumnat | 4 | `7c928064663957498b043c9985606ce8afdc9bd2a88f452ce8307882904a736b` | `49b880d629b2cb382bf1b4d0f8a5c24213270aa97f999873f2a9dab483ae3114` |
| 03 docent | 5 | `62fbb02d1573b0653a4510d1f7cdad082bf4b0ffa81e5e1bfb2f4b513721a394` | `228dfb7c89ddc6f2e541cfe56053f354c192ac28c05f8e6b5be048bdeb4514ea` |
| 04 alumnat | 5 | `cd1cf62fa372c861492241a80fb950dccfe9597372522c33e32bd82f57a10e4c` | `914781ee99aa0d648ed0f59b9fa6ddf492e412d1011bcc7256cd4b4dc31f5290` |
| 04 docent | 5 | `a7d5c4e8a8ee95a7723de68cd76100234ee2ce9671cedb4dea62121f2c4ec98f` | `ac3638590c732166e98842ad2f43d9ee2c6256f97fdc5ec7be99ad48bd6f3425` |

Fonts docents modificades: 01 `13cf21a906a4e01e893d7cf8686ee5aa0b9eb2636c5a9b5af38cb5ec25f9a648`; 02 `0511680bf1c4397fe56541c0956937ba7550fa0db12203c71f6a08c3a489d8a7`; 03 `2966a358b32b211f088f3ffe7012bb7770e646ad13f0e53e60d584ace4edde4b`. El 14 d'octubre es van verificar els 197 artefactes i les 36 referències d'entrada dels rebuts contra els fitxers vigents aleshores, inclosa la configuració. Els PDFs són A4 apaïsats amb ESBORRANY a totes les pàgines i sense Overfull, errors LaTeX o caràcters perduts als logs. Els tres docents modificats es van obrir i inspeccionar; els altres cinc PDFs eren byte-idèntics als anteriors. El lot queda com a evidència històrica després de la revisió 0.2.0.

## Guies docents i Moodle — revisió 0.2.0 del 15 d'octubre

L'encàrrec del 15 d'octubre adapta el patró docent de TIG a primer curs de Gestió en Turisme i Hoteleria, TIGIT 21224102. La [reserva de continuació](https://github.com/geourv/tigit/issues/14#issuecomment-6200474177) identifica tretze paths: les vuit lectures, l'índex, els tres informes i `context/writing-profile.md`, única ampliació de reserva explícitament demanada per l'autor. Les referències de TIG s'han consultat readonly. El perfil de redacció incorpora el patró durador «Guies de pràctiques, conducció docent i Moodle».

Cada docent incorpora preparació, materials, durades estimades, aturades, preguntes de discussió, errors habituals, encaix de la qualificació, «Preparar Moodle» i un «Enunciat per copiar a la descripció» autònom. El bloc copiable identifica pregunta/entrades, quatre apartats B, dues ampliacions, productes, controls i qualificació; les instruccions de configuració de la Tasca queden fora del bloc. Es mantenen les demostracions tècniques anteriors, els equips i els territoris assignats. Les lectures d'alumnat expressen la mateixa selecció, continuïtat, ampliacions i criteris de lliurament.

La qualificació interna és 70% bàsic, 20% ampliacions i 10% documentació: màxims de 7, 2 i 1 punts, no automàtics. Bàsic i documentació complets poden arribar a 8/10 sense ampliacions. Una aportació es valora una sola vegada; una ampliació seleccionada com a obligatòria entra al bàsic. El professorat anuncia els obligatoris a classe i els enumera a Moodle, preservant les entrades de continuïtat o identificant una preparació del mateix territori. Una comparació petita ben contrastada pot satisfer el bloc d'ampliacions; acumular fitxers no garanteix punts.

S'ha contrastat la [guia oficial URV 2026/27, avaluació](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&fitxa_apartat=61&any_academic=2026_27): activitats TIC d'aula 5% conjunt, presentacions/síntesi 30%, seguiment 5%, proves mixtes 30% i proves pràctiques 30%. El 70–20–10 és la rúbrica interna sol·licitada, no un percentatge prescrit per aquesta guia ni un 5% de curs per a cada pràctica. La [planificació oficial](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&fitxa_apartat=58&any_academic=2026_27) preveu 22 hores TIC d'aula i 20 autònomes; les estimacions següents cobreixen només aquestes quatre pràctiques i expliciten supòsits i exclusions, sense mesurament amb alumnat ni dates de calendari.

| Pràctica | Aula | Treball autònom per estudiant, en equip | Preparació docent |
| --- | --- | --- | --- |
| 01 | 150–180 min | 90–150 min | 45–60 min |
| 02 | 120–150 min | 60–90 min | 30–45 min |
| 03 | 120–150 min | 90–150 min | 30–45 min |
| 04 | 180–240 min | 90–150 min | 45–60 min |

Les ampliacions són comparacions controlades amb pregunta, variació, referència, comprovacions i interpretació:

- 01: importació automàtica/controlada del mateix CSV; duplicat i omissió en còpies separades de prova.
- 02: mitjana simple/ponderada i ràtio de sumes; residents per habitatges totals/principals.
- 03: barres apilades absolutes/100%; histograma d'intervals de 10/20 punts percentuals amb domini, límits i absències controlats.
- 04: quantils/intervals iguals amb les altres decisions constants; tres/cinc classes, o parella admissible si hi ha pocs valors diferents.

Es conserven C07/C14, els límits 2021/2025/2026 i la distinció entre habitatge no principal i activitat turística. Les guies identifiquen la plantilla inicial o la fita pròpia com a punt de partida; els llibres `-teaching` i els projectes resolts són materials de preparació docent. La configuració efectiva de Tasques, grups, dates i trameses correspon al professorat a Moodle.

### PDFs i integritat del lot

Les vuit lectures passen `prose_check` individual, `ok: true`, `files_checked: 1`, incloses les darreres correccions de paginació. `manual_practice_pdf_build` ha generat jobs nous 0.2.0 amb el mateix worker immutable, `state: built` i `publishes: false`. Totes les fonts mantenen `lang: ca`, `content_status: draft` i el codi 21224102. Les metadades de portada continuen sent les compartides del manual, que inclou les guies de Geografia i Turisme; l'adaptació del text és a Turisme 21224102.

Patró de path: `sandbox/practiques/<slug>/lectura-0.2.0-ca-<destinatari>-<run>/outputs/LLEGIU-ME.pdf`. Cada job conserva el seu `receipt.json`. [L'índex local](../practiques/README.md) enllaça les fonts, els vuit PDFs vigents i els materials de demostració; els PDFs de sandbox són locals i ignorats, no descàrregues publicades.

| Lectura | Run | Pàgines | SHA font |
| --- | --- | ---: | --- |
| 01 alumnat | `moodle-20261015-01` | 6 | `481f2742a88361c3952d364d7646fc3bcb4201644b87586cdec56c1e740e0b16` |
| 01 docent | `moodle-20261015-01` | 8 | `9cc9714fe107c2f55faee74493070cc0fd9cb056a82a9df7e73be89512163d0b` |
| 02 alumnat | `moodle-20261015-02` | 5 | `99b168ed5ab73f5c68a69d8280f5c1a03f045f0fb36f83fc0c3f987ddc48df3d` |
| 02 docent | `moodle-20261015-01` | 7 | `276a34e994c2f0c7c023eeaf842b91b01389e2d78f5c60637e8a8261acc6b593` |
| 03 alumnat | `moodle-20261015-03` | 5 | `1169b72dcc9d6e35fab89ac9e8a49fd7b688e1f07cb0490def6a8a103d78ff1c` |
| 03 docent | `moodle-20261015-01` | 9 | `4a4db55e1ce4c86458c16fd221134c1ce4eb8e1fe17a4b8d5b8c0cdc6e14b350` |
| 04 alumnat | `moodle-20261015-02` | 7 | `6bdc30fa7f365f9b3c769456e6efd60b59ad8740475690945f4d3732aa5538fd` |
| 04 docent | `moodle-20261015-01` | 9 | `1e6dd9fc552fa11e6a4e5b6f2289b36c0e4ddd65dfa32889868bee67bf46b951` |

| Lectura | SHA PDF | SHA receipt |
| --- | --- | --- |
| 01 alumnat | `7137f2fc85a8662935031b542304d5930f15114c091fa0279e9b5510a9a5cdde` | `fbd2b0a6d1865407e7218842b391e3ead44200effe99ed51aa7012caba19287f` |
| 01 docent | `9807c84a7b2513eb8451a457200b474fdc74b126707b42b9cf46243d93943248` | `1e9dbca77f3d4e92fc20aa5cf956af2e59ae847e547fb20a03131e99991e5f8a` |
| 02 alumnat | `d6b0ee5bf150a2009c4c39a771b80ddfc0a4c07deec657ac2a898326ff91f758` | `6fc3ce664f4d3763f71c7a23caaf3aa88b4eb5fbcc4daddfa5ea653e6c659361` |
| 02 docent | `ee8913d39cf94000c424bc69b279a3cbb8812ef610845fd239de42325c7990b1` | `747842f9b3cddbe6246453aacf0e5b5d6838265d06bf791a04beb5e7b119a812` |
| 03 alumnat | `1cad67aa5ccbd66abd5fe409774b2cba6459f529ad71fad7d5d213ca8fb93b2a` | `c987b03e38cbe8b889c8c81845734cc40dcfb20f2d85bcb10d470e9798d974ab` |
| 03 docent | `867c132fd1fc17eef0d674334fc57c6ae3edf5ef9cd7b8a394184ab2d76e4753` | `88f2abffb16ff050aab6e767b84d01cf5c4d44ebf370416e0e54ba7255eaf005` |
| 04 alumnat | `c72ffea82b9a02420de03eb1621dac363b7ba2c03d922292c2346608e5580357` | `9ffb78906fb9c467e5be3c3416d98919007b75f9adb13e6ee4b136f7cac9b9e9` |
| 04 docent | `e5049e496e9aa04171b383b05d8724908f3cb8ef9cfe82dc65026f3afa179ffd` | `3dba206eb16d1d777e87d7e91d53a86aa9b1aea49d7895a4293a749b09cb8b21` |

La comprovació readonly del lot confirma 197 artefactes i 36 referències d'entrada, incloses les fonts vigents, configuració i imatges. Els vuit PDFs són A4 apaïsats, amb ESBORRANY a totes les pàgines, percentatges i 8/10 presents; els docents contenen els camps Moodle previstos. No hi ha Overfull, errors LaTeX ni caràcters perduts als logs i les caixes de totes les paraules extretes queden dins de la pàgina. Això no substitueix una revisió visual completa.

S'han inspeccionat visualment les pàgines 3–5 dels quatre docents i la pàgina final de cadascun dels quatre PDFs d'alumnat. Les fonts d'alumnat 02/04 es van compactar per evitar una pàgina quasi buida; en 03 la rúbrica es va passar a llista i es van integrar resultats/lliurament per mantenir la secció final cohesionada. La darrera pàgina de 03, run03, s'ha revisat després d'aquests ajustos. Els intents anteriors i tot el lot 0.1.0 queden retinguts amb els seus rebuts originals, que descriuen les fonts d'aquell moment.

El comprovador temporal és `/tmp/opencode/tigit-moodle-pdf-check-20261015.py --summary`; les evidències locals retingudes són els jobs i els seus receipts. Aquest lot és una revisió de guies i PDFs: reutilitza els llibres de run04, el procés QGIS run05 i les captures run03. Continua pendent la revisió humana del resultat, així com els límits de dades, compatibilitat Excel, fons i contracte d'empaquetat ja descrits.

## Lliurament autoritzat del 18 d'octubre

L'autor ha confirmat que ha revisat el manual i els PDF i ha autoritzat explícitament publicar i lliurar aquesta versió de treball, amb la indicació ESBORRANY. L'autorització de commit, PR, fusió i Pages consta a [TIGIT #14](https://github.com/geourv/tigit/issues/14#issuecomment-6253802016). Les fonts continuen `draft`; la distribució de treball no és una aprovació d'edició definitiva ni de guia docent oficial.

La configuració final exclou la demo de tema Plotly de la publicació mitjançant `defaults/published: false`, preservant tots els defaults del core. `_config.yml` té SHA `d70e5c43e2f7706d0f8ec31b651115f3868dc4dbef56d8d091e5f4b40f02cdd0`. S'han reconstruït les vuit lectures amb run **`pages-20261018-02`**, versió 0.2.0, i els seus PDF són byte-idèntics als revisats el dia 15: mateixes fonts, pàgines i SHA PDF de les taules anteriors. Els rebuts vigents són:

| Lectura | SHA receipt de `pages-20261018-02` |
| --- | --- |
| 01 alumnat | `cd2d7b8f89b2722d1bd3f5b22704a0f9161f236787aa04417c29cae860cbcb2e` |
| 01 docent | `e2c7707e25b2b75a5a2abbd724ce822588fb1e447818c79618e1a042cca6ff4c` |
| 02 alumnat | `3e45c67ebef13eada0628d2b9f35b6447e30ab4d3e75b87d9ff11ab7ff4a71d8` |
| 02 docent | `b3316e274400ff4e98113b3df421f1bf472faae9f84dc78b33eef0c5a234926f` |
| 03 alumnat | `ecd6be053a8f69a60ef8a8a5e2d6a1e936b7c53c85a93ed15dd987e72850a89b` |
| 03 docent | `10cf2ea08f7b58f40b7229bdea311a0d67fdb610fad30dddd61391b69131fff7` |
| 04 alumnat | `4a3fd368ee274c3c259f92798bebf0ff8fceed2088bac59c9e6ce138ce3c0704` |
| 04 docent | `bd8a8815a9f059baf2dba69387a960b8fe701bc7f5a0efafaa2167117170bfd8` |

La verificació confirma novament 197 artefactes i 36 referències d'entrada vigents, A4 apaïsat i logs sense errors de composició. Les divuit proves de reproducció també passen. El primer intent `pages-20261018-01` es conserva amb la configuració anterior; ni els seus rebuts ni els dels dies 12–15 s'han modificat.

La carpeta `sandbox/practiques/moodle-2026-10-18/`, oberta amb `xdg-open`, conté cinc adjunts a `PER-PUJAR-A-MOODLE`: quatre PDF d'alumnat i la plantilla 01 buida de run04. `PROFESSORAT` conté els quatre PDF docents, cinc llibres resolts i la còpia íntegra del bundle QGIS. Les 138 còpies s'han verificat per SHA; `manifest-fitxers.json`, SHA `2956a8b1eb855b15a07419c1fb4334621323fdb79371b7f5e2c76a19ed7623a0`, registra les fonts de còpia, i `OBRE-AQUI.html` explica els adjunts. Els PDF copiats de run01 també coincideixen amb els de run02, vinculats a la configuració final.

Les pràctiques 02/03 continuen els llibres propis dels equips. A 04 cal afegir les bases geogràfiques dels territoris assignats; el bundle del Tarragonès és el cas docent, no un paquet per a tots els equips. S'han lliurat fitxers individuals i el bundle íntegre: no s'ha fabricat una edició tabular amb GIS ni un ZIP de productor fictici. El SHA publicat i l'execució de Pages es registraran al retorn de la issue.
