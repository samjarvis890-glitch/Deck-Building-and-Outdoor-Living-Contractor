with open('assets/css/theme.css', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.split('\n'):
    if 'data-theme="dark"' in line:
        print(line[:80])
