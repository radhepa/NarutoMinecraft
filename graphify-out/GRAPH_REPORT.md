# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 329 files · ~746,303 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 5413 nodes · 12717 edges · 242 communities (181 shown, 61 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1393 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b42ed347`
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
- kit_market.py
- kit_kinoshita.py
- Json
- 5. Data formats built for the whole story
- k
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- .classic
- 4. Technical architecture
- 6. The map
- Shops
- 8. The beta, chapter by chapter
- kit_tobari.py
- Prices
- Roster
- kit_hagane.py
- Run
- .daily
- Playthrough.java
- utility_pole
- Trait
- Value
- .play
- Person
- Meters
- Grades
- Act
- Stage
- BondWorld
- Category
- .person
- EconomySim.java
- set
- Life together
- kit_suzuran.py
- Personality
- ClanProfile
- mockups.py
- kit_yuhi.py
- Bond
- .of
- Conflict
- .answer
- Def
- Peeve
- Deed
- .xpAt
- RuleOfThumbTest
- Squad
- org.junit.jupiter.api.Test
- Playthrough.java
- Mood
- kit_market.py
- 4.3 The noble clans
- kit_field.py
- .tier
- Plan
- Desk
- Niche
- Missions
- konoha/preview.py
- Meter
- .effectiveLevel
- .name
- Village
- Side quests
- 4.4 The minor clans
- CreatorRules
- 2. Quest framework
- Recipes
- kit_household.py
- Home
- kit_tsuchigumo.py
- Tex
- Experience
- FirstFifteenHours.java
- 8. Beta catalogue
- economy/build.gradle
- .receive
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
- Bonds
- Kind
- .everyKeyTheEngineEmitsIsListed
- VisitsTest
- BondInput
- 4. Clan quest lines
- Ranks
- creator/preview.py
- .receive
- Keepsake
- Player
- Json
- Rng
- pathlib
- shop_tea_house.py
- Kind
- ClanPower
- .strings
- 1. The registry
- AgeStage
- Stretch
- ROADMAP.md
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
- Items, shops and crafting
- SquadTest
- .name
- 3. Crafting
- Bonds
- Mission catalogue
- paper_lantern
- Rng
- The village
- .fill
- mission
- Person
- kunai
- Tier
- Naruto Minecraft
- Data
- home/build.gradle
- roster/build.gradle
- missions/build.gradle
- docs.py
- .familyNames
- 9. Delivery plan
- SeedsTest.java
- Side quest secrets
- utility_pole
- seal_script
- kit_specialist.py
- Pool
- Weaver
- Data
- clans.py
- Chakra
- ComboMachine
- Tier
- SignBook
- Animation clips
- Technique catalogue
- Technique
- GossipTest
- State
- SquadTest
- Tier
- Tier
- EmberLink
- Rng
- .read
- Bonds
- 6. Filler arcs
- Plan
- SocialTie
- Box
- .person
- ClanProfile
- ClanRelations
- .talk
- Question
- progression.py
- load_clans
- Question
- Writing dialogue for the Leaf
- weapons.py
- Conditions
- senbon
- build
- leaf_block.py
- Piece
- home_plaster_2f.py
- .valuesAndToneLandOnTheirPersonalityAndOppositePolesContradict
- SampleQuestions
- animations.py
- Tier
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
- `9. Pacing with time together` --references--> `TimeAndPacingTest`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java

## Import Cycles
- None detected.

## Communities (242 total, 61 thin omitted)

### Community 0 - "Activity"
Cohesion: 0.08
Nodes (8): 8. Growing up together, Hooks for the other mods, Pulling their weight, The 60 hours, simulated, Contribution, GrowthEvent, Grower, Roster

### Community 1 - "VillageScaleTest"
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

### Community 6 - "solid"
Cohesion: 0.03
Nodes (40): weapon, How the pieces work, drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash() (+32 more)

