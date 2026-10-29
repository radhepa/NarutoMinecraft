# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 94 files · ~113,658 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 1814 nodes · 4247 edges · 114 communities (76 shown, 38 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 416 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c5b4b975`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Run
- Act
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- rnd
- kit_yuhi.py
- Squad
- list
- .tier
- kit_suzuran.py
- 7. Systems in the beta
- strip_fabric
- stamp
- kit_hyuga.py
- scalp
- kit_kunoichi.py
- kit_tobari.py
- Garment
- kit_sarutobi.py
- org.junit.jupiter.api.Test
- arm_bone
- .of
- kit_hagane.py
- Value
- kit_aburame.py
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- Stage
- 4. Technical architecture
- 6. The map
- Meters
- 8. The beta, chapter by chapter
- 9. Delivery plan
- Face
- kit_akimichi.py
- kokuto
- lock
- load_clans
- BondWorld
- rot_matrix
- build
- Box
- BondWorld
- shade
- Deed
- .test
- VillageScaleTest
- Bond
- Personality
- Bonds
- Def
- Meter
- Person
- mandarin_collar
- .read
- .page
- Tier
- fabric
- Levels
- .week
- Title
- GossipTest
- ClanRelations
- State
- solid
- chain
- Mood
- Village
- .romance
- k
- kit_uchiha.py
- kit_shinobi.py
- leg_bone
- kit_specialist.py
- cel_box
- kit_nara.py
- Courtship
- kit_yamanaka.py
- Label
- kit_gekko.py
- kit_hatake.py
- kit_shimura.py
- CourtshipTest
- SocietyHook
- hood_down
- Stage
- paint.py
- curtain
- mesh_shirt
- sleeve_roll
- shin_wraps
- gloves
- vest
- sword_strap
- coat_skirts
- wave_band
- pauldron
- scarf
- split_toe_boots
- clip
- waves

## God Nodes (most connected - your core abstractions)
1. `k()` - 176 edges
2. `BondWorld` - 129 edges
3. `solid()` - 120 edges
4. `Act` - 101 edges
5. `fabric()` - 91 edges
6. `Village` - 62 edges
7. `Bond` - 44 edges
8. `strip_fabric()` - 43 edges
9. `Person` - 42 edges
10. `stamp()` - 40 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `15. Pacing` --references--> `TimeAndPacingTest`  [INFERRED]
  BONDS.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java
- `18. Village scale` --references--> `ClanProfile`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/ClanProfile.java

## Import Cycles
- None detected.

## Communities (114 total, 38 thin omitted)

### Community 0 - "Run"
Cohesion: 0.07
Nodes (18): BondEvent, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS, GENIN (+10 more)

