import re
import os

with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

srcs = re.findall(r'<img\b[^>]*src=["\']([^"\']+)["\']', html)
print(f"Total img tags in gallery.html: {len(srcs)}")

unique_srcs = sorted(list(set(srcs)))
print(f"Unique img sources: {len(unique_srcs)}")

missing = []
for s in unique_srcs:
    clean_s = s.split('?')[0].split('#')[0]
    if not os.path.exists(clean_s):
        missing.append(s)
    else:
        size = os.path.getsize(clean_s)
        # print first few
        # print(f"  OK: {clean_s} ({size/1024:.1f} KB)")

print(f"Missing image files: {len(missing)}")
if missing:
    print("Missing:", missing)
else:
    print("ALL 100% of image references in gallery.html exist and are valid on disk!")