### Community 7 - "Story bible"
Cohesion: 0.10
Nodes (21): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Clan lines, District quests and one-offs, Filler arcs, Kindling Bond, Recurring characters (+13 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "creator.py"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

### Community 10 - "kit_uchiha.py"
Cohesion: 0.05
Nodes (20): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar(), bandage_turns() (+12 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - ".roll"
Cohesion: 0.05
Nodes (33): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+25 more)

### Community 13 - "items.py"
Cohesion: 0.08
Nodes (16): Band, Economy, End, ABANDONED, DONE, FAILED, PARTIAL, GradeRow (+8 more)

### Community 14 - ".obj"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - "paint.py"
Cohesion: 0.09
Nodes (11): 18. The engine, Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan (+3 more)

### Community 17 - "Economy"
Cohesion: 0.07
Nodes (30): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), Exam-Week Stalls (`exam_stalls`), gift (+22 more)

### Community 18 - "AnswerTag"
Cohesion: 0.19
Nodes (5): 8. Questions and choices, Answered, Outcome, Questions, QuestionsTest

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "blocks.py"
Cohesion: 0.06
Nodes (60): compose(), flush_kernel(), flush_template(), fail(), main(), assign_ids(), build(), check_condition() (+52 more)

### Community 21 - "Home"
Cohesion: 0.14
Nodes (35): 4.1 The format, Code by mod, The quest format, anchor(), buy(), choose(), chose(), collect() (+27 more)

### Community 22 - "mkit.py"
Cohesion: 0.06
Nodes (28): Catalog, FurnitureSet, Category, BATH, BED, DECOR, DISPLAY, FIXTURE (+20 more)

### Community 23 - "sprites.py"
Cohesion: 0.09
Nodes (9): Catalogue, Branch, Step, Template, Twist, DeskDays, Profile, Run (+1 more)

### Community 24 - "Catalogue"
Cohesion: 0.14
Nodes (4): Friends, Day, Visit, Visits

### Community 25 - "Template"
Cohesion: 0.11
Nodes (9): Desk, Offer, Player, Rank, A, B, C, D (+1 more)

