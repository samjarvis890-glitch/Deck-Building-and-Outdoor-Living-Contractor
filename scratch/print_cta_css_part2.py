with open('assets/css/faq.css', 'r', encoding='utf-8') as f:
    text = f.read()

cta_idx = text.find('.faq-final-cta-btn-outline')
if cta_idx != -1:
    print(text[cta_idx:cta_idx+1200])
