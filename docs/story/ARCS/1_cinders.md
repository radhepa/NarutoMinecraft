# Arc 1: Cinders (the Academy, Ch 0 to 7, Beta 1)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Rules and
> backstory: [WORLD.md](../WORLD.md). Twist slots: [ROTATIONS.md](../ROTATIONS.md).

**~4 h** (2.8 h authored, 1.2 h systemic), about 12 in-game days. Child stage. Levels 1 to 5.

**What the arc is for.** Give an orphan a home, fast enough that the player feels it before the
story starts to threaten it. Plant every mystery so lightly that the beta reads as a life, not a
puzzle. By the end the player should love one bowl of ramen, one classmate, one adult, and want to
know who the girl in the next cell was.

**How each scene is written below:** *who is there* · *what happens* · *what it is for* · *what
the player can choose* (and the flags it sets). Scene functions: **plot** (moves the story),
**clue** (a mystery thread), **seed** (pays off later), **bond** (a relationship moment or
question), **teach** (a system), **life** (texture, humour).

---

## Ch 0: Cinders (20 min)

*Teaches: looking, sneaking, following, dodging, sprinting, climbing.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 0.1 | The creator screen | Player | Hair, eyes, skin, marks, outfit, a given name and the ordinary family name you remember from before the nurseries. The player is always a clanless orphan (clan-born play may return as an option later; for now the story is written for the orphan). The last step shows a small charred wooden charm, half of a pair, in the player's hand: "The only thing that is yours." | teach, seed (`item:half_charm`, `story.seed.half_charm`) | Look, given name, family name |
| 0.2 | The cell | Player, `lost_child`, two guards | You wake on straw in a cave cell. A guard in an ash-violet cloak raps the bars: "Nine. Up." Through the bars, the girl in the next cell is awake. She whispers: "They're taking me tonight. Here." She pushes a red cord through the bars: "So someone remembers I was here." The guards drag her away. She does not cry | plot, seed (`story.seed.lost_child_cord`, `story.seed.camp_number`: the word "Nine" is in the subtitle) | Say something back: "I'll remember" / "I'll find you" / say nothing (`ans.lost_child.cell`: remember, find, silent). Her return in Ch 24 and later echo this |
| 0.3 | Slipping out | Player | The cell's lock is old; an older child showed you the trick years ago. Sneak past sleeping guards; the hideout is emptying (crates, children led out in pairs) | teach (sneaking, looking) | Free the boy in the third cell on the way (+1 minute, a risk) or not (`ans.player.ch0.freed_boy`). If freed, he is one of the children the medic treats; he becomes a resident of the Leaf (an Academy junior who waves at you forever) |
| 0.4 | The raid | `captain`, `instructor`, `medic`, Leaf squad | Shouts; smoke; the Leaf squad bursts in. The `instructor` (cheerful even in a raid) scoops up two children; the `captain` cuts down a guard and looks at you for one long second | plot, bond | Run to the captain / hide / point toward where they took the girl (`ans.sensei.ch0`: run, hide, point). "Point" makes the captain send two shinobi after her: they find only an empty tunnel (the first failure the sensei carries) |
| 0.5 | The chase | Player, `captain` | Guards pursue; the squad splits. Follow the captain through the night forest: dodge, sprint, climb. You pass a burned shrine with a stone watch-fire basket still standing (the captain says nothing; you feel warm passing it) | teach, seed (`story.seed.ruined_shrine`) | — |
| 0.6 | The sample | `medic`, Player | At the rally point the medic checks every child, takes a drop of chakra on a paper slip, and writes it in a ledger: green ink, `p 88 / 112`, a tiny crane stroke. "For the records. Everyone gets one." | clue (`story.clue.medic.1`), seed (source notation) | — |
| 0.7 | The ravine | `captain`, Player | A rope bridge cut. The captain carries you on their back across the ravine on chakra-sticking feet. Halfway across: "Hold on. We're nearly out." | bond (`bond_event saved_by_them` with the captain) | — |
| 0.8 | The watcher | `yugure_leader` (silhouette) | From the far ridge a figure in a cloak with a sinking sun watches you go. The camera lingers; he raises a hand as if warming it at a fire | seed (`story.seed.watcher`) | — |

