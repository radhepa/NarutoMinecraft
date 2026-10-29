# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 212 files · ~266,433 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3691 nodes · 8821 edges · 143 communities (117 shown, 26 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 1018 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `00c89665`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- creator.py
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- kit_kurama.py
- Player
- rnd
- kit_kunoichi.py
- mkit.py
- render_kit.py
- kit_suzuran.py
- 7. Systems in the beta
- .person
- pathlib
- Economy
- kit_akimichi.py
- fabric
- Box
- VarietyGuard
- Plan
- kit_morino.py
- Missions
- kit_market.py
- kit_kinoshita.py
- Catalogue
- 5. Data formats built for the whole story
- .num
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- senbon
- 4. Technical architecture
- 6. The map
- CreatorRules
- 8. The beta, chapter by chapter
- 9. Delivery plan
- blocks.py
- k
- kokuto
- Run
- Plant
- .effectiveLevel
- org.junit.jupiter.api.Test
- .choices
- Restyle
- missions.py
- kit_tsuchigumo.py
- paint.py
- .get
- Act
- Stage
- BondWorld
- kit_hagane.py
- Character creation
- 18. The engine
- list
- Run
- Kind
- Question
- Tex
- Squad
- Kind
- VillageScaleTest
- Bond
- .classic
- Person
- catalogue.py
- Def
- Levels
- Deed
- Playthrough.java
- Rng
- AnswerTag
- Home
- Face
- Mood
- End
- 4.3 The noble clans
- kit_haruno.py
- Json
- Personality
- Village
- Rng
- Category
- .tier
- Meters
- Title
- .name
- Every building
- .of
- Side quests
- 4.4 The minor clans
- AgeStage
- 2. Quest framework
- Konoha: the build plan
- Label
- .daily
- Kind
- NamesTest
- 7. Inter-clan politics as quests
- kit_household.py
- .strings
- .look
- Tier
- Home
- noren
- Custom blocks
- .receive
- VisitsTest
- Pantry
- Flat
- Json
- FirstFifteenHours.java
- .person
- Memory
- Rng
- Desk
- Keepsake
- .run
- VillageSim.java
- Tier
- Template
- Look
- QuestionsTest
- S
- 8. Beta catalogue
- mission
- 4. Clan quest lines
- .tidiness
- Data

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 194 edges
3. `solid()` - 151 edges
4. `Act` - 126 edges
5. `fabric()` - 109 edges
6. `Bond` - 66 edges
7. `Home` - 66 edges
8. `Village` - 63 edges
9. `strip_fabric()` - 59 edges
10. `Person` - 55 edges

## Surprising Connections (you probably didn't know these)
- `7. Questions and choices` --references--> `Question`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Question.java
- `11. What waits for Phase 0` --references--> `Player`  [INFERRED]
  MISSIONS.md → progression/missions/src/main/java/dev/shinobi/progression/mission/Player.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java
- `Interior fittings` --references--> `tatami()`  [INFERRED]
  KONOHA_BUILD.md → tools/konoha/blocks.py
- `3.2 Templates` --references--> `escort()`  [INFERRED]
  SIDE_QUESTS.md → tools/missions/mkit.py

## Import Cycles
- None detected.

## Communities (143 total, 26 thin omitted)

