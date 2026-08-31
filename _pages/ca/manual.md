---
layout: manual-home
title: Tècniques d'informació geogràfica i turística
description: >
  En aquesta assignatura s'aprèn a passar d'un conjunt de dades territorials i turístiques a una explicació breu construïda amb indicadors, gràfics i mapes. Es treballa amb dades oficials i obertes, un full de càlcul, QGIS i Inkscape.
lang: ca
ref: home
profiles: [unaltremanual]
content_status: draft
permalink: /ca/
nav: false
show_chapter_index: false
cover_image: /assets/img/manual-cover-ca.png
cover_alt: Manual de Tècniques d'informació geogràfica i turística
figure_captions: true
---

## Què és aquesta assignatura

Tècniques d'informació geogràfica i turística és una assignatura de primer curs per aprendre a treballar amb dades que descriuen territoris i activitats turístiques. L'assignatura combina tres tipus de feina: calcular mesures amb un full de càlcul, representar informació amb gràfics i mapes, i explicar amb paraules què mostren els resultats i quins límits tenen.

Suposem que volem comparar la població i els habitatges dels municipis d'una comarca. Podem preguntar, per exemple, on hi ha més habitatge no principal, si aquest pes és igual en municipis grans i petits o quin patró territorial formen els valors. Una taula descarregada d'un organisme oficial encara no respon aquestes preguntes: primer cal entendre les columnes, comprovar les dades, calcular una mesura comparable i triar una representació que no indueixi a error.

Durant el curs es farà aquest recorregut amb dades oficials i obertes. S'utilitzaran Calc o Excel per preparar dades i calcular indicadors, QGIS per relacionar-les amb el territori i construir mapes, i Inkscape per reunir els resultats en una composició final. **No es tracta de memoritzar botons**, sinó d'entendre quin problema resol cada operació i com es pot comprovar que el resultat és correcte.

## Responsabilitats del professorat i de l'estudiantat

A les sessions de teoria, el professorat presentarà els conceptes necessaris per entendre les dades i prendre decisions: què compara un percentatge, per què un mapa necessita un sistema de coordenades o com canvia la lectura quan es trien uns colors o uns altres. També analitzarà exemples i errors habituals perquè els criteris d'una solució ben plantejada quedin clars sense dependre del programa.

A les sessions pràctiques, el professorat mostrarà com s'apliquen aquests criteris amb els fitxers i les eines del curs. Ajudarà a diagnosticar errors, revisarà resultats intermedis i indicarà quines comprovacions falten. La pràctica no consistirà només a reproduir una demostració: caldrà prendre decisions, conservar els fitxers de treball i justificar el resultat obtingut.

El curs introduirà les eines des de les operacions bàsiques. S'espera de l'estudiantat un treball regular: portar els fitxers necessaris, mantenir-los ordenats, completar les activitats, preguntar quan un resultat no s'entengui i aplicar les correccions rebudes. Tant en el treball individual com en grup, **cal poder explicar d'on provenen les dades, què s'ha calculat i per què s'ha triat una representació determinada**.

## El projecte del curs

El manual utilitza com a demostració comuna els municipis del Tarragonès i dades de població i habitatge de l'Idescat de 2021. Vila-seca serà el municipi de referència dins d'aquesta comarca. Es començarà amb les fonts originals i la feina es conservarà en un mateix projecte. Primer es crearà un fitxer de full de càlcul amb diversos fulls; Calc i Excel anomenen **llibre de càlcul** aquest tipus de fitxer. A continuació, QGIS servirà per gestionar la informació geogràfica, relacionar les dades estadístiques amb els límits municipals i elaborar mapes. Finalment, Inkscape permetrà combinar mapes, gràfics, textos i altres elements en una composició gràfica més elaborada.

>>>> **La demostració docent i el territori assignat no són el mateix.** El parell **Tarragonès–Vila-seca** queda reservat al professorat per mostrar el procediment complet. Cada trio rebrà un altre parell **comarca–municipi**: diversos equips poden treballar el Tarragonès, però cadascun tindrà un municipi de referència diferent, mentre que altres equips treballaran una altra comarca i un municipi d'aquella comarca. Cada equip haurà d'adaptar les dades, els noms dels fitxers, els gràfics, els mapes i la infografia al parell assignat; no haurà de reproduir com a projecte propi el cas del professorat.

