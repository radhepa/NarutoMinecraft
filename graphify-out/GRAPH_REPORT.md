# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 13 files · ~17,643 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 313 nodes · 684 edges · 8 communities
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fa621a7f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- fabric
- wardrobe.py
- anime.py
- render.py
- living_eyes.py
- Box
- Clans

## God Nodes (most connected - your core abstractions)
1. `Shared helpers` - 35 edges
2. `k()` - 33 edges
3. `fabric()` - 26 edges
4. `solid()` - 26 edges
5. `Box` - 25 edges
6. `Face` - 22 edges
7. `planes()` - 20 edges
8. `strip_fabric()` - 17 edges
9. `Garment` - 13 edges
10. `How the pieces work` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `stamp()`  [INFERRED]
  CLANS.md → tools/wardrobe/glyphs.py
- `Shared helpers` --references--> `body()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `sleeves()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `belt()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `pouch()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py

## Import Cycles
- None detected.

## Communities (8 total, 0 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.09
Nodes (21): sword_strap(), band(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows() (+13 more)

### Community 1 - "fabric"
Cohesion: 0.05
Nodes (38): How the pieces work, stamp(), arm_bone(), arm_x(), belt(), body(), collar(), flaps() (+30 more)

### Community 2 - "wardrobe.py"
Cohesion: 0.09
Nodes (26): build(), build_all(), catalog(), clan_bottoms(), clan_resident(), compatible(), hex_rgb(), json_text() (+18 more)

### Community 3 - "anime.py"
Cohesion: 0.12
Nodes (15): Shared helpers, back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock() (+7 more)

### Community 4 - "render.py"
Cohesion: 0.14
Nodes (16): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), ground_shadow() (+8 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "Box"
Cohesion: 0.07
Nodes (9): strip_line(), Box, Garment, key_rgba(), Layer, Piece, piece_corners(), rot_matrix() (+1 more)

### Community 7 - "Clans"
Cohesion: 0.11
Nodes (15): Clans, Commands, Mix and match, Piece ids, Reference images, The clan file, Commits, graphify (+7 more)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Box` connect `Box` to `paint.py`, `fabric`, `wardrobe.py`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 34 inferred relationships involving `Shared helpers` (e.g. with `back_fan()` and `bangs()`) actually correct?**
  _`Shared helpers` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0851063829787234 - nodes in this community are weakly interconnected._
- **Why does `Face` connect `paint.py` to `fabric`, `wardrobe.py`, `Box`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.05442428730099963 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `fabric` to `paint.py`, `anime.py`, `Box`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._