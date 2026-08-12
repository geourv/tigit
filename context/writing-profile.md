# Perfil de redacció del manual TIGIT

Aquest fitxer recull criteris duradors per a agents que redacten o revisen el manual. La versió catalana és la font de treball fins que el contingut estigui aprovat.

## Veu

El manual ha de sonar com una guia docent universitària escrita per a estudiants de primer curs: clara, precisa i exigent, però no distant. La redacció ha de ser narrativa i explicativa. Les llistes són útils per a instruccions, criteris o inventaris, però no han de substituir el desenvolupament d'una idea.

## Funció pedagògica

Cada secció ha d'ajudar l'estudiant a entendre una decisió. Abans d'entrar en passos de programari, el text ha d'explicar quin problema es vol resoldre, per què importa en l'anàlisi territorial i turística, i quin criteri permet saber si la resposta és adequada.

Els capítols han d'integrar teoria i pràctica. Excel, QGIS, Inkscape i altres eines s'han de presentar com a instruments per pensar i comunicar dades, no com a blocs autònoms del curs.

La utilitat social, professional i científica ha de precedir la recepta tècnica. Quan s'introdueixin indicadors, mapes, gràfics o sistemes d'informació, cal explicar com poden contribuir a divulgació, diagnosi, seguiment, decisió, planificació o recerca, amb exemples oficials, científics o professionals verificables.

El manual adopta un cicle de descobriment de coneixement territorial inspirat en KDD. Cal presentar-lo com un marc iteratiu adaptat, no afirmar que qualsevol percentatge, gràfic o mapa sigui mineria de dades ni que tota activitat produeixi coneixement científic nou.

## Estructura preferida

Quan es redacti una secció nova, cal preferir aquest ordre:

1. Situar el problema o la fase del treball.
2. Connectar-lo amb el curs i amb l'ús professional de la informació geogràfica i turística.
3. Introduir els conceptes tècnics necessaris.
4. Explicar què farà l'estudiant amb dades, eines o documents.
5. Fer explícits els criteris de qualitat o d'avaluació.
6. Tancar amb una transició cap a la fase següent.

No cal forçar tots aquests moviments en cada paràgraf. Serveixen per evitar textos massa resumits, receptes sense criteri o teoria desconnectada del laboratori.

En cada paràgraf convé identificar una funció principal i desenvolupar una idea, no acumular afirmacions. Quan el contingut ho demani, l'ordre preferent és presentar el tema o l'objectiu de lectura, formular el problema o la pregunta, desplegar els arguments amb dades o exemples, discutir-ne el significat, les alternatives o els límits, i tancar amb una conseqüència, un criteri de qualitat o una transició concreta. No tots els paràgrafs han de contenir tots aquests moviments.

Abans d'introduir un exemple cal explicar quina decisió o dificultat ajuda a entendre. Les llistes de definicions poden utilitzar-se per a vocabulari compacte; les figures compostes, les taules, els diagrames i les caixes didàctiques només s'han d'incorporar quan fan visible una relació que la prosa sola no comunica amb la mateixa claredat.

Els nivells d'encapçalament han de correspondre a divisions conceptuals reals. `##` i `###` formen la TOC secundària del capítol. `####` crea una subsecció local numerada, com `1.1.1.1`, però no apareix en aquesta TOC; és adequada per a una font, un cas, un exemple o una operació que desenvolupa una idea cohesionada en un o més paràgrafs. No s'han de crear subtítols per donar format a cada element breu d'un repertori.

No s'ha d'inventar una profunditat estructural només perquè Markdown ofereixi més nivells. Abans d'afegir un encapçalament cal comprovar que el text que segueix desenvolupa una idea pròpia. Tampoc no s'ha d'imitar un quart nivell amb una línia aïllada en negreta i acabada en punt. Si és una divisió real, cal usar `####`; si és una entrada breu, el nom destacat ha de quedar integrat al mateix paràgraf. Cal evitar la repetició mecànica de títols amb fórmules com «de X a Y» quan una denominació conceptual o funcional sigui més directa.

Les caixes didàctiques s'han d'utilitzar quan el text canvia de funció i convé interrompre la lectura: `>>` per a una nota o consell, `>>>` per a un exemple resolt, `>>>>` per a una advertència, `>>>>>` per a objectius d'aprenentatge i `>>>>>>` per a una acció que pot malmetre dades o invalidar un resultat. No s'han d'usar només per donar color a un paràgraf ni encadenar-se sense prosa entre elles. Els riscos operatius concrets, com les conversions automàtiques d'un full de càlcul, són bons candidats; les explicacions conceptuals ordinàries han de continuar en prosa.

No s'ha d'obrir sistemàticament cada capítol amb un glossari o una acumulació de vocabulari. Els termes s'han d'introduir dins de l'explicació quan ajuden a resoldre una pregunta o entendre una decisió. Les llistes de definicions es reservaran per a conjunts compactes que realment necessitin consulta conjunta.

## Evitar

- Convertir capítols sencers en punts breus o resums executius.
- Escriure frases genèriques sobre la importància de la tecnologia sense concretar dades, decisions o resultats.
- Presentar Moodle com a part del contingut conceptual del manual; Moodle gestiona calendari, avisos, lliuraments i qualificacions.
- Inventar temari, dates, percentatges d'avaluació o resultats d'aprenentatge sense contrastar-los amb la guia docent vigent.
- Fer traduccions abans que el català estigui revisat.
- Incloure en pàgines o capítols metainstruccions, notes de revisió, tasques pendents, estats editorials o referències a converses, agents, usuaris o instruccions rebudes. Tot el cos Markdown ha de poder publicar-se tal com està.

## Revisió abans de tancar

Abans de donar per bona una secció, cal revisar si cada paràgraf té una funció clara: orientació, concepte, decisió tècnica, exemple, criteri d'avaluació, advertiment o transició. Si un paràgraf només resumeix en abstracte, cal reescriure'l perquè expliqui una relació concreta entre teoria, pràctica i aprenentatge. També cal revisar ortografia, gramàtica, terminologia, precisió factual, cites, referències creuades i peus de figures i taules. Les observacions editorials s'han de conservar fora del cos publicable.
