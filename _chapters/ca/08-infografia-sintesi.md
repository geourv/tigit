---
layout: manual-chapter
title: Infografia i síntesi territorial
description: Integració de dades, gràfics, mapes, textos i fonts en una composició final amb Inkscape.
lang: ca
ref: manual-infographic-synthesis
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/infografia-sintesi/
weight: 90
part: Continguts
manual_references: true
---

La infografia és la síntesi del recorregut, no una decoració afegida al final. Ha de respondre una pregunta territorial mitjançant dades traçables, indicadors adequats, gràfics i mapes coherents, i una interpretació breu que diferenciï els resultats de les hipòtesis. Els repertoris d'infografia poden inspirar formes de síntesi, però s'han de llegir críticament: una peça espectacular no és necessàriament una explicació clara o verificable {% cite mccandlessInformacionBella2010 tufteVisualDisplay2001 %}.

En aquest manual, una **infografia** és una composició que integra text i representacions visuals per explicar una pregunta coherent. La **síntesi territorial** és l'argument que construeix amb dades, indicadors, gràfics, mapes i context. La composició només serà defensable si conserva la **traçabilitat**, és a dir, si permet reconstruir l'origen de les dades, les transformacions, els càlculs i les decisions.

## Definir el missatge

### Pregunta, públic i suport

Abans de maquetar cal concretar què ha d'entendre el lector, quina informació necessita i en quin format consultarà el document. La pregunta territorial s'ha de poder formular en una sola frase, i el suport final ha de tenir una mida i una orientació definides. Una composició pensada per a una pàgina no es pot convertir automàticament en una diapositiva o una pantalla petita sense revisar-ne la jerarquia.

El públic condiciona el context necessari. Una persona que no conegui el Tarragonès pot necessitar un mapa de situació; una persona que no conegui l'indicador necessita una definició i una unitat. Adaptar-se al públic no significa simplificar fins a perdre precisió, sinó fer visibles els coneixements que no es poden donar per suposats.

### Seleccionar evidències

No tots els càlculs i mapes del projecte han d'aparèixer al resultat final. Se seleccionaran les peces que contribueixen a una mateixa explicació.

La miniinfografia comarcal integrarà, com a orientació estable del manual:

- tres o quatre mètriques de capçalera calculades al llibre;
- dues o tres figures seleccionades entre les alternatives del capítol 3;
- un mapa temàtic municipal;
- un mapa de context, si és necessari per situar la comarca;
- una interpretació breu i una limitació rellevant.

Cada peça seleccionada ha de complir una funció. Si retirar una figura no debilita l'argument, probablement era redundant. Si una afirmació no es pot relacionar amb una dada, un mapa, un gràfic o una font preservada, no està prou sostinguda per aparèixer com a conclusió.

### Pregunta, evidència i límit

La síntesi es pot organitzar mitjançant tres elements. La **pregunta** delimita el fenomen i el territori; l'**evidència** mostra el patró principal amb indicadors, figures i mapes; i el **límit** indica què no es pot concloure amb aquestes dades. Aquesta estructura evita tant l'acumulació de peces sense missatge com una conclusió més contundent que els resultats.

Per exemple, el percentatge d'habitatge no principal pot mostrar contrastos municipals, però no identifica directament habitatges turístics ni explica per què es produeixen. La infografia pot descriure la distribució, relacionar-la amb altres indicadors i formular hipòtesis prudents, però ha de mantenir visible aquesta limitació.

## Arquitectura de la informació

### Títol, entrada i conclusió

La **jerarquia visual** organitza contrastos, posicions, mides i espais per indicar l'ordre de lectura i la importància relativa dels elements. El títol ha de formular el tema amb precisió i ocupar un nivell coherent amb aquesta funció. Una entrada breu situa la pregunta i la conclusió interpreta el patró sense repetir totes les xifres. Títols genèrics com «Anàlisi del Tarragonès» no indiquen què s'estudia; un títol informatiu identifica la relació entre població, habitatge, municipis i període.

La conclusió ha de destacar una o dues relacions sostingudes per les peces visibles. No és un resum de totes les operacions realitzades ni una enumeració de programes. Les decisions tècniques que afecten la lectura s'expliquen en notes o en la documentació del projecte, mentre que el cos principal manté el fil territorial.

### Relació entre mapa, gràfic i text

El mapa mostra la distribució espacial, el gràfic reforça una comparació i el text explica el significat i els límits. Les tres peces no han de competir ni explicar històries contradictòries.

El mapa no és adequat per ordenar amb precisió tots els municipis, i el gràfic no conserva el veïnatge geogràfic. La combinació és útil quan cada peça resol una limitació de l'altra. Repetir el mateix rànquing en un mapa, una barra i una taula ocupa espai sense aportar una lectura nova.

### Fonts, unitats i notes metodològiques

