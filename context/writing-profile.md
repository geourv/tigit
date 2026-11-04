# Perfil de redacció del manual TIGIT

Aquest fitxer recull criteris duradors per a agents que redacten o revisen el manual. La versió catalana és la font de treball fins que el contingut estigui aprovat.

## Veu

El manual ha de sonar com una guia docent universitària escrita per a estudiants de primer curs: clara, precisa i exigent, però no distant. La redacció ha de ser narrativa i explicativa. No s'ha d'adreçar directament al lector en segona persona. Cal preferir construccions impersonals amb `cal`, `convé`, `s'ha de` o una descripció directa de l'acció. Només cal esmentar l'estudiantat quan sigui necessari distingir-ne la responsabilitat de la del professorat. Les llistes són útils per a instruccions, criteris o inventaris, però no han de substituir el desenvolupament d'una idea.

## Funció pedagògica

Cada secció ha d'ajudar l'estudiant a entendre una decisió. Els passos de programari han d'estar precedits per una explicació del problema, de la seva importància per a l'anàlisi territorial i turística i del criteri que permet valorar la resposta.

Els capítols han d'integrar teoria i pràctica. Excel, QGIS, Inkscape i altres eines s'han de presentar com a instruments per pensar i comunicar dades, no com a blocs autònoms del curs.

La utilitat social, professional i científica ha de precedir la recepta tècnica. Quan s'introdueixin indicadors, mapes, gràfics o sistemes d'informació, cal explicar com poden contribuir a divulgació, diagnosi, seguiment, decisió, planificació o recerca, amb exemples oficials, científics o professionals verificables.

El manual adopta un cicle de descobriment de coneixement territorial inspirat en KDD. Cal presentar-lo com un marc iteratiu adaptat, no afirmar que qualsevol percentatge, gràfic o mapa sigui mineria de dades ni que tota activitat produeixi coneixement científic nou.

## Estructura preferida

Quan es redacti una secció nova, cal preferir aquest ordre:

1. Situar el problema o la fase del treball.
2. Connectar-lo amb el curs i amb l'ús professional de la informació geogràfica i turística.
3. Introduir els conceptes tècnics necessaris.
4. Explicar quina activitat es farà amb les dades, les eines o els documents.
5. Fer explícits els criteris de qualitat o d'avaluació.
6. Tancar amb una transició cap a la fase següent.

No cal forçar tots aquests moviments en cada paràgraf. Serveixen per evitar textos massa resumits, receptes sense criteri o teoria desconnectada del laboratori.

En cada paràgraf convé identificar una funció principal i desenvolupar una idea, no acumular afirmacions. Quan el contingut ho demani, l'ordre preferent és presentar el tema o l'objectiu de lectura, formular el problema o la pregunta, desplegar els arguments amb dades o exemples, discutir-ne el significat, les alternatives o els límits, i tancar amb una conseqüència, un criteri de qualitat o una transició concreta. No tots els paràgrafs han de contenir tots aquests moviments.

Cada exemple ha d'arribar precedit per la decisió o dificultat que ajuda a entendre. Les llistes de definicions poden utilitzar-se per a vocabulari compacte; les figures compostes, les taules, els diagrames i les caixes didàctiques només s'han d'incorporar quan fan visible una relació que la prosa sola no comunica amb la mateixa claredat.

Les figures pròpies s'han d'acotar a la relació visual que necessiten explicar. Per defecte, no han d'incorporar un títol, un subtítol, un marc exterior ni un requadre explicatiu final que dupliquin el text i el peu de figura; aquests elements només es justifiquen quan la peça ha de funcionar de manera autònoma fora del manual. També cal evitar els títols interns formulats mecànicament com «De X a Y»: si hi ha una transformació real, l'han de mostrar les formes i les connexions; si no, el concepte s'ha d'anomenar directament.

La negreta s'ha de reservar per a conceptes definits, distincions decisives i criteris que l'estudiantat hagi de poder reconèixer o explicar. Normalment n'hi ha prou amb destacar-ne la primera aparició pedagògicament rellevant; no s'han de remarcar totes les repeticions, les instruccions rutinàries ni inventaris sencers només per facilitar una lectura ràpida.

