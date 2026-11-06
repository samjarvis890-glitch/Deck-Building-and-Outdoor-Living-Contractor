import os
from PIL import Image, ImageEnhance, ImageFilter

out_dir = r"assets/images/services"
os.makedirs(out_dir, exist_ok=True)

def process_and_save(src_path, dst_name, target_size, crop_box=None, quality=88, enhance=None):
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
    
    if enhance:
        if 'color' in enhance:
            cropped = ImageEnhance.Color(cropped).enhance(enhance['color'])
        if 'contrast' in enhance:
            cropped = ImageEnhance.Contrast(cropped).enhance(enhance['contrast'])
        if 'brightness' in enhance:
            cropped = ImageEnhance.Brightness(cropped).enhance(enhance['brightness'])
            
    cropped.save(dst_path, 'WEBP', quality=quality, method=6)
    size_kb = os.path.getsize(dst_path) / 1024
    print(f"Generated {dst_name}: {tw}x{th} -> {size_kb:.1f} KB (from {os.path.basename(src_path)})")

# 1. Hero Image (Screenshot 1 fix: replaced attic living room with grand design-approach multi-level deck & pergola)
process_and_save("assets/images/index/home-design-approach.webp", "services-hero.webp", (1400, 800), quality=88)

# 2. Overview Card 1: Decks
process_and_save("assets/images/index/home-featured-deck.webp", "service-overview-deck.webp", (800, 600), quality=88)

# 3. Overview Card 2: Pergolas (replaced indoor chair with louvred pergola)
process_and_save("assets/images/index/home-featured-pergola.webp", "service-overview-pergola.webp", (800, 600), quality=88)

# 4. Overview Card 3: Covered Spaces
process_and_save("assets/images/index/home-outdoor-living.webp", "service-overview-covered.webp", (800, 600), quality=88)

# 5. Overview Card 4: Patios (terrace patio with lounge & fire table)
process_and_save("assets/images/gallery/gallery-patio-firepit.webp", "service-overview-patio.webp", (800, 600), quality=88)

# 6. Overview Card 5: Renovation (replaced kitchen with precision deck refinishing)
process_and_save("assets/images/index/home-craftsmanship.webp", "service-overview-renovation.webp", (800, 600), quality=88)

# 7. Section 1 Main: Custom Deck Construction (replaced attic living room with multi-level illuminated deck)
process_and_save("assets/images/index/home-deck.webp", "service-deck-construction.webp", (1200, 800), quality=88)

# 8. Section 1 Detail: Deck Joinery (replaced clock with precision joinery macro)
process_and_save("assets/images/index/home-craftsmanship.webp", "service-deck-detail.webp", (600, 450), quality=88)

# 9. Section 1 Spec: Material Detail (replaced indoor living room with architectural blueprints & wood samples)
process_and_save("assets/images/index/home-project-journey.webp", "service-material-detail.webp", (600, 450), quality=88)

# 10. Section 2 Banner: Architectural Pergolas (replaced indoor sofa with grand cedar pergola)
process_and_save("assets/images/index/home-pergola.webp", "service-pergola-construction.webp", (1400, 750), quality=88)

# 11. Section 3 Feature: Covered Outdoor Living
process_and_save("assets/images/index/home-final-cta.webp", "service-covered-outdoor.webp", (1200, 750), quality=88)

# 12. Section 4 Main: Patio Design (replaced bedroom with modern paved terrace patio & fire table)
process_and_save("assets/images/index/home-enjoy.webp", "service-patio-design.webp", (1000, 700), quality=88)

# 13. Section 4 Sub 1: Entertainment Area (replaced kitchen with sunken fire pit lounge deck)
process_and_save("assets/images/index/home-featured-retreat.webp", "service-entertainment-area.webp", (600, 450), quality=88)

# 14. Section 4 Sub 2: Outdoor Dining (replaced soap bottle with garden pergola alfresco dining)
process_and_save("assets/images/index/home-gather.webp", "service-outdoor-dining.webp", (600, 450), quality=88)

# 15. Section 5 Renovation Existing (Before: weathered, aged, bleached timber deck)
process_and_save(
    "assets/images/index/home-craftsmanship.webp",
    "service-renovation-existing.webp",
    (800, 600),
    quality=88,
    enhance={'color': 0.15, 'contrast': 0.85, 'brightness': 1.15} # realistic sun-bleached weathered gray look
)

# 16. Section 5 Renovation Refresh (After: freshly stained, deep luster, golden-amber cedar finish)
process_and_save(
    "assets/images/index/home-craftsmanship.webp",
    "service-renovation-refresh.webp",
    (800, 600),
    quality=88,
    enhance={'color': 1.4, 'contrast': 1.25, 'brightness': 1.05} # rich saturated freshly oiled finish
)

# 17. Section 5 Renovation Refreshed (Restored deck plank macro)
process_and_save("assets/images/index/home-featured-deck.webp", "service-renovation-refreshed.webp", (800, 600), quality=88)

# 18. Section 5 Renovation Process Detail (replaced drill with contractor blueprint & leveling on deck)
process_and_save("assets/images/index/home-project-journey.webp", "service-deck-renovation.webp", (800, 600), quality=88)

# 19. Section 7 Pathway Visual: Spatial Organization
process_and_save("assets/images/index/home-hero.webp", "service-choose-space.webp", (1200, 750), quality=88)

# 20. Section 8 Final CTA Background (Screenshot 2 fix: warmly lit architectural timber pavilion at dusk)
process_and_save("assets/images/index/home-final-cta.webp", "services-final-cta.webp", (1400, 750), quality=88)

print("\nSuccessfully updated and optimized all 20 services images!")
