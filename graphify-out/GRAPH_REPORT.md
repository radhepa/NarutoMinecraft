# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 112 files · ~160,364 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2311 nodes · 5083 edges · 102 communities (85 shown, 17 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 474 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `347217e1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- stamp
- kit_uchiha.py
- Clans
- cel_box
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- kit_inuzuka.py
- kit_yuhi.py
- kit_kunoichi.py
- preview.py
- BondWorld
- kit_suzuran.py
- 7. Systems in the beta
- Plan
- solid
- kit_nara.py
- kit_rugged.py
- fabric
- kit_tobari.py
- Garment
- kit_tsuchigumo.py
- kit_haruno.py
- noren
- k
- kit_market.py
- kit_kinoshita.py
- Value
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- Conflict
- 4. Technical architecture
- 6. The map
- utility_pole
- 8. The beta, chapter by chapter
- 9. Delivery plan
- Label
- kit_akimichi.py
- 4. Clan quest lines
- Run
- load_clans
- Tex
- rot_matrix
- build
- Box
- Face
- paint.py
- Act
- Person
- .bond
- kit_hagane.py
- .page
- list
- org.junit.jupiter.api.Test
- blocks.py
- Personality
- Custom blocks
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
- catalogue.py
- .test
- Meters
- Mood
- masks.py
- 4.3 The noble clans
- Peeve
- ClanRelations
- anime.py
- .born
- Meter
- Title
- Every building
- 18. Village scale
- utility_pole
- Side quests
- 4.4 The minor clans
- 2. Quest framework
- Conflict
- Source
- Stage
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- kit_hyuga.py
- render_kit.py
- kit_uzumaki.py

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
- `Interior fittings` --references--> `tatami()`  [INFERRED]
  KONOHA_BUILD.md → tools/konoha/blocks.py
- `The pieces` --references--> `Plan`  [INFERRED]
  KONOHA_BUILD.md → tools/konoha/kit.py
