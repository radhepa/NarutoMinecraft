# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 42 files · ~71,113 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 985 nodes · 2056 edges · 57 communities (52 shown, 5 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 73 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `43f50988`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_hatake.py
- How the pieces work
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
- arm_bone
- kit_yamanaka.py
- kit_hagane.py
- rnd
- kit_uchiha.py
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
- Face
- kit_akimichi.py
- lock
- Shared helpers
- load_clans
- bandolier
- rot_matrix
- build
- Box
- jika_tabi
- shade
- kit_morino.py
- fabric
- shin_wraps
- sash
- wrap_front

## God Nodes (most connected - your core abstractions)
1. `k()` - 190 edges
2. `solid()` - 127 edges
3. `fabric()` - 99 edges
4. `strip_fabric()` - 51 edges
5. `stamp()` - 42 edges
6. `cel_box()` - 34 edges
7. `rnd()` - 33 edges
8. `Shared helpers` - 33 edges
9. `arm_bone()` - 30 edges
10. `arm_x()` - 29 edges

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

## Communities (57 total, 5 thin omitted)

### Community 0 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 1 - "How the pieces work"
Cohesion: 0.18
Nodes (6): How the pieces work, belt(), obi(), roll(), mesh(), tanto()

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
Cohesion: 0.09
Nodes (15): drawstrings(), holster(), hood_down(), leg_cloth(), sash(), side_stripe(), sleeve_roll(), stripes() (+7 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (27): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), How to read this bible, Kindling Bond (+19 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.11
Nodes (10): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw(), ink_stains() (+2 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.06
Nodes (20): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar(), bandage_turns() (+12 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.10
Nodes (9): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), round_bun(), shin_wrap(), tabi_boots(), wave_lock() (+1 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "stamp"
Cohesion: 0.08
Nodes (14): stamp(), back_crest(), crescent(), hip_katana(), katana(), crest(), back_crest(), cross_armband() (+6 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "strip_fabric"
Cohesion: 0.12
Nodes (9): arm_cloth(), cloth_shoes(), trouser_legs(), waist(), kimono_sleeves(), tabi(), gloves(), sandals() (+1 more)

### Community 17 - "kit_sarutobi.py"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "cel_box"
Cohesion: 0.11
Nodes (13): bangs(), braid(), cel_box(), curtain(), tie(), back_sheet(), blunt_fringe(), ear_panels() (+5 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "kit_household.py"
Cohesion: 0.06
Nodes (18): bands(), blossom(), checks(), collar_band(), dots(), geta(), ichimatsu(), kasuri() (+10 more)

### Community 21 - "kit_shinobi.py"
Cohesion: 0.09
Nodes (11): decal(), hood_down(), lantern(), lantern_tag(), mantle(), muffler(), plain_body(), pleats() (+3 more)

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "k"
Cohesion: 0.10
Nodes (14): ribbed(), collar(), flaps(), footwear(), sword_strap(), obi(), legs(), coat_skirts() (+6 more)

### Community 24 - "kit_shimura.py"
Cohesion: 0.18
Nodes (5): forearm_wraps(), back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "arm_bone"
Cohesion: 0.16
Nodes (9): sode(), arm_bone(), arm_x(), arm_guards(), bracers(), kimono_sleeves(), armband(), armband() (+1 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "kit_hagane.py"
Cohesion: 0.22
Nodes (4): spike(), crown(), harness(), burst()

### Community 28 - "rnd"
Cohesion: 0.21
Nodes (5): cloth_shade(), hair_box(), hair_face(), hair_shade(), shell()

### Community 29 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.05
Nodes (22): blouse(), cargo(), chain(), collar(), gloves(), half_sleeves(), holster(), knee_guards() (+14 more)

### Community 32 - "outputs"
Cohesion: 0.17
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+8 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "kit_shiranui.py"
Cohesion: 0.21
Nodes (5): crest(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.12
Nodes (8): bun(), clip(), hairpin(), seal_script(), seal_tags(), waves(), wide_sleeves(), wrap_tie()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Face"
Cohesion: 0.09
Nodes (14): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+6 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box() (+1 more)

### Community 43 - "lock"
Cohesion: 0.12
Nodes (9): lock(), sidelocks(), back_blade(), crest(), hip_kokuto(), kokuto(), wave_lock(), beard() (+1 more)

### Community 44 - "Shared helpers"
Cohesion: 0.14
Nodes (9): Shared helpers, back_fan(), body(), leg_ring(), neckline(), wraps(), sleeves(), band() (+1 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 47 - "rot_matrix"
Cohesion: 0.33
Nodes (3): Piece, piece_corners(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.11
Nodes (3): strip_line(), Box, Layer

### Community 50 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 52 - "kit_morino.py"
Cohesion: 0.14
Nodes (8): cel_face(), ring_shell(), crown(), clipped(), combed_back(), nape_hem(), pulled_back(), scalp()

### Community 53 - "fabric"
Cohesion: 0.12
Nodes (12): shirt(), head_cloth(), arm_protector(), anbu_arms(), anbu_plates(), flak_vest(), forehead_protector(), protector_plate() (+4 more)

## Knowledge Gaps
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_hatake.py`, `How the pieces work`, `kit_senju.py`, `solid`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `kit_kunoichi.py`, `kit_aburame.py`, `stamp`, `kit_suzuran.py`, `strip_fabric`, `kit_sarutobi.py`, `cel_box`, `kit_nara.py`, `kit_household.py`, `kit_shinobi.py`, `kit_shimura.py`, `arm_bone`, `kit_yamanaka.py`, `kit_hagane.py`, `rnd`, `kit_uchiha.py`, `kit_field.py`, `kit_shiranui.py`, `kit_uzumaki.py`, `Face`, `kit_akimichi.py`, `lock`, `Shared helpers`, `jika_tabi`, `kit_morino.py`, `fabric`, `shin_wraps`, `sash`, `wrap_front`?**
  _High betweenness centrality (0.283) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `kit_hatake.py`, `How the pieces work`, `kit_senju.py`, `kit_kurama.py`, `kit_yuhi.py`, `kit_kunoichi.py`, `kit_aburame.py`, `stamp`, `kit_suzuran.py`, `strip_fabric`, `kit_sarutobi.py`, `cel_box`, `kit_nara.py`, `kit_household.py`, `kit_shinobi.py`, `k`, `kit_shimura.py`, `arm_bone`, `kit_hagane.py`, `rnd`, `kit_uchiha.py`, `kit_field.py`, `kit_shiranui.py`, `kit_uzumaki.py`, `Face`, `kit_akimichi.py`, `lock`, `Shared helpers`, `bandolier`, `Box`, `kit_morino.py`, `fabric`, `sash`?**
  _High betweenness centrality (0.177) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.161) - this node is a cross-community bridge._