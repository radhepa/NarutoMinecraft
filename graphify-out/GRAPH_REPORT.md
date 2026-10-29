# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 331 files · ~747,311 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 5429 nodes · 12666 edges · 257 communities (181 shown, 76 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1346 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c14bb3f8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Roster
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- cel_box
- creator.py
- json
- kit_kurama.py
- Items, shops and crafting
- Economy
- kit_suzuran.py
- 7. Systems in the beta
- .friends
- Shops
- .answer
- rnd
- items.py
- mkit.py
- Category
- Template
- .daily
- Desk
- strip_fabric
- dialogue.py
- kit_kinoshita.py
- Fixture
- 5. Data formats built for the whole story
- Fighter
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- Context
- 4. Technical architecture
- VillageScaleTest
- Balance
- Pillar
- Nature
- sprites.py
- kit_akimichi.py
- kit_kunoichi.py
- Run
- k
- Playthrough.java
- .of
- Meters
- Garment
- mockups.py
- .xpAt
- Home
- Home
- Act
- Stage
- BondWorld
- World
- Plan
- Restyle
- treemap
- org.junit.jupiter.api.Test
- .name
- Every building
- .play
- build.py
- Box
- Bond
- .of
- Move
- blocks.py
- Def
- Bonds
- Deed
- kit_tobari.py
- kit_hagane.py
- Squad
- paint.py
- .look
- Mood
- .num
- 4.3 The noble clans
- .test
- HandSign
- Personality
- Clan techniques and kekkei genkai
- .obj
- konoha/preview.py
- Kindling
- Meter
- Title
- Niche
- ClanRelations
- Side quests
- 4.4 The minor clans
- .shelf
- 2. Quest framework
- Missions
- Label
- roster.py
- Wallet
- FirstFifteenHours.java
- Stretch
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- Heard
- .person
- Catalogue
- 4. Clan quest lines
- Character creation
- ClanPower
- Prices
- .react
- Plant
- The village
- Ranks
- VillageSim.java
- missions.py
- Power
- .classic
- Person
- CreatorRules
- Bank
- tatami
- Naruto Minecraft
- argparse
- VisitsTest
- Clients
- Dialogue
- Names
- Styles and combo trees
- compose.py
- progression.py
- fabric
- Konoha: the build plan
- DeskTest
- creator/preview.py
- Json
- Battle.java
- Kindle
- AnswerTag
- Streams
- Custom blocks
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
- Village
- Rng
- set
- catalogue.py
- math
- noren
- Flat
- kit_haruno.py
- Pantry
- .run
- Json
- Rng
- Recipes
- Kind
- .strings
- Life together
- RuleOfThumbTest
- StatusEffects
- Mission catalogue
- Bosses
- docs.py
- Json
- MoveTest
- pathlib
- Result
- 2. The Mission Desk
- _key
- Value
- Pool
- Weaver
- NamesTest
- clans.py
- Chakra
- Peeve
- Tier
- Animation clips
- Technique catalogue
- CombatData
- Speaker
- State
- SquadTest
- Tier
- .validateCreation
- EmberLink
- Rng
- DamageType
- kunai
- Combat
- Experience
- weapons.py
- Tags
- Tex
- .romance
- Writing dialogue for the Leaf
- SocietyHook
- .set
- build
- CourtshipTest
- Cooldowns
- GossipTest
- Look
- .home
- Stage
- Outcome
- End
- Scene
- SeedsTest.java
- .needs
- Look
- resolve

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 204 edges
3. `solid()` - 151 edges
4. `Act` - 129 edges
5. `fabric()` - 108 edges
6. `Bond` - 68 edges
7. `Home` - 67 edges
8. `Fighter` - 63 edges
9. `Village` - 63 edges
10. `Battle` - 59 edges

## Surprising Connections (you probably didn't know these)
- `4. Taijutsu` --references--> `Move`  [INFERRED]
  docs/COMBAT.md → combat/core/src/main/java/dev/shinobi/combat/Move.java
- `1.7 Gift tags` --references--> `Personality`  [INFERRED]
  ITEMS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Personality.java
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java
- `6. Coordination` --references--> `tatami()`  [INFERRED]
  ITEMS.md → tools/konoha/blocks.py

