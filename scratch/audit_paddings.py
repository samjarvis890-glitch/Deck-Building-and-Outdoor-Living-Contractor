import os
import re

css_files = [
    'style.css', 'responsive.css', 'index.css', 'home2.css',
    'about.css', 'services.css', 'gallery.css', 'projects.css',
    'blog.css', 'faq.css', 'contact.css'
]

print("=== AUDIT OF SECTION AND HERO PADDINGS ===")
for f in css_files:
    p = os.path.join('assets/css', f)
    if not os.path.exists(p):
        continue
    with open(p, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find all padding on sections or heroes
    heroes = re.findall(r'(\.[a-zA-Z0-9_\-]+hero[a-zA-Z0-9_\-]*\s*\{[^}]*padding[^}]*\})', content, re.IGNORECASE)
    sections = re.findall(r'(\.[a-zA-Z0-9_\-]+section[a-zA-Z0-9_\-]*\s*\{[^}]*padding[^}]*\})', content, re.IGNORECASE)
    containers = re.findall(r'(\.container\s*\{[^}]*padding[^}]*\})', content, re.IGNORECASE)
    
    print(f"\n--- {f} ---")
    if heroes:
        for h in heroes[:3]:
            print("  HERO:", h.replace('\n', ' ').strip()[:120])
    if sections:
        for s in sections[:3]:
            print("  SEC:", s.replace('\n', ' ').strip()[:120])
    if containers:
        for c in containers:
            print("  CONT:", c.replace('\n', ' ').strip()[:120])
