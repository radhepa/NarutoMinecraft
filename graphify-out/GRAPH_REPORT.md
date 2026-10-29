# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 116 files · ~154,447 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2358 nodes · 5654 edges · 142 communities (100 shown, 42 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 546 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e7d2d348`
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
- strip_fabric
- kit_aburame.py
- kit_shinobi.py
- kit_suzuran.py
- 7. Systems in the beta
- .roll
- k
- kit_hyuga.py
- kit_rugged.py
- jika_tabi
- kit_tobari.py
- Garment
- .classic
- Meters
- arm_bone
- Shared helpers
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
- Playthrough
- Seeds
- News
- rot_matrix
- build
- Box
- chain
- kit_tsuchigumo.py
- kit_nara.py
- kit_gekko.py
- Act
- Stage
- kit_hagane.py
- BondWorld
- rnd
- Playthrough.java
- .person
- Kind
- .answer
- .everyKeyTheEngineEmitsIsListed
- Squad
- .invited
- VillageScaleTest
- Bond
- .of
- Bonds
- .valuesAndToneLandOnTheirPersonalityAndOppositePolesContradict
- Def
- Levels
- Deed
- .refuse
- .romance
- AnswerTag
- .apply
- Face
- Personality
- Mood
- .read
- 4.3 The noble clans
- kit_haruno.py
- .page
- Peeve
- ClanRelations
- Shared helpers
- kit_umino.py
- .tier
- Meter
- Title
- .name
- Village
- Run
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- Memory
- Label
- org.junit.jupiter.api.Test
- Mood
- Kind
- Question
- 7. Inter-clan politics as quests
- Conflict
- .write
- kit_household.py
- SquadTest
- .effectiveLevel
- Tier
- Phase
- flaps
- kit_hatake.py
- Layer
- anime.py
- .test
- 8. Beta catalogue
- VillageTest
- 4. Clan quest lines
- rope_face
- stripes
- wrap_front
- coat_skirts
- gloves
- shag_face
- herb_pouch
- clip
- hairpin
- blossom
- solid
- kit_sarutobi.py
- geta
- cel_box
- wave_band
- scarf

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 177 edges
3. `solid()` - 152 edges
4. `Act` - 120 edges
5. `fabric()` - 109 edges
6. `Bond` - 66 edges
7. `Village` - 63 edges
8. `strip_fabric()` - 59 edges
9. `Person` - 53 edges
10. `stamp()` - 47 edges

