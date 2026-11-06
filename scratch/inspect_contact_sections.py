with open('contact.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]+>', text)
print("Sections in contact.html:")
for s in sections:
    print(" ", s)
