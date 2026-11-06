import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter

out_dir = r"assets/images/projects"
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

projects_images = [
    {
        "filename": "projects-hero.webp",
        "size": (1600, 900),
        "theme": "hero",
        "bg": (20, 44, 34),
        "primary": TIMBER,
        "accent": SAND_BEIGE,
        "lighting": "golden_dusk",
        "elements": ["pergola", "wide_deck", "ambient_glow", "foliage", "architectural_blueprint"]
    },
    {
        "filename": "project-concept-timber-deck.webp",
        "size": (800, 600),
        "theme": "concept_deck",
        "bg": (28, 52, 40),
        "primary": (180, 125, 82),
        "accent": WARM_CREAM,
        "lighting": "daylight",
        "elements": ["deck_planks", "cable_rail", "planter_boxes"]
    },
    {
        "filename": "project-concept-garden-pergola.webp",
        "size": (800, 600),
        "theme": "concept_pergola",
        "bg": (32, 56, 44),
        "primary": (160, 110, 72),
        "accent": SAND_BEIGE,
        "lighting": "filtered_sun",
        "elements": ["pergola_rafters", "shadow_slats", "garden_foliage"]
    },
    {
        "filename": "project-concept-covered-lounge.webp",
        "size": (800, 600),
        "theme": "concept_covered",
        "bg": (22, 45, 35),
        "primary": TIMBER,
        "accent": GOLD,
        "lighting": "warm_evening",
        "elements": ["cedar_soffit", "pendant_light", "modular_lounge"]
    },
    {
        "filename": "project-concept-dining-courtyard.webp",
        "size": (800, 600),
        "theme": "concept_patio",
        "bg": (36, 44, 40),
        "primary": (155, 150, 142),
        "accent": TIMBER,
        "lighting": "alfresco_dusk",
        "elements": ["bluestone_flags", "dining_table", "string_lights"]
    },
    {
        "filename": "project-spotlight-deck.webp",
        "size": (1200, 800),
        "theme": "spotlight_deck",
        "bg": (24, 50, 38),
        "primary": (185, 130, 85),
        "accent": SAND_BEIGE,
        "lighting": "bright_sun",
        "elements": ["cantilever_deck", "glass_sliding_doors", "stepped_risers", "ambient_glow"]
    },
    {
        "filename": "project-spotlight-pergola.webp",
        "size": (1200, 800),
        "theme": "spotlight_pergola",
        "bg": (28, 54, 42),
        "primary": (165, 115, 75),
        "accent": WARM_CREAM,
        "lighting": "side_angled",
        "elements": ["freestanding_pergola", "paved_terrace", "dimension_lines"]
    },
    {
        "filename": "project-design-planning.webp",
        "size": (1200, 700),
        "theme": "planning_schematic",
        "bg": (26, 48, 38),
        "primary": (210, 205, 195),
        "accent": GOLD,
        "lighting": "drafting_studio",
        "elements": ["blueprint_grid", "architectural_elevations", "material_samples", "dimension_lines"]
    },
    {
        "filename": "project-detail-timber.webp",
        "size": (800, 600),
        "theme": "detail_timber",
        "bg": (42, 30, 24),
        "primary": (195, 135, 90),
        "accent": (220, 165, 115),
        "lighting": "macro_studio",
        "elements": ["macro_woodgrain", "concealed_clip", "chamfered_joint"]
    },
    {
        "filename": "project-detail-structure.webp",
        "size": (800, 600),
        "theme": "detail_structure",
        "bg": (30, 34, 32),
        "primary": (160, 110, 70),
        "accent": (180, 185, 190),
        "lighting": "side_shadow",
        "elements": ["mortise_tenon", "black_steel_bracket", "hex_bolts"]
    },
    {
        "filename": "project-detail-stone.webp",
        "size": (800, 600),
        "theme": "detail_stone",
        "bg": (40, 42, 40),
        "primary": (150, 145, 138),
        "accent": (120, 115, 110),
        "lighting": "raking_light",
        "elements": ["chiseled_fieldstone", "dry_stacked_joints", "deck_border"]
    },
    {
        "filename": "project-detail-lighting.webp",
        "size": (800, 600),
        "theme": "detail_lighting",
        "bg": (22, 26, 24),
        "primary": (168, 117, 78),
        "accent": (255, 230, 160),
        "lighting": "warm_graze_2700k",
        "elements": ["recessed_bronze_well", "light_graze_cone", "fascia_wood"]
    },
    {
        "filename": "project-direction-relax.webp",
        "size": (800, 600),
        "theme": "direction_relax",
        "bg": (24, 48, 38),
        "primary": TIMBER,
        "accent": SAGE,
        "lighting": "zen_morning",
        "elements": ["water_fountain", "dual_loungers", "bamboo_foliage"]
    },
    {
        "filename": "project-direction-entertain.webp",
        "size": (800, 600),
        "theme": "direction_entertain",
        "bg": (26, 46, 38),
        "primary": CHARCOAL,
        "accent": GOLD,
        "lighting": "twilight_party",
        "elements": ["outdoor_counter", "fire_pit", "deck_flooring"]
    },
    {
        "filename": "project-direction-extension.webp",
        "size": (800, 600),
        "theme": "direction_extension",
        "bg": (28, 52, 42),
        "primary": (175, 120, 80),
        "accent": WARM_CREAM,
        "lighting": "spacious_afternoon",
        "elements": ["multi_tier_deck", "pergola_transition", "lawn_connection"]
    },
    {
        "filename": "projects-final-cta.webp",
        "size": (1600, 800),
        "theme": "final_cta",
        "bg": (16, 36, 28),
        "primary": TIMBER,
        "accent": GOLD,
        "lighting": "night_luxury",
        "elements": ["illuminated_retreat", "ambient_glow", "starlight", "architectural_terrace"]
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

    # 1. Base Sky & Environmental Gradient
    for y in range(h):
        t = y / float(h)
        if "dusk" in lighting or "night" in lighting or "evening" in lighting or "party" in lighting:
            horizon = 0.52
            if t < horizon:
                st = t / horizon
                col = blend_colors((14, 24, 38), (42, 60, 52), st)
            else:
                gt = (t - horizon) / (1.0 - horizon)
                col = blend_colors((42, 60, 52), bg, gt)
        elif "golden" in lighting or "warm" in lighting:
            col = blend_colors((56, 80, 68), bg, t)
        else:
            col = blend_colors(blend_colors(bg, (46, 62, 54), 0.4), bg, t)
        draw.line([(0, y), (w, y)], fill=col)

    # 2. Render architectural elements

    # BLUEPRINT SCHEMATIC / DRAFTING GRID
    if "blueprint_grid" in elems:
        # Subtle drafting grid
        grid_size = 40
        for gx in range(0, w, grid_size):
            draw.line([(gx, 0), (gx, h)], fill=(38, 70, 56), width=1)
        for gy in range(0, h, grid_size):
            draw.line([(0, gy), (w, gy)], fill=(38, 70, 56), width=1)
        # Architectural elevation lines
        draw.line([(w * 0.15, h * 0.65), (w * 0.85, h * 0.65)], fill=WARM_CREAM, width=2)
        draw.rectangle([(w * 0.25, h * 0.35), (w * 0.75, h * 0.65)], outline=blend_colors(TIMBER, WARM_CREAM, 0.4), width=2)
        # Dimension arrows
        draw.line([(w * 0.25, h * 0.3), (w * 0.75, h * 0.3)], fill=GOLD, width=1)
        draw.polygon([(w * 0.25, h * 0.3), (w * 0.25 + 10, h * 0.3 - 4), (w * 0.25 + 10, h * 0.3 + 4)], fill=GOLD)
        draw.polygon([(w * 0.75, h * 0.3), (w * 0.75 - 10, h * 0.3 - 4), (w * 0.75 - 10, h * 0.3 + 4)], fill=GOLD)

    # DECK PLANKS (PERSPECTIVE)
    if any(k in elems for k in ["wide_deck", "deck_planks", "cantilever_deck", "multi_tier_deck", "deck_flooring"]):
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
            # Wood grain variations
            for x in range(0, w, 55):
                gx = x + (i * 37) % 45
                draw.line([(gx, y_board + board_h // 2), (min(w, gx + 28), y_board + board_h // 2)],
                          fill=blend_colors(t_col, (230, 190, 150), 0.15), width=1)

    # CABLE RAILING / METAL BALUSTER
    if "cable_rail" in elems:
        rail_top = int(h * 0.36)
        for post_x in range(40, w, int(w / 5)):
            draw.rectangle([(post_x, rail_top), (post_x + 8, int(h * 0.65))], fill=(30, 32, 30))
        for wire_y in range(rail_top + 12, int(h * 0.65), 18):
            draw.line([(0, wire_y), (w, wire_y)], fill=(185, 190, 195), width=1)

    # STONE PAVERS / FLAGSTONES
    if "bluestone_flags" in elems or "paved_terrace" in elems:
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

    # PERGOLA POSTS & BEAMS
    if any(k in elems for k in ["pergola", "pergola_rafters", "freestanding_pergola"]):
        pergola_h = int(h * 0.42)
        post_spacing = w // 5
        for p in range(1, 5):
            px = p * post_spacing
            draw.rectangle([(px - 14, 0), (px + 14, int(h * 0.68))], fill=blend_colors(primary, (25, 25, 25), 0.25))
            draw.line([(px - 14, 0), (px - 14, int(h * 0.68))], fill=blend_colors(primary, WARM_CREAM, 0.3), width=2)
        beam_y = int(h * 0.22)
        draw.rectangle([(0, beam_y - 12), (w, beam_y + 12)], fill=blend_colors(primary, (15, 15, 15), 0.2))
        draw.line([(0, beam_y - 12), (w, beam_y - 12)], fill=blend_colors(primary, WARM_CREAM, 0.4), width=2)
        for rx in range(20, w, 45):
            draw.polygon([(rx, beam_y - 35), (rx + 16, beam_y - 45), (rx + 24, beam_y + 8), (rx + 8, beam_y + 18)],
                         fill=blend_colors(primary, WARM_CREAM, 0.15))

    # COVERED SOFFIT / CEILING
    if "cedar_soffit" in elems:
        ceiling_h = int(h * 0.32)
        for cy in range(0, ceiling_h, 14):
            c_col = blend_colors(primary, (190, 140, 95), (cy % 28) / 28.0)
            draw.rectangle([(0, cy), (w, cy + 12)], fill=c_col)
            draw.line([(0, cy), (w, cy)], fill=(240, 200, 160), width=1)
        for lx in range(int(w * 0.2), int(w * 0.9), int(w * 0.28)):
            draw.line([(lx, 0), (lx, ceiling_h + 35)], fill=(50, 45, 40), width=2)
            draw.polygon([(lx - 20, ceiling_h + 35), (lx + 20, ceiling_h + 35), (lx + 32, ceiling_h + 55), (lx - 32, ceiling_h + 55)], fill=GOLD)
            draw.ellipse([(lx - 10, ceiling_h + 50), (lx + 10, ceiling_h + 68)], fill=(255, 245, 190))

    # OUTDOOR LOUNGE / SOFA / DINING
    if "modular_lounge" in elems:
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

    if "dining_table" in elems:
        tx = int(w * 0.25)
        ty = int(h * 0.55)
        tw = int(w * 0.5)
        th = int(h * 0.22)
        draw.rectangle([(tx, ty), (tx + tw, ty + 20)], fill=(155, 105, 65))
        draw.rectangle([(tx + 20, ty + 20), (tx + 36, ty + th)], fill=(35, 35, 35))
        draw.rectangle([(tx + tw - 36, ty + 20), (tx + tw - 20, ty + th)], fill=(35, 35, 35))

    # FIRE PIT / FIRE BOWL
    if "fire_pit" in elems:
        fx, fy = int(w * 0.5), int(h * 0.65)
        fr = int(min(w, h) * 0.12)
        draw.ellipse([(fx - fr, fy - fr // 2), (fx + fr, fy + fr // 2)], fill=(45, 45, 45))
        draw.ellipse([(fx - fr + 10, fy - fr // 2 + 5), (fx + fr - 10, fy + fr // 2 - 5)], fill=(25, 25, 25))
        draw.ellipse([(fx - fr // 2, fy - fr // 3), (fx + fr // 2, fy + fr // 3)], fill=(255, 180, 70))
        draw.ellipse([(fx - fr // 4, fy - fr // 5), (fx + fr // 4, fy + fr // 5)], fill=(255, 240, 160))

    # MACRO WOODGRAIN & HARDWARE
    if "macro_woodgrain" in elems:
        for y in range(h):
            factor = (math.sin(y * 0.08) * 0.3 + math.sin(y * 0.02) * 0.7 + 1) * 0.5
            col = blend_colors(primary, accent, factor)
            draw.line([(0, y), (w, y)], fill=col)
        if "concealed_clip" in elems:
            hx1, hy1 = int(w * 0.4), int(h * 0.35)
            hx2, hy2 = int(w * 0.6), int(h * 0.65)
            draw.rounded_rectangle([(hx1, hy1), (hx2, hy2)], radius=12, fill=(35, 38, 36))
            draw.ellipse([(int(w * 0.5) - 15, int(h * 0.5) - 15), (int(w * 0.5) + 15, int(h * 0.5) + 15)], fill=(180, 185, 190))

    # MORTISE & TENON STRUCTURAL DETAIL
    if "mortise_tenon" in elems:
        draw.rectangle([(w * 0.35, 0), (w * 0.65, h)], fill=(165, 115, 75))
        draw.rectangle([(0, h * 0.38), (w, h * 0.62)], fill=(145, 100, 65))
        # Black steel bracket
        draw.rectangle([(w * 0.3, h * 0.35), (w * 0.7, h * 0.65)], outline=(35, 35, 35), width=6)
        # Hex bolts
        for bx in [int(w * 0.36), int(w * 0.64)]:
            for by in [int(h * 0.42), int(h * 0.58)]:
                draw.ellipse([(bx - 8, by - 8), (bx + 8, by + 8)], fill=(180, 185, 190))

    # CHISELED DRY STACKED STONE
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
        draw.ellipse([(bx - 35, by - 14), (bx + 35, by + 14)], fill=(140, 100, 60))
        draw.ellipse([(bx - 22, by - 8), (bx + 22, by + 8)], fill=(255, 235, 170))
        cone = [(bx - 18, by - 8), (bx + 18, by - 8), (bx + 220, 0), (bx - 220, 0)]
        draw.polygon(cone, fill=blend_colors(bg, (255, 225, 140), 0.22))

    # AMBIENT GLOW / STEP LIGHTS
    if "ambient_glow" in elems:
        step_y = int(h * 0.72)
        for lx in range(int(w * 0.1), w, int(w * 0.18)):
            draw.ellipse([(lx - 8, step_y - 4), (lx + 8, step_y + 4)], fill=(255, 235, 180))

    # FOLIAGE / TREES
    if "foliage" in elems or "garden_foliage" in elems or "bamboo_foliage" in elems:
        num_plants = 16
        for f in range(num_plants):
            fx = int(f * (w / (num_plants - 1)))
            fy = int(h * 0.42 + math.sin(f * 1.5) * 30)
            fr = int(35 + (f % 5) * 16)
            plant_col = blend_colors(DEEP_FOREST, SAGE, (f % 3) * 0.3)
            draw.ellipse([(fx - fr, fy - fr), (fx + fr, fy + fr)], fill=plant_col)

    # Soft Vignette
    vig = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vig)
    for vy in range(50):
        alpha = int(75 * (1 - vy / 50.0))
        vdraw.line([(0, vy), (w, vy)], fill=(0, 0, 0, alpha))
        vdraw.line([(0, h - vy - 1), (w, h - vy - 1)], fill=(0, 0, 0, alpha))
    im.paste(vig, (0, 0), vig)

    # Save as WebP
    out_path = os.path.join(out_dir, cfg["filename"])
    im.save(out_path, "WEBP", quality=92, method=6)
    print(f"Generated {cfg['filename']} -> {w}x{h}")

for c in projects_images:
    render_image(c)

print(f"All {len(projects_images)} Projects images created successfully!")
