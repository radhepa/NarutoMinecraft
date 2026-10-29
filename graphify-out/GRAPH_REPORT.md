# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 13 files · ~17,922 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 322 nodes · 711 edges · 12 communities
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f993154d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- kit.py
- wardrobe.py
- anime.py
- render.py
- living_eyes.py
- Box
- Clans
- kit_uzumaki.py
- k
- Shared helpers
- fabric

## God Nodes (most connected - your core abstractions)
1. `k()` - 38 edges
2. `Shared helpers` - 35 edges
3. `solid()` - 29 edges
4. `fabric()` - 25 edges
5. `Box` - 25 edges
6. `Face` - 22 edges
7. `planes()` - 20 edges
8. `strip_fabric()` - 18 edges
9. `Garment` - 13 edges
10. `rnd()` - 12 edges

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

## Communities (12 total, 0 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.14
Nodes (8): button(), dark_seams(), darken_rows(), grid(), line(), rivets(), Face, shade()

### Community 1 - "kit.py"
Cohesion: 0.11
Nodes (12): body(), footwear(), leg_bone(), leg_ring(), legs(), neckline(), anbu_arms(), anbu_plates() (+4 more)

### Community 2 - "wardrobe.py"
Cohesion: 0.12
Nodes (23): build(), build_all(), catalog(), hex_rgb(), json_text(), load_characters(), load_clans(), load_eye_colors() (+15 more)

### Community 3 - "anime.py"
Cohesion: 0.07
Nodes (22): back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock(), ring_shell() (+14 more)

### Community 4 - "render.py"
Cohesion: 0.14
Nodes (16): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), ground_shadow() (+8 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "Box"
Cohesion: 0.06
Nodes (12): band(), hem(), strip_line(), Box, compatible(), Garment, key_rgba(), Layer (+4 more)

### Community 7 - "Clans"
Cohesion: 0.10
Nodes (16): Clans, Commands, Mix and match, Piece ids, The clan file, Commits, graphify, Naruto Minecraft (+8 more)

### Community 8 - "kit_uzumaki.py"
Cohesion: 0.15
Nodes (8): stamp(), arm_bone(), arm_x(), roll(), crest_patch(), seal_tags(), waves(), wide_sleeves()

### Community 9 - "k"
Cohesion: 0.16
Nodes (11): belt(), flaps(), pouch(), flak_vest(), stockings(), clip(), hairpin(), wrap_tie() (+3 more)

### Community 10 - "Shared helpers"
Cohesion: 0.17
Nodes (8): Shared helpers, bandage(), forehead_protector(), mesh(), protector_plate(), sandals(), tanto(), wraps()

### Community 11 - "fabric"
Cohesion: 0.22
Nodes (8): How the pieces work, collar(), beak(), bump(), ears(), plate(), strap(), fabric()

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Box` connect `Box` to `paint.py`, `kit.py`, `wardrobe.py`, `anime.py`, `k`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Are the 34 inferred relationships involving `Shared helpers` (e.g. with `back_fan()` and `bangs()`) actually correct?**
  _`Shared helpers` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14492753623188406 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `k` to `kit.py`, `anime.py`, `Box`, `kit_uzumaki.py`, `Shared helpers`, `fabric`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `kit.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11067193675889328 - nodes in this community are weakly interconnected._
- **Why does `Face` connect `paint.py` to `fabric`, `wardrobe.py`, `anime.py`, `Box`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._