## Import Cycles
- None detected.

## Communities (257 total, 76 thin omitted)

### Community 0 - "Roster"
Cohesion: 0.09
Nodes (5): Hooks for the other mods, Contribution, GrowthEvent, Grower, Roster

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.10
Nodes (15): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, How to read this bible (+7 more)

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
Nodes (39): deep_hood(), high_collar(), hood_down(), lenses(), drawstrings(), forearm_wraps(), holster(), hood_down() (+31 more)

### Community 7 - "Story bible"
Cohesion: 0.10
Nodes (21): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Clan lines, District quests and one-offs, Filler arcs, Kindling Bond, Recurring characters (+13 more)

### Community 8 - "cel_box"
Cohesion: 0.03
Nodes (46): Shared helpers, back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock() (+38 more)

### Community 9 - "creator.py"
Cohesion: 0.06
Nodes (22): The clan file, check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs() (+14 more)

### Community 11 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 12 - "Items, shops and crafting"
Cohesion: 0.09
Nodes (23): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+15 more)

### Community 13 - "Economy"
Cohesion: 0.10
Nodes (11): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+3 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+9 more)

### Community 16 - ".friends"
Cohesion: 0.08
Nodes (15): 6. Conversations, Activity, BondEvent, Conversation, Reply, Topic, Answer, Highlight (+7 more)

### Community 17 - "Shops"
Cohesion: 0.09
Nodes (24): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), gift, Hagane Metalworks (`hagane_metalworks`) (+16 more)

### Community 18 - ".answer"
Cohesion: 0.09
Nodes (10): DialogueKeys, Answer, Question, Answered, Outcome, Questions, DialogueKeysTest, QuestionsCompiledTest (+2 more)

### Community 19 - "rnd"
Cohesion: 0.04
Nodes (33): sprigs(), fur_edge(), clipped(), baggy_legs(), camo(), cape(), dread(), knot_bun() (+25 more)

### Community 20 - "items.py"
Cohesion: 0.17
Nodes (20): art_class(), catalogue_md(), check_all(), check_loot(), compile_all(), recipe_entry(), dumps(), err() (+12 more)

### Community 21 - "mkit.py"
Cohesion: 0.14
Nodes (35): 4.1 The format, Code by mod, The quest format, anchor(), buy(), choose(), chose(), collect() (+27 more)

### Community 22 - "Category"
Cohesion: 0.07
Nodes (27): Catalog, Category, BATH, BED, DECOR, DISPLAY, FIXTURE, FLOOR (+19 more)

### Community 23 - "Template"
Cohesion: 0.09
Nodes (9): Catalogue, Branch, Step, Template, Twist, DeskDays, Profile, Run (+1 more)

### Community 24 - ".daily"
Cohesion: 0.15
Nodes (4): Friends, Day, Visit, Visits

### Community 25 - "Desk"
Cohesion: 0.11
Nodes (10): Desk, Offer, Player, Rank, A, B, C, D (+2 more)

### Community 26 - "strip_fabric"
Cohesion: 0.03
Nodes (46): leg_cloth(), waist(), body(), blouse(), cargo(), collar(), gloves(), half_sleeves() (+38 more)

