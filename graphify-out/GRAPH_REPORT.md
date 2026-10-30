# Graph Report - NarutoMinecraft-names  (2026-10-30)

## Corpus Check
- 445 files · ~1,009,944 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 32 file(s) not represented in the graph (top: .tsv 23, (none) 4, .properties 2)

## Summary
- 6941 nodes · 16050 edges · 309 communities (214 shown, 95 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 1469 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5b62fe0a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Roster
- kit_uchiha.py
- Clans
- list
- render.py
- living_eyes.py
- ShinobiLife
- Story bible
- cel_box
- creator.py
- ShinobiProgression.java
- kit_kurama.py
- Items, shops and crafting
- Economy
- kit_suzuran.py
- 7. Systems in the beta
- .friends
- Shops
- .answer
- k
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
- load_clans
- 11. Later systems
- Shinobi Modpack: roadmap
- Context
- org.spongepowered.asm.mixin.Mixin
- .of
- Balance
- .hit
- rnd
- sprites.py
- kit_hagane.py
- Run
- solid
- Bonds
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
- VarietyGuard
- Plan
- Restyle
- net.minecraft.server.level.ServerLevel
- org.junit.jupiter.api.Test
- .name
- Every building
- kit_academy.py
- .play
- build.py
- net.minecraft.server.level.ServerPlayer
- Bond
- Pillar
- Move
- blocks.py
- Def
- com.mojang.serialization.Codec
- Deed
- kit_tobari.py
- .read
- paint.py
- Squad
- Label
- 4.3 The noble clans
- .person
- HandSign
- kit_kunoichi.py
- Clan techniques and kekkei genkai
- .obj
- konoha/preview.py
- .classic
- Meter
- Title
- Niche
- World
- ROADMAP.md
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
- AssignmentsMixin.java
- Catalogue
- 4. Clan quest lines
- Character creation
- ClanPower
- Prices
- Flat
- Plant
- The village
- Ranks
- VillageSim.java
- missions.py
- Daily.java
- SignsTest
- Person
- net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext
- Bank
- Fighter
- VisitsTest
- kit_specialist.py
- wardrobe.py
- .num
- Dialogue
- Names
- Styles and combo trees
- compose.py
- Code by mod
- fabric
- Konoha: the build plan
- DeskTest
- creator/preview.py
- Json
- Nature
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
- kit_senju.py
- Item catalogue
- Grades
- .choices
- Power
- Rng
- Playthrough.java
- sys
- pathlib
- Rounds
- argparse
- kit_haruno.py
- Experience
- .run
- Json
- Rng
- progression.py
- SquadTest
- .strings
- Life together
- RuleOfThumbTest
- StatusEffects
- AcademyGameTest.java
- Bosses
- docs.py
- Json
- KonohaBlocks.java
- Result
- GossipTest
- animations.py
- .remember
- main
- Weaver
- NamesTest
- clans.py
- .classmate
- Personality
- Tier
- Animation clips
- validate_catalog
- Technique catalogue
- CombatData
- End
- Story check handoff
- leaf_block.py
- Tier
- CreatorRules
- EmberLink
- Rng
- 13.5 Phase cards
- Pantry
- Combat
- weapons.py
- Tags
- Mission catalogue
- json
- Village
- Arc
- kit_tsuchigumo.py
- PlayerLooks
- Rng
- .sensei
- Outcome
- Dialogue brief
- Dialogue brief
- AuthoringTest
- .set
- `role:squad3_a`: the planner
- `role:squad4_a`: the heir
- 1. `twist.traitor`: the voice
- Dialogue brief
- The world behind the story
- Dialogue briefs
- Dialogue brief
- Arc
- Memory
- Dialogue brief
- Dialogue brief
- Dialogue brief
- Dialogue brief
- Look
- RadialScreen
- .runTest
- Act
- Dialogue brief
- Minor recurring roles
- Dialogue brief
- family_names
- Story flags
- Dialogue brief
- Dialogue brief
- Dialogue brief
- Dialogue brief
- Dialogue brief
- SeedsTest
- Arc 6 (optional): Night Watch (ANBU branch, N1 to N7)
- How the story uses the systems
- Journal
- `role:fallen_parent`
- ResidentNames
- Kind
- Why

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 206 edges
3. `solid()` - 151 edges
4. `Act` - 129 edges
5. `fabric()` - 108 edges
6. `Bond` - 68 edges
7. `Home` - 68 edges
8. `Fighter` - 63 edges
9. `Village` - 63 edges
10. `Battle` - 59 edges

## Surprising Connections (you probably didn't know these)
- `4. Taijutsu` --references--> `Move`  [INFERRED]
  docs/COMBAT.md → combat/core/src/main/java/dev/shinobi/combat/Move.java
- `13.3 Phase order and gate evidence` --references--> `StateGameTest`  [INFERRED]
  ROADMAP.md → core/src/gametest/java/dev/shinobi/core/StateGameTest.java
- `1.7 Gift tags` --references--> `Personality`  [INFERRED]
  ITEMS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Personality.java
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java

## Import Cycles
- None detected.

## Communities (309 total, 95 thin omitted)

### Community 0 - "Roster"
Cohesion: 0.08
Nodes (5): Hooks for the other mods, Contribution, GrowthEvent, Grower, Roster

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (10): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Reference images, clan_bottoms(), clan_resident() (+2 more)

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (19): new_canvas(), backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font() (+11 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "ShinobiLife"
Cohesion: 0.09
Nodes (4): ShinobiLife, Sold, Offer, ShopMenu

### Community 7 - "Story bible"
Cohesion: 0.12
Nodes (16): Boss secrets, Clan lines, District quests and one-offs, Filler arcs, Keys read by tools, Mission secrets, Recurring characters, Reveal pacing (+8 more)

### Community 8 - "cel_box"
Cohesion: 0.04
Nodes (38): back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock(), ring_shell() (+30 more)

### Community 9 - "creator.py"
Cohesion: 0.11
Nodes (18): check(), _hash(), hash64(), main(), _mix(), outputs(), Rng, roll_look() (+10 more)

### Community 10 - "ShinobiProgression.java"
Cohesion: 0.03
Nodes (4): ShinobiCombat, Saved, ShinobiCore, ShinobiVillage

### Community 11 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 12 - "Items, shops and crafting"
Cohesion: 0.07
Nodes (30): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+22 more)

### Community 13 - "Economy"
Cohesion: 0.09
Nodes (12): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+4 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+9 more)

