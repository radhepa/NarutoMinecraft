# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 330 files · ~747,986 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 5425 nodes · 12729 edges · 235 communities (176 shown, 59 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1394 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c14bb3f8`
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
- fabric
- creator.py
- k
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
- paint.py
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
- kit_kunoichi.py
- Playthrough
- kit_shinobi.py
- Playthrough.java
- .of
- Memory
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
- kit_yuhi.py
- org.junit.jupiter.api.Test
- Kind
- Every building
- list
- .obj
- build.py
- Box
- Bond
- .classmate
- Move
- blocks.py
- Def
- Levels
- Deed
- kit_kurama.py
- kit_hagane.py
- .read
- kit_market.py
- CreatorRules
- Mood
- kit_field.py
- 4.3 The noble clans
- Value
- HandSign
- Meters
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
- .effectiveLevel
- Plant
- The village
- BetaTalk
- VillageSim.java
- missions.py
- Power
- .classic
- kit_specialist.py
- kit_inuzuka.py
- .allowed
- 15. Furniture
- Naruto Minecraft
- render_kit.py
- VisitsTest
- .num
- Dialogue
- Names
- Styles and combo trees
- blocks.py
- progression.py
- senbon
- Konoha: the build plan
- .open
- creator/preview.py
- Json
- Battle.java
- Kindle
- AnswerTag
- Streams
- Custom blocks
- ComboMachine
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
- load_clans
- Rng
- Act.java
- NamesTest
- Battle.java
- rot_matrix
- Tier
- BondInput
- Pantry
- .run
- Json
- Rng
- .chains
- Kind
- SquadPlan
- kit_tsuchigumo.py
- RuleOfThumbTest
- StatusEffects
- Mission catalogue
- Bosses
- docs.py
- Json
- MoveTest
- leaf_block.py
- Result
- .look
- _key
- Restyle
- Pool
- Weaver
- RyoTest
- clans.py
- Chakra
- Story check handoff
- Tier
- .set
- Animation clips
- Technique catalogue
- Technique
- State
- SquadTest
- Tier
- Tier
- EmberLink
- Rng
- GossipTest
- DataTest
- Combat
- 6. Filler arcs
- weapons.py
- Tags
- Phase
- common.py
- Writing dialogue for the Leaf
- Outcome
- QuestionsAndLedgerTest
- build
- SeedsTest.java
- Cooldowns
- QuestionsCompiledTest
- Why
- Plan
- Data
- animations.py
- Kind

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 204 edges
3. `solid()` - 151 edges
4. `Act` - 129 edges
5. `fabric()` - 109 edges
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

## Communities (235 total, 59 thin omitted)

### Community 0 - "set"
Cohesion: 0.09
Nodes (4): Contribution, GrowthEvent, Grower, Roster

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
Nodes (40): weapon, How the pieces work, drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash() (+32 more)

### Community 7 - "Story bible"
Cohesion: 0.09
Nodes (22): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines, District quests and one-offs, Filler arcs, Kindling Bond (+14 more)

### Community 8 - "fabric"
Cohesion: 0.03
Nodes (57): back_fan(), bangs(), cel_box(), cel_face(), curtain(), lock(), ring_shell(), sidelocks() (+49 more)

### Community 9 - "creator.py"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

### Community 11 - "k"
Cohesion: 0.05
Nodes (33): Shared helpers, braid(), deep_hood(), high_collar(), hood_down(), lenses(), arm_bone(), arm_x() (+25 more)

### Community 12 - "Wallet"
Cohesion: 0.05
Nodes (32): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+24 more)

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
Cohesion: 0.07
Nodes (31): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), Exam-Week Stalls (`exam_stalls`), gift (+23 more)

### Community 18 - ".answer"
Cohesion: 0.15
Nodes (6): Answer, Question, Answered, Outcome, Questions, QuestionsTest

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "dialogue.py"
Cohesion: 0.05
Nodes (69): compose(), flush_kernel(), flush_template(), fail(), main(), assign_ids(), build(), check_condition() (+61 more)

### Community 21 - "mkit.py"
Cohesion: 0.14
Nodes (35): 4.1 The format, Code by mod, The quest format, anchor(), buy(), choose(), chose(), collect() (+27 more)

### Community 22 - "Category"
Cohesion: 0.04
Nodes (35): Catalog, Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST (+27 more)

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
Cohesion: 0.04
Nodes (34): leg_cloth(), waist(), arm_cloth(), bands(), blossom(), checks(), cloth_shoes(), collar_band() (+26 more)

