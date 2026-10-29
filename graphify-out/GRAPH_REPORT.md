# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 129 files · ~181,563 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2608 nodes · 6080 edges · 159 communities (109 shown, 50 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 615 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `60494805`
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
- .roll
- k
- kit_hyuga.py
- kit_rugged.py
- Plan
- kit_tobari.py
- Garment
- .receive
- Meters
- wide_sleeves
- leg_ring
- kit_market.py
- kit_kinoshita.py
- Shared helpers
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
- Run
- paint.py
- render_kit.py
- Tier
- build
- Box
- chain
- solid
- kit_nara.py
- katana
- Act
- Stage
- preview.py
- kit_hagane.py
- .refuse
- rnd
- Playthrough.java
- .person
- Kind
- .answer
- Life together
- Squad
- BondWorld
- VillageScaleTest
- Bond
- .of
- Bonds
- .valuesAndToneLandOnTheirPersonalityAndOppositePolesContradict
- Def
- Levels
- Deed
- Tex
- SocialTie
- AnswerTag
- Face
- noren
- Mood
- .read
- 4.3 The noble clans
- kit_haruno.py
- .page
- Personality
- ClanRelations
- SampleQuestions
- cel_box
- .tier
- .test
- Title
- .name
- Village
- .cap
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- Memory
- Label
- org.junit.jupiter.api.Test
- Village
- Every building
- Question
- 7. Inter-clan politics as quests
- Conflict
- Custom blocks
- kit_household.py
- SquadTest
- .effectiveLevel
- Power
- Tier
- skirt
- catalogue.py
- kit_tsuchigumo.py
- anime.py
- load_clans
- 8. Beta catalogue
- sys
- 4. Clan quest lines
- pathlib
- .write
- kit_kunoichi.py
- mesh_shirt
- jika_tabi
- shade
- kit_specialist.py
- stone_lantern
- BondEffects
- 7. Effort estimate
- seal_script
- shade
- masks.py
- stamp
- wide_sleeves
- face_mask
- hood_down
- sleeve_roll
- turned_hem
- arm_cloth
- checks
- kit_morino.py
- cloth_shoes
- collar_band
- geta
- ichimatsu
- sash
- stripes
- obi
- scarf
- cane
- bandolier
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
- `15. Pacing` --references--> `TimeAndPacingTest`  [INFERRED]
  BONDS.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `9. Pacing with time together` --references--> `TimeAndPacingTest`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `Shrine` --references--> `shimenawa()`  [INFERRED]
  KONOHA_BUILD.md → tools/wardrobe/kit_tsuchigumo.py

## Import Cycles
- None detected.