**Bond data.** `bond_event saved_by_them` (captain); `lost_child` bond created at level 2 with
`bond_flag red_cord` (it cannot grow while she is gone).

---

## Ch 1: A Key and a Bowl (20 min)

*Teaches: the HUD, ryo, shops, the apartment, talking, friendship.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 1.1 | The gate at night | `captain`, `instructor`, Hagane gate guards | The great gate; the four faces on the Rock lit by lanterns. The instructor: "That's where we're going to keep you. The whole place." | life | — |
| 1.2 | The Fourth | `hokage_4`, `elder_keeper`, `elder_councillor`, `captain` | The Hokage's office smells of grilled meat. The Fourth crouches to your height: "You came a long way. You hungry? Of course you are." He grants the orphan's stipend and a flat. The councillor hands over papers he prepared personally: "Stipend S-114. I saw to it myself." Pine seal on the corner. At the Fourth's shoulder, the keeper does not take his eyes off you | plot, clue (`story.clue.councillor.1`), seed (`story.seed.stipend`, `story.seed.keeper_noticed`, source notation S-114) | The Fourth asks: "What do you want to be, little one?" Strong enough that no one takes me again / Somewhere safe / To find the girl / Hokage (`ans.hokage_4.want`). His graduation speech (Ch 7) quotes it back |
| 1.3 | The flat | `porter`, Player | A one-room flat in a shinobi apartment block. A lanky young porter carries in a futon and a crate of bowls: "First home? I'll fix that sticky door. Doors should open for you." He does, and goes | plot, seed (the porter knows your door), teach (furnish mode intro) | Thank him / ask his name (`ans.porter.met`: asked or not. If asked, he hesitates before answering: he has to remember his cover name) |
| 1.4 | Morning: a bowl | `instructor`, `ramen_cook` | Ichiraku. "Miso or salt?" The instructor pays and tells you the Academy is not a test, it's a place. The cook remembers your order from now on | life, bond | Miso / salt / pork bone / "whatever you're having" (`ans.player.ramen`). Your order is your order for the whole game: the cook calls it out when you sit; friends tease you about it |
| 1.5 | Enrolment | `instructor`, the class (eleven classmates, [ENSEMBLE.md](../ENSEMBLE.md)) | The classroom. Introductions: `teammate_a` draws in a margin; `teammate_b` is late with a pup in their jacket; `classmate_c` lends you a pencil; `classmate_d` sits straight-backed with a wooden sword; the `rival` says "Another one from nowhere," and turns away. The rest of the class in a sweep: `squad3_a` correcting the instructor's arithmetic, `squad3_b` sharing rice crackers and being introduced, mortifyingly, as the Hokage's grandson, `squad3_c` watching everyone, `squad4_a` sitting at the exact centre of the front row, `squad4_b` and his enormous puppy, `squad4_c` smelling of mint | plot, bond | Introduce yourself: say where you came from / say "nowhere" / joke (`ans.player.intro`). The rival's later line in Ch 2 reads it |

**Seeds.** `story.seed.stipend`, `story.seed.keeper_noticed`, `story.clue.councillor.1`.
Systemic after Ch 1: shops, a first job at Ichiraku, furnishing, the first side-quest wave.

---

## Ch 2: Forms (20 min)

*Teaches: combo, heavy, dodge, block, practice kunai and shuriken.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 2.1 | Forms | `instructor`, class | Taijutsu forms in the yard; throwing at targets. The instructor praises everyone, specifically | teach | — |
| 2.2 | The spar | `rival` | A spar with the rival: they are better. Getting up after the first knockdown is the point (the spar ends at 30% health) | teach, bond | Win or lose (`spar_won`/`spar_lost`) |
| 2.3 | After | `rival` | By the water pump. The rival asks: "Who taught you to fall like that? Nobody falls like that here." | bond | The truth, "the camps" / "nobody" / "you'll have to beat it out of me" (`ans.rival.fall`). Truth: the rival is quiet, then says "...Then you've been fighting longer than me." The first crack in their pride. "Nobody": they don't believe you. Joke: rivalry +, they grin despite themselves |

---

## Ch 3: The Leaf on Your Brow (25 min)

