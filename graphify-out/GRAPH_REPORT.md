# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 233 files · ~286,430 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3943 nodes · 9369 edges · 170 communities (136 shown, 34 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1060 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6d43fa15`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- creator.py
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- creator.py
- Story bible
- kit_kurama.py
- Home
- rnd
- kit_kunoichi.py
- mkit.py
- fabric
- kit_suzuran.py
- 7. Systems in the beta
- .person
- kit_uzumaki.py
- .answer
- org.junit.jupiter.api.Test
- .person
- kit_tobari.py
- Catalogue
- Economy
- Desk
- AnswerTag
- mockups.py
- kit_market.py
- solid
- k
- 5. Data formats built for the whole story
- strip_fabric
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- .num
- 4. Technical architecture
- 6. The map
- Plan
- 8. The beta, chapter by chapter
- 9. Delivery plan
- VillageSim.java
- Missions
- blocks.py
- Run
- Plant
- CreatorRules
- Home
- .choices
- Box
- .daily
- kit_tsuchigumo.py
- cel_box
- Flat
- Act
- Stage
- BondWorld
- konoha/preview.py
- noren
- VisitsTest
- list
- .test
- Kind
- Question
- org.junit.jupiter.api.Test
- Squad
- VillageScaleTest
- Bond
- .of
- Person
- Squad
- Def
- Levels
- Deed
- Person
- Rng
- Plant
- .choices
- Face
- Restyle
- Mood
- .score
- 4.3 The noble clans
- kit_haruno.py
- .get
- Personality
- Village
- Tex
- Character creation
- .tier
- Meter
- Title
- .name
- Every building
- missions.py
- Side quests
- 4.4 The minor clans
- 2. Quest framework
- pathlib
- Label
- .daily
- catalogue.py
- Kind
- NamesTest
- 7. Inter-clan politics as quests
- RosterTest
- World
- creator/preview.py
- Player
- .look
- Tier
- ClanPower
- .run
- State
- Catalog
- Keepsake
- konoha/preview.py
- Category
- Flat
- Json
- .talk
- Rng
- render_kit.py
- Every building
- .react
- Kind
- kit_tsuchigumo.py
- AgeStage
- Template
- NamesTest
- Rng
- .look
- Pantry
- kit_sarutobi.py
- Json
- Rng
- .strings
- .page
- Kind
- Look
- TimeAndPacingTest
- shade
- Custom blocks
- SquadTest
- .set
- S
- MoveTest
- Tier
- Rng
- mission
- End
- SeedsTest.java
- 5. Process
- FurnitureSet
- 6. Filler arcs
- street.py
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
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `7. Questions and choices` --references--> `Question`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Question.java
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `11. What waits for Phase 0` --references--> `Player`  [INFERRED]
  MISSIONS.md → progression/missions/src/main/java/dev/shinobi/progression/mission/Player.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java

## Import Cycles
- None detected.

## Communities (170 total, 34 thin omitted)

