# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 214 files · ~266,055 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3700 nodes · 8830 edges · 151 communities (125 shown, 26 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1013 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `53a5479e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- creator.py
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- kit_kurama.py
- Desk
- rnd
- kit_kunoichi.py
- mkit.py
- konoha/preview.py
- kit_suzuran.py
- 7. Systems in the beta
- .person
- catalogue.py
- Economy
- kit_rugged.py
- mockups.py
- fabric
- Box
- VarietyGuard
- Plan
- wide_sleeves
- Missions
- kit_market.py
- kit_kinoshita.py
- Catalogue
- 5. Data formats built for the whole story
- Offer
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- senbon
- 4. Technical architecture
- 6. The map
- CreatorRules
- 8. The beta, chapter by chapter
- 9. Delivery plan
- blocks.py
- k
- kokuto
- Run
- Plant
- News
- org.junit.jupiter.api.Test
- .choices
- Restyle
- missions.py
- kit_tsuchigumo.py
- paint.py
- .get
- Act
- Stage
- BondWorld
- kit_hagane.py
- Character creation
- 18. The engine
- list
- .classic
- Kind
- .answer
- Tex
- Squad
- Kind
- VillageScaleTest
- Bond
- .of
- Person
- .read
- Def
- Levels
- Deed
- Playthrough.java
- Life together
- AnswerTag
- Home
- Face
- Value
- Mood
- creator/preview.py
- 4.3 The noble clans
- kit_haruno.py
- Json
- Personality
- Village
- Rng
- Category
- .tier
- Meter
- Title
- .name
- Every building
- .of
- Side quests
- 4.4 The minor clans
- AgeStage
- 2. Quest framework
- Konoha: the build plan
- Label
- .daily
- Peeve
- Kind
- NamesTest
- 7. Inter-clan politics as quests
- Conflict
- .all
- kit_household.py
- .strings
- .look
- Tier
- Home
- noren
- Custom blocks
- .receive
- VisitsTest
- Source
- Pantry
- Flat
- SampleQuestions
- Json
- FirstFifteenHours.java
- .person
- Meters
- Rng
- Rank
- Keepsake
- .run
- Tier
- Template
- Look
- shade
- .everyKeyTheEngineEmitsIsListed
- S
- 8. Beta catalogue
- mission
- .valuesAndToneLandOnTheirPersonalityAndOppositePolesContradict
- 4. Clan quest lines
- .tidiness
- Data

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 194 edges
3. `solid()` - 151 edges
4. `Act` - 126 edges
5. `fabric()` - 109 edges
6. `Bond` - 66 edges
7. `Home` - 65 edges
8. `Village` - 63 edges
9. `strip_fabric()` - 59 edges
10. `Person` - 55 edges

## Surprising Connections (you probably didn't know these)
- `7. Questions and choices` --references--> `Question`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Question.java
- `11. What waits for Phase 0` --references--> `Player`  [INFERRED]
  MISSIONS.md → progression/missions/src/main/java/dev/shinobi/progression/mission/Player.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java
- `3.2 Templates` --references--> `escort()`  [INFERRED]
  SIDE_QUESTS.md → tools/missions/mkit.py
- `Player clans` --references--> `S`  [INFERRED]
  ROADMAP.md → tools/missions/mkit.py

## Import Cycles
- None detected.

## Communities (151 total, 26 thin omitted)

### Community 0 - "creator.py"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.15
Nodes (11): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+3 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.11
Nodes (21): render_player(), new_canvas(), save_canvas(), backdrop(), Canvas, Character, clan_renders(), composite() (+13 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.03
Nodes (43): drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), side_stripe(), sleeve_roll() (+35 more)

