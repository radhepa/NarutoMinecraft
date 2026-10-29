# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 329 files · ~745,914 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 5401 nodes · 12671 edges · 238 communities (176 shown, 62 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1385 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4e9dd989`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- set
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- k
- Story bible
- kit_kurama.py
- creator.py
- .romance
- kit_kunoichi.py
- Items, shops and crafting
- Economy
- kit_suzuran.py
- 7. Systems in the beta
- .person
- Shops
- .answer
- rnd
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
- Fighter
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- Talk
- 4. Technical architecture
- 6. The map
- CombatData
- Pillar
- Nature
- sprites.py
- kit_akimichi.py
- kit_hagane.py
- Playthrough
- fabric
- Playthrough.java
- .of
- Meters
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
- FirstFifteenHours.java
- org.junit.jupiter.api.Test
- Kind
- Recipes
- list
- .obj
- build.py
- VillageScaleTest
- Bond
- .classmate
- Move
- blocks.py
- Def
- Levels
- Deed
- Conflict
- kit_hagane.py
- .person
- paint.py
- CreatorRules
- Mood
- ClanRelations
- 4.3 The noble clans
- kit_haruno.py
- HandSign
- Personality
- Clan techniques and kekkei genkai
- .obj
- konoha/preview.py
- .tier
- Meter
- Missions
- Fixture
- Village
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
- .talk
- Plant
- The village
- BetaTalk
- VillageSim.java
- missions.py
- Power
- .classic
- SampleQuestions
- pil
- Bank
- 15. Furniture
- Naruto Minecraft
- render_kit.py
- VisitsTest
- .num
- Dialogue
- Names
- Styles and combo trees
- masks.py
- progression.py
- stamp
- Konoha: the build plan
- .open
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
- NamesTest
- Rng
- .chains
- catalogue.py
- Wallet
- .look
- Restyle
- BondInput
- Pantry
- .run
- Json
- Rng
- kunai
- Kind
- SquadPlan
- TimeAndPacingTest
- RuleOfThumbTest
- StatusEffects
- Mission catalogue
- Bosses
- docs.py
- Json
- MoveTest
- Outcome
- Result
- .add
- _key
- SeedsTest.java
- Pool
- Weaver
- Data
- clans.py
- Chakra
- ComboMachine
- Tier
- kit_yamanaka.py
- Animation clips
- Technique catalogue
- Technique
- Bonds
- State
- SquadTest
- Tier
- Tier
- EmberLink
- Rng
- .Fighter
- 1. The registry
- Combat
- 6. Filler arcs
- weapons.py
- Tags
- DataTest
- common.py
- Writing dialogue for the Leaf
- senbon
- build
- Ryo
- Cooldowns
- 3. Crafting
- .allowed
- Phase
- AgeStageTest
- FirstFifteenHoursTest
- .tidiness
- animations.py
- 4. The ryo economy
- Tier
- Kind

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 201 edges
3. `solid()` - 151 edges
4. `Act` - 128 edges
5. `fabric()` - 109 edges
6. `Bond` - 67 edges
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

## Communities (238 total, 62 thin omitted)

