import re

with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

d_match = re.search(r'<ul class="drawer-nav-list">.*?</ul>', text, re.DOTALL)
if d_match:
    print(d_match.group(0))
