# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 184 files · ~244,493 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 3317 nodes · 7943 edges · 135 communities (103 shown, 32 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 916 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f808129e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- senbon
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- creator.py
- Story bible
- kit_kurama.py
- mkit.py
- rnd
- fabric
- Economy
- paint.py
- paint.py
- 7. Systems in the beta
- .roll
- blocks.py
- mockups.py
- kit_rugged.py
- org.junit.jupiter.api.Test
- Plan
- VarietyGuard
- Desk
- Meters
- wide_sleeves
- Missions
- kit_market.py
- kit_kinoshita.py
- .choices
- 5. Data formats built for the whole story
- Look
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- .answer
- 4. Technical architecture
- 6. The map
- Catalogue
- 8. The beta, chapter by chapter
- 9. Delivery plan
- CreatorRules
- k
- kokuto
- Playthrough
- konoha/preview.py
- Life together
- missions.py
- .get
- Box
- .num
- solid
- Tex
- Player
- Act
- Stage
- catalogue.py
- kit_hagane.py
- .greeting
- Character creation
- creator/preview.py
- Kind
- Json
- .everyKeyTheEngineEmitsIsListed
- Squad
- Rng
- VillageScaleTest
- Bond
- .of
- pathlib
- .valuesAndToneLandOnTheirPersonalityAndOppositePolesContradict
- Def
- Levels
- Deed
- render_kit.py
- Every building
- AnswerTag
- BondWorld
- Face
- Seeds
- Mood
- .read
- 4.3 The noble clans
- kit_haruno.py
- Konoha: the build plan
- Personality
- Village
- SampleQuestions
- Template
- .tier
- Meter
- .name
- kit_tsuchigumo.py
- NamesTest
- Custom blocks
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- .all
- .strings
- .classic
- .look
- Kind
- Question
- 7. Inter-clan politics as quests
- Conflict
- Restyle
- kit_household.py
- .receive
- .talk
- Tier
- AgeStage
- Json
- Rng
- noren
- .write
- News
- S
- 8. Beta catalogue
- Rng
- 4. Clan quest lines
- mission
- End
- kit_kunoichi.py
- street.py
- shade
- Data

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

## Communities (135 total, 32 thin omitted)

### Community 0 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

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
Cohesion: 0.08
Nodes (19): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), roll_look() (+11 more)

### Community 7 - "Story bible"
Cohesion: 0.05
Nodes (39): Commits, graphify, Naruto Minecraft, A rank, ANBU operations, B rank, C rank, D rank (+31 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "mkit.py"
Cohesion: 0.18
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

### Community 10 - "rnd"
Cohesion: 0.05
Nodes (27): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw() (+19 more)

### Community 11 - "fabric"
Cohesion: 0.03
Nodes (53): Shared helpers, How the pieces work, leg_cloth(), shirt(), waist(), belt(), body(), collar() (+45 more)

### Community 12 - "Economy"
Cohesion: 0.09
Nodes (11): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+3 more)

### Community 13 - "paint.py"
Cohesion: 0.02
Nodes (65): back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock(), ring_shell() (+57 more)

### Community 14 - "paint.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - ".roll"
Cohesion: 0.10
Nodes (10): Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan, Together (+2 more)

### Community 17 - "blocks.py"
Cohesion: 0.13
Nodes (21): 6. Prototypes, Lanterns, Roofs, Streets, auto_uv(), block(), Block, box() (+13 more)

### Community 18 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 21 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 22 - "VarietyGuard"
Cohesion: 0.11
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 23 - "Desk"
Cohesion: 0.13
Nodes (8): Desk, Offer, Rank, A, B, C, D, S

### Community 25 - "wide_sleeves"
Cohesion: 0.18
Nodes (7): arm_bone(), arm_x(), armband(), roll(), seal_script(), seal_tags(), wide_sleeves()

### Community 26 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 27 - "kit_market.py"
Cohesion: 0.04
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "Look"
Cohesion: 0.14
Nodes (6): 13. Code, and what waits for Phase 0, 9. Age stages, GrowUp, Look, Result, RestyleAndGrowUpTest

### Community 32 - "wardrobe.py"
Cohesion: 0.09
Nodes (29): build(), build_all(), catalog(), general_pool(), hex_rgb(), json_text(), load_all_groups(), load_characters() (+21 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - ".answer"
Cohesion: 0.20
Nodes (4): Answered, Outcome, Questions, QuestionsTest

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "Catalogue"
Cohesion: 0.16
Nodes (8): Catalogue, Mode, CLASSIC, VARIED, DeskDays, Profile, Run, SimulationTest

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "CreatorRules"
Cohesion: 0.21
Nodes (4): Choices, CreatorRules, Outfit, Roots

### Community 42 - "k"
Cohesion: 0.03
Nodes (35): deep_hood(), high_collar(), hood_down(), lenses(), back_crest(), shin_wraps(), flick(), gourd() (+27 more)

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Playthrough"
Cohesion: 0.11
Nodes (15): 15. Pacing, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+7 more)

### Community 45 - "konoha/preview.py"
Cohesion: 0.16
Nodes (13): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+5 more)

### Community 46 - "Life together"
Cohesion: 0.22
Nodes (9): 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Questions and choices, 8. Data and quest hooks, 9. Pacing with time together (+1 more)

### Community 47 - "missions.py"
Cohesion: 0.17
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 49 - "Box"
Cohesion: 0.08
Nodes (9): strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece, piece_corners() (+1 more)