### Community 27 - "dialogue.py"
Cohesion: 0.13
Nodes (35): assign_ids(), build(), check_condition(), check_text(), compiled(), compiled_question(), content_key(), coverage() (+27 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Fixture"
Cohesion: 0.15
Nodes (6): Kind, CYCLE, LINE, REPEAT, Fixture, TalkTest

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.14
Nodes (12): 1. At a glance, 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Ranks and milestones, Rotating story roles, Story flags (+4 more)

### Community 31 - "Fighter"
Cohesion: 0.12
Nodes (7): Battle, Chain, Event, Plan, Result, Strike, Fighter

### Community 32 - "wardrobe.py"
Cohesion: 0.11
Nodes (25): catalog(), compatible(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans(), load_collections() (+17 more)

### Community 33 - "11. Later systems"
Cohesion: 0.12
Nodes (13): 6. Squad missions, 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Later techniques and combat, Player clans, Ranks after Chunin (+5 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.06
Nodes (31): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, 6. The map, 8. The beta, chapter by chapter, 9. Delivery plan, Beta 1: the opening and the Academy (~4 h) (+23 more)

### Community 35 - "Context"
Cohesion: 0.12
Nodes (9): Context, Line, Overheard, Said, Talk, Why, BUDGET, EXHAUSTED (+1 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "VillageScaleTest"
Cohesion: 0.12
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 38 - "Balance"
Cohesion: 0.09
Nodes (10): Build, Enemy, Difficulty, Balance, Share, Stats, BalanceTest, Skill (+2 more)

### Community 39 - "Pillar"
Cohesion: 0.07
Nodes (20): Attack, Damage, Defence, Delivery, AREA, JUTSU, MELEE, THROWN (+12 more)

### Community 40 - "Nature"
Cohesion: 0.18
Nodes (8): Clash, Nature, EARTH, FIRE, LIGHTNING, NONE, WATER, WIND

### Community 41 - "sprites.py"
Cohesion: 0.10
Nodes (21): build(), Canvas, charm(), flak_vest(), forehead_protector(), framed_ladle(), headband(), hexrgb() (+13 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+1 more)

### Community 43 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 44 - "Run"
Cohesion: 0.07
Nodes (15): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+7 more)

### Community 45 - "k"
Cohesion: 0.03
Nodes (51): arm_bone(), arm_x(), belt(), collar(), flaps(), footwear(), sword_strap(), wrap_front() (+43 more)

### Community 46 - "Playthrough.java"
Cohesion: 0.09
Nodes (3): Household, Leaf, SampleQuestions

### Community 47 - ".of"
Cohesion: 0.15
Nodes (4): Rest, Rested, ComfortTest, RestTest

### Community 48 - "Meters"
Cohesion: 0.06
Nodes (9): Levels, Memory, Meters, Source, HEARD, SEEN, SELF, TOLD (+1 more)

### Community 49 - "Garment"
Cohesion: 0.14
Nodes (6): Garment, key_rgba(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 50 - "mockups.py"
Cohesion: 0.18
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 51 - ".xpAt"
Cohesion: 0.16
Nodes (3): Day, RosterTest, TechniqueTest

### Community 52 - "Home"
Cohesion: 0.13
Nodes (15): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 1. Design rules, 20. By beta slice (+7 more)

### Community 54 - "Act"
Cohesion: 0.02
Nodes (79): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+71 more)

### Community 55 - "Stage"
Cohesion: 0.08
Nodes (10): Conflict, Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+2 more)

### Community 56 - "BondWorld"
Cohesion: 0.07
Nodes (8): 17. Proposed ROADMAP edits, 1. The data model, 9. Quarrels with arcs, 18. The engine, BondEffects, BondWorld, Standing, Conditions and actions

### Community 57 - "World"
Cohesion: 0.14
Nodes (4): 9. The generator, Resident, World, SampleVillage

### Community 58 - "Plan"
Cohesion: 0.07
Nodes (13): Kinoshita Yard (`kinoshita_yard`), scroll, 3.1 Stations, 3.2 Recipes, 3.3 Unlocks, 3.4 Quality grades, 3.5 Repair and upgrade, 3.6 Where materials come from (+5 more)

### Community 59 - "Restyle"
Cohesion: 0.15
Nodes (9): 7. Locked and changeable, Restyle, Result, Venue, BARBER, HOME, LOCKED, SETTINGS (+1 more)

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.05
Nodes (11): DataTest, 19. Pacing, ReactionTest, CatalogueTest, JsonTest, LivingTest, FirstFifteenHoursTest, CurveAndTierTest (+3 more)

### Community 62 - ".name"
Cohesion: 0.06
Nodes (23): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+15 more)

### Community 63 - "Every building"
Cohesion: 0.12
Nodes (17): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+9 more)

### Community 65 - ".play"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 66 - "build.py"
Cohesion: 0.14
Nodes (12): all_techniques(), build(), check(), statuses_in(), fold(), main(), public_text_hashes(), short() (+4 more)

### Community 67 - "Box"
Cohesion: 0.12
Nodes (3): strip_line(), Box, Layer

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (5): Bond, LifeEvents, News, FollowUp, Kindling Bond