### Community 0 - "set"
Cohesion: 0.10
Nodes (4): Hooks for the other mods, Contribution, GrowthEvent, Roster

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.12
Nodes (14): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+6 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (20): new_canvas(), save_canvas(), backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads() (+12 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "k"
Cohesion: 0.02
Nodes (68): deep_hood(), high_collar(), hood_down(), lenses(), back_crest(), drawstrings(), forearm_wraps(), holster() (+60 more)

### Community 7 - "Story bible"
Cohesion: 0.09
Nodes (22): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines, District quests and one-offs, Filler arcs, Kindling Bond (+14 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "creator.py"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - "Items, shops and crafting"
Cohesion: 0.15
Nodes (11): 2.1 How buying works, 2.2 The shops, 2.3 Part-time jobs, 2.4 Interiors (blocks asked of the Konoha session), 2. Shops, 5. Item art, 6. Coordination, 7. What waits for Phase 0 (+3 more)

### Community 13 - "Economy"
Cohesion: 0.08
Nodes (16): Band, Economy, End, ABANDONED, DONE, FAILED, PARTIAL, GradeRow (+8 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - ".person"
Cohesion: 0.09
Nodes (10): Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan, Together (+2 more)

### Community 17 - "Shops"
Cohesion: 0.08
Nodes (25): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), gift, Hagane Metalworks (`hagane_metalworks`) (+17 more)

### Community 18 - ".answer"
Cohesion: 0.16
Nodes (5): Answered, Outcome, Questions, QuestionsCompiledTest, QuestionsTest

### Community 19 - "rnd"
Cohesion: 0.03
Nodes (36): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+28 more)

### Community 20 - "dialogue.py"
Cohesion: 0.07
Nodes (60): compose(), flush_kernel(), flush_template(), fail(), main(), assign_ids(), build(), check_condition() (+52 more)

### Community 21 - "mkit.py"
Cohesion: 0.14
Nodes (35): 4.1 The format, Code by mod, The quest format, anchor(), buy(), choose(), chose(), collect() (+27 more)

### Community 22 - "Category"
Cohesion: 0.06
Nodes (28): Catalog, FurnitureSet, Category, BATH, BED, DECOR, DISPLAY, FIXTURE (+20 more)

### Community 23 - "Template"
Cohesion: 0.09
Nodes (9): Catalogue, Branch, Step, Template, Twist, DeskDays, Profile, Run (+1 more)

### Community 24 - ".daily"
Cohesion: 0.12
Nodes (4): Friends, Day, Visit, Visits

### Community 25 - "Desk"
Cohesion: 0.11
Nodes (9): Desk, Offer, Player, Rank, A, B, C, D (+1 more)

### Community 26 - "fabric"
Cohesion: 0.05
Nodes (24): arm_cloth(), bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta() (+16 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+14 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Fixture"
Cohesion: 0.17
Nodes (3): Fixture, QuestionsAndLedgerTest, TalkTest

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.13
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Principles, Ranks and milestones, Rotating story roles (+5 more)

### Community 31 - "Fighter"
Cohesion: 0.09
Nodes (11): Battle, Plan, Plan, Plan, Plan, Chain, Event, Plan (+3 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.10
Nodes (26): catalog(), clan_bottoms(), clan_resident(), compatible(), hex_rgb(), json_text(), load_all_groups(), load_characters() (+18 more)

### Community 33 - "11. Later systems"
Cohesion: 0.12
Nodes (14): 6. Squad missions, 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans (+6 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.09
Nodes (23): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, 8. The beta, chapter by chapter, 9. Delivery plan, Beta 1: the opening and the Academy (~4 h), Beta 1: the opening and the Academy (~4 h main path) (+15 more)

### Community 35 - "Talk"
Cohesion: 0.17
Nodes (7): Overheard, Said, Talk, Why, BUDGET, EXHAUSTED, NONE

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "CombatData"
Cohesion: 0.08
Nodes (13): Boss, Build, CombatData, Enemy, Phase, Difficulty, Balance, Share (+5 more)

### Community 39 - "Pillar"
Cohesion: 0.08
Nodes (19): Attack, Damage, Defence, Delivery, AREA, JUTSU, MELEE, THROWN (+11 more)

### Community 40 - "Nature"
Cohesion: 0.11
Nodes (16): Armour, CHAKRA, NONE, PHYSICAL, WILL, DamageType, Clash, Nature (+8 more)

### Community 41 - "sprites.py"
Cohesion: 0.14
Nodes (21): build(), Canvas, charm(), flak_vest(), forehead_protector(), framed_ladle(), headband(), hexrgb() (+13 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode()

### Community 43 - "kit_hagane.py"
Cohesion: 0.06
Nodes (20): gear, smithy, weapon, Weapon Shop (`weapon_shop`), shuriken(), hip_katana(), katana(), bracers() (+12 more)

### Community 44 - "Playthrough"
Cohesion: 0.07
Nodes (15): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+7 more)

### Community 45 - "fabric"
Cohesion: 0.04
Nodes (35): leg_cloth(), shirt(), waist(), body(), arm_guards(), cargo(), gloves(), half_sleeves() (+27 more)

### Community 46 - "Playthrough.java"
Cohesion: 0.06
Nodes (5): Stage, ADULT, CHILD, TEEN, Leaf

### Community 47 - ".of"
Cohesion: 0.12
Nodes (7): Score, Practice, Session, Rest, Rested, ComfortTest, RestTest

### Community 48 - "Meters"
Cohesion: 0.10
Nodes (8): Memory, Meters, Source, HEARD, SEEN, SELF, TOLD, ReactionTest

### Community 49 - "Box"
Cohesion: 0.14
Nodes (6): Garment, key_rgba(), Piece, piece_corners(), png_bytes(), world_bounds()

### Community 50 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 51 - ".xpAt"
Cohesion: 0.15
Nodes (3): Day, RosterTest, TechniqueTest

### Community 52 - "Home"
Cohesion: 0.07
Nodes (25): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 17. What the map needs, 1. Design rules (+17 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (78): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+70 more)

### Community 55 - "Stage"
Cohesion: 0.06
Nodes (13): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+5 more)

### Community 56 - "BondWorld"
Cohesion: 0.07
Nodes (3): BondWorld, Household, LifeEvents

### Community 57 - "VarietyGuard"
Cohesion: 0.10
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 58 - "Plan"
Cohesion: 0.06
Nodes (23): 3. Building catalogue, 9. Open questions, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes (+15 more)

### Community 59 - "Look"
Cohesion: 0.11
Nodes (4): 7. Locked and changeable, Look, Result, RestyleAndGrowUpTest

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.06
Nodes (9): GossipTest, CatalogueTest, JsonTest, RyoTest, CatalogTest, LivingTest, CurveAndTierTest, CatalogueTest (+1 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Recipes"
Cohesion: 0.14
Nodes (17): apothecary, cooking.oven, cooking.pot, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient (+9 more)

### Community 65 - ".obj"
Cohesion: 0.15
Nodes (9): SeasonTest, Profile, DEVOTED, RECKLESS, TYPICAL, Result, Row, Season (+1 more)

### Community 66 - "build.py"
Cohesion: 0.21
Nodes (9): all_techniques(), build(), check(), statuses_in(), fold(), main(), public_text_hashes(), short() (+1 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.13
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.04
Nodes (5): Bond, BondConditions, BondWeb, News, FollowUp

### Community 70 - "Move"
Cohesion: 0.08
Nodes (3): Move, Style, ComboAndStatusTest

### Community 71 - "blocks.py"
Cohesion: 0.09
Nodes (31): Beta 1, furniture, Furniture Shop (`furniture_shop`), workbench, 6. Prototypes, 8. Registration notes for Phase 0, By building type, Facades and shop fronts (+23 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.07
Nodes (9): 3. Levels and story gates, Levels, LevelsTest, Tier, BARE, BELOVED, COMFORTABLE, COSY (+1 more)

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 75 - "Conflict"
Cohesion: 0.11
Nodes (3): Conflict, Recruitment, VillageTest

### Community 76 - "kit_hagane.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 78 - ".person"
Cohesion: 0.08
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 79 - "paint.py"
Cohesion: 0.05
Nodes (26): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), band() (+18 more)

### Community 80 - "CreatorRules"
Cohesion: 0.18
Nodes (3): 13. Code, and what waits for Phase 0, CreatorRules, Roots

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - "HandSign"
Cohesion: 0.09
Nodes (16): HandSign, BIRD, BOAR, DOG, DRAGON, HARE, HORSE, MONKEY (+8 more)

### Community 86 - "Personality"
Cohesion: 0.06
Nodes (27): 20. What the roadmap asks of bonds, 5. Personality, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY (+19 more)

### Community 87 - "Clan techniques and kekkei genkai"
Cohesion: 0.08
Nodes (26): Aburame (noble), Akimichi (noble), Clan techniques and kekkei genkai, Gekko (noble), Hagane (minor), Haruno (minor), Hatake (noble), Hyuga (noble) (+18 more)

### Community 89 - "konoha/preview.py"
Cohesion: 0.16
Nodes (13): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+5 more)

### Community 90 - ".tier"
Cohesion: 0.12
Nodes (13): 11. Kindling Bond, 12. The bond book, Bonfire, Flame, Kindling, Read, Sight, Thread (+5 more)

### Community 91 - "Meter"
Cohesion: 0.10
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Missions"
Cohesion: 0.15
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Fixture"
Cohesion: 0.10
Nodes (13): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+5 more)

### Community 96 - "Side quests"
Cohesion: 0.25
Nodes (8): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 9. Open questions, Contents, Side quests

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - ".shelf"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 101 - ".classic"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "Label"
Cohesion: 0.17
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 105 - "Catalogue"
Cohesion: 0.13
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "Heard"
Cohesion: 0.12
Nodes (3): 4. Storage, Heard, Speaker

### Community 109 - ".person"
Cohesion: 0.13
Nodes (7): 18. The engine, 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest, BondFriends

### Community 110 - "Catalogue"
Cohesion: 0.16
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Character creation"
Cohesion: 0.10
Nodes (20): 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 1 Name, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 114 - "ClanPower"
Cohesion: 0.19
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 115 - "Prices"
Cohesion: 0.15
Nodes (3): Pawn, Prices, PricesTest

### Community 116 - ".talk"
Cohesion: 0.07
Nodes (18): 13. Data formats, 6. Conversations, BondDialogue, Conversation, Reply, Topic, DialogueKeys, BondDialogueTest (+10 more)

### Community 117 - "Plant"
Cohesion: 0.11
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 118 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 119 - "BetaTalk"
Cohesion: 0.12
Nodes (16): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+8 more)

### Community 121 - "missions.py"
Cohesion: 0.18
Nodes (15): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), item_id() (+7 more)

### Community 122 - "Power"
Cohesion: 0.20
Nodes (7): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON

### Community 123 - ".classic"
Cohesion: 0.11
Nodes (7): BondBook, Fact, MemoryLine, Page, BondEffects, ConditionsAndEffectsTest, KindlingAndBookTest

### Community 126 - "Bank"
Cohesion: 0.14
Nodes (6): Bank, Line, Turn, Facet, Pacing, Rules

### Community 127 - "15. Furniture"
Cohesion: 0.50
Nodes (4): 15. Furniture, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now)

