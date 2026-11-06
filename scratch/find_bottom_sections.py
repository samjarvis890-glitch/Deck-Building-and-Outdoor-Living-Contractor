from PIL import Image

im = Image.open('scratch/faq_tall_light.png')
print("Total image height:", im.size[1])

# Let's crop from 4500 to bottom in 500px steps
for y in range(4500, im.size[1] - 400, 400):
    im.crop((0, y, 1440, min(im.size[1], y + 600))).save(f'scratch/faq_bottom_{y}.png')
    print(f"Saved bottom {y}")
