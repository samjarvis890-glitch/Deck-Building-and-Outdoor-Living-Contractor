import os
import re

html_path = 'contact.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("--- 1. IMAGE EXISTENCE & SOURCE CHECK ---")
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total img tags in contact.html: {len(img_srcs)}")

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

print("\n--- 2. EXACT 5 CONTACT IMAGE ASSETS VERIFICATION ---")
required_5_images = [
    "contact-hero.webp",
    "contact-form-side.webp",
    "contact-checklist.webp",
    "contact-map-support.webp",
    "contact-final-cta.webp"
]

all_found = True
for img_name in required_5_images:
    file_path = os.path.join("assets", "images", "contact", img_name)
    if not os.path.exists(file_path):
        print(f"FAILED: Missing file {file_path}")
        all_found = False
    elif img_name not in html:
        print(f"FAILED: File {img_name} not referenced in contact.html")
        all_found = False

if all_found:
    print(f"PASSED: All {len(required_5_images)} unique Contact images exist and are referenced in contact.html!")

print("\n--- 3. EXACT 8 SECTIONS VERIFICATION ---")
sections = [
    ("SECTION 1: Contact Hero", r'<section[^>]+id=["\']contactHero["\']'),
    ("SECTION 2: Contact Information", r'<section[^>]+id=["\']contactInfo["\']'),
    ("SECTION 3: Project Enquiry Form", r'<section[^>]+id=["\']consultation["\']'),
    ("SECTION 4: Enquiry Process", r'<section[^>]+id=["\']contactProcess["\']'),
    ("SECTION 5: Location and Map", r'<section[^>]+id=["\']contactMap["\']'),
    ("SECTION 6: Project Checklist", r'<section[^>]+id=["\']contactChecklist["\']'),
    ("SECTION 7: Contact FAQs", r'<section[^>]+id=["\']contactFaq["\']'),
    ("SECTION 8: Final CTA", r'<section[^>]+id=["\']contactFinalCta["\']')
]

for name, pattern in sections:
    match = re.search(pattern, html)
    if match:
        print(f"PASSED: {name} found.")
    else:
        print(f"FAILED: {name} not found!")

main_sections = re.findall(r'<section\b', html)
print(f"Total <section> elements in contact.html: {len(main_sections)} (Must be exactly 8)")

print("\n--- 4. NAVBAR & FOOTER CONSISTENCY VERIFICATION ---")
if 'class="nav-link-item active" aria-current="page">Contact</a>' in html:
    print("PASSED: Contact nav link is active in desktop menu.")
else:
    print("WARNING: Check Contact nav link active state in desktop menu.")

if 'class="drawer-link active" aria-current="page">Contact</a>' in html:
    print("PASSED: Contact drawer link is active in mobile drawer.")
else:
    print("WARNING: Check Contact drawer link active state.")

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

print("\n--- 5. FORM MULTI-STEP CHECK ---")
step1_match = 'id="contactStep1"' in html
step2_match = 'id="contactStep2"' in html
step3_match = 'id="contactStep3"' in html
consent_match = 'id="enquiryConsent"' in html
feedback_match = 'id="contactFormFeedback"' in html

if step1_match and step2_match and step3_match and consent_match and feedback_match:
    print("PASSED: All 3 form steps, review, consent checkbox, and honest static demo feedback are present!")
else:
    print("FAILED: Missing form step elements!")
