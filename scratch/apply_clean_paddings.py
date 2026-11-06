import os
import re

updates = {
    'assets/css/index.css': [
        ('.final-cta-section {\n  position: relative;\n  padding: 8rem 0;',
         '.final-cta-section {\n  position: relative;\n  padding: clamp(3.75rem, 6vw, 5.5rem) 0;')
    ],
    'assets/css/home2.css': [
        ('.home2-section {\n  padding: 6.5rem 0;',
         '.home2-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.home2-final {\n  position: relative;\n  padding: 8rem 0;',
         '.home2-final {\n  position: relative;\n  padding: clamp(3.75rem, 6vw, 5.5rem) 0;')
    ],
    'assets/css/about.css': [
        ('padding-top: calc(88px + 4rem);\n  padding-bottom: 5.5rem;',
         'padding-top: calc(var(--nav-height-desktop, 88px) + clamp(1.75rem, 3vw, 2.75rem));\n  padding-bottom: clamp(3rem, 4.5vw, 4.75rem);'),
        ('.about-philosophy-section {\n  padding: 6.5rem 0;',
         '.about-philosophy-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.about-lifestyle-section {\n  padding: 6.5rem 0;',
         '.about-lifestyle-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.about-principles-section {\n  padding: 6.5rem 0;',
         '.about-principles-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.about-craftsmanship-section {\n  padding: 6.5rem 0;',
         '.about-craftsmanship-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.about-planning-section {\n  padding: 6.5rem 0;',
         '.about-planning-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.about-details-section {\n  padding: 6.5rem 0;',
         '.about-details-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.about-commitment-section {\n  padding: 6.5rem 0;',
         '.about-commitment-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.about-final-cta-section {\n  position: relative;\n  padding: 8rem 0;',
         '.about-final-cta-section {\n  position: relative;\n  padding: clamp(3.75rem, 6vw, 5.5rem) 0;')
    ],
    'assets/css/services.css': [
        ('padding-top: calc(var(--header-height, 80px) + 3.5rem);\n  padding-bottom: 5.5rem;',
         'padding-top: calc(var(--nav-height-desktop, 88px) + clamp(1.75rem, 3vw, 2.75rem));\n  padding-bottom: clamp(3rem, 4.5vw, 4.75rem);'),
        ('.services-section {\n  padding: 6.5rem 0;',
         '.services-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.services-final-cta-section {\n  position: relative;\n  padding: 8rem 0;',
         '.services-final-cta-section {\n  position: relative;\n  padding: clamp(3.75rem, 6vw, 5.5rem) 0;')
    ],
    'assets/css/gallery.css': [
        ('.gallery-section {\n  padding: 6.5rem 0;',
         '.gallery-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.gallery-final-cta-section {\n  position: relative;\n  padding: 8rem 0;',
         '.gallery-final-cta-section {\n  position: relative;\n  padding: clamp(3.75rem, 6vw, 5.5rem) 0;')
    ],
    'assets/css/projects.css': [
        ('padding-top: calc(var(--header-height, 80px) + 3.5rem);\n  padding-bottom: 5.5rem;',
         'padding-top: calc(var(--nav-height-desktop, 88px) + clamp(1.75rem, 3vw, 2.75rem));\n  padding-bottom: clamp(3rem, 4.5vw, 4.75rem);'),
        ('.projects-section {\n  padding: 6.5rem 0;',
         '.projects-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.projects-final-cta-section {\n  position: relative;\n  padding: 8rem 0;',
         '.projects-final-cta-section {\n  position: relative;\n  padding: clamp(3.75rem, 6vw, 5.5rem) 0;')
    ],
    'assets/css/blog.css': [
        ('.blog-hero {\n  position: relative;\n  padding: calc(var(--nav-height-desktop) + 3rem) 0 5rem;',
         '.blog-hero {\n  position: relative;\n  padding: calc(var(--nav-height-desktop, 88px) + clamp(1.75rem, 3vw, 2.75rem)) 0 clamp(3rem, 4.5vw, 4.75rem);'),
        ('.blog-section {\n  padding: 5.5rem 0;',
         '.blog-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.blog-final-cta {\n  position: relative;\n  padding: 6.5rem 0;',
         '.blog-final-cta {\n  position: relative;\n  padding: clamp(3.75rem, 6vw, 5.5rem) 0;')
    ],
    'assets/css/faq.css': [
        ('.faq-hero {\n  position: relative;\n  padding: calc(var(--nav-height-desktop) + 3rem) 0 5rem;',
         '.faq-hero {\n  position: relative;\n  padding: calc(var(--nav-height-desktop, 88px) + clamp(1.75rem, 3vw, 2.75rem)) 0 clamp(3rem, 4.5vw, 4.75rem);'),
        ('.faq-section {\n  padding: 5.5rem 0;',
         '.faq-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.faq-final-cta {\n  position: relative;\n  padding: 6.5rem 0;',
         '.faq-final-cta {\n  position: relative;\n  padding: clamp(3.75rem, 6vw, 5.5rem) 0;')
    ],
    'assets/css/contact.css': [
        ('.contact-hero {\n  position: relative;\n  padding: calc(var(--nav-height-desktop) + 3rem) 0 5rem;',
         '.contact-hero {\n  position: relative;\n  padding: calc(var(--nav-height-desktop, 88px) + clamp(1.75rem, 3vw, 2.75rem)) 0 clamp(3rem, 4.5vw, 4.75rem);'),
        ('.contact-section {\n  padding: 5.5rem 0;',
         '.contact-section {\n  padding: clamp(3.25rem, 5.5vw, 5.5rem) 0;'),
        ('.contact-final-cta {\n  position: relative;\n  padding: 6.5rem 0;',
         '.contact-final-cta {\n  position: relative;\n  padding: clamp(3.75rem, 6vw, 5.5rem) 0;')
    ]
}

for path, pairs in updates.items():
    if not os.path.exists(path):
        print(f"Skipping {path}: not found")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    count = 0
    for old, new in pairs:
        # Normalize CRLF
        if old in c:
            c = c.replace(old, new)
            count += 1
        elif old.replace('\n', '\r\n') in c:
            c = c.replace(old.replace('\n', '\r\n'), new.replace('\n', '\r\n'))
            count += 1
        else:
            # try fuzzy regex replace if spacing differed
            print(f"  Note: exact target not matched in {path}: {repr(old[:30])}")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated {path}: {count} replacements applied.")
