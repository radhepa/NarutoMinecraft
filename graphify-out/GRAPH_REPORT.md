# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 233 files · ~287,160 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3950 nodes · 9394 edges · 172 communities (130 shown, 42 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1068 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `34b4e875`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Home
- fabric
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- creator.py
- Story bible
- kit_kurama.py
- kit_hagane.py
- kit_yuhi.py
- Economy
- mkit.py
- Roster
- paint.py
- 7. Systems in the beta
- .roll
- CreatorRules
- stamp
- kit_rugged.py
- FirstFifteenHours.java
- strip_fabric
- Box
- Category
- Meters
- wide_sleeves
- kit_field.py
- k
- solid
- .play
- 5. Data formats built for the whole story
- Seeds
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- Playthrough.java
- 4. Technical architecture
- 6. The map
- .num
- 8. The beta, chapter by chapter
- 9. Delivery plan
- mockups.py
- .of
- RosterTest
- Run
- Desk
- .talk
- Plan
- build
- Missions
- kit_tsuchigumo.py
- Restyle
- blocks.py
- Niche
- Act
- Stage
- Catalogue
- .choices
- .run
- Flat
- konoha/preview.py
- Kind
- Question
- noren
- Squad
- VillageScaleTest
- Bond
- .of
- Bonds
- The village
- Def
- Levels
- Deed
- Tex
- SocialTie
- AnswerTag
- BondWorld
- paint.py
- News
- Mood
- BondEvent
- 4.3 The noble clans
- Plant
- missions.py
- Personality
- roster.py
- CourtshipTest
- pathlib
- .tier
- Meter
- Title
- Character creation
- Home
- VisitsTest
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- Memory
- Label
- list
- .romance
- Kind
- .xpAt
- 7. Inter-clan politics as quests
- AgeStage
- State
- kit_household.py
- org.junit.jupiter.api.Test
- .person
- Tier
- Tier
- .cap
- catalogue.py
- Ranks
- creator/preview.py
- Player
- 8. Beta catalogue
- .get
- 4. Clan quest lines
- Keepsake
- kit_kunoichi.py
- World
- Json
- Rng
- ClanPower
- render_kit.py
- Every building
- Kind
- .all
- NamesTest
- Stretch
- Template
- Rng
- Side quest secrets
- .strings
- Pantry
- Json
- Naruto Minecraft
- Rng
- VillageSim.java
- Look
- Label
- Tier
- TimeAndPacingTest
- shade
- S
- Tier
- Rng
- Mission catalogue
- mission
- 15. Furniture
- FurnitureSet
- End
- 5. Process
- street.py
- Outfit
- Data
- Custom blocks

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 196 edges
3. `solid()` - 151 edges
4. `Act` - 128 edges
5. `fabric()` - 109 edges
6. `Bond` - 66 edges
7. `Home` - 66 edges
8. `Village` - 63 edges
9. `strip_fabric()` - 59 edges
10. `Person` - 55 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `7. Questions and choices` --references--> `Question`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Question.java
- `9. Pacing with time together` --references--> `TimeAndPacingTest`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `11. What waits for Phase 0` --references--> `Player`  [INFERRED]
  MISSIONS.md → progression/missions/src/main/java/dev/shinobi/progression/mission/Player.java

## Import Cycles
- None detected.

## Communities (172 total, 42 thin omitted)

### Community 0 - "Home"
Cohesion: 0.07
Nodes (10): Friends, Home, Tidiness, LIVED_IN, MESSY, TIDY, Photo, Day (+2 more)

### Community 1 - "fabric"
Cohesion: 0.03
Nodes (38): back_crest(), hood_down(), collar(), kimono_sleeves(), kyahan(), tabi(), back_crest(), gloves() (+30 more)

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (20): new_canvas(), save_canvas(), backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads() (+12 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "creator.py"
Cohesion: 0.09
Nodes (18): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), roll_look() (+10 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "kit_hagane.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.06
Nodes (19): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar(), bandage_turns() (+11 more)

### Community 11 - "Economy"
Cohesion: 0.09
Nodes (12): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+4 more)

### Community 12 - "mkit.py"
Cohesion: 0.17
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 13 - "Roster"
Cohesion: 0.09
Nodes (5): Hooks for the other mods, Contribution, GrowthEvent, Grower, Roster

### Community 14 - "paint.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - ".roll"
Cohesion: 0.09
Nodes (11): Activity, BondEvent, Answer, FollowUp, Highlight, Invitation, Outcome, Plan (+3 more)

### Community 17 - "CreatorRules"
Cohesion: 0.13
Nodes (6): 13. Code, and what waits for Phase 0, CreatorRules, Roots, LifeRoll, Rolled, LifeRollTest

