import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter

out_dir = r"assets/images/faq"
os.makedirs(out_dir, exist_ok=True)

# Brand Color Constants
FOREST = (37, 75, 59)
DEEP_FOREST = (24, 56, 44)
SAGE = (130, 151, 123)
WARM_CREAM = (248, 245, 237)
SAND_BEIGE = (233, 223, 201)
TIMBER = (168, 117, 78)
CHARCOAL = (41, 47, 42)
MUTED = (112, 119, 111)
SOFT_BORDER = (228, 225, 216)
GOLD = (212, 163, 89)

def blend(c1, c2, factor):
    factor = max(0.0, min(1.0, factor))
    return (
        int(c1[0] * (1 - factor) + c2[0] * factor),
        int(c1[1] * (1 - factor) + c2[1] * factor),
        int(c1[2] * (1 - factor) + c2[2] * factor)
    )

faq_images = [
    # 1. FAQ Hero: Welcoming outdoor deck with thoughtfully arranged seating & pergola
    {
        "filename": "faq-hero.webp",
        "size": (1600, 1000),
        "theme": "faq_hero",
        "bg": (26, 50, 40),
        "primary": TIMBER,
        "accent": SAND_BEIGE,
        "lighting": "inviting_morning",
        "elements": ["welcoming_deck", "pergola_canopy", "armchairs_and_low_table", "potted_olive_trees", "ambient_soft_sky"]
    },
    # 2. FAQ Support: Consultation desk, design discussion, timber & stone tactile samples
    {
        "filename": "faq-support.webp",
        "size": (800, 600),
        "theme": "faq_support",
        "bg": (32, 48, 40),
        "primary": (175, 125, 80),
        "accent": WARM_CREAM,
        "lighting": "studio_warm",
        "elements": ["consultation_table", "architectural_blueprint_sketch", "timber_swatches", "ceramic_mug", "garden_view"]
    },
    # 3. FAQ Final CTA: Twilight outdoor lounge, lantern glow, serene evening setting
    {
        "filename": "faq-final-cta.webp",
        "size": (1600, 800),
        "theme": "faq_final_cta",
        "bg": (18, 36, 28),
        "primary": (165, 115, 75),
        "accent": GOLD,
        "lighting": "twilight_serenity",
        "elements": ["twilight_terrace", "pergola_rafters", "glowing_step_lights", "outdoor_fireplace_hearth", "deep_night_sky"]
    }
]

