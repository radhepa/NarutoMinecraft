# `role:yugure_blade`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

## At a glance

| | |
|---|---|
| Role | The second's partner in her two-man cell; Yūgure's best swordsman; the player's recurring duel |
| Look (fixed) | About forty, broad-shouldered, a grey-streaked topknot, a face weathered like old wood. Dark blue-black clothes under the ash-violet cloak, sleeves tied back. A long, plain sword in a black lacquer scabbard he calls **Last Light**. Ink-dark lines hang in the air for a heartbeat after each cut. Under Transformation in Ch 15 to 17 he is a foreign Genin who writes left-handed |
| Pronouns | He / him |
| Clan | No clan. An ordinary family name of the Reed Marshes (rolled; Given Family order). From the **Reed Marshes**, a small country between two great nations' armies, burned in a border war when he was fourteen. The great villages' shinobi fought over the marsh roads and left |
| Rank | Missing-nin; Jonin-level kenjutsu |
| Archetype | `steadfast` leaning `stern` (warmth .1, bold .3, pride .3, discipline .8, open -.3) |
| Values | Loyalty, duty |
| Peeves | Cowardice, dishonesty |
| Dream | Protect what is left (the second; the marsh children in Yūgure) |
| First appears | Ch 14.2 (one cut that drops a bridge) |
| Duels | Ch 19.3 (with the sensei, seen), Ch 27.2, Ch 37.3, Ch 51.4 |
| Last appears | Ch 52.5 (he dies on the Rock); Ch 54.2 (his burial, if asked) |

## Arc

### Wants

To end the system that burned the Reed Marshes: the hidden villages that hire out war. The creed
of dusk is his faith, plainly held; he never asked what the Bonfire needed. Personally: to keep the
second alive. He has been her partner for twelve years and loves her the way a sword loves its
scabbard: without saying so, and without needing to.

### Fears

That he is a tool. He has been one twice (for the marsh lord who sold his village's road, and for
the leader) and fights with honour so that at least the cuts are his own.

### Secrets

| Secret | Who learns it |
|---|---|
| He has spared Leaf children before (he forfeited his prelim in Ch 17 rather than draw on a child in front of the Jonin, and because he would not) | The player, Ch 51.4 if they ask |
| He knows nothing of the Hollow Crown | He learns it on the Rock, Ch 52.5 |
| He knows the second lost a child (both lineages; he does not know the child in A is the player) | — |

### His thread

Through Thread Sight he has **one strong thread, to the second**, and nothing else: not to the
leader, not to Yūgure. The player can see it from Ch 27. In Ch 52.4, when the mirror tears her
hollow, the player sees his thread go taut and then dark; that is the moment he turns.

### How he changes

| Duel | Who he is |
|---|---|
| Ch 14 | A legend in a cloak: one cut, no fight. "Not with children" |
| Ch 19 | The sensei's equal; he pulls the second away when the sensei's kunai is at her throat |
| Ch 27 | He fights the player for the first time, as a teacher would: lets them pick up a dropped kunai. Stopped by the second |
| Ch 37 | He breaks into the archive for the Hearthstone on orders. Beaten, he warns the player of a trap if they try to capture him (`ans.yugure_blade.archive`) |
| Ch 51 | His best fight, on the rooftops at dusk. Beaten, he asks why the player never killed him (`ans.yugure_blade.why`). All answers send him to the Rock |
| Ch 52 | He sees the second torn hollow by the leader's mirror, understands what the Bonfire is, and turns his sword on the leader: "Dusk was supposed to end in morning." He dies |

## Dialogue brief

### Voice

- **Few words, all of them weighted.** He speaks in the rhythm of kata: a short line, a pause, a
  shorter line. No contractions in formal moments ("I will not").
- **Sword words for everything:** "edge", "draw", "sheathe", "line". He judges people by their
  stance.
