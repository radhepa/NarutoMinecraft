# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,681 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 600 nodes · 1333 edges · 31 communities (29 shown, 2 thin omitted)
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
- arm_x
- kit_akimichi.py
- Box
- seal_script
- stamp
- kit_hyuga.py
- kit_nara.py
- glyphs.py
- stamp
- anime.py
- kit_hatake.py
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- kit_morino.py
- anime.py
- bangs
- spike

## God Nodes (most connected - your core abstractions)
1. `k()` - 112 edges
2. `solid()` - 71 edges
3. `fabric()` - 60 edges
4. `Shared helpers` - 34 edges
5. `cel_box()` - 29 edges
6. `stamp()` - 29 edges
7. `rnd()` - 28 edges
8. `strip_fabric()` - 25 edges
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

## Communities (31 total, 2 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.08
Nodes (17): band(), button(), cloth_shade(), curls_face(), dark_seams(), darken_rows(), grid(), hair_box() (+9 more)

### Community 1 - "solid"
Cohesion: 0.12
Nodes (18): Shared helpers, How the pieces work, belt(), collar(), flaps(), hakama_legs(), leg_bone(), leg_ring() (+10 more)

### Community 2 - "wardrobe.py"
Cohesion: 0.06
Nodes (42): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+34 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_shinobi.py"
Cohesion: 0.15
Nodes (6): arm_protector(), anbu_plates(), mesh(), protector_plate(), sandals(), wraps()

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.14
Nodes (8): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw(), rnd()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.09
Nodes (13): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+5 more)

### Community 11 - "Shared helpers"
Cohesion: 0.15
Nodes (10): body(), footwear(), kimono_sleeves(), legs(), gloves(), anbu_arms(), sleeves(), waistband() (+2 more)

### Community 12 - "k"
Cohesion: 0.08
Nodes (15): deep_hood(), high_collar(), hood_down(), lenses(), slanted_protector(), obi(), tabi(), guardian_sash() (+7 more)

### Community 13 - "arm_x"
Cohesion: 0.18
Nodes (8): sode(), arm_bone(), arm_x(), kimono_sleeves(), armband(), roll(), arm_warmers(), wide_sleeves()

### Community 14 - "kit_akimichi.py"
Cohesion: 0.12
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box()

### Community 15 - "Box"
Cohesion: 0.08
Nodes (7): Box, Garment, key_rgba(), Layer, Piece, piece_corners(), world_bounds()

### Community 17 - "stamp"
Cohesion: 0.15
Nodes (7): crest(), crest_patch(), flame_hem(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.14
Nodes (10): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), wrap_front() (+2 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "glyphs.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 21 - "stamp"
Cohesion: 0.21
Nodes (5): stamp(), crest(), crest_patch(), bump(), plate()

### Community 22 - "anime.py"
Cohesion: 0.14
Nodes (7): back_fan(), braid(), cel_face(), lock(), sidelocks(), hime_locks(), beard()

### Community 23 - "kit_hatake.py"
Cohesion: 0.20
Nodes (4): decal(), face_mask(), shoulder_decal(), white_fang_tanto()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "kit_morino.py"
Cohesion: 0.18
Nodes (5): back_crest(), coat_skirts(), head_cloth(), heavy_boots(), forehead_protector()

### Community 28 - "anime.py"
Cohesion: 0.20
Nodes (6): ring_shell(), crown(), clipped(), combed_back(), pulled_back(), scalp()

### Community 29 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `solid`, `kit_senju.py`, `kit_shinobi.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `arm_x`, `kit_akimichi.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `anime.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `kit_morino.py`, `anime.py`?**
  _High betweenness centrality (0.256) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08194905869324474 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `kit_senju.py`, `kit_shinobi.py`, `kit_kurama.py`, `Shared helpers`, `k`, `arm_x`, `kit_akimichi.py`, `Box`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_morino.py`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `solid` be split into smaller, more focused modules?**
  _Cohesion score 0.12413793103448276 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `Shared helpers` to `paint.py`, `solid`, `kit_senju.py`, `kit_shinobi.py`, `kit_kurama.py`, `k`, `arm_x`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `kit_morino.py`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._