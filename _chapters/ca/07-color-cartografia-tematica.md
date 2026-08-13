---
layout: manual-chapter
title: Color i cartografia temàtica
description: Teoria del color, paletes, accessibilitat, normalització, classificació i simbolització cartogràfica.
lang: ca
ref: manual-color-thematic-cartography
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/color-cartografia-tematica/
weight: 80
part: Continguts
manual_references: true
---

Un cop introduïts els gràfics, les variables visuals i el llenguatge del mapa, el color es pot estudiar com una decisió analítica i cartogràfica. El capítol parteix de principis generals de percepció i producció cromàtica, els contrasta en gràfics i mapes, i acaba aplicant-los a la cartografia temàtica amb QGIS. Les lectures de Brown i Feringa, Pellicer Corellano, Brewer, Slocum i Wilke permeten connectar els fonaments cromàtics amb decisions específicament cartogràfiques {% cite brownColourBasicsGIS2002 pellicerColorLenguajeCartografico1993 brewerDesigningBetterMaps2005 slocumThematicCartography2009 wilkeFundamentalsDataVisualization2019 %}.

## Fonaments del color

### To, saturació i lluminositat

Aquestes dimensions permeten construir diferències visuals amb funcions distintes. El **to** diferencia famílies com blau, verd o taronja; la **saturació** expressa la intensitat o puresa aparent; i la **lluminositat** diferencia valors clars i foscos. La lluminositat pot suggerir ordre, mentre que el to separa categories amb més facilitat.

En semiologia gràfica, el **valor** designa la progressió perceptiva de clar a fosc. Està relacionat amb la lluminositat percebuda, però no s'ha de confondre automàticament amb el component *value* o *lightness* d'un selector digital, perquè els models de color el calculen de maneres diferents. El criteri cartogràfic és que l'ordre clar–fosc sigui perceptible en el resultat final.

Una seqüència quantitativa ha de mantenir una progressió visual recognoscible. Afegir molts tons diferents a una sèrie ordenada pot fragmentar-la en categories aparentment independents; canviar només la saturació pot produir diferències massa febles. La paleta s'ha d'avaluar com un conjunt i sobre la geometria real del mapa.

### RGB, CMYK i codis HEX

RGB descriu la combinació additiva de llum utilitzada habitualment en pantalles; CMYK correspon a un procés subtractiu d'impressió amb tintes. Els codis HEX expressen colors RGB de manera compacta, com `#226699`. Els models de pantalla i d'impressió no produeixen exactament els mateixos resultats.

El projecte conservarà els valors RGB o HEX de la paleta per mantenir una definició coherent entre el full de càlcul, QGIS i Inkscape. Si el producte s'ha d'imprimir, caldrà revisar una prova o la conversió requerida pel sistema d'impressió; canviar el mode de color no garanteix per si sol una correspondència perceptiva exacta.

### Contrast i accessibilitat

Una paleta ha de funcionar en la mida i el suport finals. No s'ha de confiar només en diferències cromàtiques subtils ni en combinacions problemàtiques per a part del públic. Les classes han de mantenir un ordre perceptible en escala de grisos, quan l'ordre és important, i s'han de revisar amb una simulació de deficiències de visió cromàtica disponible en una eina adequada.

El color no treballa aïlladament. El contrast amb el fons, els límits, les etiquetes i els símbols superposats pot reforçar o anul·lar una diferència. Els territoris sense dades necessiten un tractament neutral i recognoscible que no es confongui amb el valor més baix de la sèrie.

Quan una categoria sigui essencial, convé aplicar una **codificació redundant** i no confiar exclusivament en el color. En un diagrama de dispersió es poden combinar to i forma; en línies o mapes es poden afegir etiquetes directes, patrons o una jerarquia textual. Aquesta redundància és especialment útil quan els símbols són petits, les categories se superposen, el document s'imprimeix en grisos o dues classes resulten similars sota una deficiència de visió cromàtica {% cite wilkeFundamentalsDataVisualization2019 %}.

## Paletes segons el tipus de dada

### Paletes qualitatives

Permeten diferenciar categories sense suggerir un ordre que les dades no tenen. Els tons han de ser distingibles, tenir una importància visual semblant quan cap categoria és prioritària i limitar-se a un nombre que continuï sent llegible al mapa i a la llegenda.

