# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 101 files · ~134,564 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2081 nodes · 4728 edges · 146 communities (89 shown, 57 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 415 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `afa129ae`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- stamp
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
- waves
- solid
- cel_box
- kit_rugged.py
- kit_household.py
- strip_fabric
- Garment
- mesh_shirt
- kit_shimura.py
- arm_bone
- k
- kit_market.py
- kit_kinoshita.py
- kit_morino.py
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
- kokuto
- Run
- load_clans
- belt
- rot_matrix
- build
- Box
- chain
- Face
- ring_shell
- kit_gekko.py
- Act
- Person
- .bond
- kit_hagane.py
- Conflict
- kit_specialist.py
- org.junit.jupiter.api.Test
- surf
- Personality
- list
- BondWorld
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
- Playthrough.java
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
- .person
- Meter
- Title
- .name
- 18. Village scale
- Experience
- Side quests
- 4.4 The minor clans
- GossipTest
- 2. Quest framework
- Memory
- Label
- Source
- Trait
- lock
- CourtshipTest
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- bangs
- glyphs.py
- paint.py
- 4. Clan quest lines
- vial
- shade
- stripes
- side_stripe
- body
- sword_strap
- white_fang_tanto
- obi
- wrap_front
- claw_marks
- fang
- fang_small
- paw
- sashiko
- frog_buttons
- brush_stroke
- wrap_front
- leg_ring
- checks
- open_front
- stripes
- sashiko
- wave_band
- straw_sandals
- flame_hem
- trench_knife
- bandolier
- apothecary_sash
- bell_charm
- bell_hem
- gloves

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
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java
- `18. Village scale` --references--> `ClanProfile`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/ClanProfile.java
- `Bonds` --references--> `ClanProfile`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/ClanProfile.java

## Import Cycles
- None detected.

