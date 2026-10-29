# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 164 files · ~223,301 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3014 nodes · 7170 edges · 172 communities (117 shown, 55 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 789 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ab7b2e1f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- stamp
- mkit.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- kit_inuzuka.py
- kit_yuhi.py
- kit_kunoichi.py
- Economy
- Catalogue
- kit_suzuran.py
- 7. Systems in the beta
- kit_umino.py
- kit_tsuchigumo.py
- cel_box
- kit_rugged.py
- kit_household.py
- strip_fabric
- .friends
- .num
- Desk
- kit_uchiha.py
- Shared helpers
- kit_market.py
- kit_kinoshita.py
- Missions
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- missions.py
- 4. Technical architecture
- 6. The map
- kit_uzumaki.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- .get
- kit_aburame.py
- Player
- Playthrough
- Question
- .strings
- Plan
- Rng
- Box
- Seeds
- Face
- ring_shell
- Json
- Act
- Stage
- BondWorld
- kit_hagane.py
- .tier
- World
- .classic
- Person
- Personality
- blocks.py
- Village
- VillageScaleTest
- Bond
- .classmate
- Bonds
- Squad
- Def
- Levels
- Deed
- fabric
- Template
- Tier
- preview.py
- Meters
- Value
- Mood
- SquadTest
- 4.3 The noble clans
- S
- .page
- Peeve
- ClanRelations
- TimeAndPacingTest
- Tex
- paint.py
- Meter
- End
- mission
- pathlib
- Conflict
- Side quests
- 4.4 The minor clans
- .of
- 2. Quest framework
- Kind
- catalogue.py
- kit_shinobi.py
- kit_specialist.py
- lock
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- solid
- AnswerTag
- 4. Clan quest lines
- .romance
- .all
- render_kit.py
- Every building
- Title
- Konoha: the build plan
- Custom blocks
- k
- noren
- .receive
- kit_sarutobi.py
- kit_shiranui.py
- Kind
- cap
- kit_nara.py
- Label
- forehead_protector
- kit_namiashi.py
- kit_yamanaka.py
- shade
- News
- kit_gekko.py
- .everyKeyTheEngineEmitsIsListed
- armband
- SampleQuestions
- furoshiki
- bandage_turns
- shade
- snack_pouch
- sode
- strap
- mandarin_collar
- obi
- bib
- gathered_ankles
- geta
- tasuki
- rolled_cuffs
- coat_skirts
- wave_band
- pauldron
- bandaged_arm
- bandolier
- wrap_tie
- .effectiveLevel
- .name
- .read
- .populate
- Question
- .write
- ConflictTest
- Trait
- .theCompiledShapeParses

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 184 edges
3. `solid()` - 151 edges
4. `Act` - 121 edges
5. `fabric()` - 109 edges
6. `Bond` - 66 edges
7. `Village` - 63 edges
8. `strip_fabric()` - 59 edges
9. `Person` - 53 edges
10. `stamp()` - 47 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `7. Questions and choices` --references--> `Question`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Question.java
- `9. Pacing with time together` --references--> `TimeAndPacingTest`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java
- `Interior fittings` --references--> `tatami()`  [INFERRED]
  KONOHA_BUILD.md → tools/konoha/blocks.py

## Import Cycles
- None detected.

## Communities (172 total, 55 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.11
Nodes (10): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), back_crest(), crest_patch(), bump() (+2 more)

### Community 1 - "mkit.py"
Cohesion: 0.18
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 2 - "Clans"
Cohesion: 0.29
Nodes (7): Clans, Commands, Mix and match, Piece ids, Population, Reference images, The clan file

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (20): new_canvas(), save_canvas(), backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads() (+12 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.07
Nodes (13): back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), sash(), shin_wraps(), side_stripe() (+5 more)

