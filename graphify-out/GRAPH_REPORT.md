# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,302 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 600 nodes · 1313 edges · 37 communities (33 shown, 4 thin omitted)
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
- k
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Clans
- k
- arm_x
- bandage_turns
- Garment
- kit_uzumaki.py
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
- lock
- anime.py
- kit_umino.py
- Piece
- anime.py
- kit_akimichi.py
- bangs
- fur_face
- thorn_band
- rose

## God Nodes (most connected - your core abstractions)
1. `k()` - 105 edges
2. `solid()` - 68 edges
3. `fabric()` - 57 edges
4. `Shared helpers` - 34 edges
5. `stamp()` - 30 edges
6. `cel_box()` - 29 edges
7. `rnd()` - 26 edges
8. `Box` - 25 edges
9. `strip_fabric()` - 22 edges
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

## Communities (37 total, 4 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.06
Nodes (21): band(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows(), grid() (+13 more)

### Community 1 - "solid"
Cohesion: 0.05
Nodes (41): Shared helpers, How the pieces work, deep_hood(), belt(), body(), collar(), flaps(), footwear() (+33 more)

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

### Community 6 - "k"
Cohesion: 0.10
Nodes (11): lames(), snack_pouch(), obi(), tabi(), wrap_front(), fur_edge(), bead_clip(), bun() (+3 more)

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.10
Nodes (10): back_crest(), brush_pin(), brush_stroke(), ink_clouds(), side_fringe(), splatter(), stamp(), wave_lock() (+2 more)

### Community 9 - "rnd"
Cohesion: 0.15
Nodes (6): spike(), burst(), claw_marks(), fang(), fang_small(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.15
Nodes (8): mist_swirls(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock(), wave_shell()

### Community 11 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 12 - "k"
Cohesion: 0.22
Nodes (3): high_collar(), hood_down(), lenses()

### Community 13 - "arm_x"
Cohesion: 0.21
Nodes (7): sode(), arm_bone(), arm_x(), kimono_sleeves(), roll(), arm_warmers(), wide_sleeves()

### Community 15 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.12
Nodes (8): bun(), clip(), crest_patch(), hairpin(), seal_script(), seal_tags(), waves(), wrap_tie()

### Community 17 - "stamp"
Cohesion: 0.15
Nodes (7): crest(), crest_patch(), flame_hem(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.15
Nodes (10): cel_box(), curtain(), tie(), flick(), back_sheet(), ear_panels(), gathered_tail(), hair_tie() (+2 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "glyphs.py"
Cohesion: 0.18
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 21 - "stamp"
Cohesion: 0.18
Nodes (6): stamp(), shoku_disc(), crest(), guardian_sash(), dolphin(), wave_band()

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
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "lock"
Cohesion: 0.20
Nodes (5): back_fan(), lock(), hime_locks(), beard(), falling_tail()

### Community 28 - "anime.py"
Cohesion: 0.24
Nodes (5): ring_shell(), crown(), pulled_back(), combed_up(), scalp()

### Community 29 - "kit_umino.py"
Cohesion: 0.20
Nodes (4): brush_tail(), scroll(), surf(), waves()

### Community 30 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 31 - "anime.py"
Cohesion: 0.25
Nodes (3): braid(), cel_face(), sidelocks()

### Community 32 - "kit_akimichi.py"
Cohesion: 0.25
Nodes (3): gourd(), puff(), quilt()

### Community 33 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `solid`, `kit_senju.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `k`, `arm_x`, `bandage_turns`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `kit_hatake.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `lock`, `anime.py`, `kit_umino.py`, `anime.py`, `kit_akimichi.py`, `fur_face`, `thorn_band`, `rose`?**
  _High betweenness centrality (0.244) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.058469945355191254 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `kit_akimichi.py`, `paint.py`, `kit_senju.py`, `k`, `kit_kurama.py`, `k`, `arm_x`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `kit_hatake.py`, `kit_uchiha.py`, `kit_umino.py`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `solid` be split into smaller, more focused modules?**
  _Cohesion score 0.053554040895813046 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `solid` to `paint.py`, `kit_senju.py`, `k`, `kit_kurama.py`, `k`, `arm_x`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `kit_hatake.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `kit_umino.py`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._