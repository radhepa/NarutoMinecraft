# Dialogue

How the Leaf talks to you: the dialogue engine, the heard ledger and talk budgets that keep lines
fresh, how a line is chosen, how conversations are built, the questions residents ask you, and the
pipeline that produces lines at scale. It builds on Village Friends' dialogue (`tools/dialogue/`,
`talk/Talk.java`, `NarrativeEngine`, `Gossip`, the conversation window) and the bond engine's
dialogue keys ([BONDS.md](BONDS.md#13-data-formats), [LIFE_TOGETHER.md](LIFE_TOGETHER.md#6-conversation)).

**No spoilers here.** Story-gated pools live in `docs/story/dialogue/`, next to the story bible;
this file only says how they are gated.

**The owner's rule.** *Dialogue should feel fresh: once a line is used, it is never used again. You
can only talk to an NPC a certain number of times; past that, they begin to repeat.* And: *every
piece of dialogue serves a function (some can be filler), and friendship has questions and
choices.* Sections 1 to 3 are how the engine keeps that promise.

| Piece | Where |
|---|---|
| The engine (pure Java, no Minecraft): selection, the heard ledger, budgets, repeats, tokens, questions, barks, overheard talk | [`village/dialogue`](village/dialogue), package `dev.shinobi.village.dialogue` |
| The authoring pipeline: compiler and validators, the composer | [`tools/dialogue/dialogue.py`](tools/dialogue/dialogue.py), [`compose.py`](tools/dialogue/compose.py) |
| The writers' guide: format, tags, functions, voices, rules | [`tools/dialogue/WRITING.md`](tools/dialogue/WRITING.md) |
| Sources | `tools/dialogue/lines/`, `seeds/` (→ `generated/`), `exchanges/`, `questions/`; story-gated: `docs/story/dialogue/` |
| Tuning (budgets, facets, filler cap, specificity weights) | [`tools/dialogue/rules.json`](tools/dialogue/rules.json) |
| The compiled bank | `src/main/resources/data/narutominecraft/dialogue/*.json` (moves to the Village mod in Phase 0) |
| Stable ids | `tools/dialogue/ids.lock` (append-only) |

```
python3 tools/dialogue/compose.py                  # seeds -> generated pools
python3 tools/dialogue/dialogue.py                 # compile (validates everything)
python3 tools/dialogue/dialogue.py --check --stats --report
./gradlew :village:dialogue:test                   # the engine's tests
./gradlew :village:dialogue:simulate               # a thorough player's beta against the real bank
./gradlew :village:dialogue:bondKeys               # refresh tools/dialogue/bond_keys.txt from the bond engine
```

On a JDK older than 25, add `-PjavaRelease=21`: the engine uses nothing newer.

## Contents

1. [Freshness: never repeat](#1-freshness-never-repeat)
2. [Talk budgets](#2-talk-budgets)
3. [Beyond the budget](#3-beyond-the-budget)
4. [Storage](#4-storage)
5. [Selection: the most specific line wins](#5-selection-the-most-specific-line-wins)
6. [Conversations](#6-conversations)
7. [Every line serves a function](#7-every-line-serves-a-function)
8. [Questions and choices](#8-questions-and-choices)
9. [Mass production](#9-mass-production)
10. [Pool sizing](#10-pool-sizing)
11. [Simulation](#11-simulation)
12. [Story-gated pools](#12-story-gated-pools)
13. [What waits](#13-what-waits)
14. [Decisions and open questions](#14-decisions-and-open-questions)

## 1. Freshness: never repeat

Every line, every overheard exchange and every question has a **stable integer id**, assigned once by
the compiler and kept in `ids.lock` (a hash of the pool and the text, mapped to the next free
number; ids are never reused, and a removed line's id is retired). The save keeps a **heard
ledger**: one bit per id the player has heard.

- **A heard line is never chosen again while a fresh line fits.** The ledger is per player, not per
  speaker: hearing a line from the grocer spends it for the fishmonger too, because the player would
  notice the same words in two mouths.
- **Groups.** Composed lines that are one piece of content in several voices (the rain on the
  gutters, said warmly by one resident and briskly by another) share a group; hearing any voice
  spends the group. Composition widens *who* can say a thing, never *how many* things there are to
  hear, so freshness is counted in distinct pieces.
- **Questions** are spent once answered: no one asks them again. Deeper follow-ups are their own ids.
- **What is not spent.** The *repeatable set* (`kind=repeat`: "we already talked", closing lines),
  and *cycling pools* (`kind=cycle`: combat barks, shop transactions, ambient exchanges), which deal
  every line once before any comes back. A fight fires dozens of barks, and a shop confirms dozens of
  purchases, so these may come back, but only after every line in their pool has been used.

## 2. Talk budgets

Each speaker has a limited number of **fresh exchanges** for the player: a daily allowance, banked
on days you do not talk, and, for everyone but the cast, a **lifetime allowance** that grows with
the bond.

| Tier | Who | Daily | Banked up to | Lifetime |
|---|---|---|---|---|
| `cast` | The bound roles: squad, sensei, rival, classmates, instructor, medic, the merchant | 6 | 18 | none (story pools keep feeding them) |
| `named` | Shopkeepers, clan elders, quest givers, recurring residents | 4 | 12 | 40 + 8 per bond level + 10 per slice reached |
| `resident` | Everyone else who lives in the Leaf | 3 | 9 | 16 + 6 per bond level + 4 per slice reached |
| `passerby` | Gate guards on duty, crowd extras, visitors | 1 | 3 | 5 + 2 per bond level |

- **Conversations carry over** (the owner's decision). A day without talk banks that day's
  allowance, up to **three days' worth**. A friend you have not seen in a while has more to say, and
  it plays out over the visit. A longer absence banks no more, so a week away is not a wall of talk.
  Only the *count* is banked, never lines: every line is chosen when it is said, from what fits then
  (the time, the season, an event, your rank and stage, a quarrel...), so nothing stale or
  time-bound comes out of the bank. Partly used days bank what is left. The bank starts the day
  you meet someone.

- **An exchange** is one fresh line given in answer to the player: a topic, a question, a second
  greeting. **The first greeting of the day is free.** So a resident's day is a hello plus three
  things to say.
- **Exempt** (they never count and are never refused): news the speaker has not told you yet
  (`bond.seen.*`, `bond.heard.*`), bond moments and level-ups, quarrel greetings, life events,
  follow-ups, callbacks, society hooks, quest, mission and story lines, combat barks and shop talk.
  Something worth saying is always said.
- **Why per in-game day.** The Leaf runs on a day (VF's routines, the calendar, the bond engine's
  once-a-day talk warmth), and a day is 20 minutes of play, about the time between visits to the
  same street. A daily allowance makes residents feel like people with their own day. The player
  comes back tomorrow instead of draining someone in one sitting, and the conversation window can
  show it ("They seem busy").
- **Why a lifetime cap, scaled by importance and the bond.** 300 residents share the pools. Without
  a cap, a player who talks to the same baker every day for 100 hours would use up the baker's share
  of the bank. The cap matches how real acquaintances work: a passerby has a handful of things to
  say, a neighbour more, a friend more still, and every bond level opens six more fresh exchanges
  with a resident. Each new slice of the story adds a few, because the village has new things to talk
  about. The cast has no cap: they carry the story, and their pools grow with it.
- **Tuning:** every number is in `rules.json` (`budget.tiers` with `daily` and `bank_days`,
  `budget.exempt`).

## 3. Beyond the budget

When a speaker is out of fresh exchanges for today (their banked ones included), has reached their lifetime allowance, or simply
has nothing fresh that fits, the player has used up their time with that speaker, and the speaker
begins to repeat, in three steps:

1. **"We already talked."** A line from the repeatable `again` pool, in their personality's voice
   ("Again? Ha! I'm out of stories till tomorrow!" from a fiery resident; "We have spoken enough for
   one day" from a stern one).
2. **A repeat.** One of the last six lines this speaker said to you, said again. It is honest
   repetition, as people do repeat themselves, and it is clearly a repeat because the player heard
   it from them before.
3. **A polite close** from the `close` pool ("Well, I'd better get back to it"). The chat ends for
   today: the window keeps gifts, trades and quest talk, and hides the talk topics until tomorrow.

A repeated line is not marked in the window (the owner's decision): the "we already talked" line
says enough.

The counter resets each in-game day. Running out of fresh lines (not of budget) follows the same
three steps. The simulation counts it separately, because it is the repetition the player would
notice; the pools are sized so a thorough player almost never sees it in the beta (section 11).

## 4. Storage

The heard ledger is a player attachment (`narutominecraft:heard`, format 1, Codec-wrapped by the
Village mod; `Heard.write` / `Heard.read`):

| Field | Size |
|---|---|
| `lines`: a bitset of heard ids, Base64 | 1 bit per line in the bank: 30,000 lines → 3.75 KB raw, 5 KB as text |
| `groups`: a bitset of spent groups | 1 bit per group |
| `speakers`: per speaker talked to, in base 36: day, today's count, over-budget step, greeting day, lifetime count, fresh count, filler count, last question day, banked credits and their day, and the last six line ids said | ~45 bytes each; 300 speakers → 13 KB |
| `answers`: question → answer; `axes`: axis → last pole and question; `asked_by`: per-friend questions by speaker | ~25 bytes per answered question |

A **100-hour worst case** (30,000 lines with 25,000 of them heard, all 300 residents with a full
recall ring, 80 answered questions) is about **25 KB** (`QuestionsAndLedgerTest`); the beta's real
ledger is a few KB. A newer ledger format is refused with a clear message rather than misread.
Because the ledger is a bitset over append-only ids, adding lines never invalidates a save: new ids
are simply unheard.

## 5. Selection: the most specific line wins

The glue reads the moment into a `Context` of tags:

| Who is speaking | Their relationship to you | The world | You |
|---|---|---|---|
| `role` (cast), `personality` (VF's 16), `clan`, `group` (civilian, clanless, noble, minor), `rank`, `job`, `stage` (child, teen, adult), `gender`, `tier` | `level` (the level they act on, BONDS.md §3), `band` (VF's: stranger to best), `quarrel` (none to falling_out); meters, memories and moments through conditions | `time`, `weather`, `season`, `market`, `district`, `place`, `event` (festivals, exams, clan days), `mood` (BONDS village moods) | `player_rank`, `player_stage`, `clan_status` (born, member, other, clanless), `same_clan`, `slice` (beta1 to beta3); story flags, standing, reputation and recent deeds through conditions |

**How a line is chosen** (`Talk`):

1. **A topic picks a facet by weight.** A greeting draws from the event of the day (weight 8), the
   weather (5, if not clear), Market Day, your rank, the time, your relationship, their personality,
   their clan, their job, the place, the season; small talk from their own life (6), their job,
   their clan, rank life, the village, the place, the weather, the time, the season, and a tutorial
   helper now and then. A facet applies only if its tag is present (`needs` in `rules.json`), like
   VF's weighted pools in `Talk.pools`.
2. **Within the facet, the most specific fresh line wins.** Each line's tags are requirements; a line
   matches if every tag holds and its condition passes. Its **specificity** is the sum of its tags'
   weights (role 10, quarrel 6, event 4, clan 4, personality 4, deed 4, job 3, rank 3, level and band
   3, same clan 3, place 3, district 2, weather 2, player rank 2, time 1, season 1, a condition 3...).
   Among matching fresh lines, the highest specificity wins, ties at random. So a proud Uchiha
   Chunin at dusk in the rain says the line written for exactly that before the line for the rain.
3. **A facet with nothing fresh is skipped**, and the next is drawn. Explicit key lists from the bond
   engine (`BondDialogue.greeting`: the quarrel, a missed birthday, jealousy, the level; each as
   `<key>.<archetype>` then `<key>`) are tried in order, and a trailing personality is that line's
   `personality` tag, so `talk.food.fiery` beats `talk.food` for a fiery speaker.
4. **Children speak only from children's lines.** A line with no `stage` tag is said by teens and
   adults; Academy kids draw from `greet.child`, `chat.child` and anything tagged `stage=child`.

**Conditions** are Core's condition language (ROADMAP §5): `flag`, `quest_state`, `rank_at_least`,
`friendship`, `bond_meter`, `bond_memory`, `standing`, `event_active`, `village_mood`, `answered`...
The engine asks a `Conditions` interface; in the game that is Core's registry, so Shinobi Life
answers the bond conditions and Progression the quest states. `Conditions.basic` answers the common
ones for tests and the simulation.

**Tokens** (`Tokens.fill`): `{player}`, `{player_family}`, `{player_full}`, `{player_rank}`,
`{player_clan}`; `{name:<ref>}`, `{given:<ref>}`, `{family:<ref>}` for a role or resident;
`{hokage:<n>}`; `{twist:<slot>}` (story-gated pools only); pronouns `{they:<ref>}`, `{them:<ref>}`,
`{their:<ref>}`, `{theirs:<ref>}`; and situational fills from the context (`{friend}`, `{neighbor}`,
`{rival}`, `{kin}`, `{place}`, `{item}`, `{dish}`, `{special}`, `{shop}`, `{technique}`, `{client}`,
`{target}`, `{count}`, `{pay}`, `{event}`, `{season}`, `{weekday}`, `{time}`, `{other}`, `{squad}`).
A line whose token cannot be filled here is skipped, as in VF.

## 6. Conversations

The conversation window keeps VF's layout (portrait, typed line, numbered replies, the dock). What
the player can do, and where the lines come from:

| Part | Pools | Notes |
|---|---|---|
| **Greeting** | `greet.*` facets; bond greetings first when a quarrel, a missed birthday, jealousy or a courtship applies (`bond.greet.*`); news they have not told you (`bond.seen.*`, `bond.heard.*`) and VF's deed reactions open the line | The first greeting of the day is free |
| **Small talk** ("How's your day?") | `chat.*` facets; the bond engine's `talk.small_talk` is the same | |
| **Topics** | The bond engine's conversation topics (`talk.<topic>`, opening with the bond: food, training, a compliment, village news, their hobby, their family, your story, teasing, their values, advice, their dream, their worries) and VF's (news, heart, favourite things) | The reaction (warm, fine, awkward, pried) and its warmth are the bond engine's (`Conversation.talk`) |
| **Questions** they ask you | `questions.json` | Section 8 |
| **Gifts** | `gift.<loved/liked/plain/disliked/hated>`, personality variants | The taste and its effect are the bond engine's |
| **Bond moments** | `bond.level.<n>` on a level-up, `bond.memory.*` and `bond.perk.*` in the bond book, `hangout.*` scenes, `callback.*`, `followup.*`, `life.*` news and your response | Exempt from the budget |
| **Rumours and hooks** | `hook.<type>.offer` and outcomes; `ambient.hook.*` exchanges with a `lead:` | A lead lands in the journal (SIDE_QUESTS §2.3) |
| **Shop talk** | `shop.<shop>.<part>` (greet, browse, buy, can't afford, sold out, sell back, haggle, closing, recommend, regulars) | Transactions cycle; shop chat is fresh |
| **Missions** | `mission.<rank>.<template>.<part>` (title, brief, accept, decline, progress, success, fail, report), `.twist.<id>`, `.choice.<step>`; `mission.banter.<moment>.<speaker>[.<band>]`; `mission.desk.*` | The missions session's 65 beta templates; slot names are tokens; the clerk speaks the report, the client success and fail |
| **Combat barks** | `combat.<event>.<speaker kind>`, `combat.command_ack.<order>` (`speaker=player_ally`), `combat.sensei_tip.<habit>`, `combat.boss.<id>.phase_<n>` | The combat session's keys; cycling, throttled by Combat (one per speaker per 6 s) |
| **Overheard chatter** | `ambient.<relation>`: two residents' exchange, shown as subtitles when the player walks by; stopping to listen turns a lead into a journal entry | Cycling; VF's neighbour chats (`chat_speak`, `chat_listen`) |
| **Events** | `greet.event`, `chat.event` with `event=` (the Leaf Festival, New Year, Market Day, graduations, the exam weeks, clan days, the first snow...), `village.mood.<label>` | The event facet weighs most on its day |
| **Repeats** | `again`, `close` (per personality) | Section 3 |

**Your replies and what they do.** Every choice the player makes in a conversation is a bond action,
which the engine hands to Shinobi Life:

| Choice | Bond engine |
|---|---|
| Talk at all (once a day) | `talk`: warmth 1, a contact day |
| A topic | `Conversation.talk`: warmth by how much they like the topic; a personal topic too soon is prying; teasing a proud speaker is rude |
| Answer a question | `Questions.answer` (agreed with the bonds session): the answer's values honoured or violated through their personality, its tone, a remembered answer, a contradiction if it goes against an earlier one |
| Respond to their news (congratulate, comfort, help, shrug) | `LifeEvents` responses |
| A gift | `gift`: by their taste |
| Accept or decline a hangout | `Together` |
| Mediate, take sides, keep or tell a secret (hooks and quests) | `resolve_hook`, `bond_event` with the act |

## 7. Every line serves a function

Every pool carries a required `fn=` tag from a fixed taxonomy, checked by the compiler:

| Function | The line... |
|---|---|
| `teach` | explains a mechanic in the world's own words (fatigue, ryo, furnishing, chakra, the Mission Desk) |
| `guide` | points somewhere (where, when it opens) |
| `quest` | advances or gates a mission or side quest |
| `reveal_character` | shows who the speaker is: past, taste, values, fears |
| `deepen_bond` | is about the two of you |
| `foreshadow` | plants a story seed: story-gated pools only, and keyed by story id (`story=<id>`, required) |
| `worldbuild` | lore, clans, places, customs |
| `react` | answers the player's deeds, rank, the time, the weather, an event |
| `callback` | remembers an answer, a memory, a hangout |
| `hook` | a rumour or need that can become a side quest |
| `commerce` | buying and selling |
| `filler` | pure pleasantry |

**Filler is capped twice.** At run time, a speaker's fresh lines to the player stay at or under **20%
filler** (`filler_cap`): past the cap, a filler line is chosen only when nothing else fits. At
build time, `dialogue.py --report` prints the filler share per pool family and per coverage cell,
and writers keep each pool's filler under a fifth. The mix is in [section 9](#the-bank-today).

## 8. Questions and choices

Residents ask the player real questions: opinions, values, advice, preferences, their past and
plans, and small dilemmas. The player picks one of 2 to 4 answers.

```text
? q.values.honest_or_kind | fn: reveal_character deepen_bond | level: 3 | axis: honesty_vs_kindness
Q: A friend shows you a painting, and it's awful. Do you tell them?
Q: Say your friend's cooking is terrible. Do you tell them?
- Tell them, gently :: Gently. Yes. Kind and true at once. {values:+honesty} {tone:warm} {pole:1} [NOTE]
- Praise it anyway :: That's sweet. Though I'd want to know, if it were me. {values:+kindness -honesty} {tone:warm} {pole:-1}
- Ask what they think :: Clever. Make them say it first. {values:+knowledge} {tone:curious}
```

Compiled (`questions.json`): `{"id", "num" (the ledger id), "fn", "level", "kind", "tags", "when",
"axis", "follows", "public", "gap", "sets", "depth", "asks": [...], "answers": [{"id", "label",
"reply", "mood", "values", "tone", "pole", "actions"}]}`. The bond engine reads this file as it is
(`life/bonds` `Question.parse`); the format was agreed with the bonds session.

- **Who owns what.** Answers carry *stances*, not numbers: the values they honour (+1) or violate
  (-1), from BONDS.md's ten; a tone (warm, gentle, joking, teasing, stern, cold, or a trait tag such
  as blunt, honest, loyal, ambitious, humble, proud, curious); and a pole on the question's axis. The
  bond engine owns the effect (`Questions.answer`). An answer +1 on a value the asker holds is +1.5
  affection and +1.5 trust; one that goes against a value they hold is -2 affection and -2.5 trust.
  The tone lands through their traits, and the bond keeps the answer as a fact
  (`answer:<question>=<answer>`).
- **Kinds** weigh differently: confessions 1.3, dilemmas and advice 1.15, preferences 0.7 (`kind:`,
  or the id family: `q.values`, `q.dilemma`, `q.advice`, `q.pref`, `q.past`, `q.plans`,
  `q.confess`). **Public** answers (opinions about clans, people or the village) travel by gossip,
  so someone else can catch a contradiction.
- **Remembered, then called back.** Every answer has a callback pool,
  `callback.answer.<question>.<answer>` ("You told me you'd take the long road if it meant seeing
  the sea..."), brought up at least a week later, once (`Questions.callback`). The resident's
  immediate reaction comes from `reaction.<label>` (touched, pleased, amused, impressed, fine,
  stung_but_respects, hurt, noticed_contradiction) and their personality's variants.
- **Contradictions are noticed.** An answer on the same axis with the opposite pole is a
  contradiction, including one the asker heard about through gossip. Answers older than a year do
  not count. It costs a little trust (the bond engine's `CAUGHT_CONTRADICTION`), and the speaker
  says a `callback.contradict` line. The dialogue engine also records each axis's last pole, for
  when it runs on its own (`Answered.contradicts`).
- **Deeper versions.** A question can `follow` another (`depth: 2`, a higher level, an optional
  `gap` in days): it is asked only after the first is answered, and deeper questions come first
  once open.
- **Never repeated.** Answering spends the question in the heard ledger: no one asks it again.
- **Per-friend opinion questions** (`per_friend: yes`, the owner's decision): a few light opinion
  questions ("What season do you like best?", "How do you order your ramen?") may be asked once by
  each close friend (level 5 or more) rather than once in all. They are kept per speaker
  (`asked_by`). Twelve questions are per-friend today.
- **Pacing** is the bond engine's (`Questions.next`). Questions start at bond level 2, at most one
  a day across everyone, and one person waits 8, 6 or 4 days between questions at levels 2-3, 4-6
  and 7+. It calls the dialogue engine's `Talk.askable` as a veto: never answered, the level, the
  tags (who may ask: `personality`, `role`, `clan`), `when`, the question followed, the tokens, and a
  fresh exchange left in the speaker's budget (a question costs one). `Talk.ask` mirrors the pacing
  for the simulation (`rules.json`, `questions`).
- **How many.** Over 60 hours a close friend draws on 30 to 40 questions open to them. So the beta
  needs about 150 general questions (about 10 per personality) and 10 to 15 per major character.
  The bank has **310** (150 general, 10 per personality, a third of them follow-ups); the cast's own
  wait for the story briefs.

## 9. Mass production

**The pipeline** (`tools/dialogue/`):

1. **Write** pools in VF's dialogue text format, extended with context tags, a function, a kind,
   moods and groups ([WRITING.md](tools/dialogue/WRITING.md)); questions in VF's question format,
   extended with stances; overheard exchanges as `A:`/`B:` turns.
2. **Compose** (`compose.py`): seeds become reviewable pools in `generated/`.
   - **Voice kernels:** one idea, voiced per personality register (warm, bright, bold, calm, precise,
     quiet, proud, dreamy, guard) or clan, sharing a group.
   - **Slot templates:** a frame filled from lists, where the last slot's fills are used once each.
     Use them for shop wares and situational observations, not padding.
3. **Compile and validate** (`dialogue.py`). The compiler rejects:
   - unknown tags, values, functions, kinds, moods, tokens, conditions and actions;
   - lines over 300 characters;
   - exact duplicates, and **near duplicates**: Jaccard over words and word pairs ≥ 0.72 between any
     two lines in reach of one player, except the voices of one group;
   - **literal names** (the clan and family name pools, the given-name pool once it exists) and canon
     characters or catchphrases;
   - **gendered pronouns** with no gendered word in the line to anchor them (VF's rule: pronoun-free
     where possible, `{they:ref}` otherwise), and gendered address to the player (boy, girl, sir,
     young lady);
   - **romance** in any line a child could say or hear (a romantic word needs `stage` and
     `player_stage` tags that exclude child: nothing romantic in the beta);
   - **spoilers**: any term the story bible holds and no public doc uses, plus
     `docs/story/dialogue/spoiler_terms.txt`, outside the story-gated pools;
   - `foreshadow` without a story id, and `{twist:...}` outside the gated pools.

   It then assigns ids, writes one JSON file per pool family plus `questions.json`, `story.json`,
   `rules.json` and a manifest, and reports counts, coverage, the function mix and the bond keys
   still to write.
4. **Check** (`--check`): the compiled files and `ids.lock` must match the sources, as the
   wardrobe's `--check` does.

### The bank today

**15,766 pieces of dialogue** (`dialogue.py --stats`): 15,154 lines in 3,780 pools, 302 overheard
exchanges (696 turns) and 310 questions (1,043 answers), with 8 story-gated pilot lines. By kind,
10,050 lines are said once per save, 5,232 cycle and 174 are in the repeatable set.

| Family | Lines | What |
|---|---|---|
| `chat.*` | 3,836 | Small talk: 45 per personality, rank life, the village, jobs (28), clans (25 plus the clanless and civilian), districts, weather, time, seasons, 122 tutorial helpers, 931 children's lines |
| `greet.*` | 2,558 | Greetings by time (300), weather, season, relationship band, the player's rank, personality (20 each), clan (14 each), job, place, Market Day, events, 437 children's |
| `mission.*` | 1,667 | Every key of the missions session's 65 beta templates (titles, briefs, outcomes, 147 twists, 23 choices), 105 banter pools with cohesion bands, the desk clerk |
| `callback.*` | 1,318 | A callback for every one of the 1,043 answers, contradictions, 250 hangout highlights |
| `shop.*`, `job.*` | 1,414 | The items session's 31 shops by part, the 10 part-time jobs |
| `hangout.*` | 939 | 27 activities (22 plus the 5 hosted at home): every part, highlights |
| `talk.*` | 803 | The bond engine's conversation topics: about 18 general, 2 per personality and 6 for children per topic |
| `combat.*` | 798 | Barks for bandits, rogues, bystanders, sparring partners and exam Genin; a pilot for allies and the rival; sensei tips |
| `bond.*` | 655 | Greetings by level and quarrel state, level-ups, news, the bond book (memories, facts, feelings, perks, goals, kindling, level names) |
| `home.*` | 438 | The home session's visits, notes, pantry, keys |
| Others | 750 | Life events (235), gifts, hooks, reactions, follow-ups, village moods, the repeatable "again" and "close" sets by personality |
| Exchanges | 302 | Overheard talk by relation (212) and 90 hook leads |
| Questions | 310 | 150 general and 10 per personality; 101 follow-ups; levels 2 to 7; six contradiction axes |

**Coverage.** Every pool the bond engine asks for exists (`DialogueKeys.required()` on `bonds-2`:
1,371 of 1,371). For every personality × clan voice × rank × relationship band (8,400 cells, a
spring morning at the market, a Genin player), a speaker can reach at least 86 fresh greetings
(median 112) and 404 fresh small-talk pieces (median 466).

**The function mix** (primary function): react 21.7%, reveal_character 19.2%, worldbuild 13.0%,
deepen_bond 11.0%, callback 10.0%, commerce 9.5%, quest 8.2%, teach 3.4%, hook 2.1%, guide 1.2%,
**filler 0.7%** (at most 5.2% in any family: small talk).

## 10. Pool sizing

**The inputs.**

| | Beta | Whole game |
|---|---|---|
| Hours (main path + a thorough player's side content) | 15 + 10 = 25 | 60 + 40 = 100 |
| In-game days (three to an hour, BONDS.md §15) | ~75 | ~300 |
| Residents | ~200 in the beta's districts, 300 by the end | 300 |
| Cast | 9 bound roles | grows by arc |

**The demand.** A thorough player talks to about three residents in each part of the day (morning,
afternoon, evening) and about four of the cast each day, and a conversation is a greeting plus one
to three exchanges (two on average):

```
resident lines  = 9 conversations/day x 3 lines x 75 days  ≈ 2,000   (greetings 675, exchanges 1,350)
cast lines      = 4 conversations/day x 3 lines x 75 days  ≈   900   (role and bond pools first, then the shared pools)
question asks   ≈ 1 exchange in 10                         ≈   200   (bounded by eligibility: levels, follow-ups)
```

The talk budget bounds the extremes: a resident gives at most 3 fresh exchanges a day and 16 + 6 per
level + 4 per slice in a lifetime, so even a player who talks to every one of 200 beta residents
until they are dry draws at most about 200 x (16 + 6 x 2 + 4 x 3) ≈ 8,000 lines, and in practice
far fewer, because nobody meets everyone often.

**From demand to supply.** A facet gets a share of the requests (its weight over the weights that
apply), and each share is spread over the contexts that can reach a line. For a pool that one kind
of speaker uses (chat.personal for one personality), the supply has to cover that personality's
share of the demand with a margin:

```
need(pool) = requests x P(topic) x P(facet | topic) x P(context reaches the pool) / target_use
target_use = 0.6    (at the beta's end at most 60% of a pool is spent, so "most specific first" still has choices
                     and a second playthrough differs)
```

| Pool family | Requests in the beta (thorough) | Share | Needed | Rule of thumb |
|---|---|---|---|---|
| Greetings (`greet.*`) | ~975 | time 3, rank 3, band 3, personality 2, clan 2, job 2, place 2, season 1, weather 5 on wet days, event 8 on event days | ~1,600 | ~45 per time of day; ~40 per relationship band; ~20 per personality; ~14 per clan; ~10 per job |
| Small talk (`chat.*`) | ~1,250 | personal 6, job 4, clan 3, rank 3, village 3, weather 3, place 2, time 2, season 2, teach 2 | ~2,000 | ~45 per personality (each sees ~1/16 of 20% of the demand, doubled for the cast's fixed personalities); ~15 per job; ~16 per clan; ~200 village |
| Bond topics (`talk.*`) | ~600 | by topic, opening with level | ~1,000 | 3 or more per topic, 2 per archetype for the topics that personality colours |
| Children (`*.child`) | ~250 | 15% of residents | ~400 | |
| Questions | ~200 asked | | ~150 written | follow-ups at depth 2 for a third |
| Shops, barks, ambient | cycling | | ~50 per shop, ~15 per bark event and speaker, ~300 exchanges | They cycle, so size is for variety, not freshness |

**The whole game.** About four times the beta's talk. The beta's pools are not meant to carry it:
later slices add rank pools (Chunin, Jonin), new events, the teen and adult player stages, new
districts and the cast's story pools, and the lifetime caps keep the background residents from
draining the shared pools. The simulation's third run plays 300 days on the beta's pools alone, to
show where the next writing must go first.

## 11. Simulation

`./gradlew :village:dialogue:simulate` loads the compiled bank and plays a village of 300 residents
(population weights: 45% civilian, 28% clanless, 14% minor clans, 13% noble; 15% Academy children;
30 named), the beta's nine cast roles, the calendar (seasons, weather, Market Day, graduations, the
exam weeks, the Leaf Festival) and the player's rank and stage by slice. The player meets known faces
first and someone new now and then, and asks topics and answers questions at the rates above.

Seed 20261029, the bank above, with talk banked for up to three days:

| A thorough player's beta (75 days, 975 conversations, 175 people) | Requests | Fresh | Past the budget | Nothing fresh left |
|---|---|---|---|---|
| Small talk, all speakers | 904 | 99.8% | 0.2% | 0 |
| Greetings, all speakers | 524 | 99.8% | 0.2% | 0 |
| Bond topics, all speakers | 97 | 95.9% | 4.1% | 0 |
| **Everything** (children and the cast included) | **2,815** | **99.6%** | **0.4%** | **0** |

- **Nothing runs dry in a thorough player's beta**: no request finds nothing fresh, and 0.7% of
  conversations reach a speaker's budget (4.3% before talk was banked). 35 questions are answered
  (two contradicting an earlier answer), the filler share of fresh lines is 1.4%, 2,837 lines are
  heard, and the ledger is 14 KB.
- **A player who talks to everyone** (eight residents per part of the day, seven of the cast, three
  to six exchanges each) reaches a speaker's budget in 11% of conversations and finds nothing fresh
  in 39% of requests from day 20. Because a line heard from anyone is spent for all (the owner's
  decision), a player who drains the shared pools hears the repeat steps: "we already talked", a
  line said before, a close.
- **The whole game on the beta's pools alone** (300 days) runs dry for 41% of requests after day
  80. This is expected: later slices bring their own pools (rank, stage, events, districts, the
  cast's story voices). The ledger reaches 25 KB.
- **What it took.** The first run (11,000 lines) repeated for 20% of requests from day 20, because
  the beta's classmates and teammates are children and children could speak only from children's
  pools. Opening the bond engine's pools to every age (with adult-only lines tagged), 1,100 more
  children's lines and 480 more topic lines brought it to 0.45%; banking talk took it to 0. The pools
  most used at the beta's end are the tutorial helpers (102 of 122), the place greetings (105 of
  132), Market Day (19 of 25) and the bond topics (compliments 41 of 56): the next writing goes there.

## 12. Story-gated pools

Lines that touch the story's secrets live in `docs/story/dialogue/` (lines, exchanges and questions,
in the same format), are keyed by the story id they serve (`story=<flag or seed>`) and gated by a
condition on it. They compile into `story.json`, which the engine loads like any other file. The
compiler lets the story bible's terms appear only there, and requires `foreshadow` lines to carry a
story id. This file, commit messages and reports never quote them.

**Waiting on the story lock.** The story session is writing and reviewing the full story, then
per-character dialogue briefs: voice, topics, what each must not reveal before which flag, and their
questions for the player. Until then only a pilot of story-gated pools exists. The cast's own
voices (role-tagged greetings, topics, hangouts, highlights, life events, combat barks for
`player_ally` and `rival`, mission banter by role) wait for those briefs. The engine already selects
them: a `role=` tag outweighs every other tag.

## 13. What waits

| What | Waits for |
|---|---|
| The glue: building a `Context` from a resident and the world (including `speaker` for barks and `job=mission_desk` for the clerk), the conversation window's topics and questions, the ledger's attachment and Codec, Core's condition registry behind `Conditions`, the name resolver behind `Names` (the cast, rolled names, pronouns, pets), speech bubbles from `mood` | Phase 0 (the Village mod and Core) |
| The cast's voices: role-tagged greetings, topics, hangouts, life events, their questions (10 to 15 each), the `player_ally` and `rival` barks beyond the pilot, mission banter by role, and the story-gated pools | The story lock and the character briefs (the story session, `docs/story/DIALOGUE_BRIEFS.md`) |
| Category-flavoured mission banter (`mission.banter.<category>.*`) | Later, as flavour (the missions session: delivery, pets, escort, beasts and guard first) |
| The final bark list | The combat session's `data/combat/barks.json` (the pools follow its keys already) |
| Districts and anchors | The Konoha build's `districts.json` (the `district` tag's list is provisional) |
| Moving the compiled bank to `village/src/main/resources` | Phase 0's repository layout |
| A JDK 25 run of the tests | This session's container had JDK 21 (`-PjavaRelease=21`) |

## 14. Decisions and open questions

Decided by the owner:

- **Budgets:** 3 fresh exchanges a day for residents and 6 for the cast, with unused talk banked
  (up to three days' worth here; section 2).
- **Repeats are not marked** in the window.
- **Spending stays global:** a line heard from anyone is spent for everyone.
- **A few opinion questions** can be asked once per close friend (section 8).
- **The writers' small inventions stay:** the ferry, the river island, the courier office, the
  district wells, the mural bathhouse, ramen at 8 ryo, the gate closing at dusk, the weekday names.
  The Konoha build adds the places.

Still open:

- **The bank's size.** Three days' worth (9 exchanges for a resident) is generous for one visit.
  Playtests may want two days, or a cap per conversation.