### Community 16 - ".friends"
Cohesion: 0.09
Nodes (13): Plan, 6. Conversations, Activity, Conversation, Reply, Topic, Answer, Invitation (+5 more)

### Community 17 - "Shops"
Cohesion: 0.07
Nodes (30): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), Exam-Week Stalls (`exam_stalls`), gift (+22 more)

### Community 18 - ".answer"
Cohesion: 0.08
Nodes (15): Answer, Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS (+7 more)

### Community 19 - "k"
Cohesion: 0.03
Nodes (43): deep_hood(), high_collar(), hood_down(), lenses(), sword_strap(), face_mask(), hakama_legs(), obi() (+35 more)

### Community 20 - "items.py"
Cohesion: 0.17
Nodes (20): art_class(), catalogue_md(), check_all(), check_loot(), compile_all(), recipe_entry(), dumps(), err() (+12 more)

### Community 21 - "mkit.py"
Cohesion: 0.14
Nodes (34): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+26 more)

### Community 22 - "Category"
Cohesion: 0.07
Nodes (27): Catalog, Category, BATH, BED, DECOR, DISPLAY, FIXTURE, FLOOR (+19 more)

### Community 23 - "Template"
Cohesion: 0.09
Nodes (9): Catalogue, Branch, Step, Template, Twist, DeskDays, Profile, Run (+1 more)

### Community 24 - ".daily"
Cohesion: 0.12
Nodes (4): Friends, Day, Visit, Visits

### Community 25 - "Desk"
Cohesion: 0.10
Nodes (10): Desk, Offer, Player, Rank, A, B, C, D (+2 more)

### Community 26 - "strip_fabric"
Cohesion: 0.02
Nodes (51): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+43 more)