### Community 27 - "paint.py"
Cohesion: 0.05
Nodes (27): clipped(), coat_skirts(), combed_back(), head_cloth(), nape_hem(), forehead_protector(), seal_script(), seal_tags() (+19 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.13
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Principles, Ranks and milestones, Rotating story roles (+5 more)

### Community 31 - "Fighter"
Cohesion: 0.09
Nodes (10): Battle, Plan, Plan, Plan, Chain, Event, Plan, Result (+2 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.17
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+8 more)

### Community 33 - "11. Later systems"
Cohesion: 0.12
Nodes (14): 6. Squad missions, 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans (+6 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.09
Nodes (23): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, 8. The beta, chapter by chapter, 9. Delivery plan, Beta 1: the opening and the Academy (~4 h), Beta 1: the opening and the Academy (~4 h main path) (+15 more)

### Community 35 - "Talk"
Cohesion: 0.17
Nodes (5): Context, Line, Overheard, Said, Talk

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "CombatData"
Cohesion: 0.06
Nodes (13): Boss, Build, CombatData, Enemy, Phase, Weapon, Balance, Share (+5 more)

### Community 39 - "Pillar"
Cohesion: 0.07
Nodes (20): Attack, Damage, Defence, Delivery, AREA, JUTSU, MELEE, THROWN (+12 more)

### Community 40 - "Nature"
Cohesion: 0.11
Nodes (16): Armour, CHAKRA, NONE, PHYSICAL, WILL, DamageType, Clash, Nature (+8 more)

### Community 41 - "sprites.py"
Cohesion: 0.07
Nodes (35): cooking.oven, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient, Market Grocer (`grocer`), material (+27 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode()

### Community 43 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 44 - "Playthrough"
Cohesion: 0.06
Nodes (17): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+9 more)

### Community 45 - "kit_shinobi.py"
Cohesion: 0.06
Nodes (19): shirt(), anbu_arms(), anbu_plates(), flak_vest(), mesh(), sandals(), wraps(), decal() (+11 more)

### Community 47 - ".of"
Cohesion: 0.15
Nodes (4): Rest, Rested, ComfortTest, RestTest

### Community 48 - "Memory"
Cohesion: 0.20
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 49 - "Box"
Cohesion: 0.31
Nodes (3): compatible(), Garment, key_rgba()

### Community 50 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 51 - ".xpAt"
Cohesion: 0.16
Nodes (3): Day, RosterTest, TechniqueTest

### Community 52 - "Home"
Cohesion: 0.07
Nodes (25): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 17. What the map needs, 1. Design rules (+17 more)

### Community 53 - "Home"
Cohesion: 0.08
Nodes (6): Home, Tidiness, LIVED_IN, MESSY, TIDY, Photo

### Community 54 - "Act"
Cohesion: 0.02
Nodes (79): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+71 more)

### Community 55 - "Stage"
Cohesion: 0.05
Nodes (14): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+6 more)

### Community 56 - "BondWorld"
Cohesion: 0.05
Nodes (6): BondEffects, BondWorld, LifeEvents, Departure, Squad, Standing

### Community 57 - "VarietyGuard"
Cohesion: 0.10
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 58 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 59 - "Look"
Cohesion: 0.11
Nodes (4): 7. Locked and changeable, Look, Result, RestyleAndGrowUpTest

### Community 60 - "kit_yuhi.py"
Cohesion: 0.05
Nodes (20): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar(), bandage_turns() (+12 more)

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.06
Nodes (9): 19. Pacing, CatalogueTest, JsonTest, LivingTest, FirstFifteenHoursTest, CurveAndTierTest, CatalogueTest, SlotFillerTest (+1 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Every building"
Cohesion: 0.11
Nodes (18): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+10 more)

### Community 65 - ".obj"
Cohesion: 0.15
Nodes (9): SeasonTest, Profile, DEVOTED, RECKLESS, TYPICAL, Result, Row, Season (+1 more)

### Community 66 - "build.py"
Cohesion: 0.19
Nodes (9): all_techniques(), build(), check(), statuses_in(), fold(), main(), public_text_hashes(), short() (+1 more)

### Community 67 - "Box"
Cohesion: 0.11
Nodes (3): strip_line(), Box, Layer

### Community 68 - "Bond"
Cohesion: 0.04
Nodes (6): 15. Pacing, Bond, BondConditions, BondWeb, News, FollowUp

### Community 69 - ".classmate"
Cohesion: 0.19
Nodes (3): 3. Levels and story gates, LevelsTest, MemoryTest

### Community 70 - "Move"
Cohesion: 0.08
Nodes (3): Move, Style, ComboAndStatusTest

