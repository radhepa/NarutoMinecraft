# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 13 files · ~17,557 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 315 nodes · 688 edges · 8 communities
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 74 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `46fd25d1`
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
2. `k()` - 34 edges
3. `fabric()` - 26 edges
4. `solid()` - 26 edges
5. `Box` - 25 edges
6. `Face` - 22 edges
7. `planes()` - 20 edges
8. `strip_fabric()` - 17 edges
9. `Garment` - 13 edges
10. `cel_box()` - 12 edges

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

## Communities (8 total, 0 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.08
Nodes (19): cel_face(), ring_shell(), button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows() (+11 more)

### Community 1 - "fabric"
Cohesion: 0.06
Nodes (42): Shared helpers, How the pieces work, braid(), stamp(), arm_bone(), arm_x(), belt(), body() (+34 more)

### Community 2 - "wardrobe.py"
Cohesion: 0.10
Nodes (24): build(), build_all(), catalog(), hex_rgb(), json_text(), load_characters(), load_clans(), load_eye_colors() (+16 more)

### Community 3 - "anime.py"
Cohesion: 0.10
Nodes (12): back_fan(), bangs(), cel_box(), curtain(), lock(), sidelocks(), spike(), tie() (+4 more)

### Community 4 - "render.py"
Cohesion: 0.14
Nodes (16): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), ground_shadow() (+8 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "Box"
Cohesion: 0.07
Nodes (11): band(), hem(), strip_line(), Box, compatible(), Garment, key_rgba(), Layer (+3 more)

### Community 7 - "Clans"
Cohesion: 0.10
Nodes (16): Clans, Commands, Mix and match, Piece ids, The clan file, Commits, graphify, Naruto Minecraft (+8 more)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Box` connect `Box` to `paint.py`, `fabric`, `wardrobe.py`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **Are the 34 inferred relationships involving `Shared helpers` (e.g. with `back_fan()` and `bangs()`) actually correct?**
  _`Shared helpers` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0821256038647343 - nodes in this community are weakly interconnected._
- **Why does `Face` connect `paint.py` to `fabric`, `wardrobe.py`, `Box`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.06151742993848257 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `fabric` to `paint.py`, `anime.py`, `Box`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._