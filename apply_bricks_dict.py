import sys
import re

# Read the BricksExtras translation file
with open('C:\\Users\\Alpharez\\Desktop\\BricksExtras_Persian_Translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Execute to load translations
exec(content)

# Now apply to PO file
po_file = 'C:\\Users\\Alpharez\\Desktop\\bricksextras\\bricksextras-fa_IR.po'
with open(po_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

result = []
new_trans = 0
i = 0

while i < len(lines):
    line = lines[i]
    if line.startswith('msgid "'):
        m = re.match(r'msgid "(.*)"', line.strip())
        if m:
            msgid = m.group(1)
            result.append(line)
            i += 1
            
            if i < len(lines) and lines[i].startswith('msgstr'):
                m2 = re.match(r'msgstr "(.*)"', lines[i].strip())
                if m2 and m2.group(1) == '' and msgid in translations:
                    result.append(f'msgstr "{translations[msgid]}"\n')
                    new_trans += 1
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

print(f"Done! Applied {new_trans} new translations")
