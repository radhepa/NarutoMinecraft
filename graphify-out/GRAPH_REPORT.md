# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,922 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 603 nodes · 1322 edges · 30 communities (29 shown, 1 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1733db15`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- How the pieces work
- wardrobe.py
- cel_box
- render.py
- living_eyes.py
- Shared helpers
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- k
- solid
- fabric
- kit_akimichi.py
- strip_fabric
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- kit_nara.py
- stamp
- Clans
- Garment
- load_clans
- kit_shimura.py
- main
- kit_yamanaka.py
- Piece
- hood_down
- curtain

## God Nodes (most connected - your core abstractions)
1. `k()` - 113 edges
2. `solid()` - 72 edges
3. `fabric()` - 58 edges
4. `Shared helpers` - 34 edges
5. `stamp()` - 30 edges
6. `cel_box()` - 27 edges
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
Nodes (21): fur_edge(), band(), button(), cloth_shade(), curls_face(), dark_seams(), darken_rows(), grid() (+13 more)

### Community 1 - "How the pieces work"
Cohesion: 0.20
Nodes (6): How the pieces work, mesh(), tanto(), beak(), ears(), strap()

### Community 2 - "wardrobe.py"
Cohesion: 0.17
Nodes (15): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+7 more)

### Community 3 - "cel_box"
Cohesion: 0.14
Nodes (7): braid(), cel_box(), cel_face(), ear_panels(), bun(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "Shared helpers"
Cohesion: 0.16
Nodes (8): Shared helpers, back_fan(), lock(), sidelocks(), hime_locks(), leg_ring(), beard(), wraps()

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.11
Nodes (9): spike(), burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_face(), paw() (+1 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "k"
Cohesion: 0.14
Nodes (12): belt(), collar(), flaps(), footwear(), legs(), neckline(), pouch(), lames() (+4 more)

### Community 12 - "solid"
Cohesion: 0.09
Nodes (12): deep_hood(), high_collar(), hood_down(), lenses(), face_mask(), white_fang_tanto(), obi(), kimono_sleeves() (+4 more)

### Community 13 - "fabric"
Cohesion: 0.12
Nodes (9): body(), crest(), kimono_sleeves(), arm_protector(), forehead_protector(), protector_plate(), sleeves(), lantern() (+1 more)

### Community 14 - "kit_akimichi.py"
Cohesion: 0.12
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box()

### Community 15 - "strip_fabric"
Cohesion: 0.13
Nodes (10): tabi(), anbu_arms(), anbu_plates(), flak_vest(), sandals(), plain_body(), shin_wraps(), split_toe_boots() (+2 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.06
Nodes (21): sode(), arm_bone(), arm_x(), roll(), arm_crest(), arm_warmers(), back_crest(), chest_crest() (+13 more)

### Community 17 - "stamp"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.14
Nodes (9): bangs(), tie(), blunt_fringe(), gathered_tail(), hair_tie(), hakama_legs(), parted_fringe(), wrap_front() (+1 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.13
Nodes (9): ring_shell(), crown(), back_crest(), crest(), mesh_shirt(), net(), pulled_back(), tuft() (+1 more)

### Community 20 - "stamp"
Cohesion: 0.09
Nodes (12): stamp(), crescent(), hip_katana(), katana(), sword_strap(), decal(), shoulder_decal(), slanted_protector() (+4 more)

### Community 21 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 28 - "hood_down"
Cohesion: 0.33
Nodes (3): hood_down(), mantle(), pleats()

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `cel_box`, `Shared helpers`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `solid`, `fabric`, `kit_akimichi.py`, `strip_fabric`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `stamp`, `kit_shimura.py`, `kit_yamanaka.py`, `hood_down`?**
  _High betweenness centrality (0.265) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05605499735589635 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `How the pieces work`, `cel_box`, `Shared helpers`, `kit_kurama.py`, `k`, `fabric`, `kit_akimichi.py`, `strip_fabric`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `stamp`, `kit_shimura.py`, `hood_down`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `cel_box` be split into smaller, more focused modules?**
  _Cohesion score 0.1437908496732026 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `paint.py`, `How the pieces work`, `cel_box`, `Shared helpers`, `kit_kurama.py`, `k`, `solid`, `strip_fabric`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `stamp`, `kit_shimura.py`, `kit_yamanaka.py`, `hood_down`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._