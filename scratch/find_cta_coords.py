from PIL import Image
import numpy as np

im = Image.open('scratch/gallery_tall_v2_light.png')
print("Image size:", im.size)
arr = np.array(im)

# Let's search from the bottom upwards for the CTA section
# The CTA has a dark forest green background (#12281F -> rgb ~18, 40, 31)
# and footer is dark green (#112019 -> rgb ~17, 32, 25)
# Let's inspect rows every 100px from y=5000 to 7500
for y in range(5000, 7500, 100):
    print(f"y={y}: rgb={arr[y, 720][:3]}")
