import os
import re

with open('scratch/populate_real_images.py') as f:
    code = f.read()

matches = re.findall(r'"([a-z_]+)":\s*"(https://images\.unsplash\.com/[^"]+)"', code)
for k, v in matches:
    print(f"{k}: {v}")
