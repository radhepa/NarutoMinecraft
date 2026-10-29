# Dialogue briefs

> **SPOILERS: for developers only.** Part of the [story bible](STORY_BIBLE.md).

The handbook for writing the story's dialogue. Each character's own brief is the **Dialogue brief**
section of their file in [CHARACTERS/](CHARACTERS/); this page holds the rules every line follows,
the global spoiler gates, and the index of the questions characters ask the player.

## 1. Every line has a job

Tag every line (in the dialogue source, as a comment) with its function. A line with no job is cut.

| Tag | Job | Example |
|---|---|---|
| `plot` | Moves the story | The Fourth grants the stipend |
| `clue` | Carries a mystery thread; must be exact, because the case board quotes it | The councillor: "Stipend S-114. I saw to it myself." |
| `seed` | Plants something a later line pays | The sensei at the stone: "A teammate. The best of us." |
| `bond` | A relationship moment, a question, an answer remembered | teammate_a: "Did you feel that too?" |
| `callback` | Pays off an earlier answer or memory (reads a flag) | The Fourth quoting `ans.hokage_4.want` |
| `teach` | Teaches a system, in character | The instructor on the leaf exercise |
| `life` | Texture: humour, food, weather, the village going on | The cook calling out your order |
| `filler` | Small talk that keeps a character alive between beats; allowed, but in the character's voice and tied to their topics | teammate_b complaining about the pup's breakfast |

Filler is welcome (the user asked for it), but even filler says something about who is talking.

## 2. Tokens and pronouns

- Names: `{name:<role>}`, `{given:<role>}`, `{family:<role>}`, `{hokage:<n>}`, `{player}`. Never a
  literal name from the pools.
