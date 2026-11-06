from PIL import Image, ImageDraw
import os

faq_dir = 'assets/images/faq'
files = sorted([f for f in os.listdir(faq_dir) if f.endswith('.webp')])

cols = 3
rows = 1
cell_w, cell_h = 400, 260
pad = 10
label_h = 40

grid_w = cols * (cell_w + pad) + pad
grid_h = (cell_h + label_h + pad) + pad

grid = Image.new('RGB', (grid_w, grid_h), (240, 240, 240))
draw = ImageDraw.Draw(grid)

for idx, f in enumerate(files):
    x = pad + idx * (cell_w + pad)
    y = pad
    
    path = os.path.join(faq_dir, f)
    try:
        im = Image.open(path).convert('RGB')
        im.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)
        px = x + (cell_w - im.size[0]) // 2
        py = y + (cell_h - im.size[1]) // 2
        grid.paste(im, (px, py))
    except Exception as e:
        draw.rectangle([x, y, x + cell_w, y + cell_h], fill=(200, 50, 50))
    
    draw.text((x + 5, y + cell_h + 5), f"{f}\n({im.size[0]}x{im.size[1]})", fill=(10, 10, 10))

grid.save('scratch/audit_faq_imgs.png')
print("Saved scratch/audit_faq_imgs.png")
