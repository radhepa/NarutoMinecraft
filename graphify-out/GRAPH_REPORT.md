# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 118 files · ~156,115 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2382 nodes · 5761 edges · 173 communities (105 shown, 68 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 567 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0fd360a3`
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
- cel_box
- paint.py
- 7. Systems in the beta
- .roll
- sword_strap
- kit_hyuga.py
- kit_rugged.py
- Stage
- kit_specialist.py
- Garment
- load_clans
- Meters
- arm_bone
- kit_field.py
- kit_market.py
- kit_kinoshita.py
- k
- 5. Data formats built for the whole story
- Seeds
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- QuestionsTest
- 4. Technical architecture
- 6. The map
- kit_morino.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- kit_yamanaka.py
- curls_face
- kokuto
- Run
- paint.py
- Life together
- kit_shinobi.py
- build
- Box
- kit_tsuchigumo.py
- solid
- kit_nara.py
- kit_gekko.py
- Act
- Stage
- .snapshot
- kit_hagane.py
- BondWorld
- rnd
- Playthrough.java
- kit_nara.py
- Kind
- Question
- .everyKeyTheEngineEmitsIsListed
- Squad
- .populate
- VillageScaleTest
- Bond
- .of
- Bonds
- How the pieces work
- Def
- Levels
- Deed
- Experience
- SocialTie
- AnswerTag
- BondWorld
- Face
- News
- Mood
- BondEvent
- 4.3 The noble clans
- tool_belt
- .page
- Personality
- CourtshipTest
- kit_umino.py
- .tier
- Meter
- Title
- .greeting
- ClanProfile
- obi
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- Memory
- Label
- .classic
- .romance
- Kind
- .read
- 7. Inter-clan politics as quests
- Conflict
- State
- kit_household.py
- SquadTest
- .person
- Tier
- Tier
- .cap
- wave_band
- GossipTest
- Shared helpers
- senbon
- 8. Beta catalogue
- fur_face
- 4. Clan quest lines
- Schedule
- kit.py
- ConditionsAndEffectsTest
- flaps
- jika_tabi
- bandolier
- bandolier
- hairpin
- Layer
- kit_uzumaki.py
- Piece
- masks.py
- kit_hatake.py
- apothecary_sash
- bell_charm
- Side quest secrets
- gloves
- herb_pouch
- seal_script
- Naruto Minecraft
- stamp
- bun
- waves
- holster
- hood_down
- sash
- shin_wraps
- gourd
- scarf
- lames
- snack_pouch
- face_mask
- arm_cloth
- blossom
- checks
- cloth_shoes
- ichimatsu
- stripes
- wrap_front
- coat_skirts
- neckline
- scroll_tube
- shimenawa
- lamellar
- clip
- wrap_tie

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 187 edges
3. `solid()` - 152 edges
4. `Act` - 123 edges
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
- `Shared helpers` --references--> `wraps()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit_shinobi.py

## Import Cycles
- None detected.

## Communities (173 total, 68 thin omitted)

### Community 0 - "kit_nara.py"
Cohesion: 0.22
Nodes (4): arm_protector(), protector_plate(), backward_bandana(), crest()

### Community 1 - "kit_uchiha.py"
Cohesion: 0.19
Nodes (6): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.28
Nodes (3): lames(), plate(), shoulder_guards()

### Community 4 - "render.py"
Cohesion: 0.13
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.12
Nodes (8): drawstrings(), forearm_wraps(), ribbed(), side_stripe(), stripes(), turned_hem(), waist_pouch(), zip_pull()

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.11
Nodes (9): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), part_line(), splatter(), stamp() (+1 more)

### Community 9 - "kit_hagane.py"
Cohesion: 0.11
Nodes (9): spike(), crown(), burst(), claw_marks(), fang(), fang_small(), paw(), pineapple() (+1 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.06
Nodes (18): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), wave_lock(), mist_swirls() (+10 more)

### Community 11 - "fabric"
Cohesion: 0.07
Nodes (15): leg_cloth(), waist(), body(), footwear(), trouser_legs(), waist(), kimono_sleeves(), tabi() (+7 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "cel_box"
Cohesion: 0.10
Nodes (11): cel_box(), flick(), topknot(), ear_panels(), round_bun(), wave_lock(), wave_lock(), nape_hem() (+3 more)

### Community 14 - "paint.py"
Cohesion: 0.14
Nodes (7): armband(), back_crest(), bell_hem(), bell_print(), bell_sprig(), sash_vials(), vial()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".roll"
Cohesion: 0.10
Nodes (9): Activity, Answer, Highlight, Invitation, Outcome, Plan, Together, TogetherTest (+1 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.13
Nodes (8): tie(), back_sheet(), blunt_fringe(), gathered_tail(), hair_tie(), hime_locks(), parted_fringe(), wrap_front()

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "Stage"
Cohesion: 0.33
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 21 - "kit_specialist.py"
Cohesion: 0.07
Nodes (17): shirt(), vest(), pouch(), anbu_plates(), shirt(), decal(), hood_down(), lantern() (+9 more)

### Community 23 - "load_clans"
Cohesion: 0.19
Nodes (8): compatible(), load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 25 - "arm_bone"
Cohesion: 0.13
Nodes (10): sleeve_roll(), sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), tasuki(), armband() (+2 more)

### Community 26 - "kit_field.py"
Cohesion: 0.06
Nodes (19): blouse(), cargo(), chain(), collar(), gloves(), half_sleeves(), holster(), knee_guards() (+11 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (21): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+13 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.14
Nodes (9): back_crest(), crest(), kyahan(), pencil(), _piece(), sashiko(), saw(), square() (+1 more)

### Community 29 - "k"
Cohesion: 0.15
Nodes (8): collar(), mandarin_collar(), mandarin_collar(), shin_wrap(), combed_back(), trench_knife(), stockings(), k()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "Seeds"
Cohesion: 0.21
Nodes (3): 5. Personality, Rng, Seeds

### Community 32 - "wardrobe.py"
Cohesion: 0.15
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+8 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_morino.py"
Cohesion: 0.22
Nodes (4): back_crest(), gloves(), head_cloth(), forehead_protector()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 42 - "curls_face"
Cohesion: 0.40
Nodes (3): puff(), curls_box(), curls_face()

### Community 43 - "kokuto"
Cohesion: 0.24
Nodes (4): back_blade(), crest(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.11
Nodes (15): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough, Profile (+7 more)

### Community 45 - "paint.py"
Cohesion: 0.14
Nodes (8): cloth_shade(), dark_seams(), hair_box(), hair_face(), hair_shade(), shell(), strip_line(), shade()

### Community 46 - "Life together"
Cohesion: 0.22
Nodes (9): 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Questions and choices, 8. Data and quest hooks, 9. Pacing with time together (+1 more)

### Community 47 - "kit_shinobi.py"
Cohesion: 0.15
Nodes (6): back_crest(), bandaged_arm(), anbu_arms(), bandage(), flak_vest(), wraps()

### Community 48 - "build"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.18
Nodes (3): band(), hem(), Box

### Community 50 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 51 - "solid"
Cohesion: 0.14
Nodes (7): harness(), white_fang_tanto(), pauldron(), cane(), coat_skirts(), high_collar(), solid()

### Community 52 - "kit_nara.py"
Cohesion: 0.20
Nodes (6): cel_face(), ring_shell(), crown(), pulled_back(), combed_up(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (76): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+68 more)

### Community 55 - "Stage"
Cohesion: 0.15
Nodes (9): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+1 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.27
Nodes (4): bracers(), mace(), plate(), shin_guards()

### Community 58 - "BondWorld"
Cohesion: 0.11
Nodes (3): 12. The bond book, BondWorld, Standing

### Community 59 - "rnd"
Cohesion: 0.10
Nodes (11): quilt(), sprigs(), fur_edge(), ink_clouds(), wisteria_hem(), clipped(), ink_stains(), seal_trim() (+3 more)

### Community 60 - "Playthrough.java"
Cohesion: 0.06
Nodes (3): Recruitment, DialogueKeysTest, Leaf

### Community 61 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): back_crest(), crest(), mesh_shirt(), net(), tuft()

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Question"
Cohesion: 0.15
Nodes (6): Answer, Question, Answered, Outcome, Questions, QuestionsCompiledTest

### Community 66 - ".populate"
Cohesion: 0.23
Nodes (3): 20. What the roadmap asks of bonds, Report, VillageSim

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (3): Bond, BondConditions, FollowUp

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (14): 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+6 more)

### Community 71 - "How the pieces work"
Cohesion: 0.15
Nodes (10): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, How the pieces work, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village, mesh() (+2 more)

### Community 72 - "Def"
Cohesion: 0.12
Nodes (5): Def, Size, BIG, NOTABLE, SMALL

### Community 74 - "Deed"
Cohesion: 0.10
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 75 - "Experience"
Cohesion: 0.17
Nodes (10): Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION, SPAR (+2 more)

### Community 77 - "AnswerTag"
Cohesion: 0.11
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 79 - "Face"
Cohesion: 0.20
Nodes (6): mark(), button(), darken_rows(), grid(), rivets(), Face

### Community 81 - "Mood"
Cohesion: 0.15
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "BondEvent"
Cohesion: 0.21
Nodes (4): BondEvent, Gifts, Received, GiftsTest

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "tool_belt"
Cohesion: 0.20
Nodes (5): chisel(), mallet(), nail_pouch(), tool_belt(), wood_grain()

### Community 85 - ".page"
Cohesion: 0.21
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Personality"
Cohesion: 0.07
Nodes (25): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+17 more)

### Community 89 - "kit_umino.py"
Cohesion: 0.14
Nodes (6): falling_tail(), knot(), scroll(), surf(), wave_band(), waves()

### Community 90 - ".tier"
Cohesion: 0.18
Nodes (5): 11. Kindling Bond, Household, Bonfire, Flame, Kindling

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.22
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 94 - "ClanProfile"
Cohesion: 0.17
Nodes (3): 18. Village scale, ClanProfile, House

### Community 96 - "Side quests"
Cohesion: 0.20
Nodes (10): 1. Scope and budget, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents, In the beta (+2 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.14
Nodes (7): Memory, Source, HEARD, SEEN, SELF, TOLD, MemoryTest

### Community 101 - "Label"
Cohesion: 0.12
Nodes (9): Base, ClanRelations, Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL (+1 more)

### Community 102 - ".classic"
Cohesion: 0.14
Nodes (3): BondDialogueTest, KindlingAndBookTest, VillageTest

### Community 104 - "Kind"
Cohesion: 0.17
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 108 - "State"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 109 - "kit_household.py"
Cohesion: 0.11
Nodes (10): bands(), collar_band(), dots(), geta(), kasuri(), overlap(), sash(), socks() (+2 more)

### Community 112 - ".person"
Cohesion: 0.13
Nodes (5): BondWeb, Conversation, Reply, Topic, 6. Conversation

### Community 113 - "Tier"
Cohesion: 0.13
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 114 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 119 - "Shared helpers"
Cohesion: 0.15
Nodes (9): Shared helpers, back_fan(), bangs(), braid(), curtain(), lock(), sidelocks(), side_fringe() (+1 more)

### Community 120 - "senbon"
Cohesion: 0.25
Nodes (4): mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 126 - "kit.py"
Cohesion: 0.16
Nodes (5): belt(), frog_buttons(), kimono_sleeves(), obi(), roll()

### Community 128 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 129 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 135 - "Piece"
Cohesion: 0.33
Nodes (3): Piece, piece_corners(), world_bounds()

### Community 136 - "masks.py"
Cohesion: 0.16
Nodes (7): back_crest(), crest(), beak(), bump(), plate(), strap(), fabric()

### Community 137 - "kit_hatake.py"
Cohesion: 0.25
Nodes (3): decal(), shoulder_decal(), slanted_protector()

### Community 140 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 146 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 147 - "stamp"
Cohesion: 0.17
Nodes (8): stamp(), shoku_disc(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), dolphin()

## Knowledge Gaps
- **213 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+208 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 968 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **68 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `ROADMAP.md`, `Shared helpers`?**
  _High betweenness centrality (0.452) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _213 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Meters`, `Seeds`, `.snapshot`, `BondWorld`, `.populate`, `Deed`, `SocialTie`, `Mood`, `BondEvent`, `Personality`, `CourtshipTest`, `.tier`, `.greeting`, `ClanProfile`, `Person`, `Memory`, `Label`, `Conflict`, `ROADMAP.md`, `.cap`?**
  _High betweenness centrality (0.438) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13277310924369748 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `flaps`, `Clans`, `kit_morino.py`, `neckline`, `How the pieces work`, `kit_hagane.py`, `masks.py`, `fabric`, `cel_box`, `kit_shinobi.py`, `Box`, `solid`, `kit_nara.py`, `kit_specialist.py`, `kit_field.py`, `kit.py`?**
  _High betweenness centrality (0.408) - this node is a cross-community bridge._