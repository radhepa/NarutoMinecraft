# Rotations: the twist slots in full

> **SPOILERS: for developers only.** Part of the [story bible](STORY_BIBLE.md).

Three slots are bound at world creation by the `twists` stream, in Classic and Varied alike:
`twist.traitor` (4 candidates), `twist.lineage` (2), `twist.fourth_fate` (3). This file is the
contract for each: every candidate's clue trail, its innocent explanation when not bound, the
decisive evidence, the reveal, and the fairness checks. `quests.py --check` verifies that every
candidate has a complete trail and an innocent explanation (ROADMAP §5).

**The fair-play rule.** Through the whole beta, all candidates' clues play identically in every
save: a player cannot tell the bound candidate from beta content alone, and a player who knows the
answer from another save learns nothing. From the Chunin arc on, the bound candidate's trail and
the innocents' trails diverge, a little at a time, so an attentive player can solve it before the
Jonin arc's reveal, and every player can solve it at the case board (Ch 38) from evidence they have
been shown.

---

## 1. `twist.traitor`: the voice

### What is fixed in every save

- **The hand** is always the `porter` (fixed role, fixed look: a lanky young man with a carrying
  frame, polite, a burn scar on his palm). He was a nursery child, "rescued" by Yūgure at nine and
  sent into the Leaf at sixteen as a porter for the furniture shop and the post. He carries for
  everyone: furniture into the player's flat (Ch 1), the library's returns cart, the hospital's
  linen, the council's letter bags, crates loaded onto merchants' carts at the east gate. He lays
  the array's cinder seals under what he carries. He scratched the sinking sun on the player's door
  (Ch 4) and is the figure on the rooftops.
