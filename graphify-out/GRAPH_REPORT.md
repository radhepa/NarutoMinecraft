# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,798 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 614 nodes · 1348 edges · 36 communities (30 shown, 6 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1733db15`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- kit_shinobi.py
- wardrobe.py
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- k
- kit_uzumaki.py
- bandage_turns
- kit_shimura.py
- k
- stamp
- kit_hyuga.py
- kit_nara.py
- Clans
- fabric
- Garment
- load_clans
- main
- kit_uchiha.py
- kit_yamanaka.py
- anime.py
- anime.py
- Piece
- cel_box
- curtain
- hairpin
- mist_swirls
- thorn_vine
- thorn_band

## God Nodes (most connected - your core abstractions)
1. `k()` - 114 edges
2. `solid()` - 75 edges
3. `fabric()` - 61 edges
4. `Shared helpers` - 34 edges
5. `stamp()` - 29 edges
6. `cel_box()` - 27 edges
7. `rnd()` - 26 edges
8. `strip_fabric()` - 26 edges
9. `Box` - 25 edges
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

## Communities (36 total, 6 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.05
Nodes (23): puff(), band(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows() (+15 more)

### Community 1 - "kit_shinobi.py"
Cohesion: 0.12
Nodes (8): arm_protector(), anbu_arms(), anbu_plates(), forehead_protector(), mesh(), protector_plate(), tanto(), wraps()

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

### Community 6 - "solid"
Cohesion: 0.10
Nodes (16): drawstrings(), holster(), hood_down(), sash(), shirt(), side_stripe(), stripes(), turned_hem() (+8 more)

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
Cohesion: 0.17
Nodes (7): rose(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock(), wave_shell()

### Community 11 - "Shared helpers"
Cohesion: 0.11
Nodes (14): Shared helpers, belt(), body(), flaps(), footwear(), tabi(), leg_ring(), legs() (+6 more)

### Community 12 - "k"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_uzumaki.py"
Cohesion: 0.09
Nodes (13): sleeve_roll(), gourd(), lames(), sode(), arm_bone(), arm_x(), kimono_sleeves(), kimono_sleeves() (+5 more)

### Community 15 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): forearm_wraps(), bandaged_arm(), cane(), bandage()

### Community 16 - "k"
Cohesion: 0.09
Nodes (12): ribbed(), shin_wraps(), quilt(), snack_pouch(), obi(), wrap_front(), stockings(), bun() (+4 more)

### Community 17 - "stamp"
Cohesion: 0.05
Nodes (23): stamp(), back_crest(), shoku_disc(), crescent(), hip_katana(), katana(), sword_strap(), decal() (+15 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.21
Nodes (6): bangs(), tie(), blunt_fringe(), gathered_tail(), hair_tie(), parted_fringe()

### Community 19 - "kit_nara.py"
Cohesion: 0.16
Nodes (7): spike(), back_crest(), crest(), mesh_shirt(), net(), pineapple(), tuft()

### Community 20 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 21 - "fabric"
Cohesion: 0.15
Nodes (10): How the pieces work, leg_cloth(), waist(), collar(), beak(), bump(), ears(), plate() (+2 more)

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 24 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "anime.py"
Cohesion: 0.24
Nodes (4): back_fan(), lock(), sidelocks(), hime_locks()

### Community 28 - "anime.py"
Cohesion: 0.25
Nodes (4): cel_face(), ring_shell(), crown(), pulled_back()

### Community 29 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 30 - "cel_box"
Cohesion: 0.22
Nodes (5): braid(), cel_box(), flick(), ear_panels(), beard()

## Knowledge Gaps
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `kit_shinobi.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `k`, `kit_uzumaki.py`, `bandage_turns`, `kit_shimura.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `fabric`, `kit_uchiha.py`, `kit_yamanaka.py`, `anime.py`, `anime.py`, `cel_box`, `hairpin`, `mist_swirls`, `thorn_vine`, `thorn_band`?**
  _High betweenness centrality (0.260) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05432692307692308 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `hairpin`, `kit_shinobi.py`, `paint.py`, `kit_senju.py`, `kit_kurama.py`, `Shared helpers`, `k`, `kit_uzumaki.py`, `kit_shimura.py`, `k`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `fabric`, `kit_uchiha.py`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `kit_shinobi.py` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `paint.py`, `kit_shinobi.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `Shared helpers`, `k`, `kit_uzumaki.py`, `kit_shimura.py`, `k`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `kit_uchiha.py`, `kit_yamanaka.py`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._