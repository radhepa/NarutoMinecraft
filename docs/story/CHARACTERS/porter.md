# `role:porter`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Fixed in every
> save: the porter is always **the hand** ([ROTATIONS.md](../ROTATIONS.md) §1).

## At a glance

| | |
|---|---|
| Role | `role:porter`, a porter for the furniture shop and the post |
| Look | Fixed: a lanky young man (~22), cropped brown hair, a wooden carrying frame on his back, a plain work tunic, a cloth wrap on his right palm over a burn scar |
| Pronouns | He / him |
| Clan | No clan; a cover name (rolled given name and an ordinary family name from the pool). His real name is lost |
| Rank | Civilian (in truth, a nursery child trained as an agent) |
| Archetype | `gentle` (warmth .7, bold −.4, pride −.5, discipline .1, open .3) |
| Values | kindness, family (the "family" that rescued him) |
| Peeves | cruelty, rudeness |
| Dream | "find where they belong" |
| First appearance | Ch 1 (carries your futon in; fixes your door) |
| Last appearance | Ch 55 epilogue (sweeping the shrine) |

## Arc

**Who he is.** A nursery child "rescued" by Yūgure at eight from a burning orphanage (the kind of
rescue the medic remembers too), raised in a hearth's care, sent into the Leaf at sixteen (Y-6) to take over from the first hand, an old east-road
carter who died in a road accident that year, under a
cover name to carry. He carries for everyone: the furniture shop, the post, the library's returns
cart, the hospital's linen, the council's letter bags, crates for merchants' carts at the east gate.
He is genuinely kind. He also laid eighty-one cinder seals under what he carried and scratched the
sinking sun on the player's door.

**Wants.** To belong to the people who saved him; to be a good son to the leader. And, without
admitting it, to be a porter: a man people say good morning to.

**Fears.** Being sent away; being asked to hurt someone in front of him (he can lay a seal under a
doorstep, but he has never seen what it does).

**Secrets.** He is the hand: he carries the voice's messages out and Yūgure's orders in, steals what
the hearths ask (the cut page, the ledger pages, the borrowed seal), and lays the array. He does not
know the Hollow Crown; he was told the marks are "so we can find our friends' homes".

**What he knows.** The voice's identity (he cannot say it: a cinder seal in his palm, under the burn scar, burns his memory out if he tries); the array's
anchors (in his ledger, as deliveries); the Ch 0 raid's muster (he loaded the raid squad's supply
crates and reported it himself: the hand, not the voice, warned the leader). He carries the voice's reports sealed
and has never read them.

**How he changes.**

| Arc | He is |
|---|---|
| Cinders | A friendly face: carries furniture in, fixes the door (Ch 1), says good morning in the stairwell (Ch 4), stacks the graduation benches (Ch 7). The rooftop figure (Ch 4) |
| Paper Trail and Dusk | In the background of every errand: the library, the hospital, the council gallery, the east gate |
| Embers | Lays the last anchors; caught in Ch 28 |
| After Ch 28 | Empty and gentle; sweeps the shrine; smiles at the player without knowing why |

**Ch 28.** Caught on the Rock's slope after the second rooftop chase. The Classic Morino
interrogator (`role:sensei_4`) reaches him first and tries to hold the seal back, and cannot. He tries to name the voice;
the cinder seal in his palm flares under the burn scar; he says the same line in every save: "Years in its
own hand. All of them in its own hand." Then the seal burns his memory away. His delivery ledger, found in
his room, is the array map (Ch 49).

**Ch 28.5.** In his room, `role:squad5_c` stands in the doorway: "He carried my sister's cot up four
floors." (`shared_moment bond.squad5_c.porter`.) It is the only time anyone in the village says what
the porter was to them, and it is true in every save.

**Ending.** He lives, remembering nothing before Ch 28. The shrine priest takes him in. In the Road
to Hokage he sweeps the restored Kagari shrine (or the village shrine if the player founded their own
clan). In the epilogue he fixes a sticky door at the clan hall and says, puzzled, "Doors should open
for you," and does not know where the words came from.

## Thread Sight and the porter

The porter is never bonded to the player at 6 or more before Ch 28 (his friendliness stays at
levels 2 to 4: he keeps people at a carrying distance), so the player can never see his thread to
the voice. After Ch 28 his memory is burned and the tie is gone. If the player rebuilds a friendship
with him afterwards (`ans.porter.after = now`), his thread at 6+ is clear and steady: nothing hidden.

## Dialogue brief

### Voice

