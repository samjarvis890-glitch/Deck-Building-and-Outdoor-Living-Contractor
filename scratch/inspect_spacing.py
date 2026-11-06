with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Check section padding, container padding, spacing variables
print("--- style.css Spacing Variables & Rules ---")
for line in text.split('\n'):
    if any(k in line.lower() for k in ['--spacing', '--section-padding', 'padding:', '.container {', 'section {']):
        print(line[:100])
