# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 118 files · ~155,601 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2376 nodes · 5738 edges · 151 communities (101 shown, 50 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 561 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1452396e`
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
- stamp
- paint.py
- 7. Systems in the beta
- .roll
- sword_strap
- cel_box
- kit_rugged.py
- assertions
- kit_specialist.py
- Garment
- load_clans
- Meters
- arm_bone
- leg_bone
- kit_market.py
- kit_kinoshita.py
- k
- 5. Data formats built for the whole story
- kit_field.py
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
- kit_akimichi.py
- kokuto
- Run
- paint.py
- Life together
- kit_shinobi.py
- build
- Box
- chain
- solid
- kit_nara.py
- kit_gekko.py
- Act
- Stage
- Mood
- kit_hagane.py
- BondWorld
- rnd
- Playthrough.java
- kit_nara.py
- Kind
- .answer
- .everyKeyTheEngineEmitsIsListed
- Squad
- bangs
- VillageScaleTest
- Bond
- .of
- Bonds
- .valuesAndToneLandOnTheirPersonalityAndOppositePolesContradict
- Def
- Levels
- Deed
- SocialTie
- AnswerTag
- Face
- tape
- Mood
- .read
- 4.3 The noble clans
- kit_haruno.py
- .page
- Personality
- ClanRelations
- SampleQuestions
- kit_umino.py
- .tier
- Meter
- Title
- white_fang_tanto
- obi
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- Memory
- Label
- org.junit.jupiter.api.Test
- .romance
- Kind
- Question
- 7. Inter-clan politics as quests
- Conflict
- ReactionTest.java
- kit_household.py
- wrap_front
- .talk
- Tier
- Tier
- kyahan
- arm_warmers
- wave_band
- cape
- Shared helpers
- ragged
- 8. Beta catalogue
- fur_face
- 4. Clan quest lines
- rope_face
- cane
- kit_kunoichi.py
- mesh_shirt
- rope_hair
- shag_face
- bandolier
- bandolier
- hairpin
- coat_skirts
- kit_uzumaki.py
- bandage_turns
- masks.py
- kit_hatake.py
- apothecary_sash
- bell_charm
- tabi
- gloves
- herb_pouch
- lantern_tag
- shin_wraps
- kit_sarutobi.py
- bun
- waves
- scarf

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 185 edges
3. `solid()` - 152 edges
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
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py

## Import Cycles
- None detected.

## Communities (151 total, 50 thin omitted)

