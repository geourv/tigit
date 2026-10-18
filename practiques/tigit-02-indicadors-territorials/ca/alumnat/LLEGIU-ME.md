---
title: "Càlcul d'indicadors territorials: LLEGIU-ME de l'alumnat"
lang: ca
ref: tigit-practica-02-alumnat
content_status: draft
recipient: alumnat
subject: "Tècniques d'informació geogràfica i turística"
subject_code: "21224102"
---

Una magnitud ajuda a descriure un territori, però no sempre permet comparar-lo amb un altre de mida diferent. Aquesta pràctica transforma la taula municipal preparada en percentatges, ràtios i densitats amb denominadors explícits. El resultat ha de permetre explicar què mesura cada indicador i reconstruir-ne el càlcul.

El treball continua amb el parell comarca–municipi assignat. Tarragonès–Vila-seca és la demostració del professorat; els recomptes i els valors de control d'aquell cas no es poden traslladar automàticament a una altra comarca. El [capítol d'indicadors del manual](https://geourv.github.io/tigit/ca/chapters/indicadors-territorials/) desenvolupa les definicions i els exemples.

>>>>> - Construir indicadors amb numerador, denominador, unitat i fórmula visibles.
>>>>> - Calcular agregats comarcals a partir de components compatibles.
>>>>> - Detectar absències, divisions impossibles i denominadors petits.
>>>>> - Interpretar patrons descriptius sense convertir-los en explicacions causals.

# Selecció del treball i organització de l'equip

El professor comunica a classe els apartats i indicadors obligatoris i els enumera a Moodle. Els blocs són **B1, definició; B2, càlcul; B3, agregació; i B4, interpretació i continuïtat**. La guia presenta sis indicadors de consulta, però no tots són automàticament obligatoris. Els equips i els territoris comarca–municipi es mantenen.

Convé alternar operació, verificació i documentació i registrar les contribucions. Cada membre ha de poder explicar el numerador, el denominador i la limitació d'un indicador. Per continuar a 03/04 cal conservar les claus, els components i els percentatges d'habitatge no principal i població de 65+. Si s'acota una operació necessària, el professorat ha d'indicar com es completarà abans de continuar.

Amb la fita 01 validada i el programa instal·lat, s'estimen **120–150 minuts d'aula i 60–90 de treball autònom per estudiant treballant en equip**. Són estimacions no mesurades amb alumnat; exclouen reconstruir la base anterior i desenvolupar ampliacions. Dates i sessions es concreten a Moodle.

# Punt de partida i continuació del llibre

Cal partir del llibre propi `tigit-01-preparacio-dades.xlsx`, amb `municipal`, `sources`, `dictionary` i `checks` revisats. Es conserva aquesta fita i es desa una còpia de continuació amb el nom `tigit-02-indicadors-territorials.xlsx`. La solució docent de la fase 02 no és el punt de partida de l'exercici.

Abans de calcular, cal comprovar que cada municipi apareix una sola vegada i que els components necessaris són numèrics, tenen cobertura suficient i conserven les seves definicions. Les incidències de la preparació continuen vigents: una fórmula no pot resoldre una incompatibilitat entre períodes o territoris.

# Indicadors i organització

El nucli guiat es distribueix entre `indicators_demography` i `indicators_housing`. Cada full conserva codi, nom, components de càlcul i resultat; els components es vinculen a `municipal`, sense tornar a escriure les xifres.

| Indicador | Construcció | Unitat |
| --- | --- | --- |
| Pes de la població jove | Població de 0–14 / població total × 100 | Percentatge |
| Pes de la població gran | Població de 65+ / població total × 100 | Percentatge |
| Índex d'envelliment | Població de 65+ / població de 0–14 × 100 | Persones de 65+ per 100 de 0–14 |
| Densitat de població | Població total / superfície | Habitants per km² |
| Pes de l'habitatge no principal | Habitatges no principals / habitatges totals × 100 | Percentatge |
| Residents per habitatge principal | Població total / habitatges principals | Residents per habitatge principal |

Table: Repertori d'indicadors del llibre; Moodle concreta la selecció obligatòria.

Els indicadors descriuen població i habitatge. L'habitatge no principal no identifica habitatges turístics, i residents per habitatge principal no equival a la grandària oficial de la llar. Cada definició ha d'incloure una pregunta, un ús possible i una limitació al diccionari.

# Construir i comprovar les fórmules

Una divisió exigeix un denominador adequat i un tractament explícit dels casos no calculables. Si `D2` és un component i `C2` el total compatible, un percentatge es pot formular així:

```spreadsheet
=IF(AND(ISNUMBER(D2),ISNUMBER(C2),C2>0),D2/C2*100,NA())
```

La fórmula comprova els tipus i el denominador abans de dividir. `NA()` manté visible un resultat no calculable; no s'ha de substituir indiscriminadament per zero. També s'ha de revisar la font: una referència a una cel·la buida pot donar un zero aparent i el control del full d'indicadors no substitueix el registre d'absències de la preparació.

1. Cal vincular els components de cada indicador a `municipal` i comprovar una primera fila amb el municipi de referència.
2. La fórmula s'estén a totes les files del territori, revisant referències relatives i rangs. El darrer número de fila depèn de la comarca.
3. Cal comprovar un resultat de cada família amb un càlcul independent i revisar mínims, màxims i denominadors petits.
4. Les causes d'un resultat no calculable es registren a `checks`, i el seu tractament es documenta a `dictionary`.

Les funcions i els separadors poden aparèixer localitzats a Calc o Excel. En aquest llibre, els camps percentuals es calculen sobre 100: un valor `25` significa 25%. Aplicar-hi després el format percentual que interpreta `1` com a 100% produiria una representació incorrecta. Cal diferenciar valor, format de presentació i arrodoniment.

>>>> Si encara no s'ha justificat la compatibilitat de la superfície amb la població, la densitat ha de conservar aquesta limitació. Es pot estudiar la fórmula, però no presentar-ne el resultat com una comparació territorial plenament validada.

# Agregar la comarca

`indicators_summary` conserva els totals, els components, el factor d'escala i el resultat agregat. El percentatge comarcal d'habitatge no principal es calcula dividint la suma d'habitatges no principals per la suma d'habitatges totals, amb la mateixa cobertura municipal als dos costats.

La mitjana simple dels percentatges municipals respon una altra pregunta: dona el mateix pes a cada municipi, independentment del seu parc residencial. Cal conservar numeradors i denominadors perquè la diferència entre tots dos procediments es pugui explicar.

Abans d'aplicar `SUM`, cal comprovar quins municipis entren a cada component. La funció pot ometre text o cel·les buides i generar un total aparentment correcte sobre una cobertura incompleta. Qualsevol exclusió ha de ser justificada, coherent i visible.

# Ampliacions controlades

Una proposta seleccionada com a bàsica es puntua només en aquell bloc. Per al 20% cal afegir una pregunta i un contrast justificats, no només una columna nova.

## A1. Comparar ponderacions municipals

La pregunta és què canvia entre descriure el municipi mitjà i descriure el conjunt del parc residencial. Es varia la ponderació dels percentatges d'habitatge no principal, mantenint dades i cobertura. La referència és la ràtio de sumes de la comarca.

Cal calcular la mitjana simple i la ponderada pels habitatges totals. El pes de cada municipi és el seu total dividit pel total comarcal; els pesos han de sumar 1 i la mitjana ponderada ha de coincidir amb la ràtio de sumes, dins de la precisió de càlcul. La interpretació identifica quins municipis pesen més i quina pregunta respon cada resultat. Es comproven les absències abans d'agregar.

## A2. Canviar el denominador residencial

La pregunta és què expressa dividir la població entre tots els habitatges o només entre els principals. Es manté la població i es varia el denominador. La referència és residents per habitatge principal; cal conservar ambdós components i etiquetar les dues ràtios.

Es comproven denominadors positius, unitats i tres municipis. Els habitatges principals no poden superar el total; amb les mateixes dades positives, la ràtio per habitatge total no ha de superar la ràtio per principal. La interpretació explica la diferència sense confondre-la amb la grandària oficial de la llar o amb ocupació turística. Es conserven fórmules i una comparació comentada.

# Interpretació i resultat

Per a cada indicador seleccionat, el `README.md` ha de contenir una frase sobre el patró observat, una sobre el seu ús i una sobre allò que no permet concloure. La interpretació ha de considerar territori, període, definició, base del càlcul i casos extrems; una associació no demostra una causa.

La fita es conserva quan els càlculs seleccionats, els agregats i les incidències es poden revisar dins del mateix llibre i hi ha les entrades necessàries per continuar. Cal desar-lo, tancar-lo, tornar-lo a obrir i comprovar que els resultats es recalculen. Les fórmules mantenen la precisió de treball; els decimals es redueixen en etiquetes o textos quan ho requereix la comunicació.

El llibre 02 revisat alimentarà la pràctica de gràfics. La continuació reutilitzarà els rangs i les claus existents, sense transcriure els indicadors a un altre fitxer desvinculat.

# Lliurament i qualificació interna

Cal preparar el llibre 02 i uns apunts breus en PDF amb definicions, resultats interpretats, controls i contribucions de l'equip. Les captures d'una fórmula i d'un control han de permetre llegir rangs i valors. Es conserven el llibre 01, els originals i els registres; Moodle concreta quins fitxers s'han de trametre i el format del conjunt.

| Bloc | Màxim | Què es valora |
| --- | ---: | --- |
| Bàsic, 70% | 7 punts | Definicions, fórmules, controls i interpretació dels apartats seleccionats. |
| Ampliacions, 20% | 2 punts | Pregunta, comparació controlada i conclusions justificades. |
| Documentació, 10% | 1 punt | Apunts clars, captures llegibles, atribucions i organització. |

Table: Qualificació interna de la pràctica d'indicadors sobre 10.

Els màxims no són automàtics. Bàsic i documentació complets poden arribar a 8/10 sense ampliacions. Aquestes no substitueixen obligatoris i acumular fitxers no garanteix punts. Cada aportació tècnica es valora al bàsic o a l'ampliació; el 10% valora comunicació i organització, sense duplicar-la. El 70–20–10 és intern; Moodle concreta el pes global i els requisits de superació d'acord amb la [guia docent de TIGIT, 21224102](https://guiadocent.urv.cat/docnet/guia_docent/index.php?centre=21&ensenyament=2122&assignatura=21224102&fitxa_apartat=61&any_academic=2026_27).