### Community 27 - "dialogue.py"
Cohesion: 0.13
Nodes (35): assign_ids(), build(), check_condition(), check_text(), compiled(), compiled_question(), content_key(), coverage() (+27 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Fixture"
Cohesion: 0.14
Nodes (3): Fixture, QuestionsAndLedgerTest, TalkTest

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.14
Nodes (12): 1. At a glance, 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Ranks and milestones, Rotating story roles, Story flags (+4 more)

### Community 31 - "Fighter"
Cohesion: 0.11
Nodes (6): Battle, Chain, Event, Result, Strike, Fighter

### Community 32 - "load_clans"
Cohesion: 0.15
Nodes (10): Population, catalog(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_groups(), load_population() (+2 more)

### Community 33 - "11. Later systems"
Cohesion: 0.11
Nodes (14): 6. Squad missions, 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Later techniques and combat, Player clans, Ranks after Chunin (+6 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.06
Nodes (31): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, 6. The map, 8. The beta, chapter by chapter, 9. Delivery plan, Beta 1: the opening and the Academy (~4 h) (+23 more)

### Community 35 - "Context"
Cohesion: 0.15
Nodes (6): Context, Line, Turn, Overheard, Said, Talk

### Community 36 - "org.spongepowered.asm.mixin.Mixin"
Cohesion: 0.05
Nodes (12): AvatarRendererMixin, HumanoidModelMixin, EntityMixin, LivingEntityMixin, SnowballMixin, TripWireBlockMixin, Tools, PlayerSkins (+4 more)

### Community 37 - ".of"
Cohesion: 0.07
Nodes (7): 20. What the roadmap asks of bonds, 5. Personality, ClanProfile, Report, VillageSim, VillageScaleTest, VillageTest

### Community 38 - "Balance"
Cohesion: 0.12
Nodes (7): Difficulty, Balance, Share, Stats, BalanceTest, Trace, 15. Balance

### Community 39 - ".hit"
Cohesion: 0.11
Nodes (15): Attack, Damage, Defence, Delivery, AREA, JUTSU, MELEE, THROWN (+7 more)

### Community 40 - "rnd"
Cohesion: 0.04
Nodes (27): sprigs(), burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face() (+19 more)

### Community 41 - "sprites.py"
Cohesion: 0.07
Nodes (36): cooking.oven, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient, Market Grocer (`grocer`), material (+28 more)

### Community 43 - "kit_hagane.py"
Cohesion: 0.09
Nodes (14): gear, smithy, Weapon Shop (`weapon_shop`), shuriken(), arm_guards(), bracers(), crown(), harness() (+6 more)

### Community 44 - "Run"
Cohesion: 0.07
Nodes (16): BondEvent, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+8 more)

### Community 45 - "solid"
Cohesion: 0.04
Nodes (46): Shared helpers, How the pieces work, arm_bone(), arm_x(), belt(), body(), collar(), flaps() (+38 more)

### Community 46 - "Bonds"
Cohesion: 0.06
Nodes (26): 12. The bond book, 13. Data formats, 16. What stays in Village Friends, and what moves, 19. Society hooks, 21. Open questions, 2. The meters, 4. Memories, 6. Shared experiences and moments (+18 more)

### Community 47 - ".of"
Cohesion: 0.10
Nodes (7): Score, Practice, Session, Rest, Rested, ComfortTest, RestTest

### Community 48 - "Meters"
Cohesion: 0.10
Nodes (4): 3. Levels and story gates, Levels, Meters, LevelsTest

### Community 49 - "Garment"
Cohesion: 0.15
Nodes (6): 2 Body, Garment, key_rgba(), Piece, piece_corners(), world_bounds()

### Community 50 - "mockups.py"
Cohesion: 0.18
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 51 - ".xpAt"
Cohesion: 0.14
Nodes (4): Day, CurveAndTierTest, RosterTest, TechniqueTest

### Community 52 - "Home"
Cohesion: 0.09
Nodes (22): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 16. Keepsakes, 1. Design rules, 20. By beta slice (+14 more)

### Community 53 - "Home"
Cohesion: 0.09
Nodes (7): Design programs, Home, Tidiness, LIVED_IN, MESSY, TIDY, Photo

### Community 54 - "Act"
Cohesion: 0.02
Nodes (79): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+71 more)

### Community 55 - "Stage"
Cohesion: 0.07
Nodes (13): 10. Romance and family (after the beta), Round 8 — did not pass, Conflict, Courtship, Stage, CRUSH, DATING, ENGAGED (+5 more)

### Community 56 - "BondWorld"
Cohesion: 0.06
Nodes (12): 17. Proposed ROADMAP edits, 1. The data model, 9. Quarrels with arcs, 10. How residents address you, 18. The engine, 3. Bonds, Markers, BondWorld (+4 more)

### Community 57 - "VarietyGuard"
Cohesion: 0.11
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 58 - "Plan"
Cohesion: 0.09
Nodes (6): Kinoshita Yard (`kinoshita_yard`), scroll, base_name(), mc(), Plan, solid()

### Community 59 - "Restyle"
Cohesion: 0.15
Nodes (9): 7. Locked and changeable, Restyle, Result, Venue, BARBER, HOME, LOCKED, SETTINGS (+1 more)

### Community 60 - "net.minecraft.server.level.ServerLevel"
Cohesion: 0.07
Nodes (9): LaunchGameTest, LeafNamesGameTest, TestStreetGameTest, Blueprint, LeafNames, LeafWardrobe, Built, TestStreet (+1 more)

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.04
Nodes (14): DataTest, ResourcesTest, 19. Pacing, ConflictTest, CatalogueTest, JsonTest, LivingTest, MoveTest (+6 more)

### Community 62 - ".name"
Cohesion: 0.06
Nodes (23): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+15 more)

### Community 63 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Every building, Forest of Death, Homes, Landmarks, Lore from dialogue (+8 more)

### Community 64 - "kit_academy.py"
Cohesion: 0.06
Nodes (16): drawstrings(), forearm_wraps(), holster(), hood_down(), leg_cloth(), ribbed(), sash(), shin_wraps() (+8 more)

### Community 65 - ".play"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 66 - "build.py"
Cohesion: 0.12
Nodes (14): all_techniques(), build(), check(), statuses_in(), fold(), main(), public_text_hashes(), short() (+6 more)

### Community 67 - "net.minecraft.server.level.ServerPlayer"
Cohesion: 0.11
Nodes (7): Daily, Rest, Buff, Dishes, Fed, Quest, ShinobiProgression

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (7): Bond, LifeEvents, News, FollowUp, Highlight, Outcome, Kindling Bond

### Community 69 - "Pillar"
Cohesion: 0.10
Nodes (7): Build, Pillar, NINJUTSU, TAIJUTSU, WEAPONS, Scaling, Skill

### Community 70 - "Move"
Cohesion: 0.08
Nodes (5): ComboMachine, Context, Started, Move, Style

