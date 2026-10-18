---
title: "Gràfics a partir de les dades: LLEGIU-ME de l'alumnat"
lang: ca
ref: tigit-practica-03-alumnat
content_status: draft
recipient: alumnat
subject: "Tècniques d'informació geogràfica i turística"
subject_code: "21224102"
---

Un gràfic ha de permetre veure una relació que costa reconèixer a la taula. Aquesta pràctica converteix els indicadors revisats en figures vinculades a les dades i en una selecció de dues o tres candidates per a la síntesi territorial. La pregunta, el tipus de dada i la tasca de lectura han de justificar cada geometria.

Es treballa amb el territori assignat i el llibre de la pràctica 02. La demostració del professorat utilitza el Tarragonès, però els noms, els rangs i els resultats del projecte propi han de correspondre a les dades de cada equip. El [capítol de semiologia i visualització](https://geourv.github.io/tigit/ca/chapters/semiologia-visualitzacio/) desenvolupa les decisions gràfiques i els procediments d'exportació.

>>>>> - Construir gràfics editables vinculats a rangs comprovats.
>>>>> - Triar geometria, ordre i escala segons la pregunta.
>>>>> - Auditar marques, valors, unitats, retolació i absències.
>>>>> - Conservar dues o tres exportacions candidates i el llibre que les genera.

# Selecció del treball i organització de l'equip

El professor indica a classe els gràfics i apartats obligatoris i els enumera a Moodle. Els blocs són **B1, rangs; B2, comparació municipal; B3, segona lectura; i B4, auditoria i continuïtat**. La guia ofereix més representacions que les necessàriament seleccionades; no s'han de construir totes per defecte.

Es manté l'equip i el territori comarca–municipi. Convé alternar qui construeix el gràfic, qui contrasta tres valors i qui n'explica la lectura. Cal registrar contribucions i conservar les claus, els components i els indicadors que passaran a QGIS, a més de les figures candidates per a la síntesi.

Amb el llibre 02 validat i dues representacions seleccionades, s'estimen **120–150 minuts d'aula i 90–150 de treball autònom per estudiant treballant en equip**. Són estimacions no mesurades amb alumnat; no inclouen instal·lacions, obtenció de sèries noves ni ampliacions. Moodle concreta sessions i terminis.

# Entrada i taules auxiliars

Cal conservar `tigit-02-indicadors-territorials.xlsx` i crear-ne la continuació `tigit-03-semiologia-visualitzacio.xlsx`. Els indicadors han de mantenir les seves fórmules i els controls de cobertura. Si encara hi ha una incidència que afecta un indicador, la figura ha de respectar aquest límit.

`charts_data` reuneix els rangs que alimenten els gràfics mitjançant referències al llibre. Cada bloc ha de conservar el codi municipal juntament amb el nom i els valors. Ordenar una columna aïllada pot trencar la correspondència entre municipi i indicador: cal ordenar el bloc complet i verificar almenys tres casos.

# Preguntes i gràfics del nucli guiat

| Pregunta | Figura adequada | Comprovació principal |
| --- | --- | --- |
| Quins municipis tenen més pes d'habitatge no principal? | Barres horitzontals ordenades | Una barra per municipi; ordre coherent; longitud des de zero. |
| Com es comparen habitatges principals i no principals? | Barres agrupades | Mateixa unitat i origen per comparar les dues sèries. |
| Quin volum total i quina composició té el parc? | Barres apilades absolutes | Categories compatibles; el total de la barra té significat. |
| Com varia l'estructura d'edats entre municipis? | Barres apilades al 100% | Tres grups exhaustius i un denominador explícit. |
| S'observa associació entre envelliment i habitatge no principal? | Dispersió, si la pregunta és pertinent | Un punt per municipi; parelles X/Y del mateix codi. |

Table: Preguntes que orienten la selecció de gràfics.

Cada figura ha de tenir un full de treball identificable, com `chart_02_nonprincipal`. Els gràfics continuen sent objectes editables del llibre: una captura de pantalla no en conserva les sèries, els eixos ni els vincles.

# Construcció i auditoria

Cal començar amb les barres ordenades d'habitatge no principal. Es seleccionen els noms municipals i el percentatge del mateix bloc de `charts_data`, i es comprova quina sèrie interpreta l'aplicació com a categories i quina com a valors.

1. Cal revisar el rang de dades i comprovar que no inclogui totals, files buides o una altra comarca.
2. Es tria el tipus de gràfic i es contrasten les marques amb tres municipis del llibre.
3. Es revisen l'ordre visible i els eixos. En barres horitzontals, l'eix horitzontal és numèric i el vertical conté els municipis; algunes aplicacions inverteixen l'ordre de les categories respecte de la taula.
4. El títol identifica fenomen, territori i període. Les unitats han de correspondre a l'eix numèric i la font ha de quedar documentada.
5. Cal simplificar quadrícula, llegenda i elements decoratius sense eliminar informació necessària.

`chart_00_audit` conservarà una versió inicial i una de revisada. Al `README.md` s'explicaran almenys tres decisions que s'han contrastat: per exemple, orientació, ordre, eixos o retolació. Les correccions s'han de justificar per la lectura de les dades, no només per una preferència estètica.

En les barres d'edats al 100%, el denominador és la suma dels tres grups representats. Si aquesta suma difereix del total publicat, la discrepància es registra i no es reparteix manualment. En una dispersió, les X i les Y han de pertànyer al mateix municipi; els punts no s'uneixen amb línies perquè no formen una seqüència temporal.

# Ampliacions controlades

Es pot desenvolupar una comparació que vagi més enllà dels obligatoris. Una representació o comparació ja seleccionada com a bàsica no es torna a puntuar al 20%.

## A1. Comparar volum i composició

La pregunta és quins contrastos es veuen o s'amaguen en passar de barres apilades absolutes a barres al 100%. Es varia la normalització i es mantenen municipis, ordre, categories i colors. La referència són els habitatges principals, no principals i totals validats al llibre.

Cal comprovar que els components sumin el total, que els denominadors siguin positius i que cada barra relativa representi el 100%. La interpretació diferencia mida del parc i composició amb exemples del territori. La comparació no permet deduir quants habitatges tenen ús turístic. Es conserven els dos gràfics editables, les exportacions i una explicació del contrast.

## A2. Comparar intervals d'un histograma

La pregunta és com canvia la lectura de la distribució d'habitatge no principal amb intervals de 10 o 20 punts percentuals. Es varia només l'amplada dels intervals i es manté el domini de 0 a 100. La referència és la mateixa taula de percentatges validats.

Cal comprovar que no hi hagi buits ni solapaments, incloure el 100 al darrer interval i obtenir una suma igual al nombre de municipis vàlids. Les absències es compten separadament. La interpretació explica quin detall es guanya o es perd i quines limitacions té un conjunt amb pocs municipis; més barres no equivalen a una millor anàlisi.

## Altres recorreguts amb dades pròpies

La sèrie temporal, la piràmide i l'histograma tenen funcions diferents. Només es construeixen quan es disposa de les entrades i dels controls corresponents; els fitxers de Vila-seca serveixen a la demostració docent, no substitueixen els del municipi assignat.

- La línia temporal requereix una sèrie de la mateixa operació estadística, amb anys ordenats, cobertura i possibles ruptures documentades.
- La piràmide requereix edat i sexe. Els homes es poden situar amb signe negatiu per construir la geometria, però les magnituds representades continuen sent recomptes de persones.
- L'histograma compta municipis dins d'intervals numèrics. Els intervals no són noms municipals i han de tenir límits coherents, sense buits ni solapaments.

Les fonts addicionals s'incorporen a `sources`, es conserven a `data/raw` i es transformen en fulls `prepared_*`. No es poden deduir una sèrie temporal o una distribució per sexe a partir d'una taula que només conté un total anual.

Si un d'aquests recorreguts es planteja com a ampliació, cal concretar amb el professorat pregunta, decisió que varia, referència, controls i interpretació. La presència d'una figura addicional no garanteix puntuació.

# Exportació i selecció

La selecció final d'aquesta pràctica és de dues o tres figures candidates que aportin informació complementària. Cal exportar cada figura des del seu full o selecció, en PDF vectorial, amb un nom que identifiqui fenomen, territori i període. Les exportacions es desen a `outputs/figures`; el llibre conserva la capacitat de regenerar-les.

En Calc es revisen estil de pàgina i àrea d'impressió abans d'exportar a PDF. En Excel es pot utilitzar un full de gràfic i publicar el full actiu o la selecció corresponent. El resultat s'ha d'obrir a mida final: no hi han d'aparèixer cel·les alienes, etiquetes tallades o una figura convertida en una imatge de baixa resolució.

La inspecció a Inkscape ha de permetre seleccionar una marca i un text com a objectes vectorials. Els errors de valors, ordre o geometria es corregeixen al llibre i es tornen a exportar. El registre cromàtic s'ampliarà a la fase de color abans de reutilitzar-lo als mapes.

# Resultats, lliurament i qualificació interna

Cal conservar els llibres 02/03, els originals, els rangs vinculats, els gràfics editables, l'auditoria inicial/revisada i els PDFs candidats. El `README.md` identifica pregunta, tipus de dada, marca, variable visual, font i limitació. Si es descarta una figura, cal justificar-ho.

Per al lliurament es prepara el llibre 03, els PDF seleccionats i uns apunts breus en PDF amb tres decisions justificades, controls i contribucions de l'equip. Moodle concreta el conjunt i la tramesa; les captures no substitueixen els objectes editables. Les figures han de conservar unitats, territori, període i font visibles per reutilitzar-les amb els mapes a la síntesi.

- **Bàsic, 70%: fins a 7 punts**, per construcció, vinculació, controls i justificació dels gràfics seleccionats.
- **Ampliacions, 20%: fins a 2 punts**, per pregunta, comparació i interpretació pròpies.
- **Documentació, 10%: fins a 1 punt**, per apunts clars, captures útils, gràfics llegibles, atribucions i organització.

Els màxims no són automàtics. Bàsic i documentació complets poden arribar a 8/10 sense ampliacions. Aquestes no substitueixen obligatoris i acumular figures no garanteix punts. Cada aportació tècnica es valora al bàsic o a l'ampliació; el 10% valora comunicació i organització, sense duplicar-la. El 70–20–10 és intern; Moodle concreta el pes global i els requisits de superació d'acord amb la [guia docent de TIGIT, 21224102](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&fitxa_apartat=61&any_academic=2026_27).