**El projecte del curs culminarà en una infografia territorial** amb tres o quatre dades destacades, dues o tres peces visuals i una interpretació breu. El resultat final conservarà també el llibre de càlcul revisable, els gràfics i els mapes editables perquè sigui possible comprovar com s'ha construït la infografia.

El producte no es construeix d'una sola vegada. Cada fase afegeix una peça que serà necessària més endavant:

::: table "Què es construeix en cada fase del projecte comarcal"
| Fase | Què es prepararà i es conservarà |
| --- | --- |
| Fonts i preparació | Un llibre de càlcul amb les dades originals, un diccionari, les comprovacions i una fila per municipi |
| Indicadors | Percentatges, ràtios i densitats calculats al mateix fitxer |
| Gràfics | Figures editables per comparar valors, distribucions i evolucions |
| Color | Paletes amb una funció definida, codis registrats i proves bàsiques d'accessibilitat |
| Dades espacials | Límits municipals documentats i sistemes de coordenades comprovats |
| SIG | Un projecte QGIS que uneix la taula municipal amb el mapa i permet revisar la correspondència |
| Llenguatge cartogràfic | Un mapa de context amb escala, retolació i jerarquia llegibles |
| Cartografia temàtica | Un mapa d'un indicador comparable, amb classes, colors i llegenda justificats |
| Síntesi | Una infografia composta amb Inkscape que reuneix les peces seleccionades i n'explica el resultat |
:::

### Per què el mapa no és el punt de partida

Un mapa pot semblar acabat encara que parteixi d'una columna equivocada, d'un percentatge mal calculat o d'una unió incompleta. Per això comprovarem les fonts i els codis, calcularem els indicadors i només representarem les dades quan sapiguem què significa cada valor. Si al final apareix una incoherència, tornarem al pas on s'ha originat en lloc de corregir només l'aspecte del gràfic o del mapa.

## Com treballarem a classe

**La teoria i la pràctica tractaran el mateix problema des de dos moments diferents.** Quan estudiem un percentatge, per exemple, a teoria veurem què compara i quin denominador necessita. A la pràctica localitzarem les columnes adequades, escriurem la fórmula al full de càlcul i comprovarem què passa si falta una dada o el denominador és zero. El resultat de la pràctica servirà després per construir un gràfic o un mapa sense haver de repetir el càlcul des del principi.

### Com plantejar un dubte

**Els dubtes s'han de plantejar tan aviat com apareguin.** Al començament de cada sessió convé comentar les preguntes sorgides durant la lectura, la pràctica anterior o la preparació dels fitxers. Aquest intercanvi permet detectar dificultats compartides, aclarir dubtes, corregir errors i beneficiar tot el grup amb la resposta.

Quan el dubte no quedi resolt a l'aula, **el canal recomanat és el fòrum de dubtes de Moodle**. Una pregunta publicada al fòrum i la resposta corresponent poden ser útils per a altres persones que es trobin amb el mateix problema. Si el fòrum no és suficient o la consulta inclou una situació individual que no convé fer pública, el pas següent és escriure un correu i, si cal, acordar una tutoria.

El missatge s'ha d'enviar des del **correu institucional** i ha d'identificar l'estudiant amb nom, cognoms, titulació i grup. L'assumpte ha d'indicar l'assignatura i el tema concret. El cos del missatge ha d'incloure una pregunta elaborada, els passos o recursos que ja s'han provat, el resultat que s'esperava i el resultat obtingut; quan sigui necessari, s'hi pot afegir un fitxer, una captura o un enllaç que permeti reproduir el problema. Un missatge com «no em funciona» no aporta prou informació per diagnosticar-ne la causa. **El professorat decidirà si el dubte es pot respondre per correu o si és preferible treballar-lo en una tutoria.**

![Circuit de dubtes: sessió, fòrum de Moodle, correu i tutoria]({{ site.baseurl }}/assets/diagrams/course-question-flow.mmd.svg "Els dubtes es comenten a l'inici de la sessió. Si no es resolen, es traslladen al fòrum de Moodle; si encara persisteixen, s'envia un correu institucional documentat i el professorat respon o proposa una tutoria."){: data-figure-width-web="31rem" data-figure-width-pdf="80%"}

### Com utilitzar aquest manual

