with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find(':root')
print(text[idx:idx+1200])
