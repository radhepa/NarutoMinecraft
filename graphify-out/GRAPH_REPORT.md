# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 43 files · ~73,319 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 1031 nodes · 2152 edges · 62 communities (55 shown, 7 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 72 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bdea99db`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_hatake.py
- Shared helpers
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- kit_kurama.py
- rnd
- kit_yuhi.py
- kit_kunoichi.py
- kit_aburame.py
- stamp
- kit_suzuran.py
- 7. Systems in the beta
- strip_fabric
- kit_sarutobi.py
- cel_box
- kit_nara.py
- kit_household.py
- kit_shinobi.py
- Garment
- k
- kit_shimura.py
- fabric
- kit_yamanaka.py
- kit_market.py
- rnd
- solid
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_shiranui.py
- 4. Technical architecture
- 6. The map
- kit_uzumaki.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- kit_tsuchigumo.py
- kit_akimichi.py
- kit_namiashi.py
- lock
- load_clans
- kit_specialist.py
- rot_matrix
- build
- Box
- rnd
- Face
- kit_morino.py
- kit_gekko.py
- hood_down
- side_panels
- bandage_turns
- bands
- stripes
- topknot
- gathered_ankles
- thorn_vine

## God Nodes (most connected - your core abstractions)
1. `k()` - 206 edges
2. `solid()` - 138 edges
3. `fabric()` - 101 edges
4. `strip_fabric()` - 56 edges
5. `stamp()` - 42 edges
6. `rnd()` - 36 edges
7. `cel_box()` - 34 edges
8. `arm_bone()` - 32 edges
9. `Shared helpers` - 32 edges
10. `arm_x()` - 31 edges

