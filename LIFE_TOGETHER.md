# Life together

How relationships in the Shinobi Modpack should feel real: people you spend time with, who ask you
out, who have lives of their own, who remember the good evenings and bring them up, who ask how
your exam went, and who notice when you stop showing up. Minecraft is the engine; this is the
game. It sits on the bond engine ([BONDS.md](BONDS.md)) and its numbers, in the same pure module
(`life/bonds`: `Activity`, `Schedule`, `Together`, `LifeEvents`, `Conversation`, `DialogueKeys`).

**No spoilers here.** Story-specific hangouts and scenes belong in the developers-only story bible.

## 1. What makes a relationship feel real

The design rules every system below follows, and every piece of content should too:

1. **They have their own lives.** People are busy (lessons, shifts, duty), have good and bad weeks,
   and tell you about them when you are close enough to hear it.
2. **They take the first step too.** Friends invite you out, not only the other way round, and stop
   if you keep turning them down.
3. **They remember specifics.** Not "we had ramen" but the night the bowl tipped over. A great
   evening leaves a highlight they bring up weeks later.
4. **They follow up.** Tell someone about your exam and they ask how it went. Comfort a friend
   through something hard and they tell you later how it turned out.
5. **Habits become yours.** The same ramen with the same friend three times in five weeks becomes
   *your* ramen; it goes better, and they miss it when it lapses.
6. **Depth is earned.** You can talk about the weather on day one; their dream, only when they
   trust you. Asking too soon is prying.
7. **Everyone is different.** The same tease delights one friend and stings another; one loves the
   river at dawn and finds the bathhouse awkward.
8. **Friends connect.** Bring two friends along and they become friends with each other; bring two
   who dislike each other and the evening sours.
9. **Absence is noticed.** A missed birthday, a plan you never showed up to, hard news you never
   answered: all remembered.
10. **It is never a vending machine.** Gifts and talk alone stop at level 3 (story gates, BONDS.md
    section 3); the rest needs time and moments.

## 2. Schedules

Everyone keeps VF's day: asleep 23:00 to 6:00; Academy children in lessons 9 to 12 on weekdays;
civilians with a workplace at work 9 to 17 on weekdays; shinobi away on duty some days from 8 to 18
(about a third of the days for a Genin, more than half for a Jonin), rolled per person and day from
the save seed. `Schedule.doing` says what someone is doing at an hour; the world glue can replace it
with VF's live routine block. Asking someone who is busy gets a no **and the next time they are
free** within three days.

## 3. Hangouts

Twenty-two activities, as data (`Activity`; the Adventure datapack adds more with the same fields):

| Activity | Where | Hours | Season | Ryo | From level | Up to | Counts as | Loved by |
|---|---|---|---|---|---|---|---|---|
| Ramen | Ichiraku | 11–23 | | 8 | 1 | 4 | a meal | fiery, warmhearted, playful, adventurous |
| Dango | tea house | 10–19 | | 6 | 1 | 4 | a meal | gentle, shy, playful, warmhearted |
| Barbecue | barbecue house | 17–23 | | 30 | 4 | 6 | a meal | warmhearted, fiery, steadfast |
| Sparring | training ground | 6–20 | | 0 | 2 | 2 | training | proud, fiery, adventurous, protective |
| Training | Training Ground 3 | 6–19 | | 0 | 1 | 4 | training | stern, meticulous, steadfast, proud |
| Fishing | the river | 5–11 | | 0 | 2 | 3 | hanging out | reserved, steadfast, pragmatic |
| Stargazing | the Hokage Rock | 20–2 | | 0 | 4 | 3 | hanging out | curious, imaginative, shy, thoughtful |
| Painting | the overlook | 9–18 | | 5 | 3 | 2 | hanging out | imaginative, shy, gentle |
| Shogi | tea house | 13–21 | | 0 | 2 | 2 | hanging out | thoughtful, meticulous, pragmatic, stern |
| Library | Academy library | 9–18 | | 0 | 1 | 4 | studying | thoughtful, curious, meticulous |
| Market stroll | market street | 9–20 | | 10 | 1 | 4 | hanging out | playful, curious, warmhearted |
| Rooftop race | the rooftops | 7–21 | | 0 | 2 | 4 | training | fiery, adventurous, playful |
| Bathhouse | bathhouse | 16–23 | | 5 | 3 | 6 | hanging out | warmhearted, steadfast, playful |
| Shrine visit | the shrine | 6–18 | | 0 | 2 | 4 | hanging out | steadfast, gentle, stern |
| Walking a pet | the river | 6–20 | | 0 | 1 | 3 | hanging out | protective, fiery, gentle |
| Dinner at their home | their home | 18–21 | | 0 | 5 | 6 | a meal | warmhearted, protective, steadfast |
| Flower viewing | flower park | 9–19 | spring | 0 | 2 | 6 | a festival | gentle, imaginative, warmhearted |
| Swimming | the lake | 9–18 | summer | 0 | 2 | 6 | hanging out | adventurous, playful, fiery |
| Moon viewing | the Hokage Rock | 19–24 | autumn | 0 | 3 | 6 | hanging out | thoughtful, gentle, stern |
| Snowball fight | training ground | 9–17 | winter | 0 | 1 | 8 | hanging out | playful, fiery, adventurous |
| Evening walk | the river | 18–23 | | 0 | 7 | 2 | a date (teen+, dating) | gentle, shy, imaginative, warmhearted |
| Lantern night | the lake | 19–24 | | 5 | 7 | 2 | a date (teen+, dating) | imaginative, thoughtful, gentle |

