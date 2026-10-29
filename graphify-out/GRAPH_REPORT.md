# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 112 files · ~161,791 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2314 nodes · 5090 edges · 141 communities (105 shown, 36 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 474 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `56270fae`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_shiranui.py
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- kit_hagane.py
- kit_yuhi.py
- kit_kunoichi.py
- strip_fabric
- cel_box
- kit_suzuran.py
- 7. Systems in the beta
- Plan
- solid
- kit_nara.py
- kit_rugged.py
- kit_household.py
- kit_tobari.py
- Garment
- kit_tsuchigumo.py
- kit_haruno.py
- Levels
- k
- kit_market.py
- kit_kinoshita.py
- Personality
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- stamp
- 4. Technical architecture
- 6. The map
- hair_face
- 8. The beta, chapter by chapter
- 9. Delivery plan
- Tier
- kit_akimichi.py
- 4. Clan quest lines
- Run
- preview.py
- Tex
- rot_matrix
- build
- Box
- Bond
- Face
- scalp
- pathlib
- Act
- Konoha: the build plan
- .bond
- rnd
- Person
- fabric
- list
- .classic
- blocks.py
- noren
- Custom blocks
- kit_specialist.py
- render_kit.py
- VillageScaleTest
- org.junit.jupiter.api.Test
- .name
- Bonds
- .read
- Def
- Mood
- Deed
- anime.py
- Experience
- catalogue.py
- .test
- Meters
- kit_aburame.py
- kit_namiashi.py
- kit_shinobi.py
- 4.3 The noble clans
- kit_umino.py
- Canvas
- Source
- .slant
- Label
- lock
- .born
- Meter
- Title
- Every building
- Village
- chain
- Side quests
- 4.4 The minor clans
- kit_gekko.py
- 2. Quest framework
- Trait
- senbon
- Memory
- Person
- Stage
- kit_shimura.py
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- kit_hyuga.py
- jika_tabi
- bangs
- mesh_shirt
- rope_hair
- json
- seal_script
- rope_face
- bandage_turns
- paint.py
- wave_face
- resolve
- wide_sleeves
- holster
- sash
- shin_wraps
- bands
- checks
- geta
- overlap
- scarf
- sash
- robe_skirt
- skirt
- stripes
- coat_skirts
- camo
- patch
- trench_knife
- scroll

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `solid()` - 151 edges
3. `BondWorld` - 129 edges
4. `fabric()` - 109 edges
5. `Act` - 101 edges
6. `Village` - 62 edges
7. `strip_fabric()` - 59 edges
8. `stamp()` - 47 edges
9. `Bond` - 44 edges
10. `rnd()` - 43 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `Interior fittings` --references--> `tatami()`  [INFERRED]
  KONOHA_BUILD.md → tools/konoha/blocks.py
- `The pieces` --references--> `Plan`  [INFERRED]
  KONOHA_BUILD.md → tools/konoha/kit.py
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java

## Import Cycles
- None detected.

## Communities (141 total, 36 thin omitted)

