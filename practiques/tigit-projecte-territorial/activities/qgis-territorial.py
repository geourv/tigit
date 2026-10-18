"""TIGIT domain model: real ICGC/Idescat join and authored cartography.

Public compute/verify/compose callbacks for the shared qgis-practice-v2 producer.
The provider owns snapshots, containers, project saving, UI captures, native
exports, the descriptor, dependency closure and offline reopening.
"""
import csv
import math
from pathlib import Path
import shutil


EXPECTED_ABOVE_50 = {"430120", "430509", "431310", "431536", "431649", "439057"}
CSV_FIELDS = ["mun_code", "municipality", "county_code", "year", "population_total",
              "population_65_plus", "population_65_plus_pct", "housing_total",
              "housing_non_main", "housing_non_main_pct", "indicator_status"]


def _layer(path, name, table=None):
    from qgis.core import QgsVectorLayer
    layer = QgsVectorLayer(str(path) + ("|layername=" + table if table else ""), name, "ogr")
    if not layer.isValid():
        raise ValueError("Invalid persisted layer: " + name)
    return layer


def compute(context):
    from qgis.core import QgsProject, QgsVectorFileWriter
    context.copy_inputs()
    base = _layer(context.output("territorial-base"), "Municipis", "municipalities_250k")
    with Path(context.output("indicators-table")).open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    codes = [str(feature["CODIMUNI"]) for feature in base.getFeatures()]
    table_codes = [row["mun_code"] for row in rows]
    if len(codes) != 22 or len(set(codes)) != 22 or len(table_codes) != 22 or len(set(table_codes)) != 22:
        raise ValueError("The demonstration requires 22 unique municipalities on each side")
    if set(codes) != set(table_codes):
        raise ValueError("The two territorial key sets differ")
    if any(row["year"] != "2021" or row["county_code"] != "36" or row["indicator_status"] != "ok" for row in rows):
        raise ValueError("Unexpected period, county or indicator status")

    context.processing("native:joinattributestable", {
        "INPUT": context.output("territorial-base") + "|layername=municipalities_250k", "FIELD": "CODIMUNI", "INPUT_2": context.output("indicators-table"),
        "FIELD_2": "mun_code", "FIELDS_TO_COPY": CSV_FIELDS, "METHOD": 1,
        "DISCARD_NONMATCHING": False, "PREFIX": "", "OUTPUT": context.output("joined-data")})
    context.processing("native:pointonsurface", {
        "INPUT": context.output("joined-data") + "|layername=municipal_joined",
        "ALL_PARTS": False, "OUTPUT": context.output("symbol-points")})

    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = "ESRI Shapefile"
    options.fileEncoding = "UTF-8"
    options.attributes = [base.fields().indexFromName(name) for name in ("CODIMUNI", "NOMMUNI", "CODICOMAR")]
    result = QgsVectorFileWriter.writeAsVectorFormatV3(
        base, context.output("municipalities-shp"), QgsProject.instance().transformContext(), options)
    if result[0] != QgsVectorFileWriter.NoError:
        raise ValueError("Shapefile export failed: " + str(result))
    shutil.copyfile("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", context.output("font-regular"))