- `Shared helpers` --references--> `wraps()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit_shinobi.py
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py

## Import Cycles
- None detected.

## Communities (102 total, 17 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.03
Nodes (35): stamp(), crescent(), hip_katana(), katana(), sword_strap(), decal(), shoulder_decal(), slanted_protector() (+27 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.13
Nodes (8): arm_crest(), arm_warmers(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "cel_box"
Cohesion: 0.10
Nodes (10): cel_box(), flick(), topknot(), round_bun(), wave_lock(), bun(), nape_hem(), bun() (+2 more)

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (20): new_canvas(), save_canvas(), backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads() (+12 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.07
Nodes (14): back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps() (+6 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (32): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+24 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.10
Nodes (10): back_crest(), bead_clip(), brush_stroke(), ink_clouds(), part_line(), splatter(), stamp(), wave_lock() (+2 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.11
Nodes (8): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), shin_wrap(), thigh_holster(), wrap_front()

### Community 12 - "preview.py"
Cohesion: 0.18
Nodes (12): axis_rot(), block_quads(), blockstate(), custom_variant(), face_corners(), is_full(), model(), model_quads() (+4 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "Plan"
Cohesion: 0.07
Nodes (8): 9. Open questions, build(), build(), build(), base_name(), mc(), Plan, solid()

### Community 17 - "solid"
Cohesion: 0.04
Nodes (30): deep_hood(), high_collar(), hood_down(), lenses(), mandarin_collar(), face_mask(), white_fang_tanto(), sash() (+22 more)

### Community 18 - "kit_nara.py"
Cohesion: 0.18
Nodes (6): back_crest(), crest(), mesh_shirt(), net(), pineapple(), tuft()

### Community 19 - "kit_rugged.py"
Cohesion: 0.08
Nodes (12): camo(), cape(), dread(), knot_bun(), leg_wraps(), ragged(), rope(), rope_face() (+4 more)

### Community 20 - "fabric"
Cohesion: 0.04
Nodes (37): leg_cloth(), shirt(), waist(), body(), half_sleeves(), shirt(), trousers(), arm_cloth() (+29 more)

### Community 21 - "kit_tobari.py"
Cohesion: 0.09
Nodes (13): anbu_plates(), decal(), hood_down(), lantern(), lantern_tag(), mantle(), muffler(), plain_body() (+5 more)

### Community 22 - "Garment"
Cohesion: 0.31
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 24 - "kit_haruno.py"
Cohesion: 0.16
Nodes (6): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim()

### Community 25 - "noren"
Cohesion: 0.19
Nodes (10): 6. Prototypes, Facades and shop fronts, Lanterns, Roofs, awning(), block(), facing_states(), kawara_ridge() (+2 more)

### Community 26 - "k"
Cohesion: 0.05
Nodes (33): Shared helpers, arm_bone(), arm_x(), belt(), collar(), flaps(), footwear(), blossom() (+25 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (20): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kyahan() (+12 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Value"
Cohesion: 0.15
Nodes (11): Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY, KINDNESS (+3 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.07
Nodes (13): arm_guards(), blouse(), cargo(), chain(), collar(), gloves(), holster(), knee_guards() (+5 more)

### Community 32 - "outputs"
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

### Community 38 - "utility_pole"
Cohesion: 0.22
Nodes (7): 2. Style guide: the Konoha kit, By building type, Shared palette, Shrine, Streets, utility_pole(), shimenawa()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Label"
Cohesion: 0.22
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 42 - "kit_akimichi.py"
Cohesion: 0.12
Nodes (8): gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode(), curls_box()

### Community 43 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 44 - "Run"
Cohesion: 0.07
Nodes (20): 15. Pacing, 5. Personality, BondEvent, Rng, Seeds, Chapter, Phase, ACADEMY (+12 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 46 - "Tex"
Cohesion: 0.14
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 47 - "rot_matrix"
Cohesion: 0.18
Nodes (5): wave_lock(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.10
Nodes (5): band(), hem(), strip_line(), Box, Layer

### Community 51 - "Face"
Cohesion: 0.14
Nodes (9): mark(), button(), curls_face(), dark_seams(), darken_rows(), grid(), rivets(), Face (+1 more)

### Community 52 - "paint.py"
Cohesion: 0.08
Nodes (18): cel_face(), ring_shell(), sprigs(), crown(), kasuri(), clipped(), combed_back(), pulled_back() (+10 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.19
Nodes (5): bracers(), harness(), mace(), plate(), shin_guards()

### Community 58 - ".page"
Cohesion: 0.20
Nodes (5): 12. The bond book, BondBook, Fact, MemoryLine, Page

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.12
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, SquadTest

### Community 62 - "blocks.py"
Cohesion: 0.15
Nodes (15): auto_uv(), Block, box(), check(), compile_all(), main(), ref(), shoji() (+7 more)

### Community 63 - "Personality"
Cohesion: 0.17
Nodes (3): Personality, Reaction, ReactionTest

### Community 64 - "Custom blocks"
Cohesion: 0.15
Nodes (13): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival, Furniture (the Leaf set) (+5 more)

### Community 66 - "Village"
Cohesion: 0.21
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 67 - "VillageScaleTest"
Cohesion: 0.12
Nodes (5): 20. What the roadmap asks of bonds, ClanProfile, Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.11
Nodes (5): ConflictTest, GossipTest, Leaf, MemoryTest, VillageTest

### Community 70 - "Bonds"
Cohesion: 0.12
Nodes (13): 11. Kindling Bond, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+5 more)

### Community 71 - ".read"
Cohesion: 0.23
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.08
Nodes (14): Def, Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR (+6 more)

### Community 73 - "Levels"
Cohesion: 0.05
Nodes (21): 3. Levels and story gates, State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, Tier (+13 more)

### Community 74 - "Deed"
Cohesion: 0.15
Nodes (3): 8. The village talks, Deed, Gossip

### Community 77 - "catalogue.py"
Cohesion: 0.19
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 82 - "masks.py"
Cohesion: 0.15
Nodes (8): How the pieces work, mesh(), tanto(), beak(), bump(), ears(), plate(), strap()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 86 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 89 - "anime.py"
Cohesion: 0.07
Nodes (16): back_fan(), braid(), lock(), sidelocks(), spike(), crown(), hime_locks(), side_fringe() (+8 more)

### Community 91 - "Meter"
Cohesion: 0.10
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.17
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Every building"
Cohesion: 0.12
Nodes (16): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+8 more)

### Community 94 - "18. Village scale"
Cohesion: 0.14
Nodes (3): 18. Village scale, House, Village

### Community 95 - "utility_pole"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook, as these templates expect it, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 102 - "Source"
Cohesion: 0.22
Nodes (6): Know, Source, HEARD, SEEN, SELF, TOLD

### Community 103 - "Stage"
Cohesion: 0.09
Nodes (15): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+7 more)

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "kit_hyuga.py"
Cohesion: 0.10
Nodes (11): bangs(), curtain(), tie(), back_sheet(), blunt_fringe(), ear_panels(), gathered_tail(), hair_tie() (+3 more)

### Community 114 - "render_kit.py"
Cohesion: 0.12
Nodes (10): light_for(), Scene, blocks_sheet(), building_sheet(), full_state(), load_blueprint(), main(), street() (+2 more)

### Community 118 - "kit_uzumaki.py"
Cohesion: 0.18
Nodes (5): bun(), crest_patch(), seal_script(), seal_tags(), waves()

## Knowledge Gaps
- **153 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+148 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 986 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bonds` connect `Bonds` to `Conflict`, `VillageScaleTest`, `Stage`, `.read`, `Story bible`, `Levels`, `Deed`, `Run`, `.romance`, `Meters`, `Mood`, `Person`, `ClanRelations`, `.page`, `18. Village scale`, `Personality`?**
  _High betweenness centrality (0.460) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _153 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `stamp` be split into smaller, more focused modules?**
  _Cohesion score 0.0340258958145137 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `k`, `Story bible`?**
  _High betweenness centrality (0.367) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `k` to `stamp`, `Clans`, `cel_box`, `kit_hyuga.py`, `Box`, `masks.py`, `paint.py`, `fabric`, `anime.py`?**
  _High betweenness centrality (0.305) - this node is a cross-community bridge._