# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 37 files · ~63,664 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 842 nodes · 1744 edges · 61 communities (49 shown, 12 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 76 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c94968b0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_tsuchigumo.py
- fabric
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- rnd
- rnd
- Shared helpers
- k
- kit_haruno.py
- k
- 7. Systems in the beta
- seal_script
- kit_hatake.py
- kit_hyuga.py
- kit_nara.py
- kit_akimichi.py
- hood_down
- Garment
- stamp
- kit_shimura.py
- kit_uchiha.py
- kit_yamanaka.py
- kit_hagane.py
- scalp
- solid
- 5. Data formats built for the whole story
- kit_namiashi.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_gekko.py
- 4. Technical architecture
- 6. The map
- arm_bone
- 8. The beta, chapter by chapter
- 9. Delivery plan
- Face
- paint.py
- wardrobe.py
- lock
- load_clans
- Box
- rot_matrix
- build
- hair_face
- Layer
- bangs
- bell_print
- vial
- crown
- hakama_legs
- obi
- tabi
- wrap_front
- burst
- thorn_band

## God Nodes (most connected - your core abstractions)
1. `k()` - 152 edges
2. `solid()` - 101 edges
3. `fabric()` - 82 edges
4. `stamp()` - 38 edges
5. `Shared helpers` - 34 edges
6. `strip_fabric()` - 32 edges
7. `cel_box()` - 29 edges
8. `rnd()` - 28 edges
9. `Box` - 25 edges
10. `arm_bone()` - 22 edges

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

## Communities (61 total, 12 thin omitted)

### Community 0 - "kit_tsuchigumo.py"
Cohesion: 0.12
Nodes (9): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+1 more)

### Community 1 - "fabric"
Cohesion: 0.11
Nodes (12): back_crest(), coat_skirts(), gloves(), head_cloth(), heavy_boots(), arm_protector(), forehead_protector(), protector_plate() (+4 more)

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.14
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.10
Nodes (10): drawstrings(), holster(), hood_down(), leg_cloth(), sash(), side_stripe(), stripes(), waist() (+2 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (27): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), How to read this bible, Kindling Bond (+19 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (12): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), part_line(), side_fringe(), splatter() (+4 more)

### Community 9 - "rnd"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "rnd"
Cohesion: 0.15
Nodes (10): quilt(), bandage_turns(), thorn_wrap(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock() (+2 more)

### Community 11 - "Shared helpers"
Cohesion: 0.08
Nodes (22): Shared helpers, shirt(), body(), flaps(), footwear(), leg_ring(), legs(), neckline() (+14 more)

### Community 12 - "k"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 14 - "k"
Cohesion: 0.08
Nodes (13): ribbed(), shin_wraps(), ink_clouds(), stockings(), apothecary_sash(), bell_charm(), gloves(), shin_wraps() (+5 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 17 - "kit_hatake.py"
Cohesion: 0.17
Nodes (5): decal(), face_mask(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.12
Nodes (12): braid(), cel_box(), curtain(), spike(), tie(), back_sheet(), ear_panels(), gathered_tail() (+4 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 20 - "kit_akimichi.py"
Cohesion: 0.14
Nodes (6): flick(), gourd(), lames(), puff(), shoku_disc(), snack_pouch()

### Community 21 - "hood_down"
Cohesion: 0.33
Nodes (3): hood_down(), mantle(), pleats()

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "stamp"
Cohesion: 0.08
Nodes (15): stamp(), back_crest(), crest(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey() (+7 more)

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
Cohesion: 0.17
Nodes (7): turned_hem(), bracers(), harness(), mace(), plate(), shin_guards(), leg_bone()

### Community 28 - "scalp"
Cohesion: 0.16
Nodes (7): cel_face(), ring_shell(), crown(), clipped(), combed_back(), pulled_back(), scalp()

### Community 29 - "solid"
Cohesion: 0.09
Nodes (15): How the pieces work, belt(), collar(), roll(), tanto(), muffler(), sash(), clip() (+7 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_namiashi.py"
Cohesion: 0.20
Nodes (5): back_blade(), crest(), hip_kokuto(), kokuto(), wave_band()

### Community 32 - "outputs"
Cohesion: 0.23
Nodes (11): catalog(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes(), main() (+3 more)

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
Cohesion: 0.11
Nodes (12): sleeve_roll(), sode(), arm_bone(), arm_x(), kimono_sleeves(), kimono_sleeves(), armband(), armband() (+4 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Face"
Cohesion: 0.25
Nodes (4): button(), darken_rows(), rivets(), Face

### Community 42 - "paint.py"
Cohesion: 0.16
Nodes (7): band(), curls_box(), curls_face(), dark_seams(), grid(), hem(), shade()

### Community 43 - "wardrobe.py"
Cohesion: 0.20
Nodes (5): hex_rgb(), png_bytes(), ramp(), rgb_hex(), _toward()

### Community 44 - "lock"
Cohesion: 0.17
Nodes (6): back_fan(), lock(), sidelocks(), hime_locks(), wave_lock(), beard()

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 47 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "hair_face"
Cohesion: 0.29
Nodes (4): hair_box(), hair_face(), hair_shade(), shell()

### Community 51 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

## Knowledge Gaps
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_tsuchigumo.py`, `fabric`, `kit_senju.py`, `kit_academy.py`, `kit_kurama.py`, `rnd`, `rnd`, `Shared helpers`, `k`, `kit_haruno.py`, `kit_hatake.py`, `kit_hyuga.py`, `kit_nara.py`, `kit_akimichi.py`, `hood_down`, `stamp`, `kit_shimura.py`, `kit_uchiha.py`, `kit_yamanaka.py`, `kit_hagane.py`, `scalp`, `solid`, `kit_namiashi.py`, `kit_gekko.py`, `arm_bone`, `Face`, `paint.py`, `lock`, `hair_face`, `bell_print`, `vial`, `hakama_legs`, `obi`, `tabi`, `wrap_front`, `thorn_band`?**
  _High betweenness centrality (0.259) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `kit_tsuchigumo.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12418300653594772 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.178) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.10666666666666667 - nodes in this community are weakly interconnected._
- **Why does `Shinobi Modpack: roadmap` connect `Shinobi Modpack: roadmap` to `11. Later systems`, `4. Technical architecture`, `6. The map`, `Story bible`, `8. The beta, chapter by chapter`, `9. Delivery plan`, `7. Systems in the beta`, `5. Data formats built for the whole story`?**
  _High betweenness centrality (0.167) - this node is a cross-community bridge._