# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 124 files · ~178,670 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 30 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 2459 nodes · 5582 edges · 113 communities (82 shown, 31 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 585 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5802e804`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- fabric
- Wallet
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- solid
- Story bible
- kit_kurama.py
- kit_inuzuka.py
- kit_yuhi.py
- wave_lock
- .roll
- items.py
- .obj
- 7. Systems in the beta
- waves
- scroll
- cel_box
- kit_rugged.py
- kit_household.py
- strip_fabric
- Garment
- sprites.py
- Catalogue
- kit.py
- .shelf
- kit_market.py
- kit_kinoshita.py
- Json
- 5. Data formats built for the whole story
- kit_field.py
- outputs
- 11. Later systems
- Shinobi Modpack: roadmap
- kit_shiranui.py
- 4. Technical architecture
- 6. The map
- Shops
- 8. The beta, chapter by chapter
- 9. Delivery plan
- Prices
- k
- arm_guards
- Run
- load_clans
- Item catalogue
- rot_matrix
- build
- Box
- chain
- Face
- ring_shell
- Grades
- Act
- Person
- .bond
- crown
- Conflict
- VillageSim.java
- org.junit.jupiter.api.Test
- surf
- Personality
- assertions
- ROADMAP.md
- Village
- VillageScaleTest
- Bond
- .of
- Bonds
- .read
- Def
- Levels
- Deed
- food
- RuleOfThumbTest
- Tier
- .test
- Meters
- Value
- Mood
- How the pieces work
- 4.3 The noble clans
- kit_haruno.py
- .page
- Recipes
- kunai
- wave_band
- Person
- Meter
- Title
- .name
- Result
- Side quest secrets
- Side quests
- 4.4 The minor clans
- flick
- 2. Quest framework
- Memory
- topknot
- round_bun
- nape_hem
- flicks
- bun
- side_panels
- 8. Beta catalogue
- wrap_front

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
- `1.7 Gift tags` --references--> `Personality`  [INFERRED]
  ITEMS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Personality.java
- `3.2 Recipes` --references--> `CatalogueTest`  [INFERRED]
  ITEMS.md → life/economy/src/test/java/dev/shinobi/life/economy/CatalogueTest.java
- `Code by mod` --references--> `stats()`  [INFERRED]
  ROADMAP.md → tools/items/items.py
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java

## Import Cycles
- None detected.

## Communities (113 total, 31 thin omitted)

### Community 0 - "fabric"
Cohesion: 0.04
Nodes (34): stamp(), back_crest(), crescent(), decal(), shoulder_decal(), slanted_protector(), crest(), back_crest() (+26 more)

### Community 1 - "Wallet"
Cohesion: 0.05
Nodes (33): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+25 more)