## Surprising Connections (you probably didn't know these)
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Shared helpers` --references--> `cel_box()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `lock()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `spike()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `bangs()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (62 total, 7 thin omitted)

### Community 0 - "kit_hatake.py"
Cohesion: 0.20
Nodes (4): decal(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 1 - "Shared helpers"
Cohesion: 0.14
Nodes (11): Shared helpers, How the pieces work, forearm_wraps(), bandage(), flak_vest(), mesh(), sandals(), tanto() (+3 more)

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.07
Nodes (14): back_crest(), drawstrings(), holster(), hood_down(), ribbed(), sash(), shin_wraps(), side_stripe() (+6 more)

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
Cohesion: 0.13
Nodes (9): mist_swirls(), rose(), thorn_band(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock() (+1 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.10
Nodes (10): belt(), arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), shin_wrap(), tabi_boots() (+2 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "stamp"
Cohesion: 0.13
Nodes (9): stamp(), crest(), back_crest(), crest(), beak(), bump(), ears(), plate() (+1 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.11
Nodes (9): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), sash_vials() (+1 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "strip_fabric"
Cohesion: 0.10
Nodes (11): leg_cloth(), body(), arm_cloth(), cloth_shoes(), trouser_legs(), waist(), tabi(), gloves() (+3 more)

### Community 17 - "kit_sarutobi.py"
Cohesion: 0.22
Nodes (5): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey()

### Community 18 - "cel_box"
Cohesion: 0.09
Nodes (16): bangs(), braid(), cel_box(), cel_face(), curtain(), tie(), back_sheet(), blunt_fringe() (+8 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "kit_household.py"
Cohesion: 0.08
Nodes (14): blossom(), checks(), collar_band(), dots(), geta(), ichimatsu(), jika_tabi(), kasuri() (+6 more)

### Community 21 - "kit_shinobi.py"
Cohesion: 0.10
Nodes (11): shirt(), vest(), anbu_plates(), shirt(), decal(), lantern(), lantern_tag(), plain_body() (+3 more)

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "k"
Cohesion: 0.11
Nodes (14): collar(), flaps(), footwear(), face_mask(), sash(), legs(), sash(), neckline() (+6 more)

### Community 24 - "kit_shimura.py"
Cohesion: 0.20
Nodes (3): back_crest(), bandaged_arm(), cane()

### Community 25 - "fabric"
Cohesion: 0.05
Nodes (30): sode(), arm_bone(), arm_x(), arm_guards(), bracers(), harness(), mace(), plate() (+22 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "kit_market.py"
Cohesion: 0.06
Nodes (17): checks(), dots(), furoshiki(), geta(), jika_tabi(), kasuri(), kyahan(), mark() (+9 more)

### Community 28 - "rnd"
Cohesion: 0.15
Nodes (8): button(), dark_seams(), hair_box(), hair_face(), hair_shade(), shell(), strip_line(), shade()

### Community 29 - "solid"
Cohesion: 0.05
Nodes (21): lames(), snack_pouch(), mandarin_collar(), obi(), brush_pin(), bib(), waist_apron(), coat_skirts() (+13 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.06
Nodes (20): blouse(), cargo(), chain(), collar(), gloves(), half_sleeves(), holster(), knee_guards() (+12 more)

### Community 32 - "outputs"
Cohesion: 0.22
Nodes (11): hex_rgb(), json_text(), load_eye_colors(), load_hair_colors(), load_palettes(), outputs(), png_bytes(), ramp() (+3 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "kit_shiranui.py"
Cohesion: 0.14
Nodes (8): arm_protector(), protector_plate(), backward_bandana(), bandolier(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.18
Nodes (5): bun(), crest_patch(), seal_script(), seal_tags(), waves()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 42 - "kit_akimichi.py"
Cohesion: 0.14
Nodes (7): flick(), gourd(), puff(), quilt(), shoku_disc(), curls_box(), curls_face()

### Community 43 - "kit_namiashi.py"
Cohesion: 0.20
Nodes (5): back_blade(), crest(), hip_kokuto(), kokuto(), wave_band()

### Community 44 - "lock"
Cohesion: 0.17
Nodes (6): back_fan(), lock(), sidelocks(), hime_locks(), beard(), flicks()

### Community 45 - "load_clans"
Cohesion: 0.18
Nodes (9): catalog(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_groups(), load_population(), population_weights() (+1 more)

### Community 46 - "kit_specialist.py"
Cohesion: 0.29
Nodes (3): bandolier(), cross_armband(), strap()

### Community 47 - "rot_matrix"
Cohesion: 0.18
Nodes (5): wave_lock(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.19
Nodes (8): build(), build_all(), load_marks(), load_module(), main(), natural(), sources(), validate_catalog()

### Community 50 - "rnd"
Cohesion: 0.12
Nodes (9): sprigs(), fur_edge(), ink_clouds(), splatter(), wisteria_hem(), ink_stains(), seal_trim(), cloth_shade() (+1 more)

### Community 51 - "Face"
Cohesion: 0.27
Nodes (3): darken_rows(), rivets(), Face

### Community 52 - "kit_morino.py"
Cohesion: 0.13
Nodes (9): ring_shell(), crown(), clipped(), combed_back(), head_cloth(), nape_hem(), pulled_back(), forehead_protector() (+1 more)

### Community 53 - "kit_gekko.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 54 - "hood_down"
Cohesion: 0.33
Nodes (3): hood_down(), mantle(), pleats()

### Community 55 - "side_panels"
Cohesion: 0.40
Nodes (3): robe_skirt(), skirt(), side_panels()

## Knowledge Gaps
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_hatake.py`, `Shared helpers`, `kit_senju.py`, `solid`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `kit_kunoichi.py`, `kit_aburame.py`, `stamp`, `kit_suzuran.py`, `strip_fabric`, `kit_sarutobi.py`, `cel_box`, `kit_nara.py`, `kit_household.py`, `kit_shinobi.py`, `kit_shimura.py`, `fabric`, `kit_yamanaka.py`, `kit_market.py`, `rnd`, `solid`, `kit_field.py`, `kit_shiranui.py`, `kit_uzumaki.py`, `kit_tsuchigumo.py`, `kit_akimichi.py`, `kit_namiashi.py`, `lock`, `kit_specialist.py`, `rnd`, `Face`, `kit_morino.py`, `kit_gekko.py`, `hood_down`, `bandage_turns`, `gathered_ankles`, `thorn_vine`?**
  _High betweenness centrality (0.317) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `Shared helpers` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `kit_hatake.py`, `Shared helpers`, `kit_senju.py`, `solid`, `kit_kurama.py`, `kit_kunoichi.py`, `kit_aburame.py`, `stamp`, `kit_suzuran.py`, `strip_fabric`, `kit_sarutobi.py`, `cel_box`, `kit_nara.py`, `kit_household.py`, `kit_shinobi.py`, `k`, `kit_shimura.py`, `fabric`, `kit_market.py`, `rnd`, `kit_field.py`, `kit_shiranui.py`, `kit_uzumaki.py`, `kit_tsuchigumo.py`, `kit_akimichi.py`, `kit_namiashi.py`, `kit_specialist.py`, `Box`, `kit_morino.py`, `kit_gekko.py`, `hood_down`, `side_panels`, `gathered_ankles`?**
  _High betweenness centrality (0.177) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._