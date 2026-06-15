#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply Agent-Generated Translations to PO File
"""

import re
import sys

# Import translations from agent-generated file
try:
    from persian_translations import MEGA_DICT
    print(f"Loaded {len(MEGA_DICT)} translations from persian_translations.py")
except ImportError:
    print("Could not import MEGA_DICT from persian_translations.py")
    sys.exit(1)

def apply_translations(po_file):
    """Apply translations from MEGA_DICT to PO file"""
    with open(po_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    new_translations = 0
    i = 0

    while i < len(lines):
        line = lines[i]
        if line.startswith('msgid "'):
            match = re.match(r'msgid "(.*)"', line.strip())
            if match:
                msgid = match.group(1)
                result.append(line)
                i += 1

                if i < len(lines) and lines[i].startswith('msgstr'):
                    match = re.match(r'msgstr "(.*)"', lines[i].strip())
                    if match and match.group(1) == '' and msgid in MEGA_DICT:
                        result.append(f'msgstr "{MEGA_DICT[msgid]}"\n')
                        new_translations += 1
                    else:
                        result.append(lines[i])
                    i += 1
            else:
                result.append(line)
                i += 1
        else:
            result.append(line)
            i += 1

    with open(po_file, 'w', encoding='utf-8') as f:
        f.writelines(result)

    print(f"Applied {new_translations} translations")
    return new_translations

if __name__ == "__main__":
    applied = apply_translations("bricksextras-fa_IR.po")
    print(f"Total new translations: {applied}")
