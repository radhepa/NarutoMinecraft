# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 278 files · ~654,629 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 4661 nodes · 11094 edges · 201 communities (152 shown, 49 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1300 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c0e9115b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- fabric
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- kit_kurama.py
- creator.py
- math
- kit_kunoichi.py
- Wallet
- org.junit.jupiter.api.Test
- kit_suzuran.py
- 7. Systems in the beta
- .person
- Economy
- Home
- kit_rugged.py
- mkit.py
- Template
- Roster
- kit_hagane.py
- Desk
- .play
- Category
- kit_market.py
- kit_kinoshita.py
- k
- 5. Data formats built for the whole story
- strip_fabric
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- sprites.py
- 4. Technical architecture
- 6. The map
- .daily
- 8. The beta, chapter by chapter
- 9. Delivery plan
- mockups.py
- kit_akimichi.py
- Flat
- Playthrough
- dialogue.py
- blocks.py
- Niche
- VarietyGuard
- Box
- Plan
- .xpAt
- Look
- Personality
- Act
- Stage
- BondWorld
- CreatorRules
- .tier
- items.py
- .greeting
- Kind
- Meters
- list
- .obj
- Village
- .classic
- Bond
- State
- Bonds
- .read
- Def
- Levels
- Deed
- Context
- .romance
- Playthrough.java
- .person
- paint.py
- Value
- Mood
- paper_lantern
- 4.3 The noble clans
- kit_haruno.py
- konoha/preview.py
- Peeve
- ClanRelations
- cel_box
- .shelf
- Heard
- Meter
- Missions
- Fixture
- 18. Village scale
- Side quests
- 4.4 The minor clans
- GossipTest
- 2. Quest framework
- json
- Label
- compose.py
- VillageSim.java
- Question
- Catalogue
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- .score
- Run
- Character creation
- 4. Clan quest lines
- Prices
- VisitsTest
- render_kit.py
- .name
- FirstFifteenHours.java
- The village
- BetaTalk
- Seeds
- Plant
- Context
- Side quest secrets
- Tier
- Bank
- Dialogue
- Person
- Json
- Conflict
- missions.py
- .num
- Writing dialogue for the Leaf
- .answer
- Home
- Tex
- .open
- creator/preview.py
- .receive
- Recipes
- Ranks
- AnswerTag
- Streams
- Json
- Names
- Rng
- Outcome
- pathlib
- ClanPower
- Kind
- Every building
- Json
- Naruto Minecraft
- Keepsake
- Kind
- AgeStage
- Item catalogue
- Konoha: the build plan
- Grades
- catalogue.py
- .choices
- NamesTest
- Stretch
- Rng
- .chains
- Shops
- .look
- Restyle
- Custom blocks
- Pantry
- .run
- Json
- Rng
- QuestionsAndLedgerTest
- Kind
- .set
- SquadPlan
- TimeAndPacingTest
- BondInput
- RuleOfThumbTest
- S
- VillageSim
- Mission catalogue
- SquadTest
- Score
- MoveTest
- .classmate
- AgeStageTest
- Result
- mission
- SeedsTest.java
- Data

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 201 edges
3. `solid()` - 151 edges
4. `Act` - 130 edges
5. `fabric()` - 109 edges
6. `Bond` - 67 edges
7. `Home` - 66 edges
8. `Village` - 63 edges
9. `strip_fabric()` - 59 edges
10. `Person` - 50 edges

## Surprising Connections (you probably didn't know these)
- `1.7 Gift tags` --references--> `Personality`  [INFERRED]
  ITEMS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Personality.java
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java
- `6. Coordination` --references--> `tatami()`  [INFERRED]
  ITEMS.md → tools/konoha/blocks.py
- `Leaf Festival Stalls (`festival_stalls`)` --references--> `paper_lantern()`  [INFERRED]
  docs/items/CATALOGUE.md → tools/konoha/blocks.py

## Import Cycles
- None detected.

## Communities (201 total, 49 thin omitted)

