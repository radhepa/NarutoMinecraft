# The senior squad: `role:squad5_a`, `role:squad5_b`, `role:squad5_c`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Ensemble plan:
> [ENSEMBLE.md](../ENSEMBLE.md). Their sensei: [senseis.md](senseis.md#rolesensei_5).

A squad a year ahead of the player's class, under the old sealing master `sensei_5`. They take the
same Chunin Exams (Ch 15 to 20) as the player, and run a step ahead of them all story long. All
three have **rolled looks in Varied** (so *they* here, pronoun tokens in dialogue); the role traits
below stay fixed in every save.

**Unset answers.** Every main-path read of an `ans.*` flag in this file has an `unset` branch: the
unset line given in its row, or else the character's line for that beat without the callback
("You said ___" is dropped, nothing else changes).

| | squad5_a | squad5_b | squad5_c |
|---|---|---|---|
| Specialty | Staff and fire | Silent scouting, smothering | Kenjutsu and ninjutsu, self-taught |
| Want | To be Hokage | That her quarter is seen | Never to be poor or powerless again |
| Flaw | Believes in the village like scripture | Says nothing, even when she should | Takes any power offered |
| Plot weight | Ch 40 faith breaks; Ch 42 chooses; Ch 55 Jonin Commander | Ch 30 to 31 the Tobari crisis | Ch 19 the blade; N-branch, Ch 44, Ch 47: betray or not |

---

## `role:squad5_a`

### At a glance

| | |
|---|---|
| Name | Given Family, rolled. Classic: a **Sarutobi** |
| Look | Classic: curated: a broad, grinning boy with a long clan staff across his back and a headband tied as a sash. Varied: rolled |
| Pronouns | Classic: he. Varied: rolled; dialogue uses `{they:squad5_a}` |
| Specialty and style | The Sarutobi long staff with fire: wide sweeps, a burning spin; fights in the open and loudly |
| Rank | Genin at Y0 (a year ahead) → Chunin in the time skip → Jonin by Ch 33 → the Eighth's Jonin Commander (Ch 55) |
| Archetype | Classic: **fiery** (warmth .6, boldness .9, openness .8) |
| Values | Loyalty, courage |
| Peeves | Cowardice, neglect |
| Dream | Become Hokage |
| Tier | Story-driving |
| First / last | Ch 7 / Ch 55 |

### Arc

**Wants.** The hat. He says so to everyone, and means it as a promise to the village, not as
ambition.

**Fears.** That the village he believes in isn't real.

**Secrets.** None at first: he is the least secret person in the Leaf. After Ch 40 one: he no longer
knows what he believes.

**What he knows and when.** Public knowledge only until Ch 40 (the Quiet Ending made public; and
that the Third, a Sarutobi, kept the silence). The Hollow Crown at Ch 49.

**How he changes.**

| Arc | Change |
|---|---|
| 1 Cinders | Ch 7: heckles the graduation cheerfully: "Welcome to the bottom! It's great down here!" |
| 3 Dusk | Exams: fights in the preliminaries with a showy staff bout and loses gracefully; when the attack begins at the opening lantern-lighting he carries Academy children out of the stands |
| 4 Embers | Chunin after the skip; declares himself the player's rival "for the hat" (friendly; the bond engine's rivalry meter is the joke) |
| 5 Ashes | Ch 40.2: the council. His clan's Hokage kept the silence for thirty years; he stands through the whole session without a word and sits only when the vote is called. Ch 40.2b: that night, on the Rock under the Third's face, he asks the player the question he can't ask his family (`ans.squad5_a.will`). Ch 42: the naming is contested: the council balks at a Hokage who signed the Ash Road field report. He stands up in the public gallery and says "I'm with them," the crowd follows, and his stand carries the vote |
| 7 Last Bonfire | Ch 51a: on the wall with the former Fifth, the Tobari and the Hagane. Ch 53: a face among the flames (a short line only if the player is very close to him). Ch 55: becomes the Eighth's Jonin Commander in `sensei_2`'s place, his oath quoting `ans.squad5_a.will`, and taking the post "until I take your hat" |

**Endings.** He lives; the epilogue line reads `ans.squad5_a.serve` and `ans.squad5_a.will`.

### Dialogue brief