## Communities (146 total, 57 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.17
Nodes (8): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), crest_patch(), guardian_sash(), monkey()

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
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.08
Nodes (12): drawstrings(), forearm_wraps(), holster(), hood_down(), leg_cloth(), ribbed(), sash(), shin_wraps() (+4 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (32): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+24 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.09
Nodes (11): back_crest(), bead_clip(), brush_pin(), bun(), ink_clouds(), part_line(), side_fringe(), splatter() (+3 more)

### Community 9 - "rnd"
Cohesion: 0.17
Nodes (8): fur_box(), fur_edge(), fur_face(), hair_box(), hair_face(), hair_shade(), rnd(), shell()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.11
Nodes (8): arm_warmers(), kimono_sleeves(), mandarin_collar(), round_bun(), shin_wrap(), tabi_boots(), wave_lock(), wrap_front()

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "fabric"
Cohesion: 0.12
Nodes (10): back_crest(), crest(), arm_protector(), back_crest(), crest(), protector_plate(), backward_bandana(), dolphin() (+2 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.29
Nodes (3): back_crest(), bell_print(), bell_sprig()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 17 - "solid"
Cohesion: 0.10
Nodes (10): face_mask(), sash(), coat_skirts(), pauldron(), scarf(), cane(), herb_pouch(), shimenawa() (+2 more)

### Community 18 - "cel_box"
Cohesion: 0.15
Nodes (9): cel_box(), tie(), ear_panels(), gathered_tail(), hair_tie(), nape_hem(), pineapple(), tuft() (+1 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (16): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+8 more)

### Community 20 - "kit_household.py"
Cohesion: 0.05
Nodes (23): arm_cloth(), bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta() (+15 more)

### Community 21 - "strip_fabric"
Cohesion: 0.05
Nodes (23): shirt(), vest(), trouser_legs(), waist(), kimono_sleeves(), tabi(), anbu_plates(), sandals() (+15 more)

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 24 - "kit_shimura.py"
Cohesion: 0.29
Nodes (3): back_crest(), bandaged_arm(), bandage()

### Community 25 - "arm_bone"
Cohesion: 0.11
Nodes (13): sleeve_roll(), sode(), arm_bone(), arm_x(), arm_guards(), wide_sleeves(), kimono_sleeves(), tasuki() (+5 more)

### Community 26 - "k"
Cohesion: 0.18
Nodes (10): collar(), flaps(), footwear(), legs(), neckline(), pouch(), roll(), stockings() (+2 more)

### Community 27 - "kit_market.py"
Cohesion: 0.06
Nodes (17): bib(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri(), kyahan() (+9 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.11
Nodes (13): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+5 more)

### Community 29 - "kit_morino.py"
Cohesion: 0.16
Nodes (5): back_crest(), gloves(), head_cloth(), anbu_arms(), forehead_protector()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.07
Nodes (16): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+8 more)

### Community 32 - "outputs"
Cohesion: 0.17
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+8 more)

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
Cohesion: 0.12
Nodes (8): bun(), clip(), crest_patch(), hairpin(), seal_script(), seal_tags(), waves(), wrap_tie()

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
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.07
Nodes (19): 15. Pacing, BondEvent, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS (+11 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

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
Cohesion: 0.08
Nodes (15): mark(), drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+7 more)

### Community 52 - "ring_shell"
Cohesion: 0.16
Nodes (7): cel_face(), ring_shell(), crown(), clipped(), combed_back(), pulled_back(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 55 - "Person"
Cohesion: 0.07
Nodes (10): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+2 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.18
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 58 - "Conflict"
Cohesion: 0.10
Nodes (3): Conflict, Grant, Recruitment

### Community 59 - "kit_specialist.py"
Cohesion: 0.15
Nodes (6): bandolier(), coat_skirts(), ink_stains(), scroll_tube(), seal_trim(), strap()

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.14
Nodes (5): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, SquadTest, VillageTest

### Community 63 - "Personality"
Cohesion: 0.12
Nodes (5): 20. What the roadmap asks of bonds, 5. Personality, Personality, Reaction, ReactionTest

### Community 64 - "list"
Cohesion: 0.12
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 66 - "Village"
Cohesion: 0.15
Nodes (5): Tier, BACKGROUND, CAST, KNOWN, Village

### Community 67 - "VillageScaleTest"
Cohesion: 0.16
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.15
Nodes (3): ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.12
Nodes (14): 11. Kindling Bond, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 3. Levels and story gates (+6 more)

### Community 71 - ".read"
Cohesion: 0.23
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.12
Nodes (5): Def, Size, BIG, NOTABLE, SMALL

### Community 77 - "Playthrough.java"
Cohesion: 0.14
Nodes (7): Household, Kindling, Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 80 - "Value"
Cohesion: 0.13
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "masks.py"
Cohesion: 0.14
Nodes (8): How the pieces work, flak_vest(), mesh(), tanto(), beak(), bump(), ears(), strap()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - ".page"
Cohesion: 0.23
Nodes (5): 12. The bond book, BondBook, Fact, MemoryLine, Page

### Community 86 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 88 - "Shared helpers"
Cohesion: 0.18
Nodes (7): Shared helpers, back_fan(), braid(), curtain(), sidelocks(), back_sheet(), wraps()

### Community 89 - "kit_umino.py"
Cohesion: 0.15
Nodes (6): spike(), burst(), brush_tail(), combed_up(), falling_tail(), wave_band()

### Community 91 - "Meter"
Cohesion: 0.15
Nodes (6): Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - "Title"
Cohesion: 0.19
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.15
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 95 - "Experience"
Cohesion: 0.17
Nodes (9): Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR, STUDY (+1 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook, as these templates expect it, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 101 - "Label"
Cohesion: 0.22
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "Source"
Cohesion: 0.25
Nodes (6): Know, Source, HEARD, SEEN, SELF, TOLD

### Community 103 - "Trait"
Cohesion: 0.29
Nodes (7): Lean, Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH

### Community 104 - "lock"
Cohesion: 0.25
Nodes (4): lock(), hime_locks(), beard(), flicks()

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

## Knowledge Gaps
- **153 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+148 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 880 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **57 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bonds` connect `Bonds` to `GossipTest`, `Conflict`, `Memory`, `.read`, `Story bible`, `CourtshipTest`, `Run`, `.romance`, `Meters`, `Value`, `Mood`, `.page`, `Person`, `ClanRelations`, `.person`, `18. Village scale`, `Personality`?**
  _High betweenness centrality (0.486) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _153 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.463) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._