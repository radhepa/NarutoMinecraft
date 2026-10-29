# `role:medic`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). A
> `twist.traitor` candidate: read [ROTATIONS.md](../ROTATIONS.md) §1 first.

## At a glance

| | |
|---|---|
| Role | The medic of the rescue squad; the hospital's young medic; a traitor candidate |
| Look | Classic: curated (young, clanless, hospital whites, ink-stained fingers, green ink). Varied: rolled; the green ink stain stays |
| Pronouns | *they*; `{they:medic}` and the rest |
| Clan | Classic: clanless |
| Rank | Chunin medic → head of children's care (Jonin arc) |
| Archetype | Classic: **meticulous** (discipline .8; values duty, knowledge) |
| Peeves | Lateness, recklessness |
| Dream | *Heal people*; specifically, children from the camps |
| Notation | The hospital intake ledger: pulse counts in green ink (`p 88 / 112`) with a tiny folded-crane stroke |
| First / last | Ch 0 (the sample) / Ch 55 epilogue (treating the lost child, or in a cell) |

## Arc

### In every save

The medic was a nursery-age orphan once: an orphanage on the border burned when they were seven;
cloaked strangers pulled them out three days before the Leaf arrived and kept them a month in a
camp, kindly, before leaving them at a Leaf outpost. They never knew who the strangers were.
They became a medic to be the person who arrives in time. They test every rescued child (the Ch 0
sample) because the hospital found that camp children carry chakra injuries no one sees.

**Wants.** To be the one who arrives in time. **Fears.** Being too late again; being owed to
anyone. **Habit.** Writes everything down. Folds paper cranes when anxious; the crane stroke on
each record is a tiny promise ("this one gets better").

### If bound (`twist.traitor = medic`)

They learned who the strangers were at nineteen, when a letter came: "You were ours once. We need
only numbers." For six years they sent readings, telling themselves numbers hurt no one and that
the people who saved them were saving others. They sent your Ch 0 reading. They visited after the
flare (Ch 3) to report it (and were glad the instructor gave them a reason). They tore the intake
pages on the night shift (a twenty-minute gap in the surgery roster). Then the lost child came back
hollow (Ch 24): they had measured her, years ago, from a ledger at a border clinic. That broke them.
By Ch 25 they are half ready to be caught; the slip ("better than ninety, for a ninth—") is almost
a confession.

### If innocent

Everything in "every save" is true and nothing else. The visit was the instructor's request. The
pages were torn by the night patient (the Ch 11 smuggler) while they were in surgery all night.
The diverted supplies' requisition was forged (`side.b3.hospital_supplies` clears them).

**What they know and when.**

