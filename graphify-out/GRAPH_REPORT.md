# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 39 files · ~66,353 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 894 nodes · 1866 edges · 55 communities (49 shown, 6 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 73 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d354f7db`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_tsuchigumo.py
- kit_shinobi.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- rnd
- kit_yuhi.py
- kit.py
- kit_aburame.py
- kit_haruno.py
- kit_suzuran.py
- 7. Systems in the beta
- fabric
- kit_hatake.py
- kit_hyuga.py
- kit_nara.py
- snack_pouch
- kit_tobari.py
- Garment
- kit_sarutobi.py
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- kit_hagane.py
- kit_morino.py
- k
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- stamp
- 4. Technical architecture
- 6. The map
- arm_bone
- 8. The beta, chapter by chapter
- 9. Delivery plan
- Box
- rnd
- kokuto
- lock
- load_clans
- cel_box
- rot_matrix
- build
- bandage_turns
- spike
- curtain
- protector_plate
- coat_skirts
- hairpin

## God Nodes (most connected - your core abstractions)
1. `k()` - 168 edges
2. `solid()` - 115 edges
3. `fabric()` - 89 edges
4. `stamp()` - 40 edges
5. `strip_fabric()` - 40 edges
6. `Shared helpers` - 33 edges
7. `rnd()` - 31 edges
8. `cel_box()` - 29 edges
9. `arm_bone()` - 26 edges
10. `arm_x()` - 25 edges

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

## Communities (55 total, 6 thin omitted)

### Community 0 - "kit_tsuchigumo.py"
Cohesion: 0.13
Nodes (8): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 1 - "kit_shinobi.py"
Cohesion: 0.14
Nodes (8): How the pieces work, belt(), flak_vest(), mesh(), tanto(), wraps(), beak(), ears()

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

### Community 6 - "kit_academy.py"
Cohesion: 0.08
Nodes (17): drawstrings(), holster(), hood_down(), sash(), side_stripe(), sleeve_roll(), stripes(), turned_hem() (+9 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (27): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), How to read this bible, Kindling Bond (+19 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "kit.py"
Cohesion: 0.10
Nodes (15): Shared helpers, body(), collar(), flaps(), footwear(), leg_ring(), legs(), neckline() (+7 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_haruno.py"
Cohesion: 0.11
Nodes (9): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar(), wave_lock() (+1 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.14
Nodes (7): back_crest(), bell_hem(), bell_print(), bell_sprig(), herb_pouch(), sash_vials(), vial()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "fabric"
Cohesion: 0.11
Nodes (13): leg_cloth(), shirt(), waist(), half_sleeves(), shirt(), trousers(), kimono_sleeves(), gloves() (+5 more)

### Community 17 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.11
Nodes (10): bangs(), tie(), blunt_fringe(), crest(), gathered_tail(), hair_tie(), obi(), parted_fringe() (+2 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 21 - "kit_tobari.py"
Cohesion: 0.10
Nodes (10): decal(), hood_down(), lantern(), lantern_tag(), mantle(), muffler(), pleats(), sash() (+2 more)

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_sarutobi.py"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 24 - "kit_shimura.py"
Cohesion: 0.18
Nodes (5): forearm_wraps(), back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.19
Nodes (6): arm_crest(), back_crest(), chest_crest(), crest(), lamellar(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "kit_hagane.py"
Cohesion: 0.27
Nodes (4): bracers(), mace(), plate(), shin_guards()

### Community 28 - "kit_morino.py"
Cohesion: 0.13
Nodes (9): ring_shell(), crown(), back_crest(), clipped(), combed_back(), head_cloth(), pulled_back(), forehead_protector() (+1 more)

### Community 29 - "k"
Cohesion: 0.06
Nodes (17): ribbed(), shin_wraps(), lames(), shoku_disc(), sword_strap(), coat_skirts(), wave_band(), scroll_tube() (+9 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.08
Nodes (14): blouse(), cargo(), chain(), collar(), gloves(), holster(), knee_guards(), mesh_arms() (+6 more)

### Community 32 - "outputs"
Cohesion: 0.17
Nodes (15): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+7 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "stamp"
Cohesion: 0.13
Nodes (8): stamp(), back_crest(), crescent(), hip_katana(), katana(), crest_patch(), bump(), plate()

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "arm_bone"
Cohesion: 0.11
Nodes (13): sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), armband(), roll(), cross_armband() (+5 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Box"
Cohesion: 0.06
Nodes (20): puff(), band(), button(), curls_box(), curls_face(), dark_seams(), darken_rows(), grid() (+12 more)

### Community 42 - "rnd"
Cohesion: 0.19
Nodes (5): quilt(), ink_stains(), seal_trim(), cloth_shade(), rnd()

### Community 43 - "kokuto"
Cohesion: 0.24
Nodes (4): back_blade(), crest(), hip_kokuto(), kokuto()

### Community 44 - "lock"
Cohesion: 0.14
Nodes (7): back_fan(), braid(), cel_face(), lock(), sidelocks(), hime_locks(), beard()

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 46 - "cel_box"
Cohesion: 0.22
Nodes (5): cel_box(), flick(), ear_panels(), nape_hem(), bun()

### Community 47 - "rot_matrix"
Cohesion: 0.33
Nodes (3): Piece, piece_corners(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 50 - "spike"
Cohesion: 0.25
Nodes (4): spike(), crown(), burst(), pineapple()

## Knowledge Gaps
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_tsuchigumo.py`, `kit_shinobi.py`, `kit_senju.py`, `kit_academy.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `kit.py`, `kit_aburame.py`, `kit_haruno.py`, `kit_suzuran.py`, `fabric`, `kit_hatake.py`, `kit_hyuga.py`, `kit_nara.py`, `snack_pouch`, `kit_tobari.py`, `kit_sarutobi.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `kit_hagane.py`, `kit_morino.py`, `kit_field.py`, `stamp`, `arm_bone`, `Box`, `rnd`, `kokuto`, `lock`, `cel_box`, `bandage_turns`, `coat_skirts`, `hairpin`?**
  _High betweenness centrality (0.268) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `kit_tsuchigumo.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `kit_academy.py` to `kit_tsuchigumo.py`, `kit_shinobi.py`, `kit_senju.py`, `kit_kurama.py`, `kit.py`, `kit_aburame.py`, `kit_haruno.py`, `kit_suzuran.py`, `fabric`, `kit_hatake.py`, `kit_hyuga.py`, `kit_nara.py`, `snack_pouch`, `kit_tobari.py`, `kit_sarutobi.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_hagane.py`, `kit_morino.py`, `k`, `kit_field.py`, `stamp`, `arm_bone`, `Box`, `rnd`, `kokuto`, `protector_plate`, `coat_skirts`, `hairpin`?**
  _High betweenness centrality (0.178) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `kit_shinobi.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14166666666666666 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `kit.py`, `Story bible`?**
  _High betweenness centrality (0.173) - this node is a cross-community bridge._