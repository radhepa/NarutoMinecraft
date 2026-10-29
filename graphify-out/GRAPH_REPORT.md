# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 255 files · ~334,081 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 30 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 4343 nodes · 10277 edges · 190 communities (140 shown, 50 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1215 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c0e9115b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- creator.py
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_kinoshita.py
- Story bible
- rnd
- Player
- kit_akimichi.py
- kit_kunoichi.py
- mkit.py
- render_kit.py
- kit_suzuran.py
- 7. Systems in the beta
- .person
- pathlib
- Economy
- list
- .classic
- k
- Box
- VarietyGuard
- Plan
- Shops
- Missions
- sprites.py
- solid
- Catalogue
- 5. Data formats built for the whole story
- .num
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- fabric
- 4. Technical architecture
- 6. The map
- CreatorRules
- 8. The beta, chapter by chapter
- 9. Delivery plan
- blocks.py
- kit_rugged.py
- Roster
- Run
- Plant
- .talk
- SquadTest
- .choices
- Restyle
- missions.py
- kit_hagane.py
- cel_box
- .get
- Act
- Stage
- BondWorld
- paper_lantern
- Character creation
- 18. The engine
- map
- .play
- Kind
- Question
- Tex
- Village
- Kind
- Person
- Bond
- GossipTest
- Conflict
- catalogue.py
- Def
- Levels
- Deed
- Squad
- Rng
- AnswerTag
- Home
- Face
- Mood
- items.py
- 4.3 The noble clans
- kit_haruno.py
- Json
- Personality
- Tier
- Rng
- Category
- .obj
- arraylist
- Title
- .name
- .shelf
- .of
- Side quests
- 4.4 The minor clans
- AgeStage
- 2. Quest framework
- Item catalogue
- Label
- .daily
- mockups.py
- Kind
- NamesTest
- 7. Inter-clan politics as quests
- RosterTest
- Bonds
- kit_household.py
- .strings
- .look
- Tier
- Home
- Konoha: the build plan
- Custom blocks
- Niche
- Meter
- konoha/preview.py
- roster.py
- Pantry
- Recipes
- Ranks
- Json
- FirstFifteenHours.java
- Every building
- Meters
- Rng
- Desk
- .add
- .run
- Tier
- Catalogue
- Look
- org.junit.jupiter.api.Test
- S
- 8. Beta catalogue
- mission
- creator/preview.py
- 4. Clan quest lines
- Prices
- Data
- ClanRelations
- creator.py
- Items, shops and crafting
- ClanPower
- Stretch
- Rng
- SocialTie
- Streams
- TimeAndPacingTest
- Json
- Tier
- News
- .cap
- VillageSim
- Playthrough.java
- 6. Filler arcs
- Grades
- .person
- 4. The ryo economy
- ROADMAP.md
- math
- Garment
- Ryo
- FirstFifteenHours.java
- load_clans
- Wallet
- BondInput
- RuleOfThumbTest
- rot_matrix
- 1. The registry
- build
- Mission catalogue
- 3. Crafting
- The village
- Result
- Side quest secrets

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 201 edges
3. `solid()` - 151 edges
4. `Act` - 128 edges
5. `fabric()` - 109 edges
6. `Bond` - 67 edges
7. `Home` - 67 edges
8. `Village` - 63 edges
9. `strip_fabric()` - 59 edges
10. `Person` - 55 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `1.7 Gift tags` --references--> `Personality`  [INFERRED]
  ITEMS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Personality.java
- `7. Questions and choices` --references--> `Question`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Question.java
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `11. What waits for Phase 0` --references--> `Player`  [INFERRED]
  MISSIONS.md → progression/missions/src/main/java/dev/shinobi/progression/mission/Player.java

## Import Cycles
- None detected.

## Communities (190 total, 50 thin omitted)

