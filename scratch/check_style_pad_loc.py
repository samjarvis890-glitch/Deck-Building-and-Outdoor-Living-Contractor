with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('LAYOUT CONTAINERS & PADDING')
print(text[idx-50:idx+600])
