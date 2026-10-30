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
| Family | A daughter who runs the barbecue house; a grandson, `squad3_b` (Akimichi in every save), in your Academy class |
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
| 2 Paper Trail | Ch 14.6: at the barbecue house when the squad comes for dinner; he insists on paying, tells the sensei to put their purse away, and asks you who you ate with this week |
| 3 Dusk | Buns at the training ground; then his fate on the east stair |
| 4 Embers | Falls: a statue and a bowl. Crippled: a teacher in a wheelchair. Taken: a hollowed man brought home who still jokes |
| 5 Ashes | (Living) hears the archive's truth and admits he chose not to ask |
| 7 Last Bonfire | (Living) feels the array (crippled: "at the stadium"; taken: "in their hold"); sits in the Academy with the children in Ch 51a, sending word to the Seventh; in Ch 53.4 the chakra the leader took returns through the array and some of it reaches him: he stands up for a moment, laughing; at your inauguration |

**Endings.**

| `twist.fourth_fate` | His end |
|---|---|
| Falls | Hit in the stands while carrying Academy children down the east stair (no seat, no barrier); he dies there, shown through the cinematic cutaway (child-stage safe); his last words to you as you pass on the stair: "Win for you." (Ch 19). Ch 20: an **Akimichi farewell feast**: the whole village eats his favourite dish in the street, his bowl set at an empty place; `squad3_b` or his daughter quotes `ans.hokage_4.want`. His bowl to you (Ch 21). The stipend continues in his name; you **extend** it as the Eighth (Ch 55) |
| Crippled | Hit on the same east stair, carrying children; the dark mirror tears half his chakra. Abdicates from his bed and names the Fifth. Mentor through the Chunin arc; at the Academy with the children in Ch 51a, sending word to the Seventh; at your inauguration |
| Taken | Hit on the east stair with a binding seal and carried off over the wall in Ch 19 (`squad3_b`, beside you on the stair, runs after him); rescued in Ch 21 (The Empty Seat, led by `sensei_2`; `squad3_b` carries his grandfather out), hollowed; mentor as crippled; warns of the array in Ch 49 |

## Dialogue brief

### Voice

Big, slow, warm; food in every metaphor; laughs at his own jokes before they land. Calls children
"little one" and adults by their given name. Becomes very quiet and very still when serious, and
that frightens people more than shouting. Never threatens; never talks about weight.

Voice samples, not shipped lines:
- "You came a long way. You hungry? Of course you are."
- "The bowl's on me a while longer. I'm proud of you."
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
| `ans.hokage_4.ate_with` | Ch 14.6 at the barbecue house (or any meeting, Ch 7 to 18, level 2) | "Who did you eat with today?" | my squad / alone / the cook counts / you, right now | Family | Ch 18.3 (he brings enough buns for whoever you named) | "Alone": he asks the instructor to make sure you never are |
| `ans.hokage_4.stipend` | Ch 7.3 aside (level 2) | "When you're grown, would you keep it going? The stipend?" | yes / for every village / I'll do better | — | Ch 55.3 (extending it in his name, to the same children in every save; your one line as you sign it reads your answer: yes: "I said I would." every village: "Every village. I told him." I'll do better: "Better. That was the promise." Unset: no line) | "Every village": his dream line changes |
| `ans.hokage_4.hard` | Crippled/taken: Ch 22 to 31, visiting him | "Is she too hard on you? The Fifth?" | yes / she's scared / she's right to watch me | Kindness | Ch 31.4 (he visits her after she steps down and repeats it) | "She's scared": he softens the village toward her after she steps down |
| `ans.hokage_4.didnt_ask` | Living, Ch 40 | "I chose not to ask what was under the Rock. Would you have asked?" | yes / no / I'd have asked the keeper to tell me himself | Honesty | Ch 49 war council | — |
| `ans.hokage_4.bun` | Ch 18.3 | "Pork or bean paste?" (the buns) | pork / bean / both / for my squad first | Family | Ch 21 (falls: his daughter knows your bun; living: he brings it) | — (life with a function: a memory to grieve or keep) |
| `ans.hokage_4.office` | Ch 1, after the stipend (level 1) | "Big office, isn't it? Too big?" | too big / just right / it smells like food | — | Ch 20 (falls: the empty office; crippled: he asks again from his bed; taken: not asked, he is captive) | — |
| `ans.hokage_4.council` | Ch 9 to 14, a village meeting (level 2) | "The council wants me to be harder. Should a Hokage be feared a little?" | yes, a little / never / feared by enemies only | Kindness | Ch 20 (crippled: he cites it naming the Fifth); Ch 31 | — |
| `ans.hokage_4.daughter` | Level 3, at the barbecue house | "My girl wants to close early on festival nights. Should I let her?" | yes / no, the village needs the grill / ask her why | Family | Ch 21 (falls: she tells you he took your advice) | — |
| `ans.hokage_4.practised` | Taken: Ch 21.2c; crippled: Ch 22 to 25 | "Do you want to know what they did to me? Some people don't." | yes / not now / only what helps us stop them | — | Ch 49.3 (how much he tells the council) | Sets how much of the dark mirror he describes |
| `ans.hokage_4.inauguration` | Ch 55 (living fates) | "Can I still call you little one? Just once more." | yes / only in private / call me Lord Eighth | — (warmth) | Epilogue line | — |

**Who sees the guard rotation.** Crippled or taken, if asked (Chunin or Jonin arc, or at the case board): "Half the village, child. Medics, vendors, the council, the Academy." Identical in every rotation.

**Unset answers.** Every main-path read of an `ans.hokage_4.*` flag (Ch 7.3, Ch 20, Ch 55) has an `unset` branch; Ch 7.3's speech then lists all four wants. Ch 20 (falls) with `want` unset: "He said you came here hungry. Eat."

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
- `ans.hokage_4.bun` (pork, bean, both, squad)
- `ans.hokage_4.office` (too_big, right, food)
- `ans.hokage_4.council` (a_little, never, enemies)
- `ans.hokage_4.daughter` (yes, no, ask_why)
- `ans.hokage_4.practised` (yes, not_now, helps)
- `ans.hokage_4.inauguration` (yes, private, lord)
