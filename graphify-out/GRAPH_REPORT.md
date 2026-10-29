# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 115 files · ~152,093 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2320 nodes · 5514 edges · 156 communities (102 shown, 54 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 533 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6f28ab56`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- fabric
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- rnd
- kit_yuhi.py
- kit_kunoichi.py
- kit_aburame.py
- kit_shinobi.py
- kit_suzuran.py
- 7. Systems in the beta
- .person
- k
- cel_box
- kit_rugged.py
- jika_tabi
- kit_tobari.py
- Garment
- mesh_shirt
- glyphs.py
- arm_bone
- strip_fabric
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
- kit_uzumaki.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- kit_yamanaka.py
- kit_akimichi.py
- kokuto
- Run
- load_clans
- News
- rot_matrix
- build
- Box
- chain
- kit_tsuchigumo.py
- ring_shell
- kit_gekko.py
- Act
- Stage
- kit_hagane.py
- BondWorld
- rnd
- Playthrough.java
- org.junit.jupiter.api.Test
- Kind
- .answer
- Squad
- Village
- VillageScaleTest
- Bond
- .of
- Bonds
- Question
- Def
- Levels
- Deed
- ReactionTest.java
- .romance
- AnswerTag
- .apply
- Face
- Personality
- Mood
- masks.py
- 4.3 The noble clans
- kit_haruno.py
- .page
- Peeve
- ClanRelations
- Shared helpers
- kit_umino.py
- .day
- Meter
- Title
- .name
- ROADMAP.md
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- Memory
- Label
- Activity
- Mood
- Kind
- CourtshipTest
- 7. Inter-clan politics as quests
- Conflict
- kit_nara.py
- kit_household.py
- hair_face
- .talk
- Tier
- Schedule
- flaps
- Stage
- The village
- anime.py
- BondConditions
- bangs
- .cap
- Side quest secrets
- bandage
- paint.py
- wide_sleeves
- vest
- rope_hair
- shag_face
- leg_bone
- footwear
- bands
- blossom
- checks
- cloth_shoes
- solid
- kit_sarutobi.py
- collar_band
- bandolier
- dots
- geta
- ichimatsu
- kasuri
- overlap
- topknot
- kyahan
- tabi
- coat_skirts
- gloves
- wave_band
- pauldron
- sash
- scarf

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 170 edges
3. `solid()` - 152 edges
4. `Act` - 118 edges
5. `fabric()` - 109 edges
6. `Village` - 63 edges
7. `Bond` - 62 edges
8. `strip_fabric()` - 59 edges
9. `Person` - 53 edges
10. `stamp()` - 47 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `15. Pacing` --references--> `TimeAndPacingTest`  [INFERRED]
  BONDS.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `9. Pacing with time together` --references--> `TimeAndPacingTest`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `3. Hangouts` --references--> `Activity`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Activity.java

## Import Cycles
- None detected.

## Communities (156 total, 54 thin omitted)

