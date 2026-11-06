from PIL import Image, ImageDraw
import os
import glob

files = sorted(glob.glob('scratch/test_*.jpg'))
print(f"Total test files: {len(files)}")

cols = 4
rows = (len(files) + cols - 1) // cols
cell_w, cell_h = 360, 240
pad = 10
label_h = 40

grid_w = cols * (cell_w + pad) + pad
grid_h = rows * (cell_h + label_h + pad) + pad

grid = Image.new('RGB', (grid_w, grid_h), (240, 240, 240))
draw = ImageDraw.Draw(grid)

for idx, f in enumerate(files):
    r = idx // cols
    c = idx % cols
    x = pad + c * (cell_w + pad)
    y = pad + r * (cell_h + label_h + pad)
    
    label = os.path.basename(f).replace('test_', '').replace('.jpg', '')
    try:
        im = Image.open(f).convert('RGB')
        im.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)
        px = x + (cell_w - im.size[0]) // 2
        py = y + (cell_h - im.size[1]) // 2
        grid.paste(im, (px, py))
    except Exception as e:
        draw.rectangle([x, y, x + cell_w, y + cell_h], fill=(200, 50, 50))
    
    draw.text((x + 5, y + cell_h + 5), f"{label}\n({im.size[0]}x{im.size[1]})", fill=(10, 10, 10))

grid.save('scratch/contact_candidates.png')
print("Saved scratch/contact_candidates.png")
