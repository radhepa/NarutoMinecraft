# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 184 files · ~244,365 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3315 nodes · 7931 edges · 146 communities (113 shown, 33 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 913 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1deb3adb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- creator.py
- mkit.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- rnd
- kit_inuzuka.py
- mockups.py
- .all
- Economy
- Catalogue
- bell_print
- 7. Systems in the beta
- Personality
- masks.py
- Look
- kit_rugged.py
- CreatorRules
- fabric
- .person
- .num
- Desk
- konoha/preview.py
- Character creation
- kit_market.py
- kit_kinoshita.py
- Missions
- 5. Data formats built for the whole story
- render_kit.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- missions.py
- 4. Technical architecture
- 6. The map
- creator/preview.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- .get
- k
- Player
- Playthrough
- paint.py
- .strings
- .choices
- Rng
- Box
- Seeds
- Face
- NamesTest
- Json
- Act
- Stage
- BondWorld
- AgeStage
- Conflict
- VarietyGuard
- .classic
- solid
- Meters
- catalogue.py
- kit_uchiha.py
- Village
- VillageScaleTest
- Bond
- .of
- VillageSim.java
- .look
- Def
- Restyle
- Deed
- Squad
- kit_hagane.py
- Tier
- .snapshot
- Json
- Rng
- Mood
- org.junit.jupiter.api.Test
- 4.3 The noble clans
- S
- .page
- Peeve
- Experience
- Meters
- Question
- Recruitment
- Meter
- End
- mission
- kit_akimichi.py
- .read
- Side quests
- 4.4 The minor clans
- Kind
- 2. Quest framework
- catalogue.py
- 8. Beta catalogue
- katana
- senbon
- .talk
- 7. Inter-clan politics as quests
- .answer
- vial
- Plan
- Person
- blocks.py
- Title
- kokuto
- Data
- Side quest secrets
- Tex
- State
- 4. Clan quest lines
- AnswerTag
- Kind
- mesh_shirt
- Every building
- kit_tsuchigumo.py
- kit_haruno.py
- Konoha: the build plan
- Custom blocks
- Label
- Template
- noren
- .receive
- shade
- shade
- .everyKeyTheEngineEmitsIsListed
- Life together
- Mission catalogue
- QuestionsTest
- The village
- Naruto Minecraft

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 184 edges
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

## Communities (146 total, 33 thin omitted)

### Community 0 - "creator.py"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

