---
layout: manual-chapter
title: Dades territorials, informació turística i indicadors
description: Fonts de dades, codis territorials, depuració i construcció d'indicadors per al treball del curs.
lang: ca
ref: manual-data-indicators
profiles: [unaltremanual]
content_status: draft
permalink: /ca/chapters/dades-territorials-indicadors/
weight: 20
part: Continguts
manual_references: false
---

El primer bloc de continguts comença abans d'obrir QGIS. Qualsevol mapa temàtic depèn de les dades que el sostenen, i aquestes dades gairebé mai arriben preparades per representar-se directament. El treball inicial consisteix a entendre d'on ve la informació, què mesura, amb quin territori es pot relacionar i quines transformacions cal fer abans d'interpretar-la.

En turisme, aquesta qüestió és especialment important perquè els valors absoluts poden enganyar. Un municipi pot tenir moltes places turístiques perquè té molta població, perquè té molta superfície, perquè concentra una tipologia concreta d'allotjament o perquè forma part d'una dinàmica territorial més àmplia. La primera decisió tècnica del curs és aprendre a convertir dades disponibles en indicadors que es puguin comparar amb prudència.

Aquest capítol treballa, per tant, una competència que sembla discreta però sosté tot el manual: saber llegir una taula abans de convertir-la en una imatge. Una dada no és només una xifra; és el resultat d'una font, una definició, una unitat territorial i un moment de recollida. Quan alguna d'aquestes peces queda implícita, el gràfic o el mapa posterior pot semblar convincent però transmetre una interpretació fràgil.

## Fonts i unitats territorials

Les fonts de dades del curs han de permetre treballar amb població resident, allotjament turístic, límits administratius i superfície territorial. Aquestes fonts poden venir de portals de dades obertes, registres administratius, fonts estadístiques o organismes cartogràfics oficials. Abans de calcular res, cal identificar la unitat territorial de cada taula: municipi, comarca, província, àmbit territorial o una altra delimitació.

El codi territorial és la peça que permet unir una taula amb una capa cartogràfica. Si el codi municipal es perd, es transforma en nombre o queda escrit amb formats diferents en dues fonts, la unió espacial pot fallar encara que les dades semblin correctes. Per això, una part del treball de dades és aparentment modesta però decisiva: revisar camps buits, duplicats, formats numèrics, formats de text i zeros inicials.

També cal distingir entre el nom visible d'un territori i el seu identificador estable. Els noms poden portar accents, variants administratives, espais dobles o denominacions diferents segons la font. Els codis, en canvi, permeten una unió més robusta si es conserven com a text i es revisen abans de calcular. En un entorn professional, aquesta cura evita errors que després serien difícils de detectar només mirant el mapa.

::: table "Revisions mínimes abans de calcular indicadors"
| Element | Pregunta de control |
| --- | --- |
| Font | Qui produeix la dada i amb quin criteri? |
| Unitat territorial | A quin nivell espacial es pot comparar? |
| Codi d'unió | Coincideix amb el codi de la capa cartogràfica? |
| Format | Els camps numèrics i textuals estan ben interpretats? |
| Cobertura | Hi ha territoris sense dada, duplicats o valors inesperats? |
:::

## Indicadors i comparació

Un indicador és una manera de fer comparable una informació que, en brut, pot ser difícil d'interpretar. Les places turístiques totals, per exemple, poden descriure volum, però no sempre descriuen intensitat. Si volem comparar territoris de mida o població diferent, sovint necessitarem ràtios, percentatges o densitats.

La decisió no és automàtica. Un percentatge pot explicar composició; una ràtio pot relacionar oferta turística i població resident; una densitat pot introduir la superfície; i un valor absolut pot continuar sent necessari quan interessa saber volum total. El manual treballarà aquests casos amb dades concretes perquè l'estudiant aprengui a justificar cada transformació.

Un bon indicador respon una pregunta concreta. Si la pregunta és on es concentra l'oferta, potser cal començar pels valors absoluts. Si la pregunta és quins territoris suporten més pressió relativa, caldrà incorporar població resident, superfície o una altra base de comparació. Si la pregunta és com es reparteixen tipologies d'allotjament, probablement serà més útil treballar amb percentatges o proporcions. L'important és que la fórmula no aparegui com un automatisme, sinó com una decisió vinculada a una lectura territorial.

::: table "De la pregunta territorial a l'indicador"
| Pregunta | Indicador possible | Precaució principal |
| --- | --- | --- |
| On hi ha més oferta turística? | Places o establiments totals | No confondre volum amb intensitat |
| On pesa més el turisme respecte de la població resident? | Places per habitant o per 1.000 habitants | Revisar territoris amb població molt baixa |
| On és més densa l'oferta? | Places per km² | Comprovar que la superfície és comparable |
| Quina tipologia domina? | Percentatge per categoria | No perdre de vista el volum total |
:::

## Del full de càlcul al mapa

El full de càlcul és el primer espai de control. Allí es preparen codis, es documenten fórmules, es calculen indicadors i es deixen taules prou netes per passar a QGIS. Aquesta fase no és una tasca auxiliar: condiciona tot el que vindrà després. Un mapa amb bona simbologia no compensa un indicador mal definit o una unió territorial mal resolta.

El resultat esperat d'aquest bloc és una taula clara, traçable i preparada per unir-se a una capa cartogràfica. La qualitat del treball es reconeix quan una altra persona pot entendre d'on surt cada camp, quin càlcul s'ha fet i per què l'indicador resultant és adequat per respondre la pregunta territorial plantejada.

Per això, el full de càlcul no s'ha d'entendre com un lloc de pas ràpid. Ha de conservar la relació entre dades originals, camps revisats i indicadors finals. Quan es generi una taula per a QGIS, convé que el nom dels camps sigui curt però comprensible, que les unitats quedin clares i que les fórmules importants es puguin reconstruir. Aquesta traçabilitat facilita la revisió del professorat i, sobretot, ajuda l'estudiant a defensar el seu propi resultat.
