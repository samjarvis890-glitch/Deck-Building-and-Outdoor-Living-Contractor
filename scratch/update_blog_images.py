import os
from PIL import Image

out_dir = r"assets/images/blog"
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

brain_hero = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\hero_deck_outdoor_living_1793850319432.jpg"
brain_flow = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\indoor_outdoor_flow_deck_1793850483924.jpg"
brain_retreat = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\serene_deck_garden_retreat_1793850797959.jpg"

print("--- GENERATING AND UPDATING BLOG IMAGES ---")

# 1. Blog Hero (Replaces attic couch room!)
process_and_save(brain_hero, "blog-hero.webp", (1400, 800), quality=90)

# 2. Featured Article (Replaces indoor living room!)
process_and_save(brain_flow, "blog-featured-article.webp", (1000, 650), quality=88)

# 3. Article 1: Deck Planning
process_and_save("scratch/test_architect_drawing_deck.jpg", "blog-article-deck-planning.webp", (800, 550), quality=88)

# 4. Article 2: Pergola Style (Replaces white indoor chair!)
process_and_save("assets/images/index/home-pergola.webp", "blog-article-pergola-style.webp", (800, 550), quality=88)

# 5. Article 3: Small Backyard Space (Replaces cabin on grass!)
process_and_save("assets/images/index/home-featured-retreat.webp", "blog-article-small-backyard.webp", (800, 550), quality=88)

# 6. Article 4: Deck Materials (Replaces WALL CLOCK!)
process_and_save("scratch/test_cedar_wood_grain.jpg", "blog-article-deck-materials.webp", (800, 550), quality=88)

# 7. Article 5: Outdoor Dining (Replaces SHAMPOO BOTTLE!)
process_and_save("assets/images/gallery/gallery-patio-dining.webp", "blog-article-outdoor-dining.webp", (800, 550), quality=88)

# 8. Article 6: Natural Style (Replaces HOTEL BEDROOM!)
process_and_save("assets/images/gallery/gallery-patio-gathering.webp", "blog-article-natural-style.webp", (800, 550), quality=88)

# 9. Topic 1: Deck Design
process_and_save("assets/images/index/home-featured-deck.webp", "blog-topic-deck-design.webp", (500, 350), quality=88)

# 10. Topic 2: Pergolas & Shade (Replaces SYNTHETIC PIL STRIPES!)
process_and_save("assets/images/index/home-featured-pergola.webp", "blog-topic-pergola.webp", (600, 450), quality=88)

# 11. Topic Pergolas variant (Replaces indoor futon!)
process_and_save("assets/images/index/home-featured-pergola.webp", "blog-topic-pergolas.webp", (500, 350), quality=88)

# 12. Topic 3: Outdoor Living (Replaces BEIGE HOTEL ROOM!)
process_and_save("assets/images/index/home-hero.webp", "blog-topic-outdoor-living.webp", (500, 350), quality=88)

# 13. Topic 4: Materials (Macro wood grain)
process_and_save("scratch/test_cedar_wood_grain.jpg", "blog-topic-materials.webp", (500, 350), quality=88)

# 14. Topic 5: Garden Integration (Replaces WINTER SNOW CABIN!)
process_and_save(brain_retreat, "blog-topic-garden.webp", (500, 350), quality=88)

# 15. Topic 6: Planning (Replaces SYNTHETIC PIL STRIPES!)
process_and_save("scratch/test_architect_drawing_deck.jpg", "blog-topic-planning.webp", (600, 450), quality=88)

# 16. Topic Maintenance (Replaces INDOOR KITCHEN!)
process_and_save("assets/images/index/home-project-journey.webp", "blog-topic-maintenance.webp", (500, 350), quality=88)

# 17. Guide 1: Deck Planning Guide
process_and_save("assets/images/index/home-deck.webp", "blog-guide-deck-planning.webp", (600, 450), quality=88)

# 18. Guide 2: Pergola Planning
process_and_save("assets/images/index/home-pergola.webp", "blog-guide-pergola-planning.webp", (600, 450), quality=88)

# 19. Guide 3: Entertaining (Replaces INDOOR KITCHEN!)
process_and_save("assets/images/index/home-gather.webp", "blog-guide-entertaining.webp", (600, 450), quality=88)

# 20. Material 1: Natural Timber (Replaces WALL CLOCK!)
process_and_save("scratch/test_cedar_wood_grain.jpg", "blog-material-natural-timber.webp", (600, 450), quality=88)

# 21. Material 2: Composite Decking (Concealed clips & joinery)
process_and_save("assets/images/index/home-craftsmanship.webp", "blog-material-composite.webp", (600, 450), quality=88)

# 22. Material 3: Natural Stone (Replaces INDOOR LIVING ROOM!)
process_and_save("assets/images/gallery/gallery-patio-gathering.webp", "blog-material-natural-stone.webp", (600, 450), quality=88)

# 23. Idea 1: Outdoor Lighting (Replaces INDOOR KITCHEN!)
process_and_save("scratch/test_stair_lights.webp", "blog-idea-outdoor-lighting.webp", (500, 350), quality=88)

# 24. Idea 2: Garden Seating (Replaces INDOOR FUTON!)
process_and_save("assets/images/index/home-relax.webp", "blog-idea-garden-seating.webp", (500, 350), quality=88)

# 25. Idea 3: Greenery & Pergolas (Replaces soil trowel!)
process_and_save("assets/images/index/home-featured-pergola.webp", "blog-idea-greenery.webp", (500, 350), quality=88)

# 26. Idea 4: Outdoor Finishing (Replaces INDOOR KITCHEN!)
process_and_save("assets/images/gallery/gallery-patio-dining.webp", "blog-idea-outdoor-finishing.webp", (500, 350), quality=88)

# 27. Newsletter (Architectural blueprints on desk)
process_and_save("scratch/test_architect_drawing_deck.jpg", "blog-newsletter.webp", (800, 600), quality=88)

# 28. Final CTA (Replaces concrete pool villa!)
process_and_save("assets/images/index/home-final-cta.webp", "blog-final-cta.webp", (1400, 700), quality=90)

print("--- ALL 28 BLOG IMAGES GENERATED SUCCESSFULLY ---")
