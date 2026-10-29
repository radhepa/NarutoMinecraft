# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,520 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 598 nodes · 1314 edges · 39 communities (37 shown, 2 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 74 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1733db15`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Face
- How the pieces work
- wardrobe.py
- kit_senju.py
- render.py
- living_eyes.py
- k
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- fabric
- k
- arm_x
- rnd
- Clans
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- kit_nara.py
- stamp
- kit_akimichi.py
- solid
- kit_hatake.py
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- Box
- anime.py
- Shared helpers
- Garment
- paint.py
- cel_box
- load_clans
- main
- Piece
- forehead_protector
- curls_face
- curtain

## God Nodes (most connected - your core abstractions)
1. `k()` - 107 edges
2. `solid()` - 72 edges
3. `fabric()` - 57 edges
4. `Shared helpers` - 34 edges
5. `stamp()` - 29 edges
6. `rnd()` - 29 edges
7. `cel_box()` - 27 edges
8. `Box` - 25 edges
9. `strip_fabric()` - 24 edges
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

## Communities (39 total, 2 thin omitted)

### Community 0 - "Face"
Cohesion: 0.19
Nodes (5): button(), grid(), line(), rivets(), Face

### Community 1 - "How the pieces work"
Cohesion: 0.20
Nodes (6): How the pieces work, collar(), mesh(), tanto(), beak(), ears()

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
Cohesion: 0.15
Nodes (11): belt(), flaps(), footwear(), sword_strap(), legs(), neckline(), pouch(), side_panels() (+3 more)

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): spike(), burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "fabric"
Cohesion: 0.15
Nodes (11): body(), kimono_sleeves(), anbu_arms(), anbu_plates(), flak_vest(), sandals(), sleeves(), shirt() (+3 more)

### Community 12 - "k"
Cohesion: 0.22
Nodes (3): high_collar(), hood_down(), lenses()

### Community 13 - "arm_x"
Cohesion: 0.21
Nodes (7): sode(), arm_bone(), arm_x(), kimono_sleeves(), roll(), arm_warmers(), wide_sleeves()

### Community 14 - "rnd"
Cohesion: 0.14
Nodes (9): fur_edge(), ink_stains(), seal_trim(), cloth_shade(), hair_box(), hair_face(), hair_shade(), rnd() (+1 more)

### Community 15 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.12
Nodes (8): bun(), clip(), crest_patch(), hairpin(), seal_script(), seal_tags(), waves(), wrap_tie()

### Community 17 - "stamp"
Cohesion: 0.13
Nodes (8): beard(), crest(), crest_patch(), flame_hem(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.12
Nodes (9): bangs(), blunt_fringe(), hakama_legs(), obi(), parted_fringe(), tabi(), wrap_front(), leg_bone() (+1 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "stamp"
Cohesion: 0.13
Nodes (8): stamp(), crescent(), hip_katana(), katana(), crest(), guardian_sash(), bump(), plate()

### Community 21 - "kit_akimichi.py"
Cohesion: 0.17
Nodes (5): gourd(), lames(), quilt(), shoku_disc(), snack_pouch()

### Community 22 - "solid"
Cohesion: 0.16
Nodes (8): deep_hood(), bandolier(), coat_skirts(), cross_armband(), scroll_tube(), strap(), strap(), solid()

### Community 23 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 28 - "anime.py"
Cohesion: 0.22
Nodes (5): cel_face(), ring_shell(), crown(), pulled_back(), scalp()

### Community 29 - "Shared helpers"
Cohesion: 0.20
Nodes (7): Shared helpers, back_fan(), braid(), lock(), sidelocks(), hime_locks(), wraps()

### Community 30 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 31 - "paint.py"
Cohesion: 0.19
Nodes (6): band(), dark_seams(), darken_rows(), hem(), strip_line(), shade()

### Community 32 - "cel_box"
Cohesion: 0.20
Nodes (7): cel_box(), tie(), flick(), ear_panels(), gathered_tail(), hair_tie(), pineapple()

### Community 33 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 34 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 35 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 36 - "forehead_protector"
Cohesion: 0.33
Nodes (3): arm_protector(), forehead_protector(), protector_plate()

### Community 37 - "curls_face"
Cohesion: 0.40
Nodes (3): puff(), curls_box(), curls_face()

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `Face`, `How the pieces work`, `kit_senju.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `fabric`, `k`, `arm_x`, `rnd`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `stamp`, `kit_akimichi.py`, `solid`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `anime.py`, `Shared helpers`, `paint.py`, `cel_box`, `forehead_protector`, `curls_face`?**
  _High betweenness centrality (0.246) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `How the pieces work`, `kit_senju.py`, `k`, `kit_kurama.py`, `fabric`, `k`, `arm_x`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `stamp`, `kit_akimichi.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `Box`, `Shared helpers`, `paint.py`, `forehead_protector`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `kit_kurama.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07692307692307693 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `Face`, `How the pieces work`, `kit_senju.py`, `k`, `kit_kurama.py`, `k`, `arm_x`, `rnd`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `stamp`, `solid`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `Shared helpers`, `paint.py`, `forehead_protector`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._