### Community 0 - "creator.py"
Cohesion: 0.09
Nodes (5): Hooks for the other mods, Contribution, GrowthEvent, Grower, Roster

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
Cohesion: 0.12
Nodes (20): new_canvas(), save_canvas(), backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads() (+12 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "creator.py"
Cohesion: 0.09
Nodes (18): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), roll_look() (+10 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (39): Commits, graphify, Naruto Minecraft, A rank, ANBU operations, B rank, C rank, D rank (+31 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+5 more)

### Community 9 - "Home"
Cohesion: 0.09
Nodes (6): Home, Tidiness, LIVED_IN, MESSY, TIDY, Photo

### Community 10 - "rnd"
Cohesion: 0.04
Nodes (36): gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode(), claw_marks() (+28 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.08
Nodes (11): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), tabi_boots() (+3 more)

### Community 12 - "mkit.py"
Cohesion: 0.17
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 13 - "fabric"
Cohesion: 0.03
Nodes (40): How the pieces work, stamp(), back_crest(), crescent(), hip_katana(), katana(), decal(), shoulder_decal() (+32 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - ".person"
Cohesion: 0.10
Nodes (10): Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan, Together (+2 more)

### Community 17 - "kit_uzumaki.py"
Cohesion: 0.12
Nodes (8): bun(), clip(), crest_patch(), hairpin(), seal_script(), seal_tags(), waves(), wrap_tie()

### Community 18 - ".answer"
Cohesion: 0.13
Nodes (5): Answered, Outcome, Questions, QuestionsTest, SampleQuestions

### Community 19 - "org.junit.jupiter.api.Test"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - ".person"
Cohesion: 0.11
Nodes (9): 12. The bond book, 18. The engine, 7. Keepsakes, curios, photos and chests, Chests and storage, Gifts, Received, GiftsTest, BondFriends (+1 more)

### Community 21 - "kit_tobari.py"
Cohesion: 0.05
Nodes (22): shirt(), anbu_plates(), bandolier(), coat_skirts(), cross_armband(), ink_stains(), scroll_tube(), seal_trim() (+14 more)

### Community 22 - "Catalogue"
Cohesion: 0.11
Nodes (9): Catalogue, Mode, CLASSIC, VARIED, CatalogueTest, DeskDays, Profile, Run (+1 more)

### Community 23 - "Economy"
Cohesion: 0.10
Nodes (10): Band, Economy, GradeRow, Performance, Grade, A, B, C (+2 more)

### Community 24 - "Desk"
Cohesion: 0.11
Nodes (9): Desk, Result, Offer, Rank, A, B, C, D (+1 more)

### Community 25 - "AnswerTag"
Cohesion: 0.09
Nodes (20): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+12 more)

### Community 26 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 27 - "kit_market.py"
Cohesion: 0.04
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+14 more)

### Community 28 - "solid"
Cohesion: 0.04
Nodes (39): drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps(), side_stripe() (+31 more)

