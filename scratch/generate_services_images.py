import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter

out_dir = r"assets/images/services"
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

services_images = [
    {
        "filename": "services-hero.webp",
        "size": (1600, 900),
        "theme": "hero",
        "bg": (22, 45, 36),
        "primary": TIMBER,
        "accent": SAND_BEIGE,
        "lighting": "golden_hour",
        "elements": ["pergola", "deck_planks", "lounge", "foliage", "recessed_glow"]
    },
    {
        "filename": "service-overview-deck.webp",
        "size": (800, 600),
        "theme": "deck",
        "bg": (30, 58, 46),
        "primary": (175, 122, 82),
        "accent": SAND_BEIGE,
        "lighting": "daylight",
        "elements": ["deck_planks", "stairs", "planters", "foliage"]
    },
    {
        "filename": "service-overview-pergola.webp",
        "size": (800, 600),
        "theme": "pergola",
        "bg": (45, 60, 50),
        "primary": (150, 105, 70),
        "accent": WARM_CREAM,
        "lighting": "filtered_sun",
        "elements": ["pergola", "shadow_slats", "paved_floor"]
    },
    {
        "filename": "service-overview-covered.webp",
        "size": (800, 600),
        "theme": "covered",
        "bg": (24, 48, 38),
        "primary": TIMBER,
        "accent": GOLD,
        "lighting": "evening_ambient",
        "elements": ["solid_roof", "ceiling_timber", "pendant_light", "deck_planks"]
    },
    {
        "filename": "service-overview-patio.webp",
        "size": (800, 600),
        "theme": "patio",
        "bg": (38, 45, 40),
        "primary": (160, 155, 145),
        "accent": TIMBER,
        "lighting": "afternoon",
        "elements": ["stone_pavers", "fire_bowl", "foliage", "deck_border"]
    },
    {
        "filename": "service-overview-renovation.webp",
        "size": (800, 600),
        "theme": "renovation_card",
        "bg": (35, 52, 42),
        "primary": TIMBER,
        "accent": (140, 120, 100),
        "lighting": "clear_sky",
        "elements": ["split_finish_deck", "measure_lines", "precision_border"]
    },
    {
        "filename": "service-deck-construction.webp",
        "size": (1400, 900),
        "theme": "deck_hero",
        "bg": (25, 50, 40),
        "primary": (180, 125, 85),
        "accent": SAND_BEIGE,
        "lighting": "bright_morning",
        "elements": ["wide_deck_planks", "glass_railing", "lush_trees", "recessed_glow"]
    },
    {
        "filename": "service-deck-detail.webp",
        "size": (700, 500),
        "theme": "deck_macro",
        "bg": (40, 30, 25),
        "primary": (190, 130, 88),
        "accent": (210, 160, 115),
        "lighting": "side_angled",
        "elements": ["macro_woodgrain", "hidden_clip", "chamfered_joint"]
    },
    {
        "filename": "service-pergola-construction.webp",
        "size": (1600, 850),
        "theme": "pergola_hero",
        "bg": (28, 55, 42),
        "primary": (165, 115, 75),
        "accent": WARM_CREAM,
        "lighting": "bright_sun",
        "elements": ["grand_pergola_beams", "louver_array", "stone_pedestals", "climbing_vines"]
    },
    {
        "filename": "service-covered-outdoor.webp",
        "size": (1400, 850),
        "theme": "covered_hero",
        "bg": (20, 42, 34),
        "primary": TIMBER,
        "accent": GOLD,
        "lighting": "warm_dusk",
        "elements": ["vaulted_soffit", "recessed_downlights", "outdoor_sofa", "deck_planks"]
    },
    {
        "filename": "service-patio-design.webp",
        "size": (1000, 700),
        "theme": "patio_terrace",
        "bg": (35, 42, 38),
        "primary": (155, 150, 140),
        "accent": SAGE,
        "lighting": "soft_daylight",
        "elements": ["bluestone_flags", "low_retaining_wall", "potted_olive", "timber_bench"]
    },
    {
        "filename": "service-entertainment-area.webp",
        "size": (800, 600),
        "theme": "entertainment",
        "bg": (25, 45, 38),
        "primary": CHARCOAL,
        "accent": TIMBER,
        "lighting": "party_evening",
        "elements": ["outdoor_counter", "bar_stools", "string_lights", "deck_flooring"]
    },
    {
        "filename": "service-outdoor-dining.webp",
        "size": (800, 600),
        "theme": "dining",
        "bg": (28, 52, 42),
        "primary": TIMBER,
        "accent": WARM_CREAM,
        "lighting": "candlelit_dusk",
        "elements": ["dining_table", "chairs", "pergola_canopy", "lanterns"]
    },
    {
        "filename": "service-renovation-existing.webp",
        "size": (900, 650),
        "theme": "before_deck",
        "bg": (45, 48, 45),
        "primary": (130, 120, 110),
        "accent": (105, 95, 88),
        "lighting": "overcast",
        "elements": ["weathered_planks", "grey_patina", "traditional_wood_baluster"]
    },
    {
        "filename": "service-renovation-refresh.webp",
        "size": (900, 650),
        "theme": "after_deck",
        "bg": (26, 52, 40),
        "primary": (185, 130, 85),
        "accent": GOLD,
        "lighting": "brilliant_sun",
        "elements": ["fresh_stained_deck", "black_cable_railing", "modern_flush_leds"]
    },
    {
        "filename": "service-choose-space.webp",
        "size": (1200, 800),
        "theme": "landscape_aerial",
        "bg": (22, 48, 36),
        "primary": TIMBER,
        "accent": SAGE,
        "lighting": "afternoon_high",
        "elements": ["zoned_deck", "pergola_zone", "stone_walkway", "sculpted_lawn"]
    },
    {
        "filename": "services-final-cta.webp",
        "size": (1600, 750),
        "theme": "final_vista",
        "bg": (18, 38, 30),
        "primary": TIMBER,
        "accent": GOLD,
        "lighting": "blue_hour_twilight",
        "elements": ["illuminated_pavilion", "glass_reflections", "starlit_garden", "deck_expanse"]
    },
    {
        "filename": "service-material-detail.webp",
        "size": (800, 600),
        "theme": "material_board",
        "bg": (32, 40, 36),
        "primary": TIMBER,
        "accent": (180, 140, 100),
        "lighting": "studio_directional",
        "elements": ["material_swatches", "bronze_hardware", "grain_variations", "stone_sample"]
    }
]

