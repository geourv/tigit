# TIGIT

Manual del curs **Tècniques d'informació geogràfica i turística** de la Universitat Rovira i Virgili.

Aquest repositori és un lloc `unaltraweb` amb perfil `unaltremanual`. El manual ha de ser la font central per a estudiants i professorat: teoria, pràctiques, dades, rúbriques i criteris compartits.

## Criteri editorial

- Idioma base: català (`default_lang: ca`).
- Les traduccions a castellà o anglès es faran només abans de publicació, quan el contingut català estigui aprovat.
- Moodle conserva dates, lliuraments i qualificacions. El manual explica procediments, criteris i materials estables.
- La guia docent oficial és el marc normatiu; el manual desplega el treball del curs.

## Desenvolupament local

```bash
make build
make serve SITE_PROFILE=unaltremanual
make visualization-status
make visualization-render
make visualization-check
make test
make manual-pdf-sync MANUAL_PDF_LANG=ca
make manual-pdf-check
```

Cal renderitzar les visualitzacions Vega declarades a `.vegavisuals.yml` abans de publicar-les; el build rebutja artefactes absents o desactualitzats. `make serve`, `make build`, `make test` i `make publish` regeneren i sincronitzen el PDF i la coberta públics abans de renderitzar el web, de manera que la descàrrega sempre correspon al mateix estat del manual.

La web pública prevista és:

```text
https://geourv.github.io/tigit/
```
