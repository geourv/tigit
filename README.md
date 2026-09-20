# TIGIT

Manual del curs **Tècniques d'informació geogràfica i turística** de la Universitat Rovira i Virgili.

Aquest repositori és un lloc `unaltraweb` amb perfil `unaltremanual`. El manual ha de ser la font central per a estudiants i professorat: teoria, pràctiques, dades, rúbriques i criteris compartits.

## Col·laboració

El contracte compartit és a `.github/CONTRIBUTING.md`. Defineix les branques curtes, les reserves exactes de fitxers, la coordinació en un únic checkout i les integracions amb proveïdors.

1. Obriu o trieu una incidència concreta i acordeu la reserva exacta abans d'editar.
2. Treballeu en el checkout mutable primari i manteniu una sola sessió d'edició activa al repositori.
3. Executeu el preflight de només lectura, creeu una branca curta i obriu una pull request en esborrany després del primer canvi coherent.
4. No creeu ni manipuleu worktrees vinculades com a part d'una sessió d'edició.

Per al treball amb MCP, demaneu `unaltraweb` com a únic MCP de primer nivell i deixeu que el pla de control n'activi les dependències declarades. L'arrel del consumidor s'ha de transmetre amb `MCP_CONSUMER_WORKSPACE`; les operacions `build`, `check` i `smoke` de cada factory es mantenen al checkout del factory.

## Criteri editorial

- Idioma base: català (`default_lang: ca`).
- Les traduccions a castellà o anglès es faran només abans de publicació, quan el contingut català estigui aprovat.
- Moodle conserva dates, lliuraments i qualificacions. El manual explica procediments, criteris i materials estables.
- La guia docent oficial és el marc normatiu; el manual desplega el treball del curs.

## Desenvolupament local

```bash
make build
make serve
make test
make down
```

Les visualitzacions Vega, els diagrames i els càlculs es renderitzen explícitament amb les eines MCP i els factories corresponents. `make build`, `make serve` i `make test` preparen els PDF i les portades de previsualització que falten o són obsolets, i en deixen còpies ignorades controlades per rebut; `make test` també executa l'auditoria HTML. Cap d'aquestes ordres publica el lloc.

La web pública prevista és:

```text
https://geourv.github.io/tigit/
```
