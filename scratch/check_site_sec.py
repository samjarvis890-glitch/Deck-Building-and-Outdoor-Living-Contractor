with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.site-section')
print(text[idx-100:idx+800])
