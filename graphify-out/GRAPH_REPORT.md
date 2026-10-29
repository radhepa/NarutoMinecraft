# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 136 files · ~177,078 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2490 nodes · 5840 edges · 138 communities (99 shown, 39 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 597 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `84355dee`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- stamp
- mkit.py
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- kit_inuzuka.py
- kit_yuhi.py
- .all
- Economy
- Catalogue
- kit_suzuran.py
- 7. Systems in the beta
- kit_umino.py
- masks.py
- cel_box
- kit_rugged.py
- kit_household.py
- strip_fabric
- Garment
- .num
- Desk
- arm_bone
- fabric
- kit_market.py
- kit_kinoshita.py
- Missions
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- missions.py
- 4. Technical architecture
- 6. The map
- kit_uzumaki.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- .get
- k
- Player
- Playthrough
- kit_hyuga.py
- .strings
- kit_shinobi.py
- Rng
- Box
- Seeds
- Face
- scalp
- Json
- Act
- Stage
- BondWorld
- kit_nara.py
- Person
- VarietyGuard
- list
- .classic
- solid
- Personality
- assertions
- kit_uchiha.py
- Village
- VillageScaleTest
- Bond
- .of
- Bonds
- .read
- Def
- Levels
- Deed
- Squad
- kit_hagane.py
- Tier
- .test
- Meters
- Value
- .name
- org.junit.jupiter.api.Test
- 4.3 The noble clans
- S
- Person
- Peeve
- kit_morino.py
- TimeAndPacingTest
- kit_specialist.py
- rnd
- Meter
- End
- mission
- kit_akimichi.py
- kit_aburame.py
- Side quests
- 4.4 The minor clans
- GossipTest
- 2. Quest framework
- CourtshipTest
- kit_hatake.py
- kit_yamanaka.py
- kit_gekko.py
- kit_shiranui.py
- glyphs.py
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- build
- flaps
- 4. Clan quest lines
- jika_tabi
- .title
- kokuto
- paint.py
- mesh_shirt
- rope_hair
- shag_face
- rope_face
- wrap_front
- shade
- sword_strap
- arm_cloth
- blossom
- sash
- arm_warmers
- shin_wrap
- wrap_front
- coat_skirts
- bell_charm
- gloves
- lamellar
- bun
- waves

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `solid()` - 152 edges
3. `BondWorld` - 129 edges
4. `fabric()` - 109 edges
5. `Act` - 101 edges
6. `Village` - 62 edges
7. `strip_fabric()` - 59 edges
8. `stamp()` - 47 edges
9. `Bond` - 44 edges
10. `rnd()` - 43 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `7.3 Classic and Varied` --references--> `DeskTest`  [INFERRED]
  MISSIONS.md → progression/missions/src/test/java/dev/shinobi/progression/mission/DeskTest.java
- `3.2 Templates` --references--> `escort()`  [INFERRED]
  SIDE_QUESTS.md → tools/missions/mkit.py
- `Player clans` --references--> `S`  [INFERRED]
  ROADMAP.md → tools/missions/mkit.py
- `2.1 Kinds` --references--> `mission()`  [INFERRED]
  SIDE_QUESTS.md → tools/missions/mkit.py

## Import Cycles
- None detected.

## Communities (138 total, 39 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.13
Nodes (10): stamp(), crest(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), dolphin() (+2 more)

### Community 1 - "mkit.py"
Cohesion: 0.18
Nodes (30): 4.1 The format, The quest format, anchor(), buy(), choose(), chose(), collect(), count() (+22 more)

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
Nodes (13): back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps() (+5 more)

