# Arc 4: Embers (Chunin, Ch 21 to 32, later)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**~13 h** (about 6.5 h authored over 12 chapters, 6.5 h systemic: about 10 B-rank board missions,
the second-nature trials, clan lines' steps 2 and 3, Chunin side quests, the first dating). Opens
with the first time skip: **a year later**, the player is a teen (0.9 scale). Levels 18 to 30.

**What the arc is for.** The gift wakes, and the village stops being safe. The player learns what
they are (Kagari, though not yet what that means), learns that someone inside is helping the
enemy, and watches fear of their kind break a Hokage. The emotional centre is the border post:
the first time a friend falls for you and their fire answers. The arc ends with the village a
little wiser and the player trusted by one more Hokage and one old man who keeps a door.

**Arc-wide systems.** The Fifth's **curfew**: from 22:00 a Chunin needs a night pass (the sensor
shadow can grant one); breaking curfew is a small bad deed with the `rank:chunin` community.
**B-rank missions** carry Yūgure trail drops (`mission.b.*`, see [SYSTEMS.md](../SYSTEMS.md)).
**Romance** opens at the teen stage (dating at level 7).

---

## Ch 21: A Year of Ash (35 min)

*The time skip. Variant by `twist.fourth_fate`.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 21.1 | A year | Player, squad | A montage of the year, playable in three short vignettes: a B-rank, a festival, a fight with the rival on the Rock. You are a teen. The flat has your furniture; the cord hangs by your bed | plot, life (`time_skip`) | — |
| 21.2a | *Falls*: the statue | the village | The Fourth's statue unveiled in the Academy yard; his daughter (who runs the barbecue house) gives you his old bowl: "He said you ate like he did" | bond | — |
| 21.2b | *Crippled*: the teacher | `hokage_4` | He teaches the Academy's history class from a wheelchair and asks you to help with the little ones. He is your mentor this arc (a weekly visit gives advice lines and small XP) | bond | — |
| 21.2c | *Taken*: **The Empty Seat** | squad, `sensei`, `hokage_4` | A letter on ember-burned paper (the second's) gives a Yūgure hold in the hills. A rescue: sneak, fight two cells, carry him out. He is thin, grey, half his chakra torn away. "They practised on me," he says. "They're practising for something." He becomes a mentor as in 21.2b, too weak to rule | plot, seed (`story.seed.leader_practising`) | — |
| 21.3 | The stone | `sensei` | The Ash Road anniversary. The sensei leaves a persimmon at the memorial stone, at the name beside the gap, as they do every year. "They loved these." If you told them about a persimmon tree in Ch 14, the sensei is silent a long time (both lineages: in A it is only memory) | seed (lineage) | — |

---

## Ch 22: Curfew (30 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 22.1 | Anomalous | sensor corps | A sweep of the shinobi apartment blocks. A sensor's hand stops over you: "Anomalous." You are summoned | plot | — |
| 22.2 | The Fifth | `hokage_5`, `elder_hyuga`, `sensei` | The Fifth asks what the woman in the stadium said to you. The sensei stands behind you | plot, bond | Keep your promise and say nothing / tell her ("Kagari") / ask why she wants to know (`ans.hokage_5.word`). Saying nothing: the sensei's trust rises (`kept_promise`), the Fifth's falls. Telling: the elder flinches at the word; the Fifth's trust rises a little; the sensei's falls a little. Either way she assigns you a sensor shadow |
| 22.3 | Her question | `hokage_5` | "If your power endangered this village, what would you do?" | bond | Leave the village / Learn to control it / Trust the village to help me (`ans.hokage_5.danger`). Quoted back when she steps down (Ch 31) |
| 22.4 | The shadow | `sensor_shadow` | A young Hyuga Chunin, assigned to follow you everywhere, awkward about it. They become a friend if you let them (a minor bond with its own question, see the character file) | bond, life | — |

---

## Ch 23: Ash-Violet (40 min)

*A story B-rank.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 23.1 | The free school | squad | A border market town has a "free school" for poor children, run by kind strangers who test every child with paper | plot | — |
| 23.2 | The test | squad | You go in under Transformation as a child. The tester's paper chars ash-violet in your hand, all the way | plot, seed | — |
| 23.3 | The tester | a Yūgure tester (the night patient, if `story.seed.night_patient`) | Captured, the tester laughs: "The paper looks for the old fire. For people like you. We've been looking for you for six years." He knows nothing more (cells know little) | plot | Let the squad hear it / take him aside first (`ans.player.tester_heard`). Letting them hear it shares the secret with the squad (`bond_flag knows_flame` for both teammates); they react in Ch 24 |
| 23.4 | The children | the children | Seven children to bring home to the Leaf orphanage; one has a red thread on her wrist like your cord, a Yūgure tally | plot, bond (`helped_resident`) | — |

---

## Ch 24: The Border Post (60 min)

The arc's centre. *Teaches: the kindle effect (if the final design differs, the nearest ability).*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 24.1 | The signal | squad, `sensei` | A flare from the border post on the Ash Road. Reinforce it | plot | — |
| 24.2 | The raid | `lost_child` | The post is burning. A pale girl walks through it in an ash-violet cloak, using three natures she should not have (stolen embers forced into her). Her eyes are flat; her voice repeats things others have said. She is the girl from the next cell | plot | — |
| 24.3 | The order | `sensei` | She is too strong. The sensei orders: "Fall back. Now." | bond | Obey / ask why (no time; it becomes obey) / stay and fight (`disobeyed_orders`). The sensei's response reads `ans.sensei.orders`: if you said you would do what's right, they say "Then do it right," and stay with you |
| 24.4 | The fall | the teammate at the highest level, at 6 or more; else the `sensei` | Her strike comes at you; your friend takes it and goes down (knocked out, gravely hurt). Their last words before the fall read their questions: teammate_a's fear (`ans.teammate_a.your_fear`: "You won't be alone—"), the freeze ("I didn't freeze"); teammate_b's promise ("Told you. Drag me back—"); the sensei: "Keep your fire low—no. Not now." | bond (`saved_by_them`, permanent) | — |
| 24.5 | The kindling | Player, the fallen friend | Their chakra leans toward you like the campfire did. A small watch-fire flame burns between your hand and theirs. Their nature is yours for a few casts | plot (`set_flag story.kindling.awakened`, `kindle`), teach | — |
| 24.6 | The cord | `lost_child` | You finish the fight with their nature. As she falls back she sees the red cord on your wrist and stops. Her flat voice says your Ch 0 words back to you if you spoke them ("I'll remember"/"I'll find you"); if you said nothing, she says "...someone remembers." Then the cloaks pull her away | plot, bond (`lost_child` bond stays at 2; `bond_flag saw_cord`) | — |

---

## Ch 25: What Burns (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 25.1 | Visitors | the four traitor candidates | In the hospital, the medic treats you; the librarian brings books; the councillor visits for the council; the merchant sends fruit with a note. **The bound candidate's line holds the slip** ([ROTATIONS.md](../ROTATIONS.md) §1) | clue (`story.clue.slip.heard`) | Talk to each (optional; all four are there or sent) |
| 25.2 | The friend | the fallen friend | They wake. They saw the flame. "That was the warm room again" (teammate_a, if the Ch 3 flare was shared) / "You stole my move!" (teammate_b) / the sensei says nothing for a long time, then "I've seen that fire before" | bond | — |
| 25.3 | The name | the `librarian` if innocent and at `friendship 3`, else the `elder_keeper` | They come at night with an old song book: the watch-fire song, and a drawing of a charm like your half. "Watch-fire charms are carved in pairs: one for a parent, one for a child." The gift has an old name: **Kindling** | plot, seed (lineage hint `story.lineage.hint`) | — |
| 25.4 | The sensei | `sensei` | The sensei sits by your bed. "Do you want to know what you are? Even if it changes how you see yourself?" | bond | Yes, everything / Only what I need / No, I'm me (`ans.sensei.know`). The sensei tells as much as you asked for: that a teammate of theirs had this fire, and died for it |
| 25.5 | Training, in secret | `sensei` (if `bond_meter [sensei, trust, 50]`), else the keeper or librarian | Kindling training at night at Training Ground 3, away from the sensor shadow (whom you must evade or befriend into silence) | teach | — |

---

## Ch 26: The Bridge Again (45 min)

*`teammate_b`'s road. Reads `story.seed.teammate_approached` and `bond_meter [teammate_b, trust]`.*

| Branch | When | What happens | Flags |
|---|---|---|---|
| **Stays** | trust 60 or more | A second note: "Your parent asked for you." b brings it straight to you. Together you set a watch on the bridge; the stranger comes, sees the trap and escapes over the water, ember-lit, and the squad sees her face: the woman from the stadium. b says: "My parent is with *them*." | `story.teammate_b.path = stayed` |
| **Nearly joins** | 30 to 59 | b goes to the bridge alone. You follow (the promise `ans.teammate_b.drag_back` gives you a line that stops them). At the old well outside the wall the stranger offers b a cloak. b chooses: if the drag-back promise was made and your trust is at least 45, b turns back on the spot; else b takes the cloak, walks a few steps, and you must chase and fight them, then talk them down (`squad_can_return` is bypassed by `return_to_squad`) | `story.teammate_b.path = nearly` |
| **Leaves** | under 30 | b quits the squad (`remove_from_squad story`) and stops speaking to you. They stay in the village, train alone, and are seen at the bridge some nights. A stand-in classmate joins. b's return is Ch 32 (if you do their return quest) or the Jonin arc | `story.teammate_b.path = left` |

In every branch, b learns their parent is alive and with Yūgure (`story.teammate_b.parent_alive`).

---

## Ch 27: Shadows on the Water (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 27.1 | The cell | squad | A B-rank tracks a two-man cell to a river ferry | plot | — |
| 27.2 | The blade | `yugure_blade` | Duel two with the swordsman (the first was the cut bridge; he did not fight Genin). He fights like ink on paper: no wasted stroke. He is honourable: he lets you pick up a dropped kunai | plot, teach | — |
| 27.3 | The second | `yugure_second` | She stops the duel. To you: "Don't let them make you a candle." To the blade: "Not this one." They go | plot, seed (`story.seed.candle`) | Call after her: "Who are you?" / "What's a candle?" / nothing (`ans.yugure_second.first`). She answers only the second: "Something that burns so others can see" |
| 27.4 | The persimmon | — | The next morning a persimmon sits on your windowsill. (Lineage A: the second. Lineage B: the sensei, on the anniversary) | seed (lineage) | — |

---

## Ch 28: The Hand (45 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 28.1 | A new mark | Player, neighbours | A fresh sinking sun on a door in your block | plot | — |
| 28.2 | The stake-out | Player, the sensor shadow (if befriended) | A night stake-out (fatigue, curfew pass). The figure again: low and steady, the gait of someone who carries heavy things (Ch 4 callback) | clue | — |
| 28.3 | The chase | `porter` | Over the rooftops, the same route as Ch 4. Caught on the Rock's slope. The hood comes off: the porter who fixed your door | plot | — |
| 28.4 | The seal | `porter` | He tries to say who sends him. A cinder seal on his tongue burns; he gets out: "The voice keeps the names in its own hand. Six years in its own hand." Then the seal burns his memory away | plot, clue (same line in every save) | Hold him while it burns / call for the medic / ask one more question (`ans.porter.end`). Holding him: he remembers your door, the last thing: "Doors should open for you" |
| 28.5 | After | `porter`, `medic` | He lives, gentle and empty, and later sweeps the shrine. His delivery ledger is found in his room: every crate, sill and doorstep for six years (the Ch 49 array map, not yet understood) | seed (`story.seed.porter_ledger`) | — |

---

## Ch 29: Second Nature (30 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 29.1 | The trials | a nature master | The second-nature trials (systemic, three trials) frame the chapter | teach | — |
| 29.2 | The rival | `rival` | The rival has heard the rumour of your fire. A spar on the Rock: "Is it yours, or borrowed?" | bond | Spar (`spar_won`/`spar_lost`) |
| 29.3 | Their question | `rival` | "If your strength comes from other people, what's left when they're gone?" | bond | My memory of them / Nothing, so I won't let them go / Me, the person they chose to trust (`ans.rival.borrowed`). Ch 53: the rival's line when they offer their flame answers yours |

---

## Ch 30: Smoke in the Lanes (45 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 30.1 | Cinder bombs | the village | Three cinder bombs in the dark lanes behind the wall, in the Tobari quarter. No one heard a thing: a sound-smothering technique | plot, mood (`mood_event village tension`) | — |
| 30.2 | Lockdown | `hokage_5`, sensor corps, Tobari elders | The Fifth locks the Tobari quarter down: a Tobari deserter is known to have taught Yūgure that technique. The Hagane gate guards, who share the wall with the Tobari, refuse night duty in protest | plot | — |
| 30.3 | teammate_a's choice | `teammate_a` | The sensor corps wants teammate_a (a gift for illusions and sensing). Their family wants it. They ask you (reads `ans.teammate_a.family`) | bond | Join if you want to / Don't let them choose for you / Join, and keep your eyes open for us (`ans.teammate_a.corps`). Their path in the Jonin arc (a sensor captain, or a painter-shinobi who paints the memorial) |
| 30.4 | The lanes | a Tobari watchman | Investigate the lanes at night with a Tobari watchman (the `clan.tobari.3` line, if done, gives a shortcut) | teach, clue | — |

---

## Ch 31: The Quarter at the Wall (50 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 31.1 | The drain | a Yūgure cell | The cell hides in the old storm drain under the wall. A fight in the dark, sound smothered | plot | — |
| 31.2 | Seen | Tobari elders, the sensor corps | The fight spills into the quarter's square; you kindle in the open. A Tobari elder, watching, does something no one has done: offers you their fire. A flame leans *toward* you from a near-stranger (a resident at friendship 3 or more with you; else the Tobari watchman). (Milestone: the gift seen in the open) | plot, bond | — |
| 31.3 | The council | `hokage_5`, council, the Tobari | You bring the cell to the council and testify (a Chunin may testify). The Tobari's innocence is plain | plot | How you testify: for the Tobari / against the lockdown / for the Fifth's right to fear, but not this way (`ans.player.testify`) |
| 31.4 | The Fifth steps down | `hokage_5` | She steps down to take responsibility: "I asked you what you'd do if your power endangered the village. I should have asked myself." Quotes `ans.hokage_5.danger` | plot, bond | — |

---

## Ch 32: The Sixth (30 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 32.1 | The Sixth | `hokage_6`, the village | A soft-spoken Yamanaka is named Sixth Hokage. The Fifth's face is carved on the Rock (story beat) | plot (`set_hokage 6`, `carve_face 5`) | — |
| 32.2 | The keeper | `elder_keeper` | If `bond_meter [elder_keeper, trust, 40]`: he asks to walk with you. "Come to me when you are a Jonin. I will show you a door." Else he only nods | seed | — |
| 32.3 | b comes back | `teammate_b` (if they left) | If `teammate_b` left and their return quest is done: b at the bridge at dawn: "You were supposed to drag me back. You took your time" | bond (`return_to_squad`, `reconciled`) | — |
| 32.4 | On the Rock | squad, `sensei` | The squad on the Rock above the new face. The sensei: "Jonin, then. All of you. Three years." | bond | — |

The second time skip (three years) opens the Jonin arc.