Per preparar una pràctica cal llegir la introducció de la fase i identificar la pregunta, els fitxers que s'utilitzaran i el resultat que cal obtenir. Durant la sessió, es pot consultar el procediment quan calgui i convé anotar al projecte les decisions que no quedin visibles al resultat. En acabar, **no n'hi ha prou amb comprovar que el fitxer existeix**: cal tornar-lo a obrir, revisar els criteris indicats al capítol i comprovar que se'n podria explicar la procedència.

No totes les indicacions del curs són en aquest manual. Cal consultar cada espai segons la informació necessària:

::: table "On trobar cada tipus d'informació"
| Espai | Què s'hi troba |
| --- | --- |
| Manual | Explicacions, exemples, procediments i criteris per revisar la feina |
| Moodle | Què toca fer cada setmana, avisos, dates, enunciats, fitxers de lliurament i qualificacions |
| Guia docent | Organització oficial de l'assignatura, activitats d'avaluació i condicions generals |
:::

## Avaluació

L'avaluació combina evidències complementàries del procés i del resultat. El treball continuat a l'aula permet observar el seguiment de les activitats, la resolució de dubtes i la incorporació de correccions; les proves individuals comproven la comprensió dels continguts i l'aplicació dels criteris amb el full de càlcul i QGIS; i el producte final mostra si aquestes decisions es poden integrar en una síntesi territorial traçable. Les dates, els enunciats i els fitxers que s'han de lliurar es publicaran a Moodle. La guia docent fixa els blocs i els pesos següents:

### Primera convocatòria

::: table "Blocs d'avaluació de la primera convocatòria"
| Activitat | Pes | Com es farà |
| --- | --- | --- |
| Pràctiques a través de TIC en aules informàtiques | 5% | Seguiment, exercicis i evidències intermèdies indicades a Moodle |
| Presentació, exposició o infografia territorial | 30% | Projecte de síntesi en trios mixtos |
| Atenció personalitzada | 5% | Participació, resolució de dubtes i incorporació de correccions |
| Prova mixta de continguts | 30% | Prova individual de comprensió teòrica i aplicació de criteris |
| Prova pràctica de full de càlcul | 15% | Prova individual sobre preparació de dades, codis i indicadors |
| Prova pràctica de QGIS | 15% | Prova individual sobre unions, simbolització i resolució cartogràfica |
:::

Per seguir l'itinerari ordinari d'avaluació continuada **cal assistir almenys al 80% de les sessions pràctiques** o justificar adequadament les absències, fer un seguiment regular de la resta de sessions i lliurar les activitats intermèdies indicades a Moodle. **Una activitat principal amb una nota inferior a 4 sobre 10 no es pot compensar automàticament amb les altres notes.**

La prova de continguts comprovarà la capacitat d'interpretar indicadors, llegir gràfics, detectar problemes visuals, entendre sistemes de referència i valorar decisions cartogràfiques. Les dues proves pràctiques comprovaran la capacitat de preparar una taula i calcular indicadors, d'una banda, i d'incorporar dades a QGIS, unir-les amb una capa i simbolitzar-les, de l'altra.

**La infografia territorial serà el producte de síntesi.** Els trios hauran de combinar estudiants de Geografia i de Turisme: no poden estar formats per tres persones de la mateixa titulació. La infografia integrarà dades traçables, indicadors justificats, dues o tres peces visuals entre gràfics i mapes, i una interpretació breu dins d'una composició elaborada amb Inkscape. Qualsevol membre del grup haurà de poder explicar les fonts, els càlculs, les unions, els mapes i les decisions visuals principals.

### Segona convocatòria

La recuperació depèn del seguiment de l'avaluació continuada i de les parts pendents després de la primera convocatòria:

::: table "Què cal recuperar en segona convocatòria"
| Situació després de la primera convocatòria | Recuperació prevista |
| --- | --- |
| S'ha seguit l'avaluació continuada, però una activitat principal té una nota inferior a 4 | Caldrà recuperar aquesta activitat o el bloc suspès; les parts superades es conservaran |
| S'ha seguit l'avaluació continuada, però la mitjana no arriba a 5 | Caldrà recuperar les parts necessàries per assolir el nivell mínim |
| El projecte de síntesi està pendent de recuperació | Caldrà elaborar una infografia o un document equivalent de manera individual i amb un abast més reduït |
| No s'ha seguit l'avaluació continuada amb l'assistència i la participació requerides | Caldrà recuperar el conjunt de l'assignatura; no es conservaran activitats ni blocs parcials de la primera convocatòria i les infografies exigides seran individuals |
:::

