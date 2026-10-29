# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 131 files · ~165,079 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2482 nodes · 5735 edges · 153 communities (104 shown, 49 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 542 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `59625dbf`
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
- paint.py
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
- wide_sleeves
- 8. The beta, chapter by chapter
- 9. Delivery plan
- floral_trim
- kit_akimichi.py
- kokuto
- Playthrough
- .xpAt
- News
- rot_matrix
- Personality
- Box
- chain
- .xpAt
- ring_shell
- kit_gekko.py
- Act
- Stage
- .bond
- kit_hagane.py
- Recruitment
- kit_specialist.py
- org.junit.jupiter.api.Test
- Kind
- Meters
- list
- .play
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
- kit_shinobi.py
- Squad
- Face
- Life together
- Label
- kit_shinobi.py
- 4.3 The noble clans
- kit_haruno.py
- .cap
- Personality
- ClanRelations
- Shared helpers
- kit_umino.py
- .page
- Meter
- Title
- Niche
- 18. Village scale
- Side quests
- 4.4 The minor clans
- 2. Quest framework
- hood_down
- Label
- roster.py
- .optional
- Seeds
- Stretch
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- glyphs.py
- rnd
- 4. Clan quest lines
- Tier
- Rng
- flaps
- Conflict
- Tier
- The village
- Ranks
- wrap_front
- Tier
- Side quest secrets
- .talk
- jika_tabi
- bangs
- belt
- Naruto Minecraft
- wide_sleeves
- bandolier
- BondWeb
- sword_strap
- white_fang_tanto
- arm_cloth
- topknot
- bands
- kit_sarutobi.py
- wave_band
- bandolier
- checks
- bun
- sash
- trench_knife
- scarf
- coat_skirts
- shimenawa
- waves
- flower
- wrapped

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
10. `Roster` - 47 edges

