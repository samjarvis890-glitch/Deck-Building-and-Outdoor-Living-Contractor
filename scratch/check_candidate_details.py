import os
from PIL import Image

def get_info(path):
    try:
        with Image.open(path) as img:
            return f"{img.size}, {img.format}"
    except Exception as e:
        return str(e)

# Candidate stock images in scratch:
scratch_candidates = [
    'scratch/test_alfresco_patio_stone.jpg',
    'scratch/test_architect_drawing_deck.jpg',
    'scratch/test_backyard_lawn_pergola.jpg',
    'scratch/test_cedar_wood_grain.jpg',
    'scratch/test_contemporary_patio.jpg',
    'scratch/test_deck_construction_wood.jpg',
    'scratch/test_deck_pool_twilight.jpg',
    'scratch/test_featured_deck_concept.webp',
    'scratch/test_garden_deck_pergola.jpg',
    'scratch/test_garden_walkway_deck.jpg',
    'scratch/test_luxury_timber_house.jpg',
    'scratch/test_modern_house_deck.jpg',
    'scratch/test_modern_villa_patio.jpg',
    'scratch/test_outdoor_bistro_lights.jpg',
    'scratch/test_outdoor_sofa_patio.jpg',
    'scratch/test_outdoor_terrace_view.jpg',
    'scratch/test_stair_lights.webp',
    'scratch/test_stone_paver_terrace.jpg',
    'scratch/test_terrace_dining_stone.jpg',
    'scratch/test_timber_planks_texture.jpg',
    'scratch/test_timber_wood_decking.jpg',
    'scratch/candidates/candidate_courtyard.jpg',
    'scratch/candidates/candidate_covered_room.jpg',
    'scratch/candidates/candidate_deck_sanctuary.jpg',
    'scratch/candidates/candidate_dining_pergola.jpg',
    'scratch/candidates/candidate_firepit_deck.jpg',
    'scratch/candidates/candidate_garden_deck.jpg',
    'scratch/candidates/candidate_grain_texture.jpg',
    'scratch/candidates/candidate_lush_patio.jpg',
    'scratch/candidates/candidate_modern_patio.jpg',
    'scratch/candidates/candidate_oiled_cedar.jpg',
    'scratch/candidates/candidate_patio_lounge.jpg',
    'scratch/candidates/candidate_stone_timber.jpg',
    'scratch/candidates/candidate_stone_wall.jpg',
    'scratch/candidates/candidate_sunken_deck.jpg',
    'scratch/candidates/candidate_wood_planks.jpg'
]

print(f"Total scratch candidates: {len(scratch_candidates)}")
for c in scratch_candidates:
    print(f"  {c}: {get_info(c)}")
