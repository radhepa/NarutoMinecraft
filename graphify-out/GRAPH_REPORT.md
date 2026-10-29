# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 329 files · ~746,912 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 5414 nodes · 12719 edges · 229 communities (175 shown, 54 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1394 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8b400e5b`
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
- cel_box
- creator.py
- kit_uzumaki.py
- Wallet
- Economy
- kit_suzuran.py
- 7. Systems in the beta
- .person
- Shops
- .answer
- k
- items.py
- mkit.py
- Category
- Template
- .daily
- Desk
- fabric
- dialogue.py
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
- later_ranks.py
- kit_hagane.py
- .person
- paint.py
- CreatorRules
- Mood
- Template
- 4.3 The noble clans
- kit_sarutobi.py
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
- SignBook
- Rank
- Bank
- 15. Furniture
- Naruto Minecraft
- render_kit.py
- VisitsTest
- .num
- Dialogue
- Names
- Styles and combo trees
- sys
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
- load_clans
- Rng
- Act.java
- catalogue.py
- main
- rot_matrix
- Tier
- BondInput
- Pantry
- .run
- Json
- Rng
- S
- Kind
- SquadPlan
- .share
- RuleOfThumbTest
- StatusEffects
- Mission catalogue
- Bosses
- docs.py
- Json
- MoveTest
- leaf_block.py
- Result
- 2. The Mission Desk
- mission
- 8. The beta, chapter by chapter
- Pool
- Weaver
- 9. Delivery plan
- clans.py
- Chakra
- build
- Tier
- kit_yamanaka.py
- COMBAT.md
- Technique catalogue
- Technique
- State
- SquadTest
- Tier
- Tier
- EmberLink
- Rng
- chain
- Side quest secrets
- Combat
- 6. Filler arcs
- weapons.py
- Tags
- common.py
- Writing dialogue for the Leaf
- Error
- build
- Cooldowns
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
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java
- `6. Coordination` --references--> `tatami()`  [INFERRED]
  ITEMS.md → tools/konoha/blocks.py

## Import Cycles
- None detected.

## Communities (229 total, 54 thin omitted)

### Community 0 - "set"
Cohesion: 0.09
Nodes (4): Hooks for the other mods, GrowthEvent, Grower, Roster

### Community 1 - "kit_uchiha.py"
Cohesion: 0.07
Nodes (15): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar(), arm_crest() (+7 more)

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

### Community 6 - "k"
Cohesion: 0.03
Nodes (40): deep_hood(), high_collar(), hood_down(), lenses(), back_crest(), drawstrings(), forearm_wraps(), holster() (+32 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (18): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Kindling Bond, Recurring characters, Reveal pacing, Spoilers behind the roadmap's neutral wording (+10 more)

### Community 8 - "cel_box"
Cohesion: 0.03
Nodes (42): back_fan(), bangs(), cel_box(), curtain(), lock(), sidelocks(), tie(), flick() (+34 more)

### Community 9 - "creator.py"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

### Community 11 - "kit_uzumaki.py"
Cohesion: 0.09
Nodes (12): arm_bone(), arm_x(), armband(), roll(), bun(), clip(), crest_patch(), seal_script() (+4 more)

### Community 12 - "Wallet"
Cohesion: 0.05
Nodes (33): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+25 more)

### Community 13 - "Economy"
Cohesion: 0.07
Nodes (17): Band, Economy, End, ABANDONED, DONE, FAILED, PARTIAL, GradeRow (+9 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - ".person"
Cohesion: 0.06
Nodes (25): 6. Conversations, 18. The engine, Activity, Conversation, Reply, Topic, Schedule, Answer (+17 more)

### Community 17 - "Shops"
Cohesion: 0.07
Nodes (31): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), Exam-Week Stalls (`exam_stalls`), gift (+23 more)

### Community 18 - ".answer"
Cohesion: 0.14
Nodes (7): Answer, Question, Answered, Outcome, Questions, QuestionsCompiledTest, QuestionsTest

### Community 19 - "k"
Cohesion: 0.03
Nodes (59): braid(), cel_face(), ring_shell(), quilt(), crown(), claw_marks(), fang(), fang_small() (+51 more)

### Community 20 - "items.py"
Cohesion: 0.17
Nodes (20): art_class(), catalogue_md(), check_all(), check_loot(), compile_all(), recipe_entry(), dumps(), err() (+12 more)

