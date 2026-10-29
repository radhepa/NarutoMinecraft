# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 110 files · ~146,119 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2228 nodes · 5218 edges · 171 communities (99 shown, 72 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 504 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `aae920e2`
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
- kit_shinobi.py
- kit_suzuran.py
- 7. Systems in the beta
- .person
- solid
- cel_box
- kit_rugged.py
- kit_household.py
- kit_tobari.py
- Garment
- mesh_shirt
- kit_shimura.py
- arm_bone
- fabric
- kit_market.py
- kit_kinoshita.py
- k
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
- curls_face
- kokuto
- Run
- load_clans
- .roll
- rot_matrix
- build
- Box
- chain
- kit_tsuchigumo.py
- ring_shell
- kit_gekko.py
- Act
- Person
- .bond
- kit_hagane.py
- .effectiveLevel
- kit_specialist.py
- .classic
- Kind
- Meters
- Life together
- VillageScaleTest
- Bond
- .of
- Bonds
- Squad
- Def
- Levels
- Deed
- org.junit.jupiter.api.Test
- .romance
- Playthrough.java
- .snapshot
- Face
- Value
- Mood
- masks.py
- 4.3 The noble clans
- kit_haruno.py
- .page
- Personality
- ClanRelations
- Shared helpers
- kit_umino.py
- .day
- Meter
- Title
- .name
- 18. Village scale
- ROADMAP.md
- Side quests
- 4.4 The minor clans
- GossipTest
- 2. Quest framework
- Memory
- Label
- wardrobe.py
- VillageSim.java
- SquadTest
- CourtshipTest
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- kit_nara.py
- glyphs.py
- paint.py
- 4. Clan quest lines
- Tier
- shade
- flaps
- Stage
- The village
- white_fang_tanto
- wrap_front
- .cap
- Side quest secrets
- Tier
- kit.py
- pocket
- furoshiki
- rope_hair
- shag_face
- leg_bone
- checks
- open_front
- stripes
- sashiko
- rope_face
- bandolier
- kit_sarutobi.py
- bandage_turns
- bandolier
- apothecary_sash
- hood_down
- sash
- gloves
- gourd
- lames
- quilt
- harness
- frog_clasps
- kimono_trim
- mandarin_collar
- face_mask
- sash
- mandarin_collar
- shin_wrap
- geta
- head_cloth
- arm_protector
- neckline
- coat_skirts
- scroll_tube
- lantern_tag
- muffler
- lamellar
- scroll
- clip
- hairpin
- wrap_tie
- waves

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 155 edges
3. `solid()` - 152 edges
4. `Act` - 113 edges
5. `fabric()` - 109 edges
6. `Village` - 63 edges
7. `strip_fabric()` - 59 edges
8. `Bond` - 57 edges
9. `Person` - 51 edges
10. `stamp()` - 47 edges

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

