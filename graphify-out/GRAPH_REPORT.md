# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~33,757 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 604 nodes · 1315 edges · 32 communities (31 shown, 1 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1733db15`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- fabric
- wardrobe.py
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Clans
- kit_kurama.py
- rnd
- kit_uchiha.py
- Shared helpers
- k
- kit_akimichi.py
- Box
- kit_suzuran.py
- kit_uzumaki.py
- stamp
- kit_hyuga.py
- kit_nara.py
- glyphs.py
- stamp
- Shared helpers
- kit_hatake.py
- kit_shimura.py
- k
- kit_yamanaka.py
- How the pieces work
- anime.py
- cel_box
- spike
- curtain

## God Nodes (most connected - your core abstractions)
1. `k()` - 110 edges
2. `solid()` - 69 edges
3. `fabric()` - 57 edges
4. `Shared helpers` - 34 edges
5. `stamp()` - 29 edges
6. `cel_box()` - 27 edges
7. `rnd()` - 26 edges
8. `Box` - 25 edges
9. `strip_fabric()` - 22 edges
10. `Face` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `wraps()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit_shinobi.py
- `Shared helpers` --references--> `cel_box()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `spike()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `bangs()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `ring_shell()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (32 total, 1 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.07
Nodes (21): puff(), fur_edge(), pulled_back(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams() (+13 more)

### Community 1 - "fabric"
Cohesion: 0.15
Nodes (10): crest(), arm_protector(), anbu_arms(), anbu_plates(), flak_vest(), forehead_protector(), protector_plate(), wraps() (+2 more)

### Community 2 - "wardrobe.py"
Cohesion: 0.06
Nodes (42): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+34 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.22
Nodes (4): bun(), lames(), plate(), shoulder_guards()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.19
Nodes (9): belt(), collar(), flaps(), hakama_legs(), leg_bone(), leg_ring(), pouch(), side_panels() (+1 more)

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (12): back_crest(), bead_clip(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe(), splatter() (+4 more)

### Community 9 - "rnd"
Cohesion: 0.15
Nodes (6): claw_marks(), fang(), fang_small(), fur_box(), fur_face(), paw()

### Community 10 - "kit_uchiha.py"
Cohesion: 0.06
Nodes (19): arm_crest(), back_crest(), chest_crest(), crest(), lamellar(), police_badge(), bandage_turns(), mist_swirls() (+11 more)

### Community 11 - "Shared helpers"
Cohesion: 0.13
Nodes (8): body(), footwear(), kimono_sleeves(), tabi(), legs(), sleeves(), waistband(), strip_fabric()

### Community 12 - "k"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_akimichi.py"
Cohesion: 0.10
Nodes (12): gourd(), lames(), quilt(), shoku_disc(), snack_pouch(), sode(), arm_bone(), arm_x() (+4 more)

### Community 14 - "Box"
Cohesion: 0.08
Nodes (9): band(), hem(), Box, Garment, key_rgba(), Layer, Piece, piece_corners() (+1 more)

### Community 15 - "kit_suzuran.py"
Cohesion: 0.11
Nodes (9): apothecary_sash(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch(), sash_vials() (+1 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.14
Nodes (7): bun(), clip(), hairpin(), seal_script(), seal_tags(), wide_sleeves(), wrap_tie()

### Community 17 - "stamp"
Cohesion: 0.22
Nodes (5): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.17
Nodes (7): bangs(), tie(), blunt_fringe(), gathered_tail(), hair_tie(), parted_fringe(), wrap_front()

### Community 19 - "kit_nara.py"
Cohesion: 0.28
Nodes (4): back_crest(), crest(), mesh_shirt(), net()

### Community 20 - "glyphs.py"
Cohesion: 0.18
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 21 - "stamp"
Cohesion: 0.24
Nodes (5): stamp(), back_crest(), crest_patch(), bump(), plate()

### Community 22 - "Shared helpers"
Cohesion: 0.15
Nodes (8): Shared helpers, back_fan(), braid(), lock(), sidelocks(), hime_locks(), beard(), sandals()

### Community 23 - "kit_hatake.py"
Cohesion: 0.20
Nodes (4): decal(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "k"
Cohesion: 0.10
Nodes (11): face_mask(), obi(), brush_pin(), neckline(), pauldron(), scarf(), trench_knife(), stockings() (+3 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "How the pieces work"
Cohesion: 0.20
Nodes (6): How the pieces work, mesh(), tanto(), beak(), ears(), strap()

### Community 28 - "anime.py"
Cohesion: 0.29
Nodes (3): cel_face(), ring_shell(), crown()

### Community 29 - "cel_box"
Cohesion: 0.22
Nodes (5): cel_box(), flick(), ear_panels(), tuft(), side_panels()

### Community 30 - "spike"
Cohesion: 0.33
Nodes (3): spike(), burst(), pineapple()

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `fabric`, `kit_senju.py`, `solid`, `kit_kurama.py`, `rnd`, `kit_uchiha.py`, `Shared helpers`, `k`, `kit_akimichi.py`, `Box`, `kit_suzuran.py`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `Shared helpers`, `kit_hatake.py`, `kit_shimura.py`, `kit_yamanaka.py`, `anime.py`, `cel_box`?**
  _High betweenness centrality (0.263) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07183673469387755 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `fabric`, `kit_senju.py`, `kit_kurama.py`, `kit_uchiha.py`, `Shared helpers`, `k`, `kit_akimichi.py`, `Box`, `kit_suzuran.py`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `Shared helpers`, `kit_hatake.py`, `kit_shimura.py`, `k`, `How the pieces work`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.14736842105263157 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `paint.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `kit_uchiha.py`, `Shared helpers`, `k`, `kit_akimichi.py`, `kit_suzuran.py`, `kit_uzumaki.py`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `glyphs.py`, `stamp`, `Shared helpers`, `kit_hatake.py`, `kit_shimura.py`, `k`, `kit_yamanaka.py`, `How the pieces work`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._