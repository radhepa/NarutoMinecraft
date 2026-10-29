# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 277 files · ~659,596 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 4671 nodes · 11123 edges · 197 communities (155 shown, 42 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1306 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a011e0c4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- set
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- kit_kurama.py
- creator.py
- k
- kit_kunoichi.py
- Wallet
- Economy
- kit_suzuran.py
- 7. Systems in the beta
- .person
- Shops
- .answer
- kit_rugged.py
- dialogue.py
- mkit.py
- Category
- Template
- .daily
- Desk
- fabric
- kit_market.py
- kit_kinoshita.py
- Fixture
- 5. Data formats built for the whole story
- strip_fabric
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- 4. Technical architecture
- 6. The map
- wide_sleeves
- 8. The beta, chapter by chapter
- 9. Delivery plan
- sprites.py
- kit_akimichi.py
- kit_hagane.py
- Playthrough
- BondInput
- Playthrough.java
- .of
- VarietyGuard
- Box
- mockups.py
- .xpAt
- Home
- Home
- Act
- Stage
- BondWorld
- VarietyGuard
- Plan
- Look
- map
- org.junit.jupiter.api.Test
- Kind
- Meters
- list
- .obj
- .romance
- VillageScaleTest
- Bond
- FirstFifteenHours.java
- Bonds
- blocks.py
- Def
- Levels
- Deed
- Person
- .romance
- set
- .person
- paint.py
- CreatorRules
- Mood
- items.py
- 4.3 The noble clans
- kit_haruno.py
- konoha/preview.py
- Personality
- ClanRelations
- .obj
- konoha/preview.py
- .classic
- Meter
- Missions
- Fixture
- 18. Village scale
- ROADMAP.md
- Side quests
- 4.4 The minor clans
- .shelf
- 2. Quest framework
- Missions
- .classic
- Label
- Context
- leaf_block.py
- Catalogue
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- Heard
- .person
- Catalogue
- 4. Clan quest lines
- Character creation
- ClanPower
- Prices
- BondEvent
- Plant
- The village
- BetaTalk
- VillageSim.java
- missions.py
- .name
- Side quest secrets
- .talk
- Tex
- Bank
- tatami
- Naruto Minecraft
- render_kit.py
- VisitsTest
- .num
- Dialogue
- Names
- utility_pole
- Tier
- pathlib
- stamp
- Every building
- .open
- creator/preview.py
- Json
- AnswerTag
- .receive
- Recipes
- AnswerTag
- Keepsake
- Json
- Rng
- Question
- BetaTalk
- Json
- Kind
- AgeStage
- Item catalogue
- Grades
- .choices
- NamesTest
- Rng
- .chains
- catalogue.py
- kit_tsuchigumo.py
- .look
- Restyle
- Pantry
- .run
- Rng
- math
- Kind
- TimeAndPacingTest
- RuleOfThumbTest
- Score
- Mission catalogue
- S
- Writing dialogue for the Leaf
- leaf_block.py
- MoveTest
- Outcome
- Result
- .tidiness
- mission
- shade
- Kind
- economy/build.gradle
- home/build.gradle
- missions/build.gradle
- Writing dialogue for the Leaf
- Naruto Minecraft

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
10. `Person` - 50 edges

## Surprising Connections (you probably didn't know these)
- `1.7 Gift tags` --references--> `Personality`  [INFERRED]
  ITEMS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Personality.java
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java
- `2.4 Reporting back` --references--> `report()`  [INFERRED]
  MISSIONS.md → tools/dialogue/dialogue.py
- `6. Coordination` --references--> `tatami()`  [INFERRED]
  ITEMS.md → tools/konoha/blocks.py

## Import Cycles
- None detected.

## Communities (197 total, 42 thin omitted)

### Community 0 - "set"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

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
Cohesion: 0.18
Nodes (7): arm_bone(), arm_x(), armband(), roll(), seal_script(), seal_tags(), wide_sleeves()

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (18): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Kindling Bond, Recurring characters, Reveal pacing, Spoilers behind the roadmap's neutral wording (+10 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "creator.py"
Cohesion: 0.23
Nodes (4): Mode, CLASSIC, VARIED, Unlocks

