# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 112 files · ~158,133 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2310 nodes · 5081 edges · 141 communities (100 shown, 41 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 473 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0de803a1`
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
- kit_shiranui.py
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
- wardrobe/kit.py
- kit_market.py
- kit_kinoshita.py
- kimono_sleeves
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_shiranui.py
- 4. Technical architecture
- 6. The map
- wide_sleeves
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
- Person
- .bond
- kit_hagane.py
- .page
- fabric
- list
- org.junit.jupiter.api.Test
- blocks.py
- Personality
- Custom blocks
- pathlib
- org.junit.jupiter.api.Test
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
- ClanProfile
- Mood
- masks.py
- 4.3 The noble clans
- .name
- Experience
- Peeve
- ClanRelations
- Shared helpers
- kit_umino.py
- .born
- Meter
- Title
- Every building
- 18. Village scale
- utility_pole
- Side quests
- 4.4 The minor clans
- strip_fabric
- 2. Quest framework
- ROADMAP.md
- Conflict
- Source
- CourtshipTest
- Memory
- lock
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- kit_hyuga.py
- The village
- paint.py
- SquadTest
- kit_specialist.py
- json
- Trait
- GossipTest
- Side quest secrets
- k
- .populate
- Tier
- hood_down
- sash
- turned_hem
- furoshiki
- seal_script
- bandage_turns
- footwear
- geta
- loose_legs
- tasuki
- waist_apron
- sash
- rolled_cuffs
- sleeves
- sandals
- kit_sarutobi.py
- scroll_tube

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
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java

## Import Cycles
- None detected.

