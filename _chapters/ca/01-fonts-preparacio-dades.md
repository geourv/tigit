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

Mai no havíem tingut tants recursos per observar el territori. Les administracions publiquen estadístiques, registres, ortofotos, mapes, sensors, serveis de consulta automàtica i portals de dades obertes; les plataformes digitals generen rastres de mobilitat, consum, opinió i activitat; i els models de llenguatge han afegit una nova capa d'assistència per cercar, resumir, transformar i interpretar informació. Aquesta abundància, però, no resol automàticament cap problema territorial.

Com més dades i eines hi ha, més important esdevé el **criteri**. Cal criteri per plantejar preguntes que es puguin respondre, per distingir una font fiable d'una xifra sense context, per saber què diu realment una taula, per detectar què no diu i per transformar informació dispersa en decisions més ben fonamentades. En geografia i turisme, treballar amb dades no és acumular fitxers: és construir una cadena d'evidència defensable.

Aquest capítol introdueix aquesta cadena. Primer parteix de reptes territorials, turístics i ambientals que exigeixen preguntes concretes. Després ordena els tipus de fonts i mostra on buscar dades a escala global, europea, estatal, catalana i local. A continuació explica com verificar una font, llegir-ne les metadades, respectar-ne les condicions d'ús i triar vies d'accés adequades. Finalment, prepara una primera taula territorial en un full de càlcul, normalment comarcal en la demostració del curs, amb originals conservats, transformacions documentades i dades a punt per calcular, representar i cartografiar en els capítols següents.

>>>>> En acabar el capítol, cal poder localitzar una font adequada, llegir-ne les metadades bàsiques i preparar una primera taula territorial sense perdre la traçabilitat.
>>>>>
>>>>> - Formular una pregunta abans de descarregar dades.
>>>>> - Relacionar reptes territorials, turístics i ambientals amb evidències possibles.
>>>>> - Reconèixer qui produeix una dada, on es documenta, com s'obté i quan incorpora geometria.
>>>>> - Reconèixer llicències, dates, cobertura, unitats i limitacions.
>>>>> - Separar una taula de publicació d'una taula analítica rectangular.
>>>>> - Conservar originals, fonts, transformacions i comprovacions.

La ruta mínima de treball és sempre la mateixa, encara que la font canviï. Primer es formula una pregunta amb fenomen, territori, període, unitat d'observació i mesura. Després es tria una font que realment pugui respondre-la, es comproven productor, definició, cobertura, data i llicència, i només aleshores es descarrega o consulta la dada. El resultat del capítol no és un fitxer acumulat sense criteri, sinó una primera base territorial que conserva els originals, explica d'on surt cada camp i deixa preparades les comprovacions per als capítols següents.

## Preguntes i dades

El primer pas no és descarregar una taula, sinó delimitar què es vol saber. Una pregunta clara permet decidir quina unitat d'observació, quin període, quina mesura i quin nivell territorial cal buscar.

>>>>> El treball comença convertint una curiositat inicial en una pregunta de dades comprovable.
>>>>>
>>>>> - Formular una pregunta abans d'obrir un portal.
>>>>> - Distingir opinió, prejudici, hipòtesi, evidència, coneixement i valor.
>>>>> - Separar fenomen, unitat d'observació, territori, període i mesura.
>>>>> - Entendre que una dada és una representació construïda, no el fet mateix.

### Reptes territorials i preguntes de dades

Un mateix territori pot llegir-se com a sistema ambiental, paisatge, espai residencial, destinació turística, infraestructura hídrica, mercat laboral, xarxa de mobilitat o espai de risc. Cada lectura obre preguntes diferents i exigeix fonts diferents. La funció de les dades no és substituir el judici professional, sinó convertir una preocupació general en una pregunta que es pugui contrastar amb evidències.

Entre molts problemes possibles, podem destacar els següents. No formen un catàleg tancat ni jeràrquic: energia, salut pública, treball, patrimoni, alimentació, fiscalitat local o risc tecnològic també poden requerir dades territorials. La utilitat de la llista és mostrar que cada repte obliga a canviar la pregunta, la unitat d'observació, l'escala i la font.

- **Medi ambient i canvi climàtic.** Els reptes més amplis apareixen quan el territori s'entén com a part d'un sistema climàtic i ecològic. L'escalfament global ja afecta extrems meteorològics, ecosistemes, salut i activitats humanes, i a Europa els riscos climàtics comprometen energia, alimentació, aigua, infraestructures i salut pública {% cite ipccClimateChange2023Synthesis eeaEuropeanClimateRiskAssessment2024 %}. Una pregunta territorial no pot limitar-se a preguntar si «fa més calor»: ha de precisar lloc, període, exposició, vulnerabilitat i indicador, com temperatura màxima, nits tropicals, risc d'incendi, episodis de sequera o impacte sobre una activitat turística concreta.
- **Usos del sòl, paisatge i biodiversitat.** Els canvis en cobertes i usos del sòl transformen paisatges, hàbitats, serveis ecosistèmics i possibilitats d'ús social. La pressió urbanitzadora, l'abandonament agrari, la intensificació agrícola, les infraestructures i la fragmentació ecològica no es poden valorar només amb impressions visuals. La recerca sobre usos del sòl mostra que aquests canvis tenen conseqüències globals sobre clima, aigua, biodiversitat i serveis ecosistèmics, i que la pèrdua de biodiversitat local s'associa de manera directa amb la transformació i intensificació del territori {% cite foleyGlobalConsequencesLandUse2005 newboldGlobalEffectsLandUse2015 eeaSignalsLandSoil2019 %}. En aquest curs, això pot traduir-se en preguntes sobre superfície urbanitzada, cobertes forestals, canvis de conreu, continuïtat d'espais oberts o pèrdua de paisatge agrari.
- **Aigua i recursos hídrics.** La disponibilitat d'aigua connecta clima, usos del sòl, agricultura, població resident, turisme i ecosistemes. No n'hi ha prou amb preguntar si «hi ha sequera»; cal distingir precipitació, reserves, demanda, consum, pressió estacional i mesures de gestió. L'indicador europeu d'escassetat hídrica mostra que la pressió sobre els recursos d'aigua dolça varia espacialment i temporalment i pot intensificar-se en períodes secs o zones amb elevada demanda, mentre que la literatura sobre turisme i aigua remarca la necessitat de relacionar consum, temporada, allotjament, infraestructures i seguretat hídrica {% cite eeaWaterScarcityWEI2025 gosslingTourismWaterUse2012 %}. Per tant, una destinació amb molta ocupació turística pot requerir dades de població present, allotjament, consums, conques, infraestructures i restriccions.
- **Activitat turística i capacitat d'acollida.** El turisme genera ocupació, ingressos i serveis, però també pressions sobre espai públic, recursos, residus, mobilitat, habitatge i convivència. Els marcs d'indicadors de turisme sostenible insisteixen que la gestió d'una destinació necessita mesurar impactes econòmics, socials, culturals i ambientals, no només arribades o pernoctacions; els debats sobre sobrefreqüentació turística recorden, a més, que els impactes depenen del context urbà, dels actors afectats i de la governança de la destinació {% cite europeanCommissionETIS2016 unTourismStatisticalFrameworkMST2024 torresDelgadoMeasuringSustainableTourism2014 koensIsOvertourismOverused2018 %}. Preguntar si una destinació és competitiva no equival a preguntar si és sostenible; preguntar si hi ha molta oferta d'allotjament tampoc no equival a saber si aquesta oferta pressiona l'aigua, el paisatge o l'habitatge.
- **Mobilitat, accessibilitat i seguretat.** La mobilitat quotidiana i estacional condiciona accés a serveis, congestió, emissions, sinistralitat, exposició a riscos i experiència turística. Les dades agregades de telefonia mòbil o de targetes de transport permeten estudiar fluxos i perfils temporals, però sempre amb limitacions de cobertura, privacitat i mètode {% cite ministerioMovilidadBigData2026 gutierrezSmartTravelCardTourism2020 zaragoziPassiveMobileData2021 %}. Una pregunta útil no és només si «hi ha molta gent», sinó en quines franges, en quins corredors, amb quins mitjans, amb quina població exposada i amb quins efectes sobre accessibilitat, seguretat o qualitat de vida.
- **Despoblament i desigualtat territorial.** Els territoris rurals i interiors no només afronten menys densitat de població; poden acumular envelliment, pèrdua de serveis, dificultats d'accés, menor diversificació econòmica i dependència de xarxes de mobilitat o connectivitat digital. L'OCDE planteja el benestar rural com una qüestió de geografia d'oportunitats, en què població, serveis, ocupació, accessibilitat i qualitat ambiental s'han d'analitzar conjuntament, i la literatura sobre evolució rural mostra que el declivi o la revitalització depenen de trajectòries territorials, connexions, polítiques i estructura econòmica, no només de la grandària del municipi {% cite oecdRuralWellBeing2020 liWhyRuralAreasDecline2019 %}. Per això el despoblament no es pot reduir a una variació negativa del padró: cal observar estructura per edat, habitatges buits, temps d'accés, activitat econòmica, equipaments i relació amb municipis propers.
- **Habitatge i vida quotidiana.** La crisi d'habitatge combina disponibilitat, distribució territorial, règim de tinença, preus, renda, mobilitat i usos residencials o turístics. L'OCDE mostra que l'habitatge s'ha d'entendre alhora com a bé de consum, actiu econòmic i component de benestar, amb efectes sobre desigualtat, localització de la població i oportunitats, mentre que la recerca sobre allotjament turístic de curta durada ha documentat tensions específiques entre plataforma, mercat residencial, regulació urbana i vida quotidiana {% cite oecdBrickByBrick2021 gurranWhenTouristsMove2017 wachsmuthAirbnbRentGap2018 %}. En un municipi turístic, preguntar pel nombre d'habitatges no basta: cal distingir habitatge principal, secundari, buit, lloguer, compravenda, habitatge d'ús turístic, accessibilitat econòmica i distribució per barris o seccions censals.

Aquest recorregut va de problemes amplis a qüestions cada vegada més operatives. Els grans reptes orienten la mirada, però l'anàlisi comença quan es formula una pregunta capaç d'identificar fenomen, unitat d'observació, territori, període i mesura. Sense aquesta concreció, les dades només acumulen xifres; amb aquesta concreció, poden corregir impressions, fer visibles desigualtats i sostenir decisions més responsables.

El pas de repte a pregunta es fa avui en un entorn informatiu saturat. Internet, les xarxes socials, els sistemes de recomanació, la publicitat segmentada i els reenviaments instantanis poden amplificar rumors, simplificacions i afirmacions falses abans que una institució, un equip científic o un mitjà les hagi pogut verificar. No tot error és desinformació: també hi ha confusions honestes, dades mal interpretades, titulars exagerats i desacords legítims. Però la recerca sobre informació falsa en línia mostra que les notícies falses poden difondre's ràpidament en xarxes socials, i els estudis sobre *fake news* les situen com un problema sociotècnic que combina incentius econòmics, plataformes, actors polítics, bots, audiències i manca de verificació {% cite vosoughiSpreadTrueFalseNews2018 lazerScienceFakeNews2018 wardleInformationDisorder2017 %}.

La fabricació de dubte no comença amb internet. *Merchants of Doubt* mostra com alguns actors van explotar la incertesa científica per sembrar confusió pública en debats sobre tabac, pluja àcida, ozó i canvi climàtic {% cite oreskesMerchantsDoubt2010 %}. Aquest patró és important per a la informació geogràfica i turística perquè molts conflictes territorials barregen dades, interessos, valors i identitats: sostenibilitat, habitatge, mobilitat, aigua o canvi climàtic poden aparèixer com a disputes d'opinió quan en realitat inclouen afirmacions que sí que es poden contrastar. El problema no és que hi hagi debat; el problema és presentar una afirmació sense font, una incertesa parcial o una estratègia de comunicació interessada com si tinguessin el mateix pes que una evidència documentada.

A partir d'aquest problema s'entén millor per què interessen Mill, Popper i Kuhn. En *On Liberty*, publicat el 1859, John Stuart Mill defensa la llibertat de pensament i discussió davant la pressió social i política per silenciar opinions dissidents. El seu argument no és que totes les opinions siguin igualment bones, sinó que una societat necessita exposar-les a discussió perquè l'error es pugui detectar, les veritats parcials es puguin corregir i les idees acceptades no es converteixin en dogmes morts {% cite millOnLiberty1859 %}.

Popper escriu en un altre context. *Conjectures and Refutations*, publicat el 1963, és una obra de filosofia de la ciència centrada en com creix el coneixement mitjançant conjectures, crítica i intents de refutació. El seu criteri de falsabilitat no diu que una afirmació sigui falsa d'entrada, sinó que una afirmació que vol ser analítica ha d'exposar-se a proves que podrien mostrar-ne els errors. En una obra anterior, *The Open Society and Its Enemies*, publicada el 1945 després de l'experiència dels totalitarismes europeus, Popper defensa la societat oberta contra doctrines que tanquen la discussió i presenten decisions imposades com si fossin conseqüències inevitables de la història {% cite popperConjecturesRefutations1963 popperOpenSocietyEnemies1945 %}. En el context del curs, aquesta oposició entre societat oberta i societat tancada no s'ha de llegir com una etiqueta política simple, sinó com una defensa de l'espai on les afirmacions públiques poden ser discutides, documentades i revisades.

> «[…] real support can be obtained only from observations undertaken as tests (by “attempted refutations”); and for this purpose criteria of refutation have to be laid down beforehand […].» {% cite popperConjecturesRefutations1963 %}

Una tercera peça ajuda a no convertir aquesta exigència crítica en una recepta fixa. Kuhn va mostrar que la ciència treballa dins de marcs compartits, o **paradigmes**, que orienten quins problemes semblen rellevants, quins mètodes es consideren acceptables i quin tipus d'evidència compta com a resposta; aquests marcs també poden canviar quan s'acumulen anomalies i una comunitat reorganitza la manera d'entendre el seu camp {% cite kuhnStructureScientificRevolutions1962 %}. Lectures contemporànies sobre el funcionament de la ciència, com la de Strevens, insisteixen que la força del treball científic no prové d'un mètode immòbil, sinó de normes compartides que obliguen a fer públics els arguments empírics i a sotmetre'ls a discussió {% cite strevensKnowledgeMachine2020 %}. En aquest manual, això implica que els marcs que ordenen el pas de les dades a la informació, al coneixement i a la decisió són útils, però adaptables: ajuden a orientar la recerca, no substitueixen la necessitat de revisar-los quan el problema, l'escala o l'evidència ho demanen. Canviar de marc quan les dades i la discussió ho exigeixen no és el mateix que fabricar dubte per evitar una conclusió incòmoda.

Traslladada al treball territorial, aquesta idea no exigeix convertir una pràctica de primer curs en filosofia de la ciència. El criteri és més simple: una opinió analítica ha d'indicar quina observació podria matisar-la o fer-la insostenible. Dir que un centre urbà està saturat, que una destinació és sostenible o que el turisme pressiona l'habitatge només és útil si s'especifiquen indicadors, escales, períodes i fonts que permetin discutir la frase obertament. Per tant, una opinió pot ser legítima i orientar una recerca, però només esdevé útil per a l'anàlisi quan es formula de manera que pugui ser contrastada amb definicions, dades fiables i lògica.

La taula següent és un **marc lèxic de treball**, no una taxonomia filosòfica tancada. Serveix per distingir nivells de solidesa argumental en una diagnosi territorial i per evitar que una preferència, un prejudici o una impressió es presentin com si fossin evidència. La progressió no elimina els valors: ajuda a fer-los explícits i a separar-los de les afirmacions que sí que s'han de poder contrastar.

::: table "Marc lèxic de la percepció a una pregunta contrastable"
| Punt de partida | Exemple | Com es treballa amb dades |
| --- | --- | --- |
| Opinió | «El centre està saturat» | Definir saturació, període, lloc, indicador i font abans de valorar-la |
| Prejudici | «Els visitants sempre degraden el barri» | Formular una hipòtesi que es pugui contrastar amb residència, ús, temporada i altres factors |
| Hipòtesi o idea guia | «La pressió varia segons temporada, carrer i tipus d'allotjament» | Definir observacions esperades, fonts, unitats i criteri de contrast |
| Evidència | Recompte, registre, mesura o observació documentada | Verificar productor, definició, cobertura, qualitat i comparabilitat |
| Coneixement | Relació defensable entre pressió turística, habitatge, mobilitat o consum d'aigua | Integrar diverses fonts, explicar límits i contrastar alternatives |
| Valor | Prioritzar sostenibilitat, seguretat, equitat, competitivitat o preservació del paisatge | Fer explícit el criteri de decisió i no presentar-lo com si fos una dada neutra |
:::

### La pregunta precedeix la cerca

Una cerca sense pregunta acostuma a produir una acumulació de fitxers, no una base d'anàlisi. Abans d'obrir un portal convé formular què es vol saber i precisar almenys cinc components:

1. **El fenomen:** població resident, oferta d'allotjament, arribades, pernoctacions, despesa, ocupació, mobilitat o coberta del sòl, entre d'altres.
2. **La unitat d'observació:** una persona, un establiment, un municipi, una comarca, una regió, un país o una cel·la ràster.
3. **L'àmbit territorial:** quins territoris s'inclouen i a quin nivell geogràfic.
4. **El període:** un instant, un mes, un any, una temporada o una sèrie temporal.
5. **La mesura:** recompte, percentatge, mitjana, índex, taxa, superfície o una altra unitat.

No és equivalent preguntar quants establiments estan inscrits en un registre, quants estan oberts, quantes places ofereixen o quantes pernoctacions han registrat. Tampoc no és equivalent comptar turistes, viatgers, arribades, visites, passatgers o pernoctacions. Una font pot ser oficial i de qualitat i, malgrat això, no servir per respondre la pregunta formulada.

### Un cicle per elaborar coneixement territorial

El curs utilitza el descobriment de coneixement en bases de dades, o **KDD** (*knowledge discovery in databases*), com a marc general per entendre el procés. Fayyad, Piatetsky-Shapiro i Smyth descriuen el KDD com un procés interactiu i iteratiu que passa per selecció de dades, preprocessament, transformació, mineria de dades i interpretació o avaluació dels patrons trobats; en aquest recorregut apareixen dades objectiu, dades preprocessades, dades transformades, patrons i coneixement {% cite fayyadDataMiningKnowledge1996 %}. En aquest manual no s'entén com una promesa que qualsevol gràfic produeixi un descobriment científic nou. Serveix per recordar que el coneixement territorial depèn d'una cadena de decisions: què s'observa, quines dades es conserven, com es preparen, quin patró s'analitza i com s'interpreta.

Aquest cicle es pot relacionar amb la jerarquia dades-informació-coneixement-saviesa, sovint coneguda com a DIKW. Rowley en revisa les representacions i mostra que és una jerarquia molt utilitzada, però també discutida, perquè no sempre hi ha acord sobre què transforma les dades en informació, la informació en coneixement i el coneixement en saviesa {% cite rowleyWisdomHierarchy2007 %}. Per això aquí s'utilitza com una guia crítica, no com una escala automàtica. Una observació es converteix en dada quan queda codificada amb unitat, temps, lloc i mètode. Les dades es converteixen en informació quan s'hi afegeixen context, metadades i comparació. L'anàlisi busca patrons, diferències i relacions. El coneixement apareix quan aquests resultats es contrasten amb definicions, teoria, experiència territorial i altres fonts. La saviesa pràctica no és només saber més: és usar aquest coneixement amb criteri, experiència i valors explícits per orientar una decisió.