### Community 21 - "mkit.py"
Cohesion: 0.19
Nodes (16): buy(), choose(), chose(), collect(), count(), end(), merchant_camp_talk(), one_of() (+8 more)

### Community 22 - "Category"
Cohesion: 0.06
Nodes (28): Catalog, FurnitureSet, Category, BATH, BED, DECOR, DISPLAY, FIXTURE (+20 more)

### Community 23 - "Template"
Cohesion: 0.15
Nodes (5): Catalogue, DeskDays, Profile, Run, SimulationTest

### Community 24 - ".daily"
Cohesion: 0.16
Nodes (4): Friends, Day, Visit, Visits

### Community 25 - "Desk"
Cohesion: 0.11
Nodes (7): Desk, Mode, CLASSIC, VARIED, Offer, Player, Unlocks

### Community 26 - "fabric"
Cohesion: 0.05
Nodes (23): arm_cloth(), bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta() (+15 more)

### Community 27 - "dialogue.py"
Cohesion: 0.31
Nodes (18): check_condition(), check_text(), _excludes_child(), fail(), lint(), load_all(), parse_answer(), parse_heading() (+10 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (13): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+5 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.14
Nodes (14): How to read this bible, 2. Decisions, 5. Data formats built for the whole story, Authoring tools, Chapters and arcs, Conditions and actions, Names rolled per save, Principles (+6 more)

### Community 31 - "Fighter"
Cohesion: 0.08
Nodes (11): Battle, Plan, Plan, Plan, Plan, Chain, Event, Plan (+3 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.18
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+8 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.22
Nodes (9): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap, Still open (+1 more)

### Community 35 - "Talk"
Cohesion: 0.16
Nodes (4): Line, Turn, Overheard, Talk

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "CombatData"
Cohesion: 0.07
Nodes (14): Boss, Build, CombatData, Enemy, Phase, Weapon, Difficulty, Balance (+6 more)

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
Cohesion: 0.13
Nodes (6): gourd(), lames(), puff(), shoku_disc(), snack_pouch(), sode()

### Community 43 - "kit_kunoichi.py"
Cohesion: 0.05
Nodes (25): gear, smithy, weapon, Weapon Shop (`weapon_shop`), arm_guards(), hip_katana(), katana(), shin_guards() (+17 more)

### Community 44 - "Playthrough"
Cohesion: 0.05
Nodes (19): 15. Pacing, BondEvent, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER (+11 more)

### Community 45 - "fabric"
Cohesion: 0.03
Nodes (48): Shared helpers, leg_cloth(), shirt(), waist(), belt(), body(), collar(), cargo() (+40 more)

### Community 47 - ".of"
Cohesion: 0.12
Nodes (7): Score, Practice, Session, Rest, Rested, ComfortTest, RestTest

### Community 48 - "Meters"
Cohesion: 0.10
Nodes (7): Memory, Meters, Source, HEARD, SEEN, SELF, TOLD

### Community 49 - "Box"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 50 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 51 - ".xpAt"
Cohesion: 0.18
Nodes (3): Day, RosterTest, TechniqueTest

### Community 52 - "Home"
Cohesion: 0.08
Nodes (22): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 1. Design rules, 20. By beta slice (+14 more)

### Community 53 - "Home"
Cohesion: 0.06
Nodes (9): 17. What the map needs, Flat, Room, Home, Tidiness, LIVED_IN, MESSY, TIDY (+1 more)

### Community 54 - "Act"
Cohesion: 0.02
Nodes (79): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+71 more)

### Community 55 - "Stage"
Cohesion: 0.05
Nodes (14): 10. Romance and family (after the beta), Conflict, Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST (+6 more)

### Community 56 - "BondWorld"
Cohesion: 0.06
Nodes (5): 12. The bond book, BondEffects, BondWorld, LifeEvents, Standing

### Community 57 - "VarietyGuard"
Cohesion: 0.11
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 58 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 59 - "Look"
Cohesion: 0.07
Nodes (11): GrowUp, Look, Restyle, Result, Venue, BARBER, HOME, LOCKED (+3 more)

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.04
Nodes (13): DataTest, ResourcesTest, 19. Pacing, CatalogueTest, JsonTest, RyoTest, CatalogTest, LivingTest (+5 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Every building"
Cohesion: 0.11
Nodes (18): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+10 more)

### Community 65 - ".obj"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 66 - "build.py"
Cohesion: 0.21
Nodes (9): all_techniques(), build(), check(), statuses_in(), fold(), main(), public_text_hashes(), short() (+1 more)

### Community 67 - "Box"
Cohesion: 0.12
Nodes (3): strip_line(), Box, Layer

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (4): Bond, BondConditions, BondWeb, News

### Community 70 - "Move"
Cohesion: 0.06
Nodes (6): ComboMachine, Context, Started, Move, Style, ComboAndStatusTest

### Community 71 - "blocks.py"
Cohesion: 0.08
Nodes (33): furniture, Furniture Shop (`furniture_shop`), 6. Prototypes, Facades and shop fronts, Interior fittings, Lanterns, Roofs, Streets (+25 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.15
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 75 - "later_ranks.py"
Cohesion: 0.26
Nodes (15): 4.1 The format, Code by mod, The quest format, anchor(), craft(), defeat(), deliver(), enemy_group() (+7 more)

### Community 76 - "kit_hagane.py"
Cohesion: 0.11
Nodes (9): spike(), bracers(), crown(), harness(), mace(), plate(), burst(), pineapple() (+1 more)

### Community 78 - ".person"
Cohesion: 0.08
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 79 - "paint.py"
Cohesion: 0.03
Nodes (38): checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri(), kyahan() (+30 more)

### Community 80 - "CreatorRules"
Cohesion: 0.11
Nodes (8): Choices, CreatorRules, Outfit, Roots, LifeRoll, Rolled, Data, LifeRollTest

### Community 81 - "Mood"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - "Template"
Cohesion: 0.18
Nodes (4): Branch, Step, Template, Twist

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_sarutobi.py"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 85 - "HandSign"
Cohesion: 0.09
Nodes (14): HandSign, BIRD, BOAR, DOG, DRAGON, HARE, HORSE, MONKEY (+6 more)

### Community 86 - "Personality"
Cohesion: 0.05
Nodes (26): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+18 more)

### Community 87 - "Clan techniques and kekkei genkai"
Cohesion: 0.08
Nodes (26): Aburame (noble), Akimichi (noble), Clan techniques and kekkei genkai, Gekko (noble), Hagane (minor), Haruno (minor), Hatake (noble), Hyuga (noble) (+18 more)

### Community 89 - "konoha/preview.py"
Cohesion: 0.16
Nodes (14): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+6 more)