### Community 18 - "stamp"
Cohesion: 0.03
Nodes (53): back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock(), ring_shell() (+45 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "FirstFifteenHours.java"
Cohesion: 0.18
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 21 - "strip_fabric"
Cohesion: 0.04
Nodes (40): Shared helpers, How the pieces work, drawstrings(), forearm_wraps(), leg_cloth(), shirt(), side_stripe(), stripes() (+32 more)

### Community 22 - "Box"
Cohesion: 0.08
Nodes (9): strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece, piece_corners() (+1 more)

### Community 23 - "Category"
Cohesion: 0.07
Nodes (27): Catalog, Category, BATH, BED, DECOR, DISPLAY, FIXTURE, FLOOR (+19 more)

### Community 25 - "wide_sleeves"
Cohesion: 0.18
Nodes (7): arm_bone(), arm_x(), armband(), roll(), seal_script(), seal_tags(), wide_sleeves()

### Community 26 - "kit_field.py"
Cohesion: 0.07
Nodes (13): arm_guards(), blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards() (+5 more)

### Community 27 - "k"
Cohesion: 0.02
Nodes (52): deep_hood(), high_collar(), hood_down(), lenses(), holster(), ribbed(), shin_wraps(), sleeve_roll() (+44 more)

### Community 28 - "solid"
Cohesion: 0.03
Nodes (44): sash(), turned_hem(), gourd(), lames(), snack_pouch(), sode(), bracers(), crown() (+36 more)

### Community 29 - ".play"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.12
Nodes (23): catalog(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_eye_colors() (+15 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - ".num"
Cohesion: 0.12
Nodes (4): Clients, Rapport, SlotFiller, VarietyGuard

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 42 - ".of"
Cohesion: 0.13
Nodes (6): Comfort, Score, Rest, Rested, ComfortTest, RestTest

### Community 43 - "RosterTest"
Cohesion: 0.14
Nodes (3): BondInput, Day, RosterTest

### Community 44 - "Run"
Cohesion: 0.08
Nodes (14): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+6 more)

### Community 45 - "Desk"
Cohesion: 0.13
Nodes (8): Desk, Offer, Rank, A, B, C, D, S

### Community 46 - ".talk"
Cohesion: 0.08
Nodes (18): 13. Data formats, BondDialogue, Conversation, Reply, Topic, DialogueKeys, BondDialogueTest, 10. Content plan (+10 more)

### Community 47 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 50 - "kit_tsuchigumo.py"
Cohesion: 0.15
Nodes (7): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 51 - "Restyle"
Cohesion: 0.13
Nodes (10): 7. Locked and changeable, Restyle, Result, Venue, BARBER, HOME, LOCKED, SETTINGS (+2 more)

### Community 52 - "blocks.py"
Cohesion: 0.15
Nodes (15): Roofs, Streets, auto_uv(), block(), Block, box(), compile_all(), kawara_ridge() (+7 more)

### Community 53 - "Niche"
Cohesion: 0.11
Nodes (13): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+5 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (76): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+68 more)

### Community 55 - "Stage"
Cohesion: 0.15
Nodes (9): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+1 more)

### Community 56 - "Catalogue"
Cohesion: 0.16
Nodes (8): Catalogue, Mode, CLASSIC, VARIED, DeskDays, Profile, Run, SimulationTest

### Community 58 - ".run"
Cohesion: 0.15
Nodes (8): 19. Pacing, Practice, Session, FirstFifteenHours, Result, Slice, Snapshot, FirstFifteenHoursTest

### Community 59 - "Flat"
Cohesion: 0.10
Nodes (12): 17. What the map needs, 2. The flat, The Classic flat: `flat.leaf_block.3a`, Varied candidates, Tier, BARE, BELOVED, COMFORTABLE (+4 more)

### Community 61 - "konoha/preview.py"
Cohesion: 0.16
Nodes (13): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+5 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Question"
Cohesion: 0.12
Nodes (7): Answer, Question, Answered, Outcome, Questions, QuestionsCompiledTest, QuestionsTest

### Community 64 - "noren"
Cohesion: 0.12
Nodes (18): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 6. Prototypes, 7. Effort estimate, 8. Registration notes for Phase 0, By building type, Calibration, Contents (+10 more)

### Community 65 - "Squad"
Cohesion: 0.10
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 67 - "VillageScaleTest"
Cohesion: 0.12
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.04
Nodes (6): 20. What the roadmap asks of bonds, Bond, BondConditions, BondWeb, ConditionsAndEffectsTest, VillageTest

### Community 69 - ".of"
Cohesion: 0.11
Nodes (3): ConflictTest, GossipTest, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.09
Nodes (18): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+10 more)

### Community 71 - "The village"
Cohesion: 0.29
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 75 - "Tex"
Cohesion: 0.14
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 77 - "AnswerTag"
Cohesion: 0.11
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 78 - "BondWorld"
Cohesion: 0.06
Nodes (3): BondEffects, BondWorld, Standing

### Community 79 - "paint.py"
Cohesion: 0.06
Nodes (25): flick(), puff(), quilt(), clipped(), combed_back(), nape_hem(), band(), button() (+17 more)

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "BondEvent"
Cohesion: 0.21
Nodes (7): 18. The engine, 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest, HomeHangout

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "Plant"
Cohesion: 0.13
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 85 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 86 - "Personality"
Cohesion: 0.05
Nodes (26): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+18 more)

