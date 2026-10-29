# `role:yugure_blade`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

## At a glance

| | |
|---|---|
| Role | The second's partner: "the only pair he ever allowed" (every other Yūgure unit is a hearth of three or more); Yūgure's best swordsman; the player's recurring duel |
| Look (fixed) | About forty, broad-shouldered, a grey-streaked topknot, a face weathered like old wood. Dark blue-black road clothes, sleeves tied back, a soot sinking sun on the inside of his wrist; an ash-violet scarf over his face when they mean to be seen. A long, plain sword in a black lacquer scabbard he calls **Last Light**. Ink-dark lines hang in the air for a heartbeat after each cut. In Ch 15 to 19 he enters the Leaf openly as an adult escort of a real foreign team, under false papers; he writes left-handed |
| Pronouns | He / him |
| Clan | No clan. An ordinary family name of the Reed Marshes (rolled; Given Family order). From the **Reed Marshes**, a small country between two great nations' armies, burned in a border war when he was fourteen. The great villages' shinobi fought over the marsh roads and left |
| Rank | Missing-nin; Jonin-level kenjutsu |
| Archetype | `steadfast` leaning `stern` (warmth .1, bold .3, pride .3, discipline .8, open -.3) |
| Values | Loyalty, duty |
| Peeves | Cowardice, dishonesty |
| Dream | Protect what is left (the second; the marsh children in Yūgure) |
| First appears | Ch 14.2 (one cut that drops a bridge) |
| Duels | Ch 19.3 (with the sensei, seen), Ch 27.2, Ch 37.3, Ch 51b (the last; he turns after it) |
| Last appears | Ch 52 (he fights the leader beside the player and is wounded); Ch 54 (in custody); the epilogue (guarding the shrine or the second's grave) |

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
| He has spared Leaf children before: in the Forest of Death (Ch 16), as an escort, he turned two Leaf Genin teams away from a ravine trap he had found instead of letting it spring | The player, Ch 51b if they ask |
| He knows nothing of the Hollow Crown | The player tells him after their last duel (Ch 51b), or he guesses it from the array lighting; he sees it with his own eyes on the Rock (Ch 52) |
| He knows the second lost a child (both lineages; he does not know the child in A is the player) | — |

### His thread

He has **one strong thread, to the second**, and nothing else: not to the leader, not to Yūgure.
It is a scripted exception (a `thread_floor`) shown **only in Ch 52**: on the Rock the player sees
it run from him to her, and in Ch 52.4, when the mirror tears her, it goes taut. Before Ch 52 the
player sees no thread of his (he is not bonded to the player at 6+).

### How he changes

| Duel | Who he is |
|---|---|
| Ch 14 | A legend in a scarf: one cut, no fight. "Not with children" |
| Ch 19 | The sensei's equal; he pulls the second away when the sensei's kunai is at her throat |
| Ch 27 | He fights the player for the first time, as a teacher would: lets them pick up a dropped kunai. Stopped by the second |
| Ch 37 | He breaks into the archive for the Hearthstone on orders. Beaten, he warns the player of a trap if they try to capture him (`ans.yugure_blade.archive`) |
| Ch 51b | His best fight, on the rooftops at dusk. Beaten, he asks why the player never killed him (`ans.yugure_blade.why`). **He turns here**, on the player's answer, before the second falls: he learns (or guesses, from the array lighting) what the Bonfire needs, and goes to the Rock to stop the leader |
| Ch 52 | He fights the leader beside the player. When the mirror tears the second (52.4) he says "Dusk was supposed to be for them, not for her," and throws himself at the leader; he is wounded and **lives**. After the war he is taken into custody. In the epilogue he asks to guard the shrine (or the second's grave, if she died), Last Light at his side or not by `ans.yugure_blade.sword` |

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
- (Ch 52) "Dusk was supposed to be for them, not for her."
- (Epilogue, at the shrine gate) "I keep the door. Nobody asked me to. That is the point."

### Never reveal before

| Line or fact | Not before |
|---|---|
| His country's name and story | Ch 37 (if `ans.yugure_blade.country` is asked) |
| Any tenderness toward the second in words | Ch 52 |
| That he does not know the Bonfire's truth | Ch 51b (he says "I don't need to know what it burns. I know what it ends") |

### Questions for the player

Every main-path read below has an unset default: the neutral version of the line, or no callback.

| Id | When | Question | Options | Honours / tests | Remembered | How it changes him |
|---|---|---|---|---|---|---|
| `ans.yugure_blade.fight` | Ch 27.2, mid-duel, as he lets the player pick up the kunai | "Why do you fight?" | for my friends, for the village, so no one takes me again, I don't know yet | Loyalty / duty; "I don't know yet" honours honesty (he respects it most) | Ch 51b: "You told me once you fought for ___. Still?" | His Ch 51 stance: he fights harder against "for the village" (his enemy's reason), more gently against "for my friends" |
| `ans.yugure_blade.archive` | Ch 37.3 | (Player: let him go when beaten / try to capture him) | let_go, capture | — | Ch 51b: if "let_go": "You let me walk out of the archive. I didn't understand it then" | Capture shows his honour: he warns of a trap he set |
| `ans.yugure_blade.country` | Ch 37.3, after the duel, as he backs into the dark | "Do you know what the Reed Marshes were?" | no (tell me), a country the great villages burned, should I? | Knowledge / honesty | Epilogue: if he told it, he asks to plant marsh reeds by the shrine he guards | Being asked lets him say the country's name out loud for the first time in the game |
| `ans.yugure_blade.why` | Ch 51b, after the last duel | "Why did you never kill me?" | kunai ("Because you let me pick up the kunai"), her ("Because she wouldn't want it"), see ("Because I want you to see what he's doing"); plus "She asked me to" if `ans.yugure_second.blade = yes` | Each sends him to the Rock | Ch 51b, at once: his turn is coloured by it (kunai: a salute to the player, then he sheathes; her: "Then I will go to her"; see: he looks up at the array lighting on the Rock, then turns; she-asked: he is silent a long time, then goes). Unset: "Then go. I will follow" | — |
| `ans.yugure_blade.sword` | Ch 54, as he is taken into custody | "Take it. Last Light. I will not need it where they are putting me. Don't hang it on a wall." | take (keep it), back ("Give it back to you when they let you out"), her ("Give it to her"; if she died, "Lay it on her grave") | Duty / family | The epilogue: the sword in your house's hall, at his side guarding the shrine, or with the second (or her grave). Unset: the Seventh's armoury | — |
| `ans.yugure_blade.stance` | Ch 27.2, mid-duel, after the first exchange | "Who taught you to stand like that?" | my sensei; no one; the camps | Honesty | Ch 37.3: "Your guard is your sensei's. Your feet are your own" (varies: "the camps" makes him say "Your feet are the camps'. Unlearn them") | — |
| `ans.yugure_blade.burn` | Ch 37.3, among the shelves, before he strikes | "Would you burn this place to keep what's in it secret?" | yes; no; it's been burning for eighty years | Honesty / theme | Ch 51b: he has read nothing from the archive, but the third answer makes him ask what was in it | "Eighty years" seeds his doubt one arc early |
| `ans.yugure_blade.dusk` | Ch 51b, before the last duel | "Do you know what dusk is for?" | the end; the night; the morning after | Theme | Ch 52: his line ("Dusk was supposed to be for them, not for her") answers the player's: "the end": "You were right, it was an end" first; "the night": unchanged; "the morning after": "Make it morning" after. Unset: unchanged | — |

### What his lines are for

| Function | Where |
|---|---|
| **Combat teaching** | Each duel's dialogue teaches the player something about his style before he uses it (a telegraph in words) |
| **Theme** | A sincere believer, so Yūgure is not only the leader's lie |
| **Plot** | Ch 37.3 (the Hearthstone attempt), Ch 51b (the turn), Ch 52 (beside the player) |
| **Mood states** | `duel` (respectful), `turned`, `wounded`, `custody`, `keeper` (epilogue) |
| **Pools** | `story.blade.<chapter>.<beat>`; duel barks `combat.bark.yugure_blade.<event>` (opening, landed hit, took hit, low health, yield) for the combat session |

### Variants

| Flag | Changes |
|---|---|
| `twist.lineage` | None before Ch 52; in A his line to the second on the Rock can be "Your child fights like you" (he has guessed) |
| `story.second.lives` | His epilogue post: the shrine with her (A: the house's hall at times) or her grave (A: under the persimmon tree; B: at the shrine beside the basket) |

## New flags

- `ans.yugure_blade.fight` (friends, village, never_taken, dont_know)
- `ans.yugure_blade.country` (tell_me, burned, should_i)
- `ans.yugure_blade.sword` (take, back, her)
- `ans.yugure_blade.stance` (sensei, no_one, camps)
- `ans.yugure_blade.burn` (yes, no, eighty_years)
- `ans.yugure_blade.dusk` (end, night, morning)
