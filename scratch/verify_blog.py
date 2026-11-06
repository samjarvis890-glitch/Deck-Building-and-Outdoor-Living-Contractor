import os
import re

html_path = 'blog.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("--- 1. IMAGE EXISTENCE & SOURCE CHECK ---")
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f"Total img tags in blog.html: {len(img_srcs)}")

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

print("\n--- 2. EXACT 26 BLOG IMAGE ASSETS VERIFICATION ---")
required_26_images = [
    "blog-hero.webp",
    "blog-featured-article.webp",
    "blog-article-deck-planning.webp",
    "blog-article-pergola-style.webp",
    "blog-article-small-backyard.webp",
    "blog-article-deck-materials.webp",
    "blog-article-outdoor-dining.webp",
    "blog-article-natural-style.webp",
    "blog-topic-deck-design.webp",
    "blog-topic-pergola.webp",
    "blog-topic-outdoor-living.webp",
    "blog-topic-materials.webp",
    "blog-topic-garden.webp",
    "blog-topic-planning.webp",
    "blog-guide-deck-planning.webp",
    "blog-guide-pergola-planning.webp",
    "blog-guide-entertaining.webp",
    "blog-material-natural-timber.webp",
    "blog-material-composite.webp",
    "blog-material-natural-stone.webp",
    "blog-idea-outdoor-lighting.webp",
    "blog-idea-garden-seating.webp",
    "blog-idea-greenery.webp",
    "blog-idea-outdoor-finishing.webp",
    "blog-newsletter.webp",
    "blog-final-cta.webp"
]

all_found = True
for img_name in required_26_images:
    file_path = os.path.join("assets", "images", "blog", img_name)
    if not os.path.exists(file_path):
        print(f"FAILED: Missing file {file_path}")
        all_found = False
    elif img_name not in html:
        print(f"FAILED: File {img_name} not referenced in blog.html")
        all_found = False

if all_found:
    print(f"PASSED: All {len(required_26_images)} unique blog images are generated and referenced!")

print("\n--- 3. EXACT 9 SECTIONS VERIFICATION ---")
sections = [
    ("SECTION 1: Hero", r'<section[^>]+id=["\']journalHero["\']'),
    ("SECTION 2: Featured Article", r'<section[^>]+id=["\']featuredArticle["\']'),
    ("SECTION 3: Latest Articles", r'<section[^>]+id=["\']latestArticles["\']'),
    ("SECTION 4: Browse By Topic", r'<section[^>]+id=["\']browseTopics["\']'),
    ("SECTION 5: Practical Guides", r'<section[^>]+id=["\']practicalGuides["\']'),
    ("SECTION 6: Material Knowledge", r'<section[^>]+id=["\']materialKnowledge["\']'),
    ("SECTION 7: Outdoor Design Ideas", r'<section[^>]+id=["\']designIdeas["\']'),
    ("SECTION 8: Journal Subscription", r'<section[^>]+id=["\']journalSubscription["\']'),
    ("SECTION 9: Final CTA", r'<section[^>]+id=["\']finalCta["\']')
]

for name, pattern in sections:
    match = re.search(pattern, html)
    if match:
        print(f"PASSED: {name} found.")
    else:
        print(f"FAILED: {name} not found!")

main_sections = re.findall(r'<section\b', html)
print(f"Total <section> elements in blog.html: {len(main_sections)} (Must be exactly 9)")

print("\n--- 4. NAVBAR & FOOTER CONSISTENCY VERIFICATION ---")
# Check active Blog state
if 'class="nav-link-item active" aria-current="page">Blog</a>' in html:
    print("PASSED: Blog nav link is active in desktop menu.")
else:
    print("WARNING: Check blog nav link active state in desktop menu.")

if 'class="drawer-link active" aria-current="page">Blog</a>' in html:
    print("PASSED: Blog nav link is active in mobile drawer.")
else:
    print("WARNING: Check blog drawer link active state.")

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

# Check Article Modal
if 'id="blogArticleModal"' in html:
    print("PASSED: Article Detail Modal (#blogArticleModal) is present.")
else:
    print("FAILED: Article Detail Modal is missing!")

# Check Search and Filters
if 'id="blogSearchInput"' in html and 'id="articleCardsContainer"' in html:
    print("PASSED: Search field and Article container are present.")
else:
    print("FAILED: Search input or Article container missing!")