### Community 71 - "blocks.py"
Cohesion: 0.07
Nodes (35): 15. Furniture, Beta 1, Beta 2, Fixtures and starter pieces (Beta 1), Later (designed now), furniture, Furniture Shop (`furniture_shop`), 6. Prototypes (+27 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (16): Def, Size, BIG, NOTABLE, SMALL, Peeve, BRAGGING, COWARDICE (+8 more)

### Community 73 - "com.mojang.serialization.Codec"
Cohesion: 0.13
Nodes (4): StateGameTest, PlayerRecord, SaveSeed, SavedTest

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 75 - "kit_tobari.py"
Cohesion: 0.09
Nodes (11): decal(), hood_down(), lantern(), lantern_tag(), mantle(), muffler(), plain_body(), pleats() (+3 more)

### Community 78 - ".read"
Cohesion: 0.13
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 79 - "paint.py"
Cohesion: 0.04
Nodes (25): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+17 more)

### Community 80 - "Squad"
Cohesion: 0.10
Nodes (3): BondEffects, Departure, Squad

### Community 81 - "Label"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - ".person"
Cohesion: 0.13
Nodes (6): 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest, BondFriends

### Community 85 - "HandSign"
Cohesion: 0.12
Nodes (15): HandSign, BIRD, BOAR, DOG, DRAGON, HARE, HORSE, MONKEY (+7 more)

### Community 86 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 87 - "Clan techniques and kekkei genkai"
Cohesion: 0.08
Nodes (26): Aburame (noble), Akimichi (noble), Clan techniques and kekkei genkai, Gekko (noble), Hagane (minor), Haruno (minor), Hatake (noble), Hyuga (noble) (+18 more)

### Community 89 - "konoha/preview.py"
Cohesion: 0.12
Nodes (15): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+7 more)

### Community 90 - ".classic"
Cohesion: 0.06
Nodes (16): 11. Kindling Bond, BondConditions, BondWeb, Bonfire, Flame, Kindling, Read, Sight (+8 more)

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Niche"
Cohesion: 0.11
Nodes (14): Pulling their weight, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+6 more)

### Community 94 - "World"
Cohesion: 0.14
Nodes (4): The clan file, load_rules(), World, colors()

### Community 95 - "ROADMAP.md"
Cohesion: 0.21
Nodes (5): Commits, Development continuation, Focused workflow, graphify, Naruto Minecraft

### Community 96 - "Side quests"
Cohesion: 0.20
Nodes (9): 1. Scope and budget, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents, In the beta, Later (foundation), Later one-offs (foundation) (+1 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - ".shelf"
Cohesion: 0.13
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 99 - "2. Quest framework"
Cohesion: 0.22
Nodes (9): 2.1 Kinds, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied, 2.9 Density for 300 residents (+1 more)

### Community 100 - "Missions"
Cohesion: 0.08
Nodes (25): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back, 2.5 Failure, partial success and abandonment (+17 more)

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "roster.py"
Cohesion: 0.18
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 103 - "Wallet"
Cohesion: 0.11
Nodes (3): Ryo, Wallet, RyoTest

### Community 104 - "FirstFifteenHours.java"
Cohesion: 0.09
Nodes (7): Stage, ADULT, CHILD, TEEN, Rng, Seeds, Comfort

### Community 105 - "Stretch"
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
Nodes (4): 4. Storage, Heard, Speaker, BetaDialogueTest

### Community 109 - "AssignmentsMixin.java"
Cohesion: 0.19
Nodes (3): LeafFlats, AssignmentsMixin, LeafFlatsTest

### Community 110 - "Catalogue"
Cohesion: 0.14
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Character creation"
Cohesion: 0.11
Nodes (18): 12. Clan-born play: a later option, 13. Code, and what waits for Phase 0, 14. Open questions, 1. At a glance, 1 Name, 2. World creation first, 3 Hair, 3. Where the creator sits in the opening (+10 more)

### Community 114 - "ClanPower"
Cohesion: 0.15
Nodes (7): 1. The hierarchy, ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 115 - "Prices"
Cohesion: 0.14
Nodes (4): 2.1 How buying works, Pawn, Prices, PricesTest

### Community 116 - "Flat"
Cohesion: 0.13
Nodes (9): 17. What the map needs, Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY, Flat (+1 more)

### Community 117 - "Plant"
Cohesion: 0.08
Nodes (21): 9. Mass production, The bank today, Look, DROOPING, HEALTHY, WILTED, Plant, Stage (+13 more)

### Community 118 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 119 - "Ranks"
Cohesion: 0.07
Nodes (19): 4. Comfort, style and sets, 10. Open questions, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+11 more)

### Community 121 - "missions.py"
Cohesion: 0.11
Nodes (23): catalogue_doc(), check(), check_quests(), condition(), err(), check_tables(), compiled(), derive_places() (+15 more)

### Community 124 - "Person"
Cohesion: 0.09
Nodes (7): BondBook, Fact, MemoryLine, Page, Person, Recruitment, Schedule

