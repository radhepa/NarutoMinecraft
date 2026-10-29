# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,070 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 596 nodes · 1303 edges · 41 communities (35 shown, 6 thin omitted)
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
- hakama_legs
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- k
- arm_x
- k
- Clans
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- fabric
- glyphs.py
- fabric
- kit_haruno.py
- kit_hatake.py
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- cel_box
- anime.py
- solid
- Garment
- load_clans
- main
- anime.py
- Piece
- kit_shinobi.py
- curtain
- thorn_band
- back_crest
- mist_swirls
- rose

## God Nodes (most connected - your core abstractions)
1. `k()` - 107 edges
2. `solid()` - 68 edges
3. `fabric()` - 59 edges
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

## Communities (41 total, 6 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.05
Nodes (21): puff(), band(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows() (+13 more)

### Community 1 - "How the pieces work"
Cohesion: 0.18
Nodes (7): How the pieces work, belt(), collar(), mesh(), tanto(), ears(), strap()

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

### Community 6 - "hakama_legs"
Cohesion: 0.40
Nodes (3): hakama_legs(), leg_bone(), leg_ring()

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (12): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), part_line(), side_fringe(), splatter() (+4 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.15
Nodes (10): quilt(), bandage_turns(), thorn_wrap(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock() (+2 more)

### Community 11 - "Shared helpers"
Cohesion: 0.13
Nodes (14): Shared helpers, body(), flaps(), footwear(), legs(), neckline(), pouch(), anbu_plates() (+6 more)

### Community 12 - "k"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "arm_x"
Cohesion: 0.33
Nodes (3): arm_x(), kimono_sleeves(), roll()

### Community 14 - "k"
Cohesion: 0.08
Nodes (13): face_mask(), obi(), tabi(), wrap_front(), ink_clouds(), pauldron(), scarf(), trench_knife() (+5 more)

### Community 15 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.14
Nodes (7): bun(), clip(), crest_patch(), hairpin(), seal_script(), seal_tags(), wide_sleeves()

### Community 17 - "stamp"
Cohesion: 0.22
Nodes (5): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.21
Nodes (6): bangs(), tie(), blunt_fringe(), gathered_tail(), hair_tie(), parted_fringe()

### Community 19 - "fabric"
Cohesion: 0.24
Nodes (5): arm_protector(), forehead_protector(), protector_plate(), beak(), fabric()

### Community 20 - "glyphs.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 21 - "fabric"
Cohesion: 0.24
Nodes (5): stamp(), shoku_disc(), crest(), bump(), plate()

### Community 22 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 23 - "kit_hatake.py"
Cohesion: 0.20
Nodes (4): decal(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.17
Nodes (8): arm_bone(), kimono_sleeves(), arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "cel_box"
Cohesion: 0.12
Nodes (9): braid(), cel_box(), cel_face(), spike(), flick(), ear_panels(), pineapple(), tuft() (+1 more)

### Community 28 - "anime.py"
Cohesion: 0.19
Nodes (6): ring_shell(), crown(), mesh_shirt(), net(), pulled_back(), scalp()

### Community 29 - "solid"
Cohesion: 0.17
Nodes (7): gourd(), lames(), snack_pouch(), sode(), side_panels(), high_collar(), solid()

### Community 30 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 31 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 32 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 33 - "anime.py"
Cohesion: 0.24
Nodes (4): back_fan(), lock(), sidelocks(), hime_locks()

### Community 34 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

## Knowledge Gaps
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `How the pieces work`, `kit_senju.py`, `hakama_legs`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `k`, `arm_x`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `fabric`, `glyphs.py`, `fabric`, `kit_haruno.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `cel_box`, `anime.py`, `solid`, `anime.py`, `kit_shinobi.py`, `thorn_band`, `mist_swirls`, `rose`?**
  _High betweenness centrality (0.252) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05446853516657853 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `How the pieces work`, `kit_senju.py`, `hakama_legs`, `kit_kurama.py`, `Shared helpers`, `k`, `arm_x`, `k`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `fabric`, `glyphs.py`, `fabric`, `kit_haruno.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `anime.py`, `kit_shinobi.py`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `paint.py`, `How the pieces work`, `kit_senju.py`, `kit_kurama.py`, `Shared helpers`, `k`, `arm_x`, `k`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `glyphs.py`, `fabric`, `kit_haruno.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `anime.py`, `kit_shinobi.py`, `back_crest`?**
  _High betweenness centrality (0.111) - this node is a cross-community bridge._