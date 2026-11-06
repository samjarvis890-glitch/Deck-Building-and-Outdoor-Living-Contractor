import os, hashlib
from PIL import Image

def get_hash(p):
    with open(p, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

existing_hashes = {}
for root, dirs, files in os.walk('assets/images'):
    for f in files:
        if f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png')):
            p = os.path.join(root, f).replace('\\', '/')
            existing_hashes[get_hash(p)] = p

print(f"Existing files in assets/images: {len(existing_hashes)}")

# Check candidate images
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

unused = []
for c in scratch_candidates:
    h = get_hash(c)
    if h in existing_hashes:
        print(f"Candidate {c} already used in {existing_hashes[h]}")
    else:
        unused.append(c)

print(f"\nUnused candidates ready to assign: {len(unused)}")
for u in unused:
    print(" ", u)