### Community 0 - "kit_shiranui.py"
Cohesion: 0.22
Nodes (4): arm_protector(), protector_plate(), backward_bandana(), crest()

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.18
Nodes (15): backdrop(), Character, clan_renders(), cube_quads(), font(), general_renders(), ground_shadow(), hair_chart() (+7 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.10
Nodes (10): drawstrings(), forearm_wraps(), hood_down(), ribbed(), side_stripe(), sleeve_roll(), stripes(), turned_hem() (+2 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (32): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+24 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+5 more)

### Community 9 - "kit_hagane.py"
Cohesion: 0.06
Nodes (17): spike(), bracers(), crown(), harness(), mace(), plate(), shin_guards(), burst() (+9 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.14
Nodes (8): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_fan(), wave_lock()

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.08
Nodes (11): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), tabi_boots() (+3 more)

### Community 12 - "strip_fabric"
Cohesion: 0.12
Nodes (9): leg_cloth(), waist(), arm_cloth(), cloth_shoes(), trouser_legs(), waist(), sandals(), sleeves() (+1 more)

### Community 13 - "cel_box"
Cohesion: 0.15
Nodes (7): cel_box(), flick(), topknot(), ear_panels(), nape_hem(), knot(), bun()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (10): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 17 - "solid"
Cohesion: 0.11
Nodes (10): face_mask(), white_fang_tanto(), pauldron(), cane(), side_panels(), clip(), hairpin(), wrap_tie() (+2 more)

### Community 18 - "kit_nara.py"
Cohesion: 0.33
Nodes (3): back_crest(), crest(), tuft()

### Community 19 - "kit_rugged.py"
Cohesion: 0.10
Nodes (9): baggy_legs(), knot_bun(), leg_wraps(), shag_box(), shag_face(), shin_guard(), soft_boots(), straw_sandals() (+1 more)

### Community 20 - "kit_household.py"
Cohesion: 0.14
Nodes (6): blossom(), collar_band(), dots(), ichimatsu(), kasuri(), socks()

### Community 21 - "kit_tobari.py"
Cohesion: 0.07
Nodes (15): shirt(), vest(), anbu_plates(), decal(), hood_down(), lantern(), lantern_tag(), mantle() (+7 more)

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 24 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 25 - "Levels"
Cohesion: 0.19
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 26 - "k"
Cohesion: 0.05
Nodes (32): Shared helpers, braid(), arm_bone(), arm_x(), belt(), body(), collar(), flaps() (+24 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kyahan() (+14 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.12
Nodes (12): back_crest(), chisel(), crest(), mallet(), nail_pouch(), pencil(), _piece(), sashiko() (+4 more)

### Community 29 - "Personality"
Cohesion: 0.05
Nodes (28): 20. What the roadmap asks of bonds, ClanProfile, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY (+20 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.07
Nodes (13): arm_guards(), blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards() (+5 more)

### Community 32 - "outputs"
Cohesion: 0.12
Nodes (23): catalog(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_eye_colors() (+15 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "stamp"
Cohesion: 0.11
Nodes (11): stamp(), back_crest(), decal(), shoulder_decal(), slanted_protector(), crest(), crest(), crest_patch() (+3 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "hair_face"
Cohesion: 0.29
Nodes (4): hair_box(), hair_face(), hair_shade(), shell()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Tier"
Cohesion: 0.33
Nodes (5): Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 42 - "kit_akimichi.py"
Cohesion: 0.13
Nodes (7): gourd(), lames(), puff(), shoku_disc(), snack_pouch(), sode(), curls_box()

### Community 43 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 44 - "Run"
Cohesion: 0.07
Nodes (20): 15. Pacing, 5. Personality, BondEvent, Rng, Seeds, Chapter, Phase, ACADEMY (+12 more)

### Community 45 - "preview.py"
Cohesion: 0.16
Nodes (14): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+6 more)

### Community 46 - "Tex"
Cohesion: 0.15
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 47 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.10
Nodes (5): band(), hem(), strip_line(), Box, Layer

### Community 51 - "Face"
Cohesion: 0.18
Nodes (6): button(), dark_seams(), darken_rows(), rivets(), Face, shade()

### Community 52 - "scalp"
Cohesion: 0.18
Nodes (7): ring_shell(), crown(), clipped(), combed_back(), pulled_back(), combed_up(), scalp()

### Community 53 - "pathlib"
Cohesion: 0.12
Nodes (4): build(), build(), flat(), build()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 55 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 57 - "rnd"
Cohesion: 0.13
Nodes (8): quilt(), sprigs(), kasuri(), straw_sandals(), cape(), ragged(), curls_face(), rnd()

### Community 58 - "Person"
Cohesion: 0.14
Nodes (5): BondBook, Fact, MemoryLine, Page, Person

### Community 59 - "fabric"
Cohesion: 0.19
Nodes (6): back_crest(), gloves(), head_cloth(), heavy_boots(), forehead_protector(), fabric()

### Community 61 - ".classic"
Cohesion: 0.13
Nodes (4): ConditionsAndEffectsTest, GossipTest, Leaf, VillageTest

### Community 62 - "blocks.py"
Cohesion: 0.13
Nodes (20): Roofs, Streets, auto_uv(), block(), Block, box(), check(), compile_all() (+12 more)

### Community 63 - "noren"
Cohesion: 0.20
Nodes (10): 2. Style guide: the Konoha kit, 6. Prototypes, By building type, Facades and shop fronts, Lanterns, Shared palette, awning(), facing_states() (+2 more)

### Community 64 - "Custom blocks"
Cohesion: 0.12
Nodes (15): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+7 more)

### Community 65 - "kit_specialist.py"
Cohesion: 0.11
Nodes (8): bandolier(), coat_skirts(), cross_armband(), ink_stains(), scroll_tube(), seal_trim(), shirt(), strap()

### Community 66 - "render_kit.py"
Cohesion: 0.24
Nodes (6): blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 67 - "VillageScaleTest"
Cohesion: 0.13
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "org.junit.jupiter.api.Test"
Cohesion: 0.12
Nodes (5): BondDialogueTest, ConflictTest, KindlingAndBookTest, MemoryTest, SquadTest

### Community 69 - ".name"
Cohesion: 0.15
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (13): 11. Kindling Bond, 13. Data formats, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+5 more)

### Community 71 - ".read"
Cohesion: 0.10
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.12
Nodes (5): Def, Size, BIG, NOTABLE, SMALL

### Community 73 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 74 - "Deed"
Cohesion: 0.17
Nodes (3): 8. The village talks, Deed, Know

### Community 75 - "anime.py"
Cohesion: 0.17
Nodes (5): back_fan(), cel_face(), curtain(), sidelocks(), back_sheet()

### Community 76 - "Experience"
Cohesion: 0.18
Nodes (9): Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR, STUDY (+1 more)

### Community 77 - "catalogue.py"
Cohesion: 0.21
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 78 - ".test"
Cohesion: 0.07
Nodes (4): 12. The bond book, BondConditions, BondEffects, BondWeb

### Community 80 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 81 - "kit_namiashi.py"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 82 - "kit_shinobi.py"
Cohesion: 0.12
Nodes (9): How the pieces work, anbu_arms(), flak_vest(), mesh(), tanto(), beak(), bump(), ears() (+1 more)

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_umino.py"
Cohesion: 0.20
Nodes (4): dolphin(), surf(), wave_band(), waves()

### Community 85 - "Canvas"
Cohesion: 0.22
Nodes (3): light_for(), Scene, Canvas

### Community 86 - "Source"
Cohesion: 0.22
Nodes (5): Source, HEARD, SEEN, SELF, TOLD

### Community 88 - "Label"
Cohesion: 0.22
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 89 - "lock"
Cohesion: 0.14
Nodes (7): lock(), hime_locks(), side_fringe(), wave_lock(), beard(), flicks(), falling_tail()

### Community 90 - ".born"
Cohesion: 0.09
Nodes (4): BondDialogue, Household, Grant, Recruitment

### Community 91 - "Meter"
Cohesion: 0.15
Nodes (6): Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - "Title"
Cohesion: 0.17
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Every building"
Cohesion: 0.12
Nodes (17): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+9 more)

### Community 94 - "Village"
Cohesion: 0.06
Nodes (12): 18. Village scale, 19. Society hooks, Base, ClanRelations, SocialTie, SocietyHook, House, Tier (+4 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook, as these templates expect it, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Trait"
Cohesion: 0.29
Nodes (7): Lean, Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH

### Community 101 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 103 - "Person"
Cohesion: 0.10
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 104 - "Stage"
Cohesion: 0.33
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 105 - "kit_shimura.py"
Cohesion: 0.29
Nodes (3): back_crest(), bandaged_arm(), bandage()

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "kit_hyuga.py"
Cohesion: 0.12
Nodes (8): tie(), gathered_tail(), hair_tie(), hakama_legs(), kimono_sleeves(), obi(), tabi(), wrap_front()

### Community 109 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 110 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

### Community 118 - "paint.py"
Cohesion: 0.14
Nodes (3): crest(), crest_patch(), cloth_shade()

## Knowledge Gaps
- **153 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+148 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 988 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **36 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bonds` connect `Bonds` to `Memory`, `Person`, `.read`, `Story bible`, `Deed`, `Mood`, `Run`, `.test`, `Meters`, `Levels`, `Person`, `Personality`, `Village`?**
  _High betweenness centrality (0.460) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _153 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `k`, `Story bible`?**
  _High betweenness centrality (0.368) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `k` to `Clans`, `kit_hagane.py`, `kit_shimura.py`, `anime.py`, `strip_fabric`, `cel_box`, `bangs`, `Box`, `kit_shinobi.py`, `scalp`, `lock`, `fabric`?**
  _High betweenness centrality (0.296) - this node is a cross-community bridge._