def verify(context):
    """Reopen the saved datasets; expected values are independent course controls."""
    from qgis.PyQt.QtCore import QVariant
    base = _layer(context.output("territorial-base"), "Base", "municipalities_250k")
    county = _layer(context.output("territorial-base"), "Comarca", "comarca_250k")
    detail = _layer(context.output("territorial-base"), "Vila-seca", "vila_seca_50k")
    countries = _layer(context.output("counties-context"), "Comarques", "counties_250k")
    joined = _layer(context.output("joined-data"), "Unió", "municipal_joined")
    points = _layer(context.output("symbol-points"), "Punts", "municipal_points")
    table = _layer(context.output("indicators-table"), "CSV")
    shape = _layer(context.output("municipalities-shp"), "Shapefile")
    base_rows = {str(f["CODIMUNI"]): f for f in base.getFeatures()}
    joined_rows = {str(f["CODIMUNI"]): f for f in joined.getFeatures()}
    selected = {str(f["CODIMUNI"]) for f in joined.getFeatures() if f["housing_non_main_pct"] > 50}
    if selected != EXPECTED_ABOVE_50:
        raise ValueError("The >50% selection differs: " + repr(sorted(selected)))
    with Path(context.input("idescat-csv")).open(encoding="utf-8", newline="") as stream:
        original = {row["mun_code"]: row for row in csv.DictReader(stream)}
    agreement = 0
    for code, feature in joined_rows.items():
        row = original[code]
        if str(feature["mun_code"]) != code:
            raise ValueError("Unexpected key correspondence")
        for name in CSV_FIELDS[3:10]:
            if not math.isclose(float(feature[name]), float(row[name]), rel_tol=0, abs_tol=1e-10):
                raise ValueError("Persisted join changed " + code + ":" + name)
        agreement += 1
    total = sum(f["housing_total"] for f in joined_rows.values())
    non_main = sum(f["housing_non_main"] for f in joined_rows.values())
    geometries_equal = sum(f.geometry().equals(base_rows[code].geometry()) for code, f in joined_rows.items())
    inside = sum(base_rows[str(f["CODIMUNI"])].geometry().contains(f.geometry()) for f in points.getFeatures())
    shape_names = {str(f["CODIMUNI"]): str(f["NOMMUNI"]) for f in shape.getFeatures()}
    checks = []
    def add(identity, actual, expected, tolerance=0, units="count"):
        checks.append(dict(id=identity, actual=actual, expected=expected, tolerance=tolerance, units=units))
    for identity, layer, count in (("municipalities", base, 22), ("county", county, 1),
                                    ("focus-municipality", detail, 1), ("catalonia-counties", countries, 43),
                                    ("joined", joined, 22), ("symbol-points", points, 22),
                                    ("typed-csv", table, 22), ("shapefile", shape, 22)):
        add(identity + "-count", layer.featureCount(), count)
        if layer.isSpatial():
            add(identity + "-crs", int(layer.crs().authid() == "EPSG:25831"), 1)
            add(identity + "-invalid-geometries", sum(not f.geometry().isGeosValid() for f in layer.getFeatures()), 0)
    add("unique-base-keys", len(base_rows), 22)
    add("unique-joined-keys", len(joined_rows), 22)
    add("join-unmatched", len(set(base_rows) ^ set(joined_rows)), 0)
    add("values-agree-with-input", agreement, 22)
    add("geometry-preserved-by-join", geometries_equal, 22)
    add("points-inside-municipalities", inside, 22)
    add("six-municipalities-above-50", len(selected), 6)
    add("vila-seca-percentage", joined_rows["431711"]["housing_non_main_pct"], 49.9052649710053, 1e-10, "percent")
    add("roda-percentage", joined_rows["431310"]["housing_non_main_pct"], 64.7454918968272, 1e-10, "percent")
    add("pobla-percentage", joined_rows["431093"]["housing_non_main_pct"], 12.0743034055728, 1e-10, "percent")
    add("county-housing-total", total, 169179, units="dwellings")
    add("county-non-main", non_main, 66105, units="dwellings")
    add("county-ratio-of-sums", non_main / total * 100, 39.07399854591882, 1e-10, "percent")
    add("csv-key-is-text", int(table.fields().field("mun_code").type() == QVariant.String), 1)
    add("joined-percentage-is-real", int(joined.fields().field("housing_non_main_pct").type() == QVariant.Double), 1)
    add("shapefile-key-is-text", int(shape.fields().field("CODIMUNI").type() == QVariant.String), 1)
    add("shapefile-names-preserved", sum(shape_names[code] == str(f["NOMMUNI"]) for code, f in base_rows.items()), 22)
    add("font-bytes", Path(context.output("font-regular")).stat().st_size, 759720, units="bytes")
    return checks


def _quantile(values, proportion):
    ordered = sorted(values)
    index = (len(ordered) - 1) * proportion
    lower = math.floor(index)
    upper = math.ceil(index)
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (index - lower)


