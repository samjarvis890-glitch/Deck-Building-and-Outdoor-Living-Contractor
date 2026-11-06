import os
from PIL import Image

def crop_and_save(src_path, dest_path, target_w, target_h, quality=88):
    im = Image.open(src_path).convert('RGB')
    orig_w, orig_h = im.size
    target_ratio = target_w / target_h
    orig_ratio = orig_w / orig_h
    
    if orig_ratio > target_ratio:
        # source is wider -> crop width
        new_w = int(orig_h * target_ratio)
        left = (orig_w - new_w) // 2
        im_cropped = im.crop((left, 0, left + new_w, orig_h))
    else:
        # source is taller -> crop height
        new_h = int(orig_w / target_ratio)
        top = (orig_h - new_h) // 2
        im_cropped = im.crop((0, top, orig_w, top + new_h))
        
    im_resized = im_cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
    im_resized.save(dest_path, 'WEBP', quality=quality, method=6)
    print(f"Saved {dest_path}: {target_w}x{target_h} ({os.path.getsize(dest_path)} bytes)")

brain_dir = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea"

# 1. contact-hero.webp (1600x1000)
hero_src = os.path.join(brain_dir, "bespoke_deck_outdoor_living_1793873045878.jpg")
crop_and_save(hero_src, "assets/images/contact/contact-hero.webp", 1600, 1000, quality=88)

# 2. contact-form-side.webp (800x1000 vertical)
side_src = "scratch/candidates/candidate_pavilion.jpg"
crop_and_save(side_src, "assets/images/contact/contact-form-side.webp", 800, 1000, quality=88)

# 3. contact-map-support.webp (1200x600)
map_src = os.path.join(brain_dir, "serene_deck_garden_retreat_1793850797959.jpg")
crop_and_save(map_src, "assets/images/contact/contact-map-support.webp", 1200, 600, quality=88)

# 4. contact-checklist.webp (800x600)
check_src = "scratch/test_terrace_dining_stone.jpg"
crop_and_save(check_src, "assets/images/contact/contact-checklist.webp", 800, 600, quality=88)

# 5. contact-final-cta.webp (1600x800)
cta_src = "scratch/test_modern_villa_patio.jpg"
crop_and_save(cta_src, "assets/images/contact/contact-final-cta.webp", 1600, 800, quality=88)

print("\nAll 5 Contact images successfully updated and saved!")
