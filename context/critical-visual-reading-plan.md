# Pla de lectura crítica de gràfics i mapes

Aquest document planifica com incorporar al manual TIGIT una lectura crítica inspirada en Gerald Everett Jones, *How to Lie with Charts*, i Mark Monmonier, *How to Lie with Maps*. No és contingut publicable. Serveix per decidir on encaixa cada problema, quina mena de peça docent necessita i quines parts ja estan parcialment cobertes.

La intenció no és ensenyar "trucs per enganyar", sinó fer visible que tota taula, gràfic, mapa o infografia redueix, classifica i interpreta dades. El manual ha de convertir aquesta idea en criteris pràctics: detectar l'error, entendre per què importa i produir una versió més honesta o més ben documentada.

## Fonts de partida

| Font | Ús docent previst | Nota editorial |
| --- | --- | --- |
| Jones, *How to Lie with Charts* | Errors de dades, etiquetes, pastissos, eixos, barres, tendències, fulls de càlcul, paraules del gràfic, color, dashboards i presentacions | El manual citarà la quarta edició de 2018, que és la versió local més actual disponible. |
| Monmonier, *How to Lie with Maps* | Elements del mapa, generalització, errors cartogràfics, color, mapes publicitaris, propaganda, dades temàtiques, imatge, mapes interactius i lectura crítica | El `figure-plan` ja el vincula amb generalització i classificació/color. Cal estendre aquesta lectura als capítols 4, 6, 8 i 9. |
| Wilke, *Fundamentals of Data Visualization* | Proporcionalitat de tinta, eixos, paletes, gràfics llegibles i decisions de disseny | Ja s'està usant al capítol 3 i al pla de figures. Complementa Jones amb una formulació més contemporània i menys retòrica. |

Les figures originals dels llibres no s'han de copiar ni redibuixar com a adaptacions sense una revisió de drets. El camí preferent és crear figures pròpies amb dades sintètiques o del projecte comarcal, citant la font com a referència conceptual.

## Criteri d'integració

| Tipus de material | Quan usar-lo | Sintaxi prevista |
| --- | --- | --- |
| Prosa teòrica | Quan el problema canvia la manera d'entendre dades, mapes o indicadors | Secció o paràgraf integrat al flux del capítol |
| Nota o consell | Quan convé donar un criteri de revisió sense interrompre massa | `>>` |
| Exemple resolt | Quan cal comparar una versió problemàtica i una de revisada | `>>>` |
| Advertència | Quan una decisió pot invalidar el resultat o induir una lectura falsa | `>>>>` |
| Objectius d'aprenentatge | Quan el bloc introdueix una activitat nova | `>>>>>` |
| Risc greu o acció que malmet dades | Quan l'acció és operativa i pot destruir traçabilitat o significat | `>>>>>>` |
| Figura pròpia | Quan el contrast visual comunica millor que la prosa | SVG, PNG documentat o figura generada des de dades reproduïbles |

## Encaix per capítol

