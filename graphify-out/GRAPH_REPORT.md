# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,322 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 596 nodes · 1295 edges · 33 communities
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1733db15`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- solid
- wardrobe.py
- kit_senju.py
- render.py
- living_eyes.py
- kit_shinobi.py
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- k
- Clans
- rnd
- cel_box
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- kit_nara.py
- glyphs.py
- kit_akimichi.py
- kit_tsuchigumo.py
- kit_hatake.py
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- Garment
- anime.py
- lock
- load_clans
- main
- Piece

## God Nodes (most connected - your core abstractions)
1. `k()` - 105 edges
2. `solid()` - 69 edges
3. `fabric()` - 57 edges
4. `Shared helpers` - 34 edges
5. `cel_box()` - 27 edges
6. `stamp()` - 27 edges
7. `rnd()` - 26 edges
8. `Box` - 25 edges
9. `strip_fabric()` - 22 edges
10. `Face` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `wraps()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit_shinobi.py
- `Shared helpers` --references--> `cel_box()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `lock()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `spike()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `bangs()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (33 total, 0 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.05
Nodes (21): puff(), band(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows() (+13 more)

### Community 1 - "solid"
Cohesion: 0.18
Nodes (11): How the pieces work, belt(), collar(), pouch(), flak_vest(), tanto(), beak(), ears() (+3 more)

### Community 2 - "wardrobe.py"
Cohesion: 0.17
Nodes (15): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+7 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_shinobi.py"
Cohesion: 0.15
Nodes (6): anbu_arms(), anbu_plates(), forehead_protector(), mesh(), sandals(), wraps()

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.10
Nodes (10): back_crest(), bead_clip(), brush_pin(), brush_stroke(), part_line(), splatter(), stamp(), wave_lock() (+2 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "Shared helpers"
Cohesion: 0.14
Nodes (14): Shared helpers, body(), flaps(), footwear(), kimono_sleeves(), leg_ring(), legs(), neckline() (+6 more)

### Community 12 - "k"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 14 - "rnd"
Cohesion: 0.17
Nodes (7): quilt(), ink_clouds(), seal_script(), seal_tags(), bandage_turns(), thorn_wrap(), rnd()

### Community 15 - "cel_box"
Cohesion: 0.16
Nodes (9): braid(), cel_box(), cel_face(), curtain(), spike(), tie(), gathered_tail(), hair_tie() (+1 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.13
Nodes (9): sword_strap(), bun(), bun(), clip(), crest_patch(), hairpin(), waves(), wrap_tie() (+1 more)

### Community 17 - "stamp"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.11
Nodes (10): bangs(), back_sheet(), blunt_fringe(), ear_panels(), hakama_legs(), obi(), parted_fringe(), tabi() (+2 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.16
Nodes (7): arm_protector(), back_crest(), crest(), mesh_shirt(), net(), tuft(), protector_plate()

### Community 20 - "glyphs.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 21 - "kit_akimichi.py"
Cohesion: 0.17
Nodes (5): flick(), gourd(), lames(), shoku_disc(), snack_pouch()

### Community 22 - "kit_tsuchigumo.py"
Cohesion: 0.13
Nodes (8): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 23 - "kit_hatake.py"
Cohesion: 0.12
Nodes (9): stamp(), decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto(), crest(), bump() (+1 more)

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.10
Nodes (14): sode(), arm_bone(), arm_x(), kimono_sleeves(), roll(), arm_crest(), arm_warmers(), back_crest() (+6 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 28 - "anime.py"
Cohesion: 0.29
Nodes (4): ring_shell(), crown(), pulled_back(), scalp()

### Community 29 - "lock"
Cohesion: 0.17
Nodes (6): back_fan(), lock(), sidelocks(), hime_locks(), side_fringe(), beard()

### Community 30 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 31 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 32 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `kit_uzumaki.py` to `paint.py`, `solid`, `kit_senju.py`, `kit_shinobi.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `k`, `rnd`, `cel_box`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `kit_akimichi.py`, `kit_tsuchigumo.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `anime.py`, `lock`?**
  _High betweenness centrality (0.248) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05446853516657853 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `kit_senju.py`, `kit_shinobi.py`, `kit_kurama.py`, `Shared helpers`, `k`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `kit_akimichi.py`, `kit_tsuchigumo.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `Shared helpers` to `paint.py`, `solid`, `kit_senju.py`, `kit_shinobi.py`, `kit_kurama.py`, `k`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `kit_tsuchigumo.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._