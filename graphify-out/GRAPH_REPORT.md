# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,263 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 594 nodes · 1300 edges · 39 communities (35 shown, 4 thin omitted)
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
- k
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- k
- Clans
- bandage_turns
- anime.py
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- kit_nara.py
- glyphs.py
- fabric
- Garment
- kit_hatake.py
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- solid
- anime.py
- load_clans
- kit_namiashi.py
- rnd
- main
- Piece
- bangs
- forehead_protector
- hairpin
- mist_swirls
- rose

## God Nodes (most connected - your core abstractions)
1. `k()` - 105 edges
2. `solid()` - 68 edges
3. `fabric()` - 57 edges
4. `Shared helpers` - 34 edges
5. `stamp()` - 29 edges
6. `cel_box()` - 27 edges
7. `rnd()` - 26 edges
8. `Box` - 25 edges
9. `strip_fabric()` - 22 edges
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
Cohesion: 0.05
Nodes (21): puff(), band(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows() (+13 more)

### Community 1 - "kit_shinobi.py"
Cohesion: 0.18
Nodes (6): anbu_arms(), anbu_plates(), flak_vest(), mesh(), tanto(), cap()

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

### Community 6 - "k"
Cohesion: 0.10
Nodes (11): lames(), shoku_disc(), snack_pouch(), sword_strap(), obi(), wrap_front(), wave_band(), clip() (+3 more)

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
Cohesion: 0.09
Nodes (19): Shared helpers, belt(), body(), flaps(), footwear(), hakama_legs(), tabi(), leg_bone() (+11 more)

### Community 12 - "k"
Cohesion: 0.22
Nodes (3): high_collar(), hood_down(), lenses()

### Community 13 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 15 - "anime.py"
Cohesion: 0.16
Nodes (6): back_fan(), braid(), lock(), sidelocks(), hime_locks(), beard()

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.22
Nodes (4): bun(), crest_patch(), seal_script(), seal_tags()

### Community 17 - "stamp"
Cohesion: 0.18
Nodes (7): stamp(), crest(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.19
Nodes (8): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), pineapple()

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "glyphs.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 21 - "fabric"
Cohesion: 0.21
Nodes (8): How the pieces work, collar(), beak(), bump(), ears(), plate(), strap(), fabric()

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.07
Nodes (17): sode(), arm_bone(), arm_x(), kimono_sleeves(), kimono_sleeves(), wave_lock(), roll(), arm_crest() (+9 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "solid"
Cohesion: 0.17
Nodes (6): deep_hood(), pauldron(), scarf(), trench_knife(), plate(), solid()

### Community 28 - "anime.py"
Cohesion: 0.22
Nodes (5): cel_face(), ring_shell(), crown(), pulled_back(), scalp()

### Community 29 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 30 - "kit_namiashi.py"
Cohesion: 0.24
Nodes (4): back_blade(), crest(), hip_kokuto(), kokuto()

### Community 31 - "rnd"
Cohesion: 0.25
Nodes (4): flick(), gourd(), quilt(), rnd()

### Community 32 - "main"
Cohesion: 0.28
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 33 - "Piece"
Cohesion: 0.33
Nodes (3): Piece, piece_corners(), world_bounds()

### Community 34 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

### Community 35 - "forehead_protector"
Cohesion: 0.33
Nodes (3): arm_protector(), forehead_protector(), protector_plate()

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `kit_shinobi.py`, `kit_senju.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `k`, `bandage_turns`, `anime.py`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `solid`, `anime.py`, `kit_namiashi.py`, `rnd`, `forehead_protector`, `hairpin`, `mist_swirls`, `rose`?**
  _High betweenness centrality (0.254) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05446853516657853 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `kit_shinobi.py`, `kit_senju.py`, `k`, `kit_kurama.py`, `Shared helpers`, `k`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `fabric`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_namiashi.py`, `rnd`, `forehead_protector`, `hairpin`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `paint.py`, `kit_shinobi.py`, `kit_senju.py`, `k`, `kit_kurama.py`, `Shared helpers`, `k`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `kit_hatake.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `solid`, `kit_namiashi.py`, `forehead_protector`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._