with open('assets/css/contact.css', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of contact.css:", len(text))

# Let's search for hero, cta, and dark mode in contact.css
for section in ['contact-hero', 'contact-final-cta', 'dark']:
    matches = [i for i in range(len(text)) if text.startswith(section, i) or text.startswith('.' + section, i) or text.startswith('[data-theme="dark"]' + section, i)]
    print(f"Occurrences related to '{section}': {len(matches)}")

# Let's print the final-cta rules
idx = text.find('contact-final-cta')
if idx != -1:
    print("\n--- contact-final-cta CSS ---")
    print(text[idx-50:idx+1600])

# Let's check dark theme blocks in contact.css
print("\n--- Dark theme blocks in contact.css ---")
dark_idx = 0
while True:
    d = text.find('[data-theme="dark"]', dark_idx)
    if d == -1:
        break
    print(text[d:d+250])
    print("-" * 40)
    dark_idx = d + 250