![Cicle d'elaboració de coneixement territorial]({{ site.baseurl }}/assets/img/data-sources/kdd-dikw-cycle.svg "El diagrama ajuda a llegir una dada com a part d'un procés: el repte genera observacions, les dades se seleccionen i es preparen, l'anàlisi detecta patrons i l'avaluació els converteix en coneixement útil per decidir. La decisió retorna al repte i pot obrir noves observacions. Figura d'elaboració pròpia basada en el procés KDD.")

El diagrama també mostra un retorn: una decisió o una política pot reformular el repte inicial i generar noves observacions. Si una destinació limita l'accés a un espai natural, canvia la mobilitat o regula l'allotjament, el coneixement acumulat no tanca el problema; obliga a observar què ha passat després. Aquesta és la diferència entre una dada aïllada i una pràctica informada: l'aprenentatge es reaprofita, però continua sotmès a revisió.

### Les dades no són els fets mateixos

Una dada és una representació codificada d'algun aspecte de la realitat. Entre el fenomen i la cel·la d'una taula hi ha decisions: què es considera turista, com es recull la resposta, com es tracta una absència, quin territori s'assigna a l'observació i quan es revisa la sèrie. Per això no existeixen dades completament «crues» en el sentit d'estar lliures de decisions prèvies. Sí que es pot parlar de **dades originals del projecte** per designar la còpia rebuda o descarregada abans de modificar-la.

La qualitat no consisteix només a evitar errors numèrics. També exigeix que les dades siguin adequades per a l'ús previst, que les definicions siguin clares i que el procés pugui reconstruir-se. Els principis fonamentals de l'estadística oficial de les Nacions Unides vinculen la confiança pública amb la imparcialitat, els mètodes científics i la transparència sobre fonts i procediments {% cite unitedNationsFundamentalPrinciples2014 %}. El Codi de bones pràctiques de les estadístiques europees concreta aquests compromisos en dimensions com la rellevància, l'exactitud, l'oportunitat, la coherència, la comparabilitat, l'accessibilitat i la claredat {% cite europeanStatisticalSystemCodePractice2018 %}.

>>>> **Un nombre sense context encara no és una evidència.** Jones recorda que un valor necessita etiqueta, unitat i relació amb allò que mesura per convertir-se en informació útil {% cite jonesHowLieCharts2018 %}. En el projecte, una cel·la amb `42` no diu si parla d'habitants, establiments, places, percentatge, any, municipi o casos absents. Abans de calcular o representar, cal poder respondre: què compta, on, quan, amb quina unitat, segons quina font i amb quines exclusions.

## Tipus de fonts

Un cop formulada la pregunta, el pas següent no és encara descarregar. Cal entendre quin tipus de font pot sostenir la resposta i quins riscos porta associats. Les fonts es poden ordenar de diverses maneres: segons la seva relació amb la pregunta, segons el procés que les produeix, segons el nivell d'elaboració, segons l'estructura de les dades o segons les condicions d'accés. Aquesta classificació no serveix per memoritzar etiquetes, sinó per anticipar quines comprovacions seran necessàries abans d'utilitzar les dades.

>>>>> En aquesta secció es classifiquen les fonts per anticipar-ne els riscos principals abans d'utilitzar-les.
>>>>>
>>>>> - Distingir fonts primàries, secundàries i terciàries segons la pregunta.
>>>>> - Reconèixer si una dada prové d'una estadística, un registre, un sensor, una enquesta o una plataforma comercial.
>>>>> - Separar dades estadístiques, administratives, geoespacials, de recerca, col·laboratives i comercials.
>>>>> - Identificar si es treballa amb microdades, agregats, indicadors, textos, mapes o imatges.
>>>>> - Entendre que la categoria de la font orienta les comprovacions posteriors.

### Fonts primàries, secundàries i terciàries

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
| Resposta d'un model de llenguatge gran | Definició o valor estadístic | Font terciària de descoberta: cal verificar-la externament |
:::

### Fonts segons el procés de producció

Una altra classificació útil diferencia les fonts per la manera com es genera la informació:

- **Estadístiques:** censos, enquestes, estimacions i estadística derivada, amb metodologia, univers, mostra i procediments de qualitat documentats.
- **Administratives:** registres creats per gestionar permisos, impostos, establiments o serveis. Poden tenir molt detall, però representen l'activitat administrativa, no necessàriament el fenomen complet.
- **Geoespacials de referència:** límits, xarxes, toponímia, ortofotos, models d'elevació i bases topogràfiques mantingudes per organismes cartogràfics.
- **Observació de la Terra i sensors:** imatges de satèl·lit, escaneig làser, estacions meteorològiques, comptadors o dispositius. La resolució, el calibratge i el nivell de processament són part essencial de la dada.
- **Recerca:** dades produïdes en projectes científics. Cal examinar el disseny de la recerca, el repositori, la documentació i la llicència.
- **Col·laboratives o generades pels usuaris:** OpenStreetMap, ressenyes, fotografies o publicacions socials. La cobertura i els criteris poden ser desiguals, però poden ser valuoses si la pregunta i el mètode ho justifiquen.
- **Comercials:** telefonia, transaccions, reserves o mobilitat. Poden oferir detall i actualitat, però solen tenir restriccions, biaixos de cobertura i metodologies no auditables completament.

### Altres distincions pràctiques

Les classificacions anteriors no esgoten les decisions que cal prendre. Una mateixa font pot ser estadística oficial, secundària respecte de la pregunta, agregada per municipis, publicada com a sèrie anual i accessible amb una llicència oberta. Per això convé afegir altres preguntes abans de triar-la:

::: table "Altres maneres de distingir les fonts"
| Dimensió | Distinció habitual | Per què importa |
| --- | --- | --- |
| Nivell d'elaboració | Microdades, registres, agregats, indicadors, índexs o productes derivats | Determina què es pot recalcular, quina privacitat cal protegir i quina part del procés ja ha fet el productor |
| Estructura | Taula, geometria, imatge, text, document o resposta estructurada | Condiciona l'eina de treball, les metadades necessàries i els errors possibles d'importació |
| Cobertura | Cens complet, mostra, registre parcial, sensor, participació voluntària o plataforma comercial | Afecta la representativitat i els biaixos que es poden esperar |
| Temporalitat | Fotografia d'un moment, sèrie temporal, actualització periòdica o flux continu | Obliga a conservar període de referència, data d'accés i possibles revisions |
| Accés i reutilització | Obert, amb registre, sota conveni, comercial, restringit o només visualitzable | Indica si es pot descarregar, compartir, automatitzar o incorporar al treball final |
| Paper en el projecte | Font de càlcul, font de context, font de comprovació o font de descoberta | Evita donar el mateix pes a una dada analítica que a una pista inicial |
:::

La categoria no determina automàticament la qualitat. Un registre administratiu oficial pot contenir duplicats; una font col·laborativa pot estar molt actualitzada; una enquesta rigorosa pot no ser representativa a escala municipal. La classificació tampoc substitueix la lectura metodològica: serveix per saber quines preguntes caldrà fer després. Abans d'avaluar una font concreta, però, cal saber en quins àmbits institucionals i territorials és més probable trobar-la.

## Algunes fonts rellevants

Aquesta secció presenta algunes fonts rellevants per al curs, sense pretendre convertir-se en un catàleg complet ni en una guia definitiva d'ús. Amb la pregunta i una primera tipologia de fonts ja plantejades, la cerca pot orientar-se. No es tracta de recórrer portals a l'atzar, sinó de començar per l'escala on és més probable trobar la unitat territorial i la definició adequades. L'escala geogràfica condiciona qui produeix les dades, quin detall es pot obtenir i fins a quin punt són comparables. Les fonts globals harmonitzen conceptes per comparar països, però sovint perden detall territorial. Les fonts estatals, catalanes i locals acostumen a oferir més desagregació, però poden emprar classificacions pròpies i cobrir només el seu àmbit administratiu.

Les mencions a formats, metadades, llicències o serveis que apareixen en els exemples no s'han d'entendre encara com una explicació completa d'aquests conceptes. Serveixen per mostrar què caldrà mirar quan s'obri una fitxa real. La lectura detallada d'una font exigeix explorar el portal, obrir la pàgina metodològica, revisar la fitxa del conjunt, identificar les opcions de descàrrega o consulta i conservar la informació que permetrà reconstruir el camí seguit. Les seccions posteriors d'aquest capítol expliquen com verificar una font, què implica reutilitzar-la i com accedir-hi de manera reproduïble; els capítols següents desenvoluparan la part territorial, cartogràfica i visual.

No sempre s'ha de començar per l'escala més gran. Si la pregunta tracta els municipis catalans, Idescat o la Generalitat poden ser punts de partida més directes que Eurostat. Si es vol comparar Catalunya amb regions europees, caldrà buscar una classificació territorial harmonitzada i comprovar si la variable existeix al mateix nivell. Si la pregunta baixa a barris, equipaments o planejament, les fonts municipals poden aportar el detall que no apareix en cap portal supramunicipal.

>>>>> Aquesta secció situa algunes fonts rellevants segons l'escala i el tipus de dada que solen oferir, i prepara la lectura detallada que vindrà després.
>>>>>
>>>>> - Comparar fonts globals, europees, estatals, catalanes i locals.
>>>>> - Triar el primer punt de cerca segons la unitat territorial i la variable necessària.
>>>>> - Detectar quan una font és massa general o massa local per a l'ús previst.
>>>>> - Separar taules estadístiques, registres administratius i geodades.
>>>>> - Llegir una captura de portal com una invitació a explorar metadades, recursos i condicions, no com a resultat final.

### Mapa inicial de fonts per escala

La taula següent no és un inventari exhaustiu. Funciona com un mapa de consulta per decidir per on començar segons l'abast territorial de la pregunta i per recordar que, a cada escala, les taules i les capes cartogràfiques s'han de verificar per separat. L'ordre pràctic no és «provar portals» fins que aparegui una xifra, sinó triar el primer punt de cerca que tingui més probabilitat d'oferir la unitat territorial, la variable i la documentació necessàries.

::: table "Orientació inicial per escala"
| Escala | Estadística i informació | Geodades i cartografia | Ús característic |
| --- | --- | --- | --- |
| Global | FAOSTAT, World Bank Data, UNData, UN Tourism, Wikidata | Natural Earth, GADM, CIA Maps, OpenStreetMap | Comparar països o observar processos globals |
| Europa | Eurostat | GISCO, Copernicus | Comparar estats i regions europees amb criteris harmonitzats |
| Espanya | INE, Dataestur, datos.gob.es, AEMET | IGN/CNIG, Cadastre | Treballar comunitats, províncies, municipis, zones turístiques i bases estatals |
| Catalunya | Idescat, Registre de Turisme, Dades Obertes de la Generalitat, coneixement turístic | ICGC i geoserveis de la Generalitat | Analitzar comarques, municipis, establiments i territori detallat |
| Local i supramunicipal | Mercuri, Reus Open Data, TGN Dades, dades obertes municipals | Geoportals municipals, cartografia local i infraestructures de dades espacials locals | Estudiar barris, equipaments, planejament, serveis i detall urbà |
:::

::: table "Triar el primer punt de cerca"
| Si la pregunta demana... | Punt de partida més eficient | Control abans de descarregar |
| --- | --- | --- |
| Comparar països o grans regions | Organismes internacionals o Eurostat | Definició comuna, unitat i cobertura temporal |
| Treballar municipis, comarques o províncies | Idescat, INE, Generalitat, Dataestur o CNIG segons la variable | Codi territorial, any de classificació i nivell disponible |
| Baixar a barris, equipaments o planejament | Portals municipals, observatoris locals o geoportals | Divisió interna, data, llicència i possibilitat de descarregar dades |
| Representar una taula en un mapa | Font estadística més geometria compatible | Codi d'unió, sistema de referència i escala de la geometria |
:::

Els apartats següents apliquen aquest ordre: àmbit global, europeu, estatal, català i local. Dins de cada àmbit, es presenten primer els recursos estadístics, informatius o administratius, i al final les fonts geoespacials. Aquesta separació ajuda a recordar que una taula estadística i una capa cartogràfica poden provenir del mateix organisme, però responen a operacions diferents i tenen metadades, llicències i escales pròpies.

### Fonts d'àmbit global

Les fonts globals existeixen perquè hi ha problemes que no es poden analitzar només amb estadístiques d'un país. Comparar fam, producció agrària, desenvolupament, migracions o turisme requereix definicions comunes i organismes capaços de coordinar dades produïdes per molts estats. Per això aquest apartat comença pels portals estadístics i de descoberta, i deixa per al final les bases cartogràfiques globals. Aquesta harmonització facilita la comparació, però també obliga a examinar qui va observar originàriament cada valor, quines estimacions s'hi han aplicat i quin detall territorial s'ha perdut.

#### FAO i FAOSTAT

L'[Organització de les Nacions Unides per a l'Alimentació i l'Agricultura](https://www.fao.org/about/en/) (FAO) és una agència especialitzada de les Nacions Unides que lidera esforços internacionals contra la fam i treballa per millorar la seguretat alimentària. Per orientar polítiques, inversions i seguiment dels sistemes agroalimentaris necessita dades comparables sobre producció, comerç, preus, nutrició, recursos naturals i sostenibilitat. Per això recull informació dels estats membres, desenvolupa mètodes i classificacions i dona suport als països perquè millorin els seus sistemes estadístics.

El principal portal estadístic general de l'organització és [FAOSTAT](https://www.fao.org/faostat/en/#data). Ofereix accés gratuït a sèries de més de 245 països i territoris, en molts casos des de 1961, sobre agricultura, ramaderia, silvicultura, usos del sòl, comerç, seguretat alimentària i emissions. Altres sistemes de la FAO cobreixen àmbits més específics, com AQUASTAT per als recursos hídrics o FishStat per a pesca i aqüicultura.

FAOSTAT permet filtrar països, productes, elements i anys i ofereix descàrregues massives. Moltes sèries incorporen **flags** o notes que indiquen si el valor és oficial, estimat, imputat o sotmès a alguna qualificació metodològica. La comparabilitat internacional és un avantatge, però una dada publicada per la FAO pot continuar procedint d'un organisme estatal i tenir una qualitat o actualització diferent de la d'un altre país.

#### Banc Mundial i World Bank Data

El [Grup del Banc Mundial](https://www.worldbank.org/en/about/what-we-do) finança projectes de desenvolupament i ofereix assistència tècnica, recerca i assessorament als països. Necessita indicadors per diagnosticar necessitats, orientar finançament i avaluar resultats. La seva funció explica l'amplitud temàtica de [World Bank Data](https://data.worldbank.org/): població, pobresa, economia, educació, infraestructures, medi ambient i turisme, entre molts altres àmbits.

El portal facilita comparacions mundials, descàrregues i un servei de consulta automàtica sense clau. Cada indicador inclou definició, unitat, font original i notes metodològiques. El Banc Mundial, però, no produeix necessàriament totes les sèries que difon. Alguns indicadors provenen d'instituts nacionals o d'altres organismes internacionals; cal revisar el camp *source* i no interpretar els valors absents com a zero.

#### Sistema de les Nacions Unides i turisme internacional

La Divisió d'Estadística de les Nacions Unides coordina estàndards i compila informació perquè fenòmens globals es puguin comparar. [UNData](https://data.un.org/) agrega bases de població, comptes nacionals, comerç, energia, medi ambient i altres àmbits. És un bon punt de descoberta, però la traça s'ha de seguir fins a l'agència productora. Per als Objectius de Desenvolupament Sostenible també es disposa d'un [servei oficial de consulta dels indicadors ODS](https://unstats.un.org/SDGAPI/swagger/).

Dins del mateix sistema, [UN Tourism](https://www.unwto.org/tourism-statistics/tourism-statistics-database) té el mandat especialitzat d'impulsar un turisme responsable, sostenible i accessible. Per observar-ne l'evolució promou recomanacions estadístiques comunes i reuneix arribades, pernoctacions, despesa, allotjament i indicadors macroeconòmics. L'accés i la reutilització no són iguals per a tots els productes; abans de redistribuir una descàrrega cal revisar-ne les condicions específiques.

#### Wikipedia, Wikidata i recursos de descoberta

[Wikipedia](https://www.wikipedia.org/) és una enciclopèdia construïda i revisada col·laborativament. Pot ajudar a descobrir conceptes, topònims i referències, però és una font secundària narrativa: una afirmació s'ha de comprovar mitjançant les cites, l'historial i, quan sigui possible, la font original.

[Wikidata](https://www.wikidata.org/) aplica el mateix principi col·laboratiu a una base de coneixement estructurada i multilingüe. Cada element té un identificador, com `Q` seguit d'un número, i pot contenir propietats, valors, coordenades, referències i enllaços a altres bases. Les dades es publiquen sota `CC0` i es poden consultar amb llenguatges i serveis de consulta estructurada. El seu caràcter obert i estructurat en facilita la reutilització, però les declaracions continuen depenent de les fonts aportades, de les regles comunitàries i de la cobertura desigual.

#### Fonts geoespacials globals

[Natural Earth](https://www.naturalearthdata.com/) ofereix cartografia mundial generalitzada a escales 1:10.000.000, 1:50.000.000 i 1:110.000.000. Inclou països, subdivisions principals, ciutats, costes, rius, xarxes i ràsters de fons. Les dades són de domini públic i són molt útils per a mapes mundials de petita escala. No és una base adequada per delimitar parcel·les, municipis o fronteres jurídiques amb precisió. L'escala seleccionada ha de correspondre a la mida i la finalitat del mapa: més detall no sempre produeix un mapa millor.

[GADM](https://gadm.org/) distribueix divisions administratives de molts nivells per a països de tot el món. Pot resultar pràctic quan no hi ha una única font global comparable, però **no és una font oficial de fronteres i no és dades obertes**. La [llicència de GADM](https://gadm.org/license.html) permet usos acadèmics i altres usos no comercials, però prohibeix en general la redistribució i l'ús comercial sense autorització. Per tant, els fitxers GADM no s'incorporaran al repositori públic del manual. Si s'utilitzen en una activitat, cada participant els haurà d'obtenir del lloc oficial, registrar-ne la versió i respectar-ne la llicència.

La Central Intelligence Agency dels Estats Units necessita informació bàsica geogràfica, política, demogràfica i econòmica per a les seves funcions d'intel·ligència. El *World Factbook* va néixer com una publicació interna, després es va fer públic i durant dècades va oferir perfils sintètics de països i territoris. Si el portal o la mateixa institució indiquen que un recurs ha deixat de mantenir-se, no s'ha de recomanar com a base vigent encara que continuï sent consultable. El recurs actiu [CIA Maps](https://www.cia.gov/resources/cia-maps/) permet explorar mapes de països i territoris; pot servir per observar topònims, fronteres i criteris de representació, però no substitueix una base vectorial com Natural Earth ni una font oficial del territori estudiat.

[OpenStreetMap](https://www.openstreetmap.org/about) (OSM) és una base de dades geogràfica construïda per una comunitat que combina coneixement local, treball de camp, traces del sistema de posicionament global (GPS) i imatges autoritzades. Es distribueix sota l'Open Database License i permet obtenir objectes, consultar-ne l'historial i produir mapes derivats. [Google Maps](https://www.google.com/maps) és principalment un servei cartogràfic comercial orientat a la cerca de llocs, navegació, negocis, fotografies i ressenyes. Poder consultar-ne el mapa no autoritza a extreure'n massivament les dades ni a reutilitzar-ne les imatges com si fossin dades obertes.

La diferència entre models de producció es fa visible en comparacions locals. La taula descriu allò que era observable als mapes estàndard l'11 d'agost de 2026; no demostra quines dades pot conservar internament cada plataforma.

::: table "Dos llocs on OpenStreetMap ofereix més detall territorial observable"
| Lloc i vistes comparables | Detall especialment ric a OSM | Fortalesa visible de Google Maps | Explicació plausible |
| --- | --- | --- | --- |
| [Campus de Vila-seca a OSM](https://www.openstreetmap.org/#map=18/41.10266/1.14784) i [a Google Maps](https://www.google.com/maps/@41.10266,1.14784,18z?hl=ca) | Carrils bici amb segregació i sentit; pistes i piscines com a geometries; aparcaments de bicicletes; accessibilitat; desfibril·lador; font; mobiliari de parada i arbrat | Equipaments, fitxes de llocs, fotografies i alguns aparcaments | Contribució local i temàtica, incloses edicions d'accessibilitat, davant d'una representació comercial orientada a cerca i navegació |
| [Camí de Ronda de Cap Salou a OSM](https://www.openstreetmap.org/#map=17/41.05650/1.16480) i [a Google Maps](https://www.google.com/maps/@41.05650,1.16480,17z?hl=ca) | Continuïtat del sender; distinció entre camí i escales; pendents i restriccions; accessos a cales; roca, matollar, platges i microtoponímia | Hotels, comerços, miradors, fotografies i llocs d'interès | Edició excursionista centrada en topologia, transitabilitat i medi físic davant d'una selecció centrada en destinacions i serveis |
:::

Més detall no significa necessàriament més exactitud. Els atributs d'OSM poden estar desactualitzats o no haver estat verificats sobre el terreny, i Google pot mostrar informació addicional en una fitxa o una ruta que no apareix al mapa base. La comparació serveix per entendre que cada sistema prioritza objectes diferents i que cap mapa no s'ha d'acceptar sense comprovar-lo.

>> **Les fonts també desapareixen o canvien de funció.** Quan una base deixa de mantenir-se, una URL no garanteix que continuï sent una font vigent. En un treball reproduïble cal registrar la data d'accés i conservar, quan la llicència ho permeti, la versió exacta utilitzada.

### Fonts d'àmbit europeu

En l'àmbit europeu, Eurostat és la font estadística comparativa principal. Després de localitzar la taula o l'indicador, cal revisar el component geogràfic d'Eurostat, GISCO, i Copernicus, perquè aporten les geometries harmonitzades i l'observació de la Terra que sovint permeten representar o contextualitzar aquestes estadístiques.

#### Eurostat

[Eurostat](https://ec.europa.eu/eurostat/data/database) és l'oficina estadística de la Unió Europea. El seu valor principal és l'harmonització: les dades dels estats s'organitzen amb definicions i classificacions comunes per facilitar la comparació. Inclou població, economia, treball, transport, medi ambient i un bloc ampli de turisme amb capacitat d'allotjament, arribades, pernoctacions, ocupació i viatges dels residents.

El **Data Browser** permet seleccionar dimensions i descarregar resultats. Eurostat també ofereix descàrrega massiva i serveis de consulta en formats tabulars i estructurats. Les taules tenen codis estables, com `demo_pjan` per a població, i moltes disposen d'un identificador digital persistent. Els flags identifiquen valors estimats, provisionals, confidencials o afectats per ruptures.

Les taules d'Eurostat es revisen i una mateixa consulta pot retornar la versió vigent en el moment d'accés. Per reproduir una activitat cal conservar el fitxer o la resposta exacta utilitzada, la data i el codi del conjunt.

La classificació **NUTS** (*Nomenclature of territorial units for statistics*, nomenclatura d'unitats territorials estadístiques) és una peça central d'aquesta comparabilitat territorial. Els estats europeus no organitzen el territori de la mateixa manera: Alemanya té *Länder*, Espanya té comunitats autònomes i províncies, França té regions i departaments, i altres països utilitzen divisions pròpies amb funcions, mides i competències diferents. Comparar directament una província espanyola amb un *Land* alemany o una regió francesa pot ser enganyós si no se sap quin paper té cada unitat dins del sistema administratiu del país.

NUTS no elimina aquestes diferències polítiques i administratives, però crea una malla estadística comuna perquè les dades regionals europees es puguin recollir, analitzar i representar amb criteris harmonitzats. Eurostat divideix cada país de la Unió Europea en tres nivells principals: NUTS 1 per a grans regions socioeconòmiques, NUTS 2 per a regions bàsiques de política regional i NUTS 3 per a regions petites orientades a diagnòstics més detallats {% cite eurostatNutsOverview2026 %}. A Espanya, per exemple, les comunitats autònomes solen correspondre al nivell NUTS 2 i les províncies al nivell NUTS 3; en altres països, la correspondència amb les divisions administratives és diferent. Per això, quan es comparen regions europees, cal citar el nivell i la versió NUTS utilitzats, no només el nom administratiu visible al mapa.

Això no vol dir que qualsevol variable existeixi a qualsevol nivell: un indicador pot estar disponible per estat i regió, però no per municipi, o pot canviar de definició quan baixa d'escala. També cal recordar que NUTS canvia amb el temps. Si una sèrie combina geometries o codis de versions diferents, la comparació pot introduir ruptures territorials encara que el nom de la regió sembli estable.

#### Fonts geoespacials europees: GISCO i Copernicus

[GISCO](https://ec.europa.eu/eurostat/web/gisco/geodata) és el component geogràfic d'Eurostat. Distribueix geometries de països, regions NUTS, unitats locals, ciutats i altres capes en diferents escales i sistemes de referència. Permet unir les estadístiques d'Eurostat amb geometries compatibles. Cal revisar la llicència de cada família de capes: algunes fronteres administratives incorporen drets d'EuroGeographics i restriccions específiques.

[Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) dona accés a imatges Sentinel i altres productes d'observació de la Terra. El navegador permet cercar per lloc, dates, missió, cobertura de núvols i tipus de producte. També hi ha catàlegs, serveis de consulta, processament en línia i descàrrega. La data de captació, el nivell de processament, la resolució, els núvols i la llicència de cada col·lecció formen part de la selecció; «publicat al Data Space» no implica que tot el contingut tingui exactament les mateixes condicions.

Les captures globals i europees no s'han de memoritzar com a interfícies estables. Serveixen per aprendre on apareixen el cercador, el codi del conjunt, les dimensions, les metadades, les descàrregues i les famílies de geodades.

::: subfigures a+b/c "Useu aquests portals per localitzar indicadors comparables i geodades harmonitzades; abans de descarregar, identifiqueu el codi del recurs, les metadades, la unitat, la data i la llicència. Captures pròpies dels portals indicats."
![Portal World Bank Open Data amb cercador, àrees temàtiques i indicadors globals]({{ site.baseurl }}/assets/img/data-sources/world-bank-data-2026-08-13.png "Localitzeu indicadors globals a partir del cercador, les àrees temàtiques i les fitxes d'indicador; després comproveu definició, unitat i font original. Captura pròpia del portal World Bank Open Data, 13 d'agost de 2026.")
![Data Browser d'Eurostat amb codi del conjunt, metadades, dimensions, filtres i descàrrega]({{ site.baseurl }}/assets/img/data-sources/eurostat-data-browser.png "Llegiu el codi del conjunt, les dimensions, els filtres, les metadades i les opcions de descàrrega abans de copiar cap valor d'Eurostat. Captura pròpia del Data Browser d'Eurostat, 11 d'agost de 2026.")
![Pàgina GISCO Geodata d'Eurostat amb famílies de geodades i avís de metadades]({{ site.baseurl }}/assets/img/data-sources/gisco-geodata-2026-08-13.png "Trieu les geometries per escala, família de dades i condicions d'ús, no només pel nom de la capa. Captura pròpia de GISCO Geodata d'Eurostat, 13 d'agost de 2026.")
:::

### Fonts d'àmbit estatal: Espanya

En l'àmbit estatal, l'INE concentra bona part de l'estadística oficial; Dataestur i `datos.gob.es` ajuden a descobrir dades procedents de productors diversos; i l'IGN, el CNIG i el Cadastre aporten informació geogràfica de referència. L'ordre de lectura manté aquesta separació: primer estadística, indicadors i catàlegs; després cartografia, geoserveis i parcel·lari.

#### INE i INEbase

L'[Instituto Nacional de Estadística](https://www.ine.es/) produeix censos, enquestes i estadístiques sobre població, habitatge, economia, treball, mobilitat i turisme. INEbase permet navegar per operacions i taules, seleccionar dimensions i descarregar resultats. En turisme s'hi troben estadístiques d'ocupació hotelera i extrahotelera, FRONTUR, EGATUR i turisme de residents, entre d'altres.

La desagregació varia segons l'operació: una taula pot arribar a municipis, províncies, comunitats autònomes, punts o zones turístiques. Les enquestes no són necessàriament representatives a totes les escales. Cal diferenciar també padró, cens i estimacions de població, així com dada provisional i definitiva.

L'INE també ofereix un [servei de consulta en format estructurat](https://www.ine.es/dyngs/DAB/index.htm?cid=1099). La desagregació depèn de cada operació i els codis territorials s'han de conservar com a text. Cens, padró, estimació de població, punt turístic i municipi no són categories intercanviables.

#### Datos.gob.es, Dataestur i altres organismes estatals

[datos.gob.es](https://datos.gob.es/es/catalogo/conjuntos-datos) és el catàleg estatal de dades obertes. Ajuda a localitzar conjunts d'administracions estatals, autonòmiques i locals, però normalment no n'és el productor. Una fitxa del catàleg pot estar actualitzada mentre que una distribució enllaçada ja no funciona; cal identificar i citar l'organisme publicador original.

[Dataestur](https://www.dataestur.es/) integra indicadors turístics procedents de l'INE, AENA, la Seguretat Social, AEMET i altres fonts. Resulta útil per explorar el sector, però els indicadors no comparteixen necessàriament metodologia, unitat ni escala. Per a una anàlisi reproduïble convé recuperar la dada del productor original quan sigui possible.

Altres fonts estatals complementàries són [AEMET OpenData](https://opendata.aemet.es/) per a observacions i prediccions meteorològiques. Una estació meteorològica no representa automàticament tot un municipi; cal conservar l'estació, la variable, el període i les condicions de mesura.

#### Fonts geoespacials estatals: IGN, CNIG i Cadastre

L'Instituto Geográfico Nacional produeix informació geogràfica de referència i el Centro Nacional de Información Geográfica la distribueix mitjançant el [Centro de Descargas del CNIG](https://centrodedescargas.cnig.es/CentroDescargas/catalogo). S'hi troben mapes topogràfics, bases cartogràfiques, límits administratius, CartoCiudad, ortofotos del Pla Nacional d'Ortofotografia Aèria, models digitals del terreny, núvols de punts d'escaneig làser, ocupació del sòl i noms geogràfics.

Els productes tenen escales, resolucions, dates, formats i sistemes de referència diferents. Una ortofoto de «màxima actualitat» pot ser un mosaic d'imatges captades en anys diferents. A més de descàrregues, l'[IGN publica serveis web](https://www.ign.es/web/ign/portal/ide-area-nodo-ide-ign) per veure mapes, consultar dades vectorials o treballar amb cobertures ràster.

Els [serveis cadastrals publicats dins la infraestructura europea d'informació espacial](https://www.catastro.hacienda.gob.es/webinspire/index.html) permeten accedir a parcel·les, edificis i adreces. La cartografia cadastral és molt útil per localitzar immobles i estudiar estructura parcel·lària, però una parcel·la cadastral no equival necessàriament a una finca registral ni al planejament urbanístic.

En l'àmbit estatal, les interfícies també separen estadística i cartografia. INEbase ajuda a entrar per operació estadística; el Centro de Descargas del CNIG ajuda a entrar per producte geogràfic, escala, format i cobertura.

::: subfigures a+b "A escala estatal, separeu la cerca estadística de la cerca cartogràfica: una operació estadística i un producte geogràfic tenen filtres, metadades i criteris de descàrrega diferents. Captures pròpies dels portals indicats."
![INEbase amb categories d'operacions estadístiques i llistat d'operacions]({{ site.baseurl }}/assets/img/data-sources/inebase-2026-08-13.png "Entreu a INEbase per operació estadística i reviseu categoria, taula, període i nivell territorial abans de descarregar. Captura pròpia del portal de l'INE, 13 d'agost de 2026.")
![Centro de Descargas del CNIG amb catàleg de productes geogràfics]({{ site.baseurl }}/assets/img/data-sources/cnig-downloads-2026-08-13.png "Entreu al Centro de Descargas del CNIG per producte geogràfic, escala, format i cobertura, no per una captura del mapa final. Captura pròpia, 13 d'agost de 2026.")
:::

### Fonts d'àmbit català

En l'àmbit català, Idescat concentra l'estadística oficial; els departaments publiquen registres i dades sectorials mitjançant Dades Obertes; i l'ICGC produeix la informació cartogràfica i geològica de referència. Primer convé identificar la dada estadística, administrativa o sectorial, i després comprovar quina geometria o cartografia permet representar-la amb l'escala adequada.

#### Idescat

L'[Institut d'Estadística de Catalunya](https://www.idescat.cat/) publica informació demogràfica, econòmica, social, territorial i turística. Segons l'operació, les dades poden estar disponibles per Catalunya, àmbits territorials, comarques, municipis, districtes o seccions censals. La secció de [dades obertes](https://www.idescat.cat/dades/obertes/) facilita descàrregues, i el [servei de consulta de l'Idescat](https://www.idescat.cat/dev/api/) retorna part de les taules en un format estructurat.

Idescat també manté [codis i classificacions territorials](https://www.idescat.cat/codis/) i informa de rectificacions. Alguns resultats són producció pròpia i d'altres són explotacions de dades de l'INE o dels departaments de la Generalitat; l'autoria metodològica completa s'ha de conservar. Els canvis de comarca, municipi o secció censal poden trencar una sèrie.

#### Dades Obertes de la Generalitat i informació turística

El [catàleg de Dades Obertes de la Generalitat](https://analisi.transparenciacatalunya.cat/) reuneix conjunts de molts departaments i organismes. La plataforma permet filtrar, visualitzar, exportar formats de taula o de dades estructurades i, en molts casos, fer consultes estructurades al portal. Com passa amb `datos.gob.es`, el catàleg no substitueix el productor que consta a cada fitxa.

Un conjunt especialment útil és el [Registre de Turisme de Catalunya](https://analisi.transparenciacatalunya.cat/Turisme/Establiments-d-allotjament-tur-stic-inscrits-al-Re/t2h3-cgys/about_data), que conté establiments inscrits, tipus, estat, municipi, comarca, places i altres camps. És una font administrativa: una alta no demostra que l'establiment estigui obert, que les places estiguin disponibles ni que hi hagi hagut ocupació. Aquesta diferència permet treballar la distància entre **oferta registrada** i **activitat observada**.

El portal de [coneixement turístic de la Generalitat](https://empresa.gencat.cat/ca/treb_ambits_actuacio/turisme/coneixement_planificacio/) agrupa estadístiques, estudis i eines sectorials. Les marques turístiques que hi apareixen no són necessàriament divisions administratives i la seva composició s'ha de documentar abans de fer unions territorials.

#### Fonts geoespacials catalanes: ICGC i geoserveis

L'[Institut Cartogràfic i Geològic de Catalunya](https://www.icgc.cat/ca/Geoinformacio-i-mapes) produeix cartografia topogràfica, ortofotos, models d'elevació, núvols de punts d'escaneig làser, límits administratius, geologia, cobertes del sòl i toponímia. El [visor de descàrregues](https://visors.icgc.cat/appdownloads/) permet obtenir productes per full o àrea, i la secció de [geoserveis](https://www.icgc.cat/ca/Geoinformacio-i-mapes/Geoinformacio-en-linia-Geoserveis) documenta serveis per visualitzar mapes, obtenir tessel·les, consultar objectes geogràfics i connectar eines externes.

Molts productes catalans utilitzen ETRS89 / UTM fus 31N, un sistema de referència habitual per situar coordenades a Catalunya, però sempre cal comprovar la fitxa. L'escala, la resolució, l'edició i el sistema de referència no s'han de deduir només del nom del fitxer.

### Fonts d'àmbit local i supramunicipal

Les fonts locals són importants quan la unitat de treball deixa de ser el municipi i passa a ser el barri, el carrer, l'equipament, la parcel·la, el servei o una actuació municipal. També són útils quan es necessita una lectura aplicada del territori: mobilitat quotidiana, planejament, manteniment urbà, serveis públics, activitat econòmica o indicadors de ciutat. En aquest àmbit es revisen primer els sistemes d'informació, observatoris i portals de dades, i es tanca amb els geoportals municipals. El límit principal és la comparabilitat: dues ciutats poden publicar variables semblants amb criteris, dates o divisions internes diferents.

En un treball de primer curs, aquestes fonts no s'han d'usar només per «trobar una xifra». El seu valor és aprendre a llegir quina administració observa el fenomen, amb quin nivell de detall i amb quin objectiu de gestió. Un observatori municipal pot ser excel·lent per orientar una diagnosi de ciutat, però si l'indicador prové d'Idescat, INE o d'un registre sectorial cal conservar també aquesta procedència original.

::: table "Lectura pràctica dels recursos locals"
| Recurs | Primera utilitat docent | Què cal conservar |
| --- | --- | --- |
| Mercuri | Comparar municipis de la demarcació i descobrir indicadors locals | Font original de cada indicador, data, definició i escala territorial |
| Reus Open Data | Obtenir taules municipals reutilitzables, sovint per barri o servei | Identificador del conjunt, recurs descarregat, camps, llicència i tractaments d'anonimització |
| Observatori de Reus | Entendre indicadors de ciutat i localitzar fonts relacionades | Enllaç cap al conjunt o productor que sosté cada dada utilitzada |
| TGN Dades | Llegir quadres de comandament i mapes públics de Tarragona | Diferència entre visualització, indicador i conjunt descarregable |
| Geoportals municipals | Localitzar cartografia de detall, serveis i capes urbanes | Escala, data, sistema de referència, servei o fitxer i condicions d'ús |
:::

Les captures catalanes i locals mostren el canvi d'escala i de funció institucional: estadística oficial, registre administratiu, descàrrega cartogràfica i síntesi supramunicipal. En tots els casos cal seguir fins al productor, la data, la definició i la llicència.

::: subfigures a+b/c+d "Per baixar d'escala, combineu estadística oficial, registres administratius, cartografia de referència i sistemes supramunicipals de síntesi; en tots els casos, seguiu la traça fins al productor, la data, la definició i la llicència. Captures pròpies dels portals indicats."
![Portal de l'Idescat amb accés a dades, mètodes, territori i actualitzacions de l'estadística oficial de Catalunya]({{ site.baseurl }}/assets/img/data-sources/idescat.png "Useu l'Idescat per trobar dades, mètodes, territoris i actualitzacions de l'estadística oficial catalana abans de construir una taula. Captura pròpia, 11 d'agost de 2026.")
![Fitxa del Registre de Turisme de Catalunya al portal de Dades Obertes]({{ site.baseurl }}/assets/img/data-sources/generalitat-open-data-tourism-register-2026-08-13.png "Llegiu la fitxa del Registre de Turisme com a registre administratiu: productor, actualització, camps i exportacions expliquen què es pot usar i què no. Captura pròpia del portal de Dades Obertes de la Generalitat, 13 d'agost de 2026.")
![Visor de descàrregues de l'ICGC amb selecció de l'àrea, família de producte i format de sortida]({{ site.baseurl }}/assets/img/data-sources/icgc-downloads.png "Trieu producte, àrea i format al visor de l'ICGC abans d'incorporar una base cartogràfica al projecte. Captura pròpia, 11 d'agost de 2026.")
![Sistema Mercuri de la Diputació de Tarragona amb menú d'indicadors, dades municipals, mapes i informes]({{ site.baseurl }}/assets/img/data-sources/mercuri-dipta-2026-08-13.png "Useu Mercuri per explorar indicadors municipals i detectar preguntes, però conserveu la font primària quan el sistema indiqui un productor anterior. Captura pròpia del sistema Mercuri de la Diputació de Tarragona, 13 d'agost de 2026.")
:::

#### Mercuri i informació supramunicipal de la demarcació

El sistema [Mercuri](https://www.dipta.cat/mercuri/menu_pre.asp) de la Diputació de Tarragona concentra informació socioeconòmica local de la demarcació. Reuneix dades municipals, dades de la demarcació, indicadors, informes, gràfics i mapes temàtics. El seu valor docent és doble: permet observar molts municipis del Camp de Tarragona, les Terres de l'Ebre i el Baix Penedès amb una mateixa interfície, i mostra com una administració supramunicipal reorganitza fonts de productors diferents per donar suport a polítiques locals.

Mercuri inclou blocs com entorn, demografia, qualitat de vida, activitat econòmica i mercat de treball. La informació pot provenir d'Idescat, INE, departaments de la Generalitat, registres sectorials o elaboracions de la mateixa Diputació. Per això s'ha de llegir com una font d'informació i síntesi: quan un indicador sigui central en una anàlisi reproduïble, cal identificar la font primària, la data i la definició concreta.

En una primera exploració comarcal, Mercuri pot ajudar a formular preguntes: quins municipis concentren població, quins tenen més especialització residencial, on apareixen contrastos de renda, edat o activitat, i quins valors mereixen una comprovació posterior. La dada que es descarregui per al llibre del curs, però, no ha de quedar citada només com «Mercuri» si el propi sistema indica un productor anterior. El bon ús és descobrir-hi el patró, seguir la traça fins a la font i registrar totes dues peces quan siguin rellevants.

#### Reus: dades obertes i observatori

El [portal de dades obertes de Reus](https://opendata.reus.cat/) publica conjunts municipals en formats reutilitzables. Per exemple, les dades de [població](https://opendata.reus.cat/dataset/poblaci-per-barri-edat-i-sexe-i-nacionalitat) permeten treballar el padró per barris, codis postals, edat, sexe i nacionalitat, amb descàrregues en formats de taula i de dades estructurades. La pàgina de recurs documenta camps, tipus i llicència, i també avisa de tractaments d'anonimització quan cal evitar la identificació de persones.

L'[Observatori de Reus](https://observatori.reus.cat/) funciona com a porta d'entrada a informació socioeconòmica i enllaça altres recursos d'interès, com Reus Open Data, Mercuri, Idescat o INE. En un treball del curs pot servir per descobrir dades i indicadors de ciutat, però la cita metodològica ha d'arribar al conjunt o productor concret utilitzat.

Reus és un bon exemple de canvi d'escala. Si el projecte compara municipis, una taula per barris no es pot afegir directament a la taula comarcal sense agregació o sense canviar la unitat d'observació. Si, en canvi, la pregunta és urbana, el barri pot ser la unitat adequada i el municipi passa a ser el context. Aquesta decisió s'ha d'escriure abans d'unir dades: una fila per municipi, una fila per barri i una fila per equipament no poden conviure en la mateixa taula analítica com si fossin observacions equivalents.

#### Tarragona: TGN Dades i dades obertes

L'espai [TGN Dades](https://www.tarragona.cat/governobert/tgn-dades) de l'Ajuntament de Tarragona agrupa indicadors, mapes i panells per conèixer la ciutat. Presenta informació sobre demografia i societat, economia, territori, mobilitat, turisme, habitatge i altres àmbits. La funció principal és facilitar la lectura pública de la ciutat, de manera que cal distingir entre el quadre de comandament o visualització i el conjunt de dades que hi ha al darrere.

El portal municipal de [dades obertes de Tarragona](https://seu-e.cat/ca/web/tarragona/dades-obertes) publica conjunts en categories com demografia, economia, medi ambient, transport, turisme, urbanisme i sector públic. Les fitxes poden oferir taules, descàrregues, consultes automàtiques, gràfics o mapes. Com en qualsevol portal d'aquest tipus, cal conservar l'identificador del conjunt i del recurs, la data de modificació, la llicència, el format i la consulta concreta quan s'utilitzi aquesta via.

Els quadres de comandament municipals són útils per veure ràpidament una situació i per aprendre com una institució comunica indicadors. No substitueixen la taula de treball. Si una visualització mostra un percentatge, s'ha de preguntar quin numerador, quin denominador, quin període i quin territori el produeixen. Si només es conserva la captura o el gràfic, el resultat no es podrà recalcular ni defensar.

#### Fonts geoespacials locals: geoportals i cartografia municipal

El [Geoportal de Reus](https://geoportal.reus.cat/inici/serveis.html) dona accés a serveis i dades geoespacials municipals. Documenta mapes base, ortoimatges, serveis per visualitzar mapes i tessel·les, capes descarregables i una interfície per consultar dades geoespacials. L'Ajuntament de Reus també descriu el manteniment de bases cartogràfiques municipals a escala 1:500 i 1:1000, produïdes i actualitzades per al terme municipal.

Tarragona disposa d'un [Geoportal](https://www.tarragona.cat/governobert/tgn-dades) integrat en l'ecosistema TGN Dades i d'un servei municipal de [Topografia i Geomàtica](https://www.tarragona.cat/lajuntament/territori/topografia-i-geomatica). Aquest departament s'encarrega de la cartografia topogràfica 1:1000, la xarxa topogràfica municipal i informació temàtica georeferenciada com vialer o barris. Algunes bases topogràfiques municipals poden requerir sol·licitud i condicions específiques d'ús; el fet que una informació sigui consultable en un mapa no implica que es pugui redistribuir lliurement.

Les geodades locals poden tenir molt més detall que les fonts catalanes o estatals, però aquest detall té àmbit i data. Una capa de barris de Reus no es pot aplicar a Tarragona; una cartografia municipal pot tenir una escala excel·lent per al nucli urbà però no servir per comparar territoris diferents; i una capa publicada en un geoportal pot ser una visualització, una descàrrega o un servei, amb drets i capacitats diferents.

En aquests recursos locals convé començar amb preguntes molt concretes: quina capa representa barris, carrers, equipaments o planejament; si es pot descarregar o només visualitzar; quin sistema de referència declara; i si la fitxa indica condicions de reutilització. Aquestes preguntes no es resolen només mirant el mapa: cal obrir metadades, recursos, enllaços metodològics i avisos del portal. Les coordenades i els sistemes de referència s'estudiaran amb més detall al capítol 4, però des del primer capítol ja s'ha d'aprendre a no ignorar-los quan apareixen en una fitxa.

El resultat d'aquesta secció no hauria de ser una llista de portals memoritzats, sinó una manera d'entrar-hi. Cada font demana una exploració pròpia: localitzar el productor, entendre la definició de la variable, comprovar l'escala, llegir les metadades, identificar els recursos disponibles i veure sota quines condicions es poden usar. Les seccions següents ordenen aquests passos amb més detall perquè la font deixi de ser només una troballa i pugui convertir-se en evidència dins d'un treball territorial.

## Verificar abans d'utilitzar

Després de classificar una font, cal decidir si pot entrar en la cadena d'evidència. Una dada trobada en un portal, una captura, una consulta automatitzada o un informe encara no és una dada defensable. La verificació transforma una dada trobada en una dada utilitzable: abans de calcular, cal comprovar qui la produeix, què mesura, com s'ha obtingut, quines limitacions declara i si existeixen altres fonts que en confirmen o matisen la lectura.

>>>>> La verificació ha de permetre revisar una font abans d'incorporar-la a una anàlisi.
>>>>>
>>>>> - Distingir autoritat institucional i adequació metodològica.
>>>>> - Localitzar productor, definició, cobertura, qualitat, actualitat i llicència.
>>>>> - Conservar metadades i procedència juntament amb la còpia de dades.

### Autoritat institucional i límits de les fonts

Cal prioritzar fonts que identifiquin un productor responsable, publiquin metodologia i permetin obtenir les dades i les metadades. Els organismes estadístics i cartogràfics oficials ofereixen garanties institucionals importants, però les seves dades també contenen revisions, estimacions, canvis de classificació, errors rectificats i limitacions d'escala. La verificació no consisteix a preguntar només «és oficial?», sinó també «és adequada, comparable i prou documentada per a aquest ús?».

Una xifra trobada en una xarxa social, en un pseudomitjà, en una infografia sense crèdits o en una resposta d'un **model de llenguatge gran** —LLM, de l'anglès *large language model*— no s'ha d'incorporar directament a una anàlisi. Primer cal localitzar-ne l'origen, comprovar si la publicació original existeix, llegir-ne la definició i contrastar-la. Un LLM pot ajudar a proposar paraules de cerca, explicar un format o esbossar una consulta, però no és el productor de les dades ni garanteix que un valor, una URL o una citació siguin reals.

Hi ha una excepció metodològica important: si la pregunta estudia què es diu a les xarxes o què respon un LLM, aquests continguts poden convertir-se en dades primàries de la recerca. En aquest cas encara cal definir la mostra, el període, el model o servei, les limitacions, l'ètica i el procediment de recollida. Estudiar un rumor no converteix el rumor en un fet.

![Circuit de verificació d'una font]({{ site.baseurl }}/assets/diagrams/data-source-verification.mmd "Seguiu aquest circuit abans d'incorporar una dada al projecte: relacioneu la pregunta amb el productor, reviseu metodologia, cobertura i llicència, contrasteu el resultat i conserveu una còpia original documentada.")

### Dades personals, agregació i secret estadístic

Les dades poden no aparèixer «crues» encara que provinguin d'un registre oficial. Moltes fonts administratives i estadístiques parteixen d'informació individualitzada sobre persones, llars, empreses, targetes, terminals o vehicles, però allò que es publica és una versió agregada, anonimitzada, arrodonida o filtrada. Aquesta transformació no és un defecte: és una condició jurídica i metodològica perquè la informació sigui útil sense revelar identitats ni comportaments particulars.

Cal distingir dos marcs relacionats però diferents. La **protecció de dades personals** regula qualsevol tractament d'informació que identifiqui o pugui identificar una persona física. A la Unió Europea, el Reglament general de protecció de dades estableix principis com licitud, finalitat determinada, minimització, exactitud, limitació del termini de conservació, integritat i confidencialitat; a l'Estat espanyol, la Llei orgànica de protecció de dades personals i garantia dels drets digitals adapta i completa aquest marc {% cite europeanUnionGdpr2016 spanishLopdgdd2018 %}. Per això una enquesta pròpia, una taula amb correus electrònics, una trajectòria GPS o una base amb identificadors d'usuaris no es pot tractar com si fos una taula territorial ordinària.

El **secret estadístic** és una obligació específica de l'estadística oficial. La Llei de la funció estadística pública protegeix les dades confidencials que permeten identificar directament o indirectament les unitats estadístiques, prohibeix revelar-les i n'impedeix l'ús per a finalitats no estadístiques; la Llei d'estadística de Catalunya regula el mateix principi per a l'activitat estadística catalana, i el Reglament europeu sobre estadístiques europees incorpora la confidencialitat estadística com a principi de la producció estadística europea {% cite spanishPublicStatisticalFunction1989 cataloniaStatisticsLaw1998 europeanStatisticsRegulation2232009 %}. La unitat protegida no és només una persona: també pot ser una llar, una empresa, un establiment o qualsevol unitat informant que pugui quedar identificada per la combinació de variables.

A la pràctica, aquests marcs expliquen per què els portals poden agrupar edats, publicar només totals municipals, suprimir cel·les amb pocs casos, arrodonir valors, aplicar llindars de difusió o oferir informació per seccions censals en lloc de per adreces. Una secció censal permet baixar d'escala dins d'un municipi, però continua sent una unitat agregada: no representa una persona ni una casa concreta. Quan es treballa amb padró, cens, enquestes o mobilitat, cal entendre que el procediment de difusió forma part de la dada i que no s'ha de reconstruir allò que la publicació ha protegit deliberadament.

::: table "Privacitat i formes de publicació de dades"
| Situació | Què pot contenir l'origen | Forma habitual de difusió | Precaució |
| --- | --- | --- | --- |
| Padró o cens | Persones, llars, edats, sexes, adreces o unitats territorials fines | Taules agregades per municipi, secció censal, grup d'edat o sexe | No interpretar l'agregat com si fos microdada individual |
| Registre administratiu | Expedients, titulars, establiments, permisos o dates de tramitació | Camps seleccionats, dades públiques i exclusions de camps sensibles | Distingir activitat administrativa i fenomen real |
| Telefonia mòbil | Registres generats per terminals i xarxes | Matrius origen-destinació, fluxos agregats o indicadors per zones i franges | Revisar metodologia, cobertura, biaixos i llindars de privacitat |
| Targetes de transport | Validacions, línies, parades, títols i hores | Dades agregades o anonimitzades sota conveni o recerca controlada | Evitar reconstruir trajectòries personals o perfils identificables |
| Enquestes pròpies | Respostes, opinions, edat, lloc, contacte o altres atributs | Taula depurada amb consentiment, minimització i anonimització | Informar participants i recollir només allò necessari |
| GPS tracking | Trajectòries, ritmes, temps d'aturada i llocs freqüents | Indicadors agregats, traces anonimitzades o resultats resumits | Les traces poden revelar domicili, feina o hàbits personals |
:::

Les dades de mobilitat produïdes de manera passiva són un exemple especialment important per a geografia i turisme. El Ministeri de Transports utilitza tecnologies de Big Data i intel·ligència artificial aplicades a registres generats per terminals de telefonia mòbil per estudiar la mobilitat a escala estatal i difon resultats oberts agregats, juntament amb metodologia per interpretar-los {% cite ministerioMovilidadBigData2026 %}. En altres projectes, les dades de telefonia poden adquirir-se a empreses operadores o intermediàries ja agregades per zones, franges horàries i tipus de visitant; això permet estudiar mobilitats estacionals en destinacions litorals, però limita la verificació externa perquè l'equip investigador no controla tot el procés de generació, filtratge i anonimització dels registres originals {% cite zaragoziPassiveMobileData2021 %}. A escala regional, les dades de targetes intel·ligents de transport també poden informar sobre patrons de mobilitat turística, com mostra l'estudi sobre l'ús de transport públic a la Costa Daurada amb dades del sistema de validació del Camp de Tarragona {% cite gutierrezSmartTravelCardTourism2020 %}. Aquest tipus de dades exigeix convencions de noms, control de duplicats i traçabilitat perquè diferents persones no refacin el mateix procés ni perdin la relació entre fitxers, consultes i resultats {% cite zaragoziFileNamingConvention2020 %}. En aquests casos, el valor analític prové del volum i la granularitat temporal, però l'accés als registres originals acostuma a requerir convenis, controls estrictes i formats que preservin el secret estadístic i la privacitat. Per això cal distingir entre resultats oberts agregats, dades comprades ja agregades i microdades restringides: no ofereixen la mateixa capacitat d'auditoria ni de reproducció.

Les dades recollides pel mateix estudiantat també exigeixen responsabilitat. Una enquesta amb Microsoft Forms, Google Forms o una eina similar ha d'explicar qui recull la informació, amb quina finalitat, quines preguntes són obligatòries, durant quant temps es conservaran les respostes i si es compartiran resultats. El consentiment informat no és només una casella: és la garantia que la persona participant entén què està aportant i quin ús se'n farà. Si es recullen ubicacions, fotografies, opinions sensibles, identificadors o dades de menors, cal extremar la prudència i consultar el professorat abans de continuar.

En recerca universitària, alguns projectes amb persones, dades sensibles o seguiment de comportaments poden requerir revisió per un comitè d'ètica o un procediment institucional equivalent. Aquí és útil distingir la protecció de les persones de la qualitat de la documentació. Els principis FAIR proposen que les dades siguin **localitzables** (*findable*), **accessibles** (*accessible*), **interoperables** (*interoperable*) i **reutilitzables** (*reusable*) {% cite wilkinsonFAIRGuidingPrinciples2016 %}. No són una ordre de publicar-ho tot a internet, sinó una pauta perquè un conjunt de dades, o almenys la seva documentació, pugui ser trobat, entès i usat correctament per altres persones autoritzades.

Que unes dades siguin **localitzables** vol dir que tenen un títol, un identificador, una fitxa o una ruta estable i prou metadades perquè es puguin tornar a trobar. Que siguin **accessibles** vol dir que s'indica com obtenir-les o sota quines condicions es poden consultar; l'accés pot ser obert, restringit o fins i tot tancat si hi ha motius legals o ètics. Que siguin **interoperables** vol dir que utilitzen formats, codis, vocabularis, sistemes de referència i estructures que altres programes o persones poden interpretar sense dependre d'una explicació oral. Que siguin **reutilitzables** vol dir que inclouen procedència, llicència, qualitat, cobertura, unitats i limitacions suficients perquè una altra persona sàpiga què pot fer amb elles i què no.

Per tant, FAIR no elimina les obligacions de privacitat ni el secret estadístic. Una solució responsable pot ser publicar metadades, codi, mètode, dades agregades o taules anonimitzades, i mantenir les microdades sota accés restringit quan la llei, el consentiment o l'ètica ho exigeixen. En un treball del curs, una enquesta pot ser FAIR si el projecte documenta la pregunta, el formulari, el període, la mostra, el tractament d'anonimització i les taules agregades, encara que les respostes individuals no es comparteixin.

>>>>>> **No s'han de publicar microdades identificables.** Una taula amb noms, correus, telèfons, adreces, coordenades de trajectes, identificadors de targeta o combinacions rares d'atributs pot revelar persones encara que no inclogui el nom complet. Abans de compartir dades pròpies, cal reduir el detall, eliminar identificadors, agregar resultats i comprovar que el consentiment permet l'ús previst.

### Pauta per verificar una font

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

### Exemples de metadades en fonts diferents

Les metadades poden aparèixer en una pàgina metodològica, una fitxa de catàleg, la capçalera d'un fitxer o la resposta d'un servei de consulta. Es poden distingir metadades de **descoberta**, que permeten trobar el recurs; d'**avaluació**, que ajuden a decidir si és adequat; i d'**ús**, que expliquen com interpretar-lo o connectar-s'hi. En fonts geoespacials també cal diferenciar les metadades del conjunt, del servei i de cada capa.

::: table "Nivells que pot caldre documentar segons el tipus de recurs"
| Nivell | Quan apareix | Què cal documentar |
| --- | --- | --- |
| Catàleg o fitxa | Quan un portal descriu conjunts de dades abans de descarregar-los | Productor, títol, territori, data, llicència i distribucions disponibles |
| Distribució tabular | Quan el conjunt s'obté com a taula, fitxer o resposta tabular d'un servei | Format, dimensions, filtres, unitats, període i URL o consulta completa |
| Servei | Quan un servidor respon peticions i retorna dades, metadades, mapes renderitzats o objectes | Adreça de consulta, operacions, formats, límits, condicions d'ús i sistema d'identificació de recursos |
| Capa geoespacial | Quan es treballa amb dades espacials en un sistema d'informació geogràfica (SIG), un servei cartogràfic o un fitxer amb geometria o cobertura | Nom de capa, geometria o ràster, sistema de referència, extensió, escala o resolució i atributs disponibles |
:::

Una capa no és qualsevol tema d'una taula. Una taula de població municipal continua sent una dada plana encara que després es vulgui cartografiar; només esdevé una capa de treball quan s'uneix a una geometria municipal, conté coordenades o s'obre en un SIG com a recurs espacial. Per això cal distingir la distribució tabular, que conserva valors i dimensions, de la capa geoespacial, que afegeix geometria, sistema de referència i extensió.

![Camins que cal documentar segons si la font és una taula, una resposta tabular, una dada geoespacial o un servei cartogràfic]({{ site.baseurl }}/assets/diagrams/data-source-levels.mmd "Documenteu el camí que porta fins a la dada final: el catàleg ajuda a descobrir el recurs, el conjunt defineix què mesura, les dades planes segueixen una ruta tabular, les dades espacials segueixen una ruta geoespacial, i una taula només esdevé capa quan s'uneix amb geometria o coordenades.")

El diagrama no descriu una jerarquia obligatòria en tots els portals. Una taula estadística descarregada directament pot no tenir cap capa; un servei de consulta pot retornar una taula sense cap geometria; un fitxer geoespacial pot contenir diverses capes sense que hi hagi cap servei web actiu; i un servei cartogràfic pot permetre veure una ortofoto sense descarregar-ne els píxels originals. La utilitat és recordar que la dada final no s'explica només pel fitxer que queda al disc. També s'ha de conservar el camí que ha portat fins a aquell fitxer, resposta o capa derivada.

#### Eurostat: una taula estadística multidimensional

El conjunt [`demo_pjan`](https://ec.europa.eu/eurostat/databrowser/view/demo_pjan/default/table?lang=en) no es descriu només amb el títol «Population on 1 January by age and sex». La fitxa mostra el codi persistent, l'identificador digital d'objecte (DOI), la font, la darrera actualització i l'enllaç a la fitxa metodològica demogràfica d'Eurostat. La resposta estructurada del servei afegeix dimensions com freqüència, unitat, edat, sexe, territori i temps. Els flags d'observació informen si un valor és provisional, estimat o afectat per una ruptura. Per interpretar una única xifra cal conservar totes les categories que la defineixen.

::: table "Lectura mínima de les metadades d'Eurostat"
| Element | Exemple a `demo_pjan` | Pregunta que resol |
| --- | --- | --- |
| Identificador | `demo_pjan` i DOI `10.2908/DEMO_PJAN` | Quin conjunt exacte s'ha utilitzat? |
| Dimensions | `freq`, `unit`, `age`, `sex`, `geo`, `time` | Quina combinació representa cada valor? |
| Unitat | `NR`, nombre | El valor és un recompte, percentatge o taxa? |
| Actualització | Data i hora de la versió publicada | Quan es va revisar la base? |
| Estat | Flags associats a l'observació | És provisional, estimada o confidencial? |
:::

#### Idescat: metadades dins d'una resposta estructurada

El [servei de consulta de Taules de l'Idescat](https://www.idescat.cat/dev/api/taules/) retorna conjuntament dades i estructura. Una [consulta de població](https://api.idescat.cat/taules/v2/pmh/1180/8078/com/data?SEX=F&COM=01,TOTAL&_LAST_=1) inclou dimensions, categories, rols geogràfic i temporal, unitats, font, notes i data d'actualització. L'extensió `break` pot avisar d'una ruptura territorial. Això permet que un programa sàpiga què significa cada posició del vector de valors, però només si es conserva la resposta completa i no se n'extreu una columna descontextualitzada.

#### Servei d'ortofotos estatals i metadades de capa

El Pla Nacional d'Ortofotografia Aèria (PNOA) es pot consultar mitjançant serveis cartogràfics de l'Instituto Geográfico Nacional (IGN) i del Centro Nacional de Información Geográfica (CNIG). El seu [document de capacitats](https://www.ign.es/wms-inspire/pnoa-ma?SERVICE=WMS&REQUEST=GetCapabilities) és una resposta tècnica de text estructurat. A escala de servei identifica l'IGN i la Infraestructura de Datos Espaciales de España (IDEE), descriu el mosaic d'ortofotos i Sentinel-2, declara els formats de resposta i informa de la condició d'atribució Creative Commons indicada pel servei. A escala de capa, `OI.OrthoimageCoverage` enumera sistemes de referència, extensió geogràfica, atribució, estils i enllaços a registres normalitzats de metadades per a cada campanya.

::: table "Conjunt, servei i capa en el PNOA"
| Nivell | Metadades característiques | Decisió que permeten prendre |
| --- | --- | --- |
| Conjunt | Data de vol, resolució, cobertura i mètode de mosaic | Saber si la imatge és adequada per al període i detall requerits |
| Servei cartogràfic | Operacions, formats, límits de mida, organisme i condicions | Saber com formular la petició i com atribuir el resultat |
| Capa | Nom tècnic, sistema de referència, extensió, estil i consulta disponible | Identificar la capa i construir una petició de mapa |
:::

La pràctica de lectura consistirà a localitzar en cada exemple cinc elements: productor, definició, cobertura, data i llicència. Si algun d'aquests elements no es pot trobar, la limitació s'ha de registrar abans de continuar.

## Obertura, estàndards i reproduïbilitat

Quan una font ja sembla adequada, encara queda una pregunta pràctica: es pot usar de manera responsable i reconstruïble? Treballar amb dades no consisteix només a obtenir un fitxer. Cal saber si es pot reutilitzar legalment, si el format permet processar-lo, si altres eines el poden llegir i si el resultat es podrà reconstruir més endavant. Aquesta secció situa l'obertura, els estàndards i la reproduïbilitat com a condicions del treball, no com a complements administratius.

>>>>> Un projecte de dades ha de preparar-se amb criteris mínims d'obertura, documentació i reproduïbilitat.
>>>>>
>>>>> - Distingir dades obertes, formats oberts, estàndards oberts i programari lliure.
>>>>> - Llegir llicències i condicions de servei abans de reutilitzar un recurs.
>>>>> - Reconèixer que les plataformes privades poden canviar permisos, límits i vies d'accés.
>>>>> - Organitzar fitxers, carpetes i documentació perquè el resultat es pugui revisar.

### Sentits diferents de l'obertura

En un projecte es poden combinar diversos tipus d'obertura que no s'han de confondre:

- **Dades obertes:** dades accessibles sota una llicència que en permet la reutilització i redistribució.
- **Format obert:** especificació pública que diferents programes poden implementar, com CSV, GeoJSON o un contenidor geoespacial documentat públicament.
- **Estàndard obert:** acord tècnic publicat per facilitar que sistemes diferents intercanviïn informació, per exemple quan un SIG es connecta a un servidor cartogràfic.
- **Programari lliure i de codi obert:** programari que permet usar, estudiar, modificar i redistribuir el codi segons una llicència determinada.
- **Recerca oberta:** pràctiques que faciliten l'accés a publicacions, dades, codi, mètodes i resultats.

Una base de dades pot publicar-se en un format obert i mantenir una llicència restrictiva. A la inversa, unes dades amb llicència oberta poden distribuir-se en un format difícil de processar. També es pot fer una anàlisi reproduïble amb programari privatiu si se'n documenten prou bé els passos i versions, encara que una altra persona necessitarà accés al mateix programari. L'obertura facilita la reproducció, però no la garanteix per si sola.

Les llicències més habituals en els portals del capítol inclouen Creative Commons, llicències pròpies de les administracions i, en el cas de bases de dades, l'Open Database License. Sempre cal llegir la condició concreta. `CC BY 4.0` exigeix atribució; domini públic i `CC0` redueixen les restriccions; `ODbL` incorpora obligacions específiques per a bases derivades. «Sense cost» no informa de cap d'aquestes condicions.

### Llicències de dades, codi i serveis

La llicència indica els permisos i les obligacions, però primer cal identificar quin objecte regula. Les dades, el codi font, la documentació, una captura, una base cartogràfica i l'accés automatitzat a un servei web poden tenir condicions diferents dins del mateix portal.

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

Finalment, les **condicions d'un servei** poden limitar volum, freqüència de peticions, emmagatzematge o ús de tessel·les encara que les dades subjacents siguin obertes. La llicència d'OpenStreetMap no converteix els servidors públics de tessel·les en una infraestructura sense límits; de la mateixa manera, una clau d'accés gratuïta no atorga drets generals sobre totes les respostes.

### Plataformes privades i accés canviant

Les plataformes privades poden ser fonts valuoses per estudiar mobilitat, imatges, ressenyes o converses públiques, però no funcionen com un arxiu públic neutral. Quan una persona crea un compte, puja contingut o utilitza una eina de consulta automatitzada, accepta unes condicions que poden regular propietat intel·lectual, permisos de visualització, ús comercial, conservació o retirada de contingut, comunicació a tercers, límits de peticions i responsabilitat sobre còpies de seguretat. Aquestes condicions poden canviar amb el temps i poden ser diferents de la llicència concreta associada a una fotografia, una ruta o una publicació.

Flickr permet veure aquesta separació amb claredat. Les seves condicions generals indiquen que l'usuari conserva els drets de propietat intel·lectual sobre el contingut que puja, però concedeix a la plataforma els permisos necessaris per prestar el servei, complir instruccions i requeriments legals, i gestionar determinades situacions de seguretat o retirada {% cite flickrTermsConditionsUse2025 %}. Les condicions de la seva interfície de programació d'aplicacions, o **API**, recorden que les fotografies són propietat dels usuaris i que una aplicació ha de respectar les llicències, la privacitat i les retirades que decideixi cada titular; també imposen límits d'ús, restriccions comercials, requisits d'atribució i la possibilitat que l'accés es modifiqui, limiti o acabi {% cite flickrAPITermsUse2018 %}. Per tant, obtenir dades mitjançant una API no equival a adquirir un dret general sobre tot allò que la plataforma mostra.

Aquest problema no és només legal, sinó metodològic. La recerca sobre xarxes socials ha documentat que moltes plataformes han restringit l'accés programàtic que abans permetia estudiar comunicació pública a gran escala. Bruns descriu aquest gir com una «APIcalypse» que dificulta la recerca crítica perquè les plataformes controlen cada vegada més què es pot observar, amb quin volum i sota quines condicions {% cite brunsAfterAPIcalypse2019 %}. Freelon parla d'una etapa post-API en què la recerca computacional ha de combinar vies diverses, negociar accessos i acceptar que determinades dades ja no són reproduïbles amb la mateixa facilitat que abans {% cite freelonComputationalResearchPostAPI2018 %}. En un treball del curs, això obliga a documentar no només la URL o la consulta, sinó també la data, la política vigent, els permisos acceptats, els camps obtinguts, els límits aplicats i qualsevol canvi que impedeixi repetir l'extracció.

Quan hi ha dades personals, la situació és encara més exigent. A la Unió Europea, el Reglament general de protecció de dades no tracta les dades personals com un recurs lliurement explotable pel fet que una plataforma les hagi recollit. Exigeix base jurídica, finalitat determinada, minimització, termini de conservació, seguretat i drets de les persones, entre altres principis {% cite europeanUnionGdpr2016 %}. Aquest marc és més garantista que el d'altres territoris i no s'ha de diluir presentant la governança de les dades personals com una simple qüestió d'acceptar condicions privades. Si una plataforma no permet entendre clarament què es pot obtenir i reutilitzar, la decisió responsable és reduir l'abast, usar dades agregades o buscar una font alternativa.

### Estàndards per intercanviar dades

Un estàndard descriu una manera compartida de representar o intercanviar informació. No és una marca comercial ni un programa. Aplicacions, servidors institucionals i biblioteques de programació poden entendre's perquè implementen la mateixa especificació. Quan QGIS obre un servei de mapes web com **WMS** (*Web Map Service*) de l'IGN o quan un portal estadístic retorna **JSON-stat**, un format per codificar dades estadístiques multidimensionals, no hi ha màgia: hi ha un acord públic sobre com s'escriu una petició, com s'identifica una capa, com s'expressa una dimensió o com s'anuncia una llicència.

Els estàndards també tenen una dimensió institucional. L'[Open Geospatial Consortium](https://www.ogc.org/about-ogc/) reuneix administracions, empreses, universitats i altres organitzacions que treballen en comitès tècnics, grups de treball d'estàndard i grups de domini per consensuar especificacions geoespacials. [ISO/TC 211](https://committee.iso.org/home/tc211) és el comitè tècnic d'ISO per a informació geogràfica i geomàtica; el seu àmbit inclou models de dades, serveis, metadades, qualitat i esquemes espaciotemporals. La feina d'aquests organismes no substitueix els portals de dades, però crea el llenguatge comú que després implementen portals, servidors i programes.

En informació geogràfica i turística apareixen diversos organismes i famílies d'estàndards. La taula no s'ha de memoritzar com un glossari de sigles; serveix per saber quin problema resol cada peça quan apareix en un portal, una URL o una fitxa de metadades.

::: table "Famílies d'estàndards i funció principal"
| Família | Què ajuda a resoldre | Exemple que pot aparèixer al curs | Confusió habitual |
| --- | --- | --- | --- |
| ISO/TC 211 | Descriure informació geogràfica, metadades, qualitat i sistemes de referència | ISO 19115 per a metadades o ISO 19111 per a sistemes de referència de coordenades (CRS) | Pensar que ISO és un portal de dades |
| OGC | Fer interoperables serveis, APIs, formats i models geogràfics | WMS, WMTS, WFS, GeoPackage, OGC API Features | Pensar que un servei OGC implica dades obertes |
| SDMX | Intercanviar dades estadístiques multidimensionals amb dimensions, unitats i atributs | Respostes i estructures estadístiques d'Eurostat | Copiar només el vector de valors i perdre les dimensions |
| DCAT | Descriure catàlegs, conjunts, serveis i distribucions de dades al web | Fitxes federades entre portals de dades obertes | Confondre la fitxa del catàleg amb la dada analítica |
| INSPIRE | Coordinar la infraestructura europea d'informació espacial pública | Serveis i metadades harmonitzats d'administracions europees | Tractar INSPIRE com si fos un format únic |
| IETF i W3C | Fer funcionar el web i els formats generals d'intercanvi | URI, HTTP, JSON, RDF, DCAT i GeoJSON | Oblidar que aquests estàndards no defineixen per si sols la qualitat de les dades |
:::

La lectura pràctica és preguntar-se què està regulant cada peça. ISO ajuda a descriure conceptes, metadades i qualitat; OGC permet connectar eines geogràfiques; SDMX conserva dimensions estadístiques; DCAT ajuda a descobrir conjunts i serveis; INSPIRE coordina la infraestructura institucional europea. L'[IETF](https://www.ietf.org/about/introduction/) publica estàndards d'internet com els relacionats amb URI, HTTP i altres protocols; el [W3C](https://www.w3.org/about/) desenvolupa estàndards del web i vocabularis com [DCAT](https://www.w3.org/TR/vocab-dcat-3/). Per això una API geogràfica combina sovint capes: HTTP per transportar la petició, una URL per identificar el recurs, JSON o XML per codificar la resposta, i una especificació OGC o estadística per definir què vol dir cada camp.

La confusió més habitual és tractar una sigla com si identifiqués tota la font. **INSPIRE** no és un format de fitxer ni una capa concreta: és un marc europeu, recollit a la [INSPIRE Knowledge Base](https://knowledge-base.inspire.ec.europa.eu/index_en), perquè les administracions publiquin determinades dades espacials amb metadades i serveis harmonitzats. **OGC** no garanteix que les dades siguin obertes, actuals o adequades: publica especificacions perquè un client com QGIS, un navegador o un script pugui demanar mapes, tessel·les, cobertures o objectes geogràfics a un servidor. **SDMX** tampoc no és una taula concreta d'Eurostat, sinó una manera d'intercanviar dades estadístiques amb dimensions, atributs, codis i metadades. Per això una font pot ser pública, INSPIRE, OGC i alhora tenir una llicència, una escala o una data que la faci inadequada per a una pregunta determinada.

Un format tampoc no és necessàriament un estàndard de servei. GeoPackage és un format d'emmagatzematge i WMS és una interfície que produeix mapes. WFS i OGC API Features, en canvi, estan orientats a objectes vectorials; WMTS està pensat per servir tessel·les; WCS treballa amb cobertures ràster. Distingir aquestes funcions evita demanar a un WMS una taula d'atributs o confondre un mapa visualitzat amb les dades que l'han generat.

>>> **Llegir una URL amb diverses capes de significat.** A `https://www.ign.es/wms-inspire/pnoa-ma`, `wms` indica una interfície OGC que retorna mapes com a imatge; `inspire` suggereix que el servei s'inscriu en el marc europeu d'informació espacial; i `pnoa-ma` identifica el producte o servei concret. Cap d'aquestes parts, per separat, no diu encara quina capa s'ha demanat, quin rectangle d'extensió espacial (`BBOX`) s'ha utilitzat ni quina llicència s'ha d'atribuir.

### Programari i codi obert

El programari de codi obert permet inspeccionar les operacions i redueix barreres perquè altres persones repeteixin el treball. [LibreOffice](https://www.libreoffice.org/) ofereix un full de càlcul de codi obert, mentre que [OpenRefine](https://openrefine.org/) està especialitzat en l'exploració i transformació de dades tabulars. Que una eina sigui oberta no converteix automàticament el projecte en reproduïble: encara cal registrar-ne la versió, conservar les dades i explicar les operacions.

### Reproduïbilitat i ordre del projecte

Un resultat és reproduïble quan una altra persona pot partir de les mateixes dades originals, seguir les decisions documentades i obtenir el mateix resultat o explicar qualsevol diferència. No n'hi ha prou amb lliurar el mapa final. Cal conservar els ingredients, l'entorn i la seqüència que l'han produït. En ciència computacional, aquesta exigència s'ha formulat com la necessitat de publicar prou dades, codi i instruccions perquè els resultats puguin regenerar-se i no només llegir-se {% cite pengReproducibleResearchComputational2011 %}. Les dificultats són reals: una enquesta de *Nature* a més de 1.500 investigadors va fer visible la percepció d'una crisi de reproduïbilitat i la freqüència amb què resultats propis o aliens no es podien reproduir fàcilment {% cite baker1500ScientistsLift2016 %}.

La reproduïbilitat forma un espectre. Compartir només una figura ofereix molt poca capacitat de comprovació; afegir dades, codi, versions del programari, llicències i documentació redueix progressivament les ambigüitats. En projectes avançats es poden incorporar scripts i quaderns executables, control de versions, fitxers de dependències, proves automatitzades, contenidors Docker o Podman i fluxos que reconstrueixen els resultats des de l'inici {% cite zaragoziContainerTechnologies2020 %}.

Els fluxos basats en LLM introdueixen més elements que cal fixar, però no són reproduïbles en el mateix sentit que una fórmula, una consulta o un script determinista. Encara que es conservin el prompt, el xat, el model declarat i la data, el mateix agent pot respondre de manera diferent, el proveïdor pot canviar el model i una versió posterior pot donar una sortida diferent. En un procés amb generació augmentada per recuperació, o RAG, caldria documentar el corpus consultat, la seva versió, el model, les instruccions, els paràmetres, el mètode de fragmentació, les representacions vectorials i la configuració de recuperació. RAG pot fer més traçable l'origen de les respostes, però no garanteix per si sol que dues execucions siguin idèntiques.

Aquestes tècniques requereixen més coneixements i infraestructura. Les bones pràctiques, però, comencen amb accions molt més senzilles: noms comprensibles, una estructura estable de carpetes, originals immutables i un registre de procedència. Una convenció compartida evita duplicacions i permet entendre un projecte sense dependre de la memòria de qui l'ha creat {% cite zaragoziFileNamingConvention2020 %}.

No existeix un únic arbre correcte per a tots els projectes. Es recomana utilitzar noms breus en anglès, minúscules i caràcters ASCII perquè funcionin de manera consistent entre sistemes operatius, scripts i serveis. Quan existeix una convenció àmpliament reconeguda, convé aprofitar-la: `src` per al codi font, `data` per a les dades, `outputs` per als resultats generats, `dist` per als lliurables i `README.md` per a la documentació inicial. Quan no existeix un nom establert, s'ha de triar un terme amb significat semàntic clar i mantenir-lo durant tot el projecte.

![Estructura orientativa d'un projecte reproduïble]({{ site.baseurl }}/assets/diagrams/reproducible-project-structure.puml "Organitzeu el projecte perquè una altra persona pugui reconstruir-lo: originals a data/raw, dades preparades a data/processed, instruccions a src, projecte SIG a qgis, resultats a outputs, lliurables a dist, proves a sandbox i explicació inicial a README.md."){: data-figure-width="15rem"}

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

## Com s'accedeix a les dades

Localitzar una font no és el mateix que obtenir-ne dades analitzables. Abans de triar una eina cal distingir d'on surt la dada i per quina via s'hi accedeix. Una part del curs treballarà amb dades publicades formalment per organismes, una altra pot recollir dades pròpies amb enquestes o observació, i excepcionalment es pot extreure informació visible en una pàgina web o continguda en un document digital, com un PDF, una imatge, un escaneig o una taula incrustada. No tenen les mateixes garanties ni les mateixes obligacions: una recollida pròpia exigeix consentiment i minimització, una font publicada exigeix llegir metadades i llicència, i qualsevol extracció automatitzada exigeix permís, prudència tècnica i verificació manual.

Quan les dades ja estan publicades, una mateixa institució pot oferir el mateix conjunt mitjançant una taula interactiva, un fitxer, una interfície de programació d'aplicacions —API, de l'anglès *application programming interface*— i un geoservei. No són fonts diferents: són vies d'accés amb propietats diferents.

>>>>> L'accés a les dades exigeix distingir vies diferents i decidir quina convé a cada tasca.
>>>>>
>>>>> - Diferenciar dades recollides pel projecte, dades publicades i informació extreta de pàgines o documents digitals.
>>>>> - Distingir una interfície gràfica, un fitxer descarregable, una API i un geoservei.
>>>>> - Saber quan una imatge servida com a mapa web serveix per veure i quan cal una dada vectorial per analitzar.
>>>>> - Reconèixer que l'extracció automatitzada de pàgines o documents només és adequada amb supervisió i permís.

![Vies d'accés i de producció de dades]({{ site.baseurl }}/assets/diagrams/data-access-modes.mmd "Trieu la via d'accés segons la tasca: recollida pròpia, publicació formal, interfície, fitxer, API, geoservei, extracció web o extracció documental supervisada no tenen les mateixes garanties ni obligacions.")

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
| GeoTIFF | Imatge ràster georeferenciada | Comprovar resolució, sistema de referència, nombre de bandes i valor nodata |
| GML | Objectes geogràfics estructurats en XML | Esquema complex i fitxers voluminosos |
| LAZ/LAS | Núvols de punts LiDAR | Gran volum i necessitat d'eines específiques |
:::

>>>> **No s'ha de confiar en l'aplicació predeterminada.** Obrir un fitxer amb doble clic delega la interpretació al programa que el sistema operatiu hi hagi associat. En un CSV, el full de càlcul pot convertir codis en nombres o dates, triar un delimitador incorrecte i confondre punts i comes decimals. És preferible **importar-lo** indicant que els codis són text, quina codificació utilitza i com representa els decimals i els valors absents. El mateix criteri s'aplica als altres formats: un visor d'imatges pot mostrar un GeoTIFF però ignorar-ne la georeferenciació; un descompressor no interpreta les capes d'un GeoPackage; i obrir només el `.shp` no garanteix que es conservin tots els components d'un Shapefile. Primer cal identificar el format i després escollir l'eina adequada.

### Accés mitjançant API

Una **API** és una interfície perquè un programa demani dades a un altre sistema de manera estructurada. En una API web, la petició sol ser una URL formada per un endpoint i uns paràmetres; la resposta acostuma a ser JSON, JSON-stat, CSV o XML.

L'API és útil quan cal repetir una consulta, actualitzar-la o recuperar només una part d'un conjunt gran. No elimina la necessitat d'entendre la font: una petició tècnicament correcta pot seleccionar la variable o la unitat equivocada.

En aquest capítol, una API no s'introdueix com una exigència de programació avançada, sinó com una manera de fer explícita la selecció. Una URL amb paràmetres pot deixar escrit el país, l'any, l'indicador i el format; una descàrrega feta només amb clics pot ser igualment vàlida, però caldrà conservar més notes perquè una altra persona pugui repetir-la.

Endpoint
: Adreça base que rep la petició, com `https://api.worldbank.org/v2/`.

Paràmetres
: Opcions que concreten la consulta, com el país, l'indicador, l'any, el format o el límit de files. Sovint apareixen després del signe `?` i se separen amb `&`.

Resposta
: Contingut retornat pel servidor. Pot incloure valors, metadades, codis d'error, paginació o avisos de limitació. Copiar només una xifra i perdre la resta de la resposta elimina part del mètode.

>> **La URL també forma part del mètode.** Quan els paràmetres d'una consulta apareixen a la URL, conservar l'adreça completa ajuda a repetir la selecció. Encara cal registrar la data d'accés, perquè el servidor pot actualitzar els valors mantenint la mateixa consulta.

#### Exemple mínim amb el Banc Mundial

La petició següent demana la població total (`SP.POP.TOTL`) d'Espanya (`ESP`) per a 2023 i sol·licita una resposta JSON:

```text
https://api.worldbank.org/v2/country/ESP/indicator/SP.POP.TOTL?date=2023&format=json
```

Es pot enganxar directament al navegador. La URL es pot llegir per parts:

```text
https://api.worldbank.org/v2/      # servei i versió
country/ESP/                       # territori
indicator/SP.POP.TOTL              # indicador
?date=2023&format=json             # paràmetres
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

### Extracció automatitzada sense descàrrega ni API

De vegades una web o un document mostra informació útil però no ofereix cap fitxer descarregable ni cap API documentada. En aquest cas pot aparèixer la idea de fer **extracció automatitzada de dades**: capturar parts d'una pàgina web, un PDF, una imatge, un escaneig o un altre document digital i convertir-les en una taula. El cas més conegut és el *web scraping*, manlleu anglès que designa l'extracció automàtica d'elements HTML d'una pàgina. En documents també es poden emprar tècniques com l'extracció de taules de PDF o el reconeixement òptic de caràcters, OCR, en imatges i escanejos.

Aquestes tècniques són potents, però més fràgils i avançades que les vies anteriors. En una pàgina web cal entendre mínimament com està construïda i com s'organitzen els elements que es volen seleccionar. En un PDF o una imatge cal comprovar si el text és realment text o només píxels, si les columnes es poden reconstruir sense errors i si el reconeixement automàtic introdueix confusions. La font pot canviar d'estructura, carregar contingut de manera dinàmica, limitar peticions, mostrar dades amb drets restringits o incloure informació personal que no s'hauria de copiar.

En aquest curs, l'extracció automatitzada de pàgines i documents no és una via principal per obtenir dades. Pot entendre's com una ampliació opcional per a estudiants que ja dominen la lectura de fonts, fitxers i API. Una eina visual del navegador, com l'extensió [Web Scraper per a Firefox](https://addons.mozilla.org/firefox/addon/web-scraper/) o una eina equivalent, pot servir per provar l'extracció de pocs camps d'una pàgina senzilla. En documents, qualsevol resultat obtingut d'un PDF, una imatge o un OCR s'ha de contrastar amb el document original perquè els errors de segmentació, columnes, accents o nombres són freqüents. Tot i així, abans de capturar res cal revisar les condicions d'ús, evitar dades personals, no sobrecarregar servidors, conservar l'URL o la referència exacta del document i documentar quins elements s'han seleccionat.

Els assistents basats en IA generativa poden ajudar a preparar una extracció, proposar quins elements seleccionar, interpretar una estructura HTML o explicar per què una taula d'un PDF no surt com s'esperava. També poden equivocar-se: poden inventar camps, ignorar paginació, seleccionar anuncis en lloc de dades, confondre columnes, llegir malament caràcters d'una imatge, saltar-se avisos legals o repetir peticions massa sovint. Per això un agent d'IA només hauria d'actuar amb instruccions molt concretes, volum baix, supervisió humana i comprovacions contra la font original. Si existeix una descàrrega oficial o una API, normalment és preferible a l'extracció automatitzada.

>>>>>> **No s'ha de fer extracció automatitzada de dades sensibles ni de fonts sense permís.** Si una pàgina o document prohibeix l'extracció, exigeix autenticació, mostra dades personals, o no permet entendre clarament la llicència, cal buscar una alternativa o demanar autorització. Que una dada sigui visible al navegador, en un PDF o en una imatge no implica que es pugui copiar, redistribuir o automatitzar-ne la captura.

### Accés mitjançant geoserveis

Els geoserveis publiquen informació geogràfica a través d'estàndards web. Un SIG com QGIS actua com a client: envia una petició al servidor i interpreta la resposta. La persona que fa l'anàlisi no necessita programar el servei, però sí entendre què està demanant. Les peces mínimes són el servidor, l'operació, la capa, el sistema de referència, l'extensió espacial i el format de resposta.

La primera decisió és separar **veure** de **analitzar**. Un WMS pot ser perfecte per comprovar visualment una ortofoto de fons, però només retorna una imatge composta pel servidor. Si cal comptar entitats, filtrar atributs o unir geometries amb una taula, cal una descàrrega vectorial, un WFS, una OGC API Features o un altre accés que proporcioni objectes i atributs.

Els principals tipus que es trobaran al curs són:

- **WMS:** retorna una imatge del mapa. Serveix per visualitzar, però no proporciona les geometries vectorials per analitzar-les.
- **WMTS:** retorna tessel·les d'imatge preparades i és eficient com a cartografia de fons.
- **WFS:** retorna objectes vectorials amb geometria i atributs que es poden consultar i processar.
- **OGC API Features:** ofereix objectes vectorials mitjançant una API web moderna, habitualment en GeoJSON.

També existeixen WCS per a cobertures ràster i catàlegs com STAC per descobrir imatges d'observació de la Terra. Abans de connectar un servei cal consultar-ne les capacitats, les capes, el sistema de referència, l'escala i les condicions d'ús. Que una capa es pugui veure no significa que es pugui descarregar o redistribuir.

::: table "Escollir un geoservei segons la tasca"
| Necessitat | Servei més probable | Resultat esperable | Precaució |
| --- | --- | --- | --- |
| Veure una ortofoto o un mapa de fons | WMS o WMTS | Imatge renderitzada | No és una capa vectorial editable |
| Analitzar geometries i atributs | WFS o OGC API Features | Objectes vectorials | Cal revisar límits, volum i llicència |
| Descobrir imatges de satèl·lit disponibles | STAC | Fitxes d'escenes i enllaços | La fitxa no és la imatge processada final |
| Treballar amb una cobertura ràster | WCS o descàrrega de fitxer | Valors ràster o fitxer GeoTIFF | Cal comprovar resolució, bandes i nodata |
:::

>> **`GetCapabilities` abans de `GetMap`.** En un servei OGC, la petició de capacitats explica quines operacions, capes, formats i sistemes de referència ofereix el servidor. La petició de mapa o dades ja és una selecció concreta. Si es guarda només la imatge final, es perd la informació que permet reconstruir per què aquella imatge era possible i quines alternatives existien.

#### Una petició WMS que es pot obrir al navegador

Un WMS no descarrega una tessel·la predefinida. L'operació `GetMap` demana al servidor que compongui una imatge amb una capa, una extensió geogràfica, un sistema de referència, una amplada, una alçada i un format. La petició següent utilitza la capa `OI.OrthoimageCoverage` del PNOA i una extensió centrada en la Facultat de Turisme i Geografia:

>> **No cal dominar encara una petició WMS completa.** En aquest punt n'hi ha prou amb entendre que una URL pot contenir paràmetres que concreten què es demana a un servidor. `SERVICE`, `REQUEST`, `LAYERS`, `CRS`, `BBOX`, `WIDTH` i `FORMAT` funcionen com a peces d'una instrucció. Els codis `EPSG`, les coordenades i els sistemes de referència s'entendran millor al capítol 4; aquí serveixen per veure que Internet no envia «el mapa», sinó una resposta a una petició concreta. Aquesta lectura també ajuda quan es demana suport a un assistent basat en LLM: com més explícits siguin servei, lloc, capa i format, més comprovable serà l'ajuda rebuda.

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

![Ortofoto PNOA de la Facultat de Turisme i Geografia]({{ site.baseurl }}/assets/img/data-sources/pnoa-facultat-turisme-geografia.jpg "La petició WMS retorna una imatge concreta de l'entorn de la Facultat de Turisme i Geografia; si canvien capa, extensió, mida o sistema de referència, canvia també el resultat. Font: IGN/CNIG, PNOA màxima actualitat, CC BY 4.0, consulta de l'11 d'agost de 2026.")

## Introducció als fulls de càlcul

Quan les dades ja s'han localitzat i obtingut, comença una feina menys visible però decisiva: preparar-les perquè puguin respondre la pregunta. El primer entorn de treball serà el full de càlcul perquè combina una taula, un llenguatge de fórmules i una interfície visual. Permet inspeccionar les dades directament, provar una operació i veure'n el resultat sense construir primer un programa complet. Aquesta immediatesa el fa adequat per començar a treballar amb taules territorials de volum moderat, però també pot afavorir canvis manuals difícils de reconstruir si el llibre no s'organitza amb criteri.

La secció és una introducció operativa, no un curs complet de fulls de càlcul. Està pensada perquè una persona que no ha treballat mai amb Excel, LibreOffice Calc o Google Sheets pugui arribar al laboratori amb els conceptes mínims anotats: llibre, full, cel·la, rang, referència, fórmula, còpia, tipus de dada i comprovació. Les classes pràctiques serviran per adquirir fluïdesa; el manual deixa escrit el vocabulari i els criteris perquè el procediment no depengui només de recordar on era cada botó.

Els exemples de fórmules utilitzen sovint noms de funció en anglès i separadors habituals en documentació tècnica. Segons l'aplicació i la configuració regional, caldrà adaptar noms com `SUM`, `IF`, `XLOOKUP` o `WEEKDAY`, i potser substituir comes per punts i coma. El criteri important és entendre l'operació: què entra a la fórmula, quina cel·la o rang consulta i quin resultat ha de retornar.

>>>>> El primer llibre de treball ha de permetre preparar una taula territorial revisable.
>>>>>
>>>>> - Reconèixer llibres, fulls, columnes, files, cel·les, rangs i fórmules.
>>>>> - Copiar cel·les, rangs, valors i fórmules sense perdre la traçabilitat.
>>>>> - Distingir referències relatives, absolutes i entre fulls.
>>>>> - Separar valor, tipus i format abans de calcular.
>>>>> - Preparar codis, correspondències, dates, absències i fórmules de comprovació.
>>>>> - Entendre per què les fórmules són més reproduïbles que una resposta d'un LLM.

### Orientar-se en el llibre, el full i la graella

Excel, LibreOffice Calc, Google Sheets i altres aplicacions comparteixen un funcionament bàsic. Un **llibre** és el fitxer de treball; dins del llibre hi ha **fulls**; cada full organitza una graella de **columnes** i **files**; i la intersecció d'una columna i una fila és una **cel·la**. Les columnes es designen amb lletres: `A`, `B`, `C` fins a `Z`, després `AA`, `AB`, `AC` i així successivament. Les files es numeren `1`, `2`, `3` fins al límit que admeti l'aplicació. Aquest límit no és infinit i varia segons el programa i la versió. Si una font supera el nombre de files o columnes que el full pot gestionar amb seguretat, caldrà treballar amb una eina de consulta, una base de dades o un llenguatge de programació.

Una referència com `B2` identifica la cel·la situada a la columna `B` i a la fila `2`. Una referència com `A2:D10` identifica un **rang** rectangular: totes les cel·les compreses entre les columnes `A` i `D` i les files `2` i `10`. Un rang pot ocupar una sola columna, com `B2:B100`, una sola fila, com `A2:D2`, o un bloc amb diverses files i columnes. Pensar el rang com un rectangle és important perquè moltes operacions del full de càlcul assumeixen aquesta forma: ordenar, filtrar, fer gràfics, copiar fórmules o construir una taula dinàmica.

Les fórmules comencen amb `=` i poden combinar valors, referències, operadors i funcions. En `=B2+C2`, `B2` i `C2` són cel·les d'origen, `+` és l'operador i el resultat apareix a la cel·la on s'ha escrit la fórmula. La pantalla pot mostrar `200`, però el mètode és la fórmula que explica d'on surt aquest `200`. Per això no s'ha de substituir una fórmula validada per un nombre escrit a mà si el resultat ha de poder revisar-se.

::: table "Capacitats estàndard d'un full de càlcul"
| Capacitat | Funcionament esperable | Aplicació al curs |
| --- | --- | --- |
| Graella | Organitzar cel·les en files i columnes | Reconèixer quina unitat representa cada fila i cada columna |
| Referències | Relacionar una fórmula amb cel·les o rangs | Calcular un indicador sense transcriure valors manualment |
| Fórmules i funcions | Fer operacions aritmètiques, lògiques, textuals, estadístiques i temporals | Comprovar tipus, calcular ràtios i validar totals |
| Emplenament | Estendre una fórmula mantenint referències relatives o absolutes | Aplicar el mateix càlcul a tots els municipis |
| Ordenació i filtre | Reorganitzar o mostrar files segons valors i condicions | Inspeccionar casos extrems, absències i categories |
| Agregació | Resumir dades amb funcions o taules dinàmiques | Obtenir totals per municipi o tipologia |
| Gràfics | Vincular una representació a un rang de dades | Comparar magnituds, composicions i relacions |
| Importació i exportació | Llegir i escriure formats com CSV, XLSX, ODS o PDF | Conservar dades, intercanviar llibres i exportar figures |
:::

Aquest nucli permet transferir l'aprenentatge entre programes. Entendre la diferència entre rang, valor i format, o el sentit d'una funció condicional, és més útil que memoritzar la posició exacta d'un botó. En un full de càlcul és més important saber dir què es vol fer —sumar un rang, buscar una correspondència, separar un codi, comptar absències o fixar un denominador— que recordar on es troben totes les funcions i eines de la interfície. Les funcions avançades, els gràfics disponibles, les taules dinàmiques, les macros, l'automatització i el treball col·laboratiu sí que poden variar considerablement.

Els programes de full de càlcul incorporen llistats explorables de funcions, assistents, categories i exemples. També es pot demanar ajuda a la documentació, al professorat o a un model de llenguatge quan cal construir una fórmula més complexa. Aquesta ajuda només és segura si la persona que treballa sap explicar l'operació i comprovar-ne el resultat: cap assistent substitueix la revisió dels rangs, dels tipus de dada, de les referències absolutes i del valor obtingut en una fila de prova.

![Esquema d'un assistent de funcions amb caixa de cerca, categories, resultats i comprovació]({{ site.baseurl }}/assets/img/data-sources/spreadsheet-function-browser.svg "Useu el cercador de funcions per passar d'una operació formulada amb paraules a una fórmula concreta; després reviseu rangs, separadors, referències i resultat amb una fila de prova. Esquema d'elaboració pròpia d'un assistent de funcions.")

No totes les habilitats tenen el mateix nivell de dificultat ni el mateix rendiment immediat. La progressió següent ordena allò que convé practicar de més bàsic a més avançat. Les primeres files són imprescindibles per al curs; les darreres obren possibilitats que poden requerir més pràctica.

::: table "Progressió d'habilitats en fulls de càlcul"
| Nivell | Habilitat | Operacions característiques | Utilitat en el curs |
| --- | --- | --- | --- |
| 1 | Orientació i selecció | Reconèixer fulls, cel·les, files, columnes i rangs rectangulars | No perdre's en una taula ni seleccionar fragments incorrectes |
| 2 | Importació i tipus | Importar CSV, fixar codis com a text, revisar decimals, dates i absències | Evitar errors abans de calcular |
| 3 | Còpia i emplenament | Copiar cel·les o rangs, arrossegar el controlador d'emplenament i enganxar valors, fórmules o formats | Repetir una operació sense reescriure-la fila a fila |
| 4 | Referències | Usar referències relatives, absolutes i entre fulls | Separar originals, transformacions i resultats |
| 5 | Fórmules bàsiques | Sumar, restar, dividir, calcular percentatges, ràtios i comprovacions | Construir indicadors simples i revisables |
| 6 | Codis i correspondències | Separar codis, comprovar longituds, buscar correspondències i detectar no coincidents | Unir taules sense dependre de l'ordre de les files |
| 7 | Funcions lògiques, textuals i temporals | Usar condicions, netejar text, classificar dates i calcular durades | Preparar camps i justificar decisions |
| 8 | Filtre, ordenació i validació | Filtrar, ordenar, buscar duplicats, comptar blancs i revisar rangs plausibles | Detectar problemes abans de fer gràfics o mapes |
| 9 | Resums i taules dinàmiques | Agrupar per comarca, tipologia o categoria; resumir totals, mitjanes i recomptes | Explorar patrons sense alterar la taula original |
| 10 | Importació avançada i automatització | Power Query, OpenRefine, scripts o connexions a API | Repetir processos quan el treball manual deixa de ser segur |
:::

>> **Practicar amb un projecte mascota.** La millor manera de guanyar fluïdesa és mantenir un petit projecte propi al marge de les activitats obligatòries: una base de dades de pel·lícules, cançons, restaurants, llocs visitats, comerços amb valoracions pròpies o lectures pendents. Un projecte així permet practicar codis, categories, dates, filtres, fórmules, taules dinàmiques i gràfics amb dades que resulten familiars. Si més endavant s'hi volen incorporar valoracions o informació recollida del web, cal aplicar les mateixes cauteles que en qualsevol font externa.

::: subfigures a+b "Identifiqueu els elements comuns d'un full de càlcul i llegiu una fórmula com una instrucció reproduïble, independentment del programa concret. Esquemes d'elaboració pròpia."
![Esquema d'un full de càlcul amb barra de fórmules, capçaleres, files, cel·la activa i rang]({{ site.baseurl }}/assets/img/data-sources/spreadsheet-parts.svg "Localitzeu barra de fórmules, capçaleres, números de fila, cel·la activa, referències i rang abans de revisar una taula. Esquema d'elaboració pròpia.")
![Esquema d'una fórmula que suma les cel·les B2 i C2 i mostra el resultat a D2]({{ site.baseurl }}/assets/img/data-sources/spreadsheet-sum-formula.svg "Llegiu la fórmula com una operació verificable: D2 conté =B2+C2, pren els valors de B2 i C2 i mostra el resultat calculat. Esquema d'elaboració pròpia.")
:::

### Seleccionar, copiar i emplenar

Seleccionar una cel·la no és el mateix que seleccionar una fila, una columna o un rang. Una fórmula escrita en una sola cel·la només afecta aquella cel·la; una operació aplicada a un rang pot afectar moltes files i columnes alhora. Per això, abans de copiar, eliminar, ordenar o formatar, cal mirar quin rectangle està seleccionat. Ordenar només una columna d'una taula, per exemple, pot desconnectar noms, codis i valors de la mateixa fila.

Una cel·la o un conjunt de cel·les es pot copiar dins del mateix full, a un altre full del mateix llibre o a un altre llibre de càlcul. Allò que s'enganxa pot ser el contingut complet, només el valor visible, només la fórmula, només el format o un enllaç a la cel·la d'origen, segons l'opció d'enganxat. Aquesta diferència és decisiva: enganxar **valors** conserva el resultat però elimina la fórmula; enganxar **fórmules** conserva el mètode però pot canviar les referències; enganxar **formats** només canvia l'aparença.

::: table "Opcions habituals d'enganxat"
| Opció | Què conserva | Quan pot ser útil | Risc principal |
| --- | --- | --- | --- |
| Enganxat complet | Valors, fórmules, formats i altres propietats | Moure un bloc dins del mateix llibre | Arrossegar formats o fórmules que no convenen |
| Enganxar valors | El resultat visible o emmagatzemat | Fixar una sortida exportable o importar una taula ja calculada | Perdre la fórmula que permetia auditar el càlcul |
| Enganxar fórmules | La regla de càlcul | Repetir el mateix mètode en un altre rang | Referències relatives que apunten a cel·les equivocades |
| Enganxar formats | L'aparença visual | Homogeneïtzar capçaleres o decimals visibles | Confondre aparença amb tipus de dada |
| Enganxar enllaç o referència | La connexió amb la cel·la d'origen | Construir un full preparat que llegeix un full original | Trencar l'enllaç si es mou o elimina l'origen |
:::

El controlador d'emplenament permet arrossegar una fórmula o un patró cap avall, cap amunt o lateralment. Si `D2` conté `=B2+C2` i s'arrossega cap a `D3`, normalment la fórmula es convertirà en `=B3+C3`. Aquesta adaptació és útil perquè aplica el mateix càlcul a totes les files. També pot crear errors si el full interpreta com a patró allò que només era un identificador, una etiqueta o una data que no s'havia de continuar automàticament.

Arrossegar també pot continuar patrons. Si una columna conté `2021`, `2022`, el full pot proposar `2023`; si conté dilluns i dimarts, pot continuar dies de la setmana; si conté `001`, pot convertir-lo en nombre o continuar una seqüència no desitjada. Per això, després d'emplenar, cal revisar les primeres i les darreres files del rang, i comprovar si s'ha copiat una fórmula, un valor o una sèrie automàtica.

>>>> **No s'ha d'ordenar una columna aïllada dins d'una taula.** Si es vol ordenar per població, habitatge o codi, s'ha de seleccionar tota la taula o activar el filtre sobre el bloc complet. Si només s'ordena una columna, els valors deixen de correspondre als municipis originals.

### Referències relatives, absolutes i entre fulls

Una referència **relativa** canvia quan la fórmula es copia. En `=B2+C2`, copiar la fórmula una fila més avall produeix normalment `=B3+C3`. Aquest comportament és adequat quan cada fila ha de calcular-se amb valors de la mateixa fila. Una referència **absoluta** queda fixada amb el signe `$`. En `$B$2`, ni la columna `B` ni la fila `2` canvien quan la fórmula es copia. També es pot fixar només la columna (`$B2`) o només la fila (`B$2`).

La referència absoluta és útil quan moltes files han d'utilitzar un mateix valor: una taxa de conversió, un total comarcal, una data de referència o un llindar. Si `B2:B23` conté la població municipal i `B25` conté el total comarcal, la fórmula `=B2/$B$25*100` calcula el pes del primer municipi i es pot copiar cap avall sense que el denominador deixi d'apuntar al total. Si s'escrivís `=B2/B25*100`, en copiar-la una fila avall el denominador passaria a `B26`, que podria estar buit o contenir una altra cosa.

Les fórmules també poden apuntar a altres fulls. Una referència com `raw_population!B2` indica la cel·la `B2` del full `raw_population`. Si el nom del full conté espais, moltes aplicacions escriuen la referència amb cometes simples, com `'Població 2021'!B2`. Aquesta capacitat permet conservar els fulls `raw_*` sense tocar i construir fulls preparats que llegeixen les dades originals mitjançant fórmules, consultes o passos documentats.

::: table "Comportament de les referències quan es copien"
| Fórmula original | Si es copia una fila avall | Lectura |
| --- | --- | --- |
| `=B2+C2` | `=B3+C3` | Les dues referències són relatives |
| `=B2/$B$25` | `=B3/$B$25` | El numerador canvia, el total queda fixat |
| `=$B2/C2` | `=$B3/C3` | La columna del primer terme queda fixada |
| `=B$2+C2` | `=B$2+C3` | La fila del primer terme queda fixada |
| `=raw_population!B2` | `=raw_population!B3` | La fórmula llegeix un altre full i manté la relació entre files |
:::

### La taula rectangular com a objectiu

Per analitzar dades territorials, el full de càlcul s'ha d'acostar al comportament d'una taula de base de dades relacional. Això vol dir una estructura rectangular: una sola fila de capçalera, una variable per columna, una observació per fila i el mateix significat per a totes les cel·les d'una mateixa columna. Aquesta forma permet filtrar, ordenar, calcular, unir amb geometries i exportar sense haver d'interpretar manualment cada bloc.

![Esquema d'una taula rectangular separada de metadades, diccionari i resultats]({{ site.baseurl }}/assets/img/data-sources/rectangular-table.svg "Prepareu la taula d'anàlisi amb una sola capçalera, una fila per municipi i variables en columnes; deixeu metadades, diccionari i resultats en fulls o sortides separades. Esquema d'elaboració pròpia.")

Les taules publicades per a lectura humana sovint no tenen aquesta forma. Poden incloure títols dins del rang, notes al peu, cel·les agrupades, subtotals intercalats, anys en columnes o codis i noms dins de la mateixa cel·la. Aquestes decisions poden facilitar la lectura en pantalla, però compliquen l'anàlisi. La preparació consisteix a transformar-les amb criteri, no a «decorar» el full: les metadades han d'anar al full `sources`, les definicions al `dictionary`, les comprovacions a `checks` i els resultats o indicadors en fulls separats. Si el filtre automàtic no funciona sobre tot el bloc sense seleccionar manualment fragments, la taula encara no és prou rectangular.

### Valor, tipus i format

Un full de càlcul no veu una taula com la veu una persona. Cada cel·la conté un valor que el programa interpreta amb un tipus determinat. Aquest tipus condiciona les operacions possibles, l'ordenació, els filtres, els gràfics i la manera com la dada s'exportarà a altres programes. Per això no n'hi ha prou que una columna «sembli correcta» a la pantalla.

El **valor** és el contingut emmagatzemat; el **tipus** indica com es pot tractar, i el **format** en modifica la presentació sense canviar necessàriament el valor. El nombre `0,25`, per exemple, es pot mostrar com `25%`, però continua sent el mateix valor numèric. Mostrar un nombre amb un decimal no elimina els decimals interns; només n'oculta una part a la pantalla. Aplicar un format numèric al text `25%` tampoc no el converteix automàticament en un nombre vàlid.

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

Un **identificador** és un valor que serveix per reconèixer una entitat dins d'un sistema. Pot identificar una persona, una pàgina web, un correu electrònic, un establiment o un municipi. El seu valor no és que permeti sumar, sinó que permet comprovar si dues files parlen de la mateixa entitat i creuar informació de taules diferents. Si dues pàgines web tinguessin exactament la mateixa URL, o dos comptes actius el mateix correu electrònic dins d'un servei, el sistema no podria decidir a quin objecte es refereix una acció.

Un bon identificador funciona com un contracte. El nom d'una persona pot aparèixer amb accents, abreviatures o ordres diferents, però un DNI té una estructura definida i una lletra de control que es pot validar algorítmicament. De manera semblant, els codis municipals d'Idescat o de l'INE tenen una longitud i una codificació que permeten comprovar formats, detectar errors i unir taules territorials sense dependre només del nom del municipi.

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

### Codis i correspondències entre taules

Moltes pràctiques territorials consisteixen a relacionar taules mitjançant una clau comuna. Una taula pot contenir el codi municipal i la població; una altra, el mateix codi municipal i la comarca; una tercera, el codi i la superfície. La unió només és segura si el codi conserva el mateix sistema, longitud i tipus en totes les fonts. No s'han d'unir taules per la posició de les files, perquè dues descàrregues poden ordenar els municipis de manera diferent.

Un cas habitual és una taula de correspondència o **lookup**: la primera columna conté el codi que es busca i una altra columna conté el valor que es vol recuperar. Si el full `lookup_comarques` té `codi_municipi` a la columna `A` i `codi_comarca` a la columna `B`, una fórmula orientativa per portar el codi de comarca al full de treball és:

```text
=XLOOKUP(A2,lookup_comarques!$A$2:$A$1000,lookup_comarques!$B$2:$B$1000,"sense correspondència")
```

La fórmula busca el valor d'`A2` dins de la columna de codis del full `lookup_comarques` i retorna el valor corresponent de la columna de comarques. Els signes `$` fixen els rangs de cerca i retorn perquè no es moguin quan la fórmula es copiï cap avall.

La lletra de la funció explica part de la seva història. En `VLOOKUP` o `BUSCARV`, la `V` vol dir **vertical**: la funció tradicional busca cap avall a la primera columna d'una taula i retorna una columna indicada per posició. També existeixen variants horitzontals, com `HLOOKUP` o `BUSCARH`, pensades per a taules disposades per files. `XLOOKUP`, que en algunes interfícies traduïdes pot aparèixer com `BUSCARX`, és una funció més recent i general: separa el rang on es busca del rang que es vol retornar, de manera que no obliga a comptar columnes ni a mantenir el valor retornat a la dreta de la clau. Si la versió del programa no disposa d'aquesta funció, es pot usar una alternativa, com `VLOOKUP`, `BUSCARV` o una combinació d'índex i coincidència. L'objectiu no és memoritzar una funció, sinó entendre que es busca una clau en una taula auxiliar i es retorna un camp relacionat.

![Exemple d'una fórmula XLOOKUP que busca un codi municipal i retorna el codi de comarca]({{ site.baseurl }}/assets/img/data-sources/xlookup-example.svg "Llegiu la correspondència d'esquerra a dreta: el codi municipal de la taula de treball es busca a la taula auxiliar i la fórmula retorna el codi de comarca; en copiar-la cap avall, els rangs fixats amb $ continuen apuntant al lookup. Exemple d'elaboració pròpia amb dades simplificades.")

::: table "Controls abans d'una correspondència"
| Control | Pregunta | Risc si no es revisa |
| --- | --- | --- |
| Tipus | Els codis són text en totes dues taules? | Perdre zeros inicials o crear coincidències falses |
| Longitud | Tots els codis tenen el nombre de caràcters esperat? | Barrejar codis municipals, comarcals o provincials |
| Unicitat | La taula de correspondència té una sola fila per codi? | Retornar una coincidència arbitrària o duplicar files |
| Cobertura | Quants codis no troben correspondència? | Excloure municipis sense adonar-se'n |
| Versió | Les dues fonts utilitzen la mateixa classificació territorial? | Unir territoris amb límits o codis incompatibles |
:::

Quan una correspondència falla, no s'ha de corregir el codi per intuïció. Primer cal mirar si hi ha espais invisibles, zeros inicials perduts, codis d'anys diferents, agregats comarcals barrejats amb municipis o topònims que no formen part de la mateixa classificació. Les incidències s'han de comptar i documentar al full `checks`.

### Operacions lògiques i de text

Les fórmules no només calculen nombres. També poden classificar files, netejar text, construir etiquetes i comprovar condicions. Aquestes operacions són útils quan una taula publicada arriba amb codis i noms junts, categories escrites de maneres diferents o camps que necessiten una etiqueta auxiliar abans de filtrar o resumir.

::: table "Operacions de text i condició"
| Necessitat | Fórmula orientativa | Lectura |
| --- | --- | --- |
| Eliminar espais sobrants | <code>=TRIM(B2)</code> | Neteja espais inicials, finals o repetits en un text |
| Obtenir els dos primers caràcters | <code>=LEFT(A2,2)</code> | Permet extreure un prefix, com el codi provincial |
| Construir una etiqueta | <code>=A2&" - "&B2</code> | Uneix codi i nom en un text de lectura |
| Classificar amb una condició | <code>=IF(D2&gt;=10000,"gran","petit")</code> | Assigna una categoria segons un llindar documentat |
| Detectar una absència | <code>=IF(ISBLANK(D2),"revisar","ok")</code> | Marca files que necessiten comprovació |
| Combinar condicions | <code>=IF(AND(D2&gt;0,E2&gt;0),D2/E2,"")</code> | Només calcula si numerador i denominador són vàlids |
:::

Les categories creades amb condicions no són neutrals. Si es decideix que un municipi és «gran» a partir de 10.000 habitants, aquest llindar ha d'estar justificat o, com a mínim, documentat. Una condició pot ajudar a revisar dades, però també pot amagar matisos si converteix una variable contínua en dues etiquetes massa simples.

### Operacions numèriques i arrodoniment

Les operacions numèriques bàsiques del curs no són complicades, però sí que exigeixen coherència. Sumar una població té sentit si totes les files representen municipis compatibles; calcular una densitat exigeix dividir població per superfície; i obtenir un percentatge obliga a identificar quin total fa de denominador. Una fórmula curta pot ser tècnicament correcta i, alhora, respondre una pregunta equivocada si barreja períodes, unitats o escales.

::: table "Operacions numèriques habituals"
| Operació | Fórmula orientativa | Pregunta que resol |
| --- | --- | --- |
| Sumar una columna | <code>=SUM(D2:D23)</code> | Quin total tenen els municipis seleccionats? |
| Calcular una diferència | <code>=D2-C2</code> | Quina variació hi ha entre dues columnes comparables? |
| Calcular un percentatge | <code>=D2/C2*100</code> | Quin pes té una part sobre el total? |
| Calcular una ràtio | <code>=F2/D2</code> | Quantes unitats d'una variable corresponen a una altra? |
| Evitar divisió per zero | <code>=IF(C2=0,"",D2/C2)</code> | La fórmula només calcula si el denominador és vàlid |
| Arrodonir un resultat | <code>=ROUND(D2/C2*100,1)</code> | Quin valor arrodonit es vol comunicar o exportar? |
:::

El format i l'arrodoniment no són el mateix. Si una cel·la conté `12,3456` i es mostra amb un decimal, el valor intern pot continuar sent `12,3456`. Si s'aplica `ROUND(A2,1)`, el resultat calculat passa a ser `12,3`. En general, convé conservar els valors de treball amb precisió suficient i controlar l'arrodoniment només en els resultats que es comuniquen, sempre indicant unitat i criteri. Canviar només el format pot ser adequat per llegir millor una taula; arrodonir amb una fórmula canvia la dada derivada i ha de ser una decisió explícita.

Les mitjanes també demanen criteri. La mitjana simple dels percentatges municipals no equival necessàriament al percentatge comarcal. Per calcular el pes comarcal d'habitatge no principal, cal sumar habitatges no principals i dividir pel total d'habitatges, no fer la mitjana dels percentatges de cada municipi. Aquesta idea es desenvoluparà al capítol 2, però des d'ara cal recordar que una funció estadística només és correcta si la unitat d'observació i el denominador són adequats.

### Operacions amb dates

Una data no és un text decoratiu. Els fulls de càlcul solen desar-la com un nombre de sèrie i aplicar-hi un format de calendari. En molts llibres, aquest nombre representa dies transcorreguts des d'una data d'origen propera a 1900; en altres sistemes informàtics és habitual representar instants com a segons o mil·lisegons transcorreguts des de l'1 de gener de 1970, l'anomenada època Unix. Això permet ordenar, restar dates i sumar durades, però també genera resultats aparentment absurds si es confon el valor intern amb el que es mostra.

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

També es poden classificar dates per obtenir variables auxiliars. Si `A2` conté la data d'una observació, `=WEEKDAY(A2,2)>5` identifica dissabtes i diumenges en moltes aplicacions perquè numera dilluns com a `1` i diumenge com a `7`. `=NETWORKDAYS(A2,B2)` compta dies laborables entre dues dates segons el calendari estàndard de dilluns a divendres; si s'han de tenir en compte festius locals, cal afegir una llista de festius i documentar-la. En una enquesta o recompte de visitants, distingir cap de setmana i dia feiner pot ser més informatiu que treballar només amb la data completa.

::: table "Preguntes freqüents amb dates"
| Pregunta | Fórmula orientativa | Precaució |
| --- | --- | --- |
| Quants dies han passat? | <code>=TODAY()-A2</code> | El resultat ha de ser número, no data |
| Quina edat completa té? | <code>=DATEDIF(A2,TODAY(),"Y")</code> | Depèn de l'aniversari ja complert |
| Quin és l'aniversari d'aquest any? | <code>=DATE(YEAR(TODAY()),MONTH(A2),DAY(A2))</code> | El 29 de febrer requereix revisar el cas en anys no bixests |
| La data cau en cap de setmana? | <code>=WEEKDAY(A2,2)&gt;5</code> | No identifica festius entre setmana |
| Quants dies feiners hi ha entre dues dates? | <code>=NETWORKDAYS(A2,B2)</code> | Els festius locals s'han d'afegir si són rellevants |
:::

>>>> **Escriure una forma ISO no garanteix que la cel·la sigui una data.** Segons l'aplicació i la configuració regional, `2026-04-03` pot importar-se com un valor temporal o quedar com a text. Cal comprovar-ho amb `ISNUMBER`, ordenar una mostra i revisar el format. Dins del llibre convé conservar una data real amb format visible `yyyy-mm-dd`; en un CSV, cal documentar que la columna textual segueix ISO 8601 i tornar-la a interpretar explícitament en importar-la.

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

### Fórmules bàsiques per inspeccionar

Les fórmules següents són útils abans de transformar una taula. Suposen que les dades comencen a la fila 2. No cal aplicar-les totes sempre, però cada taula hauria de tenir controls equivalents per comprovar tipus, files, codis, absències i correspondències.

::: table "Comprovacions inicials amb fórmules"
| Pregunta | Fórmula orientativa | Interpretació |
| --- | --- | --- |
| La cel·la és numèrica? | <code>=ISNUMBER(B2)</code> | Retorna cert si el programa reconeix un nombre |
| La cel·la és text? | <code>=ISTEXT(B2)</code> | Ajuda a detectar nombres o dates importats com a text |
| Quants caràcters té el codi? | <code>=LEN(A2)</code> | Permet comprovar longituds i zeros inicials |
| El codi està duplicat? | <code>=COUNTIF($A$2:$A$100,A2)&gt;1</code> | Marca claus repetides dins del rang |
| El codi té correspondència? | <code>=COUNTIF(lookup!$A$2:$A$1000,A2)&gt;0</code> | Comprova si la clau existeix a la taula auxiliar |
| Quantes cel·les són buides? | <code>=COUNTBLANK(B2:B100)</code> | Quantifica absències, però no n'explica el significat |
| Quants valors són numèrics? | <code>=COUNT(B2:B100)</code> | Es pot contrastar amb el nombre de files esperat |
| Quantes files compleixen una condició? | <code>=COUNTIF(F2:F100,"sense correspondència")</code> | Resumeix incidències que cal revisar |
:::

Els noms de les funcions i el separador d'arguments poden variar. Una configuració pot usar comes i una altra punt i coma; algunes aplicacions tradueixen els noms i d'altres conserven l'anglès. El criteri important és entendre la prova, no memoritzar una única sintaxi de la interfície.

### Models de llenguatge i fulls de càlcul

Alguns fulls de càlcul incorporen assistents basats en LLM i també hi ha extensions que envien instruccions i dades a aquests models per proposar fórmules, resumir taules, classificar textos o respondre preguntes sobre un llibre. Aquestes funcions poden ser útils quan el problema està ben delimitat, especialment per suggerir una fórmula complexa, explicar un error o explorar una columna de text no estructurat. No converteixen, però, una petició ambigua en un mètode fiable.

Un model de llenguatge pot actuar com una caixa negra. Pot generar una fórmula plausible que use un rang equivocat, confondre una absència amb un zero, inventar una categoria o donar respostes diferents davant de peticions semblants. Aquesta tendència a produir respostes inventades o aparentment correctes però falses sovint s'anomena **al·lucinació**. En fulls de càlcul pot aparèixer com una funció que no existeix en l'aplicació utilitzada, una barreja de noms d'Excel i Calc, separadors d'arguments incorrectes, una referència absoluta oblidada o una fórmula que funciona en una fila però falla quan es copia. Si l'extensió envia dades a un servei extern, també cal revisar quina informació es transfereix, amb quines condicions i si el conjunt conté dades personals o restringides.

La validació ha de ser concreta. Abans d'acceptar una fórmula suggerida per un LLM, cal llegir-la, comprovar quins rangs consulta, provar-la en una fila amb resultat conegut, copiar-la a altres files, revisar casos límit i comparar el resultat amb un càlcul manual o una font de control quan sigui possible. Una fórmula que no es pot explicar no s'hauria d'incorporar a la taula analítica.

La reproduïbilitat exigeix saber quina operació s'ha aplicat. Una fórmula visible com `=F2/D2*1000`, una consulta de Power Query o un script versionat es poden inspeccionar i tornar a executar. Una resposta generada en una conversa amb un LLM o un agent no és reproduïble en sentit estricte: guardar dades d'entrada, instrucció, resultat, data, model i comprovacions ajuda a auditar què es va acceptar, però no garanteix que la mateixa eina torni a donar la mateixa resposta.

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

## Activitats: preparar les dades del territori de treball

Tot el recorregut anterior convergeix ara en una primera tasca concreta: preparar la base de dades que alimentarà els indicadors, els gràfics, els mapes i la miniinfografia final. La guia docent situa aquest flux dins de les pràctiques TIC, les proves pràctiques i el producte de síntesi. El capítol d'inici resumeix l'organització general de l'avaluació; Moodle i el professorat indicaran el calendari, el territori de treball i quins fitxers s'han de lliurar en cada moment.

El fil conductor estable del manual serà una diagnosi breu de **població i habitatge d'una comarca tarragonina**. En aquest cas, cada fila representarà un municipi de la comarca i tots els capítols reutilitzaran les mateixes dades. El Tarragonès pot funcionar com a demostració comuna perquè combina una capital, municipis litorals turístics, espais residencials i municipis petits d'interior. En una classe pràctica també es pot començar amb un cas puntual, com Vila-seca, per aprendre a reconèixer codis, files, columnes i valors; aquest exemple de control no substitueix necessàriament el territori assignat per al projecte.

Si el professorat assigna una altra comarca o valida una altra unitat de treball, el criteri és mantenir la coherència durant tot el procés. Una comarca es treballa habitualment amb una fila per municipi; un municipi, si s'utilitza com a territori principal, requeriria una altra unitat d'observació, com barris, seccions censals, equipaments o registres. No s'han de barrejar municipis, barris i equipaments dins d'una mateixa taula analítica com si fossin observacions equivalents.

En la demostració comarcal, la pregunta general serà: **com es distribueixen la població i el parc d'habitatges entre els municipis de la comarca, i quins contrastos territorials s'hi observen?** En aquest capítol encara no es calcularan indicadors ni es produiran figures. Es prepararà una fila coherent per municipi que pugui alimentar els càlculs, gràfics i mapes posteriors.

>>>>> L'activitat produeix un primer paquet de dades territorial preparat per als capítols següents.
>>>>>
>>>>> - Distingir l'exemple de demostració del territori assignat o validat per al projecte.
>>>>> - Descarregar fonts d'Idescat sense modificar els originals.
>>>>> - Separar codi i nom de municipi quan apareixen en una sola cel·la.
>>>>> - Filtrar una comarca amb codis, no només amb noms.
>>>>> - Construir una taula municipal preparada per calcular, representar, cartografiar i sintetitzar.

El resultat mínim és una taula de treball amb tipus de dades correctes, forma rectangular, una sola fila de capçalera, codis municipals conservats com a text, metadades fora del bloc analític i filtres que funcionin sense seleccionar fragments a mà. Aquest objectiu és més important que descarregar moltes taules. La miniinfografia final no comença a Inkscape, sinó aquí: si la base inicial no conserva fonts, codis, unitats i transformacions, els indicadors, gràfics i mapes posteriors no es podran defensar.

::: table "Paquet mínim de dades per municipi"
| Component | Contingut | Font de demostració | Ús posterior |
| --- | --- | --- | --- |
| Identificació territorial | Codi i nom de municipi; codi i nom de comarca | Idescat, Codis territorials i d'entitats | Filtrar la comarca i controlar les unions |
| Població | Total municipal i, en una ampliació, sexe o grans grups d'edat | Idescat, Cens de població i habitatges 2021 | Estructura demogràfica i denominadors |
| Habitatges | Total, principals i no principals | Idescat, Cens de població i habitatges 2021 | Composició del parc residencial |
| Territori | Superfície municipal en km² | Idescat, Indicadors demogràfics i de territori | Densitat de població i context espacial |
:::

Població i habitatges es fixen en 2021 perquè provenen de la mateixa operació censal i són comparables temporalment. Una xifra de població més recent seria útil per a altres preguntes, però barrejar-la sense advertiment amb habitatges de 2021 faria que els quocients ja no descrivissin exactament el mateix moment.

>>>> **Habitatge no principal no significa habitatge turístic.** En aquesta taula, la categoria combina habitatges ocupats ocasionalment i habitatges buits. Pot ajudar a interpretar contrastos residencials i territorials, però no permet afirmar quants habitatges es destinen al turisme. Aquesta relació requeriria una altra font i una definició específica.

### Descarregar manualment les taules d'Idescat

La demostració començarà a la pàgina de cada taula, no en una API. Això obliga a llegir-ne el títol, l'any, les categories, la metodologia i les notes abans de descarregar-la.

Abans de descarregar massivament, és útil seguir un municipi de control. Vila-seca pot servir a l'aula perquè és conegut pel grup i apareix dins del Tarragonès: permet comprovar si el codi municipal, el nom, la comarca, la població i els habitatges arriben correctament a cada pas. Després, la mateixa lògica s'ha d'aplicar a tots els municipis del territori assignat; no s'ha de preparar només el municipi de demostració si el projecte demana una comarca.

1. Obriu [Població. Per sexe i edat any a any](https://www.idescat.cat/pub/?id=censph&n=10&hist=taules%2Fv2%2Fcensph%2F10%2F5975%2Fmun%2Fdata%3FAGE%3DTOTAL%5Ecl%3D1%2C1%2Fc%3D3%2Fr%3D1%2Ft%3D-1c%3B0d%2C1%3B-2c%3B-3c%2Fe%3D0), reviseu que l'any seleccionat sigui **2021**, que el concepte sigui població i que el nivell territorial sigui **municipi**. Si la taula mostra sexe, conserveu el total o documenteu quines columnes s'han triat abans de descarregar.
2. Obriu [Habitatges. Per tipus d'habitatge](https://www.idescat.cat/pub/?id=censph&n=30&lang=ca), manteniu l'any 2021, seleccioneu **tots els municipis** i descarregueu la taula.
3. Descarregueu la taula de [codis de municipis i comarques](https://www.idescat.cat/codis/?id=50&n=9&lang=ca). Aquesta correspondència permet identificar els municipis de la comarca sense filtrar només pel nom.
4. Obriu [Superfície, densitat i entitats singulars](https://www.idescat.cat/pub/?id=inddt&n=396&lang=ca) i descarregueu la superfície municipal disponible.
5. Deseu els fitxers tal com arriben a `data/raw` i registreu-ne l'URL, la data d'accés, l'any de referència i qualsevol selecció aplicada.

>> **La fitxa de fonts també és una dada del projecte.** Una fila del full `sources` ha de permetre entendre quin recurs s'ha usat sense tornar a preguntar-ho oralment: productor, títol exacte, URL de la taula, any o període, data d'accés, llicència, format descarregat i selecció aplicada. Si una descàrrega es pot repetir amb una URL o una API, aquesta adreça completa s'ha de conservar.

Les descàrregues d'Idescat poden arribar com a text separat per punt i coma. S'han d'**importar** amb codificació UTF-8, delimitador `;` i codi municipal com a text. Obrir-les directament amb doble clic pot eliminar zeros inicials o interpretar incorrectament accents, decimals i dates.

En algunes taules, el municipi apareix en una mateixa cel·la amb una forma semblant a `[431711] Vila-seca`. Aquesta presentació és còmoda per llegir, però no és ideal per analitzar. Cal separar el codi i el nom en dues columnes. Es pot fer amb **Text to Columns**, **Text en columnes**, Power Query o fórmules equivalents. El criteri és que `431711` quedi en una columna textual `codi_municipi` i `Vila-seca` en una columna `municipi`, sense claudàtors ni espais sobrants.

>>> **Separar el codi abans de filtrar.** Si una cel·la conté `[431711] Vila-seca`, primer cal obtenir `431711` com a text. Després es pot crear una columna de comprovació amb el prefix provincial, per exemple els dos primers caràcters. En moltes configuracions la fórmula serà `=LEFT(A2,2)` o `=ESQUERRA(A2;2)`, segons idioma i separador d'arguments. El resultat `43` identifica municipis de la província de Tarragona, però no identifica encara una comarca concreta.

La taula de codis conté el codi de comarca. Primer s'incorporarà aquesta correspondència a les altres taules mitjançant el codi municipal de sis dígits; després es filtraran les files de la comarca seleccionada. El prefix provincial `43` no és suficient, perquè inclou tots els municipis de la província de Tarragona.

Si les notes d'una taula censal indiquen arrodoniment, protecció del secret estadístic o una altra regla de difusió, alguna suma de components pot diferir lleugerament del total publicat. Aquesta diferència no s'ha de «corregir» repartint-la manualment: s'ha de conservar i documentar.

### Descarregar i preservar els originals

Les dades descarregades rarament es poden analitzar de manera immediata. Poden contenir títols dins de la taula, capçaleres dobles, notes al peu, totals barrejats amb territoris, codis convertits en nombres, símbols de confidencialitat, decimals interpretats com a text o una estructura pensada per a lectura humana i no per al càlcul.

La preparació no és una operació mecànica que «neteja» qualsevol irregularitat. Cada canvi implica una decisió sobre el significat de les dades. El procés ha de separar els errors corregibles dels valors desconeguts i de les diferències conceptuals que no es poden harmonitzar legítimament.

![Cadena de preparació de dades]({{ site.baseurl }}/assets/diagrams/data-preparation-pipeline.mmd "Conserveu cada pas de preparació: còpia original, importació, neteja, normalització, validació, taula analítica i productes finals han de poder relacionar-se entre si.")

### Eines de preparació segons el problema

No hi ha una única eina de preparació. L'elecció depèn del volum, la complexitat, la necessitat de repetir els passos i el tipus de dada.

::: table "Eines habituals per preparar dades"
| Família | Exemples | Ús adequat | Límit que cal vigilar |
| --- | --- | --- | --- |
| Full de càlcul | Aplicació compatible acordada a l'inici del curs | Inspecció, fórmules, taules dinàmiques i transformacions de volum moderat | Canvis manuals difícils de rastrejar, conversions automàtiques i diferències de compatibilitat |
| Transformació visual | Power Query, OpenRefine | Passos repetibles, remodelació, normalització de text i correspondències | Cal conservar i documentar la seqüència aplicada |
| Programació | Python amb pandas; R amb readr o dplyr | Automatització, grans volums, validacions i processos repetits | Requereix codi, dependències i versions documentades |
:::

En aquest primer bloc, les operacions s'explicaran segons el funcionament comú dels fulls de càlcul i amb l'aplicació acordada a l'inici del curs. Les biblioteques de Python o R no seran un requisit general, però permeten entendre com pot evolucionar el procés quan una transformació s'ha de repetir moltes vegades o deixa de ser segura manualment. Les eines cartogràfiques s'introduiran més endavant, quan les taules ja estiguin preparades.

### Construir una taula analitzable

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

L'estructura proposada separa `data/raw` de `data/processed`. Tot el treball tabular es farà en **un únic llibre**, amb un nom que identifiqui el territori de treball, com `territorial_context_tarragones.xlsx` en la demostració comarcal. No es crearà un llibre per a cada font ni còpies com `final2.xlsx`. Dins del llibre, els noms dels fulls han de seguir el mateix criteri que els noms de fitxers: han de dir quina unitat treballen, si són originals importats, taules preparades, indicadors o gràfics.

::: table "Fulls del llibre acumulatiu"
| Full | Funció |
| --- | --- |
| `project` | Pregunta, territori, autoria, aplicació, configuració regional i ubicació de treball |
| `sources` | Productor, taula, URL, any, data d'accés, llicència i notes |
| `dictionary` | Camp, definició, tipus, unitat, font i tractament d'absències |
| `raw_municipal` | Còpia importada de codis, comarca, municipi, superfície i altres camps territorials de base |
| `raw_population` | Còpia importada de la taula de població de 2021, si arriba separada de la base municipal |
| `raw_housing` | Còpia importada de la taula d'habitatges de 2021 |
| `checks` | Recompte de files, duplicats, absències, sumes i incidències |
| `municipal` | Taula preparada per a l'anàlisi, amb una fila per municipi i variables de base |
| `indicators_municipal` | Indicadors calculats només amb variables municipals de base, com densitats o controls territorials |
| `indicators_municipal_housing` | Indicadors que creuen municipis, població i habitatge, amb fórmules visibles |
| `plots_municipal_housing` | Taules auxiliars i gràfics editables derivats dels indicadors de població i habitatge |
| `map_export` | Taula plana que es reutilitzarà més endavant als mapes |
:::

Els fulls `raw_*` no se sobreescriuran amb correccions manuals. Els fulls següents es construiran copiant per referència, amb fórmules, consultes o passos documentats, de manera que una cel·la de `municipal` pugui apuntar a `raw_municipal`, i un indicador de `indicators_municipal_housing` pugui apuntar a `municipal` i `raw_housing` sense trencar la traça. Si cal corregir un valor, no s'ha de substituir silenciosament: cal afegir una columna de tractament, una regla explícita o una nota al diccionari i a `checks`. Aquest flux és més complex que copiar i enganxar valors, però és el procediment més reproduïble que es pot aconseguir amb fulls de càlcul sense passar encara a programació.

### Fer la inspecció inicial amb el full de càlcul

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

### Validar les dades després de transformar-les

Cada transformació ha de tenir una comprovació. Si es remodela una taula, s'ha de verificar que no s'han perdut valors. Si s'eliminen duplicats, cal explicar per què eren duplicats i no observacions legítimes. Si s'uneixen fonts, s'han de comptar coincidències i absències. Si es calcula un total, s'ha de contrastar amb una publicació de referència quan sigui possible.

Una taula preparada no és necessàriament correcta perquè Excel no mostri errors. La validació combina controls tècnics, comparació amb la font i judici substantiu sobre valors plausibles.

### Preparar i auditar la taula municipal

Les quatre descàrregues no formen encara una taula analítica. Poden ordenar els municipis de manera diferent, anomenar els camps amb capçaleres de publicació i barrejar totals amb components. La preparació haurà d'obtenir una única fila per municipi sense copiar valors a mà ni unir les fonts per posició de fila.

**1. Documentar les fonts.** Es registrarà per a cada taula el productor, el títol exacte, la metodologia, el període, la unitat, la cobertura, la data d'accés i la llicència. La fitxa inclourà l'URL de la taula, no només la portada d'Idescat.

**2. Diagnosticar sense corregir.** Es descriurà la unitat d'observació, s'identificarà la clau territorial i es construiran controls de files, valors absents, duplicats i rangs. Els problemes es classificaran com a errors de format, possibles errors de contingut o diferències conceptuals.

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

**3. Transformar amb rastre.** La versió preparada no substituirà l'original. El llibre distingirà les dades rebudes, el diccionari, les comprovacions i el full `municipal`. Es conservaran els codis com a text, es filtraran els municipis mitjançant el codi de comarca i es documentaran els valors no numèrics.

**4. Validar.** La taula final haurà de superar quatre controls: nombre justificat de files, clau territorial sense duplicats inesperats, valors dins de rangs plausibles i correspondència amb un total o resultat publicat.

### Evidències de la preparació que s'han de conservar

La guia docent preveu activitats de laboratori, proves pràctiques i una presentació o producte de síntesi. Per això aquesta activitat ha de deixar preparades evidències revisables del procés, tant per al treball de síntesi en equip com per a les proves o recuperacions individuals, encara que Moodle indiqui quines s'han de trametre en cada moment:

::: table "Evidències de la preparació territorial"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| Arrel | `README.md` | Territori assignat, pregunta, fonts, llicències, dates i estructura del projecte |
| `data/raw` | Fitxers originals | Descàrregues sense modificar i, si escau, URL o consulta de l'API |
| `data/processed` | Un únic llibre de treball | Fulls descrits al model acumulatiu, sense llibres paral·lels |
| `data/processed` | `municipal` | Una fila per municipi, codis com a text, unitats explícites i valors absents documentats |
| `data/processed` | Registre de transformacions | Regles aplicades, correspondències i incidències no resoltes |
:::

La carpeta `outputs` encara no ha de contenir la infografia final. Les figures que es generin al capítol 3 s'hi desaran com a resultats intermedis reutilitzables; els mapes s'afegiran després des de QGIS, i el document final de síntesi s'exportarà més endavant a `dist`. Aquesta separació ajuda a no confondre una activitat de preparació amb el producte final, però també deixa clar que el producte final dependrà de la qualitat d'aquesta base.

El resultat final d'aquest capítol serà una base territorial depurada, normalment comarcal i amb una fila per municipi, amb codis consistents i camps preparats per calcular indicadors. La competència principal no és descarregar molts fitxers, sinó construir una cadena d'evidència defensable: pregunta, productor, definició, selecció, còpia original, transformacions i validació.

Aquest és el primer pas del cicle de descobriment de coneixement territorial. Encara no s'han calculat indicadors, no s'han fet gràfics ni s'han elaborat mapes, però ja s'ha decidit què s'observa, d'on surt la informació i com es conserva el rastre de cada decisió. Els capítols següents treballaran sobre aquesta base: primer per calcular i interpretar indicadors, després per representar-los visualment i cartogràficament, i finalment per convertir-los en una síntesi territorial argumentada.
