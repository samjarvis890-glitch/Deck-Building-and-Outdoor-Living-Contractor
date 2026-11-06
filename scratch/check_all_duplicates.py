import os, hashlib

all_imgs = {}
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png')):
            p = os.path.join(root, f)
            with open(p, 'rb') as fp:
                data = fp.read()
                h = hashlib.md5(data).hexdigest()
            if h in all_imgs:
                all_imgs[h].append(p)
            else:
                all_imgs[h] = [p]

duplicates = {k: v for k, v in all_imgs.items() if len(v) > 1}
print(f"Total unique hashes: {len(all_imgs)}")
print(f"Duplicates count: {len(duplicates)}")
for h, files in duplicates.items():
    print("DUPLICATE GROUP:")
    for f in files:
        print("  ", f)
