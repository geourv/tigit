---
layout: manual-chapter
title: Color
description: Percepció cromàtica, rodes de color, models RGB, CMYK, RYB, HSL i HSV, paletes, accessibilitat i coherència gràfica.
lang: ca
ref: manual-color
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/color/
weight: 80
part: Continguts
manual_references: true
---

El color participa en gairebé totes les figures del curs, però no sempre fa la mateixa feina. En un gràfic pot destacar una sèrie, separar categories o reforçar una jerarquia. En un mapa pot ajudar a reconèixer aigua, vegetació o sòl urbà, ordenar una intensitat o mostrar desviacions respecte d'un valor de referència. Aquest capítol estudia el color abans d'aplicar-lo a la classificació temàtica del capítol següent, per evitar que la paleta es decideixi com un acabat decoratiu.

Les decisions cromàtiques combinen tres plans. El primer és físic i tècnic: pantalles, tinta i selectors digitals no generen el color de la mateixa manera. El segon és perceptiu: el contrast, la lluminositat, la mida de les marques i les deficiències de visió cromàtica condicionen el que es pot distingir. El tercer és cultural i cartogràfic: alguns colors activen associacions compartides, però aquestes associacions poden ajudar, confondre o introduir jerarquies que les dades no contenen. Les lectures de Brown i Feringa, Pellicer Corellano, Brewer i Wilke permeten connectar aquests fonaments amb l'ús de mapes i figures {% cite brownColourBasicsGIS2002 pellicerColorLenguajeCartografico1993 brewerDesigningBetterMaps2005 wilkeFundamentalsDataVisualization2019 %}.

## Fonaments del color

### Llum, pigment i percepció

El color no és una propietat simple que es pugui traslladar sense canvis d'una pantalla a un full imprès, d'un selector digital a un mapa o d'una llegenda a una àrea concreta. En una pantalla es combinen llums; en la impressió es combinen tintes que absorbeixen part de la llum incident; i en la lectura humana intervenen l'ull, el cervell, la mida de les marques, el fons, el contrast i l'experiència cultural del lector. Per això una paleta no s'ha de jutjar només en una mostra aïllada, sinó sobre el mapa, el gràfic i el suport final {% cite brownColourBasicsGIS2002 pellicerColorLenguajeCartografico1993 brewerPredictionSurroundInduced1991 %}.

La retina conté receptors sensibles a la lluminositat i receptors que contribueixen a la percepció cromàtica. Aquesta explicació biològica bàsica ajuda a entendre per què el contrast de valor pot continuar funcionant quan el to falla, i per què una diferència aparent en pantalla pot perdre's en impressió, en una projecció o en una còpia en grisos. Les deficiències de visió cromàtica no són un cas excepcional que es resolgui al final: obliguen a no confiar tota la lectura en una oposició de tons, especialment en combinacions problemàtiques com alguns verds i vermells.

### To, saturació i lluminositat

Aquestes dimensions permeten construir diferències visuals amb funcions distintes. El **to** diferencia famílies com blau, verd o taronja; la **saturació** expressa la intensitat o puresa aparent; i la **lluminositat** diferencia valors clars i foscos. La lluminositat pot suggerir ordre, mentre que el to separa categories amb més facilitat.

En semiologia gràfica, el **valor** designa la progressió perceptiva de clar a fosc. Està relacionat amb la lluminositat percebuda, però no s'ha de confondre automàticament amb el component *value* o *lightness* d'un selector digital, perquè els models de color el calculen de maneres diferents. El criteri cartogràfic és que l'ordre clar-fosc sigui perceptible en el resultat final.

Una seqüència quantitativa ha de mantenir una progressió visual recognoscible. Afegir molts tons diferents a una sèrie ordenada pot fragmentar-la en categories aparentment independents; canviar només la saturació pot produir diferències massa febles. La paleta s'ha d'avaluar com un conjunt i sobre la geometria real del mapa.

### Rodes de color i relacions entre tons

