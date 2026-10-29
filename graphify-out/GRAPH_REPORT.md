# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 277 files · ~658,360 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 4670 nodes · 11119 edges · 191 communities (149 shown, 42 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1305 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `66f5ddad`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- creator.py
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- rnd
- Story bible
- kit_kurama.py
- Player
- kit_market.py
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
- kit_morino.py
- 4. Technical architecture
- 6. The map
- CreatorRules
- kit_kinoshita.py
- tatami
- blocks.py
- kit_rugged.py
- Roster
- Run
- Plant
- .greeting
- Squad
- Look
- Restyle
- missions.py
- kit_hagane.py
- cel_box
- .get
- Act
- ClanRelations
- BondWorld
- Bonds
- Character creation
- .romance
- FirstFifteenHours.java
- .play
- Kind
- paint.py
- Tex
- Recipes
- Kind
- Peeve
- Bond
- .of
- Stage
- catalogue.py
- Def
- Levels
- Deed
- Squad
- ClanProfile
- AnswerTag
- Home
- shade
- Mood
- items.py
- 4.3 The noble clans
- kit_haruno.py
- Json
- Personality
- senbon
- Rng
- Category
- .obj
- .effectiveLevel
- .name
- .shelf
- .of
- Side quests
- 4.4 The minor clans
- AgeStage
- 2. Quest framework
- Item catalogue
- dialogue.py
- .daily
- mockups.py
- leaf_block.py
- NamesTest
- 7. Inter-clan politics as quests
- RosterTest
- Outcome
- fabric
- .strings
- .look
- shuriken
- Home
- Konoha: the build plan
- Custom blocks
- Niche
- Meter
- konoha/preview.py
- roster.py
- Pantry
- street.py
- Ranks
- Json
- FirstFifteenHours.java
- Every building
- Meters
- Rng
- Desk
- Kind
- .run
- VillageSim.java
- Tier
- Catalogue
- Talk
- Village
- org.junit.jupiter.api.Test
- Fixture
- 8. Beta catalogue
- creator/preview.py
- 4. Clan quest lines
- Prices
- Data
- Label
- Person
- Wallet
- ClanPower
- Stretch
- Rng
- Streams
- TimeAndPacingTest
- Json
- Tier
- Memory
- VillageScaleTest
- VisitsTest
- Playthrough.java
- 6. Filler arcs
- Grades
- .person
- Heard
- kunai
- Context
- .receive
- Bank
- BondInput
- RuleOfThumbTest
- Json
- BetaTalk
- .answer
- Mission catalogue
- Keepsake
- The village
- Result
- Side quest secrets
- Question
- .choices
- Dialogue
- Names
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
- `6. Coordination` --references--> `tatami()`  [INFERRED]
  ITEMS.md → tools/konoha/blocks.py
- `Leaf Festival Stalls (`festival_stalls`)` --references--> `paper_lantern()`  [INFERRED]
  docs/items/CATALOGUE.md → tools/konoha/blocks.py

## Import Cycles
- None detected.

## Communities (191 total, 42 thin omitted)

### Community 0 - "creator.py"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.12
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

### Community 6 - "rnd"
Cohesion: 0.03
Nodes (33): quilt(), sprigs(), burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge() (+25 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (18): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Kindling Bond, Recurring characters, Reveal pacing, Spoilers behind the roadmap's neutral wording (+10 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "Player"
Cohesion: 0.23
Nodes (4): Mode, CLASSIC, VARIED, Unlocks

### Community 10 - "kit_market.py"
Cohesion: 0.05
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+14 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - "mkit.py"
Cohesion: 0.13
Nodes (36): 4.1 The format, Code by mod, The quest format, anchor(), buy(), choose(), chose(), collect() (+28 more)

### Community 13 - "render_kit.py"
Cohesion: 0.15
Nodes (8): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - ".person"
Cohesion: 0.09
Nodes (11): 18. The engine, Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan (+3 more)

### Community 17 - "pathlib"
Cohesion: 0.14
Nodes (7): compose(), flush_kernel(), flush_template(), fail(), main(), build(), build()

### Community 18 - "Economy"
Cohesion: 0.08
Nodes (16): Band, Economy, End, ABANDONED, DONE, FAILED, PARTIAL, GradeRow (+8 more)

### Community 20 - ".classic"
Cohesion: 0.06
Nodes (26): 11. Kindling Bond, BondBook, Fact, MemoryLine, Page, Bonfire, Flame, Kindling (+18 more)

### Community 21 - "k"
Cohesion: 0.04
Nodes (36): deep_hood(), high_collar(), hood_down(), lenses(), arm_bone(), arm_x(), belt(), collar() (+28 more)

### Community 22 - "Box"
Cohesion: 0.07
Nodes (10): strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece, piece_corners() (+2 more)

### Community 23 - "VarietyGuard"
Cohesion: 0.10
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 24 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 25 - "Shops"
Cohesion: 0.08
Nodes (25): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), gift, Hagane Metalworks (`hagane_metalworks`) (+17 more)

