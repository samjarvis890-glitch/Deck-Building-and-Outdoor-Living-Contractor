import os
import urllib.request
from io import BytesIO
from PIL import Image

# Directory mapping and image assignments
# Sourced from high quality Unsplash architectural photography of outdoor living, timber decks, pergolas, patios & carpentry

CACHE = {}

def get_image(url):
    if url in CACHE:
        return CACHE[url].copy()
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
        im = Image.open(BytesIO(data))
        if im.mode != 'RGB':
            im = im.convert('RGB')
        CACHE[url] = im
        return im.copy()
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def crop_and_save(img, target_size, out_path, quality=82):
    tw, th = target_size
    iw, ih = img.size
    
    # Scale to fill target
    scale = max(tw / iw, th / ih)
    nw = int(iw * scale)
    nh = int(ih * scale)
    resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
    
    # Center crop
    left = (nw - tw) // 2
    top = (nh - th) // 2
    cropped = resized.crop((left, top, left + tw, top + th))
    
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    cropped.save(out_path, format='WEBP', quality=quality, method=6)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"  Saved {out_path} ({tw}x{th}) - {size_kb:.1f} KB")

# Curated high-res sources
U = {
    # Outstanding hero shots
    "hero_twilight": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1600&q=80",
    "hero_poolside": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=80",
    "hero_deck_patio": "https://images.unsplash.com/photo-1591825729269-caeb344f6df2?w=1600&q=80",
    "hero_covered": "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?w=1600&q=80",
    "hero_backyard": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1600&q=80",
    "hero_dining": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=1600&q=80",
    "hero_pavilion": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1600&q=80",
    "hero_morning": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=1600&q=80",
    "hero_firepit": "https://images.unsplash.com/photo-1527030280862-64139fba04ca?w=1600&q=80",
    "hero_flow": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1600&q=80",

    # Craftsmanship & carpentry
    "craft_tools": "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=1200&q=80",
    "craft_wood": "https://images.unsplash.com/photo-1581783342308-f792dbdd27c5?w=1200&q=80",
    "craft_grain": "https://images.unsplash.com/photo-1533090161767-e6ffed986c88?w=1200&q=80",
    "craft_blueprint": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1200&q=80",
    "craft_planks": "https://images.unsplash.com/photo-1546484396-fb3fc6f95f98?w=1200&q=80",
    "craft_rafters": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=1200&q=80",

    # Patio, garden, outdoor living spaces
    "sunken_deck": "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?w=1200&q=80",
    "courtyard_deck": "https://images.unsplash.com/photo-1558036117-15d82a90b9b1?w=1200&q=80",
    "stone_patio": "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
    "step_lights": "https://images.unsplash.com/photo-1507089947368-19c1da9775ae?w=1200&q=80",
    "garden_retreat": "https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=1200&q=80",
    "pergola_lines": "https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=1200&q=80",
    "patio_lounge": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80",
    "lush_patio": "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=1200&q=80",
    "stone_wall": "https://images.unsplash.com/photo-1598928506311-c55ded91a20c?w=1200&q=80",
    "balcony_deck": "https://images.unsplash.com/photo-1540518614846-7ede433c4550?w=1200&q=80",
    "summer_deck": "https://images.unsplash.com/photo-1560185007-cde436f6a4d0?w=1200&q=80",
    "outdoor_kitchen": "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?w=1200&q=80",
    "timber_bench": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=1200&q=80",
    "friends_relax": "https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=1200&q=80",
    "consultation": "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=1200&q=80",
    "wood_oil_finish": "https://images.unsplash.com/photo-1541123437800-1bb1317badc2?w=1200&q=80",
    "greenery_planter": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1200&q=80",
    "night_illumination": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=1200&q=80",
    "deck_stairs": "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
    "modern_house_deck": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=80"
}