### Community 1 - "mkit.py"
Cohesion: 0.18
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 2 - "Clans"
Cohesion: 0.15
Nodes (12): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+4 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.11
Nodes (21): render_player(), new_canvas(), save_canvas(), backdrop(), Canvas, Character, clan_renders(), composite() (+13 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.02
Nodes (49): back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps() (+41 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "rnd"
Cohesion: 0.03
Nodes (35): sprigs(), back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves() (+27 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 12 - "Economy"
Cohesion: 0.09
Nodes (11): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+3 more)

### Community 13 - "Catalogue"
Cohesion: 0.16
Nodes (8): Catalogue, Mode, CLASSIC, VARIED, DeskDays, Profile, Run, SimulationTest

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - "Personality"
Cohesion: 0.09
Nodes (9): Personality, Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH, Reaction (+1 more)

### Community 17 - "masks.py"
Cohesion: 0.22
Nodes (5): How the pieces work, mesh(), tanto(), beak(), ears()

### Community 18 - "Look"
Cohesion: 0.14
Nodes (4): 9. Age stages, Look, Result, RestyleAndGrowUpTest

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "CreatorRules"
Cohesion: 0.20
Nodes (5): 13. Code, and what waits for Phase 0, Choices, CreatorRules, Outfit, Roots

### Community 21 - "fabric"
Cohesion: 0.03
Nodes (56): leg_cloth(), shirt(), waist(), body(), arm_guards(), cargo(), gloves(), half_sleeves() (+48 more)

### Community 22 - ".person"
Cohesion: 0.10
Nodes (11): Activity, BondEvent, Answer, FollowUp, Highlight, Invitation, Outcome, Plan (+3 more)

### Community 24 - "Desk"
Cohesion: 0.13
Nodes (8): Desk, Offer, Rank, A, B, C, D, S

### Community 25 - "konoha/preview.py"
Cohesion: 0.16
Nodes (13): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+5 more)

### Community 26 - "Character creation"
Cohesion: 0.11
Nodes (19): 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair, 3. Where the creator sits in the opening (+11 more)

### Community 27 - "kit_market.py"
Cohesion: 0.04
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "render_kit.py"
Cohesion: 0.18
Nodes (7): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 32 - "outputs"
Cohesion: 0.09
Nodes (29): build(), build_all(), catalog(), general_pool(), hex_rgb(), json_text(), load_all_groups(), load_characters() (+21 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "missions.py"
Cohesion: 0.18
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "creator/preview.py"
Cohesion: 0.17
Nodes (7): draw_player(), grown(), _label(), lineup(), samples(), stage_scale(), stages_sheet()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 42 - "k"
Cohesion: 0.03
Nodes (38): deep_hood(), high_collar(), hood_down(), lenses(), arm_bone(), arm_x(), belt(), collar() (+30 more)

### Community 44 - "Playthrough"
Cohesion: 0.08
Nodes (16): 15. Pacing, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+8 more)

### Community 45 - "paint.py"
Cohesion: 0.02
Nodes (69): Shared helpers, back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock() (+61 more)

### Community 46 - ".strings"
Cohesion: 0.25
Nodes (3): Band, Mate, SquadPlan

### Community 49 - "Box"
Cohesion: 0.07
Nodes (10): strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece, piece_corners() (+2 more)

### Community 50 - "Seeds"
Cohesion: 0.18
Nodes (3): 5. Personality, Rng, Seeds

### Community 51 - "Face"
Cohesion: 0.20
Nodes (6): drawn_line(), button(), darken_rows(), line(), rivets(), Face

### Community 52 - "NamesTest"
Cohesion: 0.19
Nodes (5): 10. How residents address you, 1 Name, Names, PlayerName, NamesTest

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "BondWorld"
Cohesion: 0.07
Nodes (4): 20. What the roadmap asks of bonds, BondEffects, BondWorld, Standing

### Community 57 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 58 - "Conflict"
Cohesion: 0.08
Nodes (8): 11. Kindling Bond, 13. Data formats, BondDialogue, Conflict, Household, Bonfire, Flame, Kindling

### Community 59 - "VarietyGuard"
Cohesion: 0.11
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 61 - ".classic"
Cohesion: 0.13
Nodes (5): 8. The village talks, BondDialogueTest, ConditionsAndEffectsTest, GossipTest, KindlingAndBookTest

### Community 62 - "solid"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 63 - "Meters"
Cohesion: 0.15
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 64 - "catalogue.py"
Cohesion: 0.21
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 65 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 66 - "Village"
Cohesion: 0.05
Nodes (22): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+14 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.12
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.11
Nodes (7): Stage, ADULT, CHILD, TEEN, ConflictTest, Leaf, MemoryTest

### Community 71 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 72 - "Def"
Cohesion: 0.12
Nodes (5): Def, Size, BIG, NOTABLE, SMALL

### Community 73 - "Restyle"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 76 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 77 - "Tier"
Cohesion: 0.13
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 81 - "Mood"
Cohesion: 0.15
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "org.junit.jupiter.api.Test"
Cohesion: 0.08
Nodes (3): SquadTest, SeedsTest, AgeStageTest

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), merchant_camp_talk(), S, twist()

### Community 85 - ".page"
Cohesion: 0.11
Nodes (7): 3. Levels and story gates, BondBook, Fact, MemoryLine, Page, Levels, LevelsTest

### Community 86 - "Peeve"
Cohesion: 0.08
Nodes (23): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+15 more)

