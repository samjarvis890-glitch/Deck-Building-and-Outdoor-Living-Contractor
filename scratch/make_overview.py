from PIL import Image

im = Image.open('scratch/gallery_tall_12000.png')
w, h = im.size
print("Size:", w, h)

# Resize to width 360 to see overview
overview = im.resize((360, int(h * 360 / w)), Image.Resampling.LANCZOS)
overview.save('scratch/gallery_overview.png')
print("Saved scratch/gallery_overview.png of size", overview.size)