- **Register:** shy, polite, short sentences; a working man's good mornings.
- **Habits:** always carrying something; offers to carry yours; apologises to doors he bumps.
- **Tics:** pauses before saying his own name (he has to remember his cover name); hums while working,
  never the watch-fire song.
- **Never says:** anything about where he is from; "Yūgure"; a name for the voice (he physically
  cannot).
- **After Ch 28:** slower, simpler, happy; repeats small kindnesses; no memory of the player except a
  feeling.

*Voice samples, not shipped lines:*

- (Ch 1) "First home? I'll fix that sticky door. Doors should open for you."
- (Ch 4) "Morning. Heavy one today. Who orders a stone basin to the fourth floor?"
- (Ch 28) "Years in its own hand. All of them in its own hand." (Every save.)
- (after Ch 28) "Do I know you? I feel like I carried something for you once."

### Topics they care about

| Depth | Topics |
|---|---|
| 0 to 2 | The weight of things; stairs; the furniture shop's orders; the weather for carrying |
| 3 to 4 | What makes a home a home; the families he delivers to |
| 5 | "Family" (he means the hearths, and talks about them as if they were a large kind household in the east) |

### Never reveal before

| Secret | Gate |
|---|---|
| That he is Yūgure | Ch 28 |
| That he was the rooftop figure in Ch 4 | Ch 28 (the gait is shown, never said) |
| The marks' purpose | Ch 49 (and he never knew it) |
| The voice | Never by him: the line "in its own hand" is all |

### Questions for the player

| Id | When | Question | Options | Remembered | Changes him |
|---|---|---|---|---|---|
| `ans.porter.met` | Ch 1 | (The player thanks him or asks his name) | Asked / not | Asked: he hesitates over his cover name; at Ch 28 the player can say "That isn't your name, is it?" | — |
| `ans.porter.home` | Level 2 (stairwell, Paper Trail) | "What makes a place a home, do you think? I carry so many things into so many rooms." | The people / your own things / a door that opens for you | Ch 28 (holding him), epilogue | "A door": in the epilogue he fixes your clan hall's door unasked |
| `ans.porter.family` | Level 3 (Chunin, before Ch 28) | "If the people who saved you asked you to do something you didn't understand, would you do it?" | Yes, I'd trust them / I'd ask why / It depends what it costs others | Ch 28: "You said ask why. I never asked." | "Ask why" or "costs others": he hesitates on the roof in Ch 28 and lets himself be caught a moment sooner |
| `ans.porter.heavy` | Level 2 | "What's the heaviest thing you've ever carried?" | Someone / a secret / nothing yet | Ch 28 | "Someone": he says "Me too" and doesn't explain (the children in carts) |
| `ans.porter.end` | Ch 28.4 | (Hold him while it burns / call for the medic / ask one more question) | hold, medic, ask | Epilogue: "Doors should open for you" if held | Held: he keeps the feeling of the player after the burn; his post-28 greeting to the player is warmer |
| `ans.porter.after` | After Ch 28, level 1 (re-met) | "Did we know each other? You look at me like we did." | Yes, you were kind to me / No / We will now | Shrine scenes, epilogue | "We will now" restarts his bond at 1 and lets it grow (a new friendship with the man he became) |
| `ans.porter.carry` | Ch 4 (stairwell, level 1) | "Want to take the other end? It's a basin. It's heavier than it looks." | Help / not today | Kindness; a small shared act (`favor`) | After Ch 28 he asks again, and if you helped then: "I feel like we've done this" | Helping keeps his level at 3 by Ch 28 (never 6) |
| `ans.porter.shrine` | After Ch 28, level 2 (at the shrine) | "Do you think the people who lived here were happy, once?" | Yes, before / they will be again / I don't know | Grace | Ch 46: he sweeps the restored shrine and repeats the answer to new members | — |

### What their lines are for

- **Functions:** life (a friendly face in the beta), clue (the gait, the door, his presence at every
  source), plot (the hand, the array), tragedy (the burned memory), grace (the epilogue).
- **Mood states:** `cheerful` (before Ch 28), `caught` (Ch 28), `empty` (after), `content` (Road to
  Hokage).
- **Pools:** `npc.porter.*` (greetings while carrying), `talk.q.porter.<topic>`, `npc.porter.after.*`.

### Variants

- Fixed in every save and both modes; name rolled (a cover name).
- He steals for the voice whoever it is: the cut page, the ledger pages, the borrowed seal, the dead
  drops. His Ch 28 line is identical in every rotation.

## New flags

`ans.porter.home`, `ans.porter.family`, `ans.porter.heavy`, `ans.porter.after`. Also: `ans.porter.carry`, `ans.porter.shrine`.
