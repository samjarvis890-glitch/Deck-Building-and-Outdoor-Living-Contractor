import os
import re

css_files = ['style.css', 'index.css', 'home2.css', 'about.css', 'services.css', 'gallery.css', 'projects.css', 'blog.css', 'faq.css', 'contact.css', 'responsive.css']

for f in css_files:
    p = os.path.join('assets/css', f)
    with open(p, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # check media queries for max-width
    mqs = re.findall(r'@media\s*\([^)]*max-width[^)]*\)\s*\{([^}]*section[^}]*)\}', content, re.IGNORECASE)
    print(f"\n--- {f} Responsive Section Rules ---")
    if mqs:
        for m in mqs[:5]:
            print("  ", m.replace('\n', ' ').strip()[:100])
    else:
        print("  NO responsive section rules found!")