### Community 0 - "fabric"
Cohesion: 0.15
Nodes (7): back_crest(), crest(), back_crest(), head_cloth(), forehead_protector(), dolphin(), fabric()

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
Cohesion: 0.10
Nodes (10): drawstrings(), holster(), hood_down(), sash(), side_stripe(), sleeve_roll(), stripes(), turned_hem() (+2 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.09
Nodes (11): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+3 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.10
Nodes (10): belt(), arm_warmers(), frog_buttons(), mandarin_collar(), obi(), round_bun(), shin_wrap(), tabi_boots() (+2 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_shinobi.py"
Cohesion: 0.14
Nodes (7): shirt(), anbu_arms(), anbu_plates(), flak_vest(), cross_armband(), shirt(), cap()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".person"
Cohesion: 0.11
Nodes (9): BondEvent, Answer, Highlight, Invitation, Outcome, Plan, Together, TogetherTest (+1 more)

### Community 17 - "k"
Cohesion: 0.09
Nodes (12): ribbed(), shin_wraps(), tape(), sword_strap(), face_mask(), obi(), wrap_front(), trench_knife() (+4 more)

### Community 18 - "cel_box"
Cohesion: 0.15
Nodes (10): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), pineapple() (+2 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.11
Nodes (9): cape(), knot_bun(), leg_wraps(), patch(), rope(), rope_face(), soft_boots(), straw_sandals() (+1 more)

### Community 20 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 21 - "kit_tobari.py"
Cohesion: 0.09
Nodes (11): decal(), hood_down(), lantern(), lantern_tag(), mantle(), muffler(), plain_body(), pleats() (+3 more)

### Community 22 - "Garment"
Cohesion: 0.17
Nodes (6): compatible(), Garment, key_rgba(), Piece, piece_corners(), world_bounds()

### Community 25 - "arm_bone"
Cohesion: 0.11
Nodes (13): sode(), arm_bone(), arm_x(), arm_guards(), bracers(), kimono_sleeves(), kimono_sleeves(), kimono_sleeves() (+5 more)

### Community 26 - "strip_fabric"
Cohesion: 0.11
Nodes (9): leg_cloth(), waist(), gloves(), half_sleeves(), shirt(), trousers(), tabi(), sandals() (+1 more)

### Community 27 - "kit_market.py"
Cohesion: 0.06
Nodes (17): bib(), checks(), dots(), furoshiki(), geta(), jika_tabi(), kyahan(), open_front() (+9 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.12
Nodes (12): back_crest(), chisel(), crest(), mallet(), nail_pouch(), pencil(), _piece(), sashiko() (+4 more)

### Community 29 - "kit.py"
Cohesion: 0.14
Nodes (8): body(), collar(), legs(), neckline(), pouch(), sleeves(), stockings(), waistband()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.13
Nodes (7): blouse(), cargo(), collar(), holster(), knee_guards(), pocket(), strap()

### Community 32 - "wardrobe.py"
Cohesion: 0.13
Nodes (18): catalog(), hex_rgb(), json_text(), load_characters(), load_collections(), load_eye_colors(), load_groups(), load_hair_colors() (+10 more)

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

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.11
Nodes (9): bun(), clip(), crest_patch(), hairpin(), seal_script(), seal_tags(), waves(), wide_sleeves() (+1 more)

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
Cohesion: 0.24
Nodes (4): back_blade(), crest(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.08
Nodes (18): 20. What the roadmap asks of bonds, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS, GENIN (+10 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): Population, load_all_groups(), load_clans(), load_population(), population_weights(), validate_clans(), village_resident()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.08
Nodes (7): band(), dark_seams(), hem(), strip_line(), Box, Layer, shade()

### Community 51 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 52 - "ring_shell"
Cohesion: 0.17
Nodes (7): ring_shell(), crown(), combed_back(), nape_hem(), pulled_back(), combed_up(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (73): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+65 more)

### Community 55 - "Stage"
Cohesion: 0.15
Nodes (9): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+1 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.20
Nodes (5): spike(), crown(), mace(), plate(), brush_tail()

### Community 58 - "BondWorld"
Cohesion: 0.09
Nodes (3): 12. The bond book, BondWorld, Standing

### Community 59 - "rnd"
Cohesion: 0.09
Nodes (12): sprigs(), splatter(), wisteria_hem(), kasuri(), clipped(), camo(), ragged(), ink_stains() (+4 more)

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.12
Nodes (6): 8. The village talks, BondDialogueTest, ConditionsAndEffectsTest, GossipTest, KindlingAndBookTest, SquadTest

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - ".answer"
Cohesion: 0.17
Nodes (3): Answered, Outcome, Questions

### Community 66 - "Village"
Cohesion: 0.17
Nodes (5): Tier, BACKGROUND, CAST, KNOWN, Village

### Community 67 - "VillageScaleTest"
Cohesion: 0.12
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (3): Bond, BondWeb, FollowUp

### Community 69 - ".of"
Cohesion: 0.13
Nodes (3): ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (14): 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+6 more)

### Community 71 - "Question"
Cohesion: 0.07
Nodes (19): 14. Save format and versioning, DialogueKeys, Answer, Question, SaveFormat, DialogueKeysTest, QuestionsTest, SampleQuestions (+11 more)

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 77 - "AnswerTag"
Cohesion: 0.11
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 79 - "Face"
Cohesion: 0.18
Nodes (7): mark(), button(), curls_face(), darken_rows(), grid(), rivets(), Face

### Community 80 - "Personality"
Cohesion: 0.08
Nodes (15): 5. Personality, Personality, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM (+7 more)

### Community 81 - "Mood"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - "masks.py"
Cohesion: 0.15
Nodes (8): How the pieces work, mesh(), tanto(), beak(), bump(), ears(), plate(), strap()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - ".page"
Cohesion: 0.33
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 88 - "Shared helpers"
Cohesion: 0.14
Nodes (9): Shared helpers, back_fan(), lock(), sidelocks(), hime_locks(), wave_lock(), beard(), wraps() (+1 more)

### Community 89 - "kit_umino.py"
Cohesion: 0.20
Nodes (4): falling_tail(), surf(), wave_band(), waves()

### Community 91 - "Meter"
Cohesion: 0.10
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.22
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.25
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 95 - "ROADMAP.md"
Cohesion: 0.33
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 96 - "Side quests"
Cohesion: 0.12
Nodes (16): 1. Scope and budget, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 8. Beta catalogue, 9. Open questions, Beta 1: the opening and the Academy (+8 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.13
Nodes (15): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.4 The minor clans, 4.5 Clan quest counts, 4. Clan quest lines, Hagane, Haruno, Kinoshita (+7 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.10
Nodes (7): Memory, Meters, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 103 - "Mood"
Cohesion: 0.20
Nodes (3): 18. Village scale, Mood, House

### Community 104 - "Kind"
Cohesion: 0.20
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 108 - "kit_nara.py"
Cohesion: 0.16
Nodes (6): arm_protector(), back_crest(), crest(), protector_plate(), backward_bandana(), crest()

### Community 109 - "kit_household.py"
Cohesion: 0.22
Nodes (5): arm_cloth(), socks(), stripes(), trouser_legs(), waist()

### Community 110 - "hair_face"
Cohesion: 0.29
Nodes (4): hair_box(), hair_face(), hair_shade(), shell()

### Community 112 - ".talk"
Cohesion: 0.39
Nodes (4): Conversation, Reply, Topic, 6. Conversation

### Community 113 - "Tier"
Cohesion: 0.18
Nodes (8): 11. Kindling Bond, Grant, Kindling, Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 115 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 117 - "Stage"
Cohesion: 0.33
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 118 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 121 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

### Community 123 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 124 - "bandage"
Cohesion: 0.33
Nodes (3): forearm_wraps(), bandaged_arm(), bandage()

### Community 130 - "leg_bone"
Cohesion: 0.11
Nodes (10): shin_guards(), hakama_legs(), leg_bone(), leg_ring(), gathered_ankles(), loose_legs(), rolled_cuffs(), heavy_boots() (+2 more)

### Community 136 - "solid"
Cohesion: 0.13
Nodes (8): harness(), white_fang_tanto(), thigh_holster(), cane(), bandolier(), strap(), scroll(), solid()

### Community 137 - "kit_sarutobi.py"
Cohesion: 0.15
Nodes (9): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), crest_patch(), flame_hem(), guardian_sash() (+1 more)

## Knowledge Gaps
- **204 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+199 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 958 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **54 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `Shared helpers`, `load_clans`, `ROADMAP.md`?**
  _High betweenness centrality (0.464) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _204 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Person`, `Memory`, `.cap`, `Question`, `Mood`, `CourtshipTest`, `Conflict`, `Run`, `.romance`, `Personality`, `Tier`, `.person`, `ClanRelations`, `BondWorld`, `Playthrough.java`, `org.junit.jupiter.api.Test`, `ROADMAP.md`?**
  _High betweenness centrality (0.450) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12698412698412698 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `fabric`, `Clans`, `footwear`, `leg_bone`, `solid`, `kit_kunoichi.py`, `kit_shinobi.py`, `Box`, `cel_box`, `flaps`, `ring_shell`, `masks.py`, `anime.py`, `bangs`, `strip_fabric`, `bandage`, `kit.py`, `kit_hagane.py`?**
  _High betweenness centrality (0.406) - this node is a cross-community bridge._