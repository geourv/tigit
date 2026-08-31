# Dades processades

Aquest directori conté artefactes intermedis utilitzats pels scripts. Els snapshots que ha de consultar el professorat es publiquen a `dist/teaching/chapter-NN/`; el punt de partida de l'estudiant es publica a `dist/student/chapter-01/`. No s'ha d'utilitzar `data/processed` com a carpeta de lliurament.

Els llibres acumulatius es poden regenerar, en ordre, amb:

```bash
make chapter-01
make chapter-02
make chapter-03
make chapter-07
make qgis-transfer
```

El `Makefile` crea un entorn virtual local, instal·la `openpyxl`, genera el punt de partida i desenvolupa les versions docents de preparació, indicadors, gràfics, color i transferència a QGIS. Els prefixos tècnics es conserven: `tigit-07-teoria-color.xlsx` alimenta `tigit-05-integracio-sig.xlsx`, que hi afegeix `map_export`. `make check` comprova les fonts, les dimensions de la consulta de població, els fulls i les fórmules principals. Per evitar sobreescriure feina manual fora del pipeline, el generador del llibre inicial es nega a substituir un fitxer existent si no s'utilitza `--force`.
