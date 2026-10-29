# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 85 files · ~101,773 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 1641 nodes · 3720 edges · 78 communities (58 shown, 20 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 326 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e9d673b7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Run
- Act
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- kit_kurama.py
- rnd
- kit_yuhi.py
- Squad
- .tier
- kit_suzuran.py
- 7. Systems in the beta
- fabric
- paint.py
- kit_hyuga.py
- kit_nara.py
- kit_kunoichi.py
- kit_tobari.py
- Garment
- kit_sarutobi.py
- org.junit.jupiter.api.Test
- arm_bone
- .of
- kit_hagane.py
- Personality
- k
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
- .meters
- rot_matrix
- build
- Box
- BondWorld
- shade
- Deed
- .bond
- .test
- Bond
- Value
- Bonds
- Def
- Meter
- Person
- kit_haruno.py
- Memory
- .page
- Tier
- Playthrough.java
- Levels
- Experience
- Title
- GossipTest
- .cap
- State
- ReactionTest.java
- chain

## God Nodes (most connected - your core abstractions)
1. `k()` - 176 edges
2. `solid()` - 120 edges
3. `BondWorld` - 118 edges
4. `Act` - 94 edges
5. `fabric()` - 91 edges
6. `Bond` - 43 edges
7. `strip_fabric()` - 43 edges
8. `stamp()` - 40 edges
9. `Meters` - 36 edges
10. `Person` - 35 edges

## Surprising Connections (you probably didn't know these)
- `10. Romance and family (after the beta)` --references--> `CourtshipTest`  [INFERRED]
  BONDS.md → life/bonds/src/test/java/dev/shinobi/life/bond/CourtshipTest.java
- `15. Pacing` --references--> `TimeAndPacingTest`  [INFERRED]
  BONDS.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java
- `13. Data formats` --references--> `Memory`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Memory.java

## Import Cycles
- None detected.

## Communities (78 total, 20 thin omitted)

### Community 0 - "Run"
Cohesion: 0.07
Nodes (19): 5. Personality, BondEvent, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS (+11 more)

### Community 1 - "Act"
Cohesion: 0.03
Nodes (56): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+48 more)

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.28
Nodes (3): lames(), plate(), shoulder_guards()

