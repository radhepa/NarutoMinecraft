# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 124 files · ~180,177 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 30 file(s) not represented in the graph (top: .tsv 23, (none) 3, .properties 2)

## Summary
- 2460 nodes · 5588 edges · 154 communities (100 shown, 54 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 586 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b06ca035`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- fabric
- Wallet
- Clans
- kit_senju.py
- render.py
- living_eyes.py
- kit_academy.py
- Story bible
- kit_kurama.py
- kit_inuzuka.py
- kit_yuhi.py
- kit_kunoichi.py
- .roll
- items.py
- .obj
- 7. Systems in the beta
- kit_umino.py
- solid
- cel_box
- kit_rugged.py
- strip_fabric
- strip_fabric
- Garment
- sprites.py
- Catalogue
- arm_bone
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
- kit_akimichi.py
- katana
- Run
- stamp
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
- kit_hagane.py
- .test
- .classic
- kit_suzuran.py
- Personality
- Village
- .romance
- org.junit.jupiter.api.Test
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
- k
- anime.py
- Meter
- Title
- .name
- Result
- rnd
- Side quests
- 4.4 The minor clans
- kit_sarutobi.py
- 2. Quest framework
- Memory
- kit_household.py
- kit_shinobi.py
- Peeve
- ClanRelations
- kit_uchiha.py
- kit_uzumaki.py
- 8. Beta catalogue
- arm_guards
- paint.py
- Experience
- Label
- kit_aburame.py
- .populate
- kit_yamanaka.py
- Conflict
- GossipTest
- wrap_front
- SquadTest
- jika_tabi
- 7. Inter-clan politics as quests
- side_panels
- Tier
- 4. Clan quest lines
- belt
- bandolier
- bandage_turns
- wide_sleeves
- sash
- sleeve_roll
- sword_strap
- face_mask
- arm_cloth
- collar_band
- dots
- ichimatsu
- overlap
- stripes
- obi
- wood_grain
- coat_skirts
- wave_band
- bandolier
- coat_skirts
- shin_wraps
- sash
- high_collar
- wrap_tie

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
- `10. Romance and family (after the beta)` --references--> `CourtshipTest`  [INFERRED]
  BONDS.md → life/bonds/src/test/java/dev/shinobi/life/bond/CourtshipTest.java
- `3.2 Recipes` --references--> `CatalogueTest`  [INFERRED]
  ITEMS.md → life/economy/src/test/java/dev/shinobi/life/economy/CatalogueTest.java
- `Code by mod` --references--> `stats()`  [INFERRED]
  ROADMAP.md → tools/items/items.py

## Import Cycles
- None detected.

## Communities (154 total, 54 thin omitted)

### Community 0 - "fabric"
Cohesion: 0.11
Nodes (11): back_crest(), crest(), back_crest(), head_cloth(), arm_protector(), forehead_protector(), protector_plate(), backward_bandana() (+3 more)

### Community 1 - "Wallet"
Cohesion: 0.05
Nodes (33): 1.1 Ids and owners, 1.2 Fields, 1.3 Highlights by family, 1.4 Grades, 1.5 Outfits, 1.6 Key items and spoilers, 1.7 Gift tags, 1.8 Kits (+25 more)

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
Cohesion: 0.09
Nodes (11): drawstrings(), forearm_wraps(), holster(), hood_down(), ribbed(), shin_wraps(), side_stripe(), stripes() (+3 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (32): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+24 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.07
Nodes (14): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), kimono_sleeves(), part_line() (+6 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): spike(), burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.11
Nodes (8): arm_warmers(), frog_buttons(), mandarin_collar(), round_bun(), shin_wrap(), tabi_boots(), wave_lock(), wrap_front()

### Community 12 - ".roll"
Cohesion: 0.11
Nodes (5): Rng, Seeds, Rng, Streams, StreamsTest

### Community 13 - "items.py"
Cohesion: 0.14
Nodes (20): art_class(), catalogue_md(), check_all(), check_loot(), compile_all(), recipe_entry(), dumps(), err() (+12 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "kit_umino.py"
Cohesion: 0.10
Nodes (10): lock(), hime_locks(), wave_lock(), beard(), flicks(), brush_tail(), falling_tail(), surf() (+2 more)

### Community 17 - "solid"
Cohesion: 0.11
Nodes (10): harness(), white_fang_tanto(), cane(), scroll_tube(), herb_pouch(), muffler(), scroll(), clip() (+2 more)

### Community 18 - "cel_box"
Cohesion: 0.17
Nodes (9): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), pineapple() (+1 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "strip_fabric"
Cohesion: 0.08
Nodes (13): leg_cloth(), waist(), body(), cloth_shoes(), trouser_legs(), waist(), kimono_sleeves(), tabi() (+5 more)

### Community 21 - "strip_fabric"
Cohesion: 0.11
Nodes (10): shirt(), shirt(), decal(), hood_down(), lantern(), lantern_tag(), mantle(), plain_body() (+2 more)

### Community 22 - "Garment"
Cohesion: 0.18
Nodes (5): compatible(), Garment, key_rgba(), png_bytes(), world_bounds()

### Community 23 - "sprites.py"
Cohesion: 0.13
Nodes (21): build(), Canvas, charm(), flak_vest(), forehead_protector(), framed_ladle(), headband(), hexrgb() (+13 more)

### Community 24 - "Catalogue"
Cohesion: 0.19
Nodes (9): Catalogue, Ingredient, Item, Job, Recipe, Service, Station, Variant (+1 more)

### Community 25 - "arm_bone"
Cohesion: 0.16
Nodes (9): sode(), arm_bone(), arm_x(), kimono_sleeves(), tasuki(), armband(), cross_armband(), armband() (+1 more)

### Community 26 - ".shelf"
Cohesion: 0.14
Nodes (8): Line, Shop, Ladder, Mode, CLASSIC, VARIED, Stock, StockTest

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (13): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+5 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.06
Nodes (18): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+10 more)

### Community 32 - "outputs"
Cohesion: 0.13
Nodes (22): catalog(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans(), load_collections(), load_eye_colors() (+14 more)

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
Cohesion: 0.08
Nodes (27): Academy Supply Counter (`academy_supply`), Barbecue House (`barbecue_house`), Barber (`barber`), Bath House (`bath_house`), Bookshop (`bookshop`), Cat Shelter (`cat_shelter`), Furniture Shop (`furniture_shop`), gift (+19 more)

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "Prices"
Cohesion: 0.12
Nodes (4): Pawn, Prices, CatalogueTest, PricesTest

### Community 42 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box() (+1 more)

### Community 43 - "katana"
Cohesion: 0.18
Nodes (6): weapon, hip_katana(), katana(), back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.09
Nodes (17): 15. Pacing, BondEvent, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER (+9 more)

### Community 45 - "stamp"
Cohesion: 0.15
Nodes (7): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), bump(), plate()

### Community 46 - "Item catalogue"
Cohesion: 0.12
Nodes (16): collectible, consumable, container, curio, currency, furniture, Item catalogue, keepsake (+8 more)

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.08
Nodes (6): dark_seams(), strip_line(), Box, Layer, Piece, shade()

### Community 51 - "Face"
Cohesion: 0.09
Nodes (13): drawn_line(), glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+5 more)

### Community 52 - "ring_shell"
Cohesion: 0.11
Nodes (11): ring_shell(), crown(), clipped(), combed_back(), nape_hem(), back_crest(), crest(), pulled_back() (+3 more)

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 55 - "Person"
Cohesion: 0.07
Nodes (15): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+7 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.24
Nodes (4): bracers(), crown(), mace(), plate()

### Community 58 - ".test"
Cohesion: 0.07
Nodes (5): BondConditions, BondDialogue, BondWeb, Household, Recruitment

### Community 61 - ".classic"
Cohesion: 0.13
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 62 - "kit_suzuran.py"
Cohesion: 0.11
Nodes (9): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), sash_vials() (+1 more)

### Community 63 - "Personality"
Cohesion: 0.13
Nodes (5): 20. What the roadmap asks of bonds, 5. Personality, Personality, Reaction, ReactionTest

### Community 69 - ".of"
Cohesion: 0.15
Nodes (3): ConflictTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.12
Nodes (13): 10. Romance and family (after the beta), 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+5 more)

### Community 71 - ".read"
Cohesion: 0.19
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.12
Nodes (5): Def, Size, BIG, NOTABLE, SMALL

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (3): Deed, Know, Gossip

### Community 75 - "food"
Cohesion: 0.20
Nodes (12): cooking.oven, cooking.prep, Dango Stand (`dango_stand`), Fish Stall (`fishmonger`), food, ingredient, Market Grocer (`grocer`), dango() (+4 more)

### Community 77 - "Tier"
Cohesion: 0.22
Nodes (8): 11. Kindling Bond, Grant, Kindling, Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 78 - ".test"
Cohesion: 0.09
Nodes (3): BondEffects, Departure, Squad

### Community 80 - "Value"
Cohesion: 0.10
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (9): 18. Village scale, Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY (+1 more)

### Community 82 - "How the pieces work"
Cohesion: 0.29
Nodes (4): How the pieces work, mesh(), beak(), ears()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - ".page"
Cohesion: 0.16
Nodes (5): 12. The bond book, BondBook, Fact, MemoryLine, Page

### Community 86 - "Recipes"
Cohesion: 0.25
Nodes (8): apothecary, cooking.pot, Ninja Tool Shop (`tool_shop`), Recipes, sealing, tailoring, workbench, smoke_bomb()

### Community 88 - "kunai"
Cohesion: 0.29
Nodes (7): Exam-Week Stalls (`exam_stalls`), tool, along(), f(), kunai(), blade(), shuriken()

### Community 89 - "k"
Cohesion: 0.18
Nodes (10): collar(), flaps(), footwear(), legs(), neckline(), pouch(), roll(), stockings() (+2 more)

### Community 90 - "anime.py"
Cohesion: 0.15
Nodes (8): Shared helpers, back_fan(), bangs(), braid(), sidelocks(), blunt_fringe(), parted_fringe(), wraps()

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.11
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.15
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 95 - "rnd"
Cohesion: 0.14
Nodes (9): cel_face(), fur_edge(), ink_stains(), seal_trim(), hair_box(), hair_face(), hair_shade(), rnd() (+1 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 98 - "kit_sarutobi.py"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.15
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "kit_household.py"
Cohesion: 0.11
Nodes (9): bands(), blossom(), checks(), geta(), kasuri(), sash(), socks(), sprigs() (+1 more)

### Community 102 - "kit_shinobi.py"
Cohesion: 0.14
Nodes (6): back_crest(), bandaged_arm(), anbu_arms(), anbu_plates(), bandage(), flak_vest()

### Community 103 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 105 - "kit_uchiha.py"
Cohesion: 0.19
Nodes (6): arm_crest(), back_crest(), chest_crest(), crest(), lamellar(), police_badge()

### Community 106 - "kit_uzumaki.py"
Cohesion: 0.16
Nodes (6): bun(), crest_patch(), seal_script(), seal_tags(), waves(), wide_sleeves()

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 109 - "arm_guards"
Cohesion: 0.22
Nodes (8): gear, smithy, Weapon Shop (`weapon_shop`), arm_guards(), shin_guards(), mesh_shirt(), net(), tanto()

### Community 112 - "paint.py"
Cohesion: 0.18
Nodes (4): crescent(), band(), cloth_shade(), hem()

### Community 113 - "Experience"
Cohesion: 0.18
Nodes (9): Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR, STUDY (+1 more)

### Community 114 - "Label"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 115 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 118 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 123 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 124 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 125 - "side_panels"
Cohesion: 0.40
Nodes (3): robe_skirt(), skirt(), side_panels()

### Community 126 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 127 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

## Knowledge Gaps
- **155 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+150 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 974 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **54 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `fabric`, `belt`, `bandage_turns`, `wide_sleeves`, `sash`, `sleeve_roll`, `kit_academy.py`, `sword_strap`, `face_mask`, `kit_inuzuka.py`, `kit_kurama.py`, `kit_kunoichi.py`, `kit_senju.py`, `kit_yuhi.py`, `obi`, `wood_grain`, `kit_umino.py`, `solid`, `cel_box`, `coat_skirts`, `strip_fabric`, `wave_band`, `kit_rugged.py`, `bandolier`, `strip_fabric`, `arm_bone`, `coat_skirts`, `kit_market.py`, `kit_kinoshita.py`, `sash`, `shin_wraps`, `kit_field.py`, `high_collar`, `wrap_tie`, `kit_shiranui.py`, `Shops`, `kit_akimichi.py`, `stamp`, `Face`, `ring_shell`, `kit_hagane.py`, `kit_suzuran.py`, `kit_haruno.py`, `anime.py`, `rnd`, `kit_sarutobi.py`, `kit_household.py`, `kit_shinobi.py`, `kit_uchiha.py`, `kit_uzumaki.py`, `arm_guards`, `paint.py`, `kit_aburame.py`, `kit_yamanaka.py`, `wrap_front`, `jika_tabi`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _155 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `fabric` be split into smaller, more focused modules?**
  _Cohesion score 0.10869565217391304 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `.romance`, `Memory`, `.read`, `Story bible`, `Levels`, `ClanRelations`, `Run`, `Tier`, `Meters`, `Value`, `Mood`, `.page`, `Person`, `Conflict`, `GossipTest`, `Personality`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Wallet` be split into smaller, more focused modules?**
  _Cohesion score 0.04698581560283688 - nodes in this community are weakly interconnected._