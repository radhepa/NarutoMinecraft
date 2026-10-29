# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 30 files · ~56,071 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 695 nodes · 1411 edges · 42 communities (40 shown, 2 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 76 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bed51259`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- masks.py
- wardrobe.py
- kit_senju.py
- render.py
- living_eyes.py
- kit_shinobi.py
- Story bible
- kit_kurama.py
- rnd
- kit_yuhi.py
- fabric
- k
- forehead_protector
- bandage_turns
- 7. Systems in the beta
- kit_uzumaki.py
- solid
- kit_hyuga.py
- kit_nara.py
- kit_akimichi.py
- anime.py
- Box
- stamp
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- kit_hagane.py
- anime.py
- k
- 5. Data formats built for the whole story
- rnd
- bangs
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_gekko.py
- 4. Technical architecture
- 6. The map
- arm_x
- 8. The beta, chapter by chapter
- 9. Delivery plan
- math

## God Nodes (most connected - your core abstractions)
1. `k()` - 107 edges
2. `solid()` - 71 edges
3. `fabric()` - 58 edges
4. `Shared helpers` - 34 edges
5. `cel_box()` - 27 edges
6. `stamp()` - 27 edges
7. `rnd()` - 26 edges
8. `Box` - 25 edges
9. `strip_fabric()` - 22 edges
10. `Face` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
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

## Communities (42 total, 2 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.08
Nodes (18): puff(), band(), button(), curls_box(), curls_face(), dark_seams(), darken_rows(), grid() (+10 more)

### Community 1 - "masks.py"
Cohesion: 0.19
Nodes (7): How the pieces work, tanto(), beak(), bump(), ears(), plate(), strap()

### Community 2 - "wardrobe.py"
Cohesion: 0.06
Nodes (42): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+34 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_shinobi.py"
Cohesion: 0.22
Nodes (5): anbu_plates(), flak_vest(), mesh(), sandals(), cap()

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (27): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), How to read this bible, Kindling Bond (+19 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.11
Nodes (9): back_crest(), bead_clip(), brush_stroke(), bun(), part_line(), side_fringe(), stamp(), wave_lock() (+1 more)

### Community 9 - "rnd"
Cohesion: 0.11
Nodes (9): spike(), crown(), burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_face() (+1 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.14
Nodes (8): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_fan(), wave_lock()

### Community 11 - "fabric"
Cohesion: 0.16
Nodes (9): body(), footwear(), crest(), legs(), anbu_arms(), sleeves(), waistband(), fabric() (+1 more)

### Community 12 - "k"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "forehead_protector"
Cohesion: 0.33
Nodes (3): arm_protector(), forehead_protector(), protector_plate()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.12
Nodes (8): bun(), clip(), hairpin(), seal_script(), seal_tags(), waves(), wide_sleeves(), wrap_tie()

### Community 17 - "solid"
Cohesion: 0.13
Nodes (8): face_mask(), obi(), brush_pin(), pauldron(), scarf(), trench_knife(), side_panels(), solid()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.13
Nodes (11): cel_box(), curtain(), tie(), flick(), back_sheet(), ear_panels(), gathered_tail(), hair_tie() (+3 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "kit_akimichi.py"
Cohesion: 0.17
Nodes (5): gourd(), lames(), quilt(), shoku_disc(), snack_pouch()

### Community 21 - "anime.py"
Cohesion: 0.14
Nodes (9): Shared helpers, back_fan(), braid(), cel_face(), lock(), sidelocks(), hime_locks(), beard() (+1 more)

### Community 22 - "Box"
Cohesion: 0.07
Nodes (8): Box, Garment, key_rgba(), Layer, Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 23 - "stamp"
Cohesion: 0.11
Nodes (11): stamp(), decal(), shoulder_decal(), slanted_protector(), white_fang_tanto(), crest(), crest_patch(), flame_hem() (+3 more)

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.15
Nodes (9): arm_bone(), arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar() (+1 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "kit_hagane.py"
Cohesion: 0.15
Nodes (8): bracers(), harness(), mace(), plate(), shin_guards(), hakama_legs(), leg_bone(), leg_ring()

### Community 28 - "anime.py"
Cohesion: 0.29
Nodes (4): ring_shell(), crown(), pulled_back(), scalp()

### Community 29 - "k"
Cohesion: 0.22
Nodes (8): belt(), collar(), flaps(), neckline(), pouch(), roll(), stockings(), k()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "rnd"
Cohesion: 0.18
Nodes (6): fur_edge(), ink_clouds(), splatter(), wisteria_hem(), cloth_shade(), rnd()

### Community 32 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "kit_gekko.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "arm_x"
Cohesion: 0.25
Nodes (4): sode(), arm_x(), kimono_sleeves(), kimono_sleeves()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `paint.py`, `masks.py`, `kit_senju.py`, `kit_shinobi.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `fabric`, `k`, `forehead_protector`, `bandage_turns`, `kit_uzumaki.py`, `solid`, `kit_hyuga.py`, `kit_nara.py`, `kit_akimichi.py`, `anime.py`, `stamp`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `kit_hagane.py`, `anime.py`, `rnd`, `kit_gekko.py`, `arm_x`, `math`?**
  _High betweenness centrality (0.202) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.080338266384778 - nodes in this community are weakly interconnected._
- **Why does `Shinobi Modpack: roadmap` connect `Shinobi Modpack: roadmap` to `11. Later systems`, `4. Technical architecture`, `6. The map`, `Story bible`, `8. The beta, chapter by chapter`, `9. Delivery plan`, `7. Systems in the beta`, `5. Data formats built for the whole story`?**
  _High betweenness centrality (0.201) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `wardrobe.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06196291270918137 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `wardrobe.py` to `anime.py`, `Story bible`?**
  _High betweenness centrality (0.201) - this node is a cross-community bridge._