*Teaches: chakra, meditation, hand signs (typed or radial).*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 3.1 | The leaf | `instructor`, class | A leaf held to the forehead by chakra unlocks the chakra bar. Comedy: `teammate_b`'s leaf keeps flying off | teach, life | — |
| 3.2 | The paired exercise | `teammate_a` | Partners pass chakra palm to palm into a scorched training post. Your chakra flares and for a moment takes on your partner's nature (shown with its effect: water beads on the scorched wood for a water nature, a spark for lightning, and so on). Your partner stares | plot, seed (`story.seed.flare`), bond (`bond_event trained_together`) | — |
| 3.3 | Hushed | `instructor`, `elder_keeper` (at the window) | The instructor claps: "Nice control, both of you! Next pair!" and moves everyone on too fast. At the window the keeper watches, then is gone. Behind you `squad3_c` whispers, half to himself: "Your chakra just moved into theirs." (Reply: "What do you mean?" / "Don't tell anyone" / walk away, `ans.squad3_c.moved`) | clue (the keeper, red herring), seed (squad3_c, paid in Ch 22) | — |
| 3.4 | After class | `teammate_a` | teammate_a catches you at the gate: "Did you feel that too? It was like you were... inside my chakra. Like a warm room." | bond | Yes, I felt it / No, you imagined it / "Don't tell anyone" (`ans.teammate_a.flare`). "Yes" and "don't tell" make it a shared secret (`bond_flag flare_secret`); in Ch 24 teammate_a says "That's the warm room again" if it was shared |
| 3.5 | The evening visit | `medic` | The medic drops by your flat "to check on you", checks your pulse, asks if anything strange happened today. Writes in a small notebook | clue (`story.clue.medic.2`) | Tell the medic about the flare / say nothing (`ans.medic.flare`). Telling has no effect on the bound answer; it changes the medic's reveal or clearing line |

---

## Ch 4: Sinking Sun (25 min)