Els nivells d'encapçalament han de correspondre a divisions conceptuals reals. `##` i `###` formen la TOC secundària del capítol. `####` crea una subsecció local numerada, com `1.1.1.1`, però no apareix en aquesta TOC; és adequada per a una font, un cas, un exemple o una operació que desenvolupa una idea cohesionada en un o més paràgrafs. No s'han de crear subtítols per donar format a cada element breu d'un repertori.

No s'ha d'inventar una profunditat estructural només perquè Markdown ofereixi més nivells. Un encapçalament només es justifica si el text que segueix desenvolupa una idea pròpia. Tampoc no s'ha d'imitar un quart nivell amb una línia aïllada en negreta i acabada en punt. Si és una divisió real, cal usar `####`; si és una entrada breu, el nom destacat ha de quedar integrat al mateix paràgraf. Cal evitar la repetició mecànica de títols amb fórmules com «de X a Y» quan una denominació conceptual o funcional sigui més directa.

Les caixes didàctiques s'han d'utilitzar quan el text canvia de funció i convé interrompre la lectura: `>>` per a una nota o consell, `>>>` per a un exemple resolt, `>>>>` per a una advertència, `>>>>>` per a objectius d'aprenentatge i `>>>>>>` per a una acció que pot malmetre dades o invalidar un resultat. No s'han d'usar només per donar color a un paràgraf ni encadenar-se sense prosa entre elles. Els riscos operatius concrets, com les conversions automàtiques d'un full de càlcul, són bons candidats; les explicacions conceptuals ordinàries han de continuar en prosa.

Les caixes d'objectius han de destacar entre tres i cinc resultats d'aprenentatge essencials i observables. No han d'acumular tot el vocabulari del capítol, noms de programes, formats, fitxers, rutes o passos de lliurament. Els conceptes necessaris s'introdueixen en el moment que ajuden a entendre una decisió; els procediments i les evidències queden dins de l'activitat corresponent. Si una caixa supera cinc punts, cal agrupar-ne els resultats, traslladar-ne els detalls al desenvolupament o dividir el recorregut en fases conceptuals reals.

No s'ha d'obrir sistemàticament cada capítol amb un glossari o una acumulació de vocabulari. Els termes s'han d'introduir dins de l'explicació quan ajuden a resoldre una pregunta o entendre una decisió. Les llistes de definicions es reservaran per a conjunts compactes que realment necessitin consulta conjunta.

## Guies de pràctiques, conducció docent i Moodle

Les guies de TIGIT s'adrecen a primer curs del Grau en Gestió en Turisme i Hoteleria, assignatura 21224102. Cal explicar les operacions inicials sense donar per consolidat el domini d'Excel, Calc o QGIS. El treball es manté per equips i sobre el parell comarca–municipi assignat; Tarragonès–Vila-seca és la demostració, no el territori que tots els equips han de reproduir.

