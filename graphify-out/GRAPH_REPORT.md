# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 121 files · ~154,427 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2368 nodes · 5426 edges · 133 communities (108 shown, 25 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 529 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c6888198`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- kit_hatake.py
- mockups.py
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
- kit_aburame.py
- stamp
- kit_suzuran.py
- 7. Systems in the beta
- CreatorRules
- solid
- kit_hyuga.py
- kit_rugged.py
- kit_household.py
- kit_tobari.py
- Garment
- mesh_shirt
- glyphs.py
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
- kit_namiashi.py
- Run
- load_clans
- org.junit.jupiter.api.Test
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
- .apply
- Conflict
- kit_specialist.py
- VillageSim.java
- org.junit.jupiter.api.Test
- fabric
- Personality
- list
- World
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
- creator.py
- .test
- Character creation
- Value
- Mood
- masks.py
- 4.3 The noble clans
- leg_bone
- .page
- Peeve
- ClanRelations
- anime.py
- kit_umino.py
- preview.py
- Meter
- Title
- rnd
- 18. Village scale
- .choices
- Side quests
- 4.4 The minor clans
- Seeds
- 2. Quest framework
- Memory
- Label
- AgeStage
- Trait
- kit_sarutobi.py
- SocietyHook
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- Restyle
- NamesTest
- paint.py
- 4. Clan quest lines
- cel_box
- shade
- Json
- Rng
- kit_nara.py
- kit_shinobi.py
- Rng
- TimeAndPacingTest
- flaps
- hair_face
- bandage
- protector_plate
- shag_face
- rope_face
- bandolier
- bandage_turns
- Data

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

## Communities (133 total, 25 thin omitted)

### Community 0 - "kit_hatake.py"
Cohesion: 0.20
Nodes (4): decal(), face_mask(), shoulder_decal(), slanted_protector()

### Community 1 - "mockups.py"
Cohesion: 0.25
Nodes (22): all_screens(), body_screen(), character_image(), die(), eye_rgb(), face_screen(), font(), hair_rgb() (+14 more)

