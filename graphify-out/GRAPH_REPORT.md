# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 235 files · ~285,668 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3951 nodes · 9376 edges · 167 communities (126 shown, 41 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 1055 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4652d147`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Roster
- kit_uchiha.py
- Clans
- Meters
- render.py
- living_eyes.py
- solid
- Story bible
- rnd
- kit_hagane.py
- konoha/preview.py
- cel_box
- blocks.py
- creator.py
- kit_suzuran.py
- 7. Systems in the beta
- .person
- org.junit.jupiter.api.Test
- Catalogue
- kit_rugged.py
- strip_fabric
- kit_nara.py
- Home
- mkit.py
- Economy
- Category
- mockups.py
- k
- kit_kinoshita.py
- wide_sleeves
- 5. Data formats built for the whole story
- kit_field.py
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- .tier
- 4. Technical architecture
- 6. The map
- .daily
- 8. The beta, chapter by chapter
- 9. Delivery plan
- VarietyGuard
- kit_akimichi.py
- blocks.py
- Playthrough
- .xpAt
- .effectiveLevel
- Plan
- Peeve
- Box
- Desk
- .add
- kit_hyuga.py
- Question
- Act
- Person
- .bond
- .set
- Missions
- Home
- map
- .classic
- Kind
- Memory
- .play
- Flat
- VillageScaleTest
- Bond
- .of
- Bonds
- awning
- Def
- Meters
- Deed
- .romance
- CreatorRules
- Squad
- Face
- Life together
- Label
- Playthrough.java
- 4.3 The noble clans
- kit_haruno.py
- Plant
- Value
- ClanRelations
- .num
- .choices
- .day
- Meter
- Title
- Niche
- Village
- 7. Inter-clan politics as quests
- Side quests
- 4.4 The minor clans
- shop_tea_house.py
- 2. Quest framework
- Restyle
- home_plaster_2f.py
- roster.py
- Personality
- Seeds
- Stretch
- Tier
- 8. Beta catalogue
- 4. Clan quest lines
- Player
- .get
- Character creation
- Tier
- Rng
- Conflict
- render_kit.py
- Ranks
- VisitsTest
- .score
- missions.py
- apartment_block.py
- Tex
- .person
- AnswerTag
- Json
- Rng
- .page
- creator/preview.py
- Every building
- Kind
- AgeStage
- catalogue.py
- Konoha: the build plan
- .friends
- NamesTest
- Keepsake
- Rng
- .look
- .receive
- Pantry
- Custom blocks
- .run
- Template
- Json
- Rng
- SquadPlan
- Look
- Tier
- GossipTest
- State
- SquadTest
- Tier
- S
- mission
- End
- Data

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 194 edges
3. `solid()` - 151 edges
4. `Act` - 126 edges
5. `fabric()` - 109 edges
6. `Bond` - 66 edges
7. `Home` - 65 edges
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

## Communities (167 total, 41 thin omitted)

### Community 0 - "Roster"
Cohesion: 0.09
Nodes (5): Hooks for the other mods, Contribution, GrowthEvent, Grower, Roster

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.25
Nodes (8): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file

### Community 4 - "render.py"
Cohesion: 0.13
Nodes (18): render_player(), new_canvas(), backdrop(), Canvas, Character, clan_renders(), cube_quads(), font() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.03
Nodes (55): How the pieces work, stamp(), back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed() (+47 more)

### Community 7 - "Story bible"
Cohesion: 0.05
Nodes (39): Commits, graphify, Naruto Minecraft, A rank, ANBU operations, B rank, C rank, D rank (+31 more)

### Community 8 - "rnd"
Cohesion: 0.03
Nodes (34): sprigs(), back_crest(), bead_clip(), brush_pin(), brush_stroke(), ink_clouds(), kimono_sleeves(), part_line() (+26 more)

### Community 9 - "kit_hagane.py"
Cohesion: 0.06
Nodes (16): spike(), bracers(), crown(), harness(), mace(), plate(), shin_guards(), burst() (+8 more)

### Community 10 - "konoha/preview.py"
Cohesion: 0.14
Nodes (15): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+7 more)

