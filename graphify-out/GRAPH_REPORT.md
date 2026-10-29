# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 112 files · ~161,190 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2312 nodes · 5084 edges · 135 communities (101 shown, 34 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 474 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d6452123`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_shiranui.py
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
- fabric
- k
- kit_suzuran.py
- 7. Systems in the beta
- Plan
- solid
- kit_nara.py
- kit_rugged.py
- kit_household.py
- kit_tobari.py
- Garment
- kit_tsuchigumo.py
- kit_haruno.py
- Levels
- wardrobe/kit.py
- kit_market.py
- kit_kinoshita.py
- Value
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- stamp
- 4. Technical architecture
- 6. The map
- paint.py
- 8. The beta, chapter by chapter
- 9. Delivery plan
- Playthrough.java
- kit_akimichi.py
- 4. Clan quest lines
- Run
- load_clans
- Tex
- rot_matrix
- build
- Box
- Face
- scalp
- pathlib
- Act
- CourtshipTest
- .bond
- kit_hagane.py
- .page
- kit_shinobi.py
- .classic
- blocks.py
- Personality
- Custom blocks
- kit_specialist.py
- Tier
- VillageScaleTest
- org.junit.jupiter.api.Test
- .of
- Bonds
- .read
- Def
- .name
- Deed
- cel_box
- VillageSim.java
- catalogue.py
- .test
- Meters
- kit_aburame.py
- kit_namiashi.py
- masks.py
- 4.3 The noble clans
- kit_umino.py
- kit_yamanaka.py
- Peeve
- GossipTest
- wide_sleeves
- Shared helpers
- .born
- Meter
- .invited
- Every building
- Village
- chain
- Side quests
- 4.4 The minor clans
- kit_gekko.py
- 2. Quest framework
- kit_hatake.py
- Memory
- Person
- Stage
- glyphs.py
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- kit_hyuga.py
- masks.py
- curtain
- rope_hair
- json
- shag_face
- rope_face
- kit_uzumaki.py
- tape
- strap
- sword_strap
- face_mask
- cloth_shoes
- hakama_legs
- tabi
- kyahan
- tabi
- pauldron
- scarf
- bandolier
- clip
- waves

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
- `The pieces` --references--> `Plan`  [INFERRED]
  KONOHA_BUILD.md → tools/konoha/kit.py
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py

## Import Cycles
- None detected.

## Communities (135 total, 34 thin omitted)

