import os
import urllib.request
from io import BytesIO
from PIL import Image

# Curated Unsplash photo IDs for Deck Building, Pergolas, Outdoor Living & Craftsmanship
PHOTO_COLLECTION = {
    # Large Heroes & Architecture
    "luxury_deck_twilight": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1600&q=80",
    "modern_patio_pool": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=80",
    "timber_pergola_deck": "https://images.unsplash.com/photo-1591825729269-caeb344f6df2?w=1600&q=80",
    "covered_outdoor_room": "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?w=1600&q=80",
    "backyard_sanctuary": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1600&q=80",
    "alfresco_dining_pergola": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=1600&q=80",
    "contemporary_pavilion": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=1600&q=80",
    "garden_deck_morning": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=1600&q=80",
    "outdoor_firepit_lounge": "https://images.unsplash.com/photo-1527030280862-64139fba04ca?w=1600&q=80",
    "indoor_outdoor_flow": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1600&q=80",
    
    # Craftsmanship, Carpentry & Wood
    "woodworking_tools": "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=1200&q=80",
    "carpenter_planing": "https://images.unsplash.com/photo-1581783342308-f792dbdd27c5?w=1200&q=80",
    "timber_grain_planks": "https://images.unsplash.com/photo-1533090161767-e6ffed986c88?w=1200&q=80",
    "architectural_sketches": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1200&q=80",
    "wood_texture_macro": "https://images.unsplash.com/photo-1546484396-fb3fc6f95f98?w=1200&q=80",
    "timber_rafters_sky": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=1200&q=80",
    
    # Specific Decks & Settings
    "sunken_seating_deck": "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?w=1200&q=80",
    "courtyard_deck": "https://images.unsplash.com/photo-1558036117-15d82a90b9b1?w=1200&q=80",
    "stone_timber_terrace": "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?w=1200&q=80",
    "stair_riser_lights": "https://images.unsplash.com/photo-1507089947368-19c1da9775ae?w=1200&q=80",
    "peaceful_garden_retreat": "https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=1200&q=80",
    "modern_pergola_lines": "https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=1200&q=80",
    "patio_lounge_daylight": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80",
    "lush_green_patio": "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=1200&q=80",
    "natural_stone_wall": "https://images.unsplash.com/photo-1598928506311-c55ded91a20c?w=1200&q=80",
    "balcony_timber_deck": "https://images.unsplash.com/photo-1540518614846-7ede433c4550?w=1200&q=80",
    "summer_alfresco_deck": "https://images.unsplash.com/photo-1560185007-cde436f6a4d0?w=1200&q=80",
    "outdoor_kitchen_deck": "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?w=1200&q=80",
    "minimalist_timber_bench": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=1200&q=80",
    "lifestyle_friends_relax": "https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=1200&q=80",
    "consultation_table": "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=1200&q=80"
}

print(f"Total curated photo sources: {len(PHOTO_COLLECTION)}")
