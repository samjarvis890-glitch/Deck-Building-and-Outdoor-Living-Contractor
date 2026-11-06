import os
import re

html_path = 'faq.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("--- 1. IMAGE EXISTENCE & SOURCE CHECK ---")
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total img tags in faq.html: {len(img_srcs)}")

missing_imgs = []
for src in img_srcs:
    if not src:
        continue
    clean_src = src.split('?')[0].split('#')[0]
    if not os.path.exists(clean_src):
        missing_imgs.append(clean_src)

if missing_imgs:
    print(f"FAILED: Missing images found: {missing_imgs}")
else:
    print("PASSED: All referenced image sources exist locally on disk!")

print("\n--- 2. EXACT 3 FAQ IMAGE ASSETS VERIFICATION ---")
required_3_images = [
    "faq-hero.webp",
    "faq-support.webp",
    "faq-final-cta.webp"
]

all_found = True
for img_name in required_3_images:
    file_path = os.path.join("assets", "images", "faq", img_name)
    if not os.path.exists(file_path):
        print(f"FAILED: Missing file {file_path}")
        all_found = False
    elif img_name not in html:
        print(f"FAILED: File {img_name} not referenced in faq.html")
        all_found = False

if all_found:
    print(f"PASSED: All {len(required_3_images)} unique FAQ images exist and are referenced in faq.html!")

print("\n--- 3. EXACT 9 SECTIONS VERIFICATION ---")
sections = [
    ("SECTION 1: FAQ Hero", r'<section[^>]+id=["\']faqHero["\']'),
    ("SECTION 2: Quick Search", r'<section[^>]+id=["\']faqSearch["\']'),
    ("SECTION 3: Category Navigation", r'<section[^>]+id=["\']faqCategories["\']'),
    ("SECTION 4: General Questions", r'<section[^>]+id=["\']sectionGeneral["\']'),
    ("SECTION 5: Decks, Pergolas & Covered Spaces", r'<section[^>]+id=["\']sectionStructures["\']'),
    ("SECTION 6: Materials & Finishes", r'<section[^>]+id=["\']sectionMaterials["\']'),
    ("SECTION 7: Planning & Consultations", r'<section[^>]+id=["\']sectionPlanning["\']'),
    ("SECTION 8: Still Have a Question", r'<section[^>]+id=["\']faqSupport["\']'),
    ("SECTION 9: Final CTA", r'<section[^>]+id=["\']finalCta["\']')
]

for name, pattern in sections:
    match = re.search(pattern, html)
    if match:
        print(f"PASSED: {name} found.")
    else:
        print(f"FAILED: {name} not found!")

main_sections = re.findall(r'<section\b', html)
print(f"Total <section> elements in faq.html: {len(main_sections)} (Must be exactly 9)")

print("\n--- 4. NAVBAR & FOOTER CONSISTENCY VERIFICATION ---")
if 'class="nav-link-item active" aria-current="page">FAQ</a>' in html:
    print("PASSED: FAQ nav link is active in desktop menu.")
else:
    print("WARNING: Check FAQ nav link active state in desktop menu.")

if 'class="drawer-link active" aria-current="page">FAQ</a>' in html:
    print("PASSED: FAQ drawer link is active in mobile drawer.")
else:
    print("WARNING: Check FAQ drawer link active state.")

# Check Quick Links 6 items
ql_match = re.search(r'<h4[^>]*>Quick Links</h4>\s*<ul[^>]*>(.*?)</ul>', html, re.DOTALL)
if ql_match:
    ql_links = re.findall(r'<li><a', ql_match.group(1))
    print(f"Quick Links count: {len(ql_links)} (Expected 6)")

# Check Our Services 6 items
os_match = re.search(r'<h4[^>]*>Our Services</h4>\s*<ul[^>]*>(.*?)</ul>', html, re.DOTALL)
if os_match:
    os_links = re.findall(r'<li><a', os_match.group(1))
    print(f"Our Services count: {len(os_links)} (Expected 6)")

# Check Explore 6 items
ex_match = re.search(r'<h4[^>]*>Explore</h4>\s*<ul[^>]*>(.*?)</ul>', html, re.DOTALL)
if ex_match:
    ex_links = re.findall(r'<li><a', ex_match.group(1))
    print(f"Explore count: {len(ex_links)} (Expected 6)")

# Check Customer Support 6 items
cs_match = re.search(r'<h4[^>]*>Customer Support</h4>\s*<ul[^>]*>(.*?)</ul>', html, re.DOTALL)
if cs_match:
    cs_links = re.findall(r'<li><a', cs_match.group(1))
    print(f"Customer Support count: {len(cs_links)} (Expected 6)")

print("\n--- 5. QUESTION ITEMS VERIFICATION ---")
items = re.findall(r'class="faq-item"\s+id="([^"]+)"', html)
print(f"Total question items in faq.html: {len(items)} (Expected 23)")
if len(items) == 23:
    print("PASSED: All 23 required questions are rendered!")
else:
    print("FAILED: Question count mismatch!")
