# Arc 7: The Last Bonfire (Road to Hokage, Ch 46 to 55, later)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**~15 h** main path: about 7.6 h authored over 11 chapters (455 min) and about 7.4 h systemic
main-path play. Story time Y+7 to Y+8. Levels 42 to 50.

**Where the systemic play sits.** All of it before the war, so nothing is a grind after it:

| When | Systemic main-path play | About |
|---|---|---|
| Between Ch 46 and Ch 48 | S-ranks clearing the last hearths (each one cleared removes a wave from Ch 51a; `story.cells_cleared`), raising your house (the registry's tasks, recruiting), leading your Genin, the fourth-nature trial | ~5 h |
| Ch 50 (after its authored core) | The anchor hunt across the village | ~1.5 h |
| Ch 49 gate | Level 47 | — |
| Ch 51a to Ch 53 | The war's XP carries the player to level 50 | — |

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
| **`squad5_c`**, Night Watch not finished | Before dawn, `squad5_c` comes to the shrine with Undercroft orders to take her. Talk him down (`ans.squad5_c.offer`) or fight him: a betrayal, or not (`story.squad5_c.stand`). Either way the orders reach the Seventh, and the Undercroft is disbanded quietly |
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
| The heart of it | She tells you first: "The map, the night they raided the hills. That was mine. I didn't know you were in there." Then: "I sang you that song. I didn't know you'd keep it. He told me you burned with the house." And, about the stadium: "I nearly took you to him. I would have." | "I carried you over a ravine and didn't know. Then I suspected, and the report said the persimmon house burned with everyone in it, and I was afraid to be wrong, so I never opened the box." |
| The player's answer | "You're my mother" / "You left me" / "You saved me twice" (the map, the forest) (`ans.player.parent_meet`) | "You found me anyway" / "You should have looked" / say their teammate's name (`ans.player.parent_meet`) |
| After | She asks for nothing. She will tell you what she knows (Ch 49) | The second's letter arrives that night (her defection, Ch 49) |

---

## Ch 49: The Hollow Crown (40 min)

*Needs level 47.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 49.1 | The truth | `yugure_second`, the Seventh, Player | She tells the Seventh's council the leader's true plan: the array, the Hearthstone, the wick, the taking ([WORLD.md](../WORLD.md)). "The Bonfire was never for all of us. It was for him." She learned it from his own notes. The blade does not know | plot (`story.hollow_crown.known`), bond (a `shared_moment bond.second.truth` if you vouch or let her speak: her first real moment with you) | Whether the council trusts her: you vouch / you let her speak for herself / you say nothing (`ans.player.vouch`). Vouching ties your standing to her (a deed) |
| 49.2 | The map | Player, the porter's ledger | The porter's ledger (Ch 28) is the array: eighty-one doorsteps, sills and crates. One of them is your old door (Ch 4). `squad3_c` can feel the anchors once he knows what to listen for; `squad3_a` turns the ledger into a plan; `sensei_5` teaches the village to break a cinder seal | plot, seed paid (`story.seed.door_mark`, `story.seed.porter_ledger`) | — |
| 49.3 | The Fourth | `hokage_4` (if crippled or taken) | Crippled: "I felt this at the stadium, when he tore at me. It was practice for this." Taken: "I've felt this before. In their hold. It was practice for this" | plot | — |

**The second's thread.** From Ch 49 Thread Sight shows her one-sided thread toward you. If your
bond with her stays low, it frays a little each day toward Ch 51: the game's way of saying she will
not survive the night unless something holds her (Ch 53.6).

---

## Ch 50: Eighty-One Doors (30 min authored, then the hunt)

The authored core: the plan at the Seventh's table (squad3_a, squad3_c, sensei_5), the first
anchor broken together at your old door, and a squad dinner at the barbecue house the night
before the hunt (teammate_b and `squad4_b` argue over whose dog will find more anchors; the bowl is
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

The assault on the Leaf, first half: the village holds.

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 51a.1 | The wall | the Seventh, the Fifth, `squad5_b`, `squad5_c`, the Tobari, the Hagane, the Undercroft's head (if disbanded) | Yūgure comes at dusk from three sides. The former Fifth fights on the wall beside the Tobari she once locked down (she reads your Ch 31 testimony: `ans.player.testify`; unset: "You were right that day."). `squad5_b`'s smothering hides the wall's gaps. `squad5_c` returns to the wall whatever happened in the branch | plot, bond | — |
| 51a.2 | The Academy | `instructor`, `sensei_3`, `squad3_b`, the Fourth (if alive), children | The instructor holds the Academy with the children inside, with `sensei_3`'s genjutsu hiding the evacuation route and `squad3_b`, expanded, as the Academy's door; cheerful in the worst hour ("Rows of two! Who wants to see a really big clone?") | plot, bond | — |
| 51a.3 | The hospital | `sensei_4`, `squad4_c`, the medic | The hospital is a fortress: `sensei_4` binds the doors, `squad4_c` and the medic (or the medic's replacement, if arrested) work the wards | plot | — |
| 51a.4 | The parent | `teammate_b`, `squad4_b`, b's parent (`yugure_b_parent`) | In the market street, held by `squad4_b` and his dogs, b meets their parent in road clothes with an ash-violet scarf. b asks your question (`ans.teammate_b.ask`; unset: "Why?"). The parent's answer, and b's choice, read `ans.teammate_b.come_back` (unset: "only if sorry"): bring them in (yes), make them say sorry first (only if sorry; `bond_flag parent_sorry` if they do), or let them go (no). The parent lives in all three; only "yes", or "only if sorry" with an apology, brings them home | plot, bond | Stand with b / let b choose alone (`ans.player.b_parent`) |

---

## Ch 51b: The Door (40 min)

The assault, second half: the player crosses the burning village to the Rock.

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 51b.1 | The crossing | Player, `squad4_a` | `squad4_a`'s Byakugan is the Seventh's eyes from the Rock's shoulder; she calls your route. You cross by Ember Mark from friend to friend where you have Blaze bonds (each jump is a friend's face in a fight); where you have none, it is a rooftop run she guides. The crossing is shorter the more Blaze friends you have | plot, teach | — |
| 51b.2 | The blade | `yugure_blade` | The last duel, on the rooftops at dusk. He fights at his best. Beaten, he asks why you never killed him | plot | "Because you let me pick up the kunai" / "Because she wouldn't want it" / "Because I want you to see what he's doing" (`ans.yugure_blade.why`; unset: he answers it himself, "So I'd see"). All three send him to the Rock |
| 51b.3 | The gate | `sensei_2`, the Seventh, Player | The route passes the main gate. `sensei_2` has held it with a handful of Chunin until the evacuation was through. You and the Seventh reach him together; he is dying. "Did I win?" "You won," the Seventh says: the only contest they ever conceded. (`ans.sensei_2.serious` may add a second line, never replace these) | plot, bond | — |
| 51b.4 | The door | `elder_keeper` | The archive door. The keeper is alive, holding it against a hearth. You fight beside him; in the fight he takes the blow meant for the basket, and as he falls the hearth carries the Hearthstone out. He presses the archive keys into your hand: "I kept it quiet forty years. You say it now. All of it." | plot, bond | — |
| 51b.5 | The voice | `yugure_leader` (through the array) | As you climb, every unbroken anchor hums, and the leader's voice comes through them, gentle: "You came. Good. Bring them all with you, little flame." He asks you one question through the array (his file, `ans.yugure_leader.*` for 51b) | plot | His question |
| 51b.6 | The stair | `rival` | The strongest hearth holds the Rock's stair. The rival is already there: "Go. You owe me a match." They hold it alone while you climb | plot, bond | — |

---

## Ch 52: The Last Bonfire (45 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 52.1 | The array lights | `yugure_leader`, Player, `sensei_5` | The leader sets the Hearthstone in the old stone channels on the Rock's top. Every unbroken anchor in the village flares ash-violet. You feel the village's chakra being dragged toward you, into you. You are the wick. `sensei_5` reaches the top behind you and throws himself on the nearest anchor channel to hold part of the array shut | plot | — |
| 52.2 | The leader | `yugure_leader` | Ageless, gentle, tired. In Thread Sight he has no threads at all. He tells you about the shrine, the ash pit, nine years old, the sound of the chiselling. "They took our names. I'll take everything. Then nothing can ever be taken from anyone again, because I'll be holding it." He sings two lines of the watch-fire song | plot | His questions (his file) |
| 52.3 | The offer | `yugure_leader` | "Or you hold it. Take it from me instead. You could heal every hollow child. You could make them kneel and say our names forever." The dark mirror, offered | plot | **Refuse** / **Reach for it** (`story.finale.reached`). Reaching plays a vision: the village hollow, you alone on the Rock, the red cord on your wrist gone grey. In every save the cord pulls first (her voice: "So someone remembers"), then the people you love by bond, and you let go. Either way you refuse |
| 52.4 | The shield | `yugure_second` | The leader turns the mirror on you. The second steps in front of it and is torn hollow | plot, bond | — |
| 52.5 | The blade | `yugure_blade` | The blade reached the Rock after 51b.2. He sees the second fall and understands. He turns his sword on the leader: "Dusk was supposed to be for them, not for her." He dies on the Rock | plot | — |

---

## Ch 53: Every Fire (40 min)

| # | Scene | What happens |
|---|---|---|
| 53.1 | The pull | The array keeps dragging the village's fire into you, by force. It hurts everyone |
| 53.2 | Given | Then the flames start to come on their own, freely given, each with a face and a line, in this fixed order. **First, in every save**, the red cord: the lost child (home by now in every save) kindles at any level: "So someone remembers. It's mine to give." **Second, in every save**, the sensei (`saved_by_them` from Ch 0): their line reads `ans.sensei.orders` and `ans.sensei.know` (unset: "I carried you once. Let me again."). Then everyone at friendship 6 or more who chooses to: your spouse (if married); your teammates (reading their questions; unset defaults in their files); the rival, from the stair below (one line per `ans.rival.theirs` answer, then `ans.rival.why_came`; unset: "Take it. Don't say anything."); the instructor; your Genin; your house. Rituals add their line (the squad's ramen, the rival's race: "Our race isn't finished."). Then whole clans and districts that freely offer their flame (`offered_flame`, by standing) as one fire each. The leader's answers only colour his own lines, never this order |
| 53.3 | The size | The watch-fire's size is `BondWeb.score` ([BONDS.md](../../../BONDS.md) §11): **a small fire** (under 15: the cord, the sensei, a few friends; a quiet Rock, only the people you know by name, lit faces in the dark), **a strong fire** (15 to 39: the squad and friends), **a great fire** (40 to 69), **the whole village** (70: every street lit on the Rock's face). The thresholds are data. Every size wins |
| 53.4 | It won't burn for him | The leader reaches into the wick to take the gathered fire. A fire given freely cannot be taken. His mirror turns on him; eighty years of taken chakra goes back to the array, back to the village, out of him |
| 53.5 | The last Kagari | He is old now, as old as he is. You can kindle toward him: offer him a bond (`story.finale.offered_leader`). He can't take it; there is no bond to take. He hears the song from you (its last line is in the song book of Ch 25.3; the player knows it), sings it with you, and dies on the Rock at dawn |
| 53.6 | The second | She lives if any holds: `bond_web 40`; or `friendship [yugure_second, 4]`; or `friendship [squad4_c, 6]` and `ans.squad4_c.second` is not "someone else first" (`squad4_c`, on the Rock's slope, has her healing kindled into a revival). Else she dies at dawn, holding your half of the charm with hers (`story.second.lives`) |

---

## Ch 54: Morning (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 54.1 | After | the village | Smoke, rubble dressing, people finding each other in the streets. Your order at Ichiraku, from a stand set up in the street | life, bond | — |
| 54.2 | Funerals | the village, `sensei` | The keeper; `sensei_2` (the Seventh finds his notebook of their contests: the last entry, in a shaky hand, written before the gate, "Held the gate longer than you would have. 39 to 211. Mine."); the blade (if you ask, buried outside the wall with his sword); the second (if she died, under the persimmon tree); the fallen of the war | bond | — |
| 54.3 | The leader's name | the Seventh, Player | What to do with his name: carve it among the Kagari / leave him off / carve it apart, with the year he was nine (`ans.player.leader_name`; unset: carved apart) | plot, bond | — |
| 54.4 | Successor | the Seventh | On the Rock: "When you're ready. I'll still be around to complain." The Seventh names you their successor | plot | — |

---

## Ch 55: The Eighth (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 55.1 | Ready | the Seventh | The succession needs level 50 (the war's XP brings it) and **Hero standing with the village, Good Neighbor in every district and clan quarter**. The end of Ch 53 fires the deed `saved_the_village` (worth 40, village news) for every player who finishes it, so Hero with the village is always reached; defending the village in Ch 51 counts as a great deed everywhere, so a player who fought the war is there or nearly there. The New Year succession comes within about an in-game hour of play after Ch 54 (the calendar skips to New Year once the requirements are met) | plot (`set_hokage 8`) | — |
| 55.2 | The speech | the Seventh, then Player | The Seventh's speech reads lineage B (their teammate's name) or A (the second, alive or remembered). Then yours: pick the three things you say from what the story gave you (`ans.player.speech`: the cord, the bell, the bowl, the names, the fire) | plot | — |
| 55.3 | First acts | Player | As Hokage: **extend the orphan's stipend** in the Fourth's name (in every fate; he is there to see it if he lives) to every child brought home from the nurseries and the war (the Valley children, the hollowed, the orphans of Ch 51), and make it law so no Hokage can end it; rule on the voice (pardon / exile / service to your house's archive) (`story.traitor.ruling`); `classmate_d` takes the post of your guard (quoting `ans.classmate_d.stand`; unset: "Beside you, then."); `squad5_a` becomes your Jonin Commander in `sensei_2`'s place (quoting `ans.squad5_a.will`; unset: "I'll say it out loud for you."); `squad3_b` stands beside you when the stipend becomes law | plot, bond | The ruling |
| 55.4 | The face | the Rock | Your face is carved as the Eighth; the instructor asks the Ch 5 question one more time | plot (`carve_face 8`) | — |
| 55.5 | Epilogue | everyone | A montage read from flags: the squad, the lost child, the second (or her grave under the persimmon tree), b and their parent, the rival, your house, your Genin, the porter sweeping the shrine, the child who repeats what the Leaf is. **Its size follows the web**: a wide web fills the montage with names; a lonely one shows the empty places honestly (a table set for few, a festival you watch from the Rock), and the Seventh says, without scolding: "You carried this with very few hands. Next time, let more in." The last image is chosen by `ans.lost_child.cord`: the red cord tied on the stone watch-fire basket at the shrine, on her wrist, or on yours (unset: the basket) | bond | — |

The post-game opens: the Hokage's duties (assigning teams, festivals, clan estates), children
(if married), and side content that waited for peace.