### Community 70 - "Move"
Cohesion: 0.07
Nodes (5): ComboMachine, Context, Started, Move, Style

### Community 71 - "blocks.py"
Cohesion: 0.15
Nodes (14): Roofs, auto_uv(), Block, box(), check(), compile_all(), kawara_ridge(), main() (+6 more)

### Community 72 - "Def"
Cohesion: 0.10
Nodes (5): Def, Size, BIG, NOTABLE, SMALL

### Community 73 - "Bonds"
Cohesion: 0.10
Nodes (16): 12. The bond book, 15. Pacing, 16. What stays in Village Friends, and what moves, 21. Open questions, 2. The meters, 3. Levels and story gates, 4. Memories, 6. Shared experiences and moments (+8 more)

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 75 - "kit_tobari.py"
Cohesion: 0.08
Nodes (14): shirt(), anbu_plates(), decal(), hood_down(), lantern(), lantern_tag(), mantle(), muffler() (+6 more)

### Community 76 - "kit_hagane.py"
Cohesion: 0.08
Nodes (17): gear, smithy, weapon, Weapon Shop (`weapon_shop`), arm_guards(), hip_katana(), katana(), bracers() (+9 more)

### Community 78 - "Squad"
Cohesion: 0.07
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 79 - "paint.py"
Cohesion: 0.05
Nodes (22): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), band() (+14 more)

### Community 80 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - ".test"
Cohesion: 0.15
Nodes (6): 7. Keepsakes, curios, photos and chests, Chests and storage, BondConditions, Gifts, Received, GiftsTest

### Community 85 - "HandSign"
Cohesion: 0.09
Nodes (16): HandSign, BIRD, BOAR, DOG, DRAGON, HARE, HORSE, MONKEY (+8 more)

### Community 86 - "Personality"
Cohesion: 0.13
Nodes (4): 20. What the roadmap asks of bonds, 5. Personality, Personality, Reaction

### Community 87 - "Clan techniques and kekkei genkai"
Cohesion: 0.08
Nodes (26): Aburame (noble), Akimichi (noble), Clan techniques and kekkei genkai, Gekko (noble), Hagane (minor), Haruno (minor), Hatake (noble), Hyuga (noble) (+18 more)

### Community 89 - "konoha/preview.py"
Cohesion: 0.16
Nodes (14): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+6 more)

### Community 90 - "Kindling"
Cohesion: 0.13
Nodes (12): 11. Kindling Bond, Bonfire, Flame, Kindling, Read, Sight, Thread, Tier (+4 more)

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Niche"
Cohesion: 0.08
Nodes (18): 12. Story-gated pools, 8. Growing up together, Pulling their weight, The 60 hours, simulated, The model, Niche, GENJUTSU, KENJUTSU (+10 more)

### Community 96 - "Side quests"
Cohesion: 0.22
Nodes (9): 1. Scope and budget, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents, In the beta, Later (foundation), Later one-offs (foundation) (+1 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - ".shelf"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 99 - "2. Quest framework"
Cohesion: 0.22
Nodes (9): 2.1 Kinds, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied, 2.9 Density for 300 residents (+1 more)

### Community 100 - "Missions"
Cohesion: 0.11
Nodes (18): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 3.1 Pay and XP bands, 3.2 Client standing and village reputation, 3. Ranks and the economy, 4.2 D rank: village life with a twist (41), 4.3 C rank: the roads, the border and real fights (26) (+10 more)

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "roster.py"
Cohesion: 0.18
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 103 - "Wallet"
Cohesion: 0.11
Nodes (3): Ryo, Wallet, RyoTest

### Community 105 - "Stretch"
Cohesion: 0.14
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "Heard"
Cohesion: 0.12
Nodes (3): 4. Storage, Heard, QuestionsAndLedgerTest

### Community 109 - ".person"
Cohesion: 0.10
Nodes (4): 13. Data formats, BondDialogue, Recruitment, BondFriends

### Community 110 - "Catalogue"
Cohesion: 0.16
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Character creation"
Cohesion: 0.10
Nodes (19): 12. Clan-born play: a later option, 13. Code, and what waits for Phase 0, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair, 3. Where the creator sits in the opening (+11 more)

### Community 114 - "ClanPower"
Cohesion: 0.17
Nodes (7): 1. The hierarchy, ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 115 - "Prices"
Cohesion: 0.14
Nodes (4): 2.1 How buying works, Pawn, Prices, PricesTest

### Community 116 - ".react"
Cohesion: 0.11
Nodes (7): Score, Tidiness, LIVED_IN, MESSY, TIDY, Practice, Session

### Community 117 - "Plant"
Cohesion: 0.16
Nodes (5): 9. Mass production, The bank today, Plant, Growing up, Rules the compiler enforces

### Community 118 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 119 - "Ranks"
Cohesion: 0.09
Nodes (16): 4. Comfort, style and sets, 10. Open questions, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+8 more)