### Community 0 - "creator.py"
Cohesion: 0.08
Nodes (19): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), roll_look() (+11 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.15
Nodes (12): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+4 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.05
Nodes (63): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+55 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.03
Nodes (43): back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps() (+35 more)

### Community 7 - "Story bible"
Cohesion: 0.05
Nodes (39): Commits, graphify, Naruto Minecraft, A rank, ANBU operations, B rank, C rank, D rank (+31 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 10 - "rnd"
Cohesion: 0.04
Nodes (29): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw() (+21 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - "mkit.py"
Cohesion: 0.17
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 13 - "render_kit.py"
Cohesion: 0.14
Nodes (9): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street(), paste() (+1 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - ".person"
Cohesion: 0.09
Nodes (11): 18. The engine, Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan (+3 more)

### Community 17 - "pathlib"
Cohesion: 0.12
Nodes (3): build(), build(), build()

### Community 18 - "Economy"
Cohesion: 0.10
Nodes (11): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+3 more)

### Community 20 - "kit_akimichi.py"
Cohesion: 0.10
Nodes (10): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+2 more)

### Community 21 - "fabric"
Cohesion: 0.03
Nodes (53): Shared helpers, How the pieces work, leg_cloth(), shirt(), waist(), belt(), body(), collar() (+45 more)

### Community 22 - "Box"
Cohesion: 0.07
Nodes (9): strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece, piece_corners() (+1 more)

### Community 23 - "VarietyGuard"
Cohesion: 0.10
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 24 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 25 - "kit_morino.py"
Cohesion: 0.08
Nodes (13): arm_bone(), arm_x(), armband(), back_crest(), clipped(), coat_skirts(), combed_back(), head_cloth() (+5 more)

### Community 26 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 27 - "kit_market.py"
Cohesion: 0.04
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Catalogue"
Cohesion: 0.14
Nodes (8): Catalogue, Mode, CLASSIC, VARIED, DeskDays, Profile, Run, SimulationTest

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.09
Nodes (29): build(), build_all(), catalog(), general_pool(), hex_rgb(), json_text(), load_all_groups(), load_characters() (+21 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "CreatorRules"
Cohesion: 0.20
Nodes (5): 13. Code, and what waits for Phase 0, Choices, CreatorRules, Outfit, Roots

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "blocks.py"
Cohesion: 0.12
Nodes (23): 6. Prototypes, Lanterns, Roofs, Streets, auto_uv(), block(), Block, box() (+15 more)

### Community 42 - "k"
Cohesion: 0.03
Nodes (39): deep_hood(), high_collar(), hood_down(), lenses(), collar(), tape(), sword_strap(), hakama_legs() (+31 more)

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.10
Nodes (16): 15. Pacing, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+8 more)

### Community 45 - "Plant"
Cohesion: 0.12
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 46 - ".effectiveLevel"
Cohesion: 0.16
Nodes (5): Conversation, Reply, Topic, Standing, 6. Conversation

### Community 47 - "org.junit.jupiter.api.Test"
Cohesion: 0.05
Nodes (10): 19. Pacing, ConflictTest, SquadTest, LivingTest, MoveTest, FirstFifteenHoursTest, CatalogueTest, SeedsTest (+2 more)

### Community 49 - "Restyle"
Cohesion: 0.15
Nodes (9): 7. Locked and changeable, Restyle, Result, Venue, BARBER, HOME, LOCKED, SETTINGS (+1 more)

### Community 50 - "missions.py"
Cohesion: 0.17
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 51 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 52 - "paint.py"
Cohesion: 0.02
Nodes (61): back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock(), ring_shell() (+53 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "BondWorld"
Cohesion: 0.08
Nodes (3): BondEffects, BondWorld, LifeEvents

### Community 57 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 58 - "Character creation"
Cohesion: 0.10
Nodes (20): 10. How residents address you, 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Question"
Cohesion: 0.12
Nodes (6): Answer, Question, Answered, Outcome, Questions, QuestionsCompiledTest

### Community 64 - "Tex"
Cohesion: 0.14
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 65 - "Squad"
Cohesion: 0.07
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 66 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.12
Nodes (4): ClanProfile, Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (5): Bond, BondConditions, BondWeb, News, FollowUp

### Community 69 - ".classic"
Cohesion: 0.08
Nodes (7): 8. The village talks, BondDialogueTest, ConditionsAndEffectsTest, GossipTest, Leaf, MemoryTest, VillageTest

### Community 70 - "Person"
Cohesion: 0.04
Nodes (26): 13. Data formats, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 20. What the roadmap asks of bonds, 21. Open questions, 2. The meters, 4. Memories (+18 more)

### Community 71 - "catalogue.py"
Cohesion: 0.22
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.17
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 77 - "AnswerTag"
Cohesion: 0.08
Nodes (24): Lean, AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL (+16 more)

### Community 78 - "Home"
Cohesion: 0.10
Nodes (3): Beta 1, Home, Photo

### Community 79 - "Face"
Cohesion: 0.18
Nodes (6): button(), dark_seams(), darken_rows(), rivets(), Face, shade()

### Community 81 - "Mood"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 86 - "Personality"
Cohesion: 0.06
Nodes (26): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+18 more)

### Community 87 - "Village"
Cohesion: 0.05
Nodes (13): 18. Village scale, 19. Society hooks, Base, ClanRelations, Mood, SocialTie, SocietyHook, House (+5 more)

### Community 89 - "Category"
Cohesion: 0.07
Nodes (27): Catalog, Category, BATH, BED, DECOR, DISPLAY, FIXTURE, FLOOR (+19 more)

### Community 90 - ".tier"
Cohesion: 0.11
Nodes (10): 11. Kindling Bond, 12. The bond book, BondBook, Fact, MemoryLine, Page, Bonfire, Flame (+2 more)

### Community 91 - "Meters"
Cohesion: 0.10
Nodes (7): Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Meters

### Community 92 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.25
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 94 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 95 - ".of"
Cohesion: 0.11
Nodes (7): Score, Practice, Session, Rest, Rested, ComfortTest, RestTest

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - ".daily"
Cohesion: 0.14
Nodes (4): Friends, Day, Visit, Visits

### Community 104 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 105 - "NamesTest"
Cohesion: 0.25
Nodes (4): 1 Name, Names, PlayerName, NamesTest

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 109 - "kit_household.py"
Cohesion: 0.05
Nodes (23): bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta(), ichimatsu() (+15 more)

### Community 110 - ".strings"
Cohesion: 0.35
Nodes (3): Band, Mate, SquadPlan

### Community 112 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 113 - "Tier"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 114 - "Home"
Cohesion: 0.09
Nodes (23): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 15. Furniture, 16. Keepsakes, 1. Design rules (+15 more)

### Community 115 - "noren"
Cohesion: 0.24
Nodes (7): 2. Style guide: the Konoha kit, By building type, Facades and shop fronts, Shared palette, awning(), facing_states(), noren()

### Community 116 - "Custom blocks"
Cohesion: 0.12
Nodes (15): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+7 more)

### Community 117 - ".receive"
Cohesion: 0.29
Nodes (5): 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest

### Community 118 - "VisitsTest"
Cohesion: 0.19
Nodes (3): Cast, Setup, VisitsTest

### Community 121 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 122 - "Flat"
Cohesion: 0.10
Nodes (12): 17. What the map needs, 2. The flat, The Classic flat: `flat.leaf_block.3a`, Varied candidates, Tier, BARE, BELOVED, COMFORTABLE (+4 more)

### Community 127 - "Memory"
Cohesion: 0.20
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 129 - "Desk"
Cohesion: 0.14
Nodes (8): Desk, Offer, Rank, A, B, C, D, S

### Community 130 - "Keepsake"
Cohesion: 0.12
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 131 - ".run"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 132 - "VillageSim.java"
Cohesion: 0.15
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 133 - "Tier"
Cohesion: 0.25
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 134 - "Template"
Cohesion: 0.24
Nodes (4): Branch, Step, Template, Twist

### Community 137 - "QuestionsTest"
Cohesion: 0.14
Nodes (5): DialogueKeys, DialogueKeysTest, QuestionsTest, SampleQuestions, 10. Content plan

### Community 138 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), merchant_camp_talk(), S, twist()

### Community 140 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 141 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 143 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 146 - ".tidiness"
Cohesion: 0.40
Nodes (4): Tidiness, LIVED_IN, MESSY, TIDY

## Knowledge Gaps
- **291 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+286 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1346 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `VillageSim.java`, `QuestionsTest`, `.person`, `list`, `Run`, `.effectiveLevel`, `org.junit.jupiter.api.Test`, `Stage`, `list`, `Run`, `Question`, `Squad`, `VillageScaleTest`, `Bond`, `.classic`, `Person`, `Deed`, `Playthrough.java`, `Village`, `.tier`, `.receive`, `VisitsTest`, `.person`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _291 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `creator.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08405797101449275 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `kit_uchiha.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `rnd`, `kit_kunoichi.py`, `kit_suzuran.py`, `kit_akimichi.py`, `fabric`, `kit_morino.py`, `kit_market.py`, `kit_kinoshita.py`, `senbon`, `kit_tsuchigumo.py`, `paint.py`, `kit_hagane.py`, `Face`, `kit_haruno.py`, `kit_household.py`, `Custom blocks`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Person` to `Squad`, `VillageScaleTest`, `.classic`, `Story bible`, `Levels`, `Run`, `.person`, `Village`, `Stage`, `Personality`, `.tier`, `Meters`, `Memory`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05070892410341952 - nodes in this community are weakly interconnected._