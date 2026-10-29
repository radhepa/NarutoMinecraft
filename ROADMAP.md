# Shinobi Modpack: roadmap

From a wardrobe of Naruto-styled residents to the **Shinobi Modpack**: a modpack and adventure map
of the Hidden Leaf, where you arrive as an orphaned academy student and grow up to be the Eighth
Hokage.

**No spoilers here.** This roadmap describes systems, formats, the map and the plan, with neutral
chapter descriptions. The plot, its twists and its characters' secrets are in a separate,
developers-only [story bible](docs/story/STORY_BIBLE.md). Do not open it if you want to play the
game unspoiled.

**How to read this plan.** We build the first **~15 hours** (the beta, Academy to Chunin) and lay
out the foundations of the whole **~60-hour** story without building it yet. Every section carries
one of two tags:

- **BUILD (beta):** what we build now, in full detail.
- **FOUNDATION (later):** laid out so the beta plants the right seeds and the formats hold it, but
  not built until the beta has been played.

This plan builds on [Village Friends](https://github.com/radhepa/Village-Friends-Minecraft-Mod)
(VF below) wherever VF already solves a problem. File links point at VF's `main` branch.

## Contents

| # | Section | Tag |
|---|---|---|
| 1 | [Vision](#1-vision) | both |
| 2 | [Decisions](#2-decisions) | both |
| 3 | [Where we start](#3-where-we-start) | BUILD (beta) |
| 4 | [Technical architecture](#4-technical-architecture) | BUILD (beta) |
| 5 | [Data formats built for the whole story](#5-data-formats-built-for-the-whole-story) | BUILD (beta) |
| 6 | [The map](#6-the-map) | BUILD (beta) districts, FOUNDATION (later) for the rest |
| 7 | [Systems in the beta](#7-systems-in-the-beta) | BUILD (beta) |
| 8 | [The beta, chapter by chapter](#8-the-beta-chapter-by-chapter) | BUILD (beta) |
| 9 | [Delivery plan](#9-delivery-plan) | BUILD (beta) |
| 10 | [Story bible](#10-story-bible) (spoilers, in a separate file) | FOUNDATION (later) |
| 11 | [Later systems](#11-later-systems) | FOUNDATION (later) |
| 12 | [Risks and open questions](#12-risks-and-open-questions) | both |

## 1. Vision

*Both.*

The Shinobi Modpack is a single-player adventure of the Hidden Leaf: a pack of separate mods plus a
hand-made map of one walled village under the Hokage Rock, full of residents who live their own
days.

**The story.** You are an orphan. A Leaf squad rescues you from a rogue ninja hideout, and the
Hokage enrolls you in the Academy and gives you a small apartment. From there it is your life in the
village: lessons, missions, money, friends, a squad of your own, a pet, and every night home to
bed. You cannot break or place blocks in the world. What you can do is earn ryo, buy and craft
things, furnish your apartment and fill its chests, grow up from an Academy kid into an adult, and
find out who took you and why. Four Hokage look down from the Rock when you arrive; one day your
face is meant to join them.

**Length.** The main path from the Academy to Hokage is about **60 hours**: Academy ~4 h, Genin
~8 h, Chunin Exams ~3 h, Chunin ~13 h, Jonin ~17 h, the road to Hokage ~15 h. The optional ANBU
branch adds ~8 h. Side quests, filler arcs and the life sim take a completionist run to **100 hours
or more**. Hokage is earned through requirements, exams and story, not padding.

**The beta.** The first 15 hours of main path (Academy to Chunin), released in three playable
slices: Beta 1, the opening and the Academy (~4 h); Beta 2, Genin life (~8 h); Beta 3, the Chunin
Exams (~3 h). Side quests come on top of each slice.

The village matters more than the fighting, and most of it belongs to no great clan: civilians,
clanless shinobi with ordinary family names, and families of the minor clans. Residents wake, work, eat at Ichiraku, gossip,
train,
fall in love and remember what you did. That is VF's resident model, which already runs routines,
friendships, romance, families, deeds and notice boards. The Shinobi Modpack dresses those
residents as shinobi and civilians of the Leaf, gives each one a rank, and adds what VF lacks:
ninja combat, chakra, jutsu, missions, exams, a day-and-night life for the player, a squad, and an
original ninja plot.

**Every save can feel different.** At world creation you choose **Classic** (a curated cast and
order) or **Varied** (cast, families, side-quest arcs, missions, shops and your apartment rolled
from the save's seed). The main plot beats are the same in both.

**Ladder:** Academy → Genin → Chunin → Jonin → Hokage, with **ANBU** as an optional branch from
Jonin.

## 2. Decisions

*Both.* The owner's decisions, and the defaults recorded for questions the owner left to us (marked
*default*). Every section follows them.

| Topic | Decision |
|---|---|
| Name and shape | The **Shinobi Modpack**: a modpack and adventure pack, not one jar. Separate mods with a one-way dependency direction, plus the map and a pack manifest ([Architecture](#4-technical-architecture)). |
| Build scope | **The first ~15 hours** (Academy to Chunin), detailed fully and built in three slices. The whole ~60-hour story is laid out as foundations: a story bible, seeds in the beta, and data formats that hold the later arcs without a rewrite. |
| Length | Main path ~60 h (Academy ~4, Genin ~8, Chunin Exams ~3, Chunin ~13, Jonin ~17, road to Hokage ~15); ANBU branch +~8 h; completionist 100 h or more. All tuned by playtesting. |
| Side quests | A ton of optional side quests and anime-filler-style arcs, outside the main-path hour budget, as data in the Adventure datapack ([Side quests](#side-quests-in-the-beta)). |
| World creation | **Classic** (curated, fixed cast and order) or **Varied** (rolled from one save seed, reproducible). Main plot beats fixed in both ([World creation](#world-creation-classic-or-varied)). |
| Minecraft version | Stay on VF's version, **Minecraft 26.3, Fabric Loader 0.19.5**, pinned for the whole beta. No version chasing mid-beta; port only between beta slices, if VF moves. |
| Story and villain | An original antagonist and plot, kept in the developers-only [story bible](docs/story/STORY_BIBLE.md). The story specifics are the developers' creative call, so the owner can play it unspoiled. |
| No spoilers | ROADMAP.md and the README stay spoiler-free: systems, formats, the map, the delivery plan and neutral chapter descriptions only. Every twist lives in the story bible. |
| Bond ability | **Kindling Bond**: you can kindle a bonded ally's chakra nature or technique and borrow it briefly; deeper bonds (teammates, sensei, friends, spouse) unlock more, and it is one of the ways to gain more natures. A bond-flame flickers between you and the ally. Unlocked by a story moment after the beta ([Kindling Bond](#kindling-bond)). |
| Hokage | All Hokage are original characters with custom faces. Four faces are on the Rock at the start; the player is meant to become the **Eighth**. Their **names are rolled per save**; their looks, clans and eras are fixed, because faces, portraits and statues are baked into the map. |
| Names | **Most character names are rolled per save, in Classic and Varied alike**: squadmates, sensei, rivals, elders, recurring characters and the antagonists. Roles, personalities and looks stay as designed (Classic stays curated in everything but names). Given names come from seeded pools by gender; family names from the character's clan, or from the ordinary `family_names` pool in `tools/wardrobe/population.json`. All text uses name tokens ([Names](#names-rolled-per-save)). |
| Rotating story roles | Some story roles are assigned per save from a few candidates, each with its own seeded clue trail, so a twist still surprises a player who knows the answer from another save ([Rotating story roles](#rotating-story-roles)). Which roles rotate, and the candidates, are in the story bible only. |
| Canon | Original characters only, maybe cameos of named characters. |
| Players | **Single player first.** Multiplayer is later. The code stays server-authoritative (single player runs an integrated server). |
| World | A **fixed, hand-made map with a border**. Only the Leaf for now; more regions later, with room left in the architecture. |
| Generation | Nothing is procedurally generated. Vanilla and VF world generation are off. Map tools paste blueprints at fixed spots while the map is being built. |
| Master world | Ships as a release asset (a zipped save on GitHub Releases), not in git. The repository keeps only what rebuilds or checks it: blueprints, paste scripts and the datapack. |
| Content mod id | `narutominecraft`, kept. |
| VF's RPG add-on | Not shipped. |
| VF changes | *Default:* fine to add small public APIs to VF: extra wardrobe namespaces, a currency item, hand-built taverns, and a resident appearance seed (for Varied saves). |
| Character creation | A creator screen at the opening: hair, eyes, skin and outfit from the wardrobe, and clan or clanless. |
| Growing up | Academy kid, teen, adult, then adult for good. No old age and no death of age. |
| Clans | 25 clans: the 15 noble clans and 10 minor clans ([CLANS.md](CLANS.md)). Born into one of them or clanless. *Default:* all 25 pickable at creation, alongside clanless; a player can also create their own clan. *Default:* a clanless player can join a clan later through marriage or a clan's invitation at high friendship. |
| Population | The village is mostly clanless, drawn by clan rarity from `tools/wardrobe/population.json` (weights per thousand): about 45% civilians, 28% clanless shinobi with ordinary family names, 15% from the 10 minor clans and 13% from the 15 noble clans (an Uchiha or a Hyuga about 1 in 70, a Hatake about 1 in 500). Civilians wear their own clothing collections (market and household); the general shinobi wardrobe adds 100 tops, 100 bottoms and 50 hairstyles ([Population](#population)). |
| Kekkei genkai | Playable through clan membership. Out of scope for now: summoning, and with it tailed beasts. |
| Squad | Teammates and sensei are original characters with personalities, friendship levels and connections, fixed per save (curated in Classic, rolled in Varied). They can leave the squad. |
| Romance | Friendships can grow into romance and marriage, from the teen stage. Foundation only for now: nothing romantic in the beta, and the beta does not end on a time skip or a dating unlock. |
| Children | A married player can have children in the post-game (a life-sim foundation). |
| Pets | Adopt a pet that follows you: a ninken pup or a cat. No summons. |
| Hunger | Vanilla hunger stays; food from shops and Ichiraku adds small buffs. |
| Gear | Shops, plus crafting at a **smithy** (kunai, shuriken, blades) and a **workbench** (paper bombs, smoke bombs, tags, furniture), station blocks in the world and in your apartment. |
| ANBU | An optional branch from Jonin, not a required rung. |
| Hand signs | Both typed key sequences and a radial menu, chosen in the settings. |
| Learning jutsu | A mix of mentors, scrolls bought with ryo, and mission rewards. |
| Elemental nature | You choose your first nature and gain more through training and milestones. |
| Death | One level lost (never below your rank's floor) and the thrown tools you carry; on a mission, the mission fails. *Default:* no hospital bill. |
| Difficulty | Forgiving and cinematic by default, and tunable. |
| Story premise | Orphan rescued by a squad; the Hokage grants an apartment; no block breaking; buy things, earn money, store in chests; sleep each night, or stay up and grow tired and slower. |

## 3. Where we start

*BUILD (beta).*

| Have | Where |
|---|---|
| Naruto wardrobe: hair, tops, bottoms, headwear, faces, palettes, eye colors (Sharingan, Byakugan), compiled from Python | `tools/wardrobe/` → `src/main/resources/assets/narutominecraft/wardrobe/` |
| 21 characters with a `rank`: Genin, Jonin, ANBU and kage/signature looks | `tools/wardrobe/characters/`, renders in `docs/renders/` |
| Clan system: clan JSON, resident mixing after VF's OutfitFactory, id blocks per clan | [CLANS.md](CLANS.md), `tools/wardrobe/clans/` |
| The 15 noble clans merged into the wardrobe (535 compiled pieces): Senju, Uzumaki, Uchiha, Hyuga, Nara, Akimichi, Yamanaka, Inuzuka, Sarutobi, Aburame, Hatake, Kurama, Shimura, Yuhi, Gekko | `tools/wardrobe/clans/`, renders in `docs/renders/clans/` |
| Id blocks for 10 minor clans: Shiranui, Morino, Umino, Haruno, Namiashi, Hagane, Kinoshita, Tsuchigumo, Suzuran, Tobari | [CLANS.md](CLANS.md) |
| Population weights and collections: residents drawn by clan rarity; clanless and civilian residents mix across collections (core, academy_genin, field, kunoichi, specialist, rugged for shinobi; market and household for civilians) and take ordinary family names | `tools/wardrobe/population.json`, `tools/wardrobe/collections/`, `render.py --village` |

| Missing | Notes |
|---|---|
| Any Java: no mod, entities, items or gameplay | Phase 0 |
| The minor clans' and new collections' pieces | Id blocks are reserved; the market and household collections are the civilians' wardrobe |
| Chunin outfits | Still to come (README) |
| Buildings, furniture, the map, animations for ninja | Phase 0 to Beta 3 |

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
economy, player fatigue, player romance, quests beyond notice boards, a fixed hand-made map, and
anything Japanese in its building kit.

**Where VF assumes generated villages.** VF finds a village's houses and its tavern through the
village *structure pieces* that world generation leaves behind (`home/HouseSurvey`,
`tavern/TavernSurvey`). Our map has none. Houses still work: a House Plaque flood-fills a
hand-built house into a home. Settlements work through the Village Marker. The tavern needs a small
VF hook so a hand-built building can be registered by marker or by bounds (Phase 0).

## 4. Technical architecture

*BUILD (beta).*

### Versions

Every mod in the pack targets VF's version: **Minecraft 26.3, Fabric Loader 0.19.5**, Fabric API
0.161.0+26.3, Loom 1.17.21, Java 25 (VF 2.29.1, see its
[gradle.properties](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/gradle.properties)).
These are pinned for the whole beta. If VF moves to a new Minecraft version, the pack ports
between beta slices, never during one.

### The pack: separate mods

The Shinobi Modpack ships as a modpack plus a map. Each piece is its own mod with its own jar, and
dependencies run one way. Village Friends stays its own mod; we only add small public APIs to it.

| Piece | Mod id | Owns | Depends on |
|---|---|---|---|
| **Village Friends** | `villagefriends` | Residents, routines, society, dialogue, homes, taverns, notice boards, calendar, knockouts, pets, animation clips | Fabric API. Unchanged except small public APIs: extra wardrobe namespaces, a currency item, hand-built taverns, a resident appearance seed |
| **Shinobi Core** | `shinobi_core` | The shared player record (rank, level, age stage, clan id, difficulty), the **save seed** and its derived streams, the **condition and action language**, story flags, the event bus, stat modifiers, data loading and validation, settings, the wallet and region interfaces | Fabric API |
| **Shinobi Village** (the Naruto content mod) | `narutominecraft` | The wardrobe, the 25 clans, the collections, the population draw and the clan loader, Leaf residents spawned from map markers (curated or rolled), name rolling and name tokens, resident ranks, the character creator and the player's look, age-stage scaling, the resident animation pack and dialogue pools, Konoha decor blocks | Village Friends, Shinobi Core |
| **Shinobi Combat** | `shinobi_combat` | Chakra, techniques, hand-sign input, elemental natures, kekkei genkai, genjutsu, taijutsu, chakra movement, ninja tools, the shinobi enemy entity and its AI, sparring, the player poser | Shinobi Core, Shinobi Village |
| **Shinobi Life** | `shinobi_life` | Adventure rules, the player's home, furniture and furnish mode, moving, ryo, shops and jobs, crafting stations, food buffs, pets, player romance, the daily cycle, sleep, fatigue, waking at home or in hospital | Shinobi Core, Village Friends |
| **Shinobi Progression** | `shinobi_progression` | Ranks and milestones, levels and XP, the death penalty, the **quest engine** (main chapters, side quests, filler arcs, board missions), exams, the event director, the squad and roles, rotating story roles (twist slots), cutscenes and time skips, player clans, residents reacting to rank | Shinobi Core, Shinobi Village, Shinobi Combat, Shinobi Life, Village Friends |
| **Shinobi Adventure** (the map) | world save (a GitHub Release asset) + datapack `shinobi_adventure` | The hand-made Leaf with its border; the story, chapters, side quests, missions, events, the Classic cast, shop stock, homes, districts and regions as data | Every mod above |
| **Pack manifest** | `pack/` | A Modrinth `.mrpack` (and a CurseForge export) pinning Minecraft 26.3, Fabric Loader 0.19.5, Fabric API, Village Friends and every Shinobi mod by version and hash, with default config as overrides; the world is a separate release download | — |

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

- **Events:** `RankChanged`, `LevelChanged`, `PlayerDied`, `DayStarted`, `QuestStepChanged`,
  `FlagChanged`, `TechniqueLearned`, `AgeStageChanged`.
- **Conditions and actions:** every mod registers the conditions it can answer (`life:has_ryo`,
  `combat:knows`) and the actions it can perform (`life:give_ryo`, `combat:teach`) in Core's
  registry, so quest data can use them without Progression depending on their code.
- **Stat modifiers:** Life's fatigue writes movement, damage and chakra-regen modifiers; Combat
  reads chakra regen; movement and damage use vanilla attributes, so they work without Combat.
- **Wallet:** Life implements it with ryo; Progression pays rewards through it.
- **Player record and seed:** rank, level, age stage, clan id and the save seed live in Core.

### Each mod on its own

| Mod | Usable or testable alone |
|---|---|
| Shinobi Core | Unit tests; no content |
| Shinobi Village | In any VF world: residents wear the Naruto wardrobe and clans, the creator screen dresses the player, age stages scale the model |
| Shinobi Combat | With Village: every technique works in any world; unlocked by a command or an "all techniques" setting when Progression is absent; a test arena game test |
| Shinobi Life | In any VF world: claim a house with a plaque as your home, furnish it, trade in ryo, craft, keep a pet, sleep and feel fatigue. Adventure rules are a game rule, off by default outside the map |
| Shinobi Progression | With the mods it depends on: ranks, levels, the quest engine with its sample quests, generic missions and events, in any VF world |
| Shinobi Adventure | Only as the full pack |

### Repository layout

This repository becomes a Gradle multi-project, the way VF hosts `rpg/`: `core/`, `village/`
(today's wardrobe resources move here), `combat/`, `life/`, `progression/`, `adventure/` (the
datapack, blueprints and paste scripts) and `pack/` (the manifest). Python authoring tools stay
under `tools/`. Each mod has its own version; the pack manifest pins a tested set.

The master world is **not** in git. It ships as a zipped save on GitHub Releases; the repository
keeps only what rebuilds or checks it: blueprints, paste scripts and the datapack.

### Code by mod

| Mod | Packages | Pure, unit-tested core |
|---|---|---|
| Core | `record`, `seed`, `logic` (conditions, actions), `flags`, `events`, `stats`, `data`, `settings`, `wallet`, `region` | `SaveSeed`, `Conditions`, `FlagStore`, `Difficulty`, `StatMath` |
| Village | `wardrobe`, `clan`, `resident` (markers, cast), `look` (creator, age stages), client `render` | `ClanFile`, `CastRoll`, `AgeStage` |
| Combat | `chakra`, `technique`, `combat`, `movement`, `tools`, `shinobi`, client `anim`, `hud`, `signs` | `SignSequence`, `Mastery`, `Costs`, `ComboTiming`, `HitArc`, `WallRun`, `RangeBands` |
| Life | `rules`, `home`, `furniture`, `economy`, `craft`, `food`, `pet`, `romance`, `day`, client `furnish`, `hud` | `Fatigue`, `DayClock`, `FurnishRules`, `Prices`, `Courtship` |
| Progression | `rank`, `level`, `quest`, `mission`, `exam`, `event`, `squad`, `cutscene`, `playerclan`, `reaction`, client `journal`, `screens` | `Ladder`, `Levels`, `QuestGraph`, `MissionRoll`, `Judging`, `RoleBinding`, `Recruiting` |

Every mod follows the VF pattern: pure classes with JUnit tests, thin world glue, and client game
tests with screenshots (`-Ptests=...`).

### Regions

Only the Leaf ships now, but travel is designed in. A **region** is a dimension declared by the
map's datapack (an empty generator, a border, pasted builds, entry points) and registered through
Core's region interface. The Leaf is the first region. Far mission locations are small regions
reached from the travel desk at the main gate with a short travel scene. New regions are datapack
regions plus their world data, with no mod changes.

### Saves

- **Player:** each mod keeps its own Fabric attachment on the player (Core's record and flags;
  Combat's chakra and techniques; Life's home, fatigue and wallet; Progression's quests,
  milestones and squad), copied on death and synced to the owner.
- **World:** level attachments like VF's: the save seed and mode, the bound cast, the event
  director's state, exam results, furniture ownership, player clans with their clan files.
- **Content version:** every save records the pack's content version; quest and flag migrations
  run on load ([Versioning](#versioning-and-migrations)).

### Multiplayer (later)

Single player first. Because single player runs an integrated server, the code is
server-authoritative from the start, which keeps multiplayer possible later: squads of players,
one home per player, exam brackets, a Hokage rule, shared sleep, combat at 100 ms ping.

## 5. Data formats built for the whole story

*BUILD (beta).* The beta's quest, mission, story-flag and rank systems must hold every later arc
without a rewrite. These are the format decisions, fixed before Beta 1 content is written.

### Principles

1. **Everything that is story is data.** Chapters, side quests, filler arcs, board missions,
   events, cutscenes, dialogue and ranks are JSON (and dialogue text) in the Adventure datapack.
   Java provides engines, objective types, conditions and actions; adding an arc never needs code
   unless it needs a new objective, condition or action type.
2. **One quest format for everything.** Main chapters, side quests, filler arcs, clan quests and
   board missions are all quests with a `kind`. The journal, tracking, rewards, failure and save
   code is written once.
3. **Characters by role, not by entity.** Quests name roles (`role:sensei`, `role:teammate_a`,
   `role:rival`, `role:instructor`), never a resident's UUID. A save binds roles to characters
   (curated in Classic, rolled in Varied; names rolled in both), so later arcs written today work in
   every save. Text never contains a character's name, only name tokens.
4. **Places by anchor.** Quests name anchors (`place:academy.yard`, `place:forest.gate_12`) defined
   in `districts.json`, never coordinates, so the map can be rebuilt without editing quests.
5. **One condition and action language** in Core, shared by quests, missions, events, dialogue,
   shops and unlocks.
6. **Stable ids, versioned files.** Ids are never reused or renamed; every file has `"format": N`;
   the save records the content version and migrations run on load.

### Story flags

- **Shape:** namespaced keys with a value: `story.ch3.done = true`,
  `story.arc2.trust = 2`, `side.ramen_thief.culprit = "role:rival"`. Values are booleans,
  integers or strings.
- **Scopes:** `player` (your story, the default) and `world` (the village's state: `world.hokage = 4`,
  `world.stadium.damaged = true`).
- **Seeds and payoffs:** flags set in the beta that later arcs read are declared in
  `story/seeds.json` with the arc that pays them off, so a validator can warn when a seed is never
  used or a payoff reads a flag nothing sets (the seed table is in the spoiler-only [story bible](docs/story/STORY_BIBLE.md)).
- **Never deleted:** retired flags move to a `deprecated` list with their migration.

### Conditions and actions

```json
{"all": [
  {"rank_at_least": "genin"},
  {"flag": "story.ch14.done"},
  {"not": {"quest_state": ["side.paper_lanterns", "done"]}},
  {"any": [{"clan": "nara"}, {"friendship": ["role:teammate_b", 6]}]},
  {"time_between": ["18:00", "23:00"]}
]}
```

Conditions in the beta: `flag`, `rank_at_least`, `level_at_least`, `quest_state`, `friendship`,
`clan`, `clanless`, `age_stage`, `time_between`, `calendar` (season, day, weekday), `at_place`,
`has_item`, `has_ryo`, `knows_technique`, `nature`, `mode` (classic or varied), `difficulty`,
`random` (from the quest's seed stream). Combinators: `all`, `any`, `not`.

Actions in the beta: `set_flag`, `start_quest`, `advance_quest`, `fail_quest`, `give_item`,
`take_item`, `give_ryo`, `give_xp`, `teach_technique`, `add_friendship`, `cutscene`, `dialogue`,
`spawn_group` (enemies or residents at an anchor), `move_role` (send a character somewhere),
`promote`, `unlock` (a place, a shop item, a recipe), `news` (VF village news), `set_time`.
Reserved now for later arcs, so the format does not change: `time_skip`, `carve_face`,
`set_hokage`, `remove_from_squad`, `found_clan`, `marry`.

### The quest format

```json
{
  "format": 1,
  "id": "main.ch11.paper_trail",
  "kind": "main",
  "arc": "genin",
  "title": "quest.main.ch11.title",
  "giver": "role:sensei",
  "unlock": {"all": [{"quest_state": ["main.ch10.climbing_trees", "done"]}, {"rank_at_least": "genin"}]},
  "squad": true,
  "fail": {"on_death": true, "timeout_days": 3},
  "start": "meet",
  "steps": {
    "meet":   {"objective": {"type": "go", "place": "place:gate.main"}, "next": "escort"},
    "escort": {"objective": {"type": "escort", "who": "role:merchant", "to": "place:road.east_waystation"},
               "on_enter": [{"spawn_group": ["bandits_small", "place:road.east_bend"]}],
               "next": "search"},
    "search": {"objective": {"type": "inspect", "target": "cart_cargo"},
               "on_done": [{"set_flag": ["story.seed.cargo_found", true]}],
               "branch": [{"if": {"friendship": ["role:teammate_a", 5]}, "next": "campfire"}],
               "next": "report"},
    "campfire": {"objective": {"type": "talk", "who": "role:teammate_a", "dialogue": "bond.campfire.a"}, "next": "report"},
    "report": {"objective": {"type": "talk", "who": "role:sensei"}, "next": null}
  },
  "rewards": {"ryo": 450, "xp": 320, "friendship": {"role:squad": 3}},
  "journal": {"category": "main", "chapter": 11}
}
```

- **Steps form a graph** (`next`, `branch`), not a list, so later arcs can branch on choices and
  flags without a new format.
- **Objective types in the beta:** `go`, `talk`, `inspect`, `collect`, `deliver`, `craft`, `buy`,
  `defeat`, `escort`, `protect`, `survive` (until a time or day), `sneak` (reach a place unseen),
  `perform` (cast a technique, land a combo, hit targets), `wait_until`, `sleep`, `choose` (a
  dialogue choice that sets a flag). New types are added in code as later arcs need them.
- **Kinds:** `main`, `side`, `filler` (an arc of linked side quests), `clan`, `bond` (squad and
  friend stories), `mission` (board missions), `event`.
- **Text** is keys into the dialogue bank, never inline strings, and names are always tokens.

### Board missions

Board missions are quests generated from templates. A template fixes the objective graph and
leaves slots (who, where, what, how many, pay band) filled from the mission stream of the save
seed:

```json
{"format": 1, "id": "mission.d.lost_pet", "kind": "mission", "rank": "d",
 "slots": {"client": {"pick": "resident", "where": {"has_pet": true}},
           "pet_spot": {"pick": "anchor", "tag": "pet_hideout"}},
 "steps": {"find": {"objective": {"type": "collect", "target": "slot:client.pet", "at": "slot:pet_spot"}, "next": "return"},
           "return": {"objective": {"type": "deliver", "to": "slot:client"}, "next": null}},
 "pay": {"band": "d", "xp_band": "d"}}
```

### Ranks and milestones

`ranks.json` defines the **whole ladder now**, including ranks the beta does not reach, so the
save format never changes:

```json
{"format": 1,
 "ranks": [
   {"id": "academy", "floor": 1},
   {"id": "genin",   "floor": 5,  "exam": "exam.graduation", "requires": {"all": [{"level_at_least": 5}, {"quest_state": ["main.ch6.exam_eve", "done"]}]}},
   {"id": "chunin",  "floor": 15, "exam": "exam.chunin", "requires": {"all": [{"level_at_least": 15}, {"flag": "story.ch14.recommended"}]}},
   {"id": "jonin",   "floor": 30, "exam": "exam.jonin_trial", "requires": {"level_at_least": 30}, "content": "later"},
   {"id": "anbu",    "floor": 35, "branch_of": "jonin", "content": "later"},
   {"id": "hokage",  "floor": 50, "requires": {"level_at_least": 50}, "content": "later"}
 ]}
```

Milestones are conditions, so any rank can ask for any mix of quests, flags, levels and counts.

### Chapters and arcs

`story/arcs.json` lists every arc of the 60-hour story with its chapters and its status
(`beta` or `later`). The beta ships the Academy, Genin and Chunin Exams arcs; later arcs exist as
stubs (titles, unlock conditions, the seeds they read) so the journal, flags and validators already
know their shape.

### Versioning and migrations

- Every file carries `"format"`. The engine reads older formats or refuses with a clear log line.
- The save stores the content version. A migration file maps renamed flags and replaced quests:
  `{"from": "0.2", "flags": {"story.ch3.finished": "story.ch3.done"}}`.
- Board missions in progress are stored by template id plus their rolled slots, so a template edit
  never corrupts a save.

### Authoring tools

- **Quest compiler:** `tools/quests/quests.py` compiles a compact authoring format (one YAML-like
  `.quest` text file per quest or arc, with steps as indented blocks) to the JSON above, and
  `--check` validates: unknown objective types, conditions or actions; unreachable or dead-end
  steps; missing dialogue keys; roles and anchors that do not exist; seeds never paid off.
- **Templates:** `tools/quests/new.py <template> <id>` scaffolds the common shapes (fetch, deliver,
  escort, defeat, investigate, talk chain, filler arc of N parts) so a side quest starts as a
  filled-in file.
- **Dialogue** uses VF's dialogue text format and compiler (`tools/dialogue/`), with our pools.
- **In game (builder mode):** `/shinobi quest start|step|reset <id>`, a flag inspector
  (`/shinobi flags`), role and anchor inspectors, `/reload` for hot reload, and a debug overlay
  that draws anchors and the active objective.
- **Graph view:** `quests.py --graph <arc>` renders an arc's quests and flags as a diagram for
  review.

### World creation: Classic or Varied

At world creation the player picks a mode; the save stores it with one **save seed** (64-bit,
taken from the world seed or typed in).

- **Classic:** the curated cast (`cast/classic.json`: sensei, classmates, rival, families: looks,
  personalities and clans curated, names rolled),
  curated clan populations, a fixed order of side-quest arcs, a fixed apartment, curated shop stock;
  missions and events still use the seed, so even Classic is reproducible from its seed.
- **Varied:** the seed rolls the sensei, classmates and rival (looks from the wardrobe and clan
  pools, VF personalities, families), resident families and clan populations, which side-quest arcs
  appear and in what order, mission and event rolls, shop stock, and the apartment from a set of
  candidate flats in `homes.json`.
- **Fixed in both:** the main plot beats, the looks and roles of the story bible's fixed
  characters, and every authored chapter. Names and the rotating story roles are rolled in both.

**One seed, many streams.** Each system draws from its own stream derived from the save seed, so
systems never disturb each other and a save is reproducible with the same seed and pack version:

```text
stream(domain, key) = SplitMix64(hash64(saveSeed, domain, key))
```

| Domain | Key | Rolls | Mod |
|---|---|---|---|
| `cast` | role id | Squad, rival and classmate looks, personality, family | Village (Varied only) |
| `residents` | map marker id | Each `any` marker's group (by the population weights), then the resident's appearance, name and family | Village (Varied only; via VF's appearance seed API) |
| `apartment` | — | Which candidate flat is yours | Life (Varied only) |
| `sidequests` | arc slot | Which arcs appear and in what order | Progression (Varied only) |
| `missions` | board id + day | The board's missions and their slots | Progression |
| `events` | year + event id | Event variations (stall lineups, festival games) | Progression |
| `shops` | shop id + week | Weekly stock | Life (Varied only) |
| `quest` | quest id + step | `random` conditions inside quests | Progression |
| `names` | role id | Given name (by gender) and, for clanless characters, a family name; Hokage get a given name only | Village (both modes) |
| `twists` | twist slot | Which candidate fills each rotating story role | Progression (both modes) |
| `combat` | encounter id | Enemy loadout variations | Combat |

Residents are shipped as **markers** in the map (a resident spot with a home, a job and a role
tag), not as saved entities. On first load, Shinobi Village spawns each one from its curated
profile (Classic) or its rolled profile (Varied), so the same world file serves both modes.

### Names rolled per save

- **Pools:** `names/given.json` in Shinobi Village (original Japanese given names by gender:
  male, female, unisex), family names from each clan file (a clan character carries the clan's
  name) and from `family_names` in `tools/wardrobe/population.json` for clanless shinobi and
  civilians.
- **Who:** every role-bound and fixed story character, in both modes; the Hokage's given names.
  Residents spawned from markers already get rolled names in Varied (VF's name pools are not used
  for Leaf residents).
- **Tokens:** dialogue and quest text use `{name:<role>}` (full name), `{given:<role>}`,
  `{family:<role>}`, `{hokage:<n>}` and `{player}`; the journal, speech bubbles and VF's dialogue
  bank resolve them. A name is never written into text.
- **Checks:** `quests.py --check` and the dialogue compiler reject any literal from the name pools
  in authored text, and every token must name a role that exists.
- **Stable within a save:** names are rolled once, at world creation, from the `names` stream and
  saved with the cast, so a character keeps their name for the whole playthrough.

### Rotating story roles

- **Twist slots:** `story/twists.json` lists slots, each with 2 to 4 candidate characters. At world
  creation the `twists` stream binds one candidate per slot, in Classic and Varied alike.
- **Clue trails:** each candidate has its own clue quests and flags (`story.clue.<candidate>.<n>`).
  Every candidate's clues are planted; the bound candidate's turn out true, the others' get innocent
  explanations. Quests address the bound character as `role:twist.<slot>` or `{twist:<slot>}`.
- **Checks:** `quests.py --check` verifies that every candidate has a complete clue trail and an
  innocent explanation, and that every arc reads the slot rather than a fixed character.
- **No spoilers:** which roles rotate and who the candidates are live only in the story bible.

## 6. The map

*BUILD (beta) for the districts each slice needs (see the schedule below); FOUNDATION (later) for the rest of the village, which is laid out now and built after the beta.*

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
  **Four faces** at the start, with room for more. The streets fan out from its foot, so
  the Rock is visible from every street.
- **Outside the wall:** the Forest of Death, outer training grounds, the hills of the prologue,
  bandit camps and roads to the gates. The whole map is about **1,200 × 1,200 blocks**, closed by
  a world border dressed as mountains and deep forest so it never ends in a bare wall. Mission
  locations beyond it (other villages, far roads) are separate small areas reached by travel
  scenes at the border gates, not open terrain.
- **No generation:** the shipped world uses an empty generator outside the map; vanilla structures
  and VF villages are switched off by a data pack.
- **Population:** about 300 residents when the whole village is built, about 200 in the beta's
  districts. VF residents tick routines once a second, so measure before going higher.
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
| Hokage Rock | By hand | Voxel sculpting; four custom faces of original Hokage, with room for more. Faces, portraits and statues are baked, so each Hokage's look is fixed while their name is rolled per save. The village expands onto the plateau above it only in a much later era, so leave the top as forest ([Hokage Rock](https://naruto.fandom.com/wiki/Hokage_Rock)) |
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

### Population

Most of the Leaf belongs to no great clan. Every resident comes from a map **marker** (a spot with
a home, a job and a group tag). A marker either names its group (a clan elder in a clan seat, the
ramen cook) or says `any`, and then the group is drawn by weight from
[`population.json`](tools/wardrobe/population.json) through the save seed: Classic saves use the
curated draw, Varied saves roll it.

| Group | Share | About, of 300 | Look | Where they live |
|---|---|---|---|---|
| Civilians | ~45% | 135 | The market and household collections; ordinary family names | Civilian districts: the market street, the residential streets, the riverside |
| Clanless shinobi | ~28% | 84 | Mixed across the six shinobi collections; ordinary family names | Shinobi apartment blocks and ordinary streets, everywhere |
| Minor clans (10) | ~15% | 45 | Their clan pieces | Mixed neighbourhoods, no walls |
| Noble clans (15) | ~13% | 39 | Their clan pieces | Their clan seats; an Uchiha or a Hyuga is about 1 in 70 (4 or 5 each), a Hatake about 1 in 500 (one, if any) |

**Civilian districts and shops.** Civilians run the village's daily life: the grocer, the fish and
vegetable stalls, the tea house, the furniture maker, the tailor, the bath house, the pawn shop,
the flower stalls, Ichiraku. Their shops are where you spend ryo and take part-time jobs, and their
streets are where most D-rank missions happen. VF's professions map onto them (farmers,
fishermen, cooks, tailors, carpenters), and VF's routines give them their days.

### Clan quarters

Twenty-five clans live in the village ([CLANS.md](CLANS.md)), sized to their rarity. The eight
great noble clans have a **clan seat**: a gate, a main hall, a training yard and 1 to 3 homes in the
clan's style, for their few members (2 to 6). The seven smaller noble clans have a **clan home**:
one hand-built house or dojo with its signature feature. The ten **minor clans** have no walls: they
share mixed neighbourhoods with civilians and clanless shinobi, with a family house or workshop
that marks each one. Each quarter is one plot group in the map layout file, filled from its clan
JSON. A clan-born player can move into their clan's quarter from Chunin on.

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
| Shimura | Clan home | Close to the Hokage Rock, near the hidden ANBU entrance | A stern, quiet house |
| Yuhi | Clan home | Residential district with gardens | House in a grove of old trees used for genjutsu training |
| Gekko | Clan home | By the training grounds | Kenjutsu dojo with a moon-viewing platform |

The minor clans, in mixed neighbourhoods:

| Minor clan | Neighbourhood | Marks it | Ability |
|---|---|---|---|
| Shiranui | Near the gate barracks | A family house with a senbon target wall | — |
| Morino | Near the police HQ | A severe house with barred windows | — |
| Umino | The Academy streets | Teachers' houses by the Academy | — |
| Haruno | A residential street | A neat family house and garden | — |
| Namiashi | Near the training grounds | A small dojo for footwork | — |
| Hagane | The market street | A metalworker's shop beside the forge | — |
| Kinoshita | The carpenters' lane | The carpenters' and builders' yard (furniture is made here) | — (original; carpenters and builders) |
| Tsuchigumo | The quarry edge of the village | Stone houses by the quarry | Earth and web-like binding techniques (the canon anime clan) |
| Suzuran | The herb gardens by the hospital | Herbalists' houses and drying racks | Poison resistance and herbal medicine (original) |
| Tobari | Dark lanes behind the wall | Shuttered houses with sound-dampened walls | Sound-smothering night scouting (original) |

### District schedule

What must exist, playable and populated, by the end of each slice. Everything else stays sealed
off (closed gates, streets under repair) or is not built yet.

| By | Districts and landmarks | Why |
|---|---|---|
| Phase 0 | One test street of pasted homes with plaques and a Village Marker | Proves pasting, homes, residents and ryo trades on a hand-made map |
| **Beta 1** | The prologue hills, the hideout and a ruined shrine; the main gate and its stretch of wall; the main street to the Hokage Residence (exterior and ground floor); the Academy (by hand) with its yard, library and workshop; the player's apartment block (all candidate flats for Varied) and ~12 homes around it; Ichiraku; the furniture shop, grocer and Inuzuka clinic (pets); the hospital; the shrine; the Hokage Rock with its four faces; a gate and main hall for each of the 15 noble clan quarters; the civilian market street and residential streets | The opening, the Academy, life sim, pets, clan-born kin from day one, seeds for later |
| **Beta 2** | The Mission Desk (Residence ground floor); Training Ground 3 (by hand) and two pasted training grounds with the lake and the climbing cliff; the market street with the weapon shop and forge, scroll shop, tea house, barbecue house; the 15 noble clan quarters filled out; the 10 minor clans' neighbourhoods; bandit camps outside the wall; the east road and its waystation; the first far-location region (a border village) | Genin missions, training arcs, crafting, story C-ranks, clan techniques |
| **Beta 3** | The Forest of Death (pasted trees, the tower by hand, 44 gates); the stadium with seated spectators; the exam hall in the Academy; foreign teams' lodging | The Chunin Exams and the attack |
| Later | The rest of the homes and shops, police HQ, the full wall and all gates, ANBU HQ, the later arcs' story locations, the four vacant estates, the far regions of later arcs | Chunin to Hokage ([Story bible](#10-story-bible)) |

### How the map is made

1. A **map layout file** (`tools/konoha/layout.json`) places every district: polygon, streets,
   plots, which designs go on which plots, the landmarks' positions and rotations, the **anchors**
   quests refer to, the resident **markers**, the candidate flats and the vacant estates.
2. Design programs in `tools/konoha/buildings/*.py` write blueprints in VF's format; VF's
   compiler turns them into NBT.
3. A **paste tool** (a dev command, `/shinobi paste <district>`, only in builder mode) pastes a
   district's blueprints into the master world at their fixed spots. Re-pasting one district never
   touches the others.
4. The world is finished by hand (terrain, the Rock, the hand-built landmarks), plaques, markers
   and anchors are checked by `layout.py --check`, and the world is zipped as a release asset.

## 7. Systems in the beta

*BUILD (beta).* Every system the first 15 hours need, and which slice brings it.

### Systems by slice

| System | Beta 1 (opening, Academy) | Beta 2 (Genin) | Beta 3 (Chunin Exams) |
|---|---|---|---|
| World creation | Classic or Varied, the save seed | — | — |
| Character creation | Creator screen, one of 25 clans or clanless | — | — |
| Adventure rules | No breaking or placing | — | — |
| Home and furniture | Apartment, furnish mode, chests | Forge for the apartment | — |
| Ryo and shops | Stipend, jobs, furniture shop, grocer, Ichiraku | Mission pay, tool, weapon and scroll shops | Exam-week stalls |
| Daily cycle | Schedule, sleep, fatigue, Well Rested, hospital wake | — | Bedroll camping, On Duty |
| Food | Vanilla hunger, Leaf dish buffs | Barbecue house, tea house | — |
| Crafting | Workbench (smoke bombs, tags, furniture) | Smithy (kunai, shuriken), crafted grades | — |
| Pets | Adopt a pup or a cat | Ninken tracking on missions | — |
| Friendship | VF friendship levels with classmates and neighbours; squad roles bound | Bond stories, teammates can leave | Bond payoffs in the forest and finals |
| Levels | 1 to 5, death penalty, floors | 5 to 15 | 15 to 18 |
| Ranks | Academy → Genin | Chunin Exam eligibility | Genin → Chunin (judged) |
| Growing up | Child stage (the whole beta) | — | — |
| Hand signs and chakra | Chakra bar, typed and radial signs | — | — |
| Jutsu | Clone, Transformation, Substitution | Nature ceremony, one jutsu per nature, clan technique first tier, kekkei genkai first stage | One exam reward technique |
| Taijutsu | Three-hit combo, heavy, dodge, block | Parry, launcher | — |
| Chakra movement | — | Tree walking, wall-running, water-walking, chakra jump, ninja run | — |
| Tools | Practice kunai and shuriken | Thrown kunai, shuriken, paper and smoke bombs, tool pouch | — |
| Enemies | Sparring classmates; the prologue's guards (scripted) | Bandits, rogue ninja, enemy scouts | Exam rivals, enemy cells |
| Quests | Main chapters, bond and side quests | Mission Desk (D and C rank), filler arcs, clan quests | Exam stages |
| Events | — | Leaf Festival, New Year | Chunin Exams as a calendar event |

### Character creation

A creator screen in the prologue: hair, eyes, skin (the six complexions), marks and a starting
outfit from the wardrobe, shown on your child-stage model; then born to one of the 25 clans (its
look, and from Genin its technique and kekkei genkai) or clanless.

### Adventure rules

- **No breaking or placing blocks** anywhere in the world. Shinobi Life enforces it with Fabric's
  block break and use-block events, not only with Adventure mode, so it holds in every game mode
  except builder mode (for making the map).
- **Allowed:** doors, gates, buttons and levers, sitting, sleeping, chests, furniture and stations
  inside your own home, shop trading, world stations you are allowed to use.
- **Techniques never change the map:** fire, bombs and wind do not break blocks; barriers are
  short-lived entities.

### Your apartment and furniture

Your home is a VF house: its House Plaque flood fill gives exact bounds (`home/HouseBounds`), and
furnishing is only allowed inside them. In Varied saves the apartment is rolled from a set of
candidate flats; in Classic it is always the same one.

- **Furnish mode.** Press `F` at home (or right-click your door plaque). Furniture items in your
  inventory show a ghost preview snapped to the block grid; scroll to rotate, click to place. Aim
  at a piece you own and click to pick it back up into your inventory, with its contents. Leaving
  your bounds or pressing `F` again ends furnish mode.
- **What counts as furniture:** blocks tagged `shinobi_life:furniture`, plus chests, stations and
  storage. The beta's Leaf set: futon and bed, low tables, cushions, tatami, screens, scroll
  shelves, lamps, potted plants, posters, a weapon rack, a training dummy, a pet bed; VF's tavern
  furniture; a Hearth & Harvest cooking pot; the workbench (Beta 1) and a small forge (Beta 2).
- **Your bed** is furniture too, but every home always keeps one bed; it is the bed that clears
  fatigue.
- **Upgrades** (a flat, a house, a clan room, an estate) come after the beta ([Later systems](#11-later-systems)).

### Ryo

Ryo is the only money: notes as items (1, 10, 100 and 1,000 ryo), so it works with vanilla
trading, fits in chests and shows on the HUD as a total. VF's notice rewards and trades use ryo
through the currency API. The economy is small and closed; rule of thumb: a day of D-rank missions
covers food and leaves about half to save, and the first proper furniture set takes about an
in-game week (a little over two hours) of play.

| Earn (beta) | Ryo | Spend (beta) | Ryo |
|---|---|---|---|
| Orphan's stipend (Academy only) | 30 a day | Ramen, onigiri, tea | 3 to 10 |
| Part-time jobs (Ichiraku, grocer, flower shop, forge) | 40 to 80 a shift | Kunai, shuriken, smoke and paper bombs | 5 to 40 each |
| D-rank mission | 60 to 150 | Soldier pill | 60 |
| C-rank mission | 300 to 600 | Furniture | 20 to 800 a piece |
| Side quests | 20 to 300 | Outfit variants (rank outfits are given) | 100 to 600 |
| Festival games | small prizes | Crafting materials (steel, paper, powder) | 2 to 30 |

Furniture sells back at half price; loot from bandit camps sells at the pawn shop. There is no
other way to turn things into money.

### The daily cycle

A Minecraft day is 20 minutes. The village runs on VF's routines and calendar (4 seasons of 28
days, a seven-day week with Market Day), and the player's day fits around it.

| Time | What is on |
|---|---|
| 6:00 | You wake at home. Shops open around 7:00 |
| 8:00 to 18:00 | Mission Desk open (from Genin) |
| 9:00 to 12:00 | Academy lessons on weekdays |
| Afternoon | Training, missions, jobs, friends |
| Evening | Ramen, events, festivals (events end by midnight) |
| Night | Go home and sleep |

**Fatigue.** Sleeping in a bed at night skips to 6:00. If you stay up, fatigue builds (thresholds
by difficulty):

| Stage | From (Story) | Effect |
|---|---|---|
| Tired | 01:00 | Movement −10%, chakra regen −25% |
| Exhausted | 03:00 | Movement −20%, chakra regen −50%, damage −20%, a darkened screen edge, chakra jumps may fall short |
| Collapse | 06:00 still awake | You pass out and wake in your bed at noon; timed missions lose the morning |

Your own bed clears fatigue fully, and sleeping before midnight gives **Well Rested** (+10% chakra
regen until noon). Other beds (hospital, a camp bedroll) clear it without the bonus. Green tea
pushes the next stage back an hour; a meal halves the movement penalty for an hour. Night duty (the
Forest of Death) gives *On Duty*, delaying fatigue by three hours.

### Death

- **Levels:** one level lost (XP drops to the start of the level below), never below your rank's
  floor; you never lose a rank.
- **Tools:** the thrown tools you carry are lost.
- **Missions:** dying on a mission fails it: no pay, a small standing loss with the client.
- **Waking:** in the hospital the next morning, fatigue cleared. No bill.
- **Sparring** never kills: a spar ends at 30% health or a yield, with no level loss.

### Food

Vanilla hunger stays. Leaf dishes from Ichiraku, the barbecue house, the tea house, the grocer or
your own cooking pot add small, short buffs through VF's `WellFed` tiers: ramen restores a little
chakra, dango speeds chakra regen, barbecue raises taijutsu damage slightly, green tea holds off
fatigue.

### Gear and crafting

| Station | Where | From | Makes |
|---|---|---|---|
| Workbench | The Academy workshop; one for your apartment | Beta 1 | Smoke bombs, wire, sealing tags, paper bombs (from Genin), furniture from planks and cloth |
| Smithy (forge and anvil) | The weapon shop's forge; a small forge for your apartment | Beta 2 | Kunai, shuriken, senbon, a tanto, from steel bought at the smithy and salvage from bandit camps |
| Cooking station | VF Hearth & Harvest pot, oven, prep table | Beta 1 | Leaf dishes |

Recipes unlock by rank, by mentors (the smith teaches you after a few jobs at the forge) and by
scrolls. Crafted tools can be a grade better than shop stock. Stations reuse VF's workstation
pattern (`WorkstationBlock`, Hearth's `StationBlock` and its screens), with recipes as data.

### Pets

Adopt a **ninken pup** at the Inuzuka clinic or a **cat** at the shelter (Beta 1). Pets are vanilla
wolves and cats tamed to you and driven by VF's pet code (`pet/`: following, resting, playing,
tricks and pet play clips). Your pet follows you, waits at home during missions it cannot join,
sleeps at the foot of your bed, and from Beta 2 a ninken can track scents on missions. Pets are
knocked out, never killed. No summons.

### Friendship and bonds

The squad, classmates and neighbours are VF residents, so friendship uses VF's ten levels,
relationship meters, gifts, speech bubbles and dialogue. The beta adds **bond quests** (`kind:
bond`) gated by friendship (bond levels also feed [Kindling Bond](#kindling-bond) after the beta): two per classmate in Beta 1 and two per teammate in Beta 2, with
payoffs in Beta 3. Romance waits for the teen stage, after the beta; children have friendships and
VF's harmless crushes in dialogue only, enforced in code.

### Levels

Levels are power; ranks are story. Every rank exam asks for a minimum level, and reaching a level
never promotes you by itself.

- **Each level:** +3 maximum chakra and +1% taijutsu damage; +1 heart every 6 levels (10 hearts at
  level 1). Jutsu have a minimum level as well as a rank.
- **XP:** missions give most of it, then training milestones, exams, events, side quests, jobs and
  fights. Fight XP falls off for repeated kills of the same kind (a rule borrowed from VF's RPG
  add-on, which the pack does not ship), and bandit camps refill weekly.

The whole curve is defined now (in `ranks.json`); the beta reaches level 18.

| Stretch | Main-path hours | Cumulative | Levels | Gate | Floor after |
|---|---|---|---|---|---|
| **Academy** | ~4 | 4 | 1 → 5 | Graduation: level 5 | 5 |
| **Genin** | ~8 | 12 | 5 → 15 | Chunin Exams: level 15 | — |
| **Chunin Exams** | ~3 | 15 | 15 → 18 | Promotion by judging | 15 |
| Chunin | ~13 | 28 | 18 → 30 | Jonin trial: level 30 | 30 |
| Jonin | ~17 | 45 | 30 → 42 | The road to Hokage opens at 42 | — |
| Road to Hokage | ~15 | 60 | 42 → 50 | Succession: level 50 | 50 |
| ANBU (optional) | +~8 | — | from 35 | Invitation: level 35 | 35 |

In the beta a level takes about 45 to 50 minutes of main path; later about 65 to 110 minutes.
Level 60 is post-game. Side quests add XP, so a player who does them reaches gates earlier and can
skip some board missions.

### Growing up

| Stage | Age | When | Model |
|---|---|---|---|
| Child | 11 to 12 | The whole beta | The player model at **0.78** scale through vanilla's `scale` attribute (hitbox, eye height and reach follow it), with the head drawn 10% larger by the player poser |
| Teen | 13 to 17 | From the time skip that opens the Chunin arc (after the beta) | **0.9** scale, normal head |
| Adult | 18 and up | From the second time skip, before the Jonin trial (later) | **1.0** scale, forever |

The same wardrobe pieces fit every stage, because the model is scaled, not changed; the rank
outfits line up with the stages. Your classmates and squad are adult VF residents with a `stage`
tag and the same scale values, so they grow up alongside you (VF's own children stay vanilla
babies with their games and lessons). The calendar alone would age you less than two years in 60
hours, so the story uses two time skips: about a year after the Chunin Exams (opening the Chunin arc,
after the beta) and about three years before the Jonin trial.

### Your squad and roles

Quests refer to characters by **role**; the save binds each role to a character.

| Role | Who | Classic | Varied |
|---|---|---|---|
| `role:captain` / `role:sensei` | The Jonin who rescues you, later your sensei | Curated | Rolled |
| `role:instructor` | The Chunin from the rescue, your Academy instructor | Curated | Rolled |
| `role:medic` | The medic from the rescue, at the hospital | Curated | Rolled |
| `role:teammate_a`, `role:teammate_b` | Two classmates who become your squad | Curated | Rolled from the four classmates |
| `role:classmate_c`, `role:classmate_d` | The other two classmates, later on a rival squad | Curated | Rolled |
| `role:rival` | Your rival, on another squad | Curated | Rolled |
| Fixed story roles | The characters the story bible fixes in every save | Fixed | Fixed |

Names are rolled per save in both modes. Rolled characters (Varied) take a group by the population weights (shinobi groups only, so most are clanless), a look from that group's pieces, a VF personality, a family in the
village and a name from VF's name pools; once rolled they are fixed for the save. A teammate can
leave the squad (low friendship that stays low, a failed exam, or the story), stays in the village
and is replaced by a classmate. Squad members are knocked out, never killed.

### Combat in the beta

The beta's combat is the core of the full system; later ranks add techniques, not new rules.

**Taijutsu.**

| Mechanic | How in Minecraft | Slice |
|---|---|---|
| Combo chain | Empty hand or kunai in hand: left click is caught (client mixin on the attack key) and sent as a combo input; the server runs the chain. 3 light strikes, about 6 ticks apart, the third knocks back. Vanilla's attack cooldown does not apply inside a chain; a 10-tick recovery follows | Beta 1 |
| Heavy | Hold left click for 8 ticks | Beta 1 |
| Launcher | A heavy during a chain launches the target upward for an air follow-up | Beta 2 |
| Hit detection | Server-side sweep: a 60° arc, 3 blocks deep. Each combo hit lowers the target's hurt invulnerability so chains land | Beta 1 |
| Dodge | Double-tap a direction or press `Left Alt`: a 4-block dash with invulnerable ticks, 1.5 s cooldown, a little chakra | Beta 1 |
| Block and parry | Right click with an empty hand: block (−60% melee damage); block just as a hit lands: parry, staggers the attacker | Block Beta 1, parry Beta 2 |
| Substitution | Dodge as a hit lands, with enough chakra: blink back 5 blocks, a log entity drops. Once per 20 s | Beta 1 |

**Chakra movement** (Beta 2; client-side movement, with the server checking and charging chakra):
the ninja run (+15% sprint, arms back), the chakra jump (hold to charge, up to 3× height, no fall
damage while chakra lasts), tree and roof hopping (a forward boost off leaves, logs and roofs),
wall-running (along or up a wall for up to 3 s), water-walking (a mixin on `canStandOnFluid`, the
method vanilla uses for striders on lava; sneak to sink).

**Hand signs and chakra.** Twelve signs (Rat, Ox, Tiger, Hare, Dragon, Snake, Horse, Ram, Monkey,
Bird, Dog, Boar). Hold the **Weave** key (`R`) and enter signs one of two ways, chosen in the
settings: **typed** (a key per sign, by default `1` to `0`, `-` and `=`) or a **radial** wheel
(mouse or controller stick). Release to cast. Each sign takes 4 ticks and plays its pose; a wrong
sequence fizzles. A jutsu used often becomes **mastered**: bindable to a quick slot (`Z`, `X`,
`C`, `V`) and cast with fewer signs. Chakra is a bar beside hunger; it refills slowly, fast while
meditating (sneak and stand still), and from soldier pills; maximum chakra grows with level.

**Learning jutsu:** from **mentors** (the instructor, your sensei, clan elders, nature masters, at
friendship and level thresholds, with a short trial), **scrolls** bought at the scroll shop (Beta 2),
and **mission rewards**.

**The beta's techniques.**

| Technique | Signs | Mechanic | Slice, learned from |
|---|---|---|---|
| Clone | Ram-Snake-Tiger | Illusory copies of you that run off; mobs may target them | Beta 1, the instructor |
| Transformation | Dog-Boar-Ram | Your render becomes a chosen resident's look; mobs lose their target; residents do not recognize you | Beta 1, lessons |
| Substitution | (dodge timing) | See taijutsu | Beta 1, lessons |
| Nature jutsu (one per nature) | e.g. Snake-Ram-Monkey-Boar-Horse-Tiger (Fireball) | Fire: a projectile that sets mobs alight; Wind: a wind-charge gust; Water: a pushing wave that puts out fire; Earth: a short-lived wall entity; Lightning: a stunning palm strike | Beta 2, the nature ceremony (you choose your first nature) |
| Clan technique, first tier | per clan (the noble clans and the three minor clans with abilities: Tsuchigumo, Suzuran, Tobari) | For example Shadow Possession (Nara), Expansion (Akimichi), Gentle Fist (Hyuga), Fang over Fang with your ninken (Inuzuka), Insect swarm (Aburame); the full table is in [Later systems](#clan-techniques-and-kekkei-genkai) | Beta 2, your clan's elder (clan-born); clanless players learn one lesser technique from a friendly clan |
| Kekkei genkai, first stage | — | Byakugan's sight through walls within 16 blocks; the Sharingan's first tomoe (earlier telegraphs); Wood Release's binding roots | Beta 2 (Byakugan, Wood), Beta 3 (the Sharingan awakens in the forest) |
| Exam reward | — | One C-rank technique chosen by your sensei after the preliminaries | Beta 3 |

**Ninja tools.** Kunai (combo weapon; right click throws it like a trident, retrievable),
shuriken (stackable, fast, three at once from Genin), paper bombs (stick to a surface or a kunai;
damage entities, never blocks), smoke bombs (blind, mobs lose their target), wire (a trip trap),
the tool pouch (quick-throw from the hotbar). Shop or crafted.

**Enemies and sparring.** One **shinobi entity** for every human enemy, drawn with VF's resident
model and our wardrobe. Its brain keeps a range band (close for taijutsu, mid for throws, far for
jutsu), strafes, dodges telegraphed attacks with a chance set by rank, uses substitution once per
fight and retreats to heal. Each enemy has a loadout file (techniques, rank, level, tools). Beta
enemies: the prologue's guards (scripted), sparring classmates, bandits, rogue ninja, enemy
scouts, exam rivals, enemy cells. Sparring with ranked residents at training grounds
raises friendship.

**Difficulty.**

| Setting | Story (default) | Shinobi | Hard |
|---|---|---|---|
| Parry and dodge windows | 6 and 8 ticks | 4 and 6 | 3 and 5 |
| Enemy telegraphs | long, with a flash | normal | short |
| Enemy damage | 60% | 100% | 130% |
| Death | one level, never below the floor | the same | two levels |
| Fatigue starts | 01:00 | 00:00 | 23:00 |
| Cinematic camera on finishers and jutsu | on | on | off |

Every number lives in data (`difficulty.json`, overridable per world), and the setting can change
at any time.

**Animation.** VF's clip system poses residents only (`ResidentLife`, `ResidentPoser`). Resident
clips are a pack in our namespace (`assets/narutominecraft/resident_animations/`, authored in
Python like VF's `tools/animations/`), which VF loads without Java. For the player, Shinobi Combat
adds a **player poser** that samples the same clip format onto the player model, with a
first-person arm path for hand signs and throws: Phase 0's spike and Beta 1's main risk. Clips by
slice: the prologue's crouch, slipping out and being carried, hand signs, combo strikes, heavy,
dodge, block, throw, meditation, a tired slouch, petting (Beta 1); parry, launcher, ninja run,
chakra jump, wall-run, water stance, forging and workbench, the first clan techniques (Beta 2);
the finals' fighters and the stadium crowd (Beta 3).

### Residents react to your rank

Rank-specific greeting and reaction pools in VF's dialogue bank (`tools/dialogue/lines/naruto-*.txt`)
for Academy, Genin and Chunin in the beta; residents get a rank from their outfit's `rank` field;
superiors get a salute clip, peers a nod, kids an excited wave; gate guards turn you away from
places above your rank (the Forest of Death outside the exams) by dialogue, not barrier blocks.

## 8. The beta, chapter by chapter

*BUILD (beta).* Every main chapter of the first 15 hours, with its time on the main path (a
first-time player, Story difficulty) and what it teaches, described neutrally. What happens in each
chapter, and what it sets up for later, is in the spoiler-only
[story bible](docs/story/STORY_BIBLE.md).

### Beta 1: the opening and the Academy (~4 h)

About 2.8 hours of authored chapters and 1.2 hours of systemic play (lessons between chapters,
jobs, furnishing, adopting a pet, friends), over about 12 in-game days. Chapter titles here are
working titles; the story behind each chapter is in the story bible.

| Ch | Chapter | Time | Content | Teaches |
|---|---|---|---|---|
| 0 | Prologue | 20 min | The creator screen; the rescue from a rogue ninja hideout; a chase through the forest | Looking, sneaking, following, dodging, sprinting, climbing |
| 1 | First morning | 20 min | The gate, the Hokage, your apartment and stipend; Ichiraku; enrolment; your classmates and your rival | The HUD, ryo, shops, the apartment, talking, VF friendship |
| 2 | First lessons | 20 min | Taijutsu forms and throwing; a spar with your rival | Combo, heavy, dodge, block, practice kunai and shuriken |
| 3 | Chakra | 25 min | The chakra lesson and a paired chakra exercise | Chakra, meditation, hand signs (typed or radial) |
| 4 | Night | 25 min | A night out in the village | Night, fatigue, roof running, the cost of staying up |
| 5 | Errands at the Academy | 15 min | A library chore and a tour of the Hokage Rock | Errands, the journal, inspecting |
| 6 | Exam eve | 20 min | A study night with your classmates | Clone, Transformation, Substitution; bond quests |
| 7 | Graduation | 25 min | The graduation exam and the forehead protector | The exam flow, promotion |

### Beta 2: Genin life (~8 h)

About 4 hours of authored chapters and 4 hours of systemic play: about 12 board D-ranks (~2 h),
3 board C-ranks (~1.5 h), training and your clan's lesson (~0.5 h), over about 24 in-game days.

| Ch | Chapter | Time | Content | Teaches |
|---|---|---|---|---|
| 8 | Team assignment | 35 min | Your squad and sensei; the bell test at Training Ground 3 | Squad commands, parry, teamwork |
| 9 | The Mission Desk | 15 min | The squad's first D-rank; the board opens | Board missions, mission pay, failure on death |
| 10 | Tree walking | 25 min | Chakra training at Training Ground 3 | Tree walking, wall-running, chakra jump, roof hopping |
| 11 | First C-rank | 45 min | Escorting a merchant east; bandits on the road; a night at camp | Escort, defeat, inspect, camping, bond |
| 12 | Water walking and natures | 30 min | The lake; the nature ceremony; your clan's lesson (or a friendly clan's) | Water-walking, natures, the first elemental jutsu, the clan technique, the scroll shop |
| 13 | A far village | 45 min | The first far region and an investigation there | Travel, investigation, ninken tracking |
| 14 | Second C-rank | 50 min | Another escort east, and a recommendation for the Chunin Exams | Enemy cells, smoke and paper bombs |

### Beta 3: the Chunin Exams (~3 h)

About 2.5 hours authored and 0.5 hours systemic (the training break). The exams are also a
calendar event that runs with NPC teams every season. The beta ends with the promotion results,
not a time skip.

| Ch | Chapter | Time | Content | Teaches |
|---|---|---|---|---|
| 15 | Written test | 20 min | Ten impossible questions; gather answers unseen | Stealth objectives, choice |
| 16 | Forest of Death | 60 min | One scroll of a pair and five in-game days to reach the tower with both | Survival, bedroll camping, On Duty, tree-hopping fights |
| 17 | Preliminaries | 20 min | One-on-one bouts in the tower's arena | Duels, judged performance |
| 18 | Training break | 30 min | Six days of training with your sensei; festival crowds | Systemic: training, crafting, side quests; your exam reward technique |
| 19 | Chunin Exams finals | 40 min | The finals in the stadium before the whole village | Duels and protect objectives, the cinematic camera |
| 20 | Results | 10 min | Promotion results, judged on how you fought | Promotion |

### The squad bonding arc

Bond quests (`kind: bond`) carry the squad through the beta, gated by friendship: a study night
(Ch 6), two bond quests per classmate in Beta 1, the bell test (Ch 8), a campfire talk (Ch 11), two
bond quests per teammate and a squad dinner in Beta 2, a choice about a teammate (Ch 13), the
forest night watch (Ch 16) and the finals (Ch 19). Low friendship changes how these play out.

### Side quests in the beta

Optional, outside the main-path hours, all `side`, `filler`, `clan`, `bond` or `event` quests in
the Adventure datapack, unlocked by rank, place, friendship, clan and events.

| Slice | Target | Includes |
|---|---|---|
| Beta 1 | 10 | The filler arc **The Ramen Thief** (3 parts: who keeps eating Ichiraku's stock at night?); 4 bond quests; one-offs like the lost Academy cat, the old shogi player, the flower shop's delivery |
| Beta 2 | 20 + 25 clan quests | The filler arcs **Lanterns on the Lake** (4 parts: a ghost light over the training lake) and **Dogs and Bugs** (3 parts: an Inuzuka-Aburame feud over a missing beetle); 4 bond quests; one-offs (the pawn shop's forged scroll, the forge's apprentice, a festival lost child); one quest per clan (noble and minor) for its members and friends; civilian quests on the market street |
| Beta 3 | 4 | Exam week: a lost foreign Genin, a stall thief, the *rival*'s younger sibling, the hospital's missing supplies |

That is about 34 side quests plus 25 clan quests, roughly 8 to 10 hours of optional play. In
Varied saves each slice draws from a larger pool (for example 30 Beta 2 one-offs, 12 shown) and
the filler arcs come in a rolled order; Classic uses a fixed selection.

### The Classic cast

The curated cast of a Classic save (all original), mostly clanless like the village. Their looks,
personalities and clans are curated; **their names are rolled per save** like everyone's. Varied
saves roll these roles entirely, by the population weights (shinobi groups only).

| Role | Classic design (name rolled per save) |
|---|---|
| `role:captain` / `role:sensei` | A quiet clanless Jonin with an old burn scar |
| `role:instructor` | A cheerful clanless Chunin who believes in everyone |
| `role:medic` | The hospital's young clanless medic |
| `role:teammate_a` | A Kurama: shy, imaginative, paints, a born genjutsu user |
| `role:teammate_b` | Clanless, loud and fearless, with a stray pup |
| `role:classmate_c`, `role:classmate_d` | A Kinoshita carpenter's child (thoughtful) and a Gekko (protective, a kenjutsu prodigy) |
| `role:rival` | An Uchiha: proud and lonely |
| `role:merchant` | A travelling merchant who keeps hiring the squad |

## 9. Delivery plan

*BUILD (beta).* Phase 0, then three slices, each a release: the `.mrpack` with every mod pinned,
plus the zipped world on GitHub Releases. Each slice is playtested and tuned before the next starts.
Deliverables name the mod they land in: **Core**, **Village**, **Combat**, **Life**, **Progression**,
**Map** (world, blueprints, datapack), **Pack**, **VF**.

### Phase 0: Foundations

**Deliverables**
- **Pack:** the Gradle multi-project, CI building every jar, a `.mrpack` pinning Minecraft 26.3,
  Fabric Loader 0.19.5 and VF 2.29.x, and a release job that zips the master world.
- **VF:** the public APIs: extra wardrobe namespaces (VF reads wardrobe textures and the catalog
  only from the `villagefriends` namespace today, see
  [ResidentSkins.java](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/src/client/java/dev/villagefriends/client/ResidentSkins.java)
  and [Wardrobe.java](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/src/main/java/dev/villagefriends/outfit/Wardrobe.java)),
  a currency item, hand-built taverns, a resident appearance seed.
- **Core:** the player record, the save seed and its streams, the condition and action language,
  story flags, events, stat modifiers, data loading with validation, settings and difficulty.
- **Progression:** the quest engine skeleton (the quest format, the journal, roles, anchors,
  versioning) with sample quests; `ranks.json` with the whole ladder.
- **Village:** today's wardrobe moved into the content mod; residents from map markers; the clan
  loader; the creator screen v1; age-stage scaling.
- **Life:** adventure rules as a game rule.
- **Combat:** the player poser spike: one clip on the player in third and first person.
- **Map:** the master world (empty generator, border, VF and vanilla worldgen off, builder mode),
  the paste tool, `layout.py --check`, one test street.
- **Tools:** `quests.py` with `--check`, `--graph` and the templates.

**Exit criteria**
- CI builds every jar; each mod boots on its own with only its dependencies; the `.mrpack`
  installs with the zipped world; `wardrobe.py --check` and `quests.py --check` pass.
- In the test street, ten Leaf residents spawned from markers walk, blink, sleep in their own beds,
  eat and greet you, and a resident trade costs ryo; a Varied world and a Classic world from the
  same file give different and the same residents respectively, and the same seed gives the same
  residents twice.
- A sample quest with a branch, a role, an anchor and a flag runs start to finish and survives a
  save and reload; nothing in the test street can be broken or placed.

### Beta 1: the opening and the Academy (~4 h main path)

**Deliverables:** chapters 0 to 7 and Beta 1's side quests ([section 8](#beta-1-the-opening-and-the-academy-4-h)); from [section 7](#systems-by-slice), every Beta 1 system; the Beta 1 districts ([schedule](#district-schedule)).

- **Village:** the full creator screen, all 25 clans pickable; the population draw and the civilian collections; Academy outfits; Academy kids and
  the instructor with lesson routines; the Classic cast and Varied rolls; the child stage.
- **Life:** apartment and furnish mode, the first Leaf furniture set, chests, ryo, stipend, jobs,
  the daily cycle and fatigue, hospital wakes, Leaf dish buffs, the workbench, pets.
- **Combat:** chakra, typed and radial signs, Clone, Transformation, Substitution, taijutsu v1,
  practice tools, the Story difficulty, the prologue's scripted guards.
- **Progression:** levels 1 to 5, death penalty and floors, roles bound, the Academy chapters,
  bond quests, the graduation exam, promotion to Genin, the Academy rank pools.
- **Map:** the prologue, the Academy district and the other Beta 1 districts.

**Exit criteria**
- Playtesters finish Beta 1 in 3 to 5 hours (median main path) with no commands, from the creator
  screen to Genin, in both Classic and Varied.
- They earn ryo, buy, craft and place furniture, store things in a chest, sleep every night, feel
  fatigue if they stay up, and have a pet following them; classmates have names, personalities,
  families and friendship levels.
- Every Beta 1 seed flag is set by the end of the slice (checked by `quests.py --check` against
  `story/seeds.json`).
- Unit tests cover combo timing, sign matching, chakra, fatigue, level loss, furnish bounds, the
  seed streams and role binding; client game tests run the prologue and the graduation with
  screenshots.

### Beta 2: Genin life (+~8 h)

**Deliverables:** chapters 8 to 14, Beta 2's side, filler and clan quests; every Beta 2 system;
the Beta 2 districts.

- **Progression:** the Mission Desk with D-rank (five templates) and C-rank (escort, bandit
  clearing, delivery to a far region) board missions, paid in ryo and XP and failing on death;
  team assignment and the bell test; teammates who can leave; mentors; levels 5 to 15; the event
  director with the Leaf Festival and New Year.
- **Combat:** chakra movement; parry and launcher; the nature ceremony and one jutsu per nature;
  the clan techniques (first tier) of the 15 noble clans and the three minor clans with abilities and the first kekkei genkai stages; thrown tools and bombs;
  the shinobi entity and brain v1 (bandits, rogue ninja, enemy scouts and cells).
- **Life:** the tool, weapon and scroll shops; the smithy and its recipes; crafted grades.
- **Core:** the region interface and the first far region.
- **Map:** the Beta 2 districts.

**Exit criteria**
- Playtesters go from Genin to Chunin Exam eligibility (level 15) in 6 to 10 hours (median main
  path), learning jutsu from a mentor, a bought scroll and a mission reward.
- Every mission template completes, and fails on death, in a client game test; a Varied save's
  board differs from a Classic save's and is the same for the same seed.
- Bandits use at least four techniques and dodge; each clan technique works for a clan-born player
  and a clan sparring partner.

### Beta 3: the Chunin Exams (+~3 h)

**Deliverables:** chapters 15 to 20, Beta 3's side quests; every Beta 3 system; the Beta 3
districts.

- **Progression:** the Chunin Exams as a calendar event, with NPC teams every season and results in
  village news; the three stages; judged promotion; the exam reward technique.
- **Combat:** the finals' enemy loadouts; the Sharingan's awakening.
- **Life:** bedroll camping and On Duty fatigue.
- **Village:** the Chunin wardrobe.
- **Map:** the Forest of Death, the stadium with seated spectators, the attack dressing (smoke,
  rubble entities, closed streets).

**Exit criteria**
- The whole beta plays from the creator screen to Chunin in 12 to 18 hours (median main path), with
  side quests on top.
- The exams run with and without the player each season; a player can enter, finish all three
  stages and be promoted or not on judged performance; the attack plays start to finish.
- 150 seated residents in the stadium keep 60 fps on a mid-range PC.
- Every seed in `story/seeds.json` marked `beta` is set somewhere in the beta, and the later arcs'
  stubs load without errors.

### Playtesting

- Every slice goes to playtesters before the next is built. The pack writes an opt-in local play
  log (time per chapter, deaths, ryo earned and spent, missions taken, fatigue hits, side quests
  done) that testers can send with their notes.
- Tuning happens in data (`ranks.json`, `economy.json`, `life.json`, `difficulty.json`, quests),
  not code, so a balance pass is a datapack update.
- After Beta 3, the hour budget for the later stretches is revisited with real numbers.

## 10. Story bible

*FOUNDATION (later).* The whole ~60-hour story is laid out in a separate file:

> **[docs/story/STORY_BIBLE.md](docs/story/STORY_BIBLE.md): SPOILERS, for developers only.** It holds
> the antagonist, the twists, the Hokage line, the recurring characters, the arcs from the Academy
> to the Eighth Hokage, the beta's chapters in full and the seeds the beta plants for later arcs.
> Do not open it if you want to play the game unspoiled.

What the roadmap needs from it, spoiler-free:

- **Stretches and hours** follow the [length budget](#1-vision): Academy, Genin and Chunin Exams in
  the beta; Chunin, Jonin, the optional ANBU branch and the road to Hokage later.
- **Seeds:** every story flag the beta sets for a later arc is declared in `story/seeds.json`, and
  `quests.py --check` warns about seeds never paid off ([Story flags](#story-flags)).
- **Roles:** the story's characters are role-bound or fixed ([Your squad and roles](#your-squad-and-roles)),
  so later arcs work in Classic and Varied saves alike.
- **Later arcs** exist as stubs in `story/arcs.json` (titles, unlock conditions, the seeds they read).

## 11. Later systems

*FOUNDATION (later).* Systems the later arcs need. Their data shapes are already reserved in
[section 5](#5-data-formats-built-for-the-whole-story) (ranks, actions such as `time_skip`,
`carve_face`, `found_clan`, `marry`), so they plug in without a rewrite.

### Ranks after Chunin

| Rank | Requirements | Unlocks |
|---|---|---|
| Chunin | Promotion in Beta 3 | B-rank missions, leading NPC Genin on missions, the outer training grounds, a flat or a clan room, founding a clan, the second-nature trials |
| Jonin | Level 30, 10 B-rank and 2 A-rank missions, lead three squad missions without losing a teammate, master one A-rank jutsu; a trial bout and a council review | The Jonin wardrobe, A-rank missions, your own NPC Genin team, the standby station, clan masters, the third nature |
| ANBU (optional branch) | An invitation at level 35 with a stealth record and no bad deeds in the last season; a night infiltration test | Masks and armor, ANBU HQ, S-rank and covert missions; the mask hides your identity from residents; you can return to regular duty at any time |
| Hokage | Jonin (ANBU or not), level 50, the highest standing in every district and clan quarter, the last arc | The Kage hat and haori, the office and quarters, assigning NPC teams, setting festivals, approving promotions and clan estates, your face as the Eighth |

### Homes after the beta

| Rank | Home |
|---|---|
| Chunin | Rent a two-room flat with a balcony (300 ryo a week), or move into your clan's quarter if clan-born |
| Jonin | Buy a small house (about 30,000 ryo), or a larger clan room |
| Clan founder | Your clan's estate |
| Hokage | Quarters in the Residence |

Moving is a mover NPC: furniture and chests are packed into moving crates (items that keep their
contents) and placed again in furnish mode.

### Player clans

A clanless player (or a clan-born player leaving their clan) can found a clan at the registry in
the Hokage Residence: Chunin, level 20, 20,000 ryo, and Good Neighbor standing or better.

- **The clan file:** saved as a clan JSON in exactly the [CLANS.md](CLANS.md) format, in the world
  save (`shinobi_progression/clans/<id>.json`); Shinobi Village reads shipped and player clans with
  the same loader.
- **The editor:** a name (id prefixed `player_`), colors from a palette picker for the roles (`P`,
  `S`, `A` and the rest; the wardrobe recolors by palette at run time), a crest (a 16 × 16 pixel
  editor or a library made with `glyphs.py`, drawn as one runtime decal), a look (hairstyles, hair
  and eye colors, up to two marks), up to four outfits from pieces you own, a clan art (a technique
  you mastered) and a clan day.
- **Members:** clanless residents at friendship level 7 or more who agree; they keep face and name,
  take the clan's colors and outfits, and join your missions. Up to 3 at founding, 8 at Jonin, 20
  as Hokage.
- **Home:** one of the four vacant estates; halls open as you buy them (5,000 to 15,000 ryo each).
- **A story-unlocked option:** later in the story the registry offers one more founding path
  (details in the story bible).

### Romance and marriage

VF runs romance between residents (`social/`: meters, `Chemistry`, sweethearts at meter 50,
marriage after 30 to 150 days at 65 or more). Shinobi Life extends it to the player:

- **Who:** single residents of the same age stage (teen with teen, adult with adult), including
  squadmates; their personality and chemistry decide interest. Never children, and nothing in the
  beta.
- **Dating:** at friendship level 7 ("spend time together": walks, ramen, festival nights);
  confessing at level 8 makes you sweethearts (village news).
- **Marriage:** adults only, at level 10, a proposal and a wedding at the shrine; a spouse is the
  strongest [Kindling Bond](#kindling-bond). Your spouse moves
  in; a clanless player may join the spouse's clan, or the spouse may join yours.
- **Children (post-game):** a married player can have children. They are VF residents born into
  your household (VF already records parents, households and surnames for residents' babies),
  grow up through VF's children's routines, games and lessons, and can enrol at the Academy.

### Kindling Bond

*Decided.* A bond ability the player unlocks at a story moment after the beta (the beta at most
foreshadows it).

- **What it does:** kindle a bonded ally's chakra nature or one of their techniques and borrow it
  briefly: a few casts of their nature's jutsu, or one use of their signature technique, then the
  flame needs time to rekindle.
- **Bonds decide what you can borrow:** friendship level 6 lets you borrow an ally's nature, level 8
  one of their techniques, level 10 (or a teammate, your sensei, your spouse) both and for longer.
  It ties combat to the friendship and romance systems: the village you befriend is your arsenal.
- **Natures:** one of the ways to gain more elements. A nature borrowed often enough can be learned
  for good with a master's trial.
- **How it looks:** a bond-flame, a small watch-fire, flickers between you and the ally, and your
  chakra takes their nature's colour while it burns.
- **In the systems:** Shinobi Combat adds a `kindle` effect type; Shinobi Life's friendship and
  romance levels are its bond levels; Core's natures list gains a "borrowed" source; Progression
  unlocks it with a story flag.

### Elemental natures

| Nature | How you get it |
|---|---|
| First | Chosen at the Genin ceremony (Beta 2) |
| Second | Chunin: a nature master's three trials |
| Third | Jonin: a clan master or a mission line |
| More | [Kindling Bond](#kindling-bond) (a nature borrowed often enough through a bond can be learned with a master's trial) and rare milestones in the later arcs |

Your natures' jutsu cost 25% less; other natures' jutsu cannot be learned.

### Clan techniques and kekkei genkai

Clan-born players learn the first tier in Beta 2; later tiers come with rank. Kekkei genkai come
only through clan membership; clanless players learn one lesser technique per friendly clan.
Summoning, and with it tailed beasts, are out of scope.

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
| Tsuchigumo (minor) | Earth binding | Earth-style ninjutsu and a web-like binding trap that holds one target | sign, ground slam |
| Suzuran (minor) | Herbalist | Immunity to poison, and herbal poultices and poison coatings crafted at the workbench | — |
| Tobari (minor) | Smothering | Silences your footsteps and techniques within a few blocks at night: enemies do not hear you | sign |
| Gekko | Dance of the Crescent Moon | Kenjutsu: two short-lived clones appear and all three strike a target at once from three sides | three-way slash |

**Genjutsu.** Three clans (Kurama, Yuhi, Uchiha) use illusions, so genjutsu is one shared effect
type: a caught target sees a client-side illusion (fake entities, a distorted screen, a wrong HUD)
and moves slowly. It breaks when the target weaves the release sign, takes damage, or a teammate
touches them.

### Later techniques and combat

- **Shadow Clone** (Chunin): 2 to 4 real clone entities with basic combat AI, each costing a share
  of chakra.
- **Lightning Blade** (Jonin): charge, then a straight dash that breaks through a block or parry.
- **Mind Transfer** (Yamanaka, Chunin or later): the camera moves into a mob or resident for 8 s;
  your body slumps and can be hit.
- **Stealth** (Jonin and ANBU): detection by sight and sound, night operations.
- **Kindling Bond** (after the beta): see [Kindling Bond](#kindling-bond).

### The full event calendar

All events run off VF's calendar (112 days a year, a year is about 37 hours of play). The beta uses
the Leaf Festival, New Year and the Chunin Exams; the rest arrive with the later arcs.

| Event | When | What happens | Reuses |
|---|---|---|---|
| Leaf Festival | Summer 14, evening | Stalls on the main street, lanterns, fireworks at 21:00 over the Hokage Rock, festival games for small ryo prizes (goldfish scooping, target throwing), yukata outfits to buy | Birthday party pattern (`Birthdays`), Market Day crowd behavior |
| New Year | Winter 28 → Spring 1 | Shrine visit, the Hokage's address, the succession if due (the one night event everyone stays up for: no fatigue until 02:00) | Calendar, VF news |
| Chunin Exams | Spring 15 to 21 and Autumn 15 to 21 | Written test (day 15), Forest of Death (16 to 20), finals (21). Run every season with NPC teams; the player joins when eligible | Fishing `Contest` as the pattern for entrants and results; `Seat` for spectators |
| Academy graduation | Spring 7 and Autumn 7 | Ceremony in the yard; the player's own graduation is the first one they pass | Lessons in VF's routine |
| Weddings | When a couple marries (residents or the player) | A ceremony at the shrine with family and friends, then a party | VF romance and marriage, party behavior |
| Clan days (15 noble clans, a shared day for the minor clans' neighbourhoods, plus player clans) | One per clan per year, spread so no two fall in the same week | Senju and Uzumaki: founders' memorial at the shrine (Spring); Hyuga: main and branch house ceremony; Akimichi: harvest feast (Autumn); Inuzuka: ninken pairing, where children get their first pup; Nara: deer count in the forest; Yamanaka: flower festival (Spring); Uchiha: police parade; Sarutobi: the Will of Fire lantern walk (New Year eve); Aburame: insect night, with fireflies over the gardens (Summer); Hatake: a quiet visit to the memorial stone; Kurama: painting exhibition; Yuhi: grove viewing (Spring); Gekko: moon-viewing kenjutsu duels (Autumn full moon); Shimura: none in public, a beat of the ANBU branch instead; player clans: their chosen day | Party behavior, Hearth & Harvest dishes, VF pets for the pups |
| Border incident | Random, about weekly | Rogue ninja or bandits at a gate or on a road; a short fight, a deed, a small reward | VF guard call-out |
| Story arcs | Story-gated | The main plot's big moments, once each (see the story bible) | Guards, knockouts, the arena |

Story events never damage the map: "damage" is dressing (smoke, rubble entities, closed streets)
removed when the arc moves on.

### Regions and multiplayer

New regions (other villages and far lands) are datapack regions with their world
data ([Regions](#regions)). Multiplayer comes after the single-player story ([Multiplayer](#multiplayer-later)).

## 12. Risks and open questions

*Both.*

### Risks

| Risk | Why | What we do |
|---|---|---|
| Content volume | 60 hours of main path plus many side quests, half hand-written | The beta first, measured before writing more; half of every stretch systemic; one quest format and fast tooling; story as data |
| Formats that do not scale | Later arcs need branching, new objectives and world changes | Graph-shaped quests, roles and anchors, one condition and action language, reserved later actions, the whole ladder and every arc stubbed now, versioned files with migrations |
| Player animation | VF poses residents only; the player model and first person are new code | Spike in Phase 0; clips in VF's format |
| VF on a hand-made map | VF finds houses and taverns through generated structure pieces | Plaques and markers; a tavern API in Phase 0; residents from markers; test every VF system on the map world early |
| Reproducible Varied saves | Any unseeded randomness breaks "same seed, same save" | All rolls go through Core's seed streams; a CI test builds two saves from one seed and compares them |
| Separate mods drifting | Six mods, VF and a map must stay in step | One repository and CI; the manifest pins a tested set; each mod boots alone in CI |
| Coupling between mods | It is tempting to call a higher mod directly | Only Core's events, record, conditions, actions, stat modifiers and interfaces cross mod lines; CI checks declared dependencies |
| Version churn | VF or Minecraft moving mid-beta | Minecraft 26.3 and Loader 0.19.5 pinned for the whole beta; port only between slices |
| Romance and age | The beta's characters are children | Romance only within the same age stage and from teen, enforced in code; nothing romantic in the beta |
| Combat feel | Minecraft combat is coarse | Server-decided hits, generous windows on Story difficulty |
| Map building cost | The beta alone needs the Academy district, the civilian streets, 15 noble clan quarters, 10 minor clan neighbourhoods, training grounds, the forest and the stadium | Paste everything repeatable; hand-build only landmarks; clan quarters as cores in Beta 1 |
| Economy and fatigue balance | Too easy or too harsh | Every number in data; playtest each slice |
| Performance | 150 to 250 residents in one area | Measure in Phase 0 and Beta 3; split Konoha into several VF settlements if needed |
| Spoilers leaking | The owner will play the game | Every twist lives only in the story bible; the roadmap, the README, commit messages and summaries stay neutral |
| Naming and IP | Naruto names, symbols and places belong to their owners | Original characters, Hokage and plot; cameos only; the pack's own name; a free fan project |

### Still open

Nothing is open right now. The story's specifics are the developers' creative call, kept in the
story bible so the owner can play unspoiled.
