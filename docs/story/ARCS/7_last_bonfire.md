# Arc 7: The Last Bonfire (Road to Hokage, Ch 46 to 55, later)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**~15 h** main path: about 7.6 h authored over 11 chapters (455 min) and about 7.4 h systemic
main-path play. Story time Y+7 to Y+8. Levels 42 to 50.

**Where the systemic play sits.** All of it before the war, so nothing is a grind after it:

| When | Systemic main-path play | About |
|---|---|---|
| Between Ch 46 and Ch 48 | S-ranks clearing the last hearths (each one cleared removes a wave from Ch 51a; `story.cells_cleared`), raising your house (the registry's tasks, recruiting), leading your Genin, the fourth-nature trial | ~5 h |
| Ch 50 (after its authored core) | The anchor hunt across the village | ~1.5 h |
| The war's eve (between Ch 50 and Ch 51a) | Last hangouts and rituals before the war, the village's defences, Genin and house tasks | ~0.9 h |
| Ch 49 gate | Level 47 | — |
| Levels 48 to 50 | The anchor hunt, the war's eve and the war; finishing Ch 53 applies a level-50 floor | — |

Standing earned through side quests helps (it opens anchors in Ch 50), but the main path never
waits on it. Clan lines' Legacy steps are side content.

**What the arc is for.** Everything the player has built is tested at once. The truth of the
player's own blood, the enemy's real goal, and the answer to the story's first image (a child in a
cell, a girl pushing a red cord through bars so someone remembers). The finale is won by the
village the player befriended: the fire's size is the bond web, and every flame has a face the
player knows. A player who befriended few still wins, with a smaller fire and an honest ending.

---

## Ch 46: Old Ground (45 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 46.1 | The registry | the Seventh, the registry clerk | The registry offers a founding path no one has offered in eighty years: **restore the Kagari** under their old name and crest, on their old ground (the vacant estate nearest the south gate, and the shrine in the hills as the clan shrine), with the gift as the clan art. On the story path the fee and the standing requirement are waived in every save (the Seventh signs it; if the councillor is innocent and free, he co-signs as flavour). The registry also lets you take your house's name as your family name, or keep the one you remembered | plot (`found_clan`) | By the player's state (below) (`story.clan.choice`) |
| 46.2 | The shrine | Player, `classmate_c` | Clear the burned shrine; the stone watch-fire basket from Ch 0 stands. classmate_c's family builds the hall's door and carves into it what they would make for someone they never met (`ans.classmate_c.make`; unset: a watch-fire basket) | plot, bond | — |
| 46.3 | The first members | descendants | Descendants come to the shrine, shaped by `ans.hokage_6.names` (the table in Ch 40). Some want to join; some only want to see. Recruitment (systemic, BONDS §10) | systems | Who you invite |
| 46.4 | Night work | the registry clerk | If the Night Watch is half played and N4.1 has not begun, the registry asks before you sign: finish the night work first, or go on (going on closes the branch through Ch 47) | systems | Finish first / go on |

**The player's state at Ch 46** (the player may have founded or joined a clan earlier, ROADMAP §11,
BONDS §10):

| State | The choice | `story.clan.choice` |
|---|---|---|
| No clan | Restore the Kagari / found a clan of your own | `kagari` / `own` |
| Already founded your own clan | Re-crest it as the Kagari, keeping its members and adding the shrine / keep your clan and enshrine the Kagari at the shrine as your house's ancestors | `rekindled_own` / `enshrined` |
| Joined another clan (invitation or marriage) | Restore the Kagari as a house that stays kin of your host clan (relation +10) / leave your host clan to restore the Kagari (relation −10 with the host clan; your spouse may follow) | `kin_of_host` / `left_host` |

Every value is "your house" to the story from here on.

---

## Ch 47: The Lost Child / Home Fires (45 min)

Waits until the Night Watch is finished or declined (a half-played branch closes through this
chapter).

