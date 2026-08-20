---
layout: manual-chapter
title: Indicadors territorials i turístics
description: Construcció, usos i interpretació d'indicadors per descriure, comparar, comunicar i orientar decisions territorials.
lang: ca
ref: manual-territorial-indicators
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/indicadors-territorials/
weight: 30
part: Continguts
manual_references: true
---

Un indicador condensa dades per fer visible una situació, una diferència o una evolució que interessa comprendre. Pot ajudar a explicar a la ciutadania com canvia una comarca, permetre que una administració segueixi un objectiu, orientar la gestió d'una destinació o formular una pregunta de recerca. Quan exigeix un càlcul, l'operació és un mitjà i no la finalitat: la utilitat apareix quan la mesura es relaciona amb una pregunta, un territori, un període, un públic i una decisió.

Aquest capítol amplia, per tant, la dimensió pràctica del llibre comarcal. Abans de calcular percentatges, ràtios i densitats, situa els indicadors dins de sistemes oficials, quadres de comandament i estudis científics. Després examina com es dissenyen i interpreten, i finalment aplica aquests criteris a la població i l'habitatge dels municipis del Tarragonès.

>>>>> En acabar el capítol, cal poder dissenyar, calcular, interpretar i validar indicadors territorials coherents amb una pregunta i amb les dades disponibles.
>>>>>
>>>>> - Explicar què representa un indicador i quins límits imposen la definició, l'escala, el període i la cobertura.
>>>>> - Distingir les funcions dels sistemes oficials, els estudis de recerca i els quadres de comandament.
>>>>> - Distingir mesura, indicador simple, indicador compost i indicador indirecte, i validar-ne la relació amb el fenomen d'interès.
>>>>> - Justificar el numerador, el denominador, la unitat i el factor d'escala d'una mesura útil.
>>>>> - Calcular indicadors municipals i agregats comarcals reproduïbles als fulls `indicators_demography`, `indicators_housing` i `indicators_summary`.
>>>>> - Interpretar patrons, contrastos i casos extrems sense presentar-los com a causes demostrades.
>>>>> - Validar fórmules, compatibilitat, cobertura, absències i resultats abans de documentar-los.

## Estadística i comunicació de dades

Els indicadors no es poden entendre del tot al marge de l'estadística, però tampoc no es poden confondre amb ella. Abans de calcular el primer percentatge, cal situar què fa l'estadística, què fa aquesta assignatura i on passa la frontera entre l'una i l'altra. Aquesta frontera és doblement útil: ajuda a reconèixer què es pot afirmar amb un indicador i evita que un curs de visualització de dades es converteixi en una repetició de les assignatures d'estadística i de tècniques quantitatives que l'estudiant ja ha cursat o cursa.

L'estadística es pot dividir, de manera esquemàtica i prou acurada per a aquest curs, en dos grans blocs. L'estadística **descriptiva** organitza, resumeix i representa les dades observades: calcula percentatges, ràtios, mitjanes, dispersions i associacions, i les mostra en taules, gràfics i mapes. L'estadística **inferencial**, en canvi, va més enllà del conjunt observat: a partir d'una mostra estima paràmetres de la població, construeix intervals de confiança i contrasta hipòtesis. Les dues responen preguntes diferents i exigeixen requisits diferents.

>>>>> En acabar la secció, cal poder situar la comunicació de dades dins de l'estadística i explicar què fa i què no fa aquesta assignatura.
>>>>>
>>>>> - Distingir l'estadística descriptiva de la inferencial i posar-hi exemples concrets.
>>>>> - Explicar per què els indicadors del llibre comarcal són estadística descriptiva.
>>>>> - Justificar la complementarietat d'aquest curs amb les assignatures d'estadística i de tècniques quantitatives.
>>>>> - Reconèixer les afirmacions que un indicador descriptiu pot sostenir i les que exigeixen inferència.

### Estadística descriptiva i inferencial

La diferència entre descriure i inferir és el primer vocabulari estadístic que ha de dominar qui es dedica a visualitzar dades, perquè molts errors d'interpretació neixen de creure que descriure equival a demostrar. Els indicadors del llibre comarcal —percentatges, ràtios i densitats— són estadística descriptiva: resumeixen i posen en relació el conjunt de municipis observats. Quan es calcula el percentatge d'habitatge no principal del Tarragonès i es comparen els municipis entre si, no es fa cap afirmació sobre territoris que no són al llibre: es descriu i es compara la informació disponible. Per això l'estadística descriptiva no necessita mostres: treballa amb els casos observats o amb aquells que s'han pogut registrar.

L'estadística inferencial és una altra manera de treballar. Quan només es disposa d'una mostra i es vol dir alguna cosa sobre la població sencera —per exemple, quan una enquesta de pocs milers de llars pretén estimar la despesa turística de la regió— cal dissenyar la mostra amb un procediment conegut, assumir un model de probabilitat i quantificar la incertesa amb intervals de confiança i contrastos d'hipòtesis. El resultat no és un valor únic, sinó un valor amb una incertesa associada, i la seva validesa depèn del mostreig i dels supòsits del model.

::: table "Dues branques de l'estadística i què fan"
| | Estadística descriptiva | Estadística inferencial |
| --- | --- | --- |
| Pregunta que respon | Què mostren les dades observades? | Què es pot afirmar sobre una població més àmplia a partir d'una mostra? |
| Materials | Conjunt de casos observat: municipis, sèries, registres disponibles | Mostra obtinguda amb un procediment conegut i un model de probabilitat |
| Operacions típiques | Percentatges, ràtios, mitjanes, dispersió, associacions, taules, gràfics, mapes | Estimació de paràmetres, intervals de confiança, contrast d'hipòtesis |
| Producte habitual | Descripció i comparació d'un territori o d'un període | Afirmació sobre el conjunt més ampli, amb incertesa quantificada |
| En aquesta assignatura | És el punt de partida habitual | No és l'objectiu del curs |
:::

Aquesta taula no ordena les dues branques per importància: cada una respon una pregunta i imposa les seves precaucions. El manual se centra en la part descriptiva i, sobretot, en la comunicació visual del resultat. Per a una introducció sistemàtica als mètodes estadístics de les ciències socials, des de la descripció fins a la inferència, es pot consultar el manual d'Agresti i Finlay {% cite agrestiStatisticalMethodsSocial2009 %}.

### Una assignatura complementària a les tècniques quantitatives

Aquest manual no pretén ensenyar estadística de nou ni substituir les assignatures que l'estudiant ja té. Les assignatures d'estadística i de tècniques quantitatives ensenyen a calcular i validar mesures, a estimar, a contrastar hipòtesis i a quantificar la incertesa amb rigor. Aquesta assignatura se centra en una altra feina, complementària i posterior: decidir què es representa, com es codifica visualment, per a qui es fa i amb quins límits, a partir d'indicadors i de resultats que ja s'haurien de poder llegir críticament.

La complementarietat es pot resumir amb dues preguntes. A una assignatura d'estadística es pregunta «Què es pot inferir d'aquestes dades i amb quina incertesa?». En aquesta assignatura es pregunta «Aquesta representació permet una lectura honesta, comparable i clara del que mostren les dades?». Les dues preguntes no competeixen: un resultat ben calculat es pot comunicar malament, i una representació clara no arregla una inferència mal feta. El curs treballa la segona i suposa que la primera s'estudia en paral·lel.

