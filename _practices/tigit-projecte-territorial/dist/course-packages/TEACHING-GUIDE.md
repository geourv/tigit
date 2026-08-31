# Guia docent de desenvolupament pràctic

Aquest paquet acompanya el projecte pràctic acumulatiu de TIGIT. Està pensat per al professorat de laboratori i documenta l'estat de les dades, el llibre, els controls, les captures i els productes que s'han de demostrar.

## Estat actual

El capítol 1 diferencia el punt de partida `tigit-01-preparacio-dades.xlsx` de la versió desenvolupada `tigit-01-preparacio-dades-teaching.xlsx`. La segona conserva els originals, la consulta JSON-stat de població de 2021, les fórmules de la taula municipal i els controls reproduïbles. Encara requereix revisió humana de la compatibilitat temporal de la superfície i de les captures abans de considerar-se una solució aprovada.

La seqüència visible del projecte és fonts, indicadors, gràfics, color, dades espacials, SIG, llenguatge cartogràfic, cartografia temàtica i síntesi. Els prefixos `01`–`09` dels artefactes són identificadors tècnics estables, no una numeració que s'hagi de reordenar: la fita de color `tigit-07-teoria-color.xlsx` alimenta el llibre `tigit-05-integracio-sig.xlsx`, que hi afegeix el full `map_export` per a QGIS.

La cobertura executable només arriba al llibre de transferència cap a QGIS. Abans d'aprovar o distribuir la pràctica completa falten la integració de l'oferta turística municipal i dels indicadors que exigeix la guia docent, els quatre projectes QGIS, les composicions i exportacions cartogràfiques, el màster SVG, la prova de lectura, el PDF final i el ZIP reproduïble comprovat després d'extreure'l en una carpeta nova.

## Finalitat de la fita 01

L'estudiant ha de poder:

1. distingir originals, imports i taula preparada;
2. conservar els codis municipals com a text;
3. documentar productor, taula, URL, període, accés, llicència i selecció;
4. practicar filtres sobre comarca, tipus de fila, absències i duplicats;
5. utilitzar una taula dinàmica per comprovar recomptes o categories, sense substituir les fórmules auditables dels indicadors;
6. construir `municipal` per referència, cerca o transformació documentada, mai unint fonts per posició de fila.

## Demostració prevista

- Mostrar una descàrrega manual d'Idescat i llegir-ne les notes abans de baixar el fitxer.
- Importar un fitxer delimitat en UTF-8 i fixar el codi municipal com a text.
- Seguir Vila-seca com a municipi de control durant les transformacions.
- Filtrar el Tarragonès mitjançant el codi de comarca.
- Comparar el recompte municipal amb una font oficial.
- Registrar una incidència real a `checks` i la definició corresponent a `dictionary`.

## Captures pendents

Les captures es produiran amb una instal·lació neta i dades reals. Com a mínim, cal valorar una captura de la selecció d'Idescat, una del diàleg d'importació i una del filtre o comprovació que tingui una funció docent clara. No s'han de capturar rutes personals, historials, noms d'usuari ni notificacions.

## Regeneració

La fita completa es genera amb:

```bash
make chapter-01
make check
```

Els ZIP es reconstrueixen des de l'arrel del projecte amb:

```bash
make packages
```

La regeneració no substitueix la revisió manual a Calc o Excel ni l'aprovació visual de les captures i els resultats.
