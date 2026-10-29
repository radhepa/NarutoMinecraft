# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,215 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 594 nodes · 1308 edges · 36 communities (32 shown, 4 thin omitted)
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
- fabric
- bandage_turns
- Clans
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- kit_nara.py
- k
- anime.py
- Garment
- stamp
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- load_clans
- anime.py
- main
- Piece
- rnd
- bangs
- hairpin
- mist_swirls
- rose

## God Nodes (most connected - your core abstractions)
1. `k()` - 107 edges
2. `solid()` - 71 edges
3. `fabric()` - 58 edges
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

## Communities (36 total, 4 thin omitted)

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
Nodes (4): bun(), lames(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_shinobi.py"
Cohesion: 0.22
Nodes (4): anbu_arms(), anbu_plates(), mesh(), wraps()

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.11
Nodes (9): spike(), burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face() (+1 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.15
Nodes (8): thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock(), wave_shell()

### Community 11 - "Shared helpers"
Cohesion: 0.11
Nodes (15): Shared helpers, body(), flaps(), footwear(), hakama_legs(), leg_bone(), leg_ring(), legs() (+7 more)

### Community 12 - "k"
Cohesion: 0.22
Nodes (3): high_collar(), hood_down(), lenses()

### Community 13 - "fabric"
Cohesion: 0.14
Nodes (8): deep_hood(), crest(), kimono_sleeves(), arm_protector(), plate(), forehead_protector(), protector_plate(), fabric()

### Community 15 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.22
Nodes (4): bun(), crest_patch(), seal_script(), seal_tags()

### Community 17 - "stamp"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.19
Nodes (8): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), pineapple()

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "k"
Cohesion: 0.10
Nodes (11): lames(), shoku_disc(), snack_pouch(), sword_strap(), obi(), tabi(), wrap_front(), clip() (+3 more)

### Community 21 - "anime.py"
Cohesion: 0.16
Nodes (6): back_fan(), braid(), lock(), sidelocks(), hime_locks(), beard()

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "stamp"
Cohesion: 0.10
Nodes (11): stamp(), crescent(), hip_katana(), katana(), decal(), face_mask(), shoulder_decal(), slanted_protector() (+3 more)

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.07
Nodes (20): sode(), arm_bone(), arm_x(), bracers(), crown(), harness(), mace(), plate() (+12 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 28 - "anime.py"
Cohesion: 0.22
Nodes (5): cel_face(), ring_shell(), crown(), pulled_back(), scalp()

### Community 29 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 30 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 31 - "rnd"
Cohesion: 0.25
Nodes (4): flick(), gourd(), quilt(), rnd()

### Community 32 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `solid`, `kit_senju.py`, `kit_shinobi.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `k`, `fabric`, `bandage_turns`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `anime.py`, `stamp`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `anime.py`, `rnd`, `hairpin`, `mist_swirls`, `rose`?**
  _High betweenness centrality (0.248) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05446853516657853 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `hairpin`, `kit_senju.py`, `kit_shinobi.py`, `kit_kurama.py`, `Shared helpers`, `k`, `fabric`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `k`, `stamp`, `kit_shimura.py`, `kit_uchiha.py`, `rnd`?**
  _High betweenness centrality (0.141) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `paint.py`, `solid`, `kit_senju.py`, `kit_shinobi.py`, `kit_kurama.py`, `Shared helpers`, `k`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `k`, `stamp`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`?**
  _High betweenness centrality (0.102) - this node is a cross-community bridge._