### Community 51 - "solid"
Cohesion: 0.03
Nodes (43): drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), side_stripe(), sleeve_roll() (+35 more)

### Community 52 - "Tex"
Cohesion: 0.14
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.10
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "catalogue.py"
Cohesion: 0.18
Nodes (11): check(), main(), block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary() (+3 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 59 - "Character creation"
Cohesion: 0.11
Nodes (19): 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair, 3. Where the creator sits in the opening (+11 more)

### Community 61 - "creator/preview.py"
Cohesion: 0.16
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 64 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.33
Nodes (3): DialogueKeys, DialogueKeysTest, 10. Content plan

### Community 65 - "Squad"
Cohesion: 0.06
Nodes (4): BondEffects, Departure, Squad, Run

### Community 67 - "VillageScaleTest"
Cohesion: 0.09
Nodes (8): ClanProfile, Stage, ADULT, CHILD, TEEN, Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (4): Bond, BondConditions, BondWeb, FollowUp

### Community 69 - ".of"
Cohesion: 0.12
Nodes (4): ConflictTest, GossipTest, Leaf, MemoryTest

### Community 70 - "pathlib"
Cohesion: 0.12
Nodes (3): build(), build(), build()

### Community 72 - "Def"
Cohesion: 0.08
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.16
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.09
Nodes (9): 8. The village talks, Deed, Know, Gossip, Source, HEARD, SEEN, SELF (+1 more)

### Community 75 - "render_kit.py"
Cohesion: 0.19
Nodes (7): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 76 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 77 - "AnswerTag"
Cohesion: 0.11
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 79 - "Face"
Cohesion: 0.20
Nodes (6): drawn_line(), button(), darken_rows(), line(), rivets(), Face

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 86 - "Personality"
Cohesion: 0.05
Nodes (35): 20. What the roadmap asks of bonds, 5. Personality, Lean, Base, Peeve, BRAGGING, COWARDICE, CRUELTY (+27 more)

### Community 87 - "Village"
Cohesion: 0.04
Nodes (22): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+14 more)

### Community 89 - "Template"
Cohesion: 0.21
Nodes (4): Branch, Step, Template, Twist

### Community 90 - ".tier"
Cohesion: 0.07
Nodes (12): 11. Kindling Bond, 12. The bond book, BondBook, Fact, MemoryLine, Page, Household, Bonfire (+4 more)

### Community 91 - "Meter"
Cohesion: 0.15
Nodes (6): Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - ".name"
Cohesion: 0.08
Nodes (14): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS, Title (+6 more)

### Community 93 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (7): glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 94 - "NamesTest"
Cohesion: 0.21
Nodes (5): 10. How residents address you, 1 Name, Names, PlayerName, NamesTest

### Community 95 - "Custom blocks"
Cohesion: 0.14
Nodes (14): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+6 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 101 - ".strings"
Cohesion: 0.25
Nodes (3): Band, Mate, SquadPlan

### Community 102 - ".classic"
Cohesion: 0.13
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, SquadTest, VillageTest

### Community 103 - ".look"
Cohesion: 0.24
Nodes (3): LifeRoll, Rolled, LifeRollTest

### Community 104 - "Kind"
Cohesion: 0.17
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "Conflict"
Cohesion: 0.13
Nodes (7): Conflict, State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 108 - "Restyle"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 109 - "kit_household.py"
Cohesion: 0.05
Nodes (24): arm_cloth(), bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta() (+16 more)

### Community 110 - ".receive"
Cohesion: 0.35
Nodes (3): Gifts, Received, GiftsTest

### Community 112 - ".talk"
Cohesion: 0.33
Nodes (4): Conversation, Reply, Topic, 6. Conversation

### Community 113 - "Tier"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 114 - "AgeStage"
Cohesion: 0.17
Nodes (4): AgeStage, ADULT, CHILD, TEEN

### Community 117 - "noren"
Cohesion: 0.24
Nodes (7): 2. Style guide: the Konoha kit, By building type, Facades and shop fronts, Shared palette, awning(), facing_states(), noren()

### Community 120 - "S"
Cohesion: 0.22
Nodes (5): 6. Squad missions, travel(), merchant_camp_talk(), S, twist()

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 124 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 125 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 126 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

## Knowledge Gaps
- **234 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+229 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1224 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **32 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BondWorld` connect `BondWorld` to `.roll`, `.answer`, `Playthrough`, `Stage`, `.greeting`, `Playthrough.java`, `Squad`, `VillageScaleTest`, `Bond`, `.of`, `Deed`, `.read`, `Village`, `.tier`, `Person`, `.classic`, `Question`, `.receive`, `.talk`, `.write`, `News`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _234 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `k()` connect `k` to `senbon`, `kit_uchiha.py`, `kit_senju.py`, `kit_kurama.py`, `rnd`, `fabric`, `paint.py`, `paint.py`, `kit_rugged.py`, `wide_sleeves`, `kit_market.py`, `kit_kinoshita.py`, `solid`, `kit_hagane.py`, `Face`, `kit_haruno.py`, `kit_tsuchigumo.py`, `kit_household.py`, `kit_kunoichi.py`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12312312312312312 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Village` to `Person`, `VillageScaleTest`, `.greeting`, `Story bible`, `Levels`, `Deed`, `Conflict`, `Playthrough`, `.roll`, `Mood`, `.write`, `Stage`, `Personality`, `Meters`, `.tier`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Should `creator.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08405797101449275 - nodes in this community are weakly interconnected._