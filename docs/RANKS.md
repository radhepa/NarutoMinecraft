# Ranks

The ninja hierarchy of the Leaf: who holds which rank, how strong they really are, how many of
each live in the village and how many you meet, which of them matter most, and how your classmates,
your squad and the squad a year ahead grow up beside you.

**No spoilers here.** Every rank in this file is a character's *public* rank, the one the player
sees on first meeting them. The story's characters belong to the [story bible](story/STORY_BIBLE.md);
this file only names their role, rank and public introduction.

**Names are rolled per save** ([ROADMAP.md](../ROADMAP.md#names-rolled-per-save)). Below, people
are roles (`role:sensei`), with developer placeholder names. Anything that ships uses tokens like
`{name:role:sensei}`; placeholders never appear in the game.

- Placeholders are written **given name first, family name last**: "Natsu Nara".
- Honorifics stay natural ("Nara-sensei"), and a Hokage goes by given name only.
- **Clan members carry their clan's name.**
- **Everyone else has an ordinary family name** from `family_names` in
  [`population.json`](../tools/wardrobe/population.json). It never matches a clan, and the roster
  says so: "Riku Ogawa (no clan)", with clan `none`.

| File | What it holds |
|---|---|
| [`tools/roster/roster.json`](../tools/roster/roster.json) | Every named shinobi of the beta (65) and the story's civilians (4). Each has a role, name, rank, tier, importance, spotlight, clan and clan power, specialty, first appearance and levels. The file also holds the class's clan weights and the squads |
| [`tools/roster/rank_distribution.json`](../tools/roster/rank_distribution.json) | How every other resident gets a rank and a level: weights per group, fixed posts, rank level spreads, clan power, job ranks, the share away on missions, and the lore numbers |
| [`tools/roster/roster.py`](../tools/roster/roster.py) | `--check` validates both files against each other, the level curve, the wardrobe's clans, looks and family names, and `population.json`. `--table`, `--counts` and `--power` print the tables below |
| [`life/roster`](../life/roster) | The growth engine: pure Java, no Minecraft, seeded (`./gradlew :life:roster:test`, `./gradlew :life:roster:simulate`) |

## Contents

1. [The hierarchy](#1-the-hierarchy)
2. [Rank and power](#2-rank-and-power)
3. [Clan power](#3-clan-power)
4. [Feeling the strong](#4-feeling-the-strong)
5. [Head counts](#5-head-counts)
6. [Who matters most](#6-who-matters-most)
7. [The roster](#7-the-roster)
8. [Growing up together](#8-growing-up-together)
9. [Data, code and Phase 0](#9-data-code-and-phase-0)
10. [Open questions](#10-open-questions)

## 1. The hierarchy

```
                                  Hokage
                                    │
               ┌──────────── the council ─────────────┐
               │  three elders (advisers); clan heads  │
               │  on council days                      │
               └───────────────────────────────────────┘
                                    │
          ┌─────────────────────────┼──────────────────────────┐
         ANBU                Jonin Commander              Academy headmaster
   (answer to the Hokage     (the jonin corps, the         (instructors)
    alone; masked)            standby station, the
                              Mission Desk's C-ranks
                              and above)
                                    │
                  elite jonin · jonin · special jonin
                                    │
                                 chunin
                  (squad leaders, the desk, the gate, the
                   watch, the police, medics, teachers)
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
| **Council elders** | Three advisers at the Hokage's side, all retired jonin. They sit in the Residence and speak on council days | `civilian` (elders' robes) | 3 |
| **Jonin Commander** | Leads the jonin corps: picks senseis, runs the standby station, and briefs C-ranks and above. The post belongs to the story; the beta does not show who holds it | `jonin` | 3 |
| **ANBU** | Masked special forces outside the regular chain. They answer to the Hokage alone and guard the Residence. In the beta you see only masks: no names, no clans | `anbu` | 3 |
| **Elite jonin** | A jonin of the highest power (tier A). Not a separate rank: the village knows them by reputation | `jonin` | 3 |
| **Jonin** | Full officers: senseis, mission captains, clan heads | `jonin` | 3 |
| **Special jonin** (tokubetsu) | Jonin standing in one field only: the exam proctors, the interrogators, the head medic | `jonin` | 3 |
| **Chunin** | Squad leaders and the village's working officers: Academy teachers, the Mission Desk, the gate, the night watch, police officers, medics | `chunin` | 2 |
| **Genin** | Squads of three under a jonin sensei; D- and C-rank missions | `genin` | 1 |
| **Academy students** | Your class of 12 and the years around it | `academy` | 0 |
| **Retired shinobi** | Reserves who still train, clan elders, shopkeepers with an old forehead protector in a drawer. Rank says nothing about their power | `civilian` | 3 (former rank, for respect) |
| **Civilians** | The Hokage's clerk and the village's daily life | `civilian` | 0 |

**Who runs what.** These are the posts the player deals with. Places come from the Konoha build's
markers.

| Post | Who | Where | Job id |
|---|---|---|---|
| The Mission Desk | Desk chunin on rotation (3 slots) hand out D-ranks. Jonin brief C-ranks and above, and the Hokage signs them | The Residence's ground floor (Beta 2) | `mission_desk` |
| The jonin standby station | Jonin between missions (6 slots) | Beside the Residence (Beta 2) | `jonin_standby` |
| The gate | Hagane chunin in the booth by day (2 slots), with the gate barracks next door | The main gate (Beta 1) | `gate_guard` |
| The wall | A Tobari chunin in each wall tower at night: 2 towers in Beta 1, 5 by Beta 2, 8 by Beta 3 | The wall | `wall_watch` |
| The police | Run by the Uchiha clan: a jonin chief (the clan's head) and chunin officers on patrol | Patrols from Beta 2; the HQ in the Uchiha compound later | `police` |
| Interrogation | The Morino | The Morino house in the beta; interrogation rooms later | `interrogator` |
| The hospital | A Suzuran head medic (special jonin) and chunin medics, day and night (6 slots) | The hospital (Beta 1) | `medic` |
| The Academy | A retired headmaster, the instructor and teachers (5 slots) | The Academy (Beta 1) | `academy_teacher` |
| ANBU | Masked figures on the Residence rooftops at night | Rooftop markers; their HQ later | `anbu` |

Residents read rank from their outfit's `rank` ([ROADMAP.md](../ROADMAP.md#residents-react-to-your-rank)),
so `rank_distribution.json` maps every rank onto one of the wardrobe's seven (`outfit_rank`).

## 2. Rank and power

**Rank is what the village trusts you with; power is what you can do.** The two are separate, as in
canon:

- A genin can fight like a chunin.
- A retired shopkeeper can still be among the strongest people in the village.
- A special jonin can be jonin-strength in one field and a chunin everywhere else.

Power is a **tier**, read from a character's level on the player's own curve
([ROADMAP.md §7](../ROADMAP.md#levels)), so "can I take them?" always has an honest answer.

| Tier | Word | Levels | The player reaches it | Typical holders |
|---|---|---|---|---|
| **E** | Academy | 1–4 | From the start | Academy students |
| **D** | Genin | 5–14 | At graduation (Ch 7) | Genin |
| **C** | Chunin | 15–29 | Around the Chunin Exams (level 15) | Chunin, strong genin, most special jonin outside their field |
| **B** | Jonin | 30–41 | At the Jonin trial (level 30) | Jonin, ANBU, the council elders, retired jonin |
| **A** | Elite | 42–49 | When the road to Hokage opens (42) | Elite jonin |
| **S** | Kage-level | 50+ | At succession (50) | The Hokage; the legends the village speaks of |

In their **specialty**, people fight above their tier: the niche edge teammates get (§8) applies
to everyone. The forest proctor is level 36 (B), but fights as a 40 in survival.

**Rank against power, in the beta:**

| Who | Rank | Tier | Why |
|---|---|---|---|
| `role:squad5_c`, the clanless prodigy a year ahead | genin | D at first sight (about level 10), C by team assignment (14), about 23 by the exams | Outworks everyone: ahead of rank, and ahead of clan |
| `role:legend_veteran`, the old scroll-seller | retired | A (44) | Hung up the forehead protector; still one of the strongest people on the map |
| `role:proctor_forest` | special jonin | B (36) | A jonin in survival, a chunin at a desk |
| The council elders | elder (retired jonin) | B | Advisers, not fighters, but no one forgets what they were |
| `role:instructor` | chunin | C (24) | Strong enough to rescue you, kind enough to teach; rank is about trust as much as power |
| `role:rival` | academy, then genin | E, then D | Always a level or so ahead of you (§8) |

**The player's tier through the game.** You start at E in the Academy and are D as a genin. You
reach C around the Chunin Exams (levels 15 to 18 in the beta), B at the Jonin trial, A on the road
to Hokage, and S at the end. Everyone at B and above is out of reach in the beta, and the beta
shows it.

## 3. Clan power

People of powerful clans are **stronger on average, never by rule**. This applies to NPCs only: the
player starts as a clanless orphan, and their balance is character creation's.

| Clan power | Clans | Shift within their rank | A rolled classmate's place against you | Training drive |
|---|---|---|---|---|
| **Great** | Uchiha, Hyuga, Senju, Uzumaki | +0.6 standard deviations | +0.8 levels | ×1.06 |
| **Strong** | The other eleven noble clans | +0.3 | +0.3 | ×1.03 |
| **Minor** | The ten minor clans | 0 | −0.1 | ×1.00 |
| **Clanless** | No clan | −0.2 | −0.3 | ×1.00 |

A resident's level is drawn inside their rank's spread (`rank_levels`) and shifted by clan power.
The spreads overlap, so hard-working clanless prodigies exist. Average level of drawn residents
(`python tools/roster/roster.py --power`):

| Rank | Spread | Great | Strong | Minor | Clanless | Clanless above the great clans' median |
|---|---|---|---|---|---|---|
| Academy | 1–4 | 3.0 | 2.8 | 2.5 | 2.3 | 22% |
| Genin | 5–16 | 10.8 | 9.9 | 9.1 | 8.6 | 21% |
| Chunin | 15–30 | 23.4 | 22.2 | 21.1 | 20.4 | 21% |
| Special jonin | 26–38 | 32.8 | 31.9 | 31.1 | 30.5 | 21% |
| Jonin | 30–41 | 36.7 | 35.9 | 35.0 | 34.5 | 21% |
| Elite jonin | 42–49 | 46.1 | 45.6 | 45.1 | 44.7 | 21% |
| Retired | 12–46 | 32.6 | 30.3 | 28.1 | 26.6 | 22% |

So about one clanless shinobi in five beats the great clans' median at their rank.

**In your year** the Classic cast follows the story, with exceptions on purpose:

- **Strongest of the class:** the rival (Uchiha) and the Hyuga heir.
- **Strongest of all:** the squad a year ahead's clanless prodigy.
- **Lowest at first, then catching up:** the loud clanless teammate and the Inuzuka.

**Your class leans toward the important clans**, so familiar names appear early. The village
population stays as it is, with noble clans rare.

- **The class.** `class_clan_weights` in `roster.json` rolls the eleven classmates in a Varied save:
  68% noble, 20% minor, 12% clanless. The roll picks a clan group first, then a clan inside it by
  `population.json`'s weights. The Classic class is 8 noble, 2 minor and 1 clanless.
- **The squad a year ahead and the senseis** lean noble less (`squad_clan_weights`: 45 / 30 / 25).

## 4. Feeling the strong

The beta lasts 15 hours and tops out at tier C. The village has to make tiers B, A and S felt
without letting the player fight them. Five tools do it:

1. **Showcase moments.** Scripted scenes where someone strong does what the player cannot yet do,
   close enough to see.
2. **Sparring demos.** Elites spar each other at the training grounds on a schedule you can come and
   watch. A "last thirty seconds" spar against an elite is a lesson, and you are meant to lose it.
3. **Elites on missions.** Their squads pass yours on the road, clear what you could not, or come
   home hurt from something worse.
4. **Legends spoken of.** Residents, the standby station and the Mission Desk talk about people who
   are not there.
5. **Reading power.** When you focus on a shinobi, a tier glyph shows over their head.
   - It reads true up to two tiers above you.
   - Beyond that it shows *beyond you*, as a dim, flickering glyph.
   - As you climb, the glyphs resolve, so you see the ladder rise ahead of you.

| Slice | Moment | Who | What the player sees |
|---|---|---|---|
| Beta 1 | The rescue (Ch 0) | `role:captain` | A jonin clears a hideout you could not escape, and carries you over a ravine |
| Beta 1 | First morning (Ch 1) | `role:anbu_cat` | A mask on the Residence roof, gone when you look back |
| Beta 1 | First lessons (Ch 2) | `role:taijutsu_master`, `role:squad5_c` | In the Academy yard, the prodigy a year ahead trains under the taijutsu master. One kick splits a post you could not dent |
| Beta 1 | Night (Ch 4) | `role:night_watch` | The night watch steps out of the dark on the wall and back into it without a sound |
| Beta 1 | The Rock (Ch 5) | `{hokage:1}` to `{hokage:4}` | The four faces, and the instructor's stories about each |
| Beta 2 | The bell test (Ch 8) | `role:sensei` | Your sensei holds the bells against all three of you |
| Beta 2 | The Mission Desk (Ch 9) | Standby jonin | You queue for a D-rank while jonin walk past to the C-ranks and above |
| Beta 2 | Tree walking (Ch 10) | `role:sensei` and `role:sensei_2` | Your sensei's self-declared rival picks a fight at Training Ground 3: a minute of ninjutsu against senbon, with trees falling. The village bets on them |
| Beta 2 | The east road (Ch 11) | `role:elite_scout` | A bandit camp your squad was told to avoid is already ash; the returning captain's squad passes you, one of them carried |
| Beta 2 | The scroll shop (Ch 12) | `role:legend_veteran` | The old seller lights a candle from across the room with a flick of chakra. Residents say who he was |
| Beta 2 | The far road (Ch 13) | An ANBU team | Masks overtake your squad treetop to treetop, there and gone in a breath |
| Beta 2 | Clan welcomes (wave 1) | Clan heads | Each head shows the clan's art at full strength: the Nara shadows, the Inuzuka pack |
| Beta 2 | Standby station talk | `role:legend_wanderer` | Letters, a chair nobody sits in, and stories about the one who has been away for years |
| Beta 3 | The exams (Ch 15 to 17) | The three proctors | The written-test proctor's entrance, the forest proctor, and the finals proctor stopping a bout mid-strike |
| Beta 3 | Preliminaries (Ch 17) | `role:squad5_c` | The prodigy's bout: a clanless genin fighting at C against a great clan, and winning |
| Beta 3 | The stands (Ch 19) | `role:hokage_4`, the elites | The village's strongest people, all in one place |

**Rules for elites in the beta:**

- **They never win the player's fights for them.** A scene with an elite ends with the threat gone
  before the player arrives, or with the player doing the part they can.
- **Every spar against an elite is a "lose well" scene.** It is scored on how long you last and what
  you tried, and it raises friendship.
- **They talk about your tier honestly** ("Come back when you can walk on water"), and they notice
  when you climb.
- **Their kits are unique.** A pillar's signature technique is never sold as a scroll in the beta.

## 5. Head counts

### On the map

The finished map holds about **300 residents**, drawn by `population.json`: about 45% civilians,
28% clanless shinobi, 15% minor clans and 13% noble clans. By the end of Beta 3 about 220 have moved
in, across 110 homes, 15 apartment buildings and the clan seats. About **166** of the 300 are
shinobi, Academy students or retired shinobi. `rank_distribution.json` gives them ranks:

- **Unique posts are fixed markers, never drawn:** the Hokage, the three elders, the Jonin
  Commander's post and the six ANBU.
- **A marker bound to a named role** takes the role's rank from `roster.json`.
- **A marker that pins a rank** uses that rank, and a workplace's `rank_min` sets a floor.
- **A marker with a job** takes the job's rank.
- **Every other resident** draws a rank by weight for their group. Noble clans lean toward jonin;
  clanless and minor-clan shinobi lean toward chunin and genin.

| Rank | Clanless | Minor clans | Noble clans | **On the map** | Away on a typical day | **Home on a typical day** |
|---|---|---|---|---|---|---|
| Hokage | — | — | 1 | **1** | — | 1 |
| Council elders | 1 | — | 2 | **3** | — | 3 |
| Jonin Commander | — | — | 1 | **1** | — | 1 |
| ANBU (masked) | 6 | — | — | **6** | 50% | 3 |
| Elite jonin (tier A) | 2 | — | 2 | **4** | 50% | 2 |
| Jonin | 5 | 5 | 8 | **18** | 40% | 11 |
| Special jonin | 4 | 3 | 1 | **8** | 30% | 6 |
| Chunin | 23 | 13 | 5 | **41** | 35% | 27 |
| Genin | 17 | 8 | 7 | **32** | 25% | 24 |
| Academy students | 16 | 8 | 8 | **32** | — | 32 |
| Retired shinobi | 10 | 8 | 2 | **20** | — | 20 |
| Civilians | — | — | — | **134** | — | 134 |
| **Residents** | 84 | 45 | 37 | **300** | | |

"Away" means VF's schedule keeps them off the map that day: out of the gate, on a mission. A jonin
you meet on Monday may be gone until Friday, which makes the village feel like a working military
town. Named story characters stay when the story needs them.

### Met and known in the beta

**Met** means a named person with their own lines whom the player gets to know: their name, a bond,
and a quest or a scene. The many you merely pass are not counted.

| Rank | Beta 1 (Academy) | Beta 2 (Genin) | Beta 2.5 (clan wave 2) | Beta 3 (Exams) | **Whole beta** |
|---|---|---|---|---|---|
| Hokage | 1 | — | — | — | **1** |
| Council elders | 3 | — | — | — | **3** |
| ANBU (masked, never named) | 1 seen | 1 seen | — | (in the stands) | **2 seen** |
| Elite jonin | 2 (your captain, the taijutsu master) | 2 (the second sensei, the returning captain) | — | — | **4** |
| Jonin | 1 (the senior squad's sensei) | 8 (two senseis, two clan heads, the police chief, three standby regulars) | 3 (clan heads) | — | **12** |
| Special jonin | 1 (the head medic) | — | 2 (clan heads) | 3 (the proctors) | **6** |
| Chunin | 7 (instructors, the gate, the night watch, the medic) | 3 (the desk, a police officer) | 7 (clan heads) | — | **17** |
| Genin | 3 (the squad a year ahead) | — | — | — | **3** |
| Academy | 11 (your class) | — | — | — | **11** |
| Retired | 1 (the headmaster) | 1 (the old scroll-seller) | 3 (clan heads) | — | **5** |
| Legends | — | 1 spoken of | — | — | **1** |
| **Named shinobi** | **31** | **15** | **15** | **3** | **64 met, 1 spoken of** |

The people you **get to know well** in each slice:

- **Beta 1, about 17:** your 11 classmates, the instructor, the medic, the captain, the sensei of
  the squad a year ahead, the headmaster and a gate guard.
- **Beta 2, about 8 more:** your sensei in that role, the other senseis, the desk chunin, and the
  clan heads of your welcome quests.
- **Beta 3, 3 more:** the proctors. At the finals, nearly everyone above comes back on screen.

### The lore: the village's whole forces

The map is a slice of a bigger village. Residents, mission logs and the standby board speak of the
whole. The map holds about one in ten of the Leaf's active shinobi.

| Rank | Lore |
|---|---|
| Hokage, elders, Jonin Commander | 1, 3, 1 |
| ANBU | about 90 |
| Elite jonin | about 20 |
| Jonin | about 110 |
| Special jonin | about 45 |
| Chunin | about 480 |
| Genin | about 360 |
| Academy students | about 240 |
| Retired shinobi | about 300 |
| **Active shinobi** | **about 1,100** |

The lore numbers live in `rank_distribution.json` (`lore`), so dialogue can quote one figure instead
of inventing its own.

## 6. Who matters most

Not every jonin is equal. Every named person carries two fields:

- **`importance`** is the story's weight:
  - *story-driving*: the story moves through them.
  - *fan-favourite*: they don't move the story, but players will look for them.
  - *background*: a face with a job.
- **`spotlight`** is the writing and art budget.

| Spotlight | What they get | In the beta |
|---|---|---|
| **Pillar** | A unique look and kit, a signature technique, showcase scenes, a bond line across several slices | 12: the Hokage, the five senseis, your two teammates and the rival, the taijutsu master, the returning captain, the old scroll-seller |
| **Named** | Their own lines and a quest or a scene; a kit from the shared pool with one twist | 31: the rest of your year, the squad a year ahead, the elders, the Academy staff, the proctors, the desk, the gate, the watch, the medics, the police chief, the clan heads of Beta 2 |
| **Background** | A rank, a role outfit, generated lines from the rank pools | 21: standby jonin, ANBU, a police officer, and the clan heads of Beta 2.5 (who become named in their own clan line) |
| **Legend** | Stories, letters, a portrait at the standby station | 1: the wandering legend |

| Importance | Who |
|---|---|
| **Story-driving** (25) | The Hokage and the three elders, the five senseis, your year (all eleven) and the squad a year ahead, the instructor and the medic |
| **Fan-favourite** (13) | The taijutsu master, the returning captain, the old scroll-seller, the wandering legend, the three proctors, the gate guards and the night watch, the police chief, the Nara and Inuzuka heads |
| **Background** (27) | Everyone else: the desk, the standby regulars, the Academy teachers, the hospital, ANBU, most clan heads |

**The jonin by importance:**

- **Story-driving pillars:** the five senseis.
- **Fan-favourite pillars:** the taijutsu master and the returning captain.
- **Fan-favourite legend:** the wandering legend.
- **Other fan-favourites:** the police chief and two clan heads.
- **Background:** the standby regulars and three clan heads.

## 7. The roster

`python tools/roster/roster.py --table` generates this table from `roster.json`. The placeholder
names are for developers only.

- `*` marks a provisional entry, made here to fill a post until the story's cast reaches it.
- Levels are at the end of each beta stretch. Adults hold theirs through the beta.
- For your year and the squad ahead, levels are guides from the typical player's run. In the game
  they grow with the player (§8).

| Role | Placeholder name | Rank | Tier | Importance | Spotlight | Clan (power) | Specialty | First | Levels (Academy / Genin / Exams) |
|---|---|---|---|---|---|---|---|---|---|
| `role:hokage_4` | Hiroshi | kage | S | story-driving | pillar | akimichi (strong) | taijutsu (expansion) | beta1 | 58 / 58 / 58 |
| `role:elder_keeper` | Genzo Kubo (no clan) | elder | B | story-driving | named | none (clanless) | records | beta1 | 38 / 38 / 38 |
| `role:elder_councillor` | Ichiro Senju | elder | B | story-driving | named | senju (great) | ninjutsu | beta1 | 36 / 36 / 36 |
| `role:elder_hyuga` | Sadako Hyuga | elder | B | story-driving | named | hyuga (great) | taijutsu (gentle fist) | beta1 | 37 / 37 / 37 |
| `role:anbu_cat` | Cat (masked) | anbu | B | background | background | masked | kenjutsu | beta1 | 34 / 34 / 34 |
| `role:anbu_hawk` | Hawk (masked) | anbu | B | background | background | masked | sensing | beta2 | 33 / 33 / 33 |
| `role:sensei` | Jun Takeda (no clan) | jonin | A | story-driving | pillar | none (clanless) | ninjutsu | beta1 | 44 / 44 / 44 |
| `role:sensei_2` | Raiden Shiranui | jonin | A | story-driving | pillar | shiranui (minor) | tools (senbon) | beta2 | 43 / 43 / 43 |
| `role:sensei_3` | Akane Yuhi | jonin | B | story-driving | pillar | yuhi (strong) | genjutsu | beta2 | 39 / 39 / 39 |
| `role:sensei_4` | Masaru Morino | jonin | B | story-driving | pillar | morino (minor) | interrogation | beta2 | 37 / 37 / 37 |
| `role:sensei_5` | Benkei Uzumaki | jonin | B | story-driving | pillar | uzumaki (great) | sealing | beta1 | 40 / 40 / 40 |
| `role:teammate_a` | Sora Kurama | academy | E | story-driving | pillar | kurama (strong) | genjutsu (a painter) | beta1 | 5 / 14 / 17 |
| `role:teammate_b` | Riku Ogawa (no clan) | academy | E | story-driving | pillar | none (clanless) | taijutsu, with a stray pup | beta1 | 5 / 14 / 18 |
| `role:rival` | Ryo Uchiha | academy | E | story-driving | pillar | uchiha (great) | ninjutsu (fire) | beta1 | 5 / 16 / 19 |
| `role:classmate_c` | Kanta Kinoshita | academy | E | story-driving | named | kinoshita (minor) | traps and earth | beta1 | 5 / 14 / 17 |
| `role:classmate_d` | Aya Gekko | academy | E | story-driving | named | gekko (strong) | kenjutsu | beta1 | 5 / 15 / 18 |
| `role:squad3_a` | Natsu Nara | academy | E | story-driving | named | nara (strong) | strategy (shadows) | beta1 | 5 / 14 / 18 |
| `role:squad3_b` | Goro Akimichi | academy | E | story-driving | named | akimichi (strong) | taijutsu (expansion); cooks | beta1 | 5 / 14 / 18 |
| `role:squad3_c` | Yusei Yamanaka | academy | E | story-driving | named | yamanaka (strong) | sensing (mind) | beta1 | 5 / 14 / 18 |
| `role:squad4_a` | Rei Hyuga | academy | E | story-driving | named | hyuga (great) | taijutsu (gentle fist, Byakugan) | beta1 | 5 / 15 / 19 |
| `role:squad4_b` | Taiga Inuzuka | academy | E | story-driving | named | inuzuka (strong) | tracking, with a very large ninken | beta1 | 5 / 14 / 17 |
| `role:squad4_c` | Sumire Suzuran | academy | E | story-driving | named | suzuran (minor) | medical (herbs) | beta1 | 5 / 14 / 17 |
| `role:squad5_a` | Haruto Sarutobi | genin | D | story-driving | named | sarutobi (strong) | taijutsu (staff) | beta1 | 12 / 19 / 22 |
| `role:squad5_b` | Kasumi Tobari | genin | D | story-driving | named | tobari (minor) | sensing (night scout) | beta1 | 12 / 19 / 22 |
| `role:squad5_c` | Isamu Kondo (no clan) | genin | D | story-driving | named | none (clanless) | taijutsu (outworks everyone) | beta1 | 13 / 20 / 23 |
| `role:taijutsu_master` | Tora Matsuda (no clan) * | jonin | A | fan-favourite | pillar | none (clanless) | taijutsu | beta1 | 45 / 45 / 45 |
| `role:elite_scout` | Kyo Fujita (no clan) * | jonin | A | fan-favourite | pillar | none (clanless) | kenjutsu | beta2 | 43 / 43 / 43 |
| `role:legend_veteran` | Sanjuro Endo (no clan) * | retired | A | fan-favourite | pillar | none (clanless) | ninjutsu (fire) | beta2 | 44 / 44 / 44 |
| `role:legend_wanderer` | Mugen Aoki (no clan) * | jonin | S | fan-favourite | legend | none (clanless) | ninjutsu | spoken | 55 / 55 / 55 |
| `role:instructor` | Kenta Hayashi (no clan) | chunin | C | story-driving | named | none (clanless) | ninjutsu (teaching) | beta1 | 24 / 24 / 24 |
| `role:instructor_2` | Nobu Umino * | chunin | C | background | named | umino (minor) | tools (throwing) | beta1 | 22 / 22 / 22 |
| `role:instructor_3` | Emi Sakamoto (no clan) * | chunin | C | background | named | none (clanless) | chakra control | beta1 | 20 / 20 / 20 |
| `role:headmaster` | Tatsuo Umino * | retired | B | background | named | umino (minor) | teaching | beta1 | 34 / 34 / 34 |
| `role:proctor_written` | Kiyoshi Morino * | special jonin | B | fan-favourite | named | morino (minor) | interrogation | beta3 | 33 / 33 / 33 |
| `role:proctor_forest` | Anzu Hirano (no clan) * | special jonin | B | fan-favourite | named | none (clanless) | survival | beta3 | 36 / 36 / 36 |
| `role:proctor_finals` | Seiji Gekko * | special jonin | B | fan-favourite | named | gekko (strong) | kenjutsu | beta3 | 34 / 34 / 34 |
| `role:desk_chunin_1` | Kotaro Noguchi (no clan) * | chunin | C | background | named | none (clanless) | administration | beta2 | 19 / 19 / 19 |
| `role:desk_chunin_2` | Mika Namiashi * | chunin | C | background | named | namiashi (minor) | administration | beta2 | 18 / 18 / 18 |
| `role:gate_guard_1` | Tetsuya Hagane * | chunin | C | fan-favourite | named | hagane (minor) | tools (mace) | beta1 | 20 / 20 / 20 |
| `role:gate_guard_2` | Izumi Kikuchi (no clan) * | chunin | C | fan-favourite | named | none (clanless) | taijutsu | beta1 | 19 / 19 / 19 |
| `role:night_watch` | Shizuka Tobari * | chunin | C | fan-favourite | named | tobari (minor) | sensing (sound) | beta1 | 23 / 23 / 23 |
| `role:police_chief` | Kagen Uchiha * | jonin | B | fan-favourite | named | uchiha (great) | ninjutsu (fire) | beta2 | 39 / 39 / 39 |
| `role:police_officer` | Shun Uchiha * | chunin | C | background | background | uchiha (great) | taijutsu | beta2 | 21 / 21 / 21 |
| `role:medic` | Yui Ishikawa (no clan) | chunin | C | story-driving | named | none (clanless) | medical | beta1 | 21 / 21 / 21 |
| `role:hospital_head` | Yomogi Suzuran * | special jonin | B | background | named | suzuran (minor) | medical | beta1 | 35 / 35 / 35 |
| `role:standby_jonin_1` | Daisuke Arai (no clan) * | jonin | B | background | background | none (clanless) | ninjutsu (earth) | beta2 | 33 / 33 / 33 |
| `role:standby_jonin_2` | Mai Kawaguchi (no clan) * | jonin | B | background | background | none (clanless) | ninjutsu (water) | beta2 | 32 / 32 / 32 |
| `role:standby_jonin_3` | Satoru Ueda (no clan) * | jonin | B | background | background | none (clanless) | genjutsu | beta2 | 31 / 31 / 31 |
| `role:clan_head.nara` | Shikou Nara * | jonin | B | fan-favourite | named | nara (strong) | strategy (shadows) | beta2 | 41 / 41 / 41 |
| `role:clan_head.inuzuka` | Hayabusa Inuzuka * | jonin | B | fan-favourite | named | inuzuka (strong) | tracking, with ninken | beta2 | 36 / 36 / 36 |
| `role:clan_head.sarutobi` | Enzo Sarutobi * | jonin | B | background | background | sarutobi (strong) | ninjutsu (fire) | beta2.5 | 35 / 35 / 35 |
| `role:clan_head.aburame` | Mushi Aburame * | jonin | B | background | background | aburame (strong) | tracking (insects) | beta2.5 | 35 / 35 / 35 |
| `role:clan_head.kurama` | Utsuro Kurama * | retired | B | background | background | kurama (strong) | genjutsu | beta2.5 | 30 / 30 / 30 |
| `role:clan_head.shimura` | Gonzo Shimura * | retired | B | background | background | shimura (strong) | ninjutsu (wind) | beta2.5 | 32 / 32 / 32 |
| `role:clan_head.yuhi` | Kaede Yuhi * | jonin | B | background | background | yuhi (strong) | genjutsu | beta2.5 | 34 / 34 / 34 |
| `role:clan_head.gekko` | Tsukiko Gekko * | special jonin | B | background | background | gekko (strong) | kenjutsu | beta2.5 | 33 / 33 / 33 |
| `role:clan_head.shiranui` | Senbei Shiranui * | chunin | C | background | background | shiranui (minor) | tools (senbon) | beta2.5 | 26 / 26 / 26 |
| `role:clan_head.morino` | Takumi Morino * | special jonin | B | background | background | morino (minor) | interrogation | beta2.5 | 32 / 32 / 32 |
| `role:clan_head.umino` | Kazuo Umino * | chunin | C | background | background | umino (minor) | teaching | beta2.5 | 24 / 24 / 24 |
| `role:clan_head.haruno` | Momoe Haruno * | chunin | C | background | background | haruno (minor) | chakra control | beta2.5 | 22 / 22 / 22 |
| `role:clan_head.namiashi` | Hayato Namiashi * | chunin | C | background | background | namiashi (minor) | taijutsu (footwork) | beta2.5 | 23 / 23 / 23 |
| `role:clan_head.hagane` | Kurogane Hagane * | chunin | C | background | background | hagane (minor) | tools (metalwork) | beta2.5 | 22 / 22 / 22 |
| `role:clan_head.kinoshita` | Mokuzo Kinoshita * | retired | C | background | background | kinoshita (minor) | carpentry | beta2.5 | 18 / 18 / 18 |
| `role:clan_head.tsuchigumo` | Iwao Tsuchigumo * | chunin | C | background | background | tsuchigumo (minor) | ninjutsu (earth binding) | beta2.5 | 27 / 27 / 27 |
| `role:clan_head.tobari` | Yoru Tobari * | chunin | C | background | background | tobari (minor) | sensing (sound) | beta2.5 | 26 / 26 / 26 |

**Clan heads.** The heads of the Senju, Uzumaki, Hyuga, Akimichi and Yamanaka wait for the story's
cast. The Uchiha's head is the police chief and the Suzuran's is the head medic. The Hatake, a
near-vanished clan, have no head.

**Civilians in the story:**

| Role | Placeholder name | Slice |
|---|---|---|
| `role:librarian` | Chiyo Nishimura (no clan) | Beta 1 |
| `role:porter` | Bunta Okada (no clan) | Beta 1 |
| `role:residence_clerk` | Rika Tamura (no clan) | Beta 1 |
| `role:merchant` | Gonta Fukuda (no clan) | Beta 2 |

**The squads.** Your year makes four squads of three; the squad a year ahead is the fifth. Each has
a jonin sensei.

| Squad | Sensei | Members |
|---|---|---|
| `squad_1` | `role:sensei` (no clan) | You, `role:teammate_a` (Kurama), `role:teammate_b` (no clan); `role:classmate_c` on the bench |
| `squad_2` | `role:sensei_2` (Shiranui) | `role:rival` (Uchiha), `role:classmate_c` (Kinoshita), `role:classmate_d` (Gekko) |
| `squad_3` | `role:sensei_3` (Yuhi) | `role:squad3_a` (Nara), `role:squad3_b` (Akimichi), `role:squad3_c` (Yamanaka) |
| `squad_4` | `role:sensei_4` (Morino) | `role:squad4_a` (Hyuga), `role:squad4_b` (Inuzuka), `role:squad4_c` (Suzuran) |
| `squad_5`, a year ahead | `role:sensei_5` (Uzumaki) | `role:squad5_a` (Sarutobi), `role:squad5_b` (Tobari), `role:squad5_c` (no clan) |

## 8. Growing up together

Your teammates grow at your pace, so it never feels like you are the strong one and they are not.
So does the whole ensemble: the other squads of your year and the squad a year ahead rank up, learn
techniques and change over time skips in step with the player, some ahead and some behind. The
engine is [`life/roster`](../life/roster) (package `dev.shinobi.life.roster`).

### The model

Each person has their own XP on the player's curve (about 50 minutes a level in the beta, 65 to
112 later), their own techniques and their own niche.

- **Where they belong.** Each person has a place relative to the player, `player + offset`, and an
  offset can move with time (`Peer.offset`). The Classic offsets are the story's:

  | Who | Offset |
  |---|---|
  | The rival | +1 |
  | The Hyuga heir | +0.9 |
  | The loud teammate | −1.2, settling at −0.1 by level 15 (they catch up) |
  | The Inuzuka | −1.5, settling at −0.4 by level 20 |
  | The squad a year ahead | +7.5 to +9 at the Academy, settling at +0.8 to +1.8 by level 30; their clanless prodigy runs strongest |

  A Varied save rolls offsets from clan power (`Peer.rolled`), so a clanless kid can still outpace
  an heir.
- **Shared work.** On a day the group is together, they earn what the player earned on it: the
  same mission XP as the player on shared missions, and the same lesson XP at the Academy. The group
  is the class in the Academy and the squad from team assignment.
- **Days apart.** They train and take missions on their own. They earn the player's recent daily
  pace (a moving average of the player's own XP) times their **drive** (0.95 to 1.15). From team
  assignment the rest of the ensemble is on squads of its own, so every day is a day apart for them.
- **Catch-up and slowdown.** Their gain is scaled by `1 − 0.5 × gap` from where they belong, between
  0.2 and 2.2. Behind, they catch up; ahead, they slow down.
- **The band is a safety net.** No one strays further from where they belong than 1.5 levels for
  teammates, 2 for the rival, 2.5 for the class and 3 for the squad a year ahead.
  - Below the band, they jump back in (`caught_up`: "I trained every day you were away").
  - Above it, they wait (`plateau`).
  - The band is measured from your *best* level, so dying (a level lost) does not drag the squad
    down with you.
- **Better than you in their niche.** In their own field everyone fights `1 + 0.06 × level` levels
  higher: about 2 by the exams, 4 at level 50. A teammate a little behind you overall is still the
  one you want for genjutsu, tracking or a blade.
- **Techniques you see them learn.** Each person has a kit: the Academy three, two niche techniques,
  a nature, a clan technique for the clan-born, the exam reward, then the later arcs. Each technique
  has a minimum level and a moment.
  - The moment is a story beat (`ch12.natures`) or **training the player shares**.
  - A technique whose moment came before they were ready shows at the next beat or training where
    you see them.
  - So does one learned on another squad: you see the rival's new fire at the exams.
  - Nobody learns anything off-screen.
- **Bonds feed growth.** Training or sparring together is worth **+2% per bond level** to both of
  you, +20% at level 10. It is `Roster.trainingBonus`, the same number the Progression mod gives the
  player. A quarrel takes the bonus away.
- **Kindle makes them stronger still** (after the beta).
  - While you kindle an ally's flame, they fight 3 levels higher in their niche, and each kindling
    leaves a little XP with them.
  - A lasting Kindling bond adds to their niche for good: a *blaze* a level, a *flame* half of one
    (the bond engine's tiers: spark, flame, blaze).
- **Time skips** even everyone out halfway toward where they belong.
- **Promotions** set level floors: genin 5, chunin 15, jonin 30. No one falls below their floor,
  and anyone under it is lifted to it. Who is promoted when is the story's call; where it needs to,
  the story reads `Roster.level`.

### The 60 hours, simulated

`./gradlew :life:roster:simulate` plays the main path with the Classic ensemble for three kinds of
player. They are the same three as in the bond simulation ([BONDS.md §15](../BONDS.md#15-pacing)),
and their bond levels are its levels:

- **Devoted:** 30% more XP from side quests; rarely dies.
- **Typical:** 10% more XP from side quests; dies now and then.
- **Reckless:** fails missions, dies often and skips training. One teammate leaves at Ch 12 and a
  classmate steps in.

A player short of a gate grinds until they reach it.

**The typical player, seed 20261029.** Levels are fractional, at each chapter's end. Share is a
teammate's contribution over yours (see below).

| Ch | Hours | You | Teammate A | Teammate B | Rival | Hyuga heir | Inuzuka | Senior prodigy | Share A / B |
|---|---|---|---|---|---|---|---|---|---|
| 7 Graduation | 4.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 13.7 | — |
| 8 Team assignment | 4.9 | 5.8 | 5.5 | 5.4 | 6.9 | 6.8 | 5.6 | 14.5 | 1.02 / 1.00 |
| 11 First C-rank | 8.3 | 10.7 | 10.0 | 9.8 | 11.9 | 11.7 | 10.0 | 17.6 | 0.99 / 0.97 |
| 14 Second C-rank | 12.0 | 15.2 | 14.4 | 14.8 | 16.1 | 15.8 | 14.4 | 20.9 | 0.99 / 0.99 |
| 20 Results | 15.0 | 18.3 | 17.9 | 18.3 | 19.5 | 19.2 | 17.9 | 23.6 | 1.02 / 1.01 |
| Chunin arc end | 28.0 | 29.9 | 29.5 | 29.8 | 30.9 | 30.8 | 29.6 | 32.2 | 1.03 / 0.98 |
| Jonin arc end | 45.0 | 41.4 | 41.0 | 41.5 | 42.6 | 42.5 | 41.3 | 43.2 | 1.03 / 1.01 |
| Road to Hokage end | 60.0 | 50.0 | 48.5 | 48.7 | 50.3 | 49.9 | 48.7 | 51.0 | 1.03 / 1.00 |

**Across five seeds** (`SEEDS` in `Season`). Gaps are against your best level, over every day of the
60 hours:

| Player | Teammates vs you | Rival vs you | Rival ahead | Band stepped in | Share (Genin on) | Beta end: you / A / B / rival |
|---|---|---|---|---|---|---|
| Devoted | −2.1 to +0.5 | −0.4 to +2.0 | 93% of days | never | 0.86 to 1.08 | 21–22 / 21 / 21–22 / 23 |
| Typical | −1.7 to +1.1 | +0.0 to +2.4 | 99% | never | 0.92 to 1.12 | 18 / 17–18 / 18 / 19–20 |
| Reckless | −1.3 to +1.4 | +0.1 to +2.7 | 87% | 0.1% of days | 0.91 to 1.38 | 15–18 / 16–18 / 16–18 / 18–19 |

What it shows:

- **Everyone stays near where they belong.** The pull alone does it: the band never stepped in for
  devoted or typical players, and on 0.1% of days for reckless ones.
- **A devoted player** pulls about a level ahead. The slow-starting teammate trails by two at worst,
  early on.
- **A reckless player who keeps dying is carried for a while.**
  - Their teammates sit up to 1.4 levels above the player's best level, and further above the
    player's current level after a death.
  - Early in Genin life their share reaches 1.4.
  - The stronger squad is the game's comment on how they play.
- **The rival is ahead on 87 to 99% of days**, by about 1.3 levels on average. A devoted player
  passes them now and then.
- **The squad a year ahead** starts eight or nine levels up and is a level or two ahead by the
  Jonin arc.
- **Techniques match:** at the beta's end you have 8 and each teammate 7 or 8.

`SeasonTest` holds all of this on five seeds:

- the band;
- a mean gap under a level;
- the band stepping in on under 2% of days (5% for a reckless player);
- the share;
- the rival's lead.

### Pulling their weight

The target is teammates' damage and utility at **70 to 110% of the player's**.

- **The roster's own first estimate** is `Contribution.share`: `power = level × (1 + 0.04 ×
  techniques)`, and in 35% of fights the fight plays to their niche. For a typical player it gives
  0.92 to 1.12 from team assignment on.
- **The real numbers** come from Shinobi Combat's duel simulator, which runs the level tables above
  with each teammate's kit and returns damage and utility shares.
- **If teammates pull too much**, the lever is their offset (`Roster.CLASS`), not their XP.

### Hooks for the other mods

| Hook | From | Into the roster |
|---|---|---|
| `Day(playerXp, sharedXp, together, bonds)` | Progression: the player's XP, and which of it was shared (lessons, missions, squad training) | Once per in-game day |
| `BondInput(level, trainedTogether, quarrel, kindling)` | Life's glue, from the bond engine: `effectiveLevel(who)`, `bond(who).trainedOn(day)`, `bond(who).conflict().active()`, `Kindling.tier(w, who).id()` (`none`, `spark`, `flame`, `blaze`) | Per person, in `Day.bonds`. The glue depends on both modules; the roster depends on neither |
| `beat(id, present)` | Progression's quests: a story beat, and who was there | Techniques shown at beats |
| `promote(role, floor)` | Progression's ranks (the story decides who) | Level floors |
| `kindle(role)` | Combat's `kindle` effect | The flame's power and its ember |
| `timeSkip()` | Progression's `time_skip` action | Everyone evens out |
| `level(role)`, `tier`, `nicheLevel`, `techniques` | Read by Combat (NPC kits and stats) and the story's level reads | — |
| `squadPower()` | Read by the Mission Desk, which prefers offers near a squad's strength for chunin-led NPC genin (later) | — |

## 9. Data, code and Phase 0

```
python tools/roster/roster.py --check          # roster.json and rank_distribution.json
python tools/roster/roster.py --power          # average levels by rank and clan power
./gradlew :life:roster:test                     # 29 tests
./gradlew :life:roster:simulate                 # the 60-hour growth tables (-Pseed=N, -Pseeds=a,b,c)
./gradlew :life:roster:simulate -Pstretches     # each person's level at each stretch's end, for roster.json
```

**XP units.** `Curve` counts XP in main-path minutes, a stand-in that reproduces the roadmap's hour
budget for each stretch. Progression's `ranks.json` owns the real curve, and Missions pays fixed XP
per mission rank. The roster only needs the same XP the player earns, so in Phase 0 `Curve` reads
`ranks.json`.

**What waits for Phase 0:**

- **Life:** the glue that feeds `Day` from the player's XP and VF's daily cycle, and `BondInput`
  from `BondWorld`.
- **Saves:** saving the roster with the save (`Roster.save()` and `load()`, a line format beside
  the bond engine's).
- **Combat:** NPC stats from tiers and clan power.
- **The population sampler:** reading `rank_distribution.json` for ranks and levels.
  `tools/wardrobe` is shared, so this file is a proposal to its owner.
- **The Konoha build:** markers and workplaces tagged by job.
- **Village:** the tier glyph over residents' heads.
- **Dialogue:** the rank pools for special jonin, elders and retired shinobi.

## 10. Open questions

- **The story's cast.** The provisional posts (marked `*`) are replaced as the story's cast
  arrives: the showcase pillars (the taijutsu master, the returning captain, the old scroll-seller,
  the wandering legend), the proctors, the desk, the gate, the watch, the police, the Academy
  teachers and the clan heads.
- **The tier glyph.** Should it read true two tiers up, or only one?
- **Contribution shares.** Waiting on Combat's duel simulator.
