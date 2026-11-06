from PIL import Image, ImageDraw
import os

candidates = [
    ('test_modern_villa_patio.jpg', 'Modern Villa Evening Deck Patio'),
    ('test_deck_pool_twilight.jpg', 'Twilight Deck & Pool'),
    ('test_outdoor_terrace_view.jpg', 'Architectural Terrace Overview'),
    ('test_backyard_lawn_pergola.jpg', 'Backyard Lawn & Pergola (Vertical)'),
    ('test_deck_construction_wood.jpg', 'Deck Construction & Timber Framing')
]

cols = 3
rows = 2
cell_w, cell_h = 400, 260
pad = 10
label_h = 40

grid_w = cols * (cell_w + pad) + pad
grid_h = rows * (cell_h + label_h + pad) + pad

grid = Image.new('RGB', (grid_w, grid_h), (245, 245, 245))
draw = ImageDraw.Draw(grid)

for idx, (f, desc) in enumerate(candidates):
    c = idx % cols
    r = idx // cols
    x = pad + c * (cell_w + pad)
    y = pad + r * (cell_h + label_h + pad)
    
    p = os.path.join('scratch', f)
    if os.path.exists(p):
        try:
            im = Image.open(p).convert('RGB')
            im.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)
            px = x + (cell_w - im.size[0]) // 2
            py = y + (cell_h - im.size[1]) // 2
            grid.paste(im, (px, py))
            draw.text((x + 5, y + cell_h + 5), f"{f}\n{desc} ({im.size[0]}x{im.size[1]})", fill=(20, 20, 20))
        except Exception as e:
            draw.text((x + 5, y + cell_h + 5), f"Error: {e}", fill=(200, 20, 20))

grid.save('scratch/contact_candidates_sheet.png')
print("Saved scratch/contact_candidates_sheet.png")
