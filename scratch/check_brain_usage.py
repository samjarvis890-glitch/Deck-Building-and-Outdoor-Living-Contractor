import os

for f in ['hero_deck_outdoor_living_1793850319432.jpg', 'indoor_outdoor_flow_deck_1793850483924.jpg', 'serene_deck_garden_retreat_1793850797959.jpg']:
    found = []
    for root, dirs, files in os.walk('assets'):
        for file in files:
            # check if file size or content matches
            pass
    print(f)