def render_image(cfg):
    w, h = cfg["size"]
    im = Image.new("RGB", (w, h), cfg["bg"])
    draw = ImageDraw.Draw(im)

    bg = cfg["bg"]
    primary = cfg["primary"]
    accent = cfg["accent"]
    lighting = cfg["lighting"]
    elems = cfg["elements"]
    theme = cfg["theme"]

    # --- 1. Environmental Gradient ---
    for y in range(h):
        t = y / float(h)
        if "twilight" in lighting:
            horizon = 0.46
            if t < horizon:
                st = t / horizon
                col = blend((15, 24, 36), (48, 65, 56), st)
            else:
                gt = (t - horizon) / (1.0 - horizon)
                col = blend((48, 65, 56), bg, gt)
        elif "inviting" in lighting:
            horizon = 0.44
            if t < horizon:
                st = t / horizon
                col = blend((180, 202, 212), (160, 185, 172), st)
            else:
                col = blend((160, 185, 172), bg, (t - horizon) / (1.0 - horizon))
        else:
            col = blend(blend(bg, (52, 70, 60), 0.45), bg, t)
        draw.line([(0, y), (w, y)], fill=col)

    # --- 2. Background Garden & Foliage Silhouettes ---
    if any(k in elems for k in ["potted_olive_trees", "garden_view", "ambient_soft_sky"]):
        for _ in range(30):
            bx = random.randint(0, w)
            by = random.randint(int(h * 0.2), int(h * 0.52))
            br = random.randint(30, 85)
            leaf_col = blend(FOREST, SAGE, random.uniform(0.15, 0.75))
            draw.ellipse([(bx - br, by - br), (bx + br, by + br)], fill=leaf_col)

    # --- 3. Welcoming Timber Deck Planks ---
    if any(k in elems for k in ["welcoming_deck", "twilight_terrace", "consultation_table"]):
        deck_y = int(h * 0.46)
        num_boards = 38
        for i in range(num_boards):
            prog = (i / float(num_boards)) ** 1.35
            y_board = deck_y + int((h - deck_y) * prog)
            board_h = max(2, int((h - deck_y) / float(num_boards) * (prog * 1.8 + 0.35)))
            t_col = blend(primary, (20, 20, 20), (i % 5) * 0.05)
            draw.rectangle([(0, y_board), (w, y_board + board_h - 2)], fill=t_col)
            draw.line([(0, y_board + board_h - 1), (w, y_board + board_h - 1)], fill=(16, 18, 16), width=1)
            draw.line([(0, y_board), (w, y_board)], fill=blend(t_col, WARM_CREAM, 0.22), width=1)
            for x in range(0, w, 55):
                gx = x + (i * 33) % 45
                draw.line([(gx, y_board + board_h // 2), (min(w, gx + 28), y_board + board_h // 2)],
                          fill=blend(t_col, (235, 195, 155), 0.16), width=1)

    # --- 4. Pergola Posts & Architectural Slats ---
    if any(k in elems for k in ["pergola_canopy", "pergola_rafters"]):
        post_spacing = w // 5
        for p in range(1, 5):
            px = p * post_spacing
            draw.rectangle([(px - 14, 0), (px + 14, int(h * 0.65))], fill=blend(primary, (20, 20, 20), 0.28))
            draw.line([(px - 14, 0), (px - 14, int(h * 0.65))], fill=blend(primary, WARM_CREAM, 0.35), width=2)
        beam_y = int(h * 0.22)
        draw.rectangle([(0, beam_y - 12), (w, beam_y + 12)], fill=blend(primary, (15, 15, 15), 0.22))
        draw.line([(0, beam_y - 12), (w, beam_y - 12)], fill=blend(primary, WARM_CREAM, 0.38), width=2)
        for rx in range(20, w, 45):
            draw.polygon([(rx, beam_y - 30), (rx + 16, beam_y - 40), (rx + 22, beam_y + 8), (rx + 6, beam_y + 18)],
                         fill=blend(primary, WARM_CREAM, 0.2))

    # --- 5. Welcoming Outdoor Seating (Armchairs & Low Table) ---
    if "armchairs_and_low_table" in elems:
        # Low timber coffee table
        tx1, tx2 = int(w * 0.42), int(w * 0.58)
        ty1, ty2 = int(h * 0.68), int(h * 0.82)
        draw.rectangle([(tx1, ty1), (tx2, ty2)], fill=blend(primary, (30, 20, 15), 0.2), outline=WARM_CREAM, width=2)
        # Slat lines on table
        for sx in range(tx1 + 15, tx2 - 10, 25):
            draw.line([(sx, ty1), (sx, ty2)], fill=(25, 20, 18), width=2)
        # Deep armchairs on sides
        # Left chair
        draw.rectangle([(int(w * 0.22), int(h * 0.58)), (int(w * 0.38), int(h * 0.82))], fill=(225, 220, 212), outline=(180, 175, 168), width=2)
        draw.rectangle([(int(w * 0.24), int(h * 0.65)), (int(w * 0.36), int(h * 0.80))], fill=(240, 238, 232))
        # Right chair
        draw.rectangle([(int(w * 0.62), int(h * 0.58)), (int(w * 0.78), int(h * 0.82))], fill=(225, 220, 212), outline=(180, 175, 168), width=2)
        draw.rectangle([(int(w * 0.64), int(h * 0.65)), (int(w * 0.76), int(h * 0.80))], fill=(240, 238, 232))

    # --- 6. Design Consultation Table with Blueprints & Samples ---
    if "architectural_blueprint_sketch" in elems:
        # Table surface in foreground
        draw.rectangle([(int(w * 0.1), int(h * 0.35)), (int(w * 0.9), int(h * 0.92))], fill=blend(WARM_CREAM, (220, 210, 195), 0.3), outline=SOFT_BORDER, width=2)
        # Blueprint document rolled open
        bx1, by1 = int(w * 0.25), int(h * 0.45)
        bx2, by2 = int(w * 0.75), int(h * 0.85)
        draw.rectangle([(bx1, by1), (bx2, by2)], fill=(240, 245, 248), outline=(160, 180, 195), width=2)
        # Blueprint drafting grid lines
        for gx in range(bx1 + 20, bx2 - 10, 30):
            draw.line([(gx, by1 + 10), (gx, by2 - 10)], fill=(210, 225, 235), width=1)
        for gy in range(by1 + 20, by2 - 10, 30):
            draw.line([(bx1 + 10, gy), (bx2 - 10, gy)], fill=(210, 225, 235), width=1)
        # Deck elevation outline
        draw.rectangle([(bx1 + 40, by1 + 50), (bx2 - 40, by2 - 40)], outline=(35, 75, 95), width=2)
        draw.line([(bx1 + 40, by1 + 110), (bx2 - 40, by1 + 110)], fill=TIMBER, width=2)
        # Material swatches on desk
        # Hardwood timber block
        draw.rectangle([(int(w * 0.15), int(h * 0.50)), (int(w * 0.22), int(h * 0.75))], fill=blend(TIMBER, (210, 150, 100), 0.3), outline=(80, 50, 30), width=2)
        # Bluestone paver swatch
        draw.rectangle([(int(w * 0.78), int(h * 0.52)), (int(w * 0.86), int(h * 0.74))], fill=(155, 150, 142), outline=(110, 105, 100), width=2)
        # Ceramic coffee cup
        mug_x, mug_y = int(w * 0.78), int(h * 0.42)
        draw.ellipse([(mug_x - 22, mug_y - 22), (mug_x + 22, mug_y + 22)], fill=(245, 242, 236), outline=(190, 185, 175), width=2)
        draw.ellipse([(mug_x - 16, mug_y - 16), (mug_x + 16, mug_y + 16)], fill=(75, 45, 25))

    # --- 7. Twilight Hearth & Lantern Glow ---
    if any(k in elems for k in ["glowing_step_lights", "outdoor_fireplace_hearth"]):
        glow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(glow_layer)
        lights = [
            (int(w * 0.28), int(h * 0.55), 140),
            (int(w * 0.50), int(h * 0.65), 180),
            (int(w * 0.72), int(h * 0.55), 140)
        ]
        for lx, ly, lr in lights:
            for rad in range(lr, 10, -10):
                alpha = int(35 * (1.0 - rad / float(lr)))
                g_draw.ellipse([(lx - rad, ly - rad), (lx + rad, ly + rad)], fill=(255, 215, 140, alpha))
            g_draw.ellipse([(lx - 6, ly - 6), (lx + 6, ly + 6)], fill=(255, 250, 220, 240))
        im = Image.alpha_composite(im.convert("RGBA"), glow_layer).convert("RGB")

    im = im.filter(ImageFilter.SMOOTH_MORE)
    out_path = os.path.join(out_dir, cfg["filename"])
    im.save(out_path, "WEBP", quality=90, method=6)
    print(f"Generated {out_path} ({w}x{h})")

def main():
    print(f"Generating {len(faq_images)} unique FAQ images...")
    for cfg in faq_images:
        render_image(cfg)
    print("Successfully generated all FAQ images in assets/images/faq!")

if __name__ == "__main__":
    main()