Moodle indicarà en cada cas el territori, les dades, el format, el termini i els criteris concrets de la recuperació. La preparació exigeix comprovar quina situació de la taula correspon.

### Referència oficial

**La guia docent és la referència normativa de l'assignatura.** Si hi ha discrepàncies sobre percentatges, condicions d'avaluació o instruccions administratives, prevalen la guia docent i les indicacions publicades a Moodle.

::: table "Dades identificatives de les guies docents 2026_27"
| Camp | Valor |
| --- | --- |
| Assignatura | Tècniques d'informació geogràfica i turística |
| Guia docent | [Grau en Geografia, Anàlisi Territorial i Sostenibilitat](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2123&assignatura=21234003&any_academic=2026_27) |
| Codi | 21234003 |
| Guia docent | [Grau en Gestió en Turisme i Hoteleria](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&any_academic=2026_27) |
| Codi | 21224102 |
| Curs | Primer |
| Període | 1Q |
| Crèdits | 6 ECTS |
| Departament | Geografia |
:::

## Preparació de les eines i els fitxers

**Cal familiaritzar-se amb el sistema de fitxers de l'ordinador**: crear carpetes, reconèixer una ruta, moure i copiar fitxers, identificar una extensió i saber en quin dispositiu o servei està desat un document. Aquestes operacions formen part del treball acadèmic, encara que les aplicacions mòbils i els serveis al núvol sovint les ocultin.

::: table "Eines principals i paper dins del curs"
| Eina | Paper dins del curs |
| --- | --- |
| Full de càlcul | Depurar dades, tractar codis territorials, calcular indicadors i preparar gràfics |
| QGIS | Unir taules i capes, simbolitzar indicadors i elaborar mapes temàtics |
| Inkscape | Compondre la infografia i coordinar mapes, gràfics, textos i jerarquia visual |
| Fonts oficials de dades | Proporcionar població, habitatges, codis territorials, superfícies i límits administratius |
| VirtLabs | Accedir remotament a aplicacions acadèmiques quan no es disposa d'un entorn local |
| Moodle | Gestionar avisos, terminis, lliuraments, qualificacions i instruccions operatives |
:::

### Entorn de treball local i VirtLabs {#installacio-programari}

**Es recomana arribar a les pràctiques que utilitzen cada eina amb LibreOffice, QGIS i Inkscape instal·lats a l'ordinador personal o portàtil.** Treballar amb un entorn propi permet practicar entre sessions, gestionar carpetes i rutes, conservar els projectes i resoldre incidències habituals. LibreOffice instal·la la suite completa, dins de la qual **Calc** és l'aplicació de full de càlcul que s'utilitzarà al manual.

Les versions següents són les referències verificades l'agost de 2026. S'han escollit versions estables i, en el cas de QGIS, la versió de suport prolongat perquè prioritza l'estabilitat i la compatibilitat durant el curs.

