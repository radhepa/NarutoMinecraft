# Shinobi Modpack: roadmap

From a wardrobe of Naruto-styled residents to the **Shinobi Modpack**: a modpack and adventure map
of the Hidden Leaf, where you arrive as an orphaned academy student and grow up to be Hokage.

This plan builds on [Village Friends](https://github.com/radhepa/Village-Friends-Minecraft-Mod)
(VF below) wherever VF already solves a problem. File links point at VF's `main` branch. VF
targets **Minecraft 26.3 on Fabric** (loader 0.19.5, Fabric API 0.161.0+26.3, Loom 1.17.21,
Java 25; VF 2.29.1, see its
[gradle.properties](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/gradle.properties)).
Every mod in the Shinobi Modpack targets the same versions and stays on them. Moving to another
Minecraft version is separate work, as it is for VF.

## 1. Vision

The Shinobi Modpack is a single-player adventure of the Hidden Leaf: a pack of separate mods plus a
hand-made map of one walled village under the Hokage Rock, full of residents who live their own
days. The full game runs about **100 hours** from the Academy to the Hokage's seat, so that
becoming Hokage feels earned. The first goal is a **beta from the Academy to Chunin** (about 25
hours), released in three playable slices and tuned by playtesting before the rest is built.

**The story.** You are an orphan. A Leaf squad raids a hideout of **Yūgure**, a band of missing-nin
from across the five nations, and carries you out. The Hokage enrolls you in the Academy and gives
you a small apartment. From there it is your life in the village: lessons, missions, money,
friends, a squad of your own, romance, a pet, and every night home to bed. You cannot break or
place blocks in the world. What you can do is earn ryo, buy and craft things, furnish your
apartment and fill its chests, grow up from an Academy kid into an adult, and learn why Yūgure
took you: you carry the blood of the **Kagari**, a clan the Leaf erased and buried in its own
history. Four Hokage look down from the Rock when you arrive. Three more will rise during your
story, and you are meant to become the **Eighth**.

The village matters more than the fighting. Residents wake, work, eat at Ichiraku, gossip, train,
fall in love and remember what you did. That is VF's resident model, which already runs routines,
friendships, romance, families, deeds and notice boards. The Shinobi Modpack dresses those
residents as shinobi and civilians of the Leaf, gives each one a rank, and adds what VF lacks:
ninja combat, chakra, jutsu, missions, exams, a day-and-night life for the player, a squad, and an
original ninja plot.

Progress has two halves. **Ranks** are story milestones: exams and promotions that change your
outfit, your missions, where you may go and how the village treats you. **Levels** are your power:
XP from missions, training and fights raises your chakra, health and strength, and each rank's
exam asks for a minimum level. Dying costs a level, and fails the mission you were on. About half
of every stretch is authored story and missions; the other half is the systemic loop: board
missions, training, life in the village, events and exploration. Combat is fast, readable and
forgiving by default: chained taijutsu, dodges, chakra-powered movement across roofs and water,
jutsu woven from hand signs, and thrown and crafted tools.

**Ladder:** Academy → Genin → Chunin → Jonin → Hokage, with **ANBU** as an optional branch from
Jonin.

## 2. Decisions

The owner's decisions, and the defaults recorded for questions the owner left to us (marked
*default*). Every section below follows them.