### Community 11 - "cel_box"
Cohesion: 0.04
Nodes (28): cel_box(), tie(), topknot(), ear_panels(), gathered_tail(), hair_tie(), arm_warmers(), frog_buttons() (+20 more)

### Community 12 - "blocks.py"
Cohesion: 0.15
Nodes (17): 6. Prototypes, Interior fittings, Lanterns, Roofs, Streets, block(), Block, box() (+9 more)

### Community 13 - "creator.py"
Cohesion: 0.07
Nodes (20): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+12 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (19): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+11 more)

### Community 16 - ".person"
Cohesion: 0.11
Nodes (11): 18. The engine, Activity, BondEvent, Answer, FollowUp, Highlight, Invitation, Outcome (+3 more)

### Community 17 - "org.junit.jupiter.api.Test"
Cohesion: 0.07
Nodes (9): 19. Pacing, LivingTest, MoveTest, RentTest, FirstFifteenHoursTest, CurveAndTierTest, SeedsTest, SlotFillerTest (+1 more)

### Community 18 - "Catalogue"
Cohesion: 0.10
Nodes (9): Catalogue, Mode, CLASSIC, VARIED, CatalogueTest, DeskDays, Profile, Run (+1 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (16): baggy_legs(), camo(), cape(), dread(), leg_wraps(), patch(), ragged(), rope() (+8 more)

### Community 20 - "strip_fabric"
Cohesion: 0.03
Nodes (57): Shared helpers, leg_cloth(), shirt(), waist(), belt(), body(), collar(), half_sleeves() (+49 more)

### Community 21 - "kit_nara.py"
Cohesion: 0.09
Nodes (12): cel_face(), ring_shell(), crown(), combed_back(), arm_protector(), back_crest(), crest(), mesh_shirt() (+4 more)

### Community 22 - "Home"
Cohesion: 0.09
Nodes (6): Home, Tidiness, LIVED_IN, MESSY, TIDY, Photo

### Community 23 - "mkit.py"
Cohesion: 0.17
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 24 - "Economy"
Cohesion: 0.09
Nodes (11): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+3 more)

### Community 25 - "Category"
Cohesion: 0.07
Nodes (27): Catalog, Category, BATH, BED, DECOR, DISPLAY, FIXTURE, FLOOR (+19 more)

