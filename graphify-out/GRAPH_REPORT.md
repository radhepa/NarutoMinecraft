# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 129 files · ~162,337 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2452 nodes · 5677 edges · 146 communities (108 shown, 38 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 535 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `17072077`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Roster
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
- fabric
- kit_suzuran.py
- 7. Systems in the beta
- .person
- solid
- cel_box
- kit_rugged.py
- kit_household.py
- kit_tobari.py
- Garment
- mesh_shirt
- kit_shimura.py
- arm_bone
- strip_fabric
- kit_market.py
- kit_kinoshita.py
- k
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
- .xpAt
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
- .bond
- kit_hagane.py
- .effectiveLevel
- kit_specialist.py
- org.junit.jupiter.api.Test
- Kind
- Meters
- .play
- .romance
- VillageScaleTest
- Bond
- .of
- Bonds
- .read
- Def
- Levels
- Deed
- Person
- .romance
- Playthrough.java
- Squad
- Face
- Value
- Mood
- kit_shinobi.py
- 4.3 The noble clans
- kit_haruno.py
- .page
- Personality
- ClanRelations
- Shared helpers
- kit_umino.py
- .day
- Meter
- .name
- Niche
- 18. Village scale
- Side quests
- 4.4 The minor clans
- Run
- 2. Quest framework
- Memory
- Label
- roster.py
- VillageSim.java
- Seeds
- Stretch
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- kit_nara.py
- glyphs.py
- paint.py
- 4. Clan quest lines
- Tier
- Rng
- flaps
- Conflict
- Stage
- The village
- Ranks
- wrap_front
- Tier
- Side quest secrets
- .talk
- jika_tabi
- bangs
- Naruto Minecraft
- wide_sleeves
- leg_bone
- blossom
- cloth_shoes
- geta
- overlap
- topknot
- sprigs
- kit_sarutobi.py
- wave_band
- bandolier
- apothecary_sash
- bun
- rnd

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 155 edges
3. `solid()` - 152 edges
4. `Act` - 113 edges
5. `fabric()` - 109 edges
6. `Village` - 63 edges
7. `strip_fabric()` - 59 edges
8. `Bond` - 57 edges
9. `Person` - 51 edges
10. `stamp()` - 47 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Life together` --references--> `Activity`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Activity.java
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java

## Import Cycles
- None detected.

## Communities (146 total, 38 thin omitted)

### Community 0 - "Roster"
Cohesion: 0.07
Nodes (9): 7. Growing up together, Hooks for the other mods, Pulling their weight, The 60 hours, simulated, The model, Contribution, GrowthEvent, Grower (+1 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

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
Nodes (13): drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps(), side_stripe() (+5 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.10
Nodes (10): belt(), arm_warmers(), frog_buttons(), mandarin_collar(), obi(), round_bun(), shin_wrap(), tabi_boots() (+2 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "fabric"
Cohesion: 0.12
Nodes (10): back_crest(), crest(), back_crest(), head_cloth(), arm_protector(), forehead_protector(), protector_plate(), backward_bandana() (+2 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.16
Nodes (6): back_crest(), bell_hem(), bell_print(), bell_sprig(), sash_vials(), vial()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".person"
Cohesion: 0.09
Nodes (10): Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan, Together (+2 more)

### Community 17 - "solid"
Cohesion: 0.07
Nodes (15): face_mask(), white_fang_tanto(), obi(), coat_skirts(), pauldron(), scarf(), trench_knife(), cane() (+7 more)

### Community 18 - "cel_box"
Cohesion: 0.19
Nodes (8): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), knot()

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "kit_household.py"
Cohesion: 0.11
Nodes (9): bands(), checks(), collar_band(), dots(), ichimatsu(), kasuri(), sash(), socks() (+1 more)

### Community 21 - "kit_tobari.py"
Cohesion: 0.07
Nodes (16): shirt(), vest(), anbu_plates(), shirt(), decal(), hood_down(), lantern(), lantern_tag() (+8 more)

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 24 - "kit_shimura.py"
Cohesion: 0.29
Nodes (3): back_crest(), bandaged_arm(), bandage()

### Community 25 - "arm_bone"
Cohesion: 0.12
Nodes (12): sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), kimono_sleeves(), tasuki(), armband() (+4 more)

### Community 26 - "strip_fabric"
Cohesion: 0.09
Nodes (12): leg_cloth(), waist(), body(), arm_cloth(), trouser_legs(), waist(), kimono_sleeves(), tabi() (+4 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+14 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "k"
Cohesion: 0.12
Nodes (13): collar(), flaps(), footwear(), sword_strap(), legs(), neckline(), pouch(), stockings() (+5 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.11
Nodes (9): cargo(), collar(), gloves(), half_sleeves(), pocket(), shirt(), strap(), tape() (+1 more)

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
Cohesion: 0.21
Nodes (5): crest(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.29
Nodes (3): crest_patch(), seal_script(), seal_tags()

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
Cohesion: 0.14
Nodes (7): flick(), gourd(), lames(), puff(), shoku_disc(), snack_pouch(), curls_box()

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Playthrough"
Cohesion: 0.06
Nodes (26): 15. Pacing, DialogueKeys, DialogueKeysTest, Chapter, Phase, ACADEMY, EXAMS, GENIN (+18 more)

### Community 45 - ".xpAt"
Cohesion: 0.14
Nodes (5): 8. Data, code and Phase 0, BondInput, Day, RosterTest, TechniqueTest

### Community 47 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.10
Nodes (5): band(), hem(), strip_line(), Box, Layer

### Community 51 - "kit_tsuchigumo.py"
Cohesion: 0.15
Nodes (7): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 52 - "ring_shell"
Cohesion: 0.16
Nodes (7): cel_face(), ring_shell(), crown(), combed_back(), nape_hem(), combed_up(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (70): Act, ABANDONED_MISSION, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED, BOND_MOMENT (+62 more)

### Community 55 - "Stage"
Cohesion: 0.10
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.18
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 58 - ".effectiveLevel"
Cohesion: 0.12
Nodes (3): 20. What the roadmap asks of bonds, Recruitment, Standing

### Community 59 - "kit_specialist.py"
Cohesion: 0.15
Nodes (6): bandolier(), coat_skirts(), cross_armband(), ink_stains(), scroll_tube(), strap()

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.09
Nodes (9): 11. Kindling Bond, Grant, BondDialogueTest, ConditionsAndEffectsTest, GossipTest, KindlingAndBookTest, SquadTest, VillageTest (+1 more)

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - "Meters"
Cohesion: 0.14
Nodes (3): Meters, Reaction, ReactionTest

### Community 65 - ".play"
Cohesion: 0.12
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 66 - ".romance"
Cohesion: 0.18
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 67 - "VillageScaleTest"
Cohesion: 0.13
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.05
Nodes (4): Bond, BondConditions, BondWeb, FollowUp

### Community 70 - "Bonds"
Cohesion: 0.12
Nodes (13): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 5. Personality (+5 more)

### Community 71 - ".read"
Cohesion: 0.23
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.18
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.13
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 78 - "Squad"
Cohesion: 0.08
Nodes (3): BondEffects, Departure, Squad

### Community 79 - "Face"
Cohesion: 0.19
Nodes (6): button(), darken_rows(), grid(), line(), rivets(), Face

### Community 80 - "Value"
Cohesion: 0.12
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - "Mood"
Cohesion: 0.12
Nodes (9): 18. Village scale, Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY (+1 more)

### Community 82 - "kit_shinobi.py"
Cohesion: 0.11
Nodes (10): How the pieces work, anbu_arms(), flak_vest(), mesh(), tanto(), beak(), bump(), ears() (+2 more)

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - ".page"
Cohesion: 0.26
Nodes (5): 12. The bond book, BondBook, Fact, MemoryLine, Page

### Community 86 - "Personality"
Cohesion: 0.10
Nodes (13): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+5 more)

### Community 88 - "Shared helpers"
Cohesion: 0.13
Nodes (10): Shared helpers, back_fan(), braid(), lock(), sidelocks(), hime_locks(), wave_lock(), beard() (+2 more)

### Community 89 - "kit_umino.py"
Cohesion: 0.20
Nodes (4): falling_tail(), surf(), wave_band(), waves()

### Community 91 - "Meter"
Cohesion: 0.10
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - ".name"
Cohesion: 0.08
Nodes (13): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, Title, GOOD_NEIGHBOR (+5 more)

### Community 93 - "Niche"
Cohesion: 0.10
Nodes (13): Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING, SUPPORT (+5 more)

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
Cohesion: 0.15
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "roster.py"
Cohesion: 0.18
Nodes (9): bucket(), check(), counts(), first_level(), load(), main(), strings(), table() (+1 more)

### Community 105 - "Stretch"
Cohesion: 0.14
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "kit_nara.py"
Cohesion: 0.15
Nodes (7): spike(), back_crest(), crest(), pineapple(), pulled_back(), tuft(), brush_tail()

### Community 110 - "paint.py"
Cohesion: 0.19
Nodes (6): dark_seams(), hair_box(), hair_face(), hair_shade(), shell(), shade()

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Tier"
Cohesion: 0.33
Nodes (5): Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 115 - "flaps"
Cohesion: 0.40
Nodes (3): robe_skirt(), skirt(), side_panels()

### Community 117 - "Stage"
Cohesion: 0.33
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 118 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 119 - "Ranks"
Cohesion: 0.17
Nodes (12): 1. The hierarchy, 2. Rank and power, 3. Feeling the strong, 4. Head counts, 5. Who matters most, 6. The roster, 9. Open questions, Contents (+4 more)

### Community 122 - "Tier"
Cohesion: 0.20
Nodes (7): Tier, A, B, C, D, E, S

### Community 123 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 124 - ".talk"
Cohesion: 0.39
Nodes (4): Conversation, Reply, Topic, 6. Conversation

### Community 125 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 126 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

### Community 128 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 130 - "leg_bone"
Cohesion: 0.13
Nodes (8): blouse(), holster(), knee_guards(), hakama_legs(), thigh_holster(), leg_bone(), leg_ring(), heavy_boots()

### Community 137 - "kit_sarutobi.py"
Cohesion: 0.15
Nodes (9): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), crest_patch(), flame_hem(), guardian_sash() (+1 more)

### Community 148 - "rnd"
Cohesion: 0.18
Nodes (6): quilt(), clipped(), seal_trim(), cloth_shade(), curls_face(), rnd()

## Knowledge Gaps
- **208 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+203 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 993 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **38 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `Shared helpers`, `ROADMAP.md`?**
  _High betweenness centrality (0.441) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _208 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Roster` be split into smaller, more focused modules?**
  _Cohesion score 0.07198228128460686 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `Clans`, `leg_bone`, `kit_kunoichi.py`, `kit_nara.py`, `fabric`, `Box`, `cel_box`, `kit_shinobi.py`, `ring_shell`, `solid`, `kit_shimura.py`, `strip_fabric`, `k`, `bangs`?**
  _High betweenness centrality (0.382) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `.person`, `Playthrough`, `Stage`, `.effectiveLevel`, `org.junit.jupiter.api.Test`, `Meters`, `.read`, `Levels`, `Deed`, `Person`, `.romance`, `Value`, `Mood`, `.page`, `Personality`, `ClanRelations`, `ROADMAP.md`, `Memory`, `Conflict`?**
  _High betweenness centrality (0.370) - this node is a cross-community bridge._