| Topic | Decision |
|---|---|
| Name and shape | The **Shinobi Modpack**: a modpack and adventure pack, not one jar. Each piece is a separate mod with a clear dependency direction, plus the map and a pack manifest ([Architecture](#10-technical-architecture)). |
| Scope now | **A beta from the Academy to Chunin** (about 25 hours), built in detail and released in three slices: Beta 1 the opening and the Academy (~6 h), Beta 2 Genin life (+~14 h), Beta 3 the Chunin Exams (+~5 h). Jonin, ANBU, Hokage and the post-game stay a brief outline until the beta has been played. |
| Length | The full game is about **100 hours** on the main path: Academy ~6 h, Genin ~14 h, Chunin Exams ~5 h, Chunin ~22 h, Jonin ~28 h, the road to Hokage ~25 h. The optional ANBU branch adds ~10 to 15 h. Every figure is tuned by playtesting. |
| Content mix | About half of each stretch is authored story and missions; the rest is the systemic loop (D- and C-rank board missions, training, life sim, events, exploration). |
| Villain | **Yūgure** (夕暮れ, "Dusk"), a band of missing-nin led by the last survivor of the erased **Kagari** clan; the player carries Kagari blood ([The story](#7-the-story)). |
| Hokage | All Hokage are original characters with custom faces. Four faces are on the Rock at the start; the Fifth to Seventh come during the story; the player is meant to become the **Eighth**. |
| Canon | Original characters only, maybe cameos of named characters. |
| Players | **Single player first.** Multiplayer is a later phase. The code stays server-authoritative (single player runs an integrated server), so it is not closed off. |
| World | A **fixed, hand-made map with a border**. Only the Leaf for now; more regions later, and the architecture leaves room for them. |
| Generation | Nothing is procedurally generated. Vanilla and VF world generation are off. Map tools paste blueprints at fixed spots while the map is being built. |
| Master world | Ships as a release asset (a zipped save on GitHub Releases), not in git. The repository keeps only what rebuilds or checks it: blueprints, paste scripts and the datapack. |
| VF's RPG add-on | Not shipped. |
| VF changes | *Default:* fine to add three small public APIs to Village Friends: extra wardrobe namespaces, a currency item, hand-built taverns. |
| Character creation | A creator screen at the opening: hair, eyes, skin and outfit from the wardrobe, and clan or clanless. |
| Growing up | Academy kid, teen, adult, then adult for good. No old age and no death of age ([Growing up](#growing-up)). |
| Clans | Born into one of the 15 clans or clanless. *Default:* all 15 are pickable at creation. *Default:* a clanless player can join a clan later through marriage or a clan's invitation at high friendship. A clanless player can also found a clan, including restoring the Kagari ([Player clans](#player-clans)). |
| Kekkei genkai | Playable through clan membership. Out of scope for now: summoning, and with it tailed beasts. |
| Squad | Teammates and sensei are original characters with personalities, friendship levels and connections, generated per save, then fixed. They can leave the squad ([Your squad](#your-squad)). |
| Romance | Friendships can grow into romance and marriage ([Romance and marriage](#romance-and-marriage)). |
| Pets | You can adopt a pet that follows you: a ninken pup or a cat. No summons ([Pets](#pets)). |
| Hunger | Vanilla hunger stays; food from shops and Ichiraku adds small buffs ([Food](#food)). |
| Gear | Shops, plus crafting at a **smithy** (kunai, shuriken, blades) and a **workbench** (paper bombs, smoke bombs, tags, furniture), station blocks in the world and in your apartment ([Gear and crafting](#gear-and-crafting)). |
| ANBU | An optional branch from Jonin, not a required rung. |
| Hand signs | Both typed key sequences and a radial menu, chosen in the settings. |
| Learning jutsu | A mix of mentors, scrolls bought with ryo, and mission rewards. |
| Elemental nature | You choose your first nature and gain more through training and milestones. |
| Death | Dying costs one level (never below your rank's floor) and the thrown tools you carry; on a mission, the mission fails. *Default:* no hospital bill. |
| Difficulty | Forgiving and cinematic by default, and tunable ([Difficulty](#difficulty)). |
| Story premise | Orphan rescued by a squad; the Hokage grants an apartment; no block breaking; buy things, earn money, store in chests; sleep each night, or stay up and grow tired and slower. |

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
  **Four faces** at the start and room for four more: the Fifth to Seventh, carved during the
  story, and yours, the Eighth. The streets fan out from its foot, so
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
| Hokage Rock | By hand | Voxel sculpting; four custom faces of original Hokage, and four blank spots: the Fifth to Seventh are carved at story beats, and the Eighth becomes the player's face. The village expands onto the plateau above it only in a much later era, so leave the top as forest ([Hokage Rock](https://naruto.fandom.com/wiki/Hokage_Rock)) |
| Hokage Residence | By hand | Circular, one of the largest buildings in the village, with 火 (fire) painted on the roof. It stands near the Academy, right below the faces. Mission desk on the ground floor, the clan registry, the Hokage's office upstairs ([Hokage Residence](https://naruto.fandom.com/wiki/Hokage_Residence)) |
| Ninja Academy | By hand | A large building at the base of the Hokage Rock, recognizable by the tree with a swing out front and a big 火 sign. Classroom, yard, target posts; the vertical slice. The office part is often confused with the Hokage Residence, but they are two buildings ([Ninja Academy file](https://naruto.fandom.com/wiki/File:Ninja_Academy.png), [Hokage Residence](https://naruto.fandom.com/wiki/Hokage_Residence)) |
| Ichiraku Ramen | By hand (small) | A VF tavern building (once the tavern hook exists), so the tavern code seats and serves residents |
| Shops: furniture, tools and weapons, clothes, grocer, tea house, barbecue house, dango, flower shop, scroll shop | Pasted or small hand builds | The furniture shop has a showroom of everything it sells, placed as display pieces. Flower shop belongs to the Yamanaka compound |
| Smithy and workshop | By hand | The weapon shop's forge (smithy station) and the Academy workshop (workbench), where players craft |
| Shrine | By hand | New Year visits and weddings |
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
| Shimura | Clan home | Close to the Hokage Rock, near the hidden ANBU entrance | Stern house; its cellar links to the ANBU branch's story |
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

1. **The creator screen.** Hair, eyes, skin (the six complexions), marks and a starting outfit from
   the wardrobe, all shown on your child-stage model; then born to one of the 15 clans (its look,
   and later its technique and kekkei genkai) or clanless.
2. **Captive.** You wake locked in a cell in a hidden camp in the hills south of the village, at
   dusk, among other children with unusual chakra. You learn to look, crouch and sneak by slipping
   out and hiding in the grass while guards in ash-violet cloaks pass.
3. **The raid.** A Leaf squad breaks into the Yūgure hideout: **the captain** (a Jonin, later your
   sensei), **a Chunin** (later your Academy instructor) and **a medic** (who works at the
   hospital). They are VF companions: you follow them, wait when told, and learn to dodge, sprint
   and climb while the squad fights. A chase through the forest ends with the captain carrying you
   over a ravine. Behind you, a cloaked figure with a sinking sun on its back watches you go.
4. **The gate at night.** The guards, the main street with its lanterns, the Rock with its four
   faces. The squad takes you to the Residence.
5. **The Hokage.** The Fourth Hokage enrolls you in the Academy, grants you an apartment and an
   orphan's stipend, and hands you the key. An elder at the Hokage's side looks at you a moment too
   long.
6. **Your apartment.** One room: a bed, a chest, a low table, a window. The Chunin shows you where
   the ramen stand and the Academy are. You sleep, and the game proper starts the next morning at
   6:00, when you meet your classmates, two of whom will be your squad.

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
- **What counts as furniture:** blocks tagged `shinobi_life:furniture`, plus chests and
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
- **Tools:** the thrown tools you carry (kunai, shuriken, bombs) are lost.
- **Missions:** dying on a mission fails it: no pay, and a small standing loss with the client.
- **Where you wake:** in the hospital the next morning, fatigue cleared, with the rest of your
  inventory. No bill.

### Food

Vanilla hunger stays. Food comes from shops, Ichiraku and the barbecue house, and from your own
cooking station (a Hearth & Harvest pot or prep table in your apartment). On top of vanilla
saturation, Leaf dishes give small, short buffs through VF's `WellFed` tiers: ramen restores a
little chakra, dango speeds chakra regen, barbecue raises taijutsu damage slightly, green tea holds
off fatigue. Buffs are small enough that skipping them never blocks progress.

### Gear and crafting

Shops sell everything you need. Crafting lets you make it cheaper and better, at **station
blocks**: placed in the world by the map (the smithy, the Academy workshop) and placeable in your
apartment in furnish mode, so crafting never needs block breaking.

| Station | Where | Makes |
|---|---|---|
| Smithy (forge and anvil) | The weapon shop's forge; a small forge for your apartment from Genin | Kunai, shuriken, senbon, tanto and later blades, from steel bought at the smithy and salvage from bandit camps |
| Workbench | The Academy workshop; one for your apartment from the Academy | Paper bombs, smoke bombs, wire, sealing tags, and furniture from planks and cloth |
| Cooking station | VF Hearth & Harvest pot, oven, prep table | Leaf dishes |

Recipes unlock by rank, by mentors (the smith teaches you after a few jobs at the forge) and by
scrolls. Crafted tools can be a grade better than shop stock (sharper kunai, bigger blasts). The
stations reuse VF's workstation pattern (`WorkstationBlock`, Hearth's `StationBlock` and its
screens), with recipes as data.

### Pets

Adopt a pet that follows you: a **ninken pup** from the Inuzuka clinic or a **cat** from the
shelter. Pets are vanilla wolves and cats tamed to you and driven by VF's pet code (`pet/`: the
`PetGoal` for following, resting and playing, pet tricks and pet play clips). Your pet follows you,
waits at home while you are on missions it cannot join, sleeps at the foot of your bed, and grows
with you: a ninken can learn to track scents on missions (the Inuzuka technique builds on this).
Pets are knocked out, never killed. Summoning stays out of scope.

### Romance and marriage

Friendships can grow into romance. VF already runs romance between residents (`social/`: meters,
`Chemistry`, sweethearts at meter 50, marriage after 30 to 150 days at 65 or more, households and
news). The pack extends it to the player:

- **Who:** residents of a similar age stage (teen with teen, adult with adult) who are single,
  including squadmates and classmates. Their personality and chemistry with you decide whether
  they are interested.
- **Dating:** at friendship level 7, a "spend time together" option opens: walks, ramen, festival
  nights. Confessing at level 8 makes you sweethearts (a news item, as VF does for residents).
- **Marriage:** adults only, at level 10, with a proposal and a wedding at the shrine (an event).
  Your spouse moves into your home (it must have room) and a clanless player may join the
  spouse's clan, or a spouse may join yours.
- **Children:** not in the beta; an open question for the post-game.

## 6. Progression


### Levels

Levels are power; ranks are story. You need both: every rank exam asks for a minimum level, and
reaching a level never promotes you by itself.

- **Levels 1 to 60.** XP comes from missions (most of it), training milestones, exams, events, jobs
  and fights. Fight XP falls off for repeated kills of the same kind (a rule borrowed from VF's RPG
  add-on, which the pack does not ship), and bandit camps refill only weekly.
- **Each level:** +3 maximum chakra and +1% taijutsu damage; +1 heart every 6 levels (10 hearts at
  level 1, 20 at level 60). Jutsu have a minimum level as well as a rank.
- **Rank floors:** the level you cannot fall below once you hold the rank.

The curve is planned against the 100-hour budget (main path; all numbers in `ranks.json` and tuned
by playtesting):

| Stretch | Hours (main path) | Cumulative | Levels | Exam needs | Floor after |
|---|---|---|---|---|---|
| Academy | ~6 | 6 | 1 → 6 | graduation: level 6 | 6 |
| Genin | ~14 | 20 | 6 → 18 | Chunin Exams: level 18 | — |
| Chunin Exams | ~5 | 25 | 18 → 21 | promotion by judging | 18 |
| Chunin | ~22 | 47 | 21 → 35 | Jonin trial: level 35 | 35 |
| Jonin | ~28 | 75 | 35 → 48 | road to Hokage opens at 48 | — |
| Road to Hokage | ~25 | 100 | 48 → 55 | succession: level 55 | 55 |
| ANBU (optional) | +10 to 15 | — | from 40 | invitation: level 40 | 40 |

Level 60 is post-game. XP per level rises gently, so each level takes about the same play time
within a stretch: about 1 hour per level in the Academy, 70 minutes as a Genin, 1.5 to 2 hours
later.

### Growing up

You grow up once and then stay an adult: three stages, no old age, no death of age.

| Stage | Age | When | Model |
|---|---|---|---|
| Child | 11 to 12 | From the prologue through the Academy and Genin years | The player model at **0.78** scale through vanilla's `scale` attribute (hitbox, eye height and reach follow it), with the head drawn 10% larger by the player poser for younger proportions |
| Teen | 13 to 17 | From your promotion to Chunin | **0.9** scale, normal head |
| Adult | 18 and up | From your promotion to Jonin; then fixed | **1.0** scale, forever |

- **Time skips.** The calendar alone would age you less than three years in 100 hours (a year is
  112 days, about 37 hours of play), so the story adds two skips: about a year between the Chunin
  Exams and your first Chunin missions, and about three years before the Jonin trial. Each skip is
  a short montage: the village changes, residents age, a Hokage may change.
- **Stage changes** happen at those skips, with a mirror scene where you may restyle hair and
  outfit for free.
- **Wardrobe:** the same pieces fit every stage, because the model is scaled, not changed. The rank
  outfits already line up with the stages: Academy and Genin outfits for the child, Chunin for the
  teen, Jonin, ANBU and Kage for the adult. A few pieces get a `stages` field in their META when
  they should only appear at some stages.
- **Residents:** VF's children are vanilla baby villagers with VF's baby transformer and their own
  games and lessons. Your classmates and squad are not babies: they are adult residents with a
  `stage` tag and the same `scale` values as you, so they keep shinobi routines and grow up
  alongside you.

### Your squad

Your classmates, teammates and sensei are original characters made for **your** save.

- **Made per save:** at the start of a new game the pack rolls the rescue captain (your sensei),
  four classmates (two become your teammates) and a rival, each with a random look from the
  wardrobe and the clan pools, a VF personality (warmhearted, playful, protective and the rest), a
  family in the village, and a name from VF's name pools. Once rolled they are fixed for that save.
- **Personality and friendship:** they are VF residents, so they use VF's ten friendship levels,
  relationship meters with each other and with their families (`social/`), personalities, speech
  bubbles, dialogue and gifts. Their personality also picks their fighting style (a protective
  teammate guards you, a playful one takes risks) in their combat loadout.
- **Connections:** each has ties the story uses: a sibling in the Academy, a parent in the police,
  a crush, a grudge with the rival. VF's census already stores families and relationships.
- **Growing:** they level, rank up and grow through the stages with you, and learn new techniques
  from their sensei and clans.
- **Leaving:** a teammate can leave the squad: if your friendship falls low and stays low, if they
  fail an exam you pass (or pass one you fail), or through the story (a stranger from Yūgure approaches one of them).
  They stay in the village and remember you. A classmate or a new Genin takes their place, and from
  Chunin on you can pick who joins your missions.
- **Never killed:** squad members are knocked out, not killed (VF `Knockouts`); losing one on a
  mission counts against your record.

### Academy student

- **Start:** after the prologue you are enrolled for the final term. No chakra bar yet; it appears
  after the first chakra lesson.
- **Milestones:** attend lessons (taijutsu forms, kunai and shuriken throwing at targets, chakra
  control by sticking a leaf to your forehead, the Transformation and Substitution basics), spar a
  classmate, and win one recess game with the Academy kids (VF `Playground`).
- **Exam: graduation** (level 6). A written quiz (five questions, from dialogue), a throwing test
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
- **Eligibility for the Chunin Exams:** level 18, about 30 D-rank and 6 C-rank missions, tree walking, and
  your sensei's recommendation (friendship with the sensei at a set level).
- **Residents:** Academy kids follow you about (the VF "curious child" behavior), shopkeepers call
  you by name, Genin your age treat you as a rival.

### Chunin

- **Exam: the Chunin Exams**, in three stages (an event, section 8):
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

- **Milestones:** level 35, 10 B-rank and 2 A-rank missions, lead three squad missions without
  losing a teammate (knockouts count as losses), master one A-rank jutsu.
- **Promotion:** a trial bout against a Jonin examiner and a review by the council (a scripted
  scene in the Hokage's office).
- **Unlocks:** the Jonin wardrobe (Leaf Jonin, Sentinel, Field, Kunoichi Jonin, Commander), A-rank
  missions, taking on your own Genin team (you assign their missions; they grow), the Jonin
  standby station, jutsu training from clan masters, a third nature through clan masters.

### ANBU (optional branch)

- **Recruitment:** an invitation after Jonin (level 40), if your record includes stealth missions
  and no bad deeds in the last season. A night test: infiltrate a guarded compound unseen.
- **Unlocks:** the ANBU masks and armor (Fox, Cat, Wolf Captain, Hawk Tracker, Root looks), ANBU
  HQ, S-rank and night missions, the right to wear the mask, which hides your identity: residents
  stop recognizing you while it is on. The Shimura storyline lives here.
- **Leaving:** you can return to regular Jonin duty at any time; the branch is never required.

### Hokage

- **The Hokage before you:** four original Hokage are on the Rock at the start, each with a custom
  face built in the map. The Fifth is named after the Chunin Exam attack; the Sixth and Seventh serve
  during the Chunin and Jonin years (outline). Each new Hokage's face is carved into the Rock at a
  story beat.
- **Succession:** when you are a Jonin (ANBU or not), level 55, with the highest standing in every
  district and clan quarter (VF standing aggregated across the village), the Seventh names you as
  successor, and the last Yūgure arc is the trial ([section 7](#7-the-story)). Then the
  inauguration, and your face is carved as the **Eighth** (built from your wardrobe look).
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
| Fourth, fifth | Rare milestones: story arcs and the Hokage's archive |

### Clans

**Clan-born.** Choose one of the 15 clans at character creation. You are an orphan of that clan:
you wear its look, its residents know you as kin, you learn its signature technique at Genin from
a clan elder, and you may move into the clan's quarter from Chunin. The premise holds: you still
start in the Hokage's apartment.

**Clanless.** No clan technique and no kekkei genkai, but every clan's elders will teach friends
(friendship level 7 or more) one lesser technique, and from Chunin on you can found your own clan.
A clanless player can still join a clan later, through marriage or a clan's invitation at high
friendship. Whatever you choose, you carry Kagari blood ([section 7](#7-the-story)).

### Player clans

A clanless player can found a clan at the clan registry in the Hokage Residence: Chunin, level 25,
20,000 ryo, and Good Neighbor standing or better.

**Restoring the Kagari.** Once the story has revealed your Kagari blood, the registry offers a
second path: restore the Kagari under their old name and crest instead of inventing a clan. It
uses the same editor, starting from the Kagari's palette, crest and look, and the clan's art is the
Kagari ability once you have awakened it. A clan-born player may also restore the Kagari, leaving
their birth clan.

- **The clan file.** A player clan is saved as a clan JSON in exactly the [CLANS.md](CLANS.md)
  format, in the world save (`shinobi_progression/clans/<id>.json`). The runtime reads shipped and
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

## 7. The story

All characters are original; named canon characters appear only as cameos. The plot is data in the
adventure map's datapack (story flags, cutscene scripts, missions and events), so it can be
rewritten without touching the mods.

### Yūgure

**Yūgure** (夕暮れ, "Dusk") is a band of missing-nin from across the five nations. Like the great
rogue organizations of the shinobi world, they work in **two-man cells** and wear **ash-violet
cloaks marked with a sinking sun**. Their creed: *the shinobi world must end at dusk so that a true
dawn can come.* They gather orphans with unusual chakra, and they want you.

**The Kagari.** Yūgure's leader is the last survivor of the **Kagari** clan (篝, "bonfire"), a
clan of the Warring States period erased in the wars that founded the Leaf. The Leaf buried that
past: the Kagari are missing from its histories and its memorial stones, and only one elder knows
the truth. It gives the village a dark history of its own, as the Uchiha's does.

**You.** The orphan carries Kagari blood. That is why Yūgure took you, and why the squad found you
in that hideout. If you chose a clan at creation, the Kagari blood is your other parent's; if you
are clanless, it is all you have. Later in the story it opens the [player clan](#player-clans)
choice: restore the Kagari under their old name and crest, or found a new clan of your own.

**The Kagari ability** is an open design question. It should feel like a bonfire (chakra that
flares, gathers and spreads like flame) and must not reuse a canon kekkei genkai's name or power.
In the beta it shows only as an uncontrolled flare.

### The beta's beats (Academy to Chunin)

| Stretch | Beats |
|---|---|
| Academy | Strange watchers: a cloaked figure on a rooftop at night, a sinking-sun mark scratched on your door, a stranger asking your classmates about you. In a sparring lesson your chakra flares in the shape of fire and scorches the training post; your instructor hushes it up and the elder takes note. Graduation |
| Genin | Missions brush against Yūgure's cells without knowing it: smuggled chakra paper on a merchant's cart, a missing orphan from a border village, a two-man team that slips past your squad on a C-rank escort. Your sensei starts to suspect what you are; a teammate is approached by a stranger |
| Chunin Exams | Yūgure infiltrates the exam (a foreign team that is not what it seems), stalks your team in the Forest of Death, and attacks the stadium during the finals. In the chaos a cloaked figure stops in front of you and says the name **Kagari**. The Fourth Hokage falls defending the village; the Fifth is named |

### Later, in outline

These are sketched now and written after the beta has been played.

- **Chunin:** after the time skip, missions follow Yūgure's trail; the Kagari ability awakens and
  must be trained in secret; your first clues to the buried history.
- **Jonin:** a traitor elder is unmasked: the elder who knew the truth and fed Yūgure names. The
  truth about the Kagari comes out, and the village must face what it did. The Sixth and Seventh
  Hokage serve through these years.
- **ANBU (optional):** covert operations against Yūgure's cells, and the Shimura storyline.
- **Road to Hokage:** you can restore the Kagari, the leader of Yūgure comes for the Leaf and for
  you, and the defence of the village is the succession's trial. Then the inauguration, and your
  face is carved as the Eighth.

## 8. Events

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
| Weddings | When a couple marries (residents or the player) | A ceremony at the shrine with family and friends, then a party | VF romance and marriage, party behavior |
| Clan days (15, plus player clans) | One per clan per year, spread so no two fall in the same week | Senju and Uzumaki: founders' memorial at the shrine (Spring); Hyuga: main and branch house ceremony; Akimichi: harvest feast (Autumn); Inuzuka: ninken pairing, where children get their first pup; Nara: deer count in the forest; Yamanaka: flower festival (Spring); Uchiha: police parade; Sarutobi: the Will of Fire lantern walk (New Year eve); Aburame: insect night, with fireflies over the gardens (Summer); Hatake: a quiet visit to the memorial stone; Kurama: painting exhibition; Yuhi: grove viewing (Spring); Gekko: moon-viewing kenjutsu duels (Autumn full moon); Shimura: none in public, a beat of the ANBU branch instead; player clans: their chosen day | Party behavior, Hearth & Harvest dishes, VF pets for the pups |
| Border incident | Random, about weekly | Rogue ninja or bandits at a gate or on a road; a short fight, a deed, a small reward | VF guard call-out |
| Crisis arcs | Story-gated | The unique ninja plot, once each: Yūgure ([section 7](#7-the-story)): watchers in the Academy years, cells brushing past your Genin missions, the attack on the Chunin Exam finals, then (in outline) the traitor elder, the truth about the Kagari, and the leader's attack that decides the succession | Guards, knockouts, the arena |

Event file sketch (Progression's format, in the map's datapack `shinobi_adventure`):

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

## 9. Combat

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
Boar). Hold the **Weave** key (`R` by default) and movement slows; then enter signs in one of two
ways, chosen in the settings:

- **Typed:** each sign has a key (by default the twelve keys `1` to `0`, `-` and `=`, rebindable);
  type the sequence, release `R` to cast. Fast for players who learn the sequences.
- **Radial:** a 12-sign wheel appears; move the mouse (or a controller stick) to a sign and click to
  add it, release `R` to cast. Easier to learn, and the wheel shows the signs of jutsu you know.

Each sign takes 4 ticks and plays its pose. A wrong sequence fizzles and wastes a little chakra. A
jutsu used often enough becomes **mastered**: it can be bound to one of four quick slots (`Z`, `X`,
`C`, `V`) and cast with fewer signs.

**Learning jutsu.** A jutsu must be learned before its signs do anything, in one of three ways
(each technique file lists which apply):

- **Mentors:** your sensei, clan elders and nature masters teach at friendship and level
  thresholds, with a short trial.
- **Scrolls:** the scroll shop sells basic and C-rank jutsu for ryo; reading one teaches it.
- **Mission rewards:** rarer techniques come from mission results, exam placings and story beats.

Then practice makes it mastered.

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

**Clan techniques and kekkei genkai.** Clan-born players learn their clan's signature technique
at Genin, and a clan with a **kekkei genkai** (Uchiha's Sharingan, Hyuga's Byakugan, Senju's Wood
Release) passes it on: it unlocks through a clan milestone (the Sharingan awakens in a story moment
of danger, the Byakugan through Hyuga training). Kekkei genkai come only through clan membership.
Clanless players can learn one lesser technique per friendly clan, never a kekkei genkai; a player
clan's art is a technique its founder mastered. **Summoning is out of scope for now**, and with it
tailed beasts.

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
| Sarutobi | Fire mastery, clan staff | Fire jutsu cost 20% less; the clan's long staff (an item, not a summon) with 4.5 reach that uses the combo system | staff combo |
| Aburame | Insect swarm | A swarm entity that follows a target for 10 s, drains chakra and marks it (it glows for the caster) | arms open, swarm particles |
| Hatake | Ninken tracker, chakra sabre | Your ninken (a companion dog through VF's pet code, not a summon) tracks a mission target or hidden enemy and leads you there; the white sabre is a tanto whose combo finisher is a lightning dash | summon, sabre strikes |
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

### Difficulty

Forgiving and cinematic by default, and tunable.

| Setting | Story (default) | Shinobi | Hard |
|---|---|---|---|
| Parry and dodge windows | 6 and 8 ticks | 4 and 6 | 3 and 5 |
| Enemy telegraphs | long, with a flash | normal | short |
| Enemy damage | 60% | 100% | 130% |
| Death | lose one level, never below the rank floor | the same | two levels, and 10% of your ryo |
| Fatigue | starts at 01:00 | 00:00 | 23:00 |
| Cinematic camera on finishers and jutsu | on | on | off |

Every number lives in data (`difficulty.json` in Shinobi Core, overridden per world), and players
can change the setting at any time in the pack's settings screen.

### Animation

VF's clip system poses residents only (`ResidentLife`, `ResidentPoser`; the player is untouched).
For residents, our clips are a pack in our namespace (`assets/narutominecraft/resident_animations/`,
authored in Python like VF's `tools/animations/`), which VF already loads without Java: ninja
salutes, sparring stances, hand signs, meditation, guard duty on rooftops, and the rescue squad's
moves in the prologue.

For the player, we add a **player poser** that samples the same clip format onto the player model
(a client mixin on the player model's animation setup), with a first-person arm path for hand signs
and throws. This is the largest piece of custom client work and is Phase 0's spike and Beta 1's
main risk.

Clips needed, by phase: the prologue's crouch, slip-the-ropes and being carried, hand signs (12 +
the cross), the ninja run, chakra jump, combo strikes, heavy, dodge per direction, block, parry,
throw, meditation, a tired slouch, petting and pet play (Beta 1); wall-run, water stance, forging and
workbench clips, the first clan techniques (Beta 2); the Yūgure fighters and the stadium crowd (Beta 3);
Mind Transfer and the advanced jutsu (later).

## 10. Technical architecture


### The pack: separate mods

The Shinobi Modpack ships as a modpack plus a map. Each piece is its own mod with its own jar, and
dependencies run one way. Village Friends stays its own mod; we only add small public APIs to it.

| Piece | Mod id | Owns | Depends on |
|---|---|---|---|
| **Village Friends** | `villagefriends` | Residents, routines, society, dialogue, homes, taverns, notice boards, calendar, knockouts, animation clips | Fabric API. Unchanged except three small public APIs: extra wardrobe namespaces, a currency item for rewards and trades, registering hand-built taverns without structure pieces |
| **Shinobi Core** | `shinobi_core` | The shared player record (rank, level, age stage, clan id, difficulty), a stat-modifier registry, the event bus, data loading and validation, the settings screen, the wallet and region interfaces | Fabric API |
| **Shinobi Village** (the Naruto content mod) | `narutominecraft` (today's wardrobe namespace) | The wardrobe, the 15 clans and the clan loader (shipped and player clan files), resident ranks and looks, Leaf residents, the character creator and the player's look, age-stage scaling, the resident animation pack and dialogue pools, Konoha decor blocks | Village Friends, Shinobi Core |
| **Shinobi Combat** | `shinobi_combat` | Chakra, techniques, hand-sign input, elemental natures, kekkei genkai, genjutsu, taijutsu, chakra movement, ninja tools, the shinobi enemy entity and its AI, sparring, the player poser | Shinobi Core, Shinobi Village (enemies use the resident model and wardrobe; clips use VF's format) |
| **Shinobi Life** | `shinobi_life` | Adventure rules, the player's home, furniture and furnish mode, moving, ryo, shops and jobs, crafting stations (smithy, workbench), food buffs, pets, romance and marriage with the player, the daily cycle, sleep, fatigue, waking at home or in hospital | Shinobi Core, Village Friends (homes, plaques, trades) |
| **Shinobi Progression** | `shinobi_progression` | Ranks, levels and XP, the death penalty, missions, exams, the event director, the squad, the story engine (flags, cutscenes, time skips), player clans (registry, editor, members, estates), residents reacting to rank | Shinobi Core, Shinobi Village, Shinobi Combat, Shinobi Life, Village Friends |
| **Shinobi Adventure** (the map) | world save (a GitHub Release asset) + datapack `shinobi_adventure` | The hand-made Leaf with its border; the story, quests, missions, events, shop stock, homes, districts and regions as data | Every mod above |
| **Pack manifest** | `pack/` | A Modrinth `.mrpack` (and a CurseForge export) pinning Minecraft 26.3, Fabric Loader 0.19.5, Fabric API, Village Friends and every Shinobi mod by version and hash, with the map world and default config as overrides | — |

```text
Fabric API
 ├── Village Friends ─────────────┐
 └── Shinobi Core                 │
      ├── Shinobi Village ◄───────┤
      │    └── Shinobi Combat     │
      ├── Shinobi Life ◄──────────┘
      └── Shinobi Progression ◄── Village, Combat, Life
           └── Shinobi Adventure (map + datapack) ◄── everything
```

**How the mods talk without tangling.** Lower mods never call higher ones. They meet in Shinobi
Core:

- **Events:** `RankChanged`, `LevelChanged`, `PlayerDied`, `DayStarted`, `MissionEnded`,
  `TechniqueLearned`, `AgeStageChanged`. Progression publishes rank and level; Life publishes the
  day; Combat listens.
- **Stat modifiers:** Life's fatigue writes movement, damage and chakra-regen modifiers into the
  registry; Combat reads chakra regen from it; movement and damage use vanilla attributes, so they
  work even without Combat.
- **Wallet:** Life implements it with ryo; Progression pays mission rewards and charges the clan
  fee through it. Without Life, rewards fall back to XP only.
- **Player record:** rank, level, age stage and clan id live in Core, so Village can scale the
  model for the age stage and Combat can grant the clan's kekkei genkai without depending on
  Progression.

### Each mod on its own

| Mod | Usable or testable alone |
|---|---|
| Shinobi Core | Unit tests; no content |
| Shinobi Village | In any VF world: residents wear the Naruto wardrobe and clans, the creator screen dresses the player, age stages scale the model |
| Shinobi Combat | With Village: every technique works in any world; techniques are unlocked by a command or an "all techniques" setting when Progression is absent; a test arena game test |
| Shinobi Life | In any VF world: claim a house with a plaque as your home, furnish it, trade in ryo, sleep and feel fatigue. Adventure rules are a game rule, off by default outside the map |
| Shinobi Progression | With the mods it depends on: ranks, levels, generic missions and events from its default data, in any VF world |
| Shinobi Adventure | Only as the full pack |

### Repository layout

This repository becomes a Gradle multi-project, the way VF hosts `rpg/`: `core/`, `village/`
(today's wardrobe resources move here), `combat/`, `life/`, `progression/`, `adventure/` (the
datapack, blueprints and paste scripts) and `pack/` (the manifest). Python authoring tools stay
under `tools/`. Each mod has its own version; the pack manifest pins a tested set.

The master world is **not** in git. It ships as a release asset (a zipped save on GitHub
Releases); the repository keeps only what rebuilds or checks it: blueprints, paste scripts and the
datapack.

### Code by mod

| Mod | Packages | Pure, unit-tested core |
|---|---|---|
| Core | `record`, `events`, `stats`, `data`, `settings`, `wallet`, `region` | `Difficulty`, `StatMath` |
| Village | `wardrobe`, `clan`, `resident`, `look` (creator, age stages), client `render` | `ClanFile`, `AgeStage` |
| Combat | `chakra`, `technique`, `combat`, `movement`, `tools`, `shinobi`, client `anim`, `hud`, `signs` | `SignSequence`, `Mastery`, `Costs`, `ComboTiming`, `HitArc`, `WallRun`, `RangeBands` |
| Life | `rules`, `home`, `furniture`, `economy`, `craft`, `food`, `pet`, `romance`, `day`, client `furnish`, `hud` | `Fatigue`, `DayClock`, `FurnishRules`, `Prices`, `Courtship` |
| Progression | `rank`, `level`, `mission`, `exam`, `event`, `squad`, `story`, `playerclan`, `reaction`, client `screens` | `Ladder`, `Levels`, `MissionRoll`, `Judging`, `SquadRoll`, `StoryFlags`, `Recruiting` |

Every mod follows the VF pattern: pure classes with JUnit tests, thin world glue, and client game
tests with screenshots (`-Ptests=...`).

### Data-driven content

Each mod ships its engine with generic default data; the adventure map's datapack overrides it with
the Leaf's content. Files are JSON, validated on load (a bad file is skipped and named in the log),
and authored or checked by Python tools under `tools/` with `--check`.

| Data | Owner (default data) | The map's datapack adds |
|---|---|---|
| `difficulty.json`, settings defaults | Core | Per-world overrides |
| Wardrobe, `clans/*.json` (the CLANS.md format) | Village | — |
| `techniques/*.json`, `loadouts/*.json` | Combat | Enemy loadouts for Yūgure and bandits |
| `life.json` (day, fatigue, sleep), `economy.json`, `furniture/*.json`, `shops/*.json`, `homes.json` | Life | The Leaf's shops, stock, apartments and estates |
| `ranks.json` (ladder, levels, floors, XP curve), `missions/*.json`, `exams/*.json`, `events/*.json`, `squad.json` | Progression | The Leaf's missions, exams and calendar |
| `story/*.json` (flags, prologue, arcs, cutscenes) | Progression (engine only) | The whole plot |
| `districts.json`, `regions/*.json` | Core (format) | Zones, access rules, wake points, the Leaf region |

Technique sketch (Combat):

```json
{
  "id": "fireball",
  "signs": ["snake", "ram", "monkey", "boar", "horse", "tiger"],
  "mastered_signs": ["snake", "tiger"],
  "rank": "genin", "level": 8, "nature": "fire",
  "learn": ["mentor:fire_master", "scroll:fire_c", "reward"],
  "chakra": 30, "cooldown": 8.0,
  "clip": "shinobi_combat.player:breath_fire",
  "effect": {"type": "projectile", "entity": "shinobi_combat:fireball", "speed": 1.2, "damage": 6, "fire": 4}
}
```

Effect types are a fixed set in Combat (`projectile`, `dash`, `area`, `status`, `bind`, `wall`,
`transform`, `possess`, `illusion`); new jutsu are data unless they need a new effect type. No
effect type can change blocks.

### Regions

Only the Leaf ships now, but travel is designed in. A **region** is a dimension declared by the
map's datapack (an empty generator, a border, pasted builds, entry points) and registered through
Core's region interface. The Leaf is the first region. Far mission locations are small regions
reached from the travel desk at the main gate with a short travel scene. New regions (other
villages, the lands where Yūgure hides) are added as datapack regions plus their world
data, with no mod changes.

### Saves

- **Player:** each mod keeps its own Fabric attachment on the player (Core's record; Combat's
  chakra and techniques; Life's home, fatigue and wallet state; Progression's milestones, missions,
  story flags and squad), copied on death and synced to the owner.
- **World:** level attachments like VF's: the event director's state, exam results, the squad's
  rolled characters, story progress, furniture ownership, and player clans with their clan JSON
  files beside the save.
- **Map versions:** a new map release ships a new zipped world; carrying a save forward exports the player
  attachments and home contents into the new map.

### Multiplayer (later)

Single player comes first. Because single player runs an integrated server, the code is written
server-authoritative from the start (chakra, cooldowns, hits, ryo and XP decided by the server),
which keeps multiplayer possible. What multiplayer would add later: squads of players, one home per
player, exam brackets between players, a rule for who becomes Hokage, sleeping when not everyone is
in bed, and latency testing of combat windows.

## 11. Phased plan

The plan is built around a **beta from the Academy to Chunin** (about 25 hours), delivered in three
playable slices. Each slice is a release: the `.mrpack` with every mod pinned, plus the zipped map
world on GitHub Releases. Each slice is playtested and tuned before the next starts. Everything
after Chunin stays an outline until the beta has been played.

Each deliverable names the mod it lands in: **Core**, **Village**, **Combat**, **Life**,
**Progression**, **Map** (the world, its blueprints and its datapack), **Pack** (the manifest and
releases), **VF**.

Hours are the main path for a first-time player at the Story difficulty, about half authored and
half systemic. They are targets, adjusted by playtests.

### Phase 0: Foundations

**Deliverables**
- **Pack:** the Gradle multi-project (`core/`, `village/`, `combat/`, `life/`, `progression/`,
  `adventure/`, `pack/`), CI building every jar, a `.mrpack` that pins them with VF 2.29.x, and a
  release job that zips the master world as a GitHub Release asset.
- **VF:** the three public APIs: extra wardrobe namespaces (VF reads wardrobe textures and the
  catalog only from the `villagefriends` namespace today, see
  [ResidentSkins.java](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/src/client/java/dev/villagefriends/client/ResidentSkins.java)
  and [Wardrobe.java](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/src/main/java/dev/villagefriends/outfit/Wardrobe.java)),
  a currency item, hand-built taverns.
- **Core:** the player record, events, stat modifiers, data loading, settings and difficulty.
- **Village:** today's wardrobe moved into the content mod; residents wear it; the clan loader; the
  creator screen v1; age-stage scaling.
- **Life:** adventure rules as a game rule (no breaking or placing outside builder mode).
- **Combat:** the player poser spike: one clip on the player in third and first person.
- **Map:** the master world (empty generator, border, VF and vanilla worldgen off, builder mode),
  the paste tool, one test street of pasted homes with House Plaques and a Village Marker.

**Done when**
- CI builds every jar, the `.mrpack` installs in a launcher with the zipped world, and
  `wardrobe.py --check` passes.
- Each mod loads on its own with only its dependencies (a CI job boots each one).
- In the test street, ten Leaf residents in Naruto wardrobe walk, blink, sleep in their own beds,
  eat and greet you, and a resident trade costs ryo.
- The creator dresses a child-stage player; nothing in the test street can be broken or placed.

### Beta 1: The opening and the Academy (~6 h)

| Content | Authored (~3 h) | Systemic (~3 h) |
|---|---|---|
| What | The prologue (~20 min); 8 Academy story beats (the first day, the rival, the fire-shaped flare, the watchers, a classmate's family, the elder's visit, the exam eve, graduation); 2 short side stories per classmate | About 18 in-game days of Academy life: 12 lessons (forms, throwing, chakra control, Transformation, Substitution, Clone), part-time jobs, furnishing, crafting at the workbench, friendships with classmates and neighbours, adopting a pet, Ichiraku |

**Deliverables**
- **Village:** the full creator screen (hair, eyes, skin, outfit; clan or clanless, all 15 clans);
  Academy outfits; Academy kids and the instructor with lesson routines; the child stage.
- **Life:** the apartment and furnish mode; the furniture shop's first Leaf set; chests; ryo, the
  orphan's stipend, jobs at Ichiraku and the grocer; the daily schedule, sleep, fatigue, Well
  Rested, waking in hospital; vanilla hunger with Leaf dish buffs; the workbench; pets (a pup or a
  cat).
- **Combat:** chakra; both hand-sign inputs (typed and radial, chosen in settings); Clone,
  Transformation and Substitution; taijutsu v1 (three-hit combo, heavy, dodge, block); practice
  kunai and shuriken; the Story difficulty.
- **Progression:** levels 1 to 6 with the death penalty and floors; the squad rolled per save
  (sensei, four classmates, a rival); Academy milestones and the graduation exam with the clone
  test; promotion to Genin with the headband and Genin wardrobe; the story engine and the Academy
  beats.
- **Map:** the prologue (the Yūgure hideout, the raid, the chase); the Academy district (the
  Academy, the yard, the apartment block, ~12 homes, Ichiraku, the furniture and grocer shops, the
  workshop, the hospital, a street to the Hokage Residence, part of the wall with the main gate);
  the Hokage Rock with its four custom faces; a gate and main hall for each of the 15 clan quarters
  so clan-born players have kin from day one.

**Done when**
- Playtesters finish Beta 1 in 5 to 7 hours (median) with no commands, from the creator screen to
  Genin.
- They earn ryo, buy, craft and place furniture, store things in a chest, sleep every night, feel
  fatigue if they stay up, and have a pet following them; their classmates have names,
  personalities and friendship levels.
- Unit tests cover combo timing, sign matching, chakra, fatigue, level loss, furnish bounds and the
  squad roll; client game tests run the prologue and the graduation with screenshots.

### Beta 2: Genin life (+~14 h)

| Content | Authored (~7 h) | Systemic (~7 h) |
|---|---|---|
| What | Team assignment and the bell test; 4 story C-rank missions (~45 min each) that brush against Yūgure's cells; the training arcs (tree walking, water walking, the nature ceremony, your clan's technique from an elder); 2 side stories per teammate, one with a stranger approaching them; the sensei's suspicion | About 42 in-game days: ~30 D-rank board missions (10 to 15 min each), ~6 board C-ranks (escorts, bandit camps, deliveries to a far location), crafting at the smithy, training, jobs, friendships, events (the Leaf Festival) |

**Deliverables**
- **Progression:** the Mission Desk with D-rank (5 types, VF notice board under the hood) and
  C-rank (escort, bandit clearing, delivery by travel scene), paid in ryo and XP, failing on death;
  team assignment and the bell test; teammates who can leave; mentors who teach; levels 6 to 18;
  the event director with the Leaf Festival and New Year.
- **Combat:** tree walking, wall-running, water-walking, chakra jump, ninja run; the nature
  ceremony and one jutsu per nature; the 15 clan signature techniques (first tier) and the first
  stage of each kekkei genkai; thrown kunai, shuriken, paper and smoke bombs, the tool pouch; the
  shinobi entity and brain v1 (bandits, rogue ninja, Yūgure scouts).
- **Life:** the tool shop and the scroll shop; the smithy and its recipes; crafted tool grades.
- **Core:** the region interface and the first far-location region.
- **Map:** Training Grounds (Ground 3 by hand, two pasted), the market street, the weapon shop
  and forge, the Inuzuka clinic, the full 15 clan quarters, bandit camps, the far-location region.

**Done when**
- Playtesters go from Genin to Chunin Exam eligibility (level 18) in 12 to 16 hours (median),
  learning jutsu from a mentor, a bought scroll and a mission reward; a week of play buys the first
  furniture set.
- Every mission type completes, and fails on death, in a client game test.
- Bandits use at least four techniques and dodge; each clan technique works for a clan-born player
  and a clan sparring partner.

### Beta 3: The Chunin Exams (+~5 h)

| Content | Authored (~3.5 h) | Systemic (~1.5 h) |
|---|---|---|
| What | The written test (~30 min); the Forest of Death (~1.5 h, five in-game days); the tower preliminaries (~30 min); the finals and Yūgure's attack (~1 h); promotion, the Fourth's fall, the Fifth named, and the time-skip montage (~15 min) | The training break between the preliminaries and the finals (sparring, the sensei's lessons, crafting, the festival crowds) |

**Deliverables**
- **Progression:** the Chunin Exams as a calendar event, with NPC teams every season and results in
  village news; the three stages; judged promotion; the first time skip and the teen stage; the
  Fifth Hokage's face on the Rock.
- **Combat:** Yūgure enemies in two-man cells with their own loadouts; the uncontrolled Kagari
  flare as a story moment.
- **Life:** bedroll camping and On Duty fatigue in the forest.
- **Village:** the Chunin wardrobe; teen-stage outfit checks.
- **Map:** the Forest of Death (pasted trees and the tower) and the stadium with seated spectators;
  the attack dressing (smoke, rubble entities, closed streets).

**Done when**
- The whole beta plays from the creator screen to Chunin in 20 to 30 hours (median).
- The exams run with and without the player each season; a player can enter, finish all three
  stages and be promoted or not on judged performance; Yūgure's attack plays start to finish.
- 150 seated residents in the stadium keep 60 fps on a mid-range PC.

### Playtesting the beta

- Every slice goes to playtesters before the next is built. The pack writes an opt-in local play
  log (time per stretch, deaths, ryo earned and spent, missions taken, fatigue hits) that testers
  can send with their notes.
- Tuning happens in data (`ranks.json`, `economy.json`, `life.json`, `difficulty.json`,
  missions), not code, so a balance pass is a datapack update.
- After Beta 3, the hour budget for the later stretches is revisited with real numbers.

### Later, in outline

Written in detail after the beta.

- **Chunin (~22 h):** the teen stage after the time skip; dating opens; B-rank missions; the Kagari
  ability awakens; second nature; the Chunin flat and moving; founding a player clan (or later,
  restoring the Kagari); the Sixth Hokage.
- **Jonin (~28 h):** the second time skip and the adult stage; marriage; a house; A-rank missions
  and far regions; your own Genin team; third nature; the traitor elder and the truth about the
  Kagari; the Seventh Hokage.
- **ANBU branch (+10 to 15 h, optional):** masks and HQ, S-rank and covert missions against Yūgure,
  the Shimura storyline.
- **Road to Hokage (~25 h):** the rest of the village, restoring the Kagari, Yūgure's leader, the
  defence of the Leaf, the succession and your face as the Eighth; the post-game.
- **Multiplayer (later):** squads of players, a home per player, exam brackets, a Hokage rule,
  shared sleep, combat at 100 ms ping.
- **More regions (later):** other villages and the lands where Yūgure hides, as datapack regions.

### Risks

| Risk | Why | What we do |
|---|---|---|
| Content volume | 100 hours is a lot of game; half of it hand-written | Half systemic by design; the beta first, measured before writing more; all story as data so writers do not need Java |
| Player animation | VF poses residents only; the player model and first person are new code, and other mods touch them | Spike in Phase 0; keep clips in VF's format so the tools carry over |
| VF on a hand-made map | VF finds houses and taverns through generated structure pieces; our map has none | Plaques and markers for houses and settlements; a VF hook for taverns in Phase 0; test every VF system we use on the map world early |
| Separate mods drifting | Six mods, VF and a map must stay in step | One repository and one CI for all Shinobi mods; the pack manifest pins a tested set; a CI job boots each mod alone and the whole pack together |
| Coupling between mods | It is tempting to call a higher mod directly | Only Core's events, record, stat modifiers and interfaces cross mod lines; CI checks that a jar only references the mods it declares |
| Romance and age | The beta's characters are children | Romance is limited to the same age stage and opens at teen; children only have friendships and VF's harmless crushes in dialogue. Enforced in code, not just content |
| Growing residents | VF children are vanilla babies; squadmates grow through custom stages | Squadmates are adult residents scaled by the `scale` attribute with a stage tag; test their routines in each stage |
| Combat feel | Minecraft combat is coarse (hurt invulnerability, 20 tick/s, client-side movement) | Server-decided hits, generous windows on the Story difficulty |
| Map building cost | The Academy district, 15 clan quarters, training grounds, the forest and the stadium for the beta alone | Paste everything repeatable from blueprints; hand-build only the landmarks; clan quarters as cores first |
| Economy and fatigue balance | Money too easy kills shopping; fatigue too harsh feels like a chore | Every number in data and on the difficulty settings; playtest each slice |
| Runtime clan art | Player crests and palettes need textures made at run time, while the wardrobe is compiled offline | Palette recoloring already happens at run time; the crest is one dynamic decal layer; prototype it before player clans |
| VF changes | VF changes often (2.29 now); a change can break our mixins | Public APIs; pin a VF version per pack release; run VF's tests with our jars |
| Performance | 150 to 250 residents with routines and societies in one area | Measure in Phase 0 and Beta 3; split Konoha into several VF settlements (one per district) if one society is too big |
| Minecraft 26.3 | A very new version: few libraries, mod compatibility | Stay on VF's version; avoid extra library dependencies |
| Naming and IP | Naruto names, symbols and places belong to their owners | Original characters, Hokage and plot; cameos only; the pack's own name; keep it a free fan project |

### Still open

1. **The content mod's id.** Keep `narutominecraft` (the wardrobe's namespace today) or rename it
   to `shinobi_village` before anything depends on it? Kept as `narutominecraft` for now.
2. **The Kagari ability.** What exactly does it do? A bonfire-like chakra, with no canon kekkei
   genkai name or power.
3. **Children.** Can a married player have children in the post-game?
4. **Romance in the beta.** The beta's player is a child until the last time skip, so dating opens
   just after Beta 3. Is that right, or should the beta end on the time skip with dating unlocked
   as a teaser?