### Community 26 - ".shelf"
Cohesion: 0.04
Nodes (34): leg_cloth(), waist(), arm_cloth(), bands(), blossom(), checks(), cloth_shoes(), collar_band() (+26 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (33): Shared helpers, braid(), deep_hood(), high_collar(), hood_down(), lenses(), arm_bone(), arm_x() (+25 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Json"
Cohesion: 0.14
Nodes (4): 4. Storage, Fixture, QuestionsAndLedgerTest, TalkTest

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.13
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Principles, Ranks and milestones, Rotating story roles (+5 more)

### Community 31 - "k"
Cohesion: 0.09
Nodes (10): Battle, Plan, Plan, Plan, Chain, Event, Plan, Result (+2 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.18
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+8 more)

### Community 33 - "11. Later systems"
Cohesion: 0.12
Nodes (14): 6. Squad missions, 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans (+6 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.09
Nodes (23): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, 8. The beta, chapter by chapter, 9. Delivery plan, Beta 1: the opening and the Academy (~4 h), Beta 1: the opening and the Academy (~4 h main path) (+15 more)

### Community 35 - ".classic"
Cohesion: 0.19
Nodes (8): Line, Overheard, Said, Talk, Why, BUDGET, EXHAUSTED, NONE

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "Shops"
Cohesion: 0.07
Nodes (14): Boss, Build, CombatData, Enemy, Phase, Weapon, Difficulty, Balance (+6 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.07
Nodes (20): Attack, Damage, Defence, Delivery, AREA, JUTSU, MELEE, THROWN (+12 more)

### Community 40 - "kit_tobari.py"
Cohesion: 0.05
Nodes (33): Cooldowns, Armour, CHAKRA, NONE, PHYSICAL, WILL, DamageType, Clash (+25 more)

### Community 41 - "Prices"
Cohesion: 0.07
Nodes (35): cooking.oven, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient, Market Grocer (`grocer`), material (+27 more)

### Community 42 - "Roster"
Cohesion: 0.11
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode()

### Community 43 - "kit_hagane.py"
Cohesion: 0.09
Nodes (14): gear, smithy, Weapon Shop (`weapon_shop`), shuriken(), arm_guards(), bracers(), crown(), harness() (+6 more)

### Community 44 - "Run"
Cohesion: 0.10
Nodes (14): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+6 more)

### Community 45 - ".daily"
Cohesion: 0.06
Nodes (19): shirt(), anbu_arms(), anbu_plates(), flak_vest(), mesh(), sandals(), wraps(), decal() (+11 more)

### Community 47 - "utility_pole"
Cohesion: 0.12
Nodes (5): Rest, Rested, CatalogTest, ComfortTest, RestTest

### Community 48 - "Trait"
Cohesion: 0.29
Nodes (6): Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH

### Community 49 - "Value"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 50 - ".play"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 51 - "Person"
Cohesion: 0.14
Nodes (4): Day, BondInput, Day, RosterTest

### Community 52 - "Meters"
Cohesion: 0.08
Nodes (22): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 1. Design rules, 20. By beta slice (+14 more)

### Community 53 - "Grades"
Cohesion: 0.07
Nodes (9): 17. What the map needs, Flat, Room, Home, Tidiness, LIVED_IN, MESSY, TIDY (+1 more)

### Community 54 - "Act"
Cohesion: 0.02
Nodes (79): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+71 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 57 - "Category"
Cohesion: 0.10
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 58 - ".person"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 59 - "EconomySim.java"
Cohesion: 0.11
Nodes (4): 7. Locked and changeable, Look, Result, RestyleAndGrowUpTest

### Community 61 - "Life together"
Cohesion: 0.05
Nodes (11): DataTest, 19. Pacing, CatalogueTest, JsonTest, RyoTest, LivingTest, FirstFifteenHoursTest, CatalogueTest (+3 more)

### Community 62 - "kit_suzuran.py"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Personality"
Cohesion: 0.12
Nodes (7): Memory, Meters, Source, HEARD, SEEN, SELF, TOLD

### Community 65 - "ClanProfile"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 66 - "mockups.py"
Cohesion: 0.15
Nodes (11): all_techniques(), build(), check(), statuses_in(), fold(), main(), public_text_hashes(), short() (+3 more)

### Community 67 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (5): 20. What the roadmap asks of bonds, 5. Personality, Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.04
Nodes (7): 15. Pacing, Bonds in the story (spoilers), Bond, BondConditions, BondWeb, News, FollowUp

### Community 69 - ".of"
Cohesion: 0.09
Nodes (3): ConflictTest, MemoryTest, ReactionTest

### Community 70 - "Conflict"
Cohesion: 0.08
Nodes (3): Move, Style, ComboAndStatusTest

### Community 71 - ".answer"
Cohesion: 0.10
Nodes (29): furniture, Furniture Shop (`furniture_shop`), Leaf Festival Stalls (`festival_stalls`), Facades and shop fronts, Interior fittings, Lanterns, Roofs, auto_uv() (+21 more)

### Community 72 - "Def"
Cohesion: 0.11
Nodes (5): Def, Size, BIG, NOTABLE, SMALL

### Community 73 - "Peeve"
Cohesion: 0.09
Nodes (13): 3. Levels and story gates, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+5 more)

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (3): Deed, Know, Gossip

### Community 76 - "RuleOfThumbTest"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 78 - "Squad"
Cohesion: 0.08
Nodes (3): BondEffects, Departure, Squad

### Community 79 - "org.junit.jupiter.api.Test"
Cohesion: 0.05
Nodes (27): clipped(), coat_skirts(), combed_back(), head_cloth(), nape_hem(), forehead_protector(), seal_script(), seal_tags() (+19 more)

### Community 80 - "Playthrough.java"
Cohesion: 0.18
Nodes (3): 13. Code, and what waits for Phase 0, CreatorRules, Roots

### Community 81 - "Mood"
Cohesion: 0.25
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - "kit_market.py"
Cohesion: 0.04
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_field.py"
Cohesion: 0.07
Nodes (13): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+5 more)

### Community 85 - ".tier"
Cohesion: 0.09
Nodes (14): HandSign, BIRD, BOAR, DOG, DRAGON, HARE, HORSE, MONKEY (+6 more)

### Community 86 - "Plan"
Cohesion: 0.07
Nodes (25): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+17 more)

### Community 87 - "Desk"
Cohesion: 0.08
Nodes (26): Aburame (noble), Akimichi (noble), Clan techniques and kekkei genkai, Gekko (noble), Hagane (minor), Haruno (minor), Hatake (noble), Hyuga (noble) (+18 more)

### Community 89 - "Missions"
Cohesion: 0.16
Nodes (14): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+6 more)