- Cada guia docent inclou preparació, materials, estimacions d'aula, treball autònom i preparació del professorat, aturades de comprovació, preguntes de discussió i errors habituals. Els temps indiquen supòsits, abast i exclusions; són estimacions, no mesures fetes amb alumnat ni dates del calendari.
- Cada guia incorpora «Preparar Moodle»: crear o configurar una Tasca amb nom recognoscible, copiar l'enunciat a Descripció, adjuntar el PDF i els materials d'alumnat a Fitxers addicionals, revisar grups i tramesa, i comprovar la vista d'estudiant. Dates, límits de mida i operativa efectiva es concreten a Moodle.
- L'«Enunciat per copiar a la descripció» és autònom: pregunta, dades i punt de partida, treball bàsic identificat, ampliacions, productes, controls i qualificació. No ha de dependre de frases com «segons s'ha dit més amunt» ni contenir instruccions editorials per a l'autor.
- El professor indica a classe els apartats obligatoris i els enumera explícitament a Moodle. La guia completa pot ser més extensa que la selecció avaluada. Cal preservar les entrades de continuïtat: taula municipal i procedència en 01; components i indicadors validats en 02; llibre, rangs i figures en 03; taula de transferència, dades i projectes reobribles en 04. Si s'acota un pas necessari, s'ha de preveure com es completarà o quina preparació identificada del mateix territori permetrà continuar.
- La qualificació interna de l'activitat és **70% treball bàsic, 20% ampliacions i 10% documentació**, amb màxims de 7, 2 i 1 punts. Els 7 punts no són automàtics: exigeixen correcció, traça i comprovació dels apartats seleccionats. La documentació també pot sumar sense ampliacions; bàsic complet i documentació completa poden arribar a 8/10. Aquesta distribució no modifica els pesos globals ni els mínims de la guia docent vigent.
- Cada pràctica ofereix dues o tres ampliacions proporcionades a primer curs. Cada proposta identifica pregunta, què varia, referència, controls i interpretació. Una aportació petita ben contrastada pot satisfer el bloc d'ampliacions; acumular fitxers, captures o fórmules no garanteix punts. No s'exigeixen programació, SQL ni procediments avançats traslladats de TIG.
- Una ampliació ja seleccionada com a bàsica es valora només al 70%. La correcció tècnica correspon al bloc bàsic o a l'ampliació; el 10% valora claredat del registre, captures significatives, gràfics/mapes llegibles, atribucions i organització. No es torna a puntuar la mateixa aportació amb un altre nom.
- Les lectures d'alumnat han d'expressar la mateixa selecció, continuïtat, ampliacions i distribució de punts. Els equips registren les contribucions i tots els membres han de poder explicar una font, una decisió i un control. Això no crea una ponderació individual addicional.
- Els materials docents identifiquen el llibre o projecte resolt, originals, preparacions, captures i controls que permeten preparar la demostració. L'alumnat utilitza la plantilla buida o la seva fita anterior i les dades del seu territori. Un cas resolt compartit s'etiqueta com a exemple i no substitueix el treball propi.
- Cal contrastar l'encaix amb la guia docent de l'edició vigent i citar-la a les guies docents. El cas de població i habitatge ensenya el procediment, però no substitueix les dades d'oferta turística que exigeixi el programa. Es mantenen les limitacions temporals i conceptuals; no s'infereix habitatge turístic a partir d'habitatge no principal.
- Els canvis es fan al català i continuen `draft`. Els PDF de revisió s'obtenen amb unaltraweb en versions o runs nous i s'enllacen a l'índex local de pràctiques. La revisió d'agent i els controls tècnics no concedeixen aprovació editorial; el resultat renderitzat es revisa amb l'autor abans de commit o publicació.

## Evitar

- Convertir capítols sencers en punts breus o resums executius.
- Escriure frases genèriques sobre la importància de la tecnologia sense concretar dades, decisions o resultats.
- Presentar Moodle com a part del contingut conceptual del manual; Moodle gestiona calendari, avisos, lliuraments i qualificacions.
- Inventar temari, dates, percentatges d'avaluació o resultats d'aprenentatge sense contrastar-los amb la guia docent vigent.
- Abusar de la fórmula «X abans de Y» en títols, peus o prosa. Cal anomenar directament el concepte i expressar les dependències com a criteris o fases; només s'ha de conservar l'ordre temporal quan sigui imprescindible per al procediment, la seguretat o la cronologia descrita.
- Iniciar traduccions mentre el català continuï en revisió.
- Incloure en pàgines o capítols metainstruccions, notes de revisió, tasques pendents, estats editorials o referències a converses, agents, usuaris o instruccions rebudes. Tot el cos Markdown ha de poder publicar-se tal com està.

## Revisió editorial

Una secció només es pot donar per bona si cada paràgraf té una funció clara: orientació, concepte, decisió tècnica, exemple, criteri d'avaluació, advertiment o transició. Si un paràgraf només resumeix en abstracte, cal reescriure'l perquè expliqui una relació concreta entre teoria, pràctica i aprenentatge. També cal revisar ortografia, gramàtica, terminologia, precisió factual, cites, referències creuades i peus de figures i taules. Les observacions editorials s'han de conservar fora del cos publicable.
