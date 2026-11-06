import glob
import re

html_files = sorted(glob.glob('*.html'))
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        text = f.read()
    
    sections = re.findall(r'<section[^>]*id=["\']([^"\']*)["\'][^>]*>', text)
    headings = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', text, re.DOTALL)
    # clean headings
    clean_headings = [re.sub(r'<[^>]+>', '', h).strip().replace('\n', ' ') for h in headings if len(h.strip()) > 0]
    # collapse multiple spaces
    clean_headings = [' '.join(h.split()) for h in clean_headings]
    
    print(f"=== {hf} ===")
    print(f"  Section IDs: {sections}")
    print(f"  Headings: {clean_headings[:8]}")
    print()
