# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 13 files · ~17,455 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 311 nodes · 685 edges · 13 communities
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `61fc7936`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- k
- wardrobe.py
- anime.py
- render.py
- living_eyes.py
- Box
- Clans
- How the pieces work
- fabric
- Shared helpers
- kit_shimura.py
- solid

## God Nodes (most connected - your core abstractions)
1. `Shared helpers` - 35 edges
2. `k()` - 33 edges
3. `solid()` - 27 edges
4. `fabric()` - 26 edges
5. `Box` - 25 edges
6. `Face` - 22 edges
7. `planes()` - 20 edges
8. `strip_fabric()` - 17 edges
9. `Garment` - 13 edges
10. `How the pieces work` - 12 edges

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

## Communities (13 total, 0 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.09
Nodes (17): button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows(), grid(), hair_box() (+9 more)

### Community 1 - "k"
Cohesion: 0.15
Nodes (11): arm_bone(), arm_x(), belt(), flaps(), leg_bone(), leg_ring(), neckline(), roll() (+3 more)

### Community 2 - "wardrobe.py"
Cohesion: 0.09
Nodes (26): build(), build_all(), catalog(), clan_bottoms(), clan_resident(), compatible(), hex_rgb(), json_text() (+18 more)

### Community 3 - "anime.py"
Cohesion: 0.13
Nodes (11): back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock(), ring_shell() (+3 more)

### Community 4 - "render.py"
Cohesion: 0.14
Nodes (16): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), ground_shadow() (+8 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "Box"
Cohesion: 0.06
Nodes (11): band(), hem(), strip_line(), Box, Garment, key_rgba(), Layer, Piece (+3 more)

### Community 7 - "Clans"
Cohesion: 0.11
Nodes (15): Clans, Commands, Mix and match, Piece ids, Reference images, The clan file, Commits, graphify (+7 more)

### Community 8 - "How the pieces work"
Cohesion: 0.20
Nodes (8): How the pieces work, stamp(), collar(), beak(), bump(), ears(), plate(), strap()

### Community 9 - "fabric"
Cohesion: 0.19
Nodes (8): body(), footwear(), legs(), anbu_arms(), sleeves(), waistband(), fabric(), strip_fabric()

### Community 10 - "Shared helpers"
Cohesion: 0.20
Nodes (7): Shared helpers, forehead_protector(), mesh(), protector_plate(), sandals(), tanto(), wraps()

### Community 11 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 12 - "solid"
Cohesion: 0.32
Nodes (5): pouch(), anbu_plates(), flak_vest(), cap(), solid()

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Box` connect `Box` to `paint.py`, `fabric`, `wardrobe.py`, `solid`?**
  _High betweenness centrality (0.141) - this node is a cross-community bridge._
- **Are the 34 inferred relationships involving `Shared helpers` (e.g. with `back_fan()` and `bangs()`) actually correct?**
  _`Shared helpers` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09291521486643438 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `paint.py`, `k`, `Box`, `How the pieces work`, `fabric`, `Shared helpers`, `kit_shimura.py`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `wardrobe.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09494949494949495 - nodes in this community are weakly interconnected._
- **Why does `Face` connect `paint.py` to `fabric`, `wardrobe.py`, `Box`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._