- **Courteous to opponents.** He names the technique he is about to use if he respects you (from
  Ch 37), a marsh custom.
- **Never says:** the leader's name or title (he says "him"); a taunt; anything cruel to a child.

*Voice samples, not shipped lines:*

- (Ch 14, to his partner, as the bridge falls) "Not with children."
- (Ch 27) "Pick it up. I will not win against an empty hand."
- (Ch 37) "Your guard is your sensei's. Your feet are your own. Better."
- (Ch 51) "Why did you never finish it? You could have. Twice."
- (Ch 52.5) "Dusk was supposed to end in morning."

### Never reveal before

| Line or fact | Not before |
|---|---|
| His country's name and story | Ch 37 (if `ans.yugure_blade.country` is asked) |
| Any tenderness toward the second in words | Ch 52.5 |
| That he does not know the Bonfire's truth | Ch 51.4 (he says "I don't need to know what it burns. I know what it ends") |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | How it changes him |
|---|---|---|---|---|---|---|
| `ans.yugure_blade.fight` | Ch 27.2, mid-duel, as he lets the player pick up the kunai | "Why do you fight?" | for my friends, for the village, so no one takes me again, I don't know yet | Loyalty / duty; "I don't know yet" honours honesty (he respects it most) | Ch 51.4: "You told me once you fought for ___. Still?" | His Ch 51 stance: he fights harder against "for the village" (his enemy's reason), more gently against "for my friends" |
| `ans.yugure_blade.archive` | Ch 37.3 | (Player: let him go when beaten / try to capture him) | let_go, capture | — | Ch 51.4: if "let_go": "You let me walk out of the archive. I didn't understand it then" | Capture shows his honour: he warns of a trap he set |
| `ans.yugure_blade.country` | Ch 37.3, after the duel, as he backs into the dark | "Do you know what the Reed Marshes were?" | no (tell me), a country the great villages burned, should I? | Knowledge / honesty | Ch 52.5: if he told it, his last words include "Bury me facing the reeds" (the player can honour it in Ch 54.2) | Being asked lets him say the country's name out loud for the first time in the game |
| `ans.yugure_blade.why` | Ch 51.4 | "Why did you never kill me?" | kunai ("Because you let me pick up the kunai"), her ("Because she wouldn't want it"), see ("Because I want you to see what he's doing"); plus "She asked me to" if `ans.yugure_second.blade = yes` | Each sends him to the Rock | Ch 52.5: his turn is coloured by it (kunai: a salute to the player first; her: he goes to the second first; see: he looks at the array, then turns) | — |
| `ans.yugure_blade.sword` | Ch 52.5, dying | "Take it. Last Light. Don't hang it on a wall." | take it, bury it with you, give it to her | Duty / family | Ch 54.2 and the epilogue: the sword in your house's hall, in his grave, or at the second's side (if she lives) | — |

### What his lines are for

| Function | Where |
|---|---|
| **Combat teaching** | Each duel's dialogue teaches the player something about his style before he uses it (a telegraph in words) |
| **Theme** | A sincere believer, so Yūgure is not only the leader's lie |
| **Plot** | Ch 37 (the Hearthstone attempt), Ch 52.5 (the turn) |
| **Mood states** | `duel` (respectful), `wounded`, `turned` |
| **Pools** | `story.blade.<chapter>.<beat>`; duel barks `combat.bark.yugure_blade.<event>` (opening, landed hit, took hit, low health, yield) for the combat session |

### Variants

| Flag | Changes |
|---|---|
| `twist.lineage` | None before Ch 52; in A his last line to the second can be "Your child fights like you" (he has guessed) |
| `story.second.lives` | Nothing for him (he dies before Ch 53.6), but his grave scene reads it |

## New flags

- `ans.yugure_blade.fight` (friends, village, never_taken, dont_know)
- `ans.yugure_blade.country` (tell_me, burned, should_i)
- `ans.yugure_blade.sword` (take, bury, her)
