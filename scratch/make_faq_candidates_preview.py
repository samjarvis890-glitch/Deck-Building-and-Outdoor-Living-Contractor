from PIL import Image, ImageDraw
import os

candidates = [
    ('test_architect_drawing_deck.jpg', 'Architect Blueprint/Consultation'),
    ('test_garden_deck_pergola.jpg', 'Garden Deck with Pergola'),
    ('test_modern_house_deck.jpg', 'Modern House & Deck'),
    ('test_modern_villa_patio.jpg', 'Modern Villa Patio'),
    ('test_outdoor_terrace_view.jpg', 'Outdoor Terrace View'),
    ('test_deck_pool_twilight.jpg', 'Twilight Pool & Deck'),
    ('test_alfresco_patio_stone.jpg', 'Alfresco Patio Stone'),
    ('test_luxury_timber_house.jpg', 'Luxury Timber House'),
    ('test_outdoor_bistro_lights.jpg', 'Twilight Bistro Lights Deck')
]

cols = 3
rows = 3
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
    else:
        draw.text((x + 5, y + cell_h + 5), f"Missing: {f}", fill=(200, 20, 20))

grid.save('scratch/faq_candidates_preview.png')
print("Saved scratch/faq_candidates_preview.png")
