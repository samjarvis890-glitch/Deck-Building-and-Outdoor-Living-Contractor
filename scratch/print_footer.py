with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<footer class="site-footer"')
end = text.find('</footer>', start) + 9
print(text[start:end])
