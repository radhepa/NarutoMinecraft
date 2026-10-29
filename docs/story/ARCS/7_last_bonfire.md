# Arc 7: The Last Bonfire (Road to Hokage, Ch 46 to 55, later)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**~15 h** (about 8 h authored over 10 chapters, 7 h systemic: raising your clan, standing in every
district and clan quarter, the clan lines' Legacy steps, the last A- and S-ranks, level 42 to 50).

**What the arc is for.** Everything the player has built is tested at once. The truth of the
player's own blood, the enemy's real goal, and the answer to the story's first image (a child in a
cell, a girl pushing a red cord through bars so someone remembers). The finale is won by the
village the player befriended: the fire's size is the bond web, and every flame has a face the
player knows.

---

## Ch 46: Old Ground (45 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 46.1 | The registry | the Seventh, the registry clerk | The registry offers a founding path no one has offered in eighty years: **restore the Kagari** under their old name and crest, on their old ground (the vacant estate nearest the south gate, and the shrine in the hills as the clan shrine), with the gift as the clan art. Or found a clan of your own | plot (`found_clan`) | Restore the Kagari / found your own clan (`story.clan.choice`). Both are honoured; the story calls your clan "your house" either way. The registry also lets you take your house's name as your family name, or keep the one you remembered |
| 46.2 | The shrine | Player, `classmate_c` | Clear the burned shrine; the stone watch-fire basket from Ch 0 stands. classmate_c's family builds the hall's door and carves into it what they would make for someone they never met (`ans.classmate_c.make`) | plot, bond | — |
| 46.3 | The first members | descendants | Descendants who chose to be named (by `ans.hokage_6.names`) come to the shrine. Some want to join; some only want to see. Recruitment (systemic, BONDS §10) | systems | Who you invite |

---

## Ch 47: The Lost Child / Home Fires (45 min)

