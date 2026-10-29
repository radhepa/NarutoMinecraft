# Graph Report - NarutoMinecraft  (2026-10-29)

## Corpus Check
- 153 files · ~218,780 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .properties 2, .jar 1)

## Summary
- 2817 nodes · 6434 edges · 166 communities (111 shown, 55 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 535 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `46b4f826`
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
- Fighter
- k
- cel_box
- kit_rugged.py
- kit_household.py
- strip_fabric
- Garment
- mesh_shirt
- kit_shimura.py
- arm_bone
- strip_fabric
- kit_market.py
- kit_kinoshita.py
- Pillar
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
- kokuto
- Run
- load_clans
- Balance
- CombatData
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
- Conflict
- kit.py
- list
- org.junit.jupiter.api.Test
- Move
- Personality
- Clan techniques and kekkei genkai
- HandSign
- VillageScaleTest
- Bond
- org.junit.jupiter.api.Test
- Bonds
- .read
- Def
- Levels
- Deed
- Squad
- .romance
- Battle.java
- Bosses
- Nature
- Value
- Styles and combo trees
- masks.py
- 4.3 The noble clans
- kit_haruno.py
- .test
- Peeve
- ClanRelations
- Shared helpers
- kit_umino.py
- Combat
- Meter
- Title
- .name
- Village
- Kindle
- Side quests
- .num
- .of
- 2. Quest framework
- Memory
- Label
- build.py
- Weaver
- StatusEffects
- docs.py
- 7. Inter-clan politics as quests
- 8. Beta catalogue
- Tier
- Pool
- paint.py
- clans.py
- COMBAT.md
- ComboMachine
- Chakra
- Json
- Technique catalogue
- sword_strap
- SignsTest
- progression.py
- wrap_front
- kit_inuzuka.py
- weapons.py
- SocietyHook
- common.py
- Cooldowns
- EmberLink
- Rng
- flaps
- jika_tabi
- kit_nara.py
- Animation clips
- The village
- animations.py
- wave_band
- Tier
- bandage_turns
- wide_sleeves
- ribbed
- tape
- face_mask
- bands
- blossom
- checks
- cloth_shoes
- collar_band
- geta
- ichimatsu
- kasuri
- overlap
- sash
- topknot
- sprigs
- wrap_front
- straw_sandals
- scarf
- shimenawa
- lamellar
- bun
- clip
- hairpin

## God Nodes (most connected - your core abstractions)
1. `k()` - 227 edges
2. `solid()` - 152 edges
3. `BondWorld` - 129 edges
4. `fabric()` - 109 edges
5. `Act` - 101 edges
6. `Fighter` - 63 edges
7. `Village` - 62 edges
8. `Battle` - 59 edges
9. `strip_fabric()` - 59 edges
10. `stamp()` - 47 edges

## Surprising Connections (you probably didn't know these)
- `4. Taijutsu` --references--> `Move`  [INFERRED]
  docs/COMBAT.md → combat/core/src/main/java/dev/shinobi/combat/Move.java
- `1. The data model` --references--> `Person`  [INFERRED]
  BONDS.md → life/bonds/src/main/java/dev/shinobi/life/bond/Person.java
- `Side quests in the beta` --references--> `clan()`  [INFERRED]
  ROADMAP.md → tools/combat/clans.py
- `3.2 Templates` --references--> `clan()`  [INFERRED]
  SIDE_QUESTS.md → tools/combat/clans.py
- `14. The combat core` --references--> `Cooldowns`  [INFERRED]
  docs/COMBAT.md → combat/core/src/main/java/dev/shinobi/combat/Cooldowns.java

## Import Cycles
- None detected.

## Communities (166 total, 55 thin omitted)

### Community 0 - "stamp"
Cohesion: 0.13
Nodes (10): stamp(), decal(), shoulder_decal(), slanted_protector(), white_fang_tanto(), crest(), crest_patch(), flame_hem() (+2 more)

### Community 1 - "kit_uchiha.py"
Cohesion: 0.19
Nodes (6): arm_crest(), back_crest(), chest_crest(), crest(), high_collar(), police_badge()

### Community 2 - "Clans"
Cohesion: 0.14
Nodes (11): Clans, Collections: the general wardrobe, Commands, Mix and match, Piece ids, Reference images, The clan file, clan_bottoms() (+3 more)

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
Cohesion: 0.11
Nodes (12): drawstrings(), holster(), hood_down(), sash(), side_stripe(), sleeve_roll(), stripes(), turned_hem() (+4 more)

### Community 7 - "Story bible"
Cohesion: 0.09
Nodes (23): Beta 1: the opening and the Academy (~4 h), Beta 2: Genin life (~8 h), Beta 3: the Chunin Exams (~3 h), Bonds in the story (spoilers), Clan lines, District quests and one-offs, Filler arcs, How to read this bible (+15 more)

### Community 8 - "kit_kurama.py"
Cohesion: 0.08
Nodes (13): back_crest(), bead_clip(), brush_pin(), brush_stroke(), bun(), ink_clouds(), part_line(), side_fringe() (+5 more)

### Community 9 - "rnd"
Cohesion: 0.14
Nodes (9): cel_face(), kasuri(), ink_stains(), seal_trim(), hair_box(), hair_face(), hair_shade(), rnd() (+1 more)

### Community 10 - "kit_yuhi.py"
Cohesion: 0.12
Nodes (10): mist_swirls(), rose(), thorn_band(), thorn_vine(), wave_box(), wave_curtain(), wave_face(), wave_fan() (+2 more)

### Community 11 - "kit_kunoichi.py"
Cohesion: 0.18
Nodes (5): belt(), frog_buttons(), mandarin_collar(), obi(), thigh_holster()

### Community 12 - "kit_aburame.py"
Cohesion: 0.18
Nodes (4): deep_hood(), high_collar(), hood_down(), lenses()

### Community 13 - "fabric"
Cohesion: 0.11
Nodes (11): back_crest(), crest(), back_crest(), head_cloth(), arm_protector(), forehead_protector(), protector_plate(), backward_bandana() (+3 more)

### Community 14 - "kit_suzuran.py"
Cohesion: 0.10
Nodes (10): apothecary_sash(), back_crest(), bell_charm(), bell_hem(), bell_print(), bell_sprig(), gloves(), herb_pouch() (+2 more)

### Community 15 - "7. Systems in the beta"
Cohesion: 0.12
Nodes (17): 7. Systems in the beta, Adventure rules, Character creation, Combat in the beta, Death, Food, Friendship and bonds, Gear and crafting (+9 more)

### Community 16 - "Fighter"
Cohesion: 0.09
Nodes (10): Battle, Plan, Plan, Plan, Chain, Event, Plan, Result (+2 more)

### Community 17 - "k"
Cohesion: 0.09
Nodes (12): shin_wraps(), obi(), shin_wrap(), patch(), neckline(), pauldron(), trench_knife(), bandolier() (+4 more)

### Community 18 - "cel_box"
Cohesion: 0.13
Nodes (11): cel_box(), curtain(), tie(), back_sheet(), ear_panels(), gathered_tail(), hair_tie(), round_bun() (+3 more)

### Community 19 - "kit_rugged.py"
Cohesion: 0.06
Nodes (17): baggy_legs(), camo(), cape(), dread(), knot_bun(), leg_wraps(), patch(), ragged() (+9 more)

### Community 20 - "kit_household.py"
Cohesion: 0.20
Nodes (5): arm_cloth(), dots(), socks(), stripes(), waist()

### Community 21 - "strip_fabric"
Cohesion: 0.09
Nodes (11): decal(), hood_down(), lantern(), lantern_tag(), mantle(), muffler(), plain_body(), pleats() (+3 more)

### Community 22 - "Garment"
Cohesion: 0.31
Nodes (3): compatible(), Garment, key_rgba()

### Community 24 - "kit_shimura.py"
Cohesion: 0.18
Nodes (5): forearm_wraps(), back_crest(), bandaged_arm(), cane(), bandage()

### Community 25 - "arm_bone"
Cohesion: 0.11
Nodes (13): sode(), arm_bone(), arm_x(), arm_guards(), kimono_sleeves(), kimono_sleeves(), tasuki(), armband() (+5 more)

### Community 26 - "strip_fabric"
Cohesion: 0.04
Nodes (24): leg_cloth(), waist(), body(), gloves(), half_sleeves(), shirt(), trousers(), footwear() (+16 more)

### Community 27 - "kit_market.py"
Cohesion: 0.09
Nodes (11): bib(), checks(), dots(), furoshiki(), open_front(), pocket(), sash(), sashiko() (+3 more)

### Community 28 - "kit_kinoshita.py"
Cohesion: 0.10
Nodes (14): back_crest(), chisel(), crest(), kyahan(), mallet(), nail_pouch(), pencil(), _piece() (+6 more)

### Community 29 - "Pillar"
Cohesion: 0.07
Nodes (21): Build, Attack, Damage, Defence, Delivery, AREA, JUTSU, MELEE (+13 more)

### Community 30 - "5. Data formats built for the whole story"
Cohesion: 0.18
Nodes (11): 5. Data formats built for the whole story, Authoring tools, Board missions, Chapters and arcs, Names rolled per save, Principles, Ranks and milestones, Rotating story roles (+3 more)

### Community 31 - "kit_field.py"
Cohesion: 0.08
Nodes (14): blouse(), cargo(), collar(), holster(), knee_guards(), pocket(), strap(), hakama_legs() (+6 more)

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

### Community 38 - "kit_uzumaki.py"
Cohesion: 0.22
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
Cohesion: 0.12
Nodes (8): flick(), gourd(), lames(), puff(), quilt(), shoku_disc(), snack_pouch(), curls_box()

### Community 43 - "kokuto"
Cohesion: 0.24
Nodes (4): back_blade(), crest(), hip_kokuto(), kokuto()

### Community 44 - "Run"
Cohesion: 0.06
Nodes (19): 15. Pacing, BondEvent, Rng, Seeds, Chapter, Phase, ACADEMY, EXAMS (+11 more)

### Community 45 - "load_clans"
Cohesion: 0.23
Nodes (7): Population, load_all_groups(), load_clans(), load_population(), population_weights(), validate_clans(), village_resident()

### Community 46 - "Balance"
Cohesion: 0.12
Nodes (9): Boss, Difficulty, Balance, Share, Stats, BalanceTest, Skill, Trace (+1 more)

### Community 47 - "CombatData"
Cohesion: 0.12
Nodes (5): CombatData, Enemy, Phase, Weapon, Def

### Community 48 - "build"
Cohesion: 0.32
Nodes (5): build(), build_all(), load_module(), natural(), sources()

### Community 49 - "Box"
Cohesion: 0.07
Nodes (9): band(), hem(), strip_line(), Box, Layer, Piece, piece_corners(), rot_matrix() (+1 more)

### Community 51 - "Face"
Cohesion: 0.07
Nodes (17): mark(), drawn_line(), glyph(), spider_crest(), thread_spool(), threads(), web(), web_hem() (+9 more)

### Community 52 - "ring_shell"
Cohesion: 0.15
Nodes (8): ring_shell(), crown(), clipped(), combed_back(), nape_hem(), pulled_back(), combed_up(), scalp()

### Community 53 - "kit_gekko.py"
Cohesion: 0.29
Nodes (3): crescent(), hip_katana(), katana()

### Community 54 - "Act"
Cohesion: 0.03
Nodes (62): Act, ABANDONED_MISSION, APOLOGIZED, BIRTHDAY_REMEMBERED, BOND_MOMENT, BRAGGED, BROKE_PROMISE, BROKE_SECRET (+54 more)

### Community 55 - "Person"
Cohesion: 0.06
Nodes (12): 10. Romance and family (after the beta), Courtship, Stage, CRUSH, DATING, ENGAGED, INTEREST, MARRIED (+4 more)

### Community 57 - "kit_hagane.py"
Cohesion: 0.21
Nodes (5): bracers(), harness(), mace(), plate(), shin_guards()

### Community 58 - "Conflict"
Cohesion: 0.07
Nodes (11): 13. Data formats, Conflict, Household, Grant, Kindling, Tier, FULL, NATURE (+3 more)

### Community 59 - "kit.py"
Cohesion: 0.11
Nodes (10): shirt(), collar(), vest(), pouch(), bandolier(), coat_skirts(), scroll_tube(), shirt() (+2 more)

### Community 61 - "org.junit.jupiter.api.Test"
Cohesion: 0.17
Nodes (4): BondDialogueTest, ConditionsAndEffectsTest, KindlingAndBookTest, VillageTest

### Community 62 - "Move"
Cohesion: 0.09
Nodes (3): Move, Style, ComboAndStatusTest

### Community 64 - "Clan techniques and kekkei genkai"
Cohesion: 0.08
Nodes (26): Aburame (noble), Akimichi (noble), Clan techniques and kekkei genkai, Gekko (noble), Hagane (minor), Haruno (minor), Hatake (noble), Hyuga (noble) (+18 more)

### Community 65 - "HandSign"
Cohesion: 0.13
Nodes (15): HandSign, BIRD, BOAR, DOG, DRAGON, HARE, HORSE, MONKEY (+7 more)

### Community 67 - "VillageScaleTest"
Cohesion: 0.13
Nodes (3): Report, VillageSim, VillageScaleTest

### Community 69 - "org.junit.jupiter.api.Test"
Cohesion: 0.08
Nodes (5): DataTest, ResourcesTest, ConflictTest, MemoryTest, SquadTest

### Community 70 - "Bonds"
Cohesion: 0.11
Nodes (13): 11. Kindling Bond, 16. What stays in Village Friends, and what moves, 17. Proposed ROADMAP edits, 1. The data model, 21. Open questions, 2. The meters, 3. Levels and story gates, 4. Memories (+5 more)

### Community 71 - ".read"
Cohesion: 0.20
Nodes (3): 14. Save format and versioning, SaveFormat, SaveFormatTest

### Community 72 - "Def"
Cohesion: 0.07
Nodes (14): Def, Experience, CAMP, DATE, FESTIVAL, MEAL, MISSION, SPAR (+6 more)

### Community 73 - "Levels"
Cohesion: 0.14
Nodes (3): Levels, Meters, LevelsTest

### Community 74 - "Deed"
Cohesion: 0.12
Nodes (3): Deed, Know, Gossip

### Community 75 - "Squad"
Cohesion: 0.09
Nodes (3): BondEffects, Departure, Squad

### Community 77 - "Battle.java"
Cohesion: 0.09
Nodes (5): Band, CLOSE, FAR, MID, RangeBands

### Community 78 - "Bosses"
Cohesion: 0.08
Nodes (24): Bestiary, groups and bosses, Bosses, `combat:boss.anbu.story_1`: Story boss (chapter anbu, level 40, anbu), `combat:boss.ch11.bandit_chief`: Bandit chief (chapter 11, level 11, beta2), `combat:boss.ch14.road_ambush`: Ambush on the road (chapter 14, level 14, beta2), `combat:boss.ch16.forest_beast`: A giant of the forest (chapter 16, level 16, beta3), `combat:boss.ch16.forest_team`: A hunting team in the forest (chapter 16, level 16, beta3), `combat:boss.ch17.prelim`: Preliminary bout (chapter 17, level 16, beta3) (+16 more)

### Community 79 - "Nature"
Cohesion: 0.11
Nodes (16): Armour, CHAKRA, NONE, PHYSICAL, WILL, DamageType, Clash, Nature (+8 more)

### Community 80 - "Value"
Cohesion: 0.15
Nodes (11): Value, COURAGE, CREATIVITY, DUTY, FAMILY, FREEDOM, HONESTY, KINDNESS (+3 more)

### Community 81 - "Styles and combo trees"
Cohesion: 0.09
Nodes (23): Academy blade (`combat:style.academy_blade`, weapons), Academy taijutsu (`combat:style.academy_basics`, taijutsu), Beast Fang (Four Legs) (`combat:style.beast_fang`, taijutsu), Blossom Strength (`combat:style.blossom_strength`, taijutsu), Chain arts (`combat:style.chain_arts`, weapons), Crescent Moon kenjutsu (`combat:style.crescent_moon`, weapons), Fan arts (`combat:style.fan_arts`, weapons), Gentle Fist (`combat:style.gentle_fist`, taijutsu) (+15 more)

### Community 82 - "masks.py"
Cohesion: 0.11
Nodes (10): How the pieces work, anbu_arms(), flak_vest(), mesh(), tanto(), beak(), bump(), ears() (+2 more)

### Community 83 - "4.3 The noble clans"
Cohesion: 0.06
Nodes (31): 4.1 The shape of a clan line, 4.2 Clan relations at the start, 4.3 The noble clans, 4.4 The minor clans, 4.5 Clan quest counts, 4. Clan quest lines, Aburame, Akimichi (+23 more)

### Community 84 - "kit_haruno.py"
Cohesion: 0.15
Nodes (7): arm_crest(), back_crest(), chest_crest(), circle(), frog_clasps(), kimono_trim(), mandarin_collar()

### Community 85 - ".test"
Cohesion: 0.10
Nodes (8): 12. The bond book, BondBook, Fact, MemoryLine, Page, BondConditions, BondDialogue, BondWeb

### Community 86 - "Peeve"
Cohesion: 0.10
Nodes (15): 20. What the roadmap asks of bonds, 5. Personality, Base, Peeve, BRAGGING, COWARDICE, CRUELTY, DISHONESTY (+7 more)

### Community 88 - "Shared helpers"
Cohesion: 0.10
Nodes (13): Shared helpers, back_fan(), bangs(), braid(), lock(), sidelocks(), blunt_fringe(), hime_locks() (+5 more)

### Community 89 - "kit_umino.py"
Cohesion: 0.11
Nodes (9): spike(), crown(), burst(), brush_tail(), falling_tail(), scroll(), surf(), wave_band() (+1 more)

### Community 90 - "Combat"
Cohesion: 0.10
Nodes (18): Bonds, 10. Enemies, 11. Difficulty and feel, 12. Progression, 13. The beta loadout, 16. Animations, 17. What waits for Phase 0, 18. Ids for other systems (+10 more)

### Community 91 - "Meter"
Cohesion: 0.13
Nodes (13): Lean, Meter, AFFECTION, RESPECT, RIVALRY, ROMANCE, TRUST, Trait (+5 more)

### Community 92 - "Title"
Cohesion: 0.12
Nodes (8): Standing, Title, GOOD_NEIGHBOR, HELPING_HAND, HERO, NEWCOMER, PILLAR, UNWELCOME

### Community 93 - ".name"
Cohesion: 0.09
Nodes (13): State, ARGUMENT, COLD_SHOULDER, FALLING_OUT, MAKING_UP, NONE, Label, CALM (+5 more)

### Community 94 - "Village"
Cohesion: 0.13
Nodes (4): 18. Village scale, ClanProfile, House, Village

### Community 95 - "Kindle"
Cohesion: 0.14
Nodes (10): Boost, Burn, Form, Kindle, Tier, BLAZE, FLAME, NONE (+2 more)

### Community 96 - "Side quests"
Cohesion: 0.18
Nodes (11): 1. Scope and budget, 3.1 The hook schema, 3.2 Templates, 3. Society hooks and generated quests, 5. Civilian and district quests, 6. Filler arcs, 9. Open questions, Contents (+3 more)

### Community 98 - ".of"
Cohesion: 0.11
Nodes (6): 8. The village talks, Stage, ADULT, CHILD, TEEN, GossipTest

### Community 99 - "2. Quest framework"
Cohesion: 0.18
Nodes (13): Conditions and actions, The quest format, 2.1 Kinds, 2.2 Unlock rules, 2.3 How quests are found, 2.4 Repeatability, 2.5 Failure and expiry, 2.6 Rewards (+5 more)

### Community 100 - "Memory"
Cohesion: 0.14
Nodes (6): Memory, Source, HEARD, SEEN, SELF, TOLD

### Community 101 - "Label"
Cohesion: 0.20
Nodes (7): Label, ALLIES, COOL, FEUD, FRIENDLY, NEUTRAL, RIVALS

### Community 102 - "build.py"
Cohesion: 0.18
Nodes (10): all_techniques(), build(), check(), statuses_in(), fold(), main(), public_text_hashes(), short() (+2 more)

### Community 103 - "Weaver"
Cohesion: 0.16
Nodes (7): Outcome, CAST, EMPTY, FIZZLE, INTERRUPTED, Result, Weaver

### Community 105 - "docs.py"
Cohesion: 0.28
Nodes (12): animations_page(), bestiary_page(), clans_page(), counters(), esc(), move_rows(), signs(), styles_page() (+4 more)

### Community 106 - "7. Inter-clan politics as quests"
Cohesion: 0.33
Nodes (6): 7.1 What moves clan relations, 7.2 What clan relations do, 7.3 Council days and disputes, 7.4 Festivals and ceremonies, 7.5 In the beta, 7. Inter-clan politics as quests

### Community 107 - "8. Beta catalogue"
Cohesion: 0.33
Nodes (6): 8. Beta catalogue, Beta 1: the opening and the Academy, Beta 2.5: clan welcomes, wave 2, Beta 2: Genin life, Beta 3: the Chunin Exams, Totals and Varied pools

### Community 108 - "Tier"
Cohesion: 0.18
Nodes (6): Mastery, Tier, MASTERED, NOVICE, PERFECTED, PRACTICED

### Community 112 - "clans.py"
Cohesion: 0.23
Nodes (10): ct(), lesser(), area(), cone(), line(), proj(), st(), summon_entity() (+2 more)

### Community 113 - "COMBAT.md"
Cohesion: 0.25
Nodes (3): Commits, graphify, Naruto Minecraft

### Community 114 - "ComboMachine"
Cohesion: 0.25
Nodes (3): ComboMachine, Context, Started

### Community 117 - "Technique catalogue"
Cohesion: 0.15
Nodes (13): Chakra movement, Earth (9), Fire (10), Fuinjutsu (6), Genjutsu (8), Lightning (8), Medical ninjutsu (5), Neutral ninjutsu (14) (+5 more)

### Community 120 - "progression.py"
Cohesion: 0.35
Nodes (9): build(), gear_for(), melee_for(), pillar_cap(), ranks_for(), sim_builds(), slice_open(), teammate_build() (+1 more)

### Community 122 - "kit_inuzuka.py"
Cohesion: 0.13
Nodes (7): claw_marks(), fang(), fang_small(), fur_box(), fur_edge(), fur_face(), paw()

### Community 129 - "flaps"
Cohesion: 0.33
Nodes (4): flaps(), robe_skirt(), skirt(), side_panels()

### Community 130 - "jika_tabi"
Cohesion: 0.29
Nodes (4): jika_tabi(), _soles(), waraji(), zori()

### Community 131 - "kit_nara.py"
Cohesion: 0.33
Nodes (3): back_crest(), crest(), tuft()

### Community 132 - "Animation clips"
Cohesion: 0.33
Nodes (5): Animation clips, P0, P1, P2, P3

### Community 133 - "The village"
Cohesion: 0.33
Nodes (6): ANBU Black Ops: the Hokage's masked guard, Genin: the village's young ninja, Jonin: the elite of the Hidden Leaf, Kage and signature looks, Naruto Minecraft, The village

### Community 134 - "animations.py"
Cohesion: 0.50
Nodes (3): clip(), many(), summary()

### Community 137 - "Tier"
Cohesion: 0.50
Nodes (4): Tier, BACKGROUND, CAST, KNOWN

## Knowledge Gaps
- **201 isolated node(s):** `MELEE`, `THROWN`, `JUTSU`, `AREA`, `NONE` (+196 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1119 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **55 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `k()` connect `k` to `stamp`, `flaps`, `jika_tabi`, `kit_nara.py`, `kit_senju.py`, `kit_uchiha.py`, `kit_academy.py`, `wave_band`, `kit_kurama.py`, `rnd`, `kit_yuhi.py`, `kit_kunoichi.py`, `kit_aburame.py`, `fabric`, `ribbed`, `tape`, `face_mask`, `wide_sleeves`, `cel_box`, `blossom`, `kit_household.py`, `cloth_shoes`, `geta`, `kit_rugged.py`, `kit_shimura.py`, `arm_bone`, `strip_fabric`, `sash`, `kit_kinoshita.py`, `wrap_front`, `kit_market.py`, `kit_field.py`, `straw_sandals`, `scarf`, `shimenawa`, `kit_shiranui.py`, `lamellar`, `bun`, `kit_uzumaki.py`, `clip`, `hairpin`, `kit_yamanaka.py`, `kit_akimichi.py`, `kokuto`, `Box`, `Face`, `ring_shell`, `kit_gekko.py`, `bandage_turns`, `kit_hagane.py`, `kit.py`, `kit_suzuran.py`, `masks.py`, `kit_haruno.py`, `Shared helpers`, `kit_umino.py`, `strip_fabric`, `paint.py`, `sword_strap`, `wrap_front`, `kit_inuzuka.py`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `solid()` (e.g. with `Shared helpers` and `Box`) actually correct?**
  _`solid()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `MELEE`, `THROWN`, `JUTSU` to the rest of the system?**
  _201 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `stamp` be split into smaller, more focused modules?**
  _Cohesion score 0.12857142857142856 - nodes in this community are weakly interconnected._
- **Why does `Bonds` connect `Bonds` to `.of`, `Memory`, `.read`, `Levels`, `Run`, `.romance`, `COMBAT.md`, `.test`, `Peeve`, `Person`, `ClanRelations`, `Conflict`, `SocietyHook`, `Village`?**
  _High betweenness centrality (0.094) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `fabric()` (e.g. with `Shared helpers` and `Face`) actually correct?**
  _`fabric()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Clans` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._