### Community 90 - ".tier"
Cohesion: 0.11
Nodes (13): 11. Kindling Bond, Household, Bonfire, Flame, Kindling, Read, Sight, Thread (+5 more)

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Missions"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Fixture"
Cohesion: 0.10
Nodes (14): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+6 more)

### Community 94 - "Village"
Cohesion: 0.04
Nodes (20): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+12 more)

### Community 96 - "Side quests"
Cohesion: 0.25
Nodes (8): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 9. Open questions, Contents, Side quests

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - ".shelf"
Cohesion: 0.13
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Missions"
Cohesion: 0.11
Nodes (19): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 3.1 Pay and XP bands, 3.2 Client standing and village reputation, 3. Ranks and the economy, 4.2 D rank: village life with a twist (41) (+11 more)

### Community 101 - ".classic"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "Label"
Cohesion: 0.18
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 104 - "leaf_block.py"
Cohesion: 0.16
Nodes (3): Rng, Seeds, StreamsTest

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
Cohesion: 0.11
Nodes (4): 4. Storage, Heard, Speaker, QuestionsAndLedgerTest

### Community 109 - ".person"
Cohesion: 0.14
Nodes (6): 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest, BondFriends

### Community 110 - "Catalogue"
Cohesion: 0.16
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Character creation"
Cohesion: 0.07
Nodes (25): 10. How residents address you, 11. Data, 12. Clan-born play: a later option, 13. Code, and what waits for Phase 0, 14. Open questions, 1. At a glance, 1 Name, 2 Body (+17 more)

### Community 114 - "ClanPower"
Cohesion: 0.15
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 115 - "Prices"
Cohesion: 0.15
Nodes (3): Pawn, Prices, PricesTest