def compose(project, project_id, parameters, products):
    """Author-owned symbols/themes/base layout; generic saving and closure stay native."""
    from qgis.core import (QgsCoordinateReferenceSystem, QgsFillSymbol, QgsMarkerSymbol, QgsSingleSymbolRenderer,
                          QgsGraduatedSymbolRenderer, QgsRendererRange, QgsPalLayerSettings,
                          QgsTextFormat, QgsTextBufferSettings, QgsVectorLayerSimpleLabeling,
                          QgsMapThemeCollection, QgsPrintLayout, QgsLayoutItemMap, QgsLayoutItemLabel,
                          QgsLayoutPoint, QgsLayoutSize, QgsRectangle, QgsReferencedRectangle,
                          QgsAttributeTableConfig, QgsClassificationQuantile, QgsClassificationEqualInterval,
                          QgsColorBrewerColorRamp)
    from qgis.PyQt.QtGui import QFont, QColor

    mode = parameters.get("views", {}).get(project_id, "initial")
    if project.crs().authid() != "EPSG:25831":
        project.setCrs(QgsCoordinateReferenceSystem("EPSG:25831"))
    default_text = QgsTextFormat()
    default_text.setFont(QFont("DejaVu Sans"))
    default_text.setSize(9)
    project.styleSettings().setDefaultTextFormat(default_text)
    layers = {layer.name(): layer for layer in project.mapLayers().values()}
    view_extent = QgsRectangle(layers["Municipis · base"].extent())
    view_extent.scale(1.12)
    project.viewSettings().setDefaultViewExtent(QgsReferencedRectangle(view_extent, project.crs()))
    for name in ("Municipis · unió", "Indicadors · Idescat 2021"):
        if name not in layers:
            continue
        table_config = layers[name].attributeTableConfig()
        table_config.update(layers[name].fields())
        wanted = (["CODIMUNI", "NOMMUNI", "housing_total", "housing_non_main", "housing_non_main_pct"]
                  if name == "Municipis · unió" else ["mun_code", "municipality", "housing_total", "housing_non_main", "housing_non_main_pct"])
        aliases = {"CODIMUNI": "Codi", "mun_code": "Codi", "NOMMUNI": "Municipi", "municipality": "Municipi",
                   "housing_total": "Habitatges", "housing_non_main": "No principals", "housing_non_main_pct": "% no principal"}
        for field, alias in aliases.items():
            field_index = layers[name].fields().indexFromName(field)
            if field_index >= 0:
                layers[name].setFieldAlias(field_index, alias)
        columns = table_config.columns()
        for column in columns:
            column.hidden = column.type != QgsAttributeTableConfig.Field or column.name not in wanted
            if column.type == QgsAttributeTableConfig.Field:
                column.width = 160 if column.name in {"NOMMUNI", "municipality"} else 105
        columns.sort(key=lambda column: wanted.index(column.name) if column.name in wanted else len(wanted))
        table_config.setColumns(columns)
        layers[name].setAttributeTableConfig(table_config)
    def fill(name, colour, border="#59757c", width="0.20"):
        if name in layers:
            layers[name].setRenderer(QgsSingleSymbolRenderer(QgsFillSymbol.createSimple(
                {"color": colour, "outline_color": border, "outline_width": width})))
    def label(name, field="NOMMUNI", size=9):
        if name not in layers:
            return
        settings = QgsPalLayerSettings()
        settings.fieldName = field
        text = QgsTextFormat()
        text.setFont(QFont("DejaVu Sans"))
        text.setSize(size)
        text.setColor(QColor("#163a45"))
        buffer = QgsTextBufferSettings()
        buffer.setEnabled(True)
        buffer.setSize(0.7)
        buffer.setColor(QColor("#ffffff"))
        text.setBuffer(buffer)
        settings.setFormat(text)
        layers[name].setLabeling(QgsVectorLayerSimpleLabeling(settings))
        layers[name].setLabelsEnabled(True)
    fill("Municipis · base", "#e6eeed")
    fill("Municipis · Shapefile", "#e6eeed")
    fill("Comarca · contorn", "0,0,0,0", "#183c45", "0.55")
    fill("Vila-seca · detall", "0,0,0,0", "#d55e00", "0.65")
    fill("Catalunya · comarques", "#e8e9e4", "#ffffff", "0.15")
    fill("Tarragonès · localitzador", "#d55e00", "#8e3c16", "0.25")
    fill("Municipis · unió", "#d9e9ee")
    label("Municipis · base")
    if "Municipis · unió" in layers and mode == "join":
        label("Municipis · unió")

    palette = parameters.get("palette", ["#edf8fb", "#b2e2e2", "#66c2a4", "#2ca25f", "#006d2c"])
    if "Municipis · unió" in layers and mode not in {"initial", "join", "reference"}:
        values = [float(f["housing_non_main_pct"]) for f in layers["Municipis · unió"].getFeatures()]
        methods = {"Municipis · unió": [_quantile(values, i / 5) for i in range(6)],
                   "Coropleta · intervals iguals": [min(values) + (max(values) - min(values)) * i / 5 for i in range(6)]}
        for name, breaks in methods.items():
            if name not in layers:
                continue
            ranges = [QgsRendererRange(low, high, QgsFillSymbol.createSimple(
                {"color": palette[i], "outline_color": "#ffffff", "outline_width": "0.15"}),
                f"{low:.1f}–{high:.1f} %") for i, (low, high) in enumerate(zip(breaks, breaks[1:]))]
            renderer = QgsGraduatedSymbolRenderer("housing_non_main_pct", ranges)
            renderer.setClassificationMethod(QgsClassificationQuantile() if name == "Municipis · unió" else QgsClassificationEqualInterval())
            renderer.setSourceColorRamp(QgsColorBrewerColorRamp("BuGn", 5))
            layers[name].setRenderer(renderer)
            label(name, size=8.5)
            layers[name].styleManager().addStyleFromLayer("BuGn · " + ("quantils" if name == "Municipis · unió" else "intervals iguals"))

    for name in ("Símbols graduats", "Símbols proporcionals"):
        if name not in layers:
            continue
        values = sorted({float(f["housing_total"]) for f in layers[name].getFeatures()})
        if name == "Símbols graduats":
            breaks = [_quantile(values, i / 4) for i in range(5)]
            definitions = [(low, high, size, f"{low:.0f}–{high:.0f} habitatges")
                           for low, high, size in zip(breaks, breaks[1:], (2.5, 4.5, 7.0, 10.0))]
        else:
            # No active data-defined property is hidden from qgis-practice-v2.
            # These static sizes are proportional for this exact observed dataset;
            # new values require recomputing the authored model.
            edges = [0] + [(a + b) / 2 for a, b in zip(values, values[1:])] + [values[-1] + 1]
            definitions = [(edges[i], edges[i + 1], 12 * math.sqrt(value / max(values)), f"{value:.0f} habitatges")
                           for i, value in enumerate(values)]
        ranges = []
        for low, high, size, text in definitions:
            symbol = QgsMarkerSymbol.createSimple({"name": "circle", "color": "#2166ac",
                "outline_color": "#163a45", "outline_width": "0.15", "size": str(size)})
            symbol.setOpacity(0.72)
            ranges.append(QgsRendererRange(low, high, symbol, text))
        renderer = QgsGraduatedSymbolRenderer("housing_total", ranges)
        renderer.setGraduatedMethod(QgsGraduatedSymbolRenderer.GraduatedSize)
        if name == "Símbols graduats":
            renderer.setClassificationMethod(QgsClassificationQuantile())
        else:
            renderer.setMode(QgsGraduatedSymbolRenderer.Custom)
        layers[name].setRenderer(renderer)
        layers[name].styleManager().addStyleFromLayer(name)

    themes = {
        "Referència comarcal": ["Municipis · base", "Comarca · contorn", "Vila-seca · detall"],
        "Localització a Catalunya": ["Catalunya · comarques", "Tarragonès · localitzador"],
        "Detall municipal": ["Municipis · base", "Vila-seca · detall"],
    }
    if "Municipis · unió" in layers:
        themes["Unió comprovada"] = ["Municipis · unió", "Comarca · contorn", "Vila-seca · detall"]
    if "Coropleta · intervals iguals" in layers:
        themes["Coropleta · quantils"] = ["Municipis · unió", "Comarca · contorn", "Vila-seca · detall"]
        themes["Coropleta · intervals iguals"] = ["Coropleta · intervals iguals", "Comarca · contorn", "Vila-seca · detall"]
    for name in ("Símbols graduats", "Símbols proporcionals"):
        if name in layers:
            themes[name] = ["Municipis · base", name, "Comarca · contorn"]
    for name, names in themes.items():
        record = QgsMapThemeCollection.MapThemeRecord()
        for layer_name in names:
            if layer_name in layers:
                entry = QgsMapThemeCollection.MapThemeLayerRecord(layers[layer_name])
                entry.isVisible = True
                record.addLayerRecord(entry)
        project.mapThemeCollection().insert(name, record)
    theme = {"initial": "Referència comarcal", "join": "Unió comprovada", "reference": "Referència comarcal",
             "choropleth": "Coropleta · quantils", "graduated": "Símbols graduats", "proportional": "Símbols proporcionals"}[mode]
    visible = themes[theme]
    order = ["Vila-seca · detall", "Comarca · contorn", "Símbols graduats", "Símbols proporcionals",
             "Municipis · unió", "Coropleta · intervals iguals", "Municipis · base",
             "Tarragonès · localitzador", "Catalunya · comarques", "Municipis · Shapefile", "Indicadors · Idescat 2021"]
    project.layerTreeRoot().setHasCustomLayerOrder(True)
    project.layerTreeRoot().setCustomLayerOrder([layers[name] for name in order if name in layers])
    for node in project.layerTreeRoot().findLayers():
        node.setItemVisibilityChecked(node.layer().name() in visible)
    for layer in layers.values():
        layer.triggerRepaint()

    if mode in {"initial", "join"}:
        return
    for old in list(project.layoutManager().layouts()):
        project.layoutManager().removeLayout(old)
    layouts = {"Referència · base": ("Referència comarcal", "Tarragonès i Vila-seca · mapa de referència")}
    if "Coropleta · quantils" in themes:
        layouts.update({"Coropleta · base": ("Coropleta · quantils", "Habitatge no principal · Tarragonès, 2021"),
                        "Graduats · base": ("Símbols graduats", "Habitatges totals · símbols graduats, 2021"),
                        "Proporcionals · base": ("Símbols proporcionals", "Habitatges totals · mides proporcionals, 2021")})
    for name, (main_theme, title) in layouts.items():
        layout = QgsPrintLayout(project)
        layout.initializeDefaults()
        layout.pageCollection().page(0).setPageSize(QgsLayoutSize(150, 110))
        layout.setName(name)
        def text_item(identity, text, x, y, width, height, size):
            item = QgsLayoutItemLabel(layout)
            layout.addLayoutItem(item)
            item.setId(identity)
            item.setText(text)
            item.setFont(QFont("DejaVu Sans", size))
            item.attemptMove(QgsLayoutPoint(x, y))
            item.attemptResize(QgsLayoutSize(width, height))
        text_item("titol", title, 4, 2, 142, 9, 11)
        for identity, names, selected_theme, position, size, extent in (
            ("principal", themes[main_theme], main_theme, (4, 13), (101, 73), layers["Municipis · base"].extent()),
            ("localitzador", themes["Localització a Catalunya"], "Localització a Catalunya", (111, 13), (35, 35), layers["Catalunya · comarques"].extent()),
        ):
            frame = QgsLayoutItemMap(layout)
            layout.addLayoutItem(frame)
            frame.setId(identity)
            frame.attemptMove(QgsLayoutPoint(*position))
            frame.attemptResize(QgsLayoutSize(*size))
            frame.setCrs(project.crs())
            frame.setLayers([layers[n] for n in names])
            frame.setFollowVisibilityPreset(True)
            frame.setFollowVisibilityPresetName(selected_theme)
            box = QgsRectangle(extent)
            box.scale(1.12)
            frame.zoomToExtent(box)
        text_item("localitzacio", "Tarragonès\ndins de Catalunya", 111, 51, 35, 15, 8)
        text_item("fonts", "Dades: Idescat, 2021. Geometria: ICGC, 20-01-2026, CC BY 4.0.", 4, 89, 142, 8, 8)
        text_item("base-editable", "Base editable: llegenda i escala gràfica a completar al dissenyador.", 4, 98, 142, 8, 8)
        project.layoutManager().addLayout(layout)