### Community 7 - "Story bible"
Cohesion: 0.05
Nodes (39): Commits, graphify, Naruto Minecraft, A rank, ANBU operations, B rank, C rank, D rank (+31 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.06
Nodes (17): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mist_swirls(), rose() (+9 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - "Economy"
Cohesion: 0.10
Nodes (11): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+3 more)

### Community 13 - "Catalogue"
Cohesion: 0.14
Nodes (8): Catalogue, Mode, CLASSIC, VARIED, DeskDays, Profile, Run, SimulationTest

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - "kit_umino.py"
Cohesion: 0.14
Nodes (6): brush_tail(), dolphin(), falling_tail(), surf(), wave_band(), waves()

### Community 17 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (7): glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 18 - "cel_box"
Cohesion: 0.10
Nodes (15): bangs(), braid(), cel_box(), cel_face(), curtain(), spike(), tie(), back_sheet() (+7 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "kit_household.py"
Cohesion: 0.05
Nodes (23): bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta(), ichimatsu() (+15 more)

### Community 21 - "strip_fabric"
Cohesion: 0.10
Nodes (10): decal(), hood_down(), lantern(), lantern_tag(), mantle(), muffler(), pleats(), sash() (+2 more)

### Community 22 - ".friends"
Cohesion: 0.10
Nodes (10): BondEvent, Answer, FollowUp, Highlight, Invitation, Outcome, Plan, Together (+2 more)

### Community 24 - "Desk"
Cohesion: 0.12
Nodes (9): Desk, Offer, Rank, A, B, C, D, S (+1 more)

### Community 25 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 26 - "Shared helpers"
Cohesion: 0.14
Nodes (11): Shared helpers, belt(), body(), collar(), flaps(), footwear(), leg_bone(), leg_ring() (+3 more)

### Community 27 - "kit_market.py"
Cohesion: 0.06
Nodes (16): checks(), jika_tabi(), kasuri(), kyahan(), loose_legs(), mark(), open_front(), patch() (+8 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Missions"
Cohesion: 0.08
Nodes (25): 10. What other parts of the pack provide, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back, 2.5 Failure, partial success and abandonment (+17 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "kit_field.py"
Cohesion: 0.12
Nodes (7): arm_guards(), cargo(), gloves(), half_sleeves(), pocket(), shirt(), trousers()

### Community 32 - "outputs"
Cohesion: 0.07
Nodes (34): Collections: the general wardrobe, build(), build_all(), catalog(), clan_bottoms(), clan_resident(), compatible(), general_pool() (+26 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "missions.py"
Cohesion: 0.17
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

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
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 42 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 44 - "Playthrough"
Cohesion: 0.09
Nodes (14): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+6 more)

### Community 45 - "Question"
Cohesion: 0.17
Nodes (4): Answered, Outcome, Questions, QuestionsTest

### Community 46 - ".strings"
Cohesion: 0.25
Nodes (3): Band, Mate, SquadPlan

### Community 47 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 49 - "Box"
Cohesion: 0.08
Nodes (8): strip_line(), Box, Garment, key_rgba(), Layer, Piece, piece_corners(), world_bounds()

### Community 51 - "Face"
Cohesion: 0.20
Nodes (6): drawn_line(), button(), darken_rows(), line(), rivets(), Face

### Community 52 - "ring_shell"
Cohesion: 0.14
Nodes (8): ring_shell(), crown(), clipped(), combed_back(), nape_hem(), pulled_back(), combed_up(), scalp()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.06
Nodes (21): 10. Romance and family (after the beta), Activity, Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST (+13 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 58 - ".tier"
Cohesion: 0.12
Nodes (6): 11. Kindling Bond, Household, Bonfire, Flame, Kindling, Recruitment

### Community 59 - "World"
Cohesion: 0.16
Nodes (6): 11. What waits for Phase 0, 9. The generator, Resident, SlotFiller, World, SampleVillage

### Community 61 - ".classic"
Cohesion: 0.12
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 62 - "Person"
Cohesion: 0.13
Nodes (6): Person, Stage, ADULT, CHILD, TEEN, Schedule

### Community 65 - "blocks.py"
Cohesion: 0.16
Nodes (15): Streets, auto_uv(), block(), Block, box(), check(), compile_all(), main() (+7 more)

### Community 66 - "Village"
Cohesion: 0.11
Nodes (7): 18. Village scale, House, Tier, BACKGROUND, CAST, KNOWN, Village

### Community 70 - "Bonds"
Cohesion: 0.13
Nodes (13): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 5. Personality (+5 more)

### Community 71 - "Squad"
Cohesion: 0.07
Nodes (4): BondDialogue, BondEffects, Departure, Squad

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.16
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.13
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 75 - "fabric"
Cohesion: 0.12
Nodes (13): leg_cloth(), waist(), arm_cloth(), trouser_legs(), waist(), kimono_sleeves(), tabi_boots(), sleeves() (+5 more)

### Community 76 - "Template"
Cohesion: 0.22
Nodes (4): Branch, Step, Template, Twist

### Community 77 - "Tier"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 78 - "preview.py"
Cohesion: 0.16
Nodes (13): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+5 more)

### Community 79 - "Meters"
Cohesion: 0.10
Nodes (8): Memory, Meters, Reaction, Source, HEARD, SEEN, SELF, TOLD

### Community 80 - "Value"
Cohesion: 0.11
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "S"
Cohesion: 0.25
Nodes (4): 6. Squad missions, travel(), S, twist()

### Community 85 - ".page"
Cohesion: 0.18
Nodes (6): 12. The bond book, BondBook, Fact, MemoryLine, Page, BondWeb

### Community 86 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 89 - "Tex"
Cohesion: 0.13
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 90 - "paint.py"
Cohesion: 0.11
Nodes (13): flick(), puff(), quilt(), band(), cloth_shade(), curls_box(), curls_face(), hair_box() (+5 more)

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (7): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 93 - "mission"
Cohesion: 0.40
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 94 - "pathlib"
Cohesion: 0.11
Nodes (5): build(), build(), build(), paste(), scene()

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 101 - "catalogue.py"
Cohesion: 0.18
Nodes (10): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+2 more)

### Community 102 - "kit_shinobi.py"
Cohesion: 0.12
Nodes (9): How the pieces work, anbu_arms(), bandage(), flak_vest(), mesh(), sandals(), tanto(), wraps() (+1 more)

### Community 103 - "kit_specialist.py"
Cohesion: 0.12
Nodes (7): bandolier(), coat_skirts(), cross_armband(), ink_stains(), scroll_tube(), seal_trim(), strap()

### Community 104 - "lock"
Cohesion: 0.17
Nodes (6): back_fan(), lock(), sidelocks(), hime_locks(), wave_lock(), flicks()

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "solid"
Cohesion: 0.08
Nodes (13): gourd(), holster(), face_mask(), white_fang_tanto(), hakama_legs(), trench_knife(), cane(), side_panels() (+5 more)

### Community 110 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 116 - "render_kit.py"
Cohesion: 0.19
Nodes (7): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 117 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 118 - "Title"
Cohesion: 0.16
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 119 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 120 - "Custom blocks"
Cohesion: 0.14
Nodes (14): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+6 more)

### Community 121 - "k"
Cohesion: 0.07
Nodes (15): ribbed(), lames(), shoku_disc(), blouse(), collar(), knee_guards(), tape(), sword_strap() (+7 more)

### Community 122 - "noren"
Cohesion: 0.19
Nodes (9): 2. Style guide: the Konoha kit, By building type, Facades and shop fronts, Lanterns, Shared palette, awning(), facing_states(), noren() (+1 more)

### Community 123 - ".receive"
Cohesion: 0.35
Nodes (3): Gifts, Received, GiftsTest

### Community 125 - "kit_sarutobi.py"
Cohesion: 0.18
Nodes (6): beard(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey()

### Community 126 - "kit_shiranui.py"
Cohesion: 0.21
Nodes (5): crest(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 127 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 128 - "cap"
Cohesion: 0.18
Nodes (7): shirt(), vest(), pouch(), anbu_plates(), shirt(), plain_body(), cap()

### Community 129 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 130 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 131 - "forehead_protector"
Cohesion: 0.20
Nodes (5): head_cloth(), arm_protector(), forehead_protector(), protector_plate(), backward_bandana()

### Community 132 - "kit_namiashi.py"
Cohesion: 0.24
Nodes (4): back_blade(), crest(), hip_kokuto(), kokuto()

### Community 133 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 134 - "shade"
Cohesion: 0.28
Nodes (6): 6. Prototypes, Roofs, kawara_ridge(), tatami(), tatami_top(), shade()

### Community 137 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 138 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.33
Nodes (3): DialogueKeys, DialogueKeysTest, 10. Content plan

### Community 139 - "armband"
Cohesion: 0.33
Nodes (4): arm_bone(), arm_x(), armband(), roll()

### Community 163 - ".effectiveLevel"
Cohesion: 0.18
Nodes (4): Conversation, Reply, Topic, 6. Conversation

### Community 164 - ".name"
Cohesion: 0.13
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 166 - ".populate"
Cohesion: 0.27
Nodes (3): 20. What the roadmap asks of bonds, Report, VillageSim

### Community 170 - "Trait"
Cohesion: 0.33
Nodes (6): Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH

## Knowledge Gaps
- **226 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+221 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1154 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **55 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `News`, `.contacts`, `.friends`, `.effectiveLevel`, `.read`, `.populate`, `Question`, `.write`, `ConflictTest`, `Playthrough`, `Question`, `Stage`, `.tier`, `map`, `.classic`, `Person`, `Village`, `VillageScaleTest`, `Bond`, `Squad`, `Deed`, `SquadTest`, `.page`, `.of`, `Playthrough.java`, `Title`, `.receive`, `VillageSim.java`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _226 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `stamp` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Story bible`, `.friends`, `.populate`, `.write`, `Stage`, `.tier`, `Person`, `Personality`, `Village`, `Levels`, `Deed`, `Meters`, `Value`, `Mood`, `.page`, `ClanRelations`, `TimeAndPacingTest`, `Conflict`, `.romance`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12462462462462462 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `cap`, `stamp`, `kit_nara.py`, `forehead_protector`, `kit_namiashi.py`, `kit_senju.py`, `kit_academy.py`, `kit_yamanaka.py`, `kit_kurama.py`, `kit_gekko.py`, `kit_yuhi.py`, `kit_inuzuka.py`, `kit_kunoichi.py`, `armband`, `furoshiki`, `kit_suzuran.py`, `kit_umino.py`, `kit_tsuchigumo.py`, `cel_box`, `snack_pouch`, `sode`, `kit_household.py`, `mandarin_collar`, `obi`, `bib`, `gathered_ankles`, `Shared helpers`, `kit_market.py`, `kit_kinoshita.py`, `geta`, `rolled_cuffs`, `kit_field.py`, `tasuki`, `coat_skirts`, `wave_band`, `pauldron`, `bandolier`, `wrap_tie`, `kit_uzumaki.py`, `kit_aburame.py`, `Face`, `ring_shell`, `kit_hagane.py`, `fabric`, `bandage_turns`, `paint.py`, `kit_rugged.py`, `kit_shinobi.py`, `kit_specialist.py`, `strip_fabric`, `solid`, `kit_uchiha.py`, `kit_sarutobi.py`, `kit_shiranui.py`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Should `kit_academy.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07407407407407407 - nodes in this community are weakly interconnected._