### Community 4 - "render.py"
Cohesion: 0.12
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.05
Nodes (25): drawstrings(), forearm_wraps(), holster(), hood_down(), sash(), shin_wraps(), side_stripe(), sleeve_roll() (+17 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (28): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible (+20 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (14): back_crest(), bead_clip(), brush_stroke(), bun(), ink_clouds(), part_line(), splatter(), stamp() (+6 more)

### Community 9 - "rnd"
Cohesion: 0.10
Nodes (10): spike(), crown(), burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge() (+2 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "Squad"
Cohesion: 0.09
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "fabric"
Cohesion: 0.05
Nodes (37): Shared helpers, leg_cloth(), shirt(), waist(), body(), collar(), half_sleeves(), shirt() (+29 more)

### Community 17 - "paint.py"
Cohesion: 0.06
Nodes (17): stamp(), crescent(), hip_katana(), katana(), decal(), shoulder_decal(), slanted_protector(), back_crest() (+9 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.09
Nodes (15): cel_box(), curtain(), tie(), back_sheet(), crest(), ear_panels(), gathered_tail(), hair_tie() (+7 more)

### Community 19 - "kit_nara.py"
Cohesion: 0.10
Nodes (12): cel_face(), ring_shell(), crown(), clipped(), combed_back(), back_crest(), crest(), mesh_shirt() (+4 more)

### Community 20 - "kit_kunoichi.py"
Cohesion: 0.08
Nodes (13): How the pieces work, belt(), arm_warmers(), frog_buttons(), mandarin_collar(), obi(), shin_wrap(), thigh_holster() (+5 more)

### Community 21 - "kit_tobari.py"
Cohesion: 0.10
Nodes (10): decal(), hood_down(), lantern(), lantern_tag(), mantle(), muffler(), pleats(), sash() (+2 more)

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "kit_sarutobi.py"
Cohesion: 0.22
Nodes (5): beard(), crest(), crest_patch(), flame_hem(), monkey()

### Community 24 - "org.junit.jupiter.api.Test"
Cohesion: 0.14
Nodes (5): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, SquadTest, VillageTest

### Community 25 - "arm_bone"
Cohesion: 0.08
Nodes (18): sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), kimono_sleeves(), armband(), roll() (+10 more)

### Community 26 - ".of"
Cohesion: 0.11
Nodes (7): Stage, ADULT, CHILD, TEEN, ConflictTest, Leaf, MemoryTest

### Community 27 - "kit_hagane.py"
Cohesion: 0.21
Nodes (5): bracers(), harness(), mace(), plate(), shin_guards()

### Community 28 - "Personality"
Cohesion: 0.10
Nodes (13): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+5 more)

### Community 29 - "k"
Cohesion: 0.04
Nodes (29): deep_hood(), high_collar(), hood_down(), lenses(), back_crest(), ribbed(), snack_pouch(), sword_strap() (+21 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.11
Nodes (11): blouse(), cargo(), collar(), gloves(), holster(), knee_guards(), pocket(), strap() (+3 more)

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
Cohesion: 0.12
Nodes (10): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+2 more)

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
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Face"
Cohesion: 0.07
Nodes (17): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), button() (+9 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.17
Nodes (6): flick(), gourd(), puff(), quilt(), shoku_disc(), curls_box()

### Community 43 - "kokuto"
Cohesion: 0.14
Nodes (7): back_blade(), crest(), hip_kokuto(), kokuto(), wave_band(), wave_lock(), rot_matrix()

### Community 44 - "lock"
Cohesion: 0.12
Nodes (9): back_fan(), bangs(), braid(), lock(), sidelocks(), blunt_fringe(), hime_locks(), parted_fringe() (+1 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 47 - "rot_matrix"
Cohesion: 0.33
Nodes (3): Piece, piece_corners(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.11
Nodes (3): strip_line(), Box, Layer

### Community 52 - "Deed"
Cohesion: 0.13
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 56 - "Value"
Cohesion: 0.11
Nodes (12): Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY, KINDNESS (+4 more)

### Community 57 - "Bonds"
Cohesion: 0.12
Nodes (13): 10. Romance and family (after the beta), 13. Data formats, 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 18. Open questions, 2. The meters, 4. Memories (+5 more)

### Community 58 - "Def"
Cohesion: 0.12
Nodes (5): Def, Size, BIG, NOTABLE, SMALL

### Community 59 - "Meter"
Cohesion: 0.13
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 61 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 62 - "Memory"
Cohesion: 0.20
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 63 - ".page"
Cohesion: 0.22
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 64 - "Tier"
Cohesion: 0.18
Nodes (8): 11. Kindling Bond, Grant, Kindling, Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 67 - "Experience"
Cohesion: 0.18
Nodes (9): Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR, STUDY (+1 more)

### Community 68 - "Title"
Cohesion: 0.22
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 71 - "State"
Cohesion: 0.29
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

## Knowledge Gaps
- **132 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+127 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 683 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bonds` connect `Bonds` to `Tier`, `Run`, `.cap`, `Story bible`, `Meters`, `Squad`, `Personality`, `.meters`, `Deed`, `.test`, `Person`, `Memory`?**
  _High betweenness centrality (0.500) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _132 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Run` be split into smaller, more focused modules?**
  _Cohesion score 0.0679563492063492 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `fabric`, `Story bible`?**
  _High betweenness centrality (0.441) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Act` be split into smaller, more focused modules?**
  _Cohesion score 0.034482758620689655 - nodes in this community are weakly interconnected._