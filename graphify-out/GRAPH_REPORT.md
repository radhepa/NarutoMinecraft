# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 36 files · ~62,326 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 808 nodes · 1665 edges · 42 communities (37 shown, 5 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 76 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `15cecb79`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- paint.py
- fabric
- wardrobe.py
- kit_senju.py
- render.py
- living_eyes.py
- strip_fabric
- Story bible
- kit_kurama.py
- rnd
- kit_yuhi.py
- Shared helpers
- k
- forehead_protector
- kit_suzuran.py
- 7. Systems in the beta
- kit_uzumaki.py
- kit_hatake.py
- kit_hyuga.py
- mesh_shirt
- kit_akimichi.py
- kit_tobari.py
- Box
- stamp
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- kit_hagane.py
- rnd
- solid
- 5. Data formats built for the whole story
- kit_namiashi.py
- bandage
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_gekko.py
- 4. Technical architecture
- 6. The map
- arm_bone
- 8. The beta, chapter by chapter
- 9. Delivery plan
- back_crest

## God Nodes (most connected - your core abstractions)
1. `k()` - 141 edges
2. `solid()` - 92 edges
3. `fabric()` - 76 edges
4. `stamp()` - 36 edges
5. `Shared helpers` - 34 edges
6. `cel_box()` - 29 edges
7. `rnd()` - 28 edges
8. `strip_fabric()` - 28 edges
9. `Box` - 25 edges
10. `Face` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `wraps()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit_shinobi.py
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Shared helpers` --references--> `cel_box()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `lock()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `spike()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (42 total, 5 thin omitted)

### Community 0 - "paint.py"
Cohesion: 0.05
Nodes (25): puff(), drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web() (+17 more)

### Community 1 - "fabric"
Cohesion: 0.14
Nodes (8): crest(), back_crest(), arm_protector(), protector_plate(), beak(), bump(), plate(), fabric()

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

### Community 6 - "strip_fabric"
Cohesion: 0.14
Nodes (9): kimono_sleeves(), heavy_boots(), anbu_arms(), anbu_plates(), flak_vest(), sandals(), wraps(), waistband() (+1 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (27): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), How to read this bible, Kindling Bond (+19 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.10
Nodes (10): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), part_line(), side_fringe(), stamp() (+2 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.06
Nodes (19): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar(), bandage_turns() (+11 more)

### Community 11 - "Shared helpers"
Cohesion: 0.12
Nodes (12): Shared helpers, body(), flaps(), footwear(), leg_ring(), legs(), neckline(), pouch() (+4 more)

### Community 12 - "k"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "kit_uzumaki.py"
Cohesion: 0.13
Nodes (7): bun(), clip(), hairpin(), seal_script(), seal_tags(), waves(), wrap_tie()

### Community 17 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.08
Nodes (19): back_fan(), bangs(), braid(), cel_box(), curtain(), lock(), sidelocks(), spike() (+11 more)

### Community 20 - "kit_akimichi.py"
Cohesion: 0.17
Nodes (5): flick(), lames(), quilt(), shoku_disc(), snack_pouch()

### Community 21 - "kit_tobari.py"
Cohesion: 0.12
Nodes (10): hood_down(), lantern(), mantle(), muffler(), plain_body(), pleats(), sash(), shin_wraps() (+2 more)

### Community 22 - "Box"
Cohesion: 0.07
Nodes (11): wave_lock(), band(), hem(), Box, Garment, key_rgba(), Layer, Piece (+3 more)

### Community 23 - "stamp"
Cohesion: 0.10
Nodes (12): stamp(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf() (+4 more)

### Community 25 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "kit_hagane.py"
Cohesion: 0.13
Nodes (11): bracers(), crown(), mace(), plate(), shin_guards(), hakama_legs(), obi(), tabi() (+3 more)

### Community 28 - "rnd"
Cohesion: 0.09
Nodes (14): cel_face(), ring_shell(), crown(), ink_clouds(), splatter(), wisteria_hem(), clipped(), coat_skirts() (+6 more)

### Community 29 - "solid"
Cohesion: 0.17
Nodes (9): How the pieces work, gourd(), belt(), collar(), harness(), tanto(), ears(), strap() (+1 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_namiashi.py"
Cohesion: 0.20
Nodes (5): back_blade(), crest(), hip_kokuto(), kokuto(), wave_band()

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

### Community 38 - "arm_bone"
Cohesion: 0.16
Nodes (9): sode(), arm_bone(), arm_x(), kimono_sleeves(), armband(), roll(), armband(), arm_warmers() (+1 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

## Knowledge Gaps
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `kit_hagane.py` to `paint.py`, `fabric`, `kit_senju.py`, `strip_fabric`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `Shared helpers`, `k`, `forehead_protector`, `kit_suzuran.py`, `kit_uzumaki.py`, `kit_hatake.py`, `kit_hyuga.py`, `kit_akimichi.py`, `kit_tobari.py`, `Box`, `stamp`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `rnd`, `solid`, `kit_namiashi.py`, `kit_gekko.py`, `arm_bone`?**
  _High betweenness centrality (0.250) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `paint.py` be split into smaller, more focused modules?**
  _Cohesion score 0.054354178842782 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `wardrobe.py` to `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.182) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.13970588235294118 - nodes in this community are weakly interconnected._
- **Why does `Shinobi Modpack: roadmap` connect `Shinobi Modpack: roadmap` to `11. Later systems`, `4. Technical architecture`, `6. The map`, `Story bible`, `8. The beta, chapter by chapter`, `9. Delivery plan`, `7. Systems in the beta`, `5. Data formats built for the whole story`?**
  _High betweenness centrality (0.174) - this node is a cross-community bridge._