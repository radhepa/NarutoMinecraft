# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 45 files · ~75,939 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 1087 nodes · 2269 edges · 58 communities (55 shown, 3 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 72 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e0e7af33`
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
- cel_box
- kit_aburame.py
- solid
- kit_suzuran.py
- 7. Systems in the beta
- kit_umino.py
- stamp
- kit_hyuga.py
- kit_rugged.py
- kit_household.py
- kit_shinobi.py
- Garment
- kit_nara.py
- kit_shimura.py
- arm_x
- k
- kit_market.py
- paint.py
- kit_morino.py
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
- spike
- kit_akimichi.py
- kit_namiashi.py
- lock
- load_clans
- curtain
- rot_matrix
- build
- Box
- chain
- Face
- ring_shell
- kit_gekko.py
- arm_bone
- shade
- kit_hagane.py
- kit_specialist.py

## God Nodes (most connected - your core abstractions)
1. `k()` - 221 edges
2. `solid()` - 144 edges
3. `fabric()` - 105 edges
4. `strip_fabric()` - 59 edges
5. `stamp()` - 45 edges
6. `rnd()` - 41 edges
7. `cel_box()` - 38 edges
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

## Communities (58 total, 3 thin omitted)

### Community 0 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 1 - "fabric"
Cohesion: 0.08
Nodes (21): Shared helpers, body(), collar(), footwear(), leg_ring(), legs(), head_cloth(), arm_protector() (+13 more)

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
Nodes (11): drawstrings(), holster(), hood_down(), leg_cloth(), sash(), side_stripe(), stripes(), turned_hem() (+3 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (27): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), How to read this bible, Kindling Bond (+19 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), kimono_sleeves(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "cel_box"
Cohesion: 0.13
Nodes (8): cel_box(), flick(), topknot(), ear_panels(), round_bun(), wave_lock(), nape_hem(), beard()

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "solid"
Cohesion: 0.12
Nodes (13): How the pieces work, belt(), sash(), obi(), roll(), flak_vest(), tanto(), beak() (+5 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "kit_umino.py"
Cohesion: 0.17
Nodes (5): falling_tail(), knot(), scroll(), surf(), waves()

### Community 17 - "stamp"
Cohesion: 0.09
Nodes (14): stamp(), back_crest(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron() (+6 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.10
Nodes (11): bangs(), tie(), blunt_fringe(), crest(), gathered_tail(), hair_tie(), hakama_legs(), obi() (+3 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "kit_household.py"
Cohesion: 0.06
Nodes (24): flaps(), arm_cloth(), bands(), checks(), cloth_shoes(), collar_band(), dots(), ichimatsu() (+16 more)

### Community 21 - "kit_shinobi.py"
Cohesion: 0.10
Nodes (11): shirt(), vest(), hood_down(), lantern(), mantle(), muffler(), plain_body(), pleats() (+3 more)

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 24 - "kit_shimura.py"
Cohesion: 0.18
Nodes (5): forearm_wraps(), back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "arm_x"
Cohesion: 0.10
Nodes (10): sleeve_roll(), arm_x(), arm_guards(), kimono_sleeves(), arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar() (+2 more)

### Community 26 - "k"
Cohesion: 0.07
Nodes (17): ribbed(), shin_wraps(), tape(), blossom(), geta(), socks(), shin_wrap(), wrap_front() (+9 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+14 more)

### Community 28 - "paint.py"
Cohesion: 0.12
Nodes (12): sprigs(), clipped(), ink_stains(), seal_trim(), cloth_shade(), curls_face(), hair_box(), hair_face() (+4 more)

### Community 29 - "kit_morino.py"
Cohesion: 0.17
Nodes (5): armband(), back_crest(), coat_skirts(), gloves(), heavy_boots()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.10
Nodes (12): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+4 more)

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
Cohesion: 0.18
Nodes (6): bandolier(), crest(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.11
Nodes (9): bun(), clip(), crest_patch(), hairpin(), seal_script(), seal_tags(), waves(), wide_sleeves() (+1 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "spike"
Cohesion: 0.20
Nodes (5): spike(), crown(), burst(), pineapple(), brush_tail()

### Community 42 - "kit_akimichi.py"
Cohesion: 0.12
Nodes (8): gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode(), curls_box()

### Community 43 - "kit_namiashi.py"
Cohesion: 0.20
Nodes (5): back_blade(), crest(), hip_kokuto(), kokuto(), wave_band()

### Community 44 - "lock"
Cohesion: 0.16
Nodes (6): back_fan(), braid(), lock(), sidelocks(), hime_locks(), flicks()

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 47 - "rot_matrix"
Cohesion: 0.18
Nodes (5): wave_lock(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.10
Nodes (5): band(), hem(), strip_line(), Box, Layer

### Community 51 - "Face"
Cohesion: 0.09
Nodes (13): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+5 more)

### Community 52 - "ring_shell"
Cohesion: 0.17
Nodes (6): cel_face(), ring_shell(), crown(), combed_back(), pulled_back(), combed_up()

### Community 53 - "kit_gekko.py"
Cohesion: 0.18
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 54 - "arm_bone"
Cohesion: 0.07
Nodes (17): arm_bone(), arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar() (+9 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.21
Nodes (5): bracers(), harness(), mace(), plate(), shin_guards()

### Community 59 - "kit_specialist.py"
Cohesion: 0.15
Nodes (6): bandolier(), coat_skirts(), cross_armband(), scroll_tube(), shirt(), strap()

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_hatake.py`, `fabric`, `kit_senju.py`, `solid`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `cel_box`, `kit_aburame.py`, `solid`, `kit_suzuran.py`, `kit_umino.py`, `stamp`, `kit_hyuga.py`, `kit_rugged.py`, `kit_household.py`, `kit_shinobi.py`, `kit_nara.py`, `kit_shimura.py`, `arm_x`, `kit_market.py`, `paint.py`, `kit_morino.py`, `kit_field.py`, `kit_shiranui.py`, `kit_uzumaki.py`, `kit_akimichi.py`, `kit_namiashi.py`, `lock`, `Box`, `Face`, `ring_shell`, `kit_gekko.py`, `arm_bone`, `kit_hagane.py`, `kit_specialist.py`?**
  _High betweenness centrality (0.342) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.07682926829268293 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `kit_hatake.py`, `fabric`, `kit_senju.py`, `solid`, `kit_kurama.py`, `kit_aburame.py`, `kit_suzuran.py`, `kit_umino.py`, `stamp`, `kit_hyuga.py`, `kit_rugged.py`, `kit_household.py`, `kit_shinobi.py`, `kit_nara.py`, `kit_shimura.py`, `arm_x`, `k`, `kit_market.py`, `paint.py`, `kit_morino.py`, `kit_field.py`, `kit_shiranui.py`, `kit_uzumaki.py`, `kit_akimichi.py`, `kit_namiashi.py`, `Box`, `Face`, `kit_gekko.py`, `arm_bone`, `kit_hagane.py`, `kit_specialist.py`?**
  _High betweenness centrality (0.163) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `fabric()` connect `fabric` to `kit_hatake.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `kit_aburame.py`, `solid`, `kit_suzuran.py`, `kit_umino.py`, `stamp`, `kit_hyuga.py`, `kit_rugged.py`, `kit_household.py`, `kit_shinobi.py`, `kit_nara.py`, `kit_shimura.py`, `arm_x`, `k`, `kit_market.py`, `paint.py`, `kit_morino.py`, `kit_field.py`, `kit_shiranui.py`, `kit_uzumaki.py`, `kit_namiashi.py`, `Face`, `kit_gekko.py`, `arm_bone`, `kit_hagane.py`, `kit_specialist.py`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._