| If | What happens |
|---|---|
| **Night Watch not finished** | **The Lost Child.** She comes to the shrine at night, half hollow, hunted by Yūgure for deserting. Cells follow her. You fight them off at the stone basket, then give her your flame through the cord as in N6 (shorter: the shrine's old fire helps). `story.lost_child.home = shrine`. Needs `bond_flag red_cord` kept from Ch 0 (the cord cannot be lost); if the player never saw her in Ch 44 the scene still plays |
| **`squad5_c`** | If the Night Watch was not played, `squad5_c` comes to the shrine with Undercroft orders to take her. Talk him down (`ans.squad5_c.offer`) or fight him: a betrayal, or not. Either way the orders reach the Seventh, and the Undercroft is disbanded quietly |
| **Night Watch finished** | **Home Fires.** Her recovery, with `squad4_c` tending her and the medic watching. She stays at your clan hall. She asks the questions she never got to ask in the cells (see her character file); a walk through the village she never grew up in; the first bowl of ramen. Her answers to your questions become who she is |

---

## Ch 48: Persimmons (50 min)

The lineage reveal (`twist.lineage`, [ROTATIONS.md](../ROTATIONS.md) §2).

| | **A: the second** | **B: the fallen Leaf shinobi** |
|---|---|---|
| How it starts | A letter on ember-burned paper: a far village name and a day | The Seventh: "Walk with me. It's a long walk" |
| The place | The ruins of the persimmon house in a border village; the tree is alive, heavy with fruit | The same |
| Who is there | `yugure_second`, alone, unarmed. She has left Yūgure: in the leader's records she found "Nine: her child. Keep from her." | The Seventh, with a box: `fallen_parent`'s forehead protector and half a watch-fire charm |
| The proof | Her half of the charm; the halves fit | The box's half; the halves fit |
| The heart of it | "I sang you that song. I didn't know you'd keep it. He told me you burned with the house." Then, about the stadium: "I nearly took you to him. I would have." | "I signed the report that called it bandits. I believed it because it was easier. I should have looked for you. I carried you over a ravine and I didn't know." |
| The player's answer | What you say to her: "You're my mother" / "You left me" / "You saved me twice" (the map in Ch 0, the forest) (`ans.player.parent_meet`) | What you say to them: "You found me anyway" / "You should have looked" / say their teammate's name (`ans.player.parent_meet`) |
| After | She asks for nothing. She will tell you what she knows (Ch 49) | The second's letter arrives that night (her defection, Ch 49) |

---

## Ch 49: The Hollow Crown (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 49.1 | The truth | `yugure_second`, the Seventh, Player | She tells the Seventh's council the leader's true plan: the array, the Hearthstone, the wick, the taking ([WORLD.md](../WORLD.md)). "The Bonfire was never for all of us. It was for him." She learned it from his own notes. The blade does not know | plot (`story.hollow_crown.known`), bond (a `shared_moment bond.second.truth` if you vouch or let her speak: her first real moment with you) | Whether the council trusts her: you vouch / you let her speak for herself / you say nothing (`ans.player.vouch`). Vouching ties your standing to her (a deed) |
| 49.2 | The map | Player, the porter's ledger | The porter's ledger (Ch 28) is the array: eighty-one doorsteps, sills and crates. One of them is your old door (Ch 4). `squad3_c` can feel the anchors once he knows what to listen for; `squad3_a` turns the ledger into a plan; `sensei_5` teaches the village to break a cinder seal | plot, seed paid (`story.seed.door_mark`, `story.seed.porter_ledger`) | — |
| 49.3 | The Fourth | `hokage_4` (if crippled or taken) | "I've felt this before. In their hold. It was practice for this" | plot | — |

---

## Ch 50: Eighty-One Doors (60 min)

A village-wide hunt for the array's anchors before Yūgure lights them. **This is where the
systems pay off**: many anchors sit inside clan quarters and homes, and residents let you in only
if they trust you.

| Source of anchors found | Needs |
|---|---|
| The porter's ledger (half of them) | Nothing |
| Each clan quarter | `standing ["clan:<id>", "helping_hand"]` or the clan line's Legacy step (`clan.<id>.5`, where it exists) |
| Each district | `standing ["district:<id>", "good_neighbor"]` |
| The turned traitor (if turned) | One district already broken |
| The Undercroft (if brought under the Hokage, N7) | Twelve anchors no one else could find |
| Your Genin team and your restored house | Each member helps clear one |

Every anchor left unbroken (`story.array.unbroken`, 0 to 81) makes the finale harder: more hollow
fighters on the Rock, and a longer pull on the village in Ch 52. A thin web still wins.

---

## Ch 51: Dusk (60 min)

The assault on the Leaf. A sequence of set-pieces, each led by a character the player knows.

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 51.1 | The wall | the Seventh, the Fifth, `sensei_2`, `squad5_b`, `squad3_a`, the Tobari, the Hagane | Yūgure comes at dusk from three sides. The former Fifth fights on the wall beside the Tobari she once locked down. `sensei_2` holds the main gate with a handful of Chunin against the leader's strongest cells until the evacuation is through; when your sensei reaches him he is dying, and asks if he won. "You won," your sensei says: the only contest they ever conceded. `squad3_a`'s plan breaks with the gate, and she improvises the second line herself | plot, bond | — |
| 51.2 | The Academy | `instructor`, `sensei_3`, `squad3_b`, the Fourth (if alive), children | The instructor holds the Academy with the children inside, with `sensei_3`'s genjutsu hiding the evacuation route and `squad3_b`, expanded, as the Academy's door; cheerful in the worst hour ("Rows of two! Who wants to see a really big clone?") | plot, bond | — |
| 51.3 | The parent | `teammate_b`, `squad4_b`, b's parent (`yugure_b_parent`) | In the market street, held by `squad4_b` and his dogs, b meets their parent in an ash-violet cloak. b asks your question (`ans.teammate_b.ask`). The parent's answer, and b's choice, read `ans.teammate_b.come_back`: bring them in (yes), make them say sorry first (only if sorry), or let them go (no). The parent lives in all three; only "yes" brings them home | plot, bond | Stand with b / let b choose alone (`ans.player.b_parent`) |
| 51.4 | The blade | `yugure_blade` | The last duel, on the rooftops at dusk. He fights at his best. Beaten, he asks why you never killed him | plot | "Because you let me pick up the kunai" / "Because she wouldn't want it" / "Because I want you to see what he's doing" (`ans.yugure_blade.why`). All three send him to the Rock |
| 51.5 | The door | `elder_keeper` | The archive door. The keeper holds it alone against a cell. When you get there he is dying, and the Hearthstone is gone. He presses the archive keys into your hand: "I kept it quiet forty years. You say it now. All of it." | plot, bond | — |
| 51.6 | The Rock | Player | The leader has the Hearthstone on top of the Rock. With `squad4_a`'s Byakugan as the Seventh's eyes, you cross the burning village by Ember Mark, from friend to friend, and go up | plot | — |

---

## Ch 52: The Last Bonfire (45 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 52.1 | The array lights | `yugure_leader`, Player | The leader sets the Hearthstone in the old stone channels on the Rock's top. Every unbroken anchor in the village flares ash-violet. You feel the village's chakra being dragged toward you, into you. You are the wick. `sensei_5` reaches the top behind you and throws himself on the nearest anchor channel to hold part of the array shut | plot | — |
| 52.2 | The leader | `yugure_leader` | Ageless, gentle, tired. He tells you about the shrine, the ash pit, nine years old, the sound of the chiselling. "They took our names. I'll take everything. Then nothing can ever be taken from anyone again, because I'll be holding it." He sings two lines of the watch-fire song | plot | — |
| 52.3 | The offer | `yugure_leader` | "Or you hold it. Take it from me instead. You could heal every hollow child. You could make them kneel and say our names forever." The dark mirror, offered | plot | **Refuse** / **Reach for it** (`story.finale.reached`). Reaching plays a vision: the village hollow, you alone on the Rock, the red cord gone grey; then the people you love pull at you (their voices, by bond) and you let go. Either way you refuse |
| 52.4 | The shield | `yugure_second` | The leader turns the mirror on you. The second steps in front of it and is torn hollow | plot, bond | — |
| 52.5 | The blade | `yugure_blade` | If the blade reached the Rock (always after 51.4), he sees the second fall and understands. He turns his sword on the leader: "Dusk was supposed to end in morning." He dies on the Rock | plot | — |

---

## Ch 53: Every Fire (40 min)

| # | Scene | What happens |
|---|---|---|
| 53.1 | The pull | The array keeps dragging the village's fire into you, by force. It hurts everyone |
| 53.2 | Given | Then the flames start to come on their own. Everyone at friendship 6 or more chooses to kindle toward you, and their flame leaves the array's pull and becomes yours to hold, freely given. Each comes with a face and a line, in this order: your spouse (if married); your teammates (reading their questions); the Seventh (`ans.sensei.orders`, `ans.sensei.know`); the rival (`ans.rival.theirs` and `ans.rival.why_came`: "You said I'd be what's left. Then take it"); the lost child (if home: "So someone remembers"); the instructor; your Genin; your clan; then whole clans and districts as one fire each |
| 53.3 | The size | The watch-fire's size is `BondWeb.score` ([BONDS.md](../../../BONDS.md) §11): small (15: the squad and a few friends) / strong (40) / the whole village (70). The thresholds are data. A thin web still wins; a wide one changes the scene (the whole village lit on the Rock's face) and the epilogue |
| 53.4 | It won't burn for him | The leader reaches into the wick to take the gathered fire. A fire given freely cannot be taken. His mirror turns on him; eighty years of taken chakra goes back to the array, back to the village, out of him |
| 53.5 | The last Kagari | He is old now, as old as he is. You can kindle toward him: offer him a bond (`story.finale.offered_leader`). He can't take it; there is no bond to take. He hears the song from you, sings the last line, and dies on the Rock at dawn |
| 53.6 | The second | If `bond_web 40`, or `friendship [yugure_second, 4]`, or `friendship [squad4_c, 6]` (you kindle `squad4_c`'s healing into a revival): the watch-fire rekindles her and she lives. Else she dies at dawn, holding your half of the charm with hers (`story.second.lives`) |

---

## Ch 54: Morning (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 54.1 | After | the village | Smoke, rubble dressing, people finding each other in the streets. Your order at Ichiraku, from a stand set up in the street | life, bond | — |
| 54.2 | Funerals | the village, `sensei` | The keeper; `sensei_2` (your sensei finds his notebook of their contests: the last entry, in a shaky hand, "Held the gate longer than you would have. Mine."); the blade (if you ask, buried outside the wall with his sword); the second (if she died); the fallen of the war | bond | — |
| 54.3 | The leader's name | the Seventh, Player | What to do with his name: carve it among the Kagari / leave him off / carve it apart, with the year he was nine (`ans.player.leader_name`) | plot, bond | — |
| 54.4 | Successor | the Seventh | On the Rock: "When you're ready. I'll still be around to complain." The Seventh names you their successor (the requirements are now systemic: level 50 and Hero standing everywhere) | plot | — |

---

## Ch 55: The Eighth (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 55.1 | Ready | the Seventh | When level 50 and Hero standing everywhere are reached, the New Year succession | plot (`set_hokage 8`) | — |
| 55.2 | The speech | the Seventh, then Player | The Seventh's speech reads lineage B (their teammate's name) or A (the second, alive or remembered). Then yours: pick the three things you say from what the story gave you (`ans.player.speech`: the cord, the bell, the bowl, the names, the fire) | plot | — |
| 55.3 | First acts | Player | As Hokage: restore the orphan's stipend in the Fourth's name; rule on the voice (pardon / exile / service to the restored clan's archive) (`story.traitor.ruling`); `classmate_d` takes the post of your guard (quoting `ans.classmate_d.stand`); `squad5_a` becomes your Jonin Commander in `sensei_2`'s place (quoting `ans.squad5_a.will`); `squad3_b` stands beside you when the stipend is restored | plot, bond | The ruling |
| 55.4 | The face | the Rock | Your face is carved as the Eighth; the instructor asks the Ch 5 question one more time | plot (`carve_face 8`) | — |
| 55.5 | Epilogue | everyone | A montage read from flags: the squad, the lost child, the second (or her grave under the persimmon tree), b and their parent, the rival, your house, your Genin, the porter sweeping the shrine, the child who repeats what the Leaf is. The last image: a red cord tied on the stone watch-fire basket at the shrine | bond | — |

The post-game opens: the Hokage's duties (assigning teams, festivals, clan estates), children
(if married), and side content that waited for peace.
