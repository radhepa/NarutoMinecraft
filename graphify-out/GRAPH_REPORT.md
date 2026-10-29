# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 145 files · ~173,265 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2703 nodes · 6412 edges · 176 communities (110 shown, 66 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 642 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5e5b4d15`
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
- kit_specialist.py
- kit_suzuran.py
- 7. Systems in the beta
- .person
- k
- cel_box
- kit_rugged.py
- jika_tabi
- kit_tobari.py
- Garment
- mesh_shirt
- kit_shimura.py
- arm_bone
- strip_fabric
- kit_market.py
- kit_kinoshita.py
- kit.py
- 5. Data formats built for the whole story
- kit_field.py
- wardrobe.py
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
- Pantry
- News
- org.junit.jupiter.api.Test
- build
- Box
- chain
- kit_tsuchigumo.py
- ring_shell
- kit_gekko.py
- Act
- Stage
- BondWorld
- kit_hagane.py
- .test
- rnd
- map
- org.junit.jupiter.api.Test
- Kind
- .answer
- Squad
- VillageScaleTest
- Bond
- .of
- Bonds
- .read
- Def
- Levels
- Deed
- .romance
- AnswerTag
- Home
- Face
- Value
- Mood
- masks.py
- 4.3 The noble clans
- kit_haruno.py
- .page
- Personality
- ClanRelations
- kit_umino.py
- Category
- .day
- Meter
- Title
- .name
- Village
- .of
- Side quests
- 4.4 The minor clans
- Person
- 2. Quest framework
- Meters
- Label
- .daily
- Mood
- Kind
- CourtshipTest
- 7. Inter-clan politics as quests
- Conflict
- kit_nara.py
- kit_household.py
- hair_face
- .talk
- Tier
- Home
- flaps
- Stage
- VisitsTest
- Shared helpers
- bangs
- Flat
- QuestionsTest
- Playthrough.java
- FirstFifteenHours.java
- .person
- Memory
- rope_hair
- shag_face
- Keepsake
- .run
- Tier
- Tier
- checks
- cloth_shoes
- solid
- kit_sarutobi.py
- kit_hatake.py
- .endDay
- 8. Beta catalogue
- geta
- ichimatsu
- 4. Clan quest lines
- belt
- topknot
- fur_face
- rope_face
- coat_skirts
- bandolier
- bandage_turns
- holster
- sash
- turned_hem
- mandarin_collar
- white_fang_tanto
- arm_cloth
- stripes
- obi
- wrap_front
- shin_wrap
- back_crest
- head_cloth
- arm_protector
- scroll_tube
- apothecary_sash
- gloves
- herb_pouch
- scroll
- wrap_tie
- waves
- rose

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 179 edges
3. `solid()` - 152 edges
4. `Act` - 123 edges
5. `fabric()` - 109 edges
6. `Home` - 65 edges
7. `Village` - 63 edges
8. `Bond` - 62 edges
9. `strip_fabric()` - 59 edges
10. `Person` - 55 edges

## Surprising Connections (you probably didn't know these)
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `7. Questions and choices` --references--> `Question`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Question.java
- `Code by mod` --references--> `render()`  [INFERRED]
  ROADMAP.md → tools/wardrobe/render.py
- `Life together` --references--> `Activity`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Activity.java
- `Bonds` --references--> `BondEvent`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/BondEvent.java

## Import Cycles
- None detected.

## Communities (176 total, 66 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.14
Nodes (8): stamp(), crest(), crest(), back_crest(), dolphin(), wave_band(), bump(), plate()

### Community 1 - "kit_uchiha.py"
Cohesion: 0.19
Nodes (6): arm_crest(), back_crest(), chest_crest(), crest(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.15
Nodes (12): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+4 more)

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
Cohesion: 0.09
Nodes (11): back_crest(), drawstrings(), forearm_wraps(), hood_down(), ribbed(), shin_wraps(), side_stripe(), sleeve_roll() (+3 more)

### Community 7 - "Story bible"
Cohesion: 0.06
Nodes (32): Commits, graphify, Naruto Minecraft, Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines (+24 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.10
Nodes (10): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), part_line(), side_fringe(), stamp() (+2 more)

### Community 9 - "rnd"
Cohesion: 0.12
Nodes (8): spike(), crown(), burst(), claw_marks(), fang(), fang_small(), paw(), pineapple()

