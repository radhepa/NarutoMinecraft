# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 46 files · ~77,494 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 1115 nodes · 2330 edges · 63 communities (52 shown, 11 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 72 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7b0a34dd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_hatake.py
- fabric
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
- waves
- stamp
- cel_box
- kit_rugged.py
- kit_household.py
- kit_shinobi.py
- Garment
- kit_nara.py
- kit_shimura.py
- arm_bone
- k
- kit_market.py
- kit_kinoshita.py
- strip_fabric
- 5. Data formats built for the whole story
- leg_bone
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_shiranui.py
- 4. Technical architecture
- 6. The map
- kit_uzumaki.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- kit_yamanaka.py
- lames
- kit_namiashi.py
- flaps
- load_clans
- belt
- rot_matrix
- build
- Box
- kit_field.py
- Face
- ring_shell
- kit_gekko.py
- forehead_protector
- shin_wraps
- sash
- plate
- coat_skirts
- kit_specialist.py
- scroll_tube
- muffler
- surf

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `solid()` - 152 edges
3. `fabric()` - 109 edges
4. `strip_fabric()` - 59 edges
5. `stamp()` - 47 edges
6. `rnd()` - 43 edges
7. `cel_box()` - 38 edges
8. `arm_bone()` - 32 edges
9. `Shared helpers` - 32 edges
10. `arm_x()` - 31 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `wraps()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit_shinobi.py
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Shared helpers` --references--> `ring_shell()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `body()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py
- `Shared helpers` --references--> `neckline()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit.py

## Import Cycles
- None detected.

## Communities (63 total, 11 thin omitted)

### Community 0 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 1 - "fabric"
Cohesion: 0.11
Nodes (13): body(), collar(), footwear(), legs(), sleeves(), arm_crest(), back_crest(), chest_crest() (+5 more)

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
Nodes (19): drawstrings(), holster(), hood_down(), sash(), side_stripe(), sleeve_roll(), stripes(), turned_hem() (+11 more)

### Community 7 - "Story bible"
Cohesion: 0.05
Nodes (33): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), How to read this bible, Kindling Bond (+25 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): flick(), quilt(), back_crest(), brush_stroke(), bun(), ink_clouds(), side_fringe(), splatter() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.06
Nodes (19): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar(), bandage_turns() (+11 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.25
Nodes (3): frog_buttons(), round_bun(), wave_lock()

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "stamp"
Cohesion: 0.09
Nodes (12): stamp(), back_crest(), shoku_disc(), crest(), back_crest(), decal(), lantern_tag(), dolphin() (+4 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 17 - "stamp"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 18 - "cel_box"
Cohesion: 0.08
Nodes (22): Shared helpers, back_fan(), bangs(), braid(), cel_box(), curtain(), lock(), sidelocks() (+14 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (16): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+8 more)

### Community 20 - "kit_household.py"
Cohesion: 0.06
Nodes (20): arm_cloth(), bands(), checks(), cloth_shoes(), collar_band(), dots(), ichimatsu(), jika_tabi() (+12 more)

### Community 21 - "kit_shinobi.py"
Cohesion: 0.14
Nodes (9): shirt(), pouch(), hood_down(), lantern(), mantle(), plain_body(), pleats(), split_toe_boots() (+1 more)

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 24 - "kit_shimura.py"
Cohesion: 0.15
Nodes (5): forearm_wraps(), back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "arm_bone"
Cohesion: 0.10
Nodes (14): sode(), arm_bone(), arm_x(), arm_guards(), bracers(), crown(), kimono_sleeves(), kimono_sleeves() (+6 more)

### Community 26 - "k"
Cohesion: 0.04
Nodes (25): ribbed(), snack_pouch(), collar(), tape(), blossom(), geta(), socks(), obi() (+17 more)

### Community 27 - "kit_market.py"
Cohesion: 0.06
Nodes (18): bib(), checks(), dots(), furoshiki(), geta(), jika_tabi(), kasuri(), kyahan() (+10 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "strip_fabric"
Cohesion: 0.09
Nodes (12): leg_cloth(), waist(), tabi_boots(), sleeves(), gloves(), heavy_boots(), anbu_arms(), anbu_plates() (+4 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "leg_bone"
Cohesion: 0.08
Nodes (13): blouse(), cargo(), holster(), knee_guards(), pocket(), hakama_legs(), thigh_holster(), leg_bone() (+5 more)

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
Cohesion: 0.11
Nodes (10): arm_protector(), protector_plate(), backward_bandana(), bandolier(), crest(), flicks(), mouth_senbon(), senbon() (+2 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.24
Nodes (4): bun(), seal_script(), seal_tags(), wide_sleeves()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 43 - "kit_namiashi.py"
Cohesion: 0.20
Nodes (5): back_blade(), crest(), hip_kokuto(), kokuto(), wave_band()

### Community 44 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 47 - "rot_matrix"
Cohesion: 0.18
Nodes (5): wave_lock(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 50 - "kit_field.py"
Cohesion: 0.13
Nodes (7): chain(), gloves(), half_sleeves(), mesh_arms(), shirt(), trousers(), vest()

### Community 51 - "Face"
Cohesion: 0.05
Nodes (27): puff(), drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web() (+19 more)

### Community 52 - "ring_shell"
Cohesion: 0.13
Nodes (9): cel_face(), ring_shell(), crown(), clipped(), combed_back(), nape_hem(), pulled_back(), combed_up() (+1 more)

### Community 53 - "kit_gekko.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 57 - "plate"
Cohesion: 0.33
Nodes (3): mace(), plate(), shin_guards()

### Community 59 - "kit_specialist.py"
Cohesion: 0.18
Nodes (5): bandolier(), ink_stains(), seal_trim(), shirt(), strap()

## Knowledge Gaps
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_hatake.py`, `fabric`, `kit_senju.py`, `solid`, `Story bible`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `kit_kunoichi.py`, `kit_aburame.py`, `stamp`, `kit_suzuran.py`, `stamp`, `cel_box`, `kit_rugged.py`, `kit_household.py`, `kit_shinobi.py`, `kit_nara.py`, `kit_shimura.py`, `arm_bone`, `kit_market.py`, `kit_kinoshita.py`, `strip_fabric`, `leg_bone`, `kit_shiranui.py`, `kit_uzumaki.py`, `kit_yamanaka.py`, `lames`, `kit_namiashi.py`, `flaps`, `belt`, `kit_field.py`, `Face`, `ring_shell`, `kit_gekko.py`, `forehead_protector`, `shin_wraps`, `sash`, `plate`, `coat_skirts`, `kit_specialist.py`, `scroll_tube`, `muffler`?**
  _High betweenness centrality (0.317) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.11375661375661375 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `kit_hatake.py`, `fabric`, `kit_senju.py`, `Story bible`, `kit_kurama.py`, `kit_yuhi.py`, `kit_kunoichi.py`, `kit_aburame.py`, `stamp`, `kit_suzuran.py`, `stamp`, `cel_box`, `kit_rugged.py`, `kit_household.py`, `kit_shinobi.py`, `kit_nara.py`, `kit_shimura.py`, `arm_bone`, `k`, `kit_market.py`, `kit_kinoshita.py`, `strip_fabric`, `leg_bone`, `kit_shiranui.py`, `kit_uzumaki.py`, `lames`, `kit_namiashi.py`, `flaps`, `belt`, `Box`, `kit_field.py`, `Face`, `ring_shell`, `kit_gekko.py`, `forehead_protector`, `sash`, `plate`, `coat_skirts`, `kit_specialist.py`, `scroll_tube`, `muffler`?**
  _High betweenness centrality (0.185) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `kit_hatake.py`, `kit_senju.py`, `solid`, `Story bible`, `kit_kurama.py`, `kit_yuhi.py`, `kit_kunoichi.py`, `kit_aburame.py`, `stamp`, `kit_suzuran.py`, `stamp`, `cel_box`, `kit_rugged.py`, `kit_household.py`, `kit_shinobi.py`, `kit_nara.py`, `kit_shimura.py`, `arm_bone`, `k`, `kit_market.py`, `kit_kinoshita.py`, `strip_fabric`, `kit_shiranui.py`, `kit_uzumaki.py`, `kit_yamanaka.py`, `kit_namiashi.py`, `kit_field.py`, `Face`, `ring_shell`, `kit_gekko.py`, `forehead_protector`, `plate`, `kit_specialist.py`?**
  _High betweenness centrality (0.140) - this node is a cross-community bridge._