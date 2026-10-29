# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 44 files · ~75,097 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 1067 nodes · 2225 edges · 78 communities (58 shown, 20 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 72 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ec38955f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- white_fang_tanto
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
- strip_fabric
- stamp
- cel_box
- kit_rugged.py
- kit_household.py
- kit_shinobi.py
- Garment
- k
- kit_shimura.py
- arm_bone
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
- bandolier
- rot_matrix
- build
- Box
- rnd
- Face
- kit_nara.py
- kit_gekko.py
- kit_haruno.py
- kit_uchiha.py
- bandage_turns
- kit_hagane.py
- leg_bone
- kit_specialist.py
- gathered_ankles
- Layer
- bangs
- belt
- furoshiki
- strap
- bib
- checks
- loose_legs
- open_front
- patch
- towel_at_neck
- straw_sandals
- rolled_cuffs
- stripes
- sashiko
- cane
- hairpin

## God Nodes (most connected - your core abstractions)
1. `k()` - 219 edges
2. `solid()` - 142 edges
3. `fabric()` - 103 edges
4. `strip_fabric()` - 59 edges
5. `stamp()` - 42 edges
6. `rnd()` - 41 edges
7. `cel_box()` - 36 edges
8. `arm_bone()` - 32 edges
9. `Shared helpers` - 32 edges
10. `arm_x()` - 31 edges

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

## Communities (78 total, 20 thin omitted)

