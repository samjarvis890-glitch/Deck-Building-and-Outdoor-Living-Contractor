with open('faq.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('savedTheme')
print(text[idx-50:idx+250])
