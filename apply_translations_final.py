#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

# Read the full translations from BricksExtras_Persian_Translations.py
with open("C:\\Users\\Alpharez\\Desktop\\BricksExtras_Persian_Translations.py", "r", encoding="utf-8") as f:
    content = f.read()

# Extract translations dictionary
match = re.search(r"translations = \{(.+?)\n\}", content, re.DOTALL)
if not match:
    print("Could not find translations dictionary")
    sys.exit(1)

# Parse translations
translations_text = "{" + match.group(1) + "}"
translations_dict = eval(translations_text)

print(f"Loaded {len(translations_dict)} translations")

# Apply to PO file
po_file = "bricksextras-fa_IR.po"
with open(po_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

result = []
i = 0
translated = 0
total = 0

while i < len(lines):
    line = lines[i]
    
    if line.startswith("msgid \""):
        match = re.match(r"msgid \"(.*)\"", line.strip())
        if match:
            msgid = match.group(1)
            total += 1
            result.append(line)
            i += 1
            
            if i < len(lines) and lines[i].startswith("msgstr"):
                match = re.match(r"msgstr \"(.*)\"", lines[i].strip())
                if match and match.group(1) == "" and msgid in translations_dict:
                    result.append(f"msgstr \"{translations_dict[msgid]}\"\n")
                    translated += 1
                else:
                    result.append(lines[i])
                i += 1
        else:
            result.append(line)
            i += 1
    else:
        result.append(line)
        i += 1

with open(po_file, "w", encoding="utf-8") as f:
    f.writelines(result)

print(f"✅ تمام شد!")
print(f"📊 ترجمه شده: {translated} رشته")
print(f"📈 مجموعی: {total} رشته")
