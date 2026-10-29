# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 28 files · ~35,074 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 629 nodes · 1362 edges · 41 communities (31 shown, 10 thin omitted)
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
- cel_box
- render.py
- living_eyes.py
- kit.py
- Clans
- kit_kurama.py
- rnd
- kit_yuhi.py
- strip_fabric
- k
- How the pieces work
- Clans
- Shared helpers
- k
- fabric
- kit_hyuga.py
- kit_household.py
- Garment
- load_clans
- main
- Piece
- kit_senju.py
- kit_uzumaki.py
- kit_yamanaka.py
- flaps
- anime.py
- jika_tabi
- spike
- curtain
- arm_cloth
- blossom
- checks
- collar_band
- dots
- geta
- ichimatsu
- kasuri
- topknot

## God Nodes (most connected - your core abstractions)
1. `k()` - 112 edges
2. `solid()` - 69 edges
3. `fabric()` - 60 edges
4. `Shared helpers` - 34 edges
5. `strip_fabric()` - 30 edges
6. `cel_box()` - 29 edges
7. `rnd()` - 28 edges
8. `stamp()` - 27 edges
9. `Box` - 25 edges
10. `Face` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `cel_box()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `spike()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `bangs()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `ring_shell()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `curtain()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (41 total, 10 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.06
Nodes (19): band(), button(), cloth_shade(), curls_face(), dark_seams(), darken_rows(), grid(), hair_box() (+11 more)

### Community 1 - "kit_shinobi.py"
Cohesion: 0.20
Nodes (6): pouch(), anbu_plates(), flak_vest(), forehead_protector(), mesh(), cap()

### Community 2 - "wardrobe.py"
Cohesion: 0.17
Nodes (15): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+7 more)

### Community 3 - "cel_box"
Cohesion: 0.18
Nodes (6): cel_box(), ear_panels(), tuft(), beard(), bun(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit.py"
Cohesion: 0.14
Nodes (8): footwear(), hakama_legs(), leg_bone(), leg_ring(), legs(), neckline(), stockings(), waistband()

### Community 7 - "Clans"
Cohesion: 0.17
Nodes (9): Commits, graphify, Naruto Minecraft, ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft (+1 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (12): back_crest(), bead_clip(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe(), splatter() (+4 more)

### Community 9 - "rnd"
Cohesion: 0.14
Nodes (8): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw(), rnd()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "strip_fabric"
Cohesion: 0.12
Nodes (9): body(), cloth_shoes(), trouser_legs(), waist(), tabi(), anbu_arms(), sandals(), sleeves() (+1 more)

### Community 12 - "k"
Cohesion: 0.22
Nodes (3): deep_hood(), high_collar(), hood_down()

### Community 13 - "How the pieces work"
Cohesion: 0.15
Nodes (8): How the pieces work, belt(), collar(), roll(), tanto(), bump(), ears(), strap()

### Community 14 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 15 - "Shared helpers"
Cohesion: 0.17
Nodes (8): Shared helpers, back_fan(), braid(), cel_face(), lock(), sidelocks(), hime_locks(), wraps()

### Community 16 - "k"
Cohesion: 0.09
Nodes (17): lenses(), lames(), snack_pouch(), face_mask(), sash(), kimono_sleeves(), obi(), brush_pin() (+9 more)

### Community 17 - "fabric"
Cohesion: 0.05
Nodes (26): stamp(), crescent(), hip_katana(), katana(), sword_strap(), decal(), shoulder_decal(), slanted_protector() (+18 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.17
Nodes (7): bangs(), tie(), blunt_fringe(), gathered_tail(), hair_tie(), parted_fringe(), wrap_front()

### Community 19 - "kit_household.py"
Cohesion: 0.15
Nodes (7): bands(), overlap(), socks(), sprigs(), stripes(), trim(), wide_sleeves()

### Community 20 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 21 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 22 - "main"
Cohesion: 0.24
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 23 - "Piece"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 24 - "kit_senju.py"
Cohesion: 0.28
Nodes (3): lames(), plate(), shoulder_guards()

### Community 25 - "kit_uzumaki.py"
Cohesion: 0.05
Nodes (23): flick(), gourd(), puff(), quilt(), shoku_disc(), sode(), arm_bone(), arm_x() (+15 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 28 - "anime.py"
Cohesion: 0.19
Nodes (6): ring_shell(), crown(), mesh_shirt(), net(), pulled_back(), scalp()

### Community 29 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 30 - "spike"
Cohesion: 0.33
Nodes (3): spike(), burst(), pineapple()

## Knowledge Gaps
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `kit_shinobi.py`, `cel_box`, `kit.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `strip_fabric`, `k`, `How the pieces work`, `Shared helpers`, `fabric`, `kit_hyuga.py`, `kit_household.py`, `kit_senju.py`, `kit_uzumaki.py`, `kit_yamanaka.py`, `flaps`, `anime.py`, `jika_tabi`, `blossom`, `geta`?**
  _High betweenness centrality (0.255) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05727644652250146 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `k` to `paint.py`, `kit_shinobi.py`, `kit.py`, `kit_kurama.py`, `strip_fabric`, `k`, `How the pieces work`, `Shared helpers`, `fabric`, `kit_hyuga.py`, `kit_household.py`, `kit_senju.py`, `kit_uzumaki.py`, `flaps`, `anime.py`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `arm_cloth`, `kit_shinobi.py`, `paint.py`, `kit.py`, `kit_kurama.py`, `strip_fabric`, `k`, `How the pieces work`, `Shared helpers`, `k`, `kit_hyuga.py`, `kit_household.py`, `kit_senju.py`, `kit_uzumaki.py`, `kit_yamanaka.py`, `anime.py`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._