### Community 26 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 27 - "k"
Cohesion: 0.03
Nodes (49): deep_hood(), high_collar(), hood_down(), lenses(), sword_strap(), blossom(), geta(), bib() (+41 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "wide_sleeves"
Cohesion: 0.18
Nodes (7): arm_bone(), arm_x(), armband(), roll(), seal_script(), seal_tags(), wide_sleeves()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "kit_field.py"
Cohesion: 0.09
Nodes (10): arm_guards(), blouse(), cargo(), collar(), gloves(), holster(), knee_guards(), pocket() (+2 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.08
Nodes (34): build(), build_all(), catalog(), clan_bottoms(), clan_resident(), compatible(), general_pool(), general_resident() (+26 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - ".tier"
Cohesion: 0.19
Nodes (5): 11. Kindling Bond, Household, Bonfire, Flame, Kindling

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - ".daily"
Cohesion: 0.14
Nodes (4): Friends, Day, Visit, Visits

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "VarietyGuard"
Cohesion: 0.14
Nodes (4): 9. The generator, Resident, World, SampleVillage

### Community 42 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode()

### Community 43 - "blocks.py"
Cohesion: 0.18
Nodes (9): auto_uv(), check(), compile_all(), facing_states(), main(), ref(), shoji(), shoji_paper() (+1 more)

### Community 44 - "Playthrough"
Cohesion: 0.08
Nodes (14): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+6 more)

### Community 45 - ".xpAt"
Cohesion: 0.14
Nodes (3): BondInput, Day, RosterTest

### Community 46 - ".effectiveLevel"
Cohesion: 0.10
Nodes (13): Conversation, Reply, Topic, LifeEvents, News, 11. Open questions, 1. What makes a relationship feel real, 4. Their lives (+5 more)

### Community 47 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 48 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 49 - "Box"
Cohesion: 0.06
Nodes (11): dark_seams(), strip_line(), Box, Garment, key_rgba(), Layer, Piece, piece_corners() (+3 more)

### Community 50 - "Desk"
Cohesion: 0.15
Nodes (8): Desk, Offer, Rank, A, B, C, D, S

### Community 52 - "kit_hyuga.py"
Cohesion: 0.03
Nodes (33): back_fan(), bangs(), braid(), curtain(), lock(), sidelocks(), back_sheet(), blunt_fringe() (+25 more)

### Community 53 - "Question"
Cohesion: 0.05
Nodes (19): 14. Save format and versioning, Answer, Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST (+11 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Person"
Cohesion: 0.07
Nodes (14): 10. Romance and family (after the beta), 20. What the roadmap asks of bonds, Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST (+6 more)

### Community 58 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 59 - "Home"
Cohesion: 0.08
Nodes (25): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 15. Furniture, 16. Keepsakes, 1. Design rules (+17 more)

### Community 61 - ".classic"
Cohesion: 0.12
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Memory"
Cohesion: 0.20
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 65 - ".play"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 66 - "Flat"
Cohesion: 0.09
Nodes (8): 17. What the map needs, 2. The flat, The Classic flat: `flat.leaf_block.3a`, Varied candidates, Flat, Room, Due, Rent

### Community 67 - "VillageScaleTest"
Cohesion: 0.13
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (13): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 5. Personality (+5 more)

### Community 71 - "awning"
Cohesion: 0.33
Nodes (5): 2. Style guide: the Konoha kit, By building type, Facades and shop fronts, Shared palette, awning()

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Meters"
Cohesion: 0.16
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.13
Nodes (3): Deed, Know, Gossip

### Community 77 - "CreatorRules"
Cohesion: 0.20
Nodes (5): 13. Code, and what waits for Phase 0, Choices, CreatorRules, Outfit, Roots

### Community 78 - "Squad"
Cohesion: 0.10
Nodes (3): BondEffects, Departure, Squad

### Community 79 - "Face"
Cohesion: 0.06
Nodes (23): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+15 more)

### Community 80 - "Life together"
Cohesion: 0.27
Nodes (3): 15. Pacing, TimeAndPacingTest, 9. Pacing with time together

### Community 81 - "Label"
Cohesion: 0.12
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - "Plant"
Cohesion: 0.12
Nodes (11): Look, DROOPING, HEALTHY, WILTED, Plant, Stage, FLOWERING, GRAND (+3 more)

### Community 86 - "Value"
Cohesion: 0.08
Nodes (17): ClanProfile, Stage, ADULT, CHILD, TEEN, Value, COURAGE, CREATIVITY (+9 more)

### Community 87 - "ClanRelations"
Cohesion: 0.10
Nodes (9): Base, ClanRelations, Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL (+1 more)

### Community 88 - ".num"
Cohesion: 0.12
Nodes (4): Clients, Rapport, SlotFiller, VarietyGuard

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.12
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Niche"
Cohesion: 0.12
Nodes (13): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+5 more)

### Community 94 - "Village"
Cohesion: 0.15
Nodes (3): 18. Village scale, House, Village

### Community 95 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Restyle"
Cohesion: 0.15
Nodes (9): 7. Locked and changeable, Restyle, Result, Venue, BARBER, HOME, LOCKED, SETTINGS (+1 more)

### Community 102 - "roster.py"
Cohesion: 0.17
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 103 - "Personality"
Cohesion: 0.10
Nodes (5): DialogueKeys, Personality, DialogueKeysTest, ReactionTest, 10. Content plan

### Community 105 - "Stretch"
Cohesion: 0.13
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 106 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 112 - "Character creation"
Cohesion: 0.10
Nodes (20): 10. How residents address you, 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair (+12 more)

### Community 113 - "Tier"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 114 - "Rng"
Cohesion: 0.14
Nodes (6): ClanPower, CLANLESS, GREAT, MINOR, STRONG, ClanPowerTest

### Community 117 - "render_kit.py"
Cohesion: 0.11
Nodes (10): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street() (+2 more)

### Community 119 - "Ranks"
Cohesion: 0.11
Nodes (17): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+9 more)