### Community 116 - ".talk"
Cohesion: 0.14
Nodes (5): 13. Data formats, BondDialogue, DialogueKeys, BondDialogueTest, 10. Content plan

### Community 117 - "Plant"
Cohesion: 0.13
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
Cohesion: 0.05
Nodes (14): 20. What the roadmap asks of bonds, 5. Personality, 8. The village talks, BondBook, Fact, MemoryLine, Page, ConditionsAndEffectsTest (+6 more)

### Community 125 - "Rank"
Cohesion: 0.19
Nodes (6): Rank, A, B, C, D, S

### Community 126 - "Bank"
Cohesion: 0.14
Nodes (5): Bank, Facet, Pacing, Rules, Tier

### Community 127 - "15. Furniture"
Cohesion: 0.40
Nodes (5): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now)

### Community 128 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 129 - "render_kit.py"
Cohesion: 0.09
Nodes (10): build(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street() (+2 more)

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

### Community 135 - "sys"
Cohesion: 0.21
Nodes (6): compose(), flush_kernel(), flush_template(), fail(), main(), build()

### Community 136 - "progression.py"
Cohesion: 0.30
Nodes (10): beta_loadout(), build(), gear_for(), melee_for(), pillar_cap(), ranks_for(), sim_builds(), slice_open() (+2 more)

### Community 137 - "stamp"
Cohesion: 0.04
Nodes (34): How the pieces work, stamp(), crescent(), sword_strap(), decal(), shoulder_decal(), slanted_protector(), crest() (+26 more)

### Community 138 - "Konoha: the build plan"
Cohesion: 0.12
Nodes (17): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents (+9 more)

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
Cohesion: 0.11
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 149 - "Custom blocks"
Cohesion: 0.12
Nodes (16): Academy, Residence, hospital, stadium, By building type, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival (+8 more)

### Community 150 - "Keepsake"
Cohesion: 0.13
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 153 - "Question"
Cohesion: 0.21
Nodes (4): 8. Questions and choices, Answer, Question, Answered

### Community 154 - "BetaTalk"
Cohesion: 0.12
Nodes (15): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT, Said, Why (+7 more)

### Community 156 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 157 - "AgeStage"
Cohesion: 0.11
Nodes (5): AgeStage, ADULT, CHILD, TEEN, AgeStageTest

### Community 158 - "Item catalogue"
Cohesion: 0.09
Nodes (22): apothecary, collectible, consumable, container, cooking.pot, curio, currency, Item catalogue (+14 more)

### Community 161 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 163 - "Act.java"
Cohesion: 0.20
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 164 - "catalogue.py"
Cohesion: 0.23
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 165 - "main"
Cohesion: 0.20
Nodes (9): coverage(), main(), matches(), near_duplicates(), render(), report(), shingles(), stats() (+1 more)

### Community 166 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 167 - "Tier"
Cohesion: 0.22
Nodes (6): Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY

### Community 168 - "BondInput"
Cohesion: 0.22
Nodes (3): 9. Data, code and Phase 0, BondInput, Day

### Community 169 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 170 - ".run"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 173 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), go(), S, twist()

### Community 174 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 175 - "SquadPlan"
Cohesion: 0.35
Nodes (3): Band, Mate, SquadPlan

### Community 178 - "StatusEffects"
Cohesion: 0.13
Nodes (3): Active, Def, StatusEffects

### Community 179 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 180 - "Bosses"
Cohesion: 0.09
Nodes (22): Bosses, `combat:boss.anbu.story_1`: Story boss (chapter anbu, level 38, anbu), `combat:boss.ch11.bandit_chief`: Bandit chief (chapter 11, level 11, beta2), `combat:boss.ch14.road_ambush`: Ambush on the road (chapter 14, level 14, beta2), `combat:boss.ch16.forest_beast`: A giant of the forest (chapter 16, level 16, beta3), `combat:boss.ch16.forest_team`: A hunting team in the forest (chapter 16, level 16, beta3), `combat:boss.ch17.prelim`: Preliminary bout (chapter 17, level 16, beta3), `combat:boss.ch19.finals`: Finals bout (chapter 19, level 18, beta3) (+14 more)

### Community 181 - "docs.py"
Cohesion: 0.23
Nodes (14): 7. Every line serves a function, animations_page(), bestiary_page(), clans_page(), counters(), esc(), move_rows(), signs() (+6 more)

### Community 186 - "2. The Mission Desk"
Cohesion: 0.29
Nodes (7): 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back, 2.5 Failure, partial success and abandonment, 2.6 Grades, 2. The Mission Desk

### Community 187 - "mission"
Cohesion: 0.40
Nodes (3): _key(), mission(), outcome()

### Community 188 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 190 - "Weaver"
Cohesion: 0.17
Nodes (7): Outcome, CAST, EMPTY, FIZZLE, INTERRUPTED, Result, Weaver

### Community 191 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 197 - "clans.py"
Cohesion: 0.21
Nodes (10): ct(), lesser(), area(), cone(), line(), proj(), st(), summon_entity() (+2 more)

### Community 199 - "build"
Cohesion: 0.29
Nodes (7): assign_ids(), build(), compiled(), compiled_question(), content_key(), family(), specificity()

### Community 200 - "Tier"
Cohesion: 0.18
Nodes (6): Mastery, Tier, MASTERED, NOVICE, PERFECTED, PRACTICED

### Community 201 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 202 - "COMBAT.md"
Cohesion: 0.17
Nodes (7): Animation clips, P0, P1, P2, P3, Bestiary, groups and bosses, Groups

### Community 203 - "Technique catalogue"
Cohesion: 0.15
Nodes (13): Chakra movement, Earth (9), Fire (10), Fuinjutsu (6), Genjutsu (8), Lightning (8), Medical ninjutsu (5), Neutral ninjutsu (14) (+5 more)

### Community 206 - "State"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 208 - "Tier"
Cohesion: 0.20
Nodes (7): Tier, A, B, C, D, E, S

### Community 209 - "Tier"
Cohesion: 0.20
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 212 - "chain"
Cohesion: 0.40
Nodes (3): Board missions, chain(), mesh_arms()

### Community 213 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 214 - "Combat"
Cohesion: 0.10
Nodes (18): Bonds, 10. Enemies, 11. Difficulty and feel, 12. Progression, 13. The beta loadout, 16. Animations, 17. What waits for Phase 0, 18. Ids for other systems (+10 more)

### Community 215 - "6. Filler arcs"
Cohesion: 0.50
Nodes (4): 6. Filler arcs, In the beta, Later (foundation), Later one-offs (foundation)

### Community 221 - "Writing dialogue for the Leaf"
Cohesion: 0.29
Nodes (7): Context tags, Questions, Rules the compiler enforces, Style, The format, Voices, Writing dialogue for the Leaf

### Community 224 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 233 - "animations.py"
Cohesion: 0.50
Nodes (3): clip(), many(), summary()

### Community 236 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 237 - "Kind"
Cohesion: 0.50
Nodes (4): Kind, CYCLE, LINE, REPEAT

## Knowledge Gaps
- **391 isolated node(s):** `MELEE`, `THROWN`, `JUTSU`, `AREA`, `NONE` (+386 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1875 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **54 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `VisitsTest`, `.person`, `.answer`, `Act.java`, `Playthrough`, `Playthrough.java`, `Stage`, `FirstFifteenHours.java`, `list`, `Bond`, `.classmate`, `Deed`, `map`, `.person`, `SquadTest`, `.tier`, `Village`, `.person`, `.talk`, `.classic`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **What connects `MELEE`, `THROWN`, `JUTSU` to the rest of the system?**
  _391 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `set` be split into smaller, more focused modules?**
  _Cohesion score 0.09309309309309309 - nodes in this community are weakly interconnected._
- **Why does `Act` connect `Act` to `list`, `Act.java`, `Bond`, `.classmate`, `Def`, `Deed`, `map`, `.person`, `Playthrough.java`, `Meters`, `.person`, `.answer`, `Personality`, `Stage`, `BondWorld`, `.tier`, `Meter`, `FirstFifteenHours.java`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06756756756756757 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `k` to `kit_uchiha.py`, `kit_senju.py`, `Box`, `cel_box`, `stamp`, `kit_akimichi.py`, `kit_kunoichi.py`, `kit_hagane.py`, `fabric`, `kit_uzumaki.py`, `paint.py`, `kit_suzuran.py`, `Shops`, `k`, `kit_sarutobi.py`, `Custom blocks`, `fabric`, `kit_kinoshita.py`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._