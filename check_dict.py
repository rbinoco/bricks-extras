import re

with open('C:\\Users\\Alpharez\\Desktop\\BricksExtras_Persian_Translations.py', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'translations = \{(.*?)\n\}', content, re.DOTALL)
if match:
    dict_str = '{' + match.group(1) + '}'
    translations = eval(dict_str)

    # Show first 10 keys
    print("First 10 translation keys:")
    for i, key in enumerate(list(translations.keys())[:10]):
        print(f"{i+1}. {key}")

    # Check if specific keys exist
    test_keys = ['Header A', 'Header Notification Bar', 'Hotspots', 'Icon']
    print("\nChecking specific keys:")
    for key in test_keys:
        if key in translations:
            print(f"YES: {key}")
        else:
            print(f"NO: {key}")
