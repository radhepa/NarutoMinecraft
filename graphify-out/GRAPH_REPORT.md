# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 278 files · ~657,663 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 4665 nodes · 11102 edges · 194 communities (153 shown, 41 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1300 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b81c7cb5`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- senbon
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- kit_kurama.py
- creator.py
- .classic
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
- rnd
- Tier
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
- .obj
- Village
- Person
- Bond
- Leaf
- .talk
- .read
- Def
- Levels
- Deed
- Context
- Title
- Playthrough.java
- kit_morino.py
- paint.py
- Tier
- 1. The registry
- 15. Furniture
- 4.3 The noble clans
- kit_haruno.py
- konoha/preview.py
- Items, shops and crafting
- Tier
- cel_box
- .shelf
- Heard
- Meter
- Missions
- Fixture
- Ryo
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
- 3. Crafting
- The village
- BetaTalk
- Seeds
- Plant
- Question
- Side quest secrets
- 2. Shops
- Bank
- Dialogue
- Tokens
- 4. The ryo economy
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
- QuestionsCompiledTest
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
- 6. Filler arcs
- shade
- .set
- SquadPlan
- BondInput
- RuleOfThumbTest
- S
- Mission catalogue
- SquadTest
- Result
- mission
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
- `Interior fittings` --references--> `tatami()`  [INFERRED]
  KONOHA_BUILD.md → tools/konoha/blocks.py

## Import Cycles
- None detected.

## Communities (194 total, 41 thin omitted)

