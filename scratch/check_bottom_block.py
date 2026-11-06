with open('assets/css/faq.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('/* --------------------------------------------------------------------------\n   HIGH CONTRAST & DARK MODE ENHANCEMENTS')
print(text[idx:])
