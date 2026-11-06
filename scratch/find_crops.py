from PIL import Image

im_l = Image.open('scratch/faq_tall_light.png')
im_d = Image.open('scratch/faq_tall_dark.png')

# Let's crop a vertical strip around 3200-5500 to find the sections
# Let's crop 500px tall slices
for y in range(3000, 5000, 400):
    im_l.crop((0, y, 1440, min(im_l.size[1], y + 600))).save(f'scratch/faq_slice_{y}.png')
    print(f"Saved slice {y}")
