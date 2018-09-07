#!/usr/bin/env python
"""
Remove translation (msgstr) from entries where it is the same as the source (msgid)
Smartling copies msgid to msgstr for incomplete (In Progress) translations
"""

import sys
import polib

po_filename = sys.argv[1]
po = polib.pofile(po_filename)

translated_only = polib.POFile()
translated_only.metadata=po.metadata

for entry in po:
    if entry.msgid == entry.msgstr:
        continue
    translated_only.append(entry)

print translated_only
