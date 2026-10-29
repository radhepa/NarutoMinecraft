# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 164 files · ~224,526 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3016 nodes · 7176 edges · 167 communities (120 shown, 47 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 790 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d31a9896`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- stamp
- mkit.py
- Clans
- kit_senju.py
- preview.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- kit_inuzuka.py
- kit_yuhi.py
- .all
- Economy
- Catalogue
- kit_suzuran.py
- 7. Systems in the beta
- solid
- masks.py
- lock
- kit_rugged.py
- kit_household.py
- kit_tobari.py
- .person
- .num
- Desk
- wide_sleeves
- strip_fabric
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
- seal_script
- 8. The beta, chapter by chapter
- 9. Delivery plan
- .get
- k
- Player
- Playthrough
- cel_box
- .strings
- Shared helpers
- Rng
- Box
- Seeds
- Face
- wave_band
- Json
- Act
- Stage
- BondWorld
- kit_nara.py
- .tier
- VarietyGuard
- list
- .classic
- solid
- Meters
- catalogue.py
- kit_uchiha.py
- Village
- VillageScaleTest
- Bond
- .of
- Bonds
- Garment
- Def
- Levels
- Deed
- Squad
- kit_hagane.py
- Tier
- BondWorld
- load_clans
- News
- Mood
- SquadTest
- 4.3 The noble clans
- S
- .page
- Peeve
- kit_morino.py
- .cap
- jika_tabi
- rnd
- Meter
- End
- mission
- kit_akimichi.py
- kit_aburame.py
- Side quests
- 4.4 The minor clans
- GossipTest
- 2. Quest framework
- catalogue.py
- 8. Beta catalogue
- kit_yamanaka.py
- katana
- senbon
- .effectiveLevel
- 7. Inter-clan politics as quests
- .answer
- tool_belt
- Plan
- Person
- blocks.py
- Title
- kokuto
- bandage_turns
- SeedsTest.java
- Side quest secrets
- Tex
- Conflict
- 4. Clan quest lines
- AnswerTag
- Kind
- street.py
- mesh_shirt
- Every building
- .romance
- kit_tsuchigumo.py
- kit_haruno.py
- 5. Process
- Custom blocks
- ClanRelations
- shag_face
- Template
- waves
- noren
- .receive
- rope_face
- shade
- shade
- wide_sleeves
- .everyKeyTheEngineEmitsIsListed
- leg_ring
- bands
- blossom
- checks
- Life together
- Mission catalogue
- QuestionsTest
- The village
- protector_plate
- dots
- rot_matrix
- ichimatsu
- kasuri
- overlap
- topknot
- Naruto Minecraft
- crest_patch
- obi
- paint.py
- bandolier

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
- `3.2 Templates` --references--> `escort()`  [INFERRED]
  SIDE_QUESTS.md → tools/missions/mkit.py

## Import Cycles
- None detected.

## Communities (167 total, 47 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.08
Nodes (18): stamp(), back_crest(), crescent(), decal(), shoulder_decal(), slanted_protector(), crest(), back_crest() (+10 more)

