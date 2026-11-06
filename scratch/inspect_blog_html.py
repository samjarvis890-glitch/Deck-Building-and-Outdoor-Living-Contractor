import re

with open('blog.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find all sections
sections = re.findall(r'<section\b([^>]*)>(.*?)</section>', text, re.DOTALL)
print(f"Total sections in blog.html: {len(sections)}")
for i, (attrs, body) in enumerate(sections):
    id_m = re.search(r'id=["\']([^"\']*)["\']', attrs)
    cls_m = re.search(r'class=["\']([^"\']*)["\']', attrs)
    sid = id_m.group(1) if id_m else ''
    scls = cls_m.group(1) if cls_m else ''
    h_m = re.search(r'<h[1-3][^>]*>(.*?)</h[1-3]>', body, re.DOTALL)
    heading = re.sub(r'<[^>]+>', '', h_m.group(1)).strip() if h_m else ''
    imgs = re.findall(r'<img\b[^>]*src=["\']([^"\']*)["\']', body)
    print(f"[{i+1}] ID: '{sid}' | Class: '{scls}' | Imgs: {len(imgs)} | Title: '{heading[:50]}'")

# find all img tags in the entire file
all_imgs = re.findall(r'<img\b([^>]*)>', text)
print(f"\nTotal img tags in blog.html: {len(all_imgs)}")
for i, img_tag in enumerate(all_imgs):
    src_m = re.search(r'src=["\']([^"\']*)["\']', img_tag)
    alt_m = re.search(r'alt=["\']([^"\']*)["\']', img_tag)
    src = src_m.group(1) if src_m else ''
    alt = alt_m.group(1) if alt_m else ''
    print(f"{i+1:2d}. src='{src}' | alt='{alt[:60]}'")