**Tastes** (`Activity.taste`, -1 to 1): +0.6 if their personality loves it (-0.5 if it dislikes it),
+0.2 for each of their values it touches, +0.5 for their own favorite and -0.6 for their least
favorite (both rolled per person from the save seed, so two shy residents still differ). After two
hangouts at their favorite, the bond book shows it.

**Asking** (`Together.invite`, one or more people, an activity, a day and an hour). Each answers
yes or why not: `busy` (with a counter-proposal), `not_close_enough` (below the activity's level),
`not_like_that` (a date when you are not dating), `too_young`, `closed` (wrong hour or season),
`cold` (a quarrel), or a roll that grows with their level and taste:
`yes = 0.25 + 0.08 level + 0.3 taste - 0.15 x refusals in a row (if asked again within 2 days) + 0.1 village cheer`,
and a no is `not_their_thing` when they dislike it, else `not_today`.

**Being asked** (`Together.daily`). Each day, residents at level 3 or more may invite the player:
about 2% a day at level 3, more for closer, warmer and more open people, never twice within six
days, at most three invitations waiting. They pick what they like most that they may suggest and a
time they are free. Accepting makes a plan; turning someone down three times running makes them
feel overlooked and they stop asking for two weeks. An invitation left unanswered counts as a no.

**The hangout** (`Together.go`). Not showing up to a plan is being stood up (a memory that costs
trust; lateness is a pet peeve for some). Otherwise the time goes, per person:

```
quality = 0.45 + 0.3 taste + 0.1 chemistry + 0.1 village cheer + 0.15 if it is a ritual
          - 0.2 for each companion they dislike + a seeded +-0.2
```

The group's mean decides how it went: **rough** (under 0.3: an awkward memory), **fine**,
**good** (0.6: a little extra warmth) or **great** (0.85: a **highlight**). Each person takes the
activity's act (a meal, training, hanging out, a date), counted as a shared experience for the
story gates. Companions who had a good time warm to each other, and if they had no tie they become
friends (introductions).

**Highlights.** A great hangout picks one of the activity's highlight lines
(`hangout.ramen.highlight.4`) and every friend there keeps it, with the day and who was there, as a
notable memory that fades slowly (half-life 150 days). A week later and at most every two weeks,
they bring it up (`BondDialogue.callback`: `callback.hangout.ramen.highlight.4`), and it opens the
`shared_memory` conversation topic.

**Rituals.** The same activity with the same person three times within 35 days becomes a ritual
("our ramen"): +0.15 quality from then on, a `ritual` condition for quests, a line when it forms. Four
weeks without it, they say they miss it (`followup.ritual_missed.<activity>`); eight, and it is let go.

## 4. Their lives

`LifeEvents`: on each person's weekly turn, the people the player has met may have something
happen (35% a week for the cast, 20% for residents, at most three pending), drawn from what fits
them:

| Event | Told at level | Good or hard | Who |
|---|---|---|---|
| Promoted | 1 | good | shinobi below Jonin |
| Passed an exam | 1 | good | Academy students, Genin |
| A proud moment | 2 | good | anyone |
| A new pet | 1 | good | anyone |
| A new baby in the family | 2 | good | people with family |
| A new hobby | 2 | good | anyone |
| A step toward their dream | 4 | good | anyone with a dream |
| Moving house | 2 | neither | adults |
| Lost to a rival | 3 | hard | shinobi |
| Injured | 3 | hard | shinobi |
| Sick | 3 | hard | anyone |
| Trouble at the shop | 3 | hard | civilians with a workplace |
| A quarrel with a friend | 4 | hard | anyone |
| A setback on their dream | 5 | hard | anyone with a dream |
| A loss in the family | 4 | hard | people with family |
| Heartbreak | 5 | hard | teens and adults (never children) |

They tell the player (`life.<kind>`) the next time they talk, once the bond reaches the event's
level. The player responds: **congratulate** (good news: a warm memory; hard news: it stings),
**comfort** (hard news: a notable memory, and a real moment for the story gates at level 5 or more;
they tell you later how it turned out), **help** (they remember you stood by them), or **shrug**
(hard news: they feel overlooked). Hard news a close friend (level 5+) told you, left unanswered
for a week, is noticed. Their update arrives as the `their_news` conversation topic one to two
weeks later.

## 5. Following up

`Together.share(who, topic, days)`: tell someone what is coming up (an exam, a mission, a festival,
a date) and after that many days they ask how it went (`followup.<topic>`), once, and the bond warms
a little for it. Lapsed rituals and comforted news follow up the same way.

## 6. Conversation

`Conversation.topics` and `Conversation.talk`: what you can talk about opens with the bond. Each
topic counts once a day per person; the reply is a dialogue key (`talk.<topic>.<archetype>`, then
`talk.<topic>`) and a reaction (warm, fine, awkward, pried).

| Topic | From level | Personal | Reveals | Loved by | Disliked by |
|---|---|---|---|---|---|
| Small talk | 0 | | | | |
| Food | 1 | | | fiery, warmhearted, playful | |
| Training | 1 | | | proud, stern, fiery, adventurous | gentle |
| A compliment | 1 | | | gentle, warmhearted, shy, playful | reserved, pragmatic |
| Their hobby | 2 | yes | hobby | | |
| Village news | 3 | | | curious, playful | reserved |
| About someone (their opinion of a third person) | 3 | | | curious | stern |
| A shared memory (needs a highlight a week old) | 3 | | | | |
| How their news turned out (needs one due) | 3 | | | | |
| Their family | 4 | yes | family | warmhearted, protective | |
| Your story (you open up: a heart-to-heart) | 4 | | | warmhearted, curious, gentle | reserved |
| Teasing | 4 | | | playful, fiery, adventurous | proud, shy, stern |
| Their values | 5 | yes | values | thoughtful, steadfast | |
| Asking their advice | 5 | | | thoughtful, stern, proud, protective | |
| Their dream (a heart-to-heart) | 6 | yes | dream | | |
| What worries them (a heart-to-heart) | 7 | yes | worries | | |

A personal topic before its level is prying (a memory; nosiness is a peeve for some). A topic someone
dislikes is awkward (teasing the proud is rude). One they love is worth 1.6 times the warmth.

## 7. Questions and choices

Residents ask the player things, and the answer matters (`Question`, `AnswerTag`, `Questions`). The
lines and the question data are the dialogue team's; the engine reads a question as parsed JSON:

```json
{"format": 1, "id": "q.dilemma.found_wallet", "kind": "dilemma", "level": 3, "depth": 1,
 "follow_up_of": "", "min_gap_days": 0, "about": "value:honesty", "public": false,
 "audience": {"archetypes": [], "values": [], "roles": [], "min_stage": "child", "clan": ""},
 "answers": [{"id": "return_it", "tags": ["honest", "kind"], "stance": "honest",
              "sets": "", "nudge": {"trait": "", "amount": 0}, "deed": ""},
             {"id": "keep_it", "tags": ["ambitious", "blunt"], "stance": "self"}]}
```

- **Kinds:** an opinion, a dilemma (values in conflict), advice they ask for, a preference, the
  player's past, the player's plans, and their own small confession (how the player takes it).
  Confessions weigh 1.3, dilemmas and advice 1.15, preferences 0.7; deeper questions (depth 2 and
  3, at higher levels) weigh a quarter more per step.
- **Answers** (two to four) carry tags, resolved against the asker's personality and values like an
  act: an effect, values honored or violated, a pet peeve, leans on traits.

| Tag | Effect (aff / trust / resp / riv) | Honors | Violates | Leans |
|---|---|---|---|---|
| kind | 2 / 1 / 0 / 0 | kindness | | the warm like it more |
| blunt | -1.5 / 2 / 1 / 0 | honesty | | the warm and the proud are stung |
| honest | 0.5 / 2 / 0.5 / 0 | honesty | | |
| loyal | 1.5 / 2 / 0 / 0 | loyalty, family | | |
| ambitious | 0 / 0 / 2 / 1 | strength, courage | | the proud like it, and rise to it |
| playful | 1.5 / 0 / -0.5 / 0 | freedom | | charms the open, grates on the disciplined |
| cautious | 0 / 1.5 / -0.5 / 0 | duty | | the bold respect it less |
| bold | 0.5 / -0.5 / 1.5 / 0.5 | courage | | the bold respect it, the disciplined trust it less |
| humble | 1 / 0.5 / 0.5 / -0.5 | kindness | | the proud respect it less |
| proud | -0.5 / 0 / 1 / 1 | strength | | the proud like it, the warm do not; bragging is a peeve |
| dutiful | 0 / 1.5 / 1 / 0 | duty | freedom | the disciplined trust it |
| free | 1 / 0 / 0 / 0 | freedom, creativity | duty | |
| evasive | -1 / -1.5 / 0 / 0 | | honesty | the open dislike it |
| rude | -3 / -1 / 0 / 0 | | kindness | rudeness is a peeve |
| curious | 1 / 0.5 / 0 / 0 | knowledge | | the open like it |
| family | 1 / 1 / 0 / 0 | family | | |

- **What answering does:** the meters move (both ways: a blunt answer raises trust and costs
  warmth), the asker's **mood** today becomes touched, pleased, amused, impressed, fine,
  stung_but_respects or hurt, and the answer is a remembered memory and a ledger entry.
- **Memory:** the bond's ledger keeps every answer. A week later, at most every two weeks, they bring
  one up (`callback.answer.<question>.<answer>`), once each.
- **Contradictions:** an answer has a stance on the question's axis (`about`: a value, a clan, a
  person, a plan). Saying the opposite of what you said before on the same axis, to them or to
  someone they heard it from, is a contradiction. They notice with chance
  `0.15 + 0.07 level + 0.25 if they value honesty + 0.1 discipline`; if they do, they remember being
  lied to (`caught_contradiction`). People change their minds: answers older than a year do not count.
