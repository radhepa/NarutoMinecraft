# Ranks

The ninja hierarchy of the Leaf: who holds which rank, how strong they really are, how many of
each live in the village and how many you meet, which of them matter most, and how your classmates
and squad grow up beside you.

**No spoilers here.** Every rank in this file is a character's *public* rank, the one the player
sees on first meeting them. Story roles belong to the [story bible](story/STORY_BIBLE.md); this
file only names their role and their rank.

**Names are rolled per save** ([ROADMAP.md](../ROADMAP.md#names-rolled-per-save)). Below, people
are roles (`role:sensei`) with developer placeholders ("The Taijutsu Master"). Anything that ships
uses tokens like `{name:role:sensei_senior}`, and the placeholders never appear in the game.

| File | What it holds |
|---|---|
| [`tools/roster/roster.json`](../tools/roster/roster.json) | Every named shinobi of the beta (70) and the story's civilians: role, rank, tier, importance, clan, specialty, first appearance, levels |
| [`tools/roster/rank_distribution.json`](../tools/roster/rank_distribution.json) | How every other resident gets a rank: weights per group, fixed posts, job ranks, the share away on missions, the lore numbers |
| [`tools/roster/roster.py`](../tools/roster/roster.py) | `--check` validates both files against each other, the level curve, the wardrobe's clans and looks, and `population.json`; `--table` and `--counts` print the tables below |
| [`life/roster`](../life/roster) | The growth engine: pure Java, no Minecraft, seeded (`./gradlew :life:roster:test`, `./gradlew :life:roster:simulate`) |

## Contents

1. [The hierarchy](#1-the-hierarchy)
2. [Rank and power](#2-rank-and-power)
3. [Feeling the strong](#3-feeling-the-strong)
4. [Head counts](#4-head-counts)
5. [Who matters most](#5-who-matters-most)
6. [The roster](#6-the-roster)
7. [Growing up together](#7-growing-up-together)
8. [Data, code and Phase 0](#8-data-code-and-phase-0)
9. [Open questions](#9-open-questions)

## 1. The hierarchy

```
                                  Hokage
                                    │
              ┌────────────── the council ──────────────┐
              │  two elders (advisers); clan heads on    │
              │  council days                            │
              └──────────────────────────────────────────┘
                                    │
          ┌─────────────────────────┼──────────────────────────┐
     ANBU commander          Jonin Commander              Academy headmaster
     (answers to the         (the jonin corps, the         (instructors)
      Hokage alone)           standby station, the
          │                   Mission Desk's C-ranks
     ANBU captains            and above)
          │                         │
     ANBU operatives      elite jonin · jonin · special jonin
                                    │
                                 chunin
                    (squad leaders, the desk, the gate,
                     the watch, the police, medics, teachers)
                                    │
                         genin squads of three
                         under a jonin sensei
                                    │
                            Academy students

  Beside the ladder: retired shinobi (reserves, clan elders, shopkeepers), and civilian officials
```

| Rank | What it means in the Leaf | Wears (wardrobe rank) | Seniority (bonds) |
|---|---|---|---|
| **Hokage** | Leads the village; assigns missions above C-rank, approves promotions, sits on council days ([SIDE_QUESTS.md](../SIDE_QUESTS.md)) | `kage` | 4 |
| **Council elders** | Two advisers at the Hokage's side; retired jonin. They sit in the Residence and speak on council days | `civilian` (elders' robes) | 3 |
| **Jonin Commander** | Leads the jonin corps: picks senseis, runs the standby station, briefs C-ranks and above at the Mission Desk | `jonin` | 3 |
| **ANBU** | Masked special forces, outside the regular chain: a commander, captains and operatives. They answer to the Hokage alone, guard the Residence, and are seen and never known | `anbu` | 3 |
| **Elite jonin** | A jonin of the highest power (tier A). Not a separate rank: the village knows them by reputation | `jonin` | 3 |
| **Jonin** | Full officers: senseis, mission captains, clan heads | `jonin` | 3 |
| **Special jonin** (tokubetsu) | Jonin standing in one field only: the exam proctors, the interrogators, the head medic, sensors | `jonin` | 3 |
| **Chunin** | Squad leaders and the village's working officers: Academy teachers, the Mission Desk, the gate guard, the night watch, police officers, medics | `chunin` | 2 |
| **Genin** | Squads of three under a jonin sensei; D- and C-rank missions | `genin` | 1 |
| **Academy students** | Your class of 12 and the years around it | `academy` | 0 |
| **Retired shinobi** | Reserves who still train, clan elders, shopkeepers with an old forehead protector in a drawer. Rank says nothing about their power | `civilian` | 3 (former rank, for respect) |
| **Civilians** | The Hokage's clerk and the village's daily life | `civilian` | 0 |

**Who runs what.** These are the posts the player deals with.

| Post | Who | Where |
|---|---|---|
| The Mission Desk | Two desk chunin on rotation hand out D-ranks. The Jonin Commander briefs C-ranks, and the Hokage signs above that | The Residence's ground floor |
| The gate | Hagane chunin guards by day; a Tobari chunin keeps the night watch on the wall | The main gate, the wall |
| The police | Run by the Uchiha clan: a jonin chief and chunin officers on patrol | The police HQ in the Uchiha quarter's corner (later), patrols from Beta 2 |
| Interrogation | The Morino; their head is also the written test's proctor | Near the police HQ |
| The hospital | A Suzuran head medic (special jonin) and chunin medics | The hospital |
| The Academy | A retired headmaster, the instructor and two teachers | The Academy |
| The standby station | Jonin between missions, under the Jonin Commander | Near the Residence (Konoha build to place) |

Rank still decides what residents say to you. Residents read rank from their outfit's `rank`
([ROADMAP.md](../ROADMAP.md#residents-react-to-your-rank)), so `rank_distribution.json` maps each
rank onto one of the wardrobe's seven (`outfit_rank`).

## 2. Rank and power

**Rank is what the village trusts you with. Power is what you can do.** The two are separate, as in
canon: a genin can fight like a chunin, a retired shopkeeper can still be among the strongest
people in the village, and a special jonin can be jonin-strength in one field and a chunin
everywhere else.

Power is a **tier**, read from a character's level on the player's own curve
([ROADMAP.md §7](../ROADMAP.md#levels)), so "can I take them?" always has an honest answer.

| Tier | Word | Levels | The player reaches it | Typical holders |
|---|---|---|---|---|
| **E** | Academy | 1–4 | From the start | Academy students |
| **D** | Genin | 5–14 | At graduation (Ch 7) | Genin, new chunin teachers' students |
| **C** | Chunin | 15–29 | Around the Chunin Exams (level 15) | Chunin, strong genin, most special jonin outside their field |
| **B** | Jonin | 30–41 | At the Jonin trial (level 30) | Jonin, ANBU operatives, the council elders, retired jonin |
| **A** | Elite | 42–49 | The road to Hokage opens (42) | Elite jonin, the Jonin Commander, the ANBU commander |
| **S** | Kage-level | 50+ | Succession (50) | The Hokage; the legends the village speaks of |

In their **specialty**, people fight above their tier. A special jonin uses the niche edge that
teammates get (§7): the forest proctor is level 36 (B), but fights as a 40 in survival.

**Rank against power, in the beta:**

| Who | Rank | Tier | Why |
|---|---|---|---|
| `role:senior_a`, the prodigy a year ahead | genin | D at first, C by the exams (level 20) | Talent ahead of rank; the squad a year ahead sits the exams with you |
| `role:legend_veteran`, the old scroll-seller | retired | A (44) | Hung up the forehead protector; still among the six strongest people on the map |
| `role:proctor_forest` | special jonin | B (36) | A jonin in survival, a chunin at a desk |
| The council elders | elder (retired jonin) | B | Advisers, not fighters, but no one forgets what they were |
| `role:instructor` | chunin | C (24) | Strong enough to rescue you, kind enough to teach; rank is about trust as much as power |
| The rival | academy, then genin | E, then D | Always a level or so ahead of you (§7) |

**The player's tier through the game.** You are E in the Academy and D as a genin. You reach C
around the Chunin Exams (levels 15 to 18 in the beta), B at the Jonin trial, A on the road to
Hokage and S at the end. Everyone above tier C is out of reach in the beta, and the beta shows it.

## 3. Feeling the strong

The beta lasts 15 hours and tops out at tier C. The village has to make the player *feel* tiers B,
A and S without letting them fight those tiers. Five tools do it:

1. **Showcase moments.** Scripted scenes where someone strong does something the player cannot
   yet do, close enough to see.
2. **Sparring demos.** Elites spar each other at the training grounds on a schedule you can come and
   watch. A "last thirty seconds" spar against an elite is a lesson, and you are meant to lose it.
3. **Elites on missions.** Their squads pass yours on the road, clear what you could not, or come
   home hurt from something worse.
4. **Legends spoken of.** Residents, the standby station and the Mission Desk talk about people who
   are not there.
5. **Reading power.** Every shinobi shows a tier glyph over their head when you focus on them. It
   reads true up to two tiers above you; beyond that it shows *beyond you* (a dim, flickering
   glyph). As you climb, the glyphs resolve. The player sees the ladder rise ahead of them.

| Slice | Moment | Who | What the player sees |
|---|---|---|---|
| Beta 1 | The rescue (Ch 0) | `role:captain` | A jonin clears a hideout you could not escape, and carries you over a ravine |
| Beta 1 | First morning (Ch 1) | `role:anbu_commander`, `role:anbu_cat` | Masks on the Residence roof; gone when you look back |
| Beta 1 | First lessons (Ch 2) | `role:sensei_senior`, `role:senior_a` | In the Academy yard, the senior squad trains under the taijutsu master. One kick splits a training post you could not dent |
| Beta 1 | Night (Ch 4) | `role:night_watch` | The night watch steps out of the dark on the wall and back into it without a sound |
| Beta 1 | The Rock (Ch 5) | `{hokage:1}` to `{hokage:4}` | The four faces and the instructor's stories about each |
| Beta 2 | The bell test (Ch 8) | `role:sensei` | Your sensei holds the bells against three of you with one hand and a book in the other |
| Beta 2 | The Mission Desk (Ch 9) | `role:jonin_commander`, standby jonin | You queue for a D-rank while jonin walk past to the C-ranks and above |
| Beta 2 | Tree walking (Ch 10) | `role:sensei` and `role:sensei_senior` | The two jonin spar at Training Ground 3: a minute of ninjutsu against taijutsu, trees falling. A rivalry the village bets on |
| Beta 2 | The east road (Ch 11) | `role:elite_scout` | A bandit camp your squad was told to avoid is already ash; the returning captain's squad passes you, one of them carried |
| Beta 2 | The scroll shop (Ch 12) | `role:legend_veteran` | The old seller lights a candle from across the room with a flick of chakra. Residents say who he was |
| Beta 2 | The far road (Ch 13) | `role:anbu_captain` | An ANBU team overtakes your squad on the road, treetop to treetop, there and gone in a breath |
| Beta 2 | Clan welcomes (wave 1) | The eight clan heads | Each head shows the clan's art at full strength: the Hyuga dojo, the Nara shadows, the Inuzuka pack |
| Beta 2 | Standby station talk | `role:legend_wanderer` | Letters, a chair nobody sits in, stories about the one who has been away for years |
| Beta 3 | Exams (Ch 15 to 17) | The three proctors | The written-test proctor's entrance; the forest proctor; the finals proctor stops a bout mid-strike |
| Beta 3 | Forest and finals (Ch 16, 19) | `role:elite_sealer` | A barrier over the whole forest, and one around the arena so the crowd is safe from the bouts |
| Beta 3 | Preliminaries (Ch 17) | `role:senior_a` | The prodigy's bout: a genin fighting at C, a level you are only reaching |
| Beta 3 | The stands (Ch 19) | `role:hokage_4`, the elites | The village's strongest people, all in one place |

**Rules for elites in the beta.**

- They never win the player's fights for them. A scene with an elite ends with the threat gone
  before the player arrives, or with the player doing the part they can.
- Every spar against an elite is a "lose well" scene. It is scored on how long you last and what
  you tried, and it raises friendship.
- They talk about the player's tier honestly ("Come back when you can walk on water") and notice when
  the player climbs.
- Their kits are unique. A pillar's signature technique is never sold as a scroll in the beta.

## 4. Head counts

### On the map

About **300 residents** live on the map, drawn by `population.json` (~45% civilians, ~28% clanless
shinobi, ~15% minor clans, ~13% noble clans). About **166** of them are shinobi, Academy students
or retired shinobi. `rank_distribution.json` gives them ranks.

- Unique posts are **fixed markers** and are never drawn: the Hokage, the two elders, the Jonin
  Commander and the six ANBU.
- A marker with a job takes that job's rank (a gate guard is a chunin).
- A marker bound to a named role takes the role's rank from `roster.json`.
- Every other resident draws a rank by weight for their group. Noble clans lean toward jonin, and
  clanless and minor-clan shinobi toward chunin and genin.

| Rank | Clanless | Minor clans | Noble clans | **On the map** | Away on a typical day | **Home on a typical day** |
|---|---|---|---|---|---|---|
| Hokage | — | — | 1 | **1** | — | 1 |
| Council elders | — | — | 2 | **2** | — | 2 |
| Jonin Commander | — | — | 1 | **1** | — | 1 |
| ANBU (commander, captain, 4 operatives) | 6 (masked) | — | — | **6** | 50% | 3 |
| Elite jonin (tier A) | 2 | — | 2 | **4** | 50% | 2 |
| Jonin | 5 | 5 | 8 | **18** | 40% | 11 |
| Special jonin | 4 | 3 | 1 | **8** | 30% | 6 |
| Chunin | 23 | 13 | 5 | **41** | 35% | 27 |
| Genin | 17 | 8 | 7 | **32** | 25% | 24 |
| Academy students | 16 | 8 | 8 | **32** | — | 32 |
| Retired shinobi | 11 | 8 | 2 | **21** | — | 21 |
| Civilians | — | — | — | **134** | — | 134 |
| **Residents** | 84 | 45 | 37 | **300** | | |

Away means VF's schedule keeps them off the map that day: out of the gate, on a mission. A jonin
you meet on Monday may be gone until Friday, which makes the village feel like a working military
town. Named story characters stay when the story needs them.

### Met and known in the beta

**Met** means a named person with their own lines whom the player gets to know: their name is
learned, and they have a bond and a quest or a scene. Most people you merely pass go uncounted.

| Rank | Beta 1 (Academy) | Beta 2 (Genin) | Beta 2.5 (clan wave 2) | Beta 3 (Exams) | **Whole beta** |
|---|---|---|---|---|---|
| Hokage | 1 | — | — | — | **1** |
| Council elders | 2 | — | — | — | **2** |
| Jonin Commander | — | 1 | — | — | **1** |
| ANBU (masked, never named) | 2 seen | 2 seen | — | (in the stands) | **4 seen** |
| Elite jonin | 2 (your captain, the taijutsu master) | 1 (the returning captain) | — | 1 (the barrier master) | **4** |
| Jonin | — | 11 (three senseis, four clan heads, the police chief, three standby regulars) | 3 (clan heads) | — | **14** |
| Special jonin | 1 (the head medic) | — | 1 (a clan head) | 3 (the proctors) | **5** |
| Chunin | 7 (instructors, the gate, the night watch, the medic) | 3 (the desk, a police officer) | 7 (clan heads) | — | **17** |
| Genin | 3 (the squad a year ahead) | — | — | — | **3** |
| Academy | 11 (your class) | — | — | — | **11** |
| Retired | 1 (the headmaster) | 3 (two clan heads, the old scroll-seller) | 3 (clan heads) | — | **7** |
| Legends | — | 1 spoken of | — | — | **1** |
| **Named shinobi** | **30** | **21** | **14** | **4** | **69 met, 1 spoken of** |

The people you **get to know well** in each slice:

- **Beta 1:** about 16. Your 11 classmates, the instructor, the medic, the captain, the
  headmaster and a gate guard.
- **Beta 2:** about 8 more. Your sensei as sensei, the other three senseis, the desk chunin and the
  clan heads of your welcome quests.
- **Beta 3:** the three proctors. At the finals, nearly everyone above comes back on screen.

### The lore: the village's whole forces

The map is a slice of a bigger village; residents, mission logs and the standby board speak of the
whole. The map holds about one in ten of the Leaf's active shinobi.

| Rank | Lore |
|---|---|
| Hokage, elders, Jonin Commander | 1, 2, 1 |
| ANBU | about 90 |
| Elite jonin | about 20 |
| Jonin | about 110 |
| Special jonin | about 45 |
| Chunin | about 480 |
| Genin | about 360 |
| Academy students | about 240 |
| Retired shinobi | about 300 |
| **Active shinobi** | **about 1,100** |

These numbers live in `rank_distribution.json` (`lore`), so dialogue can quote them with a token
rather than inventing its own.

## 5. Who matters most

Not every jonin is equal. Importance decides how much writing and art a person gets.

| Importance | Who | What they get | In the beta |
|---|---|---|---|
| **Pillar** | Few, story-heavy | A unique look and kit, a signature technique, showcase scenes, a bond line across several slices, voice-like dialogue sets | 10: the Hokage, your sensei, the taijutsu master, the Jonin Commander, the ANBU commander, the returning captain, the old scroll-seller, and your two teammates and the rival |
| **Named** | The village's working faces | Their own name, lines, a quest or a scene, a kit from the shared pool with one twist | 39: the other three senseis, the clan heads of the eight clan seats, the proctors, the desk, the gate, the watch, the medics, the Academy staff, the senior squad, the rest of your class, the barrier master, the elders |
| **Background** | A face with a job | A rank, a role outfit, generated lines from the rank pools, a kit from the shared pool | 20: standby jonin, ANBU operatives, a police officer, the heads of the clans that come in Beta 2.5 (who become named in their own clan line) |
| **Legend** | Spoken of | Stories, letters, a portrait at the standby station | 1: the wandering legend |

**The jonin, by importance:**

- **Pillars (3 jonin and the Jonin Commander):** your sensei, the taijutsu master (the senior
  squad's sensei, your sensei's rival), the returning captain, and the Jonin Commander.
- **Named (9):** the three other senseis, the four jonin clan heads met in Beta 2, the police chief
  (the Uchiha head), and the barrier master.
- **Background (6):** three standby regulars, and the heads of three clans that come in Beta 2.5.
- **Legend (1):** the wandering legend, away all beta.

## 6. The roster

Generated by `python tools/roster/roster.py --table` from `roster.json`. Placeholders are for
developers only; levels are at the end of each beta stretch. Adults hold theirs through the beta.
The class's levels are guides from the typical player's run: in the game they grow with the
player (§7). In Varied saves the classmates' clans and specialties are rolled by the population
weights, so most classmates are clanless there.

| Role | Placeholder | Rank | Tier | Importance | Clan | Specialty | First | Levels (Academy / Genin / Exams) |
|---|---|---|---|---|---|---|---|---|
| `role:hokage_4` | The Fourth Hokage | kage | S | pillar | akimichi | taijutsu | beta1 | 58 / 58 / 58 |
| `role:elder_keeper` | Council Elder 1 | elder | B | named | — | sealing | beta1 | 38 / 38 / 38 |
| `role:elder_councillor` | Council Elder 2 | elder | B | named | — | support | beta1 | 36 / 36 / 36 |
| `role:jonin_commander` | The Jonin Commander | jonin commander | A | pillar | nara | strategy and shadow techniques | beta2 | 46 / 46 / 46 |
| `role:anbu_commander` | ANBU Commander (Fox mask) | anbu | A | pillar | masked | kenjutsu | beta1 | 48 / 48 / 48 |
| `role:anbu_captain` | ANBU Captain (Wolf mask) | anbu | B | named | masked | tracking | beta2 | 40 / 40 / 40 |
| `role:anbu_cat` | ANBU (Cat mask) | anbu | B | background | masked | kenjutsu | beta1 | 34 / 34 / 34 |
| `role:anbu_hawk` | ANBU (Hawk mask) | anbu | B | background | masked | sensing | beta2 | 33 / 33 / 33 |
| `role:sensei` | Your Sensei | jonin | A | pillar | clanless | ninjutsu | beta1 | 44 / 44 / 44 |
| `role:sensei_senior` | The Taijutsu Master | jonin | A | pillar | clanless | taijutsu | beta1 | 45 / 45 / 45 |
| `role:elite_scout` | The Returning Captain | jonin | A | pillar | clanless | kenjutsu | beta2 | 43 / 43 / 43 |
| `role:elite_sealer` | The Barrier Master | jonin | A | named | uzumaki | sealing and barriers | beta3 | 42 / 42 / 42 |
| `role:legend_veteran` | The Old Scroll-Seller | retired | A | pillar | clanless | ninjutsu | beta2 | 44 / 44 / 44 |
| `role:legend_wanderer` | The Wandering Legend | jonin | S | legend | clanless | ninjutsu | spoken | 55 / 55 / 55 |
| `role:instructor` | Your Academy Instructor | chunin | C | named | clanless | ninjutsu and teaching | beta1 | 24 / 24 / 24 |
| `role:instructor_2` | The Throwing Teacher | chunin | C | named | umino | tools | beta1 | 22 / 22 / 22 |
| `role:instructor_3` | The Chakra Teacher | chunin | C | named | clanless | sensing | beta1 | 20 / 20 / 20 |
| `role:headmaster` | The Academy Headmaster | retired | B | named | umino | sealing | beta1 | 34 / 34 / 34 |
| `role:teammate_a` | Teammate A | academy | E | pillar | kurama | genjutsu | beta1 | 5 / 14 / 17 |
| `role:teammate_b` | Teammate B | academy | E | pillar | clanless | taijutsu, with a ninken pup | beta1 | 5 / 14 / 18 |
| `role:rival` | The Rival | academy | E | pillar | uchiha | ninjutsu (fire) | beta1 | 5 / 16 / 19 |
| `role:classmate_c` | Classmate C | academy | E | named | kinoshita | tools and traps | beta1 | 5 / 14 / 17 |
| `role:classmate_d` | Classmate D | academy | E | named | gekko | kenjutsu | beta1 | 5 / 15 / 18 |
| `role:classmate_e` | Classmate E | academy | E | named | hyuga | sensing (Byakugan) | beta1 | 5 / 15 / 18 |
| `role:classmate_f` | Classmate F | academy | E | named | nara | support (shadows) | beta1 | 5 / 13 / 17 |
| `role:classmate_g` | Classmate G | academy | E | named | akimichi | taijutsu (expansion) | beta1 | 5 / 14 / 18 |
| `role:classmate_h` | Classmate H | academy | E | named | clanless | medical | beta1 | 5 / 14 / 17 |
| `role:classmate_i` | Classmate I | academy | E | named | inuzuka | tracking, with a ninken | beta1 | 5 / 15 / 18 |
| `role:classmate_j` | Classmate J | academy | E | named | clanless | sealing | beta1 | 5 / 13 / 17 |
| `role:sensei_2` | The Genjutsu Sensei | jonin | B | named | yuhi | genjutsu | beta2 | 38 / 38 / 38 |
| `role:sensei_3` | The Fire Sensei | jonin | B | named | sarutobi | ninjutsu (fire and wind) | beta2 | 37 / 37 / 37 |
| `role:sensei_4` | The Senbon Sensei | jonin | B | named | shiranui | tools | beta2 | 35 / 35 / 35 |
| `role:senior_a` | Senior A (the prodigy) | genin | D | named | clanless | taijutsu | beta1 | 13 / 16 / 20 |
| `role:senior_b` | Senior B | genin | D | named | clanless | tools (weapons) | beta1 | 11 / 14 / 18 |
| `role:senior_c` | Senior C | genin | D | named | yamanaka | sensing (mind) | beta1 | 11 / 14 / 17 |
| `role:proctor_written` | The Written-Test Proctor | special jonin | B | named | morino | interrogation | beta3 | 33 / 33 / 33 |
| `role:proctor_forest` | The Forest Proctor | special jonin | B | named | clanless | survival | beta3 | 36 / 36 / 36 |
| `role:proctor_finals` | The Finals Proctor | special jonin | B | named | gekko | kenjutsu | beta3 | 34 / 34 / 34 |
| `role:desk_chunin_1` | Mission Desk Chunin 1 | chunin | C | named | clanless | administration | beta2 | 19 / 19 / 19 |
| `role:desk_chunin_2` | Mission Desk Chunin 2 | chunin | C | named | namiashi | administration | beta2 | 18 / 18 / 18 |
| `role:gate_guard_1` | Gate Guard 1 | chunin | C | named | hagane | tools (mace) | beta1 | 20 / 20 / 20 |
| `role:gate_guard_2` | Gate Guard 2 | chunin | C | named | clanless | taijutsu | beta1 | 19 / 19 / 19 |
| `role:night_watch` | The Night Watch | chunin | C | named | tobari | sensing (sound) | beta1 | 23 / 23 / 23 |
| `role:police_chief` | The Police Chief | jonin | B | named | uchiha | ninjutsu (fire) | beta2 | 39 / 39 / 39 |
| `role:police_officer` | Police Officer | chunin | C | background | uchiha | taijutsu | beta2 | 21 / 21 / 21 |
| `role:medic` | The Young Medic | chunin | C | named | clanless | medical | beta1 | 21 / 21 / 21 |
| `role:hospital_head` | The Head Medic | special jonin | B | named | suzuran | medical | beta1 | 35 / 35 / 35 |
| `role:standby_jonin_1` | Standby Jonin 1 | jonin | B | background | clanless | ninjutsu (earth) | beta2 | 33 / 33 / 33 |
| `role:standby_jonin_2` | Standby Jonin 2 | jonin | B | background | clanless | ninjutsu (water) | beta2 | 32 / 32 / 32 |
| `role:standby_jonin_3` | Standby Jonin 3 | jonin | B | background | clanless | genjutsu | beta2 | 31 / 31 / 31 |
| `role:clan_head.senju` | Head of the Senju | retired | B | named | senju | ninjutsu (wood) | beta2 | 36 / 36 / 36 |
| `role:clan_head.uzumaki` | Head of the Uzumaki | retired | B | named | uzumaki | sealing | beta2 | 33 / 33 / 33 |
| `role:clan_head.hyuga` | Head of the Hyuga | jonin | B | named | hyuga | taijutsu (gentle fist) | beta2 | 41 / 41 / 41 |
| `role:clan_head.akimichi` | Head of the Akimichi | jonin | B | named | akimichi | taijutsu (expansion) | beta2 | 38 / 38 / 38 |
| `role:clan_head.yamanaka` | Head of the Yamanaka | jonin | B | named | yamanaka | sensing (mind) | beta2 | 37 / 37 / 37 |
| `role:clan_head.inuzuka` | Head of the Inuzuka | jonin | B | named | inuzuka | tracking, with ninken | beta2 | 36 / 36 / 36 |
| `role:clan_head.sarutobi` | Head of the Sarutobi | jonin | B | background | sarutobi | ninjutsu (fire) | beta2.5 | 35 / 35 / 35 |
| `role:clan_head.aburame` | Head of the Aburame | jonin | B | background | aburame | tracking (insects) | beta2.5 | 35 / 35 / 35 |
| `role:clan_head.kurama` | Head of the Kurama | retired | B | background | kurama | genjutsu | beta2.5 | 30 / 30 / 30 |
| `role:clan_head.shimura` | Head of the Shimura | retired | B | background | shimura | ninjutsu (wind) | beta2.5 | 32 / 32 / 32 |
| `role:clan_head.yuhi` | Head of the Yuhi | jonin | B | background | yuhi | genjutsu | beta2.5 | 34 / 34 / 34 |
| `role:clan_head.gekko` | Head of the Gekko | special jonin | B | background | gekko | kenjutsu | beta2.5 | 33 / 33 / 33 |
| `role:clan_head.shiranui` | Head of the Shiranui | chunin | C | background | shiranui | tools (senbon) | beta2.5 | 26 / 26 / 26 |
| `role:clan_head.umino` | Head of the Umino | chunin | C | background | umino | teaching | beta2.5 | 24 / 24 / 24 |
| `role:clan_head.haruno` | Head of the Haruno | chunin | C | background | haruno | chakra control | beta2.5 | 22 / 22 / 22 |
| `role:clan_head.namiashi` | Head of the Namiashi | chunin | C | background | namiashi | taijutsu (footwork) | beta2.5 | 23 / 23 / 23 |
| `role:clan_head.hagane` | Head of the Hagane | chunin | C | background | hagane | tools (metalwork) | beta2.5 | 22 / 22 / 22 |
| `role:clan_head.kinoshita` | Head of the Kinoshita | retired | C | background | kinoshita | tools (carpentry) | beta2.5 | 18 / 18 / 18 |
| `role:clan_head.tsuchigumo` | Head of the Tsuchigumo | chunin | C | background | tsuchigumo | ninjutsu (earth binding) | beta2.5 | 27 / 27 / 27 |
| `role:clan_head.tobari` | Head of the Tobari | chunin | C | background | tobari | sensing (sound) | beta2.5 | 26 / 26 / 26 |

**Civilians in the story:** `role:librarian` (Beta 1), `role:merchant` (Beta 2) and the Hokage's
clerk `role:residence_clerk` (Beta 1). They are listed under `civilians` with rank only.

**Squads.** Your year makes four squads of three, and every squad has a jonin sensei:

| Squad | Sensei | Members |
|---|---|---|
| `squad_1` | `role:sensei` | You, `role:teammate_a`, `role:teammate_b` (`role:classmate_c` on the bench) |
| `squad_2` | `role:sensei_2` | `role:rival`, `role:classmate_c`, `role:classmate_d` |
| `squad_3` | `role:sensei_3` | `role:classmate_e`, `role:classmate_f`, `role:classmate_g` |
| `squad_4` | `role:sensei_4` | `role:classmate_h`, `role:classmate_i`, `role:classmate_j` |
| `squad_senior` (a year ahead) | `role:sensei_senior` | `role:senior_a`, `role:senior_b`, `role:senior_c` |

## 7. Growing up together

Your teammates grow at your pace, so it never feels like you are the strong one and they are not.
The engine is [`life/roster`](../life/roster) (package `dev.shinobi.life.roster`).

### The model

Every classmate has their own XP on the player's own curve (main-path minutes: about 50 a level in
the beta and 65 to 112 later), their own techniques and their own niche.

- **Shared work.** On a day the group is together, they earn what the player earned on it. The
  group is the whole class in the Academy, and the squad from team assignment.
- **Days apart.** They train and take missions on their own. They earn the player's recent daily
  pace, a moving average of the player's own XP, times their **drive** (0.85 to 1.15). From team
  assignment the rest of the class is on squads of its own, so every day is a day apart for them.
- **Catch-up and slowdown.** Each person belongs somewhere: `player + offset`. Their gain is
  scaled by `1 − 0.5 × gap` (between 0.2 and 2.2). Behind, they catch up; ahead, they slow down.
- **The band is a safety net.** Teammates stay within 2 levels of you either way. The class stays
  within 3, and the rival within 1 behind to 3 ahead.
  - Below the band, they jump back in with a `caught_up` event: "I trained every day you were
    away".
  - Above it, they wait with a `plateau` event.
  - The band is measured from your *best* level, so dying (a level lost) does not drag the squad
    down with you.
- **The rival runs slightly ahead.** The rival's offset is +1 and their drive 1.15. You can catch
  them for a day, rarely for long.
- **Better than you in their niche.** In their own field a teammate fights `1 + 0.06 × level`
  levels higher: about 2 levels by the exams, 4 at level 50. A teammate a little behind you overall
  is still the one you want for genjutsu, tracking or a sword.
- **Techniques you see them learn.** Each person has a kit: the Academy three, two niche techniques,
  a nature, a clan technique for the clan-born, the exam reward, then the later arcs. Each technique
  has a minimum level and a moment.
  - The moment is a story beat (`ch12.natures`) or **training the player shares**.
  - A technique whose moment came before they were ready shows at the next beat or training where
    you see them.
  - So does a technique learned on another squad (you see the rival's new fire at the exams).
  - Nobody learns anything off-screen.
- **Bonds feed growth.** Training or sparring together is worth **+2% per bond level** to both of
  you (+20% at level 10; `Roster.trainingBonus`, the same number the Progression mod gives the
  player). A quarrel takes the bonus away.
- **Kindle makes them stronger still** (after the beta). While you kindle an ally's flame, they
  fight 3 levels higher in their niche, and each kindling leaves a little XP with them. A full-tier
  Kindling bond adds a permanent level to their niche.
- **Time skips** even everyone out halfway toward where they belong.
- **Promotions** set level floors (genin 5, chunin 15, jonin 30): never below, lifted to it. Who is
  promoted when is the story's call (§9).

### The 60 hours, simulated

`./gradlew :life:roster:simulate` plays the main path with the Classic class for three kinds of
player, the same three as the bond simulation ([BONDS.md §15](../BONDS.md#15-pacing)). Their bond
levels are the bond simulation's.

- **Devoted:** side quests worth 30% more XP, rarely dies.
- **Typical:** 10% more XP from side quests, dies now and then.
- **Reckless:** fails missions, dies often and skips training. One teammate leaves at Ch 12 and a
  classmate steps in.

The player grinds before a gate if they are short of it.

**The typical player, seed 20261029** (fractional levels at each chapter's end; share is a
teammate's contribution over yours, see below):

| Ch | Hours | You | Teammate A | Teammate B | Classmate C | Classmate D | Rival | Share A / B |
|---|---|---|---|---|---|---|---|---|
| 7 Graduation | 4.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | — |
| 8 Team assignment | 4.9 | 5.8 | 5.5 | 5.6 | 5.9 | 6.5 | 6.9 | 1.02 / 1.04 |
| 11 First C-rank | 8.3 | 10.7 | 10.0 | 10.4 | 10.1 | 10.9 | 12.0 | 0.99 / 1.03 |
| 14 Second C-rank | 12.0 | 15.2 | 14.4 | 14.9 | 14.4 | 15.4 | 16.1 | 0.99 / 0.99 |
| 16 Forest of Death | 13.3 | 16.6 | 15.9 | 16.2 | 16.3 | 17.0 | 18.1 | 1.00 / 0.99 |
| 20 Results | 15.0 | 18.3 | 17.9 | 18.3 | 17.8 | 18.7 | 19.5 | 1.02 / 1.01 |
| Chunin arc end | 28.0 | 29.9 | 29.4 | 29.8 | 29.5 | 30.3 | 30.9 | 1.03 / 0.99 |
| Jonin arc end | 45.0 | 41.4 | 41.0 | 41.6 | 41.0 | 41.9 | 42.7 | 1.03 / 1.01 |
| Road to Hokage end | 60.0 | 50.0 | 48.4 | 48.8 | 48.3 | 49.2 | 50.2 | 1.03 / 1.00 |

**Across five seeds** (`SEEDS` in `Season`; gaps are against your best level, every day of the
60 hours):

| Player | Teammates vs you | Rival vs you | Rival ahead | Band stepped in | Share (Genin on) | Beta end: you / A / B / rival |
|---|---|---|---|---|---|---|
| Devoted | −1.7 to +0.5 | −0.4 to +2.0 | 93% of days | never | 0.87 to 1.09 | 21–22 / 21 / 21–22 / 23–24 |
| Typical | −1.2 to +1.1 | +0.0 to +2.3 | 99% | never | 0.95 to 1.12 | 18 / 17–18 / 18–19 / 19–20 |
| Reckless | −1.0 to +1.5 | +0.1 to +2.6 | 87% | never | 0.90 to 1.43 | 15–18 / 16–18 / 16–18 / 18–19 |

What it shows:

- **Teammates stay within the band** for every player and seed, and the pull alone keeps them
  there: the band never had to step in.
- **A devoted player** pulls about a level ahead, and their teammates trail by one at worst.
- **A reckless player** who keeps dying is carried for a while. Their teammates sit up to 1.5
  levels above their best (more above their current level after a death), and early in Genin life
  their share reaches 1.4. The stronger squad is the game's comment on how they play.
- **The rival is ahead on 87 to 99% of days**, by about 1.3 levels on average. A devoted player
  passes them now and then.
- **Techniques match:** at the beta's end you have 8 techniques, and each teammate 7 or 8.

`SeasonTest` holds all of this on five seeds: the band, the mean gap under a level, the band
stepping in on under 2% of days, the share and the rival's lead.

### Pulling their weight

The target is teammates' damage and utility at **70 to 110% of the player's**.
`Contribution.share` is the roster's own first estimate:
`power = level × (1 + 0.04 × techniques)`, and in 35% of fights the fight plays to their niche.
For a typical player it gives 0.95 to 1.12 from team assignment on. The real numbers are Shinobi
Combat's duel simulator's: it runs the level tables above with each teammate's kit and returns
damage and utility shares. If the duel simulator says teammates pull too much, the lever is their
`offset` (in `Roster.CLASS`), not their XP.

### Hooks for the other mods

| Hook | From | Into the roster |
|---|---|---|
| `Day(playerXp, sharedXp, together, bonds)` | Progression (the player's XP; which XP was shared: lessons, missions, squad training) | Once per in-game day |
| `BondInput(level, trainedTogether, quarrel, kindling)` | Life's bond engine (`BondWorld`: the level each person acts on, today's training and spar acts, an active quarrel, `Kindling.tier`) | Per person, in `Day.bonds` |
| `beat(id, present)` | Progression's quests (a story beat and who was there) | Techniques shown at beats |
| `promote(role, floor)` | Progression's ranks (the story decides who) | Level floors |
| `kindle(role)` | Combat's `kindle` effect | The flame's power and its ember |
| `timeSkip()` | Progression's `time_skip` action | Everyone evens out |
| `level(role)`, `tier`, `nicheLevel`, `techniques` | Read by Combat (NPC kits and stats), Missions (`groupLevel()` for squad strength) and the story's level reads | — |

## 8. Data, code and Phase 0

```
python tools/roster/roster.py --check          # roster.json and rank_distribution.json
./gradlew :life:roster:test                     # 26 tests
./gradlew :life:roster:simulate                 # the 60-hour growth tables (-Pseed=N, -Pseeds=a,b,c)
./gradlew :life:roster:simulate -Pstretches     # each classmate's level at each stretch's end, for roster.json
```

**What waits for Phase 0:**

- The Life mod's glue: feeding `Day` from the player's XP and VF's daily cycle, and `BondInput`
  from `BondWorld`.
- Saving the roster with the save (`Roster.save()` and `load()`, a line format beside the bond
  engine's).
- NPC stats from tiers (Combat).
- The population sampler reading `rank_distribution.json` (tools/wardrobe is shared; this is a
  proposal for its owner).
- Markers tagged with jobs (Konoha build).
- The tier glyph over residents' heads (Village's client).
- The rank dialogue pools for special jonin, elders and retired shinobi (Dialogue).

## 9. Open questions

- **Promotion at the Chunin Exams.** Is the whole squad promoted together, or only some? It is a
  story question; the roster supports either.
- **Story reconciliation.** The story session confirms which story roles exist and their public
  ranks; the Hokage's circle and the pillars invented here (the Jonin Commander, the taijutsu
  master, the returning captain, the barrier master, the old scroll-seller, the wandering legend)
  await its yes.
- **The tier glyph.** Should it read true two tiers up, or only one?
- **Contribution shares.** Waiting on Combat's duel simulator.
