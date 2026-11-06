import os

# Let's search for image files or references across the project
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gemini' in root:
        continue
    for f in files:
        if f.lower().endswith(('.jpg', '.webp', '.png', '.jpeg')):
            full_path = os.path.join(root, f)
            size = os.path.getsize(full_path)
            # print if not in assets/images or if interesting
            if not root.startswith('.\\assets\\images') and not root.startswith('./assets/images'):
                print(f"{full_path} ({size} bytes)")
