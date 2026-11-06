import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# find all sections
sections = re.findall(r'<section\b([^>]*)>(.*?)</section>', content, re.DOTALL)
print(f"Total sections: {len(sections)}")
for i, (attrs, body) in enumerate(sections):
    id_match = re.search(r'id=["\']([^"\']*)["\']', attrs)
    class_match = re.search(r'class=["\']([^"\']*)["\']', attrs)
    sid = id_match.group(1) if id_match else ''
    sclass = class_match.group(1) if class_match else ''
    
    h_match = re.search(r'<h[1-3][^>]*>(.*?)</h[1-3]>', body, re.DOTALL)
    heading = re.sub(r'<[^>]+>', '', h_match.group(1)).strip() if h_match else ''
    imgs = re.findall(r'<img\b[^>]*src=["\']([^"\']*)["\']', body)
    
    print(f"[{i+1}] ID: '{sid}' | Class: '{sclass}' | Imgs: {len(imgs)} | Title: '{heading[:50]}'")