### Community 121 - "missions.py"
Cohesion: 0.18
Nodes (15): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), item_id() (+7 more)

### Community 122 - "Power"
Cohesion: 0.20
Nodes (7): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON

### Community 123 - ".classic"
Cohesion: 0.10
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 124 - "Person"
Cohesion: 0.13
Nodes (5): 10. How residents address you, Markers, Person, Schedule, 2.2 Unlock rules

### Community 125 - "CreatorRules"
Cohesion: 0.18
Nodes (4): Choices, CreatorRules, Outfit, Data

### Community 126 - "Bank"
Cohesion: 0.20
Nodes (4): Bank, Facet, Pacing, Rules

### Community 127 - "tatami"
Cohesion: 0.16
Nodes (14): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now), furniture, Furniture Shop (`furniture_shop`), workbench (+6 more)

### Community 128 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 129 - "argparse"
Cohesion: 0.23
Nodes (6): blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 130 - "VisitsTest"
Cohesion: 0.22
Nodes (3): Cast, Setup, VisitsTest

### Community 132 - "Dialogue"
Cohesion: 0.16
Nodes (11): 10. Pool sizing, 11. Simulation, 13. What waits, 14. Decisions and open questions, 1. Freshness: never repeat, 2. Talk budgets, 3. Beyond the budget, 5. Selection: the most specific line wins (+3 more)

### Community 134 - "Styles and combo trees"
Cohesion: 0.08
Nodes (24): Academy blade (`combat:style.academy_blade`, weapons), Academy taijutsu (`combat:style.academy_basics`, taijutsu), Beast Fang (Four Legs) (`combat:style.beast_fang`, taijutsu), Blossom Strength (`combat:style.blossom_strength`, taijutsu), Chain arts (`combat:style.chain_arts`, weapons), Crescent Moon kenjutsu (`combat:style.crescent_moon`, weapons), Fan arts (`combat:style.fan_arts`, weapons), Gentle Fist (`combat:style.gentle_fist`, taijutsu) (+16 more)

### Community 135 - "compose.py"
Cohesion: 0.48
Nodes (5): compose(), flush_kernel(), flush_template(), fail(), main()

### Community 136 - "progression.py"
Cohesion: 0.35
Nodes (9): build(), gear_for(), melee_for(), pillar_cap(), ranks_for(), sim_builds(), slice_open(), teammate_build() (+1 more)

### Community 137 - "fabric"
Cohesion: 0.03
Nodes (46): How the pieces work, stamp(), back_crest(), crescent(), decal(), shoulder_decal(), slanted_protector(), crest() (+38 more)

### Community 138 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 9. Open questions, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 140 - "creator/preview.py"
Cohesion: 0.16
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 143 - "Battle.java"
Cohesion: 0.13
Nodes (5): Band, CLOSE, FAR, MID, RangeBands

### Community 146 - "Kindle"
Cohesion: 0.14
Nodes (10): Boost, Burn, Form, Kindle, Tier, BLAZE, FLAME, NONE (+2 more)

### Community 147 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 148 - "Streams"
Cohesion: 0.21
Nodes (3): Rng, Streams, StreamsTest

### Community 149 - "Custom blocks"
Cohesion: 0.14
Nodes (13): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Gardens (+5 more)

### Community 150 - "Keepsake"
Cohesion: 0.12
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 153 - "Question"
Cohesion: 0.24
Nodes (4): 8. Questions and choices, Answer, Question, Answered