### Community 10 - "kit_yuhi.py"
Cohesion: 0.13
Nodes (9): mist_swirls(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan(), wave_lock() (+1 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 14 - "kit_suzuran.py"
Cohesion: 0.20
Nodes (5): bell_hem(), bell_print(), bell_sprig(), sash_vials(), vial()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".person"
Cohesion: 0.10
Nodes (8): Activity, BondEvent, Answer, Invitation, Plan, Together, TogetherTest, 3. Hangouts

### Community 17 - "k"
Cohesion: 0.07
Nodes (15): sword_strap(), frog_clasps(), kimono_trim(), kyahan(), tabi(), wrap_front(), wave_band(), neckline() (+7 more)

### Community 18 - "cel_box"
Cohesion: 0.14
Nodes (10): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), round_bun() (+2 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.08
Nodes (11): baggy_legs(), camo(), cape(), knot_bun(), leg_wraps(), patch(), ragged(), shin_guard() (+3 more)

### Community 20 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 21 - "kit_tobari.py"
Cohesion: 0.07
Nodes (16): shirt(), vest(), pouch(), anbu_plates(), decal(), hood_down(), lantern(), lantern_tag() (+8 more)

### Community 22 - "Garment"
Cohesion: 0.13
Nodes (7): compatible(), Garment, key_rgba(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 24 - "kit_shimura.py"
Cohesion: 0.29
Nodes (3): back_crest(), bandaged_arm(), bandage()

### Community 25 - "arm_bone"
Cohesion: 0.12
Nodes (12): sode(), arm_bone(), arm_x(), arm_guards(), wide_sleeves(), kimono_sleeves(), kimono_sleeves(), tasuki() (+4 more)

### Community 26 - "strip_fabric"
Cohesion: 0.11
Nodes (10): leg_cloth(), waist(), trouser_legs(), waist(), tabi(), arm_warmers(), gloves(), anbu_arms() (+2 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.12
Nodes (12): back_crest(), chisel(), crest(), mallet(), nail_pouch(), pencil(), _piece(), sashiko() (+4 more)

### Community 29 - "kit.py"
Cohesion: 0.17
Nodes (8): body(), collar(), footwear(), kimono_sleeves(), legs(), sleeves(), waistband(), fabric()

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.15
Nodes (13): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Names rolled per save, Principles, Ranks and milestones (+5 more)

### Community 31 - "kit_field.py"
Cohesion: 0.07
Nodes (17): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+9 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.11
Nodes (24): catalog(), general_pool(), hex_rgb(), json_text(), load_all_groups(), load_characters(), load_clans(), load_collections() (+16 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.20
Nodes (10): 10. Story bible, 12. Risks and open questions, 1. Vision, 2. Decisions, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap (+2 more)

### Community 35 - "kit_shiranui.py"
Cohesion: 0.14
Nodes (8): forehead_protector(), protector_plate(), backward_bandana(), crest(), mouth_senbon(), senbon(), thigh_holster(), wrist_holster()

### Community 36 - "4. Technical architecture"
Cohesion: 0.22
Nodes (9): 4. Technical architecture, Code by mod, Each mod on its own, Multiplayer (later), Regions, Repository layout, Saves, The pack: separate mods (+1 more)

### Community 37 - "6. The map"
Cohesion: 0.25
Nodes (8): 6. The map, Clan quarters, District schedule, How the map is made, Pasted or built by hand, Population, References, Scale and border

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.24
Nodes (4): crest_patch(), seal_script(), seal_tags(), wide_sleeves()

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
Cohesion: 0.24
Nodes (4): back_blade(), hip_kokuto(), kokuto(), wave_lock()

### Community 44 - "Run"
Cohesion: 0.05
Nodes (30): 15. Pacing, 5. Personality, DialogueKeys, Rng, DialogueKeysTest, Chapter, Phase, ACADEMY (+22 more)

### Community 45 - "Pantry"
Cohesion: 0.05
Nodes (28): 18. The engine, FurnitureSet, HomeHangout, Kind, CLAN_SUMMONS, GIFT, INVITATION, LANDLADY (+20 more)

### Community 47 - "org.junit.jupiter.api.Test"
Cohesion: 0.09
Nodes (7): 19. Pacing, SquadTest, CatalogTest, LivingTest, MoveTest, RentTest, FirstFifteenHoursTest

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.10
Nodes (5): band(), hem(), strip_line(), Box, Layer

### Community 51 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (8): drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem(), line()

### Community 52 - "ring_shell"
Cohesion: 0.15
Nodes (8): ring_shell(), crown(), clipped(), combed_back(), nape_hem(), pulled_back(), combed_up(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.22
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (73): Act, ABANDONED_MISSION, ANSWERED, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED (+65 more)

### Community 55 - "Stage"
Cohesion: 0.14
Nodes (9): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+1 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.27
Nodes (4): bracers(), mace(), plate(), shin_guards()

### Community 58 - ".test"
Cohesion: 0.08
Nodes (4): BondConditions, BondWeb, Recruitment, Standing

### Community 59 - "rnd"
Cohesion: 0.12
Nodes (9): sprigs(), fur_edge(), ink_clouds(), splatter(), wisteria_hem(), ink_stains(), seal_trim(), cloth_shade() (+1 more)

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.09
Nodes (6): 8. The village talks, BondDialogueTest, ConditionsAndEffectsTest, GossipTest, KindlingAndBookTest, VillageTest

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 63 - ".answer"
Cohesion: 0.23
Nodes (3): Answered, Outcome, Questions

### Community 65 - "Squad"
Cohesion: 0.07
Nodes (3): BondEffects, Departure, Squad

### Community 67 - "VillageScaleTest"
Cohesion: 0.12
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.07
Nodes (4): Bond, FollowUp, Highlight, Outcome

### Community 70 - "Bonds"
Cohesion: 0.10
Nodes (17): 11. Kindling Bond, 12. The bond book, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions, 2. The meters (+9 more)

### Community 71 - ".read"
Cohesion: 0.23
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 74 - "Deed"
Cohesion: 0.11
Nodes (3): Deed, Know, Gossip

### Community 77 - "AnswerTag"
Cohesion: 0.09
Nodes (19): AnswerTag, AMBITIOUS, BLUNT, BOLD, CAUTIOUS, CURIOUS, DUTIFUL, EVASIVE (+11 more)

### Community 78 - "Home"
Cohesion: 0.09
Nodes (6): Home, Tidiness, LIVED_IN, MESSY, TIDY, Photo

### Community 79 - "Face"
Cohesion: 0.16
Nodes (7): button(), curls_face(), dark_seams(), darken_rows(), rivets(), Face, shade()

### Community 80 - "Value"
Cohesion: 0.12
Nodes (13): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+5 more)

### Community 81 - "Mood"
Cohesion: 0.22
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - "masks.py"
Cohesion: 0.18
Nodes (6): How the pieces work, flak_vest(), mesh(), tanto(), beak(), ears()

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.25
Nodes (4): arm_crest(), back_crest(), chest_crest(), circle()

### Community 85 - ".page"
Cohesion: 0.38
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Personality"
Cohesion: 0.08
Nodes (15): 20. What the roadmap asks of bonds, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS (+7 more)

### Community 88 - "kit_umino.py"
Cohesion: 0.12
Nodes (8): lock(), hime_locks(), beard(), flicks(), brush_tail(), falling_tail(), surf(), waves()

### Community 89 - "Category"
Cohesion: 0.07
Nodes (27): Catalog, Category, BATH, BED, DECOR, DISPLAY, FIXTURE, FLOOR (+19 more)

### Community 91 - "Meter"
Cohesion: 0.12
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.22
Nodes (7): Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.22
Nodes (6): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE

### Community 95 - ".of"
Cohesion: 0.11
Nodes (7): Score, Practice, Session, Rest, Rested, ComfortTest, RestTest

### Community 96 - "Side quests"
Cohesion: 0.20
Nodes (10): 1. Scope and budget, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents, In the beta (+2 more)

### Community 97 - "4.4 The minor clans"
Cohesion: 0.18
Nodes (11): 4.4 The minor clans, Hagane, Haruno, Kinoshita, Morino, Namiashi, Shiranui, Suzuran (+3 more)

### Community 99 - "2. Quest framework"
Cohesion: 0.20
Nodes (10): 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards, 2.7 Pacing, 2.8 Classic and Varied (+2 more)

### Community 101 - "Label"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - ".daily"
Cohesion: 0.15
Nodes (4): Friends, Day, Visit, Visits

### Community 104 - "Kind"
Cohesion: 0.20
Nodes (8): Kind, ADVICE, CONFESSION, DILEMMA, OPINION, PLAYER_PAST, PLAYER_PLANS, PREFERENCE

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 108 - "kit_nara.py"
Cohesion: 0.33
Nodes (3): back_crest(), crest(), tuft()

### Community 109 - "kit_household.py"
Cohesion: 0.11
Nodes (9): bands(), blossom(), collar_band(), dots(), kasuri(), overlap(), sash(), socks() (+1 more)

### Community 110 - "hair_face"
Cohesion: 0.27
Nodes (4): hair_box(), hair_face(), hair_shade(), shell()

### Community 112 - ".talk"
Cohesion: 0.39
Nodes (4): Conversation, Reply, Topic, 6. Conversation

### Community 113 - "Tier"
Cohesion: 0.29
Nodes (5): Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 114 - "Home"
Cohesion: 0.08
Nodes (25): 10. The training corner, 11. Money, 12. Growing up: homes by era, 13. Multiplayer, 14. The story at home, 15. Furniture, 16. Keepsakes, 1. Design rules (+17 more)

### Community 115 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 117 - "Stage"
Cohesion: 0.33
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 118 - "VisitsTest"
Cohesion: 0.18
Nodes (3): Cast, Setup, VisitsTest

### Community 119 - "Shared helpers"
Cohesion: 0.20
Nodes (6): Shared helpers, back_fan(), braid(), cel_face(), sidelocks(), wraps()

### Community 121 - "bangs"
Cohesion: 0.33
Nodes (3): bangs(), blunt_fringe(), parted_fringe()

### Community 122 - "Flat"
Cohesion: 0.10
Nodes (8): 17. What the map needs, 2. The flat, The Classic flat: `flat.leaf_block.3a`, Varied candidates, Flat, Room, Due, Rent

### Community 127 - "Memory"
Cohesion: 0.20
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 130 - "Keepsake"
Cohesion: 0.17
Nodes (7): Keepsake, Kind, CLAN, FESTIVAL, GIFT, QUEST, STORY

### Community 131 - ".run"
Cohesion: 0.32
Nodes (4): FirstFifteenHours, Result, Slice, Snapshot

### Community 132 - "Tier"
Cohesion: 0.22
Nodes (6): Tier, BARE, BELOVED, COMFORTABLE, COSY, HOMELY

### Community 133 - "Tier"
Cohesion: 0.25
Nodes (6): Tier, ACADEMY_FLAT, CLAN_ESTATE, HOKAGE_QUARTERS, HOUSE, TWO_ROOM_FLAT

### Community 136 - "solid"
Cohesion: 0.12
Nodes (9): harness(), face_mask(), mandarin_collar(), cane(), shimenawa(), high_collar(), hairpin(), strap() (+1 more)

### Community 137 - "kit_sarutobi.py"
Cohesion: 0.13
Nodes (8): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey(), pauldron(), scarf(), trench_knife()

### Community 138 - "kit_hatake.py"
Cohesion: 0.25
Nodes (3): decal(), shoulder_decal(), slanted_protector()

### Community 139 - ".endDay"
Cohesion: 0.29
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 140 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 143 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

## Knowledge Gaps
- **261 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+256 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1079 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **66 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `Shared helpers`, `Story bible`?**
  _High betweenness centrality (0.405) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _261 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `stamp` be split into smaller, more focused modules?**
  _Cohesion score 0.14166666666666666 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `Person`, `Meters`, `.read`, `Story bible`, `CourtshipTest`, `Mood`, `Conflict`, `Run`, `.romance`, `.person`, `Value`, `Personality`, `ClanRelations`, `org.junit.jupiter.api.Test`, `Memory`?**
  _High betweenness centrality (0.361) - this node is a cross-community bridge._
- **Should `render.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `Clans`, `kit_shiranui.py`, `solid`, `rnd`, `k`, `cel_box`, `belt`, `ring_shell`, `flaps`, `kit_tobari.py`, `masks.py`, `kit_umino.py`, `bangs`, `strip_fabric`, `Box`, `kit.py`, `kit_shimura.py`, `kit_field.py`?**
  _High betweenness centrality (0.337) - this node is a cross-community bridge._