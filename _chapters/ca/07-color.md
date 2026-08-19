---
layout: manual-chapter
title: Teoria del color
description: Espectre visible i electromagnètic, percepció i diversitat de la visió cromàtica, cultura, models, paletes, codis reproduïbles i accessibilitat.
lang: ca
ref: manual-color
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/color/
weight: 50
part: Continguts
manual_references: true
---

El color participa en gairebé totes les figures del curs, però no sempre fa la mateixa feina. En un gràfic pot destacar una sèrie, separar categories o reforçar una jerarquia. En un mapa pot ajudar a reconèixer aigua, vegetació o sòl urbà, ordenar una intensitat o mostrar desviacions respecte d'un valor de referència. Aquest capítol estudia el color immediatament després de la semiologia gràfica perquè la paleta no es decideixi al final com un acabat decoratiu. Les mateixes decisions es reprendran després en la cartografia i en QGIS.

Les decisions cromàtiques combinen tres plans. El primer és físic i tècnic: pantalles, tinta i selectors digitals no generen el color de la mateixa manera. El segon és perceptiu: el contrast, la lluminositat, la mida de les marques i les deficiències de visió cromàtica condicionen el que es pot distingir. El tercer és cultural i cartogràfic: alguns colors activen associacions compartides, però aquestes associacions poden ajudar, confondre o introduir jerarquies que les dades no contenen. Les lectures de Brown i Feringa, Pellicer Corellano, Brewer i Wilke permeten connectar aquests fonaments amb l'ús de mapes i figures {% cite brownColourBasicsGIS2002 pellicerColorLenguajeCartografico1993 brewerDesigningBetterMaps2005 wilkeFundamentalsDataVisualization2019 %}.

>>>>> En acabar el capítol, cal poder preparar, documentar i validar una paleta coherent amb les dades abans d'aplicar-la als gràfics, als mapes i a la infografia.
>>>>>
>>>>> - Situar la radiació visible dins de l'espectre electromagnètic i diferenciar-la de l'infraroig i l'ultraviolat.
>>>>> - Explicar com l'ull i el processament neural contribueixen al color, inclosos els colors no espectrals.
>>>>> - Reconèixer la variació de la visió cromàtica entre persones i espècies, i distingir-la de les dimensions apreses i culturals.
>>>>> - Distingir to, saturació, lluminositat i valor, i relacionar-los amb RGB, CMYK, RYB, HSL i HSV.
>>>>> - Seleccionar paletes qualitatives, seqüencials, divergents, binàries o d'accent segons les dades i la pregunta.
>>>>> - Registrar codis HEX o RGB i funcions cromàtiques per reproduir una paleta entre programes.
>>>>> - Validar contrast, ordre, redundància, accessibilitat i coherència sobre una peça real i en la mida final.

## Radiació, percepció i diversitat de la visió cromàtica

### Espectre visible i radiacions invisibles

