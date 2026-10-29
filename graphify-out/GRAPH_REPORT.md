# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,438 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 598 nodes · 1311 edges · 44 communities (35 shown, 9 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `cd6bced7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- solid
- wardrobe.py
- kit_senju.py
- render.py
- living_eyes.py
- kit.py
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- k
- arm_x
- bandage_turns
- Clans
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- kit_nara.py
- stamp
- k
- kit_shinobi.py
- kit_hatake.py
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- Garment
- anime.py
- Shared helpers
- kit_shiranui.py
- load_clans
- main
- Piece
- lock
- bangs
- kit_akimichi.py
- fur_face
- tabi
- fur_edge
- neckline
- thorn_vine
- thorn_band
- rose

## God Nodes (most connected - your core abstractions)
1. `k()` - 108 edges
2. `solid()` - 70 edges
3. `fabric()` - 58 edges
4. `Shared helpers` - 34 edges
5. `stamp()` - 29 edges
6. `cel_box()` - 27 edges
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
- `Shared helpers` --references--> `ring_shell()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (44 total, 9 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.06
Nodes (21): band(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows(), grid() (+13 more)

### Community 1 - "solid"
Cohesion: 0.20
Nodes (10): How the pieces work, collar(), pouch(), flak_vest(), tanto(), beak(), ears(), strap() (+2 more)

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

### Community 6 - "kit.py"
Cohesion: 0.18
Nodes (6): belt(), flaps(), hakama_legs(), leg_bone(), leg_ring(), side_panels()

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.15
Nodes (6): spike(), burst(), claw_marks(), fang(), fang_small(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.17
Nodes (7): mist_swirls(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock(), wave_shell()

### Community 11 - "Shared helpers"
Cohesion: 0.15
Nodes (10): deep_hood(), body(), footwear(), kimono_sleeves(), legs(), anbu_arms(), sleeves(), waistband() (+2 more)

### Community 12 - "k"
Cohesion: 0.22
Nodes (3): high_collar(), hood_down(), lenses()

### Community 13 - "arm_x"
Cohesion: 0.24
Nodes (6): sode(), arm_bone(), arm_x(), kimono_sleeves(), roll(), arm_warmers()

### Community 15 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.14
Nodes (7): bun(), crest_patch(), hairpin(), seal_script(), seal_tags(), waves(), wide_sleeves()

### Community 17 - "stamp"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.16
Nodes (9): cel_box(), curtain(), tie(), flick(), back_sheet(), ear_panels(), gathered_tail(), hair_tie() (+1 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "stamp"
Cohesion: 0.15
Nodes (7): stamp(), crescent(), hip_katana(), katana(), crest(), bump(), plate()

### Community 21 - "k"
Cohesion: 0.08
Nodes (13): lames(), quilt(), shoku_disc(), snack_pouch(), sword_strap(), obi(), wrap_front(), bandolier() (+5 more)

### Community 22 - "kit_shinobi.py"
Cohesion: 0.13
Nodes (7): arm_protector(), anbu_plates(), forehead_protector(), mesh(), protector_plate(), sandals(), backward_bandana()

### Community 23 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.19
Nodes (6): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 28 - "anime.py"
Cohesion: 0.29
Nodes (4): ring_shell(), crown(), pulled_back(), scalp()

### Community 29 - "Shared helpers"
Cohesion: 0.20
Nodes (6): Shared helpers, back_fan(), braid(), cel_face(), sidelocks(), wraps()

### Community 30 - "kit_shiranui.py"
Cohesion: 0.21
Nodes (5): crest(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 31 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 32 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 33 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 34 - "lock"
Cohesion: 0.25
Nodes (4): lock(), hime_locks(), beard(), flicks()

### Community 35 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

## Knowledge Gaps
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `solid`, `kit_senju.py`, `kit.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `k`, `arm_x`, `bandage_turns`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `stamp`, `kit_shinobi.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `anime.py`, `Shared helpers`, `kit_shiranui.py`, `lock`, `kit_akimichi.py`, `fur_face`, `tabi`, `fur_edge`, `neckline`, `thorn_vine`, `thorn_band`, `rose`?**
  _High betweenness centrality (0.253) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.058469945355191254 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `kit_senju.py`, `kit.py`, `kit_kurama.py`, `Shared helpers`, `k`, `arm_x`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `stamp`, `k`, `kit_shinobi.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `Shared helpers`, `kit_shiranui.py`, `kit_akimichi.py`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `Shared helpers` to `paint.py`, `solid`, `kit_senju.py`, `kit.py`, `kit_kurama.py`, `k`, `arm_x`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `stamp`, `k`, `kit_shinobi.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `Shared helpers`, `kit_shiranui.py`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._