### Community 128 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 129 - "render_kit.py"
Cohesion: 0.15
Nodes (9): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street(), paste() (+1 more)

### Community 130 - "VisitsTest"
Cohesion: 0.19
Nodes (3): Cast, Setup, VisitsTest

### Community 132 - "Dialogue"
Cohesion: 0.10
Nodes (15): 10. Pool sizing, 11. Simulation, 12. Story-gated pools, 13. What waits, 14. Decisions and open questions, 1. Freshness: never repeat, 2. Talk budgets, 3. Beyond the budget (+7 more)

### Community 133 - "Names"
Cohesion: 0.12
Nodes (3): Names, Names, Tokens

### Community 134 - "Styles and combo trees"
Cohesion: 0.08
Nodes (24): Academy blade (`combat:style.academy_blade`, weapons), Academy taijutsu (`combat:style.academy_basics`, taijutsu), Beast Fang (Four Legs) (`combat:style.beast_fang`, taijutsu), Blossom Strength (`combat:style.blossom_strength`, taijutsu), Chain arts (`combat:style.chain_arts`, weapons), Crescent Moon kenjutsu (`combat:style.crescent_moon`, weapons), Fan arts (`combat:style.fan_arts`, weapons), Gentle Fist (`combat:style.gentle_fist`, taijutsu) (+16 more)

