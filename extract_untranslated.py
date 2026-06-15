#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def extract_untranslated(input_file):
    """Extract all msgid strings that need translation."""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    untranslated = []
    i = 0

    while i < len(lines):
        line = lines[i]
        if line.startswith('msgid "'):
            msgid_match = re.match(r'msgid "(.*)"', line.strip())
            if msgid_match:
                msgid_text = msgid_match.group(1)
                # Get the next msgstr line
                if i + 1 < len(lines) and lines[i+1].startswith('msgstr'):
                    msgstr_match = re.match(r'msgstr "(.*)"', lines[i+1].strip())
                    if msgstr_match:
                        msgstr_text = msgstr_match.group(1)
                        # If msgstr is empty, it needs translation
                        if msgstr_text == '' and msgid_text != '':
                            untranslated.append(msgid_text)
            i += 1
        else:
            i += 1

    return untranslated

if __name__ == "__main__":
    untranslated = extract_untranslated("bricksextras-fa_IR.po")
    print(f"Total untranslated: {len(untranslated)}\n")

    # Print first 100 for analysis
    for i, text in enumerate(untranslated[:100]):
        print(f"{i+1}. {text}")