### Community 87 - "roster.py"
Cohesion: 0.17
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 89 - "pathlib"
Cohesion: 0.12
Nodes (5): check(), main(), build(), build(), build()

### Community 90 - ".tier"
Cohesion: 0.09
Nodes (11): 11. Kindling Bond, 12. The bond book, BondBook, Fact, MemoryLine, Page, Household, Bonfire (+3 more)

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Character creation"
Cohesion: 0.11
Nodes (19): 10. How residents address you, 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair (+11 more)

### Community 94 - "Home"
Cohesion: 0.11
Nodes (19): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 1. Design rules, 20. By beta slice (+11 more)

### Community 95 - "VisitsTest"
Cohesion: 0.23
Nodes (3): Cast, Setup, VisitsTest

### Community 96 - "Side quests"
Cohesion: 0.22
Nodes (9): 1. Scope and budget, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents, In the beta, Later (foundation), Later one-offs (foundation) (+1 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "Person"
Cohesion: 0.07
Nodes (4): Conflict, Person, Recruitment, Schedule

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.20
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 104 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 105 - ".xpAt"
Cohesion: 0.18
Nodes (3): Technique, CurveAndTierTest, TechniqueTest

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "AgeStage"
Cohesion: 0.13
Nodes (6): 9. Age stages, AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 108 - "State"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 109 - "kit_household.py"
Cohesion: 0.04
Nodes (26): arm_cloth(), bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta() (+18 more)

### Community 110 - "org.junit.jupiter.api.Test"
Cohesion: 0.08
Nodes (6): SquadTest, CatalogTest, LivingTest, MoveTest, SeedsTest, AgeStageTest

### Community 113 - "Tier"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 114 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 117 - "catalogue.py"
Cohesion: 0.17
Nodes (10): story_reserved_family_names(), block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table() (+2 more)

### Community 118 - "Ranks"
Cohesion: 0.11
Nodes (17): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+9 more)

### Community 119 - "creator/preview.py"
Cohesion: 0.16
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 125 - "Keepsake"
Cohesion: 0.12
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 126 - "kit_kunoichi.py"
Cohesion: 0.08
Nodes (11): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), tabi_boots() (+3 more)

### Community 127 - "World"
Cohesion: 0.15
Nodes (4): 9. The generator, Resident, World, SampleVillage

### Community 130 - "ClanPower"
Cohesion: 0.16
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 131 - "render_kit.py"
Cohesion: 0.19
Nodes (7): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 132 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 133 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 135 - "NamesTest"
Cohesion: 0.23
Nodes (4): 1 Name, Names, PlayerName, NamesTest

### Community 137 - "Stretch"
Cohesion: 0.13
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 138 - "Template"
Cohesion: 0.21
Nodes (4): Branch, Step, Template, Twist

### Community 140 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 141 - ".strings"
Cohesion: 0.25
Nodes (3): Band, Mate, SquadPlan

### Community 142 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 146 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 150 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 151 - "Tier"
Cohesion: 0.20
Nodes (7): Tier, A, B, C, D, E, S

### Community 153 - "shade"
Cohesion: 0.25
Nodes (7): 4. Block catalogue, Interior fittings, Totals, Vanilla mappings, tatami(), tatami_top(), shade()

### Community 154 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), merchant_camp_talk(), S, twist()

### Community 155 - "Tier"
Cohesion: 0.25
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 157 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 158 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 159 - "15. Furniture"
Cohesion: 0.40
Nodes (5): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now)

### Community 161 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 163 - "5. Process"
Cohesion: 0.50
Nodes (4): 5. Process, Order of work, The pieces, What needs you at your PC

### Community 169 - "Custom blocks"
Cohesion: 0.13
Nodes (14): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+6 more)

## Knowledge Gaps
- **327 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+322 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1425 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **42 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `Home`, `.roll`, `VillageSim.java`, `FirstFifteenHours.java`, `Playthrough.java`, `Run`, `.talk`, `Stage`, `map`, `Question`, `Squad`, `VillageScaleTest`, `Bond`, `.of`, `Levels`, `Deed`, `News`, `BondEvent`, `CourtshipTest`, `.tier`, `VisitsTest`, `Person`, `list`, `.romance`, `org.junit.jupiter.api.Test`, `.person`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _327 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Home` be split into smaller, more focused modules?**
  _Cohesion score 0.07199032062915911 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `fabric`, `kit_senju.py`, `kit_kurama.py`, `kit_hagane.py`, `kit_yuhi.py`, `Custom blocks`, `kit_household.py`, `paint.py`, `paint.py`, `stamp`, `kit_rugged.py`, `kit_tsuchigumo.py`, `strip_fabric`, `wide_sleeves`, `kit_field.py`, `solid`, `kit_kunoichi.py`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.03209876543209877 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `fabric`, `kit_senju.py`, `kit_kurama.py`, `Custom blocks`, `kit_yuhi.py`, `kit_household.py`, `paint.py`, `paint.py`, `stamp`, `kit_rugged.py`, `kit_tsuchigumo.py`, `strip_fabric`, `Box`, `wide_sleeves`, `kit_field.py`, `k`, `kit_kunoichi.py`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._