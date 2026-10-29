# Minor recurring roles

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

Smaller parts that recur, each with a compact brief. Every main-path read of an `ans.*` flag here has
an unset default: the neutral line, or no callback. Roles marked *rolled* have a rolled look and
gender in Varied (pronoun tokens; *they* here); *fixed* roles have a fixed look and gender.

---

## `role:sensor_shadow` (retired)

The sensor who shadows the player from Ch 22 is now **`squad4_a`** (the Hyuga main-house heir, the
Fifth's niece), written in her own character file. The sensor who flags the player "Anomalous" in
Ch 22.1 is **`squad3_c`** (the Sixth's nephew). Any `sensor_shadow` reference in the arcs reads as
`squad4_a`.

---

## `role:ramen_cook`

| | |
|---|---|
| Role | Ichiraku's cook; the village's constant |
| Clan | No clan; an ordinary family name (Given Family order) |
| Look | Rolled civilian (market collection), apron, a towel on the head |
| Pronouns | They (rolled) |
| Archetype | `warmhearted` |
| Appears | Ch 1.4 onward, every arc; Ch 20.4, 45.2, 54.1 (a stand in the street after the war) |

**Arc.** None, on purpose. They remember the player's order (`ans.player.ramen`) from Ch 1 to the
epilogue and set it down without asking. Their arc is that they never change while everything else
does. In Ch 54.1 they serve from a stand in the rubble: "Ichiraku doesn't close for wars."

**Voice.** Loud, warm, food first. They call the player by their order ("Miso! Sit down!") until
level 4, then by given name.

*Voice samples, not shipped lines:* "Your usual. Don't argue." · "Your squad came in without you.
They ordered yours and stared at it. Go find them."

**Questions.**

| Id | When | Question | Options | Remembered |
|---|---|---|---|---|
| `ans.player.ramen` | Ch 1.4 (asked by the instructor; the cook keeps it) | Miso or salt? | miso, salt, pork_bone, same | Forever |
| `ans.ramen_cook.extra` | After Ch 7 graduation | "Graduation bowl. Extra egg or extra meat?" | egg, meat, give it to the kid next to me | The cook gives the extra to another Academy kid every graduation day after, "your way" (a deed the village hears of if "give") |
| `ans.ramen_cook.new_stand` | Chunin (the Rival Ramen Stand filler, if played) | "You eat over there now?" | never, once, it was good | A running joke in greetings |

**Lines are for:** life and continuity; the bowl is a motif (Ch 1, 7, 20, 45, 54).

---

## `role:undercroft_head`

| | |
|---|---|
| Role | Head of the Undercroft (Night Watch) |
| Name | No clan; an ordinary family name (Given Family order) |
| Look (fixed) | A small old woman, about seventy-five, white hair cut straight at the chin, a cane she does not need, an old ANBU tattoo on her upper arm, an ash-grey haori |
| Pronouns | She / her |
| Archetype | `stern` leaning `pragmatic` |
| Values / peeves / dream | Duty, strength / recklessness, dishonesty / protect the village (at any price) |
| Appears | N3 to N7 (N3 needs `story.ch44.done`); Ch 50 (if brought under the Hokage); Ch 51a (on the wall, any path) |

**Arc.** The Undercroft is the heirs of the **sealing team that sealed the twenty-seven** in the
Quiet Ending: a mixed-clan oath society of old ANBU and sealers who never stopped believing the
gift must be sealed and used. Their hall is the sealing team's **derelict sealing hall under the old
quarry**; the Shimura have no part in it (a Shimura is among those who expose it: in `clan.shimura.3`
a Shimura finds a stranger using their cellar as a mail drop for sealed letters, and helping finds
the Undercroft's courier, which opens N3). She is the sealing team leader's granddaughter, sworn in
as a child,
and commanded ANBU under the Third. She believes the Quiet Ending's only mistake was waste. She has
intercepted Yūgure's mail for years and knows the player's nursery number. She wants the gift caged
and aimed: in N4 to N5 her plan is **the jar**, their old sealed jar, with the lost child as its
mouth. She does not resist arrest (N7): "You will need us when he comes," and in every path she
fights at the wall in Ch 51a.

**Voice.** Precise, unhurried, contemptuous of sentiment, never raises her voice. Calls the player
"Nine" until N7, then "Hokage's hound", then (Ch 51a, if she survives the night) by name.

*Voice samples, not shipped lines:* "Nine. We have your reports too." · "Sentiment is a fire with no
hearth. It burns the house down."

**Never reveal before.** The Undercroft's existence: N3. That she knows "Nine": N3 (N3 is reachable
only after Ch 44, so it never pre-empts the voice's slip; see note below).

**Questions.**

| Id | When | Question | Options | Remembered |
|---|---|---|---|---|
| `ans.undercroft_head.offer` | N3.3 | "Join us, and no child will be taken again." | listen (pretend), refuse, walk_out | N5's opening, N7's choice framing |
| `ans.undercroft_head.waste` | N7 | "The Leaf burned your clan and wasted it. Would you rather it had kept you in a jar?" | no, I'd rather it had kept us as people, ask the lost child | Ch 51a: her last line on the wall ("You said 'as people'. Then go and be one") |

**Lines are for:** the ANBU branch's moral opponent; the Leaf's shadow version of the leader.

---

## `role:anbu_captain`

| | |
|---|---|
| Role | The masked captain who recruits and leads the player in Night Watch (N1 to N2 need level 35 and `story.ch39.done`) |
| Look | Rolled shinobi; ANBU armour and a heron mask; never unmasked in the story |
| Pronouns | They (rolled) |
| Archetype | `reserved` |
| Appears | N1, N2, N6 (fights beside the player against the Undercroft, having chosen the Hokage over old loyalties) |

**Voice.** Whispers. Never uses names in the field ("Out here you have no name. Come home with it").

**Questions.**

| Id | When | Question | Options | Remembered |
|---|---|---|---|---|
| `ans.anbu_captain.mask` | N1.2 | "Why do you want a mask?" | to work unseen, to stop being Nine, I don't, I want the job | N6: as they fight the Undercroft, "You said ___. Good. Keep it" |
| `ans.anbu_captain.name` | N6, after the fight | "If I took this off, would you want to know who I was?" | yes, no, only if you want | Epilogue: if "yes", they unmask at the inauguration (a resident the player already knows, chosen by the dialogue session from the player's level-3+ shinobi bonds) |

---

## `role:genin_1`, `role:genin_2`, `role:genin_3`

Your own Genin team (Ch 34 onward). All rolled (looks, genders, personalities), with these fixed
role traits:

| Role | Fixed trait | Arc in one line |
|---|---|---|
| `genin_1` | If `ans.player.ch0.freed_boy = freed`, he is the boy from the third cell, grown (fixed male, fixed look then); else rolled | Wants to be like the person who opened his door; learns to open doors for others (he leads the Academy children out in Ch 51a) |
| `genin_2` | A rolled clan or clanless child; the team's loud one | Wants to beat the other two; learns the cord test's lesson from your test |
| `genin_3` | A Kagari descendant with a faint sealed flame (`story.seed.genin_flame`) | Afraid of what they are once they know; the Undercroft targets them in N5 if the player refuses; in Ch 53 their flame is one of the first to kindle toward you |

**Voice.** Genin energy: arguments, eating, competing for your attention (jealousy is live: the
bond engine's favouritism applies to them as to a squad).

**Questions** (one per genin, asked in a hangout or after a mission):

| Id | Who | Question | Options | Remembered |
|---|---|---|---|---|
| `ans.genin_1.door` | genin_1 | "Why did you open my door? You didn't know me." (if freed) / "Why did you pick our test that way?" (else) | it was locked and I could open it, someone would've done it for me, I didn't think | Ch 51a: he says it to the children he leads out |
| `ans.genin_2.best` | genin_2 | "Who's your favourite? Out of us. Be honest." | none, all three, you (to genin_2), tell them honestly | Jealousy: "you" raises genin_2 and costs the others (the favouritism rule) |
| `ans.genin_3.flame` | genin_3 | "Is this thing in me going to hurt someone?" | no, not if you learn it, it might, so let's learn together | Ch 53: their line as their flame kindles toward you |

---

## `role:yugure_b_parent`

| | |
|---|---|
| Role | `teammate_b`'s parent, who walked out of the Leaf when b was small and joined Yūgure |
| Look | Rolled shinobi of the same family; older, scarred; road clothes, a soot sun on the wrist, an ash-violet scarf in Ch 51a |
| Pronouns | They (rolled) |
| Archetype | `fiery` gone sour (bitter) |
| Appears | Mentioned Ch 6.2; the stranger's lure Ch 13; alive (Ch 26); met only in Ch 51a |

**Arc.** A Leaf Chunin abandoned on a failed mission by a captain who chose the objective over his
team; the village gave the captain a medal. They walked out the next week, too ashamed to take the
child and too angry to stay. Yūgure gave them a cause. They asked the second, years later, to find
out if b was alive, and she used it as a lure (Ch 13).

**Voice.** Rough, short, defensive; softens only when b asks the player's question.

**Ch 51a.** b asks your question (`ans.teammate_b.ask`):

| Question | Their answer |
|---|---|
| why | "Because they left me on a road and gave the man who did it a medal. And because I was a coward about you." |
| sorry | (a long silence) "Every day." |
| remember | "You had a pup's ears on your hat. You cried when it rained. I remember." |

b's choice reads `ans.teammate_b.come_back` (yes: bring them in; only if sorry: make them say it;
no: let them go). They live in all three.

**Questions** (Ch 51a, to the player, only if `ans.player.b_parent = stand`):

| Id | Question | Options | Remembered |
|---|---|---|---|
| `ans.yugure_b_parent.kid` | "Is my kid a good shinobi?" | the best on our squad, better than you, ask them | Epilogue: if they came home, the line they say at b's promotion |

---

## `role:foreign_genin`

| | |
|---|---|
| Role | One of the three real Genin of the small foreign team whose adult escorts are the second and the blade under false papers (Ch 15 to 19; `side.b3.lost_genin`). Innocent |
| Look | Rolled, a small foreign village's outfit |
| Pronouns | They (rolled) |
| Archetype | `shy` |

**Arc.** A real Genin of a small village, sent to the Leaf's exam with two new escorts their
village hired on good papers. In the Forest of Death (16.4) the player finds them lost, looking for
escorts who left the forest early; before the finals the escorts vanish altogether. After the
attack they realise who the escorts were. They go home safe and write to the player once a year
(a letter in the mailbox each New Year).

**Questions.**

| Id | When | Question | Options | Remembered |
|---|---|---|---|---|
| `ans.foreign_genin.home` | Ch 20, before they leave for home | "Should I tell my village who our escorts were? They'll say we were stupid." | tell them, tell them we caught it, it's your choice | Their yearly letter's tone |
| `ans.foreign_genin.again` | First letter (after Ch 20) | "Will you be at the next exam? I want a real fight." | yes, I'm Chunin now (no), as a proctor | Their Chunin-arc cameo: a friendly bout at the next season's exam (if yes or proctor) |

---

## `role:elder_hyuga`

| | |
|---|---|
| Role | The third council elder; the Fifth's uncle |
| Look (fixed) | An old Hyuga man, white-robed, Byakugan, a walking staff, a face that has never been surprised |
| Pronouns | He / him |
| Archetype | `proud` |
| Values / peeves / dream | Family, duty / nosiness, bragging / honour their clan |
| Appears | Ch 22.2, Ch 33.3 (the council review), Ch 40.2 (walks out), Ch 51 (if the Fifth chose "yes" in `ans.hokage_5.hyuga`, he sends the main house's sensors to the wall) |

**Arc.** The keeper of the Hyuga record of the Valley of Ash. He flinches at the word Kagari (Ch 22)
because he knows more than the Fifth: the main house knew of the Quiet Ending and voted for it. He
walks out of the Ch 40 council rather than hear it. His one turn, if the Fifth asks him: he sends
the sensors.

**Voice.** Ceremonial, cold, sentences that begin "The main house...". Never addresses the player
directly before Ch 51.

**Questions.**

| Id | When | Question | Options | Remembered |
|---|---|---|---|---|
| `ans.elder_hyuga.blood` | Ch 33.3 (before the Sixth stops him) | "Do you know what you carry, Chunin?" | yes, no, do you? | Ch 40.2: "do you?" makes him answer it as he walks out: "I do. That is why I am leaving" |
| `ans.elder_hyuga.record` | After Ch 51, if he sent the sensors | "The main house's record of the Valley. Should it be read in public now?" | yes, give it to the archive, burn it | The epilogue: the record in the archive beside the charter, or read at the memorial |

---

## `role:hokage_4_daughter`

| | |
|---|---|
| Role | The Fourth Hokage's daughter, who runs the Akimichi barbecue house |
| Look (fixed) | A big, cheerful Akimichi woman of about thirty, her father's broad smile, a head scarf and a grill fork |
| Pronouns | She / her |
| Archetype | `warmhearted` |
| Appears | Ch 14.6 (she serves the squad dinner and teases the sensei about paying), Ch 21.2a (falls: she gives you his bowl), every barbecue hangout, Ch 55 (the stipend restored in her father's name) |

**Arc.** By `twist.fourth_fate`: *falls*: her grief and her father's bowl; *crippled* or *taken*:
she wheels her father to the barbecue house on Market Day and lets him cook badly. In every save
she knows about the stipend and that the player was one of its children ("He used to read the
stipend list at dinner. Every name").

**Voice.** Loud, generous, food as love, her father's phrases ("You hungry? Of course you are").

**Questions.**

| Id | When | Question | Options | Remembered |
|---|---|---|---|---|
| `ans.hokage_4_daughter.list` | After Ch 21 (any variant), at the grill | "Do you know what number you were? On his list?" | S-114, I don't remember, does it matter? | Ch 55.3: she reads the restored stipend's first name; if "S-114", she reads the number too, and laughs |
| `ans.hokage_4_daughter.taste` | A barbecue hangout | "Be honest. Is mine better than his was?" (falls) / "Is his cooking getting worse or am I imagining it?" (crippled, taken) | yes, the same, his (falls) / it's worse, it's love, tell him | Her running joke |

---

## Note on the Undercroft and the slip

The Undercroft knows the player's nursery number. N1 to N2 open after Ch 39 and N3 (the quarry hall)
only after Ch 44, so the head's "Nine" always comes after the voice's case is closed and never
muddies the Ch 25 slip.

## New flags

- `ans.ramen_cook.extra` (egg, meat, give)
- `ans.ramen_cook.new_stand` (never, once, good)
- `ans.undercroft_head.waste` (no, as_people, ask_her)
- `ans.anbu_captain.mask` (unseen, not_nine, the_job)
- `ans.anbu_captain.name` (yes, no, if_you_want)
- `ans.genin_1.door` (locked, someone_would, didnt_think)
- `ans.genin_2.best` (none, all, you, honest)
- `ans.genin_3.flame` (no, learn, together)
- `ans.yugure_b_parent.kid` (best, better_than_you, ask_them)
- `ans.foreign_genin.home` (tell, caught_it, your_choice)
- `ans.foreign_genin.again` (yes, no, proctor)
- `ans.elder_hyuga.blood` (yes, no, do_you)
- `ans.elder_hyuga.record` (public, archive, burn)
- `ans.hokage_4_daughter.list` (s114, dont_remember, matter)
- `ans.hokage_4_daughter.taste` (by fate; see table)