- Pronouns for rolled-look roles and the player (dialogue session's tokens): `{they:<ref>}`,
  `{them:<ref>}`, `{their:<ref>}`, `{theirs:<ref>}`, `{themself:<ref>}`, and agreeing verbs `{is:<ref>}`,
  `{has:<ref>}`, `{was:<ref>}` and the suffix `{s:<ref>}` ("{they:role:x} walk{s:role:x}"). The player is
  a ref too (`{they:player}`). Pets: `{pet:<ref>}`. Fixed-look roles have fixed pronouns
  ([WORLD.md](WORLD.md#conventions)).
- Answers: each `ans.<role>.<topic>` flag maps to the question format's `sets:`.
- The player's nursery number is the word **"Nine"**: it is written literally (it is not a name),
  and only in lines the gates below allow.

## 3. Global spoiler gates

No line anywhere may touch these before their gate, in any pool (greetings, gossip, news,
callbacks), for any character. Character briefs add their own.

| Fact | Gate |
|---|---|
| The word **Yūgure** | After `story.ch14.done` (the smuggler says it) |
| The word **Kagari** | After `story.ch19.named`; said aloud by Leaf characters only after Ch 22 (and only by the gated characters) |
| "Kindling" as a name for the gift | After Ch 25.3 |
| The nursery number "Nine" | Only the Ch 0 guard, the bound voice's slip (Ch 25), the Undercroft (N3), the leader (Ch 52), and the second's notes (Ch 48 A). The porter remembers nothing after Ch 28. No other line puts a count of nine near the player ("ten months", not nine) |
| Thread Sight in dialogue | A flicker means *hiding something*, steadily, never a lie in the moment. No character says "you'll know when I'm lying"; they say "you'll know I'm hiding something" |
| Anything about the archive's contents | After Ch 36 |
| The Quiet Ending, the renamed children | After Ch 36 (the purge), Ch 37 (the names); public lines after Ch 40 |
| Who the voice is | After Ch 39; innocent candidates' clearing lines only after Ch 40 |
| The array, the Hearthstone's purpose, the wick, the Hollow Crown | After Ch 49 |
| Who your parent is | After Ch 48; no character may say "your parent/mother/father" about the second or `fallen_parent` before it |
| The porter as the hand | After Ch 28 |
| teammate_b's parent in Yūgure | After Ch 26 |
| The Undercroft | After N3 (or, if the branch is not played, after Ch 47's orders reach the Seventh; Ch 50 mentions "the old night unit" only if sworn) |
| The leader's voice through the lost child | Ch 44.3 only ("Grow, little flame. I like your friends.") |

**Rotation gates.** A line that is only true for one bound candidate carries its condition
(`twist.traitor = medic`). Before Ch 39, no line may differ between rotations except the two items
in ROTATIONS §1, **Allowed divergences**: the Ch 25 slip line and the results of the four alibi
checks. Every other scene, vote, question, visit, flicker and line is identical in every save; a
candidate's held-back secret keeps their Thread Sight flicker on until Ch 39 or 40 in every save. Lineage lines that differ (`twist.lineage`) are only
allowed from Ch 48, except the persimmon on the sill (Ch 27), which shows no giver.

## 4. Questions for the player

The user's wish: friendship has questions and choices, and answers matter later.

- **Every major character asks** opinions, values, advice, their past and small confessions. Each
  character's file has a table: id, when, the question, the options, what each honours or tests,
  where it is remembered and how it changes them.
- **Answers are flags** `ans.<role>.<topic>` ([FLAGS.md](FLAGS.md)). Every one is read later at
  least once: a callback line, a changed scene, or an epilogue line.
- **No right answers.** Each option is something a decent person could say. The options differ in
  what they honour (the character's values, BONDS.md §5) and so in the meters, but more in **who
  the character becomes**.
- **Asked at the right depth.** Questions open with the bond's level (LIFE_TOGETHER.md §6): a
  question about someone's dream waits for level 6. Before that, it would be prying.
- **The player can ask back.** Most story characters also answer the same question when the
  player turns it around (a `talk.q.<role>.<topic>.back` line).
- **Remembered by others too.** Big answers can travel (a teammate tells the other), through the
  bond engine's gossip as a `told` memory, so a third character may quote you.
- **Unset defaults.** A question may never have been asked (it waited for a level or a bond quest
  the player skipped). Every read of an `ans.*` flag in a main-path scene has an `unset` line that
  assumes no answer ([FLAGS.md](FLAGS.md), "Unset defaults"). Write it with the same care: for
  most players it is the line they hear.
- **The index by chapter** is generated from the character files' question tables
  (`quests.py --questions`), so the tables stay the single source of truth. The "when" column of
  each table is what the index sorts by.

### The player's own choices (`ans.player.*`)

| Flag | Asked | Options | Read in |
|---|---|---|---|
| `ans.player.ch0.freed_boy` | Ch 0.3 | freed / not | Ch 34.1 (genin_1) |
| `ans.player.ramen` | Ch 1.4 | miso, salt, pork bone, whatever | The cook, friends, Ch 20.4, 45.2, 54.1 |
| `ans.player.intro` | Ch 1.5 | told, nowhere, joke | Ch 2.3 (the rival) |
| `ans.player.cord_given` | Ch 8.3 | handed, together | Ch 34.2, Ch 42.2 |
| `ans.player.paper` | Ch 11.3 | hid, sensei, teammate | Ch 14.4, 25.4 |
| `ans.player.foreign_team` | Ch 15 | what you noticed | Ch 18.1, Ch 20.3 (judging) |
| `ans.player.tester_heard` | Ch 23.3 | squad heard, aside | Ch 24.4, 25.2 |
| `ans.player.testify` | Ch 31.3 | for the Tobari, against the lockdown, the Fifth's right to fear | Ch 33.3, Ch 51a.1 |
| `ans.player.own_test` | Ch 34.2 | cord, rescue, scroll, night watch | The Genin's first bond quest |
| `ans.player.genin_flame` | Ch 34.3 | told, watched, reported | Reporting: genin_3 becomes the Undercroft's fallback in N5 |
| `ans.player.leaf_is` | Ch 35.4 | feeds you, trying, you choose | Ch 41.3 |
| `ans.player.archive_follow` | Ch 37.0 | followed, stayed | The sensei's and keeper's lines |
| `ans.player.council_testimony` | Ch 40.2 | the dead, the living, the silence | Ch 41.1 dedication, `side.j.roots` |
| `ans.player.parent_meet` | Ch 48 | three per lineage | Ch 53.5, Ch 55.2 |
| `ans.player.vouch` | Ch 49.1 | vouched, let her speak, silent | Ch 51a (the doubting council members watch her on the wall; the Seventh's line) |
| `ans.player.b_parent` | Ch 51a.4 | stood with b, let b choose | b's epilogue |
| `ans.player.leader_name` | Ch 54.3 | among, off, apart | The memorial; Ch 55.5 |
| `ans.player.speech` | Ch 55.2 | three of: the cord, the cord tag, the bowl, the names, the fire | Ch 55.2 |

### Where questions are asked

| Kind | Where | Example |
|---|---|---|
| Story question | In a chapter scene, a choice that sets `ans.*` | Ch 8.4, the sensei's lunch |
| Bond quest question | In a bond quest's heart scene | `bond.b1.classmate_a`: "as they are, or as they should be?" |
| Hangout question | A conversation topic during a hangout, at a level | teammate_b at Ichiraku, level 5: "What did you eat, in the camps?" |
| Life-event question | When they tell you their news | "Should I take the post?" |

## 5. The briefs

| Character | File |
|---|---|
| The sensei (captain, the Seventh) | [CHARACTERS/sensei.md](CHARACTERS/sensei.md) |
| The instructor | [CHARACTERS/instructor.md](CHARACTERS/instructor.md) |
| The medic | [CHARACTERS/medic.md](CHARACTERS/medic.md) |
| The Fourth Hokage | [CHARACTERS/hokage_4.md](CHARACTERS/hokage_4.md) |
| The Fifth Hokage | [CHARACTERS/hokage_5.md](CHARACTERS/hokage_5.md) |
| The Sixth Hokage | [CHARACTERS/hokage_6.md](CHARACTERS/hokage_6.md) |
| The fallen parent | [CHARACTERS/fallen_parent.md](CHARACTERS/fallen_parent.md) |
| teammate_a | [CHARACTERS/teammate_a.md](CHARACTERS/teammate_a.md) |
| teammate_b | [CHARACTERS/teammate_b.md](CHARACTERS/teammate_b.md) |
| The rival | [CHARACTERS/rival.md](CHARACTERS/rival.md) |
| classmate_c, classmate_d | [CHARACTERS/classmates.md](CHARACTERS/classmates.md) |
| The lost child | [CHARACTERS/lost_child.md](CHARACTERS/lost_child.md) |
| The keeper | [CHARACTERS/elder_keeper.md](CHARACTERS/elder_keeper.md) |
| The councillor | [CHARACTERS/elder_councillor.md](CHARACTERS/elder_councillor.md) |
| The librarian | [CHARACTERS/librarian.md](CHARACTERS/librarian.md) |
| The merchant | [CHARACTERS/merchant.md](CHARACTERS/merchant.md) |
| The porter | [CHARACTERS/porter.md](CHARACTERS/porter.md) |
| Yūgure's second | [CHARACTERS/yugure_second.md](CHARACTERS/yugure_second.md) |
| Yūgure's blade | [CHARACTERS/yugure_blade.md](CHARACTERS/yugure_blade.md) |
| Yūgure's leader | [CHARACTERS/yugure_leader.md](CHARACTERS/yugure_leader.md) |
| Minor recurring roles | [CHARACTERS/minor.md](CHARACTERS/minor.md) |

## 6. Work order for the dialogue session

1. **Beta 1** (Ch 0 to 7) story lines and the cast's beta greetings, by the beta's chapters; the
   questions asked in Beta 1.
2. **Beta 2 and 3** story lines, bond quests and questions.
3. The cast's own voices for LIFE_TOGETHER's pools (greetings by level, hangout lines, topics) for
   the beta roles.
4. Later arcs, chapter by chapter, once the beta has been played.
