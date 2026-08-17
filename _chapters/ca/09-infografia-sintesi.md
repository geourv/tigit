---
layout: manual-chapter
title: Infografia i síntesi territorial
description: Integració de dades, gràfics, mapes, textos i fonts en una composició final amb Inkscape.
lang: ca
ref: manual-infographic-synthesis
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/infografia-sintesi/
weight: 100
part: Continguts
manual_references: true
---

La infografia és la síntesi del recorregut, no una decoració afegida al final. Ha de respondre una pregunta territorial mitjançant dades traçables, indicadors adequats, gràfics i mapes coherents, i una interpretació breu que diferenciï els resultats de les hipòtesis. Els repertoris d'infografia poden inspirar formes de síntesi, però s'han de llegir críticament: una peça espectacular no és necessàriament una explicació clara o verificable {% cite mccandlessInformacionBella2010 tufteVisualDisplay2001 %}.

En aquest manual, una **infografia** és una composició que integra text i representacions visuals per explicar una pregunta coherent. La **síntesi territorial** és l'argument que construeix amb dades, indicadors, gràfics, mapes i context. La composició només serà defensable si conserva la **traçabilitat**, és a dir, si permet reconstruir l'origen de les dades, les transformacions, els càlculs i les decisions.

>>>>> En acabar el capítol, cal poder transformar els resultats verificats del projecte en una miniinfografia territorial clara, traçable i llegible.
>>>>>
>>>>> - Formular un missatge que relacioni una pregunta territorial i una evidència principal, i explicitar com una limitació específica n'acota o modifica la conclusió.
>>>>> - Seleccionar dues o tres peces visuals en total, inclosos els mapes, segons la funció que compleixen en l'argument.
>>>>> - Organitzar mètriques, mapes, gràfics, textos i fonts mitjançant una jerarquia i un recorregut de lectura recognoscibles.
>>>>> - Decidir si cal incorporar el mapa de context i aplicar el registre cromàtic sense crear codis contradictoris ni peces redundants.
>>>>> - Construir un màster SVG editable i generar un PDF de revisió i un PDF final verificat fora d'Inkscape.
>>>>> - Validar pregunta, resultat, limitació i llegibilitat mitjançant una prova amb una persona lectora.

## Definir el missatge

La síntesi comença delimitant què ha d'entendre el lector i quines evidències permeten sostenir-ho sense exagerar-ne l'abast.

>>>>> Aquesta fase converteix els resultats disponibles en un missatge territorial concret i contrastable.
>>>>>
>>>>> - Formular la pregunta, el públic i el suport final abans de maquetar.
>>>>> - Redactar un resultat principal vinculat a dades o peces visuals identificables.
>>>>> - Distingir observacions, interpretacions prudents i afirmacions que les dades no permeten sostenir.
>>>>> - Comparar on el mapa i el gràfic coincideixen, difereixen o matisen el missatge territorial.
>>>>> - Explicitar una limitació que modifiqui o acoti la lectura del resultat.

### Pregunta, públic i suport

Abans de maquetar cal concretar què ha d'entendre el lector, quina informació necessita i en quin format consultarà el document. La pregunta territorial s'ha de poder formular en una sola frase, i el suport final ha de tenir una mida i una orientació definides. Una composició pensada per a una pàgina no es pot convertir automàticament en una diapositiva o una pantalla petita sense revisar-ne la jerarquia.

El públic condiciona el context necessari. Una persona que no conegui el Tarragonès pot necessitar un mapa de situació; una persona que no conegui l'indicador necessita una definició i una unitat. Adaptar-se al públic no significa simplificar fins a perdre precisió, sinó fer visibles els coneixements que no es poden donar per suposats.

### Seleccionar evidències

No tots els càlculs i mapes del projecte han d'aparèixer al resultat final. Se seleccionaran les peces que contribueixen a una mateixa explicació.

La miniinfografia comarcal integrarà, com a orientació estable del manual:

- tres o quatre mètriques de capçalera calculades al llibre;
- dues o tres peces d'evidència visual en total, seleccionades entre els gràfics i els mapes disponibles;
- el mapa temàtic municipal dins d'aquesta selecció quan sostingui el patró espacial;
- el mapa de context dins d'aquesta selecció si és necessari per situar la comarca;
- una interpretació breu i una limitació rellevant.

