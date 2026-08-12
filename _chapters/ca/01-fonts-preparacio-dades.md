---
layout: manual-chapter
title: Fonts i preparació de dades territorials
description: Criteris per localitzar, verificar, obtenir, documentar i preparar dades estadístiques i geoespacials.
lang: ca
ref: manual-data-sources-preparation
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/fonts-preparacio-dades/
weight: 20
part: Continguts
manual_references: true
---

Les dades no apareixen preparades per respondre una pregunta. Són el resultat d'una observació, una enquesta, un registre administratiu, un sensor o una elaboració estadística; després es publiquen amb unes definicions, una cobertura, una data i unes condicions d'ús determinades. Abans de calcular o representar res, cal saber qui les ha produït, què mesuren realment i quines transformacions necessiten.

Aquest capítol recorre tot el procés. Primer es distingeixen els tipus de font i els criteris de qualitat. Després es presenten organismes i portals a diferents escales, des de les fonts mundials fins a les catalanes. Finalment, s'expliquen les formes d'accés i el procés de preparació que converteix un fitxer descarregat en una taula analitzable. Excel serà el primer entorn de treball, però els principis són aplicables a qualsevol eina.

## Preguntes i dades

### La pregunta precedeix la cerca

Una cerca sense pregunta acostuma a produir una acumulació de fitxers, no una base d'anàlisi. Abans d'obrir un portal convé formular què es vol saber i precisar almenys cinc components:

1. **El fenomen:** població resident, oferta d'allotjament, arribades, pernoctacions, despesa, ocupació, mobilitat o coberta del sòl, entre d'altres.
2. **La unitat d'observació:** una persona, un establiment, un municipi, una comarca, una regió, un país o una cel·la ràster.
3. **L'àmbit territorial:** quins territoris s'inclouen i a quin nivell geogràfic.
4. **El període:** un instant, un mes, un any, una temporada o una sèrie temporal.
5. **La mesura:** recompte, percentatge, mitjana, índex, taxa, superfície o una altra unitat.

No és equivalent preguntar quants establiments estan inscrits en un registre, quants estan oberts, quantes places ofereixen o quantes pernoctacions han registrat. Tampoc no és equivalent comptar turistes, viatgers, arribades, visites, passatgers o pernoctacions. Una font pot ser oficial i de qualitat i, malgrat això, no servir per respondre la pregunta formulada.

### Les dades no són els fets mateixos

Una dada és una representació codificada d'algun aspecte de la realitat. Entre el fenomen i la cel·la d'una taula hi ha decisions: què es considera turista, com es recull la resposta, com es tracta una absència, quin territori s'assigna a l'observació i quan es revisa la sèrie. Per això no existeixen dades completament «crues» en el sentit d'estar lliures de decisions prèvies. Sí que es pot parlar de **dades originals del projecte** per designar la còpia rebuda o descarregada abans de modificar-la.

La qualitat no consisteix només a evitar errors numèrics. També exigeix que les dades siguin adequades per a l'ús previst, que les definicions siguin clares i que el procés pugui reconstruir-se. Els principis fonamentals de l'estadística oficial de les Nacions Unides vinculen la confiança pública amb la imparcialitat, els mètodes científics i la transparència sobre fonts i procediments {% cite unitedNationsFundamentalPrinciples2014 %}. El Codi de bones pràctiques de les estadístiques europees concreta aquests compromisos en dimensions com la rellevància, l'exactitud, l'oportunitat, la coherència, la comparabilitat, l'accessibilitat i la claredat {% cite europeanStatisticalSystemCodePractice2018 %}.

## Tipus de fonts

### Fonts primàries i secundàries

La distinció entre font primària i secundària depèn de la pregunta i del procés de producció, no només del prestigi de l'organisme que publica.

Una **font primària** conté observacions o registres obtinguts directament pel productor per al fenomen estudiat. Ho poden ser les respostes individuals d'una enquesta, les altes d'un registre d'establiments, una imatge Sentinel captada per un sensor o les observacions d'una estació meteorològica. Una entrevista pròpia també és una font primària, encara que no sigui estadística oficial.

Una **font secundària** reorganitza, resumeix, interpreta o redistribueix informació produïda prèviament. Una taula d'Eurostat pot harmonitzar dades aportades pels instituts estadístics nacionals; un informe turístic pot combinar INE, Idescat i registres administratius; un article periodístic pot reproduir una xifra publicada en una nota de premsa. La font secundària pot aportar comparabilitat i context, però cal poder arribar fins al productor i la metodologia originals.

També es poden trobar **fonts terciàries**, com repertoris, enciclopèdies, cercadors o respostes generades automàticament, que ajuden a localitzar conceptes i recursos. Són punts d'entrada, no evidència suficient per si mateixos.

::: table "Primària o secundària segons la pregunta"
| Material | Si s'estudia... | Paper de la font |
| --- | --- | --- |
| Registre de Turisme de Catalunya | Nombre d'establiments inscrits | Primària: és el registre administratiu original |
| Informe que resumeix el registre | Evolució dels establiments inscrits | Secundària: interpreta dades del registre |
| Publicacions d'una xarxa social | Discurs dels visitants a la xarxa | Primària: les publicacions són l'objecte d'estudi |
| Publicació viral que afirma una xifra d'ocupació | Ocupació turística real | No és evidència suficient: cal trobar la font original |
| Resposta d'un model de llenguatge gran (LLM) | Definició o valor estadístic | Font terciària de descoberta: cal verificar-la externament |
:::

### Segons el procés que les produeix

Una altra classificació útil diferencia les fonts per la manera com es genera la informació:

- **Estadístiques:** censos, enquestes, estimacions i estadística derivada, amb metodologia, univers, mostra i procediments de qualitat documentats.
- **Administratives:** registres creats per gestionar permisos, impostos, establiments o serveis. Poden tenir molt detall, però representen l'activitat administrativa, no necessàriament el fenomen complet.
- **Geoespacials de referència:** límits, xarxes, toponímia, ortofotos, models d'elevació i bases topogràfiques mantingudes per organismes cartogràfics.
- **Observació de la Terra i sensors:** imatges de satèl·lit, LiDAR, estacions meteorològiques, comptadors o dispositius. La resolució, el calibratge i el nivell de processament són part essencial de la dada.
- **Recerca:** dades produïdes en projectes científics. Cal examinar el disseny de la recerca, el repositori, la documentació i la llicència.
- **Col·laboratives o generades pels usuaris:** OpenStreetMap, ressenyes, fotografies o publicacions socials. La cobertura i els criteris poden ser desiguals, però poden ser valuoses si la pregunta i el mètode ho justifiquen.
- **Comercials:** telefonia, transaccions, reserves o mobilitat. Poden oferir detall i actualitat, però solen tenir restriccions, biaixos de cobertura i metodologies no auditables completament.

La categoria no determina automàticament la qualitat. Un registre administratiu oficial pot contenir duplicats; una font col·laborativa pot estar molt actualitzada; una enquesta rigorosa pot no ser representativa a escala municipal. El que cal és avaluar l'adequació concreta de cada font.

## Verificar abans d'utilitzar

### Autoritat no significa infal·libilitat

Cal prioritzar fonts que identifiquin un productor responsable, publiquin metodologia i permetin obtenir les dades i les metadades. Els organismes estadístics i cartogràfics oficials ofereixen garanties institucionals importants, però les seves dades també contenen revisions, estimacions, canvis de classificació, errors rectificats i limitacions d'escala. La verificació no consisteix a preguntar només «és oficial?», sinó també «és adequada, comparable i prou documentada per a aquest ús?».

Una xifra trobada en una xarxa social, en un pseudomitjà, en una infografia sense crèdits o en una resposta d'un **model de llenguatge gran** —LLM, de l'anglès *large language model*— no s'ha d'incorporar directament a una anàlisi. Primer cal localitzar-ne l'origen, comprovar si la publicació original existeix, llegir-ne la definició i contrastar-la. Un LLM pot ajudar a proposar paraules de cerca, explicar un format o esbossar una consulta, però no és el productor de les dades ni garanteix que un valor, una URL o una citació siguin reals.

Hi ha una excepció metodològica important: si la pregunta estudia què es diu a les xarxes o què respon un LLM, aquests continguts poden convertir-se en dades primàries de la recerca. En aquest cas encara cal definir la mostra, el període, el model o servei, les limitacions, l'ètica i el procediment de recollida. Estudiar un rumor no converteix el rumor en un fet.

