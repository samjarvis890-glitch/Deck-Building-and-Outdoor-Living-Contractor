with open('assets/css/responsive.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.final-cta-section {')
print(text[idx-50:idx+300])