### Community 7 - "Story bible"
Cohesion: 0.05
Nodes (39): Commits, graphify, Naruto Minecraft, A rank, ANBU operations, B rank, C rank, D rank (+31 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.06
Nodes (20): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar(), bandage_turns() (+12 more)

### Community 12 - "Economy"
Cohesion: 0.09
Nodes (12): Band, Economy, GradeRow, Performance, Result, Grade, A, B (+4 more)

### Community 13 - "Catalogue"
Cohesion: 0.11
Nodes (10): Catalogue, Mode, CLASSIC, VARIED, Branch, Step, Template, Twist (+2 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.16
Nodes (6): back_crest(), bell_hem(), bell_print(), bell_sprig(), sash_vials(), vial()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "kit_umino.py"
Cohesion: 0.17
Nodes (5): falling_tail(), knot(), scroll(), surf(), waves()

### Community 17 - "masks.py"
Cohesion: 0.13
Nodes (9): How the pieces work, belt(), mesh(), tanto(), beak(), bump(), ears(), plate() (+1 more)

### Community 18 - "cel_box"
Cohesion: 0.12
Nodes (13): Shared helpers, back_fan(), bangs(), braid(), cel_box(), curtain(), lock(), sidelocks() (+5 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.08
Nodes (11): baggy_legs(), camo(), cape(), knot_bun(), leg_wraps(), patch(), ragged(), shin_guard() (+3 more)

### Community 20 - "kit_household.py"
Cohesion: 0.08
Nodes (14): bands(), checks(), cloth_shoes(), collar_band(), dots(), ichimatsu(), kasuri(), overlap() (+6 more)

### Community 21 - "strip_fabric"
Cohesion: 0.08
Nodes (15): vest(), pouch(), anbu_plates(), decal(), hood_down(), lantern(), lantern_tag(), mantle() (+7 more)

### Community 22 - "Garment"
Cohesion: 0.20
Nodes (4): compatible(), Garment, key_rgba(), png_bytes()

### Community 24 - "Desk"
Cohesion: 0.14
Nodes (9): Desk, Offer, Rank, A, B, C, D, S (+1 more)

### Community 25 - "arm_bone"
Cohesion: 0.13
Nodes (11): sleeve_roll(), sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), tasuki(), armband() (+3 more)

### Community 26 - "fabric"
Cohesion: 0.09
Nodes (19): leg_cloth(), shirt(), waist(), body(), collar(), half_sleeves(), shirt(), trousers() (+11 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (21): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+13 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Missions"
Cohesion: 0.08
Nodes (26): 10. What other parts of the pack provide, 11. What waits for Phase 0, 12. Open questions, 1. At a glance, 2.1 How missions are offered, 2.2 Accepting and the briefing, 2.3 Travel, 2.4 Reporting back (+18 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.12
Nodes (14): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+6 more)

### Community 31 - "kit_field.py"
Cohesion: 0.09
Nodes (13): blouse(), cargo(), collar(), gloves(), holster(), knee_guards(), pocket(), strap() (+5 more)

### Community 32 - "outputs"
Cohesion: 0.12
Nodes (22): catalog(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_eye_colors() (+14 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "missions.py"
Cohesion: 0.16
Nodes (14): catalogue_doc(), check(), check_tables(), compiled(), derive_places(), dump(), file_for(), main() (+6 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.25
Nodes (8): 4. Technical architecture, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods, Versions

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.16
Nodes (6): clip(), hairpin(), seal_script(), seal_tags(), wide_sleeves(), wrap_tie()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 42 - "k"
Cohesion: 0.07
Nodes (15): face_mask(), geta(), socks(), obi(), tabi(), wave_band(), neckline(), pauldron() (+7 more)

### Community 44 - "Playthrough"
Cohesion: 0.11
Nodes (14): BondEvent, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+6 more)

### Community 45 - "kit_hyuga.py"
Cohesion: 0.13
Nodes (8): tie(), back_sheet(), blunt_fringe(), ear_panels(), gathered_tail(), hair_tie(), hime_locks(), parted_fringe()

### Community 46 - ".strings"
Cohesion: 0.32
Nodes (3): Band, Mate, SquadPlan

### Community 47 - "kit_shinobi.py"
Cohesion: 0.13
Nodes (7): back_crest(), bandaged_arm(), cane(), bandage(), flak_vest(), sandals(), wraps()

### Community 49 - "Box"
Cohesion: 0.08
Nodes (8): band(), hem(), strip_line(), Box, Layer, Piece, piece_corners(), world_bounds()

### Community 51 - "Face"
Cohesion: 0.09
Nodes (13): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+5 more)

### Community 52 - "scalp"
Cohesion: 0.21
Nodes (6): ring_shell(), crown(), combed_back(), pulled_back(), combed_up(), scalp()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 55 - "Stage"
Cohesion: 0.15
Nodes (9): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+1 more)

### Community 57 - "kit_nara.py"
Cohesion: 0.13
Nodes (8): spike(), crown(), burst(), back_crest(), crest(), pineapple(), tuft(), brush_tail()

### Community 58 - "Person"
Cohesion: 0.12
Nodes (4): 20. What the roadmap asks of bonds, BondDialogue, Household, Recruitment

### Community 59 - "VarietyGuard"
Cohesion: 0.11
Nodes (6): 9. The generator, Resident, SlotFiller, VarietyGuard, World, SampleVillage

### Community 60 - "list"
Cohesion: 0.07
Nodes (3): 11. Kindling Bond, Grant, Kindling

### Community 61 - ".classic"
Cohesion: 0.17
Nodes (3): ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 62 - "solid"
Cohesion: 0.19
Nodes (6): frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), thigh_holster(), solid()

### Community 63 - "Personality"
Cohesion: 0.15
Nodes (3): Personality, Reaction, ReactionTest

### Community 64 - "assertions"
Cohesion: 0.13
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 65 - "kit_uchiha.py"
Cohesion: 0.19
Nodes (6): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), police_badge()

### Community 66 - "Village"
Cohesion: 0.05
Nodes (12): 18. Village scale, 19. Society hooks, Base, ClanRelations, SocialTie, SocietyHook, House, Tier (+4 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.15
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.13
Nodes (3): ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.10
Nodes (13): 13. Data formats, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 4. Memories, 5. Personality (+5 more)

### Community 71 - ".read"
Cohesion: 0.25
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (14): Def, Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR (+6 more)

### Community 73 - "Levels"
Cohesion: 0.14
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.09
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 75 - "Squad"
Cohesion: 0.08
Nodes (3): BondEffects, Departure, Squad

### Community 76 - "kit_hagane.py"
Cohesion: 0.21
Nodes (5): bracers(), harness(), mace(), plate(), shin_guards()

### Community 77 - "Tier"
Cohesion: 0.22
Nodes (5): Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 79 - "Meters"
Cohesion: 0.13
Nodes (7): Memory, Meters, Source, HEARD, SEEN, SELF, TOLD

### Community 80 - "Value"
Cohesion: 0.13
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - ".name"
Cohesion: 0.04
Nodes (28): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS, State (+20 more)

### Community 82 - "org.junit.jupiter.api.Test"
Cohesion: 0.16
Nodes (4): BondDialogueTest, SquadTest, SeedsTest, SimulationTest

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "S"
Cohesion: 0.25
Nodes (4): 6. Squad missions, travel(), S, twist()

### Community 85 - "Person"
Cohesion: 0.09
Nodes (7): 12. The bond book, BondBook, Fact, MemoryLine, Page, BondWeb, Person

### Community 86 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 87 - "kit_morino.py"
Cohesion: 0.18
Nodes (5): back_crest(), gloves(), head_cloth(), heavy_boots(), forehead_protector()

### Community 89 - "kit_specialist.py"
Cohesion: 0.18
Nodes (5): bandolier(), coat_skirts(), cross_armband(), scroll_tube(), strap()

### Community 90 - "rnd"
Cohesion: 0.14
Nodes (9): cel_face(), clipped(), ink_stains(), seal_trim(), hair_box(), hair_face(), hair_shade(), rnd() (+1 more)

### Community 91 - "Meter"
Cohesion: 0.10
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "End"
Cohesion: 0.40
Nodes (5): End, ABANDONED, DONE, FAILED, PARTIAL

### Community 93 - "mission"
Cohesion: 0.33
Nodes (4): Code by mod, _key(), mission(), outcome()

### Community 94 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box() (+1 more)

### Community 95 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 101 - "kit_hatake.py"
Cohesion: 0.20
Nodes (4): decal(), shoulder_decal(), slanted_protector(), white_fang_tanto()

### Community 102 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 103 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 104 - "kit_shiranui.py"
Cohesion: 0.12
Nodes (9): arm_protector(), protector_plate(), backward_bandana(), crest(), flicks(), mouth_senbon(), senbon(), thigh_holster() (+1 more)

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 110 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 115 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

## Knowledge Gaps
- **168 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+163 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 958 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **39 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `shin_wrap`, `wrap_front`, `coat_skirts`, `stamp`, `kit_senju.py`, `bell_charm`, `kit_academy.py`, `gloves`, `kit_kurama.py`, `kit_inuzuka.py`, `kit_yuhi.py`, `lamellar`, `bun`, `waves`, `kit_suzuran.py`, `kit_umino.py`, `masks.py`, `cel_box`, `kit_rugged.py`, `kit_household.py`, `strip_fabric`, `arm_bone`, `fabric`, `kit_market.py`, `kit_kinoshita.py`, `kit_field.py`, `kit_uzumaki.py`, `kit_hyuga.py`, `kit_shinobi.py`, `Box`, `Face`, `scalp`, `kit_nara.py`, `solid`, `kit_uchiha.py`, `kit_hagane.py`, `kit_morino.py`, `kit_specialist.py`, `rnd`, `kit_akimichi.py`, `kit_aburame.py`, `kit_hatake.py`, `kit_yamanaka.py`, `kit_gekko.py`, `kit_shiranui.py`, `glyphs.py`, `flaps`, `jika_tabi`, `paint.py`, `rope_hair`, `shag_face`, `rope_face`, `wrap_front`, `sword_strap`, `blossom`, `sash`, `arm_warmers`?**
  _High betweenness centrality (0.116) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _168 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `stamp` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Village`, `CourtshipTest`, `.read`, `Story bible`, `Levels`, `Deed`, `Playthrough`, `Meters`, `Value`, `.name`, `Person`, `TimeAndPacingTest`, `Person`, `list`, `Personality`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._