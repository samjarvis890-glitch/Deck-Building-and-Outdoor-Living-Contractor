with open('faq.html', 'r', encoding='utf-8') as f:
    text = f.read()

sec8_start = text.find('faq-support')
if sec8_start != -1:
    print("=== Section 8 snippet ===")
    print(text[sec8_start-100:sec8_start+1500])

sec9_start = text.find('faq-final-cta')
if sec9_start != -1:
    print("\n=== Section 9 snippet ===")
    print(text[sec9_start-100:sec9_start+1500])
