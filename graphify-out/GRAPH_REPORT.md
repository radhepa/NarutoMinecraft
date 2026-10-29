# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 118 files · ~157,772 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2401 nodes · 5837 edges · 155 communities (101 shown, 54 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 579 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6d499470`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_shiranui.py
- kit_uchiha.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- kit_inuzuka.py
- kit_haruno.py
- fabric
- kit_aburame.py
- topknot
- paint.py
- 7. Systems in the beta
- .roll
- k
- cel_box
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
- mandarin_collar
- 5. Data formats built for the whole story
- Seeds
- wardrobe.py
- 11. Later systems
- Shinobi Modpack: roadmap
- QuestionsTest
- 4. Technical architecture
- 6. The map
- head_cloth
- 8. The beta, chapter by chapter
- 9. Delivery plan
- kit_yamanaka.py
- kit_akimichi.py
- kokuto
- Playthrough
- paint.py
- Run
- kit_shinobi.py
- build
- Box
- Face
- solid
- rnd
- kit_gekko.py
- Act
- Stage
- .snapshot
- kit_hagane.py
- BondWorld
- sprigs
- Playthrough.java
- mesh_shirt
- Kind
- Question
- .everyKeyTheEngineEmitsIsListed
- Squad
- Question
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
- Label
- News
- Mood
- BondEvent
- 4.3 The noble clans
- Phase
- .page
- Personality
- kit_specialist.py
- kit_umino.py
- .tier
- BondEffects
- Title
- BondEvent
- ClanProfile
- belt
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- Memory
- Label
- ReactionTest.java
- Kind
- .read
- 7. Inter-clan politics as quests
- Conflict
- chain
- kit_household.py
- org.junit.jupiter.api.Test
- .talk
- Tier
- Tier
- shade
- wide_sleeves
- forearm_wraps
- .classic
- Shared helpers
- harness
- 8. Beta catalogue
- frog_clasps
- 4. Clan quest lines
- kimono_trim
- white_fang_tanto
- kit_kunoichi.py
- geta
- flaps
- jika_tabi
- bandolier
- bandolier
- overlap
- mandarin_collar
- shin_wrap
- Piece
- fabric
- stamp
- cane
- bell_charm
- coat_skirts
- gloves
- herb_pouch
- kit_uzumaki.py
- scroll
- stamp
- bun
- waves
- hood_down
- blossom
- cloth_shoes
- coat_skirts
- scroll_tube

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 192 edges
3. `solid()` - 152 edges
4. `Act` - 125 edges
5. `fabric()` - 109 edges
6. `Bond` - 67 edges
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
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Life together` --references--> `Activity`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Activity.java

## Import Cycles
- None detected.

## Communities (155 total, 54 thin omitted)

### Community 0 - "kit_shiranui.py"
Cohesion: 0.12
Nodes (9): forehead_protector(), protector_plate(), backward_bandana(), crest(), flicks(), mouth_senbon(), senbon(), thigh_holster() (+1 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.19
Nodes (6): arm_crest(), back_crest(), chest_crest(), crest(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.06
Nodes (30): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+22 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.09
Nodes (11): drawstrings(), holster(), ribbed(), sash(), shin_wraps(), side_stripe(), sleeve_roll(), stripes() (+3 more)

### Community 7 - "Story bible"
Cohesion: 0.05
Nodes (40): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+32 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_haruno.py"
Cohesion: 0.27
Nodes (4): arm_crest(), back_crest(), chest_crest(), circle()

### Community 11 - "fabric"
Cohesion: 0.10
Nodes (11): leg_cloth(), waist(), arm_cloth(), trouser_legs(), waist(), tabi(), arm_warmers(), gloves() (+3 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 14 - "paint.py"
Cohesion: 0.16
Nodes (6): back_crest(), bell_hem(), bell_print(), bell_sprig(), sash_vials(), vial()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".roll"
Cohesion: 0.11
Nodes (7): Activity, Answer, Invitation, Plan, Together, TogetherTest, 3. Hangouts

### Community 17 - "k"
Cohesion: 0.10
Nodes (11): back_crest(), sword_strap(), wrap_front(), wrap_front(), back_crest(), wave_band(), neckline(), stockings() (+3 more)

### Community 18 - "cel_box"
Cohesion: 0.11
Nodes (12): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), round_bun() (+4 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "Stage"
Cohesion: 0.33
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 21 - "kit_specialist.py"
Cohesion: 0.07
Nodes (16): shirt(), vest(), pouch(), anbu_plates(), decal(), hood_down(), lantern(), lantern_tag() (+8 more)

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 24 - "Meters"
Cohesion: 0.10
Nodes (7): Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Meters

### Community 25 - "arm_bone"
Cohesion: 0.13
Nodes (11): sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), kimono_sleeves(), tasuki(), armband() (+3 more)

### Community 26 - "kit_field.py"
Cohesion: 0.07
Nodes (17): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+9 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "Seeds"
Cohesion: 0.21
Nodes (3): 5. Personality, Rng, Seeds

### Community 32 - "wardrobe.py"
Cohesion: 0.17
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
Cohesion: 0.24
Nodes (4): back_blade(), crest(), hip_kokuto(), kokuto()

### Community 44 - "Playthrough"
Cohesion: 0.14
Nodes (10): 15. Pacing, Playthrough, Profile, DEVOTED, RECKLESS, TYPICAL, Result, Row (+2 more)

### Community 45 - "paint.py"
Cohesion: 0.17
Nodes (7): band(), cloth_shade(), hair_box(), hair_face(), hair_shade(), hem(), shell()

### Community 47 - "kit_shinobi.py"
Cohesion: 0.29
Nodes (3): back_crest(), bandaged_arm(), bandage()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.11
Nodes (3): strip_line(), Box, Layer

### Community 50 - "Face"
Cohesion: 0.10
Nodes (12): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), button() (+4 more)

### Community 51 - "solid"
Cohesion: 0.12
Nodes (9): face_mask(), obi(), arm_protector(), shimenawa(), high_collar(), clip(), wrap_tie(), strap() (+1 more)

### Community 52 - "rnd"
Cohesion: 0.12
Nodes (11): cel_face(), ring_shell(), crown(), clipped(), combed_back(), nape_hem(), pulled_back(), ink_stains() (+3 more)

### Community 53 - "kit_gekko.py"
Cohesion: 0.22
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (78): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+70 more)

### Community 55 - "Stage"
Cohesion: 0.11
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.27
Nodes (4): bracers(), mace(), plate(), shin_guards()

### Community 58 - "BondWorld"
Cohesion: 0.09
Nodes (3): 12. The bond book, BondWeb, BondWorld

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Question"
Cohesion: 0.19
Nodes (3): Answered, Outcome, Questions

### Community 64 - ".everyKeyTheEngineEmitsIsListed"
Cohesion: 0.19
Nodes (4): DialogueKeys, DialogueKeysTest, ReactionTest, 10. Content plan

### Community 66 - "Question"
Cohesion: 0.25
Nodes (3): Answer, Question, QuestionsCompiledTest

### Community 67 - "VillageScaleTest"
Cohesion: 0.12
Nodes (4): 20. What the roadmap asks of bonds, Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (5): Bond, BondConditions, FollowUp, Highlight, Outcome

### Community 69 - ".of"
Cohesion: 0.13
Nodes (3): ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.10
Nodes (15): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+7 more)

### Community 71 - "How the pieces work"
Cohesion: 0.18
Nodes (6): How the pieces work, flak_vest(), mesh(), tanto(), beak(), ears()

### Community 72 - "Def"
Cohesion: 0.09
Nodes (12): Def, Lean, Size, BIG, NOTABLE, SMALL, Trait, BOLDNESS (+4 more)

### Community 73 - "Levels"
Cohesion: 0.13
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (3): Deed, Know, Gossip

### Community 75 - "Experience"
Cohesion: 0.17
Nodes (10): Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION, SPAR (+2 more)

### Community 77 - "AnswerTag"
Cohesion: 0.12
Nodes (17): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+9 more)

### Community 79 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "BondEvent"
Cohesion: 0.31
Nodes (3): Gifts, Received, GiftsTest

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "Phase"
Cohesion: 0.32
Nodes (6): Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER

### Community 85 - ".page"
Cohesion: 0.21
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Personality"
Cohesion: 0.06
Nodes (25): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+17 more)

### Community 89 - "kit_umino.py"
Cohesion: 0.12
Nodes (8): spike(), crown(), burst(), brush_tail(), combed_up(), falling_tail(), surf(), waves()

### Community 90 - ".tier"
Cohesion: 0.14
Nodes (8): 11. Kindling Bond, Bonfire, Flame, Kindling, Read, Sight, Thread, KindlingAndBookTest

### Community 92 - "Title"
Cohesion: 0.12
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "BondEvent"
Cohesion: 0.14
Nodes (4): 13. Data formats, BondDialogue, BondEvent, Household

### Community 96 - "Side quests"
Cohesion: 0.20
Nodes (10): 1. Scope and budget, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents, In the beta (+2 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "Person"
Cohesion: 0.16
Nodes (3): Person, Schedule, 2. Schedules

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.21
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 104 - "Kind"
Cohesion: 0.20
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "Conflict"
Cohesion: 0.12
Nodes (7): Conflict, State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 109 - "kit_household.py"
Cohesion: 0.11
Nodes (9): bands(), checks(), collar_band(), dots(), ichimatsu(), kasuri(), sash(), socks() (+1 more)

### Community 112 - ".talk"
Cohesion: 0.39
Nodes (4): Conversation, Reply, Topic, 6. Conversation

### Community 113 - "Tier"
Cohesion: 0.12
Nodes (12): Power, EMBER_LINK, EMBER_MARK, KINDLE, SMALL_KINDLE, THREAD_SIGHT, UNISON, Tier (+4 more)

### Community 114 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 118 - ".classic"
Cohesion: 0.18
Nodes (4): 8. The village talks, BondDialogueTest, ConditionsAndEffectsTest, GossipTest

### Community 119 - "Shared helpers"
Cohesion: 0.12
Nodes (11): Shared helpers, back_fan(), bangs(), braid(), lock(), sidelocks(), blunt_fringe(), hime_locks() (+3 more)

### Community 121 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 123 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 128 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 129 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 135 - "Piece"
Cohesion: 0.18
Nodes (5): wave_lock(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 136 - "fabric"
Cohesion: 0.17
Nodes (8): body(), collar(), footwear(), kimono_sleeves(), legs(), sleeves(), waistband(), fabric()

### Community 137 - "stamp"
Cohesion: 0.10
Nodes (12): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), back_crest(), crest(), dolphin() (+4 more)

### Community 143 - "kit_uzumaki.py"
Cohesion: 0.32
Nodes (3): seal_script(), seal_tags(), wide_sleeves()

### Community 147 - "stamp"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

## Knowledge Gaps
- **215 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+210 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 972 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **54 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.441) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _215 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_shiranui.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12105263157894737 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Story bible`, `Meters`, `Seeds`, `Playthrough`, `Stage`, `.snapshot`, `BondWorld`, `VillageScaleTest`, `Levels`, `SocialTie`, `Mood`, `Personality`, `.tier`, `BondEvent`, `Person`, `Memory`, `Label`, `Conflict`, `.classic`?**
  _High betweenness centrality (0.438) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `flaps`, `kit_shiranui.py`, `Clans`, `How the pieces work`, `fabric`, `fabric`, `paint.py`, `kit_shinobi.py`, `k`, `cel_box`, `solid`, `rnd`, `kit_specialist.py`, `kit_umino.py`, `kit_field.py`, `belt`?**
  _High betweenness centrality (0.393) - this node is a cross-community bridge._