### Community 26 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 27 - "sprites.py"
Cohesion: 0.14
Nodes (21): build(), Canvas, charm(), flak_vest(), forehead_protector(), framed_ladle(), headband(), hexrgb() (+13 more)

### Community 28 - "solid"
Cohesion: 0.03
Nodes (46): How the pieces work, back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash() (+38 more)

### Community 29 - "Catalogue"
Cohesion: 0.09
Nodes (9): Catalogue, Branch, Step, Template, Twist, DeskDays, Profile, Run (+1 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.13
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Principles, Ranks and milestones, Rotating story roles (+5 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.09
Nodes (29): build(), build_all(), catalog(), general_pool(), hex_rgb(), json_text(), load_all_groups(), load_characters() (+21 more)

### Community 33 - "11. Later systems"
Cohesion: 0.11
Nodes (15): 6. Squad missions, 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans (+7 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.09
Nodes (23): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, 8. The beta, chapter by chapter, 9. Delivery plan, Beta 1: the opening and the Academy (~4 h), Beta 1: the opening and the Academy (~4 h main path) (+15 more)

### Community 35 - "kit_morino.py"
Cohesion: 0.14
Nodes (6): back_crest(), clipped(), coat_skirts(), head_cloth(), nape_hem(), forehead_protector()

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "CreatorRules"
Cohesion: 0.18
Nodes (3): 13. Code, and what waits for Phase 0, CreatorRules, Roots

### Community 39 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 40 - "tatami"
Cohesion: 0.14
Nodes (16): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now), furniture, Furniture Shop (`furniture_shop`), workbench (+8 more)

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
Nodes (16): 12. The bond book, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+8 more)

### Community 45 - "Plant"
Cohesion: 0.12
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 46 - ".greeting"
Cohesion: 0.16
Nodes (5): 13. Data formats, BondDialogue, DialogueKeys, BondDialogueTest, 10. Content plan

### Community 48 - "Look"
Cohesion: 0.11
Nodes (4): 7. Locked and changeable, Look, Result, RestyleAndGrowUpTest

### Community 49 - "Restyle"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 50 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 51 - "kit_hagane.py"
Cohesion: 0.07
Nodes (17): smithy, weapon, Weapon Shop (`weapon_shop`), hip_katana(), katana(), bracers(), crown(), harness() (+9 more)

### Community 52 - "cel_box"
Cohesion: 0.03
Nodes (61): Shared helpers, back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock() (+53 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (78): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+70 more)

### Community 57 - "Bonds"
Cohesion: 0.14
Nodes (12): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 6. Shared experiences and moments (+4 more)

### Community 58 - "Character creation"
Cohesion: 0.10
Nodes (20): 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 1 Name, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 60 - "FirstFifteenHours.java"
Cohesion: 0.14
Nodes (5): Stage, ADULT, CHILD, TEEN, Leaf

### Community 61 - ".play"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "paint.py"
Cohesion: 0.06
Nodes (22): puff(), drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+14 more)

### Community 64 - "Tex"
Cohesion: 0.14
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 65 - "Recipes"
Cohesion: 0.14
Nodes (17): apothecary, cooking.oven, cooking.pot, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient (+9 more)

### Community 66 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 67 - "Peeve"
Cohesion: 0.15
Nodes (11): Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS, NEGLECT (+3 more)

### Community 68 - "Bond"
Cohesion: 0.04
Nodes (4): Bond, BondConditions, BondWeb, FollowUp

### Community 70 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 71 - "catalogue.py"
Cohesion: 0.23
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.13
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 75 - "Squad"
Cohesion: 0.08
Nodes (11): 14. Save format and versioning, Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS (+3 more)

### Community 77 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 78 - "Home"
Cohesion: 0.08
Nodes (5): 17. What the map needs, Flat, Room, Home, Photo

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
Cohesion: 0.09
Nodes (16): 20. What the roadmap asks of bonds, 5. Personality, Base, Personality, Value, COURAGE, CREATIVITY, DUTY (+8 more)