| Tema crític | Problema que cal ensenyar | Encaix al manual | Peça recomanada | Estat |
| --- | --- | --- | --- | --- |
| Dades, etiquetes i unitats | Un nombre sense etiqueta, unitat, període o població de referència pot semblar precís però no ser interpretable | Capítol 1, `Les dades no són els fets mateixos`, `Metadades, procedència i llicència`; capítol 3, `Retolació de gràfics` | Callout `>>>>` sobre nombres despullats; figura petita dada-etiqueta-unitat-font | Callout incorporat al capítol 1; figura opcional pendent |
| Categories i criteris de recompte | Comptar exigeix decidir què entra i què queda fora; una categoria mal definida altera tot el gràfic | Capítol 1, fonts i taula rectangular; capítol 2, disseny d'indicadors | Exemple `>>>` amb habitatge no principal, habitatge turístic i habitatge buit | Parcialment cobert |
| Resums que amaguen distribucions | Totals, mitjanes i agregats poden ocultar concentració, desigualtat o valors extrems | Capítol 2, `Dissenyar una mesura útil`; capítol 3, distribució; capítol 9, seleccionar evidències | Figura pròpia amb total comarcal vs municipis; callout `>>` sobre mirar sota el total | Nou reforç |
| Mitjana, mediana i valors extrems | Una mitjana pot descriure malament una distribució turística molt asimètrica | Capítol 2, `Mètriques comarcals` i `Interpretar i comprovar`; capítol 3, distribució | Figura o taula comparant mitjana, mediana i rang amb municipis del Tarragonès | Nou reforç |
| Absència, zero i desconeguts | Amagar desconeguts o convertir-los en zero altera percentatges, pastissos, mapes i indicadors | Capítol 1, valors absents; capítol 2, no calculables; capítol 8, absències en coropletes | Advertència `>>>>>>` ja existent al capítol 1; afegir pont amb percentatges i gràfics | Parcialment cobert |
| Percentatges sense base | Un percentatge pot semblar fort si no es mostra el denominador o la mida de la població | Capítol 2, `El denominador defineix la comparació`; capítol 3, gràfics; capítol 8, coropletes | Callout `>>>>` i figura amb percentatge alt sobre base petita | Callout incorporat al capítol 2; figura opcional pendent |
| Pastissos i composició del total | Un pastís només és defensable si representa parts d'un total conegut i complet; massa sectors o sectors petits dificulten la lectura | Capítol 3, `Composició`; capítol 9, infografia | Figura pròpia pastís problemàtic vs barra 100%; callout `>>>>` sobre "100% de què?" | Callout incorporat al capítol 3; figura opcional pendent |
| Eixos truncats i origen zero | Tallar l'eix pot exagerar diferències en barres; en línies cal justificar si es prioritza variació | Capítol 3, `Eixos truncats, tres dimensions i soroll visual` | Ja hi ha figures de Wilke; afegir una activitat d'auditoria amb dades del curs | Parcialment cobert |
| Relació d'aspecte i pendents | Fer un gràfic massa alt o massa pla pot dramatitzar o suavitzar una tendència | Capítol 3, comparació temporal; capítol 9, miniinfografia | Figura pròpia de la mateixa sèrie amb tres relacions d'aspecte; callout `>>` | Figura i prosa incorporades al capítol 3 |
| Interpolació, extrapolació i tendències | Una línia de tendència o una projecció pot semblar predicció quan només és ajust visual | Capítol 3, relacions i fluxos; capítol 2, seguiment; capítol 9, límits | Advertència `>>>>` sobre no confondre tendència amb previsió; exemple resolt | Advertència incorporada al capítol 3 |
| 3D, perspectiva i efectes | Volums, ombres i rotacions fan que àrees i alçades semblin diferents sense afegir dades | Capítol 3, `Eixos truncats, tres dimensions i soroll visual`; capítol 9, importar peces | Ja hi ha referència a 3D; afegir criteri de revisió final a la miniinfografia | Parcialment cobert |
| Soroll visual i decoració | Retícules, ombres, icones o fons poden competir amb la dada | Capítol 3, jerarquia; capítol 9, arquitectura de la informació | Figura d'auditoria o callout `>>` sobre eliminar allò que no suporta la pregunta | Parcialment cobert |
| Paraules del gràfic | Títols, etiquetes i anotacions poden suggerir una conclusió no demostrada | Capítol 3, retolació; capítol 9, títol, entrada i conclusió | Callout `>>>>` sobre títols que afirmen més que les dades | Nou reforç prioritari |
| Fulls de càlcul i fórmules | Un gràfic hereta errors de fórmules, formats, arrodoniments i ordenacions del llibre | Capítol 1, introducció als fulls de càlcul; capítol 3, exportar gràfics | Ja hi ha advertiments; afegir frase-pont: "un gràfic no valida el full" | Parcialment cobert |
| Dashboard i panells comparables | Panells amb escales, períodes o posicions canviants fan que la comparació sigui falsa o cansada | Capítol 9, relació entre mapa, gràfic i text; possible capítol 3 | Figura/plantilla de miniinfografia amb escales consistents | Nou reforç |
| Projeccions i distorsió | Cap projecció preserva totes les propietats; triar projecció és triar quina distorsió es tolera | Capítol 4, `Projeccions i distorsions` i `Les projeccions ens enganyen?` | Callout `>>` o `>>>>` segons context; activitat amb The True Size i indicatrius | Parcialment cobert |
| Assignar o transformar CRS | Assignar un CRS incorrecte pot fer quadrar una capa només aparentment o desplaçar-la | Capítol 4, sistemes de referència; capítol 5, importar capes | Advertència `>>>>>>`; figura pròpia amb mateixa capa desplaçada | Parcialment cobert |
| Generalització cartogràfica | Seleccionar, simplificar, agregar o desplaçar és necessari, però pot ocultar elements o canviar jerarquies | Capítol 6, `Escala i generalització` | Figura pròpia a tres escales ja planificada; callout `>>` sobre "mentides blanques" de l'escala | Prioritari i planificat |
| Escala i precisió aparent | Una línia fina, una etiqueta exacta o un punt pot suggerir més precisió de la que admet la font | Capítol 6, escala i àrea mínima cartografiable; capítol 5, coordenades a punts | Callout `>>>>` i figura amb punt municipal vs adreça real | Nou reforç |
| Toponímia i noms | Els noms, llengües i prioritats de retolació també són decisions cartogràfiques | Capítol 6, `Retolació` | Exemple `>>>` amb nomenclàtor i criteris de prioritat | Nou reforç |
| Llegenda i omissions | Una llegenda incompleta o una classe "altres" massa ampla pot amagar la lectura real | Capítol 6, elements del mapa; capítol 8, llegenda temàtica | Callout `>>>>`; afegir a comprovacions de qualitat | Parcialment cobert |
| Color que atrau o distreu | Color intens, paletes no monotòniques o associacions semàntiques poden donar importància falsa | Capítol 7, paletes i accessibilitat; capítol 8, classificació/color | Figura pròpia rampa arc de Sant Martí vs seqüencial ja prevista; advertència `>>>>` | Parcialment cobert |
| Mapes publicitaris i turístics | Un mapa turístic pot prioritzar atracció, marca i recorregut per sobre de mesura territorial | Capítol 6, mapes turístics; capítol 9, síntesi | Prosa teòrica curta; possible exemple extern només si drets clars | Nou reforç |
| Coropletes amb recomptes | Pintar quantitats absolutes sobre àrees confon volum amb intensitat | Capítol 8, errors típics, normalitzar abans de simbolitzar | Ja hi ha figura problemàtica/revisada; mantenir com eix fort | Cobert recentment |
| MAUP i fal·làcia ecològica | Canviar unitats territorials o atribuir patrons agregats a individus pot canviar la conclusió | Capítol 8, `El fenomen i la unitat espacial`; capítol 2, comparabilitat | Prosa teòrica + callout `>>>>`; figura opcional amb agregació municipal/comarcal | Prosa i callout incorporats al capítol 8 |
| Classificació manipuladora | Quantils, Jenks, intervals iguals o talls manuals poden fabricar o suavitzar contrast | Capítol 8, classificació | Ja hi ha sèrie de classificacions; afegir advertència sobre canviar un sol paràmetre cada vegada | Advertència incorporada al capítol 8 |
| Absències cartogràfiques | Sense dades, no aplicable i zero necessiten símbols separats | Capítol 8, `Zero, absència i no aplicable` | Ja cobert; reforçar a llegenda i activitat | Cobert parcialment |
| Mapes dasimètrics i hipòtesi espacial | Refinar una coropleta amb informació auxiliar pot millorar la lectura, però també pot simular precisió | Capítol 8, `Mapes dasimètrics` | Ja hi ha prosa; possible figura futura coropleta vs dasimètric | Parcialment cobert |
| Cartogrames i anamorfosi | Fer proporcional l'espai a una magnitud fa visible un pes però sacrifica forma i distància | Capítol 8, cartogrames | Ja hi ha figura esquemàtica; afegir lectura crítica a la llegenda o callout | Parcialment cobert |
| Mapes d'imatge | Ortofotos, satèl·lit i Street View semblen "la realitat", però també tenen data, angle, processament i buits | Capítol 6, fotografia aèria, satèl·lit i Street View | Callout `>>` sobre data/angle/processament; connexió amb Monmonier, mapes d'imatge | Nou reforç |
| Mapes interactius i mòbils | Zoom, geolocalització, suggeriments i capes predeterminades condicionen la lectura | Capítol 1, geoserveis; capítol 6, Google Maps/Street View; capítol 9, comunicació | Prosa breu i criteri de captura/documentació | Nou reforç |
| Selecció narrativa en infografia | Una infografia pot mentir per selecció: mostra només les peces que reforcen una història | Capítol 9, seleccionar evidències i auditoria abans/després | Callout `>>>>` i checklist final | Callout i auditoria incorporats al capítol 9 |
| Notes metodològiques invisibles | Si fonts, període, unitats i limitacions queden massa petites, la peça sembla més certa del que és | Capítol 9, fonts, unitats i notes metodològiques | Callout `>>`; criteri de mida mínima en revisió | Parcialment cobert |