### Community 135 - "masks.py"
Cohesion: 0.18
Nodes (7): How the pieces work, mesh(), beak(), bump(), ears(), plate(), strap()

### Community 136 - "progression.py"
Cohesion: 0.30
Nodes (10): beta_loadout(), build(), gear_for(), melee_for(), pillar_cap(), ranks_for(), sim_builds(), slice_open() (+2 more)

### Community 137 - "stamp"
Cohesion: 0.02
Nodes (66): Shared helpers, back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock() (+58 more)

### Community 138 - "Konoha: the build plan"
Cohesion: 0.12
Nodes (16): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 4. Block catalogue, 5. Process, 7. Effort estimate, Calibration, Contents, Konoha: the build plan (+8 more)

### Community 140 - "creator/preview.py"
Cohesion: 0.16
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 143 - "Battle.java"
Cohesion: 0.12
Nodes (6): Band, CLOSE, FAR, MID, RangeBands, Scaling

### Community 146 - "Kindle"
Cohesion: 0.14
Nodes (10): Boost, Burn, Form, Kindle, Tier, BLAZE, FLAME, NONE (+2 more)

### Community 147 - "AnswerTag"
Cohesion: 0.10
Nodes (19): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+11 more)

### Community 148 - "Streams"
Cohesion: 0.21
Nodes (3): Rng, Streams, StreamsTest

