with open('faq.html', 'r', encoding='utf-8') as f:
    text = f.read()

drawer_start = text.find('class="nav-mobile-drawer"')
drawer_end = text.find('</aside>', drawer_start) + 8
print(text[drawer_start:drawer_end])
