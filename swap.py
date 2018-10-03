#!/usr/bin/env python
"""
Swap source (msgid) and translation (msgstr); removing source language
"""
import sys
import polib

po_filename = sys.argv[1]
po = polib.pofile(po_filename)

translated_only = polib.POFile()
translated_only.metadata=po.metadata

for entry in po:
    # Do not emit empty translations
    if not entry.msgstr or entry.msgid == entry.msgstr:
        continue

    reversed_entry = polib.POEntry(
        msgid=entry.msgstr,
        msgstr="",
        occurrences=entry.occurrences
    )
    translated_only.append(reversed_entry)

print translated_only