### Community 2 - "Clans"
Cohesion: 0.14
Nodes (11): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Reference images, The clan file, clan_bottoms() (+3 more)

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
Nodes (27): drawstrings(), forearm_wraps(), holster(), hood_down(), sash(), shin_wraps(), side_stripe(), sleeve_roll() (+19 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (12): back_crest(), bead_clip(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe(), splatter() (+4 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.07
Nodes (19): sprigs(), kasuri(), camo(), ragged(), ink_stains(), seal_trim(), bandage_turns(), mist_swirls() (+11 more)

### Community 12 - ".roll"
Cohesion: 0.11
Nodes (5): Rng, Seeds, Rng, Streams, StreamsTest

### Community 13 - "items.py"
Cohesion: 0.14
Nodes (20): art_class(), catalogue_md(), check_all(), check_loot(), compile_all(), recipe_entry(), dumps(), err() (+12 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 18 - "cel_box"
Cohesion: 0.08
Nodes (22): Shared helpers, back_fan(), bangs(), braid(), cel_box(), curtain(), lock(), sidelocks() (+14 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.07
Nodes (15): baggy_legs(), cape(), dread(), knot_bun(), leg_wraps(), patch(), rope(), rope_face() (+7 more)

### Community 20 - "kit_household.py"
Cohesion: 0.03
Nodes (39): leg_cloth(), waist(), body(), flaps(), footwear(), arm_cloth(), bands(), blossom() (+31 more)

### Community 21 - "strip_fabric"
Cohesion: 0.07
Nodes (17): shirt(), vest(), pouch(), anbu_plates(), shirt(), decal(), hood_down(), lantern() (+9 more)

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 23 - "sprites.py"
Cohesion: 0.13
Nodes (21): build(), Canvas, charm(), flak_vest(), forehead_protector(), framed_ladle(), headband(), hexrgb() (+13 more)

### Community 24 - "Catalogue"
Cohesion: 0.14
Nodes (10): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+2 more)

### Community 25 - "kit.py"
Cohesion: 0.05
Nodes (29): sode(), arm_bone(), arm_x(), belt(), bracers(), mace(), plate(), frog_buttons() (+21 more)

### Community 26 - ".shelf"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (22): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kyahan() (+14 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.07
Nodes (17): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+9 more)

### Community 32 - "outputs"
Cohesion: 0.15
Nodes (18): catalog(), hex_rgb(), json_text(), load_characters(), load_collections(), load_eye_colors(), load_groups(), load_hair_colors() (+10 more)

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

### Community 38 - "Shops"
Cohesion: 0.07
Nodes (28): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), Furniture Shop (`furniture_shop`), gift (+20 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Prices"
Cohesion: 0.19
Nodes (3): Pawn, Prices, PricesTest

### Community 42 - "k"
Cohesion: 0.03
Nodes (39): deep_hood(), high_collar(), hood_down(), lenses(), ribbed(), gourd(), lames(), puff() (+31 more)

### Community 43 - "arm_guards"
Cohesion: 0.10
Nodes (14): gear, smithy, weapon, Weapon Shop (`weapon_shop`), shuriken(), arm_guards(), hip_katana(), katana() (+6 more)

### Community 44 - "Run"
Cohesion: 0.09
Nodes (17): 15. Pacing, BondEvent, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER (+9 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): Population, load_all_groups(), load_clans(), load_population(), population_weights(), validate_clans(), village_resident()

### Community 46 - "Item catalogue"
Cohesion: 0.12
Nodes (16): collectible, consumable, container, curio, currency, furniture, Item catalogue, keepsake (+8 more)

### Community 47 - "rot_matrix"
Cohesion: 0.18
Nodes (5): wave_lock(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.09
Nodes (7): band(), dark_seams(), hem(), strip_line(), Box, Layer, shade()

### Community 51 - "Face"
Cohesion: 0.07
Nodes (17): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), button() (+9 more)

### Community 52 - "ring_shell"
Cohesion: 0.10
Nodes (12): cel_face(), ring_shell(), crown(), clipped(), combed_back(), back_crest(), crest(), net() (+4 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 55 - "Person"
Cohesion: 0.10
Nodes (11): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+3 more)

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.10
Nodes (7): BondDialogueTest, ConditionsAndEffectsTest, GossipTest, KindlingAndBookTest, SquadTest, VillageTest, RyoTest

### Community 63 - "Personality"
Cohesion: 0.08
Nodes (16): 20. What the roadmap asks of bonds, 5. Personality, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY (+8 more)

### Community 64 - "assertions"
Cohesion: 0.11
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 65 - "ROADMAP.md"
Cohesion: 0.26
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 66 - "Village"
Cohesion: 0.06
Nodes (12): 18. Village scale, 19. Society hooks, Base, ClanRelations, SocialTie, SocietyHook, House, Tier (+4 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.14
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.12
Nodes (3): ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (13): 11. Kindling Bond, 13. Data formats, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+5 more)

### Community 71 - ".read"
Cohesion: 0.23
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (14): Def, Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR (+6 more)

### Community 73 - "Levels"
Cohesion: 0.19
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 75 - "food"
Cohesion: 0.20
Nodes (12): cooking.oven, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient, Market Grocer (`grocer`), dango() (+4 more)

### Community 77 - "Tier"
Cohesion: 0.25
Nodes (5): Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 78 - ".test"
Cohesion: 0.06
Nodes (5): 12. The bond book, BondConditions, BondWeb, Departure, Squad

### Community 80 - "Value"
Cohesion: 0.11
Nodes (13): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+5 more)

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "How the pieces work"
Cohesion: 0.18
Nodes (9): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, How the pieces work, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village, mesh() (+1 more)

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - ".page"
Cohesion: 0.36
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Recipes"
Cohesion: 0.22
Nodes (9): apothecary, cooking.pot, Ninja Tool Shop (`tool_shop`), Recipes, sealing, tailoring, tool, workbench (+1 more)

### Community 88 - "kunai"
Cohesion: 0.47
Nodes (5): Exam-Week Stalls (`exam_stalls`), along(), f(), kunai(), blade()

### Community 90 - "Person"
Cohesion: 0.11
Nodes (3): BondDialogue, Household, Person

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.14
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.09
Nodes (13): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS, State (+5 more)

### Community 95 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 96 - "Side quests"
Cohesion: 0.12
Nodes (17): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 7.1 What moves clan relations, 7.2 What clan relations do (+9 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.13
Nodes (15): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.4 The minor clans, 4.5 Clan quest counts, 4. Clan quest lines, Hagane, Haruno, Kinoshita (+7 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.16
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

## Knowledge Gaps
- **155 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+150 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 974 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **31 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `fabric`, `kit_senju.py`, `solid`, `kit_kurama.py`, `kit_inuzuka.py`, `kit_yuhi.py`, `cel_box`, `kit_rugged.py`, `kit_household.py`, `strip_fabric`, `kit.py`, `kit_market.py`, `kit_kinoshita.py`, `kit_field.py`, `kit_shiranui.py`, `Shops`, `arm_guards`, `Box`, `Face`, `ring_shell`, `kit_haruno.py`, `wrap_front`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _155 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.04196738839882384 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `ROADMAP.md`, `Village`, `Memory`, `.read`, `Levels`, `Deed`, `Run`, `.test`, `Meters`, `Value`, `Mood`, `Person`, `Person`, `Personality`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Wallet` be split into smaller, more focused modules?**
  _Cohesion score 0.04698581560283688 - nodes in this community are weakly interconnected._