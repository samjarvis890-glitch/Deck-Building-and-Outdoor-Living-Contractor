with open('assets/css/faq.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    i = text.find('.faq-support', idx)
    if i == -1:
        break
    print(text[i:i+300])
    print("=" * 40)
    idx = i + 15
