import re

with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find drawer body
d_match = re.search(r'<div class="drawer-body">.*?</div>', text, re.DOTALL)
if d_match:
    print(d_match.group(0))
