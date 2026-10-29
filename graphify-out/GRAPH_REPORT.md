# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 118 files · ~155,438 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2374 nodes · 5725 edges · 155 communities (96 shown, 59 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 557 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `83a139a5`
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
- .roll
- k
- kit_hyuga.py
- kit_rugged.py
- Leaf.java
- kit_tobari.py
- Garment
- .receive
- Meters
- arm_bone
- leg_bone
- kit_market.py
- kit_kinoshita.py
- kit.py
- 5. Data formats built for the whole story
- kit_field.py
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_shiranui.py
- 4. Technical architecture
- 6. The map
- CourtshipTest
- 8. The beta, chapter by chapter
- 9. Delivery plan
- kit_yamanaka.py
- kit_akimichi.py
- kokuto
- Run
- paint.py
- SocietyHook
- Tier
- build
- Box
- chain
- solid
- kit_nara.py
- katana
- Act
- Stage
- Stage
- kit_hagane.py
- .refuse
- rnd
- .person
- Kind
- .answer
- .everyKeyTheEngineEmitsIsListed
- Squad
- .slant
- VillageScaleTest
- Bond
- .of
- Bonds
- .valuesAndToneLandOnTheirPersonalityAndOppositePolesContradict
- Def
- Levels
- Deed
- Schedule
- SocialTie
- AnswerTag
- BondWorld
- Face
- Trait
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
- Kind
- Question
- 7. Inter-clan politics as quests
- Conflict
- kit_household.py
- SquadTest
- .effectiveLevel
- Power
- Tier
- flaps
- curtain
- belt
- anime.py
- pocket
- 8. Beta catalogue
- fur_face
- 4. Clan quest lines
- rope_face
- furoshiki
- kit_kunoichi.py
- mesh_shirt
- rope_hair
- shag_face
- bandolier
- clip
- hairpin
- vial
- seal_script
- bandage_turns
- masks.py
- stamp
- mandarin_collar
- face_mask
- tabi
- ink_clouds
- jika_tabi
- patch
- rolled_cuffs
- cel_box
- coat_skirts
- pineapple
- pauldron
- high_collar
- knot
- scroll
- scarf

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 184 edges
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

## Communities (155 total, 59 thin omitted)

### Community 0 - "kit_nara.py"
Cohesion: 0.14
Nodes (7): arm_protector(), back_crest(), crest(), protector_plate(), backward_bandana(), crest(), flicks()

### Community 1 - "kit_uchiha.py"
Cohesion: 0.19
Nodes (6): arm_crest(), back_crest(), chest_crest(), crest(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.15
Nodes (12): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+4 more)

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
Cohesion: 0.08
Nodes (13): back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps() (+5 more)

### Community 7 - "Story bible"
Cohesion: 0.05
Nodes (40): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Clan lines, District quests and one-offs (+32 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.09
Nodes (11): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), part_line(), side_fringe(), splatter() (+3 more)

