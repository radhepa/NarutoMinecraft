# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 149 files · ~201,431 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2910 nodes · 6815 edges · 165 communities (117 shown, 48 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 741 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `10981532`
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
- strip_fabric
- kit_aburame.py
- paint.py
- kit_suzuran.py
- 7. Systems in the beta
- .go
- creator.py
- kit_hyuga.py
- kit_rugged.py
- Plan
- kit_tobari.py
- rot_matrix
- .receive
- Meters
- Look
- CreatorRules
- kit_market.py
- kit_kinoshita.py
- cel_box
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
- kit_akimichi.py
- kokuto
- Playthrough
- paint.py
- render_kit.py
- mockups.py
- Personality
- Box
- chain
- k
- kit_morino.py
- kit_gekko.py
- Act
- Stage
- preview.py
- org.junit.jupiter.api.Test
- Activity
- bandage_turns
- Playthrough.java
- Character creation
- Kind
- .answer
- .everyKeyTheEngineEmitsIsListed
- Squad
- .title
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
- .friends
- Value
- NamesTest
- SampleQuestions
- kit_umino.py
- .tier
- Run
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
- Conflict
- Custom blocks
- kit_household.py
- SquadTest
- .effectiveLevel
- Power
- Json
- skirt
- catalogue.py
- Rng
- anime.py
- kit_sarutobi.py
- 8. Beta catalogue
- pathlib
- 4. Clan quest lines
- pathlib
- .write
- kit_kunoichi.py
- kit_nara.py
- jika_tabi
- shade
- rnd
- stone_lantern
- TimeAndPacingTest
- Schedule
- seal_script
- Rng
- solid
- stamp
- tie
- shop_tea_house.py
- curtain
- pocket
- resolve
- hem
- checks
- gloves
- tape
- collar_band
- geta
- ichimatsu
- sash
- stripes
- trousers
- bands
- blossom
- kasuri
- robe_skirt
- ink_clouds
- part_line
- wisteria_hem
- splatter
- pauldron

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
- `Interior fittings` --references--> `tatami()`  [INFERRED]
  KONOHA_BUILD.md → tools/konoha/blocks.py
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java

## Import Cycles
- None detected.

## Communities (165 total, 48 thin omitted)

### Community 0 - "kit_nara.py"
Cohesion: 0.14
Nodes (8): back_crest(), crest(), arm_protector(), protector_plate(), backward_bandana(), crest(), flicks(), fabric()

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
Nodes (18): drawstrings(), forearm_wraps(), holster(), hood_down(), leg_cloth(), ribbed(), sash(), shin_wraps() (+10 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (32): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+24 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.11
Nodes (9): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), kimono_sleeves(), side_fringe(), stamp() (+1 more)