::: table "Programari recomanat per seguir les pràctiques"
| Programari | Versió de referència | Descàrrega oficial |
| --- | --- | --- |
| LibreOffice Calc | LibreOffice 26.8.0, versió estable | [Descarregar LibreOffice](https://www.libreoffice.org/download/download-libreoffice/) |
| QGIS Desktop | QGIS 3.44 LTR «Solothurn»; versió 3.44.13 en aquesta revisió | [Descarregar QGIS](https://qgis.org/download/) |
| Inkscape | Inkscape 1.4.4, versió estable | [Descarregar Inkscape](https://inkscape.org/release/) |
:::

Per descarregar el programari cal comprovar a la pàgina oficial que la versió continua marcada com a **estable** o **LTR** i triar l'instal·lador corresponent al sistema operatiu i a l'arquitectura de l'ordinador. Si el projecte publica una actualització de manteniment dins de la mateixa branca, convé instal·lar-la. Les versions de prova, desenvolupament o compilació nocturna només són adequades per experimentar i no constitueixen l'entorn de referència del curs.

La URV proporciona llicències i serveis institucionals, i també permet accedir a aplicacions acadèmiques mitjançant [VirtLabs](https://virtlabs.urv.cat/login). Aquest entorn virtual és una alternativa quan no es pot instal·lar el programari necessari o quan cal accedir-hi des d'un altre equip. No substitueix, però, la conveniència de disposar d'un entorn local sempre que sigui possible: en cada activitat cal comprovar on es desen els fitxers, com es recuperaran en una altra sessió i quines limitacions té l'entorn utilitzat.

### Fulls de càlcul recomanats

A les pràctiques es pot utilitzar qualsevol full de càlcul que permeti assolir els objectius i conservar un llibre interoperable. Es recomana **LibreOffice Calc** quan es vol treballar localment amb programari lliure. Quan cal editar al núvol o simultàniament, es recomana **Excel per al web dins de Microsoft 365** perquè la URV proporciona aquest entorn a la comunitat universitària.

La [guia d'Office 365 del CRAI](https://urv.libguides.com/Office365), actualitzada el febrer de 2026, documenta l'accés web a Excel i altres aplicacions, així com la possibilitat d'instal·lar les aplicacions d'escriptori fins a cinc ordinadors personals. La [guia institucional de OneDrive](https://urv.libguides.com/c.php?g=684760&p=4891187) descriu un espai personal URV al núvol, actualment de 1 TB, que permet crear, editar i compartir llibres d'Excel i treballar-hi simultàniament. S'hi accedeix mitjançant els serveis digitals de la URV, inclòs [virtual.urv.cat](https://virtual.urv.cat/). Les quotes, aplicacions i condicions poden canviar, de manera que s'ha de consultar la documentació institucional vigent.

Google Sheets, ONLYOFFICE, Apple Numbers i altres opcions també cobreixen operacions bàsiques, però no seran l'entorn de referència del manual. Si s'utilitzen, cal comprovar que fórmules, tipus, gràfics i exportacions es conserven quan el llibre s'intercanvia amb Calc o Excel.

### Saber on és el fitxer

Una aplicació pot mostrar un llibre sense fer evident on està desat. La llista de fitxers **recents** és només un índex d'accessos: no és una carpeta ni informa necessàriament de quin compte, dispositiu o núvol conté el fitxer. L'Escriptori tampoc no garanteix una ubicació local, perquè el sistema pot sincronitzar-lo amb OneDrive.

::: table "Ubicacions que no s'han de confondre"
| Ubicació | Com reconèixer-la | Risc que cal controlar |
| --- | --- | --- |
| Carpeta local | Té una ruta dins del disc de l'ordinador i es pot obrir amb el gestor de fitxers | Es pot perdre si falla o es canvia el dispositiu i no hi ha còpia |
| OneDrive personal | La sessió correspon a un compte particular | El grup pot dependre d'un compte aliè a la URV i d'un propietari únic |
| OneDrive URV | La sessió correspon al compte institucional i el fitxer apareix al OneDrive de la URV | L'accés depèn del compte institucional i dels permisos compartits |
| Carpeta sincronitzada | Té una ruta local però també un estat de sincronització al núvol | Pot estar disponible només en línia, pendent de pujada o generar conflictes |
| Escriptori o Baixades | La ubicació depèn de la configuració del sistema i del navegador | Acumula còpies, noms duplicats i fitxers difícils de tornar a localitzar |
:::

>>>> **“El veig a Recents” no demostra que se sàpiga on és.** Cal identificar la ruta local o el compte de OneDrive, obrir la carpeta des del gestor de fitxers i comprovar el nom complet del llibre. Un OneDrive personal i el OneDrive proporcionat per la URV són espais diferents, encara que l'aplicació els mostri junts.

Per treballar amb seguretat, el projecte tindrà una carpeta arrel identificable. Després de la primera sessió s'ha de poder tancar l'aplicació, navegar fins a la carpeta sense usar **Recents** i tornar a obrir el llibre. Si es treballa al núvol, no s'ha d'apagar l'ordinador fins que s'hagin comprovat el compte actiu, els permisos de les persones participants i l'estat de sincronització.

Compartir un enllaç no és el mateix que lliurar un fitxer. Quan Moodle demani un fitxer, s'ha de descarregar o exportar la versió correcta, verificar que s'obre fora de la sessió del navegador i trametre-la en el format indicat. Els enllaços compartits només substituiran el fitxer quan les instruccions ho demanin explícitament.

Amb l'entorn i la carpeta de treball preparats, la fase següent començarà formulant la pregunta territorial i localitzant les fonts oficials que permetran construir la primera taula municipal. Aquesta base serà el punt d'origen de tots els indicadors, gràfics i mapes posteriors.