- **Growth:** an answer can set a flag that quest variants read (`answered`, or the answer's own
  `sets` flag), and advice can nudge the asker's personality a little (at most 0.1 an answer and 0.3
  in all), kept in the save.
- **Gossip:** an answer to a public question (about a clan, a person, the village) becomes something
  the village knows the player said, carried along ties like a small deed, so what you told one
  clan member reaches their household; an answer can also be a deed outright (`insulted_clan`).
  The next member of that clan you tell the opposite may know.
- **Pacing:** questions start at level 2 and open by their level, deeper ones later. An answered
  question is never asked again; only its follow-ups (`follow_up_of`, after `min_gap_days`) continue
  the thread. One question per person per day at most, one every 8 days per person at levels 2 and
  3, every 6 at 4 to 6, every 4 at 7 and up, and one a day across everyone. An unanswered question
  waits three days. Scenes can ask a question outside the budget (`ask_question`).
- **Keys** (`DialogueKeys.forQuestions(bank)`): `question.<id>`, `answer.<id>.<answer>`,
  `callback.answer.<id>.<answer>`, `answer.contradiction.<about>`, and the reactions
  `reaction.<label>` (with `reaction.<id>.<answer>` and `reaction.<label>.<archetype>` as optional
  variants).

**In the simulation** (a 32-question sample bank, `SampleQuestions`): over 60 hours a typical player
answers about 150 questions, one every 24 minutes of play, about 17 from each close friend (level
5+); a devoted player, with more close friends, about 10 each; contradictions happen a handful of
times and are usually noticed by close friends. The sample bank ran dry 51 times for the typical
player: **the real bank needs about 30 to 40 questions open to each close friend** (general ones,
their personality's, their role's), so roughly 150 general questions, 10 per personality and 10 to 15
per major character for the beta.

