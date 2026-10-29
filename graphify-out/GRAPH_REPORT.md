# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 27 files · ~32,460 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 580 nodes · 1269 edges · 27 communities (25 shown, 2 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6ef484e9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- solid
- wardrobe.py
- cel_box
- render.py
- living_eyes.py
- Shared helpers
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- k
- arm_x
- rnd
- bandage
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- kit_nara.py
- glyphs.py
- fabric
- kit_hatake.py
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- anime.py

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
- `Collections: the general wardrobe` --references--> `general_resident()`  [INFERRED]
  CLANS.md → tools/wardrobe/wardrobe.py
- `Population` --references--> `village_resident()`  [INFERRED]
  CLANS.md → tools/wardrobe/wardrobe.py
- `Shared helpers` --references--> `cel_box()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `lock()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `spike()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (27 total, 2 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.06
Nodes (16): band(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows(), grid() (+8 more)

### Community 1 - "solid"
Cohesion: 0.13
Nodes (14): How the pieces work, belt(), collar(), pouch(), anbu_plates(), flak_vest(), forehead_protector(), mesh() (+6 more)

### Community 2 - "wardrobe.py"
Cohesion: 0.05
Nodes (40): build(), build_all(), catalog(), clan_bottoms(), clan_resident(), compatible(), Garment, general_pool() (+32 more)

### Community 3 - "cel_box"
Cohesion: 0.07
Nodes (16): cel_box(), spike(), flick(), gourd(), lames(), puff(), snack_pouch(), ear_panels() (+8 more)

### Community 4 - "render.py"
Cohesion: 0.13
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "Shared helpers"
Cohesion: 0.20
Nodes (6): Shared helpers, flaps(), leg_ring(), neckline(), sandals(), wraps()

### Community 7 - "Clans"
Cohesion: 0.10
Nodes (17): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+9 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.06
Nodes (18): back_fan(), lock(), sidelocks(), hime_locks(), back_crest(), bead_clip(), brush_pin(), brush_stroke() (+10 more)

### Community 9 - "rnd"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "Shared helpers"
Cohesion: 0.17
Nodes (8): body(), footwear(), legs(), anbu_arms(), side_panels(), sleeves(), waistband(), strip_fabric()

### Community 12 - "k"
Cohesion: 0.17
Nodes (7): deep_hood(), high_collar(), hood_down(), lenses(), wrap_front(), stockings(), k()

### Community 13 - "arm_x"
Cohesion: 0.25
Nodes (4): sode(), arm_x(), kimono_sleeves(), roll()

### Community 14 - "rnd"
Cohesion: 0.15
Nodes (9): quilt(), ink_clouds(), bandage_turns(), thorn_wrap(), hair_box(), hair_face(), hair_shade(), rnd() (+1 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.11
Nodes (9): bun(), clip(), crest_patch(), hairpin(), seal_script(), seal_tags(), waves(), wide_sleeves() (+1 more)

### Community 17 - "stamp"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.11
Nodes (12): bangs(), curtain(), tie(), back_sheet(), blunt_fringe(), gathered_tail(), hair_tie(), hakama_legs() (+4 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.19
Nodes (7): arm_protector(), back_crest(), crest(), mesh_shirt(), net(), protector_plate(), fabric()

### Community 20 - "glyphs.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 21 - "fabric"
Cohesion: 0.22
Nodes (5): stamp(), shoku_disc(), crest(), beak(), plate()

### Community 23 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.14
Nodes (9): arm_bone(), arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar() (+1 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 28 - "anime.py"
Cohesion: 0.16
Nodes (6): braid(), cel_face(), ring_shell(), crown(), pulled_back(), scalp()

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `solid`, `cel_box`, `Shared helpers`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `arm_x`, `rnd`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `anime.py`?**
  _High betweenness centrality (0.247) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06386066763425254 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `cel_box`, `Shared helpers`, `kit_kurama.py`, `Shared helpers`, `k`, `arm_x`, `bandage`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `solid` be split into smaller, more focused modules?**
  _Cohesion score 0.12666666666666668 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `kit_nara.py` to `paint.py`, `solid`, `cel_box`, `Shared helpers`, `kit_kurama.py`, `Shared helpers`, `k`, `arm_x`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._