### Paletes seqüencials

Representen intensitat mitjançant una progressió perceptible i són habituals en percentatges, ràtios i densitats. El sentit clar–fosc o fosc–clar ha de coincidir amb l'ordre de la llegenda, i les classes adjacents han de continuar sent diferenciables a la mida final.

Una rampa multicolor no esdevé seqüencial pel sol fet de recórrer molts tons. Si la lluminositat puja, baixa i torna a pujar, dos valors distants poden semblar pròxims i un canvi cromàtic brusc pot destacar un llindar que les dades no contenen. Les rampes de tipus arc de Sant Martí són un cas habitual d'aquesta manca de monotonia i no s'utilitzaran per representar una magnitud ordenada {% cite wilkeFundamentalsDataVisualization2019 %}.

### Paletes divergents

Mostren desviacions respecte d'un punt de referència explícit, com una mitjana o un valor zero amb significat analític. No s'han d'utilitzar només per obtenir més varietat cromàtica. El centre ha de tenir una interpretació territorial, i els dos costats de la paleta han de permetre comparar la magnitud de les desviacions.

La comparació de paletes es farà sobre una mateixa geometria, un mateix indicador i una mateixa classificació. Així es podrà observar què canvia quan es modifica el to o la lluminositat sense confondre aquest efecte amb nous punts de tall. Una segona comparació mantindrà la paleta i modificarà només la classificació.

### Coherència entre gràfics i mapes

Una mateixa categoria o idea ha de conservar un tractament cromàtic compatible en totes les peces de la infografia.

Aquesta coherència no obliga a aplicar la mateixa paleta sencera a qualsevol figura. Obliga a evitar contradiccions, com utilitzar un mateix blau per a habitatge principal en un gràfic i per a habitatge no principal en un altre. Els colors seleccionats i la seva funció es registraran abans de la composició final.

## Mètodes de cartografia temàtica

El mètode s'ha de decidir abans de la paleta. Un **mapa de coropletes** representa valors associats a unitats territorials mitjançant classes ordenades de color o valor, i és adequat per a percentatges, ràtios o densitats comparables. En un **mapa de símbols proporcionals**, la mida dels símbols varia amb una magnitud i pot representar quantitats absolutes. Les categories qualitatives exigeixen símbols distingibles que no suggereixin un ordre inexistent.

Altres mètodes responen a estructures diferents. Un mapa de punts assigna una quantitat constant a cada punt; un mapa de fluxos representa moviments o connexions mitjançant línies; i una isolínia uneix posicions amb el mateix valor d'un fenomen considerat continu. No s'aplicaran al projecte comarcal, però ajuden a entendre que la forma del fenomen precedeix la selecció de la simbologia.

En una coropleta, les unitats territorials extenses ocupen més superfície visual amb qualsevol indicador. El problema específic dels recomptes absoluts és diferent: combinen el fenomen amb la grandària de la població, del parc residencial o d'una altra població exposada. Per això no permeten comparar directament la intensitat municipal. La normalització no elimina l'efecte visual de la mida dels polígons, però defineix una quantitat comparable entre territoris i evita que una superfície ombrejada s'interpreti com si representés directament un recompte {% cite wilkeFundamentalsDataVisualization2019 %}.

::: table "Pregunta, dada i mètode cartogràfic"
| Dada o pregunta | Representació adequada | Precaució principal |
| --- | --- | --- |
| Quantitat absoluta per municipi | Símbols proporcionals | La magnitud s'ha de codificar amb l'àrea del símbol, no amb el radi |
| Percentatge, ràtio o densitat municipal | Coropleta | El denominador, la unitat i la comparabilitat han d'estar justificats |
| Categoria nominal | Colors o símbols qualitatius | No suggerir un ordre inexistent |
| Moviment entre llocs | Fluxos | Explicar direcció, amplada i unitat de les connexions |
| Fenomen continu | Isolínies o superfícies contínues | Justificar les observacions i la interpolació |
:::

El projecte comarcal utilitzarà una coropleta perquè representa un indicador relatiu associat a municipis. Aquesta elecció no converteix la coropleta en un mètode universal: si es volgués representar la població total, els símbols proporcionals serien una alternativa més coherent.

## Classificació de dades quantitatives

