import sys
import re

# Read and extract just the dictionary from BricksExtras file
with open('C:\\Users\\Alpharez\\Desktop\\BricksExtras_Persian_Translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract dictionary using regex
match = re.search(r'translations = \{(.*?)\n\}', content, re.DOTALL)
if match:
    dict_str = '{' + match.group(1) + '}'
    try:
        translations = eval(dict_str)
        print(f"Loaded {len(translations)} translations")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
else:
    print("Could not find translations dict")
    sys.exit(1)

# Apply to PO file
po_file = 'bricksextras-fa_IR.po'
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

print(f"Applied {new_trans} new translations")
