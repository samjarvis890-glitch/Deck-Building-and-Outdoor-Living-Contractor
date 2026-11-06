import os
import math
import random
from PIL import Image, ImageDraw, ImageFilter

out_dir = r"assets/images/blog"
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
WHITE = (255, 255, 255)
SKY_BLUE = (175, 195, 205)

def blend(c1, c2, factor):
    factor = max(0.0, min(1.0, factor))
    return (
        int(c1[0] * (1 - factor) + c2[0] * factor),
        int(c1[1] * (1 - factor) + c2[1] * factor),
        int(c1[2] * (1 - factor) + c2[2] * factor)
    )

blog_images = [
    # 1. Hero
    {
        "filename": "blog-hero.webp",
        "size": (1600, 1000),
        "theme": "hero_magazine",
        "bg": (28, 52, 42),
        "primary": TIMBER,
        "accent": SAND_BEIGE,
        "lighting": "editorial_morning",
        "elements": ["editorial_cover", "cantilever_pergola", "warm_timber_deck", "lush_foliage", "morning_mist"]
    },
    # 2. Featured Article
    {
        "filename": "blog-featured-article.webp",
        "size": (1200, 800),
        "theme": "featured_living",
        "bg": (32, 56, 44),
        "primary": (175, 122, 80),
        "accent": WARM_CREAM,
        "lighting": "golden_hour",
        "elements": ["indoor_outdoor_transition", "sliding_glass_doors", "seamless_deck", "lounge_sofa", "garden_trees"]
    },
    # 3. Article 1: Deck Planning
    {
        "filename": "blog-article-deck-planning.webp",
        "size": (800, 600),
        "theme": "deck_planning",
        "bg": (25, 48, 38),
        "primary": (185, 128, 82),
        "accent": SAND_BEIGE,
        "lighting": "bright_daylight",
        "elements": ["deck_joists", "planks_in_progress", "spirit_level", "measuring_tape", "lush_lawn"]
    },
    # 4. Article 2: Pergola Style
    {
        "filename": "blog-article-pergola-style.webp",
        "size": (800, 600),
        "theme": "pergola_style",
        "bg": (30, 50, 40),
        "primary": (155, 108, 70),
        "accent": WARM_CREAM,
        "lighting": "dappled_sunlight",
        "elements": ["architectural_slats", "climbing_wisteria", "geometric_shadows", "stone_patio"]
    },
    # 5. Article 3: Small Backyard
    {
        "filename": "blog-article-small-backyard.webp",
        "size": (800, 600),
        "theme": "small_backyard",
        "bg": (34, 46, 40),
        "primary": (170, 120, 80),
        "accent": SAGE,
        "lighting": "intimate_afternoon",
        "elements": ["compact_built_in_bench", "vertical_living_wall", "raised_decking", "boundary_cedar"]
    },
    # 6. Article 4: Deck Materials (Timber vs Composite)
    {
        "filename": "blog-article-deck-materials.webp",
        "size": (800, 600),
        "theme": "deck_materials",
        "bg": (40, 36, 32),
        "primary": (190, 130, 85),
        "accent": (140, 140, 140),
        "lighting": "studio_specimen",
        "elements": ["split_deck_swatches", "natural_hardwood_grain", "composite_charcoal_grooves"]
    },
    # 7. Article 5: Outdoor Dining
    {
        "filename": "blog-article-outdoor-dining.webp",
        "size": (800, 600),
        "theme": "outdoor_dining",
        "bg": (32, 45, 38),
        "primary": (160, 115, 75),
        "accent": SAND_BEIGE,
        "lighting": "alfresco_dusk",
        "elements": ["long_teak_table", "ceramic_tableware", "pendant_glow", "courtyard_hedges"]
    },
    # 8. Article 6: Natural Style
    {
        "filename": "blog-article-natural-style.webp",
        "size": (800, 600),
        "theme": "natural_style",
        "bg": (26, 48, 38),
        "primary": SAGE,
        "accent": TIMBER,
        "lighting": "soft_nordic",
        "elements": ["river_boulders", "ornamental_grasses", "weathered_deck_path", "linen_cushions"]
    },
    # 9. Topic 1: Deck Design
    {
        "filename": "blog-topic-deck-design.webp",
        "size": (600, 450),
        "theme": "topic_deck",
        "bg": (28, 52, 42),
        "primary": TIMBER,
        "accent": WARM_CREAM,
        "lighting": "warm_sun",
        "elements": ["multi_tiered_decking", "integrated_step_lights", "flush_perimeter_board"]
    },
    # 10. Topic 2: Pergola Inspiration
    {
        "filename": "blog-topic-pergola.webp",
        "size": (600, 450),
        "theme": "topic_pergola",
        "bg": (30, 54, 44),
        "primary": (150, 105, 68),
        "accent": SAND_BEIGE,
        "lighting": "high_noon_shadows",
        "elements": ["modern_pergola_rafters", "blue_sky_peeking", "timber_post_footing"]
    },
    # 11. Topic 3: Outdoor Living
    {
        "filename": "blog-topic-outdoor-living.webp",
        "size": (600, 450),
        "theme": "topic_living",
        "bg": (24, 46, 36),
        "primary": (180, 125, 80),
        "accent": GOLD,
        "lighting": "evening_lounge",
        "elements": ["covered_living_room", "woven_furniture", "outdoor_fireplace", "cozy_throws"]
    },
    # 12. Topic 4: Materials & Finishes
    {
        "filename": "blog-topic-materials.webp",
        "size": (600, 450),
        "theme": "topic_materials",
        "bg": (42, 38, 34),
        "primary": (195, 135, 90),
        "accent": (160, 165, 160),
        "lighting": "flat_lay_textures",
        "elements": ["timber_grain_swatch", "granite_paver_sample", "powder_coated_aluminum"]
    },
    # 13. Topic 5: Garden & Landscaping
    {
        "filename": "blog-topic-garden.webp",
        "size": (600, 450),
        "theme": "topic_garden",
        "bg": (22, 48, 34),
        "primary": SAGE,
        "accent": TIMBER,
        "lighting": "lush_morning",
        "elements": ["deck_meandering_lawn", "native_shrubs", "stepping_pavers", "tree_canopy"]
    },
    # 14. Topic 6: Planning & Maintenance
    {
        "filename": "blog-topic-planning.webp",
        "size": (600, 450),
        "theme": "topic_planning",
        "bg": (36, 44, 40),
        "primary": TIMBER,
        "accent": SAND_BEIGE,
        "lighting": "technical_drawing",
        "elements": ["architectural_site_plan", "pencil_and_scale", "wood_finishing_oil_can"]
    },
    # 15. Guide 1: Deck Planning Guide
    {
        "filename": "blog-guide-deck-planning.webp",
        "size": (700, 500),
        "theme": "guide_deck",
        "bg": (26, 50, 40),
        "primary": (180, 125, 80),
        "accent": WARM_CREAM,
        "lighting": "site_inspection",
        "elements": ["elevation_sketch", "deck_footing_piers", "garden_boundary_stakes"]
    },
    # 16. Guide 2: Pergola Planning Guide
    {
        "filename": "blog-guide-pergola-planning.webp",
        "size": (700, 500),
        "theme": "guide_pergola",
        "bg": (30, 52, 42),
        "primary": (160, 110, 72),
        "accent": SAND_BEIGE,
        "lighting": "sun_angle_study",
        "elements": ["pergola_framing_isometric", "solar_angles", "louver_blade_detail"]
    },
    # 17. Guide 3: Entertaining Area Guide
    {
        "filename": "blog-guide-entertaining.webp",
        "size": (700, 500),
        "theme": "guide_entertaining",
        "bg": (28, 44, 38),
        "primary": TIMBER,
        "accent": GOLD,
        "lighting": "party_twilight",
        "elements": ["outdoor_kitchen_island", "bbq_prep_counter", "dining_circulation_flow"]
    },
    # 18. Material 1: Natural Timber
    {
        "filename": "blog-material-natural-timber.webp",
        "size": (700, 500),
        "theme": "material_timber",
        "bg": (46, 32, 24),
        "primary": (200, 135, 85),
        "accent": (230, 175, 125),
        "lighting": "macro_timber",
        "elements": ["rich_spotted_gum_grain", "natural_wood_knots", "warm_oil_sheen", "beveled_edge"]
    },
    # 19. Material 2: Composite Decking
    {
        "filename": "blog-material-composite.webp",
        "size": (700, 500),
        "theme": "material_composite",
        "bg": (38, 40, 42),
        "primary": (95, 100, 105),
        "accent": (145, 150, 155),
        "lighting": "modern_matte",
        "elements": ["engineered_deck_planks", "subtle_embossed_grain", "hidden_clip_groove", "clean_gap"]
    },
    # 20. Material 3: Natural Stone
    {
        "filename": "blog-material-natural-stone.webp",
        "size": (700, 500),
        "theme": "material_stone",
        "bg": (36, 38, 36),
        "primary": (155, 150, 142),
        "accent": (195, 190, 180),
        "lighting": "stone_texture",
        "elements": ["bluestone_honed_surface", "organic_mineral_veining", "tight_mortar_joint"]
    },
    # 21. Idea 1: Layered Lighting
    {
        "filename": "blog-idea-outdoor-lighting.webp",
        "size": (700, 500),
        "theme": "idea_lighting",
        "bg": (18, 28, 34),
        "primary": GOLD,
        "accent": (255, 230, 170),
        "lighting": "nocturne_glow",
        "elements": ["step_riser_leds", "pergola_downlights", "uplit_japanese_maple", "warm_pools_of_light"]
    },
    # 22. Idea 2: Comfortable Garden Seating
    {
        "filename": "blog-idea-garden-seating.webp",
        "size": (700, 500),
        "theme": "idea_seating",
        "bg": (30, 48, 38),
        "primary": (175, 120, 80),
        "accent": SAGE,
        "lighting": "afternoon_shade",
        "elements": ["integrated_deck_daybed", "weatherproof_linen_cushions", "surrounding_bamboo"]
    },
    # 23. Idea 3: Greenery Around Timber
    {
        "filename": "blog-idea-greenery.webp",
        "size": (700, 500),
        "theme": "idea_greenery",
        "bg": (22, 45, 32),
        "primary": SAGE,
        "accent": TIMBER,
        "lighting": "botanical_morning",
        "elements": ["cedar_trellis_with_jasmine", "built_in_deck_planter_boxes", "creeping_groundcover"]
    },
    # 24. Idea 4: Finishing Touches Dining
    {
        "filename": "blog-idea-outdoor-finishing.webp",
        "size": (700, 500),
        "theme": "idea_finishing",
        "bg": (34, 46, 40),
        "primary": (170, 118, 76),
        "accent": SAND_BEIGE,
        "lighting": "stylist_editorial",
        "elements": ["stoneware_plates", "linen_napkins_with_twine", "olive_branch_centerpiece", "wine_glasses"]
    },
    # 25. Newsletter
    {
        "filename": "blog-newsletter.webp",
        "size": (800, 600),
        "theme": "newsletter",
        "bg": (28, 48, 38),
        "primary": TIMBER,
        "accent": SAND_BEIGE,
        "lighting": "quiet_sunday",
        "elements": ["open_magazine_on_deck", "ceramic_coffee_mug", "steaming_brew", "dappled_sunbeam"]
    },
    # 26. Final CTA
    {
        "filename": "blog-final-cta.webp",
        "size": (1600, 800),
        "theme": "final_cta",
        "bg": (18, 38, 30),
        "primary": TIMBER,
        "accent": GOLD,
        "lighting": "dusk_architecture",
        "elements": ["grand_deck_and_pergola_pavilion", "soft_indoor_lights_spilling", "reflecting_pond", "starry_sky"]
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

    # --- 1. Base Sky and Architectural Environment Gradient ---
    for y in range(h):
        t = y / float(h)
        if "dusk" in lighting or "nocturne" in lighting or "evening" in lighting:
            horizon = 0.48
            if t < horizon:
                st = t / horizon
                col = blend((14, 22, 34), (45, 62, 54), st)
            else:
                gt = (t - horizon) / (1.0 - horizon)
                col = blend((45, 62, 54), bg, gt)
        elif "golden" in lighting or "warm" in lighting:
            horizon = 0.42
            if t < horizon:
                st = t / horizon
                col = blend((70, 95, 80), (190, 150, 110), st)
            else:
                col = blend((190, 150, 110), bg, (t - horizon) / (1.0 - horizon))
        elif "morning" in lighting or "soft" in lighting:
            horizon = 0.45
            if t < horizon:
                col = blend((175, 195, 205), (145, 175, 160), t / horizon)
            else:
                col = blend((145, 175, 160), bg, (t - horizon) / (1.0 - horizon))
        elif "macro" in lighting or "studio" in lighting:
            # Radial / vignette soft dark gradient
            center_dist = abs(t - 0.5) * 2
            col = blend(blend(primary, bg, 0.4), (20, 22, 20), center_dist * 0.7)
        else:
            col = blend(blend(bg, (50, 68, 58), 0.5), bg, t)
        draw.line([(0, y), (w, y)], fill=col)

    # --- 2. Architectural Features & Thematic Compositions ---

    # A. Deck Planks (Perspective or Flat)
    if any(k in elems for k in ["warm_timber_deck", "seamless_deck", "deck_joists", "planks_in_progress", "raised_decking", "weathered_deck_path", "multi_tiered_decking", "open_magazine_on_deck", "grand_deck_and_pergola_pavilion"]):
        deck_y = int(h * 0.46)
        num_boards = 40
        for i in range(num_boards):
            prog = (i / float(num_boards)) ** 1.35
            y_board = deck_y + int((h - deck_y) * prog)
            board_h = max(2, int((h - deck_y) / float(num_boards) * (prog * 1.8 + 0.35)))
            t_col = blend(primary, (20, 20, 20), (i % 5) * 0.05)
            draw.rectangle([(0, y_board), (w, y_board + board_h - 2)], fill=t_col)
            # board seam & bevel highlight
            draw.line([(0, y_board + board_h - 1), (w, y_board + board_h - 1)], fill=(15, 18, 16), width=1)
            draw.line([(0, y_board), (w, y_board)], fill=blend(t_col, WARM_CREAM, 0.2), width=1)
            # Wood grain stripes
            for x in range(0, w, 50):
                gx = x + (i * 31) % 45
                draw.line([(gx, y_board + board_h // 2), (min(w, gx + 30), y_board + board_h // 2)],
                          fill=blend(t_col, (240, 200, 160), 0.16), width=1)

    # B. Pergola Beams and Rafters
    if any(k in elems for k in ["cantilever_pergola", "architectural_slats", "modern_pergola_rafters", "louver_blade_detail", "grand_deck_and_pergola_pavilion", "pergola_downlights"]):
        # Vertical Posts
        post_spacing = w // 5
        for p in range(1, 5):
            px = p * post_spacing
            draw.rectangle([(px - 14, 0), (px + 14, int(h * 0.65))], fill=blend(primary, (20, 20, 20), 0.3))
            draw.line([(px - 14, 0), (px - 14, int(h * 0.65))], fill=blend(primary, WARM_CREAM, 0.35), width=2)
        # Overhead Horizontal Beam
        beam_y = int(h * 0.22)
        draw.rectangle([(0, beam_y - 14), (w, beam_y + 14)], fill=blend(primary, (15, 15, 15), 0.25))
        draw.line([(0, beam_y - 14), (w, beam_y - 14)], fill=blend(primary, WARM_CREAM, 0.4), width=2)
        # Transverse Rafters creating rhythmic architectural shadows
        for rx in range(15, w, 45):
            draw.polygon([(rx, beam_y - 32), (rx + 16, beam_y - 42), (rx + 22, beam_y + 8), (rx + 6, beam_y + 18)],
                         fill=blend(primary, WARM_CREAM, 0.18))
            # Cast shadow on ground/deck below
            shadow_x = rx + int(h * 0.25)
            shadow_y_start = int(h * 0.50)
            draw.line([(shadow_x, shadow_y_start), (shadow_x - 30, h)], fill=(12, 16, 14), width=3)

    # C. Natural Stone Pavers & Patios
    if any(k in elems for k in ["stone_patio", "bluestone_honed_surface", "granite_paver_sample", "stepping_pavers"]):
        paver_y = int(h * 0.48) if "bluestone_honed_surface" not in elems else int(h * 0.1)
        p_rows = 14 if "bluestone_honed_surface" not in elems else 8
        p_cols = 16 if "bluestone_honed_surface" not in elems else 8
        for r in range(p_rows):
            prog = (r / float(p_rows)) ** 1.3
            y1 = paver_y + int((h - paver_y) * prog)
            y2 = paver_y + int((h - paver_y) * ((r + 1) / float(p_rows)) ** 1.3)
            for c in range(p_cols):
                offset = (r % 2) * (w // (p_cols * 2))
                x1 = c * (w // p_cols) + offset - (w // (p_cols * 2))
                x2 = x1 + (w // p_cols) - 4
                stone_shade = blend(primary, (90, 95, 90), (c * 7 + r * 11) % 5 * 0.08)
                draw.rectangle([(x1, y1), (x2, y2 - 3)], fill=stone_shade)
                draw.line([(x1, y1), (x2, y1)], fill=blend(stone_shade, (245, 245, 245), 0.28), width=1)
                # Subtle texture specks
                for _ in range(6):
                    sx = random.randint(max(0, x1), min(w - 1, x2))
                    sy = random.randint(max(0, y1), min(h - 1, y2 - 3))
                    draw.point((sx, sy), fill=blend(stone_shade, (230, 230, 230), 0.4))

    # D. Foliage, Trees & Garden Planting
    if any(k in elems for k in ["lush_foliage", "garden_trees", "climbing_wisteria", "vertical_living_wall", "lush_lawn", "native_shrubs", "river_boulders", "cedar_trellis_with_jasmine", "built_in_deck_planter_boxes"]):
        # Background greenery silhouettes
        for _ in range(35):
            bx = random.randint(0, w)
            by = random.randint(int(h * 0.2), int(h * 0.55))
            br = random.randint(25, 90)
            leaf_col = blend(FOREST, SAGE, random.uniform(0.1, 0.7))
            draw.ellipse([(bx - br, by - br), (bx + br, by + br)], fill=leaf_col)
        # Vertical living wall or climbing vines
        if "vertical_living_wall" in elems or "climbing_wisteria" in elems or "cedar_trellis_with_jasmine" in elems:
            for vy in range(int(h * 0.15), int(h * 0.7), 16):
                for vx in range(int(w * 0.05), int(w * 0.35), 20):
                    cluster_col = blend(SAGE, (45, 90, 55), (vx * 3 + vy * 5) % 10 / 10.0)
                    draw.ellipse([(vx - 12, vy - 10), (vx + 12, vy + 10)], fill=cluster_col)
                    # Small blossoms / jasmine white dots
                    if (vx + vy) % 7 == 0:
                        draw.ellipse([(vx - 3, vy - 3), (vx + 3, vy + 3)], fill=(250, 248, 240))

    # E. Architectural Plans, Blueprints & Inspection Guides
    if any(k in elems for k in ["architectural_site_plan", "elevation_sketch", "solar_angles", "spirit_level", "measuring_tape", "pencil_and_scale"]):
        # Drafting grid
        grid_step = 36
        for gx in range(0, w, grid_step):
            draw.line([(gx, 0), (gx, h)], fill=blend(DEEP_FOREST, (45, 80, 65), 0.35), width=1)
        for gy in range(0, h, grid_step):
            draw.line([(0, gy), (w, gy)], fill=blend(DEEP_FOREST, (45, 80, 65), 0.35), width=1)
        # Architectural elevation & floor plan lines
        draw.rectangle([(int(w * 0.2), int(h * 0.25)), (int(w * 0.8), int(h * 0.72))], outline=WARM_CREAM, width=2)
        draw.line([(int(w * 0.2), int(h * 0.45)), (int(w * 0.8), int(h * 0.45))], fill=blend(TIMBER, WARM_CREAM, 0.3), width=2)
        # Deck outline with hatched lines
        for hx in range(int(w * 0.25), int(w * 0.75), 18):
            draw.line([(hx, int(h * 0.45)), (hx + 25, int(h * 0.72))], fill=blend(GOLD, WARM_CREAM, 0.25), width=1)
        # Dimensions & callouts
        draw.line([(int(w * 0.2), int(h * 0.2)), (int(w * 0.8), int(h * 0.2))], fill=GOLD, width=2)
        draw.polygon([(int(w * 0.2), int(h * 0.2)), (int(w * 0.2) + 12, int(h * 0.2) - 5), (int(w * 0.2) + 12, int(h * 0.2) + 5)], fill=GOLD)
        draw.polygon([(int(w * 0.8), int(h * 0.2)), (int(w * 0.8) - 12, int(h * 0.2) - 5), (int(w * 0.8) - 12, int(h * 0.2) + 5)], fill=GOLD)

    # F. Macro Timber Close-Up (Wood Grain, Knots, Rings)
    if "macro_timber" in lighting or "rich_spotted_gum_grain" in elems or "natural_hardwood_grain" in elems:
        # High-res undulating grain lines
        for y in range(0, h, 3):
            wave = math.sin(y * 0.035) * 22 + math.cos(y * 0.08) * 12
            knot_pull = 60 / (1.0 + ((y - h * 0.45) / 45.0) ** 2)
            grain_col = blend(primary, (235, 175, 115), (math.sin(y * 0.12) + 1.0) * 0.35)
            draw.line([(0, y), (w, y + int(wave + knot_pull * 0.2))], fill=grain_col, width=2)
        # Knot ellipse
        kx, ky = int(w * 0.65), int(h * 0.45)
        for kr in range(50, 4, -4):
            k_col = blend((60, 30, 15), primary, kr / 50.0)
            draw.ellipse([(kx - kr * 1.4, ky - kr * 0.8), (kx + kr * 1.4, ky + kr * 0.8)], outline=k_col, width=2)

    # G. Engineered Composite Decking Texture
    if "engineered_deck_planks" in elems or "split_deck_swatches" in elems:
        num_planks = 6
        plank_h = h // num_planks
        for p in range(num_planks):
            py1 = p * plank_h
            py2 = py1 + plank_h - 6
            p_col = (85 + (p % 2) * 12, 90 + (p % 2) * 12, 95 + (p % 2) * 12)
            draw.rectangle([(int(w * 0.1), py1), (int(w * 0.9), py2)], fill=p_col)
            # Extruded micro-grooves
            for gy in range(py1 + 6, py2 - 4, 6):
                draw.line([(int(w * 0.1), gy), (int(w * 0.9), gy)], fill=(55, 60, 62), width=1)
                draw.line([(int(w * 0.1), gy + 1), (int(w * 0.9), gy + 1)], fill=(125, 130, 135), width=1)

    # H. Alfresco Dining, Table Settings & Finishing Touches
    if any(k in elems for k in ["long_teak_table", "stoneware_plates", "ceramic_tableware", "linen_cushions", "compact_built_in_bench", "outdoor_kitchen_island"]):
        # Teak table or built-in bench
        tbl_y1 = int(h * 0.52)
        tbl_y2 = int(h * 0.88)
        draw.rectangle([(int(w * 0.15), tbl_y1), (int(w * 0.85), tbl_y2)], fill=blend(primary, (30, 20, 15), 0.15))
        draw.line([(int(w * 0.15), tbl_y1), (int(w * 0.85), tbl_y1)], fill=blend(primary, WARM_CREAM, 0.4), width=3)
        # Teak table top slats
        for sl_x in range(int(w * 0.15), int(w * 0.85), 40):
            draw.line([(sl_x, tbl_y1), (sl_x, tbl_y2)], fill=(25, 20, 18), width=2)
            draw.line([(sl_x + 1, tbl_y1), (sl_x + 1, tbl_y2)], fill=blend(primary, WARM_CREAM, 0.25), width=1)
        # Stoneware plates / accessories
        for pl_x in [int(w * 0.3), int(w * 0.5), int(w * 0.7)]:
            draw.ellipse([(pl_x - 30, tbl_y1 + 45), (pl_x + 30, tbl_y1 + 95)], fill=(235, 230, 222), outline=(180, 175, 168), width=2)
            draw.ellipse([(pl_x - 18, tbl_y1 + 55), (pl_x + 18, tbl_y1 + 85)], fill=(245, 242, 236))
            # Linen napkin or cutlery
            draw.rectangle([(pl_x - 42, tbl_y1 + 50), (pl_x - 36, tbl_y1 + 90)], fill=(210, 205, 195))
            draw.rectangle([(pl_x + 36, tbl_y1 + 50), (pl_x + 42, tbl_y1 + 90)], fill=(210, 205, 195))

    # I. Ambient Lighting Glow & Twilight Pools of Light
    if any(k in elems for k in ["nocturne_glow", "step_riser_leds", "pendant_glow", "uplit_japanese_maple", "warm_pools_of_light", "soft_indoor_lights_spilling"]):
        # Glow overlays
        glow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(glow_layer)
        # Light centers
        lights = [
            (int(w * 0.25), int(h * 0.42), 120),
            (int(w * 0.50), int(h * 0.35), 160),
            (int(w * 0.75), int(h * 0.48), 130),
            (int(w * 0.40), int(h * 0.75), 90),
            (int(w * 0.65), int(h * 0.75), 90)
        ]
        for lx, ly, lr in lights:
            for rad in range(lr, 10, -10):
                alpha = int(35 * (1.0 - rad / float(lr)))
                g_draw.ellipse([(lx - rad, ly - rad), (lx + rad, ly + rad)], fill=(255, 215, 140, alpha))
            g_draw.ellipse([(lx - 6, ly - 6), (lx + 6, ly + 6)], fill=(255, 250, 220, 240))
        im = Image.alpha_composite(im.convert("RGBA"), glow_layer).convert("RGB")
        draw = ImageDraw.Draw(im)

    # J. Coffee Mug & Open Magazine on Deck (Newsletter)
    if "open_magazine_on_deck" in elems:
        mx, my = int(w * 0.42), int(h * 0.65)
        # Open magazine pages
        draw.rectangle([(mx - 110, my - 60), (mx, my + 60)], fill=WARM_CREAM, outline=SOFT_BORDER, width=2)
        draw.rectangle([(mx, my - 60), (mx + 110, my + 60)], fill=WARM_CREAM, outline=SOFT_BORDER, width=2)
        # Page editorial text lines
        for py in range(my - 45, my + 45, 10):
            draw.line([(mx - 95, py), (mx - 15, py)], fill=MUTED, width=2)
            draw.line([(mx + 15, py), (mx + 95, py)], fill=MUTED, width=2)
        # Ceramic mug
        mug_x, mug_y = int(w * 0.72), int(h * 0.62)
        draw.ellipse([(mug_x - 28, mug_y - 28), (mug_x + 28, mug_y + 28)], fill=(240, 238, 232), outline=(190, 185, 175), width=2)
        # Rich coffee liquid inside
        draw.ellipse([(mug_x - 20, mug_y - 20), (mug_x + 20, mug_y + 20)], fill=(75, 45, 25))

    # K. Soft Editorial Finishing & Subtle Vignette
    im = im.filter(ImageFilter.SMOOTH_MORE)
    
    # Save as WebP
    out_path = os.path.join(out_dir, cfg["filename"])
    im.save(out_path, "WEBP", quality=90, method=6)
    print(f"Generated {out_path} ({w}x{h})")

def main():
    print(f"Starting generation of {len(blog_images)} unique blog images...")
    for cfg in blog_images:
        render_image(cfg)
    print(f"Successfully generated all {len(blog_images)} blog images in {out_dir}!")

if __name__ == "__main__":
    main()