Intervals iguals
: Mètode que divideix el rang numèric en classes amb la mateixa amplitud. Les classes poden contenir nombres molt diferents d'observacions o quedar buides.

Quantils
: Mètode que distribueix aproximadament el mateix nombre d'observacions a cada classe, encara que les amplituds numèriques siguin diferents.

Trencaments naturals de Jenks
: Mètode que busca reduir la variació dins de cada classe i augmentar les diferències entre classes.

### Examinar la distribució abans de classificar

Abans d'escollir un mètode s'han de revisar el mínim, el màxim, la mediana, els valors repetits, les absències i els casos extrems. Una llista ordenada, un histograma o el diagrama de caixa construït al capítol 3 permeten observar si la distribució és uniforme, asimètrica o dominada per pocs municipis.

La classificació agrupa valors que ja existeixen; no corregeix errors ni crea comparabilitat. Si un municipi té un valor excepcional, primer s'ha de comprovar el numerador, el denominador i la font. Si és correcte, cal decidir com afecta les classes i explicar-ho, no eliminar-lo perquè dificulta el mapa.

### Nombre de classes i punts de tall

Cada mètode de classificació destaca unes diferències i n'oculta unes altres. Els intervals iguals faciliten comparar amplades numèriques, però poden deixar classes buides. Els quantils reparteixen observacions entre classes, però poden separar valors iguals o donar amplituds molt diferents. Jenks s'adapta a l'agrupació de la distribució concreta, però els punts de tall poden canviar quan canvien les dades.

La selecció es basarà en una lectura conjunta de la distribució, el nombre d'observacions per classe, l'amplada dels intervals i la pregunta territorial. Els intervals iguals no garanteixen freqüències iguals, i Jenks no reparteix les observacions de manera uniforme. Un cop escollida la classificació, se'n registraran els punts de tall exactes perquè el mapa es pugui reconstruir i comparar.

Les etiquetes de la llegenda no han de mostrar més decimals dels que es poden interpretar ni deixar buits o solapaments. Els límits de classe han de seguir un criteri consistent, especialment quan els indicadors poden prendre valors exactament iguals a un punt de tall.

### Normalització abans de classificar

La classificació no corregeix un indicador inadequat. Primer s'ha de decidir què es mesura i després com s'agrupen els valors. El percentatge d'habitatge no principal ja relaciona una part amb el parc total de cada municipi; no s'ha de tornar a dividir perquè QGIS ofereixi una opció anomenada normalització.

Un nombre absolut d'habitatges no és equivalent al percentatge. Aplicar els mateixos colors als recomptes faria que els municipis amb més volum tendissin a dominar la lectura, encara que el pes relatiu fos moderat. El nom del camp, la fórmula i la unitat s'han de contrastar amb el diccionari del llibre abans de simbolitzar.

### Casos extrems i absència de dades

Els valors extrems poden concentrar la resta d'observacions en poques classes. Es pot revisar el nombre de classes, comparar un mètode diferent o mostrar el valor de manera explícita, però qualsevol decisió ha de conservar la dada i quedar documentada.

Els territoris sense dades necessiten un tractament diferent dels valors zero. El zero és una observació possible dins de l'escala de l'indicador; l'absència indica que no es disposa d'un valor calculable o comparable. La llegenda i la simbologia han de mantenir aquesta diferència.

## Activitat: construir i comparar el mapa temàtic

La pràctica compararà mapes municipals del mateix indicador construïts amb classificacions i paletes diferents. La demostració representarà el **percentatge d'habitatge no principal** al Tarragonès. Cada projecte podrà mantenir aquest indicador o justificar l'ús del percentatge de població de 65 anys o més.

### Verificar l'indicador unit a la capa

Es continuarà el projecte QGIS del capítol 5. Abans de simbolitzar, es revisaran el camp seleccionat, el tipus numèric, la unitat, el mínim, el màxim, els nuls i almenys tres municipis contrastats amb el llibre. L'informe de la unió ha de demostrar que no hi ha codis duplicats o municipis sense correspondència inexplicada.

La construcció seguirà un procediment estable:

