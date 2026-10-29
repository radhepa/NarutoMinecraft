# Missions

The Mission Desk of the Shinobi Modpack: how missions are offered, taken, travelled, fought, graded and
paid, from a Genin's first lost cat to an ANBU operation; the catalogue of board-mission templates; the
recurring clients who keep coming back; and the pure-Java generator that rolls the board from the save's
seed. Read with [ROADMAP.md](ROADMAP.md) (data formats in §5, Ryo, Levels and Your squad in §7, the beta in
§8), [BONDS.md](BONDS.md) (bond acts, standing, the squad) and [SIDE_QUESTS.md](SIDE_QUESTS.md) (which owns
side quests; missions use the same quest format but are their own loop).

**No spoilers here.** This file holds systems, formats, premises and twists as the player meets them. The
anime shows only a handful of D- and C-ranks, so the catalogue is invented. Twists are rolled per mission,
so knowing the list does not tell you which one you will get. Anything tied to the main story's secrets
lives in the developers-only [story bible](docs/story/STORY_BIBLE.md), keyed by mission id.

**Where it lives.** Templates and tables are data in the Adventure datapack
(`adventure/data/shinobi_adventure/missions/`), authored in Python under `tools/missions/` and compiled by
`missions.py`. The generator is pure Java in [`progression/missions`](progression/missions) (package
`dev.shinobi.progression.mission`), Shinobi Progression's `mission` package and its `MissionRoll`
([ROADMAP.md](ROADMAP.md#code-by-mod)): no Minecraft, deterministic and seeded, with tests and a simulation.

```
python tools/missions/missions.py --doc     # compile templates and tables, write docs/missions/CATALOGUE.md
python tools/missions/missions.py --check   # validate; fails if the compiled JSON is stale
./gradlew :progression:missions:test        # 33 tests
./gradlew :progression:missions:simulate    # the desk through Genin life and a 200-day run (-Pseed=N)
```

## Contents

| # | Section |
|---|---|
| 1 | [At a glance](#1-at-a-glance) |
| 2 | [The Mission Desk](#2-the-mission-desk) |
| 3 | [Ranks and the economy](#3-ranks-and-the-economy) |
| 4 | [Templates](#4-templates) |
| 5 | [Recurring clients, chains and rival squads](#5-recurring-clients-chains-and-rival-squads) |
| 6 | [Squad missions](#6-squad-missions) |
| 7 | [Counts, pacing and variety](#7-counts-pacing-and-variety) |
| 8 | [Authored story missions](#8-authored-story-missions) |
| 9 | [The generator](#9-the-generator) |
| 10 | [What other parts of the pack provide](#10-what-other-parts-of-the-pack-provide) |
| 11 | [What waits for Phase 0](#11-what-waits-for-phase-0) |
| 12 | [Open questions](#12-open-questions) |

## 1. At a glance

| | D | C | B | A | S | ANBU ops | All |
|---|---|---|---|---|---|---|---|
| Templates | 41 | 26 | 16 | 10 | 4 | 6 (1 B, 3 A, 2 S) | **103** |
| In the beta | 41 | 24 | — | — | — | — | 65 |
| Twists | 95 | 56 | 33 | 21 | 8 | 12 | 225 |
| Who takes them | Genin, Chunin | Genin (after Ch 11), Chunin, Jonin | Chunin and up | Jonin and up | Jonin at level 42+ | ANBU branch | |
| Pay (ryo) | 60–150 | 300–600 | 800–1,500 | 2,000–4,000 | 6,000–12,000 | by rank | |
| Length | 8–12 min | 20–35 min, often over a camp night | 35–45 min | 45–55 min | 55–70 min | | |

The full list, with every premise and twist, is generated into
**[docs/missions/CATALOGUE.md](docs/missions/CATALOGUE.md)**.

**Key rules.**

- **One quest format.** A board mission is a quest of `kind: mission` (ROADMAP §5): a step graph with
  slots filled from the save's `missions` stream. Saves store a mission by template id and rolled slots.
- **Every job has a twist.** Each template carries two or three twists; about half the offers roll one
  (45% in Classic, 60% in Varied). A twist switches the graph onto its own branch or changes the rules.
- **D-ranks are village life; C-ranks fight.** Every C-rank has a real fight and most have a real choice.
- **Grades S, A, B, C** come from bonus objectives, knockouts, the client's safety, the role call and the
  squad's cohesion, and scale pay, XP and client rapport. A failed mission has no grade.
- **The village remembers.** Clients keep a rapport with you; pleased clients come back and ask for you
  by name; two recurring clients run whole chains across ranks; the rival squad races you once a week.
- **The beta's ryo rule holds:** a day of D-ranks covers food and leaves about half to save.

## 2. The Mission Desk

*BUILD (Beta 2).* The desk is on the Hokage Residence's ground floor (`place:residence.mission_desk`),
open 08:00 to 18:00 (ROADMAP §7, "The daily cycle"). It opens with Ch 9 ("The Mission Desk"). Two Chunin clerks
staff it (`role:desk_chunin_1`, `role:desk_chunin_2`, the ranks session's roster), and gate guards
(`role:gate_guard_1`, `role:gate_guard_2`) keep the travel desk.

### 2.1 How missions are offered

The desk shows a **board**: a column per rank the player may take, each a few offer cards.

| Player rank | D | C | B | A | S |
|---|---|---|---|---|---|
| Genin | 5 | 2 (after Ch 11) | — | — | — |
| Chunin | 2 | 3 | 3 | — | — |
| Jonin | — | 1 | 2 | 3 | by summons |
| ANBU | — | — | 1 | 2 | 1 |

- **Gates.** A rank's column needs its gate (`desk.json` `rank_gates`): D from Ch 9 until Jonin, C from
  Ch 11, B from Chunin, A from Jonin, S from Jonin at level 42. Templates add their own `unlock` (the far
  region waits for Ch 13; the orchard for tree walking), seasons (snow clearing in winter) and event
  windows (festival setup in the three days before the Leaf Festival, festival guard during it).
- **Refresh.** D refreshes daily, C and B every three days, A weekly, S each season. An offer stays up
  for its lifetime (D 2 days, C and B 4, A 7, S 14).
- **Other squads.** Offers you leave are sometimes taken by one of the village's NPC Genin squads; the
  board says so ("Squad 4 took the drain job"), which keeps the board alive and the choice real.
- **A card shows** the title, the client (by name token), the place, the party (squad, solo or either),
  the pay and the time limit. The twist is not shown: it is revealed in the field. A harder twist pays
  10% more, and the clerk remarks on the generous fee, which a sharp player learns to read.
- **Seals on a card:** *Requested* (a client asked for you by name, +15% pay), a client's chain crest
  (a recurring client), and *Contested* (the rival squad has the same job).
- **Squad or solo.** Genin take most missions as a squad; templates marked `solo` or `squad_or_solo` can
  be taken alone (a sensei lets a Genin run small errands alone). From Chunin every D and C may be solo.
  Chunin lead NPC Genin on `lead` missions; ANBU operations use an ANBU cell.

### 2.2 Accepting and the briefing

- **One mission in hand.** Two D-ranks a day, or one mission of C rank or above, which takes the day.
  Weekly caps by rank: a Genin takes one board C-rank a week (the story's C-ranks come on top); a Chunin
  three C and two B; a Jonin two B and one A (`desk.json` `caps`).
- **Declining** costs nothing. **Handing a mission back** before its first step costs a little rapport
  with the client (−0.5) and nothing else.
- **The briefing** is the template's `brief` dialogue: the clerk or the client explains the job, and on
  a squad mission the player gives each teammate a role (§6). The journal tracks the step graph.

### 2.3 Travel

| Where | How | Time |
|---|---|---|
| In the village | Walk, run, roof-hop to the anchors | Minutes |
| Outside the wall, inside the map | Out through a gate (main, east, the farm gate); bandit camps, farms, the outer training grounds, the east road and its waystation are open terrain | An hour or two of game time |
| Far regions | The **travel desk** at the main gate (`place:gate.travel_desk`): a short travel scene of the road (ROADMAP §6), then the region's entry point. The scene can roll a road event (35%, `desk.json` `road_events`): a traveller, an ambush, a night at camp, or on the east road an elite squad passing by (`role:elite_scout`) | Half a day to a day each way |

- A C-rank of two days spends a **night at camp**: a bedroll at an anchor, a `camp_night` bond act with
  the squad, a campfire banter scene, and On Duty fatigue rules when the night is a watch.
- In the beta the far region is the border village (Beta 2); later arcs add more regions (§10). Regions
  are datapack dimensions with no mod changes ([ROADMAP.md](ROADMAP.md#regions)).

### 2.4 Reporting back

The last step of every template is the report: the client signs off (a `talk` with them), and the player
turns the mission in at the desk for the **grade screen**: grade, pay, XP, the client's rapport, gifts.
After 18:00 the turn-in waits for the morning without penalty, unless the time limit runs out.

### 2.5 Failure, partial success and abandonment

| How it ends | When | Pay | XP | Rapport | Bonds and standing |
|---|---|---|---|---|---|
| **Done** | Every required step | By grade (§3) | By grade | +0.5 to +2 by grade | `mission_together`, `mission_success`; a `helped_resident` deed about the client; the grade's standing with the client's district and clan |
| **Partial** | The job is done but something required was lost: a crate broken, one of three parcels missing, a hostage hurt | 50% | 60% | 0 | As done; the grade is capped at C |
| **Failed** | Death on the mission (ROADMAP §7, "Death"), the time limit, the client or cargo lost, an escort's client knocked out | None | 10% | −2 | `mission_failed`; `failed_client` with the client (BONDS.md §4); −2 standing |
| **Given up** | Turning back mid-mission at the desk | None | None | −2 | As failed |
| **Abandoned** | Leaving the client or the squad in danger: leaving the mission region while teammates fight, running from an escort | None | None | −4 | `abandoned_mission` witnessed by the squad (BONDS.md: a big, kept memory); −4 standing |

- **Time limits** are in the template (`fail.timeout_days`): a D-rank by the next day's desk close, a
  C-rank in three days, couriers in one. A collapse from fatigue loses the morning (ROADMAP §7).
- **Squadmates are knocked out, never killed** (BONDS.md §7); a knockout costs grade, not the mission.

### 2.6 Grades

```
score = 60                                   (the job is done)
      + 40 × bonuses met / bonuses offered    (each template offers two to four, below)
      − 8 per knockout in the party, − 15 if the client or cargo was hurt
      − 10 if an alarm was raised, − 10 if late
      + 4 for a good role call (§6)
      + the cohesion band: +5 in step, 0 steady, −5 ragged, −10 split (squad missions only)
```

| Grade | Score | Pay | XP | Rapport | Standing |
|---|---|---|---|---|---|
| **S** | 100+ | ×1.25 | ×1.25 | +2 | +2 |
| **A** | 85+ | ×1.1 | ×1.1 | +1.5 | +1 |
| **B** | 65+ | ×1.0 | ×1.0 | +1 | 0 |
| **C** | below 65 | ×0.85 | ×0.85 | +0.5 | 0 |

An S needs every bonus objective. The bonuses (`mkit.BONUSES`): `fast` (within the template's fast
time), `unseen`, `no_knockouts`, `client_unharmed`, `all_found`, `gentle` (the animal or person unhurt),
`kind_choice` (the choice the client hoped for), `no_alarm`, `spared` (enemies captured or routed),
`teamwork` (every teammate's role used), `careful` (nothing fragile broken), `extra_mile` (an optional
step for the client) and `clean_record` (nothing kept that was not yours).

## 3. Ranks and the economy

*BUILD (beta) for D and C; FOUNDATION (later) for B, A and S.* All numbers are in `economy.json` and
`desk.json`, so a balance pass is a datapack update.

### 3.1 Pay and XP bands

| Rank | Ryo (the player's share) | XP, as a share of a level at the reference level | Reference level |
|---|---|---|---|
| D | 60–150 (ROADMAP §7) | 15–25% | 7 |
| C | 300–600 (ROADMAP §7) | 50–70% | 12 |
| B | 800–1,500 | 60–90% | 22 |
| A | 2,000–4,000 | 90–130% | 36 |
| S | 6,000–12,000 | 180–260% | 46 |

- **Where in the band:** each template has a pay weight (a lost cat is near the bottom, a night at the
  hospital near the top), jittered ±12% per offer and rounded to 5 ryo. A harder twist adds 10%, a
  request by name 15%, and the grade scales it on turn-in.
- **XP** is fixed per rank, so a D-rank is a fifth of a level at level 7 and a seventh at level 14:
  missions stay worth doing, and grinding D-ranks fades. The XP curve here (`200 + 40 × level` to the next
  level) is provisional; Progression's `ranks.json` owns the real one.
- **The ryo rule of thumb** (ROADMAP §7): a day of D-ranks covers food and leaves about half to save. A
  D-rank pays about 105 ryo on average; food and tools cost about 47 a day.
- **Gifts:** on a B grade or better, a client may add a thank-you from their trade (a farmer's
  vegetables, a medic's bandages, a priest's charm), as VF's notice boards do (`economy.json` `gifts`).
- **Techniques from missions** (ROADMAP §7, "Learning jutsu"): the first S grade on a C-rank or above can
  carry a technique scroll from the rank's pool (`technique_scrolls`; the pools are the combat
  session's).
- **Collectibles** (`economy.json` `collectibles`; the items session registers the ids and loot tables).
  They are ordinary items for a collector's chests and shelves; there is no separate collection book:
  - **Curios**, charming and useless things with flavor text (a cracked mask, a foreign headband, an old
    coin): on a B grade or better, 12% of D-ranks, 35% of C, 45% of B, 50% of A, 60% of S, from a table
    by the template's setting (`loot:curio.road`, `.river`, `.shrine`, `.wilds`, `.far_lands`, `.covert`
    and more); and 15% of defeated enemies drop one by their kind (`loot:curio.bandit`, `.smuggler`,
    `.ronin`, `.foreign`, `.beast`).
  - **Ninja info cards**: the item `item:info_card` with a variant, one per enemy kind on its first defeat
    (`enemy.<combat enemy id>`) and one per person met on a mission (`person.<role>`), with a card back by
    rank.
  - **Keepsakes**: 20 memorable missions give a unique display piece on their first A grade or better (the
    festival lantern, the haunted inn's lantern, a dojo signboard, the kiln family's pieces at every rank).

### 3.2 Client standing and village reputation

- **Rapport** is the desk's own tally per client: points by grade (S +2, A +1.5, B +1, C +0.5), −2 for
  a failure, −4 for abandonment, −0.5 for handing a job back. Tiers: **stranger, known (1), regular (3),
  trusted (6), patron (10)**. A client below −2 is **soured** and stops posting to you for two weeks.
- **Feelings** are the bond engine's: turn-in applies `mission_success` or `mission_failed` with the
  squad and `failed_client` with a client you failed (BONDS.md §4), and a finished job is a
  `helped_resident` deed about the client that gossip carries (BONDS.md §8). So the village's standing
  titles (Helping Hand to Hero) rise with good missions in a district.
- **How many:** two D-ranks a day at most, one board C-rank a week as a Genin (three for a Chunin), two
  B a week as a Chunin or Jonin, one A a week as a Jonin, one S a season.

## 4. Templates

*BUILD (beta) for D and C; FOUNDATION (later) for the rest.* Templates are authored in
`tools/missions/catalogue/` (`d_rank.py`, `c_rank.py`, `later_ranks.py`) with the helpers in
`tools/missions/mkit.py`, and compiled to `missions/templates/<rank>/<name>.json`.

### 4.1 The format

ROADMAP §5's board-mission example, grown into the full shape:

```json
{"format": 1, "id": "mission.d.lost_pet", "kind": "mission", "rank": "d", "category": "pets", "status": "beta",
 "title": "dlg:mission.d.lost_pet.title", "brief": "dlg:mission.d.lost_pet.brief", "minutes": 10, "party": "squad_or_solo",
 "slots": {"client":      {"pick": "resident", "where": {"has_pet": true}},
           "pet_spot":    {"pick": "anchor", "tag": "pet_hideout"},
           "second_spot": {"pick": "anchor", "tag": "pet_hideout"},
           "claimant":    {"pick": "resident"}},
 "start": "ask",
 "steps": {"ask":  {"objective": {"type": "talk", "who": "slot:client"}, "next": "find"},
           "find": {"objective": {"type": "collect", "target": "slot:client.pet", "at": "slot:pet_spot"},
                    "branch": [{"if": {"twist": "two_pets"}, "next": "second"},
                               {"if": {"twist": "rival_claims"}, "next": "claim"}],
                    "next": "return"},
           "claim": {"objective": {"type": "talk", "who": "slot:claimant"}, "next": "decide"},
           "decide": {"objective": {"type": "choose", "options": {"client": null, "claimant": "given_to_claimant"}},
                      "branch": [{"if": {"chose": ["decide", "claimant"]}, "next": "hand_over"}], "next": "return"},
           "...": "..."},
 "twists": [{"id": "two_pets", "weight": 2, "harder": false, "premise": "dlg:mission.d.lost_pet.twist.two_pets"}],
 "outcomes": {"done": {"pay": 1.0, "standing": 0},
              "given_to_claimant": {"pay": 0.6, "standing": -1, "other_standing": 2}},
 "bonus": ["gentle", "fast", "kind_choice"], "fast_hours": 3,
 "fail": {"on_death": true, "timeout_days": 1},
 "enemies": [], "places": {"anchors": ["pet_hideout"], "regions": []},
 "pay": {"band": "d", "xp_band": "d", "weight": 0.2},
 "tags": ["village", "animal", "search"], "contested": false, "classic": true,
 "banter": "dlg:mission.banter.pets"}
```

| Field | Meaning |
|---|---|
| `slots` | Filled when the offer is rolled. `resident` (a query: `job`, `age`, `group`, `clan`, `rank`, `has_pet`, `household`, `household_children`, `district` (`same:client`), `parent_of`, and `resident_of: any` to allow travellers), `anchor` (a tag in `districts.json`), `region`, `one_of`, `count`, `role` (a bound role: a recurring client, a target), `enemy_group` (the combat session's groups) and `suspect` (one of the other resident slots: the rolled culprit) |
| `steps` | The quest graph (ROADMAP §5): objectives `go`, `talk`, `inspect`, `collect`, `deliver`, `craft`, `buy`, `defeat`, `escort`, `protect`, `survive`, `sneak`, `perform`, `wait_until`, `sleep`, `choose`; `on_enter` and `on_done` actions (`spawn_group`, `bond_event`, `mission_outcome`, `lead`); a step's own `bonus` |
| `twists` | Rolled per offer. Most switch the graph through a branch on `{"twist": id}`; a `modifier` twist changes the rules instead (a fragile parcel: no running) or picks the rolled culprit. `harder` twists pay 10% more |
| `outcomes` | How the mission can end: `done` and the endings a choice leads to, each with a pay multiplier, a standing change and extra effects (a clan deed, a hook for SIDE_QUESTS's generated quests, a lead) |
| `bonus`, `fast_hours` | The bonus objectives the grade counts (§2.6) |
| `places` | Derived by the compiler: every anchor tag and region the template touches |
| `unlock`, `season`, `event` | Extra gates, in Core's condition language |
| `contested`, `chain`, `classic` | A job the rival squad can race for; a recurring client's chain; in the Classic pool |
| `trail_drop` | Later ranks: a chance and a pool of journal lines (the story session's) the mission can add to the journal on turn-in |

**The checker** (`missions.py --check`) refuses: unknown objectives, conditions or actions; steps that
are unreachable or never end; a branch on an undeclared twist, or a twist with no branch that is not a
modifier; a choice that leads to an unknown outcome; unknown slots; enemy groups spawned but not listed;
`fast` without a fast time; fewer than two twists; a C-rank or above with no fight (except mediation,
medical, investigation and ANBU work); and stale compiled files. The Java `Catalogue` re-checks the graph
and that every twist changes the path.

**Text.** Titles, twist premises, choices and banter are dialogue keys in the dialogue session's scheme,
derived from the id: `dlg:<template id>.<part>` for the parts `brief`, `accept`, `decline`, `progress`,
`success`, `fail` and `report` (every template lists them under `dialogue`), plus `.title`,
`.twist.<id>` and `.choice.<step>`. Slot tokens are the slot names (`{client}`, `{pet_spot}`,
`{bandits}`); the English premises in the authoring files (`_premise`, `_twists`)
feed the catalogue doc only. Names are always tokens.

**Perform objectives** are of two kinds: combat actions (`technique:clone`, `combo:three_hit`, `dodge`,
`spar`, `smoke_bomb`, `paper_bomb_set`, the chakra-movement ones like `wall_run_string`) and **chores**:
work points at an anchor (hold use for two to four seconds with a work clip and a progress ring, or a
short sequence). A few chores are small games: serving customers, the quiz, hauling a net, a snowball
fight. `needs.json` lists every perform id.

### 4.2 D rank: village life with a twist (41)

Civilians run the village's daily life (ROADMAP §6), and their streets are where D-ranks happen.

| Category | Templates |
|---|---|
| Pets | Lost pet (two pets, a new litter, a rival claim), dog walking for the Inuzuka clinic (the pack bolts after a scent), pet sitting (an escape artist, a neighbour's feud) |
| Children and the Academy | Babysitting (hide and seek gone too well, a demand for a real jutsu, a sick child), assisting a target-practice class (a prankster, a demonstration), tutoring (the pupil is being bullied; a cheat sheet) |
| Farms and harvests | Weeding (crows, boar tracks that lead to a C-rank, a buried kunai cache to turn in or keep), the harvest before the rain (clan deer, the storm, a broken axle), the orchard (wasps, a child stuck in a tree; tree walking), the Nara deer count, the Aburame insect gardens |
| Market and shops | Minding a Market Day stall (a haggler, a shoplifter, a rush), a shop's inventory (a slow thief to find among the staff), a wedding order at the flower shop (the language of flowers) |
| Deliveries and messages | A parcel round (swapped labels, a recipient who moved, a fragile parcel), catering to a training ground (a hungry squad), a timed messenger run (wait for a reply; a rival courier), posters in every district (someone tearing them down) |
| Festivals and nights | Festival setup (lanterns between rooftops, a missing crate, the fireworks), lighting the street lamps at dusk (no oil; a prowler) |
| Repairs and building | A leaking roof (a swallow's nest, the neighbour's cat), a fence (a boundary quarrel to settle fairly or take a side, which can raise a society hook), timber for the Kinoshita yard, moving day (an heirloom tea set, a hiding cat, a chest only chakra can lift) |
| Clearing, rivers and outdoors | A blocked drain (a lost ring to return or keep; frogs), an overgrown lot (an armed old trap, hornets), the river below the market bridge (a letter in a bottle, a snagged net, rubbish only water-walking reaches), the morning catch, the riverside laundry (a sheet flying across the rooftops) |
| Hospital, elders, shrine | Herbs on the slopes (a poisonous lookalike), a day on the wards (a wandering patient), an elder's errands (they want you to stay for a story: a heart-to-heart), the shrine steps (crows hoarding offerings; who feeds the fox statue?), the bath house (the boiler wants a fire or wind technique), the barbecue house kitchen (an honest opinion of a bad sauce) |
| Training, gate and seasons | Training-ground upkeep (a spar challenge), the gate logbook (a cart that sits too low: let it through or hold it, which leads to a district quest), snow clearing (a snowball ambush), leaf raking (a lost purse; roasting sweet potatoes with the squad) |
| A recurring client | The kiln family's night firing (§5) |

### 4.3 C rank: the roads, the border and real fights (26)

| Category | Templates (twists; choices) |
|---|---|
| Escort | A trader to the east road's waystation over two days (the bridge is down, a night raid, an extra passenger; hand captured bandits over or let them go), a scholar to the border village (falls ill at the pass; a harmless secret to keep or report), pilgrims through a mountain pass (later) |
| Bandits | Clearing a bandit camp (hostages, the leader flees; the "bandits" are starving farmers: mercy or arrest) |
| Delivery | Medicine to the border village's healer (stolen crates to track, a toll bridge to pay or fight, a storm), supplies to a hill outpost (a fever there, a landslide), the kiln family's pottery to market (§5) |
| Guard and protection | A two-day caravan (an insider signalling the raiders; a sabotaged wheel), the festival against a pickpocket gang (the fireworks, a lost noble child), a shopkeeper threatened by a rival's thugs (a bribe; the client started it: mediate), a lord's child for a day (runs away; a kidnap attempt) |
| Beasts | A giant boar (a sow with young: drive her off or fight; two boars), wolves on the farms by night (driven down by bandits' fires), a bear in the outer training grounds (lure it with honey) |
| Tracking and rescue | A thief into the forest (a false trail; the thief is a child stealing for a sick parent), a missing woodcutter (a ravine, wolves closing in) |
| Investigation | Warehouse thefts (interview three suspects, stake out, and name the rolled culprit), a haunted inn on the east road (a gang in the cellar, or a grandfather's tall tale) |
| The border | Patrol with a Chunin (foreign scouts; a lost Genin of another village), a rushed message to the border post (interceptors), a water dispute between two hamlets (hired muscle; share it fairly), a heirloom from a pawn ring (a copy in the back room) |
| Interdiction, contests, duels | Smugglers at a ford by night (caged animals; a decoy boat), the rival squad's race for a cat burglar (or a partnership), a wandering swordsman beating every dojo (honourable, or a cheat) |
| Leadership (later) | Leading fresh Genin on their first C-rank (one freezes, one charges) |

### 4.4 B, A and S rank and ANBU operations (FOUNDATION)

Templates now, authored with the later arcs; every graph is valid and the generator holds them.
Targets are roles (`role:target.warlord`, `role:target.minister`), bound when the mission is rolled.

| Rank | Templates |
|---|---|
| **B** (16) | Walking the east road to the border to report anything unusual; searching an abandoned carpenter's shop in a far region; infiltrating a warlord's hill fort for a ledger; recovering a sealed scroll from two missing-nin; defending a border village against a mercenary band; ending a bandit warlord's hold on a valley (capture or eliminate); escorting a daimyo's envoy to court; a hostage rescue at a river mill; hunting a missing-nin pair; spoiling a foreign weapons depot; finding the spy in a post town; guarding a bridge-builder; a fever quarantine in a hill village; carrying a treaty draft to an allied village; bringing a deserter home alive; the kiln family's stolen glaze |
| **A** (10) | Holding a river crossing against an enemy platoon; removing a war minister before an invasion; extracting a Leaf agent whose cover is blown; holding an outpost through the night; a forbidden scroll in a ruined fortress; the daimyo's pilgrimage; hunting an enemy cell through a far region; breaking a siege; a foreign spy ring's listening post in the market; the kiln family's eldest at court; tracking a band of rogue ninja in a far region (the region is a slot) |
| **S** (4) | A legendary missing-nin; a coup against the daimyo; a stolen forbidden technique in a foreign stronghold; guarding the five lands' peace summit |
| **ANBU** (6) | Three nights watching a house from the rooftops (B); a silent extraction from an enemy camp, proof against a court official who sells border passes (keep it as leverage or expose it), hunting a missing-nin who carries the Leaf's secrets (A); five days under a false name in a foreign town, guarding the Leaf from the rooftops on festival night (S) |

## 5. Recurring clients, chains and rival squads

*BUILD (Beta 2), growing with the later arcs.* `clients.json`.

- **Returning clients.** When the desk casts a client, it first tries (30% of the time) someone you
  have worked for before and pleased (known or better), so the market's stallholders, the vet, the
  farmers and the porters become regulars with faces.
- **Requests by name.** A client at *known* or better whose missions averaged an A posts a request for
  you: a card with the *Requested* seal, only for you, paying 15% more, up for four days, free to
  decline. At most one at a time; about a quarter of days when someone qualifies.
- **The merchant** (`role:merchant`, ROADMAP §8's Classic cast: a travelling merchant who keeps hiring the
  squad). After the second story escort, once a week the desk may post an escort or caravan job for him
  by name (`chain.merchant`). On those runs, after Ch 14, one neutral step at camp lets the merchant talk
  about the roads; it plays the same in every save and only counts the talks
  (`story.merchant.camp_talks`). Anything this chain means for the story is in the story bible.
- **The kiln family** (`chain.kiln`), a family of potters you work for from Genin to Jonin: the
  grandmother's night firing (D), the parent's pottery to the border market (C), the family's stolen glaze
  (B), and the eldest named court potter, guarded through a hostile court (A). Each stage needs the last
  done and a deeper rapport with the family (known, regular, trusted). Three roles, cast per save.
- **The rival squad** (`role:rival_squad`: the rival with two classmates, ROADMAP §7). From Ch 9, once a
  week one `contested` job carries the *Contested* seal: both squads race for it (the messenger run, the
  cat burglar, more later). Win and the rival's respect and rivalry grow (`spar_won`); lose and you get a
  consolation fee (30%) and a rivalry with an edge. A twist can turn a race into a partnership.
- **NPC squads.** Four of the village's Genin squads take what you leave on the board (about one stale
  offer in five a day), named on the board.

## 6. Squad missions

*BUILD (Beta 2).* `squad.json`, `SquadPlan`.

**Roles.** At the briefing the player gives each teammate a role:

| Role | Does | Good for |
|---|---|---|
| **Point** | Leads, scouts ahead, first into a fight | Bandits, duels, couriers, contests |
| **Guard** | Stays with the client or the cargo | Escorts, caravans, bodyguards, children |
| **Tracker** | Scent and signs: a ninken, a sensor, the Byakugan | Beasts, tracking, rescue, patrol, pets |
| **Support** | Traps, illusions, first aid, tools | Investigation, mediation, repairs, festivals |

- Each category wants two roles (`wanted`). A teammate's **aptitude** comes from their profile: a ninken
  makes a tracker (ROADMAP §7: ninken track on missions); Hyuga, Aburame, Inuzuka and Hatake track;
  Kurama, Yuhi, Yamanaka and Suzuran support; Akimichi, Gekko, Uchiha and Senju take point; discipline
  guards, boldness leads, warmth guards and supports. In the Classic cast the painter is a natural support
  and the loud one with the pup a tracker.
- **A good call** (a suited teammate in a wanted role, nobody misplaced) adds 4 to the score. Every
  assignment is attention for the bond engine's favoritism and jealousy rules (BONDS.md §7): always
  sending the same teammate ahead is noticed.
- **Cohesion** (BONDS.md §7) sets a band: **in step** (75+: +5 score, teammates assist your combos),
  **steady** (50+), **ragged** (30+: −5, no assists, the odd ignored order), **split** (below 30: −10,
  teammates ignore an order 15% of the time). Missions build cohesion back: `mission_together` on every
  squad turn-in.
- **Bond acts** the desk applies on turn-in: `mission_together` and `mission_success` (or
  `mission_failed`), `camp_night` for a night at camp; templates add their own (an elder's
  `heart_to_heart`, a spar's `spar_won`, a meal by the bonfire).
- **Banter keys** (the dialogue session writes the lines), most specific first:
  `dlg:mission.banter.<category>.<moment>.<speaker_kind>.<band>`, then without the band, then without the
  category (`dlg:mission.banter.<moment>.<speaker_kind>`). Moments `brief`, `depart`, `travel`, `arrive`,
  `ambush`, `twist`, `fight`, `low_health`, `choice`, `camp`, `victory`, `grade_s`, `partial`, `fail`,
  `report`; speaker kinds `sensei`, `teammate`, `client`; the band (`in_step`, `steady`, `ragged`,
  `split`) lets a squad that is not getting along sound like it.

## 7. Counts, pacing and variety

### 7.1 Pacing in the beta

ROADMAP §8 budgets about 12 board D-ranks (~2 h) and 3 board C-ranks (~1.5 h) in Genin life's 24
in-game days. The simulation (`./gradlew :progression:missions:simulate`, 24 seeds per row, Beta 2's
chapters on their days) gives:

| Player | Visits the desk | D | C | Distinct templates | Twists | Grades S/A/B/C | Requests | Ryo a day vs living | Saved | Board XP of Genin's 5→15 |
|---|---|---|---|---|---|---|---|---|---|---|
| Casual | 45% of days | 8 | 0.4 | 8 | 46–61% | 9/12/41/30% | 1 | 38 vs 47 | −200 (jobs and side quests cover it) | 14% |
| **Steady** | 75% of days | **10** | **3.3** | **12 of 13** | 47–63% | 23/23/37/12% | 3.5 | 102 vs 47 | ~1,300 | **38%** |
| Keen | 95%, as many as allowed | 27 | 3.5 | 25 of 31 | 45–59% | 55/18/20/3% | 4.7 | 197 vs 47 | ~3,600 | 74% |

- **Missions per hour** of systemic play: a D-rank takes 10 to 12 minutes, a C-rank 25 to 35, so about
  four D-equivalents an hour, two to three D-ranks or one C-rank per sitting.
- A steady player's board XP is about two fifths of Genin's ten levels, the rest coming from chapters,
  training and side quests, as ROADMAP §7 intends ("missions give most of it"). A keen player who grinds
  out-levels the path by the board alone, which the fading D-rank XP slows.
- Over 200 days (Chunin from day 60, Jonin from day 140) the board keeps its variety: a template never
  returns within its gap (8 days for D), and clients number in the dozens. B-to-S pay is provisional
  until the later arcs bring their costs (a house, a clan estate, furniture); the stipend runs all game and there is no rent.

### 7.2 The variety guard

| Rule | Value | Hard or soft |
|---|---|---|
| A template the player took is not offered again within | D 8 days, C 12, B 14, A 21, S 56 | Hard |
| At most one offer of a category per column | 1 | Soft: relaxed only if the column cannot fill |
| A client is not cast again within | 4 days | Soft |
| An anchor is not reused within | 2 days | Soft |
| A repeated template does not repeat its last twist within | 10 days | Hard while another twist exists |
| An offer seen in the last three days and not taken | weight ×0.35 | Soft |

### 7.3 Classic and Varied

| | Classic | Varied |
|---|---|---|
| Pool | The curated pool (`classic: true`: every template today) | Every template |
| Opening | The first boards teach in a fixed order: lost pet, deliveries, weeding, an Academy class, an elder's errands, a roof, a stall, the river | Rolled from the start |
| Twists | 45% of offers | 60% of offers |
| Weights | Even | Each template gets a per-save weight from 0.5 to 1.5, so each save has its own favourite jobs |
| Clients, places, pay | Rolled from the seed | Rolled from the seed |

Both are reproducible: the same seed and pack version give the same board every time (`DeskTest`).

## 8. Authored story missions

The main path's missions are authored quests (`kind: main`) that use the desk, not board templates.
Their premises here are ROADMAP §8's; what happens on them is in the story bible under each chapter.

| Id | Chapter | Rank | Premise | Teaches |
|---|---|---|---|---|
| `main.ch9.small_jobs` | 9 | D | The squad's first D-rank; the board opens | Board missions, pay, failure on death |
| `main.ch11.paper_trail` | 11 | C | Escorting a merchant east; bandits on the road; a night at camp | Escort, defeat, inspect, camping |
| `main.ch13.far_village` | 13 | C | The first far region and an investigation there | Travel, investigation, ninken tracking |
| `main.ch14.second_escort` | 14 | C | Another escort east, and a recommendation for the Chunin Exams | Enemy cells, smoke and paper bombs |

The desk's unlocks read these ids: the board opens with `main.ch9.small_jobs`, board C-ranks with
`main.ch11.paper_trail`, far-region C-ranks with `main.ch13.far_village`, and the merchant's chain with
`main.ch14.second_escort`. Story missions of the later arcs (Chunin, Jonin, ANBU, the road to Hokage) are
authored with those arcs and take ids `main.<arc>.<name>`; they are not part of this catalogue.

## 9. The generator

`progression/missions` (`dev.shinobi.progression.mission`), a java-library like `life:bonds`: JUnit 5,
release 25, no dependencies (the tests use `life:bonds` only to prove the seed streams match).

| Piece | Code |
|---|---|
| The catalogue and tables, read from the datapack | `Catalogue`, `Template`, `Json` |
| Pay, XP, grades and endings | `Economy`, `Grade`, `Rank` |
| The board: columns, refresh, gates, twists, requests, chains, contests, caps | `Desk`, `Offer`, `Unlocks`, `Player` |
| Casting slots | `SlotFiller`, `Resident`, `World` |
| Variety | `VarietyGuard` |
| Rapport and requests | `Clients` |
| Roles and cohesion | `SquadPlan` |
| Seed streams (Core's formula) | `Seeds` |
| A sample Leaf of ~300 residents and the simulation | `SampleVillage`, `sim.DeskDays` (tests) |

**How a board is rolled.** Each column draws from `stream(save, "missions", "desk|<day>|<rank>")`:
eligible templates (gates, unlocks, windows, the guard, not already up) are picked by weight; the slot
filler casts the client (a returning one first, sometimes), then the other slots, retrying a cast whose
later slot depends on an earlier one; a twist is rolled; pay and XP come from the band. Requests, chains
and contests have their own keyed streams, so they never disturb the columns.

**Tests** (33): the catalogue loads with no problems, has its counts and categories, every twist changes
the path, C-ranks fight and choose; pay stays in its band, the ryo rule holds, grades need every bonus
for an S, endings pay and cost as above; the seed streams equal the bond engine's; the board is the same
for the same seed and differs by mode and seed; ranks and chapters gate it; columns mix categories; a
taken template stays away for its gap; caps per day and week; seasons and events; Classic's opening;
twist rates and the twist guard; every template casts in the sample village with queries that match;
rapport, souring, requests by name reaching the board; the kiln family's four stages in order; roles and
cohesion; and Beta 2's mission counts, savings and variety for a steady player.

## 10. What other parts of the pack provide

`missions/needs.json` (generated) lists everything the templates ask for, with a `beta` section.

| From | What | Beta |
|---|---|---|
| **Konoha build** (anchors in `districts.json`) | 88 anchor tags in the beta: in-village spots (`academy.yard`, `market.stall`, `riverbank`, `street_drain`, `client_home`, `pet_hideout`, `poster_board`, `residence.mission_desk`, `residence.records`, `gate.travel_desk`, `kiln_yard` and more), outside the wall (`farm_field`, `orchard`, `woodlot`, `herb_slope`, `outside.bandit_camp`, `outside.wolf_den`, `outside.ravine`), the east road (`road.east_bend`, `road.campsite`, `road.east_waystation`, `road.ford`, `road.inn_cellar`) and the border village (`border.square`, `border.healer`, `border.post`, `border.market`, `border.pawnshop`). Generic tags (`client_home`, `pet_hideout`, `farm_field`) want several instances each; named places one | 88 of 133 |
| **Map** | Regions `region:east_road` and `region:border_village` (Beta 2); 21 later regions (hill fort, post town, capital, coast town, mountain pass, far lands and more) | 2 of 23 |
| **Combat** (enemy groups and loadouts) | 14 in the beta, from the combat session's registry: `combat:group.bandits_small`, `.road_ambush`, `.bandits_camp`, `.smugglers`, `.scout_pair`, `.wolves_pack`, `combat:enemy.bandit_chief`, `.bandit_archer`, `.bandit_ronin`, `.boar`, `.bear`; requested and not yet registered: `combat:group.hired_thugs`, `combat:group.pickpockets` (village street fights, non-lethal) and `combat:enemy.cat_burglar`. 17 later (`combat:group.rogue_pair`, `.cell_pair`, `combat:enemy.rogue_chunin`, `.foreign_jonin`, `.giant_snake` and others; requested: `fort_guards`, `mercenary_band`, `foreign_squad`, `hunter_squad`, `foreign_platoon`, `assassins`, `kidnappers`, `ronin_band`, `combat:enemy.warlord`, `.legend_rogue`). Plus the technique scroll pools and the combat performs. Combat emits the hooks the objectives listen to (`combat:defeated`, `combat:surrendered`, `combat:captured`) | 14 of 31 |
| **Items** | Registered by the items session: mission items as `item:mission_<name>` (nine reuse existing items, such as `item:quest_parcel`; the cat, the ninken, the frog and a stray pet are followers, not items), the gifts' items, the 17 curio loot tables, `item:info_card`, `item:technique_scroll` and 20 `item:keepsake_<name>` (`economy.json` `gifts` and `collectibles`; the compiler maps the authoring names) | 51 of 58 |
| **Dialogue** | Every template's `title`, `brief`, twist premises and choices; the banter keys (§6); the desk clerk's lines; NPC squads' and the rival squad's board lines | all |
| **Life** | Ryo through the wallet; bedroll camping and On Duty; chores' work clips | all |
| **Bonds** | The acts and deeds of §3.2 and §6 (`mission_success`, `failed_client`, `abandoned_mission`, `camp_night`, `helped_resident`); cohesion | all |

The Konoha build has placed all 88 beta anchor tags under these names ([KONOHA_BUILD.md](KONOHA_BUILD.md)
§3, "Mission anchors"; generic tags get 4 to 8 instances); later regions' anchors wait for those regions.
The other ids are requests until the owning sessions confirm them in their registries.

## 11. What waits for Phase 0

- **Built now:** the templates and tables as data, the authoring tool and checker, and the pure generator
  (rolling boards, casting, twists, pay, grades, rapport, requests, chains, contests, caps, variety) with
  tests and the simulation.
- **Waits for Phase 0 and Beta 2:** the quest engine that runs the steps (Progression); the desk block and
  its board screen, the grade screen and the journal's mission page; `World` over the real village
  (markers, VF's census and households) and Core's player record and flags in place of `Player`; the
  travel desk and travel scenes (Core's regions); `perform` chores as work points with clips; spawning
  enemy groups (Combat); the wallet, bedroll and On Duty (Life); bond acts and deeds on turn-in (Life's
  bond glue); saving offers and missions in hand by template id and slots; a `MissionEnded` event on Core's bus
  (template, rank, end, grade, client, `with_squad`, `slept_away`, days away) that the home's visit
  scheduler reads ([HOME.md](HOME.md) §9); and client game tests that
  complete and fail every template (ROADMAP §9, Beta 2's exit criteria).

## 12. Open questions

For the owner:

1. **Twists on the card.** Hidden until the field (current design, with the clerk hinting at a harder
   job through the fee), or shown as a one-line rumour on the card?
2. **Solo missions for a Genin.** Allowed for templates marked `solo` or `squad_or_solo` (current), or
   squad only until Chunin, as in the anime?
3. **Board C-ranks for a Genin:** one a week (current, matching ROADMAP §8's three in Genin life), or two
   for players who want more fights?
4. **Later-rank pay.** With the stipend running all game and no rent, B to S pay (800 to 12,000) piles up
   fast in the 200-day simulation (about 100,000 ryo saved by Jonin). Lower the later bands, or keep them
   and let houses, clan estates and furniture be the sinks?