>> **La tria d'un percentatge, el denominador, les classes d'un mapa o les etiquetes d'un gràfic no són decoració, sinó decisions que determinen què pot llegir el públic.** L'estadística descriptiva i la seva comunicació són, en aquest sentit, una mateixa feina d'honestedat: explicar què s'ha fet i què no permet dir el resultat.

## Per què es construeixen indicadors

Les dades originals acostumen a descriure observacions concretes: persones residents, habitatges, pernoctacions, places d'allotjament o superfície. Aquestes magnituds són indispensables, però una pregunta territorial sol exigir alguna transformació. El nombre d'habitatges no principals informa del volum; el seu percentatge dins del parc residencial informa de composició. La població informa de grandària; els habitants per quilòmetre quadrat informen de concentració.

Construir un indicador significa seleccionar alguns aspectes de la realitat i deixar-ne altres fora. Aquesta reducció és útil perquè facilita la lectura, però també comporta responsabilitat. Un indicador no és el fenomen mateix ni una explicació completa: és una representació dissenyada per observar-ne una dimensió. La definició, el numerador, el denominador, la unitat, l'escala territorial i el període determinen què es pot afirmar.

### Divulgació i rendició de comptes

Els indicadors permeten comunicar fenòmens complexos mitjançant una mesura definida i comparable. Una infografia, una notícia estadística o un perfil municipal poden presentar pocs valors de capçalera perquè el públic identifiqui ordres de magnitud i contrastos. Aquesta simplificació només és informativa si el títol, la unitat, el període i la font continuen visibles.

