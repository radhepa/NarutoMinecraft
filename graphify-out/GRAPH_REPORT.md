# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 132 files · ~466,598 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2549 nodes · 6077 edges · 182 communities (115 shown, 67 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 596 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b7ba3dc4`
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
- .person
- solid
- cel_box
- kit_rugged.py
- kit_household.py
- kit_tobari.py
- Garment
- mesh_shirt
- bandage
- arm_bone
- strip_fabric
- kit_market.py
- kit_kinoshita.py
- k
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
- dialogue.py
- .talk
- rot_matrix
- build
- Box
- chain
- kit_tsuchigumo.py
- ring_shell
- kit_gekko.py
- Act
- Stage
- kit_hagane.py
- BondWorld
- kit_specialist.py
- .classic
- Kind
- Meters
- list
- Life together
- VillageScaleTest
- Bond
- org.junit.jupiter.api.Test
- Bonds
- .read
- Def
- Levels
- Deed
- Context
- .romance
- Playthrough.java
- .test
- Face
- Value
- Mood
- kit_shinobi.py
- 4.3 The noble clans
- kit_haruno.py
- .page
- Personality
- ClanRelations
- Shared helpers
- kit_umino.py
- Heard
- Meter
- Title
- Fixture
- 18. Village scale
- Side quests
- 4.4 The minor clans
- .of
- 2. Quest framework
- Memory
- Label
- compose.py
- VillageSim.java
- .load
- CourtshipTest
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- kit_nara.py
- Squad
- paint.py
- 4. Clan quest lines
- Tier
- shade
- flaps
- Stage
- The village
- BetaTalk
- wrap_front
- Question
- Side quest secrets
- Tier
- Bank
- Dialogue
- Person
- Json
- Recruitment
- main
- Schedule
- Writing dialogue for the Leaf
- .optional
- Mood
- SocietyHook
- kit_sarutobi.py
- jika_tabi
- bandolier
- apothecary_sash
- Conditions
- gloves
- hood_down
- Names
- Names
- Outcome
- Tokens
- belt
- Kind
- face_mask
- sash
- Naruto Minecraft
- wide_sleeves
- Error
- forehead_protector
- sleeve_roll
- sword_strap
- arm_cloth
- bands
- blossom
- checks
- cloth_shoes
- dots
- geta
- hairpin
- ichimatsu
- waves
- kasuri
- overlap
- stripes
- topknot
- coat_skirts
- wave_band
- pauldron
- scarf
- bell_charm
- bun

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `BondWorld` - 155 edges
3. `solid()` - 152 edges
4. `Act` - 113 edges
5. `fabric()` - 109 edges
6. `Village` - 63 edges
7. `strip_fabric()` - 59 edges
8. `Bond` - 57 edges
9. `stamp()` - 47 edges
10. `Person` - 46 edges

## Surprising Connections (you probably didn't know these)
- `15. Pacing` --references--> `TimeAndPacingTest`  [INFERRED]
  BONDS.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `8. Pacing with time together` --references--> `TimeAndPacingTest`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/test/java/dev/shinobi/life/bond/TimeAndPacingTest.java
- `Shared helpers` --references--> `wraps()`  [INFERRED]
  CLANS.md → tools/wardrobe/kit_shinobi.py
- `Collections: the general wardrobe` --references--> `general_resident()`  [INFERRED]
  CLANS.md → tools/wardrobe/wardrobe.py
- `Life together` --references--> `Activity`  [INFERRED]
  LIFE_TOGETHER.md → life/bonds/src/main/java/dev/shinobi/life/bond/Activity.java

## Import Cycles
- None detected.

## Communities (182 total, 67 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.13
Nodes (8): stamp(), decal(), shoulder_decal(), slanted_protector(), crest(), wave_band(), bump(), plate()

### Community 1 - "kit_uchiha.py"
Cohesion: 0.16
Nodes (7): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), lamellar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.17
Nodes (12): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Population, Reference images, The clan file (+4 more)

### Community 3 - "kit_senju.py"
Cohesion: 0.18
Nodes (5): bun(), lames(), plate(), shoulder_guards(), side_panels()

### Community 4 - "render.py"
Cohesion: 0.16
Nodes (14): backdrop(), Canvas, Character, composite(), cube_quads(), font(), ground_shadow(), hair_chart() (+6 more)

### Community 5 - "living_eyes.py"
Cohesion: 0.16
Nodes (21): blend(), blush(), brow(), brow_top(), eye_top(), fit(), hex_rgb(), lash() (+13 more)

### Community 6 - "kit_academy.py"
Cohesion: 0.09
Nodes (11): drawstrings(), holster(), hood_down(), ribbed(), sash(), shin_wraps(), side_stripe(), stripes() (+3 more)

