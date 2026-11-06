with open('faq.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav_start = text.find('<nav')
nav_end = text.find('</nav>', nav_start) + 6
print(text[nav_start:nav_end])