## Surprising Connections (you probably didn't know these)
- `7. Questions and choices` --references--> `Question`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Question.java
- `15. Pacing` --references--> `TimeAndPacingTest`  [INFERRED]
  BONDS.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `9. Pacing with time together` --references--> `TimeAndPacingTest`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Life together` --references--> `Activity`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Activity.java

## Import Cycles
- None detected.

## Communities (142 total, 42 thin omitted)

### Community 0 - "fabric"
Cohesion: 0.14
Nodes (10): back_crest(), gloves(), head_cloth(), heavy_boots(), arm_protector(), forehead_protector(), protector_plate(), backward_bandana() (+2 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.19
Nodes (6): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.07
Nodes (15): drawstrings(), forearm_wraps(), holster(), hood_down(), leg_cloth(), ribbed(), sash(), shin_wraps() (+7 more)

### Community 7 - "Story bible"
Cohesion: 0.05
Nodes (41): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+33 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.09
Nodes (11): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+3 more)

### Community 9 - "rnd"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "strip_fabric"
Cohesion: 0.14
Nodes (8): arm_cloth(), cloth_shoes(), trouser_legs(), waist(), kimono_sleeves(), arm_warmers(), tabi_boots(), strip_fabric()

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_shinobi.py"
Cohesion: 0.20
Nodes (4): back_crest(), bandaged_arm(), anbu_arms(), bandage()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.12
Nodes (8): apothecary_sash(), armband(), back_crest(), bell_hem(), bell_print(), bell_sprig(), sash_vials(), vial()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".roll"
Cohesion: 0.12
Nodes (9): Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan, Together (+1 more)

### Community 17 - "k"
Cohesion: 0.08
Nodes (13): tape(), sword_strap(), mandarin_collar(), shin_wrap(), coat_skirts(), pauldron(), trench_knife(), bandolier() (+5 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.13
Nodes (8): bangs(), curtain(), back_sheet(), blunt_fringe(), obi(), parted_fringe(), tabi(), wrap_front()

### Community 19 - "kit_rugged.py"
Cohesion: 0.09
Nodes (11): baggy_legs(), cape(), dread(), knot_bun(), leg_wraps(), patch(), rope_hair(), shin_guard() (+3 more)

### Community 20 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 21 - "kit_tobari.py"
Cohesion: 0.07
Nodes (16): vest(), pouch(), anbu_plates(), shirt(), decal(), hood_down(), lantern(), lantern_tag() (+8 more)

### Community 22 - "Garment"
Cohesion: 0.20
Nodes (4): compatible(), Garment, key_rgba(), png_bytes()

### Community 23 - ".classic"
Cohesion: 0.13
Nodes (3): BondDialogueTest, KindlingAndBookTest, VillageScaleTest

### Community 25 - "arm_bone"
Cohesion: 0.12
Nodes (12): sleeve_roll(), sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), kimono_sleeves(), tasuki() (+4 more)

### Community 26 - "Shared helpers"
Cohesion: 0.20
Nodes (6): Shared helpers, sidelocks(), neckline(), mesh(), sandals(), wraps()

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (20): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kyahan() (+12 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "kit.py"
Cohesion: 0.15
Nodes (7): body(), collar(), footwear(), legs(), sleeves(), stockings(), waistband()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.08
Nodes (14): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+6 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.12
Nodes (22): catalog(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_eye_colors() (+14 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "kit_shiranui.py"
Cohesion: 0.21
Nodes (5): crest(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

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
Cohesion: 0.17
Nodes (5): flick(), gourd(), lames(), shoku_disc(), snack_pouch()

### Community 43 - "kokuto"
Cohesion: 0.24
Nodes (4): back_blade(), crest(), hip_kokuto(), kokuto()

### Community 44 - "Playthrough"
Cohesion: 0.20
Nodes (8): Playthrough, Profile, DEVOTED, RECKLESS, TYPICAL, Result, Row, TimeAndPacingTest

### Community 45 - "Seeds"
Cohesion: 0.21
Nodes (3): 5. Personality, Rng, Seeds

### Community 47 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.09
Nodes (12): puff(), band(), curls_box(), dark_seams(), hair_box(), hair_face(), hair_shade(), hem() (+4 more)

### Community 51 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (7): glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 52 - "kit_nara.py"
Cohesion: 0.10
Nodes (12): ring_shell(), crown(), clipped(), combed_back(), back_crest(), crest(), mesh_shirt(), net() (+4 more)

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (73): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+65 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.27
Nodes (4): bracers(), mace(), plate(), shin_guards()

### Community 59 - "rnd"
Cohesion: 0.08
Nodes (13): quilt(), sprigs(), splatter(), wisteria_hem(), kasuri(), camo(), ragged(), ink_stains() (+5 more)

### Community 60 - "Playthrough.java"
Cohesion: 0.05
Nodes (16): ClanProfile, Stage, ADULT, CHILD, TEEN, Value, COURAGE, CREATIVITY (+8 more)

### Community 61 - ".person"
Cohesion: 0.18
Nodes (3): 8. The village talks, GossipTest, Leaf

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - ".answer"
Cohesion: 0.15
Nodes (4): BondWeb, Answered, Outcome, Questions

### Community 64 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.16
Nodes (4): DialogueKeys, DialogueKeysTest, ReactionTest, 10. Content plan

### Community 66 - ".invited"
Cohesion: 0.19
Nodes (5): 20. What the roadmap asks of bonds, Tier, BACKGROUND, CAST, KNOWN

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (15): 12. The bond book, 13. Data formats, 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 21. Open questions, 2. The meters (+7 more)

### Community 71 - ".valuesAndToneLandOnTheirPersonalityAndOppositePolesContradict"
Cohesion: 0.19
Nodes (3): QuestionsCompiledTest, QuestionsTest, SampleQuestions

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.18
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (3): Deed, Know, Gossip

### Community 77 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 79 - "Face"
Cohesion: 0.15
Nodes (9): mark(), drawn_line(), button(), curls_face(), darken_rows(), grid(), line(), rivets() (+1 more)

### Community 80 - "Personality"
Cohesion: 0.13
Nodes (8): Personality, Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH, Reaction

### Community 81 - "Mood"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.17
Nodes (6): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim()

### Community 85 - ".page"
Cohesion: 0.30
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Peeve"
Cohesion: 0.13
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 88 - "Shared helpers"
Cohesion: 0.20
Nodes (5): lock(), hime_locks(), wave_lock(), beard(), flicks()

### Community 89 - "kit_umino.py"
Cohesion: 0.07
Nodes (15): spike(), tie(), crown(), gathered_tail(), hair_tie(), burst(), pineapple(), brush_tail() (+7 more)

### Community 90 - ".tier"
Cohesion: 0.26
Nodes (4): 11. Kindling Bond, Bonfire, Flame, Kindling

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (7): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - "Title"
Cohesion: 0.16
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

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

### Community 98 - "Person"
Cohesion: 0.16
Nodes (3): 1. The data model, Person, Schedule

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.16
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.22
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 104 - "Kind"
Cohesion: 0.18
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 109 - "kit_household.py"
Cohesion: 0.10
Nodes (11): bands(), checks(), collar_band(), dots(), ichimatsu(), kasuri(), overlap(), sash() (+3 more)

### Community 112 - ".effectiveLevel"
Cohesion: 0.15
Nodes (5): BondDialogue, Conversation, Reply, Topic, 6. Conversation

### Community 113 - "Tier"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 114 - "Phase"
Cohesion: 0.32
Nodes (6): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER

### Community 115 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 117 - "kit_hatake.py"
Cohesion: 0.25
Nodes (3): decal(), shoulder_decal(), slanted_protector()

### Community 119 - "anime.py"
Cohesion: 0.25
Nodes (3): back_fan(), braid(), cel_face()

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 136 - "solid"
Cohesion: 0.06
Nodes (21): How the pieces work, belt(), harness(), face_mask(), white_fang_tanto(), frog_buttons(), mandarin_collar(), obi() (+13 more)

### Community 137 - "kit_sarutobi.py"
Cohesion: 0.17
Nodes (8): stamp(), back_crest(), crest(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey()

### Community 147 - "cel_box"
Cohesion: 0.15
Nodes (7): cel_box(), topknot(), ear_panels(), round_bun(), wave_lock(), nape_hem(), bun()

## Knowledge Gaps
- **210 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+205 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 966 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **42 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.448) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _210 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.1380952380952381 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Story bible`, `.roll`, `Meters`, `Seeds`, `Stage`, `Playthrough.java`, `.person`, `.invited`, `Levels`, `.romance`, `Personality`, `ClanRelations`, `.tier`, `Village`, `Person`, `Memory`, `Mood`, `Conflict`, `.write`?**
  _High betweenness centrality (0.438) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `fabric`, `Clans`, `solid`, `strip_fabric`, `kit_shinobi.py`, `Box`, `kit_hyuga.py`, `cel_box`, `kit_nara.py`, `flaps`, `kit_tobari.py`, `anime.py`, `Shared helpers`, `kit_umino.py`, `kit.py`, `kit_field.py`?**
  _High betweenness centrality (0.384) - this node is a cross-community bridge._