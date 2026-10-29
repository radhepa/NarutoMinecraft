# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 256 files · ~334,700 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 30 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 4352 nodes · 10306 edges · 187 communities (140 shown, 47 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1218 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `07d71540`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Activity
- VillageScaleTest
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- kit_kurama.py
- creator.py
- kit_uchiha.py
- kit_kunoichi.py
- .roll
- items.py
- .obj
- 7. Systems in the beta
- paint.py
- Economy
- AnswerTag
- kit_rugged.py
- blocks.py
- Home
- mkit.py
- sprites.py
- Catalogue
- Template
- .shelf
- k
- kit_kinoshita.py
- Json
- 5. Data formats built for the whole story
- k
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- .classic
- 4. Technical architecture
- 6. The map
- Shops
- 8. The beta, chapter by chapter
- kit_akimichi.py
- Prices
- Roster
- kit_hagane.py
- Run
- .daily
- Item catalogue
- utility_pole
- fabric
- Value
- .play
- kit_inuzuka.py
- Meters
- Grades
- Act
- Stage
- BondWorld
- Category
- .person
- map
- Life together
- kit_suzuran.py
- Personality
- ClanProfile
- mockups.py
- kit_haruno.py
- Bond
- .of
- Person
- .answer
- Def
- Levels
- Deed
- .xpAt
- RuleOfThumbTest
- Tier
- Squad
- org.junit.jupiter.api.Test
- Playthrough.java
- Mood
- VarietyGuard
- 4.3 The noble clans
- .tier
- Plan
- Desk
- Niche
- Missions
- konoha/preview.py
- Meter
- Flat
- .name
- Result
- .of
- Side quests
- 4.4 The minor clans
- CreatorRules
- 2. Quest framework
- Recipes
- kit_household.py
- Home
- kit_tsuchigumo.py
- Tex
- FirstFifteenHours.java
- FirstFifteenHours.java
- 8. Beta catalogue
- Plant
- .choices
- argparse
- Restyle
- Label
- roster.py
- Custom blocks
- .num
- Character creation
- Tier
- missions.py
- .open
- Village
- Kind
- 7. Inter-clan politics as quests
- VisitsTest
- SocialTie
- 4. Clan quest lines
- Ranks
- creator/preview.py
- .receive
- Keepsake
- Player
- Json
- Rng
- pathlib
- Every building
- Kind
- ClanPower
- .strings
- CourtshipTest
- AgeStage
- Kind
- Stretch
- NamesTest
- Rng
- catalogue.py
- .look
- Pantry
- .run
- Json
- Rng
- Garment
- Tier
- Look
- ClanRelations
- Title
- Memory
- S
- Wallet
- build
- .everyKeyTheEngineEmitsIsListed
- Bonds
- Mission catalogue
- paper_lantern
- Rng
- The village
- mission
- senbon
- kunai
- Tier
- Naruto Minecraft
- Data
- 9. Delivery plan
- .tidiness
- Side quest secrets
- street.py

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 202 edges
3. `solid()` - 151 edges
4. `Act` - 131 edges
5. `fabric()` - 109 edges
6. `Bond` - 67 edges
7. `Home` - 66 edges
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
- `9. Pacing with time together` --references--> `TimeAndPacingTest`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java

## Import Cycles
- None detected.

## Communities (187 total, 47 thin omitted)

### Community 0 - "Activity"
Cohesion: 0.08
Nodes (15): 18. The engine, Activity, BondEvent, Conversation, Reply, Topic, Answer, Highlight (+7 more)

