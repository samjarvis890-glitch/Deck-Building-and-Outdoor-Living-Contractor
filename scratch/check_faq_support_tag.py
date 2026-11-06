with open('faq.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="faqSupport"')
print(text[idx-50:idx+300])
