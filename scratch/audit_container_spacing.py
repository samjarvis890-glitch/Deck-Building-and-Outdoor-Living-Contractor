import os
import re

files = [f for f in os.listdir('assets/css') if f.endswith('.css')]

print("=== CHECK CONTAINER PADDINGS ===")
for f in files:
    with open(os.path.join('assets/css', f), 'r', encoding='utf-8') as file:
        c = file.read()
    containers = re.findall(r'(\.container\b[^{]*\{[^}]*\})', c)
    if containers:
        print(f"\n{f}:")
        for cont in containers:
            print("  ", cont.replace('\n', ' '))

print("\n=== CHECK BODY & MAIN PADDINGS ===")
for f in files:
    with open(os.path.join('assets/css', f), 'r', encoding='utf-8') as file:
        c = file.read()
    bm = re.findall(r'((?:body|main)\s*\{[^}]*padding[^}]*\})', c)
    if bm:
        print(f"\n{f}:")
        for b in bm:
            print("  ", b.replace('\n', ' '))
