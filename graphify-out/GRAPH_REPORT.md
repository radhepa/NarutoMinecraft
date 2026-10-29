# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 38 files · ~64,724 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 860 nodes · 1789 edges · 52 communities (49 shown, 3 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 75 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4bcaa504`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_tsuchigumo.py
- kit_morino.py
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
- k
- kit_haruno.py
- kit_suzuran.py
- 7. Systems in the beta
- fabric
- stamp
- kit_hyuga.py
- kit_nara.py
- kit_akimichi.py
- kit_tobari.py
- Garment
- kit_sarutobi.py
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- kit_hagane.py
- scalp
- kit_uzumaki.py
- 5. Data formats built for the whole story
- paint.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_gekko.py
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
- bandolier
- rot_matrix
- build
- bandage_turns
- wave_face
- bangs

## God Nodes (most connected - your core abstractions)
1. `k()` - 156 edges
2. `solid()` - 107 edges
3. `fabric()` - 84 edges
4. `stamp()` - 40 edges
5. `strip_fabric()` - 34 edges
6. `Shared helpers` - 34 edges
7. `rnd()` - 31 edges
8. `cel_box()` - 29 edges
9. `Box` - 25 edges
10. `arm_bone()` - 24 edges

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

## Communities (52 total, 3 thin omitted)

### Community 0 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 1 - "kit_morino.py"
Cohesion: 0.12
Nodes (8): back_crest(), head_cloth(), arm_protector(), anbu_plates(), flak_vest(), forehead_protector(), protector_plate(), sandals()

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
Cohesion: 0.09
Nodes (16): drawstrings(), holster(), hood_down(), sash(), side_stripe(), stripes(), turned_hem(), waist_pouch() (+8 more)

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

### Community 11 - "kit.py"
Cohesion: 0.09
Nodes (13): How the pieces work, belt(), collar(), flaps(), footwear(), legs(), neckline(), pouch() (+5 more)

### Community 12 - "k"
Cohesion: 0.06
Nodes (18): deep_hood(), high_collar(), hood_down(), lenses(), ribbed(), shin_wraps(), mandarin_collar(), face_mask() (+10 more)

### Community 13 - "kit_haruno.py"
Cohesion: 0.12
Nodes (8): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), wave_lock(), rot_matrix()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.11
Nodes (9): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), sash_vials() (+1 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "fabric"
Cohesion: 0.11
Nodes (14): leg_cloth(), shirt(), waist(), body(), gloves(), heavy_boots(), anbu_arms(), sleeves() (+6 more)

### Community 17 - "stamp"
Cohesion: 0.11
Nodes (10): stamp(), back_crest(), decal(), shoulder_decal(), slanted_protector(), white_fang_tanto(), crest(), guardian_sash() (+2 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.11
Nodes (12): cel_box(), curtain(), tie(), flick(), back_sheet(), ear_panels(), gathered_tail(), hair_tie() (+4 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "kit_akimichi.py"
Cohesion: 0.17
Nodes (5): gourd(), lames(), quilt(), shoku_disc(), snack_pouch()

### Community 21 - "kit_tobari.py"
Cohesion: 0.12
Nodes (10): decal(), hood_down(), lantern(), lantern_tag(), mantle(), plain_body(), pleats(), shin_wraps() (+2 more)

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_sarutobi.py"
Cohesion: 0.22
Nodes (5): beard(), crest(), crest_patch(), flame_hem(), monkey()

### Community 24 - "kit_shimura.py"
Cohesion: 0.18
Nodes (5): forearm_wraps(), back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 26 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 27 - "kit_hagane.py"
Cohesion: 0.21
Nodes (5): bracers(), harness(), mace(), plate(), shin_guards()

### Community 28 - "scalp"
Cohesion: 0.20
Nodes (6): cel_face(), ring_shell(), crown(), combed_back(), pulled_back(), scalp()

### Community 29 - "kit_uzumaki.py"
Cohesion: 0.12
Nodes (8): bun(), clip(), hairpin(), seal_script(), seal_tags(), waves(), wide_sleeves(), wrap_tie()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "paint.py"
Cohesion: 0.12
Nodes (4): crest(), wave_band(), shirt(), cloth_shade()

### Community 32 - "outputs"
Cohesion: 0.17
Nodes (15): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+7 more)

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
Cohesion: 0.13
Nodes (11): sleeve_roll(), sode(), arm_bone(), arm_x(), kimono_sleeves(), kimono_sleeves(), armband(), roll() (+3 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Box"
Cohesion: 0.05
Nodes (19): puff(), band(), button(), curls_box(), curls_face(), dark_seams(), darken_rows(), grid() (+11 more)

### Community 42 - "rnd"
Cohesion: 0.13
Nodes (8): fur_edge(), ink_clouds(), splatter(), wisteria_hem(), clipped(), ink_stains(), seal_trim(), rnd()

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "lock"
Cohesion: 0.20
Nodes (7): Shared helpers, back_fan(), braid(), lock(), sidelocks(), hime_locks(), wraps()

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 47 - "rot_matrix"
Cohesion: 0.33
Nodes (3): Piece, piece_corners(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 51 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_tsuchigumo.py`, `kit_morino.py`, `kit_senju.py`, `kit_academy.py`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `kit.py`, `kit_haruno.py`, `kit_suzuran.py`, `fabric`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `kit_akimichi.py`, `kit_tobari.py`, `kit_sarutobi.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `kit_hagane.py`, `scalp`, `kit_uzumaki.py`, `paint.py`, `kit_gekko.py`, `arm_bone`, `Box`, `rnd`, `lock`, `bandage_turns`, `wave_face`?**
  _High betweenness centrality (0.258) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `kit_tsuchigumo.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14166666666666666 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `lock`, `Story bible`?**
  _High betweenness centrality (0.176) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `kit_morino.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11578947368421053 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `kit_academy.py` to `kit_tsuchigumo.py`, `kit_morino.py`, `kit_senju.py`, `kit_kurama.py`, `kit.py`, `k`, `kit_haruno.py`, `kit_suzuran.py`, `fabric`, `stamp`, `kit_hyuga.py`, `kit_nara.py`, `kit_akimichi.py`, `kit_tobari.py`, `kit_sarutobi.py`, `kit_shimura.py`, `kit_uchiha.py`, `kit_hagane.py`, `kit_uzumaki.py`, `paint.py`, `kit_gekko.py`, `arm_bone`, `Box`, `kokuto`, `lock`, `bandolier`?**
  _High betweenness centrality (0.170) - this node is a cross-community bridge._