### Community 121 - "VisitsTest"
Cohesion: 0.20
Nodes (3): Cast, Setup, VisitsTest

### Community 123 - ".score"
Cohesion: 0.15
Nodes (4): Rest, Rested, ComfortTest, RestTest

### Community 124 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 126 - "Tex"
Cohesion: 0.15
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 127 - ".person"
Cohesion: 0.16
Nodes (4): 12. The bond book, BondWeb, BondFriends, HomeHangout

### Community 128 - "AnswerTag"
Cohesion: 0.08
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 131 - ".page"
Cohesion: 0.29
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 132 - "creator/preview.py"
Cohesion: 0.22
Nodes (7): draw_player(), grown(), _label(), lineup(), samples(), stage_scale(), stages_sheet()

### Community 134 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 135 - "Kind"
Cohesion: 0.17
Nodes (11): Kind, CLAN_SUMMONS, GIFT, INVITATION, LANDLADY, NEIGHBOUR, NOTE, STIPEND (+3 more)

### Community 136 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 137 - "catalogue.py"
Cohesion: 0.17
Nodes (10): story_reserved_family_names(), block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table() (+2 more)

### Community 138 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 140 - "NamesTest"
Cohesion: 0.25
Nodes (4): 1 Name, Names, PlayerName, NamesTest

### Community 141 - "Keepsake"
Cohesion: 0.15
Nodes (7): Keepsake, Kind, CLAN, FESTIVAL, GIFT, QUEST, STORY

### Community 146 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 147 - ".receive"
Cohesion: 0.35
Nodes (3): Gifts, Received, GiftsTest

### Community 148 - "Pantry"
Cohesion: 0.35
Nodes (3): Food, Meal, Pantry

### Community 149 - "Custom blocks"
Cohesion: 0.15
Nodes (13): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+5 more)

### Community 150 - ".run"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 151 - "Template"
Cohesion: 0.24
Nodes (4): Branch, Step, Template, Twist

### Community 155 - "SquadPlan"
Cohesion: 0.32
Nodes (3): Band, Mate, SquadPlan

### Community 158 - "Tier"
Cohesion: 0.10
Nodes (13): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT, Tier, A (+5 more)

### Community 160 - "State"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 162 - "Tier"
Cohesion: 0.12
Nodes (9): Score, Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY, Practice (+1 more)

### Community 164 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), merchant_camp_talk(), S, twist()

### Community 170 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 172 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

## Knowledge Gaps
- **325 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+320 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1427 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **41 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `.bond` to `.page`, `.friends`, `.person`, `.receive`, `GossipTest`, `SquadTest`, `.tier`, `Playthrough`, `.effectiveLevel`, `Question`, `Person`, `map`, `.classic`, `list`, `VillageScaleTest`, `Bond`, `.of`, `Deed`, `.romance`, `Squad`, `Playthrough.java`, `Value`, `.day`, `Title`, `Village`, `Seeds`, `Conflict`, `VisitsTest`, `.person`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _325 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Roster` be split into smaller, more focused modules?**
  _Cohesion score 0.08502024291497975 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `kit_uchiha.py`, `solid`, `rnd`, `kit_hagane.py`, `kit_akimichi.py`, `cel_box`, `kit_suzuran.py`, `Face`, `kit_rugged.py`, `strip_fabric`, `kit_hyuga.py`, `kit_nara.py`, `kit_haruno.py`, `kit_kinoshita.py`, `wide_sleeves`, `kit_field.py`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Meters`, `Story bible`, `.person`, `GossipTest`, `.tier`, `Question`, `Person`, `Memory`, `Meters`, `.romance`, `Life together`, `Label`, `Value`, `ClanRelations`, `.day`, `Village`, `Personality`, `Conflict`, `.person`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Should `Meters` be split into smaller, more focused modules?**
  _Cohesion score 0.13538461538461538 - nodes in this community are weakly interconnected._