### Community 90 - "konoha/preview.py"
Cohesion: 0.09
Nodes (19): 11. Kindling Bond, Bonfire, Flame, Kindling, Power, EMBER_LINK, EMBER_MARK, KINDLE (+11 more)

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (7): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - ".effectiveLevel"
Cohesion: 0.07
Nodes (8): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME, Run

### Community 93 - ".name"
Cohesion: 0.10
Nodes (14): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+6 more)

### Community 96 - "Side quests"
Cohesion: 0.25
Nodes (8): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 9. Open questions, Contents, Side quests

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "CreatorRules"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Recipes"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 101 - "kit_household.py"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "Home"
Cohesion: 0.18
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 105 - "Experience"
Cohesion: 0.09
Nodes (11): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+3 more)

### Community 106 - "FirstFifteenHours.java"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "economy/build.gradle"
Cohesion: 0.09
Nodes (3): Heard, Speaker, Tier

### Community 109 - ".receive"
Cohesion: 0.26
Nodes (5): 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest

### Community 110 - ".choices"
Cohesion: 0.16
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 112 - "argparse"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Restyle"
Cohesion: 0.10
Nodes (20): 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 1 Name, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 114 - "Label"
Cohesion: 0.16
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 115 - "roster.py"
Cohesion: 0.15
Nodes (3): Pawn, Prices, PricesTest

### Community 116 - "Custom blocks"
Cohesion: 0.18
Nodes (3): 13. Data formats, BondDialogue, Household

### Community 117 - ".num"
Cohesion: 0.12
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 118 - "Character creation"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 119 - "Tier"
Cohesion: 0.11
Nodes (18): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+10 more)

### Community 121 - ".open"
Cohesion: 0.18
Nodes (15): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), item_id() (+7 more)

### Community 122 - "Bonds"
Cohesion: 0.09
Nodes (14): 12. The bond book, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+6 more)

### Community 123 - "Kind"
Cohesion: 0.12
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 124 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.33
Nodes (3): DialogueKeys, DialogueKeysTest, 10. Content plan

### Community 126 - "BondInput"
Cohesion: 0.18
Nodes (4): Bank, Facet, Pacing, Rules

### Community 127 - "4. Clan quest lines"
Cohesion: 0.40
Nodes (5): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now)

### Community 128 - "Ranks"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 129 - "creator/preview.py"
Cohesion: 0.14
Nodes (9): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street(), paste() (+1 more)

### Community 130 - ".receive"
Cohesion: 0.19
Nodes (3): Cast, Setup, VisitsTest

### Community 132 - "Player"
Cohesion: 0.15
Nodes (13): 10. Pool sizing, 11. Simulation, 12. Story-gated pools, 13. What waits, 14. Decisions and open questions, 1. Freshness: never repeat, 2. Talk budgets, 3. Beyond the budget (+5 more)

### Community 133 - "Json"
Cohesion: 0.12
Nodes (3): Names, Names, Tokens

### Community 134 - "Rng"
Cohesion: 0.08
Nodes (23): Academy blade (`combat:style.academy_blade`, weapons), Academy taijutsu (`combat:style.academy_basics`, taijutsu), Beast Fang (Four Legs) (`combat:style.beast_fang`, taijutsu), Blossom Strength (`combat:style.blossom_strength`, taijutsu), Chain arts (`combat:style.chain_arts`, weapons), Crescent Moon kenjutsu (`combat:style.crescent_moon`, weapons), Fan arts (`combat:style.fan_arts`, weapons), Gentle Fist (`combat:style.gentle_fist`, taijutsu) (+15 more)

### Community 135 - "pathlib"
Cohesion: 0.13
Nodes (9): Score, Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY, Practice (+1 more)

### Community 137 - "Kind"
Cohesion: 0.03
Nodes (57): back_fan(), bangs(), cel_box(), cel_face(), curtain(), lock(), ring_shell(), sidelocks() (+49 more)

### Community 138 - "ClanPower"
Cohesion: 0.11
Nodes (18): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+10 more)

### Community 140 - "1. The registry"
Cohesion: 0.15
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 143 - "Stretch"
Cohesion: 0.10
Nodes (5): Band, CLOSE, FAR, MID, RangeBands

### Community 146 - "ROADMAP.md"
Cohesion: 0.14
Nodes (10): Boost, Burn, Form, Kindle, Tier, BLAZE, FLAME, NONE (+2 more)

