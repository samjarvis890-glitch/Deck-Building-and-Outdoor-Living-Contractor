from PIL import Image, ImageDraw
import os

contact_dir = 'assets/images/contact'
files = sorted([f for f in os.listdir(contact_dir) if f.endswith('.webp')])

cols = 5
rows = 1
cell_w, cell_h = 300, 200
pad = 10
label_h = 45

grid_w = cols * (cell_w + pad) + pad
grid_h = rows * (cell_h + label_h + pad) + pad

grid = Image.new('RGB', (grid_w, grid_h), (240, 240, 240))
draw = ImageDraw.Draw(grid)

for idx, f in enumerate(files):
    x = pad + idx * (cell_w + pad)
    y = pad
    
    path = os.path.join(contact_dir, f)
    try:
        im = Image.open(path).convert('RGB')
        im.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)
        px = x + (cell_w - im.size[0]) // 2
        py = y + (cell_h - im.size[1]) // 2
        grid.paste(im, (px, py))
        draw.text((x + 5, y + cell_h + 5), f"{f}\n({im.size[0]}x{im.size[1]})", fill=(10, 10, 10))
    except Exception as e:
        draw.rectangle([x, y, x + cell_w, y + cell_h], fill=(200, 50, 50))
        draw.text((x + 5, y + cell_h + 5), f"Error: {e}", fill=(200, 20, 20))

grid.save('scratch/audit_contact_imgs.png')
print("Saved scratch/audit_contact_imgs.png")