### Community 125 - "net.fabricmc.fabric.api.client.gametest.v1.context.TestSingleplayerContext"
Cohesion: 0.14
Nodes (3): ErrandGameTest, SessionGameTest, StoryGameTest

### Community 126 - "Bank"
Cohesion: 0.13
Nodes (5): Bank, Facet, Pacing, Rules, Tier

### Community 127 - "Fighter"
Cohesion: 0.04
Nodes (10): Chakra, Spend, Cooldowns, Pool, Fighter, State, Jutsu, Timed (+2 more)

### Community 128 - "VisitsTest"
Cohesion: 0.21
Nodes (3): Cast, Setup, VisitsTest

### Community 129 - "kit_specialist.py"
Cohesion: 0.11
Nodes (8): bandolier(), coat_skirts(), cross_armband(), ink_stains(), scroll_tube(), seal_trim(), shirt(), strap()

### Community 130 - "wardrobe.py"
Cohesion: 0.24
Nodes (11): hex_rgb(), json_text(), load_eye_colors(), load_hair_colors(), load_palettes(), outputs(), png_bytes(), ramp() (+3 more)

### Community 132 - "Dialogue"
Cohesion: 0.17
Nodes (11): 10. Pool sizing, 11. Simulation, 12. Story-gated pools, 13. What waits, 14. Decisions and open questions, 1. Freshness: never repeat, 2. Talk budgets, 3. Beyond the budget (+3 more)

### Community 134 - "Styles and combo trees"
Cohesion: 0.08
Nodes (24): Academy blade (`combat:style.academy_blade`, weapons), Academy taijutsu (`combat:style.academy_basics`, taijutsu), Beast Fang (Four Legs) (`combat:style.beast_fang`, taijutsu), Blossom Strength (`combat:style.blossom_strength`, taijutsu), Chain arts (`combat:style.chain_arts`, weapons), Crescent Moon kenjutsu (`combat:style.crescent_moon`, weapons), Fan arts (`combat:style.fan_arts`, weapons), Gentle Fist (`combat:style.gentle_fist`, taijutsu) (+16 more)

### Community 135 - "compose.py"
Cohesion: 0.48
Nodes (5): compose(), flush_kernel(), flush_template(), fail(), main()

### Community 136 - "Code by mod"
Cohesion: 0.14
Nodes (12): 7. Every line serves a function, Quests, 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout (+4 more)

### Community 137 - "fabric"
Cohesion: 0.04
Nodes (41): weapon, stamp(), back_crest(), crescent(), hip_katana(), katana(), decal(), shoulder_decal() (+33 more)

### Community 138 - "Konoha: the build plan"
Cohesion: 0.12
Nodes (15): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, 9. Open questions, Calibration, Contents (+7 more)

### Community 140 - "creator/preview.py"
Cohesion: 0.14
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 143 - "Nature"
Cohesion: 0.09
Nodes (16): Armour, CHAKRA, NONE, PHYSICAL, WILL, DamageType, Clash, Nature (+8 more)

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
Cohesion: 0.11
Nodes (19): 4. Block catalogue, Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival (+11 more)

### Community 150 - "Keepsake"
Cohesion: 0.12
Nodes (9): New flags, Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST (+1 more)

### Community 153 - "Question"
Cohesion: 0.22
Nodes (4): 8. Questions and choices, Answer, Question, Answered

### Community 154 - "BetaTalk"
Cohesion: 0.23
Nodes (4): BetaTalk, Person, Player, World

### Community 156 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 157 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 158 - "Item catalogue"
Cohesion: 0.10
Nodes (20): apothecary, collectible, consumable, container, cooking.pot, curio, currency, Item catalogue (+12 more)

### Community 160 - ".choices"
Cohesion: 0.08
Nodes (10): 9. Age stages, AgeStage, ADULT, CHILD, TEEN, Choices, Outfit, GrowUp (+2 more)

### Community 161 - "Power"
Cohesion: 0.20
Nodes (7): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON

### Community 164 - "sys"
Cohesion: 0.22
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 165 - "pathlib"
Cohesion: 0.08
Nodes (7): build(), build(), build(), matches(), _same_json(), OutputChecksTest, png()

### Community 166 - "Rounds"
Cohesion: 0.07
Nodes (29): Owner approval for the beta build (30 October 2026), Review log, Round 10 — did not pass, Round 11 — did not pass, Round 12 — did not pass, Round 14 — did not pass, Round 15 — did not pass, Round 16 — did not pass (+21 more)

### Community 167 - "argparse"
Cohesion: 0.26
Nodes (6): blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 168 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 169 - "Experience"
Cohesion: 0.17
Nodes (10): Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION, SPAR (+2 more)

### Community 170 - ".run"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 173 - "progression.py"
Cohesion: 0.30
Nodes (10): beta_loadout(), build(), gear_for(), melee_for(), pillar_cap(), ranks_for(), sim_builds(), slice_open() (+2 more)

### Community 175 - ".strings"
Cohesion: 0.21
Nodes (6): Mode, CLASSIC, VARIED, Band, Mate, SquadPlan