### Community 29 - "k"
Cohesion: 0.04
Nodes (35): Shared helpers, braid(), deep_hood(), high_collar(), hood_down(), lenses(), arm_bone(), arm_x() (+27 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "strip_fabric"
Cohesion: 0.03
Nodes (43): leg_cloth(), waist(), arm_guards(), blouse(), cargo(), collar(), gloves(), half_sleeves() (+35 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.09
Nodes (29): build(), build_all(), catalog(), general_pool(), hex_rgb(), json_text(), load_all_groups(), load_characters() (+21 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - ".num"
Cohesion: 0.12
Nodes (4): Clients, Rapport, SlotFiller, VarietyGuard

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "VillageSim.java"
Cohesion: 0.10
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 42 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 43 - "blocks.py"
Cohesion: 0.15
Nodes (15): Roofs, Streets, auto_uv(), block(), Block, box(), compile_all(), kawara_ridge() (+7 more)

### Community 44 - "Run"
Cohesion: 0.08
Nodes (14): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+6 more)

### Community 45 - "Plant"
Cohesion: 0.14
Nodes (3): BondInput, Day, RosterTest

### Community 46 - "CreatorRules"
Cohesion: 0.20
Nodes (5): 13. Code, and what waits for Phase 0, Choices, CreatorRules, Outfit, Roots

### Community 47 - "Home"
Cohesion: 0.08
Nodes (24): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 15. Furniture, 16. Keepsakes, 1. Design rules (+16 more)

### Community 48 - ".choices"
Cohesion: 0.11
Nodes (5): 20. What the roadmap asks of bonds, 5. Personality, Personality, Reaction, ReactionTest

### Community 49 - "Box"
Cohesion: 0.07
Nodes (10): strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece, piece_corners() (+2 more)

### Community 50 - ".daily"
Cohesion: 0.18
Nodes (4): Friends, Day, Visit, Visits

### Community 51 - "kit_tsuchigumo.py"
Cohesion: 0.19
Nodes (3): Technique, CurveAndTierTest, TechniqueTest

### Community 52 - "cel_box"
Cohesion: 0.03
Nodes (48): back_fan(), bangs(), cel_box(), cel_face(), curtain(), lock(), ring_shell(), sidelocks() (+40 more)

### Community 53 - "Flat"
Cohesion: 0.10
Nodes (12): 17. What the map needs, 2. The flat, The Classic flat: `flat.leaf_block.3a`, Varied candidates, Tier, BARE, BELOVED, COMFORTABLE (+4 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "BondWorld"
Cohesion: 0.06
Nodes (3): BondWorld, LifeEvents, Standing

### Community 57 - "konoha/preview.py"
Cohesion: 0.16
Nodes (13): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+5 more)

### Community 58 - "noren"
Cohesion: 0.12
Nodes (18): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 6. Prototypes, 7. Effort estimate, 8. Registration notes for Phase 0, By building type, Calibration, Contents (+10 more)

### Community 59 - "VisitsTest"
Cohesion: 0.20
Nodes (3): Cast, Setup, VisitsTest

### Community 61 - ".test"
Cohesion: 0.07
Nodes (6): BondConditions, BondEffects, BondWeb, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Question"
Cohesion: 0.12
Nodes (3): Memory, Meters, MemoryTest

### Community 64 - "org.junit.jupiter.api.Test"
Cohesion: 0.06
Nodes (4): DialogueKeysTest, LivingTest, SlotFillerTest, AgeStageTest

### Community 65 - "Squad"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.14
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.07
Nodes (3): Bond, News, FollowUp

### Community 69 - ".of"
Cohesion: 0.11
Nodes (3): ConflictTest, GossipTest, Leaf

### Community 70 - "Person"
Cohesion: 0.10
Nodes (13): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 6. Shared experiences and moments (+5 more)

### Community 71 - "Squad"
Cohesion: 0.10
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.06
Nodes (22): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+14 more)

### Community 73 - "Levels"
Cohesion: 0.18
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.09
Nodes (9): 8. The village talks, Deed, Know, Gossip, Source, HEARD, SEEN, SELF (+1 more)

### Community 75 - "Person"
Cohesion: 0.08
Nodes (4): 13. Data formats, Conflict, Person, Recruitment

### Community 77 - "Plant"
Cohesion: 0.12
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 79 - "Face"
Cohesion: 0.15
Nodes (8): mark(), button(), dark_seams(), darken_rows(), grid(), rivets(), Face, shade()

### Community 80 - "Restyle"
Cohesion: 0.15
Nodes (9): 7. Locked and changeable, Restyle, Result, Venue, BARBER, HOME, LOCKED, SETTINGS (+1 more)

### Community 81 - "Mood"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - ".score"
Cohesion: 0.20
Nodes (4): Rest, Rested, ComfortTest, RestTest

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 86 - "Personality"
Cohesion: 0.08
Nodes (24): ClanProfile, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS (+16 more)

### Community 88 - "Tex"
Cohesion: 0.14
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 89 - "Character creation"
Cohesion: 0.10
Nodes (20): 10. How residents address you, 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 90 - ".tier"
Cohesion: 0.18
Nodes (5): 11. Kindling Bond, Household, Bonfire, Flame, Kindling

### Community 91 - "Meter"
Cohesion: 0.14
Nodes (6): Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.12
Nodes (13): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+5 more)

### Community 94 - "Every building"
Cohesion: 0.11
Nodes (7): 18. Village scale, House, Tier, BACKGROUND, CAST, KNOWN, Village

### Community 95 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 96 - "Side quests"
Cohesion: 0.25
Nodes (8): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 9. Open questions, Contents, Side quests

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "pathlib"
Cohesion: 0.12
Nodes (5): check(), main(), build(), build(), build()

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - ".daily"
Cohesion: 0.17
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 103 - "catalogue.py"
Cohesion: 0.17
Nodes (10): story_reserved_family_names(), block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table() (+2 more)

### Community 105 - "NamesTest"
Cohesion: 0.13
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "RosterTest"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "World"
Cohesion: 0.14
Nodes (4): 9. The generator, Resident, World, SampleVillage

### Community 109 - "creator/preview.py"
Cohesion: 0.16
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 112 - ".look"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Tier"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 114 - "ClanPower"
Cohesion: 0.17
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 115 - ".run"
Cohesion: 0.22
Nodes (6): 19. Pacing, FirstFifteenHours, Result, Slice, Snapshot, FirstFifteenHoursTest

### Community 116 - "State"
Cohesion: 0.25
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 117 - "Catalog"
Cohesion: 0.14
Nodes (10): Catalog, Piece, Source, CLAN, CRAFT, EVENT, FIXED, QUEST (+2 more)

### Community 118 - "Keepsake"
Cohesion: 0.12
Nodes (8): Keepsake, Kind, CLAN, CURIO, FESTIVAL, GIFT, QUEST, STORY