def blend_colors(c1, c2, factor):
    factor = max(0.0, min(1.0, factor))
    return (
        int(c1[0] * (1 - factor) + c2[0] * factor),
        int(c1[1] * (1 - factor) + c2[1] * factor),
        int(c1[2] * (1 - factor) + c2[2] * factor)
    )

def render_image(cfg):
    w, h = cfg["size"]
    im = Image.new("RGB", (w, h), cfg["bg"])
    draw = ImageDraw.Draw(im)

    bg = cfg["bg"]
    primary = cfg["primary"]
    accent = cfg["accent"]
    theme = cfg["theme"]

    # 1. Atmospheric Gradient
    for y in range(h):
        t = y / float(h)
        if "twilight" in cfg["lighting"] or "dusk" in cfg["lighting"] or "blue_hour" in cfg["lighting"]:
            # Dark navy sky fading to deep forest and warm amber horizon
            horizon = 0.5
            if t < horizon:
                st = t / horizon
                col = blend_colors((15, 25, 40), (45, 60, 55), st)
            else:
                gt = (t - horizon) / (1.0 - horizon)
                col = blend_colors((45, 60, 55), bg, gt)
        elif "golden" in cfg["lighting"] or "bright" in cfg["lighting"]:
            col = blend_colors((50, 75, 65), bg, t)
        else:
            col = blend_colors(blend_colors(bg, (40, 55, 48), 0.5), bg, t)
        draw.line([(0, y), (w, y)], fill=col)

    # 2. Render architectural components according to elements
    elems = cfg["elements"]

    # DECK PLANKS (PERSPECTIVE)
    if "deck_planks" in elems or "wide_deck_planks" in elems or "split_finish_deck" in elems:
        deck_start_y = int(h * 0.48)
        num_boards = 32 if "wide_deck_planks" in elems else 40
        for i in range(num_boards):
            progress = (i / float(num_boards)) ** 1.35
            y_board = deck_start_y + int((h - deck_start_y) * progress)
            board_h = max(2, int((h - deck_start_y) / float(num_boards) * (progress * 1.8 + 0.3)))
            
            # Timber plank tone
            t_col = blend_colors(primary, (20, 20, 20), (i % 4) * 0.05)
            draw.rectangle([(0, y_board), (w, y_board + board_h - 2)], fill=t_col)
            # Plank seam shadow
            draw.line([(0, y_board + board_h - 1), (w, y_board + board_h - 1)], fill=(15, 18, 16), width=1)
            # Top highlight
            draw.line([(0, y_board), (w, y_board)], fill=blend_colors(t_col, WARM_CREAM, 0.22), width=1)

            # Wood grain variations
            for x in range(0, w, 55):
                gx = x + (i * 37) % 45
                draw.line([(gx, y_board + board_h // 2), (min(w, gx + 28), y_board + board_h // 2)],
                          fill=blend_colors(t_col, (230, 190, 150), 0.15), width=1)

    # STONE PAVERS
    if "stone_pavers" in elems or "bluestone_flags" in elems:
        paver_y = int(h * 0.50)
        p_rows = 12
        p_cols = 16
        for r in range(p_rows):
            prog = (r / float(p_rows)) ** 1.4
            y1 = paver_y + int((h - paver_y) * prog)
            y2 = paver_y + int((h - paver_y) * ((r + 1) / float(p_rows)) ** 1.4)
            for c in range(p_cols):
                offset = (r % 2) * (w // (p_cols * 2))
                x1 = c * (w // p_cols) + offset - (w // (p_cols * 2))
                x2 = x1 + (w // p_cols) - 4
                stone_shade = blend_colors(primary, (100, 105, 100), (c * 7 + r * 13) % 5 * 0.06)
                draw.rectangle([(x1, y1), (x2, y2 - 3)], fill=stone_shade)
                draw.line([(x1, y1), (x2, y1)], fill=blend_colors(stone_shade, (240, 240, 240), 0.25), width=1)

    # WEATHERED BEFORE PLANKS
    if "weathered_planks" in elems:
        deck_y = int(h * 0.45)
        for i in range(35):
            prog = (i / 35.0) ** 1.3
            y = deck_y + int((h - deck_y) * prog)
            bh = max(3, int(20 * prog))
            # Grey faded weathered wood
            patina = blend_colors((120, 115, 110), (95, 90, 85), (i % 3) * 0.2)
            draw.rectangle([(0, y), (w, y + bh - 2)], fill=patina)
            draw.line([(0, y + bh - 1), (w, y + bh - 1)], fill=(40, 40, 40), width=1)
            # Weather cracks
            for cx in range(10, w, 35):
                draw.line([(cx, y + 2), (cx + 15, y + bh - 3)], fill=(60, 60, 60), width=1)

    # AFTER DECK FRESH STAIN
    if "fresh_stained_deck" in elems:
        deck_y = int(h * 0.45)
        for i in range(35):
            prog = (i / 35.0) ** 1.3
            y = deck_y + int((h - deck_y) * prog)
            bh = max(3, int(20 * prog))
            rich_timber = blend_colors((195, 135, 88), (170, 110, 65), (i % 4) * 0.15)
            draw.rectangle([(0, y), (w, y + bh - 2)], fill=rich_timber)
            draw.line([(0, y + bh - 1), (w, y + bh - 1)], fill=(25, 20, 15), width=2)
            draw.line([(0, y), (w, y)], fill=(245, 195, 140), width=1)
        # Modern black cable railings
        rail_top = int(h * 0.35)
        for post_x in range(40, w, int(w / 5)):
            draw.rectangle([(post_x, rail_top), (post_x + 8, int(h * 0.65))], fill=(30, 32, 30))
        for wire_y in range(rail_top + 10, int(h * 0.65), 18):
            draw.line([(0, wire_y), (w, wire_y)], fill=(180, 185, 190), width=1)

    # PERGOLA STRUCTURE
    if "pergola" in elems or "grand_pergola_beams" in elems or "louver_array" in elems:
        pergola_bottom = int(h * 0.38)
        # Vertical posts
        post_spacing = w // 5
        for p in range(1, 5):
            px = p * post_spacing
            draw.rectangle([(px - 14, 0), (px + 14, int(h * 0.68))], fill=blend_colors(TIMBER, (30, 30, 30), 0.3))
            draw.line([(px - 14, 0), (px - 14, int(h * 0.68))], fill=blend_colors(TIMBER, WARM_CREAM, 0.3), width=2)
        # Horizontal main beam
        beam_y = int(h * 0.22)
        draw.rectangle([(0, beam_y - 12), (w, beam_y + 12)], fill=blend_colors(TIMBER, (20, 20, 20), 0.2))
        draw.line([(0, beam_y - 12), (w, beam_y - 12)], fill=blend_colors(TIMBER, WARM_CREAM, 0.4), width=2)
        # Angled Louvers / Rafters
        for rx in range(20, w, 45):
            draw.polygon([(rx, beam_y - 35), (rx + 16, beam_y - 45), (rx + 24, beam_y + 8), (rx + 8, beam_y + 18)],
                         fill=blend_colors(TIMBER, WARM_CREAM, 0.15))

    # COVERED SOLID ROOF & CEILING
    if "solid_roof" in elems or "vaulted_soffit" in elems:
        ceiling_h = int(h * 0.32)
        # Cedar tongue-and-groove ceiling planks
        for cy in range(0, ceiling_h, 14):
            c_col = blend_colors(TIMBER, (190, 140, 95), (cy % 28) / 28.0)
            draw.rectangle([(0, cy), (w, cy + 12)], fill=c_col)
            draw.line([(0, cy), (w, cy)], fill=(240, 200, 160), width=1)
        # Recessed Downlights / Warm ambient lights
        for lx in range(int(w * 0.15), int(w * 0.9), int(w * 0.22)):
            draw.ellipse([(lx - 12, ceiling_h - 14), (lx + 12, ceiling_h - 6)], fill=(255, 245, 210))
            # Light cone glow
            cone = [(lx - 8, ceiling_h - 6), (lx + 8, ceiling_h - 6), (lx + 90, int(h * 0.8)), (lx - 90, int(h * 0.8))]
            # Subtle glow polygon
            draw.polygon(cone, fill=blend_colors(bg, (255, 235, 175), 0.12))

    # RECESSED GLOW / STEP LIGHTS
    if "recessed_glow" in elems:
        step_y = int(h * 0.72)
        for lx in range(int(w * 0.1), w, int(w * 0.18)):
            draw.ellipse([(lx - 8, step_y - 4), (lx + 8, step_y + 4)], fill=(255, 235, 180))

    # OUTDOOR FURNITURE / SOFA / DINING
    if "lounge" in elems or "outdoor_sofa" in elems:
        # Minimalist Scandinavian outdoor modular sofa
        sofa_y = int(h * 0.58)
        sofa_x = int(w * 0.2)
        sofa_w = int(w * 0.45)
        sofa_h = int(h * 0.2)
        # Base platform
        draw.rectangle([(sofa_x, sofa_y + sofa_h - 20), (sofa_x + sofa_w, sofa_y + sofa_h)], fill=(45, 38, 32))
        # Cushions (warm cream / sand beige)
        draw.rounded_rectangle([(sofa_x + 5, sofa_y), (sofa_x + sofa_w - 5, sofa_y + sofa_h - 18)], radius=10, fill=SAND_BEIGE)
        # Backrest pillows
        for p in range(3):
            px1 = sofa_x + 10 + p * (sofa_w // 3)
            px2 = px1 + (sofa_w // 3) - 15
            draw.rounded_rectangle([(px1, sofa_y - 25), (px2, sofa_y + 10)], radius=8, fill=WARM_CREAM)

    if "dining_table" in elems:
        # Long modern teak outdoor dining table
        tx = int(w * 0.25)
        ty = int(h * 0.55)
        tw = int(w * 0.5)
        th = int(h * 0.22)
        draw.rectangle([(tx, ty), (tx + tw, ty + 20)], fill=(155, 105, 65))
        draw.rectangle([(tx + 20, ty + 20), (tx + 36, ty + th)], fill=(35, 35, 35))
        draw.rectangle([(tx + tw - 36, ty + 20), (tx + tw - 20, ty + th)], fill=(35, 35, 35))

    # LUSH GARDEN FOLIAGE SILHOUETTES
    if "foliage" in elems or "lush_trees" in elems or "starlit_garden" in elems:
        num_plants = 16
        for f in range(num_plants):
            fx = int(f * (w / (num_plants - 1)))
            fy = int(h * 0.42 + math.sin(f * 1.5) * 30)
            fr = int(35 + (f % 5) * 16)
            plant_col = blend_colors(DEEP_FOREST, SAGE, (f % 3) * 0.3)
            draw.ellipse([(fx - fr, fy - fr), (fx + fr, fy + fr)], fill=plant_col)

    # MATERIAL SWATCH BOARD
    if "material_swatches" in elems:
        # 4 distinct material tiles
        board_y = int(h * 0.25)
        board_h = int(h * 0.5)
        tile_w = int(w * 0.18)
        gap = int(w * 0.04)
        start_x = int(w * 0.08)

        # Swatch 1: Teak Hardwood
        s1_x = start_x
        draw.rectangle([(s1_x, board_y), (s1_x + tile_w, board_y + board_h)], fill=(185, 125, 80))
        for gy in range(board_y, board_y + board_h, 8):
            draw.line([(s1_x, gy), (s1_x + tile_w, gy)], fill=(160, 105, 65), width=1)

        # Swatch 2: Charcoal Composite
        s2_x = s1_x + tile_w + gap
        draw.rectangle([(s2_x, board_y), (s2_x + tile_w, board_y + board_h)], fill=(45, 50, 48))
        for gy in range(board_y, board_y + board_h, 12):
            draw.line([(s2_x, gy), (s2_x + tile_w, gy)], fill=(60, 66, 64), width=1)

        # Swatch 3: Sanded Cedar
        s3_x = s2_x + tile_w + gap
        draw.rectangle([(s3_x, board_y), (s3_x + tile_w, board_y + board_h)], fill=(210, 160, 115))
        for gy in range(board_y, board_y + board_h, 10):
            draw.line([(s3_x, gy), (s3_x + tile_w, gy)], fill=(195, 145, 100), width=1)

        # Swatch 4: Architectural Bluestone
        s4_x = s3_x + tile_w + gap
        draw.rectangle([(s4_x, board_y), (s4_x + tile_w, board_y + board_h)], fill=(130, 138, 140))
        for gy in range(board_y, board_y + board_h, 16):
            draw.line([(s4_x, gy), (s4_x + tile_w, gy)], fill=(115, 122, 125), width=2)

    # MACRO WOODGRAIN & HARDWARE
    if "macro_woodgrain" in elems:
        for y in range(h):
            grain = math.sin(y * 0.12) * 15 + math.sin(y * 0.03) * 30
            c = blend_colors(primary, accent, (math.sin(y * 0.05) + 1) * 0.5)
            draw.line([(0, y), (w, y)], fill=c)
        # Concealed fastener hardware plate
        hx1, hy1 = int(w * 0.4), int(h * 0.35)
        hx2, hy2 = int(w * 0.6), int(h * 0.65)
        draw.rounded_rectangle([(hx1, hy1), (hx2, hy2)], radius=12, fill=(35, 38, 36))
        draw.ellipse([(int(w * 0.5) - 15, int(h * 0.5) - 15), (int(w * 0.5) + 15, int(h * 0.5) + 15)], fill=(180, 185, 190))

    # Architectural framing & subtle vignette
    # Top and bottom soft architectural vignetting
    vig = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vig)
    for vy in range(60):
        alpha = int(90 * (1 - vy / 60.0))
        vdraw.line([(0, vy), (w, vy)], fill=(0, 0, 0, alpha))
        vdraw.line([(0, h - vy - 1), (w, h - vy - 1)], fill=(0, 0, 0, alpha))
    im.paste(vig, (0, 0), vig)

    # Save as high-quality WebP
    out_path = os.path.join(out_dir, cfg["filename"])
    im.save(out_path, "WEBP", quality=92, method=6)
    print(f"Generated {cfg['filename']} -> {w}x{h}")

for c in services_images:
    render_image(c)

print("All 18 Services images created successfully!")