### Community 0 - "creator.py"
Cohesion: 0.12
Nodes (6): check(), load_rules(), story_reserved_family_names(), validate_roots(), World, colors()

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
Cohesion: 0.12
Nodes (19): new_canvas(), backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font() (+11 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "rnd"
Cohesion: 0.04
Nodes (32): sprigs(), fur_edge(), back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds() (+24 more)

### Community 10 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+1 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - "mkit.py"
Cohesion: 0.16
Nodes (31): 4.1 The format, Code by mod, The quest format, anchor(), buy(), choose(), chose(), collect() (+23 more)

### Community 13 - "render_kit.py"
Cohesion: 0.19
Nodes (7): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - ".person"
Cohesion: 0.06
Nodes (25): 18. The engine, Activity, BondEvent, Conversation, Reply, Topic, Schedule, Answer (+17 more)

### Community 17 - "pathlib"
Cohesion: 0.12
Nodes (3): build(), build(), build()

### Community 18 - "Economy"
Cohesion: 0.08
Nodes (16): Band, Economy, End, ABANDONED, DONE, FAILED, PARTIAL, GradeRow (+8 more)

### Community 20 - ".classic"
Cohesion: 0.08
Nodes (17): 11. Kindling Bond, BondBook, Fact, MemoryLine, Page, Bonfire, Flame, Kindling (+9 more)

### Community 21 - "k"
Cohesion: 0.02
Nodes (57): deep_hood(), high_collar(), hood_down(), lenses(), arm_bone(), arm_x(), belt(), collar() (+49 more)

### Community 22 - "Box"
Cohesion: 0.12
Nodes (3): strip_line(), Box, Layer

### Community 23 - "VarietyGuard"
Cohesion: 0.10
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 24 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 25 - "Shops"
Cohesion: 0.08
Nodes (26): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), gift, Hagane Metalworks (`hagane_metalworks`) (+18 more)

### Community 26 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 27 - "sprites.py"
Cohesion: 0.10
Nodes (21): build(), Canvas, charm(), flak_vest(), forehead_protector(), framed_ladle(), headband(), hexrgb() (+13 more)

### Community 28 - "solid"
Cohesion: 0.02
Nodes (50): drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps(), shirt() (+42 more)

### Community 29 - "Catalogue"
Cohesion: 0.09
Nodes (9): Catalogue, Branch, Step, Template, Twist, DeskDays, Profile, Run (+1 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.18
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+8 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "fabric"
Cohesion: 0.03
Nodes (43): How the pieces work, stamp(), back_crest(), crescent(), decal(), shoulder_decal(), slanted_protector(), crest() (+35 more)

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
Cohesion: 0.14
Nodes (17): Roofs, auto_uv(), awning(), block(), Block, box(), check(), compile_all() (+9 more)

### Community 42 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 43 - "Roster"
Cohesion: 0.09
Nodes (5): Hooks for the other mods, Contribution, GrowthEvent, Grower, Roster

### Community 44 - "Run"
Cohesion: 0.07
Nodes (15): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+7 more)

### Community 45 - "Plant"
Cohesion: 0.13
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 46 - ".talk"
Cohesion: 0.17
Nodes (5): 13. Data formats, BondDialogue, DialogueKeys, BondDialogueTest, 10. Content plan

### Community 49 - "Restyle"
Cohesion: 0.15
Nodes (9): 7. Locked and changeable, Restyle, Result, Venue, BARBER, HOME, LOCKED, SETTINGS (+1 more)

### Community 50 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 51 - "kit_hagane.py"
Cohesion: 0.06
Nodes (20): gear, smithy, weapon, Weapon Shop (`weapon_shop`), arm_guards(), hip_katana(), katana(), bracers() (+12 more)

### Community 52 - "cel_box"
Cohesion: 0.04
Nodes (44): Shared helpers, back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock() (+36 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (78): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+70 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 57 - "paper_lantern"
Cohesion: 0.12
Nodes (20): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now), furniture, Furniture Shop (`furniture_shop`), workbench (+12 more)

### Community 58 - "Character creation"
Cohesion: 0.10
Nodes (20): 10. How residents address you, 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 59 - "18. The engine"
Cohesion: 0.18
Nodes (4): 2. The flat, The Classic flat: `flat.leaf_block.3a`, Varied candidates, CatalogTest

### Community 61 - ".play"
Cohesion: 0.11
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Question"
Cohesion: 0.11
Nodes (7): Answer, Question, Answered, Outcome, Questions, QuestionsCompiledTest, QuestionsTest

### Community 66 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 67 - "Person"
Cohesion: 0.07
Nodes (6): 20. What the roadmap asks of bonds, BondWeb, Person, ConditionsAndEffectsTest, VillageScaleTest, VillageTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (3): Bond, BondConditions, BondEffects

