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
- Pronouns for rolled-look roles and the player: `{they:<role>}`, `{them:<role>}`,
  `{their:<role>}`, `{theirs:<role>}`, `{themself:<role>}`, plus verb agreement helpers
  (`{is:<role>}`, `{was:<role>}`, `{s:<role>}`), requested from the dialogue and character-creation
  sessions. Fixed-look roles have fixed pronouns ([WORLD.md](WORLD.md#conventions)).
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
| The nursery number "Nine" | Only the Ch 0 guard, the bound voice's slip (Ch 25), the Undercroft (N3), the leader (Ch 52), and the porter after Ch 28 |
| Anything about the archive's contents | After Ch 36 |
| The Quiet Ending, the renamed children | After Ch 36 (the purge), Ch 37 (the names); public lines after Ch 40 |
| Who the voice is | After Ch 39; innocent candidates' clearing lines only after Ch 40 |
| The array, the Hearthstone's purpose, the wick, the Hollow Crown | After Ch 49 |
| Who your parent is | After Ch 48; no character may say "your parent/mother/father" about the second or `fallen_parent` before it |
| The porter as the hand | After Ch 28 |
| teammate_b's parent in Yūgure | After Ch 26 |
| The Undercroft | After N3 (or never, if the branch is skipped; Ch 50 mentions "the old night unit" only if sworn) |

**Rotation gates.** A line that is only true for one bound candidate carries its condition
(`twist.traitor = medic`). Before Ch 39, no line may differ between rotations except the Ch 25
slip and the alibi scenes (ROTATIONS §1). Lineage lines that differ (`twist.lineage`) are only
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
