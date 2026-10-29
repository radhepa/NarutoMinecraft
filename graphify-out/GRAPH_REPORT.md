# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,628 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 604 nodes · 1324 edges · 30 communities (29 shown, 1 thin omitted)
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
- cel_box
- render.py
- living_eyes.py
- kit_kunoichi.py
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- Clans
- Shared helpers
- kit_akimichi.py
- Garment
- k
- stamp
- kit_hyuga.py
- kit_nara.py
- glyphs.py
- stamp
- load_clans
- kit_hatake.py
- main
- kit_uchiha.py
- kit_yamanaka.py
- Piece
- anime.py
- curtain

## God Nodes (most connected - your core abstractions)
1. `k()` - 111 edges
2. `solid()` - 71 edges
3. `fabric()` - 57 edges
4. `Shared helpers` - 34 edges
5. `cel_box()` - 30 edges
6. `stamp()` - 27 edges
7. `rnd()` - 26 edges
8. `strip_fabric()` - 25 edges
9. `Box` - 25 edges
10. `Face` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `cel_box()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `spike()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `bangs()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `ring_shell()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `curtain()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (30 total, 1 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.06
Nodes (20): band(), button(), cloth_shade(), curls_face(), dark_seams(), darken_rows(), grid(), hair_box() (+12 more)

### Community 1 - "solid"
Cohesion: 0.08
Nodes (18): How the pieces work, belt(), obi(), obi(), arm_protector(), pouch(), plate(), cane() (+10 more)

### Community 2 - "wardrobe.py"
Cohesion: 0.17
Nodes (15): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+7 more)

### Community 3 - "cel_box"
Cohesion: 0.16
Nodes (6): cel_box(), ear_panels(), bun(), lames(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (11): hakama_legs(), arm_warmers(), frog_buttons(), mandarin_collar(), round_bun(), shin_wrap(), thigh_holster(), wave_lock() (+3 more)

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "Shared helpers"
Cohesion: 0.16
Nodes (11): body(), collar(), footwear(), kimono_sleeves(), tabi_boots(), legs(), anbu_arms(), sleeves() (+3 more)

### Community 12 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 13 - "Shared helpers"
Cohesion: 0.14
Nodes (9): Shared helpers, back_fan(), braid(), cel_face(), lock(), sidelocks(), hime_locks(), beard() (+1 more)

### Community 14 - "kit_akimichi.py"
Cohesion: 0.12
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box()

### Community 15 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 16 - "k"
Cohesion: 0.08
Nodes (15): deep_hood(), high_collar(), hood_down(), lenses(), flaps(), tabi(), neckline(), stockings() (+7 more)

### Community 17 - "stamp"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.17
Nodes (7): bangs(), tie(), blunt_fringe(), gathered_tail(), hair_tie(), parted_fringe(), wrap_front()

### Community 19 - "kit_nara.py"
Cohesion: 0.16
Nodes (7): spike(), back_crest(), crest(), mesh_shirt(), net(), pineapple(), tuft()

### Community 20 - "glyphs.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 21 - "stamp"
Cohesion: 0.11
Nodes (10): stamp(), crest(), back_crest(), bandaged_arm(), bandage(), forehead_protector(), protector_plate(), sandals() (+2 more)

### Community 22 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 23 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 24 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.08
Nodes (17): sode(), arm_bone(), arm_x(), kimono_sleeves(), kimono_sleeves(), roll(), arm_crest(), arm_warmers() (+9 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 28 - "anime.py"
Cohesion: 0.29
Nodes (4): ring_shell(), crown(), pulled_back(), scalp()

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `solid`, `cel_box`, `kit_kunoichi.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `Shared helpers`, `kit_akimichi.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `kit_hatake.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `anime.py`?**
  _High betweenness centrality (0.259) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05875706214689266 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `cel_box`, `kit_kunoichi.py`, `kit_kurama.py`, `Shared helpers`, `Shared helpers`, `kit_akimichi.py`, `k`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `kit_hatake.py`, `kit_uchiha.py`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `solid` be split into smaller, more focused modules?**
  _Cohesion score 0.08172043010752689 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `Shared helpers` to `paint.py`, `solid`, `cel_box`, `kit_kunoichi.py`, `kit_kurama.py`, `Shared helpers`, `k`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `kit_hatake.py`, `kit_uchiha.py`, `kit_yamanaka.py`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._