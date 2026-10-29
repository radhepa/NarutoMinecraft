# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 184 files · ~243,877 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3314 nodes · 7927 edges · 145 communities (113 shown, 32 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 913 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d31a9896`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- mkit.py
- kit_uchiha.py
- Clans
- Economy
- render.py
- living_eyes.py
- solid
- Story bible
- rnd
- kit_inuzuka.py
- kit_yuhi.py
- VarietyGuard
- Desk
- Missions
- kit_suzuran.py
- 7. Systems in the beta
- .person
- creator.py
- Catalogue
- kit_rugged.py
- Plan
- Meters
- .get
- .receive
- Meter
- Look
- CreatorRules
- kit_market.py
- kit_kinoshita.py
- .num
- 5. Data formats built for the whole story
- strip_fabric
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_shiranui.py
- 4. Technical architecture
- 6. The map
- blocks.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- missions.py
- kit_akimichi.py
- kokuto
- Playthrough
- Player
- render_kit.py
- mockups.py
- Personality
- Box
- Json
- Rng
- kit_morino.py
- kit_hagane.py
- Act
- Stage
- preview.py
- org.junit.jupiter.api.Test
- Life together
- Template
- Character creation
- Kind
- .answer
- .everyKeyTheEngineEmitsIsListed
- Squad
- kit_tsuchigumo.py
- VillageScaleTest
- Bond
- .of
- .classmate
- Question
- Def
- Levels
- Deed
- Tex
- Seeds
- AnswerTag
- BondWorld
- Face
- Konoha: the build plan
- Mood
- .read
- 4.3 The noble clans
- kit_haruno.py
- .all
- Value
- NamesTest
- .strings
- .look
- .tier
- Restyle
- Title
- .name
- creator/preview.py
- AgeStage
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- Memory
- Label
- org.junit.jupiter.api.Test
- Village
- Every building
- Kind
- 7. Inter-clan politics as quests
- Conflict
- Custom blocks
- SquadTest
- News
- Power
- Json
- catalogue.py
- Rng
- S
- Mission catalogue
- 8. Beta catalogue
- pathlib
- 4. Clan quest lines
- The village
- .write
- cel_box
- mission
- Stage
- shade
- End
- noren
- Side quest secrets
- Tier
- Rng
- k
- fabric
- Naruto Minecraft
- Data
- resolve

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
- `11. What waits for Phase 0` --references--> `Player`  [INFERRED]
  MISSIONS.md → progression/missions/src/main/java/dev/shinobi/progression/mission/Player.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java

## Import Cycles
- None detected.

## Communities (145 total, 32 thin omitted)

### Community 0 - "mkit.py"
Cohesion: 0.18
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.15
Nodes (12): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+4 more)

### Community 3 - "Economy"
Cohesion: 0.09
Nodes (11): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+3 more)

