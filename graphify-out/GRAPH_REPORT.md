# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 40 files · ~67,521 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 918 nodes · 1921 edges · 57 communities (55 shown, 2 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 73 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ce876a3d`
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
- k
- kit_aburame.py
- fabric
- kit_suzuran.py
- 7. Systems in the beta
- strip_fabric
- stamp
- kit_hyuga.py
- kit_nara.py
- kit_kunoichi.py
- kit_tobari.py
- Garment
- kit_sarutobi.py
- glyphs.py
- arm_bone
- kit_yamanaka.py
- kit_hagane.py
- rnd
- solid
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_gekko.py
- 4. Technical architecture
- 6. The map
- kit_uzumaki.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- Face
- kit_akimichi.py
- kokuto
- lock
- load_clans
- cel_box
- rot_matrix
- build
- Box
- spike
- paint.py
- ring_shell
- kit_specialist.py
- bandage
- hood_down
- curls_face

## God Nodes (most connected - your core abstractions)
1. `k()` - 176 edges
2. `solid()` - 120 edges
3. `fabric()` - 91 edges
4. `strip_fabric()` - 43 edges
5. `stamp()` - 40 edges
6. `Shared helpers` - 33 edges
7. `cel_box()` - 32 edges
8. `rnd()` - 31 edges
9. `arm_bone()` - 28 edges
10. `arm_x()` - 27 edges

## Surprising Connections (you probably didn't know these)
- `Shared helpers` --references--> `wraps()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit_shinobi.py
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Shared helpers` --references--> `cel_box()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `spike()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py
- `Shared helpers` --references--> `ring_shell()`  [INFERRED]
  CLANS.md → tools/wardrobe/anime.py

## Import Cycles
- None detected.

## Communities (57 total, 2 thin omitted)

