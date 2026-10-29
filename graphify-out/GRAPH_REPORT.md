# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~34,238 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 616 nodes · 1342 edges · 34 communities (30 shown, 4 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1733db15`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- kit.py
- wardrobe.py
- kit_senju.py
- render.py
- living_eyes.py
- leg_bone
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- strip_fabric
- k
- kit_rugged.py
- bandage_turns
- Clans
- solid
- stamp
- Shared helpers
- forehead_protector
- glyphs.py
- fabric
- Garment
- kit_hatake.py
- kit_shimura.py
- kit_akimichi.py
- kit_yamanaka.py
- load_clans
- rnd
- main
- Piece
- back_crest
- thorn_band
- rose

## God Nodes (most connected - your core abstractions)
1. `k()` - 116 edges
2. `solid()` - 70 edges
3. `fabric()` - 57 edges
4. `Shared helpers` - 34 edges
5. `rnd()` - 31 edges
6. `cel_box()` - 29 edges
7. `stamp()` - 27 edges
8. `strip_fabric()` - 25 edges
9. `Box` - 25 edges
10. `Face` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `body()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `neckline()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `sleeves()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `belt()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `pouch()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py

## Import Cycles
- None detected.

## Communities (34 total, 4 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.06
Nodes (18): band(), button(), curls_face(), dark_seams(), darken_rows(), grid(), hair_box(), hair_face() (+10 more)

### Community 1 - "kit.py"
Cohesion: 0.09
Nodes (14): How the pieces work, belt(), collar(), flaps(), legs(), neckline(), pouch(), roll() (+6 more)

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

### Community 6 - "leg_bone"
Cohesion: 0.22
Nodes (5): hakama_legs(), leg_bone(), leg_ring(), baggy_legs(), shin_guard()

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.05
Nodes (23): sode(), arm_bone(), arm_x(), back_crest(), bead_clip(), brush_stroke(), bun(), kimono_sleeves() (+15 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.15
Nodes (8): mist_swirls(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock(), wave_shell()

### Community 11 - "strip_fabric"
Cohesion: 0.15
Nodes (9): body(), kimono_sleeves(), anbu_arms(), anbu_plates(), flak_vest(), sandals(), waistband(), cap() (+1 more)

### Community 12 - "k"
Cohesion: 0.19
Nodes (6): deep_hood(), high_collar(), hood_down(), lenses(), scarf(), k()

### Community 13 - "kit_rugged.py"
Cohesion: 0.08
Nodes (13): cape(), dread(), knot_bun(), leg_wraps(), patch(), rope(), rope_face(), rope_hair() (+5 more)

### Community 15 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 16 - "solid"
Cohesion: 0.08
Nodes (12): lames(), snack_pouch(), face_mask(), obi(), brush_pin(), pauldron(), trench_knife(), high_collar() (+4 more)

### Community 17 - "stamp"
Cohesion: 0.15
Nodes (8): stamp(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), crest_patch(), waves()

### Community 18 - "Shared helpers"
Cohesion: 0.06
Nodes (31): Shared helpers, back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock() (+23 more)

### Community 19 - "forehead_protector"
Cohesion: 0.33
Nodes (3): arm_protector(), forehead_protector(), protector_plate()

### Community 20 - "glyphs.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 21 - "fabric"
Cohesion: 0.13
Nodes (8): footwear(), crest(), sleeves(), beak(), bump(), plate(), cloth_shade(), fabric()

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_hatake.py"
Cohesion: 0.20
Nodes (4): decal(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_akimichi.py"
Cohesion: 0.17
Nodes (6): flick(), gourd(), puff(), quilt(), shoku_disc(), curls_box()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 28 - "rnd"
Cohesion: 0.18
Nodes (6): ink_clouds(), splatter(), wisteria_hem(), camo(), ragged(), rnd()

### Community 29 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 30 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `kit.py`, `kit_senju.py`, `leg_bone`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `strip_fabric`, `kit_rugged.py`, `bandage_turns`, `solid`, `stamp`, `Shared helpers`, `forehead_protector`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`, `kit_akimichi.py`, `kit_yamanaka.py`, `rnd`, `thorn_band`, `rose`?**
  _High betweenness centrality (0.273) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06015037593984962 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `kit.py`, `kit_senju.py`, `leg_bone`, `kit_kurama.py`, `strip_fabric`, `k`, `kit_rugged.py`, `stamp`, `Shared helpers`, `forehead_protector`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`, `kit_akimichi.py`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `kit.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09057971014492754 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `paint.py`, `kit.py`, `kit_senju.py`, `kit_kurama.py`, `strip_fabric`, `k`, `kit_rugged.py`, `stamp`, `Shared helpers`, `forehead_protector`, `glyphs.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_yamanaka.py`, `back_crest`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._