## Communities (171 total, 72 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.10
Nodes (11): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), back_crest(), decal(), dolphin() (+3 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.23
Nodes (5): arm_crest(), back_crest(), chest_crest(), crest(), police_badge()

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
Cohesion: 0.08
Nodes (12): back_crest(), drawstrings(), forearm_wraps(), holster(), ribbed(), shin_wraps(), side_stripe(), sleeve_roll() (+4 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (19): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), How to read this bible, Kindling Bond, Recurring characters, Reveal pacing (+11 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.14
Nodes (8): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw(), rnd()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.15
Nodes (6): belt(), frog_buttons(), kimono_sleeves(), obi(), round_bun(), wave_lock()

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "kit_shinobi.py"
Cohesion: 0.20
Nodes (5): forehead_protector(), protector_plate(), sandals(), wraps(), backward_bandana()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.16
Nodes (6): armband(), bell_hem(), bell_print(), bell_sprig(), sash_vials(), vial()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".person"
Cohesion: 0.10
Nodes (10): Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan, Together (+2 more)

### Community 17 - "solid"
Cohesion: 0.11
Nodes (10): snack_pouch(), obi(), coat_skirts(), cane(), herb_pouch(), sash(), shimenawa(), high_collar() (+2 more)

### Community 18 - "cel_box"
Cohesion: 0.14
Nodes (10): cel_box(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), hime_locks(), pineapple() (+2 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.08
Nodes (11): baggy_legs(), camo(), cape(), knot_bun(), leg_wraps(), patch(), ragged(), shin_guard() (+3 more)

### Community 20 - "kit_household.py"
Cohesion: 0.07
Nodes (18): bands(), checks(), collar_band(), dots(), ichimatsu(), jika_tabi(), kasuri(), overlap() (+10 more)

### Community 21 - "kit_tobari.py"
Cohesion: 0.09
Nodes (12): shirt(), vest(), anbu_plates(), flak_vest(), shirt(), hood_down(), lantern(), mantle() (+4 more)

### Community 22 - "Garment"
Cohesion: 0.24
Nodes (3): compatible(), Garment, key_rgba()

### Community 24 - "kit_shimura.py"
Cohesion: 0.29
Nodes (3): back_crest(), bandaged_arm(), bandage()

### Community 25 - "arm_bone"
Cohesion: 0.13
Nodes (10): flick(), sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), tasuki(), armband() (+2 more)

### Community 26 - "fabric"
Cohesion: 0.07
Nodes (20): leg_cloth(), waist(), body(), half_sleeves(), shirt(), trousers(), footwear(), arm_cloth() (+12 more)

### Community 27 - "kit_market.py"
Cohesion: 0.10
Nodes (10): bib(), jika_tabi(), kasuri(), kyahan(), patch(), pocket(), sash(), straw_sandals() (+2 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "k"
Cohesion: 0.07
Nodes (16): shoku_disc(), collar(), blossom(), geta(), socks(), tabi(), arm_warmers(), wrap_front() (+8 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.12
Nodes (7): blouse(), collar(), gloves(), holster(), knee_guards(), strap(), tape()

### Community 32 - "outputs"
Cohesion: 0.23
Nodes (11): catalog(), json_text(), load_characters(), load_eye_colors(), load_hair_colors(), load_marks(), load_palettes(), main() (+3 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "kit_shiranui.py"
Cohesion: 0.18
Nodes (6): crest(), flicks(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.29
Nodes (3): crest_patch(), seal_script(), seal_tags()

### Community 39 - "8. The beta, chapter by chapter"
Cohesion: 0.29
Nodes (7): 8. The beta, chapter by chapter, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Side quests in the beta, The Classic cast, The squad bonding arc

### Community 40 - "9. Delivery plan"
Cohesion: 0.29
Nodes (7): 9. Delivery plan, Beta 1: the opening and the Academy (~4 h main path), Beta 2.5: clan welcomes, wave 2 (content drop), Beta 2: Genin life (+~8 h), Beta 3: the Chunin Exams (+~3 h), Phase 0: Foundations, Playtesting

### Community 41 - "kit_yamanaka.py"
Cohesion: 0.20
Nodes (4): floral_trim(), flower(), petal_fabric(), wrapped()

### Community 42 - "curls_face"
Cohesion: 0.40
Nodes (3): puff(), curls_box(), curls_face()

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.08
Nodes (17): Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER (+9 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): load_all_groups(), load_clans(), load_collections(), load_groups(), load_population(), population_weights(), validate_clans()

### Community 46 - ".roll"
Cohesion: 0.13
Nodes (6): Conversation, Reply, Topic, LifeEvents, News, 6. Conversation

### Community 47 - "rot_matrix"
Cohesion: 0.22
Nodes (4): Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.28
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 51 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 52 - "ring_shell"
Cohesion: 0.14
Nodes (8): cel_face(), ring_shell(), crown(), clipped(), combed_back(), nape_hem(), combed_up(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.22
Nodes (4): crescent(), hip_katana(), katana(), sword_strap()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (70): Act, ABANDONED_MISSION, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED, BOND_MOMENT (+62 more)

### Community 55 - "Person"
Cohesion: 0.06
Nodes (11): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+3 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.21
Nodes (5): bracers(), crown(), mace(), plate(), shin_guards()

### Community 59 - "kit_specialist.py"
Cohesion: 0.25
Nodes (3): cross_armband(), ink_stains(), seal_trim()

### Community 61 - ".classic"
Cohesion: 0.17
Nodes (3): BondDialogueTest, ConditionsAndEffectsTest, VillageTest

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 65 - "Life together"
Cohesion: 0.15
Nodes (11): DialogueKeys, DialogueKeysTest, 10. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Data and quest hooks (+3 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.14
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.06
Nodes (3): Bond, BondConditions, FollowUp

### Community 70 - "Bonds"
Cohesion: 0.10
Nodes (16): 11. Kindling Bond, 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters (+8 more)

### Community 71 - "Squad"
Cohesion: 0.09
Nodes (5): 14. Save format and versioning, SaveFormat, Departure, Squad, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.08
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (4): 8. The village talks, Deed, Know, Gossip

### Community 79 - "Face"
Cohesion: 0.25
Nodes (4): button(), darken_rows(), rivets(), Face

### Community 80 - "Value"
Cohesion: 0.13
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - "Mood"
Cohesion: 0.14
Nodes (8): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY, Mood

### Community 82 - "masks.py"
Cohesion: 0.22
Nodes (5): How the pieces work, mesh(), tanto(), beak(), ears()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.25
Nodes (4): arm_crest(), back_crest(), chest_crest(), circle()

### Community 85 - ".page"
Cohesion: 0.18
Nodes (6): 12. The bond book, BondBook, Fact, MemoryLine, Page, BondWeb

### Community 86 - "Personality"
Cohesion: 0.08
Nodes (16): 13. Data formats, 5. Personality, Conflict, Base, Peeve, BRAGGING, COWARDICE, CRUELTY (+8 more)

### Community 88 - "Shared helpers"
Cohesion: 0.15
Nodes (9): Shared helpers, back_fan(), bangs(), braid(), curtain(), lock(), sidelocks(), blunt_fringe() (+1 more)

### Community 89 - "kit_umino.py"
Cohesion: 0.15
Nodes (6): spike(), burst(), brush_tail(), falling_tail(), surf(), waves()

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.22
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.25
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 94 - "18. Village scale"
Cohesion: 0.16
Nodes (3): 18. Village scale, House, Village

### Community 95 - "ROADMAP.md"
Cohesion: 0.33
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 96 - "Side quests"
Cohesion: 0.20
Nodes (10): 1. Scope and budget, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents, In the beta (+2 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 100 - "Memory"
Cohesion: 0.16
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "wardrobe.py"
Cohesion: 0.27
Nodes (5): hex_rgb(), png_bytes(), ramp(), rgb_hex(), _toward()

### Community 105 - "CourtshipTest"
Cohesion: 0.24
Nodes (3): 10. Romance and family (after the beta), 20. What the roadmap asks of bonds, CourtshipTest

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "kit_nara.py"
Cohesion: 0.25
Nodes (4): back_crest(), crest(), pulled_back(), tuft()

### Community 110 - "paint.py"
Cohesion: 0.12
Nodes (10): mark(), band(), cloth_shade(), grid(), hair_box(), hair_face(), hair_shade(), hem() (+2 more)

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Tier"
Cohesion: 0.29
Nodes (5): Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 115 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 117 - "Stage"
Cohesion: 0.33
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 118 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 123 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 124 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 130 - "leg_bone"
Cohesion: 0.15
Nodes (7): hakama_legs(), thigh_holster(), leg_bone(), leg_ring(), gathered_ankles(), loose_legs(), rolled_cuffs()

### Community 137 - "kit_sarutobi.py"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

## Knowledge Gaps
- **178 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+173 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 923 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **72 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `Shared helpers`, `ROADMAP.md`?**
  _High betweenness centrality (0.458) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _178 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `stamp` be split into smaller, more focused modules?**
  _Cohesion score 0.10144927536231885 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Memory`, `Squad`, `CourtshipTest`, `Deed`, `.romance`, `.person`, `Value`, `Mood`, `.page`, `Personality`, `ClanRelations`, `Person`, `.cap`, `Meters`, `18. Village scale`, `ROADMAP.md`?**
  _High betweenness centrality (0.451) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.13071895424836602 - nodes in this community are weakly interconnected._