### Community 7 - "Story bible"
Cohesion: 0.11
Nodes (18): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Kindling Bond, Recurring characters, Reveal pacing, Spoilers behind the roadmap's neutral wording (+10 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.10
Nodes (12): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw(), hair_box() (+4 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.10
Nodes (12): bandage_turns(), mist_swirls(), rose(), thorn_band(), thorn_vine(), thorn_wrap(), wave_box(), wave_curtain() (+4 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.10
Nodes (9): arm_warmers(), frog_buttons(), kimono_sleeves(), mandarin_collar(), round_bun(), shin_wrap(), tabi_boots(), wave_lock() (+1 more)

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "fabric"
Cohesion: 0.12
Nodes (9): back_crest(), crest(), back_crest(), arm_protector(), protector_plate(), backward_bandana(), dolphin(), beak() (+1 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.16
Nodes (6): back_crest(), bell_hem(), bell_print(), bell_sprig(), sash_vials(), vial()

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - ".person"
Cohesion: 0.10
Nodes (10): Activity, BondEvent, Answer, Highlight, Invitation, Outcome, Plan, Together (+2 more)

### Community 17 - "solid"
Cohesion: 0.10
Nodes (11): harness(), white_fang_tanto(), obi(), trench_knife(), cane(), herb_pouch(), scroll(), clip() (+3 more)

### Community 18 - "cel_box"
Cohesion: 0.17
Nodes (9): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), pineapple() (+1 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "kit_household.py"
Cohesion: 0.22
Nodes (5): collar_band(), socks(), sprigs(), trouser_legs(), waist()

### Community 21 - "kit_tobari.py"
Cohesion: 0.12
Nodes (9): vest(), decal(), lantern(), lantern_tag(), muffler(), plain_body(), sash(), shin_wraps() (+1 more)

### Community 22 - "Garment"
Cohesion: 0.23
Nodes (3): Garment, key_rgba(), png_bytes()

### Community 24 - "bandage"
Cohesion: 0.33
Nodes (3): forearm_wraps(), bandaged_arm(), bandage()

### Community 25 - "arm_bone"
Cohesion: 0.11
Nodes (13): sode(), arm_bone(), arm_x(), arm_guards(), bracers(), kimono_sleeves(), kimono_sleeves(), tasuki() (+5 more)

### Community 26 - "strip_fabric"
Cohesion: 0.11
Nodes (9): leg_cloth(), shirt(), waist(), body(), tabi(), gloves(), sleeves(), split_toe_boots() (+1 more)

### Community 27 - "kit_market.py"
Cohesion: 0.05
Nodes (23): bib(), checks(), dots(), furoshiki(), gathered_ankles(), geta(), jika_tabi(), kasuri() (+15 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "k"
Cohesion: 0.18
Nodes (10): collar(), flaps(), footwear(), legs(), neckline(), pouch(), roll(), stockings() (+2 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.17
Nodes (12): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Conditions and actions, Principles, Ranks and milestones, Rotating story roles (+4 more)

### Community 31 - "kit_field.py"
Cohesion: 0.05
Nodes (20): blouse(), cargo(), collar(), gloves(), half_sleeves(), holster(), knee_guards(), pocket() (+12 more)

### Community 32 - "wardrobe.py"
Cohesion: 0.09
Nodes (28): catalog(), clan_bottoms(), clan_resident(), compatible(), general_pool(), general_resident(), hex_rgb(), json_text() (+20 more)

### Community 33 - "11. Later systems"
Cohesion: 0.18
Nodes (11): 11. Later systems, Clan techniques and kekkei genkai, Elemental natures, Homes after the beta, Kindling Bond, Later techniques and combat, Player clans, Ranks after Chunin (+3 more)

### Community 34 - "Shinobi Modpack: roadmap"
Cohesion: 0.22
Nodes (9): 10. Story bible, 12. Risks and open questions, 1. Vision, 3. Where we start, Contents, Risks, Shinobi Modpack: roadmap, Still open (+1 more)

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

### Community 42 - "kit_akimichi.py"
Cohesion: 0.11
Nodes (9): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box() (+1 more)

### Community 43 - "kokuto"
Cohesion: 0.33
Nodes (3): back_blade(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.08
Nodes (17): Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS, GENIN, LATER (+9 more)

### Community 45 - "dialogue.py"
Cohesion: 0.13
Nodes (34): assign_ids(), build(), check_condition(), check_text(), compiled(), compiled_question(), content_key(), coverage() (+26 more)

### Community 46 - ".talk"
Cohesion: 0.33
Nodes (4): Conversation, Reply, Topic, 6. Conversation

### Community 47 - "rot_matrix"
Cohesion: 0.18
Nodes (5): wave_lock(), Piece, piece_corners(), rot_matrix(), world_bounds()

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.12
Nodes (3): strip_line(), Box, Layer

### Community 51 - "kit_tsuchigumo.py"
Cohesion: 0.14
Nodes (7): glyph(), shimenawa(), spider_crest(), thread_spool(), threads(), web(), web_hem()

### Community 52 - "ring_shell"
Cohesion: 0.14
Nodes (8): cel_face(), ring_shell(), crown(), clipped(), combed_back(), nape_hem(), combed_up(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (70): Act, ABANDONED_MISSION, APOLOGIZED, ASKED_ADVICE, ASKED_AFTER_THEM, AWKWARD_HANGOUT, BIRTHDAY_REMEMBERED, BOND_MOMENT (+62 more)

### Community 55 - "Stage"
Cohesion: 0.14
Nodes (9): Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED, NONE (+1 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.29
Nodes (3): spike(), crown(), burst()

### Community 58 - "BondWorld"
Cohesion: 0.08
Nodes (3): BondDialogue, BondWorld, Household

### Community 59 - "kit_specialist.py"
Cohesion: 0.13
Nodes (7): bandolier(), coat_skirts(), ink_stains(), scroll_tube(), seal_trim(), shirt(), strap()

### Community 61 - ".classic"
Cohesion: 0.18
Nodes (3): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest

### Community 62 - "Kind"
Cohesion: 0.11
Nodes (17): Kind, DREAM_SETBACK, DREAM_STEP, FAMILY_LOSS, FRIEND_QUARREL, HEARTBREAK, INJURED, MOVING (+9 more)

### Community 65 - "Life together"
Cohesion: 0.25
Nodes (8): 10. Open questions, 1. What makes a relationship feel real, 2. Schedules, 4. Their lives, 5. Following up, 7. Data and quest hooks, 8. Pacing with time together, Life together

### Community 67 - "VillageScaleTest"
Cohesion: 0.14
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 68 - "Bond"
Cohesion: 0.06
Nodes (4): Bond, LifeEvents, News, FollowUp

### Community 69 - "org.junit.jupiter.api.Test"
Cohesion: 0.13
Nodes (3): ConflictTest, MemoryTest, SquadTest

### Community 70 - "Bonds"
Cohesion: 0.07
Nodes (23): 11. Kindling Bond, 13. Data formats, 15. Pacing, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 19. Society hooks, 1. The data model, 21. Open questions (+15 more)

### Community 71 - ".read"
Cohesion: 0.23
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (15): Def, Experience, CAMP, DATE, FESTIVAL, HANGOUT, MEAL, MISSION (+7 more)

### Community 73 - "Levels"
Cohesion: 0.16
Nodes (3): 3. Levels and story gates, Levels, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 75 - "Context"
Cohesion: 0.13
Nodes (8): Context, Facet, Said, Talk, Why, BUDGET, EXHAUSTED, NONE

### Community 78 - ".test"
Cohesion: 0.06
Nodes (4): 12. The bond book, BondConditions, BondEffects, BondWeb

### Community 79 - "Face"
Cohesion: 0.20
Nodes (6): drawn_line(), button(), darken_rows(), line(), rivets(), Face

### Community 80 - "Value"
Cohesion: 0.12
Nodes (12): ClanProfile, Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY (+4 more)

### Community 81 - "Mood"
Cohesion: 0.25
Nodes (7): Label, CALM, FESTIVE, GRIEVING, PROUD, TENSE, UNEASY

### Community 82 - "kit_shinobi.py"
Cohesion: 0.12
Nodes (9): How the pieces work, anbu_arms(), anbu_plates(), flak_vest(), mesh(), sandals(), tanto(), wraps() (+1 more)

### Community 83 - "4.3 The noble clans"
Cohesion: 0.12
Nodes (16): 4.3 The noble clans, Aburame, Akimichi, Gekko, Hatake, Hyuga, Inuzuka, Kurama (+8 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - ".page"
Cohesion: 0.25
Nodes (4): BondBook, Fact, MemoryLine, Page

### Community 86 - "Personality"
Cohesion: 0.08
Nodes (15): 20. What the roadmap asks of bonds, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY, LATENESS (+7 more)

### Community 88 - "Shared helpers"
Cohesion: 0.11
Nodes (11): Shared helpers, back_fan(), bangs(), braid(), lock(), sidelocks(), blunt_fringe(), hime_locks() (+3 more)

### Community 89 - "kit_umino.py"
Cohesion: 0.20
Nodes (4): brush_tail(), falling_tail(), surf(), waves()

### Community 90 - "Heard"
Cohesion: 0.09
Nodes (6): 4. Storage, Heard, Speaker, Line, Turn, Overheard

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.16
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - "Fixture"
Cohesion: 0.19
Nodes (3): Fixture, QuestionsAndLedgerTest, TalkTest

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
Cohesion: 0.20
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.18
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "compose.py"
Cohesion: 0.33
Nodes (5): compose(), flush_kernel(), flush_template(), fail(), main()

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
Cohesion: 0.18
Nodes (4): back_crest(), band(), cloth_shade(), hem()

### Community 112 - "4. Clan quest lines"
Cohesion: 0.50
Nodes (4): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.5 Clan quest counts, 4. Clan quest lines

### Community 113 - "Tier"
Cohesion: 0.33
Nodes (5): Tier, FULL, NATURE, NONE, TECHNIQUE

### Community 115 - "flaps"
Cohesion: 0.40
Nodes (3): robe_skirt(), skirt(), side_panels()

### Community 117 - "Stage"
Cohesion: 0.33
Nodes (4): Stage, ADULT, CHILD, TEEN

### Community 118 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 119 - "BetaTalk"
Cohesion: 0.23
Nodes (4): BetaTalk, Person, Player, World

### Community 122 - "Question"
Cohesion: 0.21
Nodes (4): 8. Questions and choices, Answer, Question, Answered

### Community 123 - "Side quest secrets"
Cohesion: 0.50
Nodes (4): Clan lines, District quests and one-offs, Filler arcs, Side quest secrets

### Community 124 - "Tier"
Cohesion: 0.29
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

### Community 125 - "Bank"
Cohesion: 0.17
Nodes (4): Bank, Pacing, Rules, Tier

### Community 126 - "Dialogue"
Cohesion: 0.17
Nodes (12): 10. Pool sizing, 11. Simulation, 12. Story-gated pools, 13. What waits, 14. Open questions, 1. Freshness: never repeat, 2. Talk budgets, 3. Beyond the budget (+4 more)

### Community 131 - "main"
Cohesion: 0.25
Nodes (4): clan_renders(), general_renders(), main(), village_renders()

### Community 133 - "Writing dialogue for the Leaf"
Cohesion: 0.25
Nodes (8): Context tags, Functions, Questions, Rules the compiler enforces, Style, The format, Voices, Writing dialogue for the Leaf

### Community 134 - ".optional"
Cohesion: 0.38
Nodes (4): 9. Mass production, The bank today, DialogueKeys, 9. Content plan

### Community 137 - "kit_sarutobi.py"
Cohesion: 0.22
Nodes (5): crest(), crest_patch(), flame_hem(), guardian_sash(), monkey()

### Community 138 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 141 - "Conditions"
Cohesion: 0.33
Nodes (3): 5. Selection: the most specific line wins, Conditions, Conditions

### Community 146 - "hood_down"
Cohesion: 0.33
Nodes (3): hood_down(), mantle(), pleats()

### Community 149 - "Outcome"
Cohesion: 0.33
Nodes (6): Outcome, AGAIN, CLOSE, FRESH, NONE, REPEAT

### Community 152 - "Kind"
Cohesion: 0.50
Nodes (4): Kind, CYCLE, LINE, REPEAT

### Community 155 - "Naruto Minecraft"
Cohesion: 0.67
Nodes (3): Commits, graphify, Naruto Minecraft

## Knowledge Gaps
- **189 isolated node(s):** `TALK`, `GIFT_LOVED`, `GIFT_LIKED`, `GIFT_PLAIN`, `GIFT_DISLIKED` (+184 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 992 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **67 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Clans` connect `Clans` to `Shared helpers`, `wardrobe.py`, `ROADMAP.md`?**
  _High betweenness centrality (0.186) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `TALK`, `GIFT_LOVED`, `GIFT_LIKED` to the rest of the system?**
  _189 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `stamp` be split into smaller, more focused modules?**
  _Cohesion score 0.12987012987012986 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `.of`, `Memory`, `.read`, `Mood`, `CourtshipTest`, `Levels`, `SocietyHook`, `.romance`, `.test`, `.person`, `Value`, `Personality`, `ClanRelations`, `Meters`, `ROADMAP.md`?**
  _High betweenness centrality (0.183) - this node is a cross-community bridge._
- **Should `kit_academy.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09090909090909091 - nodes in this community are weakly interconnected._
- **Why does `Shared helpers` connect `Shared helpers` to `Clans`, `fabric`, `paint.py`, `solid`, `cel_box`, `kit_shinobi.py`, `ring_shell`, `belt`, `bandage`, `kit_hagane.py`, `strip_fabric`, `k`, `forehead_protector`, `kit_field.py`?**
  _High betweenness centrality (0.177) - this node is a cross-community bridge._