| Knowledge | From | Bound only? |
|---|---|---|
| Your chakra reading | Ch 0 | Both |
| The flare (if `ans.medic.flare = told`) | Ch 3 | Both |
| Your nursery number "Nine" | Before Ch 0 (Yūgure's lists) | **Bound only** |
| The strangers who saved them were Yūgure | Age 19 | **Bound only**; innocent: Ch 40, when the council makes the nurseries public, they realise it and come to you shaken |
| The lost child was "theirs" (measured) | Ch 24 | Bound only |

**How they change.**

| Arc | Change |
|---|---|
| 1 Cinders | The careful adult who writes you down |
| 2 Paper Trail | Treats the squad's injuries with scolding; the night shift side quest |
| 3 Dusk | Runs the stadium triage in Ch 19 |
| 4 Embers | Treats you after the border post; the slip (bound) or the parallel kind line (innocent); treats the porter (Ch 28) |
| 5 Ashes | Bound: unmasked (Ch 39). Innocent: cleared (Ch 40), asks to care for the lost child |
| 6 Night Watch | Treats the lost child after N6 (innocent; or from custody, bound, if you allow it) |
| 7 Last Bonfire | Runs the war hospital (innocent or turned); bound and arrested: asks to be let out to work; the ruling (Ch 55) |

**Endings.**

| | Bound | Innocent |
|---|---|---|
| Reveal | The hospital roof at dawn, green ink on their fingers ([ROTATIONS.md](../ROTATIONS.md)) | Cleared in Ch 40 |
| Turned | Keeps sending readings, now false; in Ch 51 they lead a hollow-fighter's wounded away from the false anchors | — |
| Arrested | Asks only to treat the lost child; the Hokage's ruling in Ch 55 (pardon / exile / service) | — |
| Wrongly accused (innocent) | — | Detained two days; `bond.c.wrongly_accused.medic`: they ask you to fold a crane with them before they'll speak |

## Dialogue brief

### Voice

Precise, quick, a little stern; medical words used correctly and then translated. Scolds out of
care ("You walked on that? For how long? Sit."). Counts things aloud under stress. Never jokes about
injuries; jokes dryly about everything else. Never says "it's fine" about a body.

Voice samples, not shipped lines:
- "For the records. Everyone gets one."
- "Anything strange happen today? Strange is a medical term. Sort of."
- "Your pulse is good. Better than you deserve, the way you climb."
- "Sit. Not there. There."
- (innocent, Ch 40) "They were kind to me. The ones who pulled me out. I think they were them."

### Topics they care about

| Topic | What they say |
|---|---|
| Food (1) | Lectures on eating; secretly lives on dango |
| Their hobby (2) | Paper cranes; there is a jar of a thousand in their room |
| Their family (4) | "The hospital." Then, at level 5, the burned orphanage |
| Their values (5) | "Come in early. Not late. Early." |
| Advice (5) | Practical, about sleep and grief; about the lost child: "Hollow isn't empty. It's quiet" |
| Their dream (6) | A children's ward for camp children, with windows that open |
| Worries (7) | Bound: that someone they measured was hurt (said obliquely before Ch 39). Innocent: that they will be too late |

### Never reveal before

| Fact | Not before |
|---|---|
| "Nine", the ninth, any count of nine near you | **Only the bound save's Ch 25 slip line**; never in any other save or scene before Ch 39 |
| Their own orphanage rescue by strangers | Level 5 (both saves; the story is the same) |
| That the strangers were Yūgure | Bound: Ch 39. Innocent: Ch 40 |
| That they measured the lost child | Bound only, Ch 39 |
| That the instructor asked them to visit | Ch 25 (both saves) |
| Any line that is warmer or colder in one save than another | Never before Ch 25: beta lines are identical in every save |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes them |
|---|---|---|---|---|---|---|
| `ans.medic.flare` | Ch 3.5 | "Anything strange happen today?" | told / silent | Honesty | Ch 39 (bound: "You told me. I wrote it down. I sent it.") / Ch 40 (innocent: "You told me, and I kept it to myself. I'm glad.") | — |
| `ans.medic.early` | Level 2, a hospital visit after an injury | "Why did you wait so long to come in?" | I didn't want to bother anyone / I thought it'd heal / I didn't trust the hospital | Duty; tests their peeve | Ch 25: they greet you with your answer | "Didn't trust": they show you their ledger and how it works (seeds the notation again, every save) |
| `ans.medic.camp_pain` | Level 4, Ch 9 to 14 | "Some camp children say nothing hurts. Do you?" | yes / sometimes / I'm learning not to | — | The war hospital (Ch 51): they ask you to talk to the Valley children with your answer | Their ward design changes (a quiet room) |
| `ans.medic.owed` | Level 5, Chunin | "If someone saved your life, would you owe them anything they asked?" | yes / only what's right / nothing; it was a gift | Tests their deepest fear | Bound Ch 39c ("You said only what's right. I didn't ask myself that"); innocent Ch 40 | Innocent: they decide they owe the strangers nothing and help hunt the nurseries |
| `ans.medic.crane` | Level 6, a dango hangout | "I fold one for every patient. Want to fold one for someone?" | for the lost girl / for my teammate / for me | — | Ch 47 or N6: the crane is on her pillow | — |
| `ans.medic.lost_child` | Ch 25 (after Ch 24) | "She was hollow. Do you think she can come back?" | yes, I'll bring her / I don't know / not without help | Kindness | N6 / Ch 47 | Bound: the question is their confession in disguise |
| `ans.medic.ruling` | Ch 55 (bound and arrested) or Ch 40 (innocent) | Bound: "What should happen to me?" Innocent: "Would you have believed it, if it was me?" | Bound: pardon / service / exile. Innocent: yes / no / I'd have checked first | Honesty | Bound: weighs on the Ch 55 ruling | — |

### What their lines are for

- **Clue:** every beta line identical across saves; the Ch 25 line is the only fork.
- **Bond:** the scolding is care; questions about pain open the player's own backstory.
- **Plot:** stadium triage, the porter, the lost child's care, the war hospital.
- **Pools:** hospital greetings (by injury), triage barks (Ch 19, 51), post-reveal (bound) cell
  visits, cleared (innocent) greetings.

### Variants

- **Bound vs innocent:** described above. All divergence is from Ch 25 on.
- **Varied archetypes:** keep the precision and the green ink; a gentle roll scolds softly, a
  fiery roll scolds loudly.
- **`twist.fourth_fate` crippled/taken:** they treat the Fourth; in the bound save the reveal
  scene never needs him (they are on the roof alone).

## New flags

- `ans.medic.early` (bother, heal, distrust)
- `ans.medic.camp_pain` (yes, sometimes, learning)
- `ans.medic.owed` (yes, right, nothing)
- `ans.medic.crane` (lost_child, teammate, self)
- `ans.medic.lost_child` (yes, unknown, help)
- `ans.medic.ruling` (bound: pardon, service, exile; innocent: yes, no, checked)