![Circuit de verificació d'una font]({{ site.baseurl }}/assets/diagrams/data-source-verification.mmd "Circuit de verificació: de la pregunta i el productor fins a la còpia original documentada")

### Una pauta de verificació

Abans de descarregar convé completar una fitxa breu de la font:

::: table "Preguntes per verificar una font"
| Dimensió | Pregunta de control | Senyal d'alerta |
| --- | --- | --- |
| Productor | Qui ha creat les dades i qui només les cataloga? | No es pot identificar l'organisme responsable |
| Finalitat | Per què i com es van recollir? | Es presenten xifres sense metodologia |
| Definició | Què representa cada variable? | S'utilitzen termes com *turista* o *plaça* sense definir-los |
| Cobertura | Quin univers, territori i període cobreix? | Es generalitza una mostra o una zona a tota la població |
| Qualitat | Hi ha flags, errors mostrals, revisions o valors imputats? | Només es mostra el resultat més favorable |
| Comparabilitat | Han canviat conceptes, codis o límits? | Es concatena una sèrie malgrat una ruptura metodològica |
| Actualitat | Quina és la data de referència i d'actualització? | Es confon la data de publicació amb el període observat |
| Accés | Es poden obtenir dades i metadades reutilitzables? | Només hi ha una captura o un gràfic sense valors |
| Llicència | Què es permet reutilitzar i com s'ha de citar? | «Gratuït» s'interpreta erròniament com «obert» |
| Coherència | El resultat concorda amb altres fonts o publicacions? | Una diferència gran no es pot explicar |
:::

### Metadades, procedència i llicència

Les **metadades** expliquen les dades: títol, productor, definicions, unitats, cobertura, periodicitat, classificacions, sistema de referència espacial, qualitat, data d'actualització i llicència. No són un complement opcional. Sense metadades, un valor com `82,4` no permet saber si representa un percentatge d'ocupació, milers de viatgers o euros per habitació.

La **procedència** o traçabilitat descriu d'on prové cada resultat i quines activitats l'han transformat. Els principis FAIR destaquen que les dades han de ser localitzables, accessibles, interoperables i reutilitzables, amb identificadors, metadades, procedència i llicències clares {% cite wilkinsonFAIRGuidingPrinciples2016 %}. En un treball del curs, això es concreta conservant:

- el nom del productor i del conjunt;
- l'URL de la fitxa i, si és diferent, l'URL de descàrrega o consulta;
- la data d'accés i el període de referència;
- la versió o data d'actualització;
- els filtres i paràmetres aplicats;
- el fitxer original sense alteracions;
- la llicència i la fórmula d'atribució;
- una relació de les transformacions efectuades.

**Dades obertes** no significa simplement dades visibles o gratuïtes. L'obertura requereix una llicència que n'autoritzi la reutilització. Un visor públic pot no permetre descarregar objectes; un recurs gratuït pot prohibir l'ús comercial o la redistribució; un catàleg obert pot enllaçar conjunts amb llicències diferents.

### Tres exemples de metadades

Les metadades poden aparèixer en una pàgina metodològica, una fitxa de catàleg, la capçalera d'un fitxer o la resposta d'una API. Es poden distingir metadades de **descoberta**, que permeten trobar el recurs; d'**avaluació**, que ajuden a decidir si és adequat; i d'**ús**, que expliquen com interpretar-lo o connectar-s'hi. En informació geogràfica també cal diferenciar les metadades del conjunt, del servei i de cada capa.

#### Eurostat: una taula estadística multidimensional

El conjunt [`demo_pjan`](https://ec.europa.eu/eurostat/databrowser/view/demo_pjan/default/table?lang=en) no es descriu només amb el títol «Population on 1 January by age and sex». La fitxa mostra el codi persistent, el DOI, la font, la darrera actualització i l'enllaç a les [metadades demogràfiques ESMS](https://ec.europa.eu/eurostat/cache/metadata/en/demo_pop_esms.htm). La resposta de l'API afegeix dimensions com freqüència, unitat, edat, sexe, territori i temps. Els flags d'observació informen si un valor és provisional, estimat o afectat per una ruptura. Per interpretar una única xifra cal conservar totes les categories que la defineixen.

::: table "Lectura mínima de les metadades d'Eurostat"
| Element | Exemple a `demo_pjan` | Pregunta que resol |
| --- | --- | --- |
| Identificador | `demo_pjan` i DOI `10.2908/DEMO_PJAN` | Quin conjunt exacte s'ha utilitzat? |
| Dimensions | `freq`, `unit`, `age`, `sex`, `geo`, `time` | Quina combinació representa cada valor? |
| Unitat | `NR`, nombre | El valor és un recompte, percentatge o taxa? |
| Actualització | Data i hora de la versió publicada | Quan es va revisar la base? |
| Estat | Flags associats a l'observació | És provisional, estimada o confidencial? |
:::

#### Idescat: metadades dins de JSON-stat

L'[API de Taules de l'Idescat](https://www.idescat.cat/dev/api/taules/) retorna conjuntament dades i estructura. Una [consulta de població](https://api.idescat.cat/taules/v2/pmh/1180/8078/com/data?SEX=F&COM=01,TOTAL&_LAST_=1) inclou dimensions, categories, rols geogràfic i temporal, unitats, font, notes i data d'actualització. L'extensió `break` pot avisar d'una ruptura territorial. Això permet que un programa sàpiga què significa cada posició del vector de valors, però només si es conserva la resposta completa i no se n'extreu una columna descontextualitzada.

#### PNOA: metadades d'un servei i de les seves capes

La petició [`GetCapabilities`](https://www.ign.es/wms-inspire/pnoa-ma?SERVICE=WMS&REQUEST=GetCapabilities) del WMS PNOA retorna un document XML. A escala de servei identifica l'IGN/IDEE, descriu el mosaic d'ortofotos i Sentinel-2, declara els formats de resposta i informa de la condició `CC BY 4.0 scne.es`. A escala de capa, `OI.OrthoimageCoverage` enumera sistemes de referència, extensió geogràfica, atribució, estils i enllaços a registres de metadades ISO 19115 per a cada campanya.

::: table "Conjunt, servei i capa en el PNOA"
| Nivell | Metadades característiques | Decisió que permeten prendre |
| --- | --- | --- |
| Conjunt | Data de vol, resolució, cobertura i mètode de mosaic | Saber si la imatge és adequada per al període i detall requerits |
| Servei WMS | Operacions, formats, límits de mida, organisme i condicions | Saber com formular la petició i com atribuir el resultat |
| Capa | Nom tècnic, CRS, extensió, estil i consulta disponible | Identificar la capa i construir una consulta com `GetMap` |
:::

La pràctica de lectura consistirà a localitzar en cada exemple cinc elements: productor, definició, cobertura, data i llicència. Si algun d'aquests elements no es pot trobar, la limitació s'ha de registrar abans de continuar.

## Obertura, estàndards i reproduïbilitat

### Obert no designa una sola cosa

En un projecte es poden combinar diversos tipus d'obertura que no s'han de confondre:

- **Dades obertes:** dades accessibles sota una llicència que en permet la reutilització i redistribució.
- **Format obert:** especificació pública que diferents programes poden implementar, com CSV, GeoJSON o GeoPackage.
- **Estàndard obert:** acord tècnic publicat per facilitar que sistemes diferents intercanviïn informació, com els serveis de l'OGC.
- **Programari lliure i de codi obert:** programari que permet usar, estudiar, modificar i redistribuir el codi segons una llicència determinada.
- **Recerca oberta:** pràctiques que faciliten l'accés a publicacions, dades, codi, mètodes i resultats.

Una base de dades pot publicar-se en un format obert i mantenir una llicència restrictiva. A la inversa, unes dades amb llicència oberta poden distribuir-se en un format difícil de processar. També es pot fer una anàlisi reproduïble amb programari privatiu si se'n documenten prou bé els passos i versions, encara que una altra persona necessitarà accés al mateix programari. L'obertura facilita la reproducció, però no la garanteix per si sola.

Les llicències més habituals en els portals del capítol inclouen Creative Commons, llicències pròpies de les administracions i, en el cas de bases de dades, l'Open Database License. Sempre cal llegir la condició concreta. `CC BY 4.0` exigeix atribució; domini públic i `CC0` redueixen les restriccions; `ODbL` incorpora obligacions específiques per a bases derivades. «Sense cost» no informa de cap d'aquestes condicions.

### Llicències de dades, codi i serveis

La llicència indica els permisos i les obligacions, però primer cal identificar quin objecte regula. Les dades, el codi font, la documentació, una captura, una base cartogràfica i l'accés a una API poden tenir condicions diferents dins del mateix portal.

::: table "Llicències habituals de dades"
| Llicència o condició | Què permet habitualment | Obligació o límit principal |
| --- | --- | --- |
| `CC0` o domini públic | Reutilització molt àmplia sense reserva de drets | Encara convé citar la procedència i no atribuir aval al productor |
| `CC BY 4.0` | Copiar, transformar i redistribuir, també comercialment | Reconeixement, enllaç a la llicència i indicació dels canvis |
| `CC BY-SA 4.0` | Reutilització i transformació | Atribució i distribució de l'adaptació amb la mateixa llicència |
| `ODbL 1.0` | Usar, adaptar i compartir una base de dades | Atribució, compartir bases derivades i mantenir oberta la reutilització |
| Llicència administrativa pròpia | Reutilització segons les condicions publicades | Pot exigir atribució, data d'actualització i no desnaturalització |
| Ús acadèmic o no comercial | Ús limitat a les finalitats autoritzades | No equival a dades obertes i pot prohibir redistribució o ús comercial |
| Sense llicència identificable | No hi ha un permís general explícit | Cal demanar autorització o buscar una alternativa |
:::

L'atribució ha d'identificar, com a mínim, productor, conjunt i llicència. Si el producte s'ha modificat, també s'ha d'indicar. Un peu com «Font: IGN/CNIG, PNOA màxima actualitat, CC BY 4.0; elaboració pròpia» és més informatiu que «Font: internet».

Les llicències de programari utilitzen altres famílies. Les **permissives**, com MIT, BSD o Apache 2.0, permeten reutilitzar el codi amb poques condicions. Les de **copyleft**, com GPL, exigeixen que determinades redistribucions d'obres derivades mantinguin les mateixes llibertats. LGPL i MPL apliquen formes de copyleft més delimitades. Una llicència propietària o EULA concedeix només els usos que estableix el titular. *Freeware* significa que no es paga per usar el programa, no que el codi sigui obert.

Creative Commons recomana no utilitzar les seves llicències per a programari. Per això un projecte pot publicar les dades sota `CC BY 4.0`, el codi sota MIT o GPL i el text del manual sota una altra llicència. Quan es distribueixi un projecte cal conservar els avisos i comprovar la compatibilitat de cada component. Les pàgines de l'[Open Source Initiative](https://opensource.org/licenses) i del [projecte GNU](https://www.gnu.org/licenses/license-list.html) permeten consultar les característiques de les llicències de programari.

Finalment, les **condicions d'un servei** poden limitar volum, freqüència de peticions, emmagatzematge o ús de tessel·les encara que les dades subjacents siguin obertes. La llicència d'OpenStreetMap no converteix els servidors públics de tessel·les en una infraestructura sense límits; de la mateixa manera, una clau d'API gratuïta no atorga drets generals sobre totes les respostes.

### Estàndards per entendre's

Un estàndard descriu una manera compartida de representar o intercanviar informació. No és una marca comercial ni un programa. Aplicacions, servidors institucionals i biblioteques de programació poden entendre's perquè implementen la mateixa especificació.

En informació geogràfica apareixen diversos organismes i famílies d'estàndards:

- **ISO/TC 211** defineix marcs per a informació geogràfica. Entre els més rellevants hi ha ISO 19115 per a metadades, ISO 19157 per a qualitat i ISO 19111 per a sistemes de referència per coordenades.
- **Open Geospatial Consortium (OGC)** publica especificacions d'interoperabilitat com WMS, WMTS, WFS, GeoPackage i OGC API Features.
- **SDMX** organitza l'intercanvi de dades i metadades estadístiques multidimensionals i és habitual en organismes com Eurostat.
- **DCAT** descriu catàlegs de dades al web i permet que portals diferents federin les seves fitxes.
- **INSPIRE** estableix a la Unió Europea un marc comú per descobrir, visualitzar i compartir informació espacial pública.
- **IETF i W3C** mantenen especificacions web generals que també s'utilitzen amb dades, com URI, HTTP, JSON i GeoJSON.

No cal memoritzar una llista de sigles. Cal saber reconèixer què resol cadascuna. ISO ajuda a descriure conceptes, metadades i qualitat; OGC permet connectar eines geogràfiques; SDMX conserva dimensions estadístiques; DCAT ajuda a descobrir conjunts; INSPIRE coordina la infraestructura institucional europea.

Un format tampoc no és necessàriament un estàndard de servei. GeoPackage és un format d'emmagatzematge i WMS és una interfície que produeix mapes. Distingir aquestes funcions evita demanar a un WMS una taula d'atributs o confondre un mapa visualitzat amb les dades que l'han generat.

### Programari i codi obert

El programari de codi obert permet inspeccionar les operacions i redueix barreres perquè altres persones repeteixin el treball. [LibreOffice](https://www.libreoffice.org/) ofereix un full de càlcul de codi obert, mentre que [OpenRefine](https://openrefine.org/) està especialitzat en l'exploració i transformació de dades tabulars. Que una eina sigui oberta no converteix automàticament el projecte en reproduïble: encara cal registrar-ne la versió, conservar les dades i explicar les operacions.

### Reproduïbilitat: començar per l'ordre

Un resultat és reproduïble quan una altra persona pot partir de les mateixes dades originals, seguir les decisions documentades i obtenir el mateix resultat o explicar qualsevol diferència. No n'hi ha prou amb lliurar el mapa final. Cal conservar els ingredients, l'entorn i la seqüència que l'han produït.

La reproduïbilitat forma un espectre. Compartir només una figura ofereix molt poca capacitat de comprovació; afegir dades, codi, versions del programari, llicències i documentació redueix progressivament les ambigüitats. En projectes avançats es poden incorporar scripts i quaderns executables, control de versions, fitxers de dependències, proves automatitzades, contenidors Docker o Podman i fluxos que reconstrueixen els resultats des de l'inici {% cite zaragoziContainerTechnologies2020 %}.

Els fluxos basats en LLM introdueixen més elements que cal fixar. En un procés amb generació augmentada per recuperació, o RAG, caldria documentar el corpus consultat, la seva versió, el model, les instruccions, els paràmetres, el mètode de fragmentació, les representacions vectorials i la configuració de recuperació. RAG pot fer més traçable l'origen de les respostes, però no garanteix per si sol que dues execucions siguin idèntiques.

Aquestes tècniques requereixen més coneixements i infraestructura. Les bones pràctiques, però, comencen amb accions molt més senzilles: noms comprensibles, una estructura estable de carpetes, originals immutables i un registre de procedència. Una convenció compartida evita duplicacions i permet entendre un projecte sense dependre de la memòria de qui l'ha creat {% cite zaragoziFileNamingConvention2020 %}.

No existeix un únic arbre correcte per a tots els projectes. Es recomana utilitzar noms breus en anglès, minúscules i caràcters ASCII perquè funcionin de manera consistent entre sistemes operatius, scripts i serveis. Quan existeix una convenció àmpliament reconeguda, convé aprofitar-la: `src` per al codi font, `data` per a les dades, `outputs` per als resultats generats, `dist` per als lliurables i `README.md` per a la documentació inicial. Quan no existeix un nom establert, s'ha de triar un terme amb significat semàntic clar i mantenir-lo durant tot el projecte.

![Estructura orientativa d'un projecte reproduïble]({{ site.baseurl }}/assets/diagrams/reproducible-project-structure.puml "Estructura orientativa amb data/raw, data/processed, src, qgis, outputs, dist, sandbox i README.md"){: data-figure-width="15rem"}

En aquesta estructura:

- `data/raw` conserva les descàrregues originals sense modificar;
- `data/processed` conté dades transformades i preparades;
- `src` reuneix scripts, consultes o altres instruccions reutilitzables;
- `qgis` conté el projecte SIG i els recursos específics que necessiti;
- `outputs` conté figures, mapes i taules generades durant el treball;
- `dist` conté només els fitxers preparats per lliurar o distribuir;
- `sandbox` permet fer proves temporals que es poden descartar i que no han de convertir-se accidentalment en dependències del resultat final;
- `README.md` descriu la finalitat, les fonts, l'estructura i la manera de reconstruir el projecte.

Els noms dels fitxers també han de conservar context. `hotel_overnights_provinces_2024.csv` és més informatiu que `data2.csv`, i `tourism_intensity_map_2024.svg` és preferible a `final_map.svg`. Cal triar un sol patró, com `snake_case` o noms separats amb guionets, i aplicar-lo de manera coherent.

Quan s'hagin de conservar diferents versions d'un mateix fitxer, és preferible registrar els canvis amb un sistema de control de versions o amb un procés que pugui regenerar el resultat. Si cal mantenir instantànies, les dates ISO `YYYY-MM-DD` o la forma compacta `YYYYMMDD` s'ordenen cronològicament també quan els noms s'ordenen alfabèticament. Per exemple, `occupancy_2026-08-11.csv` pot identificar la data d'extracció. Si diverses revisions comparteixen data, es pot afegir una versió ordenable, com `v01` i `v02`, sempre que el `README.md` expliqui què ha canviat. Noms com `final`, `final_new` o `final_definitive_2` no permeten reconstruir la seqüència.

Una primera pràctica pot consistir a crear l'estructura, incorporar un fitxer original i comprovar que una altra persona pot interpretar el projecte sense explicacions orals.

::: table "Comprovació d'una estructura reproduïble"
| Control | Criteri |
| --- | --- |
| Estructura | Cada carpeta necessària té una funció inequívoca i no s'afegeixen nivells arbitraris |
| Originals | El fitxer descarregat conserva nom, extensió i contingut originals |
| Noms | No hi ha espais, accents, noms genèrics ni versions com `final_final` |
| Procedència | El `README.md` identifica productor, URL, data d'accés i llicència |
| Portabilitat | La carpeta completa es pot moure sense trencar el projecte ni les referències relatives |
| Reconstrucció | Els resultats identifiquen les dades i els passos dels quals depenen |
:::

## Escala i fonts d'informació

### Cercar de l'escala global a la local

L'escala geogràfica condiciona qui produeix les dades, quin detall es pot obtenir i fins a quin punt són comparables. Les fonts internacionals harmonitzen conceptes per comparar països, però sovint perden detall territorial. Les fonts estatals i catalanes acostumen a oferir més desagregació, però poden emprar classificacions pròpies. Les fonts locals poden ser molt detallades i, alhora, més difícils de comparar entre municipis.

No sempre s'ha de començar per l'escala més gran. Si la pregunta tracta els municipis catalans, Idescat o la Generalitat poden ser punts de partida més directes que Eurostat. Si es vol comparar Catalunya amb regions europees, caldrà buscar una classificació harmonitzada com NUTS i comprovar si la variable existeix al mateix nivell.

::: table "Orientació inicial per escala"
| Escala | Fonts estadístiques | Fonts geoespacials | Ús característic |
| --- | --- | --- | --- |
| Mundial | FAOSTAT, World Bank Data, UNData, UN Tourism | Natural Earth, GADM, Copernicus, CIA Maps, OpenStreetMap | Comparar països o observar processos globals |
| Europea | Eurostat | GISCO, Copernicus | Comparar estats i regions NUTS amb criteris harmonitzats |
| Espanya | INE, Dataestur | IGN/CNIG, Cadastre | Treballar comunitats, províncies, municipis i zones turístiques |
| Catalunya | Idescat, Registre de Turisme, dades sectorials | ICGC, Dades Obertes de la Generalitat | Analitzar comarques, municipis, establiments i territori detallat |
| Local | Ajuntaments i ens supramunicipals | IDE i cartografia municipal | Estudiar equipaments, planejament o serveis concrets |
:::

### Fonts internacionals

Les fonts internacionals existeixen perquè hi ha problemes que no es poden analitzar només amb estadístiques d'un país. Comparar fam, producció agrària, desenvolupament, migracions o turisme requereix definicions comunes i organismes capaços de coordinar dades produïdes per molts estats. Aquesta harmonització facilita la comparació, però també obliga a examinar qui va observar originàriament cada valor, quines estimacions s'hi han aplicat i quin detall territorial s'ha perdut.

#### FAO i FAOSTAT

L'[Organització de les Nacions Unides per a l'Alimentació i l'Agricultura](https://www.fao.org/about/en/) (FAO) és una agència especialitzada de les Nacions Unides que lidera esforços internacionals contra la fam i treballa per millorar la seguretat alimentària. Per orientar polítiques, inversions i seguiment dels sistemes agroalimentaris necessita dades comparables sobre producció, comerç, preus, nutrició, recursos naturals i sostenibilitat. Per això recull informació dels estats membres, desenvolupa mètodes i classificacions i dona suport als països perquè millorin els seus sistemes estadístics.

El principal portal estadístic general de l'organització és [FAOSTAT](https://www.fao.org/faostat/en/#data). Ofereix accés gratuït a sèries de més de 245 països i territoris, en molts casos des de 1961, sobre agricultura, ramaderia, silvicultura, usos del sòl, comerç, seguretat alimentària i emissions. Altres sistemes de la FAO cobreixen àmbits més específics, com AQUASTAT per als recursos hídrics o FishStat per a pesca i aqüicultura.

FAOSTAT permet filtrar països, productes, elements i anys i ofereix descàrregues massives. Moltes sèries incorporen **flags** que indiquen si el valor és oficial, estimat o imputat. La comparabilitat internacional és un avantatge, però una dada publicada per la FAO pot continuar procedint d'un organisme estatal i tenir una qualitat o actualització diferent de la d'un altre país.

#### Banc Mundial i World Bank Data

El [Grup del Banc Mundial](https://www.worldbank.org/en/about/what-we-do) finança projectes de desenvolupament i ofereix assistència tècnica, recerca i assessorament als països. Necessita indicadors per diagnosticar necessitats, orientar finançament i avaluar resultats. La seva funció explica l'amplitud temàtica de [World Bank Data](https://data.worldbank.org/): població, pobresa, economia, educació, infraestructures, medi ambient i turisme, entre molts altres àmbits.

El portal facilita comparacions mundials, descàrregues i una API sense clau. Cada indicador inclou definició, unitat, font original i notes metodològiques. El Banc Mundial, però, no produeix necessàriament totes les sèries que difon. Alguns indicadors provenen d'instituts nacionals o d'altres organismes internacionals; cal revisar el camp *source* i no interpretar els valors absents com a zero.

#### Sistema de les Nacions Unides

La Divisió d'Estadística de les Nacions Unides coordina estàndards i compila informació perquè fenòmens globals es puguin comparar. [UNData](https://data.un.org/) agrega bases de població, comptes nacionals, comerç, energia, medi ambient i altres àmbits. És un bon punt de descoberta, però la traça s'ha de seguir fins a l'agència productora. Per als Objectius de Desenvolupament Sostenible també es disposa de l'[API oficial dels indicadors ODS](https://unstats.un.org/SDGAPI/swagger/).

Dins del mateix sistema, [UN Tourism](https://www.unwto.org/tourism-statistics/tourism-statistics-database) té el mandat especialitzat d'impulsar un turisme responsable, sostenible i accessible. Per observar-ne l'evolució promou recomanacions estadístiques comunes i reuneix arribades, pernoctacions, despesa, allotjament i indicadors macroeconòmics. L'accés i la reutilització no són iguals per a tots els productes; abans de redistribuir una descàrrega cal revisar-ne les condicions específiques.

#### CIA Maps i el llegat del World Factbook

La Central Intelligence Agency dels Estats Units necessita informació bàsica geogràfica, política, demogràfica i econòmica per a les seves funcions d'intel·ligència. El *World Factbook* va néixer com una publicació interna, després es va fer públic i durant dècades va oferir perfils sintètics de països i territoris. La CIA en va finalitzar la publicació el febrer de 2026, de manera que ja no s'ha de recomanar com una base vigent.

El recurs actiu [CIA Maps](https://www.cia.gov/resources/cia-maps/) permet explorar mapes de més de 110 localitzacions. Pot ser útil per observar topònims, fronteres i la manera com una institució nord-americana representa el món, però ofereix productes cartogràfics de referència, no una base vectorial equivalent a Natural Earth. Les denominacions, fronteres i seleccions s'han de contrastar amb fonts internacionals i amb els organismes oficials dels territoris estudiats.

>> **Les fonts també desapareixen.** El final del *World Factbook* mostra per què una URL no és una garantia de permanència. En un treball reproduïble cal registrar la data d'accés i conservar, quan la llicència ho permeti, la versió exacta utilitzada.

### Fonts europees

En l'àmbit europeu, Eurostat és la font estadística comparativa principal, mentre que GISCO i Copernicus aporten geometries harmonitzades i observació de la Terra.

#### Eurostat

[Eurostat](https://ec.europa.eu/eurostat/data/database) és l'oficina estadística de la Unió Europea. El seu valor principal és l'harmonització: les dades dels estats s'organitzen amb definicions i classificacions comunes per facilitar la comparació. Inclou població, economia, treball, transport, medi ambient i un bloc ampli de turisme amb capacitat d'allotjament, arribades, pernoctacions, ocupació i viatges dels residents.

El **Data Browser** permet seleccionar dimensions i descarregar resultats. Eurostat també ofereix descàrrega massiva i diverses API en formats JSON-stat, SDMX i TSV. Les taules tenen codis estables, com `demo_pjan` per a població, i moltes disposen de DOI. Els flags identifiquen valors estimats, provisionals, confidencials o afectats per ruptures.

Eurostat actualitza la base dues vegades al dia i només hi manté la versió més recent. Per reproduir una activitat cal conservar el fitxer o la resposta exacta utilitzada, la data i el codi del conjunt.

![Data Browser d'Eurostat]({{ site.baseurl }}/assets/img/data-sources/eurostat-data-browser.png "Data Browser d'Eurostat: codi del conjunt, metadades, dimensions, filtres i descàrrega. Captura pròpia del portal d'Eurostat, 11 d'agost de 2026.")

#### GISCO i Copernicus

[GISCO](https://ec.europa.eu/eurostat/web/gisco/geodata) és el component geogràfic d'Eurostat. Distribueix geometries de països, regions NUTS, unitats locals, ciutats i altres capes en diferents escales i sistemes de referència. Permet unir les estadístiques d'Eurostat amb geometries compatibles. Cal revisar la llicència de cada família de capes: algunes fronteres administratives incorporen drets d'EuroGeographics i restriccions específiques.

[Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) dona accés a imatges Sentinel i altres productes d'observació de la Terra. El navegador permet cercar per lloc, dates, missió, cobertura de núvols i tipus de producte. També hi ha catàlegs STAC i OData, processament en línia i descàrrega. La data de captació, el nivell de processament, la resolució, els núvols i la llicència de cada col·lecció formen part de la selecció; «publicat al Data Space» no implica que tot el contingut tingui exactament les mateixes condicions.

### Fonts estatals

Algunes de les fonts estatals més habituals són l'INE per a estadística oficial, l'IGN i el CNIG per a informació geogràfica de referència, i els catàlegs `datos.gob.es` i Dataestur per descobrir recursos de diferents productors.

#### INE i INEbase

L'[Instituto Nacional de Estadística](https://www.ine.es/) produeix censos, enquestes i estadístiques sobre població, habitatge, economia, treball, mobilitat i turisme. INEbase permet navegar per operacions i taules, seleccionar dimensions i descarregar resultats. En turisme s'hi troben estadístiques d'ocupació hotelera i extrahotelera, FRONTUR, EGATUR i turisme de residents, entre d'altres.

La desagregació varia segons l'operació: una taula pot arribar a municipis, províncies, comunitats autònomes, punts o zones turístiques. Les enquestes no són necessàriament representatives a totes les escales. Cal diferenciar també padró, cens i estimacions de població, així com dada provisional i definitiva.

L'INE també ofereix una [API JSON](https://www.ine.es/dyngs/DAB/index.htm?cid=1099). La desagregació depèn de cada operació i els codis territorials s'han de conservar com a text. Cens, padró, estimació de població, punt turístic i municipi no són categories intercanviables.

#### Datos.gob.es, Dataestur i altres organismes

[datos.gob.es](https://datos.gob.es/es/catalogo/conjuntos-datos) és el catàleg estatal de dades obertes. Ajuda a localitzar conjunts d'administracions estatals, autonòmiques i locals, però normalment no n'és el productor. Una fitxa del catàleg pot estar actualitzada mentre que una distribució enllaçada ja no funciona; cal identificar i citar l'organisme publicador original.

[Dataestur](https://www.dataestur.es/) integra indicadors turístics procedents de l'INE, AENA, la Seguretat Social, AEMET i altres fonts. Resulta útil per explorar el sector, però els indicadors no comparteixen necessàriament metodologia, unitat ni escala. Per a una anàlisi reproduïble convé recuperar la dada del productor original quan sigui possible.

Altres fonts estatals complementàries són [AEMET OpenData](https://opendata.aemet.es/) per a observacions i prediccions meteorològiques, i els serveis [INSPIRE del Cadastre](https://www.catastro.hacienda.gob.es/webinspire/index.html) per a parcel·les, edificis i adreces. Una estació meteorològica no representa automàticament tot un municipi, i una parcel·la cadastral no equival necessàriament a una finca registral ni al planejament urbanístic.

#### IGN i CNIG

L'Instituto Geográfico Nacional produeix informació geogràfica de referència i el Centro Nacional de Información Geográfica la distribueix mitjançant el [Centro de Descargas del CNIG](https://centrodedescargas.cnig.es/CentroDescargas/catalogo). S'hi troben mapes topogràfics, bases cartogràfiques, límits administratius, CartoCiudad, ortofotos PNOA, models digitals del terreny, LiDAR, ocupació del sòl i noms geogràfics.

Els productes tenen escales, resolucions, dates, formats i sistemes de referència diferents. Una ortofoto de «màxima actualitat» pot ser un mosaic d'imatges captades en anys diferents. A més de descàrregues, l'[IGN publica serveis web](https://www.ign.es/web/ign/portal/ide-area-nodo-ide-ign), com WMS, WMTS, WFS, WCS i OGC API.

### Fonts catalanes

En l'àmbit català, Idescat concentra l'estadística oficial; els departaments publiquen registres i dades sectorials mitjançant Dades Obertes, i l'ICGC produeix la informació cartogràfica i geològica de referència.

#### Idescat

L'[Institut d'Estadística de Catalunya](https://www.idescat.cat/) publica informació demogràfica, econòmica, social, territorial i turística. Segons l'operació, les dades poden estar disponibles per Catalunya, àmbits territorials, comarques, municipis, districtes o seccions censals. La secció de [dades obertes](https://www.idescat.cat/dades/obertes/) facilita descàrregues, i l'[API de l'Idescat](https://www.idescat.cat/dev/api/) retorna part de les taules en JSON-stat.

Idescat també manté [codis i classificacions territorials](https://www.idescat.cat/codis/) i informa de rectificacions. Alguns resultats són producció pròpia i d'altres són explotacions de dades de l'INE o dels departaments de la Generalitat; l'autoria metodològica completa s'ha de conservar. Els canvis de comarca, municipi o secció censal poden trencar una sèrie.

![Portal de l'Idescat]({{ site.baseurl }}/assets/img/data-sources/idescat.png "Portal de l'Idescat: accés a dades, mètodes, territori i actualitzacions de l'estadística oficial de Catalunya. Captura pròpia, 11 d'agost de 2026.")

#### Dades Obertes de la Generalitat i informació turística

El [catàleg de Dades Obertes de la Generalitat](https://analisi.transparenciacatalunya.cat/) reuneix conjunts de molts departaments i organismes. La plataforma permet filtrar, visualitzar, exportar CSV, JSON o GeoJSON i, en molts casos, consultar una API SODA. Com passa amb `datos.gob.es`, el catàleg no substitueix el productor que consta a cada fitxa.

Un conjunt especialment útil és el [Registre de Turisme de Catalunya](https://analisi.transparenciacatalunya.cat/Turisme/Establiments-d-allotjament-tur-stic-inscrits-al-Re/t2h3-cgys/about_data), que conté establiments inscrits, tipus, estat, municipi, comarca, places i altres camps. És una font administrativa: una alta no demostra que l'establiment estigui obert, que les places estiguin disponibles ni que hi hagi hagut ocupació. Aquesta diferència permet treballar la distància entre **oferta registrada** i **activitat observada**.

El portal de [coneixement turístic de la Generalitat](https://empresa.gencat.cat/ca/treb_ambits_actuacio/turisme/coneixement_planificacio/) agrupa estadístiques, estudis i eines sectorials. Les marques turístiques que hi apareixen no són necessàriament divisions administratives i la seva composició s'ha de documentar abans de fer unions territorials.

#### ICGC

L'[Institut Cartogràfic i Geològic de Catalunya](https://www.icgc.cat/ca/Geoinformacio-i-mapes) produeix cartografia topogràfica, ortofotos, models d'elevació, LiDAR, límits administratius, geologia, cobertes del sòl i toponímia. El [visor de descàrregues](https://visors.icgc.cat/appdownloads/) permet obtenir productes per full o àrea, i la secció de [geoserveis](https://www.icgc.cat/ca/Geoinformacio-i-mapes/Geoinformacio-en-linia-Geoserveis) documenta serveis WMS, WMTS, WFS i altres interfícies.

Molts productes catalans utilitzen ETRS89 / UTM fus 31N (`EPSG:25831`), però sempre cal comprovar la fitxa. L'escala, la resolució, l'edició i el sistema de referència no s'han de deduir només del nom del fitxer.

![Visor de descàrregues de l'ICGC]({{ site.baseurl }}/assets/img/data-sources/icgc-downloads.png "Visor de descàrregues de l'ICGC: selecció de l'àrea, família de producte i format de sortida. Captura pròpia, 11 d'agost de 2026.")

### Bases geoespacials mundials

Les bases mundials resolen necessitats diferents. Natural Earth està preparada per a cartografia generalitzada, GADM ofereix divisions administratives amb restriccions de llicència i OpenStreetMap construeix una base col·laborativa molt detallada. Abans d'arribar a la cartografia col·laborativa convé entendre que la producció compartida d'informació té altres formes.

#### Natural Earth

[Natural Earth](https://www.naturalearthdata.com/) ofereix cartografia mundial generalitzada a escales 1:10.000.000, 1:50.000.000 i 1:110.000.000. Inclou països, subdivisions principals, ciutats, costes, rius, xarxes i ràsters de fons. Les dades són de domini públic i són molt útils per a mapes mundials de petita escala.

No és una base adequada per delimitar parcel·les, municipis o fronteres jurídiques amb precisió. L'escala seleccionada ha de correspondre a la mida i la finalitat del mapa: més detall no sempre produeix un mapa millor.

#### GADM

[GADM](https://gadm.org/) distribueix divisions administratives de molts nivells per a països de tot el món. Pot resultar pràctic quan no hi ha una única font global comparable, però **no és una font oficial de fronteres i no és dades obertes**. La [llicència de GADM](https://gadm.org/license.html) permet usos acadèmics i altres usos no comercials, però prohibeix en general la redistribució i l'ús comercial sense autorització.

Per tant, els fitxers GADM no s'incorporaran al repositori públic del manual. Si s'utilitzen en una activitat, cada participant els haurà d'obtenir del lloc oficial, registrar-ne la versió i respectar-ne la llicència. També caldrà comprovar si existeixen condicions específiques per al país estudiat.

#### Wikipedia, Wikidata i les dades col·laboratives

[Wikipedia](https://www.wikipedia.org/) és una enciclopèdia construïda i revisada col·laborativament. Pot ajudar a descobrir conceptes, topònims i referències, però és una font secundària narrativa: una afirmació s'ha de comprovar mitjançant les cites, l'historial i, quan sigui possible, la font original.

[Wikidata](https://www.wikidata.org/) aplica el mateix principi col·laboratiu a una base de coneixement estructurada i multilingüe. Cada element té un identificador, com `Q` seguit d'un número, i pot contenir propietats, valors, coordenades, referències i enllaços a altres bases. Les dades es publiquen sota `CC0` i es poden consultar amb SPARQL o API. El seu caràcter obert i estructurat en facilita la reutilització, però les declaracions continuen depenent de les fonts aportades, de les regles comunitàries i de la cobertura desigual.

#### OpenStreetMap i Google Maps

[OpenStreetMap](https://www.openstreetmap.org/about) (OSM) és una base de dades geogràfica construïda per una comunitat que combina coneixement local, treball de camp, traces GPS i imatges autoritzades. Es distribueix sota l'Open Database License i permet obtenir objectes, consultar-ne l'historial i produir mapes derivats. [Google Maps](https://www.google.com/maps) és principalment un servei cartogràfic comercial orientat a la cerca de llocs, navegació, negocis, fotografies i ressenyes. Poder consultar-ne el mapa no autoritza a extreure'n massivament les dades ni a reutilitzar-ne les imatges com si fossin dades obertes.

La diferència entre models de producció es fa visible en comparacions locals. La taula descriu allò que era observable als mapes estàndard l'11 d'agost de 2026; no demostra quines dades pot conservar internament cada plataforma.

::: table "Dos llocs on OpenStreetMap ofereix més detall territorial observable"
| Lloc i vistes comparables | Detall especialment ric a OSM | Fortalesa visible de Google Maps | Explicació plausible |
| --- | --- | --- | --- |
| [Campus de Vila-seca a OSM](https://www.openstreetmap.org/#map=18/41.10266/1.14784) i [a Google Maps](https://www.google.com/maps/@41.10266,1.14784,18z?hl=ca) | Carrils bici amb segregació i sentit; pistes i piscines com a geometries; aparcaments de bicicletes; accessibilitat; desfibril·lador; font; mobiliari de parada i arbrat | Equipaments, fitxes de llocs, fotografies i alguns aparcaments | Contribució local i temàtica, incloses edicions d'accessibilitat, davant d'una representació comercial orientada a cerca i navegació |
| [Camí de Ronda de Cap Salou a OSM](https://www.openstreetmap.org/#map=17/41.05650/1.16480) i [a Google Maps](https://www.google.com/maps/@41.05650,1.16480,17z?hl=ca) | Continuïtat del sender; distinció entre camí i escales; pendents i restriccions; accessos a cales; roca, matollar, platges i microtoponímia | Hotels, comerços, miradors, fotografies i llocs d'interès | Edició excursionista centrada en topologia, transitabilitat i medi físic davant d'una selecció centrada en destinacions i serveis |
:::

Més detall no significa necessàriament més exactitud. Els atributs d'OSM poden estar desactualitzats o no haver estat verificats sobre el terreny, i Google pot mostrar informació addicional en una fitxa o una ruta que no apareix al mapa base. La comparació serveix per entendre que cada sistema prioritza objectes diferents i que cap mapa no s'ha d'acceptar sense comprovar-lo.

## Com s'accedeix a les dades

Una mateixa institució pot oferir el mateix conjunt mitjançant una taula interactiva, un fitxer, una API i un geoservei. No són fonts diferents: són vies d'accés amb propietats diferents.

![Vies d'accés a una font de dades]({{ site.baseurl }}/assets/diagrams/data-access-modes.mmd "Vies d'accés: interfície, fitxer, API i geoservei")

### Interfícies gràfiques

Una interfície gràfica permet cercar, seleccionar dimensions, aplicar filtres i visualitzar resultats sense escriure codi. El Data Browser d'Eurostat, INEbase, les taules d'Idescat i el navegador de Copernicus en són exemples.

Són adequades per explorar una font i entendre'n l'estructura, però presenten riscos. Pot ser difícil repetir exactament els clics, els gràfics poden arrodonir valors i una actualització de la interfície pot canviar la consulta. Per això s'ha de guardar l'enllaç persistent, si existeix, i descarregar la taula i les metadades finals.

### Fitxers descarregables

La descàrrega és la via més senzilla per conservar una còpia exacta. Els formats més habituals són:

::: table "Formats que es trobaran al curs"
| Format | Contingut habitual | Precaució principal |
| --- | --- | --- |
| CSV o TSV | Taules de text separades per comes, punt i coma o tabuladors | Importar amb la codificació, delimitador i separador decimal correctes |
| XLSX | Llibres d'Excel amb fulls, formats i fórmules | Distingir dades, presentació i càlculs ocults |
| JSON o JSON-stat | Dades estructurades i respostes d'API | Normalitzar dimensions i conservar metadades |
| GeoPackage | Capes vectorials o ràster en un únic fitxer | Identificar capa, geometria i sistema de referència |
| Shapefile | Conjunt antic de fitxers vectorials (`.shp`, `.dbf`, `.shx`...) | No separar els components; noms de camp i codificació limitats |
| GeoJSON | Objectes vectorials en text JSON | Fitxers grans i ús habitual de coordenades geogràfiques |
| GeoTIFF | Imatge ràster georeferenciada | Comprovar resolució, CRS, nombre de bandes i valor nodata |
| GML | Objectes geogràfics estructurats en XML | Esquema complex i fitxers voluminosos |
| LAZ/LAS | Núvols de punts LiDAR | Gran volum i necessitat d'eines específiques |
:::

>>>> **No s'ha de confiar en l'aplicació predeterminada.** Obrir un fitxer amb doble clic delega la interpretació al programa que el sistema operatiu hi hagi associat. En un CSV, el full de càlcul pot convertir codis en nombres o dates, triar un delimitador incorrecte i confondre punts i comes decimals. És preferible **importar-lo** indicant que els codis són text, quina codificació utilitza i com representa els decimals i els valors absents. El mateix criteri s'aplica als altres formats: un visor d'imatges pot mostrar un GeoTIFF però ignorar-ne la georeferenciació; un descompressor no interpreta les capes d'un GeoPackage; i obrir només el `.shp` no garanteix que es conservin tots els components d'un Shapefile. Primer cal identificar el format i després escollir l'eina adequada.

### API

Una **API** (*application programming interface*) és una interfície perquè un programa demani dades a un altre sistema de manera estructurada. En una API web, la petició sol ser una URL formada per un endpoint i uns paràmetres; la resposta acostuma a ser JSON, JSON-stat, CSV o XML.

L'API és útil quan cal repetir una consulta, actualitzar-la o recuperar només una part d'un conjunt gran. No elimina la necessitat d'entendre la font: una petició tècnicament correcta pot seleccionar la variable o la unitat equivocada.

>> **La URL també forma part del mètode.** Quan els paràmetres d'una consulta apareixen a la URL, conservar l'adreça completa ajuda a repetir la selecció. Encara cal registrar la data d'accés, perquè el servidor pot actualitzar els valors mantenint la mateixa consulta.

#### Exemple mínim amb el Banc Mundial

La petició següent demana la població total (`SP.POP.TOTL`) d'Espanya (`ESP`) per a 2023 i sol·licita una resposta JSON:

```text
https://api.worldbank.org/v2/country/ESP/indicator/SP.POP.TOTL?date=2023&format=json
```

Es pot enganxar directament al navegador. La URL es pot llegir per parts:

```text
https://api.worldbank.org/v2/     servei i versió
country/ESP/                      territori
indicator/SP.POP.TOTL             indicador
?date=2023&format=json             paràmetres
```

La resposta inclou metadades de la consulta i les observacions. No n'hi ha prou amb copiar el valor: també s'ha de conservar el codi de l'indicador, l'any, el país, la font i la data d'accés.

#### Exemple filtrat amb Eurostat

La consulta següent recupera la població total d'Espanya el 2024 del conjunt `demo_pjan`, filtrada per edat total i tots els sexes:

```text
https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan?lang=en&geo=ES&time=2024&age=TOTAL&sex=T
```

Eurostat retorna JSON-stat 2.0, un format multidimensional. Els valors no s'han d'interpretar sense llegir l'ordre i les categories de les dimensions. La [documentació de les API d'Eurostat](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-introduction) explica els endpoints, els formats i les limitacions.

#### Exemple d'un registre català

La plataforma de Dades Obertes permet obtenir una mostra del Registre de Turisme en JSON:

```text
https://analisi.transparenciacatalunya.cat/resource/t2h3-cgys.json?$limit=5
```

L'identificador `t2h3-cgys` correspon al conjunt i `$limit=5` limita el resultat. Altres expressions SoQL permeten seleccionar camps, filtrar files o agrupar valors. En una activitat reproduïble s'ha de conservar la consulta sencera, no només el fitxer resultant.

Aquest registre inclou camps de titularitat que no són necessaris per a la majoria d'anàlisis territorials. Les consultes docents han de seleccionar només els camps imprescindibles, com el tipus, l'estat, les places i els codis territorials, i han d'evitar copiar o redistribuir dades personals sense necessitat.

### Geoserveis

Els geoserveis publiquen informació geogràfica a través d'estàndards web. Els principals tipus que es trobaran al curs són:

- **WMS:** retorna una imatge del mapa. Serveix per visualitzar, però no proporciona les geometries vectorials per analitzar-les.
- **WMTS:** retorna tessel·les d'imatge preparades i és eficient com a cartografia de fons.
- **WFS:** retorna objectes vectorials amb geometria i atributs que es poden consultar i processar.
- **OGC API Features:** ofereix objectes vectorials mitjançant una API web moderna, habitualment en GeoJSON.

També existeixen WCS per a cobertures ràster i catàlegs com STAC per descobrir imatges d'observació de la Terra. Abans de connectar un servei cal consultar-ne les capacitats, les capes, el sistema de referència, l'escala i les condicions d'ús. Que una capa es pugui veure no significa que es pugui descarregar o redistribuir.

#### Una petició WMS que es pot obrir al navegador

Un WMS no descarrega una tessel·la predefinida. L'operació `GetMap` demana al servidor que compongui una imatge amb una capa, una extensió geogràfica, un sistema de referència, una amplada, una alçada i un format. La petició següent utilitza la capa `OI.OrthoimageCoverage` del PNOA i una extensió centrada en la Facultat de Turisme i Geografia:

```text
https://www.ign.es/wms-inspire/pnoa-ma
  ?SERVICE=WMS
  &VERSION=1.3.0
  &REQUEST=GetMap
  &LAYERS=OI.OrthoimageCoverage
  &STYLES=
  &CRS=EPSG:3857
  &BBOX=127377,5027197,128177,5027797
  &WIDTH=1000
  &HEIGHT=750
  &FORMAT=image/jpeg
```

[Obrir o descarregar la imatge generada pel WMS del PNOA](https://www.ign.es/wms-inspire/pnoa-ma?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=OI.OrthoimageCoverage&STYLES=&CRS=EPSG:3857&BBOX=127377,5027197,128177,5027797&WIDTH=1000&HEIGHT=750&FORMAT=image/jpeg). Si es canvia `BBOX`, es demana un altre lloc; si es canvien `WIDTH` i `HEIGHT`, canvia la mida del resultat. Un WMTS, en canvi, serveix tessel·les d'una quadrícula i uns nivells d'escala predefinits.

![Ortofoto PNOA de la Facultat de Turisme i Geografia]({{ site.baseurl }}/assets/img/data-sources/pnoa-facultat-turisme-geografia.jpg "Ortofoto de l'entorn de la Facultat de Turisme i Geografia obtinguda amb una petició GetMap al WMS PNOA màxima actualitat. Font: IGN/CNIG, CC BY 4.0, consulta de l'11 d'agost de 2026.")

## Introducció als fulls de càlcul

Un full de càlcul combina una taula, un llenguatge de fórmules i una interfície visual. Permet inspeccionar les dades directament, provar una operació i veure'n el resultat sense construir primer un programa complet. Aquesta immediatesa el fa adequat per començar a treballar amb taules territorials de volum moderat, però també pot afavorir canvis manuals difícils de reconstruir si el llibre no s'organitza amb criteri.

### Un model de treball compartit

Excel, LibreOffice Calc, Google Sheets i altres aplicacions comparteixen un funcionament bàsic. Un llibre conté fulls; cada full organitza cel·les en files i columnes; una referència com `B2` identifica una cel·la i un rang com `B2:B100` identifica un conjunt. Les fórmules comencen amb `=` i poden combinar valors, referències, operadors i funcions. Quan canvia una cel·la d'origen, les fórmules que en depenen es tornen a calcular.

::: table "Capacitats estàndard d'un full de càlcul"
| Capacitat | Funcionament esperable | Aplicació al curs |
| --- | --- | --- |
| Referències | Relacionar una fórmula amb cel·les o rangs | Calcular un indicador sense copiar els valors manualment |
| Fórmules i funcions | Fer operacions aritmètiques, lògiques, textuals, estadístiques i temporals | Comprovar tipus, calcular ràtios i validar totals |
| Emplenament | Estendre una fórmula mantenint referències relatives o absolutes | Aplicar el mateix càlcul a tots els municipis |
| Ordenació i filtre | Reorganitzar o mostrar files segons valors i condicions | Inspeccionar casos extrems, absències i categories |
| Agregació | Resumir dades amb funcions o taules dinàmiques | Obtenir totals per municipi o tipologia |
| Gràfics | Vincular una representació a un rang de dades | Comparar magnituds, composicions i relacions |
| Importació i exportació | Llegir i escriure formats com CSV, XLSX, ODS o PDF | Conservar dades, intercanviar llibres i exportar figures |
:::

Aquest nucli permet transferir l'aprenentatge entre programes. Entendre una referència absoluta com `$B$2`, la diferència entre valor i format o el sentit d'una funció condicional és més útil que memoritzar la posició exacta d'un botó. Les funcions avançades, els gràfics disponibles, les taules dinàmiques, les macros, l'automatització i el treball col·laboratiu sí que poden variar considerablement.

### Idiomes i configuració regional

La compatibilitat no és absoluta. Poden canviar els noms de funció, els separadors d'arguments, els separadors decimals, el reconeixement de dates, les funcions disponibles i alguns comportaments dels gràfics. La configuració regional de l'aplicació, del document i, en alguns casos, del sistema operatiu pot fer que una mateixa operació s'escrigui de maneres diferents:

```text
=SUM(A2:A10)
=SUMA(A2:A10)
=IF(B2>0,"sí","no")
=SI(B2>0;"sí";"no")
```

Aquestes variants expressen respectivament una suma i una condició equivalents. Segons l'entorn, les funcions poden aparèixer en anglès o traduïdes, i els arguments poden separar-se amb comes o amb punt i coma. Per això una fórmula trobada en un tutorial pot necessitar una adaptació sintàctica encara que el raonament sigui correcte.

Quan es treballa en grup convé acordar l'aplicació principal, la configuració regional i el format del llibre. També s'ha de comprovar el resultat després d'obrir-lo en un programa diferent. El criteri d'aprenentatge serà entendre les referències, els tipus, les operacions i les comprovacions, no memoritzar una única interfície.

### Tipus de dades

Un full de càlcul no veu una taula com la veu una persona. Cada cel·la conté un valor que el programa interpreta amb un tipus determinat. Aquest tipus condiciona les operacions possibles, l'ordenació, els filtres, els gràfics i la manera com la dada s'exportarà a altres programes. Per això no n'hi ha prou que una columna «sembli correcta» a la pantalla.

### Valor, tipus i format

El **valor** és el contingut emmagatzemat; el **tipus** indica com es pot tractar, i el **format** en modifica la presentació sense canviar necessàriament el valor. El nombre `0,25`, per exemple, es pot mostrar com `25%`, però continua sent el mateix valor numèric. Aplicar un format numèric al text `25%` no el converteix automàticament en un nombre vàlid.

::: table "Tipus habituals en una taula territorial"
| Tipus | Exemples | Operacions amb sentit | Risc habitual |
| --- | --- | --- | --- |
| Número enter o decimal | població, places, superfície, despesa | sumar, restar, calcular mitjanes, ràtios i ordenar per magnitud | decimals interpretats amb una configuració regional incorrecta |
| Text | nom del municipi, comarca, categoria | cercar, filtrar, comparar, agrupar o concatenar | variants ortogràfiques i espais invisibles |
| Identificador | codi INE, NUTS, matrícula, telèfon | comprovar igualtat, longitud, unicitat o correspondència | tractar-lo com una quantitat i perdre zeros inicials |
| Data i hora | data d'obertura, dia de consulta, instant d'una observació | ordenar cronològicament, restar dates o afegir durades | conversió automàtica o confusió entre dia i mes |
| Lògic | cert/fals, compleix/no compleix | filtrar, comptar condicions i construir comprovacions | substituir una situació desconeguda per fals |
| Absent o error | no disponible, no aplicable, divisió impossible | identificar, comptar i documentar | convertir-lo en zero o ocultar-lo sense explicació |
:::

Que una cadena estigui formada per dígits no la converteix necessàriament en una quantitat. Sumar dos números de telèfon, calcular la mitjana dels codis municipals o multiplicar un codi postal no produeix una interpretació útil. En canvi, sí que té sentit comparar-los, detectar duplicats, comprovar-ne la longitud o usar-los com a claus d'unió. El significat de la variable, i no només l'aparença, determina les operacions legítimes.

### L'alineació és una pista, no una prova

Els fulls de càlcul solen alinear el text a l'esquerra i els nombres a la dreta. Les calculadores també mostren les xifres alineades a la dreta: així es mantenen fixes les unitats, les desenes i les centenes mentre l'entrada creix cap a l'esquerra. En una columna, aquesta alineació facilita comparar ordres de magnitud i decimals.

La taula següent imita l'alineació predeterminada d'un full de càlcul. Els valors són ficticis i només serveixen per raonar sobre els tipus de dades.

::: table "Cinc files per interpretar tipus i alineacions"
| Municipi | Codi municipal | Població | Habitatge no principal | Data de referència | Revisat |
| :--- | :--- | ---: | ---: | ---: | :---: |
| Altafulla | 430120 | 5.000 | 42,0% | 2021-01-01 | CERT |
| Canonja, la | 439076 | 6.000 | 8,0% | 2021-01-01 | CERT |
| Salou | 439057 | 30.000 | 58,0% | 2021-01-01 | CERT |
| Tarragona | 431482 | 140.000 | 15,0% | 2021-01-01 | FALS |
| Vila-seca | 431711 | 23.000 | 24,0% | 2021-01-01 | CERT |
:::

`Municipi` és text: es pot ordenar alfabèticament, filtrar o agrupar, però no calcular-ne una mitjana. `Codi municipal` també ha de ser text, encara que contingui dígits. Serveix per comprovar igualtats, longituds, duplicats i correspondències; sumar els codis no descriuria cap fenomen.

`Població` és numèrica. Té sentit calcular-ne el total amb `=SUM(C2:C6)`, la mitjana amb `=AVERAGE(C2:C6)` o els valors mínim i màxim, sempre que les cinc files siguin observacions comparables. El percentatge d'habitatge no principal també és numèric, però no s'ha de sumar i la mitjana simple pot ser inadequada: per obtenir el percentatge conjunt cal sumar primer els habitatges no principals i dividir-los per la suma d'habitatges totals.

`Data de referència` és temporal. Es pot ordenar, obtenir-ne la més antiga o la més recent i restar dues dates per calcular una durada. `Revisat` és lògic: es pot filtrar o comptar amb `=COUNTIF(F2:F6,TRUE)`. Aquestes operacions depenen del significat de la columna, no només de l'alineació que mostra la pantalla.

>>> **Una comprovació visual ràpida.** Si gairebé tots els valors d'una columna queden a la dreta però una cel·la queda a l'esquerra, aquesta cel·la pot contenir un nombre desat com a text. La diferència pot venir d'un espai, un apòstrof inicial, un separador decimal inesperat o un símbol de la font.

L'alineació només és un indici. Un estil pot forçar qualsevol alineació, i les dates solen aparèixer a la dreta perquè internament es representen mitjançant nombres. Les funcions `ISNUMBER(A2)` i `ISTEXT(A2)` permeten comprovar què ha interpretat el programa. En una configuració traduïda, el nom de la funció pot aparèixer localitzat.

### Operacions amb dates

Una data no és un text decoratiu. Els fulls de càlcul solen desar-la com un nombre de sèrie i aplicar-hi un format de calendari. Això permet fer operacions temporals, però també genera resultats aparentment absurds si es confon el valor intern amb el que es mostra.

La família de normes **ISO 8601** defineix representacions de dates i hores per a l'intercanvi d'informació. En la forma estesa d'una data de calendari, ordena els components de major a menor: any de quatre dígits, mes de dos dígits i dia de dos dígits, separats per guionets: `YYYY-MM-DD` {% cite isoDateTime2019 %}. Així, `2026-04-03` identifica inequívocament el 3 d'abril de 2026.

Aquest ordre té un avantatge pràctic: si totes les dates vàlides utilitzen la mateixa representació, l'ordenació alfabètica també les ordena cronològicament. En canvi, `03/04/2026` és ambigu perquè pot significar el 3 d'abril o el 4 de març segons la convenció regional, i `3/4/26` afegeix l'ambigüitat de l'any abreujat.

::: table "Representacions ISO 8601 de data i hora"
| Exemple | Significat | Precaució |
| --- | --- | --- |
| `2026-04-03` | Data de calendari | No identifica una hora ni un fus horari |
| `2026-04-03T14:30:00` | Data i hora local | Sense desplaçament UTC, l'instant continua sent ambigu |
| `2026-04-03T14:30:00+02:00` | Data i hora amb desplaçament de dues hores respecte d'UTC | El desplaçament forma part del valor comunicat |
| `2026-04-03T12:30:00Z` | Data i hora en UTC | `Z` indica UTC i no s'ha d'afegir a una hora local |
:::

La `T` separa la data de l'hora. Els dos darrers exemples representen el mateix instant: les 14.30 amb desplaçament `+02:00` equivalen a les 12.30 UTC. Una **data de referència** com `2021-01-01` no necessita fus horari si només expressa el dia censal; una observació captada a una hora concreta sí que pot necessitar hora, desplaçament i zona temporal documentada.

Si `A2` conté una data de naixement reconeguda correctament, aquestes fórmules il·lustren operacions diferents:

```text
=TODAY()-A2
=DATEDIF(A2,TODAY(),"Y")
=A2+30
```

La primera calcula els dies transcorreguts; el resultat s'ha de formatar com a número, no com una altra data. La segona calcula els anys complets, útils per expressar l'edat en l'aniversari corresponent. La tercera suma una durada de trenta dies a una data. En canvi, sumar `A2+B2` quan totes dues cel·les contenen dates no acostuma a tenir cap interpretació temporal: el programa pot donar un resultat numèric, però l'operació no respon una pregunta coherent.

>>>> **Escriure una forma ISO no garanteix que la cel·la sigui una data.** Segons l'aplicació i la configuració regional, `2026-04-03` pot importar-se com un valor temporal o quedar com a text. Cal comprovar-ho amb `ISNUMBER`, ordenar una mostra i revisar el format. Dins del llibre convé conservar una data real amb format visible `yyyy-mm-dd`; en un CSV, cal documentar que la columna textual segueix ISO 8601 i tornar-la a interpretar explícitament en importar-la.

### Fórmules bàsiques per inspeccionar

Les fórmules següents són útils abans de transformar una taula. Suposen que les dades comencen a la fila 2:

::: table "Comprovacions inicials amb fórmules"
| Pregunta | Fórmula orientativa | Interpretació |
| --- | --- | --- |
| La cel·la és numèrica? | `=ISNUMBER(B2)` | Retorna cert si el programa reconeix un nombre |
| La cel·la és text? | `=ISTEXT(B2)` | Ajuda a detectar nombres o dates importats com a text |
| Quants caràcters té el codi? | `=LEN(A2)` | Permet comprovar longituds i zeros inicials |
| El codi està duplicat? | `=COUNTIF($A$2:$A$100,A2)>1` | Marca claus repetides dins del rang |
| Quantes cel·les són buides? | `=COUNTBLANK(B2:B100)` | Quantifica absències, però no n'explica el significat |
| Quants valors són numèrics? | `=COUNT(B2:B100)` | Es pot contrastar amb el nombre de files esperat |
:::

Els noms de les funcions i el separador d'arguments poden variar. Una configuració pot usar comes i una altra punt i coma; algunes aplicacions tradueixen els noms i d'altres conserven l'anglès. El criteri important és entendre la prova, no memoritzar una única sintaxi de la interfície.

### Models de llenguatge i fulls de càlcul

Alguns fulls de càlcul incorporen assistents basats en LLM i també hi ha extensions que envien instruccions i dades a aquests models per proposar fórmules, resumir taules, classificar textos o respondre preguntes sobre un llibre. Aquestes funcions poden ser útils quan el problema està ben delimitat, especialment per suggerir una fórmula, explicar un error o explorar una columna de text no estructurat. No converteixen, però, una petició ambigua en un mètode fiable.

Un model de llenguatge pot actuar com una caixa negra. Pot generar una fórmula plausible que use un rang equivocat, confondre una absència amb un zero, inventar una categoria o donar respostes diferents davant de peticions semblants. Si l'extensió envia dades a un servei extern, també cal revisar quina informació es transfereix, amb quines condicions i si el conjunt conté dades personals o restringides.

La reproduïbilitat exigeix saber quina operació s'ha aplicat. Una fórmula visible com `=F2/D2*1000`, una consulta de Power Query o un script versionat es poden inspeccionar i tornar a executar. Una resposta generada en una conversa només és reproduïble si es conserven com a mínim les dades d'entrada, la instrucció, el resultat, la data, el model i les comprovacions posteriors; fins i tot així, el servei i el model poden canviar.

::: table "Escollir l'eina segons l'operació"
| Situació | Eina generalment adequada | Motiu |
| --- | --- | --- |
| Mateix càlcul determinista per a moltes files | Fórmula, consulta o script | Resultat revisable, ràpid i reutilitzable |
| Neteja repetida d'una taula coneguda | Power Query, OpenRefine o script | Passos explícits que es poden tornar a executar |
| Exploració visual d'una taula petita | Full de càlcul | Inspecció directa i cost d'entrada baix |
| Interpretació inicial de text no estructurat | Model de llenguatge amb revisió humana | Pot proposar categories o patrons que després cal validar |
| Explicació d'un error o proposta de fórmula | Assistent basat en un LLM | Accelera l'exploració, però no substitueix la prova |
| Operació crítica, estable i recurrent | Fórmula validada, consulta o codi versionat | Facilita manteniment, autoria i control de canvis |
:::

Fer que un LLM processi repetidament cada fila pot consumir temps, diners, context i tokens per resoldre una operació que una fórmula executa de manera immediata i exacta. També crea una dependència d'un proveïdor i dificulta mantenir el procés quan canvien el model, el preu o l'extensió. En canvi, descartar sempre els LLM faria perdre una eina útil per a problemes que sí que requereixen interpretació flexible del llenguatge.

>>>> **Automatitzar no elimina la responsabilitat tècnica.** La decisió important no és si s'ha usat un LLM, sinó per què era l'eina adequada, quines dades ha rebut, com s'ha verificat el resultat i si el procediment es podrà mantenir i reutilitzar. Aquest criteri l'aporta la persona que coneix la pregunta, les dades i els límits de l'anàlisi.

## Activitats: preparar les dades d'una comarca

El fil conductor del manual serà una diagnosi breu de **població i habitatge d'una comarca tarragonina**. Cada fila representarà un municipi de la comarca i tots els capítols reutilitzaran les mateixes dades. El Tarragonès servirà com a demostració comuna perquè combina una capital, municipis litorals turístics, espais residencials i municipis petits d'interior. La comarca concreta de cada projecte s'indicarà o validarà mitjançant Moodle.

La pregunta general serà: **com es distribueixen la població i el parc d'habitatges entre els municipis de la comarca, i quins contrastos territorials s'hi observen?** En aquest capítol encara no es calcularan indicadors ni es produiran figures. Es prepararà una fila coherent per municipi que pugui alimentar els càlculs, gràfics i mapes posteriors.

::: table "Paquet mínim de dades per municipi"
| Component | Contingut | Font de demostració | Ús posterior |
| --- | --- | --- | --- |
| Identificació territorial | Codi i nom de municipi; codi i nom de comarca | Idescat, Codis territorials i d'entitats | Filtrar la comarca i controlar les unions |
| Població | Total i grans grups d'edat: 0–14, 15–64 i 65 anys o més | Idescat, Cens de població i habitatges 2021 | Estructura demogràfica i denominadors |
| Habitatges | Total, principals i no principals | Idescat, Cens de població i habitatges 2021 | Composició del parc residencial |
| Territori | Superfície municipal en km² | Idescat, Indicadors demogràfics i de territori | Densitat de població i context espacial |
:::

Població i habitatges es fixen en 2021 perquè provenen de la mateixa operació censal i són comparables temporalment. Una xifra de població més recent seria útil per a altres preguntes, però barrejar-la sense advertiment amb habitatges de 2021 faria que els quocients ja no descrivissin exactament el mateix moment.

>>>> **Habitatge no principal no significa habitatge turístic.** En aquesta taula, la categoria combina habitatges ocupats ocasionalment i habitatges buits. Pot ajudar a interpretar contrastos residencials i territorials, però no permet afirmar quants habitatges es destinen al turisme. Aquesta relació requeriria una altra font i una definició específica.

### Descarregar manualment les taules d'Idescat

La demostració començarà a la pàgina de cada taula, no en una API. Això obliga a llegir-ne el títol, l'any, les categories, la metodologia i les notes abans de descarregar-la.

1. Obriu [Població. Per sexe i edat en grans grups](https://www.idescat.cat/pub/?id=censph&n=540&lang=ca), seleccioneu l'any 2021 i el nivell **tots els municipis**, i premeu **Descarregar**.
2. Obriu [Habitatges. Per tipus d'habitatge](https://www.idescat.cat/pub/?id=censph&n=30&lang=ca), manteniu l'any 2021, seleccioneu **tots els municipis** i descarregueu la taula.
3. Descarregueu la taula de [codis de municipis i comarques](https://www.idescat.cat/codis/?id=50&n=9&lang=ca). Aquesta correspondència permet identificar els municipis de la comarca sense filtrar només pel nom.
4. Obriu [Superfície, densitat i entitats singulars](https://www.idescat.cat/pub/?id=inddt&n=396&lang=ca) i descarregueu la superfície municipal disponible.
5. Deseu els fitxers tal com arriben a `data/raw` i registreu-ne l'URL, la data d'accés, l'any de referència i qualsevol selecció aplicada.

Les descàrregues d'Idescat poden arribar com a text separat per punt i coma. S'han d'**importar** amb codificació UTF-8, delimitador `;` i codi municipal com a text. Obrir-les directament amb doble clic pot eliminar zeros inicials o interpretar incorrectament accents, decimals i dates.

La taula de codis conté el codi de comarca. Primer s'incorporarà aquesta correspondència a les altres taules mitjançant el codi municipal de sis dígits; després es filtraran les files de la comarca seleccionada. El prefix provincial `43` no és suficient, perquè inclou tots els municipis de la província de Tarragona.

Les dades censals d'habitatges poden aplicar arrodoniments aleatoris a múltiples de tres per protegir el secret estadístic. Per això alguna suma de components pot diferir lleugerament del total publicat. Aquesta diferència no s'ha de «corregir» repartint-la manualment: s'ha de conservar i documentar.

### Descarregar i preservar els originals

Les dades descarregades rarament es poden analitzar de manera immediata. Poden contenir títols dins de la taula, capçaleres dobles, notes al peu, totals barrejats amb territoris, codis convertits en nombres, símbols de confidencialitat, decimals interpretats com a text o una estructura pensada per a lectura humana i no per al càlcul.

La preparació no és una operació mecànica que «neteja» qualsevol irregularitat. Cada canvi implica una decisió sobre el significat de les dades. El procés ha de separar els errors corregibles dels valors desconeguts i de les diferències conceptuals que no es poden harmonitzar legítimament.

![Cadena de preparació de dades]({{ site.baseurl }}/assets/diagrams/data-preparation-pipeline.mmd "Cadena de preparació: de la còpia original a la taula analítica i els productes finals")

### Eines segons el problema

No hi ha una única eina de preparació. L'elecció depèn del volum, la complexitat, la necessitat de repetir els passos i el tipus de dada.

::: table "Eines habituals per preparar dades"
| Família | Exemples | Ús adequat | Límit que cal vigilar |
| --- | --- | --- | --- |
| Full de càlcul | Aplicació compatible acordada a l'inici del curs | Inspecció, fórmules, taules dinàmiques i transformacions de volum moderat | Canvis manuals difícils de rastrejar, conversions automàtiques i diferències de compatibilitat |
| Transformació visual | Power Query, OpenRefine | Passos repetibles, remodelació, normalització de text i correspondències | Cal conservar i documentar la seqüència aplicada |
| Programació | Python amb pandas; R amb readr o dplyr | Automatització, grans volums, validacions i processos repetits | Requereix codi, dependències i versions documentades |
:::

En aquest primer bloc, les operacions s'explicaran segons el funcionament comú dels fulls de càlcul i amb l'aplicació acordada a l'inici del curs. Les biblioteques de Python o R no seran un requisit general, però permeten entendre com pot evolucionar el procés quan una transformació s'ha de repetir moltes vegades o deixa de ser segura manualment. Les eines cartogràfiques s'introduiran més endavant, quan les taules ja estiguin preparades.

### Construir una estructura analitzable

Una taula ordenada facilita les operacions posteriors. El principi de *tidy data* proposa que cada variable ocupi una columna, cada observació una fila i cada tipus d'unitat d'observació una taula {% cite wickhamTidyData2014 %}. No és l'única estructura possible, però resulta especialment útil per filtrar, agrupar, calcular, representar i unir dades.

::: table "D'una taula de publicació a una taula analítica"
| Problema habitual | Transformació justificada | Comprovació |
| --- | --- | --- |
| Un any per columna | Passar els anys a una columna `any` i els valors a `valor` | El nombre de valors es conserva |
| Municipi i codi en una mateixa cel·la | Separar `codi_municipi` i `nom_municipi` | Tots els codis tenen la longitud prevista |
| Guions, `..` o `:` en cel·les numèriques | Conservar un camp d'estat i assignar valor absent | No es converteix confidencial o no disponible en zero |
| Totals barrejats amb municipis | Identificar el nivell territorial abans de filtrar | La suma només es compara amb totals compatibles |
| Notes sota les dades | Traslladar-les a documentació, no esborrar-les | Les definicions continuen disponibles |
| Separador decimal inconsistent | Convertir amb una regla explícita | Mínims, màxims i recompte concorden amb l'original |
:::

### Organitzar un flux de treball reproduïble

Es conservaran tres nivells de dades:

1. **Originals:** còpia exacta del fitxer o resposta obtinguda, sense canvis.
2. **Intermèdies:** dades importades i transformades, amb passos identificables.
3. **Analítiques:** taules finals preparades per calcular indicadors, fer gràfics i reutilitzar-se en les fases posteriors.

No s'ha de corregir manualment el fitxer original. Una correcció feta directament sobre una cel·la pot ser impossible de detectar després. En canvi, una columna nova, una consulta de Power Query o un full de correspondències deixa visible la regla aplicada.

L'estructura proposada separa `data/raw` de `data/processed`. Tot el treball tabular es farà en **un únic llibre**, amb un nom com `territorial_context_tarragones.xlsx`. No es crearà un llibre per a cada font ni còpies com `final2.xlsx`.

::: table "Fulls del llibre acumulatiu"
| Full | Funció |
| --- | --- |
| `project` | Pregunta, comarca, autoria, aplicació, configuració regional i ubicació de treball |
| `sources` | Productor, taula, URL, any, data d'accés, llicència i notes |
| `dictionary` | Camp, definició, tipus, unitat, font i tractament d'absències |
| `raw_codes` | Còpia importada dels codis municipals i comarcals |
| `raw_population` | Còpia importada de la taula de població de 2021 |
| `raw_housing` | Còpia importada de la taula d'habitatges de 2021 |
| `raw_territory` | Còpia importada de la superfície municipal |
| `checks` | Recompte de files, duplicats, absències, sumes i incidències |
| `municipal_table` | Una fila per municipi de la comarca i només variables preparades |
| `indicators` | Fórmules que s'afegiran al capítol 2 |
| `charts` | Gràfics editables que s'afegiran al capítol 3 |
| `map_export` | Taula plana que es reutilitzarà més endavant als mapes |
:::

Els fulls `raw_*` no se sobreescriuran amb correccions manuals. Les transformacions s'aplicaran a `municipal_table` mitjançant fórmules, consultes o passos documentats. El diccionari de dades ha d'explicar camps, tipus, unitats, codis, valors absents i procedència.

### Fer la inspecció inicial amb Excel

Abans de transformar, es farà una diagnosi:

- nombre de files i columnes;
- unitat que representa cada fila;
- tipus i rang de cada camp;
- valors únics de les variables categòriques;
- camps buits i símbols especials;
- duplicats de la clau esperada;
- totals i valors de control publicats per la font;
- coherència entre període, territori i unitat.

Les eines de filtre, ordenació, format condicional, taules dinàmiques i Power Query poden ajudar a inspeccionar. Les fórmules també permeten construir comprovacions, però no s'han d'usar per ocultar errors amb substitucions indiscriminades.

### Normalitzar codis territorials i claus d'unió

Els noms geogràfics no són claus fiables. Poden variar per llengua, accents, articles, abreviatures o canvis de denominació. Les unions s'han de fer amb identificadors documentats: codis INE, Idescat, NUTS o altres codis oficials.

>>>> **Els codis no són quantitats.** Excel i altres fulls de càlcul poden interpretar `01` com el nombre `1`, transformar codis llargs o convertir valors en dates. Els identificadors s'han d'importar com a **text**. Afegir zeros després només és legítim si es coneix l'esquema exacte del codi; no s'ha de reparar un identificador per intuïció.

Abans d'una unió cal comprovar:

- que totes dues fonts utilitzen el mateix sistema de codis i el mateix any de classificació;
- que la clau és única al costat on s'espera una fila per territori;
- quants registres coincideixen i quants queden sense correspondència;
- si hi ha agregats, territoris desapareguts o delimitacions diferents;
- si totes les taules representen realment la mateixa unitat territorial.

### Tractar valors absents, zero i confidencialitat

Un zero indica una quantitat observada igual a zero. Una cel·la buida pot indicar que no es disposa de la dada, que no és aplicable, que s'ha suprimit per confidencialitat o que la combinació no s'ha mesurat. Són situacions diferents.

>>>>>> **No s'ha de convertir una absència en zero.** Aquesta substitució altera sumes, mitjanes, taxes i gràfics, i pot transformar «no es coneix» en «no existeix». Abans de convertir una columna a número cal identificar els símbols de la font i conservar-ne el significat.

Les fonts utilitzen símbols i flags propis, com `:`, `..`, `c`, `p` o `e`. Abans de convertir una columna a número cal llegir la llegenda i conservar l'estat en una columna separada. Substituir tots els símbols per zero altera la informació i pot falsejar sumes, mitjanes i mapes.

### Validar després de transformar

Cada transformació ha de tenir una comprovació. Si es remodela una taula, s'ha de verificar que no s'han perdut valors. Si s'eliminen duplicats, cal explicar per què eren duplicats i no observacions legítimes. Si s'uneixen fonts, s'han de comptar coincidències i absències. Si es calcula un total, s'ha de contrastar amb una publicació de referència quan sigui possible.

Una taula preparada no és necessàriament correcta perquè Excel no mostri errors. La validació combina controls tècnics, comparació amb la font i judici substantiu sobre valors plausibles.

### Preparar i auditar la taula comarcal

Les quatre descàrregues no formen encara una taula analítica. Poden ordenar els municipis de manera diferent, anomenar els camps amb capçaleres de publicació i barrejar totals amb components. La preparació haurà d'obtenir una única fila per municipi sense copiar valors a mà ni unir les fonts per posició de fila.

#### 1. Documentar les fonts

Es registrarà per a cada taula el productor, el títol exacte, la metodologia, el període, la unitat, la cobertura, la data d'accés i la llicència. La fitxa inclourà l'URL de la taula, no només la portada d'Idescat.

#### 2. Diagnosticar sense corregir

Es descriurà la unitat d'observació, s'identificarà la clau territorial i es construiran controls de files, valors absents, duplicats i rangs. Els problemes es classificaran com a errors de format, possibles errors de contingut o diferències conceptuals.

::: table "Preguntes per auditar una taula territorial"
| Aspecte | Pregunta de control | Risc si no es revisa |
| --- | --- | --- |
| Unitat d'observació | Cada fila representa el mateix tipus de territori? | Comparar municipis, comarques o agregacions diferents |
| Identificador | El codi conserva longitud, prefixos i zeros inicials? | Perdre correspondències en la unió |
| Cobertura | Les fonts contenen els mateixos territoris? | Interpretar una absència com un valor zero |
| Tipus de dada | El camp és text, enter o decimal? | Impedir càlculs o unions correctes |
| Files no analítiques | Hi ha títols, notes o fonts dins de la taula? | Incorporar text com si fos una observació |
| Metadades | Es coneixen definició, període, unitat i autoria? | Produir un indicador que no es pot defensar |
:::

#### 3. Transformar amb rastre

La versió preparada no substituirà l'original. El llibre distingirà les dades rebudes, el diccionari, les comprovacions i `municipal_table`. Es conservaran els codis com a text, es filtraran els municipis mitjançant el codi de comarca i es documentaran els valors no numèrics.

#### 4. Validar

La taula final haurà de superar quatre controls: nombre justificat de files, clau territorial sense duplicats inesperats, valors dins de rangs plausibles i correspondència amb un total o resultat publicat.

### Evidències que s'han de conservar

La guia docent preveu el lliurament d'activitats de laboratori i permet que el professorat demani fitxers intermedis per comprovar el procés. Aquesta activitat ha de deixar preparades les evidències següents, encara que Moodle indiqui quines s'han de trametre en cada moment:

::: table "Evidències de la preparació comarcal"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| Arrel | `README.md` | Comarca, pregunta, fonts, llicències, dates i estructura del projecte |
| `data/raw` | Fitxers originals | Descàrregues sense modificar i, si escau, URL o consulta de l'API |
| `data/processed` | Un únic llibre de treball | Fulls descrits al model acumulatiu, sense llibres paral·lels |
| `data/processed` | `municipal_table` | Una fila per municipi, codis com a text, unitats explícites i valors absents documentats |
| `data/processed` | Registre de transformacions | Regles aplicades, correspondències i incidències no resoltes |
:::

La carpeta `outputs` encara no ha de contenir la infografia final. Les figures que es generin al capítol 3 s'hi desaran com a resultats intermedis reutilitzables; el document final de síntesi s'exportarà més endavant a `dist`.

En acabar, s'haurà construït una base comarcal depurada amb una fila per municipi, codis consistents i camps preparats per calcular indicadors. La competència principal no és descarregar molts fitxers, sinó construir una cadena d'evidència defensable: pregunta, productor, definició, selecció, còpia original, transformacions i validació.