### Community 0 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

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
Nodes (46): How the pieces work, back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash() (+38 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (18): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Kindling Bond, Recurring characters, Reveal pacing, Spoilers behind the roadmap's neutral wording (+10 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "creator.py"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

### Community 10 - ".classic"
Cohesion: 0.12
Nodes (7): BondBook, Fact, MemoryLine, Page, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 13 - "org.junit.jupiter.api.Test"
Cohesion: 0.04
Nodes (9): CatalogueTest, JsonTest, RyoTest, LivingTest, MoveTest, CatalogueTest, SeedsTest, SlotFillerTest (+1 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - ".person"
Cohesion: 0.06
Nodes (19): 18. The engine, Activity, BondEvent, Answer, FollowUp, Invitation, Plan, Together (+11 more)

### Community 17 - "Economy"
Cohesion: 0.08
Nodes (16): Band, Economy, End, ABANDONED, DONE, FAILED, PARTIAL, GradeRow (+8 more)

### Community 18 - "Home"
Cohesion: 0.08
Nodes (5): 17. What the map needs, Flat, Room, Home, Photo

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "mkit.py"
Cohesion: 0.17
Nodes (28): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+20 more)

### Community 21 - "Template"
Cohesion: 0.09
Nodes (9): Catalogue, Branch, Step, Template, Twist, DeskDays, Profile, Run (+1 more)

### Community 22 - "Roster"
Cohesion: 0.09
Nodes (5): Hooks for the other mods, Contribution, GrowthEvent, Grower, Roster

### Community 23 - "kit_hagane.py"
Cohesion: 0.07
Nodes (17): smithy, weapon, Weapon Shop (`weapon_shop`), hip_katana(), katana(), bracers(), crown(), harness() (+9 more)

### Community 24 - "Desk"
Cohesion: 0.11
Nodes (9): Desk, Offer, Player, Rank, A, B, C, D (+1 more)

### Community 25 - ".play"
Cohesion: 0.11
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 26 - "Category"
Cohesion: 0.07
Nodes (27): Catalog, Category, BATH, BED, DECOR, DISPLAY, FIXTURE, FLOOR (+19 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+14 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "k"
Cohesion: 0.04
Nodes (36): deep_hood(), high_collar(), hood_down(), lenses(), arm_bone(), arm_x(), belt(), collar() (+28 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.13
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Principles, Ranks and milestones, Rotating story roles (+5 more)

### Community 31 - "strip_fabric"
Cohesion: 0.03
Nodes (57): gear, leg_cloth(), shirt(), waist(), body(), arm_guards(), cargo(), gloves() (+49 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.09
Nodes (31): paste(), scene(), build(), build_all(), catalog(), hex_rgb(), json_text(), load_all_groups() (+23 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.22
Nodes (9): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap, Still open (+1 more)

### Community 35 - "sprites.py"
Cohesion: 0.07
Nodes (35): cooking.oven, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient, Market Grocer (`grocer`), material (+27 more)

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

### Community 42 - "rnd"
Cohesion: 0.03
Nodes (33): quilt(), sprigs(), burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge() (+25 more)

### Community 43 - "Tier"
Cohesion: 0.12
Nodes (9): Score, Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY, Practice (+1 more)

### Community 44 - "Playthrough"
Cohesion: 0.08
Nodes (17): 15. Pacing, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+9 more)

### Community 45 - "dialogue.py"
Cohesion: 0.13
Nodes (35): assign_ids(), build(), check_condition(), check_text(), compiled(), compiled_question(), content_key(), coverage() (+27 more)

### Community 46 - "blocks.py"
Cohesion: 0.10
Nodes (33): furniture, Furniture Shop (`furniture_shop`), Leaf Festival Stalls (`festival_stalls`), 8. Registration notes for Phase 0, By building type, Facades and shop fronts, Lanterns, Roofs (+25 more)

### Community 47 - "Niche"
Cohesion: 0.10
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
Cohesion: 0.14
Nodes (4): Day, CurveAndTierTest, RosterTest, TechniqueTest

### Community 52 - "Look"
Cohesion: 0.11
Nodes (4): 7. Locked and changeable, Look, Result, RestyleAndGrowUpTest

### Community 53 - "Personality"
Cohesion: 0.05
Nodes (27): ClanProfile, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS (+19 more)

### Community 54 - "Act"
Cohesion: 0.02
Nodes (79): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+71 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 57 - "CreatorRules"
Cohesion: 0.18
Nodes (3): 13. Code, and what waits for Phase 0, CreatorRules, Roots

### Community 58 - ".tier"
Cohesion: 0.11
Nodes (14): 11. Kindling Bond, 12. The bond book, Household, Bonfire, Flame, Kindling, Read, Sight (+6 more)

### Community 59 - "items.py"
Cohesion: 0.17
Nodes (20): art_class(), catalogue_md(), check_all(), check_loot(), compile_all(), recipe_entry(), dumps(), err() (+12 more)

### Community 61 - ".greeting"
Cohesion: 0.13
Nodes (8): 13. Data formats, 9. Mass production, The bank today, BondDialogue, DialogueKeys, BondDialogueTest, DialogueKeysTest, 10. Content plan

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Meters"
Cohesion: 0.09
Nodes (8): Know, Memory, Meters, Source, HEARD, SEEN, SELF, TOLD

### Community 66 - "Village"
Cohesion: 0.04
Nodes (24): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+16 more)

### Community 67 - "Person"
Cohesion: 0.06
Nodes (6): 20. What the roadmap asks of bonds, 5. Personality, Person, Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (5): Bond, BondConditions, BondWeb, Highlight, Outcome

### Community 69 - "Leaf"
Cohesion: 0.20
Nodes (3): ConflictTest, Leaf, MemoryTest

### Community 70 - ".talk"
Cohesion: 0.15
Nodes (7): 6. Conversations, Conversation, Reply, Topic, LifeEvents, News, 6. Conversation

### Community 71 - ".read"
Cohesion: 0.12
Nodes (11): Answer, Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS (+3 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.18
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 75 - "Context"
Cohesion: 0.15
Nodes (9): Context, Line, Overheard, Said, Talk, Why, BUDGET, EXHAUSTED (+1 more)

### Community 76 - "Title"
Cohesion: 0.16
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 77 - "Playthrough.java"
Cohesion: 0.06
Nodes (6): Stage, ADULT, CHILD, TEEN, Schedule, SampleQuestions

### Community 78 - "kit_morino.py"
Cohesion: 0.14
Nodes (6): back_crest(), clipped(), coat_skirts(), head_cloth(), nape_hem(), forehead_protector()

### Community 79 - "paint.py"
Cohesion: 0.06
Nodes (22): puff(), drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+14 more)

### Community 80 - "Tier"
Cohesion: 0.20
Nodes (7): Tier, A, B, C, D, E, S

### Community 81 - "1. The registry"
Cohesion: 0.22
Nodes (9): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+1 more)

### Community 82 - "15. Furniture"
Cohesion: 0.40
Nodes (5): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now)

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - "konoha/preview.py"
Cohesion: 0.14
Nodes (15): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+7 more)