### Community 87 - "Experience"
Cohesion: 0.17
Nodes (10): Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION, SPAR (+2 more)

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (7): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 93 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 94 - "kit_akimichi.py"
Cohesion: 0.10
Nodes (10): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+2 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "catalogue.py"
Cohesion: 0.11
Nodes (5): build(), build(), build(), paste(), scene()

### Community 101 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 104 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 105 - ".talk"
Cohesion: 0.17
Nodes (5): Conversation, Reply, Topic, LifeEvents, News

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - ".answer"
Cohesion: 0.19
Nodes (3): Answered, Outcome, Questions

### Community 110 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 113 - "blocks.py"
Cohesion: 0.16
Nodes (15): Streets, auto_uv(), block(), Block, box(), check(), compile_all(), main() (+7 more)

### Community 114 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 115 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 118 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 119 - "Tex"
Cohesion: 0.15
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 120 - "State"
Cohesion: 0.25
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 121 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 122 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 123 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 126 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 128 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (7): glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 129 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 130 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 131 - "Custom blocks"
Cohesion: 0.15
Nodes (13): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+5 more)

### Community 132 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 134 - "Template"
Cohesion: 0.21
Nodes (4): Branch, Step, Template, Twist

### Community 136 - "noren"
Cohesion: 0.19
Nodes (9): 2. Style guide: the Konoha kit, By building type, Facades and shop fronts, Lanterns, Shared palette, awning(), facing_states(), noren() (+1 more)

### Community 137 - ".receive"
Cohesion: 0.18
Nodes (5): 12. The bond book, BondWeb, Gifts, Received, GiftsTest

### Community 141 - "shade"
Cohesion: 0.24
Nodes (7): 6. Prototypes, Interior fittings, Roofs, kawara_ridge(), tatami(), tatami_top(), shade()

### Community 143 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.33
Nodes (3): DialogueKeys, DialogueKeysTest, 10. Content plan

### Community 150 - "Life together"
Cohesion: 0.20
Nodes (10): 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 6. Conversation, 7. Questions and choices, 8. Data and quest hooks (+2 more)

### Community 151 - "Mission catalogue"
Cohesion: 0.29
Nodes (7): A rank, ANBU operations, B rank, C rank, D rank, Mission catalogue, S rank

### Community 153 - "QuestionsTest"
Cohesion: 0.19
Nodes (3): QuestionsCompiledTest, QuestionsTest, SampleQuestions

### Community 154 - "The village"
Cohesion: 0.29
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 162 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

## Knowledge Gaps
- **234 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+229 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1224 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **33 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `.receive`, `.person`, `QuestionsTest`, `Playthrough`, `Stage`, `Conflict`, `list`, `.classic`, `Village`, `VillageScaleTest`, `Bond`, `.of`, `VillageSim.java`, `Deed`, `Squad`, `.snapshot`, `org.junit.jupiter.api.Test`, `.page`, `Meters`, `Question`, `Recruitment`, `.read`, `.talk`, `.answer`, `Person`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _234 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `creator.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07058001397624039 - nodes in this community are weakly interconnected._
- **Why does `solid()` connect `solid` to `kit_tsuchigumo.py`, `kit_haruno.py`, `kit_senju.py`, `rnd`, `masks.py`, `kit_rugged.py`, `fabric`, `kit_market.py`, `kit_kinoshita.py`, `k`, `paint.py`, `Box`, `solid`, `kit_uchiha.py`, `kit_hagane.py`, `kit_akimichi.py`, `katana`, `senbon`, `kokuto`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11282051282051282 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `kit_tsuchigumo.py`, `kit_haruno.py`, `kit_senju.py`, `solid`, `rnd`, `kit_inuzuka.py`, `bell_print`, `kit_rugged.py`, `fabric`, `kit_market.py`, `kit_kinoshita.py`, `paint.py`, `Face`, `solid`, `kit_uchiha.py`, `kit_hagane.py`, `kit_akimichi.py`, `senbon`, `vial`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Should `solid` be split into smaller, more focused modules?**
  _Cohesion score 0.02282828282828283 - nodes in this community are weakly interconnected._