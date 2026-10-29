# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 112 files · ~157,855 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2309 nodes · 5080 edges · 148 communities (101 shown, 47 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 473 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9bbd0f6d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- stamp
- kit_uchiha.py
- Clans
- kit_senju.py
- preview.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- kit_inuzuka.py
- kit_yuhi.py
- kit_kunoichi.py
- kit_aburame.py
- kit_shinobi.py
- kit_suzuran.py
- 7. Systems in the beta
- Plan
- solid
- cel_box
- kit_rugged.py
- kit_household.py
- kit_tobari.py
- Garment
- mesh_shirt
- kit_shimura.py
- sleeve_roll
- k
- kit_market.py
- kit_kinoshita.py
- strip_fabric
- 5. Data formats built for the whole story
- kit_field.py
- outputs
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
- kit_namiashi.py
- Run
- load_clans
- Tex
- rot_matrix
- build
- Box
- chain
- Face
- ring_shell
- kit_gekko.py
- Act
- Stage
- .bond
- kit_hagane.py
- Conflict
- bandolier
- list
- org.junit.jupiter.api.Test
- blocks.py
- Personality
- Custom blocks
- kit_tsuchigumo.py
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
- .romance
- box
- .test
- Meters
- Value
- Mood
- masks.py
- 4.3 The noble clans
- kit_haruno.py
- .page
- Peeve
- ClanRelations
- Shared helpers
- kit_umino.py
- Person
- Meter
- Title
- Every building
- 18. Village scale
- utility_pole
- Side quests
- 4.4 The minor clans
- fabric
- 2. Quest framework
- ROADMAP.md
- Conflict
- Source
- stone_lantern
- Gossip
- kit_nara.py
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- kit_hyuga.py
- The village
- paint.py
- 4. Clan quest lines
- kit_specialist.py
- json
- shade
- Side quest secrets
- k
- shag_face
- obi
- rope_face
- hood_down
- sash
- turned_hem
- shin_wraps
- gourd
- lames
- snack_pouch
- shoku_disc
- sode
- blouse
- holster
- knee_guards
- face_mask
- wave_band
- hakama_legs
- kit_sarutobi.py
- coat_skirts
- bandolier
- cane
- cross_armband
- scroll_tube
- lantern_tag
- muffler
- sash

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `solid()` - 151 edges
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
- `15. Pacing` --references--> `TimeAndPacingTest`  [INFERRED]
  BONDS.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `Interior fittings` --references--> `tatami()`  [INFERRED]
  KONOHA_BUILD.md → tools/konoha/blocks.py
