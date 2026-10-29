# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 184 files · ~245,092 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3319 nodes · 7951 edges · 143 communities (110 shown, 33 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 918 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fab77c4f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- mkit.py
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- kit_kurama.py
- kit_hagane.py
- rnd
- fabric
- Economy
- VarietyGuard
- kit_suzuran.py
- 7. Systems in the beta
- Activity
- creator.py
- Desk
- k
- Plan
- Missions
- rot_matrix
- .receive
- Meter
- Look
- CreatorRules
- kit_market.py
- kit_kinoshita.py
- org.junit.jupiter.api.Test
- 5. Data formats built for the whole story
- Catalogue
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_shiranui.py
- 4. Technical architecture
- 6. The map
- blocks.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- .get
- kit_akimichi.py
- kokuto
- Run
- .num
- render_kit.py
- mockups.py
- Personality
- Box
- missions.py
- Player
- kit_morino.py
- Json
- Act
- Stage
- preview.py
- org.junit.jupiter.api.Test
- kit_tsuchigumo.py
- Rng
- Character creation
- Kind
- .person
- .everyKeyTheEngineEmitsIsListed
- Squad
- Peeve
- VillageScaleTest
- Bond
- .of
- Bonds
- Question
- Def
- Levels
- Deed
- Tex
- Seeds
- AnswerTag
- BondWorld
- Face
- Konoha: the build plan
- Mood
- .read
- 4.3 The noble clans
- kit_haruno.py
- .look
- Value
- NamesTest
- SampleQuestions
- paint.py
- .tier
- Restyle
- Title
- .name
- creator/preview.py
- AgeStage
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- Meters
- Label
- org.junit.jupiter.api.Test
- Village
- Every building
- Kind
- 7. Inter-clan politics as quests
- .title
- Custom blocks
- kit_household.py
- SquadTest
- .effectiveLevel
- Template
- Json
- .all
- catalogue.py
- Rng
- .strings
- Garment
- 8. Beta catalogue
- pathlib
- 4. Clan quest lines
- Conflict
- .write
- kit_kunoichi.py
- Life together
- S
- Rng
- noren
- mission
- End
- Power
- shade
- QuestionsCompiledTest

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 185 edges
3. `solid()` - 151 edges
4. `Act` - 121 edges
5. `fabric()` - 109 edges
6. `Bond` - 66 edges
7. `Village` - 63 edges
8. `strip_fabric()` - 59 edges
9. `Person` - 53 edges
10. `stamp()` - 47 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `7. Questions and choices` --references--> `Question`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Question.java
- `9. Pacing with time together` --references--> `TimeAndPacingTest`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `11. What waits for Phase 0` --references--> `Player`  [INFERRED]
  MISSIONS.md → progression/missions/src/main/java/dev/shinobi/progression/mission/Player.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java

## Import Cycles
- None detected.

## Communities (143 total, 33 thin omitted)

### Community 0 - "mkit.py"
Cohesion: 0.18
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.25
Nodes (8): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.15
Nodes (17): new_canvas(), backdrop(), Canvas, Character, clan_renders(), cube_quads(), font(), general_renders() (+9 more)

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

### Community 9 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 10 - "rnd"
Cohesion: 0.04
Nodes (29): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw() (+21 more)

### Community 11 - "fabric"
Cohesion: 0.03
Nodes (53): Shared helpers, How the pieces work, leg_cloth(), shirt(), waist(), belt(), body(), collar() (+45 more)

### Community 12 - "Economy"
Cohesion: 0.09
Nodes (11): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+3 more)

### Community 13 - "VarietyGuard"
Cohesion: 0.11
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - "Activity"
Cohesion: 0.10
Nodes (10): Activity, Answer, FollowUp, Highlight, Invitation, Outcome, Plan, Together (+2 more)

### Community 17 - "creator.py"
Cohesion: 0.08
Nodes (19): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), roll_look() (+11 more)

### Community 18 - "Desk"
Cohesion: 0.13
Nodes (8): Desk, Offer, Rank, A, B, C, D, S

### Community 19 - "k"
Cohesion: 0.03
Nodes (39): deep_hood(), high_collar(), hood_down(), lenses(), collar(), tape(), sword_strap(), hakama_legs() (+31 more)

### Community 20 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 21 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 22 - "rot_matrix"
Cohesion: 0.33
Nodes (3): Piece, piece_corners(), world_bounds()

### Community 23 - ".receive"
Cohesion: 0.35
Nodes (3): Gifts, Received, GiftsTest

### Community 24 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 25 - "Look"
Cohesion: 0.13
Nodes (7): 13. Code, and what waits for Phase 0, 7. Locked and changeable, 9. Age stages, GrowUp, Look, Result, RestyleAndGrowUpTest

### Community 26 - "CreatorRules"
Cohesion: 0.18
Nodes (5): Choices, CreatorRules, Outfit, Roots, Data

### Community 27 - "kit_market.py"
Cohesion: 0.04
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "Catalogue"
Cohesion: 0.16
Nodes (8): Catalogue, Mode, CLASSIC, VARIED, DeskDays, Profile, Run, SimulationTest

### Community 32 - "wardrobe.py"
Cohesion: 0.08
Nodes (34): build(), build_all(), catalog(), clan_bottoms(), clan_resident(), compatible(), general_pool(), general_resident() (+26 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "kit_shiranui.py"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "blocks.py"
Cohesion: 0.12
Nodes (23): 6. Prototypes, Lanterns, Roofs, Streets, auto_uv(), block(), Block, box() (+15 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 42 - "kit_akimichi.py"
Cohesion: 0.10
Nodes (10): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+2 more)

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.08
Nodes (16): 15. Pacing, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+8 more)

