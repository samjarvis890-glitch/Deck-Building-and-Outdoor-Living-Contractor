import os
from PIL import Image

# Replacement plan mapping: target_relative_path -> (source_path, target_width, target_height)
# All targets will be converted to high-quality WEBP
plan = {
    # Group 1: About
    'assets/images/about/about-principle-materials.webp': ('scratch/candidates/candidate_wood_planks.jpg', 600, 450),

    # Group 2: Projects
    'assets/images/projects/project-direction-relax.webp': ('scratch/candidates/candidate_deck_sanctuary.jpg', 600, 450),

    # Group 3: Blog
    'assets/images/blog/blog-guide-deck-planning.webp': ('scratch/test_architect_drawing_deck.jpg', 800, 500),

    # Group 4: Blog
    'assets/images/blog/blog-guide-pergola-planning.webp': ('scratch/test_backyard_lawn_pergola.jpg', 800, 500),

    # Group 5: Projects & Services
    'assets/images/projects/project-direction-expand.webp': ('scratch/test_outdoor_terrace_view.jpg', 600, 450),
    'assets/images/services/service-entertainment-area.webp': ('scratch/test_outdoor_sofa_patio.jpg', 600, 450),

    # Group 6: Projects
    'assets/images/projects/project-spotlight-deck.webp': ('scratch/candidates/candidate_sunken_deck.jpg', 1000, 650),

    # Group 7: Blog
    'assets/images/blog/blog-topic-pergola.webp': ('scratch/candidates/candidate_dining_pergola.jpg', 600, 450),

    # Group 8: Blog & Services
    'assets/images/blog/blog-material-composite.webp': ('scratch/test_timber_planks_texture.jpg', 600, 450),
    'assets/images/services/service-deck-detail.webp': ('scratch/test_deck_construction_wood.jpg', 600, 450),

    # Group 9: Blog, Projects & Services
    'assets/images/blog/blog-guide-entertaining.webp': ('scratch/test_outdoor_bistro_lights.jpg', 800, 500),
    'assets/images/projects/project-direction-entertain.webp': ('scratch/test_terrace_dining_stone.jpg', 600, 450),
    'assets/images/services/service-outdoor-dining.webp': ('scratch/candidates/candidate_covered_room.jpg', 600, 450),

    # Group 10: Blog
    'assets/images/blog/blog-final-cta.webp': (r'C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\luxury_deck_outdoor_living_twilight_1793869978542.jpg', 1400, 700),

    # Group 11: Blog
    'assets/images/blog/blog-hero.webp': (r'C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea\serene_deck_garden_retreat_1793850797959.jpg', 1400, 800),

    # Group 12: Blog
    'assets/images/blog/blog-topic-pergolas.webp': ('scratch/test_garden_deck_pergola.jpg', 600, 450),

    # Group 13: Blog
    'assets/images/blog/blog-material-natural-stone.webp': ('scratch/candidates/candidate_stone_wall.jpg', 600, 450),

    # Group 14: Blog
    'assets/images/blog/blog-material-natural-timber.webp': ('scratch/test_cedar_wood_grain.jpg', 600, 450),

    # Group 15: Blog
    'assets/images/blog/blog-newsletter.webp': ('scratch/test_modern_house_deck.jpg', 1200, 600),

    # Group 16: Gallery
    'assets/images/gallery/gallery-pergola-garden.webp': ('scratch/candidates/candidate_garden_deck.jpg', 800, 600),

    # Group 17: Gallery
    'assets/images/gallery/gallery-covered-pavilion.webp': ('scratch/candidates/candidate_pavilion.jpg', 800, 600),

    # Group 18: Gallery
    'assets/images/gallery/gallery-deck-courtyard.webp': ('scratch/candidates/candidate_courtyard.jpg', 800, 600),

    # Group 19: Gallery
    'assets/images/gallery/gallery-deck-poolside.webp': ('scratch/test_deck_pool_twilight.jpg', 800, 600),

    # Group 20: Gallery & Services
    'assets/images/gallery/gallery-detail-decking.webp': ('scratch/candidates/candidate_grain_texture.jpg', 600, 450),
    'assets/images/services/service-renovation-refreshed.webp': ('scratch/test_garden_walkway_deck.jpg', 800, 600),

    # Group 21: Gallery
    'assets/images/gallery/gallery-detail-structure.webp': ('scratch/candidates/candidate_oiled_cedar.jpg', 600, 450),

    # Group 22: Gallery
    'assets/images/gallery/gallery-detail-timber.webp': ('scratch/test_timber_wood_decking.jpg', 600, 450),

    # Group 23: Gallery
    'assets/images/gallery/gallery-patio-firepit.webp': ('scratch/candidates/candidate_firepit_deck.jpg', 800, 600),

    # Group 24: Gallery
    'assets/images/gallery/gallery-patio-relax.webp': ('scratch/candidates/candidate_patio_lounge.jpg', 800, 600),

    # Group 25: Services
    'assets/images/services/service-overview-pergola.webp': ('scratch/test_contemporary_patio.jpg', 800, 600),

    # Group 26: Services
    'assets/images/services/service-material-detail.webp': ('scratch/candidates/candidate_stone_timber.jpg', 600, 450)
}

def process_image(src, dst, target_w, target_h):
    with Image.open(src) as img:
        img = img.convert('RGB')
        src_w, src_h = img.size
        target_aspect = target_w / target_h
        src_aspect = src_w / src_h
        
        # Center crop to target aspect ratio
        if src_aspect > target_aspect:
            # Source is wider, crop width
            new_w = int(src_h * target_aspect)
            left = (src_w - new_w) // 2
            img = img.crop((left, 0, left + new_w, src_h))
        else:
            # Source is taller, crop height
            new_h = int(src_w / target_aspect)
            top = (src_h - new_h) // 2
            img = img.crop((0, top, src_w, top + new_h))
        
        img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        img.save(dst, 'WEBP', quality=92, method=6)
        print(f"Processed: {dst} ({target_w}x{target_h}) from {os.path.basename(src)}")

for dst, (src, tw, th) in plan.items():
    if not os.path.exists(src):
        print(f"ERROR: Source does not exist: {src}")
    else:
        process_image(src, dst, tw, th)

print("All replacements completed.")
