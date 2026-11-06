import re

with open('projects.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section\b([^>]*)>(.*?)</section>', text, re.DOTALL)
print(f"Total sections: {len(sections)}")

for i, (attrs, body) in enumerate(sections):
    sid = re.search(r'id=["\']([^"\']*)["\']', attrs)
    scls = re.search(r'class=["\']([^"\']*)["\']', attrs)
    sid = sid.group(1) if sid else ''
    scls = scls.group(1) if scls else ''
    
    h_m = re.search(r'<h[1-3][^>]*>(.*?)</h[1-3]>', body, re.DOTALL)
    heading = re.sub(r'<[^>]+>', '', h_m.group(1)).strip() if h_m else ''
    
    imgs = re.findall(r'<img\b[^>]*src=["\']([^"\']*)["\'][^>]*alt=["\']([^"\']*)["\']', body)
    print(f"\n==================================================")
    print(f"Section {i+1}: ID='{sid}' | Class='{scls}' | Title='{heading}'")
    print(f"Images in this section ({len(imgs)}):")
    for src, alt in imgs:
        print(f"  - SRC: {src}")
        print(f"    ALT: {alt}")