### Community 149 - "Custom blocks"
Cohesion: 0.11
Nodes (17): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+9 more)

### Community 150 - "Keepsake"
Cohesion: 0.12
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 153 - "Question"
Cohesion: 0.21
Nodes (4): 8. Questions and choices, Answer, Question, Answered

### Community 154 - "BetaTalk"
Cohesion: 0.25
Nodes (4): BetaTalk, Person, Player, World

### Community 156 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 157 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 158 - "Item catalogue"
Cohesion: 0.13
Nodes (15): collectible, consumable, container, curio, currency, Item catalogue, keepsake, key (+7 more)

### Community 160 - ".choices"
Cohesion: 0.25
Nodes (3): Choices, Outfit, CreatorRulesTest

### Community 161 - "NamesTest"
Cohesion: 0.21
Nodes (4): 10. How residents address you, Names, PlayerName, NamesTest

### Community 163 - ".chains"
Cohesion: 0.23
Nodes (4): Mode, CLASSIC, VARIED, Unlocks

### Community 164 - "catalogue.py"
Cohesion: 0.08
Nodes (15): check(), main(), build(), build(), flat(), build(), block_totals(), building_totals() (+7 more)

### Community 166 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 167 - "Restyle"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 168 - "BondInput"
Cohesion: 0.22
Nodes (3): 9. Data, code and Phase 0, BondInput, Day

### Community 169 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 170 - ".run"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 173 - "kunai"
Cohesion: 0.24
Nodes (9): Exam-Week Stalls (`exam_stalls`), Ninja Tool Shop (`tool_shop`), Pawn Shop (`pawn_shop`), tool, along(), f(), kunai(), blade() (+1 more)

### Community 174 - "Kind"
Cohesion: 0.20
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 175 - "SquadPlan"
Cohesion: 0.35
Nodes (3): Band, Mate, SquadPlan

### Community 176 - "TimeAndPacingTest"
Cohesion: 0.27
Nodes (3): 15. Pacing, TimeAndPacingTest, 9. Pacing with time together

### Community 178 - "StatusEffects"
Cohesion: 0.13
Nodes (3): Active, Def, StatusEffects

### Community 179 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 180 - "Bosses"
Cohesion: 0.08
Nodes (24): Bestiary, groups and bosses, Bosses, `combat:boss.anbu.story_1`: Story boss (chapter anbu, level 38, anbu), `combat:boss.ch11.bandit_chief`: Bandit chief (chapter 11, level 11, beta2), `combat:boss.ch14.road_ambush`: Ambush on the road (chapter 14, level 14, beta2), `combat:boss.ch16.forest_beast`: A giant of the forest (chapter 16, level 16, beta3), `combat:boss.ch16.forest_team`: A hunting team in the forest (chapter 16, level 16, beta3), `combat:boss.ch17.prelim`: Preliminary bout (chapter 17, level 16, beta3) (+16 more)

### Community 181 - "docs.py"
Cohesion: 0.25
Nodes (13): 7. Every line serves a function, animations_page(), bestiary_page(), clans_page(), counters(), esc(), move_rows(), signs() (+5 more)

### Community 184 - "Outcome"
Cohesion: 0.33
Nodes (6): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT

### Community 190 - "Weaver"
Cohesion: 0.16
Nodes (7): Outcome, CAST, EMPTY, FIZZLE, INTERRUPTED, Result, Weaver

### Community 197 - "clans.py"
Cohesion: 0.21
Nodes (10): ct(), lesser(), area(), cone(), line(), proj(), st(), summon_entity() (+2 more)

### Community 199 - "ComboMachine"
Cohesion: 0.23
Nodes (3): ComboMachine, Context, Started