### Community 2 - "Clans"
Cohesion: 0.13
Nodes (13): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+5 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.14
Nodes (18): backdrop(), Canvas, Character, clan_renders(), composite(), cube_quads(), font(), general_renders() (+10 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.09
Nodes (11): drawstrings(), holster(), hood_down(), ribbed(), sash(), shin_wraps(), side_stripe(), sleeve_roll() (+3 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (32): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+24 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "kit_inuzuka.py"
Cohesion: 0.12
Nodes (8): burst(), claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.07
Nodes (16): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mist_swirls(), rose() (+8 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.12
Nodes (8): belt(), arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), obi(), shin_wrap(), wrap_front()

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "stamp"
Cohesion: 0.10
Nodes (11): stamp(), back_crest(), crest(), guardian_sash(), monkey(), decal(), lantern_tag(), dolphin() (+3 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "CreatorRules"
Cohesion: 0.15
Nodes (4): CreatorRules, LifeRoll, Rolled, LifeRollTest

### Community 17 - "solid"
Cohesion: 0.09
Nodes (12): mandarin_collar(), white_fang_tanto(), sash(), coat_skirts(), scarf(), trench_knife(), muffler(), sash() (+4 more)

### Community 18 - "kit_hyuga.py"
Cohesion: 0.12
Nodes (9): curtain(), tie(), back_sheet(), gathered_tail(), hair_tie(), hime_locks(), obi(), tabi() (+1 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.12
Nodes (8): dread(), knot_bun(), leg_wraps(), patch(), rope_hair(), soft_boots(), straw_sandals(), tabi()

### Community 20 - "kit_household.py"
Cohesion: 0.08
Nodes (16): bands(), checks(), collar_band(), dots(), ichimatsu(), jika_tabi(), kasuri(), overlap() (+8 more)

### Community 21 - "kit_tobari.py"
Cohesion: 0.12
Nodes (10): shirt(), vest(), shirt(), hood_down(), lantern(), mantle(), plain_body(), pleats() (+2 more)

### Community 22 - "Garment"
Cohesion: 0.27
Nodes (3): compatible(), Garment, key_rgba()

### Community 25 - "arm_bone"
Cohesion: 0.06
Nodes (23): sode(), arm_bone(), arm_x(), arm_guards(), bracers(), crown(), harness(), mace() (+15 more)

### Community 26 - "k"
Cohesion: 0.11
Nodes (13): Shared helpers, braid(), body(), collar(), footwear(), leg_ring(), legs(), neckline() (+5 more)

### Community 27 - "kit_market.py"
Cohesion: 0.06
Nodes (19): bib(), checks(), dots(), furoshiki(), geta(), jika_tabi(), kasuri(), kyahan() (+11 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "kit_morino.py"
Cohesion: 0.18
Nodes (5): back_crest(), gloves(), head_cloth(), heavy_boots(), forehead_protector()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.12
Nodes (8): blouse(), cargo(), collar(), gloves(), holster(), pocket(), strap(), tape()

### Community 32 - "outputs"
Cohesion: 0.18
Nodes (16): catalog(), hex_rgb(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes() (+8 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "kit_shiranui.py"
Cohesion: 0.15
Nodes (7): bandolier(), crest(), flicks(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

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
Cohesion: 0.14
Nodes (9): blossom(), geta(), socks(), shin_wraps(), floral_trim(), flower(), petal_fabric(), wrapped() (+1 more)

### Community 42 - "kit_akimichi.py"
Cohesion: 0.12
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box()

### Community 43 - "kit_namiashi.py"
Cohesion: 0.16
Nodes (6): back_blade(), crest(), hip_kokuto(), kokuto(), wave_band(), wave_lock()

### Community 44 - "Run"
Cohesion: 0.10
Nodes (15): BondEvent, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER, Playthrough (+7 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 46 - "org.junit.jupiter.api.Test"
Cohesion: 0.13
Nodes (4): BondDialogueTest, ConflictTest, SquadTest, AgeStageTest

### Community 47 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.11
Nodes (3): strip_line(), Box, Layer

### Community 51 - "Face"
Cohesion: 0.09
Nodes (13): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), button() (+5 more)

### Community 52 - "ring_shell"
Cohesion: 0.21
Nodes (6): ring_shell(), crown(), combed_back(), pulled_back(), combed_up(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 55 - "Person"
Cohesion: 0.07
Nodes (12): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+4 more)

### Community 57 - ".apply"
Cohesion: 0.14
Nodes (4): 10. Age stages, 13. Code, and what waits for Phase 0, Look, Result

### Community 58 - "Conflict"
Cohesion: 0.08
Nodes (8): Household, Grant, Tier, FULL, NATURE, NONE, TECHNIQUE, Recruitment

### Community 59 - "kit_specialist.py"
Cohesion: 0.25
Nodes (3): coat_skirts(), cross_armband(), scroll_tube()

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.19
Nodes (3): ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 62 - "fabric"
Cohesion: 0.11
Nodes (13): leg_cloth(), waist(), half_sleeves(), shirt(), trousers(), arm_cloth(), cloth_shoes(), kimono_sleeves() (+5 more)

### Community 63 - "Personality"
Cohesion: 0.13
Nodes (5): 20. What the roadmap asks of bonds, 5. Personality, Personality, Reaction, ReactionTest

### Community 64 - "list"
Cohesion: 0.10
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 65 - "World"
Cohesion: 0.13
Nodes (5): check(), load_rules(), story_reserved_family_names(), World, colors()

### Community 67 - "VillageScaleTest"
Cohesion: 0.19
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - ".of"
Cohesion: 0.12
Nodes (4): 8. The village talks, GossipTest, Leaf, MemoryTest

### Community 70 - "Bonds"
Cohesion: 0.08
Nodes (19): 11. Kindling Bond, 13. Data formats, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 4. Memories (+11 more)

### Community 71 - ".read"
Cohesion: 0.19
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.08
Nodes (14): Def, Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR (+6 more)

### Community 73 - "Levels"
Cohesion: 0.12
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 75 - "Squad"
Cohesion: 0.07
Nodes (4): BondDialogue, BondEffects, Departure, Squad

### Community 77 - "creator.py"
Cohesion: 0.15
Nodes (12): _hash(), hash64(), main(), _mix(), outputs(), roll_look(), roll_origin(), _rotl() (+4 more)

### Community 78 - ".test"
Cohesion: 0.10
Nodes (3): 12. The bond book, BondConditions, BondWeb

### Community 79 - "Character creation"
Cohesion: 0.11
Nodes (19): 12. Data, 14. Open questions, 1. At a glance, 1 Origin, 2. World creation first, 3 Body, 3. Where the creator sits in the opening, 4 Hair (+11 more)

### Community 80 - "Value"
Cohesion: 0.13
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - "Mood"
Cohesion: 0.15
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "masks.py"
Cohesion: 0.22
Nodes (5): How the pieces work, mesh(), tanto(), beak(), ears()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "leg_bone"
Cohesion: 0.11
Nodes (10): turned_hem(), knee_guards(), hakama_legs(), thigh_holster(), leg_bone(), gathered_ankles(), loose_legs(), rolled_cuffs() (+2 more)

### Community 85 - ".page"
Cohesion: 0.27
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Peeve"
Cohesion: 0.14
Nodes (12): Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS, LAZINESS (+4 more)

### Community 88 - "anime.py"
Cohesion: 0.18
Nodes (6): back_fan(), bangs(), lock(), sidelocks(), blunt_fringe(), parted_fringe()

### Community 89 - "kit_umino.py"
Cohesion: 0.17
Nodes (5): brush_tail(), falling_tail(), knot(), surf(), waves()

### Community 90 - "preview.py"
Cohesion: 0.17
Nodes (8): draw_player(), grown(), _label(), lineup(), render_player(), samples(), stage_scale(), stages_sheet()

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (7): Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Meters

### Community 92 - "Title"
Cohesion: 0.15
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "rnd"
Cohesion: 0.12
Nodes (9): sprigs(), clipped(), camo(), cape(), ragged(), ink_stains(), seal_trim(), cloth_shade() (+1 more)

### Community 94 - "18. Village scale"
Cohesion: 0.16
Nodes (3): 18. Village scale, House, Village

### Community 95 - ".choices"
Cohesion: 0.23
Nodes (3): Choices, Outfit, CreatorRulesTest

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.17
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.22
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "AgeStage"
Cohesion: 0.13
Nodes (5): AgeStage, ADULT, CHILD, TEEN, GrowUp

### Community 103 - "Trait"
Cohesion: 0.29
Nodes (7): Lean, Trait, BOLDNESS, DISCIPLINE, OPENNESS, PRIDE, WARMTH

### Community 104 - "kit_sarutobi.py"
Cohesion: 0.20
Nodes (5): beard(), crest(), crest_patch(), flame_hem(), pauldron()

### Community 105 - "SocietyHook"
Cohesion: 0.15
Nodes (6): 19. Society hooks, SocietyHook, Tier, BACKGROUND, CAST, KNOWN

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "Restyle"
Cohesion: 0.22
Nodes (7): Restyle, Venue, BARBER, HOME, LOCKED, TIME_SKIP, RestyleAndGrowUpTest

### Community 109 - "NamesTest"
Cohesion: 0.23
Nodes (5): 11. How residents address you, 2 Name, Names, PlayerName, NamesTest

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "cel_box"
Cohesion: 0.15
Nodes (7): cel_box(), cel_face(), topknot(), ear_panels(), round_bun(), wave_lock(), nape_hem()

### Community 117 - "kit_nara.py"
Cohesion: 0.22
Nodes (5): spike(), back_crest(), crest(), pineapple(), tuft()

### Community 118 - "kit_shinobi.py"
Cohesion: 0.20
Nodes (4): anbu_arms(), anbu_plates(), flak_vest(), sandals()

### Community 121 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 122 - "hair_face"
Cohesion: 0.29
Nodes (4): hair_box(), hair_face(), hair_shade(), shell()

### Community 123 - "bandage"
Cohesion: 0.33
Nodes (3): forearm_wraps(), bandaged_arm(), bandage()

### Community 124 - "protector_plate"
Cohesion: 0.33
Nodes (3): arm_protector(), protector_plate(), backward_bandana()

## Knowledge Gaps
- **160 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+155 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 946 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `k`, `Story bible`?**
  _High betweenness centrality (0.472) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _160 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Memory`, `.of`, `.read`, `Story bible`, `SocietyHook`, `Levels`, `Run`, `.romance`, `.test`, `Value`, `Mood`, `ClanRelations`, `Person`, `TimeAndPacingTest`, `Meter`, `18. Village scale`, `Personality`?**
  _High betweenness centrality (0.409) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13725490196078433 - nodes in this community are weakly interconnected._