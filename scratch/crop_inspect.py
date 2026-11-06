from PIL import Image
import os

p = os.path.abspath('scratch/gallery_tall_12000.png')
im = Image.open(p)

# Crop CTA & Footer around y=9500 to 11800
cta = im.crop((0, 9500, 1440, 11800))
cta.save('scratch/gallery_cta_inspect.png')

# Also crop hero (y=0 to 1200)
hero = im.crop((0, 0, 1440, 1100))
hero.save('scratch/gallery_hero_inspect.png')

# Also crop moodboard (y=8000 to 9800)
moodboard = im.crop((0, 8000, 1440, 9800))
moodboard.save('scratch/gallery_moodboard_inspect.png')

print("Cropped successfully!")
