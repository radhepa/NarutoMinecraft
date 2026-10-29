# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~34,089 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 614 nodes · 1345 edges · 32 communities (31 shown, 1 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 72 edges (avg confidence: 0.93)
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
- Shared helpers
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- k
- fabric
- bandage_turns
- kit_field.py
- Clans
- stamp
- kit_hyuga.py
- kit_nara.py
- anime.py
- kit_akimichi.py
- k
- Garment
- load_clans
- kit_uzumaki.py
- kit_yamanaka.py
- main
- anime.py
- Piece
- bangs
- spike

## God Nodes (most connected - your core abstractions)
1. `k()` - 115 edges
2. `solid()` - 74 edges
3. `fabric()` - 60 edges
4. `Shared helpers` - 33 edges
5. `strip_fabric()` - 28 edges
6. `cel_box()` - 27 edges
7. `stamp()` - 27 edges
8. `rnd()` - 26 edges
9. `Box` - 25 edges
10. `Face` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `cel_box()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `lock()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `spike()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `bangs()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `sidelocks()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (32 total, 1 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.06
Nodes (21): band(), button(), cloth_shade(), curls_face(), dark_seams(), darken_rows(), grid(), hair_box() (+13 more)

### Community 1 - "solid"
Cohesion: 0.17
Nodes (9): How the pieces work, belt(), roll(), tanto(), beak(), bump(), ears(), strap() (+1 more)

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

### Community 6 - "Shared helpers"
Cohesion: 0.14
Nodes (9): Shared helpers, flaps(), neckline(), bandaged_arm(), bandage(), flak_vest(), mesh(), sandals() (+1 more)

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.15
Nodes (6): claw_marks(), fang(), fang_small(), fur_box(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.15
Nodes (8): rose(), thorn_band(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock(), wave_shell()

### Community 11 - "Shared helpers"
Cohesion: 0.14
Nodes (11): body(), vest(), footwear(), legs(), pouch(), anbu_plates(), side_panels(), sleeves() (+3 more)

### Community 12 - "k"
Cohesion: 0.22
Nodes (3): high_collar(), hood_down(), lenses()

### Community 13 - "fabric"
Cohesion: 0.12
Nodes (10): deep_hood(), collar(), half_sleeves(), kimono_sleeves(), arm_protector(), anbu_arms(), forehead_protector(), protector_plate() (+2 more)

### Community 15 - "kit_field.py"
Cohesion: 0.07
Nodes (16): blouse(), cargo(), chain(), collar(), gloves(), holster(), knee_guards(), mesh_arms() (+8 more)

### Community 16 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 17 - "stamp"
Cohesion: 0.05
Nodes (22): stamp(), crescent(), hip_katana(), katana(), sword_strap(), decal(), face_mask(), shoulder_decal() (+14 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.22
Nodes (7): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie()

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "anime.py"
Cohesion: 0.16
Nodes (6): back_fan(), braid(), lock(), sidelocks(), hime_locks(), beard()

### Community 21 - "kit_akimichi.py"
Cohesion: 0.12
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box()

### Community 22 - "k"
Cohesion: 0.14
Nodes (8): obi(), tabi(), wrap_front(), fur_edge(), stockings(), mist_swirls(), thorn_vine(), k()

### Community 23 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 24 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 25 - "kit_uzumaki.py"
Cohesion: 0.06
Nodes (21): sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), arm_crest(), arm_warmers(), back_crest() (+13 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 28 - "anime.py"
Cohesion: 0.25
Nodes (4): cel_face(), ring_shell(), crown(), pulled_back()

### Community 29 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 30 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

### Community 31 - "spike"
Cohesion: 0.33
Nodes (3): spike(), burst(), pineapple()

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `solid`, `kit_senju.py`, `Shared helpers`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `k`, `fabric`, `bandage_turns`, `kit_field.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `anime.py`, `kit_akimichi.py`, `kit_uzumaki.py`, `kit_yamanaka.py`, `anime.py`?**
  _High betweenness centrality (0.264) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05711263881544157 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `kit_senju.py`, `Shared helpers`, `kit_kurama.py`, `Shared helpers`, `k`, `fabric`, `kit_field.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `kit_akimichi.py`, `k`, `kit_uzumaki.py`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `paint.py`, `solid`, `kit_senju.py`, `Shared helpers`, `kit_kurama.py`, `Shared helpers`, `k`, `kit_field.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `k`, `kit_uzumaki.py`, `kit_yamanaka.py`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._