### Community 176 - "Life together"
Cohesion: 0.12
Nodes (11): 15. Pacing, TimeAndPacingTest, 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Questions and choices (+3 more)

### Community 178 - "StatusEffects"
Cohesion: 0.11
Nodes (3): Active, Def, StatusEffects

### Community 180 - "Bosses"
Cohesion: 0.08
Nodes (24): Bestiary, groups and bosses, Bosses, `combat:boss.anbu.story_1`: Story boss (chapter anbu, level 38, anbu), `combat:boss.ch11.bandit_chief`: Bandit chief (chapter 11, level 11, beta2), `combat:boss.ch14.road_ambush`: Ambush on the road (chapter 14, level 14, beta2), `combat:boss.ch16.forest_beast`: A giant of the forest (chapter 16, level 16, beta3), `combat:boss.ch16.forest_team`: A hunting team in the forest (chapter 16, level 16, beta3), `combat:boss.ch17.prelim`: Preliminary bout (chapter 17, level 16, beta3) (+16 more)

### Community 181 - "docs.py"
Cohesion: 0.18
Nodes (12): animations_page(), bestiary_page(), clans_page(), counters(), esc(), move_rows(), signs(), styles_page() (+4 more)

### Community 183 - "KonohaBlocks.java"
Cohesion: 0.08
Nodes (10): KonohaBlocks, PolePart, POLE, TOP, TRANSFORMER, TankPart, BOTTOM, MIDDLE (+2 more)

### Community 187 - "animations.py"
Cohesion: 0.25
Nodes (5): arms(), clip(), keys(), many(), summary()

### Community 188 - ".remember"
Cohesion: 0.09
Nodes (21): Ch 53: Every Fire (40 min), Arc, At a glance, Dialogue brief, Fears, His plan, beat by beat, How he changes, Never reveal before (+13 more)

### Community 189 - "main"
Cohesion: 0.28
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 190 - "Weaver"
Cohesion: 0.17
Nodes (7): Outcome, CAST, EMPTY, FIZZLE, INTERRUPTED, Result, Weaver

### Community 191 - "NamesTest"
Cohesion: 0.23
Nodes (3): Names, PlayerName, NamesTest

### Community 197 - "clans.py"
Cohesion: 0.21
Nodes (10): ct(), lesser(), area(), cone(), line(), proj(), st(), summon_entity() (+2 more)

### Community 199 - "Personality"
Cohesion: 0.07
Nodes (15): Base, Personality, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM (+7 more)

### Community 200 - "Tier"
Cohesion: 0.20
Nodes (6): Mastery, Tier, MASTERED, NOVICE, PERFECTED, PRACTICED

### Community 201 - "Animation clips"
Cohesion: 0.33
Nodes (5): Animation clips, P0, P1, P2, P3

### Community 202 - "validate_catalog"
Cohesion: 0.40
Nodes (4): compatible(), load_marks(), validate_catalog(), validate_clans()

### Community 203 - "Technique catalogue"
Cohesion: 0.15
Nodes (13): Chakra movement, Earth (9), Fire (10), Fuinjutsu (6), Genjutsu (8), Lightning (8), Medical ninjutsu (5), Neutral ninjutsu (14) (+5 more)

### Community 204 - "CombatData"
Cohesion: 0.07
Nodes (8): Boss, Clip, CombatData, Enemy, Phase, Technique, Weapon, ComboAndStatusTest