### Community 119 - "konoha/preview.py"
Cohesion: 0.11
Nodes (17): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+9 more)

### Community 121 - "Category"
Cohesion: 0.12
Nodes (17): Category, BATH, BED, DECOR, DISPLAY, FIXTURE, FLOOR, KITCHEN (+9 more)

### Community 122 - "Flat"
Cohesion: 0.22
Nodes (7): Tier, A, B, C, D, E, S

### Community 124 - ".talk"
Cohesion: 0.08
Nodes (16): BondDialogue, Conversation, Reply, Topic, DialogueKeys, BondDialogueTest, 10. Content plan, 11. Open questions (+8 more)

### Community 126 - "render_kit.py"
Cohesion: 0.19
Nodes (7): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 127 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 128 - ".react"
Cohesion: 0.17
Nodes (3): Score, Practice, Session

### Community 129 - "Kind"
Cohesion: 0.17
Nodes (10): Kind, CLAN_SUMMONS, GIFT, INVITATION, NEIGHBOUR, NOTE, STIPEND, STORY (+2 more)

### Community 130 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 131 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 132 - "Template"
Cohesion: 0.21
Nodes (4): Branch, Step, Template, Twist

### Community 133 - "NamesTest"
Cohesion: 0.25
Nodes (4): 1 Name, Names, PlayerName, NamesTest

### Community 135 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 136 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 137 - "kit_sarutobi.py"
Cohesion: 0.13
Nodes (8): beard(), crest(), crest_patch(), flame_hem(), monkey(), pauldron(), scarf(), trench_knife()

### Community 140 - ".strings"
Cohesion: 0.32
Nodes (3): Band, Mate, SquadPlan

### Community 141 - ".page"
Cohesion: 0.33
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 143 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 147 - "TimeAndPacingTest"
Cohesion: 0.27
Nodes (3): 15. Pacing, TimeAndPacingTest, 9. Pacing with time together

### Community 148 - "shade"
Cohesion: 0.25
Nodes (7): 4. Block catalogue, Interior fittings, Totals, Vanilla mappings, tatami(), tatami_top(), shade()

### Community 149 - "Custom blocks"
Cohesion: 0.13
Nodes (14): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+6 more)

### Community 152 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), merchant_camp_talk(), S, twist()

### Community 154 - "Tier"
Cohesion: 0.25
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 158 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 159 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 161 - "5. Process"
Cohesion: 0.50
Nodes (4): 5. Process, Order of work, The pieces, What needs you at your PC

### Community 163 - "6. Filler arcs"
Cohesion: 0.50
Nodes (4): 6. Filler arcs, In the beta, Later (foundation), Later one-offs (foundation)

## Knowledge Gaps
- **325 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+320 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1424 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **34 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `kit_uchiha.py`, `kit_tsuchigumo.py`, `kit_senju.py`, `kit_kurama.py`, `kit_sarutobi.py`, `rnd`, `kit_kunoichi.py`, `fabric`, `kit_suzuran.py`, `kit_uzumaki.py`, `org.junit.jupiter.api.Test`, `kit_tobari.py`, `Custom blocks`, `kit_market.py`, `solid`, `strip_fabric`, `cel_box`, `Face`, `kit_haruno.py`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _325 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `creator.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08534850640113797 - nodes in this community are weakly interconnected._
- **Why does `BondWorld` connect `BondWorld` to `.page`, `.person`, `.answer`, `.person`, `SquadTest`, `AnswerTag`, `VillageSim.java`, `Run`, `Stage`, `VisitsTest`, `list`, `.test`, `org.junit.jupiter.api.Test`, `.romance`, `VillageScaleTest`, `Bond`, `.of`, `Squad`, `Deed`, `Person`, `.tier`, `Every building`, `.talk`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `kit_uchiha.py`, `kit_tsuchigumo.py`, `kit_senju.py`, `kit_kurama.py`, `kit_sarutobi.py`, `rnd`, `kit_kunoichi.py`, `fabric`, `kit_suzuran.py`, `kit_uzumaki.py`, `org.junit.jupiter.api.Test`, `kit_tobari.py`, `Custom blocks`, `kit_market.py`, `k`, `strip_fabric`, `Box`, `cel_box`, `kit_haruno.py`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12312312312312312 - nodes in this community are weakly interconnected._