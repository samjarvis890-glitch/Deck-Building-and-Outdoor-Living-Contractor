import os
import re

for root, dirs, files in os.walk('assets/css'):
    for f in files:
        if f.endswith('.css'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as file:
                c = file.read()
            matches = [m.start() for m in re.finditer(r'--bg-surface', c)]
            if matches:
                print(f"File {p} has {len(matches)} occurrences:")
                for m in matches:
                    print("  " + c[max(0, m-40):min(len(c), m+60)].replace('\n', ' '))