- `Shared helpers` --references--> `wraps()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit_shinobi.py
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py

## Import Cycles
- None detected.

## Communities (148 total, 47 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.11
Nodes (10): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), decal(), dolphin(), wave_band() (+2 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "preview.py"
Cohesion: 0.06
Nodes (40): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), light_for(), model() (+32 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.12
Nodes (8): back_crest(), drawstrings(), holster(), ribbed(), side_stripe(), stripes(), waist_pouch(), zip_pull()

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (12): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+4 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.07
Nodes (19): splatter(), wisteria_hem(), camo(), ragged(), ink_stains(), seal_trim(), bandage_turns(), mist_swirls() (+11 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_shinobi.py"
Cohesion: 0.20
Nodes (5): forehead_protector(), protector_plate(), sandals(), wraps(), backward_bandana()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "Plan"
Cohesion: 0.05
Nodes (21): 5. Process, 9. Open questions, Order of work, The pieces, What needs you at your PC, build(), build(), build() (+13 more)

### Community 17 - "solid"
Cohesion: 0.12
Nodes (9): strap(), mandarin_collar(), white_fang_tanto(), head_cloth(), arm_protector(), side_panels(), scroll(), strap() (+1 more)

### Community 18 - "cel_box"
Cohesion: 0.18
Nodes (8): cel_box(), tie(), ear_panels(), gathered_tail(), hair_tie(), pineapple(), beard(), knot()

### Community 19 - "kit_rugged.py"
Cohesion: 0.08
Nodes (11): baggy_legs(), cape(), dread(), knot_bun(), leg_wraps(), patch(), rope_hair(), shin_guard() (+3 more)

### Community 20 - "kit_household.py"
Cohesion: 0.05
Nodes (25): arm_cloth(), bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta() (+17 more)

### Community 21 - "kit_tobari.py"
Cohesion: 0.18
Nodes (7): shirt(), flak_vest(), hood_down(), mantle(), plain_body(), pleats(), cap()

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 24 - "kit_shimura.py"
Cohesion: 0.22
Nodes (4): forearm_wraps(), back_crest(), bandaged_arm(), bandage()

### Community 26 - "k"
Cohesion: 0.13
Nodes (9): body(), collar(), footwear(), leg_bone(), leg_ring(), legs(), pouch(), sleeves() (+1 more)

### Community 27 - "kit_market.py"
Cohesion: 0.04
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+14 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "strip_fabric"
Cohesion: 0.17
Nodes (6): kimono_sleeves(), gloves(), anbu_arms(), anbu_plates(), split_toe_boots(), strip_fabric()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.11
Nodes (8): arm_guards(), cargo(), gloves(), half_sleeves(), pocket(), shirt(), trousers(), vest()

### Community 32 - "outputs"
Cohesion: 0.18
Nodes (13): hex_rgb(), json_text(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes(), outputs(), png_bytes() (+5 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "kit_shiranui.py"
Cohesion: 0.18
Nodes (6): crest(), flicks(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.09
Nodes (13): arm_bone(), arm_x(), armband(), roll(), bun(), clip(), crest_patch(), hairpin() (+5 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 43 - "kit_namiashi.py"
Cohesion: 0.20
Nodes (5): back_blade(), crest(), hip_kokuto(), kokuto(), wave_lock()

### Community 44 - "Run"
Cohesion: 0.07
Nodes (19): 5. Personality, BondEvent, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS (+11 more)

### Community 45 - "load_clans"
Cohesion: 0.18
Nodes (9): catalog(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_groups(), load_population(), population_weights() (+1 more)

### Community 46 - "Tex"
Cohesion: 0.13
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 47 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (6): build(), build_all(), load_module(), main(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.11
Nodes (4): puff(), curls_box(), Box, Layer

### Community 51 - "Face"
Cohesion: 0.19
Nodes (6): button(), curls_face(), darken_rows(), grid(), rivets(), Face

### Community 52 - "ring_shell"
Cohesion: 0.13
Nodes (8): cel_face(), ring_shell(), crown(), clipped(), combed_back(), nape_hem(), pulled_back(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.22
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 55 - "Stage"
Cohesion: 0.09
Nodes (15): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+7 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 58 - "Conflict"
Cohesion: 0.11
Nodes (9): 11. Kindling Bond, Grant, Kindling, Tier, FULL, NATURE, NONE, TECHNIQUE (+1 more)

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.11
Nodes (6): BondDialogueTest, ConditionsAndEffectsTest, GossipTest, KindlingAndBookTest, SquadTest, VillageTest

### Community 62 - "blocks.py"
Cohesion: 0.18
Nodes (9): auto_uv(), check(), compile_all(), facing_states(), main(), ref(), shoji(), shoji_paper() (+1 more)

### Community 63 - "Personality"
Cohesion: 0.14
Nodes (4): 20. What the roadmap asks of bonds, Personality, Reaction, ReactionTest

### Community 64 - "Custom blocks"
Cohesion: 0.12
Nodes (16): 4. Block catalogue, Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Festival, Furniture (the Leaf set) (+8 more)

### Community 65 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 66 - "Village"
Cohesion: 0.16
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 67 - "VillageScaleTest"
Cohesion: 0.16
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.12
Nodes (3): ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.12
Nodes (13): 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+5 more)

### Community 71 - ".read"
Cohesion: 0.23
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (14): Def, Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR (+6 more)

### Community 73 - "Levels"
Cohesion: 0.09
Nodes (9): 3. Levels and story gates, State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, Levels (+1 more)

### Community 75 - "Squad"
Cohesion: 0.09
Nodes (3): BondEffects, Departure, Squad

### Community 77 - "box"
Cohesion: 0.21
Nodes (10): Facades and shop fronts, Roofs, awning(), block(), Block, box(), kawara_ridge(), noren() (+2 more)

### Community 78 - ".test"
Cohesion: 0.13
Nodes (3): 12. The bond book, BondConditions, BondWeb

### Community 80 - "Value"
Cohesion: 0.13
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - "Mood"
Cohesion: 0.13
Nodes (9): 18. Village scale, Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY (+1 more)

### Community 82 - "masks.py"
Cohesion: 0.18
Nodes (6): How the pieces work, belt(), mesh(), tanto(), beak(), ears()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.16
Nodes (6): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim()

### Community 85 - ".page"
Cohesion: 0.27
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Peeve"
Cohesion: 0.15
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 87 - "ClanRelations"
Cohesion: 0.13
Nodes (9): Base, ClanRelations, Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL (+1 more)

### Community 88 - "Shared helpers"
Cohesion: 0.18
Nodes (8): Shared helpers, back_fan(), bangs(), braid(), lock(), sidelocks(), spike(), brush_tail()

### Community 89 - "kit_umino.py"
Cohesion: 0.20
Nodes (4): combed_up(), falling_tail(), surf(), waves()

### Community 91 - "Meter"
Cohesion: 0.10
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.12
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Every building"
Cohesion: 0.14
Nodes (14): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+6 more)

### Community 95 - "utility_pole"
Cohesion: 0.18
Nodes (11): 1. The answer: how much it will be, 6. Prototypes, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan, Sessions (+3 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook, as these templates expect it, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "fabric"
Cohesion: 0.17
Nodes (6): leg_cloth(), waist(), tabi_boots(), heavy_boots(), lantern(), fabric()

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "ROADMAP.md"
Cohesion: 0.29
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 102 - "Source"
Cohesion: 0.22
Nodes (6): Know, Source, HEARD, SEEN, SELF, TOLD

### Community 103 - "stone_lantern"
Cohesion: 0.22
Nodes (7): 2. Style guide: the Konoha kit, By building type, Lanterns, Shared palette, Shrine, stone_lantern(), shimenawa()

### Community 105 - "kit_nara.py"
Cohesion: 0.33
Nodes (3): back_crest(), crest(), tuft()

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "kit_hyuga.py"
Cohesion: 0.17
Nodes (5): curtain(), back_sheet(), blunt_fringe(), hime_locks(), parted_fringe()

### Community 109 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 110 - "paint.py"
Cohesion: 0.12
Nodes (10): band(), cloth_shade(), dark_seams(), hair_box(), hair_face(), hair_shade(), hem(), shell() (+2 more)

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 115 - "shade"
Cohesion: 0.50
Nodes (3): tatami(), tatami_top(), shade()

### Community 117 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 118 - "k"
Cohesion: 0.07
Nodes (15): quilt(), collar(), tape(), flaps(), sword_strap(), sash(), tabi(), wrap_front() (+7 more)

### Community 137 - "kit_sarutobi.py"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

## Knowledge Gaps
- **153 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+148 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 984 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **47 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bonds` connect `Bonds` to `ROADMAP.md`, `Conflict`, `Person`, `.read`, `Levels`, `Deed`, `Run`, `.romance`, `.test`, `Meters`, `Value`, `Mood`, `ClanRelations`, `Stage`, `Conflict`, `Personality`?**
  _High betweenness centrality (0.458) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _153 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `stamp` be split into smaller, more focused modules?**
  _Cohesion score 0.11255411255411256 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `Shared helpers`, `ROADMAP.md`?**
  _High betweenness centrality (0.368) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `Clans`, `fabric`, `kit_hyuga.py`, `kit_shinobi.py`, `paint.py`, `cel_box`, `masks.py`, `ring_shell`, `kit_tobari.py`, `k`, `kit_shimura.py`, `k`, `strip_fabric`?**
  _High betweenness centrality (0.306) - this node is a cross-community bridge._