### Community 0 - "fabric"
Cohesion: 0.03
Nodes (42): How the pieces work, stamp(), back_crest(), crescent(), decal(), shoulder_decal(), slanted_protector(), crest() (+34 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.11
Nodes (16): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+8 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.14
Nodes (17): new_canvas(), backdrop(), Canvas, Character, clan_renders(), cube_quads(), font(), general_renders() (+9 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.03
Nodes (48): drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps(), shirt() (+40 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (18): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Kindling Bond, Recurring characters, Reveal pacing, Spoilers behind the roadmap's neutral wording (+10 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "creator.py"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

### Community 10 - "math"
Cohesion: 0.23
Nodes (9): Exam-Week Stalls (`exam_stalls`), Ninja Tool Shop (`tool_shop`), tool, along(), f(), kunai(), blade(), shuriken() (+1 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - "Wallet"
Cohesion: 0.05
Nodes (33): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+25 more)

### Community 13 - "org.junit.jupiter.api.Test"
Cohesion: 0.07
Nodes (9): 19. Pacing, CatalogueTest, JsonTest, RyoTest, LivingTest, FirstFifteenHoursTest, CurveAndTierTest, CatalogueTest (+1 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - ".person"
Cohesion: 0.06
Nodes (24): 6. Conversations, Activity, BondEvent, Conversation, Reply, Topic, Answer, FollowUp (+16 more)

### Community 17 - "Economy"
Cohesion: 0.08
Nodes (16): Band, Economy, End, ABANDONED, DONE, FAILED, PARTIAL, GradeRow (+8 more)

### Community 18 - "Home"
Cohesion: 0.08
Nodes (6): Home, Tidiness, LIVED_IN, MESSY, TIDY, Photo

### Community 19 - "kit_rugged.py"
Cohesion: 0.04
Nodes (33): sprigs(), fur_edge(), baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps() (+25 more)

### Community 20 - "mkit.py"
Cohesion: 0.16
Nodes (31): 4.1 The format, Code by mod, The quest format, anchor(), buy(), choose(), chose(), collect() (+23 more)

### Community 21 - "Template"
Cohesion: 0.09
Nodes (9): Catalogue, Branch, Step, Template, Twist, DeskDays, Profile, Run (+1 more)

### Community 22 - "Roster"
Cohesion: 0.09
Nodes (4): Contribution, GrowthEvent, Grower, Roster

### Community 23 - "kit_hagane.py"
Cohesion: 0.08
Nodes (17): gear, smithy, weapon, Weapon Shop (`weapon_shop`), arm_guards(), hip_katana(), katana(), bracers() (+9 more)

### Community 24 - "Desk"
Cohesion: 0.11
Nodes (9): Desk, Offer, Player, Rank, A, B, C, D (+1 more)

### Community 25 - ".play"
Cohesion: 0.10
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 26 - "Category"
Cohesion: 0.07
Nodes (27): Catalog, Category, BATH, BED, DECOR, DISPLAY, FIXTURE, FLOOR (+19 more)

### Community 27 - "kit_market.py"
Cohesion: 0.04
Nodes (24): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+16 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "k"
Cohesion: 0.03
Nodes (40): deep_hood(), high_collar(), hood_down(), lenses(), arm_bone(), arm_x(), belt(), body() (+32 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.13
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Principles, Ranks and milestones, Rotating story roles (+5 more)

### Community 31 - "strip_fabric"
Cohesion: 0.03
Nodes (46): leg_cloth(), waist(), blouse(), cargo(), collar(), gloves(), half_sleeves(), holster() (+38 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.09
Nodes (29): build(), build_all(), catalog(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans() (+21 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.22
Nodes (9): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap, Still open (+1 more)

### Community 35 - "sprites.py"
Cohesion: 0.10
Nodes (21): build(), Canvas, charm(), flak_vest(), forehead_protector(), framed_ladle(), headband(), hexrgb() (+13 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - ".daily"
Cohesion: 0.13
Nodes (4): Friends, Day, Visit, Visits

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode()

### Community 43 - "Flat"
Cohesion: 0.07
Nodes (18): 17. What the map needs, 2. The flat, The Classic flat: `flat.leaf_block.3a`, Varied candidates, Tier, BARE, BELOVED, COMFORTABLE (+10 more)

### Community 44 - "Playthrough"
Cohesion: 0.06
Nodes (22): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME (+14 more)

### Community 45 - "dialogue.py"
Cohesion: 0.13
Nodes (34): assign_ids(), build(), check_condition(), check_text(), compiled(), compiled_question(), content_key(), coverage() (+26 more)

### Community 46 - "blocks.py"
Cohesion: 0.13
Nodes (20): 6. Prototypes, Facades and shop fronts, Roofs, Streets, auto_uv(), awning(), block(), Block (+12 more)

### Community 47 - "Niche"
Cohesion: 0.09
Nodes (14): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+6 more)

### Community 48 - "VarietyGuard"
Cohesion: 0.10
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 49 - "Box"
Cohesion: 0.07
Nodes (10): strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece, piece_corners() (+2 more)

### Community 50 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 51 - ".xpAt"
Cohesion: 0.17
Nodes (3): Day, RosterTest, TechniqueTest

### Community 52 - "Look"
Cohesion: 0.11
Nodes (4): 7. Locked and changeable, Look, Result, RestyleAndGrowUpTest

### Community 53 - "Personality"
Cohesion: 0.12
Nodes (3): Personality, Reaction, ReactionTest

### Community 54 - "Act"
Cohesion: 0.03
Nodes (78): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+70 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "BondWorld"
Cohesion: 0.07
Nodes (3): BondEffects, BondWorld, LifeEvents

### Community 57 - "CreatorRules"
Cohesion: 0.18
Nodes (3): 13. Code, and what waits for Phase 0, CreatorRules, Roots

### Community 58 - ".tier"
Cohesion: 0.07
Nodes (18): 11. Kindling Bond, BondBook, Fact, MemoryLine, Page, Household, Bonfire, Flame (+10 more)

### Community 59 - "items.py"
Cohesion: 0.17
Nodes (20): art_class(), catalogue_md(), check_all(), check_loot(), compile_all(), recipe_entry(), dumps(), err() (+12 more)

### Community 61 - ".greeting"
Cohesion: 0.24
Nodes (3): 13. Data formats, BondDialogue, BondDialogueTest

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 67 - ".classic"
Cohesion: 0.09
Nodes (4): 20. What the roadmap asks of bonds, ConditionsAndEffectsTest, VillageScaleTest, VillageTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (3): Bond, BondConditions, News

### Community 69 - "State"
Cohesion: 0.14
Nodes (7): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, ConflictTest

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (14): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 5. Personality (+6 more)

### Community 71 - ".read"
Cohesion: 0.17
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.18
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.10
Nodes (8): Deed, Know, Gossip, Source, HEARD, SEEN, SELF, TOLD

### Community 75 - "Context"
Cohesion: 0.15
Nodes (8): Line, Overheard, Said, Talk, Why, BUDGET, EXHAUSTED, NONE

### Community 78 - ".person"
Cohesion: 0.17
Nodes (3): 12. The bond book, BondWeb, BondFriends

### Community 79 - "paint.py"
Cohesion: 0.06
Nodes (23): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+15 more)

### Community 80 - "Value"
Cohesion: 0.14
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "paper_lantern"
Cohesion: 0.12
Nodes (20): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now), furniture, Furniture Shop (`furniture_shop`), workbench (+12 more)

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - "konoha/preview.py"
Cohesion: 0.14
Nodes (15): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+7 more)

### Community 86 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 88 - "cel_box"
Cohesion: 0.04
Nodes (43): Shared helpers, back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock() (+35 more)

### Community 89 - ".shelf"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 91 - "Meter"
Cohesion: 0.09
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents, In the beta (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "json"
Cohesion: 0.14
Nodes (15): paste(), scene(), bucket(), check(), check_name(), counts(), first_level(), group_of() (+7 more)

### Community 101 - "Label"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "compose.py"
Cohesion: 0.48
Nodes (5): compose(), flush_kernel(), flush_template(), fail(), main()

### Community 104 - "Question"
Cohesion: 0.16
Nodes (6): Turn, Answer, Question, Need, Tags, Answered

### Community 105 - "Catalogue"
Cohesion: 0.16
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - ".score"
Cohesion: 0.18
Nodes (4): Rest, Rested, ComfortTest, RestTest

### Community 109 - "Run"
Cohesion: 0.07
Nodes (3): Departure, Squad, Run

### Community 110 - "Character creation"
Cohesion: 0.10
Nodes (20): 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 1 Name, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Prices"
Cohesion: 0.15
Nodes (3): Pawn, Prices, PricesTest

### Community 114 - "VisitsTest"
Cohesion: 0.20
Nodes (3): Cast, Setup, VisitsTest

### Community 115 - "render_kit.py"
Cohesion: 0.15
Nodes (8): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 116 - ".name"
Cohesion: 0.07
Nodes (14): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+6 more)

### Community 117 - "FirstFifteenHours.java"
Cohesion: 0.14
Nodes (5): Stage, ADULT, CHILD, TEEN, Comfort

### Community 118 - "The village"
Cohesion: 0.29
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 119 - "BetaTalk"
Cohesion: 0.29
Nodes (4): BetaTalk, Person, Player, World

### Community 121 - "Plant"
Cohesion: 0.13
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 123 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 124 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 125 - "Bank"
Cohesion: 0.16
Nodes (5): Bank, Facet, Pacing, Rules, Tier

### Community 126 - "Dialogue"
Cohesion: 0.12
Nodes (14): 10. Pool sizing, 11. Simulation, 12. Story-gated pools, 13. What waits, 14. Open questions, 1. Freshness: never repeat, 2. Talk budgets, 3. Beyond the budget (+6 more)

### Community 128 - "Person"
Cohesion: 0.09
Nodes (4): 18. The engine, Person, Schedule, HomeHangout

### Community 131 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 133 - "Writing dialogue for the Leaf"
Cohesion: 0.25
Nodes (8): Context tags, Functions, Questions, Rules the compiler enforces, Style, The format, Voices, Writing dialogue for the Leaf

### Community 134 - ".answer"
Cohesion: 0.10
Nodes (11): 9. Mass production, The bank today, DialogueKeys, Answer, Question, Answered, Outcome, Questions (+3 more)

### Community 135 - "Home"
Cohesion: 0.11
Nodes (19): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 1. Design rules, 20. By beta slice (+11 more)

### Community 138 - "creator/preview.py"
Cohesion: 0.16
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 139 - ".receive"
Cohesion: 0.26
Nodes (5): 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest

### Community 140 - "Recipes"
Cohesion: 0.14
Nodes (17): apothecary, cooking.oven, cooking.pot, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient (+9 more)

### Community 141 - "Ranks"
Cohesion: 0.12
Nodes (17): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+9 more)

### Community 142 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 143 - "Streams"
Cohesion: 0.21
Nodes (3): Rng, Streams, StreamsTest

### Community 147 - "Names"
Cohesion: 0.11
Nodes (3): Names, Names, Tokens

### Community 149 - "Outcome"
Cohesion: 0.33
Nodes (6): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT

### Community 150 - "pathlib"
Cohesion: 0.12
Nodes (3): build(), build(), build()

### Community 151 - "ClanPower"
Cohesion: 0.16
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 152 - "Kind"
Cohesion: 0.50
Nodes (4): Kind, CYCLE, LINE, REPEAT

### Community 153 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 155 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 156 - "Keepsake"
Cohesion: 0.13
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 157 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 158 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 159 - "Item catalogue"
Cohesion: 0.13
Nodes (15): collectible, consumable, container, curio, currency, Item catalogue, keepsake, key (+7 more)

### Community 160 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 162 - "catalogue.py"
Cohesion: 0.22
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 163 - ".choices"
Cohesion: 0.25
Nodes (3): Choices, Outfit, CreatorRulesTest

### Community 164 - "NamesTest"
Cohesion: 0.21
Nodes (4): 10. How residents address you, Names, PlayerName, NamesTest

### Community 165 - "Stretch"
Cohesion: 0.14
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 167 - ".chains"
Cohesion: 0.23
Nodes (4): Mode, CLASSIC, VARIED, Unlocks

### Community 168 - "Shops"
Cohesion: 0.08
Nodes (26): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), gift, Hagane Metalworks (`hagane_metalworks`) (+18 more)

### Community 169 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 170 - "Restyle"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 171 - "Custom blocks"
Cohesion: 0.15
Nodes (13): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+5 more)

### Community 172 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 173 - ".run"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 177 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 179 - "SquadPlan"
Cohesion: 0.35
Nodes (3): Band, Mate, SquadPlan

### Community 180 - "TimeAndPacingTest"
Cohesion: 0.27
Nodes (3): 15. Pacing, TimeAndPacingTest, 9. Pacing with time together

### Community 182 - "BondInput"
Cohesion: 0.22
Nodes (3): 9. Data, code and Phase 0, BondInput, Day

### Community 184 - "S"
Cohesion: 0.20
Nodes (6): 6. Squad missions, report(), travel(), go(), S, twist()

### Community 186 - "Mission catalogue"
Cohesion: 0.25
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 188 - "Score"
Cohesion: 0.32
Nodes (3): Score, Practice, Session

### Community 193 - "mission"
Cohesion: 0.40
Nodes (3): _key(), mission(), outcome()

## Knowledge Gaps
- **342 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+337 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1594 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **49 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `fabric`, `kit_uchiha.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `Shops`, `kit_akimichi.py`, `kit_kunoichi.py`, `kit_suzuran.py`, `paint.py`, `kit_rugged.py`, `kit_haruno.py`, `kit_hagane.py`, `cel_box`, `kit_market.py`, `kit_kinoshita.py`, `strip_fabric`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _342 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.03449048152295633 - nodes in this community are weakly interconnected._
- **Why does `BondWorld` connect `BondWorld` to `Person`, `Conflict`, `.answer`, `.receive`, `.person`, `Playthrough`, `Stage`, `VillageSim`, `.tier`, `SquadTest`, `map`, `.greeting`, `list`, `Village`, `.classic`, `Bond`, `State`, `.read`, `Deed`, `Playthrough.java`, `.person`, `VillageSim.java`, `Run`, `VisitsTest`, `FirstFifteenHours.java`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `fabric`, `kit_uchiha.py`, `kit_senju.py`, `kit_kurama.py`, `Shops`, `kit_akimichi.py`, `kit_kunoichi.py`, `kit_suzuran.py`, `paint.py`, `Box`, `kit_rugged.py`, `kit_haruno.py`, `kit_hagane.py`, `cel_box`, `kit_market.py`, `kit_kinoshita.py`, `k`, `strip_fabric`?**
  _High betweenness centrality (0.054) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.10526315789473684 - nodes in this community are weakly interconnected._