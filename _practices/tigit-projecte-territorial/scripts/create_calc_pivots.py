#!/usr/bin/env python3
"""Create real LibreOffice DataPilot tables in a workbook."""

from __future__ import annotations

import argparse
import subprocess
import time
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue
from com.sun.star.sheet.DataPilotFieldOrientation import COLUMN, DATA, ROW
from com.sun.star.sheet.GeneralFunction import COUNT, SUM
from com.sun.star.table import CellAddress, CellRangeAddress


def property_value(name, value):
    prop = PropertyValue()
    prop.Name = name
    prop.Value = value
    return prop


def connect(port: int):
    process = subprocess.Popen([
        "libreoffice", "--headless", "--nologo", "--nodefault", "--nofirststartwizard", "--norestore",
        f"--accept=socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext",
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_context)
    for _ in range(40):
        try:
            context = resolver.resolve(f"uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext")
            desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
            return process, desktop
        except Exception:
            time.sleep(0.25)
    process.terminate()
    raise RuntimeError("Could not connect to LibreOffice UNO")


def clear_sheet(sheet) -> None:
    cursor = sheet.createCursor()
    cursor.gotoEndOfUsedArea(True)
    cursor.clearContents(1023)


def insert_pivot(document, source_name, target_name, pivot_name, row_field, data_field, column_field=None, function=COUNT):
    sheets = document.getSheets()
    source = sheets.getByName(source_name)
    target = sheets.getByName(target_name)
    tables = target.getDataPilotTables()
    for existing in tables.getElementNames():
        tables.removeByName(existing)
    clear_sheet(target)

    source_cursor = source.createCursor()
    source_cursor.gotoEndOfUsedArea(True)
    source_range = source_cursor.getRangeAddress()
    descriptor = tables.createDataPilotDescriptor()
    descriptor.setSourceRange(CellRangeAddress(
        Sheet=source_range.Sheet,
        StartColumn=source_range.StartColumn,
        StartRow=source_range.StartRow,
        EndColumn=source_range.EndColumn,
        EndRow=source_range.EndRow,
    ))
    fields = descriptor.getDataPilotFields()
    fields.getByName(row_field).Orientation = ROW
    if column_field:
        fields.getByName(column_field).Orientation = COLUMN
    data = fields.getByName(data_field)
    data.Function = function
    data.Orientation = DATA
    tables.insertNewByName(pivot_name, CellAddress(Sheet=target.getRangeAddress().Sheet, Column=0, Row=0), descriptor)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--county", action="store_true")
    parser.add_argument("--schools", action="store_true")
    parser.add_argument("--population", action="store_true")
    args = parser.parse_args()

    process, desktop = connect(2083)
    document = None
    try:
        document = desktop.loadComponentFromURL(
            uno.systemPathToFileUrl(str(args.workbook.resolve())), "_blank", 0,
            (property_value("Hidden", True), property_value("UpdateDocMode", 3)),
        )
        if args.county:
            insert_pivot(document, "prepared_codes", "pivot_county_control", "CountyControl", "county_name", "municipality_code")
        if args.schools:
            insert_pivot(document, "prepared_schools", "pivot_schools_year", "SchoolsByYear", "year", "centre_code", "nature")
        if args.population:
            insert_pivot(document, "prepared_population_pyramid", "pivot_population_age_sex", "PopulationByAgeSex", "age_years", "population", "sex", SUM)
        document.calculateAll()
        document.store()
    finally:
        if document is not None:
            document.close(True)
        process.terminate()
        process.wait(timeout=10)
    print(args.workbook)


if __name__ == "__main__":
    main()