### Community 147 - "NamesTest"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 148 - "Rng"
Cohesion: 0.21
Nodes (3): Rng, Streams, StreamsTest

### Community 149 - "catalogue.py"
Cohesion: 0.13
Nodes (15): 4. Block catalogue, Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival (+7 more)

### Community 150 - ".look"
Cohesion: 0.13
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 153 - "Json"
Cohesion: 0.25
Nodes (3): Turn, Need, Tags

### Community 154 - "Rng"
Cohesion: 0.23
Nodes (4): BetaTalk, Person, Player, World

### Community 156 - "Tier"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 157 - "Look"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 158 - "ClanRelations"
Cohesion: 0.10
Nodes (21): apothecary, collectible, consumable, container, cooking.pot, curio, currency, Item catalogue (+13 more)

### Community 160 - "Memory"
Cohesion: 0.25
Nodes (3): Choices, Outfit, CreatorRulesTest

### Community 161 - "S"
Cohesion: 0.21
Nodes (4): 10. How residents address you, Names, PlayerName, NamesTest

### Community 163 - "SquadTest"
Cohesion: 0.23
Nodes (4): Mode, CLASSIC, VARIED, Unlocks

### Community 164 - ".name"
Cohesion: 0.23
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 165 - "3. Crafting"
Cohesion: 0.15
Nodes (7): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 166 - "Bonds"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 167 - "Mission catalogue"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 168 - "paper_lantern"
Cohesion: 0.14
Nodes (5): Stage, ADULT, CHILD, TEEN, Leaf

### Community 169 - "Rng"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 170 - "The village"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 173 - "Person"
Cohesion: 0.12
Nodes (6): BondBook, Fact, MemoryLine, Page, Person, 2. Schedules

### Community 174 - "kunai"
Cohesion: 0.17
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 175 - "Tier"
Cohesion: 0.35
Nodes (3): Band, Mate, SquadPlan

### Community 178 - "home/build.gradle"
Cohesion: 0.13
Nodes (3): Active, Def, StatusEffects

### Community 179 - "roster/build.gradle"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 180 - "missions/build.gradle"
Cohesion: 0.08
Nodes (24): Bestiary, groups and bosses, Bosses, `combat:boss.anbu.story_1`: Story boss (chapter anbu, level 38, anbu), `combat:boss.ch11.bandit_chief`: Bandit chief (chapter 11, level 11, beta2), `combat:boss.ch14.road_ambush`: Ambush on the road (chapter 14, level 14, beta2), `combat:boss.ch16.forest_beast`: A giant of the forest (chapter 16, level 16, beta3), `combat:boss.ch16.forest_team`: A hunting team in the forest (chapter 16, level 16, beta3), `combat:boss.ch17.prelim`: Preliminary bout (chapter 17, level 16, beta3) (+16 more)

### Community 181 - "docs.py"
Cohesion: 0.30
Nodes (11): animations_page(), bestiary_page(), clans_page(), counters(), esc(), move_rows(), signs(), styles_page() (+3 more)

### Community 184 - "SeedsTest.java"
Cohesion: 0.33
Nodes (6): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT

### Community 186 - "utility_pole"
Cohesion: 0.09
Nodes (21): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 5. Process, 6. Prototypes, 7. Effort estimate, 8. Registration notes for Phase 0, By building type, Calibration (+13 more)

### Community 188 - "kit_specialist.py"
Cohesion: 0.11
Nodes (8): bandolier(), coat_skirts(), cross_armband(), ink_stains(), scroll_tube(), seal_trim(), shirt(), strap()

### Community 190 - "Weaver"
Cohesion: 0.17
Nodes (7): Outcome, CAST, EMPTY, FIZZLE, INTERRUPTED, Result, Weaver

### Community 197 - "clans.py"
Cohesion: 0.21
Nodes (10): ct(), lesser(), area(), cone(), line(), proj(), st(), summon_entity() (+2 more)

### Community 199 - "ComboMachine"
Cohesion: 0.23
Nodes (3): ComboMachine, Context, Started

### Community 200 - "Tier"
Cohesion: 0.22
Nodes (6): Mastery, Tier, MASTERED, NOVICE, PERFECTED, PRACTICED

### Community 202 - "Animation clips"
Cohesion: 0.33
Nodes (5): Animation clips, P0, P1, P2, P3

