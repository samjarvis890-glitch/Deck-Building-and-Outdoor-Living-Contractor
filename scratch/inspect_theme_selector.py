with open('assets/css/theme.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('[data-theme="dark"]')
print(text[idx-100:idx+400])