### Community 71 - "catalogue.py"
Cohesion: 0.21
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 75 - "Squad"
Cohesion: 0.08
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 77 - "AnswerTag"
Cohesion: 0.11
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 78 - "Home"
Cohesion: 0.04
Nodes (17): 17. What the map needs, Flat, Room, Home, Tidiness, LIVED_IN, MESSY, TIDY (+9 more)

### Community 79 - "Face"
Cohesion: 0.06
Nodes (19): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), button() (+11 more)

### Community 81 - "Mood"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - "items.py"
Cohesion: 0.17
Nodes (20): art_class(), catalogue_md(), check_all(), check_loot(), compile_all(), recipe_entry(), dumps(), err() (+12 more)

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 86 - "Personality"
Cohesion: 0.05
Nodes (27): 5. Personality, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS (+19 more)

### Community 87 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 89 - "Category"
Cohesion: 0.06
Nodes (28): Catalog, FurnitureSet, Category, BATH, BED, DECOR, DISPLAY, FIXTURE (+20 more)

### Community 92 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 94 - ".shelf"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 95 - ".of"
Cohesion: 0.09
Nodes (13): Score, Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY, Practice (+5 more)

### Community 96 - "Side quests"
Cohesion: 0.25
Nodes (8): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 9. Open questions, Contents, Side quests

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Item catalogue"
Cohesion: 0.13
Nodes (15): collectible, consumable, container, curio, currency, Item catalogue, keepsake, key (+7 more)

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - ".daily"
Cohesion: 0.10
Nodes (7): Friends, Day, Visit, Visits, Cast, Setup, VisitsTest

### Community 103 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 104 - "Kind"
Cohesion: 0.17
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 105 - "NamesTest"
Cohesion: 0.25
Nodes (4): 1 Name, Names, PlayerName, NamesTest

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 108 - "Bonds"
Cohesion: 0.09
Nodes (15): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+7 more)

### Community 109 - "kit_household.py"
Cohesion: 0.03
Nodes (46): leg_cloth(), waist(), body(), blouse(), cargo(), collar(), gloves(), half_sleeves() (+38 more)

### Community 110 - ".strings"
Cohesion: 0.21
Nodes (6): Mode, CLASSIC, VARIED, Band, Mate, SquadPlan

### Community 112 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 113 - "Tier"
Cohesion: 0.20
Nodes (7): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON

### Community 114 - "Home"
Cohesion: 0.11
Nodes (19): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 1. Design rules, 20. By beta slice (+11 more)

### Community 115 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 5. Process, 6. Prototypes, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 116 - "Custom blocks"
Cohesion: 0.11
Nodes (17): 4. Block catalogue, Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival (+9 more)

### Community 117 - "Niche"
Cohesion: 0.12
Nodes (13): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+5 more)

### Community 118 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 119 - "konoha/preview.py"
Cohesion: 0.16
Nodes (14): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+6 more)

### Community 120 - "roster.py"
Cohesion: 0.17
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 121 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 122 - "Recipes"
Cohesion: 0.14
Nodes (17): apothecary, cooking.oven, cooking.pot, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient (+9 more)

### Community 123 - "Ranks"
Cohesion: 0.12
Nodes (16): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+8 more)

### Community 126 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 127 - "Meters"
Cohesion: 0.12
Nodes (7): Memory, Meters, Source, HEARD, SEEN, SELF, TOLD

### Community 129 - "Desk"
Cohesion: 0.13
Nodes (8): Desk, Offer, Rank, A, B, C, D, S

### Community 131 - ".run"
Cohesion: 0.20
Nodes (6): 19. Pacing, FirstFifteenHours, Result, Slice, Snapshot, FirstFifteenHoursTest

### Community 133 - "Tier"
Cohesion: 0.25
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 134 - "Catalogue"
Cohesion: 0.16
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 137 - "org.junit.jupiter.api.Test"
Cohesion: 0.05
Nodes (11): ConflictTest, CatalogueTest, JsonTest, RyoTest, LivingTest, MoveTest, CurveAndTierTest, CatalogueTest (+3 more)

### Community 138 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), go(), S, twist()

### Community 140 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 141 - "mission"
Cohesion: 0.40
Nodes (3): _key(), mission(), outcome()

