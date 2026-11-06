with open('faq.html', 'r', encoding='utf-8') as f:
    text = f.read()

sec1_start = text.find('class="faq-hero-grid"')
if sec1_start != -1:
    print(text[sec1_start:sec1_start+2500])