### Community 154 - "BetaTalk"
Cohesion: 0.19
Nodes (4): BetaTalk, Person, Player, World

### Community 156 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 157 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 158 - "Item catalogue"
Cohesion: 0.12
Nodes (14): collectible, consumable, container, curio, currency, Item catalogue, keepsake, key (+6 more)

### Community 161 - "Village"
Cohesion: 0.16
Nodes (3): 18. Village scale, House, Village

### Community 163 - "set"
Cohesion: 0.08
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 164 - "catalogue.py"
Cohesion: 0.22
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 165 - "math"
Cohesion: 0.18
Nodes (4): matches(), _same_json(), OutputChecksTest, png()

### Community 166 - "noren"
Cohesion: 0.14
Nodes (12): 2. Style guide: the Konoha kit, 6. Prototypes, 8. Registration notes for Phase 0, By building type, Facades and shop fronts, Shared palette, Streets, Context tags (+4 more)

### Community 167 - "Flat"
Cohesion: 0.11
Nodes (9): 17. What the map needs, Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY, Flat (+1 more)

### Community 168 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 169 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 170 - ".run"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 173 - "Recipes"
Cohesion: 0.14
Nodes (17): apothecary, cooking.oven, cooking.pot, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient (+9 more)

### Community 174 - "Kind"
Cohesion: 0.17
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 175 - ".strings"
Cohesion: 0.21
Nodes (6): Mode, CLASSIC, VARIED, Band, Mate, SquadPlan

### Community 176 - "Life together"
Cohesion: 0.14
Nodes (10): TimeAndPacingTest, 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Questions and choices, 8. Data and quest hooks (+2 more)

### Community 178 - "StatusEffects"
Cohesion: 0.12
Nodes (3): Active, Def, StatusEffects

### Community 179 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 180 - "Bosses"
Cohesion: 0.08
Nodes (24): Bestiary, groups and bosses, Bosses, `combat:boss.anbu.story_1`: Story boss (chapter anbu, level 38, anbu), `combat:boss.ch11.bandit_chief`: Bandit chief (chapter 11, level 11, beta2), `combat:boss.ch14.road_ambush`: Ambush on the road (chapter 14, level 14, beta2), `combat:boss.ch16.forest_beast`: A giant of the forest (chapter 16, level 16, beta3), `combat:boss.ch16.forest_team`: A hunting team in the forest (chapter 16, level 16, beta3), `combat:boss.ch17.prelim`: Preliminary bout (chapter 17, level 16, beta3) (+16 more)

### Community 181 - "docs.py"
Cohesion: 0.17
Nodes (17): 7. Every line serves a function, clip(), many(), summary(), animations_page(), bestiary_page(), clans_page(), counters() (+9 more)

### Community 184 - "pathlib"
Cohesion: 0.12
Nodes (4): build(), build(), flat(), build()

### Community 186 - "2. The Mission Desk"
Cohesion: 0.25
Nodes (7): 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back, 2.5 Failure, partial success and abandonment, 2.6 Grades, 2. The Mission Desk

### Community 188 - "Value"
Cohesion: 0.13
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 190 - "Weaver"
Cohesion: 0.15
Nodes (7): Outcome, CAST, EMPTY, FIZZLE, INTERRUPTED, Result, Weaver

### Community 191 - "NamesTest"
Cohesion: 0.19
Nodes (4): 1 Name, Names, PlayerName, NamesTest

### Community 197 - "clans.py"
Cohesion: 0.21
Nodes (10): ct(), lesser(), area(), cone(), line(), proj(), st(), summon_entity() (+2 more)

### Community 199 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 200 - "Tier"
Cohesion: 0.18
Nodes (6): Mastery, Tier, MASTERED, NOVICE, PERFECTED, PRACTICED

### Community 202 - "Animation clips"
Cohesion: 0.33
Nodes (5): Animation clips, P0, P1, P2, P3

### Community 203 - "Technique catalogue"
Cohesion: 0.15
Nodes (13): Chakra movement, Earth (9), Fire (10), Fuinjutsu (6), Genjutsu (8), Lightning (8), Medical ninjutsu (5), Neutral ninjutsu (14) (+5 more)