### Community 7 - "Story bible"
Cohesion: 0.05
Nodes (39): Commits, graphify, Naruto Minecraft, A rank, ANBU operations, B rank, C rank, D rank (+31 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "Desk"
Cohesion: 0.12
Nodes (4): Clients, Desk, Player, Unlocks

### Community 10 - "rnd"
Cohesion: 0.05
Nodes (27): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw() (+19 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - "mkit.py"
Cohesion: 0.17
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 13 - "konoha/preview.py"
Cohesion: 0.09
Nodes (20): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+12 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - ".person"
Cohesion: 0.08
Nodes (14): Activity, BondEvent, Conversation, Reply, Topic, Answer, Highlight, Invitation (+6 more)

### Community 17 - "catalogue.py"
Cohesion: 0.08
Nodes (14): build(), build(), build(), block_totals(), building_totals(), first_slice(), load(), main() (+6 more)

### Community 18 - "Economy"
Cohesion: 0.11
Nodes (10): Band, Economy, GradeRow, Performance, Grade, A, B, C (+2 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 21 - "fabric"
Cohesion: 0.03
Nodes (53): Shared helpers, How the pieces work, leg_cloth(), shirt(), waist(), belt(), body(), collar() (+45 more)

### Community 22 - "Box"
Cohesion: 0.06
Nodes (11): dark_seams(), strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece (+3 more)

### Community 23 - "VarietyGuard"
Cohesion: 0.09
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 24 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 25 - "wide_sleeves"
Cohesion: 0.18
Nodes (7): arm_bone(), arm_x(), armband(), roll(), seal_script(), seal_tags(), wide_sleeves()

### Community 26 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 27 - "kit_market.py"
Cohesion: 0.04
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Catalogue"
Cohesion: 0.14
Nodes (7): Catalogue, Mode, CLASSIC, VARIED, DeskDays, Profile, SimulationTest

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "Offer"
Cohesion: 0.11
Nodes (9): Rapport, End, ABANDONED, DONE, FAILED, PARTIAL, Result, Offer (+1 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.09
Nodes (30): build(), build_all(), catalog(), general_pool(), hex_rgb(), json_text(), load_all_groups(), load_characters() (+22 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "CreatorRules"
Cohesion: 0.20
Nodes (5): 13. Code, and what waits for Phase 0, Choices, CreatorRules, Outfit, Roots

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "blocks.py"
Cohesion: 0.16
Nodes (15): Streets, auto_uv(), block(), Block, box(), check(), compile_all(), main() (+7 more)

### Community 42 - "k"
Cohesion: 0.03
Nodes (35): deep_hood(), high_collar(), hood_down(), lenses(), back_crest(), shin_wraps(), flick(), gourd() (+27 more)

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.08
Nodes (14): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+6 more)

### Community 45 - "Plant"
Cohesion: 0.12
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 47 - "org.junit.jupiter.api.Test"
Cohesion: 0.07
Nodes (8): 19. Pacing, SquadTest, LivingTest, MoveTest, RentTest, FirstFifteenHoursTest, SeedsTest, AgeStageTest

### Community 49 - "Restyle"
Cohesion: 0.15
Nodes (9): 7. Locked and changeable, Restyle, Result, Venue, BARBER, HOME, LOCKED, SETTINGS (+1 more)

### Community 50 - "missions.py"
Cohesion: 0.17
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 51 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (7): glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 52 - "paint.py"
Cohesion: 0.02
Nodes (65): back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock(), ring_shell() (+57 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.10
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 58 - "Character creation"
Cohesion: 0.10
Nodes (20): 10. How residents address you, 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 59 - "18. The engine"
Cohesion: 0.13
Nodes (6): 18. The engine, FurnitureSet, HomeHangout, Practice, Session, CatalogTest

### Community 61 - ".classic"
Cohesion: 0.08
Nodes (10): 13. Data formats, BondBook, Fact, MemoryLine, Page, BondDialogue, BondDialogueTest, ConditionsAndEffectsTest (+2 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - ".answer"
Cohesion: 0.19
Nodes (4): Answered, Outcome, Questions, QuestionsTest

### Community 64 - "Tex"
Cohesion: 0.15
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 65 - "Squad"
Cohesion: 0.08
Nodes (3): BondEffects, Departure, Squad

### Community 66 - "Kind"
Cohesion: 0.14
Nodes (11): Kind, CLAN_SUMMONS, GIFT, INVITATION, LANDLADY, NEIGHBOUR, NOTE, STIPEND (+3 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.14
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (4): Bond, BondConditions, BondWeb, FollowUp

### Community 69 - ".of"
Cohesion: 0.12
Nodes (4): 8. The village talks, ConflictTest, GossipTest, Leaf

### Community 70 - "Person"
Cohesion: 0.09
Nodes (13): 12. The bond book, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 6. Shared experiences and moments (+5 more)

### Community 71 - ".read"
Cohesion: 0.23
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.13
Nodes (4): 3. Levels and story gates, Levels, LevelsTest, MemoryTest

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (3): Deed, Know, Gossip

### Community 75 - "Playthrough.java"
Cohesion: 0.06
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 76 - "Life together"
Cohesion: 0.14
Nodes (11): 15. Pacing, TimeAndPacingTest, 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Questions and choices (+3 more)

### Community 77 - "AnswerTag"
Cohesion: 0.10
Nodes (19): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+11 more)

### Community 78 - "Home"
Cohesion: 0.10
Nodes (3): Beta 1, Home, Photo

### Community 79 - "Face"
Cohesion: 0.20
Nodes (6): drawn_line(), button(), darken_rows(), line(), rivets(), Face

### Community 80 - "Value"
Cohesion: 0.12
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - "Mood"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - "creator/preview.py"
Cohesion: 0.17
Nodes (7): draw_player(), grown(), _label(), lineup(), samples(), stage_scale(), stages_sheet()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 86 - "Personality"
Cohesion: 0.11
Nodes (5): 20. What the roadmap asks of bonds, 5. Personality, Personality, Reaction, ReactionTest

### Community 87 - "Village"
Cohesion: 0.05
Nodes (13): 18. Village scale, 19. Society hooks, Base, ClanRelations, Mood, SocialTie, SocietyHook, House (+5 more)

### Community 89 - "Category"
Cohesion: 0.12
Nodes (17): Category, BATH, BED, DECOR, DISPLAY, FIXTURE, FLOOR, KITCHEN (+9 more)

### Community 90 - ".tier"
Cohesion: 0.17
Nodes (5): 11. Kindling Bond, Household, Bonfire, Flame, Kindling

### Community 91 - "Meter"
Cohesion: 0.09
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.15
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 94 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 95 - ".of"
Cohesion: 0.14
Nodes (5): Score, Rest, Rested, ComfortTest, RestTest

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - ".daily"
Cohesion: 0.15
Nodes (4): Friends, Day, Visit, Visits

### Community 103 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 104 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 105 - "NamesTest"
Cohesion: 0.25
Nodes (4): 1 Name, Names, PlayerName, NamesTest

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 109 - "kit_household.py"
Cohesion: 0.05
Nodes (24): arm_cloth(), bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta() (+16 more)

### Community 110 - ".strings"
Cohesion: 0.25
Nodes (3): Band, Mate, SquadPlan

### Community 112 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 113 - "Tier"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 114 - "Home"
Cohesion: 0.07
Nodes (27): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 15. Furniture, 16. Keepsakes, 1. Design rules (+19 more)

### Community 115 - "noren"
Cohesion: 0.19
Nodes (9): 2. Style guide: the Konoha kit, By building type, Facades and shop fronts, Lanterns, Shared palette, awning(), facing_states(), noren() (+1 more)

### Community 116 - "Custom blocks"
Cohesion: 0.15
Nodes (13): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+5 more)

### Community 117 - ".receive"
Cohesion: 0.35
Nodes (3): Gifts, Received, GiftsTest

### Community 118 - "VisitsTest"
Cohesion: 0.18
Nodes (3): Cast, Setup, VisitsTest

### Community 119 - "Source"
Cohesion: 0.17
Nodes (9): Piece, Source, CLAN, CRAFT, EVENT, FIXED, QUEST, SHOP (+1 more)

### Community 121 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 122 - "Flat"
Cohesion: 0.09
Nodes (11): 17. What the map needs, Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY, Flat (+3 more)

### Community 127 - "Meters"
Cohesion: 0.11
Nodes (7): Memory, Meters, Source, HEARD, SEEN, SELF, TOLD

### Community 129 - "Rank"
Cohesion: 0.21
Nodes (6): Rank, A, B, C, D, S

### Community 130 - "Keepsake"
Cohesion: 0.13
Nodes (8): Catalog, Keepsake, Kind, CLAN, FESTIVAL, GIFT, QUEST, STORY

### Community 131 - ".run"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 133 - "Tier"
Cohesion: 0.25
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 134 - "Template"
Cohesion: 0.31
Nodes (4): Branch, Step, Template, Twist

### Community 136 - "shade"
Cohesion: 0.24
Nodes (7): 6. Prototypes, Interior fittings, Roofs, kawara_ridge(), tatami(), tatami_top(), shade()

### Community 137 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.33
Nodes (3): DialogueKeys, DialogueKeysTest, 10. Content plan

### Community 138 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), merchant_camp_talk(), S, twist()

### Community 140 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 141 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 143 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 146 - ".tidiness"
Cohesion: 0.40
Nodes (4): Tidiness, LIVED_IN, MESSY, TIDY

## Knowledge Gaps
- **291 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+286 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1350 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `VillageSim.java`, `.person`, `Run`, `News`, `org.junit.jupiter.api.Test`, `Stage`, `list`, `.classic`, `.answer`, `Squad`, `VillageScaleTest`, `Bond`, `.of`, `Person`, `.read`, `Deed`, `Playthrough.java`, `AnswerTag`, `Village`, `.tier`, `.receive`, `VisitsTest`, `FirstFifteenHours.java`, `.person`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _291 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `creator.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07058001397624039 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `kit_uchiha.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `rnd`, `kit_kunoichi.py`, `kit_suzuran.py`, `kit_rugged.py`, `fabric`, `wide_sleeves`, `kit_market.py`, `kit_kinoshita.py`, `senbon`, `kit_tsuchigumo.py`, `paint.py`, `kit_hagane.py`, `Face`, `kit_haruno.py`, `kit_household.py`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Person` to `.of`, `.read`, `Story bible`, `Levels`, `Conflict`, `Life together`, `.person`, `Value`, `Village`, `Stage`, `Personality`, `.tier`, `.classic`, `Meters`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11282051282051282 - nodes in this community are weakly interconnected._