### Community 142 - "creator/preview.py"
Cohesion: 0.15
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 143 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 146 - "Prices"
Cohesion: 0.15
Nodes (3): Pawn, Prices, PricesTest

### Community 151 - "creator.py"
Cohesion: 0.18
Nodes (13): _hash(), hash64(), main(), _mix(), outputs(), roll_look(), roll_origin(), roll_roots() (+5 more)

### Community 152 - "Items, shops and crafting"
Cohesion: 0.15
Nodes (11): 2.1 How buying works, 2.2 The shops, 2.3 Part-time jobs, 2.4 Interiors (blocks asked of the Konoha session), 2. Shops, 5. Item art, 6. Coordination, 7. What waits for Phase 0 (+3 more)

### Community 153 - "ClanPower"
Cohesion: 0.17
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 154 - "Stretch"
Cohesion: 0.13
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 157 - "Streams"
Cohesion: 0.21
Nodes (3): Rng, Streams, StreamsTest

### Community 158 - "TimeAndPacingTest"
Cohesion: 0.27
Nodes (3): 15. Pacing, TimeAndPacingTest, 9. Pacing with time together

### Community 160 - "Tier"
Cohesion: 0.20
Nodes (7): Tier, A, B, C, D, E, S

### Community 162 - ".cap"
Cohesion: 0.19
Nodes (3): 3. Levels and story gates, LevelsTest, MemoryTest

### Community 166 - "6. Filler arcs"
Cohesion: 0.50
Nodes (4): 6. Filler arcs, In the beta, Later (foundation), Later one-offs (foundation)

### Community 169 - ".person"
Cohesion: 0.12
Nodes (7): 12. The bond book, 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest, BondFriends

### Community 170 - "4. The ryo economy"
Cohesion: 0.50
Nodes (4): 4.1 A closed loop, 4.2 Sinks and inflation guards, 4.3 The simulation, 4. The ryo economy

### Community 171 - "ROADMAP.md"
Cohesion: 0.32
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 172 - "math"
Cohesion: 0.23
Nodes (9): Exam-Week Stalls (`exam_stalls`), Ninja Tool Shop (`tool_shop`), tool, along(), f(), kunai(), blade(), shuriken() (+1 more)

### Community 173 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 176 - "FirstFifteenHours.java"
Cohesion: 0.15
Nodes (5): Stage, ADULT, CHILD, TEEN, Leaf

### Community 177 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 179 - "BondInput"
Cohesion: 0.22
Nodes (3): 9. Data, code and Phase 0, BondInput, Day

### Community 181 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 182 - "1. The registry"
Cohesion: 0.22
Nodes (9): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+1 more)

### Community 183 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 184 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 185 - "3. Crafting"
Cohesion: 0.29
Nodes (7): 3.1 Stations, 3.2 Recipes, 3.3 Unlocks, 3.4 Quality grades, 3.5 Repair and upgrade, 3.6 Where materials come from, 3. Crafting

### Community 186 - "The village"
Cohesion: 0.29
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 189 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

## Knowledge Gaps
- **331 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+326 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1514 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **50 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_uchiha.py`, `fabric`, `kit_senju.py`, `kit_kinoshita.py`, `rnd`, `kit_akimichi.py`, `kit_kunoichi.py`, `kit_rugged.py`, `kit_household.py`, `kit_suzuran.py`, `Face`, `kit_hagane.py`, `cel_box`, `kit_haruno.py`, `Custom blocks`, `Shops`, `solid`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _331 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `creator.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._
- **Why does `BondWorld` connect `BondWorld` to `.romance`, `org.junit.jupiter.api.Test`, `.person`, `.classic`, `News`, `VillageSim`, `Playthrough.java`, `.person`, `Run`, `.talk`, `SquadTest`, `FirstFifteenHours.java`, `Stage`, `Question`, `Village`, `Person`, `Bond`, `GossipTest`, `Conflict`, `Deed`, `Squad`, `arraylist`, `.daily`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `.cap`, `Person`, `Conflict`, `.person`, `Deed`, `ROADMAP.md`, `Squad`, `.talk`, `.person`, `.classic`, `Personality`, `Stage`, `ClanRelations`, `SocialTie`, `TimeAndPacingTest`, `Meters`?**
  _High betweenness centrality (0.054) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._