### Community 71 - "blocks.py"
Cohesion: 0.08
Nodes (26): furniture, Furniture Shop (`furniture_shop`), 6. Prototypes, By building type, Facades and shop fronts, Interior fittings, Lanterns, Roofs (+18 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 74 - "Deed"
Cohesion: 0.16
Nodes (3): 8. The village talks, Deed, Know

### Community 75 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 76 - "kit_hagane.py"
Cohesion: 0.09
Nodes (14): gear, smithy, Weapon Shop (`weapon_shop`), shuriken(), arm_guards(), bracers(), crown(), harness() (+6 more)

### Community 78 - ".read"
Cohesion: 0.25
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 79 - "kit_market.py"
Cohesion: 0.04
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 80 - "CreatorRules"
Cohesion: 0.18
Nodes (3): 13. Code, and what waits for Phase 0, CreatorRules, Roots

### Community 81 - "Mood"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - "kit_field.py"
Cohesion: 0.07
Nodes (13): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+5 more)

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "Value"
Cohesion: 0.08
Nodes (23): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+15 more)

### Community 85 - "HandSign"
Cohesion: 0.09
Nodes (16): HandSign, BIRD, BOAR, DOG, DRAGON, HARE, HORSE, MONKEY (+8 more)

### Community 86 - "Meters"
Cohesion: 0.09
Nodes (5): 5. Personality, Meters, Personality, Reaction, ReactionTest

### Community 87 - "Clan techniques and kekkei genkai"
Cohesion: 0.08
Nodes (26): Aburame (noble), Akimichi (noble), Clan techniques and kekkei genkai, Gekko (noble), Hagane (minor), Haruno (minor), Hatake (noble), Hyuga (noble) (+18 more)

### Community 89 - "konoha/preview.py"
Cohesion: 0.14
Nodes (15): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+7 more)

### Community 90 - ".tier"
Cohesion: 0.06
Nodes (15): 11. Kindling Bond, Conflict, Household, Bonfire, Flame, Kindling, Read, Sight (+7 more)

### Community 91 - "Meter"
Cohesion: 0.10
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Missions"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Fixture"
Cohesion: 0.10
Nodes (14): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+6 more)

### Community 94 - "Village"
Cohesion: 0.04
Nodes (24): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+16 more)

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
Cohesion: 0.14
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
Cohesion: 0.10
Nodes (4): 4. Storage, 8. Questions and choices, Heard, Speaker

### Community 109 - ".person"
Cohesion: 0.12
Nodes (8): 12. The bond book, 18. The engine, 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest, BondFriends

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
Cohesion: 0.17
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 115 - "Prices"
Cohesion: 0.15
Nodes (3): Pawn, Prices, PricesTest

### Community 116 - ".effectiveLevel"
Cohesion: 0.07
Nodes (20): 13. Data formats, 6. Conversations, 9. Mass production, The bank today, BondDialogue, Conversation, Reply, Topic (+12 more)

### Community 117 - "Plant"
Cohesion: 0.13
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 118 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 119 - "BetaTalk"
Cohesion: 0.11
Nodes (17): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+9 more)

### Community 121 - "missions.py"
Cohesion: 0.18
Nodes (15): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), item_id() (+7 more)

### Community 122 - "Power"
Cohesion: 0.20
Nodes (7): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON

### Community 123 - ".classic"
Cohesion: 0.05
Nodes (11): 20. What the roadmap asks of bonds, BondBook, Fact, MemoryLine, Page, ConditionsAndEffectsTest, KindlingAndBookTest, Report (+3 more)

### Community 124 - "kit_specialist.py"
Cohesion: 0.11
Nodes (8): bandolier(), coat_skirts(), cross_armband(), ink_stains(), scroll_tube(), seal_trim(), shirt(), strap()

### Community 125 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 126 - ".allowed"
Cohesion: 0.22
Nodes (4): Facet, Pacing, Rules, Tier

### Community 127 - "15. Furniture"
Cohesion: 0.40
Nodes (5): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now)

### Community 128 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 129 - "render_kit.py"
Cohesion: 0.13
Nodes (10): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street() (+2 more)

### Community 130 - "VisitsTest"
Cohesion: 0.23
Nodes (3): Cast, Setup, VisitsTest

### Community 132 - "Dialogue"
Cohesion: 0.13
Nodes (12): 10. Pool sizing, 11. Simulation, 12. Story-gated pools, 13. What waits, 14. Decisions and open questions, 1. Freshness: never repeat, 2. Talk budgets, 3. Beyond the budget (+4 more)

### Community 133 - "Names"
Cohesion: 0.09
Nodes (4): Conditions, Names, Names, Tokens