### Community 9 - "kit_hagane.py"
Cohesion: 0.11
Nodes (8): spike(), crown(), burst(), claw_marks(), fang(), fang_small(), paw(), brush_tail()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "fabric"
Cohesion: 0.10
Nodes (15): leg_cloth(), shirt(), waist(), half_sleeves(), shirt(), trousers(), arm_cloth(), kimono_sleeves() (+7 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_shinobi.py"
Cohesion: 0.15
Nodes (8): Shared helpers, back_crest(), bandaged_arm(), bandage(), forehead_protector(), mesh(), sandals(), wraps()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.11
Nodes (9): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+1 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".roll"
Cohesion: 0.12
Nodes (10): Activity, BondEvent, Answer, FollowUp, Highlight, Invitation, Outcome, Plan (+2 more)

### Community 17 - "k"
Cohesion: 0.08
Nodes (13): sword_strap(), blossom(), geta(), sash(), kyahan(), straw_sandals(), wave_band(), neckline() (+5 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.12
Nodes (9): tie(), blunt_fringe(), crest(), gathered_tail(), hair_tie(), hime_locks(), obi(), parted_fringe() (+1 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.14
Nodes (6): knot_bun(), leg_wraps(), patch(), soft_boots(), straw_sandals(), tabi()

### Community 21 - "kit_tobari.py"
Cohesion: 0.08
Nodes (15): vest(), pouch(), anbu_plates(), decal(), hood_down(), lantern(), lantern_tag(), mantle() (+7 more)

### Community 22 - "Garment"
Cohesion: 0.16
Nodes (6): compatible(), Garment, key_rgba(), Piece, piece_corners(), world_bounds()

### Community 23 - ".receive"
Cohesion: 0.35
Nodes (3): Gifts, Received, GiftsTest

### Community 25 - "arm_bone"
Cohesion: 0.11
Nodes (13): sleeve_roll(), sode(), arm_bone(), arm_x(), arm_guards(), bracers(), kimono_sleeves(), tasuki() (+5 more)

### Community 26 - "leg_bone"
Cohesion: 0.15
Nodes (7): knee_guards(), hakama_legs(), thigh_holster(), leg_bone(), leg_ring(), baggy_legs(), shin_guard()

### Community 27 - "kit_market.py"
Cohesion: 0.07
Nodes (15): bib(), checks(), gathered_ankles(), geta(), kasuri(), loose_legs(), mark(), open_front() (+7 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "kit.py"
Cohesion: 0.12
Nodes (7): body(), collar(), footwear(), legs(), sleeves(), shirt(), waistband()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.14
Nodes (6): blouse(), collar(), gloves(), holster(), strap(), tape()

### Community 32 - "wardrobe.py"
Cohesion: 0.10
Nodes (24): catalog(), general_pool(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans(), load_collections() (+16 more)

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
Cohesion: 0.11
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box() (+1 more)

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.07
Nodes (18): 5. Personality, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS, GENIN (+10 more)

### Community 45 - "paint.py"
Cohesion: 0.27
Nodes (4): hair_box(), hair_face(), hair_shade(), shell()

### Community 46 - "SocietyHook"
Cohesion: 0.25
Nodes (3): 19. Society hooks, SocietyHook, 3.1 The hook schema

### Community 47 - "Tier"
Cohesion: 0.25
Nodes (5): Tier, BLAZE, FLAME, NONE, SPARK

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.09
Nodes (7): band(), dark_seams(), hem(), strip_line(), Box, Layer, shade()

### Community 51 - "solid"
Cohesion: 0.12
Nodes (8): harness(), white_fang_tanto(), trench_knife(), cane(), coat_skirts(), scroll_tube(), shimenawa(), solid()

### Community 52 - "kit_nara.py"
Cohesion: 0.13
Nodes (9): ring_shell(), crown(), back_crest(), clipped(), combed_back(), head_cloth(), pulled_back(), combed_up() (+1 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (74): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+66 more)

### Community 55 - "Stage"
Cohesion: 0.15
Nodes (9): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+1 more)

### Community 56 - "Stage"
Cohesion: 0.33
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 57 - "kit_hagane.py"
Cohesion: 0.33
Nodes (3): mace(), plate(), shin_guards()

### Community 58 - ".refuse"
Cohesion: 0.13
Nodes (3): BondDialogue, Household, Recruitment

### Community 59 - "rnd"
Cohesion: 0.10
Nodes (11): cel_face(), sprigs(), fur_edge(), wisteria_hem(), camo(), cape(), ragged(), ink_stains() (+3 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - ".answer"
Cohesion: 0.18
Nodes (4): Answered, Outcome, Questions, QuestionsTest

### Community 67 - "VillageScaleTest"
Cohesion: 0.13
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.13
Nodes (3): ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.12
Nodes (12): 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 6. Shared experiences and moments (+4 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 77 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 79 - "Face"
Cohesion: 0.10
Nodes (12): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), button() (+4 more)

### Community 80 - "Trait"
Cohesion: 0.33
Nodes (6): Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH

### Community 81 - "Mood"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - ".read"
Cohesion: 0.23
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.12
Nodes (8): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), wave_lock(), rot_matrix()

### Community 85 - ".page"
Cohesion: 0.17
Nodes (7): 12. The bond book, Bonds in the story (spoilers), BondBook, Fact, MemoryLine, Page, BondWeb

### Community 86 - "Personality"
Cohesion: 0.06
Nodes (27): 20. What the roadmap asks of bonds, ClanProfile, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY (+19 more)

### Community 89 - "kit_umino.py"
Cohesion: 0.17
Nodes (5): dolphin(), falling_tail(), surf(), wave_band(), waves()

### Community 90 - ".tier"
Cohesion: 0.26
Nodes (4): 11. Kindling Bond, Bonfire, Flame, Kindling

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (7): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - "Title"
Cohesion: 0.22
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 94 - "Village"
Cohesion: 0.17
Nodes (3): 18. Village scale, House, Village

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
Cohesion: 0.16
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "org.junit.jupiter.api.Test"
Cohesion: 0.12
Nodes (5): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, TogetherTest, VillageTest

### Community 104 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 109 - "kit_household.py"
Cohesion: 0.07
Nodes (18): bands(), checks(), cloth_shoes(), collar_band(), dots(), ichimatsu(), jika_tabi(), kasuri() (+10 more)

### Community 112 - ".effectiveLevel"
Cohesion: 0.14
Nodes (6): Conversation, Reply, Topic, LifeEvents, News, 6. Conversation

### Community 113 - "Power"
Cohesion: 0.22
Nodes (7): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON

### Community 114 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 115 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 119 - "anime.py"
Cohesion: 0.16
Nodes (6): back_fan(), bangs(), braid(), lock(), sidelocks(), crest()

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 126 - "kit_kunoichi.py"
Cohesion: 0.14
Nodes (6): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), shin_wrap(), wrap_front()

### Community 136 - "masks.py"
Cohesion: 0.15
Nodes (8): How the pieces work, flak_vest(), tanto(), beak(), bump(), ears(), plate(), strap()

### Community 137 - "stamp"
Cohesion: 0.10
Nodes (11): stamp(), crescent(), decal(), shoulder_decal(), slanted_protector(), crest(), crest_patch(), flame_hem() (+3 more)

### Community 147 - "cel_box"
Cohesion: 0.12
Nodes (9): cel_box(), topknot(), ear_panels(), round_bun(), wave_lock(), nape_hem(), tuft(), beard() (+1 more)

## Knowledge Gaps
- **211 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+206 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 968 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **59 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `kit_shinobi.py`, `Story bible`?**
  _High betweenness centrality (0.451) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _211 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_nara.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13970588235294118 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Person`, `Memory`, `CourtshipTest`, `Story bible`, `Conflict`, `Run`, `SocialTie`, `SocietyHook`, `.roll`, `.read`, `.page`, `Personality`, `ClanRelations`, `Meters`, `.tier`, `.person`, `Village`, `.cap`?**
  _High betweenness centrality (0.434) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13109243697478992 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `kit_shinobi.py` to `Clans`, `masks.py`, `kit_hagane.py`, `fabric`, `k`, `Box`, `cel_box`, `kit_nara.py`, `curtain`, `belt`, `anime.py`, `flaps`, `kit_tobari.py`, `leg_bone`, `solid`, `kit.py`?**
  _High betweenness centrality (0.401) - this node is a cross-community bridge._