### Community 203 - "Technique catalogue"
Cohesion: 0.15
Nodes (13): Chakra movement, Earth (9), Fire (10), Fuinjutsu (6), Genjutsu (8), Lightning (8), Medical ninjutsu (5), Neutral ninjutsu (14) (+5 more)

### Community 206 - "State"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 208 - "Tier"
Cohesion: 0.22
Nodes (7): Tier, A, B, C, D, E, S

### Community 209 - "Tier"
Cohesion: 0.25
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 213 - ".read"
Cohesion: 0.25
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 214 - "Bonds"
Cohesion: 0.40
Nodes (3): Bonds, 18. Ids for other systems, 9. Kindling Bond

### Community 215 - "6. Filler arcs"
Cohesion: 0.50
Nodes (4): 6. Filler arcs, In the beta, Later (foundation), Later one-offs (foundation)

### Community 219 - "Box"
Cohesion: 0.12
Nodes (3): strip_line(), Box, Layer

### Community 221 - "ClanProfile"
Cohesion: 0.16
Nodes (3): 18. Village scale, ClanProfile, House

### Community 223 - ".talk"
Cohesion: 0.16
Nodes (12): Conversation, Reply, Topic, 11. Open questions, 1. What makes a relationship feel real, 4. Their lives, 5. Following up, 6. Conversation (+4 more)

### Community 225 - "progression.py"
Cohesion: 0.30
Nodes (10): beta_loadout(), build(), gear_for(), melee_for(), pillar_cap(), ranks_for(), sim_builds(), slice_open() (+2 more)

### Community 226 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 227 - "Question"
Cohesion: 0.26
Nodes (3): Answer, Question, Answered

### Community 228 - "Writing dialogue for the Leaf"
Cohesion: 0.20
Nodes (10): 7. Every line serves a function, teach(), Context tags, Functions, Questions, Rules the compiler enforces, Style, The format (+2 more)

### Community 230 - "Conditions"
Cohesion: 0.25
Nodes (3): 5. Selection: the most specific line wins, Conditions, Conditions

### Community 231 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 232 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 234 - "Piece"
Cohesion: 0.33
Nodes (3): Piece, piece_corners(), world_bounds()

### Community 238 - "animations.py"
Cohesion: 0.50
Nodes (3): clip(), many(), summary()

### Community 240 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 241 - "Kind"
Cohesion: 0.50
Nodes (4): Kind, CYCLE, LINE, REPEAT

## Knowledge Gaps
- **391 isolated node(s):** `MELEE`, `THROWN`, `JUTSU`, `AREA`, `NONE` (+386 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1874 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **61 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `.receive`, `paint.py`, `AnswerTag`, `paper_lantern`, `Run`, `Person`, `Playthrough.java`, `Trait`, `Stage`, `set`, `kit_yuhi.py`, `Bond`, `.of`, `Peeve`, `Deed`, `.xpAt`, `GossipTest`, `Squad`, `SquadTest`, `.read`, `konoha/preview.py`, `.effectiveLevel`, `.person`, `Village`, `.talk`, `Question`, `Tex`, `.receive`, `Custom blocks`, `Kind`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **What connects `MELEE`, `THROWN`, `JUTSU` to the rest of the system?**
  _391 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Activity` be split into smaller, more focused modules?**
  _Cohesion score 0.07641196013289037 - nodes in this community are weakly interconnected._
- **Why does `Act` connect `Act` to `paint.py`, `paper_lantern`, `Playthrough.java`, `BondWorld`, `Personality`, `Bond`, `.of`, `Def`, `Peeve`, `Deed`, `.xpAt`, `.read`, `Plan`, `konoha/preview.py`, `Meter`, `.effectiveLevel`, `.talk`, `Question`, `Tex`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Should `VillageScaleTest` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `VillageScaleTest`, `kit_senju.py`, `kit_kurama.py`, `Kind`, `kit_uchiha.py`, `kit_kunoichi.py`, `.obj`, `Economy`, `kit_rugged.py`, `.shelf`, `kit_market.py`, `kit_kinoshita.py`, `3. Crafting`, `Roster`, `kit_hagane.py`, `.daily`, `utility_pole`, `kit_specialist.py`, `org.junit.jupiter.api.Test`, `kit_market.py`, `kit_field.py`, `Box`, `senbon`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._