## Communities (141 total, 41 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.15
Nodes (7): stamp(), decal(), shoulder_decal(), slanted_protector(), crest_patch(), bump(), plate()

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
Cohesion: 0.11
Nodes (9): drawstrings(), forearm_wraps(), holster(), ribbed(), shin_wraps(), side_stripe(), stripes(), waist_pouch() (+1 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.10
Nodes (12): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw(), hair_box() (+4 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.07
Nodes (16): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mist_swirls(), rose() (+8 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.08
Nodes (11): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), round_bun(), shin_wrap(), tabi_boots() (+3 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_shiranui.py"
Cohesion: 0.22
Nodes (4): arm_protector(), protector_plate(), backward_bandana(), crest()

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
Cohesion: 0.10
Nodes (11): mandarin_collar(), face_mask(), white_fang_tanto(), sash(), hakama_legs(), coat_skirts(), cane(), scroll() (+3 more)

### Community 18 - "cel_box"
Cohesion: 0.13
Nodes (11): cel_box(), tie(), ear_panels(), gathered_tail(), hair_tie(), nape_hem(), back_crest(), crest() (+3 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "kit_household.py"
Cohesion: 0.05
Nodes (22): arm_cloth(), bands(), blossom(), checks(), cloth_shoes(), collar_band(), dots(), geta() (+14 more)

### Community 21 - "kit_tobari.py"
Cohesion: 0.08
Nodes (15): shirt(), pouch(), anbu_plates(), decal(), hood_down(), lantern(), lantern_tag(), mantle() (+7 more)

### Community 22 - "Garment"
Cohesion: 0.31
Nodes (3): compatible(), Garment, key_rgba()

### Community 24 - "kit_shimura.py"
Cohesion: 0.29
Nodes (3): back_crest(), bandaged_arm(), bandage()

### Community 26 - "wardrobe/kit.py"
Cohesion: 0.13
Nodes (9): belt(), body(), collar(), flaps(), leg_bone(), leg_ring(), neckline(), side_panels() (+1 more)

### Community 27 - "kit_market.py"
Cohesion: 0.07
Nodes (13): bib(), checks(), gathered_ankles(), jika_tabi(), kasuri(), kyahan(), open_front(), patch() (+5 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.07
Nodes (14): arm_guards(), blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards() (+6 more)

### Community 32 - "outputs"
Cohesion: 0.19
Nodes (15): catalog(), hex_rgb(), json_text(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes(), main() (+7 more)

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

### Community 38 - "wide_sleeves"
Cohesion: 0.28
Nodes (5): arm_bone(), arm_x(), armband(), roll(), wide_sleeves()

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
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), sode() (+1 more)

### Community 43 - "kit_namiashi.py"
Cohesion: 0.24
Nodes (4): back_blade(), crest(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.07
Nodes (19): 15. Pacing, BondEvent, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS (+11 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 46 - "Tex"
Cohesion: 0.15
Nodes (3): paper_lantern(), hexrgb(), Tex

### Community 47 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.10
Nodes (5): band(), hem(), strip_line(), Box, Layer

### Community 51 - "Face"
Cohesion: 0.07
Nodes (17): mark(), drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+9 more)

### Community 52 - "ring_shell"
Cohesion: 0.16
Nodes (7): ring_shell(), crown(), clipped(), combed_back(), pulled_back(), combed_up(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 55 - "Person"
Cohesion: 0.06
Nodes (11): BondWeb, Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.16
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 58 - ".page"
Cohesion: 0.14
Nodes (11): BondBook, Fact, MemoryLine, Page, Grant, Kindling, Tier, FULL (+3 more)

### Community 59 - "fabric"
Cohesion: 0.13
Nodes (8): back_crest(), crest(), back_crest(), head_cloth(), guardian_sash(), forehead_protector(), dolphin(), fabric()

### Community 60 - "list"
Cohesion: 0.05
Nodes (17): Stage, ADULT, CHILD, TEEN, Base, Value, COURAGE, CREATIVITY (+9 more)

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.13
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 62 - "blocks.py"
Cohesion: 0.10
Nodes (30): 2. Style guide: the Konoha kit, 6. Prototypes, By building type, Facades and shop fronts, Lanterns, Roofs, Shared palette, Streets (+22 more)

### Community 63 - "Personality"
Cohesion: 0.14
Nodes (5): 20. What the roadmap asks of bonds, 5. Personality, Personality, Reaction, ReactionTest

### Community 64 - "Custom blocks"
Cohesion: 0.12
Nodes (15): Academy, Residence, hospital, stadium, Clan signatures, Crafting stations, Crests and banners, Custom blocks, Festival, Furniture (the Leaf set), Gardens (+7 more)

### Community 65 - "pathlib"
Cohesion: 0.13
Nodes (3): build(), build(), build()

### Community 70 - "Bonds"
Cohesion: 0.15
Nodes (12): 11. Kindling Bond, 12. The bond book, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+4 more)

### Community 71 - ".read"
Cohesion: 0.20
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.12
Nodes (5): Def, Size, BIG, NOTABLE, SMALL

### Community 73 - "Levels"
Cohesion: 0.18
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.13
Nodes (3): 8. The village talks, Deed, Gossip

### Community 77 - "catalogue.py"
Cohesion: 0.21
Nodes (9): block_totals(), building_totals(), first_slice(), load(), main(), md_block_summary(), md_block_table(), md_building_totals() (+1 more)

### Community 81 - "Mood"
Cohesion: 0.12
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "masks.py"
Cohesion: 0.15
Nodes (7): How the pieces work, anbu_arms(), flak_vest(), mesh(), tanto(), beak(), ears()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - ".name"
Cohesion: 0.14
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 85 - "Experience"
Cohesion: 0.18
Nodes (9): Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR, STUDY (+1 more)

### Community 86 - "Peeve"
Cohesion: 0.15
Nodes (11): Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS, NEGLECT (+3 more)

### Community 87 - "ClanRelations"
Cohesion: 0.12
Nodes (9): Base, ClanRelations, Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL (+1 more)

### Community 88 - "Shared helpers"
Cohesion: 0.20
Nodes (6): Shared helpers, back_fan(), braid(), cel_face(), sidelocks(), wraps()

### Community 89 - "kit_umino.py"
Cohesion: 0.13
Nodes (7): spike(), burst(), brush_tail(), falling_tail(), surf(), wave_band(), waves()

### Community 90 - ".born"
Cohesion: 0.22
Nodes (3): 13. Data formats, BondDialogue, Household

### Community 91 - "Meter"
Cohesion: 0.15
Nodes (6): Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST

### Community 92 - "Title"
Cohesion: 0.17
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Every building"
Cohesion: 0.13
Nodes (15): 3. Building catalogue, Apartment buildings, Clan builds, Design programs, Every building, Forest of Death, Homes, Landmarks (+7 more)

### Community 94 - "18. Village scale"
Cohesion: 0.14
Nodes (4): 19. Society hooks, SocietyHook, House, Village

### Community 95 - "utility_pole"
Cohesion: 0.13
Nodes (15): 1. The answer: how much it will be, 4. Block catalogue, 5. Process, 7. Effort estimate, 8. Registration notes for Phase 0, Calibration, Contents, Konoha: the build plan (+7 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook, as these templates expect it, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.13
Nodes (15): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.4 The minor clans, 4.5 Clan quest counts, 4. Clan quest lines, Hagane, Haruno, Kinoshita (+7 more)

### Community 98 - "strip_fabric"
Cohesion: 0.11
Nodes (11): leg_cloth(), waist(), trouser_legs(), waist(), wide_sleeves(), tabi(), legs(), gloves() (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "ROADMAP.md"
Cohesion: 0.29
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 102 - "Source"
Cohesion: 0.22
Nodes (6): Know, Source, HEARD, SEEN, SELF, TOLD

### Community 105 - "lock"
Cohesion: 0.20
Nodes (5): lock(), hime_locks(), wave_lock(), beard(), flicks()

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "kit_hyuga.py"
Cohesion: 0.19
Nodes (5): bangs(), curtain(), back_sheet(), blunt_fringe(), parted_fringe()

### Community 109 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 113 - "kit_specialist.py"
Cohesion: 0.12
Nodes (7): bandolier(), coat_skirts(), cross_armband(), ink_stains(), seal_trim(), shirt(), strap()

### Community 114 - "json"
Cohesion: 0.38
Nodes (3): paste(), scene(), load_characters()

### Community 115 - "Trait"
Cohesion: 0.29
Nodes (7): Lean, Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH

### Community 117 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 118 - "k"
Cohesion: 0.10
Nodes (11): sword_strap(), obi(), wrap_front(), straw_sandals(), wave_band(), bandolier(), bun(), clip() (+3 more)

### Community 121 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 137 - "kit_sarutobi.py"
Cohesion: 0.15
Nodes (7): crest(), crest_patch(), flame_hem(), monkey(), pauldron(), scarf(), trench_knife()

## Knowledge Gaps
- **153 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+148 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 985 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **41 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bonds` connect `Bonds` to `ROADMAP.md`, `Conflict`, `.read`, `CourtshipTest`, `Levels`, `Deed`, `Memory`, `Run`, `.romance`, `Meters`, `ClanProfile`, `Mood`, `Person`, `ClanRelations`, `.born`, `18. Village scale`, `Personality`?**
  _High betweenness centrality (0.458) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _153 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `stamp` be split into smaller, more focused modules?**
  _Cohesion score 0.14736842105263157 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `Shared helpers`, `ROADMAP.md`?**
  _High betweenness centrality (0.368) - this node is a cross-community bridge._
- **Should `kit_uchiha.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1286549707602339 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `footwear`, `Clans`, `strip_fabric`, `sandals`, `lock`, `kit_hyuga.py`, `Box`, `cel_box`, `masks.py`, `ring_shell`, `kit_tobari.py`, `kit_shimura.py`, `kit_umino.py`, `wardrobe/kit.py`, `fabric`?**
  _High betweenness centrality (0.302) - this node is a cross-community bridge._