### Community 0 - "kit_tsuchigumo.py"
Cohesion: 0.15
Nodes (7): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 1 - "kit_shinobi.py"
Cohesion: 0.13
Nodes (7): anbu_arms(), anbu_plates(), flak_vest(), mesh(), sandals(), tanto(), wraps()

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
Cohesion: 0.10
Nodes (10): drawstrings(), holster(), hood_down(), ribbed(), sash(), shin_wraps(), side_stripe(), stripes() (+2 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (27): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), How to read this bible, Kindling Bond (+19 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (12): back_crest(), bead_clip(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe(), splatter() (+4 more)

### Community 9 - "rnd"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.06
Nodes (18): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), bandage_turns(), mist_swirls() (+10 more)

### Community 11 - "k"
Cohesion: 0.15
Nodes (12): belt(), collar(), flaps(), footwear(), obi(), legs(), neckline(), pouch() (+4 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "fabric"
Cohesion: 0.15
Nodes (9): How the pieces work, head_cloth(), forehead_protector(), beak(), bump(), ears(), plate(), strap() (+1 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.11
Nodes (9): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), sash_vials() (+1 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "strip_fabric"
Cohesion: 0.12
Nodes (8): leg_cloth(), waist(), body(), vest(), tabi(), gloves(), sleeves(), strip_fabric()

### Community 17 - "stamp"
Cohesion: 0.11
Nodes (10): stamp(), back_crest(), decal(), shoulder_decal(), slanted_protector(), white_fang_tanto(), crest(), back_crest() (+2 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.12
Nodes (9): curtain(), tie(), back_sheet(), blunt_fringe(), gathered_tail(), hair_tie(), hime_locks(), parted_fringe() (+1 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.19
Nodes (6): arm_protector(), back_crest(), crest(), mesh_shirt(), net(), protector_plate()

### Community 20 - "kit_kunoichi.py"
Cohesion: 0.12
Nodes (7): arm_warmers(), frog_buttons(), mandarin_collar(), shin_wrap(), tabi_boots(), thigh_holster(), wrap_front()

### Community 21 - "kit_tobari.py"
Cohesion: 0.12
Nodes (9): shirt(), shirt(), decal(), lantern(), lantern_tag(), plain_body(), shin_wraps(), split_toe_boots() (+1 more)

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_sarutobi.py"
Cohesion: 0.22
Nodes (5): beard(), crest(), crest_patch(), flame_hem(), monkey()

### Community 25 - "arm_bone"
Cohesion: 0.09
Nodes (15): sleeve_roll(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), kimono_sleeves(), armband(), armband() (+7 more)

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "kit_hagane.py"
Cohesion: 0.21
Nodes (5): bracers(), harness(), mace(), plate(), shin_guards()

### Community 28 - "rnd"
Cohesion: 0.14
Nodes (10): clipped(), combed_back(), ink_stains(), seal_trim(), hair_box(), hair_face(), hair_shade(), rnd() (+2 more)

### Community 29 - "solid"
Cohesion: 0.06
Nodes (18): waist_pouch(), collar(), mandarin_collar(), face_mask(), kimono_sleeves(), obi(), brush_pin(), coat_skirts() (+10 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.07
Nodes (17): blouse(), cargo(), chain(), gloves(), half_sleeves(), holster(), knee_guards(), mesh_arms() (+9 more)

### Community 32 - "outputs"
Cohesion: 0.22
Nodes (11): hex_rgb(), json_text(), load_eye_colors(), load_hair_colors(), load_palettes(), outputs(), png_bytes(), ramp() (+3 more)

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

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.14
Nodes (7): clip(), hairpin(), seal_script(), seal_tags(), waves(), wide_sleeves(), wrap_tie()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Face"
Cohesion: 0.19
Nodes (6): button(), darken_rows(), grid(), line(), rivets(), Face

### Community 42 - "kit_akimichi.py"
Cohesion: 0.14
Nodes (6): gourd(), lames(), quilt(), shoku_disc(), snack_pouch(), sode()

### Community 43 - "kokuto"
Cohesion: 0.20
Nodes (5): back_blade(), crest(), hip_kokuto(), kokuto(), wave_band()

### Community 44 - "lock"
Cohesion: 0.24
Nodes (6): Shared helpers, back_fan(), bangs(), braid(), lock(), sidelocks()

### Community 45 - "load_clans"
Cohesion: 0.18
Nodes (9): catalog(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_groups(), load_population(), population_weights() (+1 more)

### Community 46 - "cel_box"
Cohesion: 0.13
Nodes (8): cel_box(), flick(), ear_panels(), round_bun(), wave_lock(), nape_hem(), tuft(), bun()

### Community 47 - "rot_matrix"
Cohesion: 0.18
Nodes (5): wave_lock(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.19
Nodes (8): build(), build_all(), load_marks(), load_module(), main(), natural(), sources(), validate_catalog()

### Community 50 - "spike"
Cohesion: 0.25
Nodes (4): spike(), crown(), burst(), pineapple()

### Community 51 - "paint.py"
Cohesion: 0.16
Nodes (6): band(), cloth_shade(), dark_seams(), hem(), strip_line(), shade()

### Community 52 - "ring_shell"
Cohesion: 0.25
Nodes (4): cel_face(), ring_shell(), crown(), pulled_back()

### Community 53 - "kit_specialist.py"
Cohesion: 0.18
Nodes (5): bandolier(), coat_skirts(), cross_armband(), scroll_tube(), strap()

### Community 54 - "bandage"
Cohesion: 0.33
Nodes (3): forearm_wraps(), bandaged_arm(), bandage()

### Community 55 - "hood_down"
Cohesion: 0.33
Nodes (3): hood_down(), mantle(), pleats()

### Community 56 - "curls_face"
Cohesion: 0.40
Nodes (3): puff(), curls_box(), curls_face()

## Knowledge Gaps
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_tsuchigumo.py`, `kit_shinobi.py`, `kit_senju.py`, `kit_academy.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `kit_aburame.py`, `fabric`, `kit_suzuran.py`, `strip_fabric`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `kit_kunoichi.py`, `kit_tobari.py`, `kit_sarutobi.py`, `glyphs.py`, `arm_bone`, `kit_yamanaka.py`, `kit_hagane.py`, `rnd`, `solid`, `kit_field.py`, `kit_gekko.py`, `kit_uzumaki.py`, `Face`, `kit_akimichi.py`, `kokuto`, `lock`, `cel_box`, `paint.py`, `ring_shell`, `kit_specialist.py`, `hood_down`, `curls_face`?**
  _High betweenness centrality (0.275) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `kit_shinobi.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `kit_tsuchigumo.py`, `kit_shinobi.py`, `kit_senju.py`, `kit_academy.py`, `kit_kurama.py`, `kit_yuhi.py`, `k`, `kit_aburame.py`, `fabric`, `kit_suzuran.py`, `strip_fabric`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `kit_kunoichi.py`, `kit_tobari.py`, `kit_sarutobi.py`, `glyphs.py`, `arm_bone`, `kit_hagane.py`, `rnd`, `kit_field.py`, `kit_gekko.py`, `kit_uzumaki.py`, `kit_akimichi.py`, `kokuto`, `lock`, `Box`, `paint.py`, `kit_specialist.py`, `bandage`, `hood_down`?**
  _High betweenness centrality (0.180) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `lock`, `Story bible`?**
  _High betweenness centrality (0.169) - this node is a cross-community bridge._