### Community 86 - "Items, shops and crafting"
Cohesion: 0.25
Nodes (6): 5. Item art, 6. Coordination, 7. What waits for Phase 0, 8. Open questions, Contents, Items, shops and crafting

### Community 87 - "Tier"
Cohesion: 0.25
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 88 - "cel_box"
Cohesion: 0.03
Nodes (61): Shared helpers, back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock() (+53 more)

### Community 89 - ".shelf"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 90 - "Heard"
Cohesion: 0.11
Nodes (4): 4. Storage, Heard, Speaker, QuestionsAndLedgerTest

### Community 91 - "Meter"
Cohesion: 0.10
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 96 - "Side quests"
Cohesion: 0.25
Nodes (8): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 9. Open questions, Contents, Side quests

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "json"
Cohesion: 0.18
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "compose.py"
Cohesion: 0.48
Nodes (5): compose(), flush_kernel(), flush_template(), fail(), main()

### Community 104 - "Question"
Cohesion: 0.15
Nodes (3): Turn, Need, Tags

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
Cohesion: 0.20
Nodes (4): Rest, Rested, ComfortTest, RestTest

### Community 109 - "Run"
Cohesion: 0.06
Nodes (5): 14. Save format and versioning, Departure, Squad, SaveFormatTest, Run

### Community 110 - "Character creation"
Cohesion: 0.10
Nodes (20): 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 1 Name, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Prices"
Cohesion: 0.17
Nodes (3): Pawn, Prices, PricesTest

### Community 114 - "VisitsTest"
Cohesion: 0.22
Nodes (3): Cast, Setup, VisitsTest

### Community 115 - "render_kit.py"
Cohesion: 0.15
Nodes (8): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 116 - ".name"
Cohesion: 0.06
Nodes (20): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, Power, EMBER_LINK (+12 more)

### Community 117 - "3. Crafting"
Cohesion: 0.29
Nodes (7): 3.1 Stations, 3.2 Recipes, 3.3 Unlocks, 3.4 Quality grades, 3.5 Repair and upgrade, 3.6 Where materials come from, 3. Crafting

### Community 118 - "The village"
Cohesion: 0.29
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 119 - "BetaTalk"
Cohesion: 0.19
Nodes (4): BetaTalk, Person, Player, World

### Community 120 - "Seeds"
Cohesion: 0.13
Nodes (3): Rng, Seeds, Comfort

### Community 121 - "Plant"
Cohesion: 0.12
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 122 - "Question"
Cohesion: 0.21
Nodes (4): 8. Questions and choices, Answer, Question, Answered

### Community 123 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 124 - "2. Shops"
Cohesion: 0.40
Nodes (5): 2.1 How buying works, 2.2 The shops, 2.3 Part-time jobs, 2.4 Interiors (blocks asked of the Konoha session), 2. Shops

### Community 125 - "Bank"
Cohesion: 0.18
Nodes (5): Bank, Facet, Pacing, Rules, Tier

### Community 126 - "Dialogue"
Cohesion: 0.12
Nodes (14): 10. Pool sizing, 11. Simulation, 12. Story-gated pools, 13. What waits, 14. Open questions, 1. Freshness: never repeat, 2. Talk budgets, 3. Beyond the budget (+6 more)

### Community 128 - "4. The ryo economy"
Cohesion: 0.50
Nodes (4): 4.1 A closed loop, 4.2 Sinks and inflation guards, 4.3 The simulation, 4. The ryo economy

### Community 131 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 133 - "Writing dialogue for the Leaf"
Cohesion: 0.25
Nodes (8): Context tags, Functions, Questions, Rules the compiler enforces, Style, The format, Voices, Writing dialogue for the Leaf

### Community 134 - ".answer"
Cohesion: 0.17
Nodes (4): Answered, Outcome, Questions, QuestionsTest

### Community 135 - "Home"
Cohesion: 0.08
Nodes (22): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 1. Design rules, 20. By beta slice (+14 more)

### Community 138 - "creator/preview.py"
Cohesion: 0.16
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 139 - ".receive"
Cohesion: 0.23
Nodes (5): 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest

### Community 141 - "Ranks"
Cohesion: 0.11
Nodes (17): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+9 more)

