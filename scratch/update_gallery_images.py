import os
from PIL import Image

out_dir = r"assets/images/gallery"
os.makedirs(out_dir, exist_ok=True)

def process_and_save(src_path, dst_name, target_size, crop_box=None, quality=88):
    dst_path = os.path.join(out_dir, dst_name)
    im = Image.open(src_path)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    
    if crop_box:
        im = im.crop(crop_box)
        
    tw, th = target_size
    iw, ih = im.size
    scale = max(tw / iw, th / ih)
    nw = int(iw * scale)
    nh = int(ih * scale)
    im_resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
    
    left = (nw - tw) // 2
    top = (nh - th) // 2
    cropped = im_resized.crop((left, top, left + tw, top + th))
    
    cropped.save(dst_path, 'WEBP', quality=quality, method=6)
    size_kb = os.path.getsize(dst_path) / 1024
    print(f"Generated {dst_name}: {tw}x{th} -> {size_kb:.1f} KB (from {os.path.basename(src_path)})")

# Paths
brain_hero = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\hero_deck_outdoor_living_1793850319432.jpg"
brain_flow = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\indoor_outdoor_flow_deck_1793850483924.jpg"
brain_retreat = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\serene_deck_garden_retreat_1793850797959.jpg"

# 1. Hero Cover
process_and_save(brain_hero, "gallery-hero.webp", (1600, 900), quality=88)

# 2-7. Curated Portfolio Grid (6 items)
process_and_save("assets/images/index/home-deck.webp", "gallery-collection-deck.webp", (900, 700), quality=88)
process_and_save("assets/images/index/home-featured-pergola.webp", "gallery-collection-pergola.webp", (800, 1000), quality=88)
process_and_save("assets/images/index/home-outdoor-living.webp", "gallery-collection-covered.webp", (1000, 750), quality=88)
process_and_save("assets/images/gallery/gallery-patio-firepit.webp", "gallery-collection-patio.webp", (900, 650), quality=88)
process_and_save("assets/images/index/home-craftsmanship.webp", "gallery-collection-detail.webp", (750, 900), quality=88)
process_and_save(brain_retreat, "gallery-collection-landscape.webp", (1000, 700), quality=88)

# 8-11. Custom Decks in Focus (1 Lead + 3 Sub)
process_and_save("assets/images/index/home-featured-deck.webp", "gallery-deck-contemporary.webp", (1200, 800), quality=88)
process_and_save("assets/images/index/home-relax.webp", "gallery-deck-natural.webp", (800, 600), quality=88)
process_and_save("assets/images/index/home-design-approach.webp", "gallery-deck-levels.webp", (800, 600), quality=88)
process_and_save(brain_retreat, "gallery-deck-garden.webp", (800, 600), quality=88)

# 12-14. Architectural Pergolas (3 Cards)
process_and_save("assets/images/index/home-pergola.webp", "gallery-pergola-timber.webp", (900, 650), quality=88)
process_and_save(brain_hero, "gallery-pergola-modern.webp", (800, 600), quality=88)
process_and_save("assets/images/index/home-gather.webp", "gallery-pergola-garden.webp", (800, 600), quality=88)

# 15-17. Covered Environments (1 Lead + 2 Sub)
process_and_save("assets/images/index/home-outdoor-living.webp", "gallery-covered-architecture.webp", (1200, 800), quality=88)
process_and_save("assets/images/index/home-gather.webp", "gallery-covered-dining.webp", (800, 600), quality=88)
process_and_save("assets/images/index/home-final-cta.webp", "gallery-covered-lounge.webp", (800, 600), quality=88)

# 18-21. Patios & Gathering (4 Cards)
process_and_save("assets/images/index/home-enjoy.webp", "gallery-patio-dining.webp", (800, 600), quality=88)
process_and_save("assets/images/index/home-featured-retreat.webp", "gallery-patio-gathering.webp", (800, 600), quality=88)
process_and_save(brain_flow, "gallery-patio-relax.webp", (800, 600), quality=88)
process_and_save("assets/images/index/home-deck.webp", "gallery-patio-entertainment.webp", (800, 600), quality=88)

# 22-26. Architectural Details & Materials (5 Cards)
process_and_save("assets/images/index/home-craftsmanship.webp", "gallery-detail-timber.webp", (800, 600), quality=88)
process_and_save("assets/images/index/home-featured-deck.webp", "gallery-detail-decking.webp", (800, 600), quality=88)
process_and_save("assets/images/index/home-project-journey.webp", "gallery-detail-structure.webp", (800, 600), quality=88)
# For stone: crop the stone retaining wall from home-enjoy
im_enjoy = Image.open("assets/images/index/home-enjoy.webp")
ew, eh = im_enjoy.size
stone_crop = (int(ew * 0.55), int(eh * 0.25), ew, int(eh * 0.85))
process_and_save("assets/images/index/home-enjoy.webp", "gallery-detail-stone.webp", (800, 600), crop_box=stone_crop, quality=88)
# For lighting: crop the illuminated deck steps from home-deck
im_deck = Image.open("assets/images/index/home-deck.webp")
dw, dh = im_deck.size
light_crop = (int(dw * 0.2), int(dh * 0.3), int(dw * 0.8), dh)
process_and_save("assets/images/index/home-deck.webp", "gallery-detail-lighting.webp", (800, 600), crop_box=light_crop, quality=88)

# 27-30. Design Directions / Moodboards (4 Cards)
process_and_save(brain_retreat, "gallery-moodboard-natural.webp", (800, 800), quality=88)
process_and_save("assets/images/index/home-featured-deck.webp", "gallery-moodboard-contemporary.webp", (800, 800), quality=88)
process_and_save("assets/images/index/home-featured-retreat.webp", "gallery-moodboard-entertaining.webp", (800, 800), quality=88)
process_and_save("assets/images/index/home-relax.webp", "gallery-moodboard-garden.webp", (800, 800), quality=88)

# 31. Final CTA Background
process_and_save("assets/images/index/home-final-cta.webp", "gallery-final-cta.webp", (1600, 800), quality=88)

print("\nSuccessfully updated and optimized all 31 gallery images!")