### Community 204 - "CombatData"
Cohesion: 0.07
Nodes (6): Boss, CombatData, Phase, Technique, Weapon, ComboAndStatusTest

### Community 206 - "State"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 208 - "Tier"
Cohesion: 0.20
Nodes (7): Tier, A, B, C, D, E, S

### Community 212 - "DamageType"
Cohesion: 0.17
Nodes (9): Armour, CHAKRA, NONE, PHYSICAL, WILL, DamageType, 14. The combat core, 1. Core resources (+1 more)

### Community 213 - "kunai"
Cohesion: 0.20
Nodes (10): Exam-Week Stalls (`exam_stalls`), Ninja Tool Shop (`tool_shop`), Pawn Shop (`pawn_shop`), tool, along(), f(), kunai(), blade() (+2 more)

### Community 214 - "Combat"
Cohesion: 0.11
Nodes (17): Bonds, 10. Enemies, 11. Difficulty and feel, 12. Progression, 13. The beta loadout, 16. Animations, 17. What waits for Phase 0, 18. Ids for other systems (+9 more)

### Community 215 - "Experience"
Cohesion: 0.17
Nodes (10): Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION, SPAR (+2 more)

### Community 218 - "Tags"
Cohesion: 0.25
Nodes (3): Turn, Need, Tags

### Community 219 - "Tex"
Cohesion: 0.13
Nodes (4): tatami_top(), hexrgb(), shade(), Tex

### Community 221 - "Writing dialogue for the Leaf"
Cohesion: 0.40
Nodes (5): Questions, Style, The format, Voices, Writing dialogue for the Leaf

### Community 222 - "SocietyHook"
Cohesion: 0.22
Nodes (5): 19. Society hooks, SocietyHook, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests

### Community 224 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 229 - ".home"
Cohesion: 0.25
Nodes (7): 2. The flat, 9.1 Home hangouts, 9.2 Spare keys, 9. Visitors and spare keys, The Classic flat: `flat.leaf_block.3a`, Varied candidates, Your apartment and furniture

### Community 230 - "Stage"
Cohesion: 0.33
Nodes (6): Stage, FLOWERING, GRAND, LEAFY, SEEDLING, SPROUT

### Community 231 - "Outcome"
Cohesion: 0.33
Nodes (6): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT

### Community 232 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 236 - ".needs"
Cohesion: 0.22
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 237 - "Look"
Cohesion: 0.50
Nodes (4): Look, DROOPING, HEALTHY, WILTED

## Knowledge Gaps
- **800 isolated node(s):** `MELEE`, `THROWN`, `JUTSU`, `AREA`, `NONE` (+795 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1876 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **76 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `VisitsTest`, `.friends`, `.answer`, `Village`, `set`, `VillageScaleTest`, `Run`, `Playthrough.java`, `Meters`, `Stage`, `treemap`, `list`, `Bond`, `.of`, `Bonds`, `Deed`, `.week`, `Squad`, `SquadTest`, `.test`, `Kindling`, `CourtshipTest`, `GossipTest`, `FirstFifteenHours.java`, `.person`, `VillageSim.java`, `.classic`, `Person`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **What connects `MELEE`, `THROWN`, `JUTSU` to the rest of the system?**
  _800 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Roster` be split into smaller, more focused modules?**
  _Cohesion score 0.08961593172119488 - nodes in this community are weakly interconnected._
- **Why does `Act` connect `Act` to `.friends`, `.answer`, `set`, `Playthrough.java`, `Meters`, `Stage`, `BondWorld`, `Value`, `Bond`, `.of`, `Peeve`, `Def`, `Deed`, `Squad`, `Personality`, `Experience`, `Kindling`, `Meter`, `FirstFifteenHours.java`, `VillageSim.java`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `kit_uchiha.py`, `kit_senju.py`, `solid`, `cel_box`, `fabric`, `kit_akimichi.py`, `kit_haruno.py`, `kit_hagane.py`, `kit_kunoichi.py`, `kit_kurama.py`, `kit_suzuran.py`, `kit_tobari.py`, `paint.py`, `Shops`, `rnd`, `Custom blocks`, `strip_fabric`, `kit_kinoshita.py`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.1 - nodes in this community are weakly interconnected._