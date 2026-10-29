# Roadmap

From a wardrobe of Naruto-styled residents to an adventure map of the whole Hidden Leaf, where you
arrive as an orphaned academy student and rise to Hokage.

This plan builds on [Village Friends](https://github.com/radhepa/Village-Friends-Minecraft-Mod)
(VF below) wherever VF already solves a problem. File links point at VF's `main` branch. VF
targets **Minecraft 26.3 on Fabric** (loader 0.19.5, Fabric API 0.161.0+26.3, Loom 1.17.21,
Java 25; VF 2.29.1, see its
[gradle.properties](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/gradle.properties)).
Naruto Minecraft targets the same versions and stays on them. Moving to another Minecraft version
is separate work, as it is for VF.

## 1. Vision

Naruto Minecraft is a single-player adventure map of the Hidden Leaf: one walled village under the
Hokage Rock, hand-built district by district, full of residents who live their own days.

**The story.** You are an orphan. A squad of Leaf ninja rescues you, and the Hokage enrolls you in
the Academy and gives you a small apartment. From there it is your life in the village: lessons,
missions, money, friends, rivals, and every night home to bed. You cannot break or place blocks in
the world. What you can do is earn ryo, buy things, furnish your apartment and fill its chests,
and grow from a student with a wooden kunai into the Fifth Hokage, whose face is carved next to
the four already on the Rock.

The village matters more than the fighting. Residents wake, work, eat at Ichiraku, gossip, train,
fall in love and remember what you did. That is VF's resident model, which already runs routines,
friendships, families, deeds and notice boards. Naruto Minecraft dresses those residents as
shinobi and civilians of the Leaf, gives each one a rank, and adds what VF lacks: ninja combat,
chakra, jutsu, missions, exams, a day-and-night life for the player, and an original ninja plot.

Progress has two halves. **Ranks** are story milestones: exams and promotions that change your
outfit, your missions, where you may go and how the village treats you. **Levels** are your power:
XP from missions, training and fights raises your chakra, health and strength, and each rank's
exam asks for a minimum level. Dying costs levels, and fails the mission you were on. Recurring
events (festivals, the Chunin Exams twice a year, clan days) and crisis arcs give the calendar a
pulse. Combat is fast and readable: chained taijutsu, dodges, chakra-powered movement across roofs
and water, jutsu woven from hand signs, and thrown tools.

**Ladder:** Academy → Genin → Chunin → Jonin → Hokage, with **ANBU** as an optional branch from
Jonin.

## 2. Decisions

The owner's answers to the first draft's open questions. Every section below follows them.

| # | Topic | Decision |
|---|---|---|
| 1 | Clans | At the start you choose to be born into one of the 15 clans (an orphan of that clan) or to be clanless. A clanless player can later **found their own clan**: name, crest, colors, look, members recruited from residents, and a home ([Player clans](#player-clans)). |
| 2 | Canon | Original characters only for now, maybe cameos of named characters later, and a unique ninja plot. The sitting Hokage and your mentors are original characters. |
| 3 | ANBU | An optional branch from Jonin, not a required rung. The Hokage succession needs Jonin; ANBU is not required. |
| 4, 6 | Players | **Single player first.** Multiplayer is a later phase. The code stays server-authoritative (single player runs an integrated server), so it is not closed off. |
| 5 | World | A **fixed, hand-made map with a border**. |
| 7 | Generation | Nothing is procedurally generated. Vanilla and VF world generation are off. "Generated" districts in the first draft become **pasted** ones: map tools paste blueprints at fixed spots while the map is being built, and the result is saved into the shipped world. |
| 7 | VF's RPG add-on | **Assumption:** not shipped with the map. The owner's "No" on generation is read as also answering this; it also avoids two level systems fighting. Confirm. |
| 8 | Elemental nature | You **choose** your first nature and **gain more** through training and milestones. |
| 9 | Death | Dying costs levels, and if you are on a mission, the mission fails. This adds a player **level and XP** system ([Levels](#levels)). |
| 10 | Era | Four Hokage faces on the Rock at the start. The player becomes the Fifth. |
| — | Story premise | Orphan rescued by a squad; the Hokage grants an apartment; no block breaking; buy things, earn money, store in chests; sleep each night, or stay up and grow tired and slower. |

## 3. Where we start

| Have | Where |
|---|---|
| Naruto wardrobe: hair, tops, bottoms, headwear, faces, palettes, eye colors (Sharingan, Byakugan), compiled from Python | `tools/wardrobe/` → `src/main/resources/assets/narutominecraft/wardrobe/` |
| 21 characters with a `rank`: Genin, Jonin, ANBU and kage/signature looks | `tools/wardrobe/characters/`, renders in `docs/renders/` |
| Clan system: clan JSON, resident mixing after VF's OutfitFactory, id blocks per clan | [CLANS.md](CLANS.md), `tools/wardrobe/clans/` |
| Fifteen clans with id blocks in [CLANS.md](CLANS.md): Senju, Uzumaki, Uchiha, Hyuga, Nara, Akimichi, Yamanaka, Inuzuka, Sarutobi, Aburame, Hatake, Kurama, Shimura, Yuhi, Gekko | in progress on `clan/*` branches |

| Missing | Notes |
|---|---|
| Any Java: no mod, entities, items or gameplay | Phase 0 |
| Academy, Chunin and civilian outfits | README notes Academy and Chunin are still to come; civilians (shopkeepers, the ramen cook, farmers) have no Naruto wardrobe at all |
| Buildings, furniture, the map, animations for ninja | Phases 1 to 6 |

### What Village Friends already gives us

| Need | VF already has it | Use it for |
|---|---|---|
| Residents that look and move like ours | Resident model, Living Eyes, wardrobe layer, OutfitFactory ([OUTFIT_ENGINE.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/OUTFIT_ENGINE.md), [ANIMATION_EDITING.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/ANIMATION_EDITING.md)) | Every Leaf resident; our wardrobe tools are a port of this |
| Daily lives | `routine/Routine.java`, `ResidentRoutines` ([VILLAGE_DAYS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/VILLAGE_DAYS.md)): hours, meals, work, children's lessons at 10:00, night watch, Market Day | Shinobi duty shifts, Academy lessons, gate watch; the village's clock that the player's day fits around |
| Community | `social/` census, relationships, families, news, ten friendship levels, speech bubbles, Ledger ([VILLAGE_LIFE.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/VILLAGE_LIFE.md)) | Clan families, village news, recruiting members for a player clan |
| Talk | 5,898 lines in `tools/dialogue/`, chosen by `talk/Talk.java`; offers like food, mending and directions | Add rank, story and event pools |
| Reputation | Deeds, witnesses, rumors, standing ([DEEDS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/DEEDS.md)) | How the village reacts to the player beyond rank |
| Quests and pay | Notice boards: `quest/Postings`, `quest/Board`, `quest/QuestLog`, `VillageQuests`, paid in emeralds ([BIRTHDAYS_AND_NOTICES.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/BIRTHDAYS_AND_NOTICES.md)) | The D-rank mission board, paid in ryo instead |
| Shops | Residents trade through vanilla villager trading, prices moved by standing and deeds (`mixin/VillagerReputationMixin`) | Every shop: ramen, tools, furniture, outfits, priced in ryo |
| A calendar | `social/Calendar`: 4 seasons × 28 days, village weeks, Market Day | Scheduling every event and the Academy week |
| Scheduled community events | Birthdays and parties (`Birthdays`), the fishing contest (`fishing/Contest`) | The pattern for festivals and exam days |
| Escorts and companions | `CompanionController`: follow, wait, rescue | The rescue squad in the prologue, C-rank escorts, NPC teammates |
| Non-lethal defeat | `Knockouts`: residents are knocked out, not killed ([GUARDS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/GUARDS.md#knockouts)) | Sparring and exam fights |
| Defenders | Knights and archers, call-out on village grounds, guard levels (`GuardController`, `GuardProgression`) | Village defense during invasions |
| Restaurants and furniture | Tavern: seating and furniture blocks, served course by course (`tavern/TavernBlocks`, `tools/tavern/furniture.py`, [TAVERN.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/TAVERN.md)) | Ichiraku, the barbecue house, arena seating via the `Seat` entity; tables and chairs for the furniture shop |
| Homes and beds | Housing index, one bed per resident, House Plaque flood fill for hand-built houses (`home/FloodFill`, `home/HouseBounds`, [HOMES.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/HOMES.md)) | Beds for every resident in a hand-built Konoha; the player's apartment bounds for furnishing |
| Kitchens | Hearth & Harvest cooking stations and dishes from one table ([HEARTH_AND_HARVEST.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/HEARTH_AND_HARVEST.md)), `WellFed` | Ramen, dango, tea, soldier pills; a cooking pot you can buy for your apartment |
| Pets | Residents' cats and dogs ([PETS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/PETS.md)) | Inuzuka ninken, the "catch the runaway cat" D-rank |
| Children's games | `play/Games`, `Playground` ([PLAYTIME.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/PLAYTIME.md)) | Academy kids at recess |
| Buildings from code | Python design programs → blueprints → NBT (`tools/village_design/`, `tools/create_village_structures.py`, [BUILDING_EDITING.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/BUILDING_EDITING.md)); standalone templates placed by code ([standalone_templates.json](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/tools/standalone_templates.json)) | Every repeatable Konoha building, pasted at fixed spots |
| Animation clips | Python-keyed clips compiled to `resident_animations/*.json`, packs from other namespaces load too ([ANIMATION_PACKS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/ANIMATION_PACKS.md)) | Resident ninja clips with no Java; the clip format for the player too |
| An add-on precedent | `rpg/`: a separate jar requiring VF, hooked by mixins and VF's public events, a synced player attachment, keys, a HUD badge, levels, cooldown abilities, pure balance classes ([rpg/README.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/rpg/README.md)) | The shape of Naruto Minecraft's code and its level system (we do not ship the RPG itself) |
| In-game tests and screenshots | `runClientGameTest` with focused flags, gallery screenshots ([VERIFICATION.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/VERIFICATION.md)) | Done criteria for every phase |

What VF does **not** have, and we build: player animation (VF animates residents only), combat
beyond vanilla swings and guard AI, chakra and techniques, adventure rules with furnishing, a ryo
economy, player fatigue, a fixed hand-made map, and anything Japanese in its building kit.

**Where VF assumes generated villages.** VF finds a village's houses and its tavern through the
village *structure pieces* that world generation leaves behind (`home/HouseSurvey`,
`tavern/TavernSurvey`). Our map has none. Houses still work: a House Plaque flood-fills a
hand-built house into a home. Settlements work through the Village Marker. The tavern (and any
other system that reads structure pieces) needs a small VF hook so a hand-built building can be
registered by marker or by bounds. That is part of Phase 0.

## 4. The map

### References

The layout follows the Narutopedia (Naruto Fandom wiki) pages cited in each row. Image downloads
and the wiki itself were blocked by this session's network policy, so the descriptions come from
the wiki text quoted in search results, not from the art. Check each district against the images on
those pages before building it.

- **Overall shape** ([Konohagakure](https://naruto.fandom.com/wiki/Konohagakure), [Hokage Rock](https://naruto.fandom.com/wiki/Hokage_Rock)): the village
  is laid out in a fan around the Hokage Rock, the mountain with the Hokage faces carved into it.
  Streets of shops and buildings run out from it. The Hokage Residence always sits in the middle,
  right below the faces. The village is walled on every side, and the hiragana あん is painted on
  its entrance gates, one character per door.
- **Inspiration:** Kishimoto has said Konoha is modelled on his hometown in Okayama Prefecture,
  which had training fields from a nearby military base. That explains the low hills and fields
  around the walls.

### Scale and border

A Minecraft player is 1.8 m tall and a block is 1 m. Keep **heights and interiors at 1:1** so
doors, rooms and stairs feel right, and **compress distances**: the Konoha of the show is several
kilometres across, which in Minecraft would be empty walking.

- **Inside the wall:** a rough circle about **640 blocks across** (40 chunks). Sprinting across
  takes about two minutes; roof-hopping with chakra about one. That fits roughly 250 to 400
  buildings, of which perhaps 180 homes.
- **Hokage Rock:** a cliff behind the village about 70 blocks high, each face about 24 blocks tall.
  **Four faces** at the start and room for a fifth, yours. The streets fan out from its foot, so
  the Rock is visible from every street.
- **Outside the wall:** the Forest of Death, outer training grounds, the hills of the prologue,
  bandit camps and roads to the gates. The whole map is about **1,200 × 1,200 blocks**, closed by
  a world border dressed as mountains and deep forest so it never ends in a bare wall. Mission
  locations beyond it (other villages, far roads) are separate small areas reached by travel
  scenes at the border gates, not open terrain.
- **No generation:** the shipped world uses an empty generator outside the map; vanilla structures
  and VF villages are switched off by a data pack.
- **Population:** about 150 to 250 residents to start. VF residents tick routines once a second,
  so measure before going higher.

### Pasted or built by hand

Nothing is generated at play time. The rule while *making* the map: anything there are many of is
a **design program** in Python, in VF's blueprint pipeline, with a new Japanese building kit, and
the map tools paste it at a fixed spot. Anything that appears once and defines the village is
**built by hand** in the map world.

| District / landmark | How | Notes |
|---|---|---|
| Homes, apartments, shops, tea houses | Pasted from blueprints | Konoha kit: plaster walls in cream and terracotta, round water tanks on flat roofs (check against the art), awnings, paper lanterns, stacked apartment blocks. Every home has a House Plaque so VF Homes flood-fills it and assigns beds. The player's apartment block is one of these, with the player's flat kept empty of residents |
| Streets, alleys, bridges, the river | Pasted | A Konoha `roads.py`: packed dirt and stone lanes, utility poles, signs |
| Wall and gates | Pasted modules, gates by hand | Wall segments are one repeated module. The main gate, with あん painted across its doors, and the guard booth are hand-built ([Konohagakure](https://naruto.fandom.com/wiki/Konohagakure)) |
| Hokage Rock | By hand | Voxel sculpting; four faces, and a blank fifth spot that the map swaps for the player's face in Phase 6. The village expands onto the plateau above it only in a much later era, so leave the top as forest ([Hokage Rock](https://naruto.fandom.com/wiki/Hokage_Rock)) |
| Hokage Residence | By hand | Circular, one of the largest buildings in the village, with 火 (fire) painted on the roof. It stands near the Academy, right below the faces. Mission desk on the ground floor, the clan registry, the Hokage's office upstairs ([Hokage Residence](https://naruto.fandom.com/wiki/Hokage_Residence)) |
| Ninja Academy | By hand | A large building at the base of the Hokage Rock, recognizable by the tree with a swing out front and a big 火 sign. Classroom, yard, target posts; the vertical slice. The office part is often confused with the Hokage Residence, but they are two buildings ([Ninja Academy file](https://naruto.fandom.com/wiki/File:Ninja_Academy.png), [Hokage Residence](https://naruto.fandom.com/wiki/Hokage_Residence)) |
| Ichiraku Ramen | By hand (small) | A VF tavern building (once the tavern hook exists), so the tavern code seats and serves residents |
| Shops: furniture, tools and weapons, clothes, grocer, tea house, barbecue house, dango, flower shop | Pasted or small hand builds | The furniture shop has a showroom of everything it sells, placed as display pieces. Flower shop belongs to the Yamanaka compound |
| Clan compounds and clan homes (15) | Hand-built core, pasted houses | Eight great compounds and seven smaller clan homes; see [Clan quarters](#clan-quarters) |
| Vacant estates (4) | Hand-built, sealed | Empty walled estates at the village edge for player clans; their halls open as you buy them ([Player clans](#player-clans)) |
| Training grounds | Pasted props, Ground 3 by hand | Ground 3: a glade with three stumps in a row, a polished kunai-shaped memorial stone below them, a large deep river with forest on both banks and mountains in view ([Third Training Ground](https://naruto.fandom.com/wiki/Third_Training_Ground)). The Ino-Shika-Cho memorial goes near the Nara forest ([Yamanaka, Nara, and Akimichi Clan Memorial](https://naruto.fandom.com/wiki/Yamanaka,_Nara,_and_Akimichi_Clan_Memorial)). Others: target posts, logs, a lake for water-walking, a cliff for wall-running |
| Hospital | By hand | Where you wake after dying or collapsing; residents knocked out are revived here |
| Chunin Exam arena | By hand | The stadium for the finals: about 64 blocks across the floor, tiered seating for ~150 residents on VF `Seat` entities, a Kage box. The search found no canon description, so design it from the anime art ([Chūnin Exams](https://naruto.fandom.com/wiki/Ch%C5%ABnin_Exams)) |
| Forest of Death | Pasted trees, tower by hand | Training Ground 44, north of Training Ground 43. A metal fence with 44 evenly spaced gates, a river through it, and a tower in the exact centre holding an arena for the preliminaries. Its canon radius of about 10 km is compressed to a 384-block circle outside the wall. Giant trees 4 to 7 blocks thick and 60 to 90 tall come from tree design programs, pasted one by one, so they are tree-hopping terrain ([Forest of Death](https://naruto.fandom.com/wiki/Forest_of_Death)) |
| Prologue hills and bandit camp | By hand | South of the wall, inside the border; the rescue happens here |
| ANBU HQ | By hand, hidden | Under the Hokage Rock, only reachable on the ANBU branch |
| Police HQ, the market, the main street | Pasted around hand-built centres | |

### Clan quarters

Fifteen clans live in the village ([CLANS.md](CLANS.md)). The eight large clans get a **compound**:
a gate, a main hall, a training yard and 6 to 12 pasted homes in the clan's style, with 15 to 30
residents. The seven small clans get a **clan home**: one hand-built house or dojo with its
signature feature, plus 2 to 5 pasted homes in an ordinary district, with 4 to 10 residents. Each
quarter is one plot group in the map layout file, filled with that clan's residents from its clan
JSON. A clan-born player has a room waiting in their clan's quarter from Genin on.

| Clan | Kind | Where | Signature build |
|---|---|---|---|
| Senju | Compound | Beside the Hokage Residence, under the Rock: the founders' clan | Wooden hall grown around a living tree; founders' shrine |
| Uzumaki | Compound (small, mostly memorial) | Next to the Senju, their old allies | Memorial shrine with the spiral crest and a sealing-mask hall; few living members |
| Uchiha | Compound | On the village's outskirts, walled ([Uchiha Clan](https://naruto.fandom.com/wiki/Uchiha_Clan)) | Fan crest on every wall, the shrine with a hidden meeting room, the Military Police HQ in a remote corner |
| Hyuga | Compound | Central, a short walk from the Residence | Formal estate in two halves, main and branch house, with a dojo and a koi pond |
| Nara | Compound | At the edge of the village, against the clan's deer forest | Plain house, the deer forest (protected; deer as mobs), the Ino-Shika-Cho memorial |
| Akimichi | Compound | By the market street | Big kitchen hall and storehouse; the barbecue house nearby is theirs |
| Yamanaka | Compound | On the main street | Flower shop at the front, a greenhouse and a quiet hall for mind techniques behind |
| Inuzuka | Compound | By the main gate, next to the outer training fields | Kennels, a veterinary clinic and an open run for the ninken |
| Sarutobi | Clan home | Near the Residence | Family house with the monkey crest and a fire-training yard |
| Aburame | Clan home | Wooded edge of a residential district | Dark timber house with insect gardens and hive walls |
| Hatake | Clan home | A quiet lane | A lone, worn family house (a near-vanished clan), its own small yard with ninken kennels |
| Kurama | Clan home | An old artists' lane | House with a painting studio; genjutsu-themed scrolls and screens |
| Shimura | Clan home | Close to the Hokage Rock, near the hidden ANBU entrance | Stern house; its cellar links to the ANBU branch's story (Phase 5) |
| Yuhi | Clan home | Residential district with gardens | House in a grove of old trees used for genjutsu training |
| Gekko | Clan home | By the training grounds | Kenjutsu dojo with a moon-viewing platform |

### How the map is made

1. A **map layout file** (`tools/konoha/layout.json`) places every district: polygon, streets,
   plots, which designs go on which plots, the landmarks' positions and rotations, the apartment
   bounds and the vacant estates.
2. Design programs in `tools/konoha/buildings/*.py` write blueprints in VF's format; VF's
   compiler turns them into NBT.
3. A **paste tool** (a dev command, `/naruto paste <district>`, only in builder mode) pastes a
   district's blueprints into the map world at their fixed spots. Re-pasting one district never
   touches the others.
4. The world is finished by hand (terrain, the Rock, the hand-built landmarks), plaques and
   markers are placed, and it is shipped as the adventure map's save with the mod jars.

The layout file makes the map reproducible: a later version can re-paste a changed district into
the master world before release.

## 5. Life in the village

### The opening

A playable prologue of 15 to 20 minutes that doubles as the tutorial and introduces the people who
will shape your career. All characters are original.

1. **Character creation.** Hair, eyes, complexion and marks from the wardrobe; born to one of the
   15 clans (its look and, later, its technique) or clanless.
2. **Captive.** You wake tied up in a bandit camp in the hills south of the village, at dusk. You
   learn to look, crouch and sneak by slipping your ropes and hiding in the grass.
3. **The rescue.** A squad breaks in: **the captain** (a Jonin, later your sensei), **a Chunin**
   (later your Academy instructor) and **a medic** (who works at the hospital). They are VF
   companions: you follow them, wait when told, and learn to dodge, sprint and climb while the
   squad fights. A chase through the forest ends with the captain carrying you over a ravine.
4. **The gate at night.** The guards, the main street with its lanterns, the Rock with its four
   faces. The squad takes you to the Residence.
5. **The Hokage.** The sitting Hokage, the Fourth, enrolls you in the Academy, grants you an
   apartment and an orphan's stipend, and hands you the key.
6. **Your apartment.** One room: a bed, a chest, a low table, a window. The Chunin shows you where
   the ramen stand and the Academy are. You sleep, and the game proper starts the next morning at
   6:00.

### Adventure rules

- **No breaking or placing blocks** anywhere in the world. The mod enforces it with Fabric's block
  break and use-block events, not only with Adventure mode, so it holds in every game mode except
  builder mode (operators with a builder flag, for making the map).
- **Allowed:** doors, gates, buttons and levers, sitting, sleeping, chests and furniture inside
  your own home, shop trading, cooking stations you own.
- **Techniques never change the map:** fire, bombs and wind do not break blocks; an Earth Wall or
  Wood Release barrier is a temporary entity or a block that is removed on its own after a few
  seconds and can only appear on open ground.

### Your apartment and furniture

Your home is a VF house: its House Plaque flood fill gives exact bounds (`home/HouseBounds`), and
furnishing is only allowed inside them.

- **Furnish mode.** Press `F` at home (or right-click your door plaque). Furniture items in your
  inventory show a ghost preview snapped to the block grid; scroll to rotate, click to place. Aim
  at a piece you own and click to pick it back up into your inventory, with its contents. Leaving
  your bounds or pressing `F` again ends furnish mode.
- **What counts as furniture:** blocks tagged `narutominecraft:furniture`, plus chests and
  storage. The furniture shop sells a Leaf set (futon and bed, low tables, cushions, tatami,
  screens, scroll shelves, lamps, potted plants, posters, a weapon rack, a training dummy), and
  VF's tavern furniture and Hearth & Harvest cooking stations, so you can cook at home.
- **Storage:** chests and a weapon cabinet hold anything; they keep their contents when picked up
  in furnish mode.
- **Your bed** is furniture too, but every home always keeps one bed; it is the bed that clears
  fatigue.
- **Upgrades as you rise:**

| Rank | Home |
|---|---|
| Academy, Genin | The one-room apartment the Hokage gave you |
| Chunin | Rent a two-room flat with a balcony (weekly rent), or move into your clan's quarter if clan-born |
| Jonin | Buy a small house, or a larger room in your clan's quarter |
| Clan founder | Your clan's estate ([Player clans](#player-clans)) |
| Hokage | Quarters in the Residence |

  Moving is a mover NPC: your furniture and chests are packed into moving crates (items that keep
  their contents) delivered to the new home, where you place them in furnish mode.

### Ryo

Ryo is the only money: notes as items (1, 10, 100 and 1,000 ryo) so it works with vanilla trading,
fits in chests and shows on the HUD as a total. VF pays notices and offers in emeralds and prices
trades in emeralds; Phase 0 adds a currency hook to VF (or a mixin) so every VF reward and trade
uses ryo.

The economy is small and closed. Rule of thumb: a day of D-rank missions covers food and leaves
about half to save; the first proper set of furniture takes about a week of play.

| Earn | Ryo |
|---|---|
| Orphan's stipend (Academy only, collected at the Residence) | 30 a day |
| Part-time jobs (a shift at Ichiraku, the grocer, the flower shop; VF workstations) | 40 to 80 |
| D-rank mission | 60 to 150 |
| C-rank | 300 to 600 |
| B-rank | 1,000 to 2,000 |
| A-rank | 3,000 to 6,000 |
| S-rank (ANBU branch) | 8,000 to 15,000 |
| Festival games and contests | small prizes |

| Spend | Ryo |
|---|---|
| A bowl of ramen, onigiri, tea | 3 to 10 |
| Kunai, shuriken, smoke and paper bombs | 5 to 40 each |
| Soldier pill | 60 |
| Furniture | 20 to 800 a piece |
| Outfits and gear (rank outfits are given; style variants are bought) | 100 to 600 |
| Chunin flat rent | 300 a week |
| A Jonin's house | 30,000 |
| Founding a clan | 20,000, then each estate hall 5,000 to 15,000 |

Furniture sells back at half price; loot from bandit camps sells at the pawn shop. There is no
other way to turn things into money, so it cannot be farmed.

### The daily cycle

A Minecraft day is 20 minutes. The village runs on VF's routines and calendar, and the player's day
fits around it.

| Time | What is on |
|---|---|
| 6:00 | You wake at home. Shops open around 7:00 |
| 8:00 to 18:00 | Mission Desk open |
| 9:00 to 12:00 | Academy lessons on weekdays (VF's children's lessons at 10:00 sit inside this) |
| Afternoon | Training, missions, jobs, friends |
| Evening | Ramen, events, festivals (events end by midnight) |
| Night | Go home and sleep |

Market Day (VF's seventh day) has no Academy and a half-day Mission Desk.

**Fatigue.** Sleeping in a bed at night skips to 6:00, as in vanilla. If you stay up, fatigue
builds:

| Stage | From | Effect |
|---|---|---|
| Tired | 00:00 | Movement −10%, chakra regen −25% |
| Exhausted | 03:00 | Movement −20%, chakra regen −50%, taijutsu and jutsu damage −20%, a darkened screen edge, chakra jumps may fall short |
| Collapse | 06:00 still awake | You pass out where you stand and wake in your bed at noon; timed missions lose the morning |

- **Your own bed** clears fatigue fully; sleeping before midnight also gives **Well Rested** (+10%
  chakra regen until noon).
- **Other beds** (the hospital, a camp bedroll on a multi-day mission, a clan quarter guest room)
  clear fatigue without the bonus.
- **Food and rest help:** green tea pushes the next stage back one game hour; a meal halves the
  movement penalty for an hour; a soldier pill hides fatigue for two minutes and then it returns.
- **Night duty:** night missions (ANBU, the Forest of Death) give *On Duty*, which delays fatigue by
  three hours; you sleep in the next morning.

### Death

- **Levels:** dying costs one level: your XP drops to the start of the level below. It never drops
  below your rank's floor ([Levels](#levels)), and you never lose a rank.
- **Missions:** dying on a mission fails it: no pay, and a small standing loss with the client.
- **Where you wake:** in the hospital the next morning, fatigue cleared, with your inventory.
  Thrown kunai and used tools are lost.

## 6. Progression

### Levels

Levels are power; ranks are story. You need both: every rank exam asks for a minimum level, and
reaching a level never promotes you by itself.

- **Levels 1 to 60.** XP comes from missions (most of it), training milestones, exams, events, jobs
  and fights. Fight XP falls off for repeated kills of the same kind (the RPG add-on's fatigue
  rule), and bandit camps refill only weekly.
- **Each level:** +3 maximum chakra and +1% taijutsu damage; +1 heart every 6 levels (10 hearts at
  level 1, 20 at level 60). Jutsu have a minimum level as well as a rank.
- **Rank floors:** the level you cannot fall below once you hold the rank.

| Rank | Exam needs level | Floor after promotion |
|---|---|---|
| Academy | — | 1 |
| Genin (graduation) | 5 | 5 |
| Chunin (Chunin Exams) | 15 | 15 |
| Jonin | 30 | 30 |
| ANBU (optional branch) | 35 | 35 |
| Hokage | 50 | 50 |

- **The pace:** about 30 to 45 minutes to level 5, 4 to 6 hours to 15, 15 to 20 hours to 30, and 40+
  hours to 50. The `ranks.json` file holds every number, as the RPG's `Balance` does.

### Academy student

- **Start:** after the prologue you are enrolled for the final term. No chakra bar yet; it appears
  after the first chakra lesson.
- **Milestones:** attend lessons (taijutsu forms, kunai and shuriken throwing at targets, chakra
  control by sticking a leaf to your forehead, the Transformation and Substitution basics), spar a
  classmate, and win one recess game with the Academy kids (VF `Playground`).
- **Exam: graduation** (level 5). A written quiz (five questions, from dialogue), a throwing test
  (hit 6 of 10 targets), and the **clone test**: weave Ram-Snake-Tiger and make at least three
  working clones in front of your instructor, the Chunin from the rescue. Failing costs nothing but
  time; you can retake it the next week.
- **Unlocks:** the forehead protector (headwear `w02_forehead_protector`), the Genin wardrobe
  (Scout, Brawler, Kunoichi, Tracker, Scroll Bearer looks from the README), the chakra bar, the
  first three jutsu, the Mission Desk, Training Ground 3. The stipend ends; missions pay.

### Genin

- **Team assignment:** a ceremony at the Academy places you with two NPC teammates and, as sensei,
  the captain who rescued you. Teammates are VF residents with clan or role looks; they follow you
  as companions on missions, have their own personalities and friendships, and talk.
- **Bell test:** the sensei's first test at Training Ground 3: take one of two bells in five
  minutes. You only pass if a teammate gets a bell too.
- **Missions:** D-rank chores from the Mission Desk (the VF notice board with Leaf skins:
  deliveries, weeding, catching the runaway cat, babysitting, gathering), then C-rank escorts and
  bandit clearing outside the walls.
- **Training:** tree walking (unlocks wall-running), water walking (on the training lake), and
  **choosing your first elemental nature** at the chakra paper ceremony, with your first elemental
  jutsu.
- **Eligibility for the Chunin Exams:** level 15, 8 D-rank and 2 C-rank missions, tree walking, and
  your sensei's recommendation (friendship with the sensei at a set level).
- **Residents:** Academy kids follow you about (the VF "curious child" behavior), shopkeepers call
  you by name, Genin your age treat you as a rival.

### Chunin

- **Exam: the Chunin Exams**, in three stages (an event, section 7):
  1. **Written test** in an Academy hall: ten questions too hard to answer; the real test is
     gathering answers unseen (Byakugan, transformation, a clone in the rafters, bribing a proctor
     in dialogue). Caught three times and your team is out.
  2. **[Forest of Death](https://naruto.fandom.com/wiki/Forest_of_Death):** your team gets one
     scroll of a pair (Heaven or Earth) and has five game days to reach the tower with both. Rival
     NPC teams carry the other scrolls. Survival, ambushes, traps, camping on bedrolls.
  3. **Preliminaries and finals:** if too many teams reach the tower, one-on-one preliminaries run
     in the arena inside the tower. The finals follow in the stadium, with residents watching from
     the stands. Promotion is judged on how you fought (techniques used, tactics, teamwork earlier),
     not only on winning, so losing a good final can still make you Chunin.
- **Unlocks:** the Chunin flak vest (wardrobe to build), B-rank missions, leading NPC Genin on
  missions, the outer training grounds, a flat or a clan room, the right to found a clan, and the
  **second nature** training (a master's three trials).
- **Residents:** Genin salute you, Chunin speak to you as a colleague, you are invited to clan
  gatherings.

### Jonin

- **Milestones:** level 30, 10 B-rank and 2 A-rank missions, lead three squad missions without
  losing a teammate (knockouts count as losses), master one A-rank jutsu.
- **Promotion:** a trial bout against a Jonin examiner and a review by the council (a scripted
  scene in the Hokage's office).
- **Unlocks:** the Jonin wardrobe (Leaf Jonin, Sentinel, Field, Kunoichi Jonin, Commander), A-rank
  missions, taking on your own Genin team (you assign their missions; they grow), the Jonin
  standby station, jutsu training from clan masters, a third nature through clan masters.

### ANBU (optional branch)

- **Recruitment:** an invitation after Jonin (level 35), if your record includes stealth missions
  and no bad deeds in the last season. A night test: infiltrate a guarded compound unseen.
- **Unlocks:** the ANBU masks and armor (Fox, Cat, Wolf Captain, Hawk Tracker, Root looks), ANBU
  HQ, S-rank and night missions, the right to wear the mask, which hides your identity: residents
  stop recognizing you while it is on. The Shimura storyline lives here.
- **Leaving:** you can return to regular Jonin duty at any time; the branch is never required.

### Hokage

- **Succession:** when you are a Jonin (ANBU or not), level 50, with the highest standing in every
  district and clan quarter (VF standing aggregated across the village), the Fourth announces
  retirement at the next New Year. A final crisis arc decides it: defend the village (section 7).
  Then the inauguration, and your face is carved as the fifth on the Rock (the map swaps the blank
  spot for a face built from your wardrobe look).
- **Unlocks:** the Kage hat and haori, the Hokage office and quarters, assigning missions to NPC
  teams, setting the festival calendar, approving promotions of residents and player-clan estates.

### Elemental natures

Fire, Wind, Lightning, Earth, Water. Your own natures' jutsu cost 25% less; other natures' jutsu
cannot be learned.

| Nature | How you get it |
|---|---|
| First | Chosen at the Genin chakra paper ceremony |
| Second | Chunin: a nature master's three trials |
| Third | Jonin: training with a clan master or a mission line |
| Fourth, fifth | Rare milestones: crisis arcs and the Hokage's archive |

### Clans

**Clan-born.** Choose one of the 15 clans at character creation. You are an orphan of that clan:
you wear its look, its residents know you as kin, you learn its signature technique at Genin from
a clan elder, and you may move into the clan's quarter from Chunin. The premise holds: you still
start in the Hokage's apartment.

**Clanless.** No clan technique, but every clan's elders will teach friends (friendship level 7 or
more) one lesser technique, and from Chunin on you can found your own clan.

### Player clans

A clanless player can found a clan at the clan registry in the Hokage Residence: Chunin, level 20,
20,000 ryo, and Good Neighbor standing or better.

- **The clan file.** A player clan is saved as a clan JSON in exactly the [CLANS.md](CLANS.md)
  format, in the world save (`narutominecraft/clans/<id>.json`). The runtime reads shipped and
  player clans with the same loader, so the shipped clans are also packaged as runtime data, not
  only compiled into pieces.
- **Clan editor** (a screen at the registry):
  - **Name** and an id prefixed `player_`, so it never collides with shipped ids.
  - **Colors:** a palette picker for the roles (`P` main color, `S` cloth, `A` trim and so on);
    the wardrobe already recolors pieces by palette, so new colors need no new art.
  - **Crest:** a 16 × 16 pixel editor, or a crest from a library built with `glyphs.py`. It is
    drawn on the back of tops and on the clan banner as a runtime texture.
  - **Look:** pick hairstyles, hair colors, eye colors and up to two marks (rects on the face, as
    in the clan file) from what the wardrobe has.
  - **Outfits:** up to four top-and-bottom pairs from pieces you own.
  - **Clan art:** one technique you have mastered becomes the clan's technique, taught to members.
  - **Clan day:** pick a date; it joins the calendar.
- **Members.** Recruit clanless residents at friendship level 7 or more who agree (their
  personality decides). They keep their face and name, take your clan's colors and outfits (their
  outfit is re-mixed from your clan file, as `clan_resident` does), and join your missions as
  teammates. Up to 3 at founding, 8 at Jonin, 20 as Hokage.
- **Home.** Claim one of the four vacant estates. It starts with a gate and a main hall; the dojo,
  kitchen, garden and members' houses open as you buy them. Members move in through VF Homes. Your
  crest goes on the gate and banners.

### Residents react to your rank

- **Rank in dialogue:** rank-specific greeting and reaction pools, added to VF's dialogue bank
  (`tools/dialogue/lines/naruto-*.txt`), keyed on the player's rank the way VF keys on standing.
- **Residents have ranks too:** every resident gets a rank from their outfit's `rank` field. A
  resident Genin may challenge you to spar; a Jonin may teach you; ANBU ignore lower ranks.
- **Greetings:** a salute clip for superiors, a nod for peers, an excited wave from kids (new
  `greet` clips in our resident animation pack).
- **Places:** gate guards and receptionists turn you away from places above your rank (the Forest
  of Death outside the exams, ANBU HQ, the Hokage's office) by dialogue, not barrier blocks.
- **Prices and favors:** VF standing already moves prices; rank adds a small discount at clan
  shops and free ramen on promotion day.

## 7. Events

All events run off VF's calendar (`social/Calendar`: 4 seasons of 28 days, 112 days a year, a
Minecraft day is 20 minutes, so a year is about 37 hours of play). Each event is a JSON file; an
**event director** on the server checks once a game minute which events start, run or end. Events
end by midnight so they never force fatigue, except night-duty events.

| Event | When | What happens | Reuses |
|---|---|---|---|
| Leaf Festival | Summer 14, evening | Stalls on the main street, lanterns, fireworks at 21:00 over the Hokage Rock, festival games for small ryo prizes (goldfish scooping, target throwing), yukata outfits to buy | Birthday party pattern (`Birthdays`), Market Day crowd behavior |
| New Year | Winter 28 → Spring 1 | Shrine visit, the Hokage's address, the succession if due (the one night event everyone stays up for: no fatigue until 02:00) | Calendar, VF news |
| Chunin Exams | Spring 15 to 21 and Autumn 15 to 21 | Written test (day 15), Forest of Death (16 to 20), finals (21). Run every season with NPC teams; the player joins when eligible | Fishing `Contest` as the pattern for entrants and results; `Seat` for spectators |
| Academy graduation | Spring 7 and Autumn 7 | Ceremony in the yard; the player's own graduation is the first one they pass | Lessons in VF's routine |
| Clan days (15, plus player clans) | One per clan per year, spread so no two fall in the same week | Senju and Uzumaki: founders' memorial at the shrine (Spring); Hyuga: main and branch house ceremony; Akimichi: harvest feast (Autumn); Inuzuka: ninken pairing, where children get their first pup; Nara: deer count in the forest; Yamanaka: flower festival (Spring); Uchiha: police parade; Sarutobi: the Will of Fire lantern walk (New Year eve); Aburame: insect night, with fireflies over the gardens (Summer); Hatake: a quiet visit to the memorial stone; Kurama: painting exhibition; Yuhi: grove viewing (Spring); Gekko: moon-viewing kenjutsu duels (Autumn full moon); Shimura: none in public, a beat of the ANBU branch instead; player clans: their chosen day | Party behavior, Hearth & Harvest dishes, VF pets for the pups |
| Border incident | Random, about weekly | Rogue ninja or bandits at a gate or on a road; a short fight, a deed, a small reward | VF guard call-out |
| Crisis arcs | Story-gated | The unique ninja plot, once each: (1) the bandits from the prologue were working for someone, and that thread leads to an invasion during your Chunin Exam finals; (2) an infiltration in the Jonin era; (3) the attack that decides the succession. Story beats are written with original characters | Guards, knockouts, the arena |

Event file sketch (`data/narutominecraft/naruto/events/leaf_festival.json`):

```json
{
  "id": "leaf_festival",
  "when": {"season": "summer", "day": 14, "from": "17:00", "to": "23:30"},
  "recur": "yearly",
  "requires": {},
  "where": "main_street",
  "routine": "festival",
  "activities": ["stalls", "goldfish_scooping", "target_throwing"],
  "moments": [{"at": "21:00", "do": "fireworks", "over": "hokage_rock"}],
  "news": "naruto.event.leaf_festival.news"
}
```

Story-gated events use `"requires": {"player_rank": "chunin", "story": "exam_finals"}` and
`"recur": "once"`. Stages of a crisis arc are listed in the same file. Crisis arcs never damage the
map: "damage" is dressing (smoke, rubble entities, closed streets) removed when the arc ends.

## 8. Combat

Combat runs on one **technique system**: every taijutsu move, dodge, jutsu and throw is a
technique with a cost, timing, animation and effect. The player's inputs and the NPC brains call
the same code, so enemies fight with what you fight with. Level scales the player's numbers;
fatigue reduces them.

### Taijutsu

| Mechanic | How in Minecraft | Custom animation |
|---|---|---|
| Combo chain | Empty hand or kunai in hand: left click is caught (client mixin on the attack key) and sent as a combo input; the server runs the chain. 3 light strikes, about 6 ticks apart, the third knocks back. Vanilla's attack cooldown does not apply inside a chain; a 10-tick recovery follows | 3 strike clips, the finisher |
| Heavy and launcher | Hold left click for 8 ticks: a heavy strike; during a chain it launches the target upward (velocity) for an air follow-up | 2 clips |
| Hit detection | Server-side sweep: a 60° arc, 3 blocks deep, in front of the attacker. Each combo hit lowers the target's hurt invulnerability (vanilla's 10 ticks) so chains land | |
| Dodge | Double-tap a direction or press `Left Alt`: a 4-block dash with 6 invulnerable ticks, 1.5 s cooldown, a little chakra | dash clips per direction |
| Block and parry | Right click with an empty hand: block (cuts melee damage 60%). Block within 4 ticks of a hit: parry, staggers the attacker | block, parry |
| Substitution | Pressing dodge as a hit lands, with enough chakra: you blink back 5 blocks and a log entity drops where you stood. Once per 20 s | the "poof" (particles), the log entity |

### Chakra-enhanced movement

Player movement in Minecraft is client-side, so these run on the client and the server checks and
charges chakra.

| Move | How | Custom animation |
|---|---|---|
| Ninja run | Sprinting with chakra: +15% speed, arms swept back | run cycle |
| Chakra jump | Hold jump to charge (up to 1 s), release for up to 3× jump height; no fall damage while chakra lasts | crouch-and-leap |
| Tree and roof hopping | Chakra jump plus a forward boost when jumping off leaves, logs or roof blocks | leap and land |
| Wall-running | Sprint into a wall: you run along it (gravity cut) or up it (vertical climb), up to 3 s, chakra drains; jump to kick off | wall-run cycle, kick-off |
| Water-walking | While chakra lasts and you are not sneaking, water holds you up: a mixin on `canStandOnFluid`, the method vanilla uses for striders on lava. Sneak to sink | slight crouch while standing on water |

### Ninjutsu

**Hand signs.** Twelve signs (Rat, Ox, Tiger, Hare, Dragon, Snake, Horse, Ram, Monkey, Bird, Dog,
Boar). Hold the **Weave** key (`R` by default): movement slows, a 12-sign radial appears, move the
mouse to a sign and left click to add it, release `R` to cast. Each sign takes 4 ticks and plays
its pose. A wrong sequence fizzles and wastes a little chakra. A jutsu used often enough becomes
**mastered**: it can be bound to one of four quick slots (`Z`, `X`, `C`, `V`) and cast with fewer
signs. Keys are rebindable; the radial also works on a controller.

**Chakra.** A bar beside hunger (synced attachment). It refills slowly, fast while meditating
(sneak and stand still), and from soldier pills (a Hearth & Harvest dish). Maximum chakra grows
with level. Running out leaves you drained: Slowness for 10 s. Fatigue slows regen.

**Elemental natures.** See [Elemental natures](#elemental-natures): chosen first, more earned.

| Jutsu | Signs | Minecraft mechanic |
|---|---|---|
| Clone | Ram-Snake-Tiger | Illusory clones: client-visible copies of you that run off in different directions; mobs may target them. No damage |
| Transformation | Dog-Boar-Ram | Your render switches to a chosen resident's look; mobs lose their target; residents do not recognize you |
| Shadow Clone (Chunin) | Cross sign (a 13th, special) | 2 to 4 real clone entities with basic combat AI; each costs a share of chakra; they vanish in a puff when hit |
| Fireball | Snake-Ram-Monkey-Boar-Horse-Tiger | Fire projectile like a blaze fireball, sets mobs alight; never breaks or burns blocks |
| Wind Blade / Gust | Snake-Ram-Boar | Vanilla's wind charge behavior: knockback, no block changes |
| Water Wall / Dragon | Tiger-Ox-Dragon (Wall) | A wave that pushes back and puts out fire; the dragon is a longer projectile |
| Earth Wall | Tiger-Hare-Boar-Dog | A wall entity on open ground that blocks movement and projectiles and crumbles after 10 s |
| Lightning Blade (Jonin) | Ox-Hare-Monkey | Charge 1 s, then a straight dash attack that breaks through a block or parry |

**Clan techniques.** Clan-born players learn their clan's signature technique at Genin; clanless
players can learn one lesser technique per friendly clan; a player clan's art is a technique its
founder mastered.

**Genjutsu.** Three clans (Kurama, Yuhi, Uchiha) use illusions, so genjutsu is one shared effect
type: a caught target sees a client-side illusion (fake entities, a distorted screen, a wrong HUD)
and moves slowly. It breaks when the target weaves the release sign (Ram, then the cast key),
takes damage, or a teammate touches them. NPCs under genjutsu stand dazed or attack the nearest
illusion.

| Clan | Technique | Minecraft mechanic | Animation |
|---|---|---|---|
| Hyuga | Byakugan, Gentle Fist | Living things within 32 blocks glow through walls (like Spectral); Gentle Fist hits drain the target's chakra instead of only health | eye veins (face decal), palm strikes |
| Uchiha | Sharingan | Enemy attacks telegraph earlier (a client flash), parry window doubles, and a jutsu you watch an enemy cast is learnable | glowing eyes (already in the wardrobe) |
| Nara | Shadow Possession | A shadow line crawls along the ground to a target within 12 blocks; if it reaches, the target copies your movement for 5 s. Needs light: weaker at night and indoors | kneeling sign hold |
| Akimichi | Expansion, Human Boulder | Vanilla's `scale` attribute: grow to 2× for 10 s with more reach and knockback; the boulder is a rolling charge | expand, roll |
| Yamanaka | Mind Transfer | Your camera moves into a mob or resident for 8 s and you steer it; your body slumps and can be hit. Late in the plan: it is the hardest technique | slump, sign |
| Inuzuka | Fang over Fang | A spinning dash attack together with your ninken (a tamed wolf, through VF's pet code) | spin |
| Senju | Wood Release | A short-lived wooden barrier or binding roots (entities, gone after a few seconds) | sign, wood growth |
| Uzumaki | Sealing chains, large chakra | 30% more chakra; chains that hold one target for 4 s | chains |
| Sarutobi | Fire mastery, Monkey staff | Fire jutsu cost 20% less; a summoned long staff with 4.5 reach that uses the combo system | staff combo |
| Aburame | Insect swarm | A swarm entity that follows a target for 10 s, drains chakra and marks it (it glows for the caster) | arms open, swarm particles |
| Hatake | Ninken trackers, chakra sabre | Summon a ninken that tracks a mission target or hidden enemy and leads you there; the white sabre is a tanto whose combo finisher is a lightning dash | summon, sabre strikes |
| Kurama | Painted illusion | Genjutsu: a painted world closes over one target for 6 s | brush strokes in the air |
| Shimura | Vacuum blades, sealing | Wind blades in a fan that break through a guard; a sealing curse used on ANBU-branch missions | breath blades |
| Yuhi | Tree binding | Genjutsu: the target sees itself bound by a tree and cannot move for 4 s; the caster appears behind it | sign, step-behind |
| Gekko | Dance of the Crescent Moon | Kenjutsu: two short-lived clones appear and all three strike a target at once from three sides | three-way slash |

### Ninja tools

Bought with ryo at the tool shop; consumed when used or lost.

| Tool | Item and mechanic |
|---|---|
| Kunai | Melee weapon that uses the combo system; right click throws it (a projectile like the trident) and it can be picked back up |
| Shuriken | Stackable, fast, low damage; throw three at once from Genin |
| Paper bomb | Tag on a kunai or stick on a surface; explodes after 3 s; damages entities, never blocks |
| Smoke bomb | A cloud that blinds, and makes mobs drop their target |
| Wire | Ties two points for a trap that trips and roots |
| Tool pouch | A bundle-like item that only holds tools and fills its slots into the hotbar quick-throw |

### Enemy and sparring AI

- **One shinobi entity** for every human enemy, drawn with VF's resident model and our wardrobe,
  so rogue ninja and exam rivals look like the residents.
- **Brain:** a state machine on top of vanilla goals: keep a range band (close for taijutsu, mid
  for throws, far for jutsu), strafe, dodge telegraphed attacks with a chance set by rank, use
  substitution once per fight, retreat to heal, call allies. Each enemy has a loadout file:
  techniques, rank, level, chakra, tools.
- **Sparring:** challenge a resident with a shinobi rank at a training ground. The fight ends when
  someone is down to 30% health or yields; nobody dies in a spar, the player included (no level
  loss), and residents never die anyway (VF knockouts). A win or a good fight raises friendship.
- **Difficulty:** by rank and level, not by health inflation: a Jonin reacts faster and uses more
  techniques.

### Animation

VF's clip system poses residents only (`ResidentLife`, `ResidentPoser`; the player is untouched).
For residents, our clips are a pack in our namespace (`assets/narutominecraft/resident_animations/`,
authored in Python like VF's `tools/animations/`), which VF already loads without Java: ninja
salutes, sparring stances, hand signs, meditation, guard duty on rooftops, and the rescue squad's
moves in the prologue.

For the player, we add a **player poser** that samples the same clip format onto the player model
(a client mixin on the player model's animation setup), with a first-person arm path for hand signs
and throws. This is the largest piece of custom client work and is Phase 0's spike and Phase 1's
main risk.

Clips needed, by phase: the prologue's crouch, slip-the-ropes and being carried, hand signs (12 +
the cross), the ninja run, chakra jump, combo strikes, heavy, dodge per direction, block, parry,
throw, meditation, a tired slouch (Phase 1 and 2); wall-run, water stance (2); clan techniques (4);
Mind Transfer and the advanced jutsu (5).

## 9. Technical architecture

### Shape

- **Mod:** `narutominecraft`, its own jar that **requires Village Friends** (like VF's `rpg/`).
  It extends VF from outside: VF's public events, mixins on VF classes where needed, data files in
  our namespace. When we need VF to expose something, we add a small public API to VF (as its
  `stable/api` does) rather than patch around it. Phase 0 needs three: extra wardrobe namespaces, a
  currency item for rewards and trades, and registering hand-built taverns (and other
  structure-read buildings) without structure pieces.
- **Code** (package `dev.narutominecraft`):

| Package | Owns | Pure, unit-tested core |
|---|---|---|
| `rank` | Ranks, milestones, levels and XP, promotions, death penalty | `Ladder`, `Milestones`, `Levels` |
| `story` | The prologue, story flags, cutscene scripts, crisis arcs | `StoryFlags` |
| `life` | Adventure rules, the daily cycle, fatigue, sleep, waking in hospital | `Fatigue`, `DayClock` |
| `home` | The player's home, furnish mode, furniture blocks, moving, upgrades | `FurnishRules` |
| `economy` | Ryo items, prices, stipend, shop tables, VF currency glue | `Prices` |
| `clan` | Clan loading (shipped and player), clan choice, the clan editor, members, estates | `ClanFile`, `Recruiting` |
| `chakra` | The chakra bar, regen, drain | `ChakraMath` |
| `technique` | Technique registry, hand-sign input, casting, cooldowns, effects, natures | `SignSequence`, `Mastery`, `Costs` |
| `combat` | Combos, dodge, block/parry, hit sweeps | `ComboTiming`, `HitArc` |
| `movement` | Ninja run, chakra jump, wall-run, water-walk | `WallRun` |
| `tools` | Kunai, shuriken, bombs, pouch: items and projectiles | |
| `shinobi` | The shinobi entity, its brain and loadouts | `RangeBands` |
| `mission` | Mission Desk, mission types, squads, rewards, failure | `MissionRoll` |
| `event` | Event director, festival behaviors | `EventClock` |
| `exam` | Graduation and Chunin Exam stages, judging | `Judging` |
| `map` | Districts, zones, access rules, the paste tool (builder mode only) | `Zones` |
| `village` | Resident ranks, rank dialogue, VF glue | |
| client `hud`, `anim`, `look`, `screens` | Chakra, XP, ryo and fatigue on the HUD; sign radial; player poser; player wardrobe look; character creation, furnish mode, clan editor | |

- **The player's look:** the player wears the Naruto wardrobe (chosen at character creation;
  outfits unlock by rank or are bought), drawn with VF's resident model. The look is part of the
  synced player attachment.
- **Tests:** the VF pattern: pure classes with JUnit tests, world glue thin, and client game tests
  with screenshots for each feature (`-Ptests=...`).

### Data-driven content

Everything that is content is JSON under `data/narutominecraft/naruto/`, validated on load (a bad
file is skipped and named in the log, as VF does for animation packs), and authored or checked by
Python tools under `tools/` with `--check`, matching the wardrobe.

| Folder | Holds |
|---|---|
| `ranks.json` | The ladder, milestones, level requirements and floors, XP curve, death penalty |
| `life.json` | Day schedule, fatigue stages and effects, sleep rules |
| `economy.json` | Ryo denominations, stipend, mission pay bands, sell-back rate |
| `shops/*.json` | Each shop's stock and prices |
| `furniture/*.json` | Furniture pieces: block, price, footprint, storage |
| `homes.json` | Apartments, flats, houses and estates: bounds, rank, price or rent |
| `clans/*.json` | The 15 shipped clans, in the CLANS.md format (player clans live in the world save) |
| `story/*.json` | Prologue steps, story flags, crisis arc stages |
| `techniques/*.json` | Every technique: signs, cost, cooldown, rank, level, nature, clip, effect type and numbers |
| `missions/*.json` | Mission types and templates: rank, objectives, places, pay, XP, dialogue pools |
| `events/*.json` | Calendar and story events |
| `exams/*.json` | Exam stages and judging weights |
| `loadouts/*.json` | Enemy and sparring partner kits |
| `districts.json` | Zones, access rules, spawn and wake points, the map layout's runtime part |

Technique sketch:

```json
{
  "id": "fireball",
  "signs": ["snake", "ram", "monkey", "boar", "horse", "tiger"],
  "mastered_signs": ["snake", "tiger"],
  "rank": "genin", "level": 8, "nature": "fire",
  "chakra": 30, "cooldown": 8.0,
  "clip": "narutominecraft.player:breath_fire",
  "effect": {"type": "projectile", "entity": "narutominecraft:fireball", "speed": 1.2, "damage": 6, "fire": 4}
}
```

Effect types are a fixed set in Java (`projectile`, `dash`, `area`, `summon`, `status`, `bind`,
`wall`, `transform`, `possess`, `illusion`); new jutsu are data unless they need a new effect type.
No effect type can change blocks.

### Saves

- **Player:** one Fabric attachment, copied on death and synced to its owner: rank, level and XP,
  milestones, story flags, missions in hand, mastered techniques, quick slots, natures, clan, look,
  team, home, fatigue.
- **World:** level attachments like VF's (`villagefriends:societies`, `notice_boards`): the event
  director's state, exam state and results, NPC teams, crisis arc progress, furniture ownership,
  player clans (with their clan JSON files beside the save).
- **Map version:** the save stores the map version. A new map release ships a new world; carrying
  a save forward is an export of the player attachment and home contents into the new map, not a
  re-paste of districts.

### Multiplayer (later)

Single player comes first. Because single player runs an integrated server, the code is written
server-authoritative from the start (chakra, cooldowns, hits, ryo and XP decided by the server),
which keeps multiplayer possible. What multiplayer would add later: squads of players, one
apartment per player, exam brackets between players, a rule for who becomes Hokage, sleeping when
not everyone is in bed, and latency testing of combat windows.

## 10. Phased plan

Each phase ends playable. "Done" means the listed criteria are true on a clean install of the
release jars and the map save.

### Phase 0: Foundations

**Deliverables**
- Gradle Fabric project for 26.3, `narutominecraft` jar requiring VF 2.29.x; CI build.
- VF hooks: residents wear our wardrobe (VF reads wardrobe textures and the catalog only from the
  `villagefriends` namespace today, see
  [ResidentSkins.java](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/src/client/java/dev/villagefriends/client/ResidentSkins.java)
  and [Wardrobe.java](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/src/main/java/dev/villagefriends/outfit/Wardrobe.java));
  a currency item for VF rewards and trades; taverns registered without structure pieces.
- A master map world: empty generator, border, VF and vanilla worldgen off; builder mode; the
  paste tool with one test street of pasted Konoha homes with House Plaques and a Village Marker.
- Adventure rules enforced (no breaking or placing outside builder mode).
- Player attachment skeleton; JSON loaders with validation; `tools/` `--check` scripts.
- A **spike** on the player poser: one clip playing on the player in third and first person.

**Done when**
- `gradlew build` and `python tools/wardrobe/wardrobe.py --check` pass in CI.
- In the test street, ten Leaf residents in Naruto wardrobe walk, blink, sleep in their own beds,
  eat and greet you, and a resident trade costs ryo.
- In survival or adventure, no block in the test street can be broken or placed.
- The player plays one test clip in both views without breaking the vanilla walk.

### Phase 1: Vertical slice — orphan to Genin

**Deliverables**
- **The opening:** character creation (look; clan or clanless), the bandit camp, the rescue squad
  as companions, the chase, the gate, the Hokage, the apartment.
- **Home:** the apartment, furnish mode, the furniture shop with the first Leaf set, chests.
- **Ryo:** notes, the orphan's stipend, part-time jobs at Ichiraku and the grocer, shop prices.
- **The day:** the daily schedule, sleeping, fatigue stages, Well Rested, waking in the hospital
  after death, levels 1 to 10 with the death penalty and rank floor.
- Konoha building kit v1 and the Academy district: the Academy (by hand), the yard, the apartment
  block, ~12 homes, Ichiraku, the furniture and grocer shops, the hospital, a street to the Hokage
  Residence, part of the wall with the main gate, the prologue hills.
- Academy outfits (wardrobe), Academy kids and the instructor with lesson routines.
- Chakra bar, hand-sign radial, Clone, Transformation and Substitution.
- Taijutsu v1: three-hit combo, heavy, dodge, block; practice kunai and shuriken at targets.
- Academy milestones and the graduation exam with the clone test; promotion to Genin with the
  headband and Genin wardrobe unlocked.
- Rank greeting pools for Academy and Genin; prologue and apartment dialogue.

**Done when**
- A new player plays from character creation through the rescue, a few days of Academy life and
  graduation to Genin in 60 to 90 minutes, with no commands.
- They can earn ryo, buy and place furniture in their apartment, store things in a chest, sleep
  every night, and feel fatigue if they stay up.
- Unit tests cover combo timing, sign matching, chakra, fatigue stages, level loss and furnish
  bounds; a client game test runs the prologue and the graduation with screenshots.

### Phase 2: Genin life

**Deliverables**
- Mission Desk (Hokage Residence ground floor) with D-rank (5 types, VF notice board under the
  hood) and C-rank (escort, bandit clearing, delivery to a far location by travel scene), paid in
  ryo and XP, failing on death.
- Team assignment with the rescue captain as sensei, and the bell test; NPC teammates as
  companions.
- Tree walking, wall-running, water-walking, chakra jump, ninja run.
- The nature ceremony (choose your first), one jutsu per nature; kunai throwing, shuriken, paper
  and smoke bombs, the tool pouch, the tool shop.
- The shinobi entity and brain v1: bandits and rogue Genin; weekly bandit camps.
- Training Grounds (Ground 3 by hand, two pasted), the market street. Levels to 20.

**Done when**
- From Genin, a player can reach Chunin Exam eligibility (level 15) in 4 to 6 hours, and the money
  curve matches the economy table (a week of play buys the first furniture set).
- Every mission type completes, and fails on death, in a client game test.
- Bandits use at least four techniques and dodge.

### Phase 3: The Chunin Exams

**Deliverables**
- Event director and the calendar events: Chunin Exams, Academy graduation, the Leaf Festival,
  New Year.
- The three exam stages: written test, Forest of Death (pasted trees and the tower) with bedroll
  camping and On Duty fatigue, tower preliminaries and stadium finals with seated spectators.
- NPC exam teams that run every season, with results in village news.
- Chunin wardrobe, B-rank missions, judged promotion, the Chunin flat, second-nature trials.
- Crisis arc 1, the invasion during your finals, closing the prologue's thread.

**Done when**
- The exams run with and without the player each season; a player can enter, finish all three
  stages and be promoted or not on judged performance; arc 1 plays start to finish.
- 150 seated residents in the arena keep 60 fps on a mid-range PC.

### Phase 4: Clans

**Deliverables**
- **4a:** the eight great clans merged (from `clan/*`), their compounds built and populated,
  their eight techniques (Mind Transfer may slip to Phase 5), their clan days, clan rooms for
  clan-born players.
- **4b:** the seven smaller clans (Sarutobi, Aburame, Hatake, Kurama, Shimura, Yuhi, Gekko),
  their clan homes, techniques and days, and the shared genjutsu effect.
- **4c: player clans.** The clan registry, the clan editor (name, palette, crest, look, outfits,
  clan art, clan day), clan JSON saved with the world, recruiting members, the four vacant estates
  and their halls.
- Lesser techniques taught to clanless friends; clan dialogue pools.

**Done when**
- All 15 clan quarters have their residents living there with homes, and each clan technique works
  for the player and for a clan sparring partner.
- A player can found a clan, design its crest and colors, recruit three residents who change into
  the clan's look and move into the estate, and see the clan's day in the calendar.

### Phase 5: Jonin and the ANBU branch

**Deliverables**
- A-rank missions, multi-stage missions at far locations, leading your own NPC Genin team.
- Jonin trial and council promotion; buying a house; third nature.
- The optional ANBU branch: invitation, masks and HQ, stealth missions (detection by sight and
  sound, night), S-rank missions, the Shimura storyline.
- Crisis arc 2. Mind Transfer, Lightning Blade, Shadow Clone balance. Levels to 50.

**Done when**
- A player can reach Jonin, and optionally ANBU and back; arc 2 plays start to finish.

### Phase 6: Hokage and the whole village

**Deliverables**
- Every remaining district and landmark: police HQ, the rest of the homes and shops, the full wall
  and gates, the Hokage Rock with its blank fifth spot.
- The succession, the final crisis arc, the inauguration, your face carved as the fifth.
- Hokage play: assigning NPC teams, setting festivals, approving promotions and clan estates.
- The map released as a downloadable save with the jars.

**Done when**
- The full ladder plays from the prologue to Hokage on one single-player save.

### Phase 7: Multiplayer (later)

Squads of players, a home per player, player brackets in the exams, a Hokage rule, shared sleep
and fatigue, and combat tested at 100 ms ping on a dedicated server. Planned after the
single-player map is complete.

### Risks

| Risk | Why | What we do |
|---|---|---|
| Player animation | VF poses residents only; the player model and first person are new code, and other mods touch them | Spike in Phase 0; keep clips in VF's format so the tools carry over |
| VF on a hand-made map | VF finds houses and taverns through generated structure pieces; our map has none | Plaques and markers for houses and settlements; a VF hook for taverns in Phase 0; test every VF system we use on the map world early |
| Combat feel | Minecraft combat is coarse (hurt invulnerability, 20 tick/s, client-side movement) | Server-decided hits with generous windows |
| Map building cost | 300+ buildings and landmarks, 15 clan quarters, 4 estates, all hand-placed or pasted | Paste everything repeatable from blueprints; hand-build only the landmarks; one district per phase |
| Economy and fatigue balance | Money too easy kills shopping; fatigue too harsh feels like a chore | All numbers in `economy.json`, `life.json` and `ranks.json`; playtest each phase against the rules of thumb |
| Runtime clan art | Player crests and palettes need textures made at run time, while the wardrobe is compiled offline | Palette recoloring already happens at run time; the crest is one dynamic decal layer; prototype it at the start of 4c |
| VF coupling | VF changes often (2.29 now); a change can break our mixins | Prefer VF public APIs; pin a VF version per release; run VF's tests with our jar |
| Performance | 150 to 250 residents with routines and societies in one area | Measure in Phase 0 and Phase 3; split Konoha into several VF settlements (one per district) if one society is too big |
| Minecraft 26.3 | A very new version: few libraries, mod compatibility | Stay on VF's version; avoid extra library dependencies |
| Naming and IP | Naruto names, symbols and places belong to their owners | Original characters and an original plot, as decided; cameos only later and sparingly; keep it a free fan project |

### Still open

1. **The Fourth Hokage and the four faces.** Original characters as decided: who are the four
   Hokage on the Rock, and is the sitting Fourth one of the rescuers' teachers or a stranger?
2. **Joining a clan later.** Can a clanless player be adopted into one of the 15 clans later (by
   friendship with its head), or is the clan choice only at character creation?
3. **Restricted clans.** Should every clan be open at character creation, including the
   near-vanished Uzumaki and Hatake, and Shimura with its ANBU-branch story?
4. **Death details.** Is losing one level (never below your rank's floor) and the tools you threw
   the right weight, or should dying also cost ryo (a hospital bill)?
5. **VF changes.** Phase 0 needs three small public hooks in VF (wardrobe namespaces, currency,
   hand-built taverns). OK to add them to VF itself?
6. **The RPG add-on.** Confirm the assumption that the map ships without it.
7. **README.** The README's ladder still lists ANBU as a rung; update it to the optional branch?