## Surprising Connections (you probably didn't know these)
- `The 60 hours, simulated` --references--> `SeasonTest`  [INFERRED]
  docs/RANKS.md → life/roster/src/test/java/dev/shinobi/life/roster/SeasonTest.java
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Life together` --references--> `Activity`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Activity.java
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java
- `18. Village scale` --references--> `ClanRelations`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/ClanRelations.java

## Import Cycles
- None detected.

## Communities (153 total, 49 thin omitted)

### Community 0 - "Roster"
Cohesion: 0.09
Nodes (7): 8. Growing up together, Hooks for the other mods, Pulling their weight, The 60 hours, simulated, Contribution, GrowthEvent, Roster

### Community 1 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.09
Nodes (20): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+12 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.14
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.06
Nodes (16): drawstrings(), forearm_wraps(), holster(), hood_down(), leg_cloth(), ribbed(), sash(), shin_wraps() (+8 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.11
Nodes (8): frog_buttons(), kimono_sleeves(), mandarin_collar(), round_bun(), shin_wrap(), thigh_holster(), wave_lock(), wrap_front()

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "fabric"
Cohesion: 0.11
Nodes (11): back_crest(), crest(), back_crest(), head_cloth(), arm_protector(), forehead_protector(), protector_plate(), backward_bandana() (+3 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".person"
Cohesion: 0.09
Nodes (11): Activity, BondEvent, Answer, FollowUp, Highlight, Invitation, Outcome, Plan (+3 more)

### Community 17 - "solid"
Cohesion: 0.08
Nodes (12): harness(), face_mask(), obi(), coat_skirts(), pauldron(), cane(), scroll_tube(), scroll() (+4 more)

### Community 18 - "cel_box"
Cohesion: 0.17
Nodes (9): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), pineapple() (+1 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "kit_household.py"
Cohesion: 0.10
Nodes (10): blossom(), collar_band(), dots(), geta(), ichimatsu(), kasuri(), overlap(), socks() (+2 more)

### Community 21 - "kit_tobari.py"
Cohesion: 0.12
Nodes (8): decal(), lantern(), lantern_tag(), muffler(), plain_body(), sash(), shin_wraps(), split_toe_boots()

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 24 - "paint.py"
Cohesion: 0.15
Nodes (3): back_crest(), petal_fabric(), cloth_shade()

### Community 25 - "arm_bone"
Cohesion: 0.13
Nodes (11): sleeve_roll(), sode(), arm_bone(), arm_x(), arm_guards(), bracers(), kimono_sleeves(), tasuki() (+3 more)

### Community 26 - "strip_fabric"
Cohesion: 0.08
Nodes (14): body(), trousers(), vest(), cloth_shoes(), trouser_legs(), waist(), kimono_sleeves(), tabi() (+6 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "k"
Cohesion: 0.21
Nodes (9): collar(), footwear(), legs(), neckline(), pouch(), roll(), stockings(), waistband() (+1 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.06
Nodes (18): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+10 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.13
Nodes (21): build(), build_all(), catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors() (+13 more)

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

### Community 38 - "wide_sleeves"
Cohesion: 0.33
Nodes (3): seal_script(), seal_tags(), wide_sleeves()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 42 - "kit_akimichi.py"
Cohesion: 0.12
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box()

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Playthrough"
Cohesion: 0.08
Nodes (17): 15. Pacing, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+9 more)

### Community 45 - ".xpAt"
Cohesion: 0.15
Nodes (4): 9. Data, code and Phase 0, BondInput, Day, RosterTest

### Community 47 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "Personality"
Cohesion: 0.13
Nodes (5): 20. What the roadmap asks of bonds, 5. Personality, Personality, Reaction, ReactionTest

### Community 49 - "Box"
Cohesion: 0.09
Nodes (7): band(), dark_seams(), hem(), strip_line(), Box, Layer, shade()

### Community 51 - ".xpAt"
Cohesion: 0.14
Nodes (4): Grower, Technique, CurveAndTierTest, TechniqueTest

### Community 52 - "ring_shell"
Cohesion: 0.11
Nodes (11): ring_shell(), crown(), clipped(), combed_back(), nape_hem(), back_crest(), crest(), pulled_back() (+3 more)

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
Cohesion: 0.22
Nodes (4): spike(), crown(), burst(), brush_tail()

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.12
Nodes (5): BondDialogueTest, ConditionsAndEffectsTest, GossipTest, KindlingAndBookTest, SquadTest

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 64 - "list"
Cohesion: 0.11
Nodes (5): Stage, ADULT, CHILD, TEEN, DialogueKeysTest

### Community 65 - ".play"
Cohesion: 0.11
Nodes (15): SeasonTest, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Profile (+7 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.13
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.13
Nodes (3): ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.10
Nodes (14): 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Village scale, 19. Society hooks, 21. Open questions, 2. The meters, 4. Memories, 6. Shared experiences and moments (+6 more)

### Community 71 - ".read"
Cohesion: 0.25
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (9): 8. The village talks, Deed, Know, Gossip, Source, HEARD, SEEN, SELF (+1 more)

### Community 75 - "Person"
Cohesion: 0.13
Nodes (3): 1. The data model, Person, Schedule

### Community 77 - "kit_shinobi.py"
Cohesion: 0.22
Nodes (5): shirt(), anbu_arms(), anbu_plates(), flak_vest(), cap()

### Community 78 - "Squad"
Cohesion: 0.08
Nodes (3): BondEffects, Departure, Squad

### Community 79 - "Face"
Cohesion: 0.09
Nodes (13): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), button() (+5 more)

### Community 80 - "Life together"
Cohesion: 0.29
Nodes (7): 10. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Data and quest hooks, Life together

### Community 81 - "Label"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - "kit_shinobi.py"
Cohesion: 0.16
Nodes (7): How the pieces work, mesh(), tanto(), beak(), bump(), ears(), strap()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 86 - "Personality"
Cohesion: 0.08
Nodes (23): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+15 more)

### Community 88 - "Shared helpers"
Cohesion: 0.13
Nodes (10): Shared helpers, back_fan(), braid(), lock(), sidelocks(), hime_locks(), wave_lock(), beard() (+2 more)

### Community 89 - "kit_umino.py"
Cohesion: 0.20
Nodes (4): falling_tail(), surf(), wave_band(), waves()

### Community 90 - ".page"
Cohesion: 0.09
Nodes (7): 12. The bond book, BondBook, Fact, MemoryLine, Page, BondDialogue, Household

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.16
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Niche"
Cohesion: 0.11
Nodes (13): The model, Niche, GENJUTSU, KENJUTSU, MEDICAL, NINJUTSU, SEALING, SENSING (+5 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "hood_down"
Cohesion: 0.33
Nodes (3): hood_down(), mantle(), pleats()

### Community 101 - "Label"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "roster.py"
Cohesion: 0.14
Nodes (13): bucket(), check(), check_name(), counts(), first_level(), group_of(), load(), main() (+5 more)

### Community 105 - "Stretch"
Cohesion: 0.13
Nodes (9): Curve, Stretch, ACADEMY, CHUNIN, EXAMS, GENIN, JONIN, POST (+1 more)

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 110 - "rnd"
Cohesion: 0.16
Nodes (8): cel_face(), ink_stains(), seal_trim(), hair_box(), hair_face(), hair_shade(), rnd(), shell()

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Tier"
Cohesion: 0.20
Nodes (8): 11. Kindling Bond, Grant, Kindling, Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 114 - "Rng"
Cohesion: 0.10
Nodes (8): ClanPower, CLANLESS, GREAT, MINOR, STRONG, Rng, Seeds, ClanPowerTest

### Community 115 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 116 - "Conflict"
Cohesion: 0.12
Nodes (8): 13. Data formats, Conflict, State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 117 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 118 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 119 - "Ranks"
Cohesion: 0.15
Nodes (13): 10. Open questions, 1. The hierarchy, 2. Rank and power, 3. Clan power, 4. Feeling the strong, 5. Head counts, 6. Who matters most, 7. The roster (+5 more)

### Community 122 - "Tier"
Cohesion: 0.18
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

### Community 137 - "kit_sarutobi.py"
Cohesion: 0.15
Nodes (9): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), crest_patch(), flame_hem(), guardian_sash() (+1 more)

## Knowledge Gaps
- **212 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+207 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1002 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **49 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `Shared helpers`, `ROADMAP.md`?**
  _High betweenness centrality (0.434) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _212 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Roster` be split into smaller, more focused modules?**
  _Cohesion score 0.08571428571428572 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `.read`, `Deed`, `Person`, `Playthrough`, `.romance`, `Personality`, `Tier`, `.person`, `Conflict`, `.cap`, `ClanRelations`, `Stage`, `.page`, `Meters`, `ROADMAP.md`?**
  _High betweenness centrality (0.378) - this node is a cross-community bridge._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.0896551724137931 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `Clans`, `kit_academy.py`, `kit_shinobi.py`, `fabric`, `Box`, `cel_box`, `flaps`, `ring_shell`, `kit_shinobi.py`, `solid`, `kit_hagane.py`, `strip_fabric`, `kit_field.py`, `k`, `bangs`, `belt`?**
  _High betweenness centrality (0.377) - this node is a cross-community bridge._