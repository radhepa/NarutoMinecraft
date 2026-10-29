# `role:hokage_4`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). His fate is
> `twist.fourth_fate` ([ROTATIONS.md](../ROTATIONS.md) §3).

## At a glance

| | |
|---|---|
| Role | The Fourth Hokage, sitting when you arrive |
| Look | **Fixed** (baked into the Rock and portraits): a big, warm Akimichi man with a broad smile, about fifty-eight |
| Pronouns | He |
| Name | Hokage carry no family name in text: given name rolled; spoken of as "Lord Fourth" ({hokage:4}); his clan is Akimichi |
| Rank | Hokage (Y-28 to Ch 19/20) → mentor (crippled or taken) or memory (falls) |
| Archetype | **warmhearted** (with the Akimichi upbringing: warmth, sharing) |
| Values | Family, kindness |
| Peeves | Cruelty, neglect (and anyone calling an Akimichi fat) |
| Dream | That no child in the Leaf goes to bed hungry; the orphan's stipend is his |
| Family | A daughter who runs the barbecue house |
| First / last | Ch 1 / Ch 19 to 20 (falls) or Ch 55 (crippled, taken) |

## Arc

**Wants.** A village where everyone eats, together. He thinks politics is mostly feeding people.

**Fears.** That peace has made the Leaf soft and that he cannot be hard when it must be (the Fifth
is what he fears he cannot be; he names her himself if crippled).

**Secrets.** Fewer than anyone in power: the keeper never told him the archive's full contents. He
knows there is "an old shame under the Rock" and chose not to ask, because the Third asked him not
to. That choice is his only real regret, spoken only if he lives (Ch 40 or 49).

**What he knows and when.**

| Knowledge | From |
|---|---|
| You were rescued from a hideout | Ch 1 |
| The keeper watches you | Ch 1 (he notices and teases the keeper for it) |
| "Kagari" | Crippled/taken: Ch 21 onward (told by the sensei or the Fifth); falls: never |
| The archive's truth | Ch 40 (public) |
| The leader is practising the dark mirror | Taken: Ch 21 (lived it). Crippled: felt it in Ch 19 |
| The array | Ch 49 (crippled or taken: "I've felt this before") |

**How he changes.**

| Arc | Change |
|---|---|
| 1 Cinders | The warm centre of the village: the stipend, the speech |
| 3 Dusk | Buns at the training ground; then his fate |
| 4 Embers | Falls: a statue and a bowl. Crippled: a teacher in a wheelchair. Taken: a hollowed man brought home who still jokes |
| 5 Ashes | (Living) hears the archive's truth and admits he chose not to ask |
| 7 Last Bonfire | (Living) feels the array; sits in the Academy with the children in Ch 51; at your inauguration |

**Endings.**

| `twist.fourth_fate` | His end |
|---|---|
| Falls | Dies covering the evacuation (Ch 19). Funeral in rain (Ch 20). His bowl to you (Ch 21). The stipend restored in his name (Ch 55) |
| Crippled | Abdicates from his bed and names the Fifth. Mentor through the Chunin arc; at the Academy in Ch 51; at your inauguration |
| Taken | Carried off in Ch 19; rescued in Ch 21 (The Empty Seat), hollowed; mentor as crippled; warns of the array in Ch 49 |

## Dialogue brief

### Voice

Big, slow, warm; food in every metaphor; laughs at his own jokes before they land. Calls children
"little one" and adults by their given name. Becomes very quiet and very still when serious, and
that frightens people more than shouting. Never threatens; never talks about weight.

Voice samples, not shipped lines:
- "You came a long way. You hungry? Of course you are."
- "From today you earn your own bowl. I'm proud of you."
- "Don't win for me. Win for you."
- (crippled) "She is hard. The Leaf needs hard for a while."
- (taken, Ch 21) "They practised on me. They're practising for something."

### Topics they care about

| Topic | What he says |
|---|---|
| Food (1) | Everything; his favourite is his daughter's barbecue, and he says so to rival restaurants |
| Their family (4) | His daughter, his late wife, the Akimichi kitchen hall |
| Their values (5) | "A full table is a safe village" |
| Advice (5) | Gentle, always about the people around you: "Who did you eat with today?" |
| Their dream (6) | The stipend for every orphan in every village, not only the Leaf |
| Worries (7) | (living) That he did not ask about the shame under the Rock |

### Never reveal before

| Fact | Not before |
|---|---|
| "Kagari", anything about your blood | Never (falls); Ch 21 (crippled, taken) |
| The "old shame under the Rock" | Ch 40 |
| Any hint of his fate | Ch 19 (no foreshadowing of a specific fate in the beta: all three must stay possible) |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes him |
|---|---|---|---|---|---|---|
| `ans.hokage_4.want` | Ch 1.2 | "What do you want to be, little one?" | strong / safe / find_girl / hokage | Any | Ch 7.3 speech; Ch 21 (living: "Still want to be ___?") | "Find the girl": he orders the hills searched each season (taken path: the search finds his own trail) |
| `ans.hokage_4.ate_with` | Ch 7 to 18, any meeting in the village (level 2) | "Who did you eat with today?" | my squad / alone / the cook counts / you, right now | Family | Ch 18.3 (he brings enough buns for whoever you named) | "Alone": he asks the instructor to make sure you never are |
| `ans.hokage_4.stipend` | Ch 7.3 aside (level 2) | "When you're grown, would you keep it going? The stipend?" | yes / for every village / I'll do better | — | Ch 55.3 (restoring it in his name) | "Every village": his dream line changes |
| `ans.hokage_4.hard` | Crippled/taken: Ch 22 to 31, visiting him | "Is she too hard on you? The Fifth?" | yes / she's scared / she's right to watch me | Kindness | Ch 31.4 (he visits her after she steps down and repeats it) | "She's scared": he softens the village toward her after she steps down |
| `ans.hokage_4.didnt_ask` | Living, Ch 40 | "I chose not to ask what was under the Rock. Would you have asked?" | yes / no / I'd have asked the keeper to tell me himself | Honesty | Ch 49 war council | — |

### What their lines are for

- **Plot:** the stipend, the speech, his fate (the end of the beta's peace).
- **Bond:** the first powerful person who is kind to you; the fate must cost something.
- **Life:** food, laughter, his daughter's barbecue house.
- **Pools:** Hokage greetings (beta), wheelchair teacher (crippled/taken), hollowed lines (taken:
  slower, still warm), a falls-variant memorial pool for others' lines about him.

### Variants

All by `twist.fourth_fate`. No beta line may imply one fate over another.

## New flags

- `ans.hokage_4.ate_with` (squad, alone, cook, you)
- `ans.hokage_4.stipend` (yes, every_village, better)
- `ans.hokage_4.hard` (yes, scared, right)
- `ans.hokage_4.didnt_ask` (yes, no, keeper)