### Community 0 - "kit_nara.py"
Cohesion: 0.14
Nodes (8): arm_protector(), protector_plate(), backward_bandana(), crest(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 1 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.14
Nodes (11): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Reference images, The clan file, clan_bottoms() (+3 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.13
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.07
Nodes (15): back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps() (+7 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (32): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+24 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "kit_hagane.py"
Cohesion: 0.15
Nodes (6): spike(), burst(), claw_marks(), fang(), fang_small(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (11): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+3 more)

### Community 11 - "fabric"
Cohesion: 0.13
Nodes (12): leg_cloth(), waist(), body(), arm_cloth(), trouser_legs(), waist(), kimono_sleeves(), tabi_boots() (+4 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "stamp"
Cohesion: 0.11
Nodes (9): stamp(), crest(), crest(), wave_lock(), monkey(), back_crest(), decal(), dolphin() (+1 more)

### Community 14 - "paint.py"
Cohesion: 0.13
Nodes (6): back_crest(), bell_hem(), bell_print(), bell_sprig(), sash_vials(), vial()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".roll"
Cohesion: 0.09
Nodes (11): Activity, BondEvent, Answer, FollowUp, Highlight, Invitation, Outcome, Plan (+3 more)

### Community 18 - "cel_box"
Cohesion: 0.15
Nodes (10): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), nape_hem() (+2 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.11
Nodes (8): baggy_legs(), knot_bun(), leg_wraps(), patch(), shin_guard(), soft_boots(), straw_sandals(), tabi()

### Community 20 - "assertions"
Cohesion: 0.13
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 21 - "kit_specialist.py"
Cohesion: 0.12
Nodes (9): shirt(), shirt(), hood_down(), lantern(), mantle(), plain_body(), pleats(), split_toe_boots() (+1 more)

### Community 22 - "Garment"
Cohesion: 0.17
Nodes (6): compatible(), Garment, key_rgba(), Piece, piece_corners(), world_bounds()

### Community 23 - "load_clans"
Cohesion: 0.23
Nodes (7): Population, load_all_groups(), load_clans(), load_population(), population_weights(), validate_clans(), village_resident()

### Community 25 - "arm_bone"
Cohesion: 0.13
Nodes (11): sleeve_roll(), sode(), arm_bone(), arm_x(), kimono_sleeves(), tasuki(), armband(), cross_armband() (+3 more)

### Community 26 - "leg_bone"
Cohesion: 0.10
Nodes (11): blouse(), cargo(), holster(), knee_guards(), pocket(), hakama_legs(), leg_bone(), leg_ring() (+3 more)

### Community 27 - "kit_market.py"
Cohesion: 0.06
Nodes (17): bib(), checks(), dots(), furoshiki(), geta(), jika_tabi(), kyahan(), mark() (+9 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.11
Nodes (13): back_crest(), chisel(), crest(), mallet(), nail_pouch(), pencil(), _piece(), sashiko() (+5 more)

### Community 29 - "k"
Cohesion: 0.21
Nodes (9): collar(), footwear(), legs(), neckline(), pouch(), roll(), stockings(), waistband() (+1 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.14
Nodes (6): arm_guards(), gloves(), half_sleeves(), shirt(), trousers(), vest()

### Community 32 - "wardrobe.py"
Cohesion: 0.13
Nodes (18): catalog(), hex_rgb(), json_text(), load_characters(), load_collections(), load_eye_colors(), load_groups(), load_hair_colors() (+10 more)

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
Cohesion: 0.18
Nodes (5): back_crest(), gloves(), head_cloth(), heavy_boots(), forehead_protector()

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
Cohesion: 0.12
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box()

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.07
Nodes (18): 5. Personality, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS, GENIN (+10 more)

### Community 45 - "paint.py"
Cohesion: 0.29
Nodes (4): hair_box(), hair_face(), hair_shade(), shell()

### Community 46 - "Life together"
Cohesion: 0.20
Nodes (10): 11. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 6. Conversation, 7. Questions and choices, 8. Data and quest hooks (+2 more)

### Community 47 - "kit_shinobi.py"
Cohesion: 0.20
Nodes (4): anbu_arms(), anbu_plates(), flak_vest(), sandals()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.08
Nodes (7): band(), dark_seams(), hem(), strip_line(), Box, Layer, shade()

### Community 51 - "solid"
Cohesion: 0.07
Nodes (15): collar(), strap(), face_mask(), coat_skirts(), guardian_sash(), pauldron(), trench_knife(), scroll_tube() (+7 more)

### Community 52 - "kit_nara.py"
Cohesion: 0.18
Nodes (7): cel_face(), ring_shell(), crown(), combed_back(), pulled_back(), combed_up(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.10
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 56 - "Mood"
Cohesion: 0.22
Nodes (3): 18. Village scale, Mood, House

### Community 57 - "kit_hagane.py"
Cohesion: 0.18
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 58 - "BondWorld"
Cohesion: 0.07
Nodes (5): 12. The bond book, 13. Data formats, BondDialogue, BondWeb, BondWorld

### Community 59 - "rnd"
Cohesion: 0.11
Nodes (10): sprigs(), fur_edge(), kasuri(), straw_sandals(), clipped(), camo(), ink_stains(), seal_trim() (+2 more)

### Community 61 - "kit_nara.py"
Cohesion: 0.33
Nodes (3): back_crest(), crest(), tuft()

### Community 62 - "Kind"
Cohesion: 0.08
Nodes (19): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+11 more)

### Community 63 - ".answer"
Cohesion: 0.24
Nodes (3): Answered, Outcome, Questions

### Community 64 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.33
Nodes (3): DialogueKeys, DialogueKeysTest, 10. Content plan

### Community 65 - "Squad"
Cohesion: 0.09
Nodes (3): BondEffects, Departure, Squad

### Community 66 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

### Community 67 - "VillageScaleTest"
Cohesion: 0.12
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.09
Nodes (4): ConflictTest, Leaf, MemoryTest, ReactionTest

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (14): 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+6 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.13
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.16
Nodes (3): 8. The village talks, Deed, Know

### Community 77 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 79 - "Face"
Cohesion: 0.09
Nodes (13): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), button() (+5 more)

### Community 81 - "Mood"
Cohesion: 0.25
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - ".read"
Cohesion: 0.15
Nodes (6): 14. Save format and versioning, Gifts, Received, SaveFormat, GiftsTest, SaveFormatTest

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - ".page"
Cohesion: 0.28
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Personality"
Cohesion: 0.05
Nodes (33): 20. What the roadmap asks of bonds, ClanProfile, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY (+25 more)

### Community 89 - "kit_umino.py"
Cohesion: 0.14
Nodes (7): lock(), hime_locks(), flicks(), brush_tail(), falling_tail(), surf(), waves()

### Community 90 - ".tier"
Cohesion: 0.26
Nodes (4): 11. Kindling Bond, Bonfire, Flame, Kindling

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (7): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - "Title"
Cohesion: 0.15
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

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
Cohesion: 0.20
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "org.junit.jupiter.api.Test"
Cohesion: 0.11
Nodes (5): BondDialogueTest, ConditionsAndEffectsTest, GossipTest, KindlingAndBookTest, SquadTest

### Community 104 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "Conflict"
Cohesion: 0.12
Nodes (7): Conflict, State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 109 - "kit_household.py"
Cohesion: 0.05
Nodes (24): flaps(), bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta() (+16 more)

### Community 112 - ".talk"
Cohesion: 0.36
Nodes (3): Conversation, Reply, Topic

### Community 113 - "Tier"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 114 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 119 - "Shared helpers"
Cohesion: 0.24
Nodes (5): Shared helpers, back_fan(), braid(), sidelocks(), wraps()

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 126 - "kit_kunoichi.py"
Cohesion: 0.10
Nodes (10): belt(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 134 - "kit_uzumaki.py"
Cohesion: 0.29
Nodes (3): crest_patch(), seal_script(), seal_tags()

### Community 136 - "masks.py"
Cohesion: 0.15
Nodes (8): How the pieces work, mesh(), tanto(), beak(), bump(), ears(), plate(), strap()

### Community 137 - "kit_hatake.py"
Cohesion: 0.25
Nodes (3): decal(), shoulder_decal(), slanted_protector()

### Community 147 - "kit_sarutobi.py"
Cohesion: 0.25
Nodes (4): beard(), crest(), crest_patch(), flame_hem()

## Knowledge Gaps
- **211 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+206 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 968 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **50 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `load_clans`, `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.452) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _211 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_nara.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13725490196078433 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Person`, `BondWorld`, `Memory`, `Story bible`, `Levels`, `Deed`, `Conflict`, `Run`, `SocialTie`, `.roll`, `.read`, `Personality`, `Stage`, `Mood`, `ClanRelations`, `.tier`, `Meters`?**
  _High betweenness centrality (0.442) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `Clans`, `bangs`, `kit_academy.py`, `kit_morino.py`, `masks.py`, `kit_hagane.py`, `fabric`, `kit_household.py`, `kit_shinobi.py`, `Box`, `cel_box`, `solid`, `kit_nara.py`, `kit_umino.py`, `leg_bone`, `k`, `kit_kunoichi.py`?**
  _High betweenness centrality (0.403) - this node is a cross-community bridge._