### Community 1 - "fabric"
Cohesion: 0.11
Nodes (12): back_crest(), gloves(), head_cloth(), heavy_boots(), arm_protector(), anbu_arms(), flak_vest(), forehead_protector() (+4 more)

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
Cohesion: 0.08
Nodes (13): drawstrings(), forearm_wraps(), holster(), hood_down(), leg_cloth(), ribbed(), sash(), shin_wraps() (+5 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (27): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), How to read this bible, Kindling Bond (+19 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.09
Nodes (11): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), part_line(), side_fringe(), stamp() (+3 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.17
Nodes (5): frog_buttons(), round_bun(), shin_wrap(), wave_lock(), wrap_front()

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "stamp"
Cohesion: 0.16
Nodes (7): How the pieces work, mesh(), tanto(), beak(), bump(), ears(), strap()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.11
Nodes (9): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), sash_vials() (+1 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "strip_fabric"
Cohesion: 0.07
Nodes (15): waist(), body(), cloth_shoes(), kimono_sleeves(), tabi(), arm_warmers(), tabi_boots(), geta() (+7 more)

### Community 17 - "stamp"
Cohesion: 0.09
Nodes (14): stamp(), back_crest(), decal(), shoulder_decal(), slanted_protector(), crest(), back_crest(), crest() (+6 more)

### Community 18 - "cel_box"
Cohesion: 0.13
Nodes (11): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), wrap_front() (+3 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.10
Nodes (10): dread(), knot_bun(), leg_wraps(), patch(), rope(), rope_face(), rope_hair(), shag_box() (+2 more)

### Community 20 - "kit_household.py"
Cohesion: 0.05
Nodes (26): arm_cloth(), bands(), blossom(), checks(), collar_band(), dots(), geta(), ichimatsu() (+18 more)

### Community 21 - "kit_shinobi.py"
Cohesion: 0.09
Nodes (13): shirt(), anbu_plates(), hood_down(), lantern(), lantern_tag(), mantle(), muffler(), plain_body() (+5 more)

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "k"
Cohesion: 0.18
Nodes (10): collar(), flaps(), footwear(), legs(), neckline(), pouch(), roll(), stockings() (+2 more)

### Community 24 - "kit_shimura.py"
Cohesion: 0.29
Nodes (3): back_crest(), bandaged_arm(), bandage()

### Community 25 - "arm_bone"
Cohesion: 0.11
Nodes (14): sleeve_roll(), sode(), arm_bone(), arm_x(), arm_guards(), bracers(), kimono_sleeves(), kimono_sleeves() (+6 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "kit_market.py"
Cohesion: 0.18
Nodes (6): kasuri(), mark(), pocket(), sash(), waist_apron(), grid()

### Community 28 - "rnd"
Cohesion: 0.16
Nodes (7): dark_seams(), hair_box(), hair_face(), hair_shade(), shell(), strip_line(), shade()

### Community 29 - "solid"
Cohesion: 0.08
Nodes (13): holster(), harness(), face_mask(), obi(), mandarin_collar(), coat_skirts(), pauldron(), scarf() (+5 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.08
Nodes (13): blouse(), cargo(), chain(), collar(), gloves(), half_sleeves(), knee_guards(), mesh_arms() (+5 more)

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
Cohesion: 0.18
Nodes (6): bandolier(), crest(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.18
Nodes (4): crest_patch(), seal_script(), seal_tags(), waves()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "kit_tsuchigumo.py"
Cohesion: 0.13
Nodes (8): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 42 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box() (+1 more)

### Community 43 - "kit_namiashi.py"
Cohesion: 0.20
Nodes (5): back_blade(), crest(), hip_kokuto(), kokuto(), wave_band()

### Community 44 - "lock"
Cohesion: 0.11
Nodes (11): Shared helpers, back_fan(), braid(), cel_face(), lock(), sidelocks(), hime_locks(), beard() (+3 more)

### Community 45 - "load_clans"
Cohesion: 0.18
Nodes (9): catalog(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_groups(), load_population(), population_weights() (+1 more)

### Community 47 - "rot_matrix"
Cohesion: 0.18
Nodes (5): wave_lock(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.19
Nodes (8): build(), build_all(), load_marks(), load_module(), main(), natural(), sources(), validate_catalog()

### Community 49 - "Box"
Cohesion: 0.18
Nodes (3): band(), hem(), Box

### Community 50 - "rnd"
Cohesion: 0.11
Nodes (10): ink_clouds(), splatter(), clipped(), camo(), cape(), ragged(), ink_stains(), seal_trim() (+2 more)

### Community 51 - "Face"
Cohesion: 0.22
Nodes (5): button(), darken_rows(), line(), rivets(), Face

### Community 52 - "kit_nara.py"
Cohesion: 0.14
Nodes (8): ring_shell(), crown(), combed_back(), mesh_shirt(), net(), pulled_back(), tuft(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 54 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 55 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 57 - "kit_hagane.py"
Cohesion: 0.21
Nodes (5): spike(), crown(), mace(), plate(), shin_guards()

### Community 58 - "leg_bone"
Cohesion: 0.18
Nodes (6): hakama_legs(), thigh_holster(), leg_bone(), leg_ring(), baggy_legs(), shin_guard()

### Community 59 - "kit_specialist.py"
Cohesion: 0.25
Nodes (3): coat_skirts(), scroll_tube(), shirt()

### Community 62 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

## Knowledge Gaps
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `fabric`, `kit_senju.py`, `solid`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `kit_kunoichi.py`, `kit_aburame.py`, `stamp`, `kit_suzuran.py`, `strip_fabric`, `stamp`, `cel_box`, `kit_rugged.py`, `kit_household.py`, `kit_shinobi.py`, `kit_shimura.py`, `arm_bone`, `kit_yamanaka.py`, `kit_market.py`, `rnd`, `solid`, `kit_field.py`, `kit_shiranui.py`, `kit_uzumaki.py`, `kit_tsuchigumo.py`, `kit_akimichi.py`, `kit_namiashi.py`, `lock`, `Box`, `rnd`, `Face`, `kit_nara.py`, `kit_gekko.py`, `kit_haruno.py`, `kit_uchiha.py`, `bandage_turns`, `kit_hagane.py`, `leg_bone`, `kit_specialist.py`, `gathered_ankles`, `belt`, `furoshiki`, `bib`, `loose_legs`, `patch`, `straw_sandals`, `rolled_cuffs`, `hairpin`?**
  _High betweenness centrality (0.332) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.11396011396011396 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `white_fang_tanto`, `fabric`, `kit_senju.py`, `solid`, `kit_kurama.py`, `kit_kunoichi.py`, `kit_aburame.py`, `stamp`, `kit_suzuran.py`, `strip_fabric`, `stamp`, `cel_box`, `kit_rugged.py`, `kit_household.py`, `kit_shinobi.py`, `k`, `kit_shimura.py`, `arm_bone`, `kit_market.py`, `rnd`, `kit_field.py`, `kit_shiranui.py`, `kit_uzumaki.py`, `kit_tsuchigumo.py`, `kit_akimichi.py`, `kit_namiashi.py`, `lock`, `bandolier`, `Box`, `rnd`, `kit_nara.py`, `kit_gekko.py`, `kit_haruno.py`, `kit_uchiha.py`, `kit_hagane.py`, `leg_bone`, `kit_specialist.py`, `gathered_ankles`, `belt`, `furoshiki`, `strap`, `bib`, `loose_legs`, `towel_at_neck`, `rolled_cuffs`, `cane`, `hairpin`?**
  _High betweenness centrality (0.175) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `lock`, `Story bible`?**
  _High betweenness centrality (0.141) - this node is a cross-community bridge._