### Community 1 - "mkit.py"
Cohesion: 0.18
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "preview.py"
Cohesion: 0.06
Nodes (40): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+32 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.06
Nodes (15): drawstrings(), forearm_wraps(), holster(), hood_down(), leg_cloth(), ribbed(), sash(), shin_wraps() (+7 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 12 - "Economy"
Cohesion: 0.10
Nodes (10): Band, Economy, GradeRow, Performance, Grade, A, B, C (+2 more)

### Community 13 - "Catalogue"
Cohesion: 0.16
Nodes (8): Catalogue, Mode, CLASSIC, VARIED, DeskDays, Profile, Run, SimulationTest

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - "solid"
Cohesion: 0.07
Nodes (14): face_mask(), white_fang_tanto(), hakama_legs(), coat_skirts(), pauldron(), scarf(), trench_knife(), cane() (+6 more)

### Community 17 - "masks.py"
Cohesion: 0.16
Nodes (7): How the pieces work, mesh(), tanto(), beak(), bump(), ears(), strap()

### Community 18 - "lock"
Cohesion: 0.11
Nodes (9): back_fan(), bangs(), lock(), sidelocks(), blunt_fringe(), hime_locks(), parted_fringe(), beard() (+1 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.09
Nodes (10): baggy_legs(), dread(), knot_bun(), leg_wraps(), patch(), rope_hair(), shin_guard(), soft_boots() (+2 more)

### Community 20 - "kit_household.py"
Cohesion: 0.12
Nodes (7): collar_band(), geta(), robe_skirt(), sash(), skirt(), socks(), stripes()

### Community 21 - "kit_tobari.py"
Cohesion: 0.05
Nodes (22): shirt(), anbu_plates(), bandolier(), coat_skirts(), cross_armband(), ink_stains(), scroll_tube(), seal_trim() (+14 more)

### Community 22 - ".person"
Cohesion: 0.10
Nodes (10): Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan, Together (+2 more)

### Community 24 - "Desk"
Cohesion: 0.11
Nodes (9): Desk, Result, Offer, Rank, A, B, C, D (+1 more)

### Community 25 - "wide_sleeves"
Cohesion: 0.28
Nodes (5): arm_bone(), arm_x(), armband(), roll(), wide_sleeves()

### Community 26 - "strip_fabric"
Cohesion: 0.10
Nodes (11): arm_cloth(), cloth_shoes(), trouser_legs(), waist(), kimono_sleeves(), tabi(), gloves(), heavy_boots() (+3 more)

### Community 27 - "kit_market.py"
Cohesion: 0.04
Nodes (24): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+16 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.12
Nodes (11): back_crest(), crest(), kyahan(), mallet(), pencil(), _piece(), sashiko(), saw() (+3 more)

### Community 29 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "kit_field.py"
Cohesion: 0.07
Nodes (14): arm_guards(), blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards() (+6 more)

### Community 32 - "outputs"
Cohesion: 0.13
Nodes (21): build(), build_all(), catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors() (+13 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 42 - "k"
Cohesion: 0.16
Nodes (10): belt(), collar(), sword_strap(), wrap_front(), wave_band(), neckline(), pouch(), stockings() (+2 more)

### Community 44 - "Playthrough"
Cohesion: 0.09
Nodes (16): 15. Pacing, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+8 more)

### Community 45 - "cel_box"
Cohesion: 0.08
Nodes (17): cel_box(), cel_face(), curtain(), ring_shell(), spike(), tie(), back_sheet(), ear_panels() (+9 more)

### Community 46 - ".strings"
Cohesion: 0.25
Nodes (3): Band, Mate, SquadPlan

### Community 47 - "Shared helpers"
Cohesion: 0.17
Nodes (7): Shared helpers, braid(), body(), flaps(), footwear(), legs(), wraps()

### Community 49 - "Box"
Cohesion: 0.09
Nodes (6): band(), hem(), strip_line(), Box, Layer, Piece

### Community 51 - "Face"
Cohesion: 0.20
Nodes (6): drawn_line(), button(), darken_rows(), line(), rivets(), Face

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.10
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 57 - "kit_nara.py"
Cohesion: 0.18
Nodes (6): crown(), back_crest(), crest(), pulled_back(), tuft(), scalp()

### Community 58 - ".tier"
Cohesion: 0.15
Nodes (5): 11. Kindling Bond, Bonfire, Flame, Kindling, Recruitment

### Community 59 - "VarietyGuard"
Cohesion: 0.13
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 60 - "list"
Cohesion: 0.05
Nodes (5): Stage, ADULT, CHILD, TEEN, Leaf

### Community 61 - ".classic"
Cohesion: 0.16
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 62 - "solid"
Cohesion: 0.08
Nodes (11): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), tabi_boots() (+3 more)

### Community 63 - "Meters"
Cohesion: 0.10
Nodes (7): Memory, Meters, Source, HEARD, SEEN, SELF, TOLD

### Community 64 - "catalogue.py"
Cohesion: 0.20
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 65 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 66 - "Village"
Cohesion: 0.11
Nodes (7): 18. Village scale, House, Tier, BACKGROUND, CAST, KNOWN, Village

### Community 67 - "VillageScaleTest"
Cohesion: 0.12
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.04
Nodes (5): 12. The bond book, Bond, BondConditions, BondWeb, FollowUp

### Community 70 - "Bonds"
Cohesion: 0.12
Nodes (13): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 5. Personality (+5 more)

### Community 71 - "Garment"
Cohesion: 0.24
Nodes (4): compatible(), Garment, key_rgba(), world_bounds()

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 74 - "Deed"
Cohesion: 0.10
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 75 - "Squad"
Cohesion: 0.07
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 76 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 77 - "Tier"
Cohesion: 0.13
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 78 - "BondWorld"
Cohesion: 0.10
Nodes (3): BondDialogue, BondWorld, Household

### Community 79 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 81 - "Mood"
Cohesion: 0.15
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), merchant_camp_talk(), S, twist()

### Community 85 - ".page"
Cohesion: 0.27
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Peeve"
Cohesion: 0.06
Nodes (27): 20. What the roadmap asks of bonds, ClanProfile, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY (+19 more)

### Community 87 - "kit_morino.py"
Cohesion: 0.20
Nodes (4): combed_back(), head_cloth(), nape_hem(), forehead_protector()

### Community 89 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 90 - "rnd"
Cohesion: 0.12
Nodes (10): sprigs(), clipped(), camo(), cape(), ragged(), hair_box(), hair_face(), hair_shade() (+2 more)

### Community 91 - "Meter"
Cohesion: 0.09
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 93 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 94 - "kit_akimichi.py"
Cohesion: 0.10
Nodes (10): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+2 more)

### Community 95 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "catalogue.py"
Cohesion: 0.12
Nodes (5): check(), main(), build(), build(), build()

