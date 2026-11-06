import os
import re

for f in sorted(os.listdir('assets/css')):
    if f.endswith('.css'):
        p = os.path.join('assets/css', f)
        with open(p, 'r', encoding='utf-8') as file:
            content = file.read()
        matches = re.findall(r'([^{}]*\{[^{}]*(?:8rem|6\.5rem)[^{}]*\})', content)
        if matches:
            print(f"\n--- {f} has {len(matches)} occurrences ---")
            for m in matches:
                # print rule selector and padding
                sel = m.split('{')[0].strip()
                pad = [line.strip() for line in m.split('\n') if 'padding' in line]
                print(f"  {sel} -> {pad}")
