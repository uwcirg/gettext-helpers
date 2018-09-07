#!/usr/bin/env python
"""
Remove translation (msgstr) from entries where it is the same as the source (msgid)
Smartling copies msgid to msgstr for incomplete (In Progress) translations
"""

import sys
import polib

po_filename = sys.argv[1]
po = polib.pofile(po_filename)

sanitized = polib.POFile()
sanitized.metadata=po.metadata

for entry in po:
    msgstr = entry.msgstr

    # Assume untranslated if source and translation are the same
    if entry.msgid == entry.msgstr:
        msgstr = ""

    sanitized_entry = polib.POEntry(
        msgid=entry.msgid,
        msgstr=msgstr,
        occurrences=entry.occurrences
    )
    sanitized.append(sanitized_entry)

print sanitized
