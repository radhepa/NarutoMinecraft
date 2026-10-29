# Side quests

The side-quest design for the Shinobi Modpack: optional quests that fill the Hidden Leaf with
life, from the Academy to the Hokage's seat. The beta (Academy to Chunin) is detailed; the later
arcs are laid out as foundation. Read with [ROADMAP.md](ROADMAP.md) (systems, data formats,
budget) and [CLANS.md](CLANS.md) (the 25 clans and the population).

**No spoilers here.** This file holds premises (what a player sees), unlocks, structure and
rewards. Solutions, culprits and anything tied to the main story's secrets are in the
developers-only [story bible](docs/story/STORY_BIBLE.md), keyed by quest id. Do not open it if you
want to play unspoiled.

**Ownership.** Relationship dynamics (the social graph of about 300 residents, clan politics,
gossip and the *society hooks* the simulation raises) belong to the bond system (branch `bonds`).
This file owns the quests: authored side quests, filler arcs, clan lines, district quests, and the
templates that turn society hooks into generated quests.

## Contents

| # | Section | Tag |
|---|---|---|
| 1 | [Scope and budget](#1-scope-and-budget) | BUILD (beta) |
| 2 | [Quest framework](#2-quest-framework) | BUILD (beta) |
| 3 | [Society hooks and generated quests](#3-society-hooks-and-generated-quests) | BUILD (beta) |
| 4 | [Clan quest lines](#4-clan-quest-lines) | BUILD (beta) first quests, FOUNDATION (later) the rest |
| 5 | [Civilian and district quests](#5-civilian-and-district-quests) | BUILD (beta) starters, FOUNDATION (later) the rest |
| 6 | [Filler arcs](#6-filler-arcs) | BUILD (beta) three arcs, FOUNDATION (later) the rest |
| 7 | [Inter-clan politics as quests](#7-inter-clan-politics-as-quests) | BUILD (beta) light, FOUNDATION (later) |
| 8 | [Beta catalogue](#8-beta-catalogue) | BUILD (beta) |
| 9 | [Open questions](#9-open-questions) | both |

## 1. Scope and budget

*BUILD (beta).*

A Leaf of about 300 residents in 25 clans is a city, not a hamlet. A village of 20 or 30 people can
live on a notice board; ours needs quests that come from the people: their trades, their families,
their clans and the frictions between them. Side quests are how the player gets to know the
village, and what turns a 60-hour main path into a 100-hour completionist run.

| Stretch | Main path (ROADMAP §1) | Side quests, a thorough player (~70%) | Of which authored | Of which generated | Completionist |
|---|---|---|---|---|---|
| **Beta 1** (opening, Academy) | ~4 h | ~2.5 h | ~2 h | ~0.5 h | ~3 h |
| **Beta 2** (Genin) | ~8 h | ~5.5 h | ~3.5 h | ~2 h | ~8.5 h |
| **Beta 2.5** (clan welcomes, wave 2; content drop played during Genin life) | — | ~1.2 h | ~1.2 h | — | ~1.7 h |
| **Beta 3** (Chunin Exams) | ~3 h | ~1 h | ~0.75 h | ~0.25 h | ~1.3 h |
| **Beta total** | ~15 h | **~10 h** | ~7.5 h | ~2.75 h | **~14.5 h** |
| Chunin | ~13 h | ~9 h | | | |
| Jonin | ~17 h | ~11 h | | | |
| Road to Hokage | ~15 h | ~7 h | | | |
| ANBU branch | +~8 h | ~3 h | | | |
| **Whole game** | ~60 h | **~40 h** | | | |

Side quests sit outside the main-path budget: a player who skips them all still finishes. They pay
XP, so a player who does them reaches level gates earlier and can skip some board missions; side
XP is capped so the beta cannot be out-levelled by more than about two levels (§2.6).

## 2. Quest framework

*BUILD (beta).* Every side quest uses the one quest format of ROADMAP §5 (graph steps, roles,
anchors, conditions and actions, tokens). This section fixes the rules that are specific to side
content.

### 2.1 Kinds

| Kind | What it is | Length | Authored or generated | Example |
|---|---|---|---|---|
| `side` | A standalone story with its own cast | 5 to 20 min | Authored | The old shogi player wants one worthy opponent before the season ends |
| `filler` | An arc of 3 to 6 linked side quests with a finale, anime-filler style | 45 to 120 min | Authored | **The Ramen Thief** |
| `clan` | A clan's quest line: welcome, customs, trust, heart | 4 to 5 quests per clan | Authored | The Inuzuka ask you to walk a pup who will not walk for anyone |
| `bond` | A friendship story with one character, gated by bond level (content here, levels from the bond system) | 5 to 15 min each | Authored | *teammate_a* wants to paint the village from the top of the Rock |
| `event` | Tied to a calendar event or festival; returns yearly with variations | 5 to 30 min | Authored, with rolled variations | Find the Leaf Festival's missing lantern-maker before dusk |
| `district` | A chain rooted in one place and its regulars (a shop, a street, the hospital) | 2 to 5 quests | Authored | The market's price war between two tea houses |
| `generated` | A template bound to a live society hook | 5 to 15 min | Generated | Mediate a quarrel between two neighbours over a fence line |

Board missions (`mission`, D- and C-rank) are the main path's systemic loop, not side quests; the
bond system's own interactions (gifts, chats, dates) are not quests either.

### 2.2 Unlock rules

A side quest's `unlock` is a condition from the shared language, written with a small set of
standard fields so tools and the journal can explain why a quest is or is not available:

```json
{"id": "side.b1.shogi", "kind": "side", "slice": "beta1",
 "unlock": {"all": [
   {"rank_at_least": "academy"}, {"rank_at_most": "chunin"},
   {"at_place": "place:tea_house"},
   {"time_between": ["14:00", "19:00"]}, {"calendar": {"season": ["spring", "summer"]}},
   {"standing": ["district:market", "newcomer"]}
 ]},
 "window": {"expires": "season_end"}}
```

| Gate | Field | Notes |
|---|---|---|
| Rank | `rank_at_least`, `rank_at_most` | Many Academy and Genin quests close once you outgrow them ("too important now to fetch cats") |
| Place | `at_place`, `district` | The quest is offered only in its district; markers show only there |
| Friendship | `friendship`, `bond_meter`, `clan_friendship` | From the bond system |
| Clan | `clan`, `clanless`, `clan_status` | `clan_status` is clanless (the player's only start for now) or member (joined later by marriage or invitation); `born` and `other clan` are reserved for a clan-born start that may return later. (`clan_relation` is the bond system's relation between two clans, used by politics quests) |
| Standing | `standing` | Standing per district or per clan (Newcomer, Helping Hand, Good Neighbor, Pillar, Hero) |
| Events and the village | `event_active`, `flag`, `village_mood`, `hook_open` | Festivals, exams, clan days, story flags; a district's mood; a live society hook |
| Time and season | `time_between`, `calendar` | Night quests, Market Day quests, winter quests |
| Prerequisites | `quest_state` | Chains and arcs |
| Mode | `mode` | Classic-only or Varied-only content, rarely used |
| Age stage | `age_stage` | Romance-adjacent content only from teen, enforced in code |

### 2.3 How quests are found

A city needs more ways in than a notice board. Each quest names one or more `found_by` channels:

| Channel | How it works | Built on |
|---|---|---|
| **Notice boards** | District boards (market, residential, Academy, Mission Desk "favours" tray) carry small requests from residents | VF notice boards (`quest/Postings`, `quest/Board`) |
| **Quest markers** | A resident with a quest shows a small brush-stroke mark over their head when you are close; talking opens it | VF speech bubbles and emotes |
| **Gossip leads** | Residents mention a rumour in conversation; it lands in the journal's *Leads* tab with a place and a person to ask | VF gossip and news, fed by the bond system's gossip |
| **Overheard talk** | Walking past two chatting residents shows a subtitle line; stopping to listen turns it into a lead | VF neighbour chats (`chat_speak` / `chat_listen`) |
| **Clan summons** | A clan messenger knocks on your apartment door in the morning, or leaves a letter in your mailbox | A Shinobi Life mailbox furniture block and a morning visit |
| **Shop counters** | Shopkeepers mention trouble when you buy | VF trades and dialogue |
| **Your building** | Neighbours in your apartment block (Varied rolls which block) knock, leave notes, or need help in the stairwell | The apartment, VF homes |
| **Events** | Festival stalls, exam-week visitors, clan days | The event director |

Clutter rules: at most three active markers per district at a time (closest and oldest first), a
lead expires after seven in-game days if untouched, and the journal's *Leads* tab never holds more
than twelve.

### 2.4 Repeatability

| Kind | Repeat |
|---|---|
| `side`, `filler`, `clan`, `district`, `bond` | Once per save |
| `event` | Once per occurrence (yearly); the variation is rolled from the `events` stream |
| `generated` | Whenever the simulation raises a matching hook (about one visible hook per in-game day; never two for the same roles) |
| Small favours (`gen.favour` from low-urgency hooks) | As the simulation raises them, worth little: the idle loop of village life |

### 2.5 Failure and expiry

- **Authored side quests do not fail by default.** A quest fails only if it says so: a timed
  rescue, a festival that ends, a choice that closes it.
- **Generated quests expire** when their hook resolves without you (the feud cools, the item turns
  up) or after the template's window (usually 3 to 7 days). Expired is not failed: no penalty.
- **Failing** a quest that can fail costs a little friendship with its giver and may escalate its
  hook (an unmediated feud gets worse).
- **Death on a side quest** costs the usual level (ROADMAP §7) but fails the quest only if it is
  marked `fail.on_death`.
- **Rank windows:** a quest whose window closes before you finish it is archived as "missed", never
  failed.

### 2.6 Rewards

| Reward | Bands (beta) | Rules |
|---|---|---|
| Ryo | small favour 10 to 30; side 30 to 150; district step 50 to 200; filler finale 200 to 400; clan quest 50 to 250 | Below a D-rank's pay per minute, so side quests never replace missions as income |
| XP | 5% to 40% of a level | All side XP in the beta adds up to at most about two levels beyond the main path |
| Standing | +1 to +3 favours in the district or clan | Feeds VF's standing titles and the bond system's clan relations |
| Friendship | +1 to +5 with the giver; ± with others involved | Outcomes can cost friendship with the side you did not take |
| Items | Unique furniture, outfit variants, recipes, a pet accessory, keepsakes for the apartment | Every filler finale and clan welcome gives a keepsake: a display item for your home |
| Techniques | Rare: a clan's lesser technique (clan lines), a filler finale's trick | Never a main-path requirement |
| Titles | A line in the journal and in residents' greetings ("the one who caught the ramen thief") | VF deeds and news |

### 2.7 Pacing

- Each slice opens new side content in waves tied to the chapters, so the village always has
  something new: Beta 1 opens its first wave after Ch 1 and a second after Ch 4; Beta 2 opens waves
  after Ch 9, Ch 12 and Ch 14; Beta 3 opens exam-week quests at Ch 15 and the training break.
- The main path pauses for side content at natural breaks: evenings, Market Day, the training
  break (Ch 18).
- A quest's estimated length is in its file; the journal shows it ("about 10 minutes").

### 2.8 Classic and Varied

- **Classic:** a fixed selection and order for every slice; the generated templates still bind to
  live hooks, which come from the seeded simulation, so even Classic is reproducible.
- **Varied:** each slice has **slots** per kind (for example Beta 2: 10 one-off `side` slots). The
  `sidequests` stream fills them from a larger pool without repeats; filler arcs beyond the fixed
  ones are drawn in a rolled order; district chains and clan lines are always present.
- **Roles and names:** every quest character is a role (`role:side.shogi.player`), bound by a query
  ("an elderly civilian on the market street", "an Inuzuka child") at the moment the quest unlocks,
  and resolved with name tokens. Text never contains a name.
- **Clan lines adapt to the population:** a clan line is present whatever the save rolled, because
  its core members are marker-fixed in the clan's seat or neighbourhood.

### 2.9 Density for 300 residents

- **A quest budget per district:** each district may have a fixed number of open side quests and
  generated hooks at once (small districts 2, the market street 5), so the city feels busy but not
  noisy.
- **Who can give quests:** about one resident in five is a potential giver in a given season; the
  bond system's hooks decide who has a problem worth a quest.
- **Spread:** the event director and the hook throttle keep any one clan from dominating the
  journal.

## 3. Society hooks and generated quests

*BUILD (beta).* The bond system raises **society hooks**: tensions, needs and opportunities that
come out of the village simulation (two clans feuding, a newcomer who knows nobody, an elder who
needs a clan custom honoured). A generated quest is a template that binds to a hook, fills its
slots from the hook's roles, and ends by resolving the hook with one of its outcomes, which feeds
back into the simulation. Handcrafted quests stay authored; only templates bind to hooks.

### 3.1 The hook schema

The bond system's schema ([BONDS.md](BONDS.md) §18 and §19, `SocietyHook.java`, `Village.java`). Templates read these fields and nothing else.

```json
{"format": 1,
 "id": "hook.clan_feud.12",
 "type": "clan_feud",
 "roles": {"clan_a": "inuzuka", "clan_b": "aburame", "a": "resident:41", "b": "resident:87"},
 "place": "village",
 "raised": 84, "expires": 98,
 "urgency": 0.42,
 "requires": {"all": [{"rank_at_least": "genin"}]},
 "stakes": {"relation": ["inuzuka", "aburame", 10]},
 "outcomes": ["mediated", "sided_a", "sided_b"]}
```

| Field | Meaning for quests |
|---|---|
| `type` | Which template binds to it (§3.2) |
| `roles` | Residents and clans the template casts into its slots |
| `place` | `village`, `district:<id>`, `clan:<id>` or `rank:<id>`; where the quest is offered, and which district's quest budget it uses |
| `raised`, `expires` | In-game days; an unresolved hook lapses at `expires`, and the quest with it (expired, not failed) |
| `urgency` (0 to 1) | Orders hooks on boards and in dialogue: urgent ones get a quest marker, mild ones only a gossip lead |
| `requires` | Core conditions the player must meet before the quest is offered (rank, friendship, standing, age stage) |
| `stakes` | What the outcome moves (a clan relation and by how much) |
| `outcomes` | The outcome ids the template may pass to `resolve_hook` |

**Which hooks a player meets.** `Village.visibleHooks()` returns the hooks the player comes across:
someone in it is known to them, or it is in their district or clan. In the 300-resident simulation
that is about nine a week, roughly one per in-game day. The simulation keeps at most 16 open hooks,
at most 4 of a type, and never two for the same roles, so the generated loop is steady without
flooding the journal.

**Lifecycle.** The simulation raises a hook → it becomes visible (urgency picks the channel: marker,
board, gossip lead or overheard talk, §2.3) → the player takes the quest, which binds the template
→ the template's last step calls `{"resolve_hook": [hook_id, outcome]}` → the bond system applies
the outcome (relations, deeds, friendship, moods). Ignored, the hook lapses at `expires` and the
simulation moves on.

**Conditions and actions templates use.** Conditions: `hook_open`, plus the bond conditions
`friendship`, `bond_meter`, `standing`, `clan_relation [a, b, label|n]`, `village_mood [community,
label]`, `clan_friendship [clan, level]`. Actions: `resolve_hook`, `clan_event [a, b, delta, why]`,
`clan_deed {clan, act}`, `mood_event [community, cheer, tension]`. Clan relation labels: feud,
rivals, cool, neutral, friendly, allies. Moods: festive, proud, calm, uneasy, tense, grieving.

### 3.2 Templates

Each template is data (`quests/templates/*.json`) shaped like this:

```json
{"format": 1, "id": "gen.mediate_feud", "kind": "generated", "hook": "clan_feud",
 "slots": {"elder_a": "hook:a", "elder_b": "hook:b", "clan_a": "hook:clan_a", "clan_b": "hook:clan_b"},
 "steps": {
   "hear_a": {"objective": {"type": "talk", "who": "slot:elder_a"}, "next": "hear_b"},
   "hear_b": {"objective": {"type": "talk", "who": "slot:elder_b"}, "next": "facts"},
   "facts":  {"objective": {"type": "inspect", "target": "anchor:hook.place"}, "next": "settle"},
   "settle": {"objective": {"type": "choose", "dialogue": "gen.feud.settle",
               "options": {"fair": "mediated", "side_a": "sided_a", "side_b": "sided_b"}},
              "on_done": [{"resolve_hook": ["hook:id", "choice"]}], "next": null}},
 "rewards": {"ryo": 120, "xp": "band:side"}}
```

The hook's `requires` is always ANDed with the template's own unlock, so a template can be stricter
than its hook but never looser. "Feedback" below is what the bond system applies for the outcome,
plus any extra action the template adds.

| Template | Hook type | Roles (slots) | Objectives | Outcomes → feedback | Slice |
|---|---|---|---|---|---|
| `gen.mediate_feud` | `clan_feud` (14 days; Genin) | `clan_a`, `clan_b`, `a`, `b` (a spokesperson of each clan) | Hear both sides, find the facts at the hook's place, bring the spokespeople together, choose a settlement | `mediated` → relation +10; `sided_a` / `sided_b` → relation −6, one clan stood by, the other sided against. The template adds a `mood_event` in the clans' district (cheer if mediated, tension otherwise) | Beta 2 |
| `gen.mediate_quarrel` | `quarrel_to_mediate` (until it heals, 21 days; friendship 3 with either) | `a`, `b` | Hear each, carry a message or an apology, set up a meeting | `mediated` → they are on speaking terms again; `failed` → the quarrel stays | Beta 1 |
| `gen.favour` | `favor_needed` (7 days; none) | `client` | One of eight **variants**, read from the hook's `stakes.variant` (the simulation picks it from the client's life; `SocietyHook.FAVOR_VARIANTS`): `neighbor` (carry, fix, mind the shop), `elder_errand` (fetch, deliver, read a letter aloud; a clan head, elder or senior adult), `lost_pet` (track and return; your ninken helps), `escort` (see a working civilian across the village at night or to the gate), `sick_relative` (fetch medicine or a Suzuran herbalist; only for someone with family), `shop_trouble` (find why stock vanishes, fetch a delivery), `apprentice` (persuade a master to take the client on), `festival_help` (a stall short-handed, a lost child; only while the village mood is cheerful) | `done` → a helped deed with the client; `refused` → nothing | Beta 1 (`neighbor`, `elder_errand`, `lost_pet`); Beta 2 (the rest) |
| `gen.lost_item_gossip` | `lost_item` (5 days; none) | `owner` (gossips and a finder are cast from the owner's ties) | Follow the gossip trail (talk ×2 to 3), find the item, then return it or keep it | `returned` → a helped deed; `kept` → a hurt deed (you keep the item; the owner may hear) | Beta 1 |
| `gen.newcomer_settle` | `newcomer` (21 days; none) | `newcomer` (two neighbours to introduce are cast from the district) | Show them around (go ×3), introduce them, share a meal | `befriended` → a meal together, new ties for the newcomer; `ignored` → they stay alone | Beta 1 |
| `gen.clan_courtesy` | `elder_request` (14 days; the player's clan, or Helping Hand standing with it: the standing route for a clanless player) | `elder`, `clan` | Learn the custom (talk), bring what it asks (collect or craft the clan's gift, attend a clan rite), present it properly (choose the right words) | `done` → the clan hears you honoured its custom (`clan_deed`); `refused` → nothing | Beta 2 |
| `gen.rivalry_cool` | `rivalry_heating` (14 days; friendship 3 with either) | `a`, `b` (two residents, often young shinobi) | Referee their spar at a training ground, talk each down, or spar the hothead yourself, then bring them to shake hands | `cooled` → friends again; `fanned` → a quarrel (which may raise a `quarrel_to_mediate` hook) | Beta 1 |
| `gen.matchmaking` | `secret_crush` (28 days; friendship 6 with the admirer and the player at least teen; adult residents only, never offered while the player is a child) | `admirer`, `beloved` | Learn what the beloved likes, help the admirer prepare, arrange a meeting | `helped` → they become sweethearts; `kept_quiet` → nothing changes; `told` → a broken promise: the beloved knows, the admirer is hurt | **Later** (post-beta) |
| `gen.forbidden_match` | `forbidden_match` (28 days; the player a teen or older; adults) | `a`, `b`, `clan_a`, `clan_b` | Hear the couple, face each clan's objection, decide whether to stand with them | `supported` → they marry and their clans grumble; `discouraged` → they part | **Later** (post-beta) |
| `gen.family_reconcile` | `estrangement` (raised when two relatives' quarrel has lasted 28 days; lasts 42 days or until mended; the player a teen or older and friendship 3 with either) | `a`, `b` (relatives) | Hear each, find what started it (a family story from a third relative), carry a letter, keep the peace at a family dinner (choose) | `reconciled` → the grudge is lifted and the household tie mends; `failed` → the grudge stays | **Later** (post-beta) |

**In the beta:** 7 of the 10 templates (`gen.mediate_feud`, `gen.mediate_quarrel`, `gen.favour` with its
eight variants, `gen.lost_item_gossip`, `gen.newcomer_settle`, `gen.clan_courtesy`,
`gen.rivalry_cool`). Beta 1 runs five of them (the quarrel, three favour variants, lost items, newcomers and
rivalries); the clan feud and clan courtesy wait for Genin rank and clan standing.
Each template has two to four dialogue variants per role personality, so the same template sounds
different from different residents.

**From the bond system:** `favor_needed` hooks carry `stakes.variant`, and the `estrangement` hook
type backs `gen.family_reconcile` after the beta (both on the bond system's branch `bonds-2`).
Family quarrels are rarer than friends' but hold a grudge until reconciled, so the template sees
regular use once the player is a teen.

**Escalation to council.** When a `clan_feud` lapses unresolved and the two clans' relation has
reached the *feud* label, Progression may turn it into a **council case** at the next council day
(§7.3). This is Progression's rule, not a hook type.

## 4. Clan quest lines

*BUILD (beta) for each clan's first quest; FOUNDATION (later) for the rest of each line.*

**Two waves.** The welcome quests ship in two waves to spread the writing load:

- **Wave 1, Beta 2:** the eight great clans with clan seats (ROADMAP §6): Senju, Uzumaki, Uchiha,
  Hyuga, Nara, Akimichi, Yamanaka, Inuzuka.
- **Wave 2, Beta 2.5** (a content-only drop between Beta 2 and Beta 3): the seven smaller noble
  clans (Sarutobi, Aburame, Hatake, Kurama, Shimura, Yuhi, Gekko) and the ten minor clans.
- Wave-2 clans are present from Beta 2 all the same: their quarters, residents, district presence,
  and generated `gen.clan_courtesy` quests. Only their authored welcome quest
  waits for Beta 2.5.

### 4.1 The shape of a clan line

Every clan has a line of four or five quests (`clan.<id>.1` to `.5`) that follows the player's
career and continues after the beta:

| Step | Name | When | What it is |
|---|---|---|---|
| 1 | **Welcome** | Beta 2 (from Ch 12) for the eight great clans; Beta 2.5 for the other 17 | The clan's custom test for an outsider |
| 2 | **Customs** | Beta 3 or early Chunin | Take part in a clan custom or prepare its clan day |
| 3 | **Trust** | Chunin | The clan shows you something of its own: a problem it keeps from outsiders |
| 4 | **Heart** | Jonin | The clan's internal tension comes to a head; your choice settles it |
| 5 | **Legacy** | Road to Hokage (some clans) | The clan stands with you, or does not, when the village needs it |

Finishing step 1 earns the clan's welcome keepsake and opens its lesser technique (for clans with an
ability) at the bond level the roadmap sets; step 3 or 4 is where a clan may invite a clanless
player to join it (ROADMAP §2).

**Who the lines are written for.** The player starts as a clanless orphan (ROADMAP §2), so every
clan line is written for an outsider who earns the clan's regard through standing and friendship:

| Situation | Step 1 | Through the line |
|---|---|---|
| **Clanless** (every player at the start) | The welcome test, plainly: you are an outsider and must earn it | Trust grows with standing and friendship; the line can end in an invitation to join (Heart or Legacy step), or in being a trusted friend of the clan |
| **Joined a clan later** (by marriage or invitation, after the beta) | — | That clan's remaining steps switch to the member version, inside the clan's politics; other clans' lines treat you as a member of your clan, and some steps become diplomacy between the two |

A clan-born start may return later as an option; the quest data keeps a `clan_status` branch for it,
so the lines would only need its homecoming variants written.

### 4.2 Clan relations at the start

The bond system holds the live relation values; these are the starting tones the lines are written
around.

| Clans | Tone at the start |
|---|---|
| Nara, Akimichi, Yamanaka | An old three-clan alliance; their clan days are shared in spirit |
| Inuzuka and Aburame | A friendly, noisy rivalry of dogs and bugs |
| Senju and Uzumaki | Old kin; the Uzumaki memorial stands beside the Senju seat |
| Uchiha and the village | Respected and kept at arm's length; the police quarter is far from the centre |
| Uchiha and Morino | Two kinds of law: police and interrogators argue over jurisdiction |
| Hyuga, within | Main house and branch house: duty and resentment |
| Kurama and Yuhi | Two genjutsu houses, two schools of illusion, a polite rivalry |
| Gekko and Namiashi | Two families of swordsmen; moon blade against wave-foot |
| Shiranui, Namiashi and Hagane | Colleagues of the guard and the gate |
| Sarutobi and Shimura | Two old council families who disagree about everything |
| Haruno and Kinoshita | The market and the builders; the merchants and the carpenters' lane trade daily |
| Suzuran and Yamanaka | Herbs and flowers: allies at the hospital, rivals at the market |
| Tobari and Hagane | The night watch and the gate guard share the wall |
| Tsuchigumo and the Leaf | A mountain shrine clan that lives in the Leaf but keeps its own counsel |
| Hatake and everyone | A house almost empty; everyone respects it, few visit |
| Umino and the Academy | The teachers' family; half the village was taught by an Umino |

### 4.3 The noble clans

#### Senju
- **Culture:** the founders' clan: calm, generous, a long memory. A living tree grows through their
  hall; they tend it like an elder.
- **Customs:** every Senju child plants a sapling at their first clan day; guests are offered tea
  under the tree.
- **Welcome:** help tend the hall's tree through a dry week (water, prune, guard it from a
  storm). `clan.senju.1`
- **Line:** 2 the sapling ceremony at the founders' shrine · 3 a quarrel over whether the old tree
  should be cut to save the hall · 4 the founders' shrine needs a keeper, and two cousins want it.
- **Tensions:** pride in the founders against a clan that has grown small; old kinship with the
  Uzumaki.

#### Uzumaki
- **Culture:** few living members, a memorial shrine with the spiral crest, and the finest sealing
  tradition in the Leaf. Loud, warm, long-lived.
- **Customs:** seals are repainted every spring; the dead are remembered by name.
- **Welcome:** help repaint the seals on the memorial without smudging a single stroke (a precision
  task). `clan.uzumaki.1`
- **Line:** 2 a seal on the memorial is failing and only a fresh hand can renew it · 3 a scattered
  Uzumaki arrives from far away and asks for a home · 4 the clan must choose whether to stay a
  memorial or become a family again.
- **Tensions:** grief against hope; dependence on the Senju.

#### Uchiha
- **Culture:** proud, private, quick to take offence; they run the Military Police from their
  quarter at the village edge.
- **Customs:** the fan crest on everything; a police oath at sixteen; guests do not ask about eyes.
- **Welcome:** a ride-along with a police patrol: settle a market brawl without drawing a blade.
  `clan.uchiha.1`
- **Line:** 2 the police festival parade · 3 a jurisdiction quarrel with the Morino over a
  prisoner · 4 a young Uchiha wants out of the police, and the clan does not let people out.
- **Tensions:** duty against freedom; the village's distance; the Morino.

#### Hyuga
- **Culture:** formal, exact, the Byakugan; the estate is split into the main house and the branch
  house.
- **Customs:** bows of exact depth, tea in silence, sparring as conversation.
- **Welcome:** learn the estate's etiquette well enough to be received by the main house (choices
  that test it), then spar with a branch-house youth. `clan.hyuga.1`
- **Line:** 2 the main-and-branch ceremony · 3 a branch-house youth asks you to carry a petition
  the main house will not read · 4 the two houses' quarrel comes to the clan's elders, and your
  testimony counts.
- **Tensions:** main house against branch house; tradition against fairness.

#### Nara
- **Culture:** lazy-seeming strategists who think ten moves ahead; the deer forest and its herds;
  shogi on every porch.
- **Customs:** the deer are counted each year; antler medicine is a family secret.
- **Welcome:** win (or lose well) a game of shogi against a Nara elder, then help count the deer.
  `clan.nara.1`
- **Line:** 2 the deer count, with a sick herd · 3 poachers in the deer forest · 4 a quarrel over
  selling antler medicine outside the clan.
- **Tensions:** effort against ease; the alliance with the Akimichi and Yamanaka.

#### Akimichi
- **Culture:** big-hearted, big appetites, the kitchen hall; strength is shared like food.
- **Customs:** never refuse the third helping; never call an Akimichi fat.
- **Welcome:** cook and serve a feast with the clan (craft dishes, carry trays, survive the third
  helping). `clan.akimichi.1`
- **Line:** 2 the harvest feast · 3 the barbecue house is struggling and the clan is split on
  saving it · 4 a young Akimichi wants to be a chef, not a ninja.
- **Tensions:** ninja duty against the kitchen; generosity against the clan's purse.

#### Yamanaka
- **Culture:** the flower shop, the sensor corps, and mind techniques; graceful and perceptive.
- **Customs:** the language of flowers; a bouquet always says something.
- **Welcome:** make a bouquet that says the right thing to the right person (choose flowers by
  their meanings). `clan.yamanaka.1`
- **Line:** 2 the flower festival · 3 a rival flower stall (Suzuran herbs) undercuts the shop · 4 a
  Yamanaka sensor heard something in a mind they should not have, and the clan must decide what to
  do with it.
- **Tensions:** privacy against duty; the shop against the corps.

#### Inuzuka
- **Culture:** loud, loyal, wild; every Inuzuka has a ninken; the kennels and clinic by the gate.
- **Customs:** children are paired with a pup on the clan day; a dog's choice is final.
- **Welcome:** walk a pup who will not walk for anyone, until it chooses to follow you.
  `clan.inuzuka.1`
- **Line:** 2 the pup pairing day · 3 a ninken has gone missing near the wall (tracking) · 4 the
  clinic is full and the clan argues over taking in strays from the whole village.
- **Tensions:** the pack against the individual; rivalry with the Aburame.

#### Aburame
- **Culture:** quiet, logical, hidden behind lenses and collars; the insect gardens and hives.
- **Customs:** stand still and let the insects taste your chakra; never swat.
- **Welcome:** stand still in the hive garden while the kikaichu learn your chakra, then help move a
  hive. `clan.aburame.1`
- **Line:** 2 insect night (fireflies over the gardens) · 3 a rare beetle hatches and the Inuzuka's
  dogs keep disturbing it · 4 a young Aburame wants to leave the hives for the open field.
- **Tensions:** silence misread as coldness; the Inuzuka.

#### Sarutobi
- **Culture:** the Will of Fire's own house: warm, devoted to the village, a long staff tradition.
- **Customs:** the lantern walk at New Year; every guest is offered a seat by the hearth.
- **Welcome:** help prepare the lanterns for the Will of Fire walk. `clan.sarutobi.1`
- **Line:** 2 the lantern walk · 3 the clan's staff school needs a challenger to test its heir · 4
  a council quarrel with the Shimura spills into the streets.
- **Tensions:** devotion against burnout; the Shimura.

#### Hatake
- **Culture:** a near-empty house in a quiet lane: one member, or none, depending on the save; the
  ninken still come and go.
- **Customs:** the house's ninken greet whoever is worthy; the memorial stone is visited quietly.
- **Welcome:** the house's old ninken follow you home one day; take care of them and find out who
  they are waiting for. `clan.hatake.1`
- **Line:** 2 a quiet visit to the memorial stone · 3 the house's caretaker asks you to keep it from
  being sold · 4 the house's last keepsake finds its heir.
- **Tensions:** an empty house in a crowded village. *If the save has no Hatake resident, the line
  is carried by the house's caretaker and the ninken.*

#### Kurama
- **Culture:** a refined household of genjutsu painters; studios full of scrolls and screens.
- **Customs:** a portrait is a promise; a painted eye is never finished in public.
- **Welcome:** sit for a portrait, and notice what the painting does that a painting should not.
  `clan.kurama.1`
- **Line:** 2 the painting exhibition · 3 a painting has gone missing and the house will not say
  why it matters · 4 a gifted child's illusions are slipping out of the canvas.
- **Tensions:** gift against control; rivalry with the Yuhi.

#### Shimura
- **Culture:** austere, disciplined, devoted to the village in their own severe way; few words.
- **Customs:** a sealed letter is never opened by its carrier; silence is a courtesy.
- **Welcome:** carry sealed council letters across the village without reading them, while people
  try to make you. `clan.shimura.1`
- **Line:** 2 a council day errand · 3 a Shimura asks for help with a matter they will not explain ·
  4 the clan's old quarrel with the Sarutobi comes to the Hokage.
- **Tensions:** duty against trust; the Sarutobi.

#### Yuhi
- **Culture:** the genjutsu clan of the grove: roses, thorns, crimson eyes, and old trees used for
  training.
- **Customs:** the grove viewing in spring; guests drink tea that may not be tea.
- **Welcome:** a tea ceremony in the grove where nothing is quite what it seems; break the illusion
  politely. `clan.yuhi.1`
- **Line:** 2 the grove viewing · 3 one of the old trees is dying and the clan blames the Kurama's
  studio runoff · 4 a Yuhi wants to marry outside the clan.
- **Tensions:** tradition against love; the Kurama.

#### Gekko
- **Culture:** a quiet family of swordsmen of the Crescent Moon; pale, tired-eyed, polite; the
  moon-viewing platform.
- **Customs:** kenjutsu duels under the full moon; a blade is named, never lent.
- **Welcome:** watch the moonlit kata without moving for its whole length, then carry a blade to the
  smith. `clan.gekko.1`
- **Line:** 2 the moon-viewing duels · 3 a named blade has been lent, against custom, and not
  returned · 4 the Namiashi challenge the Gekko's place in the Hokage's guard.
- **Tensions:** custom against need; the Namiashi.

### 4.4 The minor clans

Minor clans live in mixed neighbourhoods (ROADMAP §6); their lines are shorter (four steps), more
neighbourly, and often intertwined with civilian life.

#### Shiranui
- **Culture:** cool-headed senbon specialists of the Hokage's guard; easy smiles, a senbon in the
  mouth.
- **Welcome:** a senbon-throwing contest by the barracks. `clan.shiranui.1`
- **Line:** 2 a guard rotation goes wrong · 3 a Shiranui is accused of sleeping on watch · 4 guarding
  a visiting dignitary.
- **Tensions:** cool manners hiding hot rivalries with the Namiashi.

#### Morino
- **Culture:** stern interrogators: long greatcoats, barred windows, and surprisingly gentle at home.
- **Welcome:** survive an "interview" without lying (dialogue choices). `clan.morino.1`
- **Line:** 2 a prisoner's family begs for news · 3 the jurisdiction quarrel with the Uchiha police ·
  4 an interrogator doubts a confession.
- **Tensions:** fear from the village against the family's kindness; the Uchiha.

#### Umino
- **Culture:** the teachers' family: brush ponytails, a scar across the nose, patience.
- **Welcome:** help an Umino teacher run a lesson for unruly Academy kids. `clan.umino.1`
- **Line:** 2 the teachers' day · 3 a pupil has stopped coming to class · 4 the Academy wants to
  close a class the Umino believe in.
- **Tensions:** stretched thin by everyone's children.

#### Haruno
- **Culture:** a cheerful merchant household whose children became ninja; cherry-blossom pink and a
  shop on the market street.
- **Welcome:** work a day at the family shop (sell, stock, bargain). `clan.haruno.1`
- **Line:** 2 the shop's anniversary sale · 3 the Haruno child who chose the shop over the Academy ·
  4 a merchants' guild vote.
- **Tensions:** shop against shinobi careers.

#### Namiashi
- **Culture:** quiet swordsmen of the Hokage's guard, the "wave-foot" family; footwork like water.
- **Welcome:** cross the river on the stepping stones in their footwork, without a splash.
  `clan.namiashi.1`
- **Line:** 2 a footwork contest · 3 the rivalry with the Gekko flares · 4 the guard's challenge.
- **Tensions:** the Gekko; the Shiranui.

#### Hagane
- **Culture:** steel-named gate guards and messengers; bandaged noses, maces, endless gossip at the
  gate.
- **Welcome:** run a message relay around the wall before the bell. `clan.hagane.1`
- **Line:** 2 the gate's busiest day · 3 a message was lost on the relay · 4 a gate guard turned
  away the wrong person.
- **Tensions:** the gate's boredom and its sudden emergencies; the Tobari night watch.

#### Kinoshita
- **Culture:** the carpenter family who raised and rebuilt the Leaf's houses; the carpenters' and
  builders' yard; furniture is made here.
- **Welcome:** build a piece of furniture at their workbench and pass a master's eye.
  `clan.kinoshita.1`
- **Line:** 2 raise a roof with the yard · 3 a builders' dispute over a cheap rival crew · 4
  rebuild after a disaster (later arcs).
- **Tensions:** craft against cost; ties to the Haruno market. *Their line unlocks better furniture
  recipes and discounts for your apartment.*

#### Tsuchigumo
- **Culture:** the earth-spider clan of a mountain shrine: shrine cloth, spider crests, shimenawa
  ropes; they guard a forbidden technique and keep to themselves.
- **Welcome:** climb to their shrine at the quarry edge and leave the right offering.
  `clan.tsuchigumo.1`
- **Line:** 2 the shrine's rope renewal · 3 someone has tried to reach the sealed shrine room · 4 the
  clan decides whether to trust the Leaf with what it guards.
- **Tensions:** isolation against belonging.

#### Suzuran
- **Culture:** lily-of-the-valley herbalists and medics; poison-resistant; the herb gardens by the
  hospital.
- **Welcome:** gather herbs with a Suzuran and taste a mild poison they swear is harmless (bring the
  antidote). `clan.suzuran.1`
- **Line:** 2 the hospital's herb shortage · 3 a poisoning in the market that only a Suzuran can
  trace · 4 the clan's antidote formula is wanted by outsiders.
- **Tensions:** healers who brew poison; the Yamanaka flower stall.

#### Tobari
- **Culture:** the night curtain: silent scouts, watchmen and lantern-keepers; shuttered houses,
  mufflers, soft steps.
- **Welcome:** walk the night watch with a Tobari without making a sound (a sneak objective at night,
  which costs fatigue). `clan.tobari.1`
- **Line:** 2 the lantern-keepers' rounds · 3 something moves on the wall at night that the watch
  cannot hear · 4 the night watch is blamed for a breach.
- **Tensions:** unseen work, unthanked; the Hagane gate.

### 4.5 Clan quest counts

| | Beta | Later | Total |
|---|---|---|---|
| Noble clans (15) | 15 (step 1: 8 in Beta 2, 7 in Beta 2.5) | 50 (steps 2 to 5; Legacy for 5 clans) | 65 |
| Minor clans (10) | 10 (step 1, Beta 2.5) | 30 (steps 2 to 4) | 40 |
| **All** | **25** | **80** | **105** |

## 5. Civilian and district quests

*BUILD (beta) for the starters below; FOUNDATION (later) for the rest.* About 45% of the Leaf is
civilian (ROADMAP §6). Their quests show the village's daily life: shops, families and trades. The
civilian cast comes from the two civilian collections: the **market** collection dresses
stallholders, the fishmonger, the grocer, tea-house staff, the tailor, porters and the pawnbroker;
the **household** collection dresses parents, grandparents, homemakers and children.

| District | Regulars | Beta quests | Later |
|---|---|---|---|
| **Your apartment block** | Neighbours across the landing, the landlady, a child upstairs | **The Neighbours** (3): the child upstairs who practises "jutsu" at midnight; the landlady's leaking roof; an old neighbour whose cat only eats fish from one stall. Varied rolls which neighbours you get | New neighbours each year; moving out (a farewell quest) |
| **The Academy** | The janitor, the librarian, Academy kids, an Umino teacher | **The Janitor's Keys**; **Overdue** (overdue library books scattered across the village) | The Academy's anniversary; teaching a class yourself as a Jonin |
| **The shrine** | The priest, worshippers | **A Hundred Wishes**: read the wish plaques and quietly grant small ones (seasonal, a few each season) | Weddings, New Year, the shrine's festival |
| **The market street** | Stallholders, tea-house owners, the tailor, the fishmonger | **The Price War** (4): two tea houses on the same corner undercut each other until the street takes sides | The merchants' guild vote; a night market |
| **Residential streets** | Families, grandparents, children | **Grandmother's Recipe**: an old woman's recipe needs one ingredient nobody sells any more | Weddings, births, moving days |
| **Riverside** | The ferryman, anglers, washerwomen, the fish stall's supplier | **The Ferryman's Last Season** (3): the ferryman wants one more good season before the new bridge opens | The bridge's opening |
| **The hospital** | Medics, patients, Suzuran herbalists | **Night Shift** (3): cover a night at the hospital (fatigue matters), with three patients who each need something | Running supplies in wartime |
| **The gate and the wall** | Hagane gate guards, Tobari watchmen, travellers | **Contraband Cabbages** (2): a farmer's cart is stuck at the gate over paperwork, and the cabbages are not getting fresher | The travel desk to far regions |
| **The training grounds** | Young shinobi, a groundskeeper | **The Unbeatable Post**: a training post nobody has ever knocked over | Tournaments |
| **The bath house** | The bath keeper, regulars | **Lost and Found**: return three lost things to their owners from clues | Bath-house gossip as a lead source |
| **The carpenters' lane** | The Kinoshita yard, apprentices | Through the Kinoshita line (§4.4) | Rebuilding after the later arcs |

District quests count toward the district's standing (VF's titles per district), which unlocks small
perks: a regular's discount, a seat saved at the tea house, a neighbour who feeds your pet.

## 6. Filler arcs

*BUILD (beta) for the first three (and a fourth for Varied pools); FOUNDATION (later) for the rest.*
Filler arcs are anime-filler style: self-contained, a little silly or a little spooky, with a cast
of their own and a finale. Premises only; the answers are in the story bible.

### In the beta

| Arc | Parts | Opens | Premise (what the player sees) | Finale reward |
|---|---|---|---|---|
| **The Ramen Thief** (`filler.ramen_thief`) | 3 | Beta 1, after Ch 4 | Someone keeps eating Ichiraku's stock at night, and the cook has a list of suspects that includes half the Academy | Free ramen for a season; the cook's keepsake (a framed ladle) |
| **Lanterns on the Lake** (`filler.lake_lanterns`) | 4 | Beta 2, after Ch 12 | A ghost light drifts over the training lake at night, and the anglers will not fish there any more | A lantern keepsake; a water-walking trick |
| **Dogs and Bugs** (`filler.dogs_and_bugs`) | 3 | Beta 2, after Ch 9 | A prize Aburame beetle has vanished, an Inuzuka dog is the prime suspect, and the two clans are not speaking | Both clans' standing; a joint keepsake; a step toward the Inuzuka and Aburame lines |
| **The Silent Bell** (`filler.silent_bell`) | 3 | Beta 2 (Varied pool) | The shrine's bell has stopped ringing, and the priest says it has never been silent in a hundred years | The shrine's charm (a small luck buff) |

Classic saves get The Ramen Thief, Lanterns on the Lake and Dogs and Bugs. Varied saves always get
The Ramen Thief and draw two of the other three in a rolled order.

### Later (foundation)

| Arc | Parts | Stretch | Premise |
|---|---|---|---|
| **A Hundred Masks** | 5 | Chunin | At the masked festival, someone is wearing your face |
| **Snowbound** | 4 | Chunin (winter) | A blizzard strands your squad at a waystation with travellers who all have something to hide |
| **The Rival Ramen Stand** | 4 | Chunin | A new ramen stand opens across from Ichiraku, and the street must choose |
| **The Puppet Theatre** | 5 | Jonin | A travelling puppet theatre's puppets keep turning up in places they could not have walked to |
| **The Forger's Ink** | 4 | Jonin | Forged mission scrolls are appearing on the Mission Desk |
| **The Tea Caravan** | 4 | Jonin | A daimyo's tea caravan vanished on a road your team cleared last month |
| **The Cat Who Knew Too Much** | 3 | ANBU branch | A cat keeps turning up at the scenes of things nobody should have seen |
| **The Last Summer** | 5 | Road to Hokage | Your old classmates plan one last summer trip before everything changes |
| **The Statue Thief** | 3 | Road to Hokage | The Hokage statues' heads keep disappearing overnight |

### Later one-offs (foundation)

Standalone `side` quests for the later stretches. Premises only; the answers are in the story bible.

| Id | Stretch | Premise |
|---|---|---|
| `side.c.returned_book` | Chunin | A library book keeps being returned on days the library is closed |
| `side.c.court_roll` | Chunin | A clerk from the daimyo's court is stuck in the village with a damaged guest roll |
| `side.c.sensor_shadow` | Chunin | The young sensor assigned to you would like, very much, to have a single day off |
| `side.c.third_time` | Chunin | A loud Genin and his enormous dog are taking the Chunin Exams for the third time |
| `side.j.roots` | Jonin | Families come asking the archive where they came from |

## 7. Inter-clan politics as quests

*BUILD (beta) light; FOUNDATION (later) in full.* The bond system keeps live relations between
clans; quests are how the player moves them.

### 7.1 What moves clan relations

| Source | Effect |
|---|---|
| Clan quest outcomes | Each clan line step can move its clan's relation with others (a Hyuga petition carried or refused) |
| Mediation | `gen.mediate_feud` and authored disputes: a fair settlement warms both sides, a favoured one shifts them |
| Witnessed deeds | Helping one clan's people in sight of another's (VF deeds and witnesses) |
| Gifts and courtesy | `gen.clan_courtesy`; bringing the right gift on a clan day |
| Membership and marriage | Joining a clan or marrying into one ties your standing to it, and its rivals notice (later) |
| Founding your own clan | Your clan enters the web with its own relations (later) |

### 7.2 What clan relations do

| Relation (the bond system's labels) | Village effect | Quest effect |
|---|---|---|
| Allies | Shared training, joint festivals, intermarriage | Joint quests; a clan vouches for you to another |
| Friendly | Trade discounts between their shops | Easier welcome tests |
| Neutral | — | — |
| Cool | Members avoid each other's streets; prices rise | Some clan quests ask you to pick a side |
| Rivals | Open competition, scuffles at training grounds | More `clan_feud` hooks between them |
| Feud | Closed shops, district tension (`village_mood` uneasy or tense) | A lapsed `clan_feud` can become a council case (§3.2, §7.3) |

Politics quests move relations with the bond system's actions: `resolve_hook` on a `clan_feud`
(+10 mediated, −6 sided), and `clan_event [a, b, delta, why]` from authored clan steps and council
outcomes.

### 7.3 Council days and disputes

- **Council day:** the first Moonday of each season, the Hokage hears petitions in the Residence (an
  event). Severity-5 hooks and clan disputes come here as **council cases**.
- **The player's part grows with rank:** as a Genin you watch from the gallery (beta); as a Chunin
  you can testify; as a Jonin you can speak for a clan or mediate; as Hokage you decide.
- **In the beta:** one council day during Genin life (`event.b2.council_day`, after Ch 12). The
  player watches from the gallery: two clans bring a dispute, the Hokage rules, and the scene
  introduces clan relations (the Ledger's clan page opens). **No choice is offered**; it is a
  scene with a few gossip leads afterwards. Testifying starts at Chunin.
- **Outcomes** move clan relations, standing and the village news, and some cases open quests (a
  ruling to enforce, a compromise to broker).

### 7.4 Festivals and ceremonies

Clan days (ROADMAP §11) and village festivals are where politics shows: who sits beside whom at the
Leaf Festival, which clans share a stall, who is missing from a ceremony. Event quests use the live
relations to pick their cast and their trouble (a feuding pair assigned neighbouring stalls).

### 7.5 In the beta

The beta keeps politics light: relations are visible (the Ledger and gossip), **Dogs and Bugs** is
the beta's inter-clan arc, `gen.mediate_feud` and `gen.clan_courtesy` run on live hooks, clan
welcome quests nudge relations, and one council day in Beta 2 is watched from the gallery with no
choice offered.

## 8. Beta catalogue

*BUILD (beta).* Every authored beta side quest. Rewards: R ryo, X XP (as a share of a level), S
standing, F friendship, K keepsake or item, T technique. Generated quests (7 templates, §3.2) come
on top.

### Beta 1: the opening and the Academy

| Id | Kind | Unlock | Premise | Rewards |
|---|---|---|---|---|
| `side.b1.shogi` | side | After Ch 1; market tea house, afternoons | The old shogi player wants one worthy opponent before the season ends | R 60, X 15%, K shogi board |
| `side.b1.academy_cat` | side | After Ch 1; Academy | The Academy cat is stuck somewhere new every day | R 30, X 10%, F |
| `side.b1.flower_delivery` | side | After Ch 2; flower shop | The flower shop's delivery runner is sick, and every bouquet says something | R 40, X 10%, S Yamanaka |
| `side.b1.sparring_partner` | side | After Ch 2; weapon shop | The weapon shop's apprentice needs a practice partner who will not quit | X 15%, K a better practice kunai |
| `district.b1.neighbours.1` | district | After Ch 1; your building, night | The child upstairs practises "jutsu" at midnight | F, S block |
| `district.b1.neighbours.2` | district | After Ch 2; your building, rain | The landlady's roof leaks over your neighbour's bed | R 40, F |
| `district.b1.neighbours.3` | district | After Ch 4; your building | An old neighbour's cat only eats fish from one stall, and the stall has closed | R 30, F, K cat figurine |
| `district.b1.academy.keys` | district | After Ch 2; Academy | The janitor has lost the keys to every door in the Academy | X 10%, F |
| `district.b1.academy.overdue` | district | After Ch 5; Academy library | Overdue library books are scattered all over the village | R 50, X 15% |
| `district.b1.shrine.wishes` | district | After Ch 1; shrine (seasonal) | Read the wish plaques and quietly grant small wishes | X 5% each, S shrine |
| `filler.ramen_thief.1` | filler | After Ch 4; Ichiraku, evening | The cook's stock vanishes at night; draw up a list of suspects | R 50 |
| `filler.ramen_thief.2` | filler | After part 1 | Stake out the stand, at night (fatigue counts) | X 20% |
| `filler.ramen_thief.3` | filler | After part 2 | Catch the thief | R 200, K framed ladle, free ramen for a season |
| `bond.b1.classmate_a` | bond | After Ch 2; bond level 3 with *teammate_a* | *teammate_a* wants to paint the village from somewhere high | F, K painting |
| `bond.b1.classmate_b` | bond | After Ch 2; bond level 3 with *teammate_b* | *teammate_b*'s stray pup has run off again | F |
| `bond.b1.classmate_c` | bond | After Ch 3; bond level 3 with *classmate_c* | *classmate_c* wants help with a gift for a parent | F |
| `bond.b1.classmate_d` | bond | After Ch 3; bond level 3 with *classmate_d* | *classmate_d* practises a kata alone every dawn and wants a witness | F |

**Beta 1: 17 quests** (4 side, 6 district, 3 filler, 4 bond).

### Beta 2: Genin life

| Id | Kind | Unlock | Premise | Rewards |
|---|---|---|---|---|
| `side.b2.tea_master` | side | After Ch 9; tea house | A tea master will only serve you if you can taste where the leaves grew | R 60, X 10%, K tea set |
| `side.b2.lost_letters` | side | After Ch 9; post office | A bag of undelivered letters from years ago turns up | R 80, X 15%, S residential |
| `side.b2.stage_fright` | side | After Ch 10; residential | A young storyteller freezes before every audience | X 10%, F |
| `side.b2.ninja_cart` | side | After Ch 10; market | A street vendor's cart keeps rolling away downhill | R 40, X 10% |
| `side.b2.rooftop_race` | side | After Ch 10 (tree walking); rooftops | Genin race across the rooftops every Market Day | X 15%, K race ribbon |
| `side.b2.forge_apprentice` | side | After Ch 12; forge | The smith's apprentice cracked a blade and is afraid to say so | X 15%, a recipe |
| `side.b2.pawned_scroll` | side | After Ch 12; pawn shop | A scroll at the pawn shop looks too good to be real | R 100, X 15% |
| `side.b2.fishing_bet` | side | After Ch 12; riverside | Two anglers bet on who lands the river's biggest fish | R 60, X 10% |
| `district.b2.grandmothers_recipe` | district | After Ch 9; residential | An old woman's recipe needs one ingredient nobody sells any more | R 50, X 10%, a recipe |
| `event.b2.festival_child` | event | Leaf Festival | A child is lost in the festival crowd, and only remembers a smell | S, F |
| `event.b2.lantern_maker` | event | Leaf Festival | The lantern-maker has not shown up, and dusk is coming | R 100, S |
| `district.b2.price_war.1` to `.4` | district | After Ch 9; market | Two tea houses undercut each other until the whole street takes sides (4 parts) | R 250 total, S market, K |
| `district.b2.ferryman.1` to `.3` | district | After Ch 11; riverside | The ferryman wants one more good season before the new bridge opens (3 parts) | R 200 total, K ferry lantern |
| `district.b2.night_shift.1` to `.3` | district | After Ch 12; hospital, night | Cover a night at the hospital, with three patients who each need something (3 parts) | X 40% total, S hospital, F |
| `district.b2.contraband.1` to `.2` | district | After Ch 11; gate | A farmer's cart is stuck at the gate over paperwork (2 parts) | R 80, S Hagane |
| `district.b2.unbeatable_post` | district | After Ch 10; training ground | A training post nobody has ever knocked over | X 20%, K |
| `district.b2.lost_and_found` | district | After Ch 9; bath house | Return three lost things from the bath house to their owners | R 60, F |
| `filler.lake_lanterns.1` to `.4` | filler | After Ch 12 | A ghost light drifts over the training lake at night (4 parts) | R 300 total, K, T water-walking trick |
| `filler.dogs_and_bugs.1` to `.3` | filler | After Ch 9 | A prize Aburame beetle has vanished; an Inuzuka dog is the prime suspect (3 parts) | R 250 total, S both clans, K |
| `bond.b2.teammate_a.1`, `.2` | bond | Bond levels 4 and 5 with *teammate_a* | Two stories with *teammate_a* | F, K |
| `bond.b2.teammate_b.1`, `.2` | bond | Bond levels 4 and 5 with *teammate_b* | Two stories with *teammate_b* | F, K |
| `event.b2.council_day` | event | After Ch 12; the Hokage Residence, the first Moonday of the season | Two clans bring a dispute to the Hokage; you watch from the gallery (no choice) | X 5%, the Ledger's clan page, leads |
| `clan.<id>.1` (8, wave 1) | clan | After Ch 12 | The welcome of each great clan: Senju, Uzumaki, Uchiha, Hyuga, Nara, Akimichi, Yamanaka, Inuzuka (§4) | R 50 to 150, S clan, K clan keepsake, T lesser technique where the clan has one |

**Beta 2: 45 quests** (8 side, 15 district in 4 chains of 12 quests and 3 singles, 3 event, 7
filler, 4 bond, 8 clan).

### Beta 2.5: clan welcomes, wave 2

A content-only drop between Beta 2 and Beta 3 (data, dialogue and small builds; no new systems).

| Id | Kind | Unlock | Premise | Rewards |
|---|---|---|---|---|
| `clan.<id>.1` (7 noble) | clan | Genin, after Ch 12 | The welcome of Sarutobi, Aburame, Hatake, Kurama, Shimura, Yuhi and Gekko (§4.3) | R 50 to 150, S clan, K clan keepsake, T lesser technique where the clan has one |
| `clan.<id>.1` (10 minor) | clan | Genin, after Ch 12 | The welcome of Shiranui, Morino, Umino, Haruno, Namiashi, Hagane, Kinoshita, Tsuchigumo, Suzuran and Tobari (§4.4) | R 50 to 120, S clan, K clan keepsake, T for Tsuchigumo, Suzuran and Tobari |

**Beta 2.5: 17 quests**, all clan welcomes.

### Beta 3: the Chunin Exams

| Id | Kind | Unlock | Premise | Rewards |
|---|---|---|---|---|
| `side.b3.lost_genin` | side | Ch 15 onward | A foreign Genin is lost in the village the night before the exam | F, S |
| `side.b3.stall_thief` | side | Ch 15 onward; exam stalls | Someone is stealing from the exam-week stalls | R 100, S market |
| `side.b3.rivals_sibling` | side | Ch 17 onward | The *rival*'s younger sibling wants to be trained before the finals, secretly | F with the *rival* |
| `side.b3.hospital_supplies` | side | Ch 17 onward; hospital | The hospital's supplies for exam injuries have gone missing | R 80, S hospital |
| `event.b3.betting_ring` | event | Ch 18; stadium streets | Someone is taking bets on the finals, and the odds on you are insulting | R, X 10% |
| `bond.b3.teammate_a` | bond | Ch 16; bond level 5 | A night-watch talk in the forest | F |
| `bond.b3.teammate_b` | bond | Ch 16; bond level 5 | A night-watch talk in the forest | F |

**Beta 3: 7 quests** (4 side, 1 event, 2 bond).

### Totals and Varied pools

| | Beta 1 | Beta 2 | Beta 2.5 | Beta 3 | Beta |
|---|---|---|---|---|---|
| Authored quests (Classic) | 17 | 45 | 17 | 7 | **86** |
| Of which clan | — | 8 | 17 | — | 25 |
| Generated templates active | 5 | 7 | 7 | 7 | 7 |
| Thorough player, hours | ~2.5 | ~5.5 | ~1.2 | ~1 | **~10** |
| Completionist, hours | ~3 | ~8.5 | ~1.7 | ~1.3 | **~14.5** |

| Varied pool | Shown | Pool |
|---|---|---|
| Beta 1 `side` one-offs | 4 | 8 |
| Your building's neighbours | 3 | 6 (by which block you get) |
| Beta 2 `side` one-offs | 8 | 20 |
| Beta 2 filler arcs | 2 | 3 |
| Beta 3 exam-week `side` | 4 | 8 |
| District chains, clan lines, bond quests | all | fixed |

## 9. Open questions

Nothing is open. Decided: clan welcomes ship in two waves (Beta 2 and Beta 2.5); council day is
watch-only in the beta, with testifying from Chunin; the generated templates follow the bond
system's hook schema (§3.1), including `stakes.variant` on favours and the post-beta
`estrangement` hook.