1. configurar una simbologia graduada sobre el camp numèric verificat;
2. separar els valors nuls abans de calcular les classes perquè no s'interpretin com a zero;
3. aplicar un primer mètode i registrar el nombre de classes, els punts de tall i les observacions de cada classe;
4. duplicar l'estil o la capa només per crear una alternativa controlada, sense duplicar les dades d'origen;
5. mantenir la mateixa extensió i composició mentre es comparen classificacions;
6. fixar els punts de tall seleccionats i comparar després les paletes;
7. desar l'estil final al projecte i, si cal reutilitzar-lo, en un fitxer d'estil al costat del projecte.

### Construir alternatives controlades

La comparació mantindrà constants el territori, l'indicador i la mida del mapa. Només canviaran el mètode de classificació o la paleta. Així es podrà atribuir la diferència de lectura a una decisió concreta i no a una acumulació de canvis simultanis.

#### Comparar classificacions

La primera comparació mantindrà una mateixa paleta seqüencial i aplicarà almenys dos mètodes de classificació. Per a cada alternativa s'anotaran el nombre d'observacions per classe, els punts de tall, les classes buides i l'efecte dels valors extrems. L'objectiu no és trobar el mapa que produeix més contrast, sinó el que respon millor a la distribució i a la pregunta.

#### Comparar paletes

La segona comparació mantindrà els punts de tall seleccionats i provarà paletes compatibles amb una dada ordenada. Es revisaran la progressió de lluminositat i el contrast amb límits i etiquetes. Els modes de previsualització del llenç de QGIS, quan estiguin disponibles, permetran comprovar l'escala de grisos i simular deficiències de visió cromàtica; alternativament, s'aplicarà la mateixa prova a una exportació. La versió final conservarà els valors HEX o RGB exactes i una nota dels problemes detectats i dels ajustos aplicats.

#### Justificar la versió final

La decisió registrarà què s'ha mantingut constant, què ha canviat, quin patró es fa més o menys visible i quines limitacions conserva. Una alternativa descartada es mantindrà com a evidència; no s'ha de presentar com un error si representa les dades correctament però respon pitjor al propòsit.

El mapa principal serà una coropleta perquè representa un percentatge. No s'hi aplicaran els colors al nombre absolut d'habitatges. Si una segona capa de símbols proporcionals representa la població total, haurà d'aportar una lectura complementària, conservar una llegenda clara i no ocultar el patró de la coropleta.

### Completar la composició i la llegenda

El mapa temàtic reutilitzarà l'extensió, la jerarquia territorial i els criteris de retolació del mapa de context. La llegenda indicarà l'indicador, la unitat, les classes i el tractament de les absències amb etiquetes comprensibles. Les fonts distingiran les dades estadístiques de la geometria municipal.

La composició es revisarà a la mida que ocuparà a la miniinfografia. El mapa s'exportarà en format vectorial a `outputs/maps`, i l'estil, la classificació i la composició editable es conservaran al projecte QGIS.

### Comprovacions de qualitat

Abans d'acceptar el mapa cal verificar que:

1. el camp, la fórmula i la unitat coincideixen amb el diccionari del capítol 2;
2. la unió no presenta duplicats ni absències inexplicades;
3. els punts de tall estan ordenats, no se solapen i coincideixen amb la llegenda;
4. les classes buides, els valors repetits i els casos extrems s'han revisat;
5. el zero i l'absència de dades tenen significats i símbols diferents;
6. la paleta conserva un ordre perceptible i contrast suficient;
7. els límits, les etiquetes i qualsevol símbol proporcional continuen sent llegibles;
8. el PDF conserva les geometries, els textos i els colors previstos.

### Evidències que s'han de conservar

::: table "Evidències de la cartografia temàtica"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `qgis` | Projecte QGIS continuat | Unió verificada, estils, classificacions i composició editable |
| `qgis` | Estil reutilitzable, si cal | Camp, classes, punts de tall, colors i símbol d'absència |
| `outputs/maps` | Mapa temàtic final | Coropleta vectorial amb llegenda, fonts, període i absències |
| `outputs/maps` | Alternativa descartada | Mateix indicador, extensió i mida amb una variació controlada |
| `README.md` | Registre de classificació | Camp, unitat, mètode, classes, punts de tall, paleta i justificació |
| `README.md` | Control d'accessibilitat | Escala de grisos, simulació cromàtica, contrast i ajustos aplicats |
:::
