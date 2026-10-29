# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~34,015 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 608 nodes · 1330 edges · 33 communities (32 shown, 1 thin omitted)
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
- arm_x
- kit_akimichi.py
- kit_kinoshita.py
- k
- stamp
- Shared helpers
- Clans
- glyphs.py
- fabric
- Garment
- kit_hatake.py
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- load_clans
- main
- Piece
- kit_shinobi.py
- wide_sleeves
- tool_belt

## God Nodes (most connected - your core abstractions)
1. `k()` - 109 edges
2. `solid()` - 74 edges
3. `fabric()` - 59 edges
4. `Shared helpers` - 34 edges
5. `stamp()` - 29 edges
6. `rnd()` - 28 edges
7. `cel_box()` - 27 edges
8. `Box` - 25 edges
9. `strip_fabric()` - 22 edges
10. `Face` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `body()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `neckline()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `sleeves()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `How the pieces work` --references--> `roll()`  [INFERRED]
  README.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `belt()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py

## Import Cycles
- None detected.

## Communities (33 total, 1 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.06
Nodes (22): puff(), band(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows() (+14 more)

### Community 1 - "How the pieces work"
Cohesion: 0.20
Nodes (6): How the pieces work, mesh(), tanto(), bump(), ears(), strap()

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
Cohesion: 0.14
Nodes (11): belt(), collar(), flaps(), hakama_legs(), leg_bone(), leg_ring(), neckline(), pouch() (+3 more)

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (12): back_crest(), bead_clip(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe(), splatter() (+4 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "Shared helpers"
Cohesion: 0.15
Nodes (7): body(), footwear(), tabi(), legs(), sleeves(), waistband(), strip_fabric()

### Community 12 - "k"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "arm_x"
Cohesion: 0.20
Nodes (5): sode(), arm_x(), kimono_sleeves(), kimono_sleeves(), roll()

### Community 14 - "kit_akimichi.py"
Cohesion: 0.17
Nodes (5): gourd(), lames(), quilt(), shoku_disc(), snack_pouch()

### Community 15 - "kit_kinoshita.py"
Cohesion: 0.11
Nodes (12): back_crest(), chisel(), crest(), kyahan(), mallet(), pencil(), _piece(), sashiko() (+4 more)

### Community 16 - "k"
Cohesion: 0.10
Nodes (12): face_mask(), obi(), brush_pin(), scarf(), trench_knife(), stockings(), bun(), clip() (+4 more)

### Community 17 - "stamp"
Cohesion: 0.18
Nodes (7): stamp(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), crest_patch()

### Community 18 - "Shared helpers"
Cohesion: 0.05
Nodes (33): Shared helpers, back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock() (+25 more)

### Community 19 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 20 - "glyphs.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 21 - "fabric"
Cohesion: 0.17
Nodes (7): crest(), arm_protector(), forehead_protector(), protector_plate(), beak(), plate(), fabric()

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_hatake.py"
Cohesion: 0.20
Nodes (4): decal(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.15
Nodes (9): arm_bone(), arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar() (+1 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 28 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 29 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 30 - "kit_shinobi.py"
Cohesion: 0.28
Nodes (4): anbu_arms(), anbu_plates(), flak_vest(), cap()

### Community 31 - "wide_sleeves"
Cohesion: 0.33
Nodes (3): seal_script(), seal_tags(), wide_sleeves()

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `k`, `arm_x`, `kit_akimichi.py`, `kit_kinoshita.py`, `stamp`, `Shared helpers`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `kit_shinobi.py`, `wide_sleeves`, `tool_belt`?**
  _High betweenness centrality (0.250) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.055811571940604196 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `How the pieces work`, `kit_senju.py`, `kit_kurama.py`, `Shared helpers`, `k`, `arm_x`, `kit_akimichi.py`, `kit_kinoshita.py`, `k`, `stamp`, `Shared helpers`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_shinobi.py`, `wide_sleeves`, `tool_belt`?**
  _High betweenness centrality (0.152) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `paint.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `Shared helpers`, `k`, `arm_x`, `kit_kinoshita.py`, `k`, `stamp`, `Shared helpers`, `glyphs.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `kit_shinobi.py`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._