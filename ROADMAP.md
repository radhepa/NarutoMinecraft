# Roadmap

From a wardrobe of Naruto-styled residents to an adventure map of the whole Hidden Leaf, where you
start as an academy student and rise to Hokage.

This plan builds on [Village Friends](https://github.com/radhepa/Village-Friends-Minecraft-Mod)
(VF below) wherever VF already solves a problem. File links point at VF's `main` branch. VF
targets **Minecraft 26.3 on Fabric** (loader 0.19.5, Fabric API 0.161.0+26.3, Loom 1.17.21,
Java 25; VF 2.29.1, see its
[gradle.properties](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/gradle.properties)).
Naruto Minecraft targets the same versions and stays on them. Moving to another Minecraft version
is separate work, as it is for VF.

## 1. Vision

Naruto Minecraft is an adventure map of the Hidden Leaf: one walled village under the Hokage Rock,
built district by district, full of residents who live their own days. You arrive as an Academy
student with a wooden practice kunai and no chakra control. You leave as Hokage, with your face
carved into the cliff.

The village matters more than the fighting. Residents wake, work, eat at Ichiraku, gossip, train,
fall in love and remember what you did. That is VF's resident model, which already runs routines,
friendships, families, deeds and notice boards. Naruto Minecraft dresses those residents as
shinobi and civilians of the Leaf, gives each one a rank, and adds what VF lacks: ninja combat,
chakra, jutsu, missions, exams and a story that moves the player up the ladder.

Progress is earned through milestones, not grinding XP. Each rank has a few things you must do
(pass an exam, finish missions, prove a technique), and each promotion visibly changes your
outfit, what you can do, where you can go and how the village treats you. Recurring events
(festivals, the Chunin Exams twice a year, clan days) and a few crisis arcs give the calendar a
pulse. Combat is fast and readable: chained taijutsu, dodges, chakra-powered movement across roofs
and water, jutsu woven from hand signs, and thrown tools. It runs on Minecraft's own systems where
it can and on custom animation where it must.

**Ladder:** Academy → Genin → Chunin → Jonin → ANBU → Hokage (as in the [README](README.md)).

## 2. Where we start

| Have | Where |
|---|---|
| Naruto wardrobe: hair, tops, bottoms, headwear, faces, palettes, eye colors (Sharingan, Byakugan), compiled from Python | `tools/wardrobe/` → `src/main/resources/assets/narutominecraft/wardrobe/` |
| 21 characters with a `rank`: Genin, Jonin, ANBU and kage/signature looks | `tools/wardrobe/characters/`, renders in `docs/renders/` |
| Clan system: clan JSON, resident mixing after VF's OutfitFactory, id blocks per clan | [CLANS.md](CLANS.md), `tools/wardrobe/clans/` |
| Eight clans (Senju, Uzumaki, Uchiha, Hyuga, Nara, Akimichi, Yamanaka, Inuzuka) | in progress on `clan/*` branches (not on `origin` yet) |

| Missing | Notes |
|---|---|
| Any Java: no mod, entities, items or gameplay | Phase 0 |
| Academy, Chunin and civilian outfits | README notes Academy and Chunin are still to come; civilians (shopkeepers, the ramen cook, farmers) have no Naruto wardrobe at all |
| Buildings, the map, animations for ninja | Phases 1 to 6 |

### What Village Friends already gives us

| Need | VF already has it | Use it for |
|---|---|---|
| Residents that look and move like ours | Resident model, Living Eyes, wardrobe layer, OutfitFactory ([OUTFIT_ENGINE.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/OUTFIT_ENGINE.md), [ANIMATION_EDITING.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/ANIMATION_EDITING.md)) | Every Leaf resident; our wardrobe tools are a port of this |
| Daily lives | `routine/Routine.java`, `ResidentRoutines` ([VILLAGE_DAYS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/VILLAGE_DAYS.md)): hours, meals, work, lessons, night watch, Market Day | Shinobi duty shifts, Academy lessons, gate watch |
| Community | `social/` census, relationships, families, news, friendship levels, speech bubbles, Ledger ([VILLAGE_LIFE.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/VILLAGE_LIFE.md)) | Clan families, village news ("The Chunin Exam finals start tomorrow") |
| Talk | 5,898 lines in `tools/dialogue/`, chosen by `talk/Talk.java` | Add rank and event pools |
| Reputation | Deeds, witnesses, rumors, standing ([DEEDS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/DEEDS.md)) | How the village reacts to the player beyond rank |
| Quests | Notice boards: `quest/Postings`, `quest/Board`, `quest/QuestLog`, `VillageQuests` ([BIRTHDAYS_AND_NOTICES.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/BIRTHDAYS_AND_NOTICES.md)) | The D-rank mission board, almost as is |
| A calendar | `social/Calendar`: 4 seasons × 28 days, village weeks, Market Day | Scheduling every event |
| Scheduled community events | Birthdays and parties (`Birthdays`), the fishing contest (`fishing/Contest`) | The pattern for festivals and exam days |
| Escorts and companions | `CompanionController`: follow, wait, rescue | C-rank escorts, NPC teammates |
| Non-lethal defeat | `Knockouts`: residents are knocked out, not killed ([GUARDS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/GUARDS.md#knockouts)) | Sparring and exam fights |
| Defenders | Knights and archers, call-out on village grounds, guard levels (`GuardController`, `GuardProgression`) | Village defense during invasions |
| Restaurants | Tavern: seating found in any tavern building, served course by course (`tavern/`, [TAVERN.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/TAVERN.md)) | Ichiraku Ramen, the barbecue house, arena seating via the `Seat` entity |
| Homes | Housing index, House Plaque flood fill for hand-built houses ([HOMES.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/HOMES.md)) | Giving every resident a bed in a hand-built Konoha |
| Pets | Residents' cats and dogs ([PETS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/PETS.md)) | Inuzuka ninken, the "catch the runaway cat" D-rank |
| Children's games | `play/Games`, `Playground` ([PLAYTIME.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/PLAYTIME.md)) | Academy kids at recess |
| Food | Hearth & Harvest dishes from one table ([HEARTH_AND_HARVEST.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/HEARTH_AND_HARVEST.md)) | Ramen, dango, soldier pills as dishes |
| Buildings from code | Python design programs → blueprints → NBT (`tools/village_design/`, `tools/create_village_structures.py`, [BUILDING_EDITING.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/BUILDING_EDITING.md)); standalone templates placed by code ([standalone_templates.json](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/tools/standalone_templates.json)) | Every repeatable Konoha building |
| Animation clips | Python-keyed clips compiled to `resident_animations/*.json`, packs from other namespaces load too ([ANIMATION_PACKS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/ANIMATION_PACKS.md)) | Resident ninja clips with no Java; the clip format for the player too |
| An add-on precedent | `rpg/`: a separate jar requiring VF, hooked by mixins and VF's public events, a synced player attachment, keys, a HUD badge, cooldown abilities, pure balance classes ([rpg/README.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/rpg/README.md)) | The shape of Naruto Minecraft's code |
| In-game tests and screenshots | `runClientGameTest` with focused flags, gallery screenshots ([VERIFICATION.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/VERIFICATION.md)) | Done criteria for every phase |

What VF does **not** have, and we build: player animation (VF animates residents only), combat
beyond vanilla swings and guard AI, chakra and abilities beyond the RPG's cooldown actives, a fixed
hand-built map (VF villages are procedural), and anything Japanese in its building kit.

## 3. The map

### Scale

A Minecraft player is 1.8 m tall and a block is 1 m. Keep **heights and interiors at 1:1** so
doors, rooms and stairs feel right, and **compress distances**: the Konoha of the show is several
kilometres across, which in Minecraft would be empty walking.

- **Inside the wall:** a rough circle about **640 blocks across** (40 chunks). Sprinting across
  takes about two minutes; roof-hopping with chakra about one. That fits roughly 250 to 400
  buildings, of which perhaps 180 homes.
- **Hokage Rock:** a cliff on the north edge about 70 blocks high; each face about 24 blocks tall.
- **Outside the wall:** the Forest of Death, outer training grounds and roads to the gates, about
  a 1,200 × 1,200 block map in all. Beyond that, ordinary generated terrain with VF villages
  switched off (see open questions).
- **Population:** about 150 to 250 residents to start. VF residents tick routines once a second,
  so measure before going higher.

### Generated or built by hand

The rule: anything there are many of is a **design program** in Python, in VF's blueprint
pipeline, with a new Japanese building kit. Anything that appears once and defines the village is
**built by hand** in a world and saved as a structure, then listed as a standalone template so the
map builder can place it again.

| District / landmark | How | Notes |
|---|---|---|
| Homes, apartments, shops, tea houses | Generated | Konoha kit: plaster walls in cream and terracotta, round water tanks on flat roofs, awnings, paper lanterns, stacked apartment blocks. Rooms must follow VF's lot contract (beds in enclosed rooms, doors with two clear blocks) so Homes can assign beds |
| Streets, alleys, bridges, the river | Generated | A Konoha `roads.py`: packed dirt and stone lanes, utility poles, signs |
| Wall and gates | Generated modules, gates by hand | Wall segments are one repeated module; the great A-UN gate and guard booth are hand-built |
| Hokage Rock | By hand | Voxel sculpting; one empty face is kept for the player (Phase 6) |
| Hokage Residence / Administration (the round red building) | By hand | Mission desk on the ground floor, Hokage's office on top |
| Ninja Academy | By hand | Classroom, yard with the swing tree, target posts; the vertical slice |
| Ichiraku Ramen | By hand (small) | A VF tavern building, so the tavern code seats and serves residents |
| Barbecue house, dango shop, flower shop, weapon shop | Generated or small hand builds | Flower shop belongs to the Yamanaka compound |
| Clan compounds (8) | Hand-built core, generated houses | Each has a gate, a main hall, a training yard and a few homes. Senju: wood and tree motifs; Uzumaki: memorial shrine with spiral crests; Uchiha: walled quarter with the fan crest and police HQ; Hyuga: formal estate with a dojo; Nara: house by the deer forest; Akimichi: big kitchen hall; Yamanaka: flower shop and greenhouse; Inuzuka: kennels and an open run |
| Training grounds | Generated props, Ground 3 by hand | Ground 3: three posts, the river and the memorial stone. Others: target posts, logs, a lake for water-walking, a cliff for wall-running |
| Hospital | By hand | Works with VF knockouts: revival happens here |
| Chunin Exam arena | By hand | About 64 blocks across the floor, tiered seating for ~150 residents on VF `Seat` entities, a Kage box |
| Forest of Death | Generated | Fenced 384 × 384 block area outside the wall, 44 gates, a tower in the middle (by hand). Giant trees 4 to 7 blocks thick and 60 to 90 tall from a tree generator, so they are tree-hopping terrain |
| ANBU HQ | By hand, hidden | Under the Hokage Rock, only reachable as ANBU |
| Police HQ, the market, the main street | Generated around hand-built centres | |

### How the map is made

1. A **map layout file** (`tools/konoha/layout.json`) places every district: polygon, streets,
   plots, which designs go on which plots, the landmarks' positions and rotations.
2. Design programs in `tools/konoha/buildings/*.py` write blueprints in VF's format; VF's
   compiler turns them into NBT.
3. A **map builder** (a dev command, `/naruto build <district>`) stamps a district into a world
   from the layout. Rebuilding one district never touches the others.
4. The world is then finished by hand (terrain, the rock, the trees) and shipped as the adventure
   map's save, with the mod jars.

Konoha is not jigsaw-random: it must look the same for everyone because the story points at
places. The layout file makes it reproducible.

## 4. Progression

Ranks are milestones, not levels. The player's rank, record and unlocks live in one synced player
attachment (like the RPG's). Each rank has a few required milestones and an exam or a promotion
event. Optional milestones speed things up or unlock extras.

### Academy student

- **Start:** you wake in a small apartment near the Academy, enrolled for the final term. No
  chakra bar yet; it appears after the first chakra lesson.
- **Milestones:** attend lessons (taijutsu forms, kunai and shuriken throwing at targets, chakra
  control by sticking a leaf to your forehead, the Transformation and Substitution basics), spar a
  classmate, and win one recess game with the Academy kids (VF `Playground`).
- **Exam: graduation.** A written quiz (five questions, from dialogue), a throwing test (hit 6 of
  10 targets), and the **clone test**: weave Ram-Snake-Tiger and make at least three working
  clones in front of the instructor. Failing costs nothing but time; you can retake it the next
  week.
- **Unlocks:** the forehead protector (headwear `w02_forehead_protector`), the Genin wardrobe
  (Scout, Brawler, Kunoichi, Tracker, Scroll Bearer looks from the README), the chakra bar, the
  first three jutsu, the Mission Desk lobby, Training Ground 3.

### Genin

- **Team assignment:** a ceremony at the Academy places you with two NPC teammates and a Jonin
  sensei, generated as VF residents with clan or role looks. They follow you as companions on
  missions (VF `CompanionController`), have their own personalities and friendships, and talk.
- **Bell test:** the sensei's first test at Training Ground 3: take one of two bells in five
  minutes. It teaches teamwork: you only pass if a teammate gets a bell too.
- **Missions:** D-rank chores from the Mission Desk (the VF notice board with Leaf skins:
  deliveries, weeding, catching the runaway cat, babysitting, gathering), then C-rank escorts and
  bandit clearing outside the walls.
- **Training:** tree walking (unlocks wall-running), water walking (on the training lake), your
  elemental affinity (chakra paper at the weapon shop), your first elemental jutsu.
- **Eligibility for the Chunin Exams:** 8 D-rank and 2 C-rank missions, tree walking, and your
  sensei's recommendation (friendship with the sensei at a set level).
- **Residents:** Academy kids follow you about (the VF "curious child" behavior), shopkeepers call
  you by name, Genin your age treat you as a rival.

### Chunin

- **Exam: the Chunin Exams**, in three stages (an event, section 5):
  1. **Written test** in an Academy hall: ten questions too hard to answer; the real test is
     gathering answers unseen (Byakugan, transformation, a clone in the rafters, bribing a proctor
     in dialogue). Caught three times and your team is out.
  2. **Forest of Death:** your team gets one scroll of a pair (Heaven or Earth) and has five game
     days to reach the tower with both. Rival NPC teams carry the other scrolls. Survival, ambushes,
     traps, camping.
  3. **Preliminaries and finals** in the arena: one-on-one bouts with residents watching from the
     stands. Promotion is judged on how you fought (techniques used, tactics, teamwork earlier),
     not only on winning, so losing a good final can still make you Chunin.
- **Unlocks:** the Chunin flak vest (wardrobe to build), B-rank missions, leading a Genin squad
  on missions, the outer training grounds, the hospital's back rooms, a second elemental nature.
- **Residents:** Genin salute you, Chunin speak to you as a colleague, you are invited to clan
  gatherings.

### Jonin

- **Milestones:** 10 B-rank and 2 A-rank missions, lead three squad missions without losing a
  teammate (knockouts count as losses), master one A-rank jutsu.
- **Promotion:** a trial bout against a Jonin examiner and a review by the council (a scripted
  scene in the Hokage's office).
- **Unlocks:** the Jonin wardrobe (Leaf Jonin, Sentinel, Field, Kunoichi Jonin, Commander), A-rank
  missions, taking on your own Genin team (you assign their missions; they grow), the Jonin
  standby station, jutsu training from clan masters.

### ANBU

- **Recruitment:** an invitation after Jonin, if your record includes stealth missions and no bad
  deeds in the last season. A night test: infiltrate a guarded compound unseen.
- **Unlocks:** the ANBU masks and armor (Fox, Cat, Wolf Captain, Hawk Tracker, Root looks), ANBU
  HQ, S-rank and night missions, the right to wear the mask, which hides your identity: residents
  stop recognizing you while it is on (VF reputation lines switch to the ANBU pool).
- **Residents:** civilians step aside, children whisper, ANBU residents finally speak to you.

### Hokage

- **Succession:** when the player is ANBU or Jonin with the highest standing in every district
  and clan compound (VF standing aggregated across the village), the sitting Hokage announces
  retirement at the next New Year. A final crisis arc decides it: defend the village (section 5).
  Then the inauguration, and your face appears on the Hokage Rock (the map builder swaps the empty
  face for yours, read from your wardrobe look).
- **Unlocks:** the Kage hat and haori, the Hokage office, assigning missions to NPC teams, setting
  the festival calendar, approving promotions of residents, and building permits (new districts
  you can open with the map builder's plots).

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

## 5. Events

All events run off VF's calendar (`social/Calendar`: 4 seasons of 28 days, 112 days a year, a
Minecraft day is 20 minutes, so a year is about 37 hours of play). Each event is a JSON file; an
**event director** on the server checks once a game minute which events start, run or end.

| Event | When | What happens | Reuses |
|---|---|---|---|
| Leaf Festival | Summer 14, evening | Stalls on the main street, lanterns, fireworks at 21:00 over the Hokage Rock, festival games (goldfish scooping, target throwing), yukata outfits | Birthday party pattern (`Birthdays`), Market Day crowd behavior |
| New Year | Winter 28 → Spring 1 | Shrine visit at midnight, the Hokage's address, the succession if due | Calendar, VF news |
| Chunin Exams | Spring 15 to 21 and Autumn 15 to 21 | Written test (day 15), Forest of Death (16 to 20), finals (21). Run every season with NPC teams; the player joins when eligible, so the world keeps its rhythm | Fishing `Contest` as the pattern for entrants and results; `Seat` for spectators |
| Academy graduation | Spring 7 and Autumn 7 | Ceremony in the yard; the player's own graduation is the first one | Lessons in VF's routine |
| Clan days (8) | One per clan per year | Hyuga ceremony at the estate, Akimichi feast, Inuzuka ninken pairing, Nara deer count, Yamanaka flower festival, Uchiha police parade, Senju and Uzumaki memorial at the shrine | Party behavior, Hearth & Harvest dishes |
| Border incident | Random, about weekly | Rogue ninja or bandits at a gate or on a road; a short fight, a deed | VF guard call-out |
| Crisis arcs | Story-gated | Multi-stage, once each: (1) an invasion during the Chunin Exam finals, (2) a rogue-ninja infiltration in the Jonin era, (3) the attack that decides the succession. Districts can be damaged and are restored by the map builder afterwards | Guards, knockouts, the arena |

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
`"recur": "once"`. Stages of a crisis arc are listed in the same file.

## 6. Combat

Combat runs on one **technique system**: every taijutsu move, dodge, jutsu and throw is a
technique with a cost, timing, animation and effect. The player's inputs and the NPC brains call
the same code, so enemies fight with what you fight with.

### Taijutsu

| Mechanic | How in Minecraft | Custom animation |
|---|---|---|
| Combo chain | Empty hand or kunai in hand: left click is caught (client mixin on the attack key) and sent as a combo input; the server runs the chain. 3 light strikes, about 6 ticks apart, the third knocks back. Vanilla's attack cooldown does not apply inside a chain; a 10-tick recovery follows | 3 strike clips, the finisher |
| Heavy and launcher | Hold left click for 8 ticks: a heavy strike; during a chain it launches the target upward (velocity) for an air follow-up | 2 clips |
| Hit detection | Server-side sweep: a 60° arc, 3 blocks deep, in front of the attacker. Each combo hit lowers the target's hurt invulnerability (vanilla's 10 ticks) so chains land | |
| Dodge | Double-tap a direction or press `Left Alt`: a 4-block dash with 6 invulnerable ticks, 1.5 s cooldown, a little chakra | dash clips per direction |
| Block and parry | Right click with an empty hand: block (cuts melee damage 60%). Block within 4 ticks of a hit: parry, staggers the attacker | block, parry |
| Substitution | Pressing dodge as a hit lands, with enough chakra: you blink back 5 blocks and a log drops where you stood. Once per 20 s | the "poof" (particles), the log entity |

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
with rank and training. Running out leaves you exhausted: Slowness for 10 s.

**Elemental natures.** Fire, Wind, Lightning, Earth, Water. The chakra paper picks your first
nature (or you choose; open question). Your own nature's jutsu cost 25% less; others are learnable
from Chunin on.

| Jutsu | Signs | Minecraft mechanic |
|---|---|---|
| Clone | Ram-Snake-Tiger | Illusory clones: client-visible copies of you that run off in different directions; mobs may target them. No damage |
| Transformation | Dog-Boar-Ram | Your render switches to a chosen resident's look; mobs lose their target; residents do not recognize you |
| Shadow Clone (Chunin) | Cross sign (a 13th, special) | 2 to 4 real clone entities with basic combat AI; each costs a share of chakra; they vanish in a puff when hit |
| Fireball | Snake-Ram-Monkey-Boar-Horse-Tiger | Fire projectile like a blaze fireball, sets mobs alight; no block damage inside the village (a rule per area) |
| Wind Blade / Gust | Snake-Ram-Boar | Vanilla's wind charge behavior: knockback, no block damage |
| Water Wall / Dragon | Tiger-Ox-Dragon (Wall) | A wave that pushes back and puts out fire; the dragon is a longer projectile |
| Earth Wall | Tiger-Hare-Boar-Dog | Places a short-lived wall of stone that crumbles after 10 s |
| Lightning Blade (Jonin) | Ox-Hare-Monkey | Charge 1 s, then a straight dash attack that breaks through a block or parry |

**Clan techniques.** Each clan grants one signature technique to members (see open questions on
whether the player picks a clan) and teaches it to friends of the clan later.

| Clan | Technique | Minecraft mechanic | Animation |
|---|---|---|---|
| Hyuga | Byakugan, Gentle Fist | Living things within 32 blocks glow through walls (like Spectral); Gentle Fist hits drain the target's chakra instead of only health | eye veins (face decal), palm strikes |
| Uchiha | Sharingan | Enemy attacks telegraph earlier (a client flash), parry window doubles, and a jutsu you watch an enemy cast is learnable | glowing eyes (already in the wardrobe) |
| Nara | Shadow Possession | A shadow line crawls along the ground to a target within 12 blocks; if it reaches, the target copies your movement for 5 s. Needs light: weaker at night and indoors | kneeling sign hold |
| Akimichi | Expansion, Human Boulder | Vanilla's `scale` attribute: grow to 2× for 10 s with more reach and knockback; the boulder is a rolling charge | expand, roll |
| Yamanaka | Mind Transfer | Your camera moves into a mob or resident for 8 s and you steer it; your body slumps and can be hit. Late in the plan: it is the hardest technique | slump, sign |
| Inuzuka | Fang over Fang | A spinning dash attack together with your ninken (a tamed wolf, through VF's pet code) | spin |
| Senju | Wood Release | Grows a short-lived wooden barrier or binding roots | sign, wood growth |
| Uzumaki | Sealing chains, large chakra | 30% more chakra; chains that hold one target for 4 s | chains |

### Ninja tools

| Tool | Item and mechanic |
|---|---|
| Kunai | Melee weapon that uses the combo system; right click throws it (a projectile like the trident) and it can be picked back up |
| Shuriken | Stackable, fast, low damage; throw three at once from Genin |
| Paper bomb | Tag on a kunai or stick on a block; explodes after 3 s; no block damage in the village |
| Smoke bomb | A cloud that blinds, and makes mobs drop their target |
| Wire | Ties two points for a trap that trips and roots |
| Tool pouch | A bundle-like item that only holds tools and fills its slots into the hotbar quick-throw |

### Enemy and sparring AI

- **One shinobi entity** for every human enemy, drawn with VF's resident model and our wardrobe,
  so rogue ninja and exam rivals look like the residents.
- **Brain:** a state machine on top of vanilla goals: keep a range band (close for taijutsu, mid
  for throws, far for jutsu), strafe, dodge telegraphed attacks with a chance set by rank, use
  substitution once per fight, retreat to heal, call allies. Each enemy has a loadout file:
  techniques, rank, chakra, tools.
- **Sparring:** challenge a resident with a shinobi rank at a training ground. The fight ends when
  someone is down to 30% health or yields; residents never die (VF knockouts). A win or a good
  fight raises friendship.
- **Difficulty:** by rank, not by health inflation: a Jonin reacts faster and uses more techniques.

### Animation

VF's clip system poses residents only (`ResidentLife`, `ResidentPoser`; the player is untouched).
For residents, our clips are a pack in our namespace (`assets/narutominecraft/resident_animations/`,
authored in Python like VF's `tools/animations/`), which VF already loads without Java: ninja
salutes, sparring stances, hand signs, meditation, guard duty on rooftops.

For the player, we add a **player poser** that samples the same clip format onto the player model
(a client mixin on the player model's animation setup), with a first-person arm path for hand signs
and throws. This is the largest piece of custom client work and is Phase 1's main risk.

Clips needed, by phase: hand signs (12 + the cross), the ninja run, chakra jump, combo strikes,
heavy, dodge per direction, block, parry, throw, meditation (Phase 1 and 2); wall-run, water
stance (2); clan techniques (4); Mind Transfer and the advanced jutsu (5).

## 7. Technical architecture

### Shape

- **Mod:** `narutominecraft`, its own jar that **requires Village Friends** (like VF's `rpg/`).
  It extends VF from outside: VF's public events, mixins on VF classes where needed, data files in
  our namespace. When we need VF to expose something, we add a small public API to VF (as its
  `stable/api` does) rather than patch around it.
- **Code** (package `dev.narutominecraft`):

| Package | Owns | Pure, unit-tested core |
|---|---|---|
| `rank` | Ranks, milestones, the player record, promotions | `Ladder`, `Milestones` |
| `chakra` | The chakra bar, regen, exhaustion | `ChakraMath` |
| `technique` | Technique registry, hand-sign input, casting, cooldowns, effects | `SignSequence`, `Mastery`, `Costs` |
| `combat` | Combos, dodge, block/parry, hit sweeps | `ComboTiming`, `HitArc` |
| `movement` | Ninja run, chakra jump, wall-run, water-walk | `WallRun` |
| `tools` | Kunai, shuriken, bombs, pouch: items and projectiles | |
| `shinobi` | The shinobi entity, its brain and loadouts | `RangeBands` |
| `mission` | Mission Desk, mission types, squads, rewards | `MissionRoll` |
| `event` | Event director, festival behaviors | `EventClock` |
| `exam` | Graduation and Chunin Exam stages, judging | `Judging` |
| `map` | Districts, zones, access rules, the map builder | `Zones` |
| `village` | Resident ranks, rank dialogue, VF glue | |
| client `hud`, `anim`, `look` | Chakra bar, sign radial, player poser, player wardrobe look | |

- **The player's look:** the player can wear the Naruto wardrobe (a character creator for hair,
  eyes, complexion and clan; outfits unlock by rank), drawn with VF's resident model. The look is
  part of the synced player attachment.
- **Tests:** the VF pattern: pure classes with JUnit tests, world glue thin, and client game tests
  with screenshots for each feature (`-Ptests=...`).

### Data-driven content

Everything that is content is JSON under `data/narutominecraft/naruto/`, validated on load (a bad
file is skipped and named in the log, as VF does for animation packs), and authored or checked by
Python tools under `tools/` with `--check`, matching the wardrobe.

| Folder | Holds |
|---|---|
| `ranks.json` | The ladder, milestones per rank, unlocks |
| `techniques/*.json` | Every technique: signs, cost, cooldown, rank, nature, clip, effect type and numbers |
| `missions/*.json` | Mission types and templates: rank, objectives, places, rewards, dialogue pools |
| `events/*.json` | Calendar and story events |
| `exams/*.json` | Exam stages and judging weights |
| `loadouts/*.json` | Enemy and sparring partner kits |
| `districts.json` | Zones, access rules, spawn points, the map layout's runtime part |

Technique sketch:

```json
{
  "id": "fireball",
  "signs": ["snake", "ram", "monkey", "boar", "horse", "tiger"],
  "mastered_signs": ["snake", "tiger"],
  "rank": "genin", "nature": "fire",
  "chakra": 30, "cooldown": 8.0,
  "clip": "narutominecraft.player:breath_fire",
  "effect": {"type": "projectile", "entity": "narutominecraft:fireball", "speed": 1.2, "damage": 6, "fire": 4, "breaks_blocks": false}
}
```

Effect types are a fixed set in Java (`projectile`, `dash`, `area`, `summon`, `status`, `bind`,
`wall`, `transform`, `possess`); new jutsu are data unless they need a new effect type.

### Saves

- **Player:** one Fabric attachment, copied on death and synced to its owner: rank, milestones,
  missions in hand, mastered techniques, quick slots, nature(s), clan, look, team.
- **World:** level attachments like VF's (`villagefriends:societies`, `notice_boards`): the event
  director's state, exam state and results, NPC teams, crisis arc progress, village damage to
  restore.
- **Map version:** the save stores the map version; a newer map with an older save triggers a
  migration step in the map builder (rebuild the districts that changed).

### Multiplayer

- Server-authoritative: chakra, cooldowns, hits and rewards are decided by the server; the client
  only predicts animation and movement.
- Teams: players can form a squad of up to four; NPC teammates fill empty places.
- Exams: players in the same exam meet in the finals bracket.
- Ranks are per player. **Hokage** is one per world; see open questions.
- Combat timing must survive 100 ms of latency: keep windows generous (parry 4 ticks, dodge
  invulnerability 6) and test on a dedicated server.

## 8. Phased plan

Each phase ends playable. "Done" means the listed criteria are true on a clean install of the
release jars and the map.

### Phase 0: Foundations

**Deliverables**
- Gradle Fabric project for 26.3, `narutominecraft` jar requiring VF 2.29.x; CI build.
- VF residents wear our wardrobe. Today VF reads wardrobe textures and the catalog only from the
  `villagefriends` namespace ([ResidentSkins.java](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/src/client/java/dev/villagefriends/client/ResidentSkins.java),
  [Wardrobe.java](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/src/main/java/dev/villagefriends/outfit/Wardrobe.java)); decide
  between a small VF API to register extra wardrobes (preferred) and an add-on that overrides
  VF's catalog.
- A Leaf resident spawn egg and a Village Marker based test settlement (VF `VillageMarkerBlock`)
  to try societies, routines and homes in a hand-built street.
- Player attachment skeleton; JSON loaders with validation; `tools/` `--check` scripts.
- A **spike** on the player poser: one clip playing on the player in third and first person.

**Done when**
- `gradlew build` and `python tools/wardrobe/wardrobe.py --check` pass in CI.
- In a dev client, ten Leaf residents in Naruto wardrobe live in a test street: they walk, blink,
  sleep in beds, eat and greet you.
- The player plays one test clip in both views without breaking the vanilla walk.

### Phase 1: Vertical slice — the Academy

**Deliverables**
- Konoha building kit v1 and the Academy district: the Academy (by hand), the yard, ~12 homes,
  Ichiraku, a street to the Hokage building's exterior, part of the wall with one gate.
- Academy outfits (wardrobe), Academy kids and an instructor with lesson routines.
- Chakra bar, hand-sign radial, Clone, Transformation and Substitution.
- Taijutsu v1: three-hit combo, heavy, dodge, block; practice kunai and shuriken at targets.
- Academy milestones and the graduation exam with the clone test; promotion to Genin with the
  headband and Genin wardrobe unlocked.
- Rank greeting pools for Academy and Genin.

**Done when**
- A new player goes from spawn to Genin in 30 to 45 minutes with no commands.
- Unit tests cover combo timing, sign matching and chakra; a client game test runs the graduation
  with screenshots.
- Combat holds up on a dedicated server at 100 ms ping (manual test, written up).

### Phase 2: Genin life

**Deliverables**
- Mission Desk district (Hokage building ground floor) with D-rank (5 types, VF notice board
  under the hood) and C-rank (escort, bandit clearing, delivery to another settlement).
- Team assignment and the bell test; NPC teammates as companions.
- Tree walking, wall-running, water-walking, chakra jump, ninja run.
- Elemental affinity and one jutsu per nature; kunai throwing, shuriken, paper and smoke bombs,
  the tool pouch.
- The shinobi entity and brain v1: bandits and rogue Genin.
- Training Grounds (Ground 3 by hand, two generated), the market street, the main gate.

**Done when**
- From Genin, a player can reach Chunin Exam eligibility in 2 to 3 hours.
- Every mission type completes in a client game test.
- Bandits use at least four techniques and dodge.

### Phase 3: The Chunin Exams

**Deliverables**
- Event director and the calendar events: Chunin Exams, Academy graduation, the Leaf Festival.
- The three exam stages: written test, Forest of Death (generated forest and the tower), arena
  preliminaries and finals with seated spectators.
- NPC exam teams that run every season, with results in village news.
- Chunin wardrobe, B-rank missions, judged promotion.

**Done when**
- The exams run with and without the player each season; a player can enter, finish all three
  stages and be promoted or not on judged performance.
- 150 seated residents in the arena keep 60 fps on a mid-range PC.

### Phase 4: Clans

**Deliverables**
- The eight clans merged (from `clan/*`), their compounds built, their residents populating them.
- Clan choice for the player (if confirmed) and the eight clan techniques, except Mind Transfer
  if it slips (then Phase 5).
- Clan days in the calendar; clan dialogue pools.

**Done when**
- Each compound has its residents living there with homes, and each clan technique works for the
  player and for a clan sparring partner.

### Phase 5: Jonin and ANBU

**Deliverables**
- A-rank and S-rank missions, multi-stage missions outside the walls, leading your own Genin team.
- Jonin trial and council promotion; ANBU invitation, masks and HQ, stealth missions (detection by
  sight and sound, night).
- Crisis arc 1 (the invasion during the exam finals) and arc 2.
- Mind Transfer, Lightning Blade, Shadow Clone balance.

**Done when**
- A player can reach ANBU, and both crisis arcs play start to finish with the village restored
  after.

### Phase 6: Hokage and the whole village

**Deliverables**
- Every remaining district and landmark: hospital, police HQ, the rest of the homes, the full wall
  and gates, the Hokage Rock with the empty face.
- The succession, the final crisis arc, the inauguration, your face on the rock.
- Hokage play: assigning NPC teams, setting festivals, approving promotions, opening plots.
- The map shipped as a downloadable save with the jars; multiplayer polish.

**Done when**
- The full ladder plays from Academy to Hokage on one save, in single player and on a server with
  four players.

### Risks

| Risk | Why | What we do |
|---|---|---|
| Player animation | VF poses residents only; the player model and first person are new code, and other mods touch them | Spike in Phase 0; keep clips in VF's format so the tools carry over |
| Combat feel | Minecraft combat is coarse (hurt invulnerability, 20 tick/s server, client-side movement) | Server-decided hits with generous windows; test at 100 ms early |
| Map building cost | 300+ buildings and landmarks | Generate everything repeatable; hand-build only the landmarks; one district per phase |
| VF coupling | VF changes often (2.29 now); a change can break our mixins | Prefer VF public APIs; pin a VF version per release; run VF's tests with our jar |
| Performance | 150 to 250 residents with routines and societies in one area | Measure in Phase 0 and Phase 3; split Konoha into several VF settlements (one per district) if one society is too big |
| Minecraft 26.3 | A very new version: few libraries, mod compatibility | Stay on VF's version; avoid extra library dependencies |
| Naming and IP | Naruto names, symbols and characters belong to their owners | Keep characters original (the wardrobe already uses role looks), keep it a free fan project, and see the open question on names |

### Open questions for the owner

1. **Clan choice.** Does the player pick a clan at the start (and get its technique), stay
   clanless and learn from clans by friendship, or both?
2. **Story canon.** Original characters only (as the wardrobe has now), or the show's named
   characters and plot (the bell test, the invasion) as written? This decides dialogue, quests and
   IP exposure.
3. **ANBU on the ladder.** Keep ANBU as a step between Jonin and Hokage (README), or make it an
   optional branch from Jonin, as in the show?
4. **Hokage in multiplayer.** One Hokage per world (first to qualify, or elected), or each player
   can become Hokage in their own story?
5. **The world outside the walls.** A fixed map with a border, or ordinary generated terrain
   beyond it? If generated, should VF's medieval villages stay switched off?
6. **Single player or server first?** It changes how much we invest early in squad play and the
   exam bracket.
7. **VF's RPG add-on.** Should the RPG work alongside us (it halves early player damage and has
   its own levels), or should the map ship without it?
8. **Elemental nature.** Random from the chakra paper, or chosen?
9. **Death.** In an adventure map, does dying cost anything (lost tools, a hospital trip), or only
   time?
10. **Era.** How many Hokage faces are already on the rock when you start (four, as early in the
    show, or five)?