### Community 200 - "Tier"
Cohesion: 0.18
Nodes (6): Mastery, Tier, MASTERED, NOVICE, PERFECTED, PRACTICED

### Community 201 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 202 - "Animation clips"
Cohesion: 0.33
Nodes (5): Animation clips, P0, P1, P2, P3

### Community 203 - "Technique catalogue"
Cohesion: 0.15
Nodes (13): Chakra movement, Earth (9), Fire (10), Fuinjutsu (6), Genjutsu (8), Lightning (8), Medical ninjutsu (5), Neutral ninjutsu (14) (+5 more)

### Community 205 - "Bonds"
Cohesion: 0.10
Nodes (15): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+7 more)

### Community 206 - "State"
Cohesion: 0.16
Nodes (7): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, ConflictTest

### Community 208 - "Tier"
Cohesion: 0.20
Nodes (7): Tier, A, B, C, D, E, S

### Community 209 - "Tier"
Cohesion: 0.25
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 213 - "1. The registry"
Cohesion: 0.22
Nodes (9): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+1 more)

### Community 214 - "Combat"
Cohesion: 0.10
Nodes (18): Bonds, 10. Enemies, 11. Difficulty and feel, 12. Progression, 13. The beta loadout, 16. Animations, 17. What waits for Phase 0, 18. Ids for other systems (+10 more)

### Community 215 - "6. Filler arcs"
Cohesion: 0.50
Nodes (4): 6. Filler arcs, In the beta, Later (foundation), Later one-offs (foundation)

### Community 221 - "Writing dialogue for the Leaf"
Cohesion: 0.25
Nodes (8): Context tags, Functions, Questions, Rules the compiler enforces, Style, The format, Voices, Writing dialogue for the Leaf

### Community 223 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 224 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 227 - "3. Crafting"
Cohesion: 0.29
Nodes (7): 3.1 Stations, 3.2 Recipes, 3.3 Unlocks, 3.4 Quality grades, 3.5 Repair and upgrade, 3.6 Where materials come from, 3. Crafting

### Community 229 - "Phase"
Cohesion: 0.33
Nodes (6): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER

### Community 232 - ".tidiness"
Cohesion: 0.40
Nodes (4): Tidiness, LIVED_IN, MESSY, TIDY

### Community 233 - "animations.py"
Cohesion: 0.50
Nodes (3): clip(), many(), summary()

### Community 235 - "4. The ryo economy"
Cohesion: 0.50
Nodes (4): 4.1 A closed loop, 4.2 Sinks and inflation guards, 4.3 The simulation, 4. The ryo economy

### Community 236 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 237 - "Kind"
Cohesion: 0.50
Nodes (4): Kind, CYCLE, LINE, REPEAT

## Knowledge Gaps
- **390 isolated node(s):** `MELEE`, `THROWN`, `JUTSU`, `AREA`, `NONE` (+385 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1871 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **62 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `VisitsTest`, `.romance`, `.person`, `.answer`, `AnswerTag`, `Playthrough`, `Playthrough.java`, `Stage`, `FirstFifteenHours.java`, `org.junit.jupiter.api.Test`, `list`, `VillageScaleTest`, `Bond`, `Deed`, `Conflict`, `.person`, `State`, `SquadTest`, `.tier`, `Missions`, `Village`, `.person`, `.talk`, `.classic`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **What connects `MELEE`, `THROWN`, `JUTSU` to the rest of the system?**
  _390 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `set` be split into smaller, more focused modules?**
  _Cohesion score 0.10114942528735632 - nodes in this community are weakly interconnected._
- **Why does `Act` connect `Act` to `Bond`, `.classmate`, `Def`, `Deed`, `Conflict`, `Playthrough`, `.person`, `Playthrough.java`, `Meters`, `.person`, `AnswerTag`, `.talk`, `Personality`, `BondWorld`, `.tier`, `Meter`, `FirstFifteenHours.java`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Levels`, `.romance`, `Conflict`, `.person`, `TimeAndPacingTest`, `.person`, `ClanRelations`, `Meters`, `.talk`, `Mood`, `Personality`, `Stage`, `.tier`, `ROADMAP.md`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._