## 8. Data and quest hooks

Conditions (Core, from Shinobi Life): `{"ritual": ["role:teammate_b", "ramen"]}`,
`{"hangouts": ["role:teammate_b", 5]}`, plus every bond condition in BONDS.md. A quest can plan a
hangout as a step (`objective: talk` at the activity's anchor) and resolve it with `bond_event` and
`shared_moment`. Saves keep plans, invitations, rituals, highlights, life news and follow-ups with
each bond (`shinobi_life:bonds`, format 1; the fields are optional, so older saves load).

**In Minecraft** (the glue, after Phase 0): an invitation arrives as a speech bubble when they see
you, a note slipped under your apartment door (VF's Sealed Letter), or a visit; the journal lists
plans; at the time, the friend walks to the anchor on VF's routine (`CompanionController` follows
the player there) and the hangout plays as a short scene: seats at Ichiraku (VF tavern seating), a
fishing clip at the river, a spar ending at 30% health, a sky-gazing pose on the Rock. Highlights
are a line and an animation beat, shown once and remembered.

## 9. Pacing with time together

The 60-hour simulation now includes time together (`./gradlew :life:bonds:simulate`, seed
20261029): a devoted player asks someone every other day and accepts nine invitations in ten; a
typical player asks every four days and accepts six in ten; a reckless one rarely asks, rarely
accepts and sometimes does not show.

| Over 60 hours | Devoted | Typical | Reckless |
|---|---|---|---|
| Hangouts asked for / held | 94 / 195 | 47 / 106 | 20 / 9 |
| Invitations from friends / accepted | 134 / 119 | 101 / 71 | 12 / 3 |
| Stood someone up | 0 | 4 | 4 |
| Highlights / rituals formed | 25 / 16 | 8 / 5 | 0 / 0 |
| Their news heard and answered | 123 | 92 | 50 (mostly shrugged off) |
| Deeper conversations | 150 | 65 | 11 |
| Questions answered / per close friend | 172 / 10 | 153 / 17 | 70 / 21 (only 2 close friends) |
| Bonds at level 10 | 3 | 3 | 0 |

That is, for a typical player, about one hangout and one invitation every other in-game day (every
35 to 40 minutes of play) from the squad and friends, and a piece of someone's news about as often. The beta's friendship
gates still hold: across five seeds a devoted player always reaches the Ch 11 campfire talk, a
typical player in four of five (the one who missed had forgotten teammate_a's birthday), a reckless
one never (`TimeAndPacingTest`). Time together mostly widens the circle: classmates, the instructor
and the rival end the 60 hours one to three levels higher than without it.

## 10. Content plan

This is where the volume is. `DialogueKeys.required()` lists every pool the engine asks for, and
the dialogue compiler checks the bank covers them all; `DialogueKeys.optional()` lists the
per-personality variants that override a general pool.

| Content | Pools | Lines for variety | Lines |
|---|---|---|---|
| Required pools (greetings by level and state, memories, facts, feelings, goals, hangout asks, answers and outcomes, highlights and callbacks, conversation topics, life events and responses, follow-ups, moods, hook offers and outcomes) | 1,178 | 3 each | ~3,500 |
| Personality variants (16 archetypes on greetings, topics, life events and hangouts) | 7,952 possible | write the 20% that matter most, 2 each | ~3,200 |
| The cast's own voices (about 10 beta roles: their own greetings, hangout lines, highlights, topic answers and life events) | ~150 per character | 2 each | ~3,000 |
| Bond quests (one per classmate in Beta 1, two per teammate in Beta 2, one per teammate in Beta 3) and the squad beats | ~20 quests and 7 beats | scenes | ~30 scenes |
| Hangout scenes (Minecraft): anchors, seats, clips, the highlight beat | 22 activities | 1 scene each, ~10 highlight beats | 22 scenes |
| Clan customs, elders' requests, feud and match hooks | 25 clans, 9 hook types | | ~800 |
| Questions (general, per personality, per major character) with 2 to 4 answers each | ~350 | question, answers, callbacks | ~2,500 |
| **Beta's social layer, about** | | | **~12,500 lines, 50 scenes** |

VF's 5,898 existing lines stay as the residents' everyday talk; ours sit on top. Work order:
(1) the required general pools, so nothing is ever silent; (2) the beta cast's voices, since they
carry the story; (3) highlights and callbacks for the eight most common activities; (4) archetype
variants where playtesters notice repetition. Authoring rules from ROADMAP.md apply: name tokens
only, no literal names, `{name:<role>}` and `{given:<role>}`; dialogue text format as VF's
(`tools/dialogue/lines/naruto-*.txt`).

## 11. Open questions

- **How often should friends ask you things?** One question a day at most across everyone (about one
  every 24 minutes of play for a typical player). Is that the right rhythm next to hangouts and news?
- **How often should friends invite you?** About one invitation every other in-game day (every 35
  to 40 minutes of play) for a typical player. More makes the village feel alive; too many feels needy.
- **Ryo for hangouts:** who pays? Today the activity has a cost the glue charges the player. Should
  close friends sometimes treat you, or split it?
- **Group hangouts** cap at the activity's size (2 for a spar, 6 for a barbecue, 8 for a snowball
  fight). Should the squad dinner and festival nights be bigger?
- **Visible numbers:** should the book show "rituals" and "highlights" as a scrapbook page? (Proposed:
  yes, a page per friend with the highlights you share.)
