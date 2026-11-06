import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter

out_dir = r"assets/images/gallery"
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

gallery_images = [
    {
        "filename": "gallery-hero.webp",
        "size": (1920, 1080),
        "theme": "hero",
        "bg": (20, 42, 34),
        "primary": TIMBER,
        "accent": SAND_BEIGE,
        "lighting": "cinematic_dusk",
        "elements": ["pergola", "wide_deck", "ambient_glow", "water_reflection", "foliage"]
    },
    {
        "filename": "gallery-collection-deck.webp",
        "size": (900, 700),
        "theme": "collection_deck",
        "bg": (28, 54, 42),
        "primary": (175, 120, 80),
        "accent": SAND_BEIGE,
        "lighting": "daylight",
        "elements": ["multi_tier_deck", "step_lights", "planters"]
    },
    {
        "filename": "gallery-collection-pergola.webp",
        "size": (800, 1000),
        "theme": "collection_pergola",
        "bg": (35, 58, 48),
        "primary": (155, 108, 72),
        "accent": WARM_CREAM,
        "lighting": "shadow_play",
        "elements": ["vertical_pergola_rafters", "geometric_shadows", "stone_base"]
    },
    {
        "filename": "gallery-collection-covered.webp",
        "size": (1000, 750),
        "theme": "collection_covered",
        "bg": (22, 46, 36),
        "primary": TIMBER,
        "accent": GOLD,
        "lighting": "warm_interior",
        "elements": ["vaulted_soffit", "pendant_light", "lounge_sofa"]
    },
    {
        "filename": "gallery-collection-patio.webp",
        "size": (900, 650),
        "theme": "collection_patio",
        "bg": (36, 44, 40),
        "primary": (160, 155, 148),
        "accent": TIMBER,
        "lighting": "firelight",
        "elements": ["flagstones", "fire_pit", "casual_chairs"]
    },
    {
        "filename": "gallery-collection-detail.webp",
        "size": (750, 900),
        "theme": "collection_detail",
        "bg": (42, 32, 26),
        "primary": (195, 135, 90),
        "accent": (215, 165, 120),
        "lighting": "macro_studio",
        "elements": ["macro_grain", "bevel_edge", "concealed_fastener"]
    },
    {
        "filename": "gallery-collection-landscape.webp",
        "size": (1000, 700),
        "theme": "collection_landscape",
        "bg": (24, 50, 38),
        "primary": TIMBER,
        "accent": SAGE,
        "lighting": "soft_morning",
        "elements": ["deck_pathway", "boulder_edging", "lush_gardens"]
    },
    {
        "filename": "gallery-deck-contemporary.webp",
        "size": (1200, 800),
        "theme": "deck_contemporary",
        "bg": (30, 48, 40),
        "primary": (140, 135, 130),
        "accent": CHARCOAL,
        "lighting": "modern_clean",
        "elements": ["composite_planks", "metal_baluster", "bench_integrated"]
    },
    {
        "filename": "gallery-deck-natural.webp",
        "size": (800, 600),
        "theme": "deck_natural",
        "bg": (26, 52, 40),
        "primary": (185, 128, 82),
        "accent": WARM_CREAM,
        "lighting": "golden_hour",
        "elements": ["teak_grain", "fern_borders", "low_profile_steps"]
    },
    {
        "filename": "gallery-deck-levels.webp",
        "size": (800, 600),
        "theme": "deck_levels",
        "bg": (28, 55, 42),
        "primary": TIMBER,
        "accent": SAND_BEIGE,
        "lighting": "bright_sun",
        "elements": ["two_level_terrace", "stepped_risers", "accent_lighting"]
    },
    {
        "filename": "gallery-deck-garden.webp",
        "size": (800, 600),
        "theme": "deck_garden",
        "bg": (22, 48, 36),
        "primary": (160, 110, 70),
        "accent": SAGE,
        "lighting": "dappled_shade",
        "elements": ["cantilever_deck", "water_mirror", "stepping_stones"]
    },
    {
        "filename": "gallery-pergola-timber.webp",
        "size": (1000, 750),
        "theme": "pergola_timber",
        "bg": (28, 56, 44),
        "primary": (170, 118, 76),
        "accent": WARM_CREAM,
        "lighting": "rustic_afternoon",
        "elements": ["heavy_cedar_posts", "notched_beams", "open_sky"]
    },
    {
        "filename": "gallery-pergola-modern.webp",
        "size": (1000, 750),
        "theme": "pergola_modern",
        "bg": (32, 42, 38),
        "primary": CHARCOAL,
        "accent": TIMBER,
        "lighting": "architectural_crisp",
        "elements": ["black_aluminum_frame", "louver_slats", "integrated_strip_light"]
    },
    {
        "filename": "gallery-pergola-garden.webp",
        "size": (1000, 750),
        "theme": "pergola_garden",
        "bg": (24, 52, 38),
        "primary": TIMBER,
        "accent": (240, 220, 230),
        "lighting": "blooming_spring",
        "elements": ["wisteria_vines", "stone_path", "garden_seating"]
    },
    {
        "filename": "gallery-covered-dining.webp",
        "size": (1400, 750),
        "theme": "covered_dining",
        "bg": (20, 40, 32),
        "primary": TIMBER,
        "accent": GOLD,
        "lighting": "intimate_dining",
        "elements": ["vaulted_timber_roof", "brass_pendants", "dining_table_set"]
    },
    {
        "filename": "gallery-covered-lounge.webp",
        "size": (800, 600),
        "theme": "covered_lounge",
        "bg": (24, 46, 36),
        "primary": (165, 115, 75),
        "accent": SAND_BEIGE,
        "lighting": "fireplace_dusk",
        "elements": ["deep_sofa", "stone_hearth", "timber_ceiling"]
    },
    {
        "filename": "gallery-covered-architecture.webp",
        "size": (800, 600),
        "theme": "covered_arch",
        "bg": (28, 48, 40),
        "primary": CHARCOAL,
        "accent": TIMBER,
        "lighting": "skylight_daylight",
        "elements": ["residence_tie_in", "glass_skylights", "flush_threshold"]
    },
    {
        "filename": "gallery-patio-dining.webp",
        "size": (1000, 750),
        "theme": "patio_dining",
        "bg": (35, 45, 40),
        "primary": (155, 150, 140),
        "accent": TIMBER,
        "lighting": "alfresco_noon",
        "elements": ["bluestone_terrace", "outdoor_kitchen_prep", "teak_chairs"]
    },
    {
        "filename": "gallery-patio-gathering.webp",
        "size": (800, 600),
        "theme": "patio_gathering",
        "bg": (30, 42, 36),
        "primary": (145, 140, 130),
        "accent": GOLD,
        "lighting": "evening_campfire",
        "elements": ["circular_flagstones", "curved_stone_bench", "fire_pit"]
    },
    {
        "filename": "gallery-patio-relax.webp",
        "size": (800, 600),
        "theme": "patio_relax",
        "bg": (34, 44, 38),
        "primary": (165, 160, 150),
        "accent": SAGE,
        "lighting": "quiet_morning",
        "elements": ["water_fountain", "dual_loungers", "terracotta_urns"]
    },
    {
        "filename": "gallery-patio-entertainment.webp",
        "size": (800, 600),
        "theme": "patio_entertainment",
        "bg": (26, 46, 38),
        "primary": CHARCOAL,
        "accent": TIMBER,
        "lighting": "string_ambient",
        "elements": ["wide_entertainment_zone", "bistro_lights", "perennial_borders"]
    },
    {
        "filename": "gallery-detail-timber.webp",
        "size": (800, 600),
        "theme": "detail_timber",
        "bg": (45, 30, 22),
        "primary": (195, 130, 85),
        "accent": (220, 165, 115),
        "lighting": "macro_grain",
        "elements": ["quarter_sawn_grain", "satin_oil_highlight", "growth_rings"]
    },
    {
        "filename": "gallery-detail-decking.webp",
        "size": (800, 600),
        "theme": "detail_decking",
        "bg": (38, 40, 36),
        "primary": TIMBER,
        "accent": WARM_CREAM,
        "lighting": "angle_light",
        "elements": ["herringbone_pattern", "picture_frame_miters", "flush_fasteners"]
    },
    {
        "filename": "gallery-detail-structure.webp",
        "size": (800, 600),
        "theme": "detail_structure",
        "bg": (30, 34, 32),
        "primary": (160, 110, 70),
        "accent": (180, 185, 190),
        "lighting": "side_shadow",
        "elements": ["mortise_tenon", "black_steel_bracket", "hex_bolts"]
    },
    {
        "filename": "gallery-detail-stone.webp",
        "size": (800, 600),
        "theme": "detail_stone",
        "bg": (40, 42, 40),
        "primary": (150, 145, 138),
        "accent": (120, 115, 110),
        "lighting": "raking_light",
        "elements": ["chiseled_fieldstone", "dry_stacked_joints", "lichen_patina"]
    },
    {
        "filename": "gallery-detail-lighting.webp",
        "size": (800, 600),
        "theme": "detail_lighting",
        "bg": (22, 26, 24),
        "primary": (168, 117, 78),
        "accent": (255, 230, 160),
        "lighting": "warm_graze_2700k",
        "elements": ["recessed_bronze_well", "light_graze_cone", "fascia_wood"]
    },
    {
        "filename": "gallery-moodboard-natural.webp",
        "size": (800, 800),
        "theme": "moodboard_natural",
        "bg": (34, 52, 42),
        "primary": TIMBER,
        "accent": SAGE,
        "lighting": "flat_lay",
        "elements": ["swatch_teak", "swatch_riverstone", "swatch_sage_linen", "swatch_moss"]
    },
    {
        "filename": "gallery-moodboard-contemporary.webp",
        "size": (800, 800),
        "theme": "moodboard_contemporary",
        "bg": (36, 40, 38),
        "primary": (60, 65, 62),
        "accent": (210, 205, 195),
        "lighting": "flat_lay",
        "elements": ["swatch_matte_black", "swatch_ash_wood", "swatch_concrete", "swatch_zinc"]
    },
    {
        "filename": "gallery-moodboard-entertaining.webp",
        "size": (800, 800),
        "theme": "moodboard_entertaining",
        "bg": (38, 48, 40),
        "primary": (180, 120, 75),
        "accent": GOLD,
        "lighting": "flat_lay",
        "elements": ["swatch_oiled_ipe", "swatch_amber_glass", "swatch_brass", "swatch_outdoor_weave"]
    },
    {
        "filename": "gallery-moodboard-garden.webp",
        "size": (800, 800),
        "theme": "moodboard_garden",
        "bg": (26, 50, 38),
        "primary": SAGE,
        "accent": (150, 115, 80),
        "lighting": "flat_lay",
        "elements": ["swatch_slate", "swatch_cedar", "swatch_forest_textile", "swatch_grasses"]
    },
    {
        "filename": "gallery-final-cta.webp",
        "size": (1600, 800),
        "theme": "final_cta",
        "bg": (16, 36, 28),
        "primary": TIMBER,
        "accent": GOLD,
        "lighting": "night_luxury",
        "elements": ["illuminated_retreat", "pool_reflections", "starlight", "architectural_terrace"]
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
    lighting = cfg["lighting"]
    elems = cfg["elements"]

    # 1. Atmospheric Gradient
    for y in range(h):
        t = y / float(h)
        if "dusk" in lighting or "night" in lighting or "evening" in lighting:
            horizon = 0.52
            if t < horizon:
                st = t / horizon
                col = blend_colors((12, 22, 35), (40, 58, 50), st)
            else:
                gt = (t - horizon) / (1.0 - horizon)
                col = blend_colors((40, 58, 50), bg, gt)
        elif "golden" in lighting or "warm" in lighting:
            col = blend_colors((55, 78, 65), bg, t)
        else:
            col = blend_colors(blend_colors(bg, (45, 60, 52), 0.4), bg, t)
        draw.line([(0, y), (w, y)], fill=col)

    # 2. Render architectural components according to elements

    # WIDE DECK / DECK PLANKS / MULTI TIER
    if any(k in elems for k in ["wide_deck", "multi_tier_deck", "composite_planks", "teak_grain", "two_level_terrace", "cantilever_deck"]):
        deck_y = int(h * 0.48)
        num_boards = 38
        for i in range(num_boards):
            prog = (i / float(num_boards)) ** 1.35
            y_board = deck_y + int((h - deck_y) * prog)
            board_h = max(2, int((h - deck_y) / float(num_boards) * (prog * 1.8 + 0.3)))
            t_col = blend_colors(primary, (20, 20, 20), (i % 4) * 0.06)
            draw.rectangle([(0, y_board), (w, y_board + board_h - 2)], fill=t_col)
            draw.line([(0, y_board + board_h - 1), (w, y_board + board_h - 1)], fill=(15, 18, 16), width=1)
            draw.line([(0, y_board), (w, y_board)], fill=blend_colors(t_col, WARM_CREAM, 0.22), width=1)
            # Wood grain highlights
            for x in range(0, w, 55):
                gx = x + (i * 37) % 45
                draw.line([(gx, y_board + board_h // 2), (min(w, gx + 28), y_board + board_h // 2)],
                          fill=blend_colors(t_col, (230, 190, 150), 0.15), width=1)

    # STEP LIGHTS / LOW PROFILE STEPS / ACCENT LIGHTING
    if "step_lights" in elems or "accent_lighting" in elems or "ambient_glow" in elems:
        step_y = int(h * 0.72)
        for lx in range(int(w * 0.1), w, int(w * 0.18)):
            draw.ellipse([(lx - 8, step_y - 4), (lx + 8, step_y + 4)], fill=(255, 235, 180))

    # STONE PAVERS / FLAGSTONES / BLUESTONE
    if any(k in elems for k in ["flagstones", "bluestone_flags", "circular_flagstones", "bluestone_terrace"]):
        paver_y = int(h * 0.50)
        p_rows, p_cols = 14, 18
        for r in range(p_rows):
            prog = (r / float(p_rows)) ** 1.4
            y1 = paver_y + int((h - paver_y) * prog)
            y2 = paver_y + int((h - paver_y) * ((r + 1) / float(p_rows)) ** 1.4)
            for c in range(p_cols):
                offset = (r % 2) * (w // (p_cols * 2))
                x1 = c * (w // p_cols) + offset - (w // (p_cols * 2))
                x2 = x1 + (w // p_cols) - 4
                stone_shade = blend_colors(primary, (95, 100, 95), (c * 7 + r * 13) % 5 * 0.06)
                draw.rectangle([(x1, y1), (x2, y2 - 3)], fill=stone_shade)
                draw.line([(x1, y1), (x2, y1)], fill=blend_colors(stone_shade, (240, 240, 240), 0.25), width=1)

    # FIRE PIT / FIRE BOWL
    if "fire_pit" in elems:
        fx, fy = int(w * 0.5), int(h * 0.65)
        fr = int(min(w, h) * 0.12)
        draw.ellipse([(fx - fr, fy - fr // 2), (fx + fr, fy + fr // 2)], fill=(45, 45, 45))
        draw.ellipse([(fx - fr + 10, fy - fr // 2 + 5), (fx + fr - 10, fy + fr // 2 - 5)], fill=(25, 25, 25))
        # Warm flame core
        draw.ellipse([(fx - fr // 2, fy - fr // 3), (fx + fr // 2, fy + fr // 3)], fill=(255, 180, 70))
        draw.ellipse([(fx - fr // 4, fy - fr // 5), (fx + fr // 4, fy + fr // 5)], fill=(255, 240, 160))

    # PERGOLA RAFTERS / BEAMS
    if any(k in elems for k in ["pergola", "vertical_pergola_rafters", "heavy_cedar_posts", "black_aluminum_frame"]):
        pergola_h = int(h * 0.42)
        post_spacing = w // 5
        # Posts
        for p in range(1, 5):
            px = p * post_spacing
            draw.rectangle([(px - 14, 0), (px + 14, int(h * 0.68))], fill=blend_colors(primary, (25, 25, 25), 0.25))
            draw.line([(px - 14, 0), (px - 14, int(h * 0.68))], fill=blend_colors(primary, WARM_CREAM, 0.3), width=2)
        # Main beam
        beam_y = int(h * 0.22)
        draw.rectangle([(0, beam_y - 12), (w, beam_y + 12)], fill=blend_colors(primary, (15, 15, 15), 0.2))
        draw.line([(0, beam_y - 12), (w, beam_y - 12)], fill=blend_colors(primary, WARM_CREAM, 0.4), width=2)
        # Angled louvers
        for rx in range(20, w, 45):
            draw.polygon([(rx, beam_y - 35), (rx + 16, beam_y - 45), (rx + 24, beam_y + 8), (rx + 8, beam_y + 18)],
                         fill=blend_colors(primary, WARM_CREAM, 0.15))

    # COVERED SOFFIT / CEILING
    if any(k in elems for k in ["vaulted_soffit", "vaulted_timber_roof", "timber_ceiling"]):
        ceiling_h = int(h * 0.32)
        for cy in range(0, ceiling_h, 14):
            c_col = blend_colors(primary, (190, 140, 95), (cy % 28) / 28.0)
            draw.rectangle([(0, cy), (w, cy + 12)], fill=c_col)
            draw.line([(0, cy), (w, cy)], fill=(240, 200, 160), width=1)
        # Brass pendant lights
        for lx in range(int(w * 0.2), int(w * 0.9), int(w * 0.28)):
            # Rod
            draw.line([(lx, 0), (lx, ceiling_h + 35)], fill=(50, 45, 40), width=2)
            # Shade
            draw.polygon([(lx - 20, ceiling_h + 35), (lx + 20, ceiling_h + 35), (lx + 32, ceiling_h + 55), (lx - 32, ceiling_h + 55)], fill=GOLD)
            # Bulb glow
            draw.ellipse([(lx - 10, ceiling_h + 50), (lx + 10, ceiling_h + 68)], fill=(255, 245, 190))

    # WATER REFLECTION / POOL MIRROR
    if any(k in elems for k in ["water_reflection", "water_mirror", "pool_reflections"]):
        water_y = int(h * 0.65)
        for wy in range(water_y, h):
            wt = (wy - water_y) / float(h - water_y)
            w_col = blend_colors((18, 38, 48), (10, 25, 32), wt)
            draw.line([(0, wy), (w, wy)], fill=w_col)
            # Subtle specular water lines
            if wy % 6 == 0:
                for wx in range(0, w, 60):
                    rx = wx + (wy * 17) % 35
                    draw.line([(rx, wy), (min(w, rx + 40), wy)], fill=(35, 75, 95), width=1)

    # OUTDOOR FURNITURE / SOFA / DINING TABLE
    if any(k in elems for k in ["lounge_sofa", "deep_sofa"]):
        sofa_y = int(h * 0.58)
        sofa_x = int(w * 0.22)
        sofa_w = int(w * 0.45)
        sofa_h = int(h * 0.2)
        draw.rectangle([(sofa_x, sofa_y + sofa_h - 20), (sofa_x + sofa_w, sofa_y + sofa_h)], fill=(45, 38, 32))
        draw.rounded_rectangle([(sofa_x + 5, sofa_y), (sofa_x + sofa_w - 5, sofa_y + sofa_h - 18)], radius=10, fill=SAND_BEIGE)
        for p in range(3):
            px1 = sofa_x + 10 + p * (sofa_w // 3)
            px2 = px1 + (sofa_w // 3) - 15
            draw.rounded_rectangle([(px1, sofa_y - 25), (px2, sofa_y + 10)], radius=8, fill=WARM_CREAM)

    if any(k in elems for k in ["dining_table_set", "outdoor_kitchen_prep"]):
        tx = int(w * 0.25)
        ty = int(h * 0.55)
        tw = int(w * 0.5)
        th = int(h * 0.22)
        draw.rectangle([(tx, ty), (tx + tw, ty + 20)], fill=(155, 105, 65))
        draw.rectangle([(tx + 20, ty + 20), (tx + 36, ty + th)], fill=(35, 35, 35))
        draw.rectangle([(tx + tw - 36, ty + 20), (tx + tw - 20, ty + th)], fill=(35, 35, 35))

    # MACRO WOODGRAIN / DETAILS
    if "macro_grain" in elems or "quarter_sawn_grain" in elems:
        for y in range(h):
            factor = (math.sin(y * 0.08) * 0.3 + math.sin(y * 0.02) * 0.7 + 1) * 0.5
            col = blend_colors(primary, accent, factor)
            draw.line([(0, y), (w, y)], fill=col)
        # Fastener plate / bevel edge
        if "concealed_fastener" in elems or "bevel_edge" in elems:
            hx1, hy1 = int(w * 0.4), int(h * 0.35)
            hx2, hy2 = int(w * 0.6), int(h * 0.65)
            draw.rounded_rectangle([(hx1, hy1), (hx2, hy2)], radius=12, fill=(35, 38, 36))
            draw.ellipse([(int(w * 0.5) - 15, int(h * 0.5) - 15), (int(w * 0.5) + 15, int(h * 0.5) + 15)], fill=(180, 185, 190))

    # HERRINGBONE DECKING PATTERN
    if "herringbone_pattern" in elems:
        unit = 70
        for y in range(0, h + unit * 2, unit):
            for x in range(0, w + unit * 2, unit * 2):
                # Diagonal planks
                draw.polygon([(x, y), (x + unit, y + unit), (x + unit - 12, y + unit), (x - 12, y)], fill=blend_colors(TIMBER, (20, 20, 20), 0.1))
                draw.polygon([(x + unit, y + unit), (x + unit * 2, y), (x + unit * 2 - 12, y), (x + unit - 12, y + unit)], fill=blend_colors(TIMBER, (230, 190, 150), 0.1))

    # DRY STACKED STONE
    if "chiseled_fieldstone" in elems:
        s_rows = 18
        for sr in range(s_rows):
            sy1 = int(sr * (h / float(s_rows)))
            sy2 = int((sr + 1) * (h / float(s_rows)))
            sx = 0
            while sx < w:
                stone_w = random.randint(60, 160)
                s_col = blend_colors(primary, accent, random.random())
                draw.rectangle([(sx, sy1), (min(w, sx + stone_w - 4), sy2 - 4)], fill=s_col)
                draw.line([(sx, sy1), (min(w, sx + stone_w - 4), sy1)], fill=(210, 210, 200), width=1)
                sx += stone_w

    # RECESSED BRONZE LIGHT GRAZE
    if "recessed_bronze_well" in elems:
        for y in range(h):
            draw.line([(0, y), (w, y)], fill=blend_colors(primary, (20, 20, 20), 0.35))
        bx, by = int(w * 0.5), int(h * 0.78)
        # Bronze fixture
        draw.ellipse([(bx - 35, by - 14), (bx + 35, by + 14)], fill=(140, 100, 60))
        draw.ellipse([(bx - 22, by - 8), (bx + 22, by + 8)], fill=(255, 235, 170))
        # Graze light fan
        cone = [(bx - 18, by - 8), (bx + 18, by - 8), (bx + 220, 0), (bx - 220, 0)]
        draw.polygon(cone, fill=blend_colors(bg, (255, 225, 140), 0.22))

    # FLAT LAY MOODBOARDS (4 Quadrant Material Swatches)
    if "flat_lay" in lighting or "swatch_teak" in elems or "swatch_matte_black" in elems:
        pad = int(min(w, h) * 0.08)
        qw = (w - pad * 3) // 2
        qh = (h - pad * 3) // 2
        coords = [
            (pad, pad),
            (pad * 2 + qw, pad),
            (pad, pad * 2 + qh),
            (pad * 2 + qw, pad * 2 + qh)
        ]
        swatch_colors = [
            blend_colors(primary, TIMBER, 0.5),
            blend_colors(accent, (200, 190, 180), 0.5),
            blend_colors(bg, SAGE, 0.5),
            blend_colors(CHARCOAL, WARM_CREAM, 0.4)
        ]
        for idx, (sx, sy) in enumerate(coords):
            sc = swatch_colors[idx]
            draw.rectangle([(sx, sy), (sx + qw, sy + qh)], fill=sc)
            draw.rectangle([(sx, sy), (sx + qw, sy + qh)], outline=blend_colors(sc, WARM_CREAM, 0.3), width=2)
            # Add tactile texture to swatch
            for ly in range(sy + 8, sy + qh, 14):
                draw.line([(sx + 8, ly), (sx + qw - 8, ly)], fill=blend_colors(sc, (30, 30, 30), 0.12), width=1)

    # GARDEN FOLIAGE / TREES
    if any(k in elems for k in ["foliage", "lush_gardens", "fern_borders", "wisteria_vines", "perennial_borders"]):
        num_plants = 16
        for f in range(num_plants):
            fx = int(f * (w / (num_plants - 1)))
            fy = int(h * 0.42 + math.sin(f * 1.5) * 30)
            fr = int(35 + (f % 5) * 16)
            plant_col = blend_colors(DEEP_FOREST, SAGE, (f % 3) * 0.3)
            draw.ellipse([(fx - fr, fy - fr), (fx + fr, fy + fr)], fill=plant_col)

    # Soft Architectural Vignette
    vig = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vig)
    for vy in range(55):
        alpha = int(80 * (1 - vy / 55.0))
        vdraw.line([(0, vy), (w, vy)], fill=(0, 0, 0, alpha))
        vdraw.line([(0, h - vy - 1), (w, h - vy - 1)], fill=(0, 0, 0, alpha))
    im.paste(vig, (0, 0), vig)

    # Save as high-quality WebP
    out_path = os.path.join(out_dir, cfg["filename"])
    im.save(out_path, "WEBP", quality=92, method=6)
    print(f"Generated {cfg['filename']} -> {w}x{h}")

for c in gallery_images:
    render_image(c)

print(f"All {len(gallery_images)} Gallery images created successfully!")