| If | What happens |
|---|---|
| **Night Watch not finished** | **The Lost Child.** She comes to the shrine at night, half hollow, hunted by Yūgure for deserting. A hearth follows her. You fight them off at the stone basket, then kindle her own flame back alive through the cord, as in N6 (shorter: the shrine's old fire helps). Her first words: "I found you this time." (variants by `ans.lost_child.cell`). `story.lost_child.home = shrine`. The cord cannot be lost, so this always plays: she comes home in every save |
| **`squad5_c`**, Night Watch not finished | The next morning, `squad5_c` comes to the shrine with Undercroft orders to take her. Talk him down (`ans.squad5_c.offer`) or fight him: a betrayal, or not (`story.squad5_c.stand`). Either way the orders reach the Seventh, and the Undercroft is disbanded quietly |
| **Night Watch finished** | **Home Fires.** Her recovery, with `squad4_c` tending her and the medic watching. She stays at your house's hall. She asks the questions she never got to ask in the cells (see her character file); a walk through the village she never grew up in; the first bowl of ramen. Her answers to your questions become who she is |

---

## Ch 48: Persimmons (50 min)

The lineage reveal (`twist.lineage`, [ROTATIONS.md](../ROTATIONS.md) §2).

| | **A: the second** | **B: the fallen Leaf shinobi** |
|---|---|---|
| How it starts | A letter on ember-burned paper in your mailbox: a far village name and a day | The Seventh, waiting in your flat: "Walk with me. It's a long walk" |
| The place | The ruins of the persimmon house in a border village; the tree is alive, heavy with fruit | The same |
| Who is there | `yugure_second`, alone, unarmed. She has left Yūgure: in the leader's records she found "Nine: her child. Keep from her." | The Seventh, with the box: `fallen_parent`'s forehead protector, half a watch-fire charm and an unsent letter |
| The proof | Her half of the charm; the halves fit | The box's half; the halves fit (the Seventh has never seen your half before; it stayed sewn in your sleeve) |
| The heart of it | She tells you first: "The map, the night they raided the hills. That was mine. I didn't know you were in there." Then: "I sang you that song. I didn't know you'd keep it. He told me you burned with the house." And, about the stadium: "I nearly told him how you burn." | "I carried you over a ravine and didn't know. Then I suspected, and the report said the persimmon house burned with everyone in it, and I was afraid to be wrong, so I never opened the box." |
| The player's answer | "You're my mother" / "You left me" / "You saved me twice" (the map, the forest) (`ans.player.parent_meet`) | "You found me anyway" / "You should have looked" / say their teammate's name (`ans.player.parent_meet`) |
| After | She asks for nothing. She will tell you what she knows (Ch 49) | The second's letter arrives that night (her defection, Ch 49): the Valley children (Ch 35) told her of the nursery where her son died, and she went into the leader's notes looking for him |

---

## Ch 49: The Hollow Crown (40 min)

*Needs level 47.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 49.1 | The truth | `yugure_second`, the Seventh, Player | She tells the Seventh's council the leader's true plan: the array, the Hearthstone, the wick, the taking ([WORLD.md](../WORLD.md)). "The Bonfire was never for all of us. It was for him." She learned it from his own notes. The blade does not know | plot (`story.hollow_crown.known`), bond (a `shared_moment bond.second.truth` if you vouch or let her speak: her first real moment with you) | Whether the council trusts her: you vouch / you let her speak for herself / you say nothing (`ans.player.vouch`). Vouching ties your standing to her (a deed) |
| 49.2 | The map | Player, the porter's ledger | The porter's ledger (Ch 28) is the array: eighty-one doorsteps, sills and crates. One of them is your old door (Ch 4). `squad3_c` can feel the anchors once he knows what to listen for; `squad3_a` turns the ledger into a plan; `sensei_5` teaches the village to break a cinder seal | plot, seed paid (`story.seed.door_mark`, `story.seed.porter_ledger`) | — |
| 49.4 | Why the wick goes up | `yugure_second`, the Seventh, Player | The array's rule, from the leader's notes: once lit, it drags every chakra in its reach into **the strongest Kagari flame in reach, wherever it stands**. Hiding you would only make it pick another wick (genin_3, the lost child, the second) or hollow you in place. The Hearthstone on the Rock is the only place the array can be broken. The Seventh argues against you going up anyway ("I carried you out once. I'm not sending you back in.") | plot, bond | Go up / let the Seventh plan without you, for now (`ans.player.go_up`; the Seventh argues again at 51b and you go in every save; the answer changes their last line before the climb) |
| 49.5 | b comes back | `teammate_b` (if b left the squad or had a falling-out) | b comes to the Seventh's council and asks to fight with the squad. A story `mend` (`return_to_squad`, `reconciled`); if you stand with b at 51a.4 instead, it mends there | bond | Take b back now / at the war |
| 49.3 | The Fourth | `hokage_4` (if crippled or taken) | Crippled: "I felt this at the stadium, when he tore at me. It was practice for this." Taken: "I've felt this before. In their hold. It was practice for this" | plot | — |

**The second's thread.** From Ch 49 Thread Sight shows her one-sided thread toward you. If your
bond with her stays low, it frays a little each day toward Ch 51: the game's way of saying she will
not survive the night unless something holds her (Ch 53.6).

---

## Ch 50: Eighty-One Doors (30 min authored, then the hunt)

The authored core: the plan at the Seventh's table (squad3_a, squad3_c, sensei_5; `teammate_a`'s painted genjutsu will hide the anchor-breakers' work from watching hearths), the first
anchor broken together at your old door, and a squad dinner at the barbecue house the night
before the hunt (a departed teammate's seat holds their Squad 2 stand-in; teammate_b and `squad4_b` argue over whose dog will find more anchors; the bowl is
set at its place if the Fourth fell). Then the hunt is systemic (~1.5 h): a village-wide search for
the anchors before Yūgure lights them. **This is where the systems pay off**: many anchors sit
inside clan quarters and homes, and residents let you in only if they trust you.

| Source of anchors found | Needs |
|---|---|
| The porter's ledger (half of them) | Nothing |
| Each clan quarter | `standing ["clan:<id>", "helping_hand"]` or the clan line's Legacy step (`clan.<id>.5`, where it exists) |
| Each district | `standing ["district:<id>", "good_neighbor"]` |
| The turned traitor (if turned) | One district already broken |
| The Undercroft (if sworn under the Hokage, N7) | Twelve anchors no one else could find |
| `sensei_5`'s seal lessons | Each district lesson attended counts double if `ans.sensei_5.teach_one = everyone` |
| Your Genin team and your house | Each member helps clear one |

Every anchor left unbroken (`story.array.unbroken`, 0 to 81) makes the finale harder: more hollow
fighters on the Rock, and a longer pull on the village in Ch 52. A thin web still wins.

---

## Ch 51a: Dusk (45 min)

The assault on the Leaf, first half: the village holds. **The player's route:** the wall (51a.1) →
the market street (51a.4) → the second line (51a.5) → the gate (51b.1). The Academy (51a.2) and the
hospital (51a.3) are cutaways.

**Who is where** (canonical for every file):

| Place | Who |
|---|---|
| The main gate | `sensei_2` with a handful of Chunin (he dies there, 51b.1); `squad3_a` builds the second line behind it when it breaks (51a.5), with `teammate_a`'s painted genjutsu hiding it; `squad5_b` smothers the lanes beside it; the Seventh, until 51b.1, then the Rock's foot |
| The wall | The former Fifth, `squad5_a`, the Tobari, the Hagane; later `squad5_c` (if he left the ANBU or stood down) and the Undercroft's head (if disbanded) |
| The Academy | The `instructor`, `sensei_3`, `squad3_b`, the Sixth, `genin_1` (leads the children out), the Fourth (if alive: falls, crippled or taken and home; with the children, sending word to the Seventh), the children |
| The hospital | `sensei_4`, `squad4_c` (until she climbs to the Rock's slope after 51b, for 53.5), the medic (or the medic's replacement, if arrested), the lost child (if home) |
| The market street | `teammate_b`, `squad4_b` and the dogs |
| The Residence steps | `classmate_d` and `classmate_c` (sent by `sensei_2`, who sent Squad 2 to the Residence and the Rock's stair) |
| The Rock's stair | The `rival` (this is where `ans.rival.ordinary` is read) |
| The Rock's shoulder (eyes) | `squad4_a`, with `squad3_c` beside her as the sensor |
| The Residence steps | (as above; `ans.classmate_d.reckless` is read here) |
| The Rock's top (from 51b.6) | The player, `sensei_5`; the blade (ahead of the player); the second (she follows the player up from the gate, unseen until 52.4) |

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 51a.1 | The wall | the Seventh, the former Fifth, `squad5_a`, the Tobari, the Hagane | Yūgure comes at dusk from three sides. The former Fifth fights on the wall beside the Tobari she once locked down (she reads your Ch 31 testimony: `ans.player.testify`; unset: "You were right that day."). The council members who doubted the second watch her hold a stretch of the wall (`ans.player.vouch`: vouched → the Seventh: "You staked your name on her. Look."; let her speak → "She spoke for herself. Now she fights for herself."; silent or unset → "Nobody vouched for her. She came anyway.") | plot, bond | — |
| 51a.2 | The Academy | `instructor`, `sensei_3`, `squad3_b`, the Fourth (if alive), children | The instructor holds the Academy with the children inside, with `sensei_3`'s falling-leaves genjutsu hiding the evacuation route and `squad3_b`, expanded, as the Academy's door; cheerful in the worst hour ("Rows of two! Who wants to see a really big clone?") | plot, bond | — |
| 51a.3 | The hospital | `sensei_4`, `squad4_c`, the medic | The hospital is a fortress: `sensei_4` binds the doors, `squad4_c` and the medic work the wards | plot | — |
| 51a.4 | The parent | `teammate_b`, `squad4_b`, b's parent (`yugure_b_parent`) | In the market street, held by `squad4_b` and his dogs, b meets their parent in road clothes with an ash-violet scarf. b asks your question (`ans.teammate_b.ask`; unset: "Why?"). The parent's answer, and b's choice, read `ans.teammate_b.come_back` (unset: "only if sorry"): bring them in (yes), make them say sorry first (only if sorry; `bond_flag parent_sorry` if they do), or let them go (no). The parent lives in all three; only "yes", or "only if sorry" with an apology, brings them home | plot, bond | Stand with b / let b choose alone (`ans.player.b_parent`) |
| 51a.5 | The second line | `squad3_a`, `teammate_a`, `squad5_b` | The gate is breaking. `squad3_a`'s plan breaks with it, and for the first time she improvises: a second line of barricades and shadow-binding behind the gate, built in minutes; `teammate_a` paints a genjutsu over it so the hearths see an empty street, and `squad5_b` smothers the lanes so they cannot hear it either | plot, bond | — |

---

## Ch 51b: The Door (40 min)

The assault, second half: the player crosses the burning village to the Rock, in this order.

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 51b.1 | The gate | `sensei_2`, the Seventh, Player | Your route reaches the main gate from the second line. `sensei_2` has held it with a handful of Chunin until the evacuation was through. You and the Seventh reach him together; he is dying. "Did I win?" "You won," the Seventh says: the only contest they ever conceded. (`ans.sensei_2.serious` may add a second line, never replace these). Then the Seventh argues once more against you going up, and you go (their last line reads `ans.player.go_up`; unset: "Then go. I'll be at the foot.") | plot, bond | — |
| 51b.2 | The crossing | Player, `squad4_a` | `squad4_a`'s Byakugan is the Seventh's eyes from the Rock's shoulder; she calls your route. A beat of play: you cross by Ember Mark from friend to friend where you have Blaze bonds (each jump is a friend's face in a fight); where you have none, it is a rooftop run she guides. The crossing is shorter the more Blaze friends you have | plot, teach | — |
| 51b.3 | The blade | `yugure_blade` | The last duel, on the rooftops at dusk. He fights at his best. Beaten, he asks why you never killed him | plot | "Because you let me pick up the kunai" / "Because she wouldn't want it" / "Because I want you to see what he's doing" (`ans.yugure_blade.why`; unset: he answers it himself, "So I'd see"). On your answer he **turns**: he goes to the Rock ahead of you to stop the leader |
| 51b.4 | The door | `elder_keeper` | The archive door. The keeper is holding it alone against a hearth, overwhelmed; you fight beside him, and as he falls the hearth carries the Hearthstone out. He presses the archive keys into your hand: "Someone has to keep it open now. Not closed. Open." (`ans.elder_keeper.forgive` adds one sentence; there is no other version) | plot, bond | — |
| 51b.5 | The stair | `rival`, the trio | The strongest hearth holds the Rock's stair. The rival is already there; you fight up it together. Near the top the trio (`squad3_a`, `squad3_b` or `squad3_c`, whoever is nearest) is pinned on the landing below; the rival turns back for them: "Go. You owe me a match." (the finals bout that was never fought) | plot, bond | — |
| 51b.6 | The climb | `yugure_leader` (through the array) | As you climb, every unbroken anchor hums, and the leader's voice comes through them, gentle: "You came. Good. Bring them all with you, little flame." | plot | — |

---

## Ch 52: The Last Bonfire (45 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 52.1 | The array lights | `yugure_leader`, Player, `sensei_5` | The leader sets the Hearthstone in the old stone channels on the Rock's top. Every unbroken anchor in the village flares ash-violet. You feel the village's chakra being dragged toward you, into you. You are the wick. `sensei_5` reaches the top behind you, kneels at the nearest channel and holds part of the array shut with seal-work, both hands on its seals, for as long as the fight lasts | plot | — |
| 52.2 | The leader | `yugure_leader`, `yugure_blade` | The blade reached the top first and strikes first, so the leader turns from you to him; then the two of you fight the leader together. The leader is ageless, gentle, tired; in Thread Sight he has no threads at all. Between blows he tells you about the shrine, the ash pit, being a boy, the sound of the chiselling. "They took our names. I'll take everything. Then nothing can ever be taken from anyone again, because I'll be holding it." He asks his first questions (`name`, `forgive`; his file) | plot | His questions |
| 52.3 | The offer | `yugure_leader` | "Or you hold it. Take it from me instead. You could heal every hollow child. You could make them kneel and say our names forever." The dark mirror, offered | plot | **Refuse** / **Reach for it** (`story.finale.reached`). Reaching plays a vision: the village hollow, you alone on the Rock, the red cord on your wrist gone grey. In every save the cord pulls first (her voice: "{given:player}." Her voice says your name, the first time anyone has said it to you on the Rock), then the people you love by bond, and you let go. Either way you refuse. Reaching leaves a trace: in 53.2 the cord's flame arrives grey-edged, and the sensei's line takes its reach variant (the Ch 53 line table in [sensei.md](../CHARACTERS/sensei.md)) |
| 52.4 | The shield | `yugure_second` | The leader turns the mirror on you. The second, who followed you up unseen from the gate, steps in front of it and is torn hollow | plot, bond | — |
| 52.5 | The blade | `yugure_blade` | The blade sees her fall. "Dusk was supposed to be for them, not for her." He fights on, badly wounded, and **lives**: after the war he is taken into custody (`story.blade.custody`). In Thread Sight, for this scene only, his one thread to the second burns bright (`thread_floor`) | plot | — |

---

## Ch 53: Every Fire (40 min)

| # | Scene | What happens |
|---|---|---|
| 53.1 | The pull | The array keeps dragging the village's fire into you, by force. It hurts everyone |
| 53.2 | Given | Then the flames start to come on their own, freely given. **The speaking rule:** six fixed speakers, in this order, each with one line from **the Ch 53 line table in their character file**: (1) **the red cord**, in every save, at any level: the lost child, home by now in every save ("So someone remembers. Take it. It's mine to give."; grey-edged if you reached in 52.3); (2) **the sensei**, in every save (`saved_by_them` from Ch 0; overrides a falling-out; base "Hold on. We're nearly out.", variants by `ans.sensei.orders`; changed if you reached); (3) **your spouse**, if married; (4) **the friend who fell for you in Ch 24** (if the sensei was the one who fell, slot 4 is skipped and slot 5 is the higher teammate); (5) **the other teammate** (skipped while a falling-out lasts or if they left and never came back; their Squad 2 stand-in appears only among the faces, at level 9+); (6) **the rival**, from the stair below (unset: "Take it. Don't say anything."). Slots (3) to (6) speak only at friendship 6 or more. **Then faces without spoken lines**: everyone else at 6 or more by level (the instructor, your Genin, your house, the ensemble), rituals shown as a remembered moment (the squad's ramen, the rival's race), and whole clans and districts that freely offer their flame (`offered_flame`, by standing) as one fire each. Anyone among the faces at level 9 or more may say one short line, in no fixed order. No other flame lines exist. The leader's answers only colour his own lines |
| 53.3 | The size | The watch-fire's size is the bond web's tier ([BONDS.md](../../../BONDS.md) §11; thresholds are data): **a small fire** (score under 20: the cord, the sensei, a few friends; a quiet Rock, only the people you know by name, lit faces in the dark), **strong** (from 20: the squad and friends, a ring of fire round the Rock's top), **the whole village** (from 41: every street lit on the Rock's face). Every size wins |
| 53.4 | It won't burn for him | The leader reaches into the wick to take the gathered fire. A fire given freely cannot be taken. His mirror turns on him; eighty years of taken chakra goes back to the array, back to the village, out of him. If the Fourth was crippled or taken, the chakra torn from him at the stadium or in the hold comes home too: in the Academy, he stands up |
| 53.5 | The second | Her thread is frayed almost through. You hold it and pour your flame into it (`thread_floor`). She lives if any holds: the web at **strong** (score 20 or more); `friendship [yugure_second, 4]`; or `friendship [squad4_c, 6]` with `ans.squad4_c.second` not "someone else first" (`squad4_c`, on the Rock's slope, has her healing kindled into a revival). **If none holds**, the thread does not break yet: you hold her in your arms through 53.6, and she dies at morning, as the first scene of Ch 54 (`story.second.lives`) |
| 53.6 | The last Kagari | He is old now, as old as he is. He asks his last questions (`cells`, `remember`; his file). You can kindle toward him: offer him a bond (`story.finale.offered_leader`). He can't take it; there is no bond to take. He hums two lines of the watch-fire song and stops. The last line is your choice: sing it (from the Ch 25.3 song book) / stay silent (`ans.player.last_line`). If you stay silent and the lost child is home, she sings it. He dies listening, on the Rock, as the sky goes grey |
| 53.7 | Morning comes | Finishing the chapter applies a **level-50 floor** and the deed `saved_the_village`, lived by every resident: the village's standing rises to Hero and every district and clan quarter to at least Good Neighbor |

---

## Ch 54: Morning (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 54.0 | Morning (if the second dies) | `yugure_second`, Player | Her own beat, first thing in the chapter. She dies at morning in your arms on the Rock. **A:** holding both halves of the charm; buried under the persimmon tree. **B:** with her son's name on her lips; buried at the shrine beside the basket, her son's name carved on the stone | bond | — |
| 54.1 | After | the village | Smoke, rubble dressing, people finding each other in the streets. Your order at Ichiraku, from a stand set up in the street | life, bond | — |
| 54.2 | Funerals | the village, `sensei` | The keeper; `sensei_2` (the Seventh finds his notebook of their contests: the last entry, in a shaky hand, written at the gate, "Held the gate longer than you would have. 52 to 290. Mine."); the blade, in custody, asks to watch from the wall and is allowed; the second (if she died: A under the persimmon tree, B at the shrine); the fallen of the war | bond | — |
| 54.3 | The leader's name | the Seventh, Player | What to do with his name: carve it among the Kagari / leave him off / carve it apart, with the year he was nine (`ans.player.leader_name`; unset: carved apart) | plot, bond | — |
| 54.4 | Successor | the Seventh | On the Rock: "When you're ready. I'll still be around to complain." The Seventh names you their successor | plot | — |

---

## Ch 55: The Eighth (40 min)

Plays directly after Ch 54: the requirements are met by Ch 53.7.

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 55.1 | Ready | the Seventh | ROADMAP's Hokage requirement (level 50, Hero standing with the village, Good Neighbor in every district and clan quarter) is met by Ch 53.7's level floor and `saved_the_village` (worth 90, lived by every resident, forgiving earlier bad deeds). The calendar goes to New Year: the succession | plot (`set_hokage 8`) | — |
| 55.2 | The speech | the Seventh, then Player | The Seventh's speech reads lineage B (their teammate's name) or A (the second, alive or remembered). Then yours: pick the three things you say from what the story gave you (`ans.player.speech`: the cord, the cord tag, the bowl, the names, the fire) | plot | — |
| 55.3 | First acts | Player | As Hokage: **extend the orphan's stipend** in the Fourth's name (in every fate; he is there to see it if he lives) to every child brought home from the nurseries and the war (the Valley children, the hollowed, the orphans of Ch 51), and make it law so no Hokage can end it; rule on the voice (pardon / exile / service to your house's archive) (`story.traitor.ruling`); `classmate_d` takes the post of your guard (quoting `ans.classmate_d.stand`; unset: "Beside you, then."); `squad5_a` becomes your Jonin Commander in `sensei_2`'s place (quoting `ans.squad5_a.will`; unset: "I'll say it out loud for you."); `squad3_b` stands beside you when the stipend becomes law | plot, bond | The ruling |
| 55.4 | The face | the Rock, `instructor` | Your face is carved as the Eighth. The instructor asks the Ch 5 question one last time ("Whose face would you put up there?") and this time you answer it: your Ch 5 answer becomes the answer you give now (`ans.instructor.face`: someone who saved me → "The ones who carried me"; someone nobody remembers → "The ones on the stone"; mine → "Mine, I suppose. Somebody has to."; yours → "Yours, if you'd let me."; unset: "Everyone who got me here") | plot (`carve_face 8`), bond | — |
| 55.5 | Epilogue | everyone | A montage read from flags: the squad, the lost child, the second (or her grave: A under the persimmon tree, B at the shrine), the blade asking to guard the shrine (or her grave), b and their parent, the rival, your house, your Genin, the porter sweeping the shrine, the child who repeats what the Leaf is. **Its size follows the web**: a wide web fills the montage with names; a lonely one shows the empty places honestly (a table set for few, a festival you watch from the Rock), and the Seventh says, without scolding: "You carried this with very few hands. Let more in now." The last image is chosen by `ans.lost_child.cord`: the red cord tied on the stone watch-fire basket at the shrine, on her wrist, or on yours (unset: the basket) | bond | — |

The post-game opens: the Hokage's duties (assigning teams, festivals, clan estates), children
(if married), and side content that waited for peace.
