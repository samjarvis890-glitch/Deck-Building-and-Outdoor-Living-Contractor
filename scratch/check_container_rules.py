with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    i = text.find('.container', idx)
    if i == -1:
        break
    print(text[i:i+200])
    print("=" * 40)
    idx = i + 15
