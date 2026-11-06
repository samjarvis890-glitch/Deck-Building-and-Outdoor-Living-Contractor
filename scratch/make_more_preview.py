from PIL import Image, ImageDraw
import os

files = [
    'test_garden_deck_pergola.jpg',
    'test_garden_walkway_deck.jpg',
    'test_luxury_timber_house.jpg',
    'test_modern_house_deck.jpg',
    'test_outdoor_sofa_patio.jpg',
    'test_stone_paver_terrace.jpg',
    'test_terrace_dining_stone.jpg',
    'test_timber_wood_decking.jpg',
    'test_contemporary_patio.jpg',
    'test_outdoor_bistro_lights.jpg'
]

cols = 5
rows = 2
cell_w, cell_h = 280, 180
pad = 10
label_h = 35

grid = Image.new('RGB', (cols * (cell_w + pad) + pad, rows * (cell_h + label_h + pad) + pad), (240, 240, 240))
draw = ImageDraw.Draw(grid)

for idx, f in enumerate(files):
    c = idx % cols
    r = idx // cols
    x = pad + c * (cell_w + pad)
    y = pad + r * (cell_h + label_h + pad)
    
    p = os.path.join('scratch', f)
    if os.path.exists(p):
        im = Image.open(p).convert('RGB')
        im.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)
        px = x + (cell_w - im.size[0]) // 2
        py = y + (cell_h - im.size[1]) // 2
        grid.paste(im, (px, py))
        draw.text((x + 5, y + cell_h + 5), f"{f}", fill=(10, 10, 10))

grid.save('scratch/more_candidates_preview.png')
print("Saved scratch/more_candidates_preview.png")
