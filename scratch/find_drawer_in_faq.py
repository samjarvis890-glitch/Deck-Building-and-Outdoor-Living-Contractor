with open('faq.html', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.split('\n'):
    if 'drawer' in line.lower() or 'mobile-menu' in line.lower() or 'hamburger' in line.lower():
        print(line[:100])