### Community 10 - "k"
Cohesion: 0.04
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - "Wallet"
Cohesion: 0.16
Nodes (32): 4.1 The format, Code by mod, The quest format, anchor(), buy(), choose(), chose(), collect() (+24 more)

### Community 13 - "Economy"
Cohesion: 0.15
Nodes (8): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - ".person"
Cohesion: 0.10
Nodes (8): Activity, Answer, FollowUp, Invitation, Plan, Together, TogetherTest, 3. Hangouts

### Community 17 - "Shops"
Cohesion: 0.14
Nodes (7): compose(), flush_kernel(), flush_template(), fail(), main(), build(), build()

### Community 18 - ".answer"
Cohesion: 0.08
Nodes (16): Band, Economy, End, ABANDONED, DONE, FAILED, PARTIAL, GradeRow (+8 more)

### Community 20 - "dialogue.py"
Cohesion: 0.06
Nodes (21): 11. Kindling Bond, 12. The bond book, BondBook, Fact, MemoryLine, Page, Household, Bonfire (+13 more)

### Community 21 - "mkit.py"
Cohesion: 0.03
Nodes (42): deep_hood(), high_collar(), hood_down(), lenses(), sword_strap(), blossom(), geta(), tabi() (+34 more)

### Community 22 - "Category"
Cohesion: 0.07
Nodes (10): strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece, piece_corners() (+2 more)

### Community 23 - "Template"
Cohesion: 0.10
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 24 - ".daily"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 25 - "Desk"
Cohesion: 0.08
Nodes (26): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), gift, Hagane Metalworks (`hagane_metalworks`) (+18 more)

