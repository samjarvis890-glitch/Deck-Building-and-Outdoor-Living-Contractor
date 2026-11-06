with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

header_start = text.find('<header')
header_end = text.find('</header>') + 9
print('=== INDEX HEADER ===')
print(text[header_start:header_end])

drawer_start = text.find('<div class="drawer-backdrop"')
drawer_end = text.find('</aside>') + 8
print('=== INDEX DRAWER ===')
print(text[drawer_start:drawer_end])
