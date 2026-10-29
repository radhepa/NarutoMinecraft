# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 27 files · ~31,181 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 559 nodes · 1223 edges · 31 communities (29 shown, 2 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 73 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `164d6ce9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Face
- solid
- wardrobe.py
- cel_box
- render.py
- living_eyes.py
- Box
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- k
- kit_uchiha.py
- paint.py
- Garment
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- kit_nara.py
- glyphs.py
- fabric
- main
- kit_hatake.py
- kit_shimura.py
- crest
- kit_yamanaka.py
- Piece
- scalp
- clan_resident
- curls_face

## God Nodes (most connected - your core abstractions)
1. `k()` - 103 edges
2. `solid()` - 66 edges
3. `fabric()` - 55 edges
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

## Communities (31 total, 2 thin omitted)

### Community 0 - "Face"
Cohesion: 0.19
Nodes (6): button(), darken_rows(), grid(), line(), rivets(), Face

### Community 1 - "solid"
Cohesion: 0.12
Nodes (15): How the pieces work, belt(), collar(), pouch(), anbu_arms(), anbu_plates(), flak_vest(), forehead_protector() (+7 more)

### Community 2 - "wardrobe.py"
Cohesion: 0.17
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_clans(), load_eye_colors(), load_hair_colors(), load_marks() (+8 more)

### Community 3 - "cel_box"
Cohesion: 0.05
Nodes (23): braid(), cel_box(), curtain(), tie(), flick(), gourd(), lames(), puff() (+15 more)

### Community 4 - "render.py"
Cohesion: 0.14
Nodes (16): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), ground_shadow() (+8 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "Box"
Cohesion: 0.11
Nodes (3): strip_line(), Box, Layer

### Community 7 - "Clans"
Cohesion: 0.11
Nodes (15): Clans, Commands, Mix and match, Piece ids, Reference images, The clan file, Commits, graphify (+7 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.05
Nodes (20): back_fan(), bangs(), lock(), sidelocks(), blunt_fringe(), hime_locks(), parted_fringe(), back_crest() (+12 more)

### Community 9 - "rnd"
Cohesion: 0.10
Nodes (12): cel_face(), ring_shell(), spike(), burst(), claw_marks(), fang(), fang_small(), fur_box() (+4 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "Shared helpers"
Cohesion: 0.13
Nodes (13): Shared helpers, body(), flaps(), footwear(), leg_ring(), legs(), neckline(), sandals() (+5 more)

### Community 12 - "k"
Cohesion: 0.10
Nodes (11): deep_hood(), high_collar(), hood_down(), lenses(), snack_pouch(), face_mask(), brush_pin(), pauldron() (+3 more)

### Community 13 - "kit_uchiha.py"
Cohesion: 0.14
Nodes (9): sode(), arm_bone(), arm_x(), kimono_sleeves(), roll(), arm_warmers(), high_collar(), lamellar() (+1 more)

### Community 14 - "paint.py"
Cohesion: 0.13
Nodes (9): band(), cloth_shade(), dark_seams(), hair_box(), hair_face(), hair_shade(), hem(), shell() (+1 more)

### Community 15 - "Garment"
Cohesion: 0.22
Nodes (4): compatible(), Garment, key_rgba(), png_bytes()

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.15
Nodes (6): clip(), hairpin(), seal_script(), seal_tags(), waves(), wrap_tie()

### Community 17 - "stamp"
Cohesion: 0.21
Nodes (7): stamp(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), crest_patch()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.17
Nodes (6): hakama_legs(), kimono_sleeves(), obi(), tabi(), wrap_front(), leg_bone()

### Community 19 - "kit_nara.py"
Cohesion: 0.19
Nodes (6): arm_protector(), back_crest(), crest(), mesh_shirt(), net(), protector_plate()

### Community 20 - "glyphs.py"
Cohesion: 0.18
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 21 - "fabric"
Cohesion: 0.22
Nodes (5): crest(), beak(), bump(), plate(), fabric()

### Community 22 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 23 - "kit_hatake.py"
Cohesion: 0.20
Nodes (4): decal(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "crest"
Cohesion: 0.20
Nodes (5): arm_crest(), back_crest(), chest_crest(), crest(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 28 - "scalp"
Cohesion: 0.33
Nodes (3): crown(), pulled_back(), scalp()

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `Face`, `solid`, `cel_box`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `kit_uchiha.py`, `paint.py`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`, `kit_yamanaka.py`, `scalp`, `curls_face`?**
  _High betweenness centrality (0.259) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `solid` be split into smaller, more focused modules?**
  _Cohesion score 0.11692307692307692 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `cel_box`, `Box`, `kit_kurama.py`, `Shared helpers`, `k`, `kit_uchiha.py`, `paint.py`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `cel_box` be split into smaller, more focused modules?**
  _Cohesion score 0.04875886524822695 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `Face`, `solid`, `cel_box`, `kit_kurama.py`, `Shared helpers`, `k`, `kit_uchiha.py`, `paint.py`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `kit_hatake.py`, `kit_shimura.py`, `crest`, `kit_yamanaka.py`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._