### Community 9 - "kit_hagane.py"
Cohesion: 0.06
Nodes (16): spike(), bracers(), crown(), harness(), mace(), plate(), shin_guards(), burst() (+8 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "strip_fabric"
Cohesion: 0.15
Nodes (8): arm_cloth(), cloth_shoes(), trouser_legs(), waist(), sandals(), sleeves(), waistband(), strip_fabric()

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "paint.py"
Cohesion: 0.12
Nodes (7): anbu_arms(), anbu_plates(), flak_vest(), cross_armband(), shirt(), cap(), cloth_shade()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - ".go"
Cohesion: 0.19
Nodes (7): BondEvent, Answer, Highlight, Invitation, Outcome, Plan, Together

### Community 17 - "creator.py"
Cohesion: 0.08
Nodes (19): check(), _hash(), hash64(), load_rules(), main(), _mix(), outputs(), roll_look() (+11 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.11
Nodes (8): blunt_fringe(), hakama_legs(), hime_locks(), kimono_sleeves(), obi(), parted_fringe(), tabi(), wrap_front()

### Community 19 - "kit_rugged.py"
Cohesion: 0.07
Nodes (15): baggy_legs(), cape(), dread(), leg_wraps(), patch(), ragged(), rope(), rope_face() (+7 more)

### Community 20 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 21 - "kit_tobari.py"
Cohesion: 0.09
Nodes (11): decal(), hood_down(), lantern(), lantern_tag(), mantle(), muffler(), plain_body(), pleats() (+3 more)

### Community 23 - ".receive"
Cohesion: 0.35
Nodes (3): Gifts, Received, GiftsTest

### Community 24 - "Meters"
Cohesion: 0.10
Nodes (8): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Meters

### Community 25 - "Look"
Cohesion: 0.10
Nodes (10): Look, Restyle, Result, Venue, BARBER, HOME, LOCKED, SETTINGS (+2 more)

### Community 26 - "CreatorRules"
Cohesion: 0.13
Nodes (8): 13. Code, and what waits for Phase 0, Choices, CreatorRules, Outfit, Roots, LifeRoll, Rolled, LifeRollTest

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kyahan() (+14 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "cel_box"
Cohesion: 0.13
Nodes (8): braid(), cel_box(), topknot(), ear_panels(), wave_lock(), tuft(), knot_bun(), bun()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.10
Nodes (9): arm_guards(), blouse(), collar(), half_sleeves(), holster(), knee_guards(), shirt(), strap() (+1 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.10
Nodes (28): build(), build_all(), catalog(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans() (+20 more)

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
Cohesion: 0.12
Nodes (22): 8. Registration notes for Phase 0, Facades and shop fronts, Roofs, Streets, auto_uv(), awning(), block(), Block (+14 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 42 - "kit_akimichi.py"
Cohesion: 0.10
Nodes (10): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+2 more)

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Playthrough"
Cohesion: 0.15
Nodes (13): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+5 more)

### Community 45 - "paint.py"
Cohesion: 0.29
Nodes (4): hair_box(), hair_face(), hair_shade(), shell()

### Community 46 - "render_kit.py"
Cohesion: 0.18
Nodes (7): Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street()

### Community 47 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 48 - "Personality"
Cohesion: 0.09
Nodes (9): Personality, Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH, Reaction (+1 more)

### Community 49 - "Box"
Cohesion: 0.07
Nodes (10): dark_seams(), strip_line(), Box, compatible(), Garment, key_rgba(), Layer, Piece (+2 more)

### Community 51 - "k"
Cohesion: 0.08
Nodes (14): sword_strap(), face_mask(), wave_band(), scarf(), trench_knife(), bandolier(), coat_skirts(), scroll_tube() (+6 more)

### Community 52 - "kit_morino.py"
Cohesion: 0.09
Nodes (12): cel_face(), ring_shell(), crown(), clipped(), coat_skirts(), combed_back(), gloves(), heavy_boots() (+4 more)

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "preview.py"
Cohesion: 0.16
Nodes (14): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+6 more)

### Community 58 - "Activity"
Cohesion: 0.15
Nodes (10): Activity, 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 3. Hangouts, 4. Their lives, 5. Following up, 7. Questions and choices (+2 more)

### Community 60 - "Playthrough.java"
Cohesion: 0.05
Nodes (10): Stage, ADULT, CHILD, TEEN, Tier, BACKGROUND, CAST, KNOWN (+2 more)

### Community 61 - "Character creation"
Cohesion: 0.10
Nodes (20): 11. Data, 12. Clan-born play: a later option, 14. Open questions, 1. At a glance, 2 Body, 2. World creation first, 3 Hair, 3. Where the creator sits in the opening (+12 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - ".answer"
Cohesion: 0.24
Nodes (4): Answered, Outcome, Questions, QuestionsTest

### Community 64 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.33
Nodes (3): DialogueKeys, DialogueKeysTest, 10. Content plan

### Community 65 - "Squad"
Cohesion: 0.07
Nodes (5): 13. Data formats, BondDialogue, BondEffects, Departure, Squad

### Community 67 - "VillageScaleTest"
Cohesion: 0.11
Nodes (4): ClanProfile, Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.04
Nodes (5): 12. The bond book, Bond, BondConditions, BondWeb, FollowUp

### Community 69 - ".of"
Cohesion: 0.13
Nodes (3): 8. The village talks, ConflictTest, GossipTest

### Community 70 - "Bonds"
Cohesion: 0.12
Nodes (12): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 6. Shared experiences and moments (+4 more)

### Community 71 - "Question"
Cohesion: 0.23
Nodes (3): Answer, Question, QuestionsCompiledTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.11
Nodes (4): 3. Levels and story gates, Levels, LevelsTest, MemoryTest

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 75 - "Tex"
Cohesion: 0.15
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 76 - "Seeds"
Cohesion: 0.18
Nodes (3): 5. Personality, Rng, Seeds

### Community 77 - "AnswerTag"
Cohesion: 0.11
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 79 - "Face"
Cohesion: 0.10
Nodes (12): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), button() (+4 more)

### Community 80 - "Konoha: the build plan"
Cohesion: 0.17
Nodes (12): 1. The answer: how much it will be, 5. Process, 6. Prototypes, 7. Effort estimate, Calibration, Contents, Konoha: the build plan, Order of work (+4 more)

### Community 81 - "Mood"
Cohesion: 0.15
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 86 - "Value"
Cohesion: 0.08
Nodes (23): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+15 more)

### Community 87 - "NamesTest"
Cohesion: 0.19
Nodes (5): 10. How residents address you, 1 Name, Names, PlayerName, NamesTest

### Community 89 - "kit_umino.py"
Cohesion: 0.14
Nodes (6): brush_tail(), dolphin(), falling_tail(), surf(), wave_band(), waves()

### Community 90 - ".tier"
Cohesion: 0.18
Nodes (5): 11. Kindling Bond, Household, Bonfire, Flame, Kindling

### Community 92 - "Title"
Cohesion: 0.20
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 94 - "creator/preview.py"
Cohesion: 0.18
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 95 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "Person"
Cohesion: 0.10
Nodes (6): 20. What the roadmap asks of bonds, BondBook, Fact, MemoryLine, Page, Person

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.20
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "org.junit.jupiter.api.Test"
Cohesion: 0.15
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 103 - "Village"
Cohesion: 0.07
Nodes (6): 18. Village scale, Base, ClanRelations, SocialTie, House, Village

### Community 104 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 105 - "Kind"
Cohesion: 0.17
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 108 - "Custom blocks"
Cohesion: 0.15
Nodes (13): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+5 more)

### Community 109 - "kit_household.py"
Cohesion: 0.20
Nodes (5): dots(), overlap(), socks(), trim(), wide_sleeves()

### Community 112 - ".effectiveLevel"
Cohesion: 0.16
Nodes (6): Conversation, Reply, Topic, LifeEvents, News, 6. Conversation

### Community 113 - "Power"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 117 - "catalogue.py"
Cohesion: 0.20
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 119 - "anime.py"
Cohesion: 0.17
Nodes (6): back_fan(), bangs(), lock(), sidelocks(), crest(), wave_lock()

### Community 120 - "kit_sarutobi.py"
Cohesion: 0.18
Nodes (6): beard(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey()

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 122 - "pathlib"
Cohesion: 0.17
Nodes (3): build(), paste(), scene()

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 126 - "kit_kunoichi.py"
Cohesion: 0.08
Nodes (11): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), tabi_boots() (+3 more)

### Community 127 - "kit_nara.py"
Cohesion: 0.28
Nodes (4): back_crest(), crest(), mesh_shirt(), net()

### Community 128 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 129 - "shade"
Cohesion: 0.29
Nodes (6): 4. Block catalogue, Totals, Vanilla mappings, tatami(), tatami_top(), shade()

### Community 130 - "rnd"
Cohesion: 0.15
Nodes (7): sprigs(), kasuri(), straw_sandals(), camo(), ink_stains(), seal_trim(), rnd()

### Community 131 - "stone_lantern"
Cohesion: 0.22
Nodes (7): 2. Style guide: the Konoha kit, By building type, Lanterns, Shared palette, Shrine, stone_lantern(), shimenawa()

### Community 132 - "TimeAndPacingTest"
Cohesion: 0.31
Nodes (3): 15. Pacing, TimeAndPacingTest, 9. Pacing with time together

### Community 136 - "solid"
Cohesion: 0.05
Nodes (33): Shared helpers, How the pieces work, arm_bone(), arm_x(), belt(), body(), collar(), flaps() (+25 more)

### Community 137 - "stamp"
Cohesion: 0.13
Nodes (8): stamp(), decal(), shoulder_decal(), slanted_protector(), back_crest(), back_crest(), crest_patch(), plate()

### Community 138 - "tie"
Cohesion: 0.29
Nodes (4): tie(), gathered_tail(), hair_tie(), knot()

## Knowledge Gaps
- **219 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+214 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1146 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **48 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `solid`, `Story bible`?**
  _High betweenness centrality (0.387) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _219 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_nara.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1437908496732026 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `TimeAndPacingTest`, `Story bible`, `.go`, `Meters`, `Personality`, `Stage`, `Squad`, `VillageScaleTest`, `Bond`, `.of`, `Levels`, `Seeds`, `Mood`, `.tier`, `Person`, `Memory`, `Village`, `Conflict`, `.write`?**
  _High betweenness centrality (0.343) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `solid` to `kit_nara.py`, `Clans`, `kit_academy.py`, `kit_hagane.py`, `strip_fabric`, `curtain`, `paint.py`, `hem`, `kit_morino.py`, `anime.py`, `cel_box`?**
  _High betweenness centrality (0.267) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._