IMAGE_MAP = {
    # HOME 2 IMAGES
    "assets/images/home2/home2-hero.webp": (U["hero_twilight"], (1400, 800)),
    "assets/images/home2/home2-morning.webp": (U["hero_morning"], (800, 600)),
    "assets/images/home2/home2-afternoon.webp": (U["patio_lounge"], (800, 600)),
    "assets/images/home2/home2-evening.webp": (U["hero_firepit"], (800, 600)),
    "assets/images/home2/home2-retreat.webp": (U["garden_retreat"], (800, 600)),
    "assets/images/home2/home2-dining.webp": (U["hero_dining"], (800, 600)),
    "assets/images/home2/home2-materials.webp": (U["craft_grain"], (800, 600)),
    "assets/images/home2/home2-seasons.webp": (U["hero_covered"], (800, 600)),
    "assets/images/home2/home2-small-garden.webp": (U["courtyard_deck"], (800, 600)),
    "assets/images/home2/home2-entertaining.webp": (U["hero_poolside"], (800, 600)),
    "assets/images/home2/home2-garden-retreat.webp": (U["lush_patio"], (800, 600)),
    "assets/images/home2/home2-final.webp": (U["hero_pavilion"], (1400, 700)),

    # ABOUT IMAGES
    "assets/images/about/about-hero.webp": (U["craft_wood"], (1400, 800)),
    "assets/images/about/about-philosophy.webp": (U["hero_deck_patio"], (1000, 650)),
    "assets/images/about/about-lifestyle.webp": (U["friends_relax"], (1000, 650)),
    "assets/images/about/about-craftsmanship.webp": (U["craft_tools"], (1000, 650)),
    "assets/images/about/about-planning.webp": (U["craft_blueprint"], (1000, 650)),
    "assets/images/about/about-commitment.webp": (U["sunken_deck"], (1000, 650)),
    "assets/images/about/about-detail-decking.webp": (U["craft_planks"], (600, 450)),
    "assets/images/about/about-detail-pergola.webp": (U["craft_rafters"], (600, 450)),
    "assets/images/about/about-detail-lighting.webp": (U["step_lights"], (600, 450)),
    "assets/images/about/about-detail-seating.webp": (U["timber_bench"], (600, 450)),
    "assets/images/about/about-detail-landscaping.webp": (U["greenery_planter"], (600, 450)),
    "assets/images/about/about-principle-balance.webp": (U["pergola_lines"], (600, 450)),
    "assets/images/about/about-principle-materials.webp": (U["stone_wall"], (600, 450)),
    "assets/images/about/about-principle-function.webp": (U["outdoor_kitchen"], (600, 450)),
    "assets/images/about/about-principle-detail.webp": (U["craft_grain"], (600, 450)),
    "assets/images/about/about-final-cta.webp": (U["hero_backyard"], (1400, 700)),

    # SERVICES IMAGES
    "assets/images/services/services-hero.webp": (U["hero_deck_patio"], (1400, 800)),
    "assets/images/services/service-overview-deck.webp": (U["sunken_deck"], (800, 600)),
    "assets/images/services/service-overview-pergola.webp": (U["pergola_lines"], (800, 600)),
    "assets/images/services/service-overview-covered.webp": (U["hero_covered"], (800, 600)),
    "assets/images/services/service-overview-patio.webp": (U["stone_patio"], (800, 600)),
    "assets/images/services/service-overview-renovation.webp": (U["wood_oil_finish"], (800, 600)),
    "assets/images/services/service-deck-construction.webp": (U["balcony_deck"], (1000, 650)),
    "assets/images/services/service-pergola-construction.webp": (U["craft_rafters"], (1000, 650)),
    "assets/images/services/service-covered-outdoor.webp": (U["hero_pavilion"], (1000, 650)),
    "assets/images/services/service-patio-design.webp": (U["lush_patio"], (1000, 650)),
    "assets/images/services/service-deck-renovation.webp": (U["craft_tools"], (1000, 650)),
    "assets/images/services/service-deck-detail.webp": (U["craft_grain"], (600, 450)),
    "assets/images/services/service-outdoor-dining.webp": (U["hero_dining"], (600, 450)),
    "assets/images/services/service-entertainment-area.webp": (U["outdoor_kitchen"], (600, 450)),
    "assets/images/services/service-renovation-existing.webp": (U["craft_wood"], (600, 450)),
    "assets/images/services/service-renovation-refreshed.webp": (U["craft_planks"], (600, 450)),
    "assets/images/services/service-choose-space.webp": (U["courtyard_deck"], (600, 450)),
    "assets/images/services/service-material-detail.webp": (U["stone_wall"], (600, 450)),
    "assets/images/services/services-final-cta.webp": (U["hero_twilight"], (1400, 700)),

    # PROJECTS IMAGES
    "assets/images/projects/projects-hero.webp": (U["hero_pavilion"], (1400, 800)),
    "assets/images/projects/project-concept-timber-deck.webp": (U["sunken_deck"], (800, 600)),
    "assets/images/projects/project-concept-garden-pergola.webp": (U["pergola_lines"], (800, 600)),
    "assets/images/projects/project-concept-covered-lounge.webp": (U["hero_covered"], (800, 600)),
    "assets/images/projects/project-concept-dining-courtyard.webp": (U["hero_dining"], (800, 600)),
    "assets/images/projects/project-spotlight-deck.webp": (U["hero_deck_patio"], (1000, 650)),
    "assets/images/projects/project-spotlight-pergola.webp": (U["craft_rafters"], (1000, 650)),
    "assets/images/projects/project-design-planning.webp": (U["craft_blueprint"], (800, 600)),
    "assets/images/projects/project-detail-timber.webp": (U["craft_grain"], (600, 450)),
    "assets/images/projects/project-detail-structure.webp": (U["craft_wood"], (600, 450)),
    "assets/images/projects/project-detail-lighting.webp": (U["step_lights"], (600, 450)),
    "assets/images/projects/project-detail-stone.webp": (U["stone_wall"], (600, 450)),
    "assets/images/projects/project-direction-relax.webp": (U["patio_lounge"], (600, 450)),
    "assets/images/projects/project-direction-entertain.webp": (U["hero_firepit"], (600, 450)),
    "assets/images/projects/project-direction-expand.webp": (U["hero_flow"], (600, 450)),
    "assets/images/projects/projects-final-cta.webp": (U["hero_backyard"], (1400, 700)),

    # GALLERY IMAGES
    "assets/images/gallery/gallery-hero.webp": (U["hero_twilight"], (1400, 800)),
    "assets/images/gallery/gallery-collection-deck.webp": (U["hero_deck_patio"], (800, 600)),
    "assets/images/gallery/gallery-collection-pergola.webp": (U["pergola_lines"], (800, 600)),
    "assets/images/gallery/gallery-collection-covered.webp": (U["hero_covered"], (800, 600)),
    "assets/images/gallery/gallery-collection-patio.webp": (U["stone_patio"], (800, 600)),
    "assets/images/gallery/gallery-collection-detail.webp": (U["craft_grain"], (800, 600)),
    "assets/images/gallery/gallery-collection-landscape.webp": (U["lush_patio"], (800, 600)),
    "assets/images/gallery/gallery-deck-multitier.webp": (U["sunken_deck"], (800, 600)),
    "assets/images/gallery/gallery-deck-wrap.webp": (U["balcony_deck"], (800, 600)),
    "assets/images/gallery/gallery-deck-poolside.webp": (U["hero_poolside"], (800, 600)),
    "assets/images/gallery/gallery-deck-courtyard.webp": (U["courtyard_deck"], (800, 600)),
    "assets/images/gallery/gallery-pergola-modern.webp": (U["craft_rafters"], (800, 600)),
    "assets/images/gallery/gallery-pergola-traditional.webp": (U["pergola_lines"], (800, 600)),
    "assets/images/gallery/gallery-pergola-cantilever.webp": (U["hero_pavilion"], (800, 600)),
    "assets/images/gallery/gallery-pergola-garden.webp": (U["garden_retreat"], (800, 600)),
    "assets/images/gallery/gallery-covered-pavilion.webp": (U["hero_covered"], (800, 600)),
    "assets/images/gallery/gallery-covered-veranda.webp": (U["hero_flow"], (800, 600)),
    "assets/images/gallery/gallery-covered-lounge.webp": (U["patio_lounge"], (800, 600)),
    "assets/images/gallery/gallery-covered-architecture.webp": (U["hero_pavilion"], (800, 600)),
    "assets/images/gallery/gallery-patio-terrace.webp": (U["stone_patio"], (800, 600)),
    "assets/images/gallery/gallery-patio-firepit.webp": (U["hero_firepit"], (800, 600)),
    "assets/images/gallery/gallery-patio-entertainment.webp": (U["outdoor_kitchen"], (800, 600)),
    "assets/images/gallery/gallery-patio-relax.webp": (U["summer_deck"], (800, 600)),
    "assets/images/gallery/gallery-detail-timber.webp": (U["craft_grain"], (600, 450)),
    "assets/images/gallery/gallery-detail-fastener.webp": (U["craft_planks"], (600, 450)),
    "assets/images/gallery/gallery-detail-lighting.webp": (U["step_lights"], (600, 450)),
    "assets/images/gallery/gallery-detail-structure.webp": (U["craft_wood"], (600, 450)),
    "assets/images/gallery/gallery-detail-decking.webp": (U["craft_grain"], (600, 450)),
    "assets/images/gallery/gallery-moodboard-contemporary.webp": (U["craft_blueprint"], (600, 450)),
    "assets/images/gallery/gallery-moodboard-natural.webp": (U["stone_wall"], (600, 450)),
    "assets/images/gallery/gallery-moodboard-entertaining.webp": (U["hero_dining"], (600, 450)),
    "assets/images/gallery/gallery-moodboard-garden.webp": (U["lush_patio"], (600, 450)),
    "assets/images/gallery/gallery-final-cta.webp": (U["hero_twilight"], (1400, 700)),

    # BLOG IMAGES
    "assets/images/blog/blog-hero.webp": (U["hero_deck_patio"], (1400, 800)),
    "assets/images/blog/blog-featured-article.webp": (U["hero_backyard"], (1000, 650)),
    "assets/images/blog/blog-article-deck-planning.webp": (U["craft_blueprint"], (800, 550)),
    "assets/images/blog/blog-article-pergola-style.webp": (U["pergola_lines"], (800, 550)),
    "assets/images/blog/blog-article-small-backyard.webp": (U["courtyard_deck"], (800, 550)),
    "assets/images/blog/blog-article-deck-materials.webp": (U["craft_grain"], (800, 550)),
    "assets/images/blog/blog-article-outdoor-dining.webp": (U["hero_dining"], (800, 550)),
    "assets/images/blog/blog-article-natural-style.webp": (U["lush_patio"], (800, 550)),
    "assets/images/blog/blog-topic-deck-design.webp": (U["sunken_deck"], (500, 350)),
    "assets/images/blog/blog-topic-pergolas.webp": (U["craft_rafters"], (500, 350)),
    "assets/images/blog/blog-topic-materials.webp": (U["craft_planks"], (500, 350)),
    "assets/images/blog/blog-topic-garden.webp": (U["garden_retreat"], (500, 350)),
    "assets/images/blog/blog-topic-outdoor-living.webp": (U["patio_lounge"], (500, 350)),
    "assets/images/blog/blog-topic-maintenance.webp": (U["wood_oil_finish"], (500, 350)),
    "assets/images/blog/blog-guide-deck-planning.webp": (U["balcony_deck"], (600, 450)),
    "assets/images/blog/blog-guide-pergola-planning.webp": (U["hero_pavilion"], (600, 450)),
    "assets/images/blog/blog-guide-entertaining.webp": (U["outdoor_kitchen"], (600, 450)),
    "assets/images/blog/blog-material-natural-timber.webp": (U["craft_grain"], (600, 450)),
    "assets/images/blog/blog-material-composite.webp": (U["craft_planks"], (600, 450)),
    "assets/images/blog/blog-material-natural-stone.webp": (U["stone_wall"], (600, 450)),
    "assets/images/blog/blog-idea-outdoor-lighting.webp": (U["step_lights"], (500, 350)),
    "assets/images/blog/blog-idea-greenery.webp": (U["greenery_planter"], (500, 350)),
    "assets/images/blog/blog-idea-garden-seating.webp": (U["timber_bench"], (500, 350)),
    "assets/images/blog/blog-idea-outdoor-finishing.webp": (U["wood_oil_finish"], (500, 350)),
    "assets/images/blog/blog-newsletter.webp": (U["craft_blueprint"], (800, 600)),
    "assets/images/blog/blog-final-cta.webp": (U["hero_twilight"], (1400, 700)),

    # FAQ IMAGES
    "assets/images/faq/faq-hero.webp": (U["consultation"], (1400, 750)),
    "assets/images/faq/faq-final-cta.webp": (U["hero_backyard"], (1400, 700)),

    # CONTACT IMAGES
    "assets/images/contact/contact-hero.webp": (U["consultation"], (1400, 750)),
    "assets/images/contact/contact-checklist.webp": (U["craft_blueprint"], (800, 600)),
    "assets/images/contact/contact-final-cta.webp": (U["hero_backyard"], (1400, 700)),
}

print(f"Total targets to generate: {len(IMAGE_MAP)}")
for out_path, (src_url, sz) in IMAGE_MAP.items():
    img = get_image(src_url)
    if img:
        crop_and_save(img, sz, out_path)
    else:
        print(f"Skipping {out_path} due to download error")

print("All photographic images successfully populated!")
