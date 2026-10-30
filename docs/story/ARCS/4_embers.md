# Arc 4: Embers (Chunin, Ch 21 to 32, later)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**~13 h** of main path: about **7 h authored** over 12 chapters (420 min) and **6 h systemic**, all
main path: about 5 B-rank board missions (~3.3 h, 35 to 45 min each, MISSIONS.md §1), the second-nature trials (~1 h), leading NPC
Genin on missions (~1 h) and training (~0.7 h). Side quests, clan lines and dating sit outside these
hours, as everywhere. Opens with the first time skip: **a year later** (Y+1), the player is 13, a
teen (0.9 scale); the arc spans about two seasons (Summer of Y+1 to the New Year into Y+2). Levels 18 to 30. The *taken* variant of
Ch 21 runs about 20 minutes longer. The arc's story B-ranks (four or five: Ch 21.1, 23, 24 and 27,
plus 21.2c only if the Fourth is taken) count toward ROADMAP §11's ten B-ranks for the Jonin trial, as
the chapter missions do at Ch 33.4; the story path never stalls on the count (SYSTEMS.md §3b).
**Where the board B-ranks sit:** they open with the Chunin vest at Ch 21; on the main path two or
three fall between Ch 21 and Ch 27 and the rest between Ch 27 and Ch 32, so a trail drop before
27.3 is possible but never required.

**What the arc is for.** The gift wakes, and the village stops being safe. The player learns what
they are (Kagari, though not yet what that means), learns that someone inside is helping the
enemy, and watches fear of their kind break a Hokage. The emotional centre is the border post:
the first time a friend falls for you and their fire answers. The arc ends with the village a
little wiser and the player trusted by one more Hokage and one old keeper of a door.

**Arc-wide systems.** The Fifth's **curfew**: from 22:00 a Chunin needs a night pass (your shadow,
`squad4_a`, can grant one); breaking curfew is a small bad deed with the `rank:chunin` community.
**B-rank missions** carry Yūgure trail drops (`mission.b.*`, see [SYSTEMS.md](../SYSTEMS.md)).
**Romance** opens at the teen stage (dating at level 7).

---

## Ch 21: A Year of Ash (35 min)

