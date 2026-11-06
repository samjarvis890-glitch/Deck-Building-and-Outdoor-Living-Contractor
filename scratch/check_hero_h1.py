with open('assets/css/faq.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    i = text.find('faq-hero-h1', idx)
    if i == -1:
        break
    print(text[max(0, i-50):min(len(text), i+200)])
    print("=" * 40)
    idx = i + 20
