# `role:hokage_6`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

## At a glance

| | |
|---|---|
| Role | The Sixth Hokage, named Ch 32; opens the archive (Ch 36), makes the Quiet Ending public (Ch 40), resigns (Ch 42) |
| Look (fixed) | A soft-spoken man of about fifty-five with long pale-blond hair in a loose tail, a gentle lined face, a sprig of a flower always in his robe (it changes with the season and the day's mood; the language of flowers). Carved on the Rock in Ch 42 |
| Pronouns | He / him |
| Clan | Yamanaka |
| Rank | Jonin; for twenty years the Leaf's chief interrogator, then head of the sensor corps |
| Archetype | `thoughtful` leaning `gentle` (warmth .5, bold -.2, pride -.2, discipline .5, open .2) |
| Values | Honesty, kindness |
| Peeves | Dishonesty, cruelty |
| Dream | Be a great teacher (he wanted to teach at the Academy and was too good at reading minds to be allowed to) |
| First appears | Ch 22 (in the sensor corps, the Fifth's deputy; one line, kinder than hers). His nephew `squad3_c` is the sensor who flags the player |
| Named | Ch 32.1 |
| Last appears | Ch 42 (resigns); Ch 51 (at the Academy with the instructor, as a teacher at last); Ch 55 |

## Arc

### Wants

The truth said out loud. Twenty years of reading minds taught him that every buried thing in a
person comes back as something worse; he thinks villages are the same. He is the first Hokage who
**wants** the archive open.

### Fears

That he is a coward who prefers other people's minds to his own decisions. That he will hand the
truth to a village that cannot bear it, and break it.

### Secrets

| Secret | Who learns it |
|---|---|
| He read the keeper's mind once, twenty years ago, by accident, and has known since then that there was a buried clan. He never acted | The player, Ch 36 (he confesses it to the keeper in front of them) |
| He does not want to be Hokage; he plans to resign the moment the truth is out | The player, Ch 40 if `friendship [hokage_6, 5]`, else Ch 42 |

### How he changes

| Stretch | Who he is |
|---|---|
| Ch 32 | A reluctant Hokage who asks more questions than he answers |
| Ch 33 to 36 | The player's protector at the council; he orders or allows the archive open |
| Ch 40 | The bravest thing he ever does: he says it all to the clan heads |
| Ch 42 | He resigns to take responsibility for the Leaf's buried crime and names the sensei. The council is **contested**: it balks at naming a Hokage who signed the Ash Road field report. He does not overrule them; `squad5_a`'s public stand ("I'm with them") carries the vote. His line after: "I could have ordered it. It's better that they chose." |
| Ch 51 | He teaches at last: at the Academy with the instructor, with children, during the assault |

## Dialogue brief

### Voice

- **Soft and slow; he rarely finishes a sentence when the listener has understood it.** He leaves
  silences on purpose (an interrogator's habit he is not proud of).
- **The language of flowers.** He gives flowers instead of praise. His robe's flower is a mood
  signal the dialogue can name ("a sprig of white camellia today").
- **He never reads the player's mind and says so, early** (Ch 32): "I won't look. You have my word."
  He keeps it.
- **Never says:** an order without a reason; "I know what you're thinking" (it would be true).

*Voice samples, not shipped lines:*

- (Ch 32.1) "I won't look inside your head. You have my word. Though I'd like to be invited, one day."
- (Ch 33.3) "A gentle question. What is a Hokage for?"
- (Ch 36.1) "Open it, keeper. We've both known for twenty years."
- (Ch 40.2) "We did not lose a clan. We ended one. I'll say it again so it is in the record."
- (Ch 42.1) "You told me a Hokage is for... I've decided you were right. Which means it isn't me."

### Never reveal before

| Line or fact | Not before |
|---|---|
| That he knew of a buried clan for twenty years | Ch 36 |
| The word Kagari | Ch 36 |
| His plan to resign | Ch 40 (at level 5) / Ch 42 |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | How it changes him |
|---|---|---|---|---|---|---|
| `ans.hokage_6.got_right` | Ch 32.1, after his naming | "What did the Fifth get right? I want to keep it." | she watched closely, she took responsibility, nothing | Kindness / honesty | Ch 33 to 40: he keeps a sensor watch (watched), or makes taking responsibility his habit (it is what he does in Ch 42); "nothing" makes him visit her and come back with an answer of his own | A small policy colour across the Jonin arc |
| `ans.hokage_6.for` | Ch 33.3 | "What is a Hokage for?" | protect (the village), forgotten (the people the village forgets), carry (what no one else should) | Each honours a different value | Ch 42.1 (his resignation answers it: protect: "and I can't protect it from what it did"; forgotten: "and the forgotten deserve a Hokage who didn't forget them"; carry: "and this one should be carried by someone else") | Shapes the resignation speech |
| `ans.hokage_6.read` | Ch 36.1, at the door | "Should I read the keeper to be sure he's showing us everything? He'd let me. I'd hate it." | yes, no (trust him), ask him first | Honesty vs kindness | Ch 36.4: if "no", the keeper volunteers the forged report unasked; if "yes", the keeper's trust in the player drops (`went_over_their_head`) and the Sixth finds the Ash Road report the keeper had kept separate; if "ask", both | The archive's order of revelations |
| `ans.hokage_6.names` | Ch 40.1 | How much to say at the council | everything, all_but_names, families_decide | Honesty vs kindness | Ch 46 recruitment; the `side.j.roots` wave | Shapes the council speech |
| `ans.hokage_6.flower` | A hangout or talk at `friendship 4`, Jonin arc | "If you had to apologise to someone with one flower, which would you send?" | something honest and plain, something beautiful, I'd go myself | Honesty / kindness | Ch 40.2: he wears the flower your answer suggests when he speaks to the clan heads; Ch 42: he sends you that flower | — |
| `ans.hokage_6.leave` | Ch 42.1 | "Will you think less of me for leaving?" | no, a little, I'd think less if you stayed | Honesty | Ch 51: at the Academy, "You said ___. I'm teaching. It turns out that's what I'm for" | "I'd think less if you stayed" makes him laugh out loud for the only time |
| `ans.hokage_6.rumour` | Ch 33, after the review | "The rumours about your blood. Shall I stop them, or will you answer them yourself?" | stop them; let me answer; let them talk | Honesty vs kindness | Ch 40.2 (whether the council has heard the player speak before) | "Let me answer" gives the player a small extra testimony line in Ch 40 |
| `ans.hokage_6.letter` | Ch 36.7, after the Third's letter | "She asked whoever came to say it for her. Will you, or shall I?" | you; me; together | Duty | Ch 40.2: who speaks first at the council | — |
| `ans.hokage_6.certain` | Ch 38.6, before the accusation (if the player brings it to him) | "Are you certain? Certain enough to ruin them if you're wrong?" | yes; no, but I have to; help me be sure | Honesty | Ch 40.3: if an innocent was accused after "help me", he shares the blame publicly | "Help me" lets him point out one missing proof (a hint, not the answer) |
| `ans.hokage_6.last_line` | Ch 41, before the unveiling | "The memorial needs a last line under the names. What should it say?" | their names were theirs; we did this; come home | Theme | The memorial's inscription for the rest of the game | — |
| `ans.hokage_6.children` | Ch 51a, at the Academy | "What do I tell the children is happening?" | the truth; that we're keeping them safe; a story | Kindness / honesty | Epilogue: an Academy child repeats what he told them | — |

### What his lines are for

| Function | Where |
|---|---|
| **Plot** | The archive and the council |
| **Theme** | Question two (is knowing enough, or must it be said?) in its purest form: he knew, and finally says it |
| **Protection** | Ch 33 and the Jonin arc: his questions to the council deflect the blood rumours |
| **Mood states** | `reluctant`, `resolved` (Ch 40), `relieved` (after Ch 42) |
| **Pools** | `story.hokage_6.<chapter>.<beat>`; bond pools in his voice; a flower-of-the-day line pool (`talk.hokage_6.flower.<season>`) |

### Variants

| Flag | Changes |
|---|---|
| `story.accused` / `story.traitor.fate` | Ch 40: if an innocent was accused, he apologises to them in front of the council |
| `elder_keeper` trust (Ch 36 path) | Whether he orders the archive open or is invited |
| `twist.lineage = fallen` | Ch 36.6: he holds the Ash Road report out to the sensei, not the player |

## New flags

- `ans.hokage_6.got_right` (watched, responsibility, nothing)
- `ans.hokage_6.read` (yes, no, ask)
- `ans.hokage_6.flower` (honest, beautiful, go_myself)
- `ans.hokage_6.leave` (no, a_little, if_stayed)
- `ans.hokage_6.rumour` (stop, answer, let_talk)
- `ans.hokage_6.letter` (you, me, together)
- `ans.hokage_6.certain` (yes, have_to, help_me)
- `ans.hokage_6.last_line` (theirs, we_did, come_home)
- `ans.hokage_6.children` (truth, safe, story)
