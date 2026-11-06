import glob
import re
from collections import Counter

html_files = sorted(glob.glob('*.html'))

all_h2_h3 = {}
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        text = f.read()
    
    headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', text, re.DOTALL)
    for h in headings:
        cleaned = ' '.join(re.sub(r'<[^>]+>', '', h).strip().split())
        if len(cleaned) > 10 and not cleaned.startswith('Quick Links') and not cleaned.startswith('Our Services') and not cleaned.startswith('Explore') and not cleaned.startswith('Customer Support') and not cleaned.startswith('Follow Us') and not cleaned.startswith('Get Outdoor Inspiration'):
            all_h2_h3.setdefault(cleaned, []).append(hf)

print("=== REPEATING HEADINGS ACROSS PAGES ===")
repeats_found = False
for heading, pages in all_h2_h3.items():
    if len(pages) > 1 and not (set(pages) == {'home-2.html', 'home2.html'}):
        print(f"Heading: '{heading}' appears in: {pages}")
        repeats_found = True

if not repeats_found:
    print("None found across different pages (excluding home2 vs home-2)!")

print("\n=== INTERNAL REPEATING HEADINGS WITHIN SAME PAGE ===")
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        text = f.read()
    headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', text, re.DOTALL)
    cleaned_h = [' '.join(re.sub(r'<[^>]+>', '', h).strip().split()) for h in headings]
    counts = Counter(cleaned_h)
    dup = {k: v for k, v in counts.items() if v > 1 and len(k) > 5}
    if dup:
        print(f"{hf}: {dup}")