### Community 26 - "fabric"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 27 - "kit_market.py"
Cohesion: 0.10
Nodes (21): build(), Canvas, charm(), flak_vest(), forehead_protector(), framed_ladle(), headband(), hexrgb() (+13 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.03
Nodes (44): How the pieces work, back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash() (+36 more)

### Community 29 - "Fixture"
Cohesion: 0.09
Nodes (9): Catalogue, Branch, Step, Template, Twist, DeskDays, Profile, Run (+1 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.13
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Principles, Ranks and milestones, Rotating story roles (+5 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.09
Nodes (31): paste(), scene(), build(), build_all(), catalog(), hex_rgb(), json_text(), load_all_groups() (+23 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.22
Nodes (9): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap, Still open (+1 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "wide_sleeves"
Cohesion: 0.18
Nodes (3): 13. Code, and what waits for Phase 0, CreatorRules, Roots

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 40 - "9. Delivery plan"
Cohesion: 0.14
Nodes (16): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now), furniture, Furniture Shop (`furniture_shop`), workbench (+8 more)

### Community 41 - "sprites.py"
Cohesion: 0.14
Nodes (17): Roofs, auto_uv(), awning(), block(), Block, box(), check(), compile_all() (+9 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 43 - "kit_hagane.py"
Cohesion: 0.09
Nodes (4): Contribution, GrowthEvent, Grower, Roster

### Community 44 - "Playthrough"
Cohesion: 0.07
Nodes (15): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+7 more)

### Community 45 - "BondInput"
Cohesion: 0.12
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 46 - "Playthrough.java"
Cohesion: 0.16
Nodes (4): 13. Data formats, BondDialogue, BondEvent, BondDialogueTest

### Community 47 - ".of"
Cohesion: 0.12
Nodes (14): 6. Conversations, Conversation, Reply, Topic, DialogueKeys, 10. Content plan, 11. Open questions, 1. What makes a relationship feel real (+6 more)

### Community 48 - "VarietyGuard"
Cohesion: 0.11
Nodes (4): 7. Locked and changeable, Look, Result, RestyleAndGrowUpTest

### Community 49 - "Box"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 50 - "mockups.py"
Cohesion: 0.17
Nodes (15): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), item_id() (+7 more)

### Community 51 - ".xpAt"
Cohesion: 0.06
Nodes (20): gear, smithy, weapon, Weapon Shop (`weapon_shop`), arm_guards(), hip_katana(), katana(), bracers() (+12 more)

### Community 52 - "Home"
Cohesion: 0.03
Nodes (58): back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock(), ring_shell() (+50 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (78): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+70 more)

### Community 57 - "VarietyGuard"
Cohesion: 0.11
Nodes (15): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+7 more)

### Community 58 - "Plan"
Cohesion: 0.10
Nodes (20): 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 1 Name, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 60 - "map"
Cohesion: 0.18
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Meters"
Cohesion: 0.05
Nodes (28): sprigs(), burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face() (+20 more)

### Community 64 - "list"
Cohesion: 0.14
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 65 - ".obj"
Cohesion: 0.14
Nodes (17): apothecary, cooking.oven, cooking.pot, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient (+9 more)

### Community 66 - ".romance"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.08
Nodes (23): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+15 more)

### Community 68 - "Bond"
Cohesion: 0.04
Nodes (6): Bond, BondConditions, BondWeb, News, Highlight, Outcome

### Community 69 - "FirstFifteenHours.java"
Cohesion: 0.07
Nodes (10): 8. The village talks, State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, ConflictTest (+2 more)

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 71 - "blocks.py"
Cohesion: 0.23
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 72 - "Def"
Cohesion: 0.08
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 74 - "Deed"
Cohesion: 0.13
Nodes (3): Deed, Know, Gossip

### Community 75 - "Person"
Cohesion: 0.07
Nodes (6): 14. Save format and versioning, BondEffects, SaveFormat, Departure, Squad, SaveFormatTest

### Community 77 - "set"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 80 - "CreatorRules"
Cohesion: 0.09
Nodes (10): blouse(), cargo(), collar(), gloves(), holster(), knee_guards(), pocket(), strap() (+2 more)

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

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
Cohesion: 0.10
Nodes (5): 20. What the roadmap asks of bonds, 5. Personality, Personality, Reaction, ReactionTest

### Community 87 - "ClanRelations"
Cohesion: 0.11
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+1 more)

### Community 89 - "konoha/preview.py"
Cohesion: 0.06
Nodes (28): Catalog, FurnitureSet, Category, BATH, BED, DECOR, DISPLAY, FIXTURE (+20 more)

### Community 92 - "Missions"
Cohesion: 0.16
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Fixture"
Cohesion: 0.15
Nodes (7): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 94 - "18. Village scale"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 95 - "ROADMAP.md"
Cohesion: 0.12
Nodes (5): Rest, Rested, CatalogTest, ComfortTest, RestTest

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents, In the beta (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - ".shelf"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Missions"
Cohesion: 0.13
Nodes (15): collectible, consumable, container, curio, currency, Item catalogue, keepsake, key (+7 more)

### Community 101 - ".classic"
Cohesion: 0.13
Nodes (35): assign_ids(), build(), check_condition(), check_text(), compiled(), compiled_question(), content_key(), coverage() (+27 more)

### Community 102 - "Label"
Cohesion: 0.11
Nodes (4): Friends, Day, Visit, Visits

### Community 103 - "Context"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 105 - "Catalogue"
Cohesion: 0.21
Nodes (4): 10. How residents address you, Names, PlayerName, NamesTest

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.12
Nodes (5): Day, Technique, CurveAndTierTest, RosterTest, TechniqueTest

### Community 108 - "Heard"
Cohesion: 0.33
Nodes (6): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT

### Community 109 - ".person"
Cohesion: 0.03
Nodes (56): Shared helpers, leg_cloth(), shirt(), waist(), belt(), body(), collar(), half_sleeves() (+48 more)

### Community 110 - "Catalogue"
Cohesion: 0.35
Nodes (3): Band, Mate, SquadPlan

### Community 112 - "4. Clan quest lines"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 113 - "Character creation"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 114 - "ClanPower"
Cohesion: 0.07
Nodes (25): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 17. What the map needs, 1. Design rules (+17 more)

### Community 115 - "Prices"
Cohesion: 0.12
Nodes (18): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 5. Process, 6. Prototypes, 7. Effort estimate, 8. Registration notes for Phase 0, By building type, Calibration (+10 more)

### Community 116 - "BondEvent"
Cohesion: 0.11
Nodes (17): 4. Block catalogue, Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival (+9 more)

### Community 117 - "Plant"
Cohesion: 0.11
Nodes (13): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+5 more)