**Voice.** Loud, open, fast; big gestures; quotes the Will of Fire; laughs at himself; uses "we"
for the village. After Ch 40, quieter; uses "I" for the first time. Never sneers; never lies.

Voice samples, not shipped lines:
- "Welcome to the bottom! It's great down here! Lots of room to climb!"
- "One day that's my face. Second from the left of the new ones. You can have the one after."
- (Ch 40.2b, on the Rock) "She lied. For thirty years. And I'd have done the lantern walk for her with my eyes shut."
- (Ch 42, in the gallery, over the council's objection) "I'm with them."
- (Ch 55) "Commander. Fine. Until I take your hat."

**Topics.** Training (1): staff sparring, every day. Family (4): the Sarutobi hearth; his
grandmother's lanterns. Values (5): "The village is everyone in it. Even the ones it forgot."
(After Ch 40 he adds the second sentence.) Dream (6): Hokage. Worries (7): that faith is
just habit.

**Never reveal before.** Nothing about the Third's silence before Ch 40; no Hollow Crown lines
before Ch 49.

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | Changes him |
|---|---|---|---|---|---|---|
| `ans.squad5_a.why_hokage` | Ch 18 (festival) or level 2 | "Why would *you* want to be Hokage?" (if `ans.hokage_4.want = hokage`, he adds "I heard you said it to the Fourth") | So nobody gets taken / To see everyone / I don't, yet / To beat you to it | His dream | Ch 42 and Ch 55: his commander's oath quotes it | — |
| `ans.squad5_a.fire_means` | Level 4 hangout (lantern prep) | "What does the Will of Fire mean to you?" | People keeping each other warm / The Hokage's word / A nice story / I'll tell you when I know | Loyalty | Ch 40.2b: on the Rock he reminds you of it before he asks his question | "Story": he argues with you, then (Ch 40) admits you might have been right |
| `ans.squad5_a.will` | Ch 40.2b (on the Rock under the Third's face) | "Does it still count, the Will of Fire, if the one who taught it to us kept this quiet?" | It counts more now / It never counted / It counts if we say it out loud | His faith | Ch 42 (he stands with the Seventh either way: "I'm with them"); Ch 55: his Jonin Commander's oath quotes it | "More now": his oath is about carrying it forward; "never": about building something truer; "out loud": he starts the custom of reading the Kagari names at the New Year lantern walk |
| `ans.squad5_a.serve` | Ch 45 or 54 | "If you get the hat instead of me, would you want me to serve you or fight you for it?" | Serve with me / Fight me, it'll keep me honest / Take it yourself | Pride, loyalty | Ch 55: he takes the commander post (serve) or a standing challenge (fight) or offers you the hat and you refuse (take) | — |
| `ans.squad5_a.lantern` | Level 3, New Year | "Whose name do you write on your lantern?" | The girl from the next cell / The Fourth / My own / Someone I haven't met | Family | Every New Year after, he writes the same on his | — |
| `ans.squad5_a.carry` | Ch 20 (after the attack) | "I carried a kid out of the stands. Didn't even ask her name. Is that weird?" | No / Go find her / That's what the Fourth did for me | Kindness | Chunin arc: the girl is a recurring Academy kid who calls him "staff man" | — |
| `ans.squad5_a.bottom` | Ch 7 (after his heckle, if you go up to the wall) | "Welcome to the bottom! Scared?" | No / A little / Of you? No | Courage | Ch 18: "You said ___ at the bottom. How about now?" before the finals | — |
| `ans.squad5_a.spar` | Level 2, a staff spar | "Staff or fists? Pick how I lose." | Staff / Fists / Neither, race me | Courage | His sparring hangout favourite becomes yours | Opens a ritual (sparring or rooftop races) |
| `ans.squad5_a.faces` | Level 4, on the Rock | "Which face up there do you like best? You can't say the Fourth, everyone says the Fourth." | The First / The Third / The empty spaces / The Fourth anyway | His faith | Ch 40.2b: under the Third's face he remembers it ("You liked her best") or not | "The Third": the Ch 40 hurt is sharper and his recovery stronger |
| `ans.squad5_a.campaign` | Ch 33 (his cheerful campaign) | "Vote for me? I'm accepting endorsements. And dumplings." | Yes / Only if you buy dumplings / I'm running too | Pride, fun | Ch 45: his speech to the squad; Ch 55: "You endorsed me once. Look where it got you" | "Running too": the rivalry meter (friendly) rises; `ans.squad5_a.serve` reads warmer |
| `ans.squad5_a.wall` | Ch 49 (war council) | "If the wall falls, do I stay on it or come to you?" | Stay on the wall / Come to me / Go where you're needed most | Duty | Ch 51a: how the wall scene ends for him (holds his stretch / sends word to the player / goes to the gate's second line); unset: holds his stretch | "Come to me": in Ch 53 his face comes with a short line if the player is very close |
| `ans.squad5_a.sensei_2` | Ch 54 (after the funerals) | "He'd have made a joke about this. Should I?" | Yes, make the worst one / No / Write it in his notebook | Grief | Ch 55: his first act as Commander (a joke at the gate, silence, or a tally line) | — |

**Unison technique (Blaze).** *Hearth Wheel*: his burning staff spin, kindled, becomes a turning
wall of fire that lets no enemy through and burns nothing it shields.

**Variants.** Varied: any bold fighter who wants the hat. The Ch 40 crisis stays: in a Varied save
where he is not a Sarutobi, it becomes his belief in the Hokage line itself ("Every one of them
knew? Then what is the hat?").

**New flags.** `ans.squad5_a.why_hokage` (nobody_taken, see_everyone, not_yet, beat_you),
`ans.squad5_a.fire_means` (warm, word, story, later), `ans.squad5_a.will` (counts_more,
never_counted, out_loud), `ans.squad5_a.serve` (serve, fight, take), `ans.squad5_a.lantern` (girl, fourth, own,
stranger), `ans.squad5_a.carry` (no, find_her, fourth), `ans.squad5_a.bottom` (no, little, of_you),
`ans.squad5_a.spar` (staff, fists, race), `ans.squad5_a.faces` (first, third, empty, fourth),
`ans.squad5_a.campaign` (yes, dumplings, running), `ans.squad5_a.wall` (stay, come, needed),
`ans.squad5_a.sensei_2` (joke, no, notebook).

---

## `role:squad5_b`

### At a glance

| | |
|---|---|
| Name | Given Family, rolled. Classic: a **Tobari** |
| Look | Classic: curated: a slight girl in dark layered cloth, a muffler over her mouth, soft-soled sandals; a lantern-keeper's hook at her belt. Varied: rolled |
| Pronouns | Classic: she. Varied: rolled; dialogue uses `{they:squad5_b}` |
| Specialty and style | Silent scouting, the Tobari smothering (no footsteps, no sound around her at night), a short hooked blade |
| Rank | Genin at Y0 → Chunin in the time skip → a night-watch captain (Jonin arc) |
| Archetype | Classic: **reserved** (warmth -.2, openness -.8, discipline .3) |
| Values | Freedom, honesty |
| Peeves | Nosiness, rudeness |
| Dream | Find where she belongs (that her quarter is seen) |
| Tier | Story-driving |
| First / last | Ch 7 / epilogue |

### Arc

**Wants.** For the Tobari's unseen work to be seen. The night watch keeps the Leaf safe, and the
Leaf crosses the street from them.

**Fears.** Being blamed for something because no one ever looked at her people.

**Secrets.** She knows the name of the Tobari deserter who taught Yūgure the smothering technique:
her mother's cousin. She has told no one, out of shame.

**What she knows and when.** The deserter's name (before Y0); that her quarter is innocent (Ch 30);
the cell in the drain (Ch 31, with the player).

**How she changes.**

| Arc | Change |
|---|---|
| 3 Dusk | Ch 16: the player glimpses her watching from the forest's high branches, never moving; Ch 19: scouts the stands and gives sensei_5 the stair routes by hand signs |
| 4 Embers | Ch 30: her quarter is locked down. She comes to the player at night, unseen, and says the longest thing she has ever said: "They'll arrest my grandmother. I need someone they'll listen to." She partners the player in the lanes and the drain (Ch 30.4, 31.1). If the player asked her (see `ans.squad5_b.deserter`), she gives up the deserter's name, which leads to the drain. Ch 31.2: her grandmother, a Tobari elder, is the first near-stranger to kindle toward the player |
| 5 Ashes | Leads the night watch; the Tobari are seen |
| 7 Last Bonfire | Ch 51a: beside the main gate, she and the Tobari smother the lanes so the evacuation moves unheard behind sensei_2's stand |

**Endings.** She lives. Epilogue: she answers sensei_5 in a full paragraph for the first time.

### Dialogue brief

**Voice.** Very few words; nods; hand signs instead of speech (subtitled); when she speaks, it is
exact and blunt. With the player at level 6+, dry humour in single lines. Never shouts. Never says
"please".

Voice samples, not shipped lines:
- "..." (a nod; subtitle: *She nods.*)
- "You're loud. Even when you're quiet."
- "They'll arrest my grandmother. I need someone they'll listen to."
- (Ch 31) "You saw us."
- (Ch 51a) "He said keep it quiet. So it's quiet." (about sensei_2, at the lanes)

**Topics.** Training (1): footwork, silence. Hobby (2): lantern-keeping; the lake's lanterns
(`filler.lake_lanterns`'s old keeper is her great-uncle). Family (4): her grandmother. Values (5):
"Do the work. Don't need the thanks. But don't take the blame." Dream (6): "That they'd wave at us
at night." Worries (7): the deserter.

**Never reveal before.** The deserter's identity: only at Ch 30 to 31, and only to the player (if
asked). Nothing of Yūgure before Ch 30 beyond public news.

**Questions for the player.** She rarely asks. Each one counts.

| Id | When | Question | Options | Honours / tests | Remembered | Changes her |
|---|---|---|---|---|---|---|
| `ans.squad5_b.quiet` | Level 2 (a night walk) | "Do you like quiet?" | Yes / I'm learning / No, but I like yours | Freedom | Her greetings: silent if yes, a single word if "learning", a whole sentence if "yours" | — |
| `ans.squad5_b.notice` | Level 4 | "Would you notice if I were gone?" | Yes / I'd notice the quiet / I'd look for you | Belonging | Ch 30: she comes to you because of it ("You said you'd look. So I came first") | Decides whether she seeks you or you must find her |
| `ans.squad5_b.sound` | Level 3, on a roof at night | "What does the village sound like to you?" | Ramen and arguments / The shrine at dusk / Safe / Like nobody's listening | Openness | Ch 54: after the war, she asks again, and you hear her answer | — |
| `ans.squad5_b.deserter` | Ch 30 (in the lanes) | (She shows you a Tobari family crest scratched out) "If someone in your family helped them... would you say?" | Yes, even if it hurts / Only to someone I trust / No | Honesty | Ch 30 to 31: she names the deserter (yes or trust); without it, the drain takes an extra investigation step | The `clan.tobari.3` shortcut opens either way |
| `ans.squad5_b.seen` | Ch 31 (after the council) | "You saw us. Why?" | Because nobody else would / Because you asked / Because I know what it's like to be watched | Belonging | Ch 51 and the epilogue's wave at night | — |
| `ans.squad5_b.teacher` | Level 5, Jonin arc | "The old man talks to me like I'm a wall he likes. Should I talk back?" | Yes / Only when you have something to say / Try once and see | Her growth | Epilogue: her paragraph to sensei_5 | — |
| `ans.squad5_b.hand` | Ch 19 (she passes routes by hand signs) | (Signs, subtitled) "Can you read this?" | Yes / Teach me / No, say it | Freedom | Chunin arc: she signs to you instead of speaking; Ch 31.1 the drain fight uses signs if you learned | "Teach me": a hand-sign hangout opens; in Ch 31 she can sign the cell's position before the Ember Link |
| `ans.squad5_b.grandmother` | Ch 31.2 (after the kindling) | "She's never given anything to anyone outside the quarter. Why you?" | Because you asked me to come / Because I listened / I don't know | Belonging | Epilogue: the grandmother's line at your inauguration | — |
| `ans.squad5_b.lanterns` | Level 3, at the lake (after `filler.lake_lanterns`, or Beta 2 lanterns) | "My great-uncle kept a lantern for a son for twenty years. Is that love or stubbornness?" | Love / Both / Stubbornness, and that's fine | Family | Ch 54: she lights a lantern on the lake for `sensei_2` and asks if it's the same | — |
| `ans.squad5_b.watch` | Level 6, Jonin arc | "Will you walk a night watch with me? Not for work." | Yes / Only if you talk / Bring ramen | Belonging | A ritual (`ritual [squad5_b, night_watch]`); Ch 53 her flame line: "Not for work" | — |
**Unison technique (Blaze).** *Lantern Hush*: her smothering, kindled, becomes a hush across a
district in which only bonded allies can hear each other.

**Variants.** Varied: any quiet scout; in a Varied save the Tobari crisis still involves a Tobari
elder (the grandmother is marker-fixed in the Tobari quarter); if squad5_b is not a Tobari, she is
the Tobari elder's apprentice instead of her granddaughter.

**New flags.** `ans.squad5_b.quiet` (yes, learning, yours), `ans.squad5_b.notice` (yes, quiet,
look), `ans.squad5_b.sound` (ramen, shrine, safe, nobody), `ans.squad5_b.deserter` (say, trust, no),
`ans.squad5_b.seen` (nobody_else, you_asked, watched), `ans.squad5_b.teacher` (yes, when_needed,
try_once), `ans.squad5_b.hand` (yes, teach_me, say_it), `ans.squad5_b.grandmother` (asked,
listened, dont_know), `ans.squad5_b.lanterns` (love, both, stubborn), `ans.squad5_b.watch` (yes,
talk, ramen).

---

## `role:squad5_c`

### At a glance

| | |
|---|---|
| Name | Given Family, rolled. Classic: **no clan**, an ordinary family name from the `family_names` pool (never a clan's) |
| Look | Classic: curated: a lean, hard-faced boy in mended clothes, a cheap sword with a perfectly kept edge, calloused hands. From Ch 19 a thin scar across the cheek. Varied: rolled, scar always added after Ch 19 |
| Pronouns | Classic: he. Varied: rolled; dialogue uses `{they:squad5_c}` |
| Specialty and style | Kenjutsu and ninjutsu, self-taught from library scrolls and watching others; fast, economical, no wasted motion; the strongest genin of all at Y0 |
| Rank | Genin at Y0 → **Chunin in Ch 20** → ANBU in the Chunin arc's last year (young) → Jonin by Ch 33 |
| Archetype | Classic: **pragmatic**, with pride (warmth -.3, boldness .3, pride .5, discipline .8, openness -.3): where the rival's pride is about who they are, his is about what he has paid for |
| Values | Strength, family (his mother and two small sisters) |
| Peeves | Bragging, nosiness |
| Dream | Master his art; underneath, never be poor or powerless again |
| Tier | Story-driving |
| First / last | Ch 7 / Ch 55 |

### Arc

**Wants.** Power that no one can take away. His family lives in one room; he works three jobs
(the forge, night loading at the east gate, the furniture shop's deliveries beside the porter) and
trains after midnight.

**Fears.** Going home with nothing.

**Secrets.** He knew the porter from the furniture shop and liked him. He took the Undercroft's
money in the Jonin arc to move his family into a house; he has told no one.

**What he knows and when.**

| Knowledge | From |
|---|---|
| The porter was kind and strange (he never slept) | Before Y0 |
| The blade's style (from fighting him) | Ch 19 |
| The porter was the hand | Ch 28 (public in the shinobi ranks) |
| The Undercroft exists | Jonin arc (recruited between Ch 39 and Ch 44) |
| The Undercroft wants the lost child | Ch 44 (N3 and later open only after Ch 44) |

**How he changes.**

| Arc | Change |
|---|---|
| 1 Cinders | Ch 7: at the graduation, ignores everything; watches the player's clone test and says "Sloppy." |
| 3 Dusk | Ch 17: wins his preliminary in seconds. Ch 19.3: in the attack he joins the player's sensei against the blade on the arena floor, holds his own for six strokes, and takes a cut across the cheek (shown as a cut; the scar comes later, no blood). The blade, leaving, tells him "Good. Get a better sword." Promoted in Ch 20 |
| 4 Embers | Ch 28.5: at the porter's empty room, the morning after, he is already there with his hands in his pockets: "He carried my sister's cot up four floors. Wouldn't take a coin." (`shared_moment bond.squad5_c.porter`). Chunin, then ANBU at the end of the arc, younger than anyone in years. Brilliant and alone |
| 5 Ashes | Between Ch 39 and Ch 44, recruited by the Undercroft, an oath society of old ANBU and sealers (the heirs of the sealing team of the Quiet Ending) who meet in the derelict sealing hall under the old quarry: money for his family, and the promise of real power ("We'll teach you what the ANBU won't"). Ch 44: on the same A-rank hill as the player, he arrives in an ANBU mask with orders to take the lost child alive; she is gone before either of them reaches her, and he will not say whose orders |
| 6 Night Watch | N4: he guards the lost child's cell, masked; the player sees him through the bars. N6: he is the last of the old masks between the player and her. **Betray or not** (below) |
| 7 Last Bonfire | Ch 47 (if the Night Watch was declined or not finished; a half-played branch resolves here): the morning after she comes home to the shrine, he arrives with Undercroft orders to take her. **Betray or not** (below); either way the orders reach the Seventh and the Undercroft is disbanded quietly. Ch 51a: whatever happened, he comes to the wall later in the fight and holds a stretch of it |

**Betray or not** (N6, or Ch 47 if the Night Watch was declined or not finished; `story.squad5_c.stand`). The
player asks him: "What did they promise you?" His answer is `ans.squad5_c.offer` (his own words,
picked by the state of his life: `power` "That I'd never be powerless again", `house` "A house.
A door that locks", `teach` "Everything the ANBU won't teach", `nothing` "Nothing I wanted. I
just said yes"). Then the player answers him, and his earlier answers decide whether the words
reach him:

| Outcome | Needs | What happens |
|---|---|---|
| **Stands down** (talked down) | `friendship [squad5_c, 4]` and the player's reply meets his offer (power → "Nobody who holds a cage is free"; house → "You'll have one. Not like this"; teach → "I'll teach you myself"; nothing → "Then say no now"), helped by `ans.squad5_c.cage = key` or `ans.squad5_c.free = never` (either lowers the friendship need to 3); or the player tells him the Undercroft's plan for her (seen in N4) | He lowers his sword: "They said she was a weapon. She's a kid from a cell." In N6 he opens the cell himself and walks out of the Undercroft with the player; in Ch 47 he turns and guards the shrine stair. He returns the Undercroft's money (`stood_down`) |
| **Fights** | Otherwise | A full duel; beaten, he yields and leaves the ANBU (N6) or is arrested on the Seventh's order (Ch 47); released for the war, he comes to the wall later in Ch 51a and fights without a word (`fought`) |

He never kills anyone in either branch, and never fully joins the dark: the story says he was
offered a cage with a key and had to choose to use the key.

**Endings.** He lives. Stood down: the epilogue shows his family in their own house, paid for
honestly by a Jonin's wage, and him teaching kenjutsu to clanless kids for free. Fought: the same,
a year later, and he says "Thanks for beating me."

### Dialogue brief

**Voice.** Clipped, flat, precise; never thanks anyone (until he does, once); measures people by
technique; contempt for clan privilege, which softens into respect for people who work. Talks
about money plainly. Tic: counts coins under his breath, and ends a hard thought with "Pay it."
Never brags. Never says "I need help".

Voice samples, not shipped lines:
- "Sloppy."
- "No clan either? Then you'll have to be better than them. Good. So do I."
- (counting under his breath) "...four, five. Pay it."
- (to the blade, Ch 19, getting up) "Not done."
- (Ch 44) "Orders. Go home, {given:player}. This isn't yours."
- (stands down) "They said she was a weapon. She's a kid from a cell."

**Topics.** Training (1): kenjutsu, with real interest. Hobby (2): denies having one (he sharpens
blades for coins). Family (4): his sisters, the one room, his mother's cough. Values (5): "Nothing
is free. So pay." Dream (6): "A door that locks. My door." Worries (7): the money.

**Never reveal before.** The Undercroft: before Ch 44, nothing (N3 opens only after it); his recruitment: only at N4
or Ch 44 (he refuses to say who gives his orders before then). His feelings for the porter: only
from Ch 28.5 ("He carried my sister's cot up four floors. Wouldn't take a coin.").

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | Changes him |
|---|---|---|---|---|---|---|
| `ans.squad5_c.clan` | Level 2 or Ch 17 | "No clan either, right? So what did you get instead?" | Friends / A sensei / Nothing, I took what I needed / Time to train | Strength | His respect from then on; Ch 47 or N6: "You said ___" before the duel | "Took what I needed" makes the fight likelier (he hears himself); "friends" makes him scoff, then remember it in the stand-down |
| `ans.squad5_c.free` | Level 3 hangout (sharpening) | "Is power ever free?" | Never / Only when someone gives it / It is, if you take it | Strength | N6 / Ch 47: the stand-down condition | "Never" or "given" help him stand down; "take it" makes the fight more likely |
| `ans.squad5_c.money` | Level 4 | "What would you do for money if you had none?" | Anything honest / Anything / Ask for help | Family, pride | N4: he admits the Undercroft's money | "Ask for help": in Ch 51 he does, once |
| `ans.squad5_c.cage` | Level 5, Jonin arc (before Ch 44) | "If someone offered you a cage with a key inside it, would you go in?" | Yes, and use the key / No / Only for my family | Pride | N6 / Ch 47: the stand-down condition ("You said there was a key. Here it is.") | — |
| `ans.squad5_c.taught` | Level 6 | "Who taught you, really? Not the Academy. Who?" | My sensei / The camps / People I watched / Myself, like you | Strength | Epilogue: his free class's first lesson repeats it | — |
| `ans.squad5_c.porter` | Ch 28.5 (at the porter's room) or later at level 3 | "Did you hate him? The porter?" | No / I don't know / I miss him | Honesty | His only gentle line, at the shrine where the porter sweeps (Ch 47 or 54) | — |
| `ans.squad5_c.thanks` | Ch 54 | "I never said thanks. For anything. Do I have to?" | No / Once would be nice / You just did | Pride | Epilogue | — |
| `ans.squad5_c.offer` | N6 or Ch 47 | (His answer to "What did they promise you?"; the player's reply follows) | power / house / teach / nothing | Pride, family | The stand-down table above; epilogue: his free class's sign | — |
| `ans.squad5_c.scar` | Ch 20 (the cheek still bandaged) | "He said get a better sword. Should I?" | Yes / Keep yours, get better / I'll help you pay for one | Pride | Ch 51a: the sword he carries (a new one, the old one, or the one you bought with him); the blade's last duel (Ch 51.4) he asks "Better sword?" if he sees him | "Help pay": a level of trust (a favor he never forgets) |
| `ans.squad5_c.anbu` | End of the Chunin arc (his ANBU appointment) | "They want me in a mask at fifteen. Should I?" | Yes, you've earned it / Not alone / Only if it pays your family | Strength, family | Ch 44: under the mask he says "You said ___" | "Not alone": he asks for you to be told where he is; in Ch 44 he lets you see his face under the mask for a moment (unset: he stays masked) |
| `ans.squad5_c.sisters` | Level 4 | "My sisters want to meet the one who keeps beating me in races. Will you come?" | Yes / Bring food / Only if you stop letting me win | Family | A dinner-at-their-home hangout; Ch 47 or N6: the sisters are the reason his stand-down line works ("They asked about you") | — |

**Unison technique (Blaze).** *Edge of Dawn*: his single perfect draw, kindled, becomes a cut of
ember light that severs a cinder seal (or a dark mirror's line) without touching the person
behind it.

**Variants.** Varied: always clanless and poor (a role trait), any temperament that fits pride.
Flags: `story.squad5_c.stand` (`stood_down`, `fought`).

**New flags.** `ans.squad5_c.clan` (friends, sensei, took, time), `ans.squad5_c.free` (never,
given, take), `ans.squad5_c.money` (honest, anything, ask), `ans.squad5_c.cage` (key, no, family),
`ans.squad5_c.taught` (sensei, camps, watched, myself), `ans.squad5_c.porter` (no, unsure,
miss), `ans.squad5_c.thanks` (no, once, did), `ans.squad5_c.offer` (power, house, teach,
nothing), `ans.squad5_c.scar` (yes, keep, help_pay), `ans.squad5_c.anbu` (earned, not_alone,
pays), `ans.squad5_c.sisters` (yes, food, stop_letting); story flag `story.squad5_c.stand` (stood_down,
fought).
