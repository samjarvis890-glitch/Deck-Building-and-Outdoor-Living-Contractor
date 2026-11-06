import re

with open('faq.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', text)
print('All img tags in faq.html:')
for m in matches:
    print('  -', m)

css_bg = re.findall(r'url\(["\']?([^"\')]+)["\']?\)', text)
print('CSS bg in faq.html:')
for c in css_bg:
    print('  -', c)

# Let's inspect sections referencing faq images
for img in ['faq-hero.webp', 'faq-support.webp', 'faq-final-cta.webp']:
    idx = text.find(img)
    if idx != -1:
        start = max(0, idx - 200)
        end = min(len(text), idx + 200)
        print(f"\n--- Context for {img} ---")
        print(text[start:end])
