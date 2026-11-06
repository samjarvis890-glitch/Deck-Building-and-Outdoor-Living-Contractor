with open('assets/css/faq.css', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of faq.css:", len(text))

# Let's search for hero, support, final-cta, and dark mode in faq.css
for section in ['faq-hero', 'faq-support', 'faq-final-cta', 'dark']:
    matches = [i for i in range(len(text)) if text.startswith(section, i) or text.startswith('.' + section, i) or text.startswith('[data-theme="dark"]' + section, i)]
    print(f"\nOccurrences related to '{section}': {len(matches)}")

# Let's check the final-cta rules specifically
idx = text.find('faq-final-cta')
if idx != -1:
    print("\n--- faq-final-cta CSS ---")
    print(text[idx-50:idx+1500])

# Let's check dark theme blocks in faq.css
dark_idx = 0
print("\n--- Dark theme blocks in faq.css ---")
while True:
    d = text.find('[data-theme="dark"]', dark_idx)
    if d == -1:
        break
    print(text[d:d+300])
    print("-" * 40)
    dark_idx = d + 300