La radiació electromagnètica es pot descriure físicament, entre altres magnituds, per la longitud d'ona. El **color percebut**, en canvi, és el resultat de la interacció entre la radiació que arriba a l'ull, el sistema visual i el context. Per a una explicació introductòria se sol situar la [franja visible humana](https://cie.co.at/eilvterm/17-21-003) aproximadament entre 380 i 780 nm, però aquests valors no són fronteres universals i abruptes: la sensibilitat disminueix gradualment i varia amb la intensitat, la persona i el criteri de mesura.

Newton va iniciar els experiments amb prismes el 1666, en va publicar una primera exposició el 1672 i els va desenvolupar a *Opticks* el 1704. El prisma dispersa la llum segons la longitud d'ona: no crea els colors, i una disposició adequada els pot recombinar en llum blanca. La banda resultant és contínua; dividir-la en set noms és una convenció descriptiva, no la descoberta de set compartiments físics separats {% cite newtonTheoryLightColours1672 %}.

El 1800, Herschel va situar termòmetres més enllà del vermell dispersat i hi va detectar radiació pels seus efectes tèrmics; era el primer pas cap al que anomenem **infraroig** {% cite herschelInvisibleRays1800 %}. El 1801, Ritter va observar que el clorur de plata s'enfosquia més de pressa més enllà del violeta; el seu resultat es va difondre en un extracte de correspondència publicat a *Annalen der Physik* per Böckmann i constitueix una observació inicial de la radiació que després s'anomenaria **ultraviolada** {% cite boeckmannRitterUltraviolet1801 %}. Ni l'infraroig ni l'ultraviolat són colors humans ni són normalment visibles. Tampoc no s'ha d'identificar l'infraroig simplement amb «la calor»: és radiació electromagnètica que pot transferir energia i produir escalfament, com també ho poden fer altres bandes.

La franja visible és només una part petita de l'espectre electromagnètic. En teledetecció, un sensor mesura radiància en bandes definides; no «veu colors» com una persona. Una [**composició de fals color**](https://science.nasa.gov/earth/earth-observatory/how-to-interpret-a-false-color-satellite-image/) assigna bandes invisibles, per exemple de l'infraroig, a canals visibles de pantalla perquè una persona pugui interpretar diferències de vegetació, humitat o materials. Aquests colors són una codificació analítica i no l'aparença que tindria la radiació invisible a ull nu.

### Ull, retina i processament del color

Una pantalla emet llum cap als ulls, mentre que una tinta o una superfície absorbeix una part de la llum incident i en reflecteix una altra. Aquesta diferència física explica per què un codi de pantalla no passa sense canvis al paper, però en tots dos casos la radiació que arriba a l'ull encara ha de ser processada. Per això una paleta no s'ha de jutjar només en una mostra aïllada, sinó sobre el mapa, el gràfic i el suport final {% cite brownColourBasicsGIS2002 pellicerColorLenguajeCartografico1993 brewerPredictionSurroundInduced1991 %}.

Els **bastons** són especialment sensibles amb poca llum i no sostenen la discriminació cromàtica diürna ordinària. Aquesta depèn sobretot de tres classes de cons, S, M i L, amb sensibilitats espectrals àmplies i superposades. Les lletres indiquen sensibilitat preferent a longituds d'ona més curtes, mitjanes o llargues; no són detectors simples de «blau», «verd» i «vermell». El sistema compara les seves respostes en canals oponents, aproximadament L-M i S respecte de L+M, i integra aquesta informació de manera distribuïda amb la forma, la lluminositat, el context i l'experiència en diverses etapes retinals i corticals. No hi ha una correspondència d'un receptor amb un color ni un únic centre cerebral del color {% cite gegenfurtnerColorVision2003 %}.

L'adaptació a la il·luminació, la constància cromàtica parcial, el contrast simultani i les postimatges mostren que l'aparença depèn tant del context com de l'estat recent del sistema visual. La constància permet que moltes superfícies mantinguin una aparença relativament estable sota il·luminacions diferents, però és incompleta i depèn de les pistes disponibles {% cite fosterColorConstancy2011 %}. A més, espectres físicament diferents poden produir una aparença igual per al mateix observador sota unes condicions especificades: aquest fenomen s'anomena [**metamerisme**](https://cie.co.at/eilvterm/17-23-038). La coincidència pot deixar de produir-se si canvien l'observador o l'il·luminant, fet que explica una part de les discrepàncies entre pantalla, tinta i il·luminació.

No tots els colors percebuts corresponen a una sola longitud d'ona. Els magentes i molts porpres són **no espectrals**: poden aparèixer quan l'estimulació relativa dels cons L i S és forta respecte de la dels M. L'estímul pot tenir un espectre físicament mesurable amb energia en regions separades; el resultat perceptiu és real, no una invenció arbitrària. El violeta, en canvi, sí que pot correspondre a radiació de longitud d'ona curta dins de l'espectre visible. Dir que «el cervell construeix el color» resumeix el processament neural, però no significa que el color sigui capriciós o purament cultural: la percepció queda restringida per l'estímul, la biologia i el context {% cite gegenfurtnerColorVision2003 %}.

::: subfigures a+b "Ull humà i receptors de la retina com a base perceptiva de les decisions cromàtiques. La subfigura a és una figura SVG de Wikimedia Commons; la subfigura b és un placeholder editorial pendent de substituir per una figura oberta sobre rods i cones."
![Tall esquemàtic de l'ull humà amb retolació anatòmica en català]({{ site.baseurl }}/assets/img/color-cartography/schematic-human-eye-ca.svg "Tall de l'ull humà. Font: Jmarchn, «Schematic diagram of the human eye ca.svg», Wikimedia Commons, 2016, CC BY-SA 3.0.")
![Placeholder per a una figura sobre bastons i cons de la retina, amb les etiquetes angleses rods i cones]({{ site.baseurl }}/assets/img/placeholders/retina-rods-cones-placeholder.svg "Figura pendent: substituir per un SVG de qualitat sobre receptors de la retina que mostri rods i cones, amb autoria, font i llicència verificades.")
:::

### Deficiències de la visió cromàtica

**Deficiència de la visió cromàtica** és un terme general recomanable; **daltonisme** és una denominació tradicional i molt estesa, però no designa una sola condició homogènia. El [Cercaterm del TERMCAT](https://www.termcat.cat/ca/cercaterm) permet consultar la terminologia catalana, i la pàgina operativa del [National Eye Institute sobre deficiències de la visió cromàtica](https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness) diferencia tipus, causes i proves. Algunes deficiències són congènites i d'altres són adquirides per canvis a la retina, el nervi òptic, el cervell, el cristal·lí o per determinats tractaments.

Les variants congènites més estudiades inclouen la **tricromàcia anòmala**, en què són presents les tres classes de fotopigments dels cons però una té una sensibilitat espectral alterada o desplaçada, i la **dicromàcia**, en què falta la funció d'una classe de con. Les famílies protan, deutan i tritan descriuen mecanismes i patrons de confusió, no una incapacitat literal de «veure el vermell», «veure el verd» o «veure el blau». L'**acromatòpsia congènita** és molt més rara i comporta una alteració greu de la funció dels cons; aquesta denominació la distingeix de l'acromatòpsia cerebral adquirida {% cite kalloniatisPerceptionColor2007 %}. La freqüència de les variants vermell-verd varia segons el sexe cromosòmic i les poblacions estudiades; no convé convertir una estimació d'una mostra en un percentatge universal {% cite birchColorDeficiencyPrevalence2012 %}.

::: table "Famílies de deficiències de la visió cromàtica i conseqüències de disseny"
| Família | Mecanisme resumit | Exemples | Confusions probables i implicació de disseny |
| --- | --- | --- | --- |
| Protan | Funció L alterada o absent | Protanomalia, protanopia | Algunes diferències vermell-verd i vermells foscos; reforçar amb valor i etiquetes |
| Deutan | Funció M alterada o absent | Deuteranomalia, deuteranopia | Algunes diferències verd-vermell, marró o taronja; no separar classes només pel to |
| Tritan | Funció S alterada o absent | Tritanomalia, tritanopia | Confusions probables entre alguns blaus i verds, grocs i vermells o rosats, i porpres i vermells; comprovar fons, valor i símbols |
| Acromatòpsia congènita | Funció general dels cons greument alterada | Acromatòpsia completa o incompleta | Discriminació cromàtica molt reduïda, sovint amb altres símptomes visuals; garantir una lectura no cromàtica |
:::

Les simulacions de deficiències cromàtiques són aproximacions útils per detectar conflictes potencials, no reproduccions literals de l'experiència subjectiva de cada persona. Quan una diferència és essencial, el disseny no l'ha de codificar només amb el to: ha de combinar valor, etiquetes directes, formes, patrons o posicions {% cite machadoColorVisionSimulation2009 %}.

### Visió cromàtica en altres espècies

Els humans i, en general, els altres primats del Vell Món som tricromàtics. Molts mamífers placentaris, inclosos els gossos, són dicromàtics, però no tots els mamífers comparteixen el mateix sistema i un gos no veu el món simplement en blanc i negre. Moltes aus diürnes solen disposar de quatre classes de cons, amb sensibilitat ultraviolada o violeta segons el llinatge, mentre que l'abella de la mel té una visió tricromàtica basada en receptors sensibles a ultraviolat, blau i verd. Aquestes etiquetes descriuen sensibilitats: el nombre de classes espectrals de fotoreceptors no demostra per si sol que un animal experimenti els nostres colors amb un canal addicional ni implica una riquesa perceptiva proporcional; cal evidència neural i conductual sobre les discriminacions que utilitza l'espècie {% cite kelberAnimalColourVision2003 %}.

Aquesta comparació té un paper modest en la interpretació de fauna i l'ecoturisme, però la senyalització i els mapes del curs s'adrecen a lectors humans diversos. La teledetecció és un cas diferent: els instruments registren bandes, també fora del visible humà, i el fals color les tradueix a canals visibles per analitzar-les.

### To, saturació i lluminositat

Aquestes dimensions permeten construir diferències visuals amb funcions distintes. El **to** diferencia famílies com blau, verd o taronja; la **saturació** expressa la intensitat o puresa aparent; i la **lluminositat** diferencia valors clars i foscos. La lluminositat pot suggerir ordre, mentre que el to separa categories amb més facilitat.

En semiologia gràfica, el **valor** designa la progressió perceptiva de clar a fosc. Està relacionat amb la lluminositat percebuda, però no s'ha de confondre automàticament amb el component *value* o *lightness* d'un selector digital, perquè els models de color el calculen de maneres diferents. El criteri cartogràfic és que l'ordre clar-fosc sigui perceptible en el resultat final.

Una seqüència quantitativa ha de mantenir una progressió visual recognoscible. Afegir molts tons diferents a una sèrie ordenada pot fragmentar-la en categories aparentment independents; canviar només la saturació pot produir diferències massa febles. La paleta s'ha d'avaluar com un conjunt i sobre la geometria real del mapa.

### Rodes de color i relacions entre tons

Una roda de color ordena els tons al voltant d'un cercle i ajuda a parlar de relacions com tons veïns, oposats o separats regularment. Aquesta representació és útil per explorar harmonies, accents i contrastos, però no garanteix que dues classes siguin llegibles en un mapa ni que una paleta sigui adequada per a una dada quantitativa. La roda tracta principalment el **to**; la lectura d'una rampa temàtica depèn també de la lluminositat, la saturació, la mida de les àrees i el fons.

Els esquemes analògics, complementaris o triàdics poden funcionar en una composició gràfica general, especialment per separar blocs d'informació o accents. En canvi, una coropleta que representa una intensitat necessita una progressió ordenada. Dos tons oposats poden semblar una diferència forta, però no indiquen per si sols quin valor és més alt. Per això la roda és un instrument d'exploració, no un criteri suficient de classificació.

Les denominacions **color primari**, **secundari** i **terciari** només tenen sentit dins d'un model de mescla determinat. Els primaris són els components escollits com a base del model; no són tres colors físicament universals ni únics. Un color secundari s'obté combinant dos primaris del model. En les rodes artístiques tradicionals, un color terciari és una mescla intermèdia entre un primari i un secundari adjacent. Aquesta darrera categoria és sobretot una convenció pràctica per ordenar tons i no té una definició única en tots els sistemes.

::: table "Colors primaris, secundaris i terciaris segons el model"
| Model | Primaris | Secundaris ideals | Terciaris o intermedis |
| --- | --- | --- | --- |
| RGB, mescla additiva de llum | vermell, verd i blau | groc, cian i magenta | combinacions intermèdies entre canals; la denominació terciària no és habitual ni universal |
| CMY/CMYK, mescla subtractiva ideal | cian, magenta i groc | blau, vermell i verd | mescles intermèdies condicionades per tintes, suport i perfil d'impressió |
| RYB, roda artística tradicional | vermell, groc i blau | taronja, verd i violeta | groc-taronja, vermell-taronja, vermell-violeta, blau-violeta, blau-verd i groc-verd |
:::

La mateixa paraula pot canviar de funció entre models. El magenta és secundari en RGB perquè combina llum vermella i blava, però és primari en CMY. El verd és primari en RGB, secundari en CMY i secundari en RYB. Per això una explicació sobre colors primaris ha d'indicar sempre si parla de llum, tintes, pigments artístics o d'una roda utilitzada per explorar harmonies.

![Roda de color amb relacions analògiques, complementàries i triàdiques, i taula de rangs habituals per RGB, HEX, CMYK, RYB, HSL i HSV]({{ site.baseurl }}/assets/img/color-cartography/color-wheels-and-ranges.svg "La roda ajuda a pensar relacions de to, mentre que els rangs indiquen convencions habituals de codificació numèrica; cada programa pot presentar canals o percentatges amb variants, i cap dels dos recursos substitueix la prova sobre la figura final. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="54rem"}

### RGB, CMYK, RYB i HSL/HSV

RGB descriu la combinació additiva de llum utilitzada habitualment en monitors, projectors, telèfons, tauletes i altres dispositius que emeten llum. Cada canal, en la codificació més comuna de 8 bits, pren valors de `0` a `255`; el negre és `RGB(0,0,0)` perquè no s'emet llum, i el blanc és `RGB(255,255,255)` perquè els canals vermell, verd i blau se sumen al màxim. Els codis HEX expressen el mateix model de manera compacta: `#226699` equival a `R=34`, `G=102`, `B=153`. Aquesta notació és pràctica per transportar colors entre QGIS, fulls de càlcul, SVG i webs.

>>> **Identificar un gris en RGB.** Quan una pipeta retorna tres canals empatats, el color no té cap component cromàtic dominant i es llegeix com un gris neutre. `RGB(0,0,0)` és negre, `RGB(255,255,255)` és blanc, `RGB(128,128,128)` és un gris mitjà i `#cccccc`, equivalent a `RGB(204,204,204)`, és un gris clar. En HSL o HSV aquest mateix principi apareix com a saturació `0%`: el to deixa de ser informatiu i la lluminositat o el valor indiquen si el gris és més clar o més fosc. Si els canals no estan empatats, com a `RGB(120,120,138)`, ja no és un gris neutre, sinó un gris amb dominant blavosa.

CMYK correspon a un procés subtractiu d'impressió amb tintes cian, magenta, groga i el canal `K`. A diferència d'una pantalla, el paper no emet llum: reflecteix la llum que rep, i cada tinta n'absorbeix una part. Per això el blanc no s'obté afegint tinta, sinó deixant el suport sense cobrir. Els canals s'expressen habitualment de `0%` a `100%`, però la conversió RGB-CMYK depèn del perfil de color, del paper, de les tintes i del sistema d'impressió, de manera que no garanteix una equivalència perceptiva exacta.

El canal `K` no s'anomena així perquè sigui simplement la lletra final de *black*. En arts gràfiques identifica la **planxa clau** o *key plate*, que habitualment porta tinta negra i aporta registre, detall i contrast. El text petit acostuma a imprimir-se només amb `K` per evitar problemes de registre entre planxes; les superfícies fosques grans poden utilitzar un **negre ric**, que combina `K` amb proporcions controlades de cian, magenta o groc. No s'ha de substituir cap d'aquestes solucions per una superposició improvisada dels canals {% cite brownColourBasicsGIS2002 %}.

El model **RYB** --vermell, groc i blau-- és útil per entendre una tradició artística de mescla de pigments i algunes harmonies cromàtiques, però no descriu amb precisió ni la llum de les pantalles ni la quadricromia d'impressió. No té un rang numèric universal comparable al de RGB o CMYK. Els selectors **HSL** i **HSV** organitzen el color al voltant de to, saturació i lluminositat o valor: `H` sol anar de `0` a `360` graus, i `S`, `L` o `V` de `0%` a `100%`. Són pràctics per ajustar una paleta perquè permeten pensar en decisions perceptives, encara que els seus components no coincideixin exactament amb la percepció humana ni amb el valor semiològic d'una rampa cartogràfica.

HSL i HSV faciliten ajustar una paleta de manera intuïtiva separant decisions de to, saturació i claredat o intensitat. Tot i això, els seus components no són mesures perceptivament uniformes i no substitueixen la comprovació final sobre el mapa, el gràfic, la pantalla o la impressió.

![Comparació esquemàtica dels models RGB, CMYK, RYB i HSL/HSV, amb la funció principal de cada model en el treball amb mapes i figures]({{ site.baseurl }}/assets/img/color-cartography/color-models-overview.svg "RGB descriu llum emesa per pantalles i dispositius; CMYK descriu tintes sobre paper i utilitza K com a planxa clau; RYB pertany a la tradició artística; HSL i HSV separen to, saturació i lluminositat o valor per ajustar paletes. Els esquemes mostren principis de lectura, no una conversió colorimètrica exacta. Figura d'elaboració pròpia, revisada el 15 d'agost de 2026."){: data-figure-width="54rem"}

El projecte conservarà els valors RGB o HEX de la paleta per mantenir una definició coherent entre el full de càlcul, QGIS i Inkscape. Si el producte s'ha d'imprimir, caldrà revisar una prova o la conversió requerida pel sistema d'impressió; canviar el mode de color no garanteix per si sol una correspondència perceptiva exacta.

La reproductibilitat tècnica d'una paleta no determina què significa el color ni com l'interpretarà un públic concret.

## Aprenentatge, cultura i significats del color

La biologia restringeix quins estímuls podem discriminar, però aprenem a anomenar-los, agrupar-los i recordar-los dins d'una llengua i unes pràctiques. Les categories cromàtiques poden influir en l'atenció, la classificació i la memòria, sobretot prop de fronteres entre categories, però no determinen completament què pot veure una persona. Per tant, no s'ha de convertir la relació entre llengua i color en una versió forta del determinisme lingüístic {% cite witzelColourCategories2019 %}.

En algunes tasques, el coneixement d'un objecte i les expectatives sobre la il·luminació poden desplaçar modestament els judicis sobre l'aparença. Aquests efectes apresos operen sobre un sistema perceptiu que ja integra adaptació, context i constància parcial {% cite fosterColorConstancy2011 %}.

Els significats semàntics i institucionals també s'aprenen. Una associació pot ser habitual en una cultura, un territori o un sector professional i canviar en un altre context; fins i tot dins d'un mateix lloc, el color d'una alerta, un partit, una línia de transport o un contenidor depèn d'una convenció. El disseny cartogràfic pot aprofitar codis coneguts, però els ha de comprovar amb el públic i la llegenda en lloc de presentar-los com a universals {% cite brownColourBasicsGIS2002 pellicerColorLenguajeCartografico1993 %}.

### Associacions en vista zenital

Una paleta qualitativa pot aprofitar **colors associatius** quan la relació és compartida i facilita la lectura. En cartografia, aquesta associació no sempre reprodueix el color frontal o material de l'objecte; sovint reprodueix la manera com el fenomen s'identifica en una vista zenital o en una convenció cartogràfica. La vegetació es representa habitualment amb verd encara que els troncs dels arbres siguin marrons, perquè el que domina des de dalt és la capçada. Una terra llaurada pot rebre un taronja o un marró clar encara que el sòl variï molt segons humitat, roca o cultiu. L'aigua pot aparèixer en blau encara que una ortofoto mostri tons grisos, verdosos o foscos. El sòl urbà pot utilitzar grisos o vermells apagats per distingir construcció, paviment i xarxa viària sense confondre'ls amb una temperatura o un risc.

Aquestes associacions ajuden sobretot en mapes de referència, usos del sòl, cobertes, serveis coneguts o esquemes turístics. Però no qualsevol associació és adequada. Si una categoria secundària rep un color massa intens, pot dominar la lectura. Si una convenció local es presenta com universal, pot confondre lectors d'altres contextos. I si el mateix color s'utilitza alhora com a identitat visual i com a classe temàtica, la llegenda deixa de ser inequívoca.

### Codis semàntics i identitat visual

Els codis semàntics funcionen de manera semblant. El vermell pot suggerir alerta, prohibició, aturada o temperatura elevada; el verd pot suggerir pas, vegetació o sostenibilitat; els colors del reciclatge poden variar segons el territori i el sistema de gestió; i una paleta corporativa pot identificar una universitat, una destinació o un esdeveniment. En una infografia del curs, aquests codis poden ajudar l'orientació visual, però no han de substituir la paleta analítica.

Si el blau d'una marca s'utilitza alhora per representar el valor més baix d'un indicador, el lector pot no saber si llegeix identitat, categoria o quantitat. La decisió correcta no consisteix a evitar qualsevol color institucional, sinó a reservar-lo per a accents, capçaleres o elements de jerarquia quan la paleta de dades ja té una funció pròpia.

![Sis exemples esquemàtics d'usos del color: associatiu, semàntic, identitat visual, reciclatge, paleta temàtica de dades i risc d'estereotip]({{ site.baseurl }}/assets/img/color-cartography/associative-semantic-colors.svg "Els colors associatius i semàntics poden accelerar la lectura, però només són útils si el codi és pertinent, compartit i compatible amb el tipus de dada. Les mostres són exemples conceptuals, no manuals corporatius ni logotips oficials. Figura d'elaboració pròpia, 14 d'agost de 2026."){: data-figure-width="48rem"}

## Paletes segons el tipus de dada

La primera decisió no és quin color agrada més, sinó quina pregunta ha de respondre la figura. Una paleta per separar tipus de recurs turístic no pot suggerir una jerarquia que les dades no tenen; una paleta per representar intensitat ha de mostrar ordre; una paleta per comparar desviacions necessita un centre amb significat; i un color d'accent només és honest si destaca una condició definida.

>>>>> Aquesta fase vincula la funció de la paleta amb l'estructura de la dada abans de triar colors concrets.
>>>>>
>>>>> - Classificar una variable com a nominal, ordinal o quantitativa segons el nivell de mesura.
>>>>> - Identificar separadament si l'estructura analítica de la paleta ha de ser seqüencial, divergent o binària segons la pregunta plantejada.
>>>>> - Proposar colors candidats o una rampa i el tractament dels valors nuls sense fixar el nombre definitiu de classes ni els punts de tall abans del capítol de cartografia temàtica.
>>>>> - Rebutjar rampes o accents que destaquin llindars i oposicions absents de les dades.

### Paletes qualitatives

Les paletes qualitatives permeten diferenciar categories sense suggerir un ordre que les dades no tenen. Els tons han de ser distingibles, tenir una importància visual semblant quan cap categoria és prioritària i limitar-se a un nombre que continuï sent llegible al mapa i a la llegenda. Si hi ha massa categories, el problema pot no ser la paleta, sinó la necessitat d'agrupar categories o canviar la pregunta.

Una paleta qualitativa pot combinar to, forma i textura quan les marques són petites o quan el document pot circular en grisos. Aquesta redundància evita que la lectura depengui d'una diferència cromàtica mínima.

En un projecte turístic, una paleta qualitativa pot separar tipus de recurs, com allotjament, restauració, patrimoni, platja o oficina d'informació, sempre que cap color sembli "més alt" que un altre. També pot diferenciar mitjans de transport, cobertes del sòl o categories administratives. En canvi, no seria adequada per representar places d'allotjament per habitant, perquè aquest indicador demana una lectura ordenada.

### Paletes seqüencials

Les paletes seqüencials representen intensitat mitjançant una progressió perceptible i són habituals en percentatges, ràtios i densitats. El sentit clar-fosc o fosc-clar ha de coincidir amb l'ordre de la llegenda, i les classes adjacents han de continuar sent diferenciables a la mida final.

Una rampa multicolor no esdevé seqüencial pel sol fet de recórrer molts tons. Si la lluminositat puja, baixa i torna a pujar, dos valors distants poden semblar pròxims i un canvi cromàtic brusc pot destacar un llindar que les dades no contenen. La [referència de mapes de color de Matplotlib](https://matplotlib.org/3.9.2/gallery/color/colormap_reference.html) mostra que entre les opcions disponibles hi ha les rampes de tipus arc de Sant Martí `rainbow` i `jet`. Aquestes rampes són un cas habitual de manca de monotonia i no s'utilitzaran per representar una magnitud ordenada {% cite wilkeFundamentalsDataVisualization2019 nunezOptimizingColormaps2018 %}.

Els usos típics del curs són coropletes de percentatge d'habitatges d'ús turístic, places d'allotjament per 1.000 habitants, densitat de pernoctacions o proporció d'ocupació. Si la dada és un recompte absolut, cal pensar abans si convé normalitzar-la, utilitzar símbols proporcionals o explicar per què la comparació territorial continua sent justa.

### Paletes divergents

Les paletes divergents mostren desviacions respecte d'un punt de referència explícit, com una mitjana, un objectiu o un valor zero amb significat analític. No s'han d'utilitzar només per obtenir més varietat cromàtica. El centre ha de tenir una interpretació territorial, i els dos costats de la paleta han de permetre comparar la magnitud de les desviacions.

Quan una dada només té valors positius i no hi ha cap referència central significativa, una paleta divergent pot induir una lectura falsa: el lector pot entendre que hi ha dos fenòmens oposats quan en realitat només hi ha valors baixos i alts d'un mateix indicador.

Una paleta divergent és útil per mostrar municipis per sota o per sobre de la mitjana comarcal, canvis positius i negatius respecte d'un any base, desviacions respecte d'un objectiu de sostenibilitat o diferències entre oferta i demanda quan el zero separa dues situacions interpretables. Si el centre és només el valor mig de la classificació i no una referència analítica, la paleta pot semblar més precisa del que és.

### Paletes binàries i d'accent

Una paleta binària diferencia dues situacions, com presència/absència, compleix/no compleix o dins/fora. També pot destacar una categoria sobre un fons neutral. Aquest recurs és potent, però ha de respondre a una decisió clara: si el mapa destaca municipis per sobre d'un llindar, el llindar ha de tenir sentit analític i constar a la llegenda.

Els accents cromàtics serveixen per conduir la mirada cap a una dada, una anotació o una conclusió. No han de crear una segona classificació implícita ni competir amb el codi principal. Una regla pràctica és que el color d'accent hauria de poder-se explicar en una frase: destaca el territori d'estudi, assenyala un valor de referència o connecta peces que parlen del mateix fenomen.

En una infografia del projecte, un accent pot marcar la comarca analitzada dins de Catalunya, els municipis costaners dins d'una sèrie comarcal o els municipis que superen un llindar acordat. La resta d'elements han de quedar visibles però subordinats. Si l'accent serveix només per "fer bonic", el lector pot atribuir-li un significat que la dada no té.

![Quatre exemples esquemàtics de paletes segons el tipus de dada: qualitativa per a categories de recursos, seqüencial per a quantitats relatives, divergent per a desviacions respecte d'una mitjana i binària o d'accent per a llindars]({{ site.baseurl }}/assets/img/color-cartography/palette-data-type-examples.svg "La funció de la paleta depèn de la pregunta: distingir categories, ordenar intensitats, comparar desviacions o destacar una condició definida; els exemples són esquemàtics i s'han d'adaptar a les dades turístiques i territorials concretes. Figura d'elaboració pròpia, 15 d'agost de 2026."){: data-figure-width="54rem"}

::: table "Tipus de dada i paleta cromàtica"
| Tipus de dada o decisió | Paleta adequada | Criteri principal | Risc habitual |
| --- | --- | --- | --- |
| Categoria nominal | Qualitativa | Tons distingibles sense ordre aparent | Massa categories o importàncies visuals desiguals |
| Categoria ordinal | Seqüencial discreta | Ordre perceptible entre classes | Fer servir tons sense progressió de valor |
| Quantitat relativa | Seqüencial | Lluminositat ordenada i classes diferenciables | Rampa arc de Sant Martí o contrast insuficient |
| Desviació respecte d'un valor | Divergent | Centre significatiu i braços equilibrats | Crear oposicions que les dades no tenen |
| Presència o llindar | Binària o accent | Dues situacions definides explícitament | Ocultar la resta de valors o triar un llindar arbitrari |
:::

## Seleccionar, registrar i transportar paletes

[ColorBrewer](https://colorbrewer2.org/) ofereix esquemes qualitatius, seqüencials i divergents pensats per a cartografia, amb advertiments sobre impressió, pantalles i deficiències de visió cromàtica {% cite harrowerColorBrewerOnline2003 brewerColorBrewerPrint2003 %}. La interfície permet escollir el tipus de dada, el nombre de classes, el sistema de codis i diverses comprovacions, com esquemes aptes per a daltonisme, impressió o còpia en blanc i negre. El seu valor docent no és només triar colors: obliga a vincular paleta, nombre de classes i funció de lectura.

![Interfície de ColorBrewer amb una paleta seqüencial BuGn de cinc classes, mapa de prova carregat i opcions de seguretat cromàtica, context i exportació de codis]({{ site.baseurl }}/assets/img/color-cartography/colorbrewer-2026-08-14.png "ColorBrewer ajuda a escollir paletes cartogràfiques segons tipus de dada, nombre de classes i condicions de reproducció. Captura pròpia retallada de ColorBrewer 2.0, Cynthia A. Brewer i Mark Harrower, The Pennsylvania State University, 15 d'agost de 2026; reproduïda per a comentari docent."){: data-figure-width="54rem"}

[Adobe Color](https://color.adobe.com/), en canvi, és una eina general de disseny que permet explorar rodes cromàtiques, comprovar contrastos, extreure paletes d'imatges i crear combinacions per a productes gràfics o identitat visual. Pot ser útil per treballar accents, coherència visual o relacions de marca, però no substitueix un criteri cartogràfic sobre dades ordenades, nuls, classes i accessibilitat.

![Mostres de paletes ColorBrewer i paletes científiques seqüencials, divergents i qualitatives]({{ site.baseurl }}/assets/img/color-cartography/palette-reference-swatches.svg "Comparació d'elaboració pròpia basada en esquemes ColorBrewer de set classes i en mostres de viridis, magma i cividis distribuïdes amb Matplotlib. Les rampes científiques, originalment contínues, es discretitzen aquí només per facilitar la comparació docent."){: data-figure-width="48rem"}

El registre de color del projecte indicarà, com a mínim, el nom de la paleta si procedeix, els codis HEX o RGB de cada classe, el significat assignat a cada color i la prova d'accessibilitat realitzada. Aquesta anotació evita que el color es refaci "a ull" en passar d'Excel a QGIS o d'un PDF importat a Inkscape. També permet detectar contradiccions abans que la infografia quedi maquetada.

## Contrast, accessibilitat i coherència

Una paleta seleccionada segons el tipus de dada encara s'ha de provar en les condicions reals de lectura. El contrast amb el fons, la mida de les marques i la continuïtat dels codis entre peces poden confirmar o invalidar la selecció inicial.

>>>>> Aquesta fase comprova que el color continuï transmetent la mateixa estructura en diferents lectors, suports i peces del projecte.
>>>>>
>>>>> - Comprovar el contrast de classes, etiquetes, límits, fons i valors nuls a la mida final.
>>>>> - Verificar l'ordre perceptiu en escala de grisos i amb una simulació de deficiències de visió cromàtica.
>>>>> - Afegir forma, patró, etiqueta o posició quan el color sol no garanteixi una distinció essencial.
>>>>> - Detectar significats cromàtics contradictoris entre gràfics, mapes i infografia.
>>>>> - Ajustar la paleta i documentar el motiu dels canvis després de les proves.

### Comprovar a la mida final

Una paleta ha de funcionar en la mida i el suport finals. No s'ha de confiar només en diferències cromàtiques subtils ni en combinacions problemàtiques per a part del públic. Les classes han de mantenir un ordre perceptible en escala de grisos, quan l'ordre és important, i s'han de revisar amb una simulació de deficiències de visió cromàtica disponible en una eina adequada.

El color no treballa aïlladament. El contrast amb el fons, els límits, les etiquetes i els símbols superposats pot reforçar o anul·lar una diferència. Els territoris sense dades necessiten un tractament neutral i recognoscible que no es confongui amb el valor més baix de la sèrie.

### Codificació redundant

Quan una categoria sigui essencial, convé aplicar una **codificació redundant** i no confiar exclusivament en el color. En un diagrama de dispersió es poden combinar to i forma; en línies o mapes es poden afegir etiquetes directes, patrons o una jerarquia textual. Aquesta redundància és especialment útil quan els símbols són petits, les categories se superposen, el document s'imprimeix en grisos o dues classes resulten similars sota una deficiència de visió cromàtica {% cite wilkeFundamentalsDataVisualization2019 %}.

### Coherència entre gràfics, mapes i infografia

Una mateixa categoria o idea ha de conservar un tractament cromàtic compatible en totes les peces de la infografia. Aquesta coherència no obliga a aplicar la mateixa paleta sencera a qualsevol figura. Obliga a evitar contradiccions, com utilitzar un mateix blau per a habitatge principal en un gràfic i per a habitatge no principal en un altre. Els colors seleccionats i la seva funció es registraran abans de la composició final.

La coherència cromàtica també ajuda a separar tres llenguatges que sovint es barregen: el color de les dades, el color de la marca o del territori i el color de la decoració. Si aquests nivells no es distingeixen, el lector pot interpretar un accent gràfic com si fos una classe de dades.

## Activitat: preparar el registre cromàtic del projecte

La demostració guiada converteix els criteris del capítol en decisions que es podran reutilitzar en la resta del projecte. Es conservarà el llibre del capítol 3 i es crearà `tigit-07-teoria-color.xlsx`, que afegirà el full `palette` i mantindrà editables els gràfics previs. El registre no serà una llista externa: els codis i les funcions del color quedaran al mateix llibre que alimenta les figures.

>>>>> L'activitat prepara una paleta reproduïble sobre un gràfic i deixa documentats els criteris que després s'aplicaran al mapa temàtic.
>>>>>
>>>>> - Inventariar les funcions del color per a dades, nuls, accents, fons, límits i text.
>>>>> - Capturar o seleccionar colors i registrar-ne els codis HEX i RGB exactes.
>>>>> - Crear al `README.md` el registre cromàtic amb funcions, origen, comprovacions i ajustos.
>>>>> - Aplicar un color neutre i un accent redundant per a Vila-seca al gràfic ordenat i conservar la prova en SVG i PDF vectorials.
>>>>> - Validar la prova en grisos i amb simulació cromàtica.

### Entrades i resultats del registre cromàtic

Per començar es disposa dels gràfics del capítol de semiologia gràfica. La demostració separa tres nivells: colors de context i identitat per a fons, text o accents; colors qualitatius per distingir sèries; i rampes seqüencials o divergents pensades per a dades cartogràfiques. Barrejar aquests nivells pot convertir un color institucional o decoratiu en una classe de dades sense justificació.

Els resultats de treball són la secció `## Registre cromàtic` al `README.md`, el full `palette` del llibre i una prova aplicada al gràfic ordenat. Totes les barres comparables mantindran un color neutre; Vila-seca podrà rebre un accent que també s'indicarà amb etiqueta o contorn perquè la distinció no depengui només del color. La rampa seqüencial destinada a la coropleta es provarà com una tira de mostres, però els intervals de classe no es fixaran fins al capítol 8.

La pràctica d'aquest capítol prepararà les decisions de color que s'utilitzaran després en gràfics, cartografia temàtica, QGIS i infografia. No es tracta d'escollir una paleta definitiva per gust, sinó de documentar opcions compatibles amb el tipus de dada i provar-les sobre peces reals o mostres controlades.

### Inventariar funcions del color

Abans d'obrir un selector cromàtic, s'identificaran les funcions del color dins del projecte: categories de gràfics, rampa per a l'indicador principal, tractament dels nuls, accents de jerarquia, fons, límits i text. Cada funció tindrà un nom i no es reutilitzarà un color amb significats incompatibles.

### Capturar una mostra amb la pipeta

La pràctica inclou la captura d'un color a partir d'una mostra visual. La pipeta o selector de color de programes com GIMP o Inkscape permet llegir el codi d'un píxel i convertir una impressió visual en una definició transportable, com un valor HEX o RGB. L'exercici pot partir d'una mostra facilitada pel professorat, per exemple el logotip de la URV, i serveix per entendre que reproduir un color no consisteix a triar-ne un de semblant, sinó a registrar-ne el codi i aplicar-lo de manera coherent.

El procediment serà breu. Primer s'obrirà la imatge de mostra i s'escollirà una zona plana del color, evitant vores, ombres, antialiasing i píxels semitransparents. Després es capturarà el color amb la pipeta i s'anotarà el valor HEX i, si el programa el mostra, els canals RGB. Finalment es reproduirà el mateix color en almenys dos objectes diferents, com un rectangle d'Inkscape, una cel·la d'un full de càlcul o una capa simbòlica de QGIS. Si es treballa amb un logotip institucional real, el color capturat d'una imatge web només serveix com a exercici tècnic: per a una publicació oficial caldrà consultar sempre el manual d'identitat o els fitxers originals proporcionats per la institució.

### Seleccionar i provar paletes

La selecció inicial inclourà una paleta seqüencial per a l'indicador relatiu principal, una paleta qualitativa per a categories o elements de referència i un color d'accent per al territori d'estudi o per a una anotació. També fixarà els colors de nuls, fons, límits i text. En aquest capítol, les paletes es provaran sobre un gràfic candidat del capítol de semiologia gràfica; la prova sobre una capa municipal i la classificació definitiva es faran després, en la cartografia temàtica.

[Adobe Color](https://color.adobe.com/) es pot utilitzar per explorar harmonies, extreure colors d'una imatge o construir una paleta de context. L'estudiant copiarà els codis HEX escollits a les files `adobe_candidate` del full `palette` i n'indicarà la funció prevista. Aquest origen no demostra que la paleta sigui adequada per representar dades ordenades. Per a mapes, [ColorBrewer](https://colorbrewer2.org/) ajudarà a seleccionar rampes segons tipus de dada, nombre de classes i condicions d'impressió o accessibilitat.

### Registrar codis i decisions

El registre cromàtic indicarà:

1. funció de cada color dins del projecte;
2. tipus de dada al qual s'aplica;
3. codi HEX i canals RGB exactes;
4. origen de la paleta, mostra capturada o criteri de construcció;
5. programa utilitzat per obtenir o comprovar el color, si escau;
6. resultat de la prova en escala de grisos o simulació cromàtica;
7. ajustos aplicats i motiu.

El full calcularà els canals RGB a partir del codi HEX. Si `E2` conté `#D55E00`, les fórmules compatibles amb Calc i Excel 365 són:

```text
=HEX2DEC(MID(E2,2,2))
=HEX2DEC(MID(E2,4,2))
=HEX2DEC(MID(E2,6,2))
```

També convertirà els canals sRGB a valors lineals per calcular luminància relativa i contrast aproximat amb blanc i negre. Aquest càlcul ajuda a detectar textos o símbols problemàtics, però no substitueix la prova sobre la mida, el fons i la geometria reals. Les files conservaran camps per a la prova en grisos, la simulació de deficiències cromàtiques i les notes de revisió.

La paleta qualitativa d'edats s'aplicarà a les barres apilades; el gràfic ordenat mantindrà totes les barres amb un gris blavós neutral i destacarà Vila-seca amb un taronja que també queda identificat pel text; i la piràmide utilitzarà dos colors divergents. Les mostres BuGn i RdBu es conservaran com a candidates per als mapes, però no fixaran encara els punts de tall.

### Evidències del registre cromàtic

::: table "Evidències del registre cromàtic"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `README.md` | Registre cromàtic | Funcions, codis HEX o RGB, origen de la paleta o mostra i comprovacions realitzades |
| `data/processed` | `tigit-07-teoria-color.xlsx` | Full `palette`, fórmules HEX/RGB, luminància, contrast, files Adobe Color i mostres ColorBrewer |
| `outputs/figures` | `palette-proof-non-principal-housing-tarragones-2021.svg` i `.pdf` | Color neutre, accent redundant de Vila-seca, colors i textos vectorials comprovables |
| `captures` | Comprovació a Inkscape | Un objecte vectorial seleccionat i el codi HEX o RGBA visible al panell d'emplenat i contorn |
:::

La decisió cromàtica quedarà preparada quan es pugui reconstruir en un altre programa i explicar per què cada color ajuda la lectura. Els capítols de cartografia i SIG utilitzaran aquest registre per classificar i simbolitzar el mapa temàtic municipal sense redissenyar la paleta a ull.
