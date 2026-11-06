import os
from PIL import Image

search_dirs = [
    'scratch',
    'scratch/candidates',
    r'C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea'
]

available = []
for sdir in search_dirs:
    if os.path.exists(sdir):
        for f in os.listdir(sdir):
            if f.lower().endswith(('.jpg', '.jpeg', '.webp', '.png')):
                p = os.path.join(sdir, f)
                try:
                    with Image.open(p) as img:
                        w, h = img.size
                        # filter out screenshots and tiny icons
                        if not f.startswith(('screenshot', 'check_', 'cta_', 'audit_', 'verify_', 'exact_', 'thumb_')) and w >= 400 and h >= 300:
                            available.append((p, f, w, h, os.path.getsize(p)))
                except Exception:
                    pass

print(f"Total candidate images found: {len(available)}")
for p, f, w, h, s in available:
    print(f"  {f}: {w}x{h}, {s} bytes -> {p}")