## Figures candidates

| ID provisional | Capítol | Idea | Font conceptual | Estat |
| --- | --- | --- | --- | --- |
| `fig-02-mean-median-outlier` | 2 | Mateixa distribució municipal resumida amb mitjana, mediana i valor extrem | Jones, dades i mitjanes | Nova |
| `fig-02-small-denominator-rate` | 2 | Percentatge alt en municipi petit vs volum absolut moderat | Jones, percentatges i etiquetes | Nova |
| `fig-03-pie-vs-100bar` | 3 | Pastís amb desconeguts ocults i alternativa amb barra 100% o barres apilades | Jones, pastissos | Nova |
| `fig-03-aspect-ratio-trend` | 3 | Mateixa sèrie temporal amb aspecte comprimit, neutre i dramatitzat | Jones, tendències | Incorporada com `assets/img/data-visualization/aspect-ratio-trend.svg` |
| `fig-06-generalization-three-scales` | 6 | Mateix territori a tres escales amb selecció, simplificació i jerarquia | Monmonier, generalització | Ja prevista a `legacy-visual-expansion-plan` |
| `fig-06-false-precision-point` | 6 | Punt o etiqueta que sembla exacta quan la font només permet una localització aproximada | Monmonier, blunders i escala | Nova |
| `fig-07-rainbow-vs-sequential-map` | 7 | Rampa arc de Sant Martí contra rampa seqüencial sobre el mateix indicador | Monmonier, color; Wilke/ColorBrewer | Ja prevista conceptualment |
| `fig-08-maup-aggregation` | 8 | Mateixos valors agregats en unitats diferents amb patró aparent diferent | Monmonier, data maps | Nova |
| `fig-08-choropleth-dasymetric` | 8 | Coropleta municipal vs redistribució dasimètrica amb sòl urbà auxiliar | Monmonier/Slocum/Rabella | Opcional |
| `fig-09-evidence-audit` | 9 | Miniinfografia amb marques d'auditoria: afirmació, evidència, font, límit | Jones/Monmonier com a lectura crítica final | Nova |