### Community 118 - "The village"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 119 - "BetaTalk"
Cohesion: 0.14
Nodes (15): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+7 more)

### Community 120 - "VillageSim.java"
Cohesion: 0.18
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 121 - "missions.py"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 122 - ".name"
Cohesion: 0.31
Nodes (3): Score, Practice, Session

### Community 123 - "Side quest secrets"
Cohesion: 0.12
Nodes (17): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+9 more)

### Community 126 - "Bank"
Cohesion: 0.11
Nodes (18): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+10 more)

### Community 127 - "tatami"
Cohesion: 0.11
Nodes (7): Memory, Meters, Source, HEARD, SEEN, SELF, TOLD

### Community 129 - "render_kit.py"
Cohesion: 0.11
Nodes (9): Desk, Offer, Player, Rank, A, B, C, D (+1 more)

### Community 130 - "VisitsTest"
Cohesion: 0.50
Nodes (4): Kind, CYCLE, LINE, REPEAT

### Community 131 - ".num"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 133 - "Names"
Cohesion: 0.11
Nodes (12): Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY, Tier, ACADEMY_FLAT (+4 more)

### Community 134 - "utility_pole"
Cohesion: 0.16
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 135 - "Tier"
Cohesion: 0.14
Nodes (9): Line, Turn, Overheard, Said, Talk, Why, BUDGET, EXHAUSTED (+1 more)

### Community 136 - "pathlib"
Cohesion: 0.18
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 137 - "stamp"
Cohesion: 0.06
Nodes (10): 19. Pacing, SquadTest, CatalogueTest, JsonTest, RyoTest, LivingTest, FirstFifteenHoursTest, CatalogueTest (+2 more)

### Community 138 - "Every building"
Cohesion: 0.25
Nodes (4): 6. Squad missions, travel(), S, twist()

### Community 139 - ".open"
Cohesion: 0.15
Nodes (3): Fixture, QuestionsAndLedgerTest, TalkTest

### Community 140 - "creator/preview.py"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 142 - "AnswerTag"
Cohesion: 0.16
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 143 - ".receive"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 146 - "Recipes"
Cohesion: 0.15
Nodes (3): Pawn, Prices, PricesTest

### Community 150 - "Keepsake"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 151 - "Json"
Cohesion: 0.08
Nodes (5): 18. The engine, Conflict, Person, Recruitment, 2. Schedules

### Community 152 - "Rng"
Cohesion: 0.05
Nodes (33): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+25 more)

### Community 153 - "Question"
Cohesion: 0.16
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 154 - "BetaTalk"
Cohesion: 0.14
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 157 - "AgeStage"
Cohesion: 0.21
Nodes (3): Rng, Streams, StreamsTest

### Community 158 - "Item catalogue"
Cohesion: 0.27
Nodes (3): 15. Pacing, TimeAndPacingTest, 9. Pacing with time together

### Community 160 - ".choices"
Cohesion: 0.07
Nodes (14): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+6 more)

### Community 161 - "NamesTest"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 162 - "Rng"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 163 - ".chains"
Cohesion: 0.15
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 164 - "catalogue.py"
Cohesion: 0.23
Nodes (3): Cast, Setup, VisitsTest

### Community 165 - "kit_tsuchigumo.py"
Cohesion: 0.08
Nodes (3): Schedule, Leaf, SampleQuestions