Cada peça seleccionada ha de complir una funció. Si retirar una figura no debilita l'argument, probablement era redundant. Si una afirmació no es pot relacionar amb una dada, un mapa, un gràfic o una font preservada, no està prou sostinguda per aparèixer com a conclusió.

>>>> **Seleccionar també pot distorsionar.** Una infografia pot ser formalment correcta i, alhora, orientar massa la lectura si només mostra les peces que reforcen una història prèvia. La lectura crítica de Jones i Monmonier ajuda a revisar aquesta selecció: quines dades han quedat fora, quina escala o classificació s'ha triat, quines absències es veuen i quin límit hauria d'acompanyar el resultat {% cite jonesHowLieCharts2018 monmonierHowLieMaps2018 %}.

![Infografia turística amb moltes xifres, gràfics, icones i blocs visuals, utilitzada com a material d'auditoria per revisar focus i jerarquia]({{ site.baseurl }}/assets/img/legacy/infographics-tourism.png "Una infografia carregada pot contenir moltes dades i, alhora, dificultar la pregunta principal, l'ordre de lectura, la unitat de cada valor i la relació entre peces. Llicència: pendent de revisar."){: data-figure-width="48rem"}

Una auditoria d'una peça densa comença per preguntar què recordaria el lector després de trenta segons. Si la resposta és només una impressió general, però no una relació territorial concreta, la composició encara no fa una síntesi. La densitat visual pot ser útil quan el document funciona com a consulta, però la miniinfografia del curs ha de prioritzar una pregunta i unes poques evidències. La resta del projecte continuarà existint als fitxers de treball i al `README.md`; no cal que tot aparegui a la pàgina final.

Un exemple més focalitzat és una infografia sobre animals sacrificats al món. La peça no tracta un cas turístic, però és útil per al capítol perquè mostra com una composició pot combinar mapa, cartodiagrama, símbols proporcionals, figures icòniques i text curt per conduir una lectura. Les dades de FAOSTAT de 2011 proporcionen la traçabilitat estadística; el disseny, en canvi, construeix una història visual sobre l'escala desigual del fenomen. La imatge forma part del *Meat Atlas 2014* {% cite chemnitzBechevaMeatAtlas2014 %}.

![Infografia sobre animals sacrificats al món, amb cercles proporcionals, siluetes, colors categòrics, barres verticals i mapes petits segons dades FAOSTAT 2011]({{ site.baseurl }}/assets/img/infographics/animals-slaughtered-worldwide-meat-atlas-2014.png "El cartodiagrama compost dona ordre de magnitud global amb bombolles, localitza països principals amb mapes petits i separa categories amb formes, colors i siluetes. Font estadística: FAOSTAT. Gràfica: Bartz/Stockmar, Meat Atlas 2014, p. 15, Heinrich Böll Foundation, Friends of the Earth Europe, BUND i Le Monde diplomatique, CC BY-SA 3.0; fitxer incorporat sense modificacions."){: data-figure-width="48rem"}

La força de la peça no depèn només de representar quantitats. Els cercles i les xifres grans fixen l'ordre de magnitud mundial, mentre que els mapes petits desplacen la lectura cap als països amb més pes en cada grup. El color actua sobretot com a codi categòric i, en alguns casos, associatiu; les siluetes dels animals reforcen la identificació quan la llegenda queda lluny. També és un bon exemple per discutir límits: la grandària dels cercles s'ha de llegir amb prudència si l'escala de mida no és explícita, i el relat visual ha de continuar distingint entre dada, selecció i interpretació.

Un altre tipus d'inspiració és una composició sobre les cent illes més grans del món. La peça no mostra les illes a la seva posició geogràfica real, sinó que les separa i les ordena per superfície perquè el lector pugui comparar formes, magnituds i relleu. Aquesta renúncia a la localització és una decisió comunicativa: no serveix per analitzar veïnatges, distàncies o rutes, però sí per fer visible una classificació territorial que en un mapa convencional quedaria dominada per la posició i per les dimensions extremes de Groenlàndia. L'[article d'Iman Ghosh a *Visual Capitalist*, amb una visualització dissenyada per David Garcia](https://www.visualcapitalist.com/visualizing-100-worlds-biggest-islands/) il·lustra aquesta estratègia.

![Infografia de les cent illes més grans del món, amb formes insulars separades, relleu ombrejat, colors climàtics i retolació individual]({{ site.baseurl }}/assets/img/infographics/100-largest-islands.png "La composició renuncia a la posició geogràfica per ordenar les illes per superfície, conservar-ne la forma recognoscible i afegir relleu i color com a codis de lectura. Font: David Garcia, Visual Capitalist, 2021."){: data-figure-width="42rem"}

Per al treball de curs, aquesta figura és útil perquè amplia el repertori d'idees sense imposar-ne l'estil. Una miniinfografia turística podria ordenar municipis, platges, equipaments o paisatges segons una magnitud i mantenir formes recognoscibles, però només si aquesta operació respon a la pregunta. La lliçó no és copiar l'efecte visual, sinó entendre què es guanya i què es perd quan una composició prioritza la comparació per damunt de la localització.

La selecció no consisteix a retallar dades fins que la pàgina respiri, sinó a assignar una funció a cada element. Una mètrica de capçalera dona ordre de magnitud; un mapa mostra patró espacial; un gràfic ordenat permet comparar municipis; una nota explica el límit de l'indicador; i les fonts permeten reconstruir el resultat. Quan dues peces fan la mateixa feina, se n'ha de conservar una o explicar per què la redundància ajuda la lectura. Quan una peça crida més l'atenció que el resultat principal, s'ha de redimensionar, simplificar o retirar.

### Pregunta, evidència i límit

La síntesi es pot organitzar mitjançant tres elements. La **pregunta** delimita el fenomen i el territori; l'**evidència** mostra el patró principal amb indicadors, figures i mapes; i el **límit** indica què no es pot concloure amb aquestes dades. Aquesta estructura evita tant l'acumulació de peces sense missatge com una conclusió més contundent que els resultats.

Per exemple, el percentatge d'habitatge no principal pot mostrar contrastos municipals, però no identifica directament habitatges turístics ni explica per què es produeixen. La infografia pot descriure la distribució, relacionar-la amb altres indicadors i formular hipòtesis prudents, però ha de mantenir visible aquesta limitació.

## Arquitectura de la informació

L'arquitectura tradueix el missatge en una seqüència visual i distribueix l'espai segons la funció de cada component.

>>>>> Aquesta fase ordena la informació perquè la pregunta, l'evidència i la interpretació es puguin seguir sense explicació oral.
>>>>>
>>>>> - Jerarquitzar títol, entrada, peces visuals, interpretació, limitació i fonts.
>>>>> - Combinar mapa, gràfic i text només quan aporten lectures complementàries.
>>>>> - Integrar el mapa de context quan sigui necessari per orientar el lector dins de la selecció total de peces.
>>>>> - Aplicar colors, tipografia, alineacions i espaiat d'acord amb el registre cromàtic i la funció informativa.
>>>>> - Comprovar que unitats, períodes, classificacions i fonts es llegeixen al lloc on s'interpreten.

### Títol, entrada i conclusió

La **jerarquia visual** organitza contrastos, posicions, mides i espais per indicar l'ordre de lectura i la importància relativa dels elements. El títol ha de formular el tema amb precisió i ocupar un nivell coherent amb aquesta funció. Una entrada breu situa la pregunta i la conclusió interpreta el patró sense repetir totes les xifres. Títols genèrics com «Anàlisi del Tarragonès» no indiquen què s'estudia; un títol informatiu identifica la relació entre població, habitatge, municipis i període.

La conclusió ha de destacar una o dues relacions sostingudes per les peces visibles. No és un resum de totes les operacions realitzades ni una enumeració de programes. Les decisions tècniques que afecten la lectura s'expliquen en notes o en la documentació del projecte, mentre que el cos principal manté el fil territorial.

>>>> **El títol no ha d'afirmar més que l'evidència.** Una frase com «el turisme buida els municipis interiors» exigiria dades sobre turisme, buidatge residencial, període i relació causal. Si la peça només mostra habitatge no principal i població resident, el títol ha de formular una lectura més prudent i verificable.

### Relació entre mapa, gràfic i text

El mapa mostra la distribució espacial, el gràfic reforça una comparació i el text explica el significat i els límits. Les tres peces no han de competir ni explicar històries contradictòries.

El mapa no és adequat per ordenar amb precisió tots els municipis, i el gràfic no conserva el veïnatge geogràfic. La combinació és útil quan cada peça resol una limitació de l'altra. Repetir el mateix rànquing en un mapa, una barra i una taula ocupa espai sense aportar una lectura nova.

### Fonts, unitats i notes metodològiques

La composició ha d'identificar les fonts i proporcionar el context mínim per entendre els indicadors, el territori i el període. Les notes han de distingir la font estadística de la cartogràfica i conservar l'autoria de la composició. Si una limitació altera la interpretació, no s'ha d'amagar en un text il·legible al peu.

Les abreviatures, unitats i categories s'han d'explicar on es llegeixen. Un percentatge ha d'identificar el total de referència; una densitat, la unitat de superfície; i una classificació cartogràfica, els intervals utilitzats. La font no substitueix aquestes definicions.

## Activitat: construir la miniinfografia

La demostració guiada reprèn tots els materials produïts fins aquí, en comprova la disponibilitat i en selecciona només els que sostenen una mateixa explicació territorial. Inventariar no significa incorporar-ho tot: la composició final combina dues o tres peces d'evidència visual en total, comptant conjuntament gràfics, coropletes, mapes de símbols i mapa de context.

>>>>> L'activitat construeix, revisa i exporta una miniinfografia a partir de peces verificades i editables.
>>>>>
>>>>> - Inventariar les peces disponibles i seleccionar-ne dues o tres en total, inclosos els mapes.
>>>>> - Compondre la síntesi en un màster SVG editable sense transcriure valors ni deformar figures importades.
>>>>> - Aplicar una retícula, una jerarquia tipogràfica i el registre cromàtic a la mida final.
>>>>> - Generar un PDF de revisió, provar-lo amb una persona lectora i registrar els canvis observables.
>>>>> - Exportar el PDF final i verificar-ne recursos, tipografies, colors, proporcions i llegibilitat fora d'Inkscape.

### Materials i resultats de treball

La composició comença amb les entrades acumulades disponibles: les fonts originals i el registre de procedència; el llibre canònic amb indicadors i mètriques; totes les figures candidates exportades; l'informe de la unió i el projecte QGIS compartit; el mapa de context; el registre cromàtic i la prova de paleta; la coropleta final i, si s'ha produït, el mapa de símbols proporcionals. L'alternativa controlada es consulta dins de QGIS com a evidència de comparació, no com una peça visible candidata. L'inventari permet validar i comparar les peces abans de seleccionar-ne dues o tres en total per a la composició, inclosos els mapes.

El flux guiat deixa un màster SVG editable, un PDF de revisió, un PDF final a `dist` i un registre al `README.md` que relaciona cada peça amb l'origen i recull la prova amb una persona lectora. S'utilitzen noms descriptius i reconstruïbles: `outputs/infografia_tarragones_2021.svg`, `outputs/infografia_tarragones_2021_review.pdf` i `dist/infografia_tarragones_2021.pdf`. L'any identifica el període de les dades, no l'any d'elaboració; els noms s'adapten al territori i al període real de cada projecte.

La composició partirà dels resultats verificats, no de captures de pantalla ni de valors transcrits a mà. Si es detecta un error, la correcció s'ha de fer al llibre, al gràfic o al projecte QGIS d'origen i després s'ha de repetir l'exportació corresponent.

### Inventariar i validar les peces

Abans d'obrir Inkscape es prepararà un inventari d'entrades:

::: table "Entrades acumulades de la miniinfografia"
| Origen | Peça | Comprovació abans d'importar |
| --- | --- | --- |
| Capítol 1 | Fonts originals i registre de procedència | Productor, recurs d'origen, llicència i traça fins a la dada preparada |
| Capítol 2 | Llibre canònic i mètriques del full `indicators` | Fitxer únic, fórmula, unitat, període i agregació comarcal |
| Capítol 3 | Figures vectorials candidates | Pregunta pròpia, valors contrastats i mida llegible |
| Capítol 5 | Informe de la unió i projecte QGIS compartit | Claus, cardinalitat, absències, casos contrastats i capa municipal unida |
| Capítol 6 | Mapa de context | Extensió, retolació, fonts i escala |
| Capítol 7 | Registre cromàtic i prova de paleta | Funcions, codis HEX i RGB, grisos i simulació cromàtica |
| Capítol 8 | Coropleta final i mapa de símbols proporcionals si s'ha produït; alternativa controlada editable com a comparació | Camps, classes o escala de mides, paleta, llegendes i absències; l'alternativa no és una peça visible candidata |
| Aquest capítol | Text d'interpretació | Observació, evidència, hipòtesi prudent i limitació |
:::

Totes les peces han de referir-se al mateix territori i a períodes compatibles. Els noms dels municipis, les unitats, els colors i les fonts es revisaran abans de maquetar, perquè una incoherència no es resol col·locant els elements en una mateixa pàgina.

### Formular l'argument

Es redactarà una frase per a la pregunta, una per al resultat principal i una per a la limitació. A continuació s'assignarà una funció a cada mètrica, figura i mapa. Les peces sense funció diferenciada es descartaran o es reservaran com a material de treball.

L'ordre de lectura ha de conduir de la pregunta a l'evidència i de l'evidència a la interpretació. No cal que coincideixi amb l'ordre cronològic en què es van produir els fitxers. La infografia explica un resultat territorial, no el dietari del procés.

### Construir un esquema de composició

Abans d'aplicar tipografies i colors es dibuixarà un esquema simple amb blocs per al títol, les mètriques, els gràfics, els mapes, la interpretació i les fonts. Aquest esquema permet comprovar si la peça principal disposa de prou espai i si el recorregut de lectura és recognoscible.

L'espai no s'ha de repartir de manera uniforme. El mapa o la figura que sosté el resultat principal pot ocupar més superfície; les fonts i notes poden ser secundàries sense deixar de ser llegibles. Si totes les peces tenen el mateix pes, la jerarquia desapareix.

### Document, retícula i marges

La configuració inicial del document determinarà la mida final, l'alineació i l'espai disponible per jerarquitzar continguts. La retícula estableix columnes, alineacions i separacions repetibles; els marges protegeixen la informació dels límits de la pàgina i de possibles talls d'impressió.

La retícula és una ajuda, no una obligació d'omplir totes les cel·les. Els elements relacionats han de compartir alineacions i proximitat, mentre que els blocs diferents necessiten separació suficient. Les guies no apareixeran a l'exportació final.

El document d'Inkscape es prepararà amb aquest procediment:

1. definir les unitats, la mida i l'orientació de la pàgina segons el suport final;
2. crear guies per als marges i les columnes de l'esquema aprovat;
3. separar fons, peces visuals, textos i elements auxiliars en capes o grups identificables;
4. col·locar primer els blocs principals i comprovar el recorregut abans d'ajustar-ne els detalls;
5. conservar una versió intermèdia quan l'arquitectura ja sigui recognoscible.

### Importar gràfics i mapes

Les peces exportades des del full de càlcul i QGIS s'incorporaran mantenint qualitat, proporcions i possibilitats d'edició quan el format ho permeti. Els PDF o SVG vectorials permeten ajustar alguns elements, però qualsevol canvi que alteri valors, classes o geometries s'ha de fer a l'aplicació d'origen.

Cada figura o mapa s'importarà com una peça identificable, es mantindrà agrupada i es redimensionarà amb la proporció bloquejada. Els recursos es deixaran incrustats al document final o, si han de continuar enllaçats durant el treball, es conservaran dins de la carpeta del projecte i se'n comprovarà la ruta abans de compartir-lo. Aquesta decisió evita que el document mostri espais buits quan s'obre en un altre ordinador.

Un mapa o un gràfic no s'ha d'estirar per omplir un espai, perquè es deformarien les proporcions i els símbols. Si la peça no encaixa, cal revisar-ne la mida d'exportació, la composició o l'esquema general. Les imatges ràster inevitables s'ampliaran al 100% de la mida final per comprovar que no presenten pixelació; en un producte imprès, una fotografia hauria de conservar aproximadament 300 píxels per polzada a la mida utilitzada.

### Tipografia i jerarquia

Famílies, cossos, pesos i espaiat han de distingir nivells d'informació sense multiplicar estils innecessaris. Una jerarquia compacta pot resoldre's amb una o dues famílies, pocs pesos i una escala coherent per al títol, subtítols, cos, etiquetes i fonts.

La tipografia es comprovarà a la mida real del document. Reduir les fonts per encabir una peça massa carregada no resol el problema d'arquitectura. Primer s'han d'eliminar redundàncies, escurçar textos i donar més espai a la informació prioritària.

### Color i coherència

La paleta definida als capítols de color i cartografia temàtica s'aplicarà de manera consistent. El disseny general no ha d'alterar el significat dels colors del mapa o dels gràfics. Els colors d'accent s'utilitzaran per reforçar la jerarquia, no per competir amb la codificació quantitativa.

Cap informació essencial dependrà només del color. Les etiquetes, la posició, les formes o els patrons poden aportar redundància quan sigui necessària, i el contrast entre text i fons s'ha de revisar a la mida i al suport finals.

Si la infografia adopta una identitat visual institucional, territorial o turística, aquesta identitat ha de quedar subordinada a la lectura de les dades. Els colors associats a una marca, una destinació, un esdeveniment o una universitat poden servir per a títols, separadors o accents, però no han de reassignar el significat d'una paleta seqüencial, divergent o qualitativa. Una peça sobre un municipi litoral pot utilitzar un accent blau per reforçar el context marítim; això no autoritza a utilitzar el mateix blau per a una classe concreta si després impedeix distingir l'indicador principal.

La coherència cromàtica també és una decisió d'autoria. Si el mapa utilitza una rampa de blaus per al percentatge d'habitatge no principal, els gràfics que representen el mateix indicador han de mantenir una relació recognoscible o explicar clarament el canvi. En canvi, les mètriques de capçalera, les notes o els elements d'orientació poden utilitzar neutres i accents per construir jerarquia sense afegir nous codis analítics. Aquesta separació evita que la infografia barregi tres llenguatges diferents: el de les dades, el de la marca i el de la decoració.

### Interpretació territorial

#### Descriure abans d'explicar

El text identificarà patrons visibles abans de proposar-ne causes. Una associació espacial o gràfica no demostra per si mateixa una relació causal.

Una interpretació breu es pot construir en cinc moviments:

1. **observació:** identificar el contrast o la distribució visible;
2. **evidència:** indicar l'indicador, els municipis o la magnitud que sostenen l'observació;
3. **interpretació:** proposar-ne un significat territorial prudent;
4. **límit:** precisar què no permet demostrar la font o l'indicador;
5. **connexió:** relacionar el resultat amb la figura següent o amb la conclusió.

No cal convertir aquests moviments en cinc frases rígides. Serveixen per evitar una explicació causal sense evidència o una descripció que només repeteixi la llegenda.

#### Explicitar límits i incertesa

Les limitacions de les fonts, els indicadors, la classificació i l'escala han de formar part de la interpretació quan afectin la conclusió.

Una limitació útil és específica. Expressions genèriques com «les dades poden tenir errors» aporten poc. En canvi, indicar que l'habitatge no principal agrupa habitatges d'ús ocasional i buits explica per què el mapa no es pot interpretar directament com una distribució d'habitatges turístics.

### Revisió del producte i del procés

#### Revisió del contingut

La primera revisió comprovarà que totes les peces comparteixen territori, període, definicions i unitats compatibles. Cada afirmació s'ha de poder relacionar amb una evidència visible o amb un fitxer preservat. També es revisaran ortografia, xifres, topònims, fonts i notes metodològiques.

#### Revisió visual i d'accessibilitat

La segona revisió es farà a mida real. Es comprovaran el recorregut de lectura, les alineacions, l'espai, el contrast, la tipografia i la capacitat de distingir símbols sense dependre només del color. Una persona que no hagi participat en la maquetació intentarà identificar la pregunta, el resultat principal i la limitació sense una explicació oral prèvia. Les tres respostes, els dubtes i els canvis que se'n derivin s'anotaran al registre de revisió.

Com a criteri del projecte, quan el format ho permeti, el document incorporarà metadades bàsiques com títol, autoria, descripció i paraules clau. El `README.md` conservarà també una descripció textual breu de la pregunta, el resultat i la limitació. Aquest text es podrà reutilitzar com a alternativa quan la infografia es publiqui en un entorn que admeti una descripció accessible.

#### Revisió tècnica i exportació

Abans d'exportar es comprovaran la mida i l'orientació de la pàgina, els objectes fora dels límits, els recursos enllaçats, les proporcions de mapes i gràfics, el gruix dels traços i la resolució de les imatges. En el PDF, les tipografies s'han d'incrustar o substituir per una alternativa disponible; la comprovació es farà obrint el fitxer en un altre visor o entorn, no només a Inkscape.

El fitxer exportat s'obrirà fora d'Inkscape. Ha de contenir la pàgina prevista, mantenir colors i transparències, mostrar tots els recursos i continuar sent llegible a la mida final. El nom distingirà el document editable, la versió de revisió i el document final; noms com `final_final.pdf` no permeten reconstruir el procés.

#### Auditoria abans/després

Cada projecte conservarà una versió intermèdia i la contrastarà amb la versió final. La revisió haurà d'identificar canvis observables: eliminació d'una figura redundant, reordenació de blocs, ampliació d'un mapa massa petit, simplificació de la paleta, millora de les fonts o reescriptura d'una conclusió massa contundent.

::: table "Auditoria de la infografia"
| Criteri | Pregunta de revisió |
| --- | --- |
| Focus | Es pot resumir la pregunta principal en una frase? |
| Coherència | Mapa, gràfic i text parlen del mateix territori, període i fenomen? |
| Jerarquia | El lector sap per on començar i què és secundari? |
| Selecció | Les peces descartades no canviarien la conclusió principal? |
| Afirmació | Cada títol o conclusió es pot relacionar amb una evidència visible? |
| Integritat | Les escales, unitats i classificacions permeten una lectura honesta? |
| Traçabilitat | Es poden identificar fonts, càlculs i fitxers de treball? |
| Llegibilitat | El document funciona a la mida i al suport de publicació? |
| Interpretació | Se separen descripció, hipòtesi, conclusió i limitacions? |
:::

#### Traçabilitat i autoria

La infografia ha d'estar sostinguda per l'únic llibre de càlcul, el projecte QGIS, el document d'Inkscape i les fonts originals. Cal poder explicar les operacions i decisions principals, també quan el producte s'ha elaborat en grup.

El `README.md` relacionarà cada component visible amb el fitxer d'origen: rang o full del llibre per a les mètriques, PDF o SVG per a les figures, composició QGIS per als mapes i document editable per al muntatge. Aquesta relació permet corregir una peça sense perdre la procedència ni introduir versions paral·leles.

#### Explicar la síntesi

Una explicació oral de la peça no repetirà tot el document ni enumerarà eines. Seguirà un argument breu: pregunta territorial, dades seleccionades, indicador i decisions visuals, resultat principal i limitacions.

#### Evidències que s'han de conservar

::: table "Evidències de la síntesi territorial"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/processed` | Llibre canònic | Fonts, transformacions, fórmules, indicadors i mètriques finals |
| `qgis` | Projecte QGIS | Unions, estils, classificació final, alternativa controlada editable, etiquetes i composicions |
| `outputs/figures` | Figures seleccionades | Exportacions vectorials utilitzades a la composició |
| `outputs/maps` | Mapes seleccionats | Mapes vectorials finals utilitzats a la composició |
| `outputs` | `infografia_tarragones_2021.svg` | Màster editable amb retícula, textos i peces importades |
| `outputs` | `infografia_tarragones_2021_review.pdf` | Estat intermedi utilitzat per a l'auditoria abans/després |
| `dist` | `infografia_tarragones_2021.pdf` | Pàgina final verificada fora d'Inkscape |
| Arrel | `README.md` | Llinatge de cada peça, inventari, procedència, decisions, prova de lectura, descripció textual, metadades i limitacions conegudes |
:::
