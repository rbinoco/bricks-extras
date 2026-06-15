import re

with open('bricksextras-fa_IR.po', 'r', encoding='utf-8') as f:
    lines = f.readlines()

remaining = []
i = 0
while i < len(lines):
    if lines[i].startswith('msgid "'):
        match = re.match(r'msgid "(.*)"', lines[i].strip())
        if match:
            msgid = match.group(1)
            if i + 1 < len(lines) and lines[i+1].startswith('msgstr ""'):
                remaining.append(msgid)
        i += 1
    else:
        i += 1

# Save to file
with open('remaining_untranslated.txt', 'w', encoding='utf-8') as f:
    for s in remaining:
        f.write(s + '\n')

print(f"Extracted {len(remaining)} untranslated strings")
for i, s in enumerate(remaining[:20]):
    print(f"{i+1}. {s}")