### Community 87 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 89 - "Category"
Cohesion: 0.06
Nodes (28): Catalog, FurnitureSet, Category, BATH, BED, DECOR, DISPLAY, FIXTURE (+20 more)

### Community 92 - ".effectiveLevel"
Cohesion: 0.07
Nodes (15): 6. Conversations, Conversation, Reply, Topic, LifeEvents, News, Standing, Title (+7 more)

### Community 93 - ".name"
Cohesion: 0.16
Nodes (7): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, ConflictTest

### Community 94 - ".shelf"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 95 - ".of"
Cohesion: 0.10
Nodes (7): Score, Practice, Session, Rest, Rested, ComfortTest, RestTest

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

### Community 101 - "dialogue.py"
Cohesion: 0.13
Nodes (34): assign_ids(), build(), check_condition(), check_text(), compiled(), compiled_question(), content_key(), coverage() (+26 more)

### Community 102 - ".daily"
Cohesion: 0.11
Nodes (8): Friends, Tidiness, LIVED_IN, MESSY, TIDY, Day, Visit, Visits

### Community 103 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 105 - "NamesTest"
Cohesion: 0.21
Nodes (4): 10. How residents address you, Names, PlayerName, NamesTest

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "RosterTest"
Cohesion: 0.13
Nodes (4): Day, CurveAndTierTest, RosterTest, TechniqueTest

### Community 108 - "Outcome"
Cohesion: 0.33
Nodes (6): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT

### Community 109 - "fabric"
Cohesion: 0.03
Nodes (57): gear, leg_cloth(), shirt(), waist(), body(), arm_guards(), cargo(), gloves() (+49 more)

### Community 110 - ".strings"
Cohesion: 0.35
Nodes (3): Band, Mate, SquadPlan

### Community 112 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 113 - "shuriken"
Cohesion: 0.40
Nodes (4): Ninja Tool Shop (`tool_shop`), tool, shuriken(), smoke_bomb()

### Community 114 - "Home"
Cohesion: 0.09
Nodes (22): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 1. Design rules, 20. By beta slice (+14 more)

### Community 115 - "Konoha: the build plan"
Cohesion: 0.12
Nodes (18): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 5. Process, 6. Prototypes, 7. Effort estimate, 8. Registration notes for Phase 0, By building type, Calibration (+10 more)

### Community 116 - "Custom blocks"
Cohesion: 0.11
Nodes (17): 4. Block catalogue, Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival (+9 more)

### Community 117 - "Niche"
Cohesion: 0.10
Nodes (14): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+6 more)

### Community 118 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 119 - "konoha/preview.py"
Cohesion: 0.14
Nodes (15): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+7 more)

### Community 120 - "roster.py"
Cohesion: 0.18
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 121 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 123 - "Ranks"
Cohesion: 0.11
Nodes (17): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+9 more)

### Community 125 - "FirstFifteenHours.java"
Cohesion: 0.13
Nodes (3): Rng, Seeds, Comfort

### Community 126 - "Every building"
Cohesion: 0.11
Nodes (18): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+10 more)

### Community 129 - "Desk"
Cohesion: 0.11
Nodes (9): Desk, Offer, Player, Rank, A, B, C, D (+1 more)

### Community 130 - "Kind"
Cohesion: 0.50
Nodes (4): Kind, CYCLE, LINE, REPEAT

### Community 131 - ".run"
Cohesion: 0.20
Nodes (6): 19. Pacing, FirstFifteenHours, Result, Slice, Snapshot, FirstFifteenHoursTest

### Community 133 - "Tier"
Cohesion: 0.11
Nodes (12): Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY, Tier, ACADEMY_FLAT (+4 more)

### Community 134 - "Catalogue"
Cohesion: 0.16
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 135 - "Talk"
Cohesion: 0.15
Nodes (8): Line, Overheard, Said, Talk, Why, BUDGET, EXHAUSTED, NONE

### Community 136 - "Village"
Cohesion: 0.13
Nodes (6): House, Tier, BACKGROUND, CAST, KNOWN, Village

### Community 137 - "org.junit.jupiter.api.Test"
Cohesion: 0.05
Nodes (11): SquadTest, CatalogueTest, JsonTest, RyoTest, CatalogTest, LivingTest, MoveTest, CatalogueTest (+3 more)

### Community 139 - "Fixture"
Cohesion: 0.15
Nodes (4): 4. Storage, Fixture, QuestionsAndLedgerTest, TalkTest

### Community 140 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 142 - "creator/preview.py"
Cohesion: 0.16
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 143 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 146 - "Prices"
Cohesion: 0.15
Nodes (3): Pawn, Prices, PricesTest

