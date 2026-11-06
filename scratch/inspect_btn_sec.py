with open('assets/css/faq.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.faq-btn-secondary')
print(text[idx:idx+800])