## Callouts prioritaris

| Capítol | Tipus | Missatge central |
| --- | --- | --- |
| 1 | `>>>>` | Un número sense etiqueta, unitat, període i font no és una dada analítica suficient. |
| 2 | `>>>>` | Un percentatge sense denominador pot exagerar una diferència o amagar una base massa petita. |
| 3 | `>>>>` | Un pastís ha de representar un total complet; si hi ha desconeguts, també formen part de la història. |
| 3 | `>>` | Canviar la relació d'aspecte pot canviar la sensació de pendent sense canviar cap dada. |
| 4 | `>>>>>>` | Assignar un CRS per fer desaparèixer un avís no equival a reprojeccionar correctament una capa. |
| 6 | `>>` | La generalització no és un defecte del mapa: és una decisió necessària que s'ha de poder justificar. |
| 6 | `>>>>` | Un mapa a escala petita no pot prometre precisió de parcel·la, adreça o itinerari local. |
| 7 | `>>>>` | Una paleta atractiva pot ser una mala paleta si trenca l'ordre de la dada o domina la jerarquia. |
| 8 | `>>>>` | Cap mètode de classificació és neutral; cal explicar quin contrast fa visible i quin cost assumeix. |
| 8 | `>>>>` | Una coropleta municipal no autoritza conclusions sobre persones, carrers o establiments concrets. |
| 9 | `>>>>` | El títol de la infografia no ha d'afirmar més del que mapes, gràfics i fonts poden sostenir. |

## Prioritats de revisió

1. Consolidar el capítol 3 com a bloc principal de lectura crítica de gràfics: pastissos, eixos, aspecte, tendències, etiquetes i soroll visual.
2. Reforçar el capítol 8 com a bloc principal de lectura crítica cartogràfica: unitat espacial, MAUP, coropletes, classificació, absències i llegenda.
3. Afegir ponts curts als capítols 1 i 2 perquè els errors visuals quedin connectats amb dades, denominadors i resums estadístics.
4. Fer que el capítol 9 funcioni com a auditoria final: cada gràfic i mapa ha de passar per pregunta, evidència, límit, font i decisió visual.
5. Mantenir Jones 2018 com a citació principal quan s'incorporin nous exemples de lectura crítica de gràfics.
