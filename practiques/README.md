# Guies i PDF de les pràctiques TIGIT

Les lectures catalanes tenen una versió per a alumnat i una per a professorat, sota `<pràctica>/ca/<destinatari>/LLEGIU-ME.md`. L'autor ha revisat i autoritzat el lliurament d'aquesta versió de treball el 18 d'octubre de 2026. Les fonts continuen `draft` i els PDF conserven ESBORRANY; l'autorització de distribuir la versió de treball no la converteix en una edició definitiva.

## Lot autoritzat 0.2.0 · 18 d'octubre de 2026

Guies de TIGIT **21224102**, per a primer del Grau en Gestió en Turisme i Hoteleria, amb treball per equips i territoris comarca–municipi assignats. Les guies docents incorporen preparació de la sessió, «Preparar Moodle» i un enunciat autònom per copiar a Descripció. Les lectures d'alumnat comparteixen els criteris de selecció, continuïtat, ampliacions i qualificació interna 7/2/1.

Els enllaços als PDF són **locals al checkout**: apunten a jobs ignorats sota `sandbox/`, no a descàrregues de GitHub ni de la web pública. Cal obrir-los des d'aquest índex local o des de l'explorador de fitxers. Cada job conserva font, recursos, PDF i `receipt.json`.

| Pràctica | PDF d'alumnat | PDF del professorat | Fonts editables |
| --- | --- | --- | --- |
| 01 · Preparació de dades | [Alumnat · 6 pàgines](../sandbox/practiques/tigit-01-preparacio-dades/lectura-0.2.0-ca-alumnat-pages-20261018-02/outputs/LLEGIU-ME.pdf) | [Professorat · 8 pàgines](../sandbox/practiques/tigit-01-preparacio-dades/lectura-0.2.0-ca-docent-pages-20261018-02/outputs/LLEGIU-ME.pdf) | [Alumnat](tigit-01-preparacio-dades/ca/alumnat/LLEGIU-ME.md) · [Professorat](tigit-01-preparacio-dades/ca/docent/LLEGIU-ME.md) |
| 02 · Indicadors territorials | [Alumnat · 5 pàgines](../sandbox/practiques/tigit-02-indicadors-territorials/lectura-0.2.0-ca-alumnat-pages-20261018-02/outputs/LLEGIU-ME.pdf) | [Professorat · 7 pàgines](../sandbox/practiques/tigit-02-indicadors-territorials/lectura-0.2.0-ca-docent-pages-20261018-02/outputs/LLEGIU-ME.pdf) | [Alumnat](tigit-02-indicadors-territorials/ca/alumnat/LLEGIU-ME.md) · [Professorat](tigit-02-indicadors-territorials/ca/docent/LLEGIU-ME.md) |
| 03 · Gràfics territorials | [Alumnat · 5 pàgines](../sandbox/practiques/tigit-03-grafics-territorials/lectura-0.2.0-ca-alumnat-pages-20261018-02/outputs/LLEGIU-ME.pdf) | [Professorat · 9 pàgines](../sandbox/practiques/tigit-03-grafics-territorials/lectura-0.2.0-ca-docent-pages-20261018-02/outputs/LLEGIU-ME.pdf) | [Alumnat](tigit-03-grafics-territorials/ca/alumnat/LLEGIU-ME.md) · [Professorat](tigit-03-grafics-territorials/ca/docent/LLEGIU-ME.md) |
| 04 · Primers mapes QGIS | [Alumnat · 7 pàgines](../sandbox/practiques/tigit-04-qgis-mapes/lectura-0.2.0-ca-alumnat-pages-20261018-02/outputs/LLEGIU-ME.pdf) | [Professorat · 9 pàgines](../sandbox/practiques/tigit-04-qgis-mapes/lectura-0.2.0-ca-docent-pages-20261018-02/outputs/LLEGIU-ME.pdf) | [Alumnat](tigit-04-qgis-mapes/ca/alumnat/LLEGIU-ME.md) · [Professorat](tigit-04-qgis-mapes/ca/docent/LLEGIU-ME.md) |

La versió de pràctica és independent de la del manual i dels productors. Els runs anteriors es conserven com a proves; els enllaços anteriors identifiquen el lot vigent. La qualificació interna 70–20–10 no modifica els pesos globals de la guia docent. La llista efectiva d'obligatoris, les dates i la tramesa es concreten a Moodle.

La [carpeta de Moodle del 18 d'octubre](../sandbox/practiques/moodle-2026-10-18/) ofereix còpies verificades amb noms recognoscibles. [OBRE-AQUI.html](../sandbox/practiques/moodle-2026-10-18/OBRE-AQUI.html) indica els cinc adjunts disponibles: quatre PDF d'alumnat i la plantilla inicial XLSX. Les guies, els cinc llibres resolts i el bundle complet QGIS del cas Tarragonès–Vila-seca són a `PROFESSORAT`. Per a la pràctica 04 cal afegir la base geogràfica verificada dels territoris assignats als equips.

## Materials per preparar la demostració

El cas docent Tarragonès–Vila-seca comparteix el codi de reproducció, el manifest d'inputs i la plantilla editable de [tigit-projecte-territorial](tigit-projecte-territorial/README.md). Les dades d'aquest cas no són les dels territoris assignats als equips.

- [Plantilla inicial i llibres docents reconstruïts](../sandbox/practiques/tigit-projecte-territorial/fulls/run04-eixos-20261014/data/processed/): la plantilla sense sufix `-teaching` és buida; els llibres amb aquest sufix són solucions del cas docent.
- [Recursos fixats i figura històrica d'auditoria](../sandbox/practiques/tigit-projecte-territorial/recursos/2026-10-14/): origen i hashes declarats a `tigit-projecte-territorial/recursos.yml`.
- [Projectes QGIS del cas docent](../sandbox/practiques/tigit-projecte-territorial/0.1.0/ca/run05-contract-20261014/payload/projects/): cal conservar el bundle complet i les dependències verificades, no copiar només els projectes.
- [Captures reals de la pràctica 04](../sandbox/practiques/tigit-04-qgis-mapes/run03/captures/): utilitzades als PDF, amb els originals i manifests del capturador.

El PDF d'alumnat i els materials inicials indicats a cada guia són els adjunts ordinaris de la Tasca. Els resolts serveixen per preparar la classe; qualsevol exemple compartit s'identifica expressament i manté les seves dependències.

`practiques/` conté fonts versionades. Els recursos, els llibres calculats, les captures i els PDFs de revisió es preparen en runs identificats sota `sandbox/practiques/`, fora de Git. Les edicions finals corresponen al compositor natiu d'unaltraweb i a `dist/practiques/<slug>/<versió>/<idioma>/`. Aquestes tres arrels estan excloses de la web Jekyll.

L'estat de la migració, la reserva de paths i les dependències de publicació són a `context/practice-migration.md`. Els bundles segellats i els rebuts antics són evidència de les execucions que els van produir; no s'actualitzen a mà quan canvien les fonts.