### Community 166 - ".look"
Cohesion: 0.40
Nodes (4): Tidiness, LIVED_IN, MESSY, TIDY

### Community 170 - ".run"
Cohesion: 0.12
Nodes (3): 4. Storage, Heard, Speaker

### Community 172 - "Rng"
Cohesion: 0.23
Nodes (9): Exam-Week Stalls (`exam_stalls`), Ninja Tool Shop (`tool_shop`), tool, along(), f(), kunai(), blade(), shuriken() (+1 more)

### Community 174 - "Kind"
Cohesion: 0.26
Nodes (5): 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest

### Community 176 - "TimeAndPacingTest"
Cohesion: 0.40
Nodes (3): _key(), mission(), outcome()

### Community 178 - "Score"
Cohesion: 0.15
Nodes (5): Bank, Facet, Pacing, Rules, Tier

### Community 179 - "Mission catalogue"
Cohesion: 0.20
Nodes (3): 9. Data, code and Phase 0, BondInput, Day

### Community 182 - "leaf_block.py"
Cohesion: 0.25
Nodes (4): BetaTalk, Person, Player, World

### Community 183 - "MoveTest"
Cohesion: 0.11
Nodes (7): Answer, Question, Answered, Outcome, Questions, QuestionsCompiledTest, QuestionsTest

### Community 184 - "Outcome"
Cohesion: 0.25
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 185 - "Result"
Cohesion: 0.12
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 186 - ".tidiness"
Cohesion: 0.29
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 189 - "shade"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 190 - "Kind"
Cohesion: 0.18
Nodes (5): Answer, Question, Need, Tags, Answered

### Community 192 - "economy/build.gradle"
Cohesion: 0.25
Nodes (3): Choices, Outfit, CreatorRulesTest

### Community 193 - "home/build.gradle"
Cohesion: 0.11
Nodes (16): 10. Pool sizing, 11. Simulation, 12. Story-gated pools, 13. What waits, 14. Decisions and open questions, 1. Freshness: never repeat, 2. Talk budgets, 3. Beyond the budget (+8 more)

### Community 194 - "missions/build.gradle"
Cohesion: 0.11
Nodes (3): Names, Names, Tokens

### Community 202 - "Writing dialogue for the Leaf"
Cohesion: 0.25
Nodes (8): Context tags, Functions, Questions, Rules the compiler enforces, Style, The format, Voices, Writing dialogue for the Leaf

### Community 211 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

## Knowledge Gaps
- **342 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+337 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1596 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **42 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `Dialogue`, `stamp`, `.person`, `dialogue.py`, `Json`, `.chains`, `catalogue.py`, `kit_tsuchigumo.py`, `Pantry`, `Playthrough`, `Playthrough.java`, `Kind`, `.of`, `MoveTest`, `map`, `Bond`, `FirstFifteenHours.java`, `Bonds`, `Levels`, `Deed`, `Person`, `.romance`, `Meter`, `Missions`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _342 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `set` be split into smaller, more focused modules?**
  _Cohesion score 0.07058001397624039 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `mkit.py` to `kit_uchiha.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `k`, `kit_kunoichi.py`, `kit_suzuran.py`, `Desk`, `kit_kinoshita.py`, `8. The beta, chapter by chapter`, `kit_akimichi.py`, `.xpAt`, `Home`, `Meters`, `CreatorRules`, `kit_haruno.py`, `ClanRelations`, `Fixture`, `.person`, `BondEvent`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `kit_kinoshita.py` to `kit_uchiha.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `k`, `kit_kunoichi.py`, `kit_suzuran.py`, `mkit.py`, `Category`, `Desk`, `8. The beta, chapter by chapter`, `kit_akimichi.py`, `.xpAt`, `Home`, `Meters`, `CreatorRules`, `kit_haruno.py`, `ClanRelations`, `Fixture`, `.person`, `BondEvent`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.10526315789473684 - nodes in this community are weakly interconnected._