Una roda de color ordena els tons al voltant d'un cercle i ajuda a parlar de relacions com tons veïns, oposats o separats regularment. Aquesta representació és útil per explorar harmonies, accents i contrastos, però no garanteix que dues classes siguin llegibles en un mapa ni que una paleta sigui adequada per a una dada quantitativa. La roda tracta principalment el **to**; la lectura d'una rampa temàtica depèn també de la lluminositat, la saturació, la mida de les àrees i el fons.

Els esquemes analògics, complementaris o triàdics poden funcionar en una composició gràfica general, especialment per separar blocs d'informació o accents. En canvi, una coropleta que representa una intensitat necessita una progressió ordenada. Dos tons oposats poden semblar una diferència forta, però no indiquen per si sols quin valor és més alt. Per això la roda és un instrument d'exploració, no un criteri suficient de classificació.

![Roda de color amb relacions analògiques, complementàries i triàdiques, i taula de rangs habituals per RGB, HEX, CMYK, RYB, HSL i HSV]({{ site.baseurl }}/assets/img/color-cartography/color-wheels-and-ranges.svg "La roda ajuda a pensar relacions de to, mentre que els rangs indiquen com un programa codifica numèricament el color; cap de les dues coses substitueix la prova sobre la figura final. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="54rem"}

### RGB, CMYK, RYB i HSL/HSV

RGB descriu la combinació additiva de llum utilitzada habitualment en pantalles. Cada canal, en la codificació més comuna de 8 bits, pren valors de `0` a `255`; el negre és `RGB(0,0,0)` i el blanc és `RGB(255,255,255)`. Els codis HEX expressen el mateix model de manera compacta: `#226699` equival a `R=34`, `G=102`, `B=153`. Aquesta notació és pràctica per transportar colors entre QGIS, fulls de càlcul, SVG i webs.

CMYK correspon a un procés subtractiu d'impressió amb tintes cian, magenta, groga i negra. Els canals s'expressen habitualment de `0%` a `100%`. El blanc no s'obté afegint tinta, sinó deixant el paper sense cobrir; el negre tècnic pot requerir el canal `K` i no només una combinació de cian, magenta i groc. La conversió RGB-CMYK depèn del perfil de color, del paper i del sistema d'impressió, de manera que no garanteix una equivalència perceptiva exacta.

El model **RYB** --vermell, groc i blau-- és útil per entendre una tradició artística de mescla de pigments i algunes harmonies cromàtiques, però no descriu amb precisió ni la llum de les pantalles ni la quadricromia d'impressió. No té un rang numèric universal comparable al de RGB o CMYK. Els selectors **HSL** i **HSV** organitzen el color al voltant de to, saturació i lluminositat o valor: `H` sol anar de `0` a `360` graus, i `S`, `L` o `V` de `0%` a `100%`. Són pràctics per ajustar una paleta perquè permeten pensar en decisions perceptives, encara que els seus components no coincideixin exactament amb la percepció humana ni amb el valor semiològic d'una rampa cartogràfica.

![Comparació esquemàtica dels models RGB, CMYK, RYB i HSL/HSV, amb la funció principal de cada model en el treball amb mapes i figures]({{ site.baseurl }}/assets/img/color-cartography/color-models-overview.svg "RGB és el llenguatge habitual de pantalla i codis HEX, CMYK orienta la impressió, RYB pertany a una tradició artística i HSL/HSV ajuda a ajustar to, saturació i lluminositat. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="48rem"}

El projecte conservarà els valors RGB o HEX de la paleta per mantenir una definició coherent entre el full de càlcul, QGIS i Inkscape. Si el producte s'ha d'imprimir, caldrà revisar una prova o la conversió requerida pel sistema d'impressió; canviar el mode de color no garanteix per si sol una correspondència perceptiva exacta.

## Color associatiu, semàntic i institucional

### Associacions en vista zenital

Una paleta qualitativa pot aprofitar **colors associatius** quan la relació és compartida i facilita la lectura. En cartografia, aquesta associació no sempre reprodueix el color frontal o material de l'objecte; sovint reprodueix la manera com el fenomen s'identifica en una vista zenital o en una convenció cartogràfica. La vegetació es representa habitualment amb verd encara que els troncs dels arbres siguin marrons, perquè el que domina des de dalt és la capçada. Una terra llaurada pot rebre un taronja o un marró clar encara que el sòl variï molt segons humitat, roca o cultiu. L'aigua pot aparèixer en blau encara que una ortofoto mostri tons grisos, verdosos o foscos. El sòl urbà pot utilitzar grisos o vermells apagats per distingir construcció, paviment i xarxa viària sense confondre'ls amb una temperatura o un risc.

Aquestes associacions ajuden sobretot en mapes de referència, usos del sòl, cobertes, serveis coneguts o esquemes turístics. Però no qualsevol associació és adequada. Si una categoria secundària rep un color massa intens, pot dominar la lectura. Si una convenció local es presenta com universal, pot confondre lectors d'altres contextos. I si el mateix color s'utilitza alhora com a identitat visual i com a classe temàtica, la llegenda deixa de ser inequívoca.

### Codis semàntics i identitat visual

Els codis semàntics funcionen de manera semblant. El vermell pot suggerir alerta, prohibició, aturada o temperatura elevada; el verd pot suggerir pas, vegetació o sostenibilitat; els colors del reciclatge poden variar segons el territori i el sistema de gestió; i una paleta corporativa pot identificar una universitat, una destinació o un esdeveniment. En una infografia del curs, aquests codis poden ajudar l'orientació visual, però no han de substituir la paleta analítica.

Si el blau d'una marca s'utilitza alhora per representar el valor més baix d'un indicador, el lector pot no saber si llegeix identitat, categoria o quantitat. La decisió correcta no consisteix a evitar qualsevol color institucional, sinó a reservar-lo per a accents, capçaleres o elements de jerarquia quan la paleta de dades ja té una funció pròpia.

![Sis exemples esquemàtics d'usos del color: associatiu, semàntic, identitat visual, reciclatge, paleta temàtica de dades i risc d'estereotip]({{ site.baseurl }}/assets/img/color-cartography/associative-semantic-colors.svg "Els colors associatius i semàntics poden accelerar la lectura, però només són útils si el codi és pertinent, compartit i compatible amb el tipus de dada. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="48rem"}

## Paletes segons el tipus de dada

### Paletes qualitatives

Les paletes qualitatives permeten diferenciar categories sense suggerir un ordre que les dades no tenen. Els tons han de ser distingibles, tenir una importància visual semblant quan cap categoria és prioritària i limitar-se a un nombre que continuï sent llegible al mapa i a la llegenda. Si hi ha massa categories, el problema pot no ser la paleta, sinó la necessitat d'agrupar categories o canviar la pregunta.

Una paleta qualitativa pot combinar to, forma i textura quan les marques són petites o quan el document pot circular en grisos. Aquesta redundància evita que la lectura depengui d'una diferència cromàtica mínima.

### Paletes seqüencials

Les paletes seqüencials representen intensitat mitjançant una progressió perceptible i són habituals en percentatges, ràtios i densitats. El sentit clar-fosc o fosc-clar ha de coincidir amb l'ordre de la llegenda, i les classes adjacents han de continuar sent diferenciables a la mida final.

Una rampa multicolor no esdevé seqüencial pel sol fet de recórrer molts tons. Si la lluminositat puja, baixa i torna a pujar, dos valors distants poden semblar pròxims i un canvi cromàtic brusc pot destacar un llindar que les dades no contenen. Les rampes de tipus arc de Sant Martí són un cas habitual d'aquesta manca de monotonia i no s'utilitzaran per representar una magnitud ordenada {% cite wilkeFundamentalsDataVisualization2019 matplotlibColormapReference2024 nunezOptimizingColormaps2018 %}.

### Paletes divergents

Les paletes divergents mostren desviacions respecte d'un punt de referència explícit, com una mitjana, un objectiu o un valor zero amb significat analític. No s'han d'utilitzar només per obtenir més varietat cromàtica. El centre ha de tenir una interpretació territorial, i els dos costats de la paleta han de permetre comparar la magnitud de les desviacions.

Quan una dada només té valors positius i no hi ha cap referència central significativa, una paleta divergent pot induir una lectura falsa: el lector pot entendre que hi ha dos fenòmens oposats quan en realitat només hi ha valors baixos i alts d'un mateix indicador.

### Paletes binàries i d'accent

Una paleta binària diferencia dues situacions, com presència/absència, compleix/no compleix o dins/fora. També pot destacar una categoria sobre un fons neutral. Aquest recurs és potent, però ha de respondre a una decisió clara: si el mapa destaca municipis per sobre d'un llindar, el llindar ha de tenir sentit analític i constar a la llegenda.

Els accents cromàtics serveixen per conduir la mirada cap a una dada, una anotació o una conclusió. No han de crear una segona classificació implícita ni competir amb el codi principal. Una regla pràctica és que el color d'accent hauria de poder-se explicar en una frase: destaca el territori d'estudi, assenyala un valor de referència o connecta peces que parlen del mateix fenomen.

::: table "Tipus de dada i paleta cromàtica"
| Tipus de dada o decisió | Paleta adequada | Criteri principal | Risc habitual |
| --- | --- | --- | --- |
| Categoria nominal | Qualitativa | Tons distingibles sense ordre aparent | Massa categories o importàncies visuals desiguals |
| Categoria ordinal | Seqüencial discreta | Ordre perceptible entre classes | Fer servir tons sense progressió de valor |
| Quantitat relativa | Seqüencial | Lluminositat ordenada i classes diferenciables | Rampa arc de Sant Martí o contrast insuficient |
| Desviació respecte d'un valor | Divergent | Centre significatiu i braços equilibrats | Crear oposicions que les dades no tenen |
| Presència o llindar | Binària o accent | Dues situacions definides explícitament | Ocultar la resta de valors o triar un llindar arbitrari |
:::

## Eines i codis per transportar paletes

ColorBrewer ofereix esquemes qualitatius, seqüencials i divergents pensats per a cartografia, amb advertiments sobre impressió, pantalles i deficiències de visió cromàtica {% cite harrowerColorBrewerOnline2003 brewerColorBrewerPrint2003 colorBrewer2026 %}. La interfície permet escollir el tipus de dada, el nombre de classes, el sistema de codis i diverses comprovacions, com esquemes aptes per a daltonisme, impressió o còpia en blanc i negre. El seu valor docent no és només triar colors: obliga a vincular paleta, nombre de classes i funció de lectura.

![Interfície de ColorBrewer amb una paleta seqüencial BuGn de cinc classes i opcions de seguretat cromàtica, impressió i exportació de codis]({{ site.baseurl }}/assets/img/color-cartography/colorbrewer-2026-08-14.png "ColorBrewer ajuda a escollir paletes cartogràfiques segons tipus de dada, nombre de classes i condicions de reproducció. Captura pròpia de ColorBrewer 2.0, Cynthia A. Brewer i Mark Harrower, The Pennsylvania State University, 14 d'agost de 2026; reproduïda per a comentari docent."){: data-figure-width="54rem"}

Adobe Color, en canvi, és una eina general de disseny que permet explorar rodes cromàtiques, comprovar contrastos, extreure paletes d'imatges i crear combinacions per a productes gràfics o identitat visual {% cite adobeColorPalettesThemes2026 %}. Pot ser útil per treballar accents, coherència visual o relacions de marca, però no substitueix un criteri cartogràfic sobre dades ordenades, nuls, classes i accessibilitat.

![Mostres de paletes ColorBrewer i paletes científiques seqüencials, divergents i qualitatives]({{ site.baseurl }}/assets/img/color-cartography/palette-reference-swatches.svg "Les paletes de referència mostren funcions diferents: ordre seqüencial, desviació divergent o categories qualitatives. Figura d'elaboració pròpia a partir de valors públics de paletes de referència, 13 d'agost de 2026."){: data-figure-width="48rem"}

El registre de color del projecte indicarà, com a mínim, el nom de la paleta si procedeix, els codis HEX o RGB de cada classe, el significat assignat a cada color i la prova d'accessibilitat realitzada. Aquesta anotació evita que el color es refaci "a ull" en passar d'Excel a QGIS o d'un PDF importat a Inkscape. També permet detectar contradiccions abans que la infografia quedi maquetada.

## Contrast, accessibilitat i coherència

### Comprovar a la mida final

Una paleta ha de funcionar en la mida i el suport finals. No s'ha de confiar només en diferències cromàtiques subtils ni en combinacions problemàtiques per a part del públic. Les classes han de mantenir un ordre perceptible en escala de grisos, quan l'ordre és important, i s'han de revisar amb una simulació de deficiències de visió cromàtica disponible en una eina adequada.

El color no treballa aïlladament. El contrast amb el fons, els límits, les etiquetes i els símbols superposats pot reforçar o anul·lar una diferència. Els territoris sense dades necessiten un tractament neutral i recognoscible que no es confongui amb el valor més baix de la sèrie.

### Codificació redundant

Quan una categoria sigui essencial, convé aplicar una **codificació redundant** i no confiar exclusivament en el color. En un diagrama de dispersió es poden combinar to i forma; en línies o mapes es poden afegir etiquetes directes, patrons o una jerarquia textual. Aquesta redundància és especialment útil quan els símbols són petits, les categories se superposen, el document s'imprimeix en grisos o dues classes resulten similars sota una deficiència de visió cromàtica {% cite wilkeFundamentalsDataVisualization2019 %}.

### Coherència entre gràfics, mapes i infografia

Una mateixa categoria o idea ha de conservar un tractament cromàtic compatible en totes les peces de la infografia. Aquesta coherència no obliga a aplicar la mateixa paleta sencera a qualsevol figura. Obliga a evitar contradiccions, com utilitzar un mateix blau per a habitatge principal en un gràfic i per a habitatge no principal en un altre. Els colors seleccionats i la seva funció es registraran abans de la composició final.

La coherència cromàtica també ajuda a separar tres llenguatges que sovint es barregen: el color de les dades, el color de la marca o del territori i el color de la decoració. Si aquests nivells no es distingeixen, el lector pot interpretar un accent gràfic com si fos una classe de dades.

## Activitat: preparar el registre cromàtic del projecte

La pràctica d'aquest capítol prepararà les decisions de color que s'utilitzaran després en la cartografia temàtica i en la infografia. No es tracta d'escollir una paleta definitiva per gust, sinó de documentar opcions compatibles amb el tipus de dada i provar-les sobre peces reals.

### Inventariar funcions del color

Abans d'obrir un selector cromàtic, s'identificaran les funcions del color dins del projecte: categories de gràfics, rampa per a l'indicador principal, tractament dels nuls, accents de jerarquia, fons, límits i text. Cada funció tindrà un nom i no es reutilitzarà un color amb significats incompatibles.

### Seleccionar i provar paletes

La selecció inicial inclourà almenys una paleta seqüencial per a un indicador relatiu, una paleta qualitativa per a categories o elements de referència i un color d'accent per al territori d'estudi o per a una anotació. Les paletes es provaran sobre un gràfic del capítol 3 i sobre una mostra de mapa del projecte QGIS, encara que la classificació definitiva es treballi al capítol 8.

### Registrar codis i decisions

El registre cromàtic indicarà:

1. funció de cada color dins del projecte;
2. tipus de dada al qual s'aplica;
3. codi HEX o RGB exacte;
4. origen de la paleta o criteri de construcció;
5. resultat de la prova en escala de grisos o simulació cromàtica;
6. ajustos aplicats i motiu.

La decisió cromàtica quedarà preparada quan es pugui reconstruir en un altre programa i explicar per què cada color ajuda la lectura. El capítol següent utilitzarà aquest registre per classificar i simbolitzar el mapa temàtic municipal.
