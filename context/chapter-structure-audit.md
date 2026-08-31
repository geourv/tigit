# Auditoria estructural dels capítols

## Seqüència adoptada

Els pesos publiquen el recorregut següent: inici, fonts, indicadors, semiologia i gràfics, color, dades espacials, SIG, llenguatge cartogràfic, cartografia temàtica, síntesi i bibliografia. Aquesta seqüència fa que el registre cromàtic estigui disponible abans de simbolitzar dades a QGIS i manté el mapa de context com una entrada de la cartografia temàtica.

Els noms `tigit-07-teoria-color.xlsx`, `tigit-04-dades-espacials.qgz`, `tigit-05-integracio-sig.xlsx`, `tigit-05-integracio-sig.qgz`, `tigit-06-llenguatge-cartografic.qgz` i `tigit-08-cartografia-tematica.qgz` es conserven com a identificadors tècnics estables. No es renumeraran mentre scripts, paquets i documentació en depenguin. La genealogia executable ha de mostrar explícitament que el llibre `07` alimenta el llibre de transferència `05`.

## Correccions aplicades en aquesta revisió

- S'han introduït els prerequisits operatius de full de càlcul, estadística descriptiva, QGIS i Inkscape abans que es necessitin a les activitats.
- S'han separat la demostració Tarragonès–Vila-seca i el territori assignat a cada trio.
- S'han definit capa digital, CRS, geocodificació, georeferenciació i unitat d'observació en el punt d'entrada corresponent.
- El mapa de context i el requadre de situació s'han consolidat a llenguatge cartogràfic; cartografia temàtica els reutilitza sense reconstruir-los.
- Els mapes turístics s'han traslladat al tram final de cartografia temàtica com a productes editorials acabats; el debat de suports hi queda destacat com una activitat sense guanyador universal.
- La síntesi final exigeix un PDF revisat amb una persona lectora i un ZIP reproduïble extret i comprovat en una carpeta nova.

## Bloquejos d'aprovació

- El projecte executable continua centrat en població i habitatge. La guia docent exigeix allotjament turístic municipal i indicadors d'intensitat, densitat i composició de l'oferta.
- La carpeta `qgis` només conté documentació. Falten els quatre projectes `.qgz`, les composicions i les exportacions que connecten dades, mapes i infografia.
- Tres figures publicables continuen sent placeholders de QGIS: dues al capítol d'integració SIG i una al de cartografia temàtica.
- Hi ha catorze marcadors explícits de llicència pendent de revisar als capítols; alguns corresponen a composicions amb més d'una imatge.
- Falten el màster SVG de la demostració, la prova de lectura registrada, el PDF final i el ZIP reproduïble comprovat.
- La mida A3 és la demostració del taller. El format de cada lliurament avaluable continuarà depenent de la instrucció vigent a Moodle.

## Prioritats pendents de revisió profunda

### Fonts i preparació de dades

- Separar millor criteris de font, repertori institucional, preparació tabular i activitat.
- Donar més pes a unitat d'observació, taula rectangular, tipus i claus.
- Convertir catàlegs de portals i vies avançades en casos o ampliacions.
- Reduir la centralitat de dates avançades, LLM i logística del ZIP.

### Indicadors territorials i turístics

- Unificar fórmules generals, denominadors i disseny de mesures en un sol bloc central.
- Evitar repetir volum, intensitat i densitat en tres llocs.
- Separar les figures crítiques d'oferta i demanda.

### Teoria del color

- Reforçar contrast, nuls, ordre perceptiu, mida final i consistència entre peces.
- Integrar altres espècies com a exemple breu.
- Subordinar la pipeta a la selecció i validació de paletes.

### Representació de la Terra i dades espacials

- Aprofundir vector, ràster, geometria, atributs, multipart, validesa i escala de les dades.
- Reduir la climatologia física que no alimenta la pràctica espacial.
- Integrar la lectura de coordenades dels centres dins de la transició cap al SIG.
- Dividir les figures que combinen massa nivells conceptuals.

### Integració SIG

- Aprofundir taula d'atributs, selecció, filtre, consulta i diferència entre vista i dada.
- Separar clarament «taula per unir» de «taula que conté coordenades».
- Agrupar l'activitat en preparar, unir/consultar i validar/conservar.

### Llenguatge cartogràfic

- Reequilibrar càlculs d'escala, fonts instal·lades i impressió amb llegenda, jerarquia, col·lisions i composició.
- Tractar Fototeca, Google Maps i Street View com a casos, no conceptes principals.
- Dividir nord tècnic i decisió comunicativa sobre orientació.

### Cartografia temàtica

- Posar primer coropleta, normalització, classificació i validació del projecte.
- Agrupar isolínies, dasimètrics i cartogrames com a repertori secundari.
- Agrupar mètodes de classificació per lògica, no un `###` per nom.
- Redissenyar la comparació de cinc classificacions com una làmina controlada.

### Infografia i síntesi territorial

- Promoure interpretació territorial a concepte principal.
- Agrupar l'activitat en argument/selecció, composició/importació i revisió/exportació.
- Presentar A3 i PowerPoint com a cas de taller després dels criteris transferibles.
- Corregir referències als noms reals dels fulls `indicators_*`.

## Figures que convé revisar

- Portals globals, estatals i catalans de fonts i preparació: separar segons el criteri que demostren.
- Oferta i demanda d'indicadors territorials: dues crítiques diferents.
- Òrbita i incidència solar de dades espacials: escala orbital i escala local.
- Reticle UTM: fus global i lectura E/N local.
- Tipus de nord de llenguatge cartogràfic: distinció tècnica i convenció gràfica.
- Cinc classificacions de cartografia temàtica: mateixa geometria, extensió, mida i paleta, amb una sola decisió variable.

## Criteri comú

Cada secció central ha d'explicar una decisió amb problema, exemple del projecte, criteri de qualitat, límit i transició. Entrades, noms de fitxer, evidències i passos de menú no han de competir a la TOC amb els conceptes que justifiquen aquestes operacions.
