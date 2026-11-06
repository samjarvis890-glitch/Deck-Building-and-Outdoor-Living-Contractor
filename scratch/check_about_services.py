import re, os

for page in ['about.html', 'services.html']:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
        print(f"=== {page} (Total images: {len(imgs)}) ===")
        for img in imgs:
            print("  ", img)
        bg_imgs = re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', content)
        if bg_imgs:
            print("  Inline CSS background images:")
            for b in bg_imgs:
                print("   ", b)
