# Projecte pràctic TIGIT

Aquest paquet inicia un projecte acumulatiu d'indicadors, gràfics, mapes i infografia territorial. El llibre `data/processed/tigit-01-preparacio-dades.xlsx` prepara l'estructura de treball del capítol 1; no conté les dades descarregades ni una solució resolta.

## Abans de començar

1. Extraieu tot el ZIP en una carpeta de treball amb permisos d'escriptura.
2. Manteniu juntes les carpetes `data`, `qgis`, `outputs` i `captures`.
3. Obriu el llibre amb l'aplicació i la configuració regional acordades a classe.
4. Completeu al full `project` l'autoria, l'aplicació i la configuració regional.
5. Descarregueu les fonts indicades al manual i conserveu-les sense modificar a `data/raw`.
6. Completeu `sources` abans de transformar les taules.

## Contingut inicial

- `data/raw`: ubicació de les descàrregues originals.
- `data/processed/tigit-01-preparacio-dades.xlsx`: fonts, diccionari, fulls `source_*`, fulls `prepared_*`, comprovacions i taula municipal.
- `qgis`: ubicació dels projectes que començaran al capítol 4.
- `outputs`: figures, mapes i infografies exportades.
- `captures`: evidències d'interfície demanades durant les activitats.
- `sandbox`: proves que encara no formen part del producte.
- `dist`: fitxers finals a lliurar i ZIP reproduïble del projecte.

No corregiu una dada al fitxer original ni a una exportació. Apliqueu la transformació al llibre o projecte editable, documenteu-la i regenereu els resultats dependents.

Els fulls `source_*` conserven les capçaleres i categories de la font. Els noms de camp propis del projecte apareixen a `prepared_*`, després d'haver documentat la transformació. No reanomeneu les columnes d'origen com si haguessin arribat així.