### Community 134 - "Styles and combo trees"
Cohesion: 0.08
Nodes (24): Academy blade (`combat:style.academy_blade`, weapons), Academy taijutsu (`combat:style.academy_basics`, taijutsu), Beast Fang (Four Legs) (`combat:style.beast_fang`, taijutsu), Blossom Strength (`combat:style.blossom_strength`, taijutsu), Chain arts (`combat:style.chain_arts`, weapons), Crescent Moon kenjutsu (`combat:style.crescent_moon`, weapons), Fan arts (`combat:style.fan_arts`, weapons), Gentle Fist (`combat:style.gentle_fist`, taijutsu) (+16 more)

### Community 135 - "blocks.py"
Cohesion: 0.09
Nodes (11): auto_uv(), check(), compile_all(), facing_states(), main(), ref(), shoji(), shoji_paper() (+3 more)

### Community 136 - "progression.py"
Cohesion: 0.30
Nodes (10): beta_loadout(), build(), gear_for(), melee_for(), pillar_cap(), ranks_for(), sim_builds(), slice_open() (+2 more)

### Community 137 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 138 - "Konoha: the build plan"
Cohesion: 0.12
Nodes (17): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents (+9 more)

### Community 140 - "creator/preview.py"
Cohesion: 0.15
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 143 - "Battle.java"
Cohesion: 0.18
Nodes (4): Band, CLOSE, FAR, MID

### Community 146 - "Kindle"
Cohesion: 0.14
Nodes (10): Boost, Burn, Form, Kindle, Tier, BLAZE, FLAME, NONE (+2 more)

### Community 147 - "AnswerTag"
Cohesion: 0.10
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 148 - "Streams"
Cohesion: 0.21
Nodes (3): Rng, Streams, StreamsTest

### Community 149 - "Custom blocks"
Cohesion: 0.13
Nodes (14): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+6 more)

### Community 150 - "ComboMachine"
Cohesion: 0.23
Nodes (3): ComboMachine, Context, Started

### Community 153 - "Question"
Cohesion: 0.18
Nodes (4): Bank, Answer, Question, Answered

### Community 154 - "BetaTalk"
Cohesion: 0.23
Nodes (4): BetaTalk, Person, Player, World

### Community 156 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 157 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 158 - "Item catalogue"
Cohesion: 0.10
Nodes (21): apothecary, collectible, consumable, container, cooking.pot, curio, currency, Item catalogue (+13 more)

### Community 160 - ".choices"
Cohesion: 0.25
Nodes (3): Choices, Outfit, CreatorRulesTest

### Community 161 - "load_clans"
Cohesion: 0.21
Nodes (8): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans(), village_resident()

### Community 163 - "Act.java"
Cohesion: 0.15
Nodes (5): Stage, ADULT, CHILD, TEEN, Comfort

### Community 164 - "NamesTest"
Cohesion: 0.21
Nodes (4): 10. How residents address you, Names, PlayerName, NamesTest

### Community 166 - "rot_matrix"
Cohesion: 0.33
Nodes (3): Piece, piece_corners(), world_bounds()

### Community 167 - "Tier"
Cohesion: 0.13
Nodes (9): Score, Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY, Practice (+1 more)

### Community 168 - "BondInput"
Cohesion: 0.22
Nodes (3): 9. Data, code and Phase 0, BondInput, Day

### Community 169 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 170 - ".run"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 173 - ".chains"
Cohesion: 0.23
Nodes (4): Mode, CLASSIC, VARIED, Unlocks

### Community 174 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 175 - "SquadPlan"
Cohesion: 0.35
Nodes (3): Band, Mate, SquadPlan

### Community 176 - "kit_tsuchigumo.py"
Cohesion: 0.15
Nodes (7): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 178 - "StatusEffects"
Cohesion: 0.14
Nodes (3): Active, Def, StatusEffects

### Community 179 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 180 - "Bosses"
Cohesion: 0.08
Nodes (24): Bestiary, groups and bosses, Bosses, `combat:boss.anbu.story_1`: Story boss (chapter anbu, level 38, anbu), `combat:boss.ch11.bandit_chief`: Bandit chief (chapter 11, level 11, beta2), `combat:boss.ch14.road_ambush`: Ambush on the road (chapter 14, level 14, beta2), `combat:boss.ch16.forest_beast`: A giant of the forest (chapter 16, level 16, beta3), `combat:boss.ch16.forest_team`: A hunting team in the forest (chapter 16, level 16, beta3), `combat:boss.ch17.prelim`: Preliminary bout (chapter 17, level 16, beta3) (+16 more)

### Community 181 - "docs.py"
Cohesion: 0.28
Nodes (14): 7. Every line serves a function, animations_page(), bestiary_page(), clans_page(), counters(), esc(), move_rows(), signs() (+6 more)

