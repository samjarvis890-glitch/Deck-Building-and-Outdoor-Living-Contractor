from PIL import Image, ImageDraw
import os

cand_dir = 'scratch/candidates'
files = sorted([f for f in os.listdir(cand_dir) if f.endswith(('.jpg', '.jpeg', '.webp', '.png'))])

cols = 4
rows = (len(files) + cols - 1) // cols
cell_w, cell_h = 320, 220
pad = 10
label_h = 35

grid = Image.new('RGB', (cols * (cell_w + pad) + pad, rows * (cell_h + label_h + pad) + pad), (240, 240, 240))
draw = ImageDraw.Draw(grid)

for idx, f in enumerate(files):
    c = idx % cols
    r = idx // cols
    x = pad + c * (cell_w + pad)
    y = pad + r * (cell_h + label_h + pad)
    
    p = os.path.join(cand_dir, f)
    try:
        im = Image.open(p).convert('RGB')
        im.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)
        px = x + (cell_w - im.size[0]) // 2
        py = y + (cell_h - im.size[1]) // 2
        grid.paste(im, (px, py))
        draw.text((x + 5, y + cell_h + 5), f"{f} ({im.size[0]}x{im.size[1]})", fill=(10, 10, 10))
    except Exception as e:
        draw.text((x + 5, y + cell_h + 5), f"Err: {e}", fill=(200, 20, 20))

grid.save('scratch/candidates_all_preview.png')
print("Saved scratch/candidates_all_preview.png")