- **The voice** is the bound candidate. For six years the voice has fed Yūgure, through the porter:
  the names of gifted children with their chakra readings (the nurseries' recruiting list), the
  guard rotations for the finals (Ch 19), and the archive door's schedule.
- **Yūgure's list** is kept in the voice's own notation. A cell's copy, captured in the Valley of
  Ash (Ch 35), spans six years of entries in one notation: the voice's.
- **The four sources and their notations**, each shown to the player in the beta, in every save:

| Candidate | Source of names | Notation (shown in) | Private mark |
|---|---|---|---|
| `librarian` | The Academy aptitude scrolls, filed in the library | Shelf marks: `Leaf 7-iii` (Ch 5, shelving the scrolls) | A small brushed circle beside a gifted child |
| `medic` | The hospital intake ledger of rescued and orphaned children | Pulse counts in green ink: `p 88 / 112` (Ch 0, your own sample) | A tiny folded-crane stroke |
| `elder_councillor` | The orphan stipend registry | Stipend numbers: `S-114` (Ch 1, your own papers; you are S-114) | A pine-sprig seal mark |
| `merchant` | Their delivery book of orphanages and waystations | Road-stop shorthand: `E3 · two · bright` (Ch 11, the book in the cart) | A tick with a tail |

- **The red herring** in every save is the `elder_keeper`, who watches the player, guards a door and
  lies about knowing things. He is never the voice; his secret is the archive.
- **Thread Sight cannot solve it.** From Ch 24 the player sees bonds as threads, and a bonded
  person who hides something flickers. The limit ([WORLD.md](WORLD.md#thread-sight-and-the-mystery-a-principled-limit)):
  it reads only people bonded to the player at 6+, it shows *that* someone hides, never *what*, and
  all four candidates hide a true secret in every save (the librarian her Kagari family history;
  the medic their letters to the strangers who saved them; the councillor his signature on the Ash
  Road sealing; the merchant old debts and bandit smuggling). All four flicker the same. The hand
  (the porter) is never in the player's web, so the voice's tie to him never shows.

### The shared clue trail (identical in every save)

| Clue | Where | What the player sees | If bound | If innocent |
|---|---|---|---|---|
| `story.clue.medic.1` | Ch 0 | The medic takes a sample of your chakra "for the records" and writes it in green ink with a crane stroke | The reading went to Yūgure | They test every rescued child; it is hospital routine |
| `story.clue.councillor.1` | Ch 1 | Your stipend papers (S-114) were arranged by the councillor personally, pine seal on the corner | He kept the wick close and on file | The keeper asked him to; he did it as a favour and a kindness |
| `story.clue.medic.2` | Ch 3 | The medic drops by the evening of the flare "to check on you" | To report the flare | The instructor asked the medic to check, worried |
| `story.clue.librarian.1` | Ch 5 | The founding history's cut page; the edge is fresh | She cut it that morning and handed it to the porter | The porter cut it while collecting returns; she found it that morning |
| `story.clue.librarian.2` | Ch 5 | The librarian is nervous and lies that the page "has been gone for years" | She is afraid of being caught | She is afraid of what the page was: her own family's secret history. She lies to protect it |
| `story.clue.librarian.3` | Side: `district.b1.academy.overdue` | One overdue book holds a slip in an unknown cipher (Yūgure's) | A dead drop she used | The porter used the returns cart as a dead drop |
| `story.clue.merchant.1` | Ch 11 | The cart's false floor of chakra paper; the delivery book with its shorthand | They carry paper and names | They bought the cart second-hand from a carpenter in the east who built the floor; they did not know |
| `story.clue.merchant.2` | Ch 14 | The merchant slows the squad on the road, inventing reasons | To let the cell slip past | A cloaked pair threatened them at the waystation the night before |
| `story.clue.councillor.2` | Ch 14 | The captured smuggler's travel pass bears the councillor's pine seal | He sealed it | His seal was borrowed from the council letter bags the porter carries |
| `story.clue.councillor.3` | Side: `event.b2.council_day` | From the gallery you see the councillor hand a sealed letter to the porter | A report | Ordinary council post |
| `story.clue.merchant.3` | Side: `district.b2.contraband` | The gate log shows the merchant's cart passed with no inspection, twice | They bribed the guard | The bored Hagane guards waved every regular through (the betting ring's guards) |
| `story.clue.medic.3` | Side: `district.b2.night_shift` | Pages are missing from the hospital's intake ledger after your night shift | They tore them out | The night patient (the smuggler) tore them out (see the alibi below) |
| `story.clue.medic.4` | Side: `side.b3.hospital_supplies` | The diverted supplies' requisition is in green ink | They signed it | A forged requisition; the trail clears them (SIDE_QUESTS bible entry) |

Every candidate has at least three beta clues; none is decisive.

### Where the trails diverge (Chunin and Jonin arcs)

**1. The slip (Ch 25).** In the hospital after the border post, all four candidates come to the
player, each for a natural reason: the medic treats you, the librarian brings books, the councillor
visits for the council (you are a Chunin on stipend files), the merchant sends a basket of fruit
with a note. Each line is warm and parallel. **The bound candidate's line holds a detail only
Yūgure's reports contain: the player's nursery number.** Guards called the player "Nine" in Ch 0;
the player never says it to anyone (no dialogue option offers it before the reveal). The slip is
quiet and lands inside a kindness:

| Bound | The slip |
|---|---|
| Librarian | "Rest. Even the ninth flame of a fire needs tending." |
| Medic | "Your pulse is good. Better than ninety, for a ninth—" (they stop, and say "for a Chunin") |
| Councillor | "The council is pleased. Number nine of the registry's children to make Chunin." (The registry has no such count; you are S-114) |
| Merchant | The note: "For the ninth of my favourite customers. Eat the persimmons first." |

Innocent candidates' parallel lines carry no number. A player who caught "Nine" in Ch 0 can solve
the case here. The journal records the line (`story.clue.slip.heard`), so the case board can recall
it.

**Ch 25.3, the gift's name.** The librarian comes that night in **every** save, with the song book:
in the innocent track she names the gift herself; in the bound track she brings the book and lets the
keeper, who arrives behind her, do the naming ("Ask him. He has read more than I have."). Both
versions are warm; neither is a tell on its own.

**Small divergences after the beta** (allowed, each with an innocent reading): the councillor's
vote at the Ch 31 council (bound: he abstains, "for the registry's neutrality"; innocent: he votes
for the Tobari), and, in the merchant's bound track, a remembered line about a cart ride "years
ago" that an innocent merchant says about a different child.

**2. The hand's last words (Ch 28).** The caught porter cannot say the voice's name: a cinder seal on
his tongue burns when he tries. What he manages: *"The voice keeps the names in its own hand.
Six years in its own hand."* This tells the player that Yūgure's list will be in the voice's
notation. Same line in every save.

**3. Alibis (Chunin side content and Ch 38).** Each innocent candidate has an alibi the player can
find; the bound candidate's alibi fails:

| Candidate | Alibi if innocent | Failing alibi if bound | Found in |
|---|---|---|---|
| Librarian | The cipher book of `overdue` was returned on the library's closed day; she was at the shrine all day (the priest's visitor book) | The visitor book shows her leaving at noon | `side.c.returned_book` (Chunin side) or the case board |
| Medic | On the night the ledger pages vanished they were in surgery from dusk to dawn (the surgery roster, and the player saw them if they did `night_shift`) | The roster shows a twenty-minute gap; if the player did the night shift, they remember the medic's empty station | `night_shift` memory or the case board |
| Councillor | The pass's date: he was at the daimyo's court that week (the court's guest roll) | He was in the village; his seal box never left his desk (his own clerk's log) | `side.c.court_roll` (Chunin side) or the case board |
| Merchant | They name the carpenter who sold the cart; a Chunin B-rank finds his abandoned shop full of false floors | The carpenter is real but the floor in their cart carries the merchant's own tool marks | `mission.b.false_floors` (Chunin B-rank) or the case board |

**4. The list (Ch 35, decoded Ch 38).** Yūgure's list, decoded, indexes six years of children in
the bound candidate's notation and carries the private mark. The player compares it with the
documents in the journal (`journal.documents`: the intake ledger page, the stipend papers, the
shelving slip, the delivery book page). Decisive.

### The case board and the accusation (Ch 38 to 39)

The case board (a journal page and a pinboard furniture piece in the apartment) collects every
clue, slip, alibi and document. To **accuse with proof** the player needs two of three: the slip,
the list's notation, a failed alibi. The player may also accuse anyone without proof.

| Accusation | What happens |
|---|---|
| **The bound candidate, with proof** | The confrontation (below). The player chooses: **arrest** them openly, or **turn** them (they keep feeding Yūgure, now false news: in Ch 51 one district's array anchors are already broken, and the leader's assault starts an hour late). Turning needs `friendship [bound, 4]` or the candidate's own wish to make amends (librarian, medic) |
| **The bound candidate, without proof** | They deny it; the keeper refuses to act; two days later they try to run (a chase at the east gate, Ch 39b). Caught: arrested, no turning |
| **An innocent candidate** | The Sixth detains them on your word. `start_conflict` with them (`went_over_their_head` if you were close). The real voice, alarmed, tries to steal the archive key that night: the chase (Ch 39b). The innocent is freed; an apology quest (`bond.c.wrongly_accused.<candidate>`) can mend it |

Every path reaches the truth in Ch 39 and the same Ch 40. Agency changes the cost and the help you
get in the finale, never whether the story continues.

### The four reveals

| Bound | The scene | What they say (the heart of it) | After |
|---|---|---|---|
| **Librarian** | In the library at night, among the aptitude scrolls; she has the cut page's copy in her sleeve | "My grandmother was one of the twenty-seven. She whispered our real name to me once and never again. He wrote to me for ten years like a cousin. He said he was finding the lost ones. I gave him children, and I told myself I was giving them home." She knew you were Nine before you came to the Leaf | Arrested: her family's secret history goes to the archive; she asks to teach the old songs to the restored clan from her cell. Turned: she sends the false signals, and in the epilogue the player as Hokage rules on her |
| **Medic** | The hospital roof at dawn; they have the green ink on their fingers | "They pulled me out of a burning orphanage when the Leaf was three days away. I owed them my life. I sent readings. Just numbers, I said. Then I saw her come back hollow." (They mean the lost child, Ch 24.) "That was mine. I measured her." | Arrested, or turned; they ask to treat the lost child, whatever happens to them |
| **Councillor** | His study, his seal box open | "My grandfather drafted the fourth clause and then voted to end them. The Senju owe a clan its name. The village would never pay; he said he would make it pay without blood. I believed the part I wanted." He arranged your stipend to keep you safe *and* on file, and cannot say which he meant more | Arrested and stripped of the council seat; the Senju clan line's Heart step (`clan.senju.4`) becomes his house's reckoning. Turned: he keeps his seat as a mole, hating every day of it |
| **Merchant** | Their cart in the rain at the east gate, half packed to run | "It was paper. Then it was paper and names. Then once there were children under the floor, and they paid me three times over, and I told myself it was the last time." They kept hiring your squad because you were the one child they had carried who came back | Arrested; their delivery book helps the A-rank hunts. Turned: they run the false cargo |

The bound candidate's bond is never gated by the reveal: the player can be close to them. On the
reveal: `start_conflict` with `broke_secret` for the bound candidate (the betrayal is of the
player's trust); a player at level 7 or more with them gets an extra scene (Ch 39c, "Why you") in
which the candidate answers the question they once asked the player (see each character file).

### Innocents cleared

When a candidate is cleared (Ch 40), each gets a scene: the librarian gives you her family's song
book (she knows the old forms of the gift; her training line opens: `friendship [librarian, 7]`);
the medic asks to care for the lost child; the councillor votes to open the archive in public; the
merchant becomes the squad's informant on the roads. If the player suspected them aloud
(`story.suspected.<candidate>`), a `reconciled` moment.

### Fairness checks (per bound candidate)

| Bound | Can an attentive player solve it before Ch 38? | Can every player solve it at Ch 38? | Cheats? |
|---|---|---|---|
| Librarian | Yes: the slip ("ninth flame") at Ch 25; the shrine visitor book (`returned_book`) | Yes: shelf marks and brushed circles on the list | None: the circles were shown in Ch 5 |
| Medic | Yes: the slip at Ch 25; the empty station if they did the night shift | Yes: green-ink pulse counts and cranes on the list | None: the crane was shown on your own sample in Ch 0 |
| Councillor | Yes: the slip at Ch 25 ("number nine of the registry" against your known S-114); the clerk's log | Yes: S-numbers and pine marks | None: your papers were shown in Ch 1 |
| Merchant | Yes: the slip in the note at Ch 25; the tool marks on the floor | Yes: road-stop shorthand and tailed ticks | None: the book was shown in Ch 11 |

---

## 2. `twist.lineage`: whose child you are

### What is fixed in every save

- The player is Kagari-blooded with the strongest flame in generations, born ~Y-12, raised to six
  in a border village house with a **persimmon tree**, by people who sang the **watch-fire song**.
- The player has one possession from before: **half a carved wooden watch-fire charm**, sewn into a
  sleeve and missed by the nursery guards (a key item from the creator screen, never droppable).
  Watch-fire charms are carved in pairs, one for a parent and one for a child.
- `fallen_parent` (the sensei's teammate, a Kagari descendant) died in the Ash Road ambush ~Y-8. In
  every save they had a young child with a civilian spouse, both reported "lost" after the ambush;
  the sensei and `sensei_3` know a child was lost and never speak of it before Ch 48. Persimmons were
  `fallen_parent`'s favourite fruit; the sensei leaves one at the memorial stone every year.
- The sensei keeps a box with `fallen_parent`'s forehead protector in every save.
- `yugure_second` is a Kagari descendant and an ember user, and she lost a child.
- **Both** the sensei and the second know the watch-fire song. Both react to it.

### The candidates

| | **A: the second is your mother** (`twist.lineage = second`) | **B: the fallen Leaf shinobi was your parent** (`twist.lineage = fallen`) |
|---|---|---|
| `fallen_parent`'s lost child | Truly died with the spouse after the ambush | Is you: the spouse fled with you to the spouse's sister in the persimmon house |
| The truth | At twenty-two, the second bore you (the father, a border-town civilian, died in a skirmish before you were born). She hid you with her sister's family in the persimmon house to keep you from the leader, who wanted a pure flame. When the cells took you at six, the leader told her you had died in the fire. She believed him | `fallen_parent` married a civilian of the border village and kept the child there, far from the village's eyes. After the Ash Road ambush the spouse fled with the child to the spouse's sister in the persimmon house. Yūgure found it two years later |
| Who holds the other charm half | The second, on a cord under her collar | The sensei, in the box with `fallen_parent`'s forehead protector (the box exists in both saves; only in B does it hold a charm half and an unsent letter) |
| Why the second spares you in the forest (Ch 16.3) and names you (Ch 19) | She feels the flame on day three; on the last night she hears the watch-fire song from your camp (16.7); she does not let herself believe | She feels a flame she has only felt once, in herself; she sees a child of the nurseries she swore to protect; her own son died in a nursery |
| Why the sensei suspects you (Ch 14) | Your flame is `fallen_parent`'s flame: the leaning campfire on their old missions. They suspect *what* you are | They suspect *who* you are; the persimmon detail (Ch 21) is a blow |
| The persimmon on the sill (Ch 27) | The second left it, having learned where you live | The sensei left it on the anniversary, as they leave one at the memorial stone every year (the stone ritual happens in both saves) |
| The hint (Chunin, Ch 25) | The librarian or keeper names the charm and the song: someone has the other half; it is your parent's | Same |
| The reveal (Road to Hokage, Ch 48) | The second defects (Ch 48), comes to the persimmon house's ruins, and shows her half. The halves fit. "I sang you that song. I did not know you would keep it" | The Seventh (the sensei) takes you to the persimmon house's ruins and gives you the box: the forehead protector, the half charm. "I should have looked for you. I believed the report I signed" |
| Who carries the succession | The second's choice in the finale (she shields you); the Seventh names you successor as a teacher | The Seventh names you successor as the child of their teammate; the succession speech carries `fallen_parent`'s name |

### Fairness

- Every clue appears in both saves (the song, the charm, the sparing, the suspicion, the persimmon).
  In each save the explanations that point the wrong way stay true (the second really did lose a
  child; the sensei really did lose a teammate with the same flame).
- The decisive evidence (the matching half charm) is held back to the reveal in both. The story
  never lies to the player: the second never claims to be or not be the parent before Ch 48; the
  sensei never says "your parent" before Ch 48.

### What changes downstream

| | A | B |
|---|---|---|
| The second's fate scene (Ch 52 to 54) | She shields you as a mother; if she lives, the epilogue has her in the restored clan's hall | She shields you as a debt to her own son; if she lives, she keeps the old shrine |
| The sensei's guilt | About their teammate, and about not seeing the flame | About the teammate *and* their child (you) |
| The memorial (Ch 41) | Her family name among the twenty-seven | `fallen_parent`'s name moved back beside the Kagari names |
| The restored clan's head of house | You, with the second as elder if she lives | You |

---

## 3. `twist.fourth_fate`: what the finals cost the Fourth

| | **Falls** | **Crippled and abdicates** | **Taken** |
|---|---|---|---|
| Ch 19 | He holds the Kage box's barrier while the stands empty, then fights the leader's two-man cells on the arena floor and dies covering the evacuation of the Academy children (you see him fall from where your squad is holding the east stair) | He takes the leader's blow meant for the stands; the dark mirror tears half his chakra. He lives | He is hit by a binding seal and carried off through the smoke by the leader's cell; you see the ash-violet cloaks lift him over the wall |
| Ch 20 | The funeral at the Rock in rain; the stipend's founder; the whole village under umbrellas. The Fifth named | The hospital; he abdicates from his bed and names the Fifth himself ("She is hard. The Leaf needs hard for a while") | The empty seat: the council names the Fifth "until he returns" |
| Ch 21 (Chunin opening) | A year later; his statue's unveiling in the Academy yard; the stipend continues in his name | A year later; he teaches the Academy's history class from a wheelchair. He is your mentor in the Chunin arc (an advisor the player can visit) | A year later: intel finally places him in a Yūgure hold; the opening mission, **The Empty Seat**, brings him home, hollowed by the leader's experiments. He returns too weak to rule and becomes a mentor (as the crippled path) |
| What it teaches the player | Loss, and the will he left | The cost of the dark mirror, seen in a man you love | The dark mirror's purpose: the leader is practising |
| Later beats | Ch 55: you restore the stipend in his name as the Eighth | Ch 51: he sits in the Kage box to defend the Academy again; Ch 55: he is at your inauguration | Ch 51 to 53: he recognises the array's feel ("I have felt this before") and warns the Seventh; Ch 55: at your inauguration |

In every save the Fifth is named in Ch 20 and `world.hokage = 5`.

---

## Rotation test matrix

`quests.py --check` (and the story review) must pass with every combination: 4 × 2 × 3 = **24**
saves. The combinations that need care:

| Combination | Watch for |
|---|---|
| Traitor = medic, fate = crippled or taken | The medic treats the Fourth; the medic's reveal scene must not need the Fourth healthy |
| Traitor = councillor, lineage = B | The councillor signed the Ash Road sealing, which hid your parent's death; his reveal adds a line about it (`if twist.lineage = fallen`) |
| Traitor = merchant, lineage = A | The merchant's note "Eat the persimmons first" (the slip) touches the persimmon motif; in A the persimmon on the sill comes from the second, not the merchant. Keep them on different days (Ch 25 and Ch 27) |
| Traitor = librarian | Without her, the gift's old forms come from the keeper (who learned them from the archive) and from the second (Ch 48) |