La composició ha d'identificar les fonts i proporcionar el context mínim per entendre els indicadors, el territori i el període. Les notes han de distingir la font estadística de la cartogràfica i conservar l'autoria de la composició. Si una limitació altera la interpretació, no s'ha d'amagar en un text il·legible al peu.

Les abreviatures, unitats i categories s'han d'explicar on es llegeixen. Un percentatge ha d'identificar el total de referència; una densitat, la unitat de superfície; i una classificació cartogràfica, els intervals utilitzats. La font no substitueix aquestes definicions.

## Activitat: construir la miniinfografia

La composició partirà dels resultats verificats, no de captures de pantalla ni de valors transcrits a mà. Si es detecta un error, la correcció s'ha de fer al llibre, al gràfic o al projecte QGIS d'origen i després s'ha de repetir l'exportació corresponent.

### Inventariar i validar les peces

Abans d'obrir Inkscape es prepararà un inventari d'entrades:

::: table "Entrades acumulades de la miniinfografia"
| Origen | Peça | Comprovació abans d'importar |
| --- | --- | --- |
| Capítol 2 | Mètriques del full `indicators` | Fórmula, unitat, període i agregació comarcal |
| Capítol 3 | Dues o tres figures vectorials | Pregunta pròpia, valors contrastats i mida llegible |
| Capítol 6 | Mapa de context, si és necessari | Extensió, retolació, fonts i escala |
| Capítol 7 | Mapa temàtic final | Camp, classes, paleta, llegenda i absències |
| Capítol 8 | Text d'interpretació | Observació, evidència, hipòtesi prudent i limitació |
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

Cada figura o mapa s'importarà com una peça identificable, es mantindrà agrupada i es redimensionarà amb la proporció bloquejada. Els recursos es deixaran incrustats al document final o, si han de continuar enllaçats durant el treball, es conservaran dins de la carpeta del projecte i se'n comprovarà la ruta abans de lliurar. Aquesta decisió evita que el document mostri espais buits quan s'obre en un altre ordinador.

Un mapa o un gràfic no s'ha d'estirar per omplir un espai, perquè es deformarien les proporcions i els símbols. Si la peça no encaixa, cal revisar-ne la mida d'exportació, la composició o l'esquema general. Les imatges ràster inevitables s'ampliaran al 100% de la mida final per comprovar que no presenten pixelació; en un producte imprès, una fotografia hauria de conservar aproximadament 300 píxels per polzada a la mida utilitzada.

### Tipografia i jerarquia

Famílies, cossos, pesos i espaiat han de distingir nivells d'informació sense multiplicar estils innecessaris. Una jerarquia compacta pot resoldre's amb una o dues famílies, pocs pesos i una escala coherent per al títol, subtítols, cos, etiquetes i fonts.

La tipografia es comprovarà a la mida real del document. Reduir les fonts per encabir una peça massa carregada no resol el problema d'arquitectura. Primer s'han d'eliminar redundàncies, escurçar textos i donar més espai a la informació prioritària.

### Color i coherència

La paleta definida al capítol anterior s'aplicarà de manera consistent. El disseny general no ha d'alterar el significat dels colors del mapa o dels gràfics. Els colors d'accent s'utilitzaran per reforçar la jerarquia, no per competir amb la codificació quantitativa.

Cap informació essencial dependrà només del color. Les etiquetes, la posició, les formes o els patrons poden aportar redundància quan sigui necessària, i el contrast entre text i fons s'ha de revisar a la mida i al suport finals.

## Interpretació territorial

### Descriure abans d'explicar

El text identificarà patrons visibles abans de proposar-ne causes. Una associació espacial o gràfica no demostra per si mateixa una relació causal.

Una interpretació breu es pot construir en cinc moviments:

1. **observació:** identificar el contrast o la distribució visible;
2. **evidència:** indicar l'indicador, els municipis o la magnitud que sostenen l'observació;
3. **interpretació:** proposar-ne un significat territorial prudent;
4. **límit:** precisar què no permet demostrar la font o l'indicador;
5. **connexió:** relacionar el resultat amb la figura següent o amb la conclusió.

No cal convertir aquests moviments en cinc frases rígides. Serveixen per evitar una explicació causal sense evidència o una descripció que només repeteixi la llegenda.

### Explicitar límits i incertesa

Les limitacions de les fonts, els indicadors, la classificació i l'escala han de formar part de la interpretació quan afectin la conclusió.

Una limitació útil és específica. Expressions genèriques com «les dades poden tenir errors» aporten poc. En canvi, indicar que l'habitatge no principal agrupa habitatges d'ús ocasional i buits explica per què el mapa no es pot interpretar directament com una distribució d'habitatges turístics.

## Revisió del producte i del procés

### Revisió del contingut

La primera revisió comprovarà que totes les peces comparteixen territori, període, definicions i unitats compatibles. Cada afirmació s'ha de poder relacionar amb una evidència visible o amb un fitxer preservat. També es revisaran ortografia, xifres, topònims, fonts i notes metodològiques.

### Revisió visual i d'accessibilitat

