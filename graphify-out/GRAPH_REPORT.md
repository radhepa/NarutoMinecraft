# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 149 files · ~201,581 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2912 nodes · 6823 edges · 176 communities (120 shown, 56 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 743 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `116e2496`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_nara.py
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- kit_hagane.py
- kit_yuhi.py
- fabric
- kit_aburame.py
- kit_shinobi.py
- kit_suzuran.py
- 7. Systems in the beta
- Activity
- creator.py
- kit_hyuga.py
- kit_rugged.py
- Plan
- kit_tobari.py
- rot_matrix
- .receive
- Meter
- Look
- CreatorRules
- kit_market.py
- kit_kinoshita.py
- org.junit.jupiter.api.Test
- 5. Data formats built for the whole story
- kit_field.py
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_shiranui.py
- 4. Technical architecture
- 6. The map
- blocks.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- kit_yamanaka.py
- paint.py
- kit_namiashi.py
- Run
- paint.py
- render_kit.py
- mockups.py
- Personality
- Box
- solid
- kit_specialist.py
- kit_morino.py
- kit_gekko.py
- Act
- Stage
- preview.py
- org.junit.jupiter.api.Test
- kit_tsuchigumo.py
- bandage_turns
- Playthrough.java
- Character creation
- Kind
- .person
- .everyKeyTheEngineEmitsIsListed
- Squad
- k
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
- QuestionsTest
- cel_box
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
- Memory
- Label
- org.junit.jupiter.api.Test
- Village
- Every building
- Kind
- 7. Inter-clan politics as quests
- .effectiveLevel
- Custom blocks
- kit_household.py
- SquadTest
- .effectiveLevel
- Power
- Json
- ROADMAP.md
- catalogue.py
- Rng
- kit_inuzuka.py
- Garment
- 8. Beta catalogue
- pathlib
- 4. Clan quest lines
- How the pieces work
- .write
- kit_kunoichi.py
- kit_nara.py
- .page
- shade
- rnd
- noren
- BondConditions
- .day
- seal_script
- Power
- Shared helpers
- stamp
- Recruitment
- re
- wide_sleeves
- The village
- resolve
- QuestionsCompiledTest
- street.py
- fur_face
- tape
- forehead_protector
- lames
- sode
- blouse
- knee_guards
- sword_strap
- brush_stroke
- kimono_sleeves
- side_fringe
- bib
- gathered_ankles
- part_line
- wisteria_hem
- tasuki
- pauldron
- sash
- rolled_cuffs
- wave_band
- trench_knife
- scarf
- bandolier
- lantern_tag
- shin_wraps
- clip
- wrap_tie
- waves

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
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Life together` --references--> `Activity`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Activity.java
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java

## Import Cycles
- None detected.

## Communities (176 total, 56 thin omitted)

### Community 0 - "kit_nara.py"
Cohesion: 0.22
Nodes (4): protector_plate(), backward_bandana(), crest(), flicks()

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.15
Nodes (17): new_canvas(), backdrop(), Canvas, Character, clan_renders(), cube_quads(), font(), general_renders() (+9 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.06
Nodes (16): back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps() (+8 more)

### Community 7 - "Story bible"
Cohesion: 0.09
Nodes (23): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines, District quests and one-offs, Filler arcs, How to read this bible (+15 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.12
Nodes (8): back_crest(), bead_clip(), brush_pin(), bun(), ink_clouds(), stamp(), wave_lock(), wrap_front()

### Community 9 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "fabric"
Cohesion: 0.11
Nodes (15): leg_cloth(), waist(), half_sleeves(), arm_cloth(), trouser_legs(), waist(), kimono_sleeves(), tabi_boots() (+7 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_shinobi.py"
Cohesion: 0.20
Nodes (4): anbu_arms(), anbu_plates(), flak_vest(), sandals()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - "Activity"
Cohesion: 0.10
Nodes (11): Activity, BondEvent, Answer, FollowUp, Highlight, Invitation, Outcome, Plan (+3 more)

### Community 17 - "creator.py"
Cohesion: 0.07
Nodes (21): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), Rng (+13 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.08
Nodes (13): bangs(), curtain(), back_sheet(), blunt_fringe(), crest(), ear_panels(), hair_tie(), hakama_legs() (+5 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 21 - "kit_tobari.py"
Cohesion: 0.12
Nodes (10): shirt(), shirt(), decal(), hood_down(), lantern(), mantle(), plain_body(), pleats() (+2 more)

### Community 22 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 23 - ".receive"
Cohesion: 0.38
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
Cohesion: 0.10
Nodes (9): checks(), dots(), furoshiki(), geta(), jika_tabi(), kyahan(), open_front(), sashiko() (+1 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.10
Nodes (9): arm_guards(), cargo(), chain(), gloves(), mesh_arms(), pocket(), shirt(), trousers() (+1 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.12
Nodes (23): catalog(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_eye_colors() (+15 more)

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
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "blocks.py"
Cohesion: 0.15
Nodes (14): Roofs, auto_uv(), Block, box(), check(), compile_all(), kawara_ridge(), main() (+6 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 42 - "paint.py"
Cohesion: 0.15
Nodes (6): flick(), puff(), shoku_disc(), band(), curls_box(), hem()

### Community 43 - "kit_namiashi.py"
Cohesion: 0.20
Nodes (5): back_blade(), crest(), hip_kokuto(), kokuto(), wave_lock()

### Community 44 - "Run"
Cohesion: 0.07
Nodes (25): 15. Pacing, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+17 more)

### Community 45 - "paint.py"
Cohesion: 0.29
Nodes (4): hair_box(), hair_face(), hair_shade(), shell()

### Community 46 - "render_kit.py"
Cohesion: 0.13
Nodes (8): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 47 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 48 - "Personality"
Cohesion: 0.07
Nodes (15): 5. Personality, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS (+7 more)

### Community 49 - "Box"
Cohesion: 0.10
Nodes (5): dark_seams(), strip_line(), Box, Layer, shade()

### Community 50 - "solid"
Cohesion: 0.09
Nodes (12): gourd(), holster(), strap(), face_mask(), white_fang_tanto(), towel_at_neck(), waist_apron(), cane() (+4 more)

### Community 51 - "kit_specialist.py"
Cohesion: 0.12
Nodes (7): bandolier(), coat_skirts(), cross_armband(), ink_stains(), scroll_tube(), seal_trim(), strap()

### Community 52 - "kit_morino.py"
Cohesion: 0.10
Nodes (11): cel_face(), ring_shell(), crown(), back_crest(), clipped(), coat_skirts(), combed_back(), nape_hem() (+3 more)

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.10
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "preview.py"
Cohesion: 0.18
Nodes (13): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+5 more)

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
Cohesion: 0.19
Nodes (3): Answered, Outcome, Questions

### Community 64 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.16
Nodes (4): DialogueKeys, DialogueKeysTest, ReactionTest, 10. Content plan

### Community 66 - "k"
Cohesion: 0.13
Nodes (9): snack_pouch(), collar(), loose_legs(), patch(), pocket(), stockings(), sash(), hairpin() (+1 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.12
Nodes (4): ClanProfile, Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.04
Nodes (3): 12. The bond book, Bond, BondWeb

### Community 69 - ".of"
Cohesion: 0.11
Nodes (7): Stage, ADULT, CHILD, TEEN, ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.09
Nodes (14): 13. Data formats, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+6 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.11
Nodes (4): 3. Levels and story gates, Levels, Meters, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 75 - "Tex"
Cohesion: 0.15
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 77 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 79 - "Face"
Cohesion: 0.20
Nodes (6): mark(), button(), darken_rows(), grid(), rivets(), Face

### Community 80 - "Konoha: the build plan"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 5. Process, 6. Prototypes, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 81 - "Mood"
Cohesion: 0.15
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
Cohesion: 0.12
Nodes (11): Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY, KINDNESS (+3 more)

### Community 87 - "NamesTest"
Cohesion: 0.21
Nodes (4): 1 Name, Names, PlayerName, NamesTest

### Community 89 - "cel_box"
Cohesion: 0.09
Nodes (16): back_fan(), braid(), cel_box(), lock(), sidelocks(), spike(), tie(), gathered_tail() (+8 more)

### Community 90 - ".tier"
Cohesion: 0.27
Nodes (4): 11. Kindling Bond, Bonfire, Flame, Kindling

### Community 91 - "Restyle"
Cohesion: 0.21
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, SETTINGS, TIME_SKIP

### Community 92 - "Title"
Cohesion: 0.20
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

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.17
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "org.junit.jupiter.api.Test"
Cohesion: 0.13
Nodes (5): 8. The village talks, BondDialogueTest, ConditionsAndEffectsTest, GossipTest, KindlingAndBookTest

### Community 103 - "Village"
Cohesion: 0.06
Nodes (10): 18. Village scale, Base, ClanRelations, SocialTie, House, Tier, BACKGROUND, CAST (+2 more)

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
Cohesion: 0.13
Nodes (14): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+6 more)

### Community 109 - "kit_household.py"
Cohesion: 0.05
Nodes (22): bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta(), ichimatsu() (+14 more)

### Community 112 - ".effectiveLevel"
Cohesion: 0.15
Nodes (6): Conversation, Reply, Topic, LifeEvents, News, 6. Conversation

### Community 113 - "Power"
Cohesion: 0.22
Nodes (5): Tier, BLAZE, FLAME, NONE, SPARK

### Community 115 - "ROADMAP.md"
Cohesion: 0.31
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 117 - "catalogue.py"
Cohesion: 0.21
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 119 - "kit_inuzuka.py"
Cohesion: 0.17
Nodes (5): burst(), claw_marks(), fang(), fang_small(), paw()

### Community 120 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 122 - "pathlib"
Cohesion: 0.12
Nodes (3): build(), build(), build()

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 124 - "How the pieces work"
Cohesion: 0.18
Nodes (6): How the pieces work, belt(), mesh(), tanto(), beak(), ears()

### Community 126 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 127 - "kit_nara.py"
Cohesion: 0.18
Nodes (6): arm_protector(), back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 128 - ".page"
Cohesion: 0.36
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 129 - "shade"
Cohesion: 0.25
Nodes (7): 4. Block catalogue, Interior fittings, Totals, Vanilla mappings, tatami(), tatami_top(), shade()

### Community 130 - "rnd"
Cohesion: 0.12
Nodes (9): quilt(), sprigs(), fur_edge(), splatter(), kasuri(), straw_sandals(), cloth_shade(), curls_face() (+1 more)

### Community 131 - "noren"
Cohesion: 0.20
Nodes (10): 2. Style guide: the Konoha kit, By building type, Facades and shop fronts, Lanterns, Shared palette, awning(), block(), facing_states() (+2 more)

### Community 135 - "Power"
Cohesion: 0.22
Nodes (7): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON

### Community 136 - "Shared helpers"
Cohesion: 0.14
Nodes (12): Shared helpers, body(), collar(), flaps(), footwear(), leg_bone(), leg_ring(), legs() (+4 more)

### Community 137 - "stamp"
Cohesion: 0.08
Nodes (15): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), crest_patch(), flame_hem(), guardian_sash() (+7 more)

### Community 139 - "re"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 140 - "wide_sleeves"
Cohesion: 0.28
Nodes (5): arm_bone(), arm_x(), armband(), roll(), wide_sleeves()

### Community 141 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

## Knowledge Gaps
- **219 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+214 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1146 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **56 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `Shared helpers`, `ROADMAP.md`?**
  _High betweenness centrality (0.392) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _219 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Person`, `VillageScaleTest`, `Bond`, `Memory`, `org.junit.jupiter.api.Test`, `Village`, `Levels`, `.effectiveLevel`, `Run`, `Personality`, `Activity`, `Mood`, `ROADMAP.md`, `Stage`, `.tier`, `.write`?**
  _High betweenness centrality (0.346) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `Clans`, `kit_academy.py`, `paint.py`, `fabric`, `kit_shinobi.py`, `kit_hyuga.py`, `kit_morino.py`, `forehead_protector`, `cel_box`, `How the pieces work`?**
  _High betweenness centrality (0.267) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1471264367816092 - nodes in this community are weakly interconnected._