### Community 1 - "VillageScaleTest"
Cohesion: 0.14
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 2 - "Clans"
Cohesion: 0.15
Nodes (12): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+4 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (19): new_canvas(), backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font() (+11 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.02
Nodes (55): deep_hood(), high_collar(), hood_down(), lenses(), drawstrings(), forearm_wraps(), holster(), hood_down() (+47 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "creator.py"
Cohesion: 0.08
Nodes (19): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), roll_look() (+11 more)

### Community 10 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - ".roll"
Cohesion: 0.21
Nodes (3): Rng, Streams, StreamsTest

### Community 13 - "items.py"
Cohesion: 0.17
Nodes (20): art_class(), catalogue_md(), check_all(), check_loot(), compile_all(), recipe_entry(), dumps(), err() (+12 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - "paint.py"
Cohesion: 0.04
Nodes (31): cel_face(), ring_shell(), crown(), kasuri(), clipped(), combed_back(), nape_hem(), pulled_back() (+23 more)

### Community 17 - "Economy"
Cohesion: 0.08
Nodes (16): Band, Economy, End, ABANDONED, DONE, FAILED, PARTIAL, GradeRow (+8 more)

### Community 18 - "AnswerTag"
Cohesion: 0.09
Nodes (20): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+12 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "blocks.py"
Cohesion: 0.13
Nodes (18): Facades and shop fronts, Roofs, auto_uv(), awning(), block(), Block, box(), check() (+10 more)

### Community 22 - "mkit.py"
Cohesion: 0.16
Nodes (31): 4.1 The format, Code by mod, The quest format, anchor(), buy(), choose(), chose(), collect() (+23 more)

### Community 23 - "sprites.py"
Cohesion: 0.13
Nodes (21): 16. Keepsakes, build(), Canvas, charm(), flak_vest(), forehead_protector(), framed_ladle(), headband() (+13 more)

### Community 24 - "Catalogue"
Cohesion: 0.16
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 25 - "Template"
Cohesion: 0.09
Nodes (9): Catalogue, Branch, Step, Template, Twist, DeskDays, Profile, Run (+1 more)

### Community 26 - ".shelf"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 27 - "k"
Cohesion: 0.03
Nodes (43): sword_strap(), wrap_front(), bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta() (+35 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "k"
Cohesion: 0.06
Nodes (24): Shared helpers, braid(), arm_bone(), arm_x(), belt(), body(), collar(), flaps() (+16 more)

### Community 32 - "outputs"
Cohesion: 0.11
Nodes (25): catalog(), compatible(), general_pool(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans() (+17 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - ".classic"
Cohesion: 0.22
Nodes (3): 13. Data formats, BondDialogue, BondDialogueTest

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "Shops"
Cohesion: 0.08
Nodes (25): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), gift, Hagane Metalworks (`hagane_metalworks`) (+17 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode()

### Community 41 - "Prices"
Cohesion: 0.15
Nodes (3): Pawn, Prices, PricesTest

### Community 42 - "Roster"
Cohesion: 0.06
Nodes (9): 8. Growing up together, Hooks for the other mods, Pulling their weight, The 60 hours, simulated, The model, Contribution, Day, GrowthEvent (+1 more)

### Community 43 - "kit_hagane.py"
Cohesion: 0.06
Nodes (20): gear, smithy, weapon, Weapon Shop (`weapon_shop`), arm_guards(), hip_katana(), katana(), bracers() (+12 more)

### Community 44 - "Run"
Cohesion: 0.05
Nodes (18): 15. Pacing, Standing, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER (+10 more)

### Community 45 - ".daily"
Cohesion: 0.14
Nodes (4): Friends, Day, Visit, Visits

### Community 46 - "Item catalogue"
Cohesion: 0.13
Nodes (15): collectible, consumable, container, curio, currency, Item catalogue, keepsake, key (+7 more)

### Community 47 - "utility_pole"
Cohesion: 0.12
Nodes (18): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 5. Process, 6. Prototypes, 7. Effort estimate, 8. Registration notes for Phase 0, By building type, Calibration (+10 more)

### Community 48 - "fabric"
Cohesion: 0.02
Nodes (64): How the pieces work, back_fan(), bangs(), cel_box(), curtain(), lock(), sidelocks(), spike() (+56 more)

### Community 49 - "Value"
Cohesion: 0.12
Nodes (12): Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY, KINDNESS (+4 more)

### Community 50 - ".play"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 51 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 54 - "Act"
Cohesion: 0.02
Nodes (79): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+71 more)

### Community 55 - "Stage"
Cohesion: 0.15
Nodes (9): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+1 more)

### Community 57 - "Category"
Cohesion: 0.06
Nodes (28): Catalog, FurnitureSet, Category, BATH, BED, DECOR, DISPLAY, FIXTURE (+20 more)

### Community 61 - "Life together"
Cohesion: 0.22
Nodes (9): 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Questions and choices, 8. Data and quest hooks, 9. Pacing with time together (+1 more)

### Community 62 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 63 - "Personality"
Cohesion: 0.08
Nodes (15): 5. Personality, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS (+7 more)

### Community 65 - "ClanProfile"
Cohesion: 0.22
Nodes (3): 18. Village scale, ClanProfile, House

### Community 66 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 67 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (4): Bond, LifeEvents, News, FollowUp

### Community 69 - ".of"
Cohesion: 0.09
Nodes (4): 8. The village talks, ConflictTest, GossipTest, MemoryTest

### Community 70 - "Person"
Cohesion: 0.05
Nodes (6): 20. What the roadmap asks of bonds, Conflict, Household, Person, Recruitment, VillageTest

### Community 71 - ".answer"
Cohesion: 0.17
Nodes (4): Answered, Outcome, Questions, QuestionsTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 74 - "Deed"
Cohesion: 0.10
Nodes (8): Deed, Know, Gossip, Source, HEARD, SEEN, SELF, TOLD

### Community 75 - ".xpAt"
Cohesion: 0.09
Nodes (8): Day, BondInput, Peer, Grower, Technique, CurveAndTierTest, RosterTest, TechniqueTest

### Community 77 - "Tier"
Cohesion: 0.22
Nodes (7): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON

### Community 78 - "Squad"
Cohesion: 0.07
Nodes (6): 14. Save format and versioning, BondEffects, SaveFormat, Departure, Squad, SaveFormatTest

### Community 79 - "org.junit.jupiter.api.Test"
Cohesion: 0.05
Nodes (10): SquadTest, CatalogueTest, JsonTest, RyoTest, LivingTest, MoveTest, CatalogueTest, SeedsTest (+2 more)

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "VarietyGuard"
Cohesion: 0.10
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 85 - ".tier"
Cohesion: 0.05
Nodes (21): 11. Kindling Bond, 12. The bond book, BondBook, Fact, MemoryLine, Page, BondConditions, BondWeb (+13 more)

### Community 86 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 87 - "Desk"
Cohesion: 0.13
Nodes (8): Desk, Offer, Rank, A, B, C, D, S

### Community 88 - "Niche"
Cohesion: 0.12
Nodes (11): Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING, SUPPORT (+3 more)

### Community 89 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 90 - "konoha/preview.py"
Cohesion: 0.16
Nodes (14): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+6 more)

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Flat"
Cohesion: 0.11
Nodes (12): 17. What the map needs, 2. The flat, The Classic flat: `flat.leaf_block.3a`, Varied candidates, Flat, Room, Tier, ACADEMY_FLAT (+4 more)

### Community 93 - ".name"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 95 - ".of"
Cohesion: 0.08
Nodes (8): Score, Practice, Session, Rest, Rested, CatalogTest, ComfortTest, RestTest

### Community 96 - "Side quests"
Cohesion: 0.22
Nodes (9): 1. Scope and budget, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents, In the beta, Later (foundation), Later one-offs (foundation) (+1 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "CreatorRules"
Cohesion: 0.20
Nodes (5): 13. Code, and what waits for Phase 0, Choices, CreatorRules, Outfit, Roots

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Recipes"
Cohesion: 0.14
Nodes (17): apothecary, cooking.oven, cooking.pot, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient (+9 more)

### Community 101 - "kit_household.py"
Cohesion: 0.03
Nodes (46): leg_cloth(), waist(), blouse(), cargo(), collar(), gloves(), half_sleeves(), holster() (+38 more)

### Community 102 - "Home"
Cohesion: 0.11
Nodes (19): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 1. Design rules, 20. By beta slice, 21. Open questions (+11 more)

### Community 103 - "kit_tsuchigumo.py"
Cohesion: 0.15
Nodes (7): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 105 - "FirstFifteenHours.java"
Cohesion: 0.15
Nodes (5): Stage, ADULT, CHILD, TEEN, Leaf

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 109 - "Plant"
Cohesion: 0.11
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 112 - "argparse"
Cohesion: 0.19
Nodes (7): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 113 - "Restyle"
Cohesion: 0.15
Nodes (9): 7. Locked and changeable, Restyle, Result, Venue, BARBER, HOME, LOCKED, SETTINGS (+1 more)

### Community 114 - "Label"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 115 - "roster.py"
Cohesion: 0.17
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 116 - "Custom blocks"
Cohesion: 0.11
Nodes (17): 4. Block catalogue, Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival (+9 more)

### Community 118 - "Character creation"
Cohesion: 0.10
Nodes (20): 10. How residents address you, 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 119 - "Tier"
Cohesion: 0.22
Nodes (6): Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY

### Community 120 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 123 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 124 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 125 - "VisitsTest"
Cohesion: 0.19
Nodes (3): Cast, Setup, VisitsTest

### Community 127 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 128 - "Ranks"
Cohesion: 0.13
Nodes (14): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+6 more)

### Community 129 - "creator/preview.py"
Cohesion: 0.15
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 130 - ".receive"
Cohesion: 0.27
Nodes (5): 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest

### Community 131 - "Keepsake"
Cohesion: 0.12
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 135 - "pathlib"
Cohesion: 0.12
Nodes (3): build(), build(), build()

### Community 136 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 137 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 138 - "ClanPower"
Cohesion: 0.12
Nodes (7): Ryo, ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 139 - ".strings"
Cohesion: 0.21
Nodes (6): Mode, CLASSIC, VARIED, Band, Mate, SquadPlan

### Community 141 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 142 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 143 - "Stretch"
Cohesion: 0.13
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 147 - "NamesTest"
Cohesion: 0.25
Nodes (4): 1 Name, Names, PlayerName, NamesTest

### Community 149 - "catalogue.py"
Cohesion: 0.21
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 150 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 151 - "Pantry"
Cohesion: 0.19
Nodes (8): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now), Food, Meal, Pantry

### Community 152 - ".run"
Cohesion: 0.20
Nodes (6): 19. Pacing, FirstFifteenHours, Result, Slice, Snapshot, FirstFifteenHoursTest

### Community 155 - "Garment"
Cohesion: 0.18
Nodes (5): Garment, key_rgba(), Piece, piece_corners(), world_bounds()

### Community 156 - "Tier"
Cohesion: 0.20
Nodes (7): Tier, A, B, C, D, E, S

### Community 159 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 161 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), go(), S, twist()

### Community 162 - "Wallet"
Cohesion: 0.05
Nodes (32): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+24 more)

