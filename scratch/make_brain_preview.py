from PIL import Image, ImageDraw
import os

brain_dir = r"C:\Users\Sam John\.gemini\antigravity\brain\aa3393d8-6479-4912-9a44-277395bd13ea"
imgs = ['hero_deck_outdoor_living_1793850319432.jpg', 'indoor_outdoor_flow_deck_1793850483924.jpg', 'serene_deck_garden_retreat_1793850797959.jpg']

cell_w, cell_h = 450, 250
pad = 10
grid = Image.new('RGB', (3 * (cell_w + pad) + pad, cell_h + 50 + pad), (240, 240, 240))
draw = ImageDraw.Draw(grid)

for idx, f in enumerate(imgs):
    p = os.path.join(brain_dir, f)
    im = Image.open(p).convert('RGB')
    im.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)
    x = pad + idx * (cell_w + pad)
    y = pad
    grid.paste(im, (x, y))
    draw.text((x + 5, y + cell_h + 5), f, fill=(0, 0, 0))

grid.save('scratch/brain_imgs_preview.png')
print("Saved scratch/brain_imgs_preview.png")
