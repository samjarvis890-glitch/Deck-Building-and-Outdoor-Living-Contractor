from PIL import Image, ImageDraw, ImageFont
import os

proj_dir = 'assets/images/projects'
files = sorted([f for f in os.listdir(proj_dir) if f.endswith('.webp')])

cols = 4
rows = (len(files) + cols - 1) // cols
cell_w, cell_h = 360, 270
pad = 10
label_h = 40

grid_w = cols * (cell_w + pad) + pad
grid_h = rows * (cell_h + label_h + pad) + pad

grid = Image.new('RGB', (grid_w, grid_h), (245, 245, 245))
draw = ImageDraw.Draw(grid)

for idx, f in enumerate(files):
    r = idx // cols
    c = idx % cols
    x = pad + c * (cell_w + pad)
    y = pad + r * (cell_h + label_h + pad)
    
    path = os.path.join(proj_dir, f)
    try:
        im = Image.open(path).convert('RGB')
        im.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)
        # paste centered
        px = x + (cell_w - im.size[0]) // 2
        py = y + (cell_h - im.size[1]) // 2
        grid.paste(im, (px, py))
    except Exception as e:
        draw.rectangle([x, y, x + cell_w, y + cell_h], fill=(200, 50, 50))
    
    draw.text((x + 5, y + cell_h + 5), f"{f}\n({im.size[0]}x{im.size[1]})", fill=(20, 20, 20))

grid.save('scratch/audit_projects_imgs.png')
print("Saved scratch/audit_projects_imgs.png")
