with open('faq.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find Section 1 Hero in faq.html
sec1_start = text.find('class="faq-hero')
if sec1_start != -1:
    print(text[sec1_start:sec1_start+1000])
else:
    print("No class='faq-hero' found, searching 'section-hero' or 'hero'")
    for line in text.split('\n'):
        if 'hero' in line.lower():
            print(line[:100])
