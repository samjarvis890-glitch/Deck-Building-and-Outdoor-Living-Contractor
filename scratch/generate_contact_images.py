import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter

out_dir = r"assets/images/contact"
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

contact_images = [
    # 1. Contact Hero: Welcoming outdoor dining / lounge terrace with pergola & lush landscaping
    {
        "filename": "contact-hero.webp",
        "size": (1600, 1000),
        "theme": "contact_hero",
        "bg": (28, 52, 42),
        "primary": TIMBER,
        "accent": SAND_BEIGE,
        "lighting": "golden_afternoon",
        "elements": ["welcoming_patio_deck", "pergola_canopy", "outdoor_dining_table", "lush_garden_border", "warm_ambient_sun"]
    },
    # 2. Form Side: Vertical architectural timber battens & sunlit foliage
    {
        "filename": "contact-form-side.webp",
        "size": (800, 1000),
        "theme": "form_side",
        "bg": (22, 46, 36),
        "primary": (175, 122, 78),
        "accent": WARM_CREAM,
        "lighting": "filtered_sunlight",
        "elements": ["vertical_cedar_battens", "shadow_patterns", "lush_fern_foliage", "architectural_joinery"]
    },
    # 3. Checklist: Project planning flat lay, drafting blueprints, timber blocks, measuring tape
    {
        "filename": "contact-checklist.webp",
        "size": (800, 600),
        "theme": "checklist_scene",
        "bg": (36, 48, 42),
        "primary": (180, 128, 82),
        "accent": GOLD,
        "lighting": "studio_drafting",
        "elements": ["architectural_blueprint_roll", "tape_measure", "hardwood_swatches", "pencil_sketch", "garden_backdrop"]
    },
    # 4. Map Support: Architectural location aesthetic, stone pavers, site boundary lines
    {
        "filename": "contact-map-support.webp",
        "size": (800, 600),
        "theme": "map_support",
        "bg": (34, 46, 40),
        "primary": (155, 150, 142),
        "accent": TIMBER,
        "lighting": "topographic_clean",
        "elements": ["bluestone_terrace", "perimeter_stone_wall", "contour_lines", "architectural_landscape"]
    },
    # 5. Final CTA: Twilight outdoor pavilion, illuminated steps, starry night reflections
    {
        "filename": "contact-final-cta.webp",
        "size": (1600, 800),
        "theme": "final_cta",
        "bg": (16, 34, 26),
        "primary": (165, 115, 75),
        "accent": GOLD,
        "lighting": "night_pavilion",
        "elements": ["wide_evening_pavilion", "step_riser_glow", "water_mirror_reflection", "starry_sky", "pergola_slats"]
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

    # 1. Base Environmental Sky / Studio Gradient
    for y in range(h):
        t = y / float(h)
        if "night" in lighting:
            horizon = 0.46
            if t < horizon:
                st = t / horizon
                col = blend((12, 20, 32), (40, 58, 50), st)
            else:
                gt = (t - horizon) / (1.0 - horizon)
                col = blend((40, 58, 50), bg, gt)
        elif "golden" in lighting:
            horizon = 0.42
            if t < horizon:
                st = t / horizon
                col = blend((65, 90, 78), (195, 155, 115), st)
            else:
                col = blend((195, 155, 115), bg, (t - horizon) / (1.0 - horizon))
        elif "filtered" in lighting:
            col = blend(blend(bg, (50, 72, 60), 0.5), bg, t)
        else:
            col = blend(blend(bg, (48, 65, 55), 0.45), bg, t)
        draw.line([(0, y), (w, y)], fill=col)

    # 2. Lush Foliage / Background Planting
    if any(k in elems for k in ["lush_garden_border", "lush_fern_foliage", "garden_backdrop", "architectural_landscape"]):
        for _ in range(35):
            bx = random.randint(0, w)
            by = random.randint(int(h * 0.15), int(h * 0.55))
            br = random.randint(25, 95)
            leaf_col = blend(FOREST, SAGE, random.uniform(0.15, 0.75))
            draw.ellipse([(bx - br, by - br), (bx + br, by + br)], fill=leaf_col)

    # 3. Vertical Cedar Battens / Architectural Joinery (Form Side)
    if "vertical_cedar_battens" in elems:
        num_battens = 28
        b_width = w // num_battens
        for b in range(num_battens):
            bx1 = b * b_width
            bx2 = bx1 + b_width - 8
            b_col = blend(primary, (25, 20, 16), (b % 4) * 0.08)
            draw.rectangle([(bx1, 0), (bx2, h)], fill=b_col)
            draw.line([(bx1, 0), (bx1, h)], fill=blend(b_col, WARM_CREAM, 0.28), width=2)
            draw.line([(bx2, 0), (bx2, h)], fill=(15, 15, 15), width=2)
            # Wood grain stripes
            for gy in range(0, h, 60):
                draw.line([(bx1 + 2, gy + (b * 17) % 50), (bx2 - 2, gy + (b * 17) % 50)],
                          fill=blend(b_col, (240, 200, 160), 0.15), width=1)
        # Overlay climbing jasmine leaves
        for _ in range(25):
            fx = random.randint(0, int(w * 0.55))
            fy = random.randint(int(h * 0.4), h)
            draw.ellipse([(fx - 18, fy - 12), (fx + 18, fy + 12)], fill=blend(SAGE, (45, 90, 55), 0.5))

    # 4. Welcoming Timber Deck Planks (Perspective Decking)
    if any(k in elems for k in ["welcoming_patio_deck", "wide_evening_pavilion"]):
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

    # 5. Pergola Rafters & Beams
    if any(k in elems for k in ["pergola_canopy", "pergola_slats"]):
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

    # 6. Outdoor Dining Table (Contact Hero)
    if "outdoor_dining_table" in elems:
        tx1, tx2 = int(w * 0.32), int(w * 0.68)
        ty1, ty2 = int(h * 0.62), int(h * 0.88)
        draw.rectangle([(tx1, ty1), (tx2, ty2)], fill=blend(primary, (35, 25, 20), 0.2), outline=WARM_CREAM, width=2)
        for sl_x in range(tx1 + 25, tx2 - 10, 35):
            draw.line([(sl_x, ty1), (sl_x, ty2)], fill=(25, 20, 18), width=2)
        # Place settings
        for px in [int(w * 0.42), int(w * 0.58)]:
            draw.ellipse([(px - 28, ty1 + 40), (px + 28, ty1 + 85)], fill=(240, 238, 230), outline=(190, 185, 175), width=2)
            draw.ellipse([(px - 16, ty1 + 48), (px + 16, ty1 + 75)], fill=(248, 245, 240))

    # 7. Project Drafting Blueprint & Swatches (Checklist)
    if "architectural_blueprint_roll" in elems:
        draw.rectangle([(int(w * 0.1), int(h * 0.35)), (int(w * 0.9), int(h * 0.92))], fill=blend(WARM_CREAM, (225, 215, 200), 0.3), outline=SOFT_BORDER, width=2)
        bx1, by1 = int(w * 0.2), int(h * 0.42)
        bx2, by2 = int(w * 0.8), int(h * 0.85)
        draw.rectangle([(bx1, by1), (bx2, by2)], fill=(240, 245, 248), outline=(155, 175, 190), width=2)
        for gx in range(bx1 + 20, bx2 - 10, 30):
            draw.line([(gx, by1 + 10), (gx, by2 - 10)], fill=(215, 230, 238), width=1)
        for gy in range(by1 + 20, by2 - 10, 30):
            draw.line([(bx1 + 10, gy), (bx2 - 10, gy)], fill=(215, 230, 238), width=1)
        # Floor plan / deck perimeter outline
        draw.rectangle([(bx1 + 45, by1 + 45), (bx2 - 45, by2 - 45)], outline=(35, 75, 95), width=2)
        draw.line([(bx1 + 45, by1 + 100), (bx2 - 45, by1 + 100)], fill=TIMBER, width=2)
        # Hardwood timber blocks
        draw.rectangle([(int(w * 0.14), int(h * 0.48)), (int(w * 0.22), int(h * 0.74))], fill=blend(TIMBER, (220, 160, 110), 0.3), outline=(90, 60, 40), width=2)
        # Steel tape measure
        draw.rectangle([(int(w * 0.78), int(h * 0.52)), (int(w * 0.86), int(h * 0.72))], fill=GOLD, outline=(140, 105, 50), width=2)

    # 8. Bluestone Pavers & Contour Site Layout (Map Support)
    if "bluestone_terrace" in elems:
        paver_y = int(h * 0.38)
        p_rows, p_cols = 12, 16
        for r in range(p_rows):
            prog = (r / float(p_rows)) ** 1.35
            y1 = paver_y + int((h - paver_y) * prog)
            y2 = paver_y + int((h - paver_y) * ((r + 1) / float(p_rows)) ** 1.35)
            for c in range(p_cols):
                offset = (r % 2) * (w // (p_cols * 2))
                x1 = c * (w // p_cols) + offset - (w // (p_cols * 2))
                x2 = x1 + (w // p_cols) - 4
                stone_shade = blend(primary, (95, 100, 95), (c * 7 + r * 11) % 5 * 0.08)
                draw.rectangle([(x1, y1), (x2, y2 - 3)], fill=stone_shade)
                draw.line([(x1, y1), (x2, y1)], fill=blend(stone_shade, (245, 245, 245), 0.28), width=1)
        # Topographic site contour arcs
        for rad in [140, 220, 320, 420]:
            draw.arc([(int(w * 0.6) - rad, int(h * 0.3) - rad // 2), (int(w * 0.6) + rad, int(h * 0.3) + rad // 2)], start=160, end=340, fill=blend(SAGE, WARM_CREAM, 0.4), width=1)

    # 9. Step Riser & Twilight Warm Glow
    if "step_riser_glow" in elems:
        glow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(glow_layer)
        lights = [
            (int(w * 0.25), int(h * 0.55), 140),
            (int(w * 0.50), int(h * 0.65), 180),
            (int(w * 0.75), int(h * 0.55), 140)
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
    print(f"Generating {len(contact_images)} unique contact images...")
    for cfg in contact_images:
        render_image(cfg)
    print("Successfully generated all contact images in assets/images/contact!")

if __name__ == "__main__":
    main()
