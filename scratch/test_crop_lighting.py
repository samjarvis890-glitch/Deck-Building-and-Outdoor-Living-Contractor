from PIL import Image

im = Image.open('assets/images/index/home-deck.webp')
w, h = im.size
print("home-deck size:", w, h)

# Stair riser lights are in the lower-left-to-center stairs
# Let's crop stairs: (w*0.25, h*0.55, w*0.85, h*0.95)
crop_box = (int(w * 0.25), int(h * 0.55), int(w * 0.85), int(h * 0.95))
cropped = im.crop(crop_box)
cropped = cropped.resize((600, 450), Image.Resampling.LANCZOS)
cropped.save('scratch/test_stair_lights.webp', 'WEBP', quality=90)
print("Saved scratch/test_stair_lights.webp")