*The time skip. Variant by `twist.fourth_fate`.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 21.1 | A year | Player, squad | A montage of the year, playable in three short vignettes: a B-rank, a festival, a fight with the rival on the Rock. You are a teen. (A player not promoted in Ch 20 makes Chunin at the next season's exam inside this montage: a short vignette, and the sensei's line "Took you long enough. Good.") The flat has your furniture. The day you made Chunin you started wearing the red cord on your wrist, and you have not taken it off since | plot, life (`time_skip`) | — |
| 21.2a | *Falls*: the statue | the village | The Fourth's statue unveiled in the Academy yard; his daughter (who runs the barbecue house) gives you his old bowl: "He said you ate like he did." If you carried his bowl to the empty place at the feast (`ans.player.feast` = carried), she adds: "You carried it to him. Now it's yours to carry." (sat or unset: the base line) | bond | — |
| 21.2b | *Crippled*: the teacher | `hokage_4` | He teaches the Academy's history class from a wheelchair and asks you to help with the little ones. He is your mentor this arc (a weekly visit gives advice lines and small XP). Asked who could have known the finals' guard rotation, he says the same in every save: "Half the village, child. Medics, vendors, the council, the Academy." (the one version, [ROTATIONS.md](../ROTATIONS.md) §1) | bond | — |
| 21.2c | *Taken*: **The Empty Seat** | squad, `sensei`, `sensei_2`, `squad3_b`, `hokage_4` | A letter on ember-burned paper (the second's) gives a Yūgure hold in the hills. `sensei_2` leads; `squad3_b`, the Fourth's grandson, refuses to be left behind. A rescue: sneak, fight two hearths, and `squad3_b` carries his grandfather out. He is thin, grey, half his chakra torn away. "They practised on me," he says. "They're practising for something." He becomes a mentor as in 21.2b, too weak to rule | plot, seed (`story.seed.leader_practising`) | — |
| 21.3 | The stone | `sensei` | The Ash Road anniversary. The sensei leaves a dried persimmon, kept from last autumn, at the memorial stone, at the name beside the gap, as they do every year. "They loved these." If you told them about a persimmon tree in Ch 14, the sensei is silent a long time (both lineages: in A it is only memory) | seed (lineage) | — |

---

## Ch 22: Curfew (30 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 22.1 | Anomalous | sensor corps, `squad3_c` | A sweep of the shinobi apartment blocks. The sensor whose hand stops over you is your classmate `squad3_c`: "...Anomalous." He won't meet your eyes. You are summoned | plot, bond | That night he finds you: "I flagged you. Are you going to hate me?" Yes / No, you did your job / Ask me when I know what I am (`ans.squad3_c.flagged`) |
| 22.2 | The Fifth | `hokage_5`, `elder_hyuga`, `sensei` | The Fifth asks what the woman in the stadium said to you. The sensei stands behind you | plot, bond | Keep your promise and say nothing / tell her ("Kagari") / ask why she wants to know (`ans.hokage_5.word`). Saying nothing: the sensei's trust rises (`kept_promise`), the Fifth's falls. Telling: the elder flinches at the word; the Fifth's trust rises a little; the sensei's falls a little. Either way she assigns you a sensor to shadow you |
| 22.3 | Her question | `hokage_5` | "If your power endangered this village, what would you do?" | bond | Leave the village / Learn to control it / Trust the village to help me (`ans.hokage_5.danger`). Quoted back when she steps down (Ch 31) |
| 22.4 | The shadow | `squad4_a` | The Fifth assigns her own niece, your classmate `squad4_a`, to follow you everywhere with her Byakugan. She is mortified and exact about it. She becomes a friend if you let her (see [squad4.md](../CHARACTERS/squad4.md)) | bond, life | — |

---

## Ch 23: Ash-Violet (30 min)

*A story B-rank.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 23.1 | The free school | squad | A border market town has a "free school" for poor children, run by kind strangers who test every child with paper | plot | — |
| 23.2 | The test | squad | You go in under Transformation as a child. The tester's paper chars ash-violet in your hand, all the way | plot, seed | — |
| 23.3 | The tester | a Yūgure tester (the night patient, if `story.seed.night_patient`), `sensei_4` | Captured and questioned by `sensei_4`, the tester laughs: "The paper looks for the old fire. For people like you. We've been looking for children like you since before you were born." He knows nothing more (hearths know little) | plot | Let the squad hear it / take him aside first (`ans.player.tester_heard`). Letting them hear it shares the secret with the squad (`bond_flag knows_flame` for both teammates); they react in Ch 24.4 and 25.2 |
| 23.4 | The children | the children | Seven children to bring home to the Leaf orphanage; the smallest will not let go of your hand | plot, bond (`helped_resident`) | — |

---

## Ch 24: The Border Post (50 min)

The arc's centre. *Teaches: Thread Sight and the kindle.* The raid is the leader's design: the lost child is ordered to wound, never to kill the wick, and to make a friend fall so the gift wakes ([WORLD.md](../WORLD.md), the leader's plan).

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 24.1 | The signal | squad, `sensei` | A flare from the border post on the Ash Road. Reinforce it | plot | — |
| 24.2 | The raid | `lost_child` | The post is burning. A pale girl walks through it, an ash-violet scarf over her mouth, using three natures she should not have (stolen embers forced into her). Her eyes are flat; her voice repeats things others have said. Something about her is familiar (the way she holds her head, a small scar at the brow), but you are not sure | plot | — |
| 24.3 | The order | `sensei` | She is too strong. The sensei orders: "Fall back. Now." | bond | Obey / ask why (no time; it becomes obey) / stay and fight (`disobeyed_orders`). The sensei's response reads `ans.sensei.orders`: if you said you would do what's right, they say "Then do it right," and stay with you |
| 24.4 | The fall | the teammate at the highest level, at 6 or more; else the `sensei` | Her strike comes at you; your friend takes it and goes down (knocked out, gravely hurt). Their last words read their questions: teammate_a's line comes from one table in [teammate_a.md](../CHARACTERS/teammate_a.md) (priority: `ans.teammate_a.your_fear`, then `ans.teammate_a.freeze`, then unset); teammate_b the promise ("Told you. Drag me back—"; unset: "Don't you dare walk off—"); the sensei: "Keep your fire low—no. Not now." If the squad already knew of your fire (`bond_flag knows_flame`, Ch 23.3), a teammate adds the `knows_flame` line in their character file | bond (`saved_by_them`, permanent) | — |
| 24.5 | The awakening | Player, the fallen friend | (Story floor: the fallen friend counts as Spark whatever their level.) The world goes quiet and you see **threads**: light running from you to your friend, to the sensei, to the squad, one of them fraying where your friend lies. An ember mark burns on your palm. You push your chakra down the thread into them, and they rise for one moment and cast their *own* technique past every limit it has (teammate_a's painted genjutsu swallows the whole post; teammate_b and the pup's fang technique becomes a storm; the sensei's fire becomes a wall of flame across the post) | plot (`set_flag story.kindling.awakened`, `kindle`), teach (Spark: Thread Sight and a small kindle) | — |
| 24.6 | The cord | `lost_child` | The kindled technique breaks her attack. As she falls back she sees the red cord on your wrist and stops, and now you are certain: it is her. In the new sight she has no threads at all except one grey one, running along the cord to you. (`thread_floor`: the cord's grey thread shows whatever her level.) Her flat voice says your Ch 0 words back to you if you spoke them ("I'll remember"/"I'll find you"); if you said nothing, she says "...the cord. Kept. Kept." Then her hearth pulls her away | plot, bond (`lost_child` bond stays at 2; `bond_flag saw_cord`) | — |
| 24.7 | The ridge | `yugure_leader` | As the post burns down, a man in road clothes on the far ridge, watching, as in Ch 0. In your new sight he has **no threads at all**, not one, and the emptiness is the most frightening thing you have seen. He turns and is gone | plot, seed | — |

---

## Ch 25: What Burns (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 25.1 | Visitors | the four traitor candidates | In the hospital, the medic treats you; the librarian brings books; the councillor visits for the council; the merchant sends fruit with a note. **The bound candidate's line holds the slip** ([ROTATIONS.md](../ROTATIONS.md) §1) | clue (`story.clue.slip.heard`) | Talk to each (optional; all four are there or sent) |
| 25.2 | The friend | the fallen friend | They wake. They felt it. A teammate's waking line is the Ch 25 line in their character file, with its `knows_flame` variant ([teammate_a.md](../CHARACTERS/teammate_a.md), [teammate_b.md](../CHARACTERS/teammate_b.md)); the sensei says nothing for a long time, then "I've seen that fire before" (with `bond_flag knows_flame`: "So that's what the tester meant"). (A teammate in a falling-out is out of the squad and never the one who falls; their mends are listed in [SYSTEMS.md](../SYSTEMS.md) §3) | bond | — |
| 25.3 | The name | the `librarian` if `friendship [librarian, 3]`, else the `elder_keeper` (the same in every save, whoever the voice is) | They come at night with an old song book, and leave you a copied page of the watch-fire song, last line included, to keep (the keeper copies it from the archive's copy). The librarian, if it is her, tells you her family's secret: her grandmother was one of the old clan's children, renamed, and the family kept the songs (she holds back what the cut page listed). The book has the watch-fire song with its words (including the last line, which you will need on the Rock), and a drawing of a charm like your half. "Watch-fire charms are carved in pairs: one for a parent, one for a child." The gift has an old name: **Kindling** | plot, seed (lineage hint `story.lineage.hint`) | — |
| 25.3b | The other survivor | `sensei_3` | `sensei_3` visits once, late, and stands at the foot of the bed: "If you're what I think, they'll tell you about a road someday. When they do, remember I was sent away. I didn't run." | seed, bond | Say "I know you didn't" / ask what road / say nothing (`ans.sensei_3.spared`) |
| 25.4 | The sensei | `sensei` | The sensei sits by your bed (a falling-out with the sensei is mended here, `mend`). "Do you want to know what you are? Even if it changes how you see yourself?" | bond | Yes, everything / Only what I need / No, I'm me (`ans.sensei.know`). The sensei tells as much as you asked for. *Everything*: a teammate of theirs had this fire, how it burned and how they died for it. *Need* (and unset): only "A teammate of mine had this fire." *No*: "Good answer too," and nothing more. In every answer the box stays hidden ([sensei.md](../CHARACTERS/sensei.md)). Whatever the answer, if you sang them the hummed song in Ch 18 (`ans.sensei.song` = sing), they add that the song was a teammate's (both lineages; otherwise or unset: nothing) |
| 25.5 | Training, in secret | `sensei` (if `bond_meter [sensei, trust, 50]`), else the keeper or the librarian (whichever came in 25.3) | Kindling training at night at Training Ground 3: Thread Sight drills and small kindles (story floor: the trainer counts as Spark), away from your shadow `squad4_a` (whom you must evade or befriend into silence) | teach | — |

---

## Ch 26: The Bridge Again (35 min)

*`teammate_b`'s road. Reads `story.seed.teammate_approached`, `bond_meter [teammate_b, trust]` and `ans.teammate_b.forest_voice`.*

| Branch | When | What happens | Flags |
|---|---|---|---|
| **Stays** | trust 60 or more | A second note: "Your parent asked for you." b brings it straight to you. Together you set a watch on the bridge, the sensei waiting with you if b told them at 16.8 (`ans.teammate_b.forest_voice` = tell; keep or unset: the squad alone); the stranger comes, sees the trap and escapes over the water, ember-lit, and the squad sees her face: the woman from the stadium. b says: "My parent is with *them*." | `story.teammate_b.path = stayed` |
| **Nearly joins** | 30 to 59 | b goes to the bridge alone. You follow. **The well rule**: if the `drag_back` promise was made and trust is 45 or more, b turns back on the spot; otherwise the chase. At the old well outside the wall the stranger offers b an ash-violet scarf. b chooses by the well rule; failing it, b takes the scarf, walks a few steps, and you must chase and fight them, then talk them down (`squad_can_return` is bypassed by `return_to_squad`) | `story.teammate_b.path = nearly` |
| **Leaves** | under 30 | b quits the squad (`remove_from_squad story`) and stops speaking to you. They stay in the village, train alone, and are seen at the bridge some nights. A stand-in classmate joins. b's return is Ch 32 (if you do their return quest) or Ch 49.5 in Arc 7 | `story.teammate_b.path = left` |

In every branch, b learns their parent is alive and with Yūgure (`story.teammate_b.parent_alive`). If b leaves, `squad4_b` is the one who keeps b company at the bridge and tells you where to find them. **Thread Sight** shows b's thread fraying a few days before the bridge in every branch (`thread_floor`: it shows whatever b's level; `squad4_b` also tells you b has been quiet). A hangout with b in those days adds 10 to the trust that picks the branch, and so does `ans.teammate_b.grandma` (asked before the bridge). A b who already left the squad in a falling-out plays the **Leaves** branch.

---

## Ch 27: Shadows on the Water (30 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 27.1 | The pair | squad | A B-rank tracks a Yūgure pair (unusual: they move in hearths) to a river ferry | plot | — |
| 27.2 | The blade | `yugure_blade` | Duel two with the swordsman (the first was the cut bridge; he did not fight Genin). He fights like ink on paper: no wasted stroke. He is honourable: he lets you pick up a dropped kunai | plot, teach | — |
| 27.3 | The second | `yugure_second` | She stops the duel. To you: "Don't let them make you a candle." To the blade: "Not this one." They go | plot, seed (`story.seed.candle`) | Call after her: "Who are you?" / "What's a candle?" / nothing (`ans.yugure_second.first`). She answers only the second: "Something that burns so others can see". If `story.trail.count` ≥ 1 (a trail drop landed before 27.3), she adds one line as she goes: "And stop reading our marks on the roads. They aren't written for you." (identical in every rotation and lineage; 0 or unset: no line) |
| 27.4 | The persimmon | — | The next morning a persimmon sits on your windowsill. (Lineage A: the second. Lineage B: the sensei, on the first frost of autumn, the day they always buy the year's first persimmons. The player is told neither) | seed (lineage) | — |

---

## Ch 28: The Hand (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 28.1 | A new mark | Player, neighbours | A fresh sinking sun on a door in your block | plot | — |
| 28.2 | The stake-out | Player, `squad4_a`, your shadow (if befriended) | A night stake-out (fatigue, curfew pass). The figure again: low and steady, the gait of someone who carries heavy things (Ch 4 callback) | clue | — |
| 28.3 | The chase | `porter` | Over the rooftops, the same route as Ch 4. Caught on the Rock's slope. The hood comes off: the porter who fixed your door | plot | — |
| 28.4 | The seal | `porter`, `sensei_4` | He tries to say who sends him. A cinder seal in his palm, under the old burn scar, flares; `sensei_4` tries to bind it and cannot (`sensei_5`, arriving, reads the seal's strokes: "Whoever drew this has been drawing for a very long time"); he gets out: "The voice keeps the names in its own hand. Years in its own hand. All of them in its own hand." Then the seal burns his memory away | plot, clue (same line in every save) | Hold him while it burns / call for the medic / ask one more question (`ans.porter.end`). Holding him: he remembers your door, the last thing: "Doors should open for you" |
| 28.5 | After | `porter`, `medic`, `squad5_c` | He lives, gentle and empty, and later sweeps the shrine. In his room, `squad5_c` is already standing among the crates: "He carried my sister's cot up four floors. Wouldn't take a coin." (`shared_moment bond.squad5_c.porter`). His delivery ledger is found under the bed: every crate, sill and doorstep since he was sixteen (the Ch 49 array map, not yet understood) | seed (`story.seed.porter_ledger`), bond | — |

---

## Ch 29: Second Nature (30 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 29.1 | The trials | a nature master | The second-nature trials (systemic, three trials) frame the chapter | teach | — |
| 29.2 | The rival | `rival` | The rival has heard the rumour of your fire. A spar on the Rock ("Is it yours, or theirs?"). It is not the match the stadium never let you fight: before either of you wins, a carver's scaffold on the Rock's face gives way above a stonecutter's apprentice, and the rival gets there first. Reaching for more than they have, the rival's own power wakes (Classic: the Sharingan's first tomoe; Varied: their clan art's first real strength), and for a moment they are better than they have ever been. They set the apprentice down and will not look at you: "This doesn't count. You still owe me a match." | bond, plot | — (the spar has no result; the debt stays open to 51b.5 and the epilogue) |
| 29.3 | Their question | `rival` | "If your strength comes from other people, what's left when they're gone?" | bond | My memory of them / Nothing, so I won't let them go / Me, the person they chose to trust (`ans.rival.theirs`). Ch 53: the rival's line when they offer their flame answers yours |

---

## Ch 30: Smoke in the Lanes (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 30.1 | Cinder bombs | the village | Three cinder bombs in the dark lanes behind the wall, in the Tobari quarter. No one heard a thing: a sound-smothering technique | plot, mood (`mood_event village tension`) | — |
| 30.2 | Lockdown | `hokage_5`, `sensei_2` (now Jonin Commander), sensor corps, Tobari elders, `squad5_b` | The Fifth locks the Tobari quarter down: a Tobari deserter is known to have taught Yūgure that technique. `sensei_2` enforces it, joking badly and hating it. The Hagane gate guards, who share the wall with the Tobari, refuse night duty in protest. `squad5_b`, the senior squad's silent Tobari scout, is locked in with her family | plot | — |
| 30.3 | teammate_a's choice | `teammate_a` | The sensor corps wants teammate_a (a gift for illusions and sensing). Their family wants it. They ask you (reads `ans.teammate_a.family`) | bond | Join if you want to / Don't let them choose for you / Join, and keep your eyes open for us (`ans.teammate_a.corps`). Their path in the Jonin arc (a sensor captain, or a painter-shinobi who paints the memorial) |
| 30.4 | The lanes | `squad5_b`, `squad4_a` | Get `squad5_b` out of the quarter (with your shadow's help, or by persuading `squad4_a` to look the other way: her first disobedience) and investigate the lanes at night with her. She hears what no one else does (the `clan.tobari.3` line, if done, gives a shortcut) | teach, clue | She asks: "You need a night pass and you will not tell me why. Do I write it?" Trust me / Come with me and see / Write it down, I'll take the blame (`ans.squad4_a.pass`); without a pass you sneak past her |

---

## Ch 31: The Quarter at the Wall (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 31.1 | The drain | a Yūgure hearth, `squad5_b`, your squad | The hearth hides in the old storm drain under the wall. A fight in the dark, sound smothered. You bind your squad into one flame for the first time: a shared pool, seeing through `squad5_b`'s ears and your teammates' eyes in the dark (story floor: everyone in the drain, the squad as fielded, any Squad 2 stand-in and `squad5_b`, counts as Flame for 31.1 to 31.2) (Flame: Ember Link; the floor above binds everyone in the drain, so it plays in every save; this is the one statement of the 31.1 link) | plot, teach | — |
| 31.2 | Seen | `squad5_b`'s grandmother (a Tobari elder), the sensor corps | The fight spills into the quarter's square; you kindle in the open. `squad5_b`'s grandmother, watching, does something no one has done: she offers you her fire (`offered_flame`: the one way someone below level 6 can kindle toward you). A thread of light runs *to* you from someone you barely know. (Milestone: the gift seen in the open) | plot, bond | — |
| 31.3 | The council | `hokage_5`, council, the Tobari, `squad4_a`, `sensei_2` | You bring the hearth to the council and testify (a Chunin may testify). The councillor abstains "for the registry's neutrality" (the same in every save). `squad4_a` testifies after you, against her aunt's lockdown, in front of her whole house. Your testimony names what the woman in the stadium called you; `sensei_2` hears the word "Kagari" for the first time, puts down the Commander's armband: "I'm with the kid." The Tobari's innocence is plain | plot | How you testify: for the Tobari / against the lockdown / for the Fifth's right to fear, but not this way (`ans.player.testify`). Read later by `elder_hyuga`'s question at the Jonin review (Ch 33.3) and by the former Fifth on the wall (Ch 51a); unset: "you spoke for them" |
| 31.4 | The Fifth steps down | `hokage_5` | She steps down to take responsibility: "I asked you what you'd do if your power endangered the village. I should have asked myself." Quotes `ans.hokage_5.danger` | plot, bond | — |

---

## Ch 32: The Sixth (30 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 32.1 | The Sixth | `hokage_6`, the village | At New Year (WORLD.md, the calendar rule), a soft-spoken Yamanaka is named Sixth Hokage. The Fifth's face is carved on the Rock (story beat) | plot (`set_hokage 6`, `carve_face 5`) | — |
| 32.2 | The keeper | `elder_keeper` | If `bond_meter [elder_keeper, trust, 40]`: he asks to walk with you. "Come to me when you are a Jonin. I will show you a door." Else he only nods | seed | — |
| 32.3 | b comes back | `teammate_b` (if they left on the Ch 26 *left* path) | If `teammate_b` left at Ch 26 and their return quest (`bond.teammate_b.return`, SYSTEMS §2) is done: b at the bridge at dawn: "You were supposed to drag me back. You took your time." (if `ans.teammate_b.drag_back` is set, any answer; unset: only "You took your time.") If the quest is done after Ch 32 and before Ch 49, the same scene plays at the next dawn. A b in a falling-out (held at level 2 or below) cannot reach the quest's `friendship 4`; they skip Ch 32 and come back at Ch 49.5 | bond (`return_to_squad`, `reconciled`) | — |
| 32.4 | On the Rock | squad, `sensei`, the class | The whole class on the Rock above the new face, as Chunin now (`squad4_b` too, if `side.c.third_time` is done; else he shouts up from below). The sensei: "Jonin, then. All of you. Four years." | bond, photo (`photo.story.class_on_rock`) | — |

The second time skip (**four years**, to Y+6; the player is 18, an adult) opens the Jonin arc.