## Communities (159 total, 50 thin omitted)

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
Cohesion: 0.13
Nodes (19): new_canvas(), backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font() (+11 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.09
Nodes (11): back_crest(), drawstrings(), forearm_wraps(), holster(), ribbed(), sash(), shin_wraps(), side_stripe() (+3 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (32): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+24 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.09
Nodes (11): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), kimono_sleeves(), part_line(), side_fringe() (+3 more)

### Community 9 - "kit_hagane.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (11): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+3 more)

### Community 11 - "strip_fabric"
Cohesion: 0.10
Nodes (11): leg_cloth(), waist(), trouser_legs(), waist(), kimono_sleeves(), tabi(), gloves(), heavy_boots() (+3 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "paint.py"
Cohesion: 0.16
Nodes (4): bandaged_arm(), anbu_arms(), bandage(), cloth_shade()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.11
Nodes (18): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Dialogue, Food, Friendship and bonds (+10 more)

### Community 16 - ".roll"
Cohesion: 0.10
Nodes (11): Activity, BondEvent, Answer, FollowUp, Highlight, Invitation, Outcome, Plan (+3 more)

### Community 17 - "k"
Cohesion: 0.16
Nodes (10): belt(), collar(), sword_strap(), wrap_front(), wave_band(), neckline(), pouch(), stockings() (+2 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.16
Nodes (6): bangs(), back_sheet(), blunt_fringe(), ear_panels(), hair_tie(), parted_fringe()

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 21 - "kit_tobari.py"
Cohesion: 0.07
Nodes (15): shirt(), vest(), anbu_plates(), decal(), hood_down(), lantern(), lantern_tag(), mantle() (+7 more)

### Community 22 - "Garment"
Cohesion: 0.16
Nodes (6): compatible(), Garment, key_rgba(), Piece, piece_corners(), world_bounds()

### Community 23 - ".receive"
Cohesion: 0.38
Nodes (3): Gifts, Received, GiftsTest

### Community 24 - "Meters"
Cohesion: 0.09
Nodes (8): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Meters

### Community 25 - "wide_sleeves"
Cohesion: 0.28
Nodes (5): arm_bone(), arm_x(), armband(), roll(), wide_sleeves()

### Community 27 - "kit_market.py"
Cohesion: 0.04
Nodes (24): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+16 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Shared helpers"
Cohesion: 0.17
Nodes (7): Shared helpers, braid(), body(), flaps(), footwear(), legs(), wraps()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.07
Nodes (13): arm_guards(), blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards() (+5 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.17
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+8 more)

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
Nodes (16): Roofs, auto_uv(), awning(), block(), Block, box(), check(), compile_all() (+8 more)

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

### Community 44 - "Run"
Cohesion: 0.09
Nodes (17): 5. Personality, Rng, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER (+9 more)

### Community 45 - "paint.py"
Cohesion: 0.29
Nodes (4): hair_box(), hair_face(), hair_shade(), shell()

### Community 46 - "render_kit.py"
Cohesion: 0.13
Nodes (10): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street() (+2 more)

### Community 47 - "Tier"
Cohesion: 0.25
Nodes (5): Tier, BLAZE, FLAME, NONE, SPARK

### Community 48 - "build"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.10
Nodes (5): band(), hem(), strip_line(), Box, Layer

### Community 51 - "solid"
Cohesion: 0.10
Nodes (11): white_fang_tanto(), hakama_legs(), coat_skirts(), pauldron(), trench_knife(), side_panels(), scroll(), clip() (+3 more)

### Community 52 - "kit_nara.py"
Cohesion: 0.13
Nodes (8): crown(), combed_back(), arm_protector(), back_crest(), crest(), pulled_back(), tuft(), scalp()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "preview.py"
Cohesion: 0.18
Nodes (13): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+5 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 58 - ".refuse"
Cohesion: 0.15
Nodes (3): BondDialogue, Household, Recruitment

### Community 59 - "rnd"
Cohesion: 0.14
Nodes (8): sprigs(), ink_clouds(), splatter(), wisteria_hem(), clipped(), bandage_turns(), thorn_wrap(), rnd()

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - ".answer"
Cohesion: 0.21
Nodes (4): Answered, Outcome, Questions, QuestionsTest

### Community 64 - "Life together"
Cohesion: 0.13
Nodes (12): DialogueKeys, DialogueKeysTest, 10. Content plan, 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up (+4 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.14
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.11
Nodes (3): ConflictTest, Leaf, ReactionTest

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (13): 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+5 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

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
Nodes (6): drawn_line(), button(), darken_rows(), line(), rivets(), Face

### Community 80 - "noren"
Cohesion: 0.14
Nodes (16): 1. The answer: how much it will be, 2. Style guide: the Konoha kit, 5. Process, 6. Prototypes, 8. Registration notes for Phase 0, By building type, Contents, Facades and shop fronts (+8 more)

### Community 81 - "Mood"
Cohesion: 0.15
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.14
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - ".page"
Cohesion: 0.28
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Personality"
Cohesion: 0.05
Nodes (32): 20. What the roadmap asks of bonds, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS (+24 more)

### Community 89 - "cel_box"
Cohesion: 0.08
Nodes (16): cel_box(), cel_face(), curtain(), ring_shell(), spike(), tie(), gathered_tail(), pineapple() (+8 more)

### Community 90 - ".tier"
Cohesion: 0.26
Nodes (4): 11. Kindling Bond, Bonfire, Flame, Kindling

### Community 92 - "Title"
Cohesion: 0.22
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 94 - "Village"
Cohesion: 0.17
Nodes (3): 18. Village scale, ClanProfile, House

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "Person"
Cohesion: 0.11
Nodes (6): Person, Stage, ADULT, CHILD, TEEN, Schedule

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.16
Nodes (7): Memory, Source, HEARD, SEEN, SELF, TOLD, MemoryTest

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "org.junit.jupiter.api.Test"
Cohesion: 0.17
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 104 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 105 - "Question"
Cohesion: 0.12
Nodes (10): Answer, Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS (+2 more)

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 108 - "Custom blocks"
Cohesion: 0.12
Nodes (16): 4. Block catalogue, Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival (+8 more)

### Community 109 - "kit_household.py"
Cohesion: 0.11
Nodes (8): bands(), blossom(), dots(), kasuri(), overlap(), robe_skirt(), socks(), topknot()

### Community 112 - ".effectiveLevel"
Cohesion: 0.09
Nodes (8): 12. The bond book, BondWeb, Conversation, Reply, Topic, LifeEvents, News, 6. Conversation

### Community 113 - "Power"
Cohesion: 0.22
Nodes (7): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON

### Community 114 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 117 - "catalogue.py"
Cohesion: 0.21
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 118 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (7): glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 119 - "anime.py"
Cohesion: 0.12
Nodes (8): back_fan(), lock(), sidelocks(), hime_locks(), crest(), wave_lock(), beard(), falling_tail()

### Community 120 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 126 - "kit_kunoichi.py"
Cohesion: 0.08
Nodes (11): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), tabi_boots() (+3 more)

### Community 128 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 129 - "shade"
Cohesion: 0.40
Nodes (4): Interior fittings, tatami(), tatami_top(), shade()

### Community 130 - "kit_specialist.py"
Cohesion: 0.11
Nodes (8): bandolier(), coat_skirts(), cross_armband(), ink_stains(), scroll_tube(), seal_trim(), shirt(), strap()

### Community 131 - "stone_lantern"
Cohesion: 0.40
Nodes (3): Lanterns, facing_states(), stone_lantern()

### Community 133 - "7. Effort estimate"
Cohesion: 0.50
Nodes (4): 7. Effort estimate, Calibration, Sessions, Your hours

### Community 136 - "masks.py"
Cohesion: 0.16
Nodes (7): How the pieces work, mesh(), tanto(), beak(), bump(), ears(), strap()

### Community 137 - "stamp"
Cohesion: 0.09
Nodes (16): stamp(), crescent(), decal(), shoulder_decal(), slanted_protector(), crest(), crest(), crest_patch() (+8 more)

### Community 147 - "kit_morino.py"
Cohesion: 0.20
Nodes (4): back_crest(), head_cloth(), nape_hem(), forehead_protector()

## Knowledge Gaps
- **211 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+206 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1079 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **50 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bonds` connect `Bonds` to `Person`, `Memory`, `Story bible`, `Conflict`, `Run`, `SocialTie`, `.effectiveLevel`, `.roll`, `Mood`, `.person`, `Personality`, `Stage`, `ClanRelations`, `Meters`, `.tier`, `.write`, `Village`, `.cap`?**
  _High betweenness centrality (0.437) - this node is a cross-community bridge._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _211 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.386) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `Clans`, `masks.py`, `stamp`, `strip_fabric`, `paint.py`, `k`, `kit_hyuga.py`, `kit_morino.py`, `Box`, `kit_nara.py`, `anime.py`, `cel_box`, `leg_ring`?**
  _High betweenness centrality (0.310) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1265597147950089 - nodes in this community are weakly interconnected._