# Divisions administratives de l'ICGC

La font espacial és `divisions-administratives-v2r2-20260120`, publicada per l'Institut Cartogràfic i Geològic de Catalunya amb llicència CC BY 4.0.

- URL: `https://datacloud.icgc.cat/datacloud/divisions-administratives/gpkg/divisions-administratives-v2r2-20260120.zip`
- Data territorial: 20 de gener de 2026.
- Mida del ZIP consultada el 18 d'agost de 2026: 69.427.405 bytes.
- SHA-256: `563fb7d81e143509d88569a9e8fe86d7c44ae9ce9e96c75b888379a7f0554162`.
- CRS: ETRS89 / UTM zona 31N, `EPSG:25831`.

El ZIP complet i el GeoPackage de 116 MB s'emmagatzemen temporalment a `tmp/` i no es versionen. `make spatial-data` comprova el checksum i genera `data/processed/tarragones-boundaries-icgc-20260120.gpkg`, un derivat compacte amb les escales necessàries per a la comarca, la província i el control de Vila-seca.