### Community 186 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 188 - "Restyle"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 190 - "Weaver"
Cohesion: 0.16
Nodes (7): Outcome, CAST, EMPTY, FIZZLE, INTERRUPTED, Result, Weaver

### Community 197 - "clans.py"
Cohesion: 0.21
Nodes (10): ct(), lesser(), area(), cone(), line(), proj(), st(), summon_entity() (+2 more)

### Community 199 - "Story check handoff"
Cohesion: 0.18
Nodes (10): Checkers, Cross-system checks, Locking and merging, Owner decisions the story must respect, Read first, Rules, Story check handoff, The review process (+2 more)

### Community 200 - "Tier"
Cohesion: 0.18
Nodes (6): Mastery, Tier, MASTERED, NOVICE, PERFECTED, PRACTICED

### Community 202 - "Animation clips"
Cohesion: 0.33
Nodes (5): Animation clips, P0, P1, P2, P3

### Community 203 - "Technique catalogue"
Cohesion: 0.15
Nodes (13): Chakra movement, Earth (9), Fire (10), Fuinjutsu (6), Genjutsu (8), Lightning (8), Medical ninjutsu (5), Neutral ninjutsu (14) (+5 more)

### Community 206 - "State"
Cohesion: 0.14
Nodes (7): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, ConflictTest

### Community 208 - "Tier"
Cohesion: 0.20
Nodes (7): Tier, A, B, C, D, E, S

### Community 209 - "Tier"
Cohesion: 0.25
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 214 - "Combat"
Cohesion: 0.10
Nodes (18): Bonds, 10. Enemies, 11. Difficulty and feel, 12. Progression, 13. The beta loadout, 16. Animations, 17. What waits for Phase 0, 18. Ids for other systems (+10 more)

### Community 215 - "6. Filler arcs"
Cohesion: 0.50
Nodes (4): 6. Filler arcs, In the beta, Later (foundation), Later one-offs (foundation)

### Community 218 - "Tags"
Cohesion: 0.25
Nodes (3): Turn, Need, Tags

### Community 219 - "Phase"
Cohesion: 0.33
Nodes (6): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER

### Community 221 - "Writing dialogue for the Leaf"
Cohesion: 0.29
Nodes (7): Context tags, Questions, Rules the compiler enforces, Style, The format, Voices, Writing dialogue for the Leaf

### Community 222 - "Outcome"
Cohesion: 0.33
Nodes (6): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT

### Community 224 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 228 - "Why"
Cohesion: 0.50
Nodes (4): Why, BUDGET, EXHAUSTED, NONE

### Community 233 - "animations.py"
Cohesion: 0.50
Nodes (3): clip(), many(), summary()

### Community 237 - "Kind"
Cohesion: 0.50
Nodes (4): Kind, CYCLE, LINE, REPEAT

## Knowledge Gaps
- **391 isolated node(s):** `MELEE`, `THROWN`, `JUTSU`, `AREA`, `NONE` (+386 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1885 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **59 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `VisitsTest`, `.person`, `.answer`, `Act.java`, `Playthrough`, `Playthrough.java`, `Stage`, `Bond`, `Deed`, `map`, `.read`, `State`, `SquadTest`, `GossipTest`, `.tier`, `Village`, `.person`, `.effectiveLevel`, `VillageSim.java`, `.classic`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **What connects `MELEE`, `THROWN`, `JUTSU` to the rest of the system?**
  _391 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `set` be split into smaller, more focused modules?**
  _Cohesion score 0.08677098150782361 - nodes in this community are weakly interconnected._
- **Why does `Act` connect `Act` to `.person`, `.answer`, `AnswerTag`, `Act.java`, `Playthrough.java`, `Memory`, `Stage`, `BondWorld`, `Bond`, `.classmate`, `Def`, `Deed`, `.read`, `Value`, `Meters`, `.tier`, `Meter`, `.effectiveLevel`, `VillageSim.java`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `kit_uchiha.py`, `kit_senju.py`, `fabric`, `senbon`, `k`, `kit_suzuran.py`, `Shops`, `kit_rugged.py`, `Custom blocks`, `fabric`, `paint.py`, `kit_kinoshita.py`, `kit_akimichi.py`, `kit_kunoichi.py`, `kit_shinobi.py`, `kit_tsuchigumo.py`, `kit_yuhi.py`, `Box`, `kit_kurama.py`, `kit_hagane.py`, `kit_market.py`, `kit_field.py`, `kit_specialist.py`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.10526315789473684 - nodes in this community are weakly interconnected._