### Community 46 - "render_kit.py"
Cohesion: 0.12
Nodes (10): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street() (+2 more)

### Community 47 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 48 - "Personality"
Cohesion: 0.12
Nodes (3): Personality, Reaction, ReactionTest

### Community 49 - "Box"
Cohesion: 0.12
Nodes (3): strip_line(), Box, Layer

### Community 50 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 52 - "kit_morino.py"
Cohesion: 0.08
Nodes (13): arm_bone(), arm_x(), armband(), back_crest(), clipped(), coat_skirts(), combed_back(), head_cloth() (+5 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.10
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "preview.py"
Cohesion: 0.14
Nodes (15): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+7 more)

### Community 58 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 61 - "Character creation"
Cohesion: 0.11
Nodes (19): 10. How residents address you, 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair (+11 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - ".person"
Cohesion: 0.18
Nodes (4): Answered, Outcome, Questions, QuestionsTest

### Community 64 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.25
Nodes (3): DialogueKeys, DialogueKeysTest, 10. Content plan

### Community 65 - "Squad"
Cohesion: 0.08
Nodes (3): BondEffects, Departure, Squad

### Community 66 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.13
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (4): 12. The bond book, Bond, BondConditions, BondWeb

### Community 69 - ".of"
Cohesion: 0.12
Nodes (7): Stage, ADULT, CHILD, TEEN, ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.09
Nodes (14): 13. Data formats, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+6 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.18
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.09
Nodes (9): 8. The village talks, Deed, Know, Gossip, Source, HEARD, SEEN, SELF (+1 more)

### Community 75 - "Tex"
Cohesion: 0.14
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 76 - "Seeds"
Cohesion: 0.18
Nodes (3): 5. Personality, Rng, Seeds

### Community 77 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 79 - "Face"
Cohesion: 0.25
Nodes (4): button(), darken_rows(), rivets(), Face

### Community 80 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 86 - "Value"
Cohesion: 0.15
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 87 - "NamesTest"
Cohesion: 0.21
Nodes (4): 1 Name, Names, PlayerName, NamesTest

### Community 89 - "paint.py"
Cohesion: 0.02
Nodes (61): back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock(), ring_shell() (+53 more)

### Community 90 - ".tier"
Cohesion: 0.07
Nodes (11): 11. Kindling Bond, BondBook, Fact, MemoryLine, Page, Household, Bonfire, Flame (+3 more)

### Community 91 - "Restyle"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 92 - "Title"
Cohesion: 0.22
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.25
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 94 - "creator/preview.py"
Cohesion: 0.18
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 95 - "AgeStage"
Cohesion: 0.17
Nodes (4): AgeStage, ADULT, CHILD, TEEN

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "Person"
Cohesion: 0.12
Nodes (3): 20. What the roadmap asks of bonds, Person, Schedule

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "org.junit.jupiter.api.Test"
Cohesion: 0.14
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, GossipTest, VillageTest

### Community 103 - "Village"
Cohesion: 0.06
Nodes (11): 18. Village scale, Base, ClanRelations, SocialTie, SocietyHook, House, Tier, BACKGROUND (+3 more)

### Community 104 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 105 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 108 - "Custom blocks"
Cohesion: 0.12
Nodes (15): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+7 more)

### Community 109 - "kit_household.py"
Cohesion: 0.05
Nodes (23): bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta(), ichimatsu() (+15 more)

### Community 112 - ".effectiveLevel"
Cohesion: 0.15
Nodes (6): Conversation, Reply, Topic, LifeEvents, News, 6. Conversation

### Community 113 - "Template"
Cohesion: 0.21
Nodes (4): Branch, Step, Template, Twist

### Community 117 - "catalogue.py"
Cohesion: 0.19
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 119 - ".strings"
Cohesion: 0.25
Nodes (3): Band, Mate, SquadPlan

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 122 - "pathlib"
Cohesion: 0.12
Nodes (3): build(), build(), build()

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 126 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 127 - "Life together"
Cohesion: 0.22
Nodes (9): 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Questions and choices, 8. Data and quest hooks, 9. Pacing with time together (+1 more)

### Community 128 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), merchant_camp_talk(), S, twist()

### Community 131 - "noren"
Cohesion: 0.24
Nodes (7): 2. Style guide: the Konoha kit, By building type, Facades and shop fronts, Shared palette, awning(), facing_states(), noren()

### Community 133 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 134 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 135 - "Power"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

## Knowledge Gaps
- **234 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+229 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1224 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **33 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `Activity`, `.receive`, `Run`, `Stage`, `Playthrough.java`, `.person`, `Squad`, `VillageScaleTest`, `Bond`, `.of`, `Bonds`, `Question`, `Deed`, `.read`, `.tier`, `Person`, `org.junit.jupiter.api.Test`, `Village`, `.title`, `SquadTest`, `.effectiveLevel`, `.write`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _234 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `kit_uchiha.py`, `kit_senju.py`, `solid`, `kit_kurama.py`, `kit_hagane.py`, `rnd`, `fabric`, `kit_suzuran.py`, `kit_market.py`, `kit_kinoshita.py`, `kit_shiranui.py`, `kit_akimichi.py`, `kit_morino.py`, `kit_tsuchigumo.py`, `Face`, `kit_haruno.py`, `paint.py`, `Custom blocks`, `kit_household.py`, `kit_kunoichi.py`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1471264367816092 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Person`, `Bond`, `Meters`, `Story bible`, `Village`, `Levels`, `Deed`, `Run`, `Seeds`, `Personality`, `Mood`, `Value`, `Stage`, `.tier`, `Conflict`, `.write`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Should `solid` be split into smaller, more focused modules?**
  _Cohesion score 0.02661064425770308 - nodes in this community are weakly interconnected._