### Community 4 - "render.py"
Cohesion: 0.15
Nodes (17): new_canvas(), backdrop(), Canvas, Character, clan_renders(), cube_quads(), font(), general_renders() (+9 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.03
Nodes (37): How the pieces work, drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps() (+29 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "rnd"
Cohesion: 0.03
Nodes (32): sprigs(), back_crest(), bead_clip(), brush_pin(), brush_stroke(), ink_clouds(), kimono_sleeves(), part_line() (+24 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "VarietyGuard"
Cohesion: 0.11
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 12 - "Desk"
Cohesion: 0.13
Nodes (8): Desk, Offer, Rank, A, B, C, D, S

### Community 13 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - ".person"
Cohesion: 0.08
Nodes (13): Activity, BondEvent, Conversation, Reply, Topic, Answer, Highlight, Invitation (+5 more)

### Community 17 - "creator.py"
Cohesion: 0.09
Nodes (18): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), roll_look() (+10 more)

### Community 18 - "Catalogue"
Cohesion: 0.16
Nodes (8): Catalogue, Mode, CLASSIC, VARIED, DeskDays, Profile, Run, SimulationTest

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (16): baggy_legs(), camo(), cape(), dread(), leg_wraps(), patch(), ragged(), rope() (+8 more)

### Community 20 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 23 - ".receive"
Cohesion: 0.35
Nodes (3): Gifts, Received, GiftsTest

### Community 24 - "Meter"
Cohesion: 0.13
Nodes (7): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 25 - "Look"
Cohesion: 0.14
Nodes (4): 9. Age stages, Look, Result, RestyleAndGrowUpTest

### Community 26 - "CreatorRules"
Cohesion: 0.20
Nodes (5): 13. Code, and what waits for Phase 0, Choices, CreatorRules, Outfit, Roots

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kyahan() (+14 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "strip_fabric"
Cohesion: 0.03
Nodes (44): leg_cloth(), waist(), arm_guards(), blouse(), cargo(), collar(), gloves(), half_sleeves() (+36 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.09
Nodes (29): build(), build_all(), catalog(), general_pool(), hex_rgb(), json_text(), load_all_groups(), load_characters() (+21 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "kit_shiranui.py"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "blocks.py"
Cohesion: 0.16
Nodes (15): Streets, auto_uv(), block(), Block, box(), check(), compile_all(), main() (+7 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+1 more)

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Playthrough"
Cohesion: 0.08
Nodes (16): 15. Pacing, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+8 more)

### Community 46 - "render_kit.py"
Cohesion: 0.13
Nodes (8): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 47 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 48 - "Personality"
Cohesion: 0.09
Nodes (10): 5. Personality, Personality, Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH (+2 more)

### Community 49 - "Box"
Cohesion: 0.07
Nodes (10): strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece, piece_corners() (+2 more)

### Community 52 - "kit_morino.py"
Cohesion: 0.08
Nodes (14): cel_face(), ring_shell(), crown(), back_crest(), clipped(), coat_skirts(), combed_back(), gloves() (+6 more)

### Community 53 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "preview.py"
Cohesion: 0.18
Nodes (13): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+5 more)

### Community 58 - "Life together"
Cohesion: 0.20
Nodes (10): 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 6. Conversation, 7. Questions and choices, 8. Data and quest hooks (+2 more)

### Community 59 - "Template"
Cohesion: 0.21
Nodes (4): Branch, Step, Template, Twist

### Community 61 - "Character creation"
Cohesion: 0.11
Nodes (19): 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair, 3. Where the creator sits in the opening (+11 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - ".answer"
Cohesion: 0.19
Nodes (3): QuestionsCompiledTest, QuestionsTest, SampleQuestions

### Community 64 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.33
Nodes (3): DialogueKeys, DialogueKeysTest, 10. Content plan

### Community 66 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (7): glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 67 - "VillageScaleTest"
Cohesion: 0.09
Nodes (4): ClanProfile, Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (5): 12. The bond book, Bond, BondConditions, BondWeb, FollowUp

### Community 69 - ".of"
Cohesion: 0.12
Nodes (5): 8. The village talks, ConditionsAndEffectsTest, GossipTest, Leaf, VillageTest

### Community 72 - "Def"
Cohesion: 0.06
Nodes (16): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+8 more)

### Community 73 - "Levels"
Cohesion: 0.16
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 75 - "Tex"
Cohesion: 0.15
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 77 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 78 - "BondWorld"
Cohesion: 0.07
Nodes (5): BondEffects, BondWorld, Answered, Outcome, Questions

### Community 79 - "Face"
Cohesion: 0.14
Nodes (9): drawn_line(), button(), curls_face(), dark_seams(), darken_rows(), line(), rivets(), Face (+1 more)

### Community 80 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 81 - "Mood"
Cohesion: 0.15
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 86 - "Value"
Cohesion: 0.08
Nodes (23): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+15 more)

### Community 87 - "NamesTest"
Cohesion: 0.19
Nodes (5): 10. How residents address you, 1 Name, Names, PlayerName, NamesTest

### Community 88 - ".strings"
Cohesion: 0.25
Nodes (3): Band, Mate, SquadPlan

### Community 89 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 90 - ".tier"
Cohesion: 0.08
Nodes (11): 11. Kindling Bond, BondBook, Fact, MemoryLine, Page, BondDialogue, Household, Bonfire (+3 more)

### Community 91 - "Restyle"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 92 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.25
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 94 - "creator/preview.py"
Cohesion: 0.18
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 95 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "Person"
Cohesion: 0.08
Nodes (4): 20. What the roadmap asks of bonds, Person, Schedule, Standing

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.15
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "org.junit.jupiter.api.Test"
Cohesion: 0.08
Nodes (3): BondDialogueTest, SeedsTest, AgeStageTest

### Community 103 - "Village"
Cohesion: 0.06
Nodes (8): 18. Village scale, 19. Society hooks, Base, ClanRelations, SocialTie, SocietyHook, House, Village

### Community 104 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 105 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "Conflict"
Cohesion: 0.09
Nodes (13): 13. Data formats, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 6. Shared experiences and moments (+5 more)

### Community 108 - "Custom blocks"
Cohesion: 0.15
Nodes (13): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+5 more)

### Community 113 - "Power"
Cohesion: 0.13
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 117 - "catalogue.py"
Cohesion: 0.17
Nodes (10): story_reserved_family_names(), block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table() (+2 more)

### Community 119 - "S"
Cohesion: 0.25
Nodes (4): 6. Squad missions, travel(), S, twist()

### Community 120 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 122 - "pathlib"
Cohesion: 0.11
Nodes (5): build(), build(), build(), paste(), scene()

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 124 - "The village"
Cohesion: 0.29
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 126 - "cel_box"
Cohesion: 0.03
Nodes (40): bangs(), cel_box(), curtain(), tie(), topknot(), back_sheet(), blunt_fringe(), ear_panels() (+32 more)

### Community 127 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 128 - "Stage"
Cohesion: 0.40
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 129 - "shade"
Cohesion: 0.24
Nodes (7): 6. Prototypes, Interior fittings, Roofs, kawara_ridge(), tatami(), tatami_top(), shade()

### Community 130 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 131 - "noren"
Cohesion: 0.19
Nodes (9): 2. Style guide: the Konoha kit, By building type, Facades and shop fronts, Lanterns, Shared palette, awning(), facing_states(), noren() (+1 more)

### Community 133 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 134 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 136 - "k"
Cohesion: 0.04
Nodes (38): Shared helpers, braid(), deep_hood(), high_collar(), hood_down(), lenses(), arm_bone(), arm_x() (+30 more)

### Community 137 - "fabric"
Cohesion: 0.03
Nodes (51): back_fan(), lock(), sidelocks(), spike(), stamp(), back_crest(), shirt(), crescent() (+43 more)

### Community 138 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

## Knowledge Gaps
- **234 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+229 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1224 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **32 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `.person`, `Meters`, `.receive`, `Playthrough`, `Stage`, `Playthrough.java`, `.answer`, `Squad`, `VillageScaleTest`, `Bond`, `.of`, `.classmate`, `Question`, `Levels`, `Deed`, `.read`, `.tier`, `Person`, `Village`, `Conflict`, `SquadTest`, `News`, `.write`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _234 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `kit_uchiha.py`, `solid`, `rnd`, `fabric`, `kit_inuzuka.py`, `kit_yuhi.py`, `kit_suzuran.py`, `kit_rugged.py`, `kit_market.py`, `kit_kinoshita.py`, `strip_fabric`, `kit_shiranui.py`, `kit_akimichi.py`, `kit_morino.py`, `kit_hagane.py`, `kit_tsuchigumo.py`, `Face`, `kit_haruno.py`, `cel_box`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Should `Economy` be split into smaller, more focused modules?**
  _Cohesion score 0.09487179487179487 - nodes in this community are weakly interconnected._
- **Why does `Act` connect `Act` to `VillageScaleTest`, `Memory`, `Bond`, `.classmate`, `Question`, `Def`, `Deed`, `Conflict`, `BondWorld`, `.person`, `News`, `.read`, `Personality`, `Meters`, `Value`, `Meter`, `.tier`, `Playthrough.java`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1471264367816092 - nodes in this community are weakly interconnected._