*Teaches: night, fatigue, roof running, the cost of staying up.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 4.1 | A scratch | Player | Coming home after dark, a sinking sun is freshly scratched into your door, still smelling of soot | plot, seed (`story.seed.door_mark`) | — |
| 4.2 | The chase | Player, a cloaked figure (the `porter`) | A figure on the roof opposite. You chase it across the rooftops (roof running; fatigue grows past 01:00). It moves like someone who carries heavy things: low and steady | teach, clue (the figure's gait; Ch 28 calls back) | Keep chasing past 01:00 or go home (fatigue lesson). Chasing to the end is the main path |
| 4.3 | The door in the Rock | `elder_keeper` | The figure vanishes at the foot of the Rock, by a stone door with no handle and old seals. The keeper steps out of the dark: "Go home, child. This door is not for you, and neither is the night." | plot, seed (`story.seed.sealed_door`), clue (keeper red herring) | Ask "What's behind it?" / "Someone was here" / leave (`ans.elder_keeper.door`). "Someone was here": he looks at the door a beat too long and says "No one comes here." He is lying, and he is frightened |
| 4.4 | Morning | the landlady, `porter` | The landlady has painted over the mark ("kids"). The porter is in the stairwell with a crate for another flat and says good morning. (The paint hides an array anchor; nothing happens now) | life, seed | — |

---

## Ch 5: The Missing Page (15 min)

*Teaches: errands, the journal, inspecting.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 5.1 | Shelving | `librarian` | A library chore: shelve the Academy aptitude scrolls by shelf mark (`Leaf 7-iii`); some have a small brushed circle beside a name. "The circles are mine. Children who might need a little more." | teach, seed (source notation) | — |
| 5.2 | The page | `librarian` | Returning the founding history, you inspect it: a page has been cut out, its edge fresh and white. The librarian goes pale: "That page has been gone for years." (The edge says otherwise) | clue (`story.clue.librarian.1`, `.2`), seed (`story.seed.missing_page`) | Say "The cut is new" / let it go (`story.suspected.librarian` if the first and later you report it). She asks: "Do you think some things are better forgotten?" Yes, if remembering only hurts / No, forgetting is how it happens again / It depends who chose to forget (`ans.librarian.forget`). Pays off at her reveal or clearing |
| 5.3 | The Rock | `instructor` | The tour: four faces and four blank spots. "One day yours, maybe. Why not? Nobody's face starts up there." | seed (`story.seed.blank_spots`), bond | The instructor asks: "Whose face would you put up there, if you could pick anyone?" Someone who saved me (the captain) / Someone nobody remembers / Mine / Yours (`ans.instructor.face`). Callback when the Seventh's face (Ch 42) or yours (Ch 55) is carved |

---

## Ch 6: Exam Eve (20 min)

*Teaches: Clone, Transformation, Substitution; bond quests.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 6.1 | The study night | `classmate_c`'s family, the four classmates, `squad3_a`, `squad3_b` | At `classmate_c`'s home (a big table, a family who feeds everyone). `squad3_b` arrives with a tray from his mother's barbecue house and `squad3_a` with a study plan nobody follows. Practise the three techniques together; everyone fails at something. You learn each classmate's family and what they want to become (`reveal_fact` family and dream for each) | teach, bond (`studied_together` with all four) | — |
| 6.2 | The confidence | `teammate_b` | On the step outside, teammate_b tells you their parent walked out of the village years ago and never came back: "Everyone says missing-nin. Don't tell anyone, okay?" | bond, seed (b's parent) | Promise / tell them it isn't their fault / ask what the parent was like (`ans.teammate_b.parent_first`). The next morning the instructor asks you if b is all right: keep it (`kept_secret`, permanent moment) or tell the instructor (`broke_secret`, a quarrel) |
| 6.3 | The dream | `lost_child` (memory) | Asleep, the girl in the next cell; then, under it, a house with a persimmon tree and someone singing a song with no words you know (the watch-fire song, first heard) | seed (`story.seed.watchfire_song`) | — |

---

## Ch 7: Graduation (25 min)

*Teaches: the exam flow, promotion.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 7.1 | The exam | `instructor`, examiners | The quiz, the throwing test, the clone test. Failing a part allows one retry on Story difficulty | teach | — |
| 7.2 | The forehead protector | `instructor` | The instructor ties it on you personally, then wipes their eyes and pretends it's dust | bond | — |
| 7.3 | The Fourth's speech | `hokage_4`, the village | In the yard. He quotes your Ch 1 answer as if about all of them ("Some of you came here wanting to be strong enough that no one takes you again..."). The stipend ends: "From today you earn your own bowl. I'm proud of you." | bond, seed | — |
| 7.3b | Empty seats | `rival`, the senior squad | The families crowd the yard. Nobody has come for the `rival`; they stand very straight beside an empty space and leave before the speech ends. On the wall, a year-older squad watches the graduates: `squad5_a` cheering too loudly, `squad5_b` silent, `squad5_c` not looking at anyone | seed (Ch 43; the senior squad) | Go after the rival / let them go (`ans.rival.graduation`: went, let go). Going: they say "Don't," and you sit with them anyway, a `stood_by_them` memory. Ch 43 reads it |
| 7.4 | Watchers | `elder_keeper`, `porter` | The keeper nods to you once, stiffly. The porter is stacking the benches | clue (both, quietly) | — |

---

## Beta 1 bond quests (one per classmate)

Classic content below; Varied saves use the same structure with the object and setting swapped by
the character's archetype and dream (see each character's brief).

| Quest | Who | Beat | Question | Answer pays off |
|---|---|---|---|---|
| `bond.b1.classmate_a` | teammate_a | Climb to the overlook to paint the village; they cannot get the Rock right | "Should a painting show things as they are, or as they should be?" (`ans.teammate_a.paint`: are, should, both) | Their Kagari memorial mural (Ch 41): the true faces (are), the faces restored to the village (should), or both on two panels |
| `bond.b1.classmate_b` | teammate_b | The stray pup runs off again; track it to the old well where b's parent used to train | "Do you think people who leave can ever come back?" (`ans.teammate_b.come_back`: yes, only if they're sorry, no) | b's choice in the Chunin arc and when facing their parent in the war (Ch 51) |
| `bond.b1.classmate_c` | classmate_c | Help carve a gift for a parent | "What would you make for someone you've never met?" (`ans.classmate_c.make`) | c builds your clan hall's door (Ch 46) with it carved in |
| `bond.b1.classmate_d` | classmate_d | Witness a dawn kata | "Is it braver to stand in front of someone or beside them?" (`ans.classmate_d.stand`) | d becomes a Hokage's guard and says it when they take the post for you (Ch 55) |