### Community 1 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

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
Cohesion: 0.10
Nodes (10): drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), side_stripe(), stripes() (+2 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (28): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible (+20 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.05
Nodes (25): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+17 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.07
Nodes (16): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mist_swirls(), rose() (+8 more)

### Community 13 - ".tier"
Cohesion: 0.11
Nodes (3): BondDialogue, Household, Recruitment

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "strip_fabric"
Cohesion: 0.08
Nodes (12): leg_cloth(), waist(), body(), half_sleeves(), shirt(), trousers(), kimono_sleeves(), tabi() (+4 more)

### Community 17 - "stamp"
Cohesion: 0.18
Nodes (5): stamp(), crest(), crest_patch(), bump(), plate()

### Community 18 - "kit_hyuga.py"
Cohesion: 0.15
Nodes (8): bangs(), tie(), blunt_fringe(), gathered_tail(), hair_tie(), obi(), parted_fringe(), wrap_front()

### Community 19 - "scalp"
Cohesion: 0.24
Nodes (5): ring_shell(), crown(), combed_back(), pulled_back(), scalp()

### Community 20 - "kit_kunoichi.py"
Cohesion: 0.12
Nodes (8): belt(), arm_warmers(), frog_buttons(), mandarin_collar(), obi(), shin_wrap(), tabi_boots(), wrap_front()

### Community 21 - "kit_tobari.py"
Cohesion: 0.11
Nodes (10): shirt(), anbu_plates(), decal(), lantern(), lantern_tag(), muffler(), plain_body(), sash() (+2 more)

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_sarutobi.py"
Cohesion: 0.22
Nodes (5): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey()

### Community 24 - "org.junit.jupiter.api.Test"
Cohesion: 0.12
Nodes (5): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, SquadTest, VillageTest

### Community 25 - "arm_bone"
Cohesion: 0.13
Nodes (11): sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), kimono_sleeves(), armband(), cross_armband() (+3 more)

### Community 27 - "kit_hagane.py"
Cohesion: 0.18
Nodes (6): bracers(), crown(), harness(), mace(), plate(), shin_guards()

### Community 28 - "Value"
Cohesion: 0.07
Nodes (24): ClanProfile, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS (+16 more)

### Community 29 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.13
Nodes (7): cargo(), collar(), holster(), knee_guards(), pocket(), strap(), tape()

### Community 32 - "outputs"
Cohesion: 0.17
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+8 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "Stage"
Cohesion: 0.17
Nodes (8): Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE, SWEETHEARTS

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "Meters"
Cohesion: 0.11
Nodes (7): Memory, Meters, Source, HEARD, SEEN, SELF, TOLD

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Face"
Cohesion: 0.09
Nodes (14): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), button() (+6 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.12
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box()

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "lock"
Cohesion: 0.14
Nodes (9): Shared helpers, back_fan(), braid(), cel_face(), lock(), sidelocks(), hime_locks(), beard() (+1 more)

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

### Community 52 - "Deed"
Cohesion: 0.11
Nodes (3): Deed, Know, Gossip

### Community 54 - "VillageScaleTest"
Cohesion: 0.15
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 56 - "Personality"
Cohesion: 0.14
Nodes (3): Personality, Reaction, ReactionTest

### Community 57 - "Bonds"
Cohesion: 0.10
Nodes (15): 13. Data formats, 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 3. Levels and story gates (+7 more)

### Community 58 - "Def"
Cohesion: 0.08
Nodes (14): Def, Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR (+6 more)

### Community 59 - "Meter"
Cohesion: 0.10
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 60 - "Person"
Cohesion: 0.09
Nodes (3): 12. The bond book, BondWeb, Person

### Community 62 - ".read"
Cohesion: 0.23
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 63 - ".page"
Cohesion: 0.36
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 64 - "Tier"
Cohesion: 0.22
Nodes (8): 11. Kindling Bond, Grant, Kindling, Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 65 - "fabric"
Cohesion: 0.14
Nodes (9): back_crest(), crest(), back_crest(), gloves(), head_cloth(), arm_protector(), forehead_protector(), protector_plate() (+1 more)

### Community 67 - ".week"
Cohesion: 0.17
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 68 - "Title"
Cohesion: 0.22
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 71 - "State"
Cohesion: 0.25
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 72 - "solid"
Cohesion: 0.11
Nodes (10): face_mask(), white_fang_tanto(), trench_knife(), cane(), side_panels(), shimenawa(), hairpin(), wrap_tie() (+2 more)

### Community 78 - "Mood"
Cohesion: 0.13
Nodes (9): 18. Village scale, Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY (+1 more)

### Community 81 - "k"
Cohesion: 0.18
Nodes (10): collar(), flaps(), footwear(), legs(), neckline(), pouch(), roll(), stockings() (+2 more)

### Community 82 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 83 - "kit_shinobi.py"
Cohesion: 0.17
Nodes (6): How the pieces work, anbu_arms(), mesh(), tanto(), beak(), ears()

### Community 84 - "leg_bone"
Cohesion: 0.15
Nodes (7): turned_hem(), blouse(), hakama_legs(), thigh_holster(), leg_bone(), leg_ring(), heavy_boots()

### Community 85 - "kit_specialist.py"
Cohesion: 0.18
Nodes (5): bandolier(), coat_skirts(), scroll_tube(), shirt(), strap()

### Community 86 - "cel_box"
Cohesion: 0.18
Nodes (6): cel_box(), ear_panels(), round_bun(), wave_lock(), nape_hem(), bun()

### Community 87 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): spike(), back_crest(), crest(), pineapple(), tuft()

### Community 89 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 90 - "Label"
Cohesion: 0.22
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 91 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 92 - "kit_hatake.py"
Cohesion: 0.25
Nodes (3): decal(), shoulder_decal(), slanted_protector()

### Community 93 - "kit_shimura.py"
Cohesion: 0.29
Nodes (3): back_crest(), bandaged_arm(), bandage()

### Community 96 - "hood_down"
Cohesion: 0.33
Nodes (3): hood_down(), mantle(), pleats()

### Community 97 - "Stage"
Cohesion: 0.40
Nodes (4): Stage, ADULT, CHILD, TEEN

## Knowledge Gaps
- **153 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+148 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 727 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **38 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bonds` connect `Bonds` to `Tier`, `Run`, `GossipTest`, `ClanRelations`, `Story bible`, `Meters`, `Value`, `Mood`, `.romance`, `BondWorld`, `Personality`, `CourtshipTest`, `Person`, `.read`, `SocietyHook`?**
  _High betweenness centrality (0.496) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _153 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Run` be split into smaller, more focused modules?**
  _Cohesion score 0.07139079851930195 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `lock`, `Story bible`?**
  _High betweenness centrality (0.436) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Act` be split into smaller, more focused modules?**
  _Cohesion score 0.03125 - nodes in this community are weakly interconnected._