### Community 142 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 143 - "Streams"
Cohesion: 0.21
Nodes (3): Rng, Streams, StreamsTest

### Community 149 - "Outcome"
Cohesion: 0.33
Nodes (6): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT

### Community 150 - "pathlib"
Cohesion: 0.12
Nodes (4): build(), build(), flat(), build()

### Community 151 - "ClanPower"
Cohesion: 0.19
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 152 - "Kind"
Cohesion: 0.50
Nodes (4): Kind, CYCLE, LINE, REPEAT

### Community 153 - "Every building"
Cohesion: 0.11
Nodes (18): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+10 more)

### Community 155 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 156 - "Keepsake"
Cohesion: 0.12
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 157 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 158 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 159 - "Item catalogue"
Cohesion: 0.09
Nodes (22): apothecary, collectible, consumable, container, cooking.pot, curio, currency, Item catalogue (+14 more)

### Community 160 - "Konoha: the build plan"
Cohesion: 0.12
Nodes (17): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 4. Block catalogue, 5. Process, 6. Prototypes, 7. Effort estimate, Calibration, Contents (+9 more)

### Community 162 - "catalogue.py"
Cohesion: 0.23
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 163 - ".choices"
Cohesion: 0.25
Nodes (3): Choices, Outfit, CreatorRulesTest

### Community 164 - "NamesTest"
Cohesion: 0.21
Nodes (4): 10. How residents address you, Names, PlayerName, NamesTest

### Community 165 - "Stretch"
Cohesion: 0.13
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 167 - ".chains"
Cohesion: 0.23
Nodes (4): Mode, CLASSIC, VARIED, Unlocks

### Community 168 - "Shops"
Cohesion: 0.07
Nodes (30): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), Exam-Week Stalls (`exam_stalls`), gift (+22 more)

### Community 169 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 170 - "Restyle"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 171 - "Custom blocks"
Cohesion: 0.12
Nodes (15): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+7 more)

### Community 172 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 173 - ".run"
Cohesion: 0.22
Nodes (6): 19. Pacing, FirstFifteenHours, Result, Slice, Snapshot, FirstFifteenHoursTest

### Community 176 - "6. Filler arcs"
Cohesion: 0.50
Nodes (4): 6. Filler arcs, In the beta, Later (foundation), Later one-offs (foundation)

### Community 178 - ".set"
Cohesion: 0.12
Nodes (6): FurnitureSet, Tidiness, LIVED_IN, MESSY, TIDY, CatalogTest

### Community 179 - "SquadPlan"
Cohesion: 0.35
Nodes (3): Band, Mate, SquadPlan

### Community 184 - "S"
Cohesion: 0.18
Nodes (7): 6. Squad missions, travel(), go(), merchant_camp_talk(), S, talk(), twist()

### Community 186 - "Mission catalogue"
Cohesion: 0.25
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 193 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

## Knowledge Gaps
- **342 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+337 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1596 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **41 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `Conflict`, `.answer`, `.classic`, `.receive`, `org.junit.jupiter.api.Test`, `.person`, `Playthrough`, `Stage`, `.tier`, `SquadTest`, `map`, `.greeting`, `Village`, `Person`, `Bond`, `Leaf`, `.talk`, `.read`, `Deed`, `Title`, `Playthrough.java`, `GossipTest`, `VillageSim.java`, `Run`, `VisitsTest`, `Seeds`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _342 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `senbon`, `kit_uchiha.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `kit_kunoichi.py`, `kit_suzuran.py`, `kit_rugged.py`, `kit_hagane.py`, `kit_market.py`, `kit_kinoshita.py`, `strip_fabric`, `Shops`, `rnd`, `Custom blocks`, `kit_morino.py`, `paint.py`, `kit_haruno.py`, `cel_box`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.10526315789473684 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `senbon`, `kit_uchiha.py`, `kit_senju.py`, `kit_kurama.py`, `kit_kunoichi.py`, `kit_suzuran.py`, `kit_rugged.py`, `kit_hagane.py`, `kit_market.py`, `kit_kinoshita.py`, `k`, `strip_fabric`, `Shops`, `rnd`, `Custom blocks`, `Box`, `kit_morino.py`, `paint.py`, `kit_haruno.py`, `cel_box`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13978494623655913 - nodes in this community are weakly interconnected._