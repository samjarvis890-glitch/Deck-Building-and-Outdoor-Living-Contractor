import os
from PIL import Image

out_dir = r"assets/images/projects"
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
    print(f"Generated {dst_name:<38}: {tw}x{th} -> {size_kb:.1f} KB (from {os.path.basename(src_path)})")

# Source paths
brain_hero = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\hero_deck_outdoor_living_1793850319432.jpg"
brain_flow = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\indoor_outdoor_flow_deck_1793850483924.jpg"
brain_retreat = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\serene_deck_garden_retreat_1793850797959.jpg"

print("--- GENERATING AND UPDATING PROJECTS IMAGES ---")

# 1. Hero Cover
process_and_save(brain_hero, "projects-hero.webp", (1400, 800), quality=90)

# 2. Concept 01: Contemporary Timber Deck
process_and_save("assets/images/index/home-deck.webp", "project-concept-timber-deck.webp", (800, 600), quality=88)

# 3. Concept 02: Garden Pergola Retreat (Replaces white chair & table)
process_and_save("assets/images/index/home-featured-pergola.webp", "project-concept-garden-pergola.webp", (800, 600), quality=88)

# 4. Concept 03: Covered Outdoor Lounge
process_and_save("assets/images/index/home-hero.webp", "project-concept-covered-lounge.webp", (800, 600), quality=88)

# 5. Concept 04: Outdoor Dining Courtyard (Replaces shampoo bottle!)
process_and_save("assets/images/gallery/gallery-patio-dining.webp", "project-concept-dining-courtyard.webp", (800, 600), quality=88)

# 6. Spotlight 01: A Deck That Brings The Garden Closer (Replaces attic couch room!)
process_and_save(brain_retreat, "project-spotlight-deck.webp", (1000, 650), quality=88)

# 7. Spotlight 02: Shade, Structure And A Sense Of Place (Replaces futon room!)
process_and_save("assets/images/index/home-pergola.webp", "project-spotlight-pergola.webp", (1000, 650), quality=88)

# 8. Design Thinking: Planning & Schematic
process_and_save("scratch/test_architect_drawing_deck.jpg", "project-design-planning.webp", (800, 600), quality=88)

# 9. Detail 01: Macro Timber Surface and Grain (Replaces wall clock!)
process_and_save("scratch/test_cedar_wood_grain.jpg", "project-detail-timber.webp", (600, 450), quality=88)

# 10. Detail 02: Structural Lines & Post-to-Beam (Replaces eucalyptus vase!)
process_and_save("assets/images/index/home-project-journey.webp", "project-detail-structure.webp", (600, 450), quality=88)

# 11. Detail 03: Natural Stone and Ground Transition (Replaces indoor living room!)
process_and_save("assets/images/gallery/gallery-patio-gathering.webp", "project-detail-stone.webp", (600, 450), quality=88)

# 12. Detail 04: Outdoor Lighting & Recessed Fixture (Replaces indoor kitchen!)
process_and_save("assets/images/about/about-detail-lighting.webp", "project-detail-lighting.webp", (600, 450), quality=88)

# 13. Direction 01: Relax and Unwind (Replaces hotel suite!)
process_and_save("assets/images/index/home-relax.webp", "project-direction-relax.webp", (600, 450), quality=88)

# 14. Direction 02: Gather and Entertain (Replaces apartment building!)
process_and_save("assets/images/index/home-gather.webp", "project-direction-entertain.webp", (600, 450), quality=88)

# 15. Direction 03: Extend Your Living Space (Replaces PIL stripe!)
process_and_save(brain_flow, "project-direction-extension.webp", (800, 600), quality=88)

# 16. Section 8 Final CTA (Replaces indoor living room!)
process_and_save("assets/images/index/home-final-cta.webp", "projects-final-cta.webp", (1400, 700), quality=90)

# 17. Direction Expand (Backup asset)
process_and_save("assets/images/index/home-featured-retreat.webp", "project-direction-expand.webp", (600, 450), quality=88)

print("--- ALL 17 IMAGES GENERATED SUCCESSFULLY ---")