### Community 163 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 165 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.33
Nodes (3): DialogueKeys, DialogueKeysTest, 10. Content plan

### Community 166 - "Bonds"
Cohesion: 0.11
Nodes (15): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 6. Shared experiences and moments (+7 more)

### Community 167 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 168 - "paper_lantern"
Cohesion: 0.20
Nodes (11): furniture, Furniture Shop (`furniture_shop`), workbench, Interior fittings, Lanterns, noren(), paper_lantern(), stone_lantern() (+3 more)

### Community 170 - "The village"
Cohesion: 0.29
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 172 - "mission"
Cohesion: 0.40
Nodes (3): _key(), mission(), outcome()

### Community 173 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 174 - "kunai"
Cohesion: 0.20
Nodes (10): Exam-Week Stalls (`exam_stalls`), Ninja Tool Shop (`tool_shop`), Pawn Shop (`pawn_shop`), tool, along(), f(), kunai(), blade() (+2 more)

### Community 175 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 176 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 183 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 184 - ".tidiness"
Cohesion: 0.40
Nodes (4): Tidiness, LIVED_IN, MESSY, TIDY

### Community 185 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

## Knowledge Gaps
- **332 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+327 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1520 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **47 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_senju.py`, `solid`, `kit_kurama.py`, `kit_uchiha.py`, `kit_kunoichi.py`, `paint.py`, `kit_rugged.py`, `kit_kinoshita.py`, `k`, `Shops`, `kit_akimichi.py`, `kit_hagane.py`, `senbon`, `fabric`, `kit_inuzuka.py`, `kit_suzuran.py`, `kit_haruno.py`, `kit_household.py`, `kit_tsuchigumo.py`, `Custom blocks`?**
  _High betweenness centrality (0.107) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _332 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Activity` be split into smaller, more focused modules?**
  _Cohesion score 0.07688828584350972 - nodes in this community are weakly interconnected._
- **Why does `11. Kindling Bond` connect `.tier` to `Bonds`, `kit_tsuchigumo.py`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **Should `VillageScaleTest` be split into smaller, more focused modules?**
  _Cohesion score 0.13846153846153847 - nodes in this community are weakly interconnected._
- **Why does `web()` connect `kit_tsuchigumo.py` to `.tier`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12477718360071301 - nodes in this community are weakly interconnected._