### Community 0 - "kit_shiranui.py"
Cohesion: 0.14
Nodes (8): protector_plate(), backward_bandana(), crest(), flicks(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

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
Cohesion: 0.06
Nodes (16): back_crest(), drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps() (+8 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (32): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+24 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.07
Nodes (18): kasuri(), camo(), ragged(), ink_stains(), seal_trim(), bandage_turns(), mist_swirls(), rose() (+10 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.09
Nodes (10): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), thigh_holster() (+2 more)

### Community 12 - "fabric"
Cohesion: 0.09
Nodes (18): leg_cloth(), waist(), body(), footwear(), arm_cloth(), trouser_legs(), waist(), wide_sleeves() (+10 more)

### Community 13 - "k"
Cohesion: 0.08
Nodes (14): blouse(), collar(), knee_guards(), mandarin_collar(), sash(), wrap_front(), back_crest(), wave_band() (+6 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.09
Nodes (11): apothecary_sash(), armband(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves() (+3 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "Plan"
Cohesion: 0.12
Nodes (5): 9. Open questions, base_name(), mc(), Plan, solid()

### Community 17 - "solid"
Cohesion: 0.09
Nodes (11): holster(), white_fang_tanto(), obi(), coat_skirts(), arm_protector(), cane(), muffler(), sash() (+3 more)

### Community 18 - "kit_nara.py"
Cohesion: 0.15
Nodes (7): spike(), burst(), back_crest(), crest(), pineapple(), tuft(), brush_tail()

### Community 19 - "kit_rugged.py"
Cohesion: 0.10
Nodes (9): baggy_legs(), cape(), knot_bun(), leg_wraps(), patch(), shin_guard(), soft_boots(), straw_sandals() (+1 more)

### Community 20 - "kit_household.py"
Cohesion: 0.05
Nodes (20): bands(), blossom(), checks(), collar_band(), dots(), geta(), ichimatsu(), jika_tabi() (+12 more)

### Community 21 - "kit_tobari.py"
Cohesion: 0.13
Nodes (9): shirt(), shirt(), hood_down(), lantern(), mantle(), plain_body(), pleats(), split_toe_boots() (+1 more)

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 24 - "kit_haruno.py"
Cohesion: 0.16
Nodes (6): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim()

### Community 25 - "Levels"
Cohesion: 0.14
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 26 - "wardrobe/kit.py"
Cohesion: 0.18
Nodes (7): collar(), flaps(), leg_bone(), leg_ring(), neckline(), pouch(), side_panels()

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (20): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kyahan() (+12 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.12
Nodes (12): back_crest(), chisel(), crest(), mallet(), nail_pouch(), pencil(), _piece(), sashiko() (+4 more)

### Community 29 - "Value"
Cohesion: 0.12
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.11
Nodes (8): arm_guards(), cargo(), gloves(), half_sleeves(), pocket(), shirt(), trousers(), vest()

### Community 32 - "outputs"
Cohesion: 0.20
Nodes (15): catalog(), hex_rgb(), json_text(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes(), main() (+7 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "stamp"
Cohesion: 0.11
Nodes (11): stamp(), crest(), crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), decal() (+3 more)

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "paint.py"
Cohesion: 0.12
Nodes (10): band(), cloth_shade(), dark_seams(), hair_box(), hair_face(), hair_shade(), hem(), shell() (+2 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Playthrough.java"
Cohesion: 0.15
Nodes (6): Kindling, Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 42 - "kit_akimichi.py"
Cohesion: 0.12
Nodes (7): flick(), gourd(), lames(), quilt(), shoku_disc(), snack_pouch(), sode()

### Community 43 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 44 - "Run"
Cohesion: 0.07
Nodes (19): 5. Personality, BondEvent, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS (+11 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 46 - "Tex"
Cohesion: 0.15
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 47 - "rot_matrix"
Cohesion: 0.18
Nodes (5): wave_lock(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.11
Nodes (4): puff(), curls_box(), Box, Layer

### Community 51 - "Face"
Cohesion: 0.18
Nodes (7): mark(), button(), curls_face(), darken_rows(), grid(), rivets(), Face

### Community 52 - "scalp"
Cohesion: 0.18
Nodes (7): ring_shell(), crown(), clipped(), combed_back(), pulled_back(), combed_up(), scalp()

### Community 53 - "pathlib"
Cohesion: 0.13
Nodes (3): build(), build(), build()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 55 - "CourtshipTest"
Cohesion: 0.20
Nodes (3): 10. Romance and family (after the beta), 20. What the roadmap asks of bonds, CourtshipTest

### Community 57 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 58 - ".page"
Cohesion: 0.19
Nodes (6): 12. The bond book, BondBook, Fact, MemoryLine, Page, BondWeb

### Community 59 - "kit_shinobi.py"
Cohesion: 0.14
Nodes (6): head_cloth(), anbu_arms(), anbu_plates(), flak_vest(), forehead_protector(), sandals()

### Community 61 - ".classic"
Cohesion: 0.16
Nodes (3): ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 62 - "blocks.py"
Cohesion: 0.10
Nodes (30): 2. Style guide: the Konoha kit, 6. Prototypes, By building type, Facades and shop fronts, Lanterns, Roofs, Shared palette, Streets (+22 more)

### Community 64 - "Custom blocks"
Cohesion: 0.11
Nodes (18): 4. Block catalogue, Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Displays (item-rendering), Festival (+10 more)

### Community 65 - "kit_specialist.py"
Cohesion: 0.17
Nodes (5): bandolier(), coat_skirts(), cross_armband(), scroll_tube(), strap()

### Community 66 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 67 - "VillageScaleTest"
Cohesion: 0.16
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.13
Nodes (3): ConflictTest, MemoryTest, ReactionTest

### Community 70 - "Bonds"
Cohesion: 0.09
Nodes (15): 11. Kindling Bond, 13. Data formats, 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters (+7 more)

### Community 71 - ".read"
Cohesion: 0.10
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (14): Def, Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR (+6 more)

### Community 73 - ".name"
Cohesion: 0.04
Nodes (28): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS, State (+20 more)

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (3): Deed, Know, Gossip

### Community 75 - "cel_box"
Cohesion: 0.23
Nodes (4): braid(), cel_box(), cel_face(), nape_hem()

### Community 77 - "catalogue.py"
Cohesion: 0.20
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 78 - ".test"
Cohesion: 0.06
Nodes (3): Bond, BondConditions, BondEffects

### Community 80 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 81 - "kit_namiashi.py"
Cohesion: 0.24
Nodes (4): back_blade(), crest(), hip_kokuto(), kokuto()

### Community 82 - "masks.py"
Cohesion: 0.18
Nodes (6): How the pieces work, belt(), mesh(), tanto(), beak(), ears()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_umino.py"
Cohesion: 0.20
Nodes (4): falling_tail(), knot(), surf(), waves()

### Community 85 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 86 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 88 - "wide_sleeves"
Cohesion: 0.28
Nodes (5): arm_bone(), arm_x(), armband(), roll(), wide_sleeves()

### Community 89 - "Shared helpers"
Cohesion: 0.20
Nodes (7): Shared helpers, back_fan(), lock(), sidelocks(), hime_locks(), beard(), wraps()

### Community 90 - ".born"
Cohesion: 0.11
Nodes (3): BondDialogue, Household, Recruitment

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 93 - "Every building"
Cohesion: 0.07
Nodes (29): 1. The answer: how much it will be, 3. Building catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Apartment buildings, Calibration, Clan builds (+21 more)

### Community 94 - "Village"
Cohesion: 0.06
Nodes (8): 18. Village scale, 19. Society hooks, Base, ClanRelations, SocialTie, SocietyHook, House, Village

### Community 95 - "chain"
Cohesion: 0.21
Nodes (4): chain(), mesh_arms(), mesh_shirt(), net()

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook, as these templates expect it, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "kit_hatake.py"
Cohesion: 0.25
Nodes (3): decal(), shoulder_decal(), slanted_protector()

### Community 102 - "Memory"
Cohesion: 0.18
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 103 - "Person"
Cohesion: 0.08
Nodes (10): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+2 more)

### Community 104 - "Stage"
Cohesion: 0.33
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "kit_hyuga.py"
Cohesion: 0.16
Nodes (7): bangs(), tie(), blunt_fringe(), ear_panels(), gathered_tail(), hair_tie(), parted_fringe()

### Community 109 - "masks.py"
Cohesion: 0.33
Nodes (3): bump(), plate(), strap()

### Community 114 - "json"
Cohesion: 0.38
Nodes (3): paste(), scene(), load_characters()

### Community 118 - "kit_uzumaki.py"
Cohesion: 0.29
Nodes (3): crest_patch(), seal_script(), seal_tags()

## Knowledge Gaps
- **153 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+148 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 987 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **34 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bonds` connect `Bonds` to `Memory`, `.read`, `Story bible`, `.name`, `Person`, `Run`, `Meters`, `GossipTest`, `CourtshipTest`, `Levels`, `.page`, `Value`, `Village`, `Personality`?**
  _High betweenness centrality (0.457) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _153 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `kit_shiranui.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13725490196078433 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.363) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `Clans`, `kit_academy.py`, `paint.py`, `cel_box`, `kit_hyuga.py`, `fabric`, `curtain`, `kit_nara.py`, `masks.py`, `scalp`, `wardrobe/kit.py`, `kit_shinobi.py`?**
  _High betweenness centrality (0.301) - this node is a cross-community bridge._