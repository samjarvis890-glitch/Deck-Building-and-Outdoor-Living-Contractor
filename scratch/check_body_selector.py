import os
import re

for f in ['about.css', 'blog.css', 'gallery.css', 'home2.css', 'index.css', 'navbar.css', 'projects.css', 'services.css']:
    p = os.path.join('assets/css', f)
    with open(p, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if re.search(r'\bbody\s*\{', line):
            prev = lines[i-1].strip() if i > 0 else ""
            print(f"{f}:{i+1} -> {prev} {line.strip()}")