### Community 205 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 206 - "Story check handoff"
Cohesion: 0.04
Nodes (40): 1. Names, 2. Dialogue, Codex handoff: Leaf names and dialogue, Done when, Rules for the names, Rules (the owner's, the same for every agent), Status, The job (+32 more)

### Community 208 - "Tier"
Cohesion: 0.20
Nodes (7): Tier, A, B, C, D, E, S

### Community 209 - "CreatorRules"
Cohesion: 0.11
Nodes (7): 11. Data, CreatorRules, Roots, LifeRoll, Rolled, Data, LifeRollTest

### Community 212 - "13.5 Phase cards"
Cohesion: 0.09
Nodes (22): 13.1 Next-step protocol, 13.2 Verification, review and token policy, 13.3 Phase order and gate evidence, 13.4 Player milestones and quality gates, 13.5 Phase cards, 13.6 Checkpoint and session handoff, 13.7 Execution controller, 13.8 Deferred story gate and owner boundaries (+14 more)

### Community 213 - "Pantry"
Cohesion: 0.09
Nodes (24): Arc, Arc, Arc, Arc, At a glance, At a glance, At a glance, At a glance (+16 more)

### Community 214 - "Combat"
Cohesion: 0.11
Nodes (17): Bonds, 10. Enemies, 11. Difficulty and feel, 12. Progression, 13. The beta loadout, 16. Animations, 17. What waits for Phase 0, 18. Ids for other systems (+9 more)

### Community 220 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 221 - "json"
Cohesion: 0.08
Nodes (7): Band, CLOSE, FAR, MID, RangeBands, paste(), scene()

### Community 222 - "Village"
Cohesion: 0.05
Nodes (14): 18. Village scale, Arc, Base, ClanRelations, Mood, SocialTie, SocietyHook, House (+6 more)

### Community 223 - "Arc"
Cohesion: 0.10
Nodes (20): Arc, At a glance, Dialogue brief, Fears, Her bond, Her thread (Thread Sight), How she changes, Lineage A track (the second is the player's mother) (+12 more)

### Community 227 - "kit_tsuchigumo.py"
Cohesion: 0.12
Nodes (9): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+1 more)

### Community 228 - "PlayerLooks"
Cohesion: 0.12
Nodes (3): CreatorGameTest, PlayerLooks, StreetGuard

### Community 230 - ".sensei"
Cohesion: 0.04
Nodes (68): Arc 1: Cinders (the Academy, Ch 0 to 7, Beta 1), Beta 1 bond quests (one per classmate), Ch 0: Cinders (20 min), Ch 1: A Key and a Bowl (20 min), Ch 2: Forms (20 min), Ch 3: The Leaf on Your Brow (25 min), Ch 4: Sinking Sun (25 min), Ch 5: The Missing Page (15 min) (+60 more)

### Community 231 - "Outcome"
Cohesion: 0.33
Nodes (6): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT

### Community 232 - "Dialogue brief"
Cohesion: 0.12
Nodes (16): Arc, At a glance, Dialogue brief, Fears, Her answer to the player's testimony, How she changes, Never reveal before, New flags (+8 more)

### Community 233 - "Dialogue brief"
Cohesion: 0.12
Nodes (16): Arc, At a glance, Common to every save, Dialogue brief, Everything before Ch 39 is identical in both tracks, How she changes, If bound (the voice), If innocent (+8 more)

### Community 237 - "`role:squad3_a`: the planner"
Cohesion: 0.12
Nodes (17): Arc, Arc, Arc, At a glance, At a glance, At a glance, Dialogue brief, Dialogue brief (+9 more)

### Community 238 - "`role:squad4_a`: the heir"
Cohesion: 0.12
Nodes (17): Arc, Arc, Arc, At a glance, At a glance, At a glance, Dialogue brief, Dialogue brief (+9 more)

### Community 257 - "1. `twist.traitor`: the voice"
Cohesion: 0.12
Nodes (17): 1. `twist.traitor`: the voice, 2. `twist.lineage`: whose child you are, 3. `twist.fourth_fate`: what the finals cost the Fourth, Allowed divergences (the only ones), Fairness, Fairness checks (per bound candidate), Innocents cleared, Rotation test matrix (+9 more)

### Community 258 - "Dialogue brief"
Cohesion: 0.12
Nodes (16): Arc, At a glance, Board chains (missions session), Common to every save, Dialogue brief, How they change, If bound (the voice), If innocent (+8 more)

### Community 259 - "The world behind the story"
Cohesion: 0.12
Nodes (16): Chronology, Elapsed time and ages, Kindling Bond in the story, Places the story adds, Story floors, Story milestones of the gift, The Hollow Crown, step by step, The Kagari (+8 more)

### Community 260 - "Dialogue briefs"
Cohesion: 0.29
Nodes (7): 1. Every line has a job, 1b. Tone and canon (line rules), 2. Tokens and pronouns, 3. Global spoiler gates, 5. The briefs, 6. Work order for the dialogue session, Dialogue briefs

### Community 262 - "Dialogue brief"
Cohesion: 0.13
Nodes (15): Arc, At a glance, Common to every save, Dialogue brief, How he changes, If bound (the voice), If innocent, Never reveal before (+7 more)

### Community 263 - "Arc"
Cohesion: 0.13
Nodes (15): Arc, At a glance, Dialogue brief, Fears, His thread, How he changes, Never reveal before, New flags (+7 more)

### Community 264 - "Memory"
Cohesion: 0.18
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 266 - "Dialogue brief"
Cohesion: 0.14
Nodes (14): Arc, At a glance, classmate_c, classmate_d, Dialogue brief, Never reveal before, New flags, Questions for the player (+6 more)

### Community 267 - "Dialogue brief"
Cohesion: 0.14
Nodes (14): Arc, At a glance, Dialogue brief, Fears, How he changes, Never reveal before, New flags, Questions for the player (+6 more)

### Community 268 - "Dialogue brief"
Cohesion: 0.14
Nodes (14): Arc, At a glance, Dialogue brief, In the war and in her recovery, Never reveal before, New flags, Questions for the player, `role:lost_child` (+6 more)

### Community 269 - "Dialogue brief"
Cohesion: 0.14
Nodes (14): Arc, At a glance, Dialogue brief, If bound (`twist.traitor = medic`), If innocent, In every save, Never reveal before, New flags (+6 more)

### Community 273 - ".runTest"
Cohesion: 0.17
Nodes (3): AcademyGameTest, Bout, Spar

### Community 274 - "Act"
Cohesion: 0.23
Nodes (3): Act, Stance, SetLook

### Community 276 - "Dialogue brief"
Cohesion: 0.17
Nodes (12): Arc, At a glance, Dialogue brief, Never reveal before, New flags, Questions for the player, `role:elder_keeper`, Thread Sight and the keeper (+4 more)

### Community 277 - "Minor recurring roles"
Cohesion: 0.17
Nodes (12): Minor recurring roles, New flags, Note on the Undercroft and the slip, `role:anbu_captain`, `role:elder_hyuga`, `role:foreign_genin`, `role:genin_1`, `role:genin_2`, `role:genin_3`, `role:hokage_4_daughter` (+4 more)

### Community 278 - "Dialogue brief"
Cohesion: 0.17
Nodes (12): Arc, At a glance, Dialogue brief, Never reveal before, New flags, Questions for the player, `role:porter`, Thread Sight and the porter (+4 more)

### Community 279 - "family_names"
Cohesion: 0.07
Nodes (27): Arc, Arc, At a glance, At a glance, At a glance, Dialogue brief, Dialogue brief, Dialogue brief (+19 more)

### Community 280 - "Story flags"
Cohesion: 0.17
Nodes (12): Acts the story asks of the bond engine, Answers (`ans.*`), Chapter flags, Gates that order the chapters, Held roles, Journal documents and other ids, Later arcs, Seed coverage rules (+4 more)

### Community 282 - "Dialogue brief"
Cohesion: 0.18
Nodes (11): Arc, At a glance, Dialogue brief, Never reveal before, New flags, Questions for the player, `role:hokage_4`, Topics they care about (+3 more)

### Community 283 - "Dialogue brief"
Cohesion: 0.18
Nodes (11): Arc, At a glance, Dialogue brief, Never reveal before, New flags, Questions for the player, `role:instructor`, Topics they care about (+3 more)

### Community 284 - "Dialogue brief"
Cohesion: 0.18
Nodes (11): Arc, At a glance, Dialogue brief, Never reveal before, New flags, Questions for the player, `role:rival`, Topics they care about (+3 more)

### Community 285 - "Dialogue brief"
Cohesion: 0.18
Nodes (11): Arc, At a glance, Dialogue brief, Never reveal before, New flags, Questions for the player, `role:sensei` (also `role:captain`), Topics they care about (+3 more)

### Community 286 - "Dialogue brief"
Cohesion: 0.18
Nodes (11): Arc, At a glance, Dialogue brief, Never reveal before, New flags, Questions for the player, `role:teammate_a`, Topics they care about (+3 more)

### Community 293 - "Arc 6 (optional): Night Watch (ANBU branch, N1 to N7)"
Cohesion: 0.25
Nodes (8): Arc 6 (optional): Night Watch (ANBU branch, N1 to N7), N1: The Mask (35 min), N2: Covert (40 min), N3: The Cellar (40 min), N4: Caged (45 min), N5: Orders (40 min), N6: Giving (50 min), N7: Daylight in the Cellar (30 min)

### Community 294 - "How the story uses the systems"
Cohesion: 0.25
Nodes (8): 1. Missions, 2. Side quests, 3b. Rank gates (the failure rule), 4. Clans, 5. Combat, 6. The Hokage requirement (wording for the roadmap), 7. Requests to other sessions (open), How the story uses the systems

### Community 299 - "`role:fallen_parent`"
Cohesion: 0.29
Nodes (7): At a glance, Brief for lines about them, New flags, Questions, `role:fallen_parent`, What remains of them, Who they were

### Community 305 - "Kind"
Cohesion: 0.50
Nodes (4): Kind, CYCLE, LINE, REPEAT

### Community 306 - "Why"
Cohesion: 0.50
Nodes (4): Why, BUDGET, EXHAUSTED, NONE

## Knowledge Gaps
- **1227 isolated node(s):** `MELEE`, `THROWN`, `JUTSU`, `AREA`, `NONE` (+1222 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2490 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **95 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Act` connect `Act` to `Memory`, `.friends`, `.answer`, `Playthrough.java`, `Experience`, `Meters`, `Stage`, `BondWorld`, `.remember`, `.name`, `Bond`, `.classmate`, `Personality`, `Def`, `Deed`, `.read`, `.classic`, `Meter`, `FirstFifteenHours.java`, `VillageSim.java`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **What connects `MELEE`, `THROWN`, `JUTSU` to the rest of the system?**
  _1227 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Roster` be split into smaller, more focused modules?**
  _Cohesion score 0.08461538461538462 - nodes in this community are weakly interconnected._
- **Why does `BondWorld` connect `BondWorld` to `VisitsTest`, `list`, `.friends`, `.answer`, `Playthrough.java`, `.of`, `Run`, `Bonds`, `SquadTest`, `Stage`, `GossipTest`, `org.junit.jupiter.api.Test`, `Bond`, `Personality`, `Deed`, `map`, `.read`, `Squad`, `.person`, `.classic`, `Village`, `Side quests`, `FirstFifteenHours.java`, `VillageSim.java`, `Person`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `family_names()` connect `family_names` to `load_clans`, `Story check handoff`, `Ranks`, `dialogue.py`, `json`, `Arc`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._