La segona revisió es farà a mida real. Es comprovaran el recorregut de lectura, les alineacions, l'espai, el contrast, la tipografia i la capacitat de distingir símbols sense dependre només del color. Una persona que no hagi participat en la maquetació intentarà identificar la pregunta, el resultat principal i la limitació sense una explicació oral prèvia. Les tres respostes, els dubtes i els canvis que se'n derivin s'anotaran al registre de revisió.

Com a criteri del projecte, quan el format ho permeti, el document incorporarà metadades bàsiques com títol, autoria, descripció i paraules clau. El `README.md` conservarà també una descripció textual breu de la pregunta, el resultat i la limitació. Aquest text es podrà reutilitzar com a alternativa quan la infografia es publiqui en un entorn que admeti una descripció accessible.

### Revisió tècnica i exportació

Abans d'exportar es comprovaran la mida i l'orientació de la pàgina, els objectes fora dels límits, els recursos enllaçats, les proporcions de mapes i gràfics, el gruix dels traços i la resolució de les imatges. En el PDF, les tipografies s'han d'incrustar o substituir per una alternativa disponible; la comprovació es farà obrint el fitxer en un altre visor o entorn, no només a Inkscape.

El fitxer exportat s'obrirà fora d'Inkscape. Ha de contenir la pàgina prevista, mantenir colors i transparències, mostrar tots els recursos i continuar sent llegible a la mida final. El nom distingirà el document editable, la versió de revisió i el lliurable; `final_final.pdf` no és una política de versions.

### Auditoria abans/després

Cada projecte conservarà una versió intermèdia i la contrastarà amb la versió final. La revisió haurà d'identificar canvis observables: eliminació d'una figura redundant, reordenació de blocs, ampliació d'un mapa massa petit, simplificació de la paleta, millora de les fonts o reescriptura d'una conclusió massa contundent.

::: table "Auditoria de la infografia"
| Criteri | Pregunta de revisió |
| --- | --- |
| Focus | Es pot resumir la pregunta principal en una frase? |
| Coherència | Mapa, gràfic i text parlen del mateix territori, període i fenomen? |
| Jerarquia | El lector sap per on començar i què és secundari? |
| Integritat | Les escales, unitats i classificacions permeten una lectura honesta? |
| Traçabilitat | Es poden identificar fonts, càlculs i fitxers de treball? |
| Llegibilitat | El document funciona a la mida i al suport de lliurament? |
| Interpretació | Se separen descripció, hipòtesi, conclusió i limitacions? |
:::

### Traçabilitat i autoria

La infografia ha d'estar sostinguda per l'únic llibre de càlcul, el projecte QGIS, el document d'Inkscape i les fonts originals. Cal poder explicar les operacions i decisions principals, també quan el producte s'ha elaborat en grup.

El `README.md` relacionarà cada component visible amb el fitxer d'origen: rang o full del llibre per a les mètriques, PDF o SVG per a les figures, composició QGIS per als mapes i document editable per al muntatge. Aquesta relació permet corregir una peça sense perdre la procedència ni introduir versions paral·leles.

### Preparació de la presentació

La presentació oral, quan correspongui, no repetirà tot el document ni enumerarà eines. Seguirà un argument breu: pregunta territorial, dades seleccionades, indicador i decisions visuals, resultat principal i limitacions. La guia docent permet una presentació individual o en grup segons indiqui el professorat, però no fixa la mida dels equips, la durada ni el suport; aquestes condicions es concretaran a Moodle.

### Evidències que s'han de conservar

::: table "Evidències de la síntesi territorial"
| Ubicació | Evidència | Contingut mínim |
| --- | --- | --- |
| `data/processed` | Llibre canònic | Fonts, transformacions, fórmules, indicadors i mètriques finals |
| `qgis` | Projecte QGIS | Unions, estils, classificació, etiquetes i composicions |
| `outputs/figures` | Figures seleccionades | Exportacions vectorials utilitzades a la composició |
| `outputs/maps` | Mapes seleccionats | Mapes vectorials finals i alternativa temàtica conservada |
| `outputs` | Document d'Inkscape | Màster editable amb retícula, textos i peces importades |
| `outputs` | Versió intermèdia | Estat utilitzat per a l'auditoria abans/després |
| `dist` | Exportació final | Pàgina verificada en el format de lliurament |
| Arrel | `README.md` | Inventari, procedència, decisions, prova de lectura, descripció textual, metadades i limitacions conegudes |
:::

## Resultat del capítol

El resultat serà una miniinfografia comarcal completa i exportada en el format indicat a Moodle. Per revisar el procés es conservaran el llibre únic, el CSV `map_export`, el projecte QGIS, el document d'Inkscape, les figures i mapes vectorials, les fonts originals i el `README.md`. El lliurable final quedarà a `dist`; els fitxers editables i les alternatives continuaran a les carpetes de treball corresponents. Moodle indicarà quins d'aquests fitxers s'han de trametre en cada lliurament.