### Community 150 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 151 - "Person"
Cohesion: 0.08
Nodes (4): Conflict, Household, Person, Recruitment

### Community 152 - "Wallet"
Cohesion: 0.05
Nodes (33): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+25 more)

### Community 153 - "ClanPower"
Cohesion: 0.14
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 154 - "Stretch"
Cohesion: 0.14
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 157 - "Streams"
Cohesion: 0.21
Nodes (3): Rng, Streams, StreamsTest

### Community 158 - "TimeAndPacingTest"
Cohesion: 0.14
Nodes (10): 15. Pacing, TimeAndPacingTest, 11. Open questions, 1. What makes a relationship feel real, 4. Their lives, 5. Following up, 7. Questions and choices, 8. Data and quest hooks (+2 more)

### Community 160 - "Tier"
Cohesion: 0.12
Nodes (7): Tier, A, B, C, D, E, S

### Community 162 - "Memory"
Cohesion: 0.13
Nodes (7): Memory, Source, HEARD, SEEN, SELF, TOLD, MemoryTest

### Community 163 - "VillageScaleTest"
Cohesion: 0.15
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 164 - "VisitsTest"
Cohesion: 0.20
Nodes (3): Cast, Setup, VisitsTest

### Community 165 - "Playthrough.java"
Cohesion: 0.08
Nodes (3): Schedule, SampleQuestions, 2. Schedules

### Community 166 - "6. Filler arcs"
Cohesion: 0.50
Nodes (4): 6. Filler arcs, In the beta, Later (foundation), Later one-offs (foundation)

### Community 172 - "kunai"
Cohesion: 0.38
Nodes (6): Exam-Week Stalls (`exam_stalls`), Pawn Shop (`pawn_shop`), along(), f(), kunai(), blade()

### Community 174 - ".receive"
Cohesion: 0.26
Nodes (5): 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest

### Community 178 - "Bank"
Cohesion: 0.16
Nodes (5): Bank, Facet, Pacing, Rules, Tier

### Community 182 - "BetaTalk"
Cohesion: 0.27
Nodes (4): BetaTalk, Person, Player, World

### Community 183 - ".answer"
Cohesion: 0.13
Nodes (7): Answer, Question, Answered, Outcome, Questions, QuestionsCompiledTest, QuestionsTest

### Community 184 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 185 - "Keepsake"
Cohesion: 0.12
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 186 - "The village"
Cohesion: 0.29
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 189 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 190 - "Question"
Cohesion: 0.16
Nodes (6): Turn, Answer, Question, Need, Tags, Answered

### Community 192 - ".choices"
Cohesion: 0.25
Nodes (3): Choices, Outfit, CreatorRulesTest

### Community 193 - "Dialogue"
Cohesion: 0.11
Nodes (16): 10. Pool sizing, 11. Simulation, 12. Story-gated pools, 13. What waits, 14. Decisions and open questions, 1. Freshness: never repeat, 2. Talk budgets, 3. Beyond the budget (+8 more)

### Community 194 - "Names"
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
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1597 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **42 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `Village`, `org.junit.jupiter.api.Test`, `.person`, `.classic`, `Person`, `VillageScaleTest`, `VisitsTest`, `Playthrough.java`, `.person`, `Run`, `.greeting`, `Squad`, `.receive`, `.answer`, `FirstFifteenHours.java`, `Bond`, `.of`, `Stage`, `Levels`, `Deed`, `Squad`, `map`, `.effectiveLevel`, `.name`, `FirstFifteenHours.java`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _342 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `creator.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07058001397624039 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `kit_uchiha.py`, `kit_senju.py`, `rnd`, `kit_kurama.py`, `kit_market.py`, `kit_kunoichi.py`, `kit_suzuran.py`, `Shops`, `solid`, `kit_morino.py`, `kit_kinoshita.py`, `kit_rugged.py`, `kit_hagane.py`, `cel_box`, `paint.py`, `kit_haruno.py`, `senbon`, `fabric`, `Custom blocks`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `kit_uchiha.py`, `kit_senju.py`, `rnd`, `kit_kurama.py`, `kit_market.py`, `kit_kunoichi.py`, `kit_suzuran.py`, `k`, `Box`, `Shops`, `kit_morino.py`, `kit_kinoshita.py`, `kit_rugged.py`, `kit_hagane.py`, `cel_box`, `paint.py`, `kit_haruno.py`, `senbon`, `fabric`, `Custom blocks`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.11578947368421053 - nodes in this community are weakly interconnected._