El marc global dels [Objectius de desenvolupament sostenible](https://unstats.un.org/sdgs/indicators/indicators-list/) mostra aquesta funció. Objectius polítics amplis es concreten en indicadors sotmesos a definicions i metadades comunes per fer-ne seguiment i informar del progrés. En turisme, l'indicador 8.9.1 mesura el PIB directe turístic com a proporció del PIB total i la seva taxa de creixement, mentre que altres mesures observen aspectes ambientals o institucionals. Cap indicador individual equival a «turisme sostenible»; el sistema obliga a distingir dimensions i a reconèixer què queda sense mesurar.

A escala catalana, [El municipi en xifres](https://www.idescat.cat/emex/) de l'Idescat reuneix dades bàsiques d'un municipi i les compara amb la comarca i Catalunya. El servei combina població, habitatge, economia, turisme i medi ambient en un perfil accessible, i ofereix una API perquè la informació es pugui integrar en altres serveis. La comparació és útil per a divulgació i diagnosi local, però els indicadors poden tenir anys de referència diferents i no tots estan disponibles als municipis petits.

### Seguiment i presa de decisions

Un indicador també pot actuar com a senyal de seguiment. Una destinació pot observar l'estacionalitat, la satisfacció de residents i visitants, l'ocupació, la despesa, el consum d'aigua o la generació de residus per detectar canvis, discutir prioritats i valorar si una intervenció avança en la direcció prevista. La decisió no surt automàticament del número: requereix objectius, llindars, recursos, coneixement local i deliberació.

El sistema europeu ETIS es va concebre com una eina local de gestió, informació i seguiment de destinacions. Organitza indicadors de gestió, valor econòmic, impacte social i cultural i impacte ambiental, i proposa que els actors de la destinació participin en la recollida i lectura de dades {% cite europeanCommissionETIS2016 %}. Aquesta orientació és important: un sistema d'indicadors no és només una classificació externa ni un rànquing, sinó una infraestructura per establir una línia de base, detectar problemes i observar canvis.

La recerca ha estudiat la mateixa qüestió a escala municipal. Torres-Delgado i López Palomeque van desenvolupar una proposta per mesurar la sostenibilitat turística dels municipis, mostrant tant la utilitat de l'escala local com les dificultats de seleccionar, normalitzar i combinar indicadors amb dades disponibles {% cite torresDelgadoMeasuringSustainableTourism2014 %}. Altres treballs han aplicat quadres d'indicadors a la planificació turística espanyola i han analitzat com poden connectar estratègia, objectius i seguiment {% cite vilaCreationUseScorecards2010 %}.

UN Tourism ha impulsat un marc estadístic que relaciona les dimensions econòmica, ambiental i social del turisme mitjançant definicions i estructures comptables compatibles. Les experiències pilot van mostrar que aquests sistemes poden produir informació per a gestors de destinacions i responsables de polítiques, però també que la disponibilitat i l'atribució de dades ambientals i socials són especialment exigents a escala subestatal {% cite unTourismSustainabilityPilots2022 %}. Aquest desenvolupament ha culminat en el *Statistical Framework for Measuring the Sustainability of Tourism*, avalat per la Comissió d'Estadística de les Nacions Unides el 2024 com a marc internacional per organitzar les dependències i els impactes econòmics, ambientals i socials del turisme {% cite unTourismStatisticalFrameworkMST2024 %}.

### Exploració, recerca i generació d'hipòtesis

Els indicadors permeten comparar territoris, períodes i dimensions, i poden revelar casos que mereixen una investigació més detallada. Un municipi amb una densitat molt alta, una estructura d'edats singular o un percentatge elevat d'habitatge no principal planteja preguntes sobre la seva forma urbana, la història demogràfica, la funció residencial o la relació amb el turisme. El valor no confirma cap d'aquestes explicacions, però ajuda a localitzar on cal buscar evidències noves.

Aquesta funció exploratòria connecta amb el procés de descobriment de coneixement presentat a l'orientació del manual {% cite fayyadDataMiningKnowledge1996 %}. Les dades se seleccionen i preparen; els indicadors construeixen representacions analítiques; els gràfics i mapes permeten examinar patrons; i la interpretació contrasta aquests patrons amb definicions, context territorial i altres fonts. El resultat pot ser una descripció sòlida o una hipòtesi raonable, no necessàriament un descobriment científic nou.

## Tipus, construcció i validesa dels indicadors

No qualsevol número és un indicador ni tots els indicadors es construeixen igual. Abans de calcular o reutilitzar un valor convé separar com s'ha mesurat, quina regla permet comparar-lo, si combina diverses dimensions i fins a quin punt observa directament el fenomen que es vol interpretar. Aquest vocabulari ajuda a justificar la construcció i a no atribuir a les dades més significat del que poden sostenir.

>>>>> En acabar la secció, cal poder classificar la construcció d'un indicador i justificar si aporta una representació vàlida del fenomen d'interès.
>>>>>
>>>>> - Distingir mesurament, mesura, mètrica i indicador segons la funció que compleixen.
>>>>> - Classificar un indicador com a simple o compost a partir de la seva construcció.
>>>>> - Distingir una mesura directa d'un indicador indirecte i explicar què substitueix aquest darrer.
>>>>> - Justificar la validesa d'un indicador amb evidència adequada a la pregunta, el lloc i el període.
>>>>> - Identificar les decisions de ponderació i explicar per què una anàlisi de sensibilitat és necessària per comprovar-ne l'efecte.

### Mesures, mètriques i indicadors simples

En aquest capítol, el **mesurament** és el procés d'observar o assignar valors segons un procediment; la **mesura** n'és el resultat, expressat amb una unitat o una escala i una cobertura definides. Utilitzarem **mètrica** per referir-nos a la regla o escala amb què es quantifica i es compara una propietat, no com a sinònim genèric de qualsevol número. Un **indicador** és una mesura seleccionada i interpretada en relació amb una pregunta i un ús: la població resident és una mesura, però pot actuar com a indicador de grandària demogràfica dins d'una diagnosi territorial.

Un indicador simple prové d'una variable o d'una relació transparent entre poques variables. No ha de ser un recompte: també pot ser un percentatge, una taxa, una ràtio o una densitat. L'Idescat utilitza l'expressió [indicadors bàsics](https://www.idescat.cat/indicadors/) per reunir valors de síntesi sobre població, economia, societat i territori; aquí «bàsics» descriu la selecció del servei i no és un sinònim tècnic d'«indicadors simples». Per consultar terminologia especialitzada en català es pot recórrer al [Cercaterm del TERMCAT](https://www.termcat.cat/ca/cercaterm), però la definició operativa de cada indicador ha de provenir sempre de les seves metadades.

::: table "Mesures i construccions d'indicadors"
| Concepte | Què representa | Exemple | Risc principal |
| --- | --- | --- | --- |
| Mesura | Resultat d'un mesurament amb unitat i cobertura | 25.000 pernoctacions registrades | Confondre el valor observat amb tot el fenomen |
| Mètrica | Regla o escala que permet quantificar o comparar | distància en quilòmetres per la xarxa viària | Aplicar una regla inadequada a la pregunta |
| Indicador simple | Mesura seleccionada o relació transparent entre variables | pernoctacions per 1.000 habitants | Ometre el denominador, el període o la cobertura |
| Indicador compost, sovint resumit en un índex sintètic | Agregació de diversos indicadors o dimensions | índex socioeconòmic territorial | Ocultar selecció, normalització i pesos |
| Indicador indirecte (*proxy*) | Variable observable usada en lloc del fenomen d'interès | radiància nocturna com a aproximació d'activitat humana | Confondre correlació contextual amb validesa |
:::

### Indicadors compostos i índexs sintètics

Un indicador compost, sovint presentat com un índex sintètic, agrega diversos indicadors per representar dimensions que un sol valor no recull. La construcció exigeix decidir quines variables entren, en quina direcció contribueixen, com es normalitzen o estandarditzen per fer-les comparables, quins pesos reben, com s'agreguen i com es tracten les dades absents. Els pesos iguals continuen sent pesos: assignen el mateix coeficient nominal a totes les parts, però no garanteixen la mateixa influència efectiva si els components tenen variàncies o correlacions diferents.

El nom **índex** no implica per si sol una construcció composta. L'índex d'envelliment que es calcularà més endavant és una ràtio simple entre població de 65 anys o més i població de 0 a 14 anys; un índex sintètic, en canvi, resumeix diversos indicadors o dimensions després de prendre decisions de normalització, ponderació i agregació.

Aquestes opcions s'han de documentar. L'anàlisi de sensibilitat comprova l'efecte de canviar pesos, normalització, imputació o agregació; l'anàlisi d'incertesa estima com la incertesa de les dades i dels supòsits es transmet al resultat. Si petits canvis alteren molt el rànquing, el resultat és fràgil. El manual de l'OCDE i el JRC ordena aquest procés i insisteix que la qualitat depèn tant del marc conceptual com de les operacions estadístiques {% cite nardoCompositeIndicators2008 %}. L'[Índex socioeconòmic territorial](https://www.idescat.cat/pub/?id=ist) de l'Idescat n'és un exemple proper: combina informació sobre situació laboral, nivell educatiu, immigració i renda per resumir diferències socioeconòmiques territorials.

Un repertori o un quadre de comandament no es converteix automàticament en un indicador compost perquè mostri molts valors alhora. Si les dimensions impliquen objectius en tensió, tenen incerteses diferents o necessiten decisions específiques, un quadre de comandament pot ser preferible a un índex únic: conserva cada indicador visible i evita que una compensació matemàtica amagui un problema rellevant. Un índex pot ser útil per a una síntesi justificada i estable, però no ha de substituir la lectura dels seus components.

### Indicadors indirectes o proxies

Un **indicador indirecte (*proxy*)**, que després anomenarem indicador indirecte, és una variable observable emprada com a substitut d'un fenomen que no es pot observar directament o amb la mateixa cobertura. «Directe o indirecte» i «simple o compost» són eixos independents: una mesura directa pot formar part d'un índex compost, i un indicador indirecte pot ser un únic recompte o una combinació de traces.

La **validesa de constructe** exigeix evidència que l'indicador representa la dimensió definida i no principalment una altra. En un indicador indirecte, aquesta evidència pot incloure un mecanisme teòric plausible, comparacions amb mesures directes o independents, convergència amb altres fonts i comprovacions en diversos llocs, períodes i grups. Una associació pot aparèixer per factors de confusió i desaparèixer quan canvien la tecnologia, les institucions o els comportaments; la correlació favorable aporta evidència, però no valida per si sola qualsevol interpretació o ús.

>>>> **No disposar de la dada directa no autoritza a utilitzar qualsevol traça disponible que hi estigui correlacionada.** Sense una relació conceptual plausible, validació externa i límits explícits, l'indicador indirecte pot descriure una altra realitat i conduir a conclusions errònies.

Les llums nocturnes permeten entendre aquesta precaució. L'instrument **Visible Infrared Imaging Radiometer Suite** (VIIRS) incorpora la **Day/Night Band**. Els [EOG VNL](https://eogdata.mines.edu/products/vnl/) resumeixen observacions de radiància de la DNB, mentre que la suite [NASA Black Marble](https://viirsland.gsfc.nasa.gov/Products/NASA/BlackMarble.html) inclou productes amb correccions d'atmosfera, llum lunar, terreny i altres efectes. No mesuren directament el PIB, els turistes ni el consum elèctric. Alguns productes de radiància composta es distribueixen en una graella de 15 segons d'arc, aproximadament 500 m a l'equador, però la petjada de la DNB és d'uns 750 m al nadir. Una font puntual prou intensa pot ser detectable, però no es pot atribuir automàticament una cel·la o una emissió a un establiment concret.

Amb validació externa, aquesta radiància pot actuar com a indicador indirecte de concentracions àmplies d'activitat humana, econòmica o nocturna i, en contextos concrets, d'activitat relacionada amb el turisme {% cite levinRemoteSensingNightLights2020 %}. La interpretació ha de considerar núvols i cobertura d'observacions; lluna, llum paràsita i processament del producte; incendis, embarcacions i torxes de gas; electrificació i canvi espectral dels LED; possible infrarepresentació del turisme rural, de natura o d'altres activitats amb poca il·luminació artificial; agregació espacial i halos lluminosos; i dependència del context.

Un altre exemple és l'estudi de Fraile-Jurado i Fernández-Díaz a Sevilla. Entre el 18 i el 20 de desembre de 2017, els autors van comptar manualment banderes d'Espanya i estendards del Nen Jesús visibles en 152 carrers, seleccionats com aproximadament el 5% dels carrers de cada districte; després d'excloure carrers amb menys de cinc habitatges, l'anàlisi va conservar 132 casos. Els recomptes, 1.178 banderes i 578 estendards, es van expressar per habitant i per habitatge, i cada carrer es va relacionar amb els resultats agregats de les meses d'un col·legi electoral a les eleccions andaluses del 2 de desembre de 2018 {% cite fraileJuradoBanderasSevilla2019 %}. La crisi catalana formava part del context polític, però l'àrea d'estudi era Sevilla.

Comptar aquests elements és un recompte espacial directe dels símbols visibles; només esdevé un indicador indirecte quan s'utilitza per aproximar expressió simbòlica, identitat, ideologia o vot. Les correlacions electorals eren modestes i requereixen una lectura limitada. Hi intervenen la fal·làcia ecològica, el desajust temporal, la diferència entre banderes i llars, el biaix de visibilitat i expressió, la possible imitació veïnal i l'assignació de resultats electorals agregats a carrers que no coincideixen exactament amb les meses. La interpolació per veí més pròxim es va utilitzar per visualitzar el patró i va produir artefactes reconeguts pels autors, però no va generar les correlacions. Geolocalitzar l'observació enriqueix l'anàlisi territorial; no valida per si sol què significa.

La condició directa o indirecta tampoc depèn de si la dada és espacial. VIIRS i les observacions als balcons són espacials perquè estan georeferenciades. El consum, les transaccions amb targeta, les enquestes o les cerques web poden arribar com a agregats no espacials o esdevenir espacials quan s'assignen a llocs. La georeferenciació permet estudiar distribucions i contextos; no demostra que una traça representi el fenomen proposat.

## Sistemes oficials, recerca i quadres de comandament

Els indicadors rarament apareixen sols. Formen sistemes perquè una realitat territorial o turística té diverses dimensions i perquè cada públic necessita una forma de consulta. Una publicació estadística pot explicar una tendència mitjançant text i figures; un quadre de comandament facilita filtres i actualitzacions; un sistema de planificació relaciona indicadors amb objectius; i un article científic fa explícita la metodologia per poder discutir-la i reproduir-la.

>>>>> La comparació entre sistemes permet decidir què es pot reutilitzar i quines comprovacions exigeix cada entorn.
>>>>>
>>>>> - Comparar la finalitat, l'escala i el grau de documentació d'un sistema oficial, un estudi científic i un quadre de comandament.
>>>>> - Distingir una interfície de consulta, una font de dades i un sistema d'indicadors.
>>>>> - Interpretar com els denominadors, les dimensions i l'harmonització modifiquen la lectura d'un fenomen.
>>>>> - Validar definició, productor, període, unitat, cobertura i metodologia abans de reutilitzar un valor.

::: table "Exemples d'ús d'indicadors territorials i turístics"
| Exemple | Escala i contingut | Utilitat principal | Precaució de lectura |
| --- | --- | --- | --- |
| [Indicadors ODS](https://unstats.un.org/sdgs/indicators/indicators-list/) | Global i estatal; marc multidimensional de desenvolupament | Seguiment públic i rendició de comptes | Un objectiu ampli no queda explicat per una sola mesura |
| [El municipi en xifres](https://www.idescat.cat/emex/) | Municipis de Catalunya; població, habitatge, economia, turisme i medi ambient | Perfil territorial, comparació i divulgació | Anys de referència i disponibilitat variables |
| [Eurostat: turisme regional](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Tourism_statistics_at_regional_level) | Regions europees; pernoctacions, estacionalitat, intensitat i densitat | Comparació regional i comunicació de pressions turístiques | La intensitat i la densitat responen preguntes diferents i tenen cobertures incompletes |
| [Dataestur](https://www.dataestur.es/) | Espanya i destinacions; demanda, despesa, allotjament, transport, ocupació i sostenibilitat | Seguiment conjuntural i intel·ligència turística | Agrega fonts amb metodologies, freqüències i escales diferents |
| [UN Tourism Data Dashboard](https://www.unwto.org/tourism-data/un-tourism-tourism-dashboard) | Mundial, regional i estatal; arribades, ingressos, estacionalitat i contribució econòmica | Seguiment internacional i divulgació | Els agregats estatals oculten diferències internes |
| ETIS | Destinació; economia, societat, cultura, medi ambient i gestió | Diagnosi participada i gestió sostenible | L'adaptació local limita la comparació estricta entre destinacions |
| GCSD | Costa mundial en graelles d'1 km; pressions, medi i recursos, societat | Recerca reproduïble, integració de dades i diagnosi costanera | La graella comuna no iguala la resolució, el període ni la incertesa de les fonts originals |
:::

### Un sistema científic d'indicadors costaners

La base GCSD constitueix un exemple especialment útil per a una assignatura que relaciona turisme, territori i informació geogràfica. Zuo i col·laboradors no parteixen d'un únic índex de sostenibilitat: defineixen tres dimensions —pressions costaneres, medi i recursos, i societat—, les despleguen en dotze subdimensions i seleccionen 65 indicadors derivats de 68 conjunts de dades obertes {% cite zuoGCSDCoastalIndicators2025 %}. Entre les mesures hi ha pressions climàtiques i humanes, ecosistemes, cobertes del sòl, infraestructura, població, activitat econòmica, energia, aigua i densitat turística costanera.

El procés de construcció és tan important com el catàleg final. Els autors revisen la bibliografia, estableixen criteris de selecció, comparen resolució, exactitud, cobertura i actualitat de les fonts, i transformen les dades a una graella costanera comuna. Aquesta seqüència mostra que un sistema d'indicadors és també un problema d'integració geogràfica i de documentació: abans de comparar cal decidir què representa la costa, quina unitat espacial s'utilitza i com es tracten els punts, les línies i els ràsters.

La base comuna d'1 km facilita l'anàlisi conjunta, però no converteix totes les fonts en observacions d'1 km. Alguns valors originals provenen de productes més grossos i s'assignen a cel·les menors sota determinats supòsits; les cobertures temporals tampoc no són idèntiques. GCSD serveix, per tant, per discutir alhora la potència i els límits de l'harmonització: homogeneïtzar formats i geometries no elimina la incertesa ni crea detall nou.

### Volum, intensitat i densitat de l'activitat turística

La publicació regional d'Eurostat il·lustra especialment bé per què no hi ha un indicador universal de «pressió turística». Les pernoctacions totals mostren el volum d'activitat; les pernoctacions per habitant aproximen la intensitat respecte de la població resident; i les pernoctacions per quilòmetre quadrat mostren concentració territorial. Una regió insular poc poblada pot destacar per intensitat, mentre que una regió urbana compacta pot destacar per densitat. No són resultats contradictoris: cada denominador construeix una pregunta diferent.

Eurostat adverteix, a més, que les pernoctacions registrades no inclouen totes les formes d'allotjament ni les visites sense pernoctació. Per tant, un indicador ben calculat encara pot infrarepresentar el fenomen. Les limitacions de cobertura formen part del resultat i s'han de comunicar juntament amb el valor.

Les pernoctacions serveixen per construir diverses lectures turístiques. El numerador pot ser el mateix, però cada denominador o partició modifica el significat:

::: table "Preguntes i indicadors habituals de demanda turística"
| Pregunta | Construcció orientativa | Unitat | Límit principal |
| --- | --- | --- | --- |
| Quin volum d'activitat registrada rep el territori? | pernoctacions totals | pernoctacions | No controla la mida del territori ni de la població resident |
| Quina intensitat representa respecte de la població? | pernoctacions / població resident × 1.000 | pernoctacions per 1.000 habitants | Pot assolir valors extrems en territoris poc poblats |
| Quina concentració territorial presenta? | pernoctacions / superfície | pernoctacions per km² | Destaca territoris compactes i no descriu la distribució interna |
| Quin pes té la demanda internacional? | pernoctacions de no residents / pernoctacions totals × 100 | percentatge | Depèn de la definició de residència i de la cobertura dels allotjaments |
| Fins a quin punt es concentra en temporada alta? | pernoctacions del període punta / pernoctacions anuals × 100 | percentatge | El resultat depèn de com es defineix el període punta |
:::

Cap d'aquestes mesures descriu per si sola la sostenibilitat, la rendibilitat o el benestar de la població. Juntes poden mostrar volum, intensitat, concentració, dependència de mercats i estacionalitat, i orientar quines dimensions econòmiques, socials o ambientals cal investigar després.

::: subfigures a+b "Dues figures útils per separar oferta i demanda turística, però també per detectar decisions de representació que caldria revisar. Llicència: pendent de revisar."
![Gràfic de barres apilades sobre establiments i places turístiques a Catalunya, amb percentatges calculats sobre totals diferents]({{ site.baseurl }}/assets/img/legacy/chart-tourist-establishments-beds-catalonia.png "Els percentatges d'establiments i de places tenen denominadors diferents i no formen parts apilables d'un mateix total")
![Gràfic d'anell sobre la distribució percentual de les pernoctacions de turistes estrangers a Catalunya segons el país d'origen]({{ site.baseurl }}/assets/img/legacy/chart-tourist-overnight-stays-catalonia.png "Les pernoctacions per origen formen una composició del 100%, però les categories es podrien identificar amb etiquetes directes")
:::

>>>> **Les dades poden ser pertinents i la representació, millorable.** A la subfigura `a`, els percentatges d'establiments i els percentatges de places es calculen sobre totals diferents. Apilar-los fa veure que són parts d'un mateix total i produeix, per exemple, una barra hotelera de `54,2 + 53,2 = 107,4%`; aquesta alçada no té una interpretació vàlida. La comparació seria més clara amb barres agrupades, punts o dos panells que mantinguessin separades les dues mesures. A la subfigura `b`, en canvi, els sectors sí que formen una composició del 100%, però la llegenda obliga a relacionar repetidament colors i categories. Si l'espai ho permet, les etiquetes directes sobre l'anell o al costat de cada sector reduirien aquest recorregut; el buit central només és útil si rep una funció informativa. Els capítols de semiologia gràfica i color reprendran aquestes decisions abans de produir les figures pròpies del projecte.

La lectura conjunta d'oferta i demanda evita una confusió habitual. Les places d'allotjament indiquen capacitat disponible o autoritzada, mentre que les pernoctacions indiquen ús registrat durant un període. Dividir places per població resident construeix una mesura de pressió potencial de l'oferta; dividir pernoctacions per població resident construeix una intensitat de demanda; dividir pernoctacions per places obertes s'acosta a l'ocupació. Els tres càlculs poden ser correctes, però no són equivalents i no s'han de presentar amb el mateix nom.

En una destinació litoral, aquesta diferència és especialment rellevant perquè el volum anual pot ocultar una concentració temporal molt forta. Un municipi pot tenir moltes places però una ocupació baixa fora de temporada, o poques places hoteleres i una presència residencial estacional que no apareix a les enquestes d'allotjament. Per això el projecte comarcal ha de conservar numeradors, denominadors i períodes abans d'escollir la fórmula final: el denominador no és un detall tècnic, sinó la manera d'indicar respecte de què es considera gran o petit el fenomen.

### Funció i límits dels quadres de comandament

Un *dashboard* o quadre de comandament reuneix indicadors, filtres i representacions per facilitar una consulta recurrent. [Dataestur](https://www.dataestur.es/) integra informació de FRONTUR, EGATUR, enquestes d'ocupació, transport, ocupació laboral, rendibilitat hotelera i fonts ambientals. El [quadre de dades d'UN Tourism](https://www.unwto.org/tourism-data/un-tourism-tourism-dashboard) presenta arribades, ingressos, contribució al PIB, estacionalitat i altres mesures internacionals.

La immediatesa visual no elimina la metodologia. Dins d'un mateix dashboard poden conviure recomptes mensuals, variacions interanuals, percentatges, dades experimentals i indicadors anuals procedents de productors diferents. Abans d'utilitzar una xifra cal obrir-ne la font, llegir la definició i comprovar el període, la unitat i l'escala. Un quadre de comandament és una interfície de consulta i decisió, no una font homogènia per definició.

## Famílies temàtiques d'indicadors

Un repertori ajuda a formular preguntes i buscar dades, però no és una llista obligatòria. Cada projecte ha de seleccionar un conjunt compacte i coherent amb el territori, la disponibilitat de fonts i l'ús previst. Les propostes següents utilitzen tres etiquetes que poden coincidir: una mesura **oficial** té una definició publicada pel productor; una mesura **derivada** combina variables mitjançant una operació transparent; i una mesura **exploratòria** funciona com a hipòtesi de treball i necessita una validació específica abans d'utilitzar-se per prendre decisions. Aquestes etiquetes segons procedència, construcció i ús són independents de si l'indicador és simple o compost, directe o indirecte.

::: table "Famílies d'indicadors territorials i turístics"
| Família | Pregunta possible | Indicadors proposats | Estat i fonts de referència |
| --- | --- | --- | --- |
| Demografia i habitatge | Quina població resident i quina estructura residencial contextualitzen la destinació? | població, densitat, pes de 65+, habitatge no principal, habitatge buit | Variables oficials d'Idescat/INE; percentatges i densitats derivats |
| Presència i càrrega estacional | Quantes persones utilitzen efectivament el municipi al llarg de l'any? | població ETCA, població estacional ETCA, taxa de vinculació ETCA | Indicadors oficials de les [Estimacions de població estacional](https://www.idescat.cat/pub/?id=epe&m=m) d'Idescat |
| Demanda turística | Quin volum, origen, durada i distribució temporal presenta la demanda registrada? | arribades, pernoctacions, estada mitjana, pes de no residents, concentració mensual | Variables i indicadors d'Idescat, INE i Eurostat; no inclouen totes les estades ni les visites sense pernoctació |
| Oferta i ocupació | Quina capacitat existeix i quina part està realment disponible i utilitzada? | establiments, habitacions, places, places per 1.000 habitants, ocupació neta | Capacitat oficial; pressió de places derivada; ocupació neta definida per Eurostat |
| Economia i treball | Quin pes econòmic té el turisme i quines condicions laborals l'acompanyen? | PIB turístic directe, ocupació atribuïble, pes de contractes temporals o jornada parcial | Els dos primers requereixen compte satèl·lit; l'ocupació en branques turístiques també inclou demanda no turística |
| Mobilitat i accessibilitat | Com s'arriba a la destinació i quins recursos pot utilitzar tothom? | repartiment modal, distància o temps d'accés, ocupació dels vehicles, recursos auditats com a accessibles | Derivats d'enquestes, xarxes o auditories amb cobertura i estàndard explícits; no hi ha una única sèrie municipal harmonitzada |
| Recursos i residus | Quants recursos consumeix l'activitat i en quin context de disponibilitat? | aigua, energia o residus atribuïbles per pernoctació; pes del turisme en el consum territorial; WEI+ | La intensitat exigeix atribució turística; WEI+ descriu estrès hídric territorial, no consum turístic aïllat |
| Costa i medi | Quines condicions ambientals i pressions afecten una destinació litoral? | qualitat de les aigües de bany, artificialització del litoral, canvi de coberta, superfície protegida, pressions climàtiques | Classificacions oficials i indicadors derivats de dades ambientals; GCSD amplia l'anàlisi a una escala global {% cite zuoGCSDCoastalIndicators2025 %} |
:::

La **població equivalent a temps complet anual** d'Idescat és especialment rellevant en municipis turístics perquè integra presències i absències associades a residència secundària, turisme, treball, estudis i, des de la base 2021, excursions. Cada persona-dia equival a $1/365$ persones ETCA. Això permet descriure una càrrega mitjana que la població resident no mostra, però els canvis entre les bases 2002, 2016 i 2021 impedeixen unir-ne les sèries sense revisar la metodologia.

L'accessibilitat i la percepció resident exigeixen una precaució diferent. El percentatge de recursos que compleixen un estàndard d'accessibilitat només és interpretable si s'han auditat totes les unitats amb el mateix protocol i en una data coneguda. De la mateixa manera, les pernoctacions per habitant, les places per resident i altres mesures directes d'intensitat poden actuar com a indicadors indirectes de l'exposició o la pressió experimentades, però no mesuren satisfacció, conflicte ni capacitat de càrrega. Aquestes dimensions necessiten enquestes representatives, observació i coneixement local.

### Fórmules generals de construcció

La notació matemàtica separa la definició conceptual de la posició concreta de les cel·les al full de càlcul. Les fórmules següents construeixen indicadors simples i transparents, no índexs compostos. Si $x_i$ és un numerador del territori $i$, $d_i$ el denominador, $A_i$ la superfície, $P_i$ la població resident i $k$ un factor d'escala, les construccions bàsiques són:

$$
\text{percentatge}_i = \frac{x_i}{d_i}\times 100
$$

$$
\text{ràtio}_i = \frac{x_i}{d_i}\times k
$$

$$
\text{densitat}_i = \frac{x_i}{A_i}
$$

El factor $k$ permet expressar, per exemple, places o pernoctacions per 1.000 habitants. No s'ha d'afegir automàticament: la unitat final ha de respondre a una escala comprensible i s'ha de mantenir al nom de l'indicador.

Per a la demanda turística, l'estada mitjana relaciona pernoctacions i arribades. La intensitat i la densitat definides a les [metadades d'ocupació turística d'Eurostat](https://ec.europa.eu/eurostat/cache/metadata/en/tour_occ_esms.htm) comparteixen numerador, però canvien el denominador:

$$
\text{estada mitjana} = \frac{\text{pernoctacions}}{\text{arribades}}
$$

$$
\text{intensitat turística} = \frac{\text{pernoctacions}}{\text{població resident}}\times 1\,000
$$

$$
\text{densitat turística} = \frac{\text{pernoctacions}}{\text{superfície en km}^2}
$$

L'ocupació neta no divideix per la capacitat nominal de tot l'any, sinó per les places realment ofertes durant els dies d'obertura. Si $b_t$ és el nombre de places disponibles el dia $t$ i $N$ les pernoctacions del període:

$$
\text{ocupació neta de places} = \frac{N}{\sum_{t=1}^{T} b_t}\times 100
$$

Quan només es disposa d'una capacitat constant $b$ i de $D$ dies efectivament oberts, el denominador es pot escriure $bD$. Utilitzar 365 dies per a un establiment tancat part de l'any produiria una ocupació bruta diferent i no comparable amb la definició neta d'Eurostat.

L'estacionalitat es pot aproximar de diverses maneres. La quota del període punta és fàcil de comunicar si els mesos punta es defineixen abans d'observar el resultat. Per a un conjunt $H$ de mesos de temporada alta i pernoctacions mensuals $N_m$:

$$
\text{concentració estacional} = \frac{\sum_{m\in H}N_m}{\sum_{m=1}^{12}N_m}\times 100
$$

Una concentració alta indica que una part gran de la demanda registrada es produeix en pocs mesos; no explica si la destinació disposa de recursos suficients ni si la població percep aquesta distribució com un problema. El resultat també depèn de si $H$ representa un mes, dos mesos o un trimestre.

Els indicadors ambientals requereixen atribuir correctament el numerador. Si es coneix el consum d'aigua imputable a l'activitat turística, es pot construir una intensitat per pernoctació:

$$
\text{intensitat hídrica turística} = \frac{\text{aigua atribuïble al turisme}}{\text{pernoctacions}}
$$

Dividir el consum municipal total per les pernoctacions seria incorrecte perquè el numerador inclouria residents, indústria, serveis i altres usos. A una altra escala, l'Agència Europea de Medi Ambient [defineix el WEI+](https://www.eea.europa.eu/en/analysis/indicators/use-of-freshwater-resources-in-europe-1) com la part dels recursos renovables consumida per l'economia:

$$
\mathrm{WEI+} = \frac{\text{captacions}-\text{retorns}}{\text{recursos hídrics renovables}}\times 100
$$

WEI+ descriu el context d'estrès d'una conca o territori. No atribueix el resultat al turisme, però permet interpretar si un consum turístic determinat es produeix en un sistema amb més o menys escassetat estacional.

## Dissenyar una mesura útil

La qualitat d'un indicador depèn de la correspondència entre la pregunta i la construcció matemàtica. El punt de partida és una frase precisa: què es vol observar, sobre quines unitats territorials, en quin període i per a quin ús. Només després es decideixen el numerador, el denominador i el factor d'escala.

Un valor absolut descriu volum. Un percentatge expressa una part d'un total. Una ràtio relaciona quantitats que poden representar fenòmens diferents. Una densitat posa una magnitud en relació amb la superfície. Aquestes formes no constitueixen una escala de sofisticació: cadascuna respon una pregunta. El volum de població pot ser rellevant per dimensionar serveis, mentre que la densitat ajuda a comparar concentració espacial.

>>>>> El disseny d'una mesura útil tradueix una pregunta territorial en una construcció matemàtica interpretable i revisable.
>>>>>
>>>>> - Formular la pregunta, la unitat territorial, el període i l'ús previst abans d'escollir una fórmula.
>>>>> - Distingir volum, percentatge, ràtio, densitat i agregació segons la comparació que permeten.
>>>>> - Justificar el numerador, el denominador, la unitat i el factor d'escala amb relació a la pregunta.
>>>>> - Validar comparabilitat, bases petites i casos extrems, i separar els patrons observats de les causes possibles.

::: table "Preguntes i indicadors possibles sobre població i habitatge"
| Pregunta | Numerador | Denominador | Lectura principal | Ús possible |
| --- | --- | --- | --- | --- |
| On viu més població? | Població resident | Cap | Volum demogràfic | Dimensionar demanda potencial o contextualitzar altres resultats |
| On pesa més la població gran? | Població de 65 anys o més | Població total | Envelliment relatiu | Detectar necessitats de serveis i comparar estructura demogràfica |
| On es concentra la població? | Població resident | Superfície en km² | Densitat demogràfica | Comparar concentració mitjana, sense descriure la distribució interna del municipi |
| On pesa més l'habitatge no principal? | Habitatges no principals | Habitatges totals | Composició del parc residencial | Identificar contrastos residencials que requereixen context addicional |
:::

### El denominador defineix la comparació

El denominador estableix respecte de què es llegeix el numerador. Comparar habitatges no principals amb habitatges totals respon una pregunta sobre composició residencial; comparar-los amb la població resident construiria una altra relació i una altra unitat. Un denominador inadequat pot produir una fórmula vàlida i un indicador irrellevant.

El factor d'escala facilita la comunicació. Una proporció es pot expressar com a percentatge multiplicant per cent, o una intensitat turística com a pernoctacions per mil habitants. El factor no modifica la relació subjacent, però sí la unitat visible i la manera d'interpretar-la. Ha de constar al nom, a la llegenda i al diccionari.

### Volum i intensitat es complementen

Els valors relatius faciliten comparacions entre territoris de mides diferents, però poden destacar bases molt petites. Un municipi amb pocs habitatges pot presentar un percentatge molt alt per una diferència de pocs casos. Per això convé conservar el numerador, el denominador i l'indicador, i llegir conjuntament volum i intensitat.

El mateix principi s'aplica als casos extrems. Una densitat alta pot descriure una ciutat compacta, i una ràtio alta pot dependre d'un denominador molt petit. No s'han d'eliminar els valors incòmodes: s'han de comprovar i contextualitzar.

>>>> **Un percentatge sense denominador pot exagerar una història.** Dir que un fenomen ha crescut un 50% no significa el mateix si passa de 2 a 3 casos que si passa de 2.000 a 3.000. En un indicador municipal cal conservar el numerador i el denominador perquè el lector pugui distingir intensitat, volum i estabilitat del càlcul. Aquesta cautela és una versió territorial dels problemes de reducció de dades que Jones descriu per als gràfics {% cite jonesHowLieCharts2018 %}.

### Comparabilitat i límits

Dos indicadors només es poden comparar si les definicions, els períodes, les unitats i les delimitacions territorials són compatibles. Una taxa municipal i una mitjana estatal poden tenir la mateixa unitat i, tanmateix, provenir de cobertures diferents. Una sèrie temporal es pot trencar si canvien el cens, la classificació, el mètode o els límits territorials.

Un indicador descriu un patró, però no n'estableix automàticament la causa. Un percentatge alt d'habitatge no principal no demostra especialització turística, despoblament ni habitatge buit. Aquestes interpretacions exigeixen altres fonts i una argumentació que separi observació, hipòtesi i conclusió.

## Activitat: construir indicadors al llibre comarcal

### Punt de partida i abast de la demostració guiada

L'activitat continua en el mateix llibre acumulatiu del capítol 1 i es resol amb Excel o Calc. Abans de començar es conservarà `tigit-01-preparacio-dades.xlsx` i es crearà `tigit-02-indicadors-territorials.xlsx`. L'abast de la demostració guiada és calcular els quatre indicadors demogràfics a `indicators_demography`, els dos d'habitatge a `indicators_housing` i els agregats comarcals a `indicators_summary`, i actualitzar `dictionary`, `checks` i `README.md`.

Els sis indicadors de la taula següent concreten l'abast de la demostració guiada i permeten seguir un mateix exemple de principi a fi. Cada full conservarà el codi i el nom de cada municipi, les variables de partida i les fórmules necessàries per revisar el resultat. La separació evita un full excessivament ample i permet treballar una família d'indicadors sense perdre de vista els components. En el projecte, la selecció efectiva d'indicadors es farà segons els camps compatibles disponibles i la pregunta acordada; pot coincidir amb aquesta sèrie o adoptar-ne només les construccions pertinents.

La demostració utilitza població i habitatge perquè aquestes variables construeixen el context i diversos denominadors necessaris per interpretar un territori. No mesura encara l'activitat turística. Per calcular intensitat, densitat, estacionalitat o rendibilitat turística caldria incorporar pernoctacions, places, establiments, ocupació, despesa o altres dades amb cobertura territorial i temporal compatible. L'habitatge no principal no s'utilitzarà com a indicador indirecte de l'activitat turística. Els indicadors turístics de la taula anterior funcionen com a model per a una ampliació posterior quan es disposi d'una font adequada.

La pregunta «on pesa més la població gran?» es tradueix, per exemple, en tres camps relacionats: població de 65 anys o més, població total i percentatge resultant. Conservar els dos primers permet revisar el tercer i entendre si un valor elevat descansa sobre una base gran o petita. La mateixa lògica s'aplica als altres indicadors abans de convertir els camps en referències de cel·la.

>>>>> L'activitat transforma les dades municipals preparades en indicadors documentats que continuaran alimentant els gràfics del llibre comarcal.
>>>>>
>>>>> - Construir als fulls `indicators_*` els indicadors municipals amb numeradors, denominadors, unitats i fórmules visibles.
>>>>> - Calcular els agregats comarcals a partir de les sumes compatibles, sense fer mitjanes simples de percentatges municipals.
>>>>> - Validar divisions, absències, cobertura, totals i casos extrems mitjançant comprovacions reproduïbles.
>>>>> - Interpretar contrastos territorials com a patrons descriptius i distingir-los de les hipòtesis causals.
>>>>> - Documentar definicions, limitacions i comprovacions a `dictionary`, `checks` i `README.md` perquè els resultats alimentin `charts_data`.

### Percentatges, ràtios i arrodoniment al full

Aquest capítol introdueix les fórmules quantitatives que el capítol 1 havia deixat pendents. Ja no es tracta només de comprovar si una cel·la és numèrica o si un codi està duplicat, sinó de relacionar una mesura amb el denominador que correspon a la pregunta.

::: table "Operacions numèriques dels indicadors"
| Operació | Fórmula orientativa | Pregunta que resol |
| --- | --- | --- |
| Total compatible | <code>=SUM(D2:D23)</code> | Quin volum sumen els municipis amb la mateixa definició i període? |
| Diferència | <code>=D2-C2</code> | Quin canvi o contrast hi ha entre dues mesures compatibles? |
| Percentatge | <code>=D2/C2*100</code> | Quin pes té una part dins del seu total? |
| Ràtio escalada | <code>=F2/D2*1000</code> | Quantes unitats corresponen a cada 1.000 unitats del denominador? |
| Densitat | <code>=D2/S2</code> | Quina magnitud correspon a cada unitat de superfície? |
| Divisió validada | <code>=IF(AND(ISNUMBER(D2),ISNUMBER(C2),C2&gt;0),D2/C2*100,NA())</code> | Es pot calcular l'indicador sense fabricar un zero? |
:::

El format i l'arrodoniment no són el mateix. Mostrar `12,3456` amb un decimal no modifica el valor intern; `ROUND(A2,1)` retorna una dada derivada igual a `12,3`. Els fulls `indicators_*` conservaran la precisió necessària per revisar i reutilitzar els càlculs. L'arrodoniment s'aplicarà als textos, etiquetes o exportacions quan la comunicació ho exigeixi, no abans de calcular agregats o classes.

Tampoc no es farà una mitjana simple de percentatges municipals per obtenir el valor comarcal. El percentatge comarcal d'habitatge no principal es calcula sumant els habitatges no principals compatibles i dividint-los per la suma dels habitatges totals. Aquesta operació pondera implícitament cada municipi segons el seu denominador i es desenvolupa a `indicators_summary`.

Cada fórmula calculable s'acompanyarà d'un estat, com `ok`, `missing_numerator`, `denominator_zero` o `incompatible_period`. `NA()` pot mantenir visible un resultat no calculable dins del llibre i evitar que un gràfic el representi com a zero. Quan el capítol 5 generi el CSV per a QGIS, l'error es convertirà en un valor nul i l'estat s'exportarà en un camp separat; mai no es transformarà en zero ni en el text literal `#N/A`.

### Fórmules, unitats i casos no calculables

Al full `indicators_demography`, la població total ocupa `C`, la població de 0 a 14 anys `D`, la de 65 anys o més `E` i la superfície `F`. Al full `indicators_housing`, la població total ocupa `C`, els habitatges totals `D`, els principals `E` i els no principals `F`. Les sis fórmules de la primera fila municipal són:

```text
indicators_demography!G2 =IF(AND(ISNUMBER(D2),ISNUMBER(C2),C2>0),D2/C2*100,NA())
indicators_demography!H2 =IF(AND(ISNUMBER(E2),ISNUMBER(C2),C2>0),E2/C2*100,NA())
indicators_demography!I2 =IF(AND(ISNUMBER(E2),ISNUMBER(D2),D2>0),E2/D2*100,NA())
indicators_demography!J2 =IF(AND(ISNUMBER(C2),ISNUMBER(F2),F2>0),C2/F2,NA())
indicators_housing!G2 =IF(AND(ISNUMBER(F2),ISNUMBER(D2),D2>0),F2/D2*100,NA())
indicators_housing!H2 =IF(AND(ISNUMBER(C2),ISNUMBER(E2),E2>0),C2/E2,NA())
```

Les condicions comproven que el numerador i el denominador siguin numèrics i que el denominador sigui superior a zero. `NA()` manté visible que l'indicador no es pot calcular, en lloc de fabricar un zero. Una cel·la buida, una dada no disponible i un zero observat no signifiquen el mateix. Els noms de les funcions i el separador d'arguments poden aparèixer localitzats segons l'aplicació, l'idioma i la configuració regional; cal adaptar-ne la sintaxi sense canviar la lògica de la prova.

Les fórmules s'han de conservar perquè es pugui revisar l'origen del resultat. Els noms dels camps han d'indicar la variable i la unitat, i el diccionari ha d'explicar la fórmula, el factor d'escala, el tipus de construcció, la relació amb el fenomen, la interpretació i les limitacions.

### Indicadors municipals

La demostració calcularà un conjunt compacte que després es podrà representar amb gràfics i mapes:

::: table "Indicadors municipals de població i habitatge"
| Indicador | Fórmula orientativa | Unitat | Lectura |
| --- | --- | --- | --- |
| Pes de la població jove | població de 0–14 / població total × 100 | percentatge | Pes de les edats joves |
| Pes de la població gran | població de 65+ / població total × 100 | percentatge | Pes de les edats avançades |
| Índex d'envelliment | població de 65+ / població de 0–14 × 100 | persones de 65+ per cada 100 de 0–14 | Relació entre els dos extrems d'edat |
| Densitat de població | població total / superfície | habitants per km² | Concentració demogràfica |
| Pes de l'habitatge no principal | habitatges no principals / habitatges totals × 100 | percentatge | Composició del parc residencial |
| Residents per habitatge principal | població total / habitatges principals | residents per habitatge principal | Relació aproximada entre població i parc principal |
:::

Els quatre primers indicadors descriuen estructura i concentració demogràfica; els dos darrers connecten població i habitatge. El percentatge d'habitatge no principal no identifica habitatges turístics, i residents per habitatge principal no substitueix una estadística oficial de grandària de la llar.

### Mesures comarcals agregades

La miniinfografia podrà destacar tres o quatre valors agregats: població total, habitatges totals, percentatge comarcal d'habitatge no principal i percentatge de població de 65 anys o més. Els percentatges comarcals s'han de recalcular a partir de les sumes:

```text
=SUM(F2:F23)/SUM(D2:D23)*100
=SUM(H2:H23)/SUM(G2:G23)*100
```

No s'ha de fer la mitjana simple dels percentatges municipals, perquè donaria el mateix pes a un municipi petit i a un de molt poblat. El darrer número de fila variarà segons la comarca.

Aquestes fórmules agregades només són vàlides després de comprovar que numerador i denominador tenen la cobertura municipal prevista. `SUM` pot ometre cel·les no numèriques i produir un resultat aparentment correcte sobre dades incompletes; qualsevol exclusió s'ha de detectar abans, aplicar-se coherentment als dos components i documentar-se.

### Validar i interpretar els indicadors municipals

Cada fórmula es calcularà per a tots els municipis. La taula permetrà observar valors habituals, extrems i contrastos que després es descriuran sense atribuir-los automàticament una causa. Abans d'acceptar els resultats caldrà:

1. comprovar que numerador i denominador corresponen a períodes i definicions compatibles;
2. evitar divisions per zero o per valors absents;
3. revisar manualment almenys un càlcul de cada família;
4. ordenar els municipis per cada indicador i inspeccionar els extrems i les bases petites;
5. comparar sumes i percentatges amb els totals de partida;
6. documentar qualsevol municipi exclòs i el motiu;
7. escriure per a cada indicador una frase sobre què mostra, una sobre per a què pot servir i una sobre què no permet concloure.

>>>> **Una fórmula correcta pot respondre una pregunta equivocada.** La validació no acaba quan el full de càlcul deixa de mostrar errors. Cal comprovar si la mesura és rellevant per a l'ús previst i si la interpretació respecta les definicions i els límits de les dades.

### Evidències del càlcul d'indicadors

::: table "Evidències del càlcul i la interpretació d'indicadors"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/processed` | `tigit-02-indicadors-territorials.xlsx` | Dades preparades, fórmules visibles i fulls `indicators_demography`, `indicators_housing` i `indicators_summary` |
| `data/processed` | Diccionari ampliat | Pregunta, fórmula, unitat, factor d'escala, tipus de construcció, relació amb el fenomen, ús i limitacions |
| `data/processed` | Taula analítica | Una fila per municipi, numeradors, denominadors i indicadors |
| `data/processed` | Comprovacions | Totals, casos absents, divisions impossibles i revisió d'extrems |
| `README.md` | Nota interpretativa | Utilitat prevista, patró observat, hipòtesi i límit de cada indicador seleccionat |
:::

Els fulls `indicators_*` quedaran calculats i documentats dins del llibre únic, acompanyats d'una justificació de com es construeix cada indicador, quina relació té amb el fenomen, per a què pot ser útil i quines precaucions requereix. Aquesta evidència no exigeix crear indicadors compostos ni indirectes. El capítol 3 utilitzarà aquests mateixos rangs per construir figures destinades a comparació, exploració i divulgació; no s'han de transcriure manualment a un altre llibre.
