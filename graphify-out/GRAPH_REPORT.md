# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 103 files · ~124,318 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 1958 nodes · 4718 edges · 89 communities (62 shown, 27 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 501 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9c3505d7`
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
- .effectiveLevel
- kit_suzuran.py
- 7. Systems in the beta
- .roll
- .talk
- k
- strip_fabric
- Garment
- stamp
- .classic
- fabric
- .of
- Meters
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
- Memory
- 8. The beta, chapter by chapter
- 9. Delivery plan
- Face
- kit_akimichi.py
- kit_namiashi.py
- kit_hyuga.py
- load_clans
- BondWorld
- Kind
- kit_tsuchigumo.py
- Box
- BondWorld
- Peeve
- Deed
- .test
- VillageScaleTest
- Bond
- Personality
- Bonds
- Def
- Meter
- Person
- Experience
- .read
- .page
- Tier
- fabric
- Levels
- .week
- Conflict
- GossipTest
- ClanRelations
- org.junit.jupiter.api.Test
- SquadTest
- .day
- MemoryTest
- Mood
- Village
- .romance
- BondWeb
- kit_shinobi.py
- Courtship
- kit_yamanaka.py
- CourtshipTest
- mesh_shirt

## God Nodes (most connected - your core abstractions)
1. `k()` - 176 edges
2. `BondWorld` - 155 edges
3. `solid()` - 120 edges
4. `Act` - 113 edges
5. `fabric()` - 91 edges
6. `Village` - 62 edges
7. `Bond` - 57 edges
8. `Person` - 50 edges
9. `strip_fabric()` - 43 edges
10. `stamp()` - 40 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `15. Pacing` --references--> `TimeAndPacingTest`  [INFERRED]
  BONDS.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `8. Pacing with time together` --references--> `TimeAndPacingTest`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `Shared helpers` --references--> `wraps()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit_shinobi.py
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py

## Import Cycles
- None detected.

## Communities (89 total, 27 thin omitted)

### Community 0 - "Run"
Cohesion: 0.07
Nodes (18): BondEvent, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS, GENIN (+10 more)

### Community 1 - "Act"
Cohesion: 0.03
Nodes (70): Act, ABANDONED_MISSION, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED, BOND_MOMENT (+62 more)

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.28
Nodes (3): lames(), plate(), shoulder_guards()

### Community 4 - "render.py"
Cohesion: 0.13
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "solid"
Cohesion: 0.04
Nodes (28): drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), sash(), shin_wraps(), side_stripe() (+20 more)

### Community 7 - "Story bible"
Cohesion: 0.07
Nodes (28): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible (+20 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (12): back_crest(), bead_clip(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe(), splatter() (+4 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.08
Nodes (17): clipped(), ink_stains(), seal_trim(), bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine() (+9 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".roll"
Cohesion: 0.07
Nodes (21): Activity, DialogueKeys, Schedule, Answer, Highlight, Invitation, Outcome, Plan (+13 more)

### Community 18 - ".talk"
Cohesion: 0.14
Nodes (6): Conversation, Reply, Topic, LifeEvents, News, 6. Conversation

### Community 20 - "k"
Cohesion: 0.06
Nodes (28): Shared helpers, belt(), body(), collar(), flaps(), footwear(), frog_clasps(), kimono_trim() (+20 more)

### Community 21 - "strip_fabric"
Cohesion: 0.05
Nodes (26): leg_cloth(), shirt(), waist(), vest(), tabi(), anbu_arms(), anbu_plates(), flak_vest() (+18 more)

### Community 22 - "Garment"
Cohesion: 0.16
Nodes (6): compatible(), Garment, key_rgba(), Piece, piece_corners(), world_bounds()

### Community 23 - "stamp"
Cohesion: 0.04
Nodes (27): stamp(), back_crest(), shoku_disc(), crescent(), hip_katana(), katana(), sword_strap(), decal() (+19 more)

### Community 24 - ".classic"
Cohesion: 0.17
Nodes (3): ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 25 - "fabric"
Cohesion: 0.06
Nodes (28): sode(), arm_bone(), arm_x(), arm_guards(), bracers(), mace(), plate(), shin_guards() (+20 more)

### Community 28 - "Value"
Cohesion: 0.12
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 29 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.07
Nodes (17): blouse(), cargo(), chain(), collar(), gloves(), half_sleeves(), holster(), knee_guards() (+9 more)

### Community 32 - "outputs"
Cohesion: 0.12
Nodes (21): build(), build_all(), catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors() (+13 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "Stage"
Cohesion: 0.20
Nodes (8): Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE, SWEETHEARTS

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "Memory"
Cohesion: 0.20
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.33
Nodes (6): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Face"
Cohesion: 0.11
Nodes (12): button(), curls_face(), dark_seams(), darken_rows(), grid(), hair_box(), hair_face(), hair_shade() (+4 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.20
Nodes (5): flick(), gourd(), puff(), quilt(), curls_box()

### Community 43 - "kit_namiashi.py"
Cohesion: 0.16
Nodes (6): back_blade(), hip_kokuto(), kokuto(), wave_band(), wave_lock(), rot_matrix()

### Community 44 - "kit_hyuga.py"
Cohesion: 0.05
Nodes (33): back_fan(), bangs(), braid(), cel_box(), cel_face(), curtain(), lock(), ring_shell() (+25 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 47 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 48 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 49 - "Box"
Cohesion: 0.10
Nodes (5): band(), hem(), strip_line(), Box, Layer

### Community 51 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 52 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 54 - "VillageScaleTest"
Cohesion: 0.12
Nodes (4): 20. What the roadmap asks of bonds, Report, VillageSim, VillageScaleTest

### Community 56 - "Personality"
Cohesion: 0.20
Nodes (3): 5. Personality, Personality, Reaction

### Community 57 - "Bonds"
Cohesion: 0.14
Nodes (13): 12. The bond book, 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 3. Levels and story gates (+5 more)

### Community 58 - "Def"
Cohesion: 0.12
Nodes (5): Def, Size, BIG, NOTABLE, SMALL

### Community 59 - "Meter"
Cohesion: 0.13
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 60 - "Person"
Cohesion: 0.15
Nodes (5): Person, Stage, ADULT, CHILD, TEEN

### Community 61 - "Experience"
Cohesion: 0.15
Nodes (10): Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION, SPAR (+2 more)

### Community 62 - ".read"
Cohesion: 0.20
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 63 - ".page"
Cohesion: 0.30
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 64 - "Tier"
Cohesion: 0.17
Nodes (8): 11. Kindling Bond, Grant, Kindling, Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 65 - "fabric"
Cohesion: 0.12
Nodes (8): back_crest(), coat_skirts(), gloves(), head_cloth(), heavy_boots(), arm_protector(), forehead_protector(), protector_plate()

### Community 66 - "Levels"
Cohesion: 0.06
Nodes (15): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, Levels, Title (+7 more)

### Community 67 - ".week"
Cohesion: 0.18
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 70 - "ClanRelations"
Cohesion: 0.11
Nodes (9): Base, ClanRelations, Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL (+1 more)

### Community 78 - "Mood"
Cohesion: 0.15
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 79 - "Village"
Cohesion: 0.12
Nodes (5): 18. Village scale, 19. Society hooks, SocietyHook, House, Village

### Community 83 - "kit_shinobi.py"
Cohesion: 0.15
Nodes (8): How the pieces work, mesh(), tanto(), beak(), bump(), ears(), plate(), strap()

### Community 89 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

## Knowledge Gaps
- **178 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+173 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 771 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **27 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bonds` connect `Bonds` to `Tier`, `Run`, `Conflict`, `GossipTest`, `ClanRelations`, `Story bible`, `Memory`, `Mood`, `Village`, `Person`, `.romance`, `VillageScaleTest`, `Personality`, `CourtshipTest`, `Meters`, `Value`, `.read`?**
  _High betweenness centrality (0.468) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _178 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Run` be split into smaller, more focused modules?**
  _Cohesion score 0.07086197778952935 - nodes in this community are weakly interconnected._
- **Why does `Clans` connect `Clans` to `k`, `Story bible`?**
  _High betweenness centrality (0.433) - this node is a cross-community bridge._
- **Should `Act` be split into smaller, more focused modules?**
  _Cohesion score 0.027777777777777776 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `k` to `fabric`, `Clans`, `solid`, `kit_hyuga.py`, `Box`, `kit_shinobi.py`, `strip_fabric`, `fabric`?**
  _High betweenness centrality (0.359) - this node is a cross-community bridge._