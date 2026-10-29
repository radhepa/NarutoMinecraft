# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 13 files · ~18,577 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 328 nodes · 712 edges · 9 communities
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3c48d9ea`
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
- kit_yuhi.py

## God Nodes (most connected - your core abstractions)
1. `k()` - 41 edges
2. `Shared helpers` - 35 edges
3. `Box` - 25 edges
4. `fabric()` - 24 edges
5. `solid()` - 24 edges
6. `Face` - 22 edges
7. `planes()` - 20 edges
8. `strip_fabric()` - 17 edges
9. `rnd()` - 15 edges
10. `Garment` - 13 edges

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

## Communities (9 total, 0 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.10
Nodes (16): button(), cloth_shade(), curls_box(), curls_face(), dark_seams(), darken_rows(), hair_box(), hair_face() (+8 more)

### Community 1 - "fabric"
Cohesion: 0.06
Nodes (41): Shared helpers, How the pieces work, stamp(), arm_bone(), arm_x(), belt(), body(), collar() (+33 more)

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
Cohesion: 0.07
Nodes (11): band(), hem(), strip_line(), Box, Garment, key_rgba(), Layer, Piece (+3 more)

### Community 7 - "Clans"
Cohesion: 0.11
Nodes (15): Clans, Commands, Mix and match, Piece ids, Reference images, The clan file, Commits, graphify (+7 more)

### Community 8 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `fabric` to `kit_yuhi.py`, `paint.py`, `anime.py`, `Box`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Are the 34 inferred relationships involving `Shared helpers` (e.g. with `back_fan()` and `bangs()`) actually correct?**
  _`Shared helpers` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09743589743589744 - nodes in this community are weakly interconnected._
- **Why does `Box` connect `Box` to `paint.py`, `fabric`, `wardrobe.py`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `Box` (e.g. with `band()` and `cap()`) actually correct?**
  _`Box` has 9 INFERRED edges - model-reasoned connections that need verification._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.06378378378378378 - nodes in this community are weakly interconnected._
- **Why does `Face` connect `paint.py` to `fabric`, `wardrobe.py`, `Box`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._