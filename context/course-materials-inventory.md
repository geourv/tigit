# Inventari de materials docents

Aquest document registra materials antics i recursos de Moodle que poden alimentar el manual TIGIT. No implica que els fitxers es puguin publicar directament. Abans d'incorporar-los cal revisar vigència, autoria, llicència, accessibilitat, dades personals i encaix amb la guia docent 2026_27.

## Repositori antic `geoteaching-tigit`

Font de treball: `sandbox/geoteaching-tigit-90437e4c4ce3.zip`.

L'arxiu, datat principalment entre 2018 i 2020 i empaquetat el 2022, conté sis jocs de diapositives, activitats i proves, taules d'Excel, capes SIG, bibliografies, tres lectures i un catàleg d'unes 280 figures. La carpeta `sandbox/` és local i està exclosa de Git.

### Criteri de reutilització

El material s'ha de tractar com una pedrera de conceptes, problemes didàctics i guions visuals. No s'han de copiar en bloc les diapositives ni publicar automàticament les imatges i les dades.

Prioritats:

1. Recuperar definicions i explicacions que continuen sent correctes, reescrites amb terminologia actual.
2. Adaptar activitats que obliguen a prendre decisions amb dades, Excel i QGIS.
3. Redibuixar o regenerar figures amb fonts obertes i autoria documentada.
4. Actualitzar les dades estadístiques i les geometries administratives.
5. Rebutjar logística antiga, captures de programari obsolet i preguntes memorístiques allunyades del flux actual.

## Materials per capítol

### 1. Fonts i preparació de dades

**Aprofitable**

- Taules `places-14.xlsx`, `viatgers-14.xlsx` i `campings_ag_14.xlsx` com a model d'una activitat de diagnosi de dades imperfectes.
- Incompatibilitat entre claus `ES11`, `11` i camps enters com a cas per treballar tipus de dada i unions.
- Files de font, registres buits, unitats poc clares i Ceuta/Melilla agregades com a errors per detectar.
- Taules històriques com `sup-forest-99.xls` per mostrar canvis territorials i zeros inicials.

**Adaptació necessària**

- Substituir valors de 1999-2014 per dades oficials recents d'Idescat, INE o altres fonts documentades.
- Substituir shapefiles antics per capes vigents de l'ICGC o l'IGN.
- Eliminar metadades personals, rutes locals i informació interna abans de distribuir fitxers.

**Buit detectat**

- Les diapositives antigues gairebé no expliquen metadades, traçabilitat, formats, valors absents, duplicats o preparació sistemàtica de taules. Aquest capítol necessita contingut nou.

### 2. Indicadors territorials i turístics

**Aprofitable**

- Gràfics antics d'establiments, places i pernoctacions per discutir universos, denominadors i composició.
- Cas integrat d'oferta, demanda, població i superfície per construir places per 1.000 habitants, densitat territorial i pes de tipologies.
- `infographics-tourism.png` com a contraexemple per identificar recomptes, percentatges, taxes, sèries i excés d'informació.

**Adaptació necessària**

- Regenerar totes les figures amb dades actuals i definicions explícites.
- No conservar títols que anticipen la conclusió, com `uk-tourists-visiting-catalonia-decrease.xls`.
- Afegir contingut nou sobre valors absoluts i relatius, percentatges, ràtios, densitats i elecció del denominador.

### 3. Semiologia gràfica i visualització

**Aprofitable**

- Contrast entre text, taula, gràfic, mapa i infografia de `1-presentacio-de-la-informacio-cat.slides.md`.
- Sèrie de gràfics circular, radial, barres, línies, dispersió i bombolles per comparar adequació perceptiva.
- Matriu `visual-variables.png` com a guió per explicar marques i variables visuals.
- Activitats antigues de cerca de bones i males pràctiques i d'elecció del gràfic adequat.

**Figures a reconstruir**

- Una matriu pròpia de posició, mida, forma, orientació, valor, textura i color aplicada a punts, línies i àrees.
- Una mateixa taula turística representada amb diversos gràfics per comparar magnitud, evolució, relació i composició.

**No prioritzar**

- Acudits visuals, gràfics decoratius i exercicis que només demanen enumerar tipus de gràfics.

### 4. Representació de la Terra i dades espacials

**Definicions prioritàries**

- Xarxa geogràfica, latitud i longitud.
- Geoide, el·lipsoide i dàtum.
- Projecció conforme, equivalent i equidistant.
- Altura i altitud.
- Sistema de referència i diferència entre assignar i reprojeccionar, que cal desenvolupar amb contingut nou.

**Figures i activitats aprofitables**

- `earth-geoid-ellipsoid.png`, `ellipsoid-definition.png` i `datum-distortions.png` com a guió per a figures noves.
- Exercici de localització amb coordenades, corregint la notació sexagesimal antiga.
- Selecció reduïda de projeccions per comparar distorsions, no la galeria enciclopèdica completa.
- Capes antigues ED50 / UTM 31N davant de capes ETRS89 com a cas deliberat de diagnosi.

**No prioritzar**

- Estacions de l'any, fusos horaris, antípodes, antecs, periecs i taxonomies exhaustives de projeccions.
- GPS com a bloc extens; els receptors i les explicacions antigues són obsolets.

### 5. Integració de dades en un SIG

**Definicions prioritàries**

- SIG com a conjunt de dades, eines, persones i mètodes per resoldre problemes territorials.
- Informació georeferenciada com a combinació d'un component temàtic i un component espacial.
- Localització directa, localització condicionada i patró espacial.
- Mètode de treball SIG com a procés traçable.

**Activitats prioritàries**

- Reescriure els diagrames `qgis-exercise-setup.uml`, `qgis-join-attributes.uml` i `qgis-visual-analysis.uml` com un únic flux actual.
- Preparar taula, revisar claus, importar CSV, unir, comptar coincidències, detectar absències i validar espacialment.
- Convertir les proves QGIS de 2018-2019 en una prova pràctica integrada, sense començar amb les dades ja resoltes.

**Actualització necessària**

- Fer servir GeoPackage, CSV i una versió actual de QGIS.
- No reutilitzar captures de QGIS 2.x com a instruccions.
- Regenerar rutes o punts amb fonts obertes; els KML antics semblen derivats de Google.

### 6. Llenguatge cartogràfic

**Definicions prioritàries**

- Escala gran i petita.
- Efectes del canvi d'escala sobre detall, informació i significat.
- Símbols puntuals, lineals i superficials.
- Generalització mitjançant selecció, simplificació, combinació, desplaçament i exageració.
- Retolació i jerarquia tipogràfica.
- Mapa turístic i responsabilitat editorial sobre què es mostra i què s'omet.

**Figures a reconstruir**

- Una mateixa costa o territori a tres escales.
- Elements i composició del mapa.
- Sèrie pròpia de retolació correcta i incorrecta en lloc dels quinze escanejos antics.
- Corbes de nivell, tintes hipsomètriques i ombreig a partir d'un model d'elevacions obert, si aquest bloc es manté.

**Activitats adaptables**

- Problemes d'escala relacionats amb la mida final del mapa o la infografia.
- Comparació de dues composicions del mateix territori a escales diferents.
- Revisió de topònims amb nomenclàtors oficials actuals.

### 7. Color i cartografia temàtica

És el bloc antic amb més potencial, però també el que exigeix més revisió tècnica i de drets.

**Definicions prioritàries**

- Mapa de punts, símbols proporcionals, cartodiagrama, fluxos, isopletes, coropletes i mapa dasimètric.
- Paletes qualitatives, seqüencials i divergents.
- Quantils, intervals iguals, desviació típica i trencaments naturals/Jenks.

**Correccions imprescindibles**

- Intervals iguals significa classes amb la mateixa amplitud, no la mateixa freqüència.
- Jenks minimitza la variació interna i separa grups; no reparteix observacions de manera uniforme.
- Les coropletes requereixen habitualment valors relatius o normalitzats.
- La terminologia antiga de cartogrames, anamorfosis i representacions isomòrfiques s'ha de revisar.

**Figures a reconstruir**

- Sèrie qualitativa, seqüencial, divergent i binària amb una paleta accessible.
- Comparació del mateix indicador amb intervals iguals, quantils i Jenks.
- Comparació entre coropleta i símbols proporcionals.
- Esquema RGB/CMYK i transferència coherent de codis HEX entre Excel, QGIS i Inkscape.

**Activitat prioritària**

- Mateix indicador i territori, classificacions i paletes alternatives, explicació de com canvia la lectura i justificació de l'opció final.

### 8. Infografia i síntesi territorial

**Aprofitable**

- Gràfics turístics i mapes de context antics com a material d'auditoria visual.
- `infographics-tourism.png` com a contraexemple de densitat excessiva i manca de focus.
- Activitat de mantenir codis RGB/HEX entre programes.
- Idea de conservar els fitxers d'Excel i QGIS com a rastre del producte final.

**Figures a reconstruir**

- Una síntesi pròpia amb dades obertes que integri un gràfic, un mapa temàtic, una interpretació i fonts.
- Exemple comparatiu entre una composició carregada i una versió amb una pregunta clara i jerarquia definida.

**Buit detectat**

- El material antic mostra infografies, però gairebé no explica retícula, jerarquia, selecció d'evidències, autoria, accessibilitat o narrativa visual. Cal desenvolupar aquest capítol amb contingut nou.

## Banc inicial de definicions

Les definicions següents es poden preparar com a llistes de definició del manual, sempre reescrites i contrastades amb bibliografia actual:

| Capítol | Termes prioritaris |
| --- | --- |
| 3 | marca gràfica, variable visual, dada qualitativa, ordinal i quantitativa |
| 4 | xarxa geogràfica, latitud, longitud, geoide, el·lipsoide, dàtum, projecció, EPSG |
| 5 | SIG, informació georeferenciada, geometria, atribut, unió, localització directa i condicionada |
| 6 | escala, generalització, retolació, implantació puntual, lineal i superficial |
| 7 | coropleta, símbol proporcional, mapa de punts, flux, isopleta, paleta qualitativa, seqüencial i divergent, quantil, Jenks |
| 8 | infografia, jerarquia visual, traçabilitat i síntesi territorial |

## Activitats troncals que convé recuperar

1. Auditoria i depuració d'una taula turística imperfecta amb Excel.
2. Construcció i justificació d'indicadors de volum, pressió, densitat i composició.
3. Representació d'una mateixa dada amb dos gràfics i comparació crítica.
4. Diagnosi d'una capa amb sistema de referència antic.
5. Unió territorial amb claus incompatibles i comprovació dels resultats.
6. Composició cartogràfica amb escala, retolació, llegenda, fonts i crèdits.
7. Comparació de classificacions i paletes sobre el mateix indicador.
8. Infografia que integri el gràfic d'Excel, el mapa de QGIS i la composició d'Inkscape.

Aquest recorregut pot alimentar les pràctiques de seguiment, la prova pràctica i la infografia. Les preguntes conceptuals i de diagnosi es poden transformar en un banc per a la prova mixta.

## Bibliografia i lectures recuperables

**Prioritat alta**

- Slocum et al., *Thematic Cartography and Geovisualization*.
- Longley et al., *Geographic Information Science and Systems*.
- Nunes, *Diccionari terminològic de sistemes d'informació geogràfica*.
- Brown i Feringa, *Colour Basics for GIS Users*.
- Jones, *How to Lie with Charts*.
- Pellicer Corellano, “El color en el lenguaje cartográfico”.

**Lectures a verificar**

- Rabella i Vives, *Mil projeccions per a un mapamundi, o l'impossible art d'aplanar la Terra*: rellevant per al capítol 4, però el PDF és un escaneig i cal comprovar-ne la distribució.
- *Mapes dasimètrics*: útil per discutir què amaga una coropleta, però és una ampliació i el PDF té restriccions de còpia.
- Planesas, *La hora oficial de España y sus cambios*: recurs lateral i no prioritari per al flux actual.

Les bibliografies antigues contenen duplicats, URLs antigues i rutes locals. Les referències seleccionades s'han de normalitzar i contrastar abans d'incorporar-les a `manual.bib`.

## Materials que no s'han de traslladar

- Horaris, tutories, terminis, percentatges i instruccions de Moodle d'edicions antigues.
- Captures instructives de QGIS 2.x o programari discontinuat.
- Receptors GPS, història tècnica extensa de GPS i afirmacions antigues sobre GNSS.
- Dades velles presentades com si descrivissin la situació actual.
- Rutes KML derivades de Google sense llicència clara.
- PDFs, portades, mapes, escanejos i infografies externes sense autoria o permís verificat.
- Enquestes antigues o altres dades personals sense base legítima i anonimització.
- Fórmules o definicions antigues que s'han identificat com a incorrectes.

## Recursos de Moodle

Els recursos de Moodle que es vagin proporcionant s'afegiran a aquest inventari amb:

- títol i tipus de recurs;
- capítol o capítols relacionats;
- funció a teoria o pràctica;
- evidència d'avaluació que prepara;
- estat d'actualització;
- autoria, llicència i restriccions de publicació;
- decisió: incorporar, adaptar, enllaçar, reservar per a Moodle o descartar.
