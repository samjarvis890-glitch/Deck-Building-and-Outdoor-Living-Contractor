import os
from PIL import Image

# Output directory
out_dir = r"assets/images/about"
os.makedirs(out_dir, exist_ok=True)

def convert_and_save(src_path, dst_name, target_size, quality=88):
    dst_path = os.path.join(out_dir, dst_name)
    im = Image.open(src_path)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    
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

# 1. Hero Image (Screenshot 1 fix: replaced white vase with newly generated bespoke multi-level deck & pergola)
hero_src = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\hero_deck_outdoor_living_1793850319432.jpg"
convert_and_save(hero_src, "about-hero.webp", (1400, 800), quality=88)

# 2. Lifestyle Panoramic Image (Screenshot 2 fix: replaced mountain hikers with newly generated indoor-outdoor flow deck)
lifestyle_src = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\indoor_outdoor_flow_deck_1793850483924.jpg"
convert_and_save(lifestyle_src, "about-lifestyle.webp", (1400, 750), quality=88)

# 3. Brand Philosophy Image (replaced attic living room with newly generated serene deck garden retreat)
philosophy_src = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\serene_deck_garden_retreat_1793850797959.jpg"
convert_and_save(philosophy_src, "about-philosophy.webp", (1000, 650), quality=88)

# 4. Final CTA (replaced indoor living room sofa with covered outdoor pavilion with fireplace)
convert_and_save("assets/images/index/home-final-cta.webp", "about-final-cta.webp", (1400, 700), quality=88)

# 5. Principles
# Principle 1: Natural Balance (pergola with lush garden & lounge)
convert_and_save("assets/images/index/home-featured-pergola.webp", "about-principle-balance.webp", (600, 450), quality=88)

# Principle 2: Functional Flow (outdoor dining under pergola)
convert_and_save("assets/images/index/home-gather.webp", "about-principle-function.webp", (600, 450), quality=88)

# Principle 3: Material Integrity (hardwood deck with steel railing overlooking landscape)
convert_and_save("assets/images/index/home-featured-deck.webp", "about-principle-materials.webp", (600, 450), quality=88)

# Principle 4: Refined Detailing (macro timber decking joinery and grain)
convert_and_save("assets/images/index/home-craftsmanship.webp", "about-principle-detail.webp", (600, 450), quality=88)

# 6. Craftsmanship Section Image
convert_and_save("assets/images/index/home-craftsmanship.webp", "about-craftsmanship.webp", (1000, 650), quality=88)

# 7. Planning Section Image (architect blueprints on deck)
convert_and_save("assets/images/index/home-project-journey.webp", "about-planning.webp", (1000, 650), quality=88)

# 8. Architectural Detail Cards
# Decking detail
convert_and_save("assets/images/index/home-featured-deck.webp", "about-detail-decking.webp", (600, 450), quality=88)

# Pergola detail
convert_and_save("assets/images/index/home-pergola.webp", "about-detail-pergola.webp", (600, 450), quality=88)

# Seating detail (sunken fire pit deck with built-in curved wooden bench seating)
convert_and_save("assets/images/index/home-featured-retreat.webp", "about-detail-seating.webp", (600, 450), quality=88)

# Landscaping detail (deck embedded in lush greenery & ferns)
convert_and_save("assets/images/index/home-relax.webp", "about-detail-landscaping.webp", (600, 450), quality=88)

# Lighting detail (recessed deck step lighting and ambient warm illumination)
convert_and_save("assets/images/index/home-deck.webp", "about-detail-lighting.webp", (600, 450), quality=88)

# 9. Commitment Section (completed architectural deck & pergola sanctuary)
convert_and_save("assets/images/index/home-deck.webp", "about-commitment.webp", (1000, 650), quality=88)

print("\nSuccessfully updated all 16 about page images!")
