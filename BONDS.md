# Bonds

The friendship system of the Shinobi Modpack: how everyone in the Leaf feels about you, why, and
what it opens. It grows out of Village Friends' friendship levels and village life
([VILLAGE_LIFE.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/VILLAGE_LIFE.md),
[DEEDS.md](https://github.com/radhepa/Village-Friends-Minecraft-Mod/blob/main/DEEDS.md)) and keeps
their shape: meters computed from real shared history, ten levels on the same thresholds, story
gates, deeds that spread by word of mouth. What it adds is depth: five meters instead of one
score, memories that fade or stay, personalities that take the same act differently, a squad with
its own dynamics, a village that talks, quarrels with arcs, romance and family after the beta, and
Kindling Bond.

Spending time together (hangouts, invitations, rituals, residents' own lives, follow-ups,
conversation topics, and the questions residents ask the player) is in
[LIFE_TOGETHER.md](LIFE_TOGETHER.md).

**No spoilers here.** This file describes systems and formats. Story-specific bond content (who
confides what, whose arc pays off where) belongs in the developers-only
[story bible](docs/story/STORY_BIBLE.md), under each role.

**Where it lives.** The engine is pure Java in [`life/bonds`](life/bonds) (package
`dev.shinobi.life.bond`): no Minecraft, deterministic and seeded, with unit tests and a whole-save
simulation. It belongs to Shinobi Life, which owns player romance and whose friendship and romance
levels are Kindling Bond's bond levels ([ROADMAP.md](ROADMAP.md#the-pack-separate-mods)). Phase 0's
Life mod depends on it (`implementation project(':life:bonds')`) and adds the thin world glue.

| Piece | Code |
|---|---|
| People, personalities, meters | `Person`, `Personality`, `Meter`, `Meters` |
| What can happen, and how it lands | `Act`, `Reaction`, `Memory` |
| One relationship | `Bond` |
| Levels and story gates | `Levels` |
| Quarrels | `Conflict` |
| Romance | `Courtship`; children: `Household` |
| The squad | `Squad` |
| Deeds, gossip, standing | `Deed`, `Gossip`, `Standing` |
| Kindling Bond | `Kindling` |
| The bond book | `BondBook` |
| Clans: joining yours, being invited to one | `Recruitment` |
| Everything together, one day at a time | `BondWorld`, `BondEvent` |
| Quest and dialogue data | `BondConditions`, `BondEffects`, `BondDialogue` |
| Save | `SaveFormat` |
| Seed streams | `Seeds` |
| The village at scale: the social graph, tiers, clans, moods, hooks | `Village`, `SocialTie`, `ClanProfile`, `ClanRelations`, `Mood`, `SocietyHook` |
| Everyone you are close to, as one number | `BondWeb` |

```
./gradlew :life:bonds:test                  # 111 tests
./gradlew :life:bonds:simulate              # the 60-hour pacing tables (-Pseed=N, -Pexplain=role:teammate_a)
./gradlew :life:bonds:simulateVillage       # a village of 300 for 180 days: cost, ties, clan drift, hooks
```

## 1. The data model

**People.** A `Person` is a role (`role:teammate_a`) or a resident id, never a name: the clan (or
none), the district, the rank (civilian, or a ladder index), the age stage (child, teen, adult),
the personality, gender and attraction (VF's `Chemistry` rules), a birthday, family (VF's `kin`
words) and the circles they move in (`class:academy`, `squad:7`, `work:ichiraku`, `household:x`,
`elder:nara`).

**A bond** is one person's feelings toward another, directional: `from` feels this way about `to`.
The player's bonds are residents' feelings toward the player; squadmates also have bonds with each
other. As in VF's `Society`, **only history is stored** and the meters are computed from it:

| Stored | What it is |
|---|---|
| met, contact days | When you met; how many days you have had any contact (a talk, a lesson, a mission) |
| warmth | Small kindnesses: talks, gifts, favors, quest rewards (`add_friendship`) |
| days together | Days spent side by side (VF's `Tie`), at most 60 |
| memories | What happened, when, what it did, how they know it, who it was about |
| experiences | Shared experiences by kind (study, training, meal, spar, mission, camp, festival, date) |
| moments | Real moments: bond quest scenes, a life saved, a secret kept, a reconciliation |
| facts | What they have told you about themselves early (`reveal_fact`) |
| conflict | The quarrel arc's state, severity and timers |
| romance | The courtship stage (teen and up only) |
| level, floor | The level reached (it falls slowly), and a level kept for good (from VF) |
| flags | Per-bond flags for quests and dialogue (`birthday:<year>`, `gated:<n>`) |

**The world** (`BondWorld`) holds the people, every bond, the squad, the deeds the village talks
about, the bond engine's story flags and the player's stage, rank, gender and clan. The glue calls
its verbs as things happen (`talk`, `gift`, `act`, `experience`, `moment`, `deed`, `promote`,
`court`, `apologize`, `reconcile`...) and `endDay()` once a day.

## 2. The meters

Five meters: **affection** (-100 to 100), **trust**, **respect**, **rivalry** and **romance** (0 to
100). Rivalry is not dislike: a rival can respect you without liking you, and still grow close.

```
affection = (5 + 15 chemistry) x (1 - e^(-contact days / 20))   familiarity
          + warmth (at most 15, diminishing)                     talks, gifts, favors
          + 0.15 x days together (at most 60 days)               side by side
          + memories (fading) + the quarrel's weight
trust     = 10 + 10 warmth trait + 5 openness + 0.2 x contact days (at most 15) + memories + quarrel
respect   = 10 + 6 x your seniority - 4 x how far they outrank you (clamped 0..60) + memories
rivalry   = for peers of the same seniority: 15 x pride + 5 x boldness (when positive) + memories
romance   = see Romance (teen and up only)
```

- **Chemistry** (-1 to 1) follows VF's `Chemistry.chemistry`: a stable spark for the pair from the
  save seed (`chemistry` stream), plus shared values (+0.15 each), nearby temperaments (up to +0.2,
  less the further apart their traits are) and a little for the warm. With the player, who has no
  personality, it is the spark plus the resident's warmth and openness.
- **Warmth** gains shrink as warmth nears its cap (`gain x (1 - warmth / 15)`), and warmth cools by
  1% a day after a week without contact. Talk is +1 once a day; gifts are +3.5 loved, +2 liked,
  +0.6 plain (+0.5 for variety), -1 disliked, three a day; a hated gift is a memory instead.
- **Family** start where VF's families do: affection and trust at least 55.
- **Seniority** is the rank ladder (academy 0, genin 1, chunin 2, jonin and ANBU 3, hokage 4);
  civilians count as 0. Respect grows as you rise: a promotion is also a deed everyone hears of.

**Feeling and closeness.** The meters fold into one *feeling*, and levels are read from it:

```
regard    = min(100, max(respect, romance) + 0.2 min(rivalry, respect))
feeling   = 0.45 affection + 0.35 trust + 0.2 regard        (-45 to 100)
closeness = feeling mapped onto VF's 0..200 points scale (straight lines between the thresholds)
```

Closeness keeps VF's ledger, goals and `friendship` numbers meaningful; a friend you like and
trust, a sensei who respects you, a sweetheart and a respectful rival can all be close.

## 3. Levels and story gates

| Level | Feeling | VF points | Name | Opens |
|---|---|---|---|---|
| 0 | 0 | 0 | New Face | |
| 1 | 5 | 5 | Familiar Face | They remember you between visits |
| 2 | 12 | 15 | Acquaintance | Favorite things; their first bond quest |
| 3 | 20 | 28 | Friendly | Village news; sparring |
| 4 | 28 | 40 | Friend | They expect you on their birthday |
| 5 | 36 | 58 | Good Friend | Heart-to-heart talks; their values |
| 6 | 45 | 80 | Close Friend | Their dream; Kindling Bond: Spark |
| 7 | 55 | 105 | Trusted Friend | Secrets; joining your clan; dating (teen and up) |
| 8 | 66 | 140 | Best Friend | Kindling Bond: Flame; a confession (teen and up) |
| 9 | 80 | 170 | Kindred Spirit | A small gift saved for you each day |
| 10 | 95 | 200 | Lifelong Bond | Kindling Bond: Blaze; marriage (adults) |

Each step is wider than the last, so the top levels need every meter near the top. **Gates** stop
points alone (`Levels.cap`), as VF's story gates do:

| To pass | Needs |
|---|---|
| 3 | A shared experience (any kind) |
| 5 | A real moment |
| 7 | Two moments and 15 contact days |
| 8 | Three moments and 35 contact days |
| 9 | Four moments and 60 contact days |

Talk and gifts alone settle at level 3. **Levels rise at once** (right after the act that earned
them, so a level-up can land mid-conversation) and **fall slowly**: only when closeness drops 10
below the level's threshold, one level a day. A level carried over from VF is a floor. The book's
goal line says what is missing: `bond.goal.points:N`, `bond.goal.experience`, `bond.goal.moment`
or `bond.goal.time`.

## 4. Memories

Every act a person lives through becomes a memory with its own effect on their meters
(`Reaction`). **Small and notable memories fade** by half every half-life and are let go below
1/16; **big memories are permanent.** A repeat of a fading act within its half-life folds into the
same memory at half weight and never grows past twice one act (`SATURATION`), so routine keeps a
memory fresh instead of piling up: the hundredth shared mission matters less than the first.
Secondhand news of the same kind folds whoever it was about. A bond keeps at most 64 memories;
past that the weakest fading memory goes first.

**How they know it** sets the weight of secondhand news: lived it 1, saw it 0.6, heard it 0.3,
you told them 0.45 (and telling someone your own bad news yourself softens it and earns 2 trust).
Secondhand news counts more the more they care about whoever it happened to
(`x (0.6 + 0.8 closeness to them)`; family count fully). Romance never travels secondhand.

**The acts** (effects are affection / trust / respect / rivalry before personality; half-life in
days; "kept" is permanent):

| Act | Size | Half-life | Effect | Kind | Honors | Violates | Peeve | Leans |
|---|---|---|---|---|---|---|---|---|
| `talk` | small | — | warmth 1 |  |  |  |  |  |
| `gift_loved` | small | 30 | 1 / 0.5 / 0 / 0; warmth 3.5 |  |  |  |  |  |
| `gift_liked` | small | — | warmth 2 |  |  |  |  |  |
| `gift_plain` | small | — | warmth .6 |  |  |  |  |  |
| `gift_disliked` | small | 20 | -1 / 0 / 0 / 0; warmth -1 |  |  |  |  |  |
| `gift_hated` | small | 30 | -3.5 / -0.5 / 0 / 0 |  |  |  | rudeness |  |
| `favor` | small | — | warmth .8 |  |  |  |  |  |
| `studied_together` | small | 30 | 1 / 0.5 / 0.5 / 0 | study | knowledge |  |  |  |
| `trained_together` | small | 30 | 0.5 / 0.5 / 0.5 / 0.5 | training | strength |  |  | discipline→respect 0.5 |
| `meal_together` | small | 30 | 2 / 0.5 / 0 / 0 | meal | family |  |  |  |
| `spar_won` | small | 40 | -0.5 / 0.5 / 3 / 3.5 | spar | strength |  |  | pride→affection -2, pride→rivalry 3, pride→respect 0.5 |
| `spar_lost` | small | 40 | 1 / 0.5 / 0.5 / 2 | spar |  |  |  | pride→respect -1, warmth→affection 0.5 |
| `mission_together` | notable | 60 | 1.5 / 2.5 / 1 / 0 | mission | duty |  |  |  |
| `camp_night` | notable | 90 | 3 / 2.5 / 0 / 0 | camp |  |  |  | openness→affection 1 |
| `festival_together` | notable | 90 | 3 / 0.5 / 0 / 0, romance 4 | festival |  |  |  | openness→affection 1 |
| `date` | notable | 90 | 2.5 / 1 / 0 / 0, romance 8 | date, romantic |  |  |  |  |
| `bond_moment` | big | kept | 1.5 / 2 / 0.5 / 0 | moment |  |  |  |  |
| `heart_to_heart` | notable | 120 | 2.5 / 3 / 0 / 0 |  |  |  |  | openness→affection 1 |
| `saved_life` | big | kept | 9 / 11 / 5 / 0 | moment, deed 20 | courage, loyalty |  |  |  |
| `saved_by_them` | big | kept | 5 / 3.5 / 0 / 0 | moment |  |  |  | warmth→affection 2 |
| `kept_secret` | big | kept | 2.5 / 8.5 / 1 / 0 | moment | loyalty, honesty |  |  |  |
| `supported_dream` | big | kept | 3.5 / 3 / 2 / 0 | moment |  |  |  |  |
| `reconciled` | big | kept | 2.5 / 3.5 / 0.5 / 0 | moment |  |  |  |  |
| `years_together` | big | kept | 2.5 / 3 / 1 / 0 |  |  |  |  |  |
| `protected_them` | notable | 120 | 2.5 / 5 / 2 / 0 | deed 6 | loyalty, courage |  |  |  |
| `stood_by_them` | notable | 120 | 2 / 3 / 0.5 / 0 |  | loyalty |  |  |  |
| `kept_promise` | notable | 90 | 1 / 4 / 0.5 / 0 |  | honesty |  |  |  |
| `birthday_remembered` | notable | 90 | 3 / 1 / 0 / 0 |  | family |  |  |  |
| `mission_success` | notable | 45 | 0.5 / 1 / 2 / 0 |  | duty |  |  | discipline→respect 0.5 |
| `followed_orders` | small | 45 | 0 / 2 / 0.5 / 0 |  | duty |  |  | discipline→trust 1 |
| `rank_up` | big | kept | 0.5 / 0 / 3.5 / 0 | deed 8 |  |  |  | pride→rivalry 2.5 |
| `helped_resident` | small | 60 | 2 / 2 / 0.5 / 0 | deed 5 | kindness |  |  |  |
| `defended_village` | notable | 120 | 2.5 / 2.5 / 3.5 / 0 | deed 12 | courage, duty |  |  |  |
| `apologized` | small | 30 | 1 / 1 / 0 / 0 |  |  |  |  |  |
| `mediated` | notable | 90 | 2 / 3 / 2 / 0 | deed 4 | kindness |  |  |  |
| `honored_custom` | notable | 90 | 2 / 2 / 1.5 / 0 | deed 4 | family, duty |  |  |  |
| `guest_in_quarter` | small | 60 | 1 / 1 / 0 / 0 | deed 1 |  |  |  |  |
| `reckless_charge` | small | 30 | 0 / -2 / 1 / 0 | professional | courage |  | recklessness | boldness→respect 2, boldness→trust 2 |
| `disobeyed_orders` | notable | 45 | -0.5 / -3.5 / -0.5 / 0 | professional |  | duty | recklessness | boldness→respect 2, discipline→trust -2 |
| `mission_failed` | notable | 30 | -0.5 / -1 / -1 / 0 | professional |  | duty |  |  |
| `bragged` | small | 20 | -1 / 0 / -0.5 / 1 |  |  |  | bragging | pride→rivalry 2 |
| `rude` | small | 20 | -2.5 / -0.5 / 0 / 0 |  |  |  | rudeness | warmth→affection -0.5 |
| `skipped_training` | small | 20 | -0.5 / -0.5 / -1 / 0 | professional |  | duty | laziness |  |
| `pried` | small | 30 | -2 / -2 / 0 / 0 |  |  |  | nosiness | openness→affection 1 |
| `missed_birthday` | notable | 30 | -2.5 / -0.5 / 0 / 0 |  |  | family | neglect |  |
| `felt_overlooked` | small | 30 | -2 / -0.5 / 0 / 1 |  |  |  | neglect | pride→rivalry 2 |
| `broke_promise` | notable | 60 | -2.5 / -6 / -0.5 / 0 |  |  | honesty | lateness |  |
| `went_over_their_head` | notable | 60 | -2 / -5 / 0 / 0.5 |  |  | loyalty |  | discipline→trust 2.5 |
| `sided_against` | notable | 60 | -3 / -3 / 0 / 1 |  |  | loyalty |  |  |
| `insulted_clan` | notable | 60 | -5 / -3 / -1 / 0 | deed -8 |  | family | rudeness |  |
| `failed_client` | notable | 60 | -2 / -3 / -1 / 0 | professional, deed -4 |  | duty |  |  |
| `hurt_resident` | notable | 60 | -7 / -7 / -1 / 0 | deed -15 |  | kindness | cruelty |  |
| `quarrel` | notable | 45 | -6 / -2.5 / 0 / 2 | quarrel, spreads |  |  |  | pride→affection -2 |
| `mocked_dream` | big | kept | -6 / -3.5 / 0 / 2 | quarrel |  |  | rudeness |  |
| `broke_secret` | big | kept | -7 / -18 / -1 / 0 | quarrel |  | loyalty, honesty | dishonesty |  |
| `abandoned_mission` | big | kept | -3.5 / -12 / -6 / 0 | deed -15 |  | duty, loyalty | cowardice |  |
| `left_them_behind` | big | kept | -8.5 / -17 / -3.5 / 0 | quarrel, deed -10 |  | loyalty | cowardice |  |
| `confession_accepted` | big | kept | 3.5 / 2.5 / 0 / 0, romance 15 | moment, romantic |  |  |  |  |
| `proposal_accepted` | big | kept | 3.5 / 3.5 / 0 / 0, romance 10 | moment, romantic |  |  |  |  |
| `wedding` | big | kept | 6 / 6 / 1 / 0, romance 10 | moment, romantic, deed 10 |  |  |  |  |
| `child_born` | big | kept | 6 / 3.5 / 0 / 0, romance 4 | moment, deed 6 |  |  |  |  |

- *Kind*: a shared experience (counted for the gates), a **moment**, a **quarrel** (starts one), a
  **professional** act (costs trust and respect but never starts a quarrel by itself), a
  **romantic** act (refused before the teen stage), and a **deed** with its standing worth (the
  village talks about it).
- Talk, gifts, favors and quest rewards go into warmth, not memories.

## 5. Personality

A `Personality` deepens VF's twelve: five **trait axes** from -1 to 1 (warmth, boldness, pride,
discipline, openness), the **values** they live by, their **pet peeves**, their **dream**, and
their gift tastes. VF's personalities are placed on the axes, plus four for the Leaf's shinobi;
rolled residents get their archetype's axes moved by up to 0.2 and a dream from the catalog
(`Personality.rolled`, from the `residents` or `cast` stream).

| Archetype | Warmth | Bold | Pride | Discipline | Open | Values | Peeves |
|---|---|---|---|---|---|---|---|
| warmhearted | .8 | 0 | -.2 | .1 | .5 | kindness, family | cruelty, neglect |
| thoughtful | .2 | -.2 | 0 | .4 | -.2 | knowledge, honesty | rudeness, bragging |
| playful | .5 | .3 | 0 | -.6 | .6 | freedom, kindness | neglect, laziness |
| adventurous | .3 | .8 | .2 | -.3 | .4 | courage, freedom | cowardice, laziness |
| meticulous | 0 | -.3 | .3 | .8 | -.2 | duty, knowledge | lateness, recklessness |
| steadfast | .3 | .2 | 0 | .5 | 0 | duty, loyalty | lateness, dishonesty |
| reserved | -.2 | -.3 | .1 | .3 | -.8 | freedom, honesty | nosiness, rudeness |
| imaginative | .3 | 0 | 0 | -.4 | .4 | creativity, freedom | rudeness, neglect |
| pragmatic | -.3 | .1 | .2 | .4 | 0 | honesty, duty | laziness, bragging |
| curious | .2 | .4 | 0 | -.1 | .6 | knowledge, freedom | neglect, rudeness |
| protective | .4 | .4 | .2 | .3 | .1 | loyalty, family | recklessness, cruelty |
| gentle | .7 | -.4 | -.5 | .1 | .3 | kindness, family | cruelty, rudeness |
| proud | -.4 | .5 | .9 | .6 | -.6 | strength, family | bragging, nosiness |
| fiery | .6 | .9 | .4 | -.5 | .8 | courage, loyalty | cowardice, neglect |
| shy | .5 | -.7 | -.4 | .2 | -.6 | creativity, kindness | rudeness, nosiness |
| stern | -.1 | .3 | .4 | .9 | -.5 | duty, loyalty | recklessness, lateness |

Values: loyalty, courage, kindness, honesty, duty, freedom, strength, knowledge, family,
creativity. Peeves: lateness, bragging, cowardice, recklessness, dishonesty, rudeness, laziness,
cruelty, nosiness, neglect. Dreams: master their art, protect the village, become Hokage, surpass
a rival, build something lasting, see the world, heal people, be a great teacher, raise a family,
honor their clan, open a shop, find where they belong.

**How an act lands** (`Reaction.react`), starting from the act's effect:

1. each lean adds `amount x trait` (a bold person respects a reckless charge; a disciplined
   sensei trusts a disobeyed order even less);
2. honoring one of their values multiplies the gains by 1.5 and adds 0.5 affection;
3. violating one multiplies the losses by 1.5 and costs 1 more trust;
4. a pet peeve multiplies the losses by 1.4 and costs 2 more affection;
5. lost affection is softened by up to a quarter for the warm and sharpened for the proud.

So beating a proud rival in a spar raises their respect and rivalry and costs a little affection,
while a gentle classmate just likes you a little more for a good match; a reckless charge earns a
bold teammate's respect and costs a careful one's trust; breaking a secret is a betrayal to someone
who lives by loyalty. A dream is a quest hook: `supported_dream` is a permanent moment,
`mocked_dream` a permanent quarrel.

## 6. Shared experiences and moments

Shared experiences count most: the effects of studying, training, meals at Ichiraku, spars,
missions, camp nights and festivals are each larger than a day's talk, they count toward the gates
by kind, and squadmates who share them grow toward each other as well. A **moment** is what the
gates want beyond points: a bond quest's heart scene (`shared_moment`, by quest id), a life saved,
a secret kept, a dream supported, a reconciliation, a confession. The main path's squad bonding arc
(ROADMAP.md, "The squad bonding arc") is a run of moments: the study night, the bell test, the
campfire, the squad dinner, the forest night watch, the finals.

## 7. The squad

- **Cohesion** (0 to 100) is the squad's own number, over every squadmate's feeling toward the
  player and toward each other:
  `0.35 avg trust + 0.35 (avg affection + 100) / 2 + 0.2 min(100, 5 x missions) + 0.1 (100 - avg jealousy) - 12 x quarrels inside the squad`.
  Combat can read it for teamwork bonuses. Who stays together through a time skip is the story's call
  (`timeSkip(days, companions)`); the simulation keeps a squad of cohesion 45 or more together.
- **NPC-to-NPC feelings:** squadmates have bonds with each other, moved by every group experience
  and by jealousy; a quarrel between two teammates costs cohesion.
- **Favoritism and jealousy:** talks (1), gifts (2), and whatever a quest marks with `favor` (a meal
  for two, picking a partner, praise) are attention, which fades by half in a week. A teammate who gets clearly
  less than their share (more than 0.15 under it) grows jealous, by `25 x gap x (1 + 0.5 pride)` a
  day; at 40 they feel overlooked (a memory toward you, and resentment and rivalry toward the
  favorite); at 70 it boils over into a quarrel, not again while that quarrel lasts. An even hand
  lets jealousy fade by 15% a day.
- **Sensei trust** is the sensei's trust meter: orders followed and disobeyed, missions won and
  failed (a dutiful, disciplined sensei feels both more). Quests read it with `bond_meter`.
- **Leaving and coming back:** after a week's grace, a teammate whose bond stays low (the level they
  act on at 1 or less, trust under 10, or a falling-out) for 14 days leaves the squad and stays in
  the village, if a classmate on the bench can take the place; at most one leaves every 14 days.
  The story, or a failed exam, can also remove someone (`remove_from_squad`). Once their bond is
  back at level 4 with no quarrel, a return quest can bring them back (`squad_can_return`, then
  `return_to_squad`; the stand-in steps back to the bench). Story departures return only by the
  story. Squadmates are never killed.

## 8. The village talks

**Communities.** Every resident counts toward a clan (`clan:nara`) or `group:clanless` /
`group:civilian`, a district (`district:market`), a rank (`rank:chunin`, `rank:civilian`) and the
whole `village`. Your **standing** with a community is what its members think of you:

```
deeds    = sum over the deeds they know of: worth x how they know it x fading
opinion  = 40 (1 - e^(-deeds / 40)) for good news (bad news counts in full)  +  2 x their level with you
standing = mean opinion over the community's members
```

Good deeds never fade; bad ones fade by half every 28 days. Titles keep VF's names: **Unwelcome**
(below -8), **Newcomer**, **Helping Hand** (4), **Good Neighbor** (10), **Pillar of the Community**
(20), **Hero** (35). The roadmap's gates read them: founding a clan wants Good Neighbor, Hokage the
highest standing in every district and clan quarter.

**Gossip** (`Gossip.spread`, after VF's `Rumors`). Once a day, everyone who knows a fresh deed
(good: 14 days, bad: 28) may tell each person they share a circle with: chance 0.12, times how
close the circle is (household or family 4, squad or class 3, workplace 2.5, clan 2, district 1.5),
times the deed's size (small 0.5, notable 1), at most 0.9. In a circle of more than 12, each member
talks with a steady seeded sample of about 8 others, like VF's ties. Small deeds travel only through
close circles; big deeds are village news, heard by everyone the next day. About half a district
hears a notable deed within three days and most within six (`GossipTest`). Everyone who learns of a
deed takes it secondhand into their bond with you, so **a teammate may hear of your quarrel before
you tell them** (`tell` then returns false), and someone who hears you saved their child thinks
more of you than a stranger does.

## 9. Quarrels with arcs

```
argument ──next day──► cold shoulder ──(2 + severity/8 days, x pride, x warmth)──► making up ──reconcile──► mended
    │                       │ apology (trust 40, or 3 days): halves it                │
    │                       │                                                          └─ 28 days alone: a mild one blows over,
    └── a third strike, or a betrayal of 60 severity ──► FALLING-OUT (permanent)          a bad one (30+) hardens into a falling-out
```

- **Triggers:** an act marked quarrel, or any personal (not professional) act that costs 14 or more
  at once. Severity is the affection and trust it cost, times `1 + 0.3 pride`.
- **While it lasts:** an argument and making-up lower the level they act on by 1 and let half of
  your warmth through; the cold shoulder lowers it by 2 and lets none through. The quarrel weighs
  on the meters (half its severity in affection, a fifth in trust), easing as it heals.
- **Making up** opens the reconciliation quest (`bond_state: making_up`); `reconcile` ends it and
  leaves a permanent `reconciled` memory: a mended bond is stronger.
- **A falling-out is permanent:** the level they act on stays at 2 or below, Kindling Bond and
  romance close, a teammate leaves, and only the story can mend it (`mend`).

## 10. Romance and family (after the beta)

Foundation only: **nothing romantic happens in the beta.** Romance needs both people to be teens or
both adults (never a child, never across stages), the resident to be romantic and drawn to the
player's gender, not family, and no falling-out. Before that, romantic acts are refused and the
romance meter stays at 0, enforced in code (`CourtshipTest`, and the simulation checks every run).

```
romance = spark x (1 - e^(-days since both were teens / 30)) + romantic memories + 0.4 max(0, affection - 40)
```

The **spark** (0 to 30) is the pair's own, from the `romance` stream and their chemistry; some pairs
never click. **Stages:** interest (romance 15, hidden) → a **crush** (30 and level 6; hidden in the
book until level 8) → **dating** (the player asks, at level 7 and romance 35) → **sweethearts** (a
confession at level 8 and 50; village news) → **engaged** (a proposal between adults at level 10
and 65, after 14 days as sweethearts) → **married** (the wedding at the shrine; a deed). One
commitment at a time. A spouse opens Kindling Bond's Blaze tier.

**Children** (post-game, `Household`): a married adult player can have a child once the post-game
flag is set, at most one a year. The child is a resident of the household (VF already records
parents, households and surnames) whose personality takes after the spouse; their bond starts
where VF's families start.

**Clan invitations:** a clanless player with Pillar standing or better with a clan, and either two
members at level 8 or a clan elder at level 9, is invited to join it.

**Recruiting for your clan:** clanless residents at level 7 or more, not quarrelling, with a free
slot (3 at Chunin, 8 at Jonin, 20 as Hokage), agree with chance
`0.45 + 0.08 (level - 7) + 0.2 loyalty + 0.1 warmth + trust / 400 - 0.2 family ties - 0.15 freedom`,
rolled once a week. Progression's `Recruiting` owns the registry and asks `Recruitment` first.

## 11. Kindling Bond

Kindling Bond is power that flows outward through the people you are bonded to and grows with the
whole web of them; it never copies or borrows techniques (ROADMAP.md, "Kindling Bond"). The bond
engine owns who can be kindled and how strongly (`Kindling`); Shinobi Combat owns what the powers do
and reads `Kindling.Flame` and `Kindling.Bonfire`; the story owns when it awakens
(`story.kindling.awakened`) and when the Bonfire can be lit (`story.kindling.bonfire`).

| Tier | Gate (the level they act on) | Powers |
|---|---|---|
| Spark | 6 | `thread_sight`, `small_kindle` |
| Flame | 8 | and `kindle`, `ember_link` |
| Blaze | 10, or your spouse (from 6) | and `ember_mark`, `unison` |
| Bonfire | the whole web | the ultimate |

- **Flame strength** (0 to 1) per bonded person: `(feeling - 45) / 50` (at least 0.1 once they have
  a tier), times the quarrel's dimming (an argument 0.5, a cold shoulder 0.25, making up 0.6, a
  quarrel left unmended for a month 0.2), plus 0.1 if you fought side by side this week. A
  falling-out snuffs it out (tier none) until the story mends it. Because the tier reads the level
  they act on, a quarrel can also drop a tier.
- **Ember Link** joins the squad members at Flame or above (`Kindling.emberLink`).
- **Resonance** toward a nature: each day you fight beside someone at Spark or above (a mission, a
  spar, training, defending the village, a kindle) counts once; at 30 their trial can teach you
  their nature (`resonance`, `Flame.natureTrialReady`). Every kindle is also counted (`kindling_uses`).
- **Bonfire** (`Kindling.bonfire`): every flame weighted by tier (Spark 1, Flame 2, Blaze 4) times
  its strength, plus half a point for each community the web reaches (a clan, a district, a rank).
  Forms: a **candle** under 5, a **campfire** under 12, a **bonfire** under 21, an **inferno** past
  that. A loner gets a candle; a village of friends, a monstrous fire.
- **Data:** `{"kindling": [who, "flame"]}`, `{"resonance": [who, 30]}`, `{"bonfire": "campfire"}` (or
  a number), `{"kindling_uses": [who, n]}`, `{"bond_web": n}`; the action `{"kindle": who}`.
  Dialogue keys: `bond.kindling.<tier>`, `bond.kindling.dimmed`, `bond.kindling.nature_trial`,
  `bond.bonfire.<form>`.

**In the simulation** (the gift awakens at the second part of the Chunin arc, hour 20.8; players
kindle a squadmate on some missions after that):

| | Devoted | Typical | Reckless |
|---|---|---|---|
| First Spark / Flame | at the awakening (20.8 h) | at the awakening (20.8 h) | Spark at 40 h, no Flame |
| First Blaze | 44 h | 59 h | never |
| Flames at 60 h | 8 | 8 | 2 |
| Nature trials ready | 3 | 3 | 2 |
| Bonfire across five seeds | inferno (about 22 to 24) | bonfire (about 19) | candle (about 2 to 4) |

**Combat reads** (no dependency on this module's internals needed beyond these records):
`Kindling.flames(world)` (brightest first: who, tier, strength, dimmed, resonance, trial ready,
kindles), `Kindling.flame(world, who)`, `Kindling.emberLink(world)`, `Kindling.bonfire(world)` and
`world.kindle(who)` to spend a kindle.

## 12. The bond book

An in-game book (Shinobi Life's client `BondBookScreen`, after VF's Ledger; the screen waits for the
Minecraft integration). `BondBook.page` already builds each page as data, every string a
dialogue-bank key, never a name:

- **Header:** their name token, level and its name, the next level's perk and the goal line.
- **What you know**, revealed as the bond deepens or early by a quest (`reveal_fact`): who they are
  (clan, rank) at 0; favorite things at 2; hobby (their VF personality) at 3; family at 4; values
  at 5; dream at 6; pet peeves at 7.
- **How they feel:** a word for each meter (`bond.feel.affection.fond`, `bond.feel.trust.relies`,
  `bond.feel.respect.admires`, `bond.feel.rivalry.rival`), the quarrel if any, the courtship once
  it is open (a secret crush shows from level 8), and the Kindling tier.
- **Shared memories:** "remembered always" (permanent memories) first, then the six strongest
  fading ones (`bond.memory.<act>`, `.seen`, `.heard`, `.told`), and the shared experiences by kind.
- **An index** of everyone you know, highest level first (`BondWorld.bonded`).

**Gifts received** (`Gifts`, for the home's collection book): every gift a resident gives the
player is kept: the item, who gave it, the day and the occasion (birthday, festival, thanks,
souvenir, wedding, farewell, quest, kindred, new_year). Kindred spirits (level 9, not quarrelling)
leave a small gift about once a week on their own, one of their favorite things. The glue and quests
add the rest (`Gifts.receive`, or the action `{"give_player": {"from", "item", "occasion"}}`). The
home reads `Gifts.received(world)` and `Gifts.from(world, who)`; when a giver sees their gift on
display in the player's home, `Gifts.seenDisplayed(world, giftId)` warms them once per gift
(`saw_gift_displayed`). Condition: `{"gifts_from": [who, n]}`.

**At the player's home** ([docs/HOME.md](docs/HOME.md)): a visit is `visited_home` (a hangout the gates
count). A keepsake or photo on show is noticed once (`Gifts.noticed(world, who, keepsake, photo)`):
a gift from the ledger is marked seen (`saw_gift_displayed`), a photo is `saw_photo_together`, and
either leaves the bond flag `home.noticed:<keepsake>`. A spare key is the bond flag `home.key`, not
a moment, so it can be taken back and does not open a story gate; `{"bond_flag": [who, flag]}` reads
either.

## 13. Data formats

Bond conditions and actions join Core's condition and action language
([ROADMAP.md](ROADMAP.md#conditions-and-actions)). Shinobi Life registers them as `life:<name>`;
quest data may write the bare name. Characters are roles; `role:squad` is the current teammates and
sensei and `role:teammates` the teammates alone. **A role group passes a condition only if every
member does, and an action applies to each member.**

**Conditions:**

```json
{"friendship":       ["role:teammate_a", 5]}          the level they act on, at least
{"bond_meter":       ["role:sensei", "trust", 60]}    a meter, at least
{"bond_memory":      ["role:teammate_b", "kept_secret"]}
{"bond_moment":      ["role:teammate_a", "bond.teammate_a.1"]}
{"bond_state":       ["role:teammate_b", "making_up"]} none, argument, cold_shoulder, making_up, falling_out
{"romance_stage":    ["role:x", "dating"]}            at least this stage
{"kindling":         ["role:teammate_a", "flame"]}    at least this tier: spark, flame, blaze
{"knows_fact":       ["role:rival", "dream"]}
{"squad_cohesion":   60}
{"in_squad":         "role:teammate_b"}
{"squad_can_return": "role:teammate_b"}
{"standing":         ["clan:nara", "good_neighbor"]}  at least this title
{"jealous":          "role:teammate_b"}
{"clan_friendship":  ["nara", 7]}                    someone of the clan at this level
{"clan_relation":    ["inuzuka", "aburame", "rivals"]} at least this label (or a number)
{"village_mood":     ["village", "festive"]}
{"hook_open":        "hook.clan_feud.12"}
{"kindling_uses":    ["role:teammate_a", 12]}
{"bond_web":         40}
{"ritual":           ["role:teammate_b", "ramen"]}   time together (LIFE_TOGETHER.md)
{"hangouts":         ["role:teammate_b", 5]}
{"answered":         ["role:teammate_b", "q.advice.first_mission", "go_for_it"]}   the answer is optional
```

**Actions:**

```json
{"add_friendship":    ["role:teammate_a", 3]}           warmth; "rewards": {"friendship": {"role:squad": 3}} is the same
{"bond_event":        ["role:squad", "camp_night"]}     an act; a group experience also moves squadmates' bonds
{"bond_event":        {"who": "role:teammate_b", "act": "saved_life", "witnesses": ["role:squad"]}}
{"shared_moment":     ["role:teammate_a", "bond.teammate_a.1"]}
{"start_conflict":    ["role:rival", "quarrel"]}
{"apologize": "role:x"}   {"reconcile": "role:x"}   {"mend": "role:x"}
{"reveal_fact":       ["role:rival", "dream"]}
{"romance":           ["role:x", "ask_out"]}            ask_out, confess, propose, wed; {"marry": "role:x"} is wed
{"remove_from_squad": ["role:teammate_b", "story"]}     story, exam, low_bond
{"return_to_squad":   "role:teammate_b"}
{"favor":             ["role:teammate_a", 3]}
{"deed":              {"act": "defended_village", "about": "", "witnesses": ["role:squad"]}}
{"celebrate_birthday": "role:x"}
{"bond_flag":         ["role:x", "met_family"]}
{"kindle":            "role:teammate_a"}                a use of Kindling Bond, counted toward a master's trial
{"resolve_hook":      ["hook.clan_feud.12", "mediated"]}
{"clan_event":        ["inuzuka", "aburame", 10, "festival"]}
{"clan_deed":         {"clan": "hyuga", "act": "honored_custom"}}
{"mood_event":        ["village", 0.4, 0]}              cheer and tension: a festival, an attack
{"ask_question":      ["role:teammate_b", "q.advice.first_mission"]}  a scene asks it now
```

An action returns "" or why it did nothing (`not_ready`, `not_eligible`, `level`...) for the quest
log. The roadmap's quest example works unchanged:

```json
"search": {"objective": {"type": "inspect", "target": "cart_cargo"},
           "branch": [{"if": {"friendship": ["role:teammate_a", 5]}, "next": "campfire"}],
           "next": "report"},
"campfire": {"objective": {"type": "talk", "who": "role:teammate_a", "dialogue": "bond.campfire.a"},
             "on_done": [{"shared_moment": ["role:teammate_a", "bond.teammate_a.campfire"]},
                         {"bond_event": ["role:teammate_a", "heart_to_heart"]}],
             "next": "report"}
```

**Dialogue.** `BondDialogue` names the pools in VF's dialogue bank a resident speaks from, most
specific first, each as `<key>.<archetype>` then `<key>`: a greeting during a quarrel
(`bond.greet.argument`, `.cold_shoulder`, `.making_up`, `.falling_out`), then a fresh missed birthday
(`bond.birthday.missed`), jealousy (`bond.jealous`), the courtship (`bond.romance.<stage>`), then the
level (`bond.greet.level.<n>`). `BondDialogue.news` gives the newest thing they saw or heard about you
and have not yet brought up (`bond.seen.<act>`, `bond.heard.<act>`), once, for the opening line after
VF's own deed reactions. The book adds `bond.fact.*`, `bond.feel.*`, `bond.memory.*`, `bond.goal.*`,
`bond.level.<n>` (the level's name) and `bond.perk.<n>`. A `level_up` event with the player is spoken from
`bond.levelup.<n>` (`BondDialogue.levelUp`). Text uses name tokens only.

**Tuning.** Every number above is a constant in one place (`Levels`, `Bond`, `Act`, `Memory`,
`Conflict`, `Squad`, `Gossip`, `Standing`, `Courtship`, `Kindling`, `Recruitment`). Phase 0 can move
them to a `bonds.json` in the Adventure datapack (`"format": 1`) so a balance pass is a datapack
update, as ROADMAP.md's playtesting section asks.

## 14. Save format and versioning

The engine saves to plain maps, lists, strings, numbers and booleans (`SaveFormat.write`), which the
Life mod wraps in a Codec as a player attachment, `shinobi_life:bonds`. People are not saved there:
the cast and residents come from Shinobi Village on load and bonds attach to them by id; a bond to
someone no longer in the pack is dropped.

```json
{"format": 1, "day": 203, "next_serial": 41, "flags": ["story.kindling.awakened"],
 "player": {"stage": "teen", "rank": 2, "gender": "MALE", "clan": ""},
 "bonds": {"role:teammate_a>player": {
     "met": 1, "last_contact": 202, "contact_days": 140, "together": 60, "warmth": 15.0,
     "talk_day": 202, "gift_day": 200, "gifts_today": 1, "last_gift": "item:brush",
     "level": 9, "floor": 0, "low_days": 0, "romance": "dating", "romance_since": 183, "teen_since": 173,
     "memories": [{"act": "camp_night", "day": 196, "delta": [6.0, 5.0, 0.0, 0.0, 0.0], "source": "self", "about": "", "count": 4}],
     "experiences": {"mission": 61, "camp": 6}, "moments": ["bond.teammate_a.1"], "facts": ["dream"], "flags": [],
     "conflict": {"state": "none", "since": -1, "until": -1, "severity": 0.0, "cause": "", "strikes": 0}}},
 "squad": {"id": "squad:7", "sensei": "role:sensei", "teammates": ["role:teammate_a", "role:teammate_b"], "bench": [],
           "formed": 12, "missions": 80, "attention": {}, "jealousy": {}, "low_days": {}, "overlooked": {}, "departed": {}},
 "deeds": [{"serial": 3, "act": "saved_life", "day": 33, "about": "role:teammate_b",
            "knowers": {"role:sensei": {"how": "seen", "day": 33, "from": ""}}}]}
```

- **The village** is a world attachment, `shinobi_life:village` (`Village.write`/`read`, `"format": 1`):
  the ties, the moved clan relations and marriage bonds, the moods and the open hooks. Clan
  structure is rebuilt from the people on load.
- **Versioning:** every save carries `format`. `SaveFormat.FORMAT` is current; older formats
  migrate on load; a newer one is refused with a clear message instead of being misread.
- **Format 0 is Village Friends' own friendship** (`FriendshipState` points, `BondState` trust and
  level per resident), so a VF world that gains Shinobi Life keeps its friendships: points become
  warmth and contact days, VF trust a permanent memory, and VF's level a floor.
- **Determinism:** the engine draws every roll from the save seed's streams
  (`stream(domain, key)`, as ROADMAP.md defines them): `chemistry` and `romance` (per pair),
  `gossip` (per deed, teller, listener and day), `ties` (who talks with whom in a big circle),
  `recruit` (per resident, clan and week) and `household` (per child). Rolls are stateless hashes,
  so the order things happen in never changes them; the same seed and the same acts give the same
  save (`SaveFormatTest`, `TimeAndPacingTest`).

## 15. Pacing

Targets for the ~60-hour main path (three in-game days to an hour of play, as the roadmap's
slices run). *Typical* is a player who talks to their squad most days, gives a gift now and then,
does most bond quests and keeps their word; *devoted* does everything; *reckless* rarely talks,
breaks a confidence, disobeys and abandons a mission.

| By | Hours | Typical player | Gates in the roadmap |
|---|---|---|---|
| Ch 1 | 0.7 | Everyone met is level 1 | — |
| Academy end (Ch 7) | ~3 to 4 | Classmates 2 to 4: one bond quest each, from level 2 | Beta 1's classmate bond quests |
| Team assignment (Ch 8) | ~4 | Teammates 4 to 6; sensei 3 | The bell test (a moment) |
| First C-rank (Ch 11) | ~7 | **teammate_a 5 or more** | The campfire branch: `friendship [teammate_a, 5]` |
| Beta end (Ch 20) | ~15 | Teammates 6 to 8, sensei 5 to 6, classmates 3 | Bond payoffs in the forest and the finals |
| Chunin arc | ~28 | Teammates 8 to 9; sensei 7; dating possible | Kindling Bond: Spark at 6, Flame at 8 |
| Jonin arc | ~45 | Teammates 9; first level-10 bonds for devoted players | Marriage at 10 (adults) |
| Road to Hokage | ~60 | Two or three bonds at 10, several at 5 to 7 | Hokage: the highest standing everywhere |

**The first 15 hours, from the simulation** (seed 20261029, typical player; the level each person
acts on at the end of each chapter, and squad cohesion):

| Ch | Chapter | Hours | Day | teammate_a | teammate_b | sensei | instructor | classmate_c | classmate_d | rival | Cohesion |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Prologue | 0.3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | — |
| 1 | First morning | 0.7 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | — |
| 2 | First lessons | 1.0 | 4 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | — |
| 3 | Chakra | 1.4 | 6 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | — |
| 4 | Night | 1.8 | 7 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | — |
| 5 | Errands at the Academy | 2.1 | 8 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | — |
| 6 | Exam eve | 2.4 | 10 | 3 | 4 | 1 | 2 | 2 | 2 | 1 | — |
| 7 | Graduation | 2.8 | 12 | 3 | 4 | 1 | 3 | 2 | 2 | 2 | — |
| 8 | Team assignment | 3.7 | 15 | 4 | 6 | 3 | 3 | 2 | 2 | 2 | 42 |
| 9 | The Mission Desk | 5.0 | 19 | 4 | 6 | 4 | 3 | 2 | 2 | 2 | 46 |
| 10 | Tree walking | 6.0 | 22 | 5 | 6 | 4 | 3 | 2 | 2 | 2 | 49 |
| 11 | First C-rank | 7.3 | 26 | 7 | 7 | 5 | 3 | 2 | 3 | 2 | 57 |
| 12 | Water walking and natures | 8.4 | 29 | 7 | 6 | 5 | 3 | 3 | 3 | 2 | 47 |
| 13 | A far village | 9.8 | 32 | 7 | 7 | 5 | 3 | 3 | 3 | 2 | 62 |
| 14 | Second C-rank | 11.3 | 36 | 7 | 9 | 6 | 3 | 3 | 3 | 2 | 70 |
| 16 | Forest of Death | 12.6 | 42 | 8 | 9 | 6 | 3 | 3 | 4 | 2 | 71 |
| 19 | Chunin Exams finals | 14.1 | 50 | 9 | 9 | 6 | 3 | 3 | 4 | 3 | 73 |
| 20 | Results | 14.3 | 51 | 9 | 9 | 6 | 4 | 3 | 4 | 3 | 73 |

With this seed the typical player reaches the Ch 11 campfire talk with teammate_a at level 6. Across
five seeds a typical player reaches it in at least four; one who forgot teammate_a's birthday can fall
a point short, and the scene plays differently, as the roadmap intends. Across the three
players:

| | Devoted | Typical | Reckless |
|---|---|---|---|
| Academy end, teammates | 3 / 5 | 3 / 4 | 2 / 1 (a broken confidence) |
| Ch 11 campfire | plays (7) | plays (6); at least 4 of 5 seeds | skipped |
| Beta end, teammates | 9 / 9 | 9 / 9 | 3 / 3 (one teammate left, replaced) |
| 60 h: bonds at level 10 (with time together) | 3 | 3 | 0 |
| Romance in the beta | none | none | none |
| 60 h: romance | married, a child in the post-game | married | none |
| Kindling with teammates | blaze / blaze | blaze / blaze | spark / spark |
| Quarrels / fallings-out | 0 / 0 | 5 / 0 | 3 / 1 |

Run `./gradlew :life:bonds:simulate` for the full tables, or `-Pexplain=role:teammate_a` to see
where one bond's meters come from. `TimeAndPacingTest` holds these targets on five seeds.

## 16. What stays in Village Friends, and what moves

| Village Friends keeps | Shinobi Life (`life/bonds`) adds | Elsewhere |
|---|---|---|
| Residents' own `Society`: meters between residents, families, resident romance and marriage, births, news, birthdays, the calendar | The player's bonds with the cast and every resident they meet: five meters, memories, personality reactions, levels and gates (replacing VF's player `FriendshipState`/`BondState` scoring through a small VF hook) | **Core:** the condition and action registry, story flags, the seed streams, the player's rank, stage and clan |
| VF's deeds, standing and prices per village (vanilla reputation stays the price engine) | Standing per clan, district and rank, and gossip over the Leaf's circles; the Life glue can feed bond deeds into VF's price term through the same mixin | **Progression:** the squad's roles and missions (it calls `Squad`/`BondWorld`), `remove_from_squad` in quests, the clan registry and `Recruiting` |
| Speech bubbles, the conversation window, VF's ledger, dialogue compiler and talk topics | The bond book's data, the `bond.*` dialogue keys, NPC-to-NPC squad bonds, quarrel arcs, player courtship and children | **Combat:** the `kindle` effect and team cohesion bonuses |
| `GiftPreferences` | Gift tastes from personality (loved, liked, disliked, hated) | **Village:** cast personalities (Classic) and rolled ones (Varied) |

The VF hooks needed (in the spirit of ROADMAP.md's "small public APIs"): a friendship provider
interface so VF's conversation window, ledger and `FriendshipLevels.goal` read the bond engine's
level and goal for a player, and a deed listener so Shinobi Life hears VF's deeds.

## 17. Proposed ROADMAP edits

Applied in the same branch, all format additions:

- **Conditions and actions:** add the bond conditions (`bond_meter`, `bond_memory`, `bond_moment`,
  `bond_state`, `romance_stage`, `kindling`, `knows_fact`, `squad_cohesion`, `in_squad`,
  `squad_can_return`, `standing`, `jealous`) and actions (`bond_event`, `shared_moment`,
  `start_conflict`, `apologize`, `reconcile`, `mend`, `reveal_fact`, `romance`, `return_to_squad`,
  `favor`, `deed`, `celebrate_birthday`, `bond_flag`) beside `friendship` and `add_friendship`;
  define `role:squad` and `role:teammates`; say that `friendship` reads the level they act on.
- **Seed streams:** add `chemistry`, `romance`, `gossip`, `ties`, `recruit` and `household` rows.
- **Friendship and bonds:** point to this file; levels come from the bond engine, not VF's points.
- **Code by mod:** Life's pure core gains the `bond` package (`life/bonds`).
- **Population:** the village's social graph, clan politics and society hooks live in the bond engine
  (section 18); the side-quest generators bind to its hooks (section 19).
- **Your squad and roles:** a teammate leaves after their bond stays low for 14 days, and can come back.

## 18. Village scale

The beta's Leaf has about 200 residents and the full village about 300 (45% civilians, 28% clanless
shinobi, 15% in the 10 minor clans, 13% in the 15 noble clans), in 25 clan quarters and
neighbourhoods and the civilian districts. VF's `Society` keeps a meter for every pair, which suits
a village of 20 to 30; at 300 it would be about 45,000 pairs. The Leaf runs on a **sparse social
graph** instead (`Village`):

- **Real ties** (`SocialTie`), at most 8 chosen ones per resident: family and household, squad and
  class, coworkers, the clan head and two clanmates, three neighbors, then friends, rivals, a
  sweetheart or spouse. A tie works like VF's: a target from chemistry (and, across clans, a little
  of the clans' relation), time known, days together, the last quarrel. When two people are tied
  twice over, the closer kind wins.
- **Everyone else is derived on demand:** `0.3 x their clans' relation + 10 x chemistry + 5 for
  the same district`. Nothing is stored for them.
- **Ties form and change** on each tie's and resident's weekly turn (a seventh of the village a
  day): friends of friends who click become friends; ties that sour become rivals (and shinobi
  peers' rivalries heat up); quarrels happen, likelier in a tense district and between the proud;
  adults fall for each other, become sweethearts and marry after eight weeks, subject to their
  clans' pressure to marry in.

**Simulation tiers.** VF ticks residents' routines once a second; the bond engine's society ticks
once a day:

| Tier | Who | Updated |
|---|---|---|
| Cast | The bound roles | Every day: full bonds, squad dynamics, their ties |
| Known | Residents the player has met | Every day: their bond with the player and their daily ties |
| Background | Everyone else | Once a week, coarsely (a week of days together at once); their opinion of the player (from gossip) once a week |

Meeting someone (`Village.meet`, any talk or shared act) promotes them to known for good.

**Clans as structures** (`Village.House`, `ClanProfile`): the head (the senior adult), elders (three
for the great noble clans, fewer for the rest), an heir (the head's child, else a younger member), a
main and branch house where the clan has one (the Hyuga), and the households of the quarter. Each
clan's upbringing adds its values and nudges its members' traits (the Hyuga dutiful and disciplined,
the Akimichi warm, the Aburame private) and names its customs for quests and dialogue (the Akimichi
share the feast, the Inuzuka respect the pack, the Hyuga bow to the main house). **Intermarriage:**
each clan has a strictness (the Hyuga 0.85, the Uchiha 0.7, the minor clans about 0.1); a match
across clans happens with chance `(1 - strictness A) x (1 - strictness B)`, and a refused one can
raise a `forbidden_match` hook.

**Clan politics** (`ClanRelations`): a symmetric matrix from -100 (feud) to 100 (sworn allies) over
the 25 clans and the clanless and civilian groups. Bases come from old alliances (the Nara, Akimichi
and Yamanaka; the Senju and Uzumaki), rivalries, grudges (the Inuzuka and Aburame), trade ties (the
merchant clans and the civilians) and marriage ties. Events move it; it drifts back 5% of the gap a
week; each marriage between two clans warms their base for good. Clans on bad terms have incidents
(raising tension and `clan_feud` hooks); allies share good days. The player moves it by mediating
feuds, taking sides, honoring or insulting customs (`clan_event`, `clan_deed`).

**Clan standing with the player:** membership and invitations (section 10), honour
(`honored_custom`, an elder's request done), insults (`insulted_clan`, a deed the whole clan hears
of), being a guest in a quarter (`guest_in_quarter`). A **clan-born** player is one of their own: their
clan starts 8 affection and 6 trust warmer, elders bring them requests, and their clan's customs bind
them. A **clanless** player starts even everywhere, earns standing with `group:clanless`, can be
invited into a clan, and learns a lesser technique from any clan where a friend is at level 7
(`clan_friendship`).

**Village-wide dynamics.**

- **Districts and ranks** are communities with their own standing (section 8); respect follows rank.
- **Gossip along ties:** news travels along real ties, by their closeness (spouse and household 4,
  squad 3, friends and coworkers 2.5, clan 2, neighbors 1.5, rivals 0.5), slower across clans on bad
  terms (`x (1 + relation / 200)`), faster when the village is tense or (for good news) cheerful.
  News nobody passes on for three days has died down.
- **Rumors bend** as they spread: each retelling keeps most of the teller's slant, leans the way the
  teller feels about the player (a friend tells it kindly, someone cold tells it worse), and picks up
  a little noise. The listener takes the news moved by its own size times the slant.
- **Moods** (`Mood`): cheer and tension per community (the village, a district, a clan), pushed by
  deeds, incidents and events (`mood_event` for a festival or an attack), easing 10% a day: festive,
  proud, calm, uneasy, tense or grieving. Dialogue reads `village.mood.<label>`.

## 19. Society hooks

The simulation raises tensions, needs and opportunities as **hooks** for the side-quest generators
to bind to (`SocietyHook`). Handcrafted quests stay with the quest engine; a generated quest names a
hook type, fills its slots from the hook's roles, checks `requires`, and ends with `resolve_hook`.

```json
{"format": 1,
 "id": "hook.clan_feud.12",
 "type": "clan_feud",
 "roles": {"clan_a": "inuzuka", "clan_b": "aburame", "a": "resident:41", "b": "resident:87"},
 "place": "village",
 "raised": 84, "expires": 98, "urgency": 0.42,
 "requires": {"all": [{"rank_at_least": "genin"}]},
 "stakes": {"relation": ["inuzuka", "aburame", 10]},
 "outcomes": ["mediated", "sided_a", "sided_b"]}
```

| Type | Raised when | Roles | Lasts | Requires | Outcomes and what they do |
|---|---|---|---|---|---|
| `clan_feud` | An incident between clans on bad terms | `clan_a`, `clan_b`, `a`, `b` | 14 days | Genin | `mediated` (+10 relation, both remember it), `sided_a` / `sided_b` (-6, one stood by, one sided against) |
| `favor_needed` | A known or nearby resident needs a hand | `client` | 7 | — | `done` (a helped deed), `refused` |
| `quarrel_to_mediate` | Two friends quarrel, one of them known | `a`, `b` | until it heals (21) | friendship 3 with either | `mediated` (their quarrel forgiven), `failed` |
| `secret_crush` | An adult falls for another adult | `admirer`, `beloved` | 28 | friendship 6 with the admirer, the player a teen or older | `helped` (sweethearts), `kept_quiet`, `told` (a broken promise) |
| `lost_item` | A known or nearby resident lost something | `owner` | 5 | — | `returned` (a helped deed), `kept` (a hurt one) |
| `newcomer` | Someone settles in the village | `newcomer` | 21 | — | `befriended` (a meal together), `ignored` |
| `elder_request` | An elder of the player's clan, or of one where they are a Helping Hand | `elder`, `clan` | 14 | the clan, or that standing | `done` (the clan hears you honored its custom), `refused` |
| `rivalry_heating` | Two shinobi peers' tie sours into rivalry | `a`, `b` | 14 | friendship 3 with either | `cooled` (friends again), `fanned` (a quarrel) |
| `forbidden_match` | A couple's clans refuse the match | `a`, `b`, `clan_a`, `clan_b` | 28 | the player a teen or older | `supported` (they marry; their clans grumble), `discouraged` |
| `estrangement` | Two relatives stopped speaking four weeks ago (family quarrels are rarer, and keep a 15-point grudge until mended) | `a`, `b` | 42, or until mended | the player a teen or older; friendship 3 with either | `reconciled` (the quarrel mended, both remember it), `failed` |

A `favor_needed` hook says what kind of help in `stakes.variant`, picked from the client's life:
`neighbor`, `lost_pet`, `sick_relative` (they have family), `shop_trouble`, `escort` and `apprentice`
(a working civilian; `apprentice` also for a senior shinobi), `elder_errand` (a clan head or elder,
or a senior adult) and `festival_help` (while the village is cheerful).

At most 16 hooks are open at once and 4 of a type; the same roles never get the same hook twice.
`Village.visibleHooks()` is what the player would come across: someone in it is known, or it is in
their district or clan. Nothing romantic surfaces while the player is a child (the crush hooks wait
for the teen stage), though adults still fall in love in the background.

**The village simulation** (`./gradlew :life:bonds:simulateVillage`, seed 20261029: 301 residents
by `population.json`'s weights plus the cast, 180 days, a player meeting two people a day and
resolving some hooks):

| Measure | Result |
|---|---|
| Cost | about 14 ms a simulated day on average, 32 ms at worst (a day is 20 real minutes); about 1,000 tie and resident updates a day |
| Ties | about 1,800 (family 312, friends 522, neighbors 403, class 264, clan 107, spouses 94, work 85, rivals 26): 6.1 chosen ties per resident, 8 at most |
| Marriages | 9 new in 180 days, 5 of them across clans or groups |
| Clan drift | Inuzuka and Aburame: -17, to a feud (incidents outpaced mediation); others moved a few points (trade warming the civilians and the Hagane) and drifted back |
| Hooks | about 9 a week raised and seen (favors 59, lost items 60, quarrels 64, elder requests 22, clan feuds 10, and after the teen stage estrangements 13 and crushes 6; rivalries 1): about one per in-game day, capped at 16 open |
| Mood | festive at the festival, proud ten days on, calm again after |

`VillageScaleTest` holds the bounds (cost, ties per resident, hooks a week) and determinism.

## 20. What the roadmap asks of bonds

| Roadmap need | Where |
|---|---|
| `friendship` condition, `add_friendship`, rewards to a role or `role:squad`, friendship branches, `kind: bond` quests | Section 13; the roadmap's quest example runs unchanged |
| New meters readable by quest data without code | `bond_meter`, `bond_memory`, `bond_state` and the rest, registered as Core conditions |
| Roles bound to VF residents with personality, family and meters, fixed per save; Varied rolls by personality; names in both | `Person` (role ids, family, personality); rolls from the `cast` stream (`Personality.rolled`, `ClanProfile.shape`) |
| Bond quests (one per classmate in Beta 1, two per teammate in Beta 2, one per teammate in Beta 3), the squad beats, low friendship changing them | Moments by quest id (`shared_moment`), gates (section 3), the beats in the simulation (section 15) |
| Teammates leaving and replaced; choosing who joins missions from Chunin | Section 7; mission companions are Progression's choice, reading `friendship` and `squad_cohesion` |
| Rivals, classmates, sparring with ranked residents raises friendship | `spar_won` / `spar_lost` (respect and rivalry; affection for a good match) |
| Mentors teach at friendship and level thresholds; the sensei's exam recommendation | `friendship` plus Core's `level_at_least`; the recommendation reads `bond_meter [role:sensei, trust, N]` and `friendship [role:sensei, N]` |
| Clanless players learn one lesser technique per friendly clan at friendship 7 | `clan_friendship [clan, 7]` |
| Kindling Bond: Spark at 6, Flame at 8, Blaze at 10 or a spouse, a Bonfire from the whole web; dimmed by quarrels, snuffed by a falling-out; natures learned by resonance and a trial | Section 11 |
| Romance from the teen stage, never children, nothing in the beta, interest from personality and chemistry, dating at 7, confessing at 8 (village news) | Section 10 and `CourtshipTest`; the confession is a deed and village news |
| Marriage: adults, level 10, a proposal and a shrine wedding; the spouse moves in; clan joining | `court(... "propose" / "wed")`; moving in and the clan change are Life's and Core's glue on the `wedding` event |
| Children in the post-game | `Household` (section 10) |
| Joining a clan by invitation (threshold proposed) | Pillar standing with the clan and two members at 8, or an elder at 9 (`Recruitment.invited`) |
| Recruiting for a player clan: clanless, friendship 7+, personality decides; 3 / 8 / 20 | `Recruitment` (section 10) |
| Standing: Good Neighbor to found a clan; the highest standing everywhere for Hokage; prices; dying on a mission costs standing with the client | Section 8; `failed_client` (a deed about the client); prices through VF's reputation hook |
| Residents react to rank, separately from friendship; pet kindness a VF deed | Unchanged (VF and Village); a VF deed can feed the bond engine as a `deed` |

## 21. Open questions

- **The Bonfire's bands** (5 / 12 / 21) are set so a devoted player's web reaches an inferno and a
  typical one a bonfire; the story may want them by bond count instead.
- **Romance and the squad.** Dating a teammate is allowed. Should it change squad dynamics
  (jealousy from the other teammate, cohesion), and what happens to the squad on a break-up?
- **Can a falling-out ever mend outside the story?** Today only a story `mend` does.
- **The cast's genders and attraction** are not in the roadmap; the tests' fixture picks its own.
  Classic needs them curated, Varied rolled.
- **Should levels ever fall below 3** from neglect alone? Today warmth cools after a week apart and a
  level falls only when closeness is 10 below it, so old friends drift but slowly.
- **How visible are the numbers?** The book shows words for each meter; should it show the meters,
  or only words and the level?
- **Hooks a week.** About nine a week (one per in-game day) once the player knows the neighborhood.
  Too many to feel special, or right for a living village? The rates are one constant each.
- **Clan drift.** Feuds can deepen if nobody mediates (the Inuzuka and Aburame slid to rivals in the
  simulation). Should relations have a floor, or can two clans end up in an open feud?
