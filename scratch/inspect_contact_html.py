import re

with open('contact.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', text)
print("All img tags in contact.html:")
for m in matches:
    print("  -", m)

# Let's inspect each occurrence of contact images
for img in ['contact-hero.webp', 'contact-form-side.webp', 'contact-map-support.webp', 'contact-checklist.webp', 'contact-final-cta.webp']:
    idx = 0
    print(f"\n==================== Context for {img} ====================")
    while True:
        i = text.find(img, idx)
        if i == -1:
            break
        print(text[max(0, i-250):min(len(text), i+300)])
        print("-" * 40)
        idx = i + len(img)