### Community 101 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 102 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 104 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 105 - ".effectiveLevel"
Cohesion: 0.16
Nodes (4): Conversation, Reply, Topic, 6. Conversation

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - ".answer"
Cohesion: 0.17
Nodes (3): Answered, Outcome, Questions

### Community 108 - "tool_belt"
Cohesion: 0.33
Nodes (3): chisel(), nail_pouch(), tool_belt()

### Community 110 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 113 - "blocks.py"
Cohesion: 0.15
Nodes (15): Roofs, Streets, auto_uv(), block(), Block, box(), compile_all(), kawara_ridge() (+7 more)

### Community 114 - "Title"
Cohesion: 0.16
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 115 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 118 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 119 - "Tex"
Cohesion: 0.14
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 120 - "Conflict"
Cohesion: 0.11
Nodes (8): 13. Data formats, Conflict, State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 121 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 122 - "AnswerTag"
Cohesion: 0.06
Nodes (28): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+20 more)

### Community 123 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 126 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 128 - "kit_tsuchigumo.py"
Cohesion: 0.17
Nodes (6): glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 129 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 130 - "5. Process"
Cohesion: 0.50
Nodes (4): 5. Process, Order of work, The pieces, What needs you at your PC

### Community 131 - "Custom blocks"
Cohesion: 0.13
Nodes (14): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+6 more)

### Community 132 - "ClanRelations"
Cohesion: 0.12
Nodes (9): Base, ClanRelations, Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL (+1 more)

### Community 134 - "Template"
Cohesion: 0.21
Nodes (4): Branch, Step, Template, Twist

### Community 136 - "noren"
Cohesion: 0.12
Nodes (18): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 6. Prototypes, 7. Effort estimate, 8. Registration notes for Phase 0, By building type, Calibration, Contents (+10 more)

### Community 137 - ".receive"
Cohesion: 0.35
Nodes (3): Gifts, Received, GiftsTest

### Community 141 - "shade"
Cohesion: 0.25
Nodes (7): 4. Block catalogue, Interior fittings, Totals, Vanilla mappings, tatami(), tatami_top(), shade()

### Community 143 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.18
Nodes (4): DialogueKeys, DialogueKeysTest, ReactionTest, 10. Content plan

### Community 150 - "Life together"
Cohesion: 0.22
Nodes (9): 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Questions and choices, 8. Data and quest hooks, 9. Pacing with time together (+1 more)

### Community 151 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 154 - "The village"
Cohesion: 0.29
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 155 - "protector_plate"
Cohesion: 0.22
Nodes (4): arm_protector(), protector_plate(), backward_bandana(), flicks()

### Community 157 - "rot_matrix"
Cohesion: 0.29
Nodes (3): wave_lock(), piece_corners(), rot_matrix()

### Community 162 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 182 - "paint.py"
Cohesion: 0.12
Nodes (6): back_crest(), bandaged_arm(), anbu_arms(), bandage(), flak_vest(), cloth_shade()

## Knowledge Gaps
- **226 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+221 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1155 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **47 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `.receive`, `.person`, `QuestionsTest`, `Playthrough`, `Stage`, `BondWorld`, `.tier`, `list`, `.classic`, `Village`, `VillageScaleTest`, `Bond`, `.of`, `Deed`, `Squad`, `News`, `SquadTest`, `.page`, `GossipTest`, `.effectiveLevel`, `.answer`, `Person`, `Title`, `AnswerTag`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _226 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `stamp` be split into smaller, more focused modules?**
  _Cohesion score 0.07897793263646923 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Village`, `Bond`, `ClanRelations`, `Deed`, `ROADMAP.md`, `Squad`, `Playthrough`, `Person`, `Mood`, `Peeve`, `Stage`, `Conflict`, `.person`, `.tier`, `.cap`, `.romance`, `Meters`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `stamp`, `kit_haruno.py`, `kit_tsuchigumo.py`, `kit_senju.py`, `Custom blocks`, `shag_face`, `kit_academy.py`, `waves`, `kit_kurama.py`, `kit_inuzuka.py`, `rope_face`, `kit_yuhi.py`, `wide_sleeves`, `kit_suzuran.py`, `solid`, `masks.py`, `lock`, `kit_rugged.py`, `kit_household.py`, `blossom`, `kit_tobari.py`, `wide_sleeves`, `strip_fabric`, `kit_market.py`, `kit_kinoshita.py`, `protector_plate`, `kit_field.py`, `obi`, `cel_box`, `Shared helpers`, `Box`, `Face`, `paint.py`, `bandolier`, `kit_nara.py`, `solid`, `kit_uchiha.py`, `kit_hagane.py`, `kit_morino.py`, `jika_tabi`, `rnd`, `kit_akimichi.py`, `kit_aburame.py`, `kit_yamanaka.py`, `senbon`, `tool_belt`, `bandage_turns`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Should `preview.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05707450444292549 - nodes in this community are weakly interconnected._