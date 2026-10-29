# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~34,666 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 626 nodes · 1365 edges · 39 communities (35 shown, 4 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 74 edges (avg confidence: 0.93)
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
- kit_market.py
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- k
- arm_x
- k
- bandage
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- kit_nara.py
- glyphs.py
- kit_akimichi.py
- Clans
- stamp
- anime.py
- kit_uchiha.py
- kit_yamanaka.py
- Garment
- anime.py
- fabric
- load_clans
- main
- Piece
- cel_box
- bangs
- spike
- curtain
- seal_script
- wave_lock

## God Nodes (most connected - your core abstractions)
1. `k()` - 119 edges
2. `solid()` - 77 edges
3. `fabric()` - 57 edges
4. `Shared helpers` - 33 edges
5. `rnd()` - 29 edges
6. `cel_box()` - 27 edges
7. `stamp()` - 27 edges
8. `strip_fabric()` - 27 edges
9. `Box` - 25 edges
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
- `Shared helpers` --references--> `sidelocks()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (39 total, 4 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.06
Nodes (19): band(), button(), cloth_shade(), curls_face(), dark_seams(), darken_rows(), grid(), hair_box() (+11 more)

### Community 1 - "solid"
Cohesion: 0.13
Nodes (15): How the pieces work, belt(), collar(), flaps(), leg_ring(), furoshiki(), pouch(), roll() (+7 more)

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

### Community 6 - "kit_market.py"
Cohesion: 0.05
Nodes (22): hakama_legs(), leg_bone(), bib(), checks(), dots(), gathered_ankles(), geta(), jika_tabi() (+14 more)

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.09
Nodes (11): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), part_line(), side_fringe(), splatter() (+3 more)

### Community 9 - "rnd"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.18
Nodes (9): bandage_turns(), thorn_wrap(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock(), wave_shell() (+1 more)

### Community 11 - "Shared helpers"
Cohesion: 0.10
Nodes (14): Shared helpers, body(), footwear(), kimono_sleeves(), legs(), neckline(), anbu_arms(), anbu_plates() (+6 more)

### Community 12 - "k"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "arm_x"
Cohesion: 0.21
Nodes (7): sode(), arm_bone(), arm_x(), kimono_sleeves(), tasuki(), arm_warmers(), wide_sleeves()

### Community 14 - "k"
Cohesion: 0.11
Nodes (10): sword_strap(), ink_clouds(), straw_sandals(), stockings(), waves(), mist_swirls(), rose(), thorn_band() (+2 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.20
Nodes (4): clip(), crest_patch(), hairpin(), wrap_tie()

### Community 17 - "stamp"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.18
Nodes (6): tie(), gathered_tail(), hair_tie(), obi(), tabi(), wrap_front()

### Community 19 - "kit_nara.py"
Cohesion: 0.28
Nodes (4): back_crest(), crest(), mesh_shirt(), net()

### Community 20 - "glyphs.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 21 - "kit_akimichi.py"
Cohesion: 0.14
Nodes (7): gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box()

### Community 22 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 23 - "stamp"
Cohesion: 0.10
Nodes (10): stamp(), decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto(), back_crest(), cane() (+2 more)

### Community 24 - "anime.py"
Cohesion: 0.14
Nodes (7): back_fan(), braid(), cel_face(), lock(), sidelocks(), hime_locks(), beard()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 28 - "anime.py"
Cohesion: 0.29
Nodes (4): ring_shell(), crown(), pulled_back(), scalp()

### Community 29 - "fabric"
Cohesion: 0.20
Nodes (6): crest(), arm_protector(), forehead_protector(), protector_plate(), sleeves(), fabric()

### Community 30 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 31 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 32 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 33 - "cel_box"
Cohesion: 0.22
Nodes (5): cel_box(), flick(), ear_panels(), tuft(), bun()

### Community 34 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

### Community 35 - "spike"
Cohesion: 0.33
Nodes (3): spike(), burst(), pineapple()

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `solid`, `kit_senju.py`, `kit_market.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `k`, `arm_x`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `kit_akimichi.py`, `stamp`, `anime.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `anime.py`, `fabric`, `cel_box`?**
  _High betweenness centrality (0.269) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05727644652250146 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `kit_senju.py`, `kit_market.py`, `kit_kurama.py`, `Shared helpers`, `k`, `arm_x`, `k`, `bandage`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `kit_akimichi.py`, `stamp`, `kit_uchiha.py`, `fabric`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `solid` be split into smaller, more focused modules?**
  _Cohesion score 0.12923076923076923 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `paint.py`, `solid`, `kit_senju.py`, `kit_market.py`, `kit_kurama.py`, `Shared helpers`, `k`, `arm_x`, `k`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `kit_uchiha.py`, `kit_yamanaka.py`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._