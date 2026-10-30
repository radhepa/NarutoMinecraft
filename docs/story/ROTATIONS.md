# Rotations: the twist slots in full

> **SPOILERS: for developers only.** Part of the [story bible](STORY_BIBLE.md).

Three slots are bound at world creation by the `twists` stream, in Classic and Varied alike:
`twist.traitor` (4 candidates), `twist.lineage` (2), `twist.fourth_fate` (3). This file is the
contract for each: every candidate's clue trail, its innocent explanation when not bound, the
decisive evidence, the reveal, and the fairness checks. `quests.py --check` verifies that every
candidate has a complete trail and an innocent explanation (ROADMAP §5).

**The fair-play rule.** Through the whole beta, all candidates' clues play identically in every
save: a player cannot tell the bound candidate from beta content alone, and a player who knows the
answer from another save learns nothing. After the beta the trails diverge only at the points in
**Allowed divergences** below, so an attentive player can solve it before the Jonin arc's reveal,
and every player can solve it at the case board (Ch 38) from evidence they have been shown.

### Allowed divergences (the only ones)

Before Ch 39, exactly three things may differ between rotations. Everything else (every scene,
vote, question, visit, withdrawal, flicker, thread and line) is identical in every save, and every
other file cites this list:

1. **The slip** (Ch 25.1): the bound candidate's one line.
2. **The recorded results of the four alibi checks** (`side.c.returned_book`, `side.c.court_roll`,
   `mission.b.false_floors`, the surgery roster at Ch 38): the innocent's alibi holds, the bound
   one's fails.
3. **The content of Yūgure's list** as decoded at Ch 38: its notation, its hand and its private mark.

**The schedule rule.** Candidates' visible daily schedules and movements are identical in every
save. The four alibi moments are never shown on screen; they exist only as records (rosters, logs,
visitor books). On each evidence date the candidate is off the player's map in every save (indoors
behind a closed door, or away from the village), so no sighting can confirm or contradict a record. The bound candidate's threads to third parties (squad4_c to the medic, and so on)
look the same in every save before Ch 39.

From Ch 39 on, the reveal, the clearing scenes and their callbacks differ freely.

**The reveal-gate rule.** A line, row or gate in any file that keys on a twist slot before that
slot's reveal (Ch 39 for the voice, Ch 48 for the lineage, the event itself for the Fourth's fate)
contradicts this file unless it is one of the three allowed divergences above, or the one
sanctioned read with no visible output: Ch 27.4 reads `twist.lineage` to set who left the persimmon,
and the giver is never shown (§2). Fix the line, never
the contract. Every downstream table here takes effect only after its slot's reveal.

---

## 1. `twist.traitor`: the voice

### What is fixed in every save

- **The hand** is always the `porter` (fixed role, fixed look: a lanky young man with a carrying
  frame, polite, a burn scar on his palm). He was a nursery child, "rescued" by Yūgure at eight and
  sent into the Leaf at sixteen as a porter for the furniture shop and the post. He carries for
  everyone: furniture into the player's flat (Ch 1), the library's returns cart, the hospital's
  linen, the council's letter bags, crates loaded onto merchants' carts at the east gate. He lays
  the array's cinder seals under what he carries. He scratched the sinking sun on the player's door
  (Ch 4) and is the figure on the rooftops. The cinder seal that silences him is in his **palm**,
  under the burn scar.
- **The voice** is the bound candidate. Since about **Y-10** the voice has fed Yūgure, in every save:
  through the porter since Y-6, and by **the first hand** before that (an old east-road carter, no
  clan, an ordinary family name, who died in a road accident at Y-6). What the voice sent: the names
  of gifted children with their chakra readings (the nurseries' recruiting list), the guard rotations
  for the finals (Ch 19), and the archive door's schedule. Every candidate was old enough at Y-10
  (the medic, born ~Y-31, was contacted at 21 as a new hospital orderly). Where a candidate speaks a
  span at their reveal, it is "sixteen years".
- **The Ch 0 raid was not the voice's leak.** The porter loaded the raid squad's supply crates and
  reported the muster himself: **the hand warned the leader**, who let the raid happen (his plan,
  WORLD.md).
- **The sources reach border children too**: the library files the border outposts' entrance tests
  with the aptitude scrolls; the stipend registry lists the border-village orphans the Leaf
  sponsors; the hospital ledger logs every rescued child; the merchant's book logs every stop.
- **The hideout's cells were unnumbered**, and no Leaf rescuer heard "Nine": only the player, the
  lost child (who heard the guards say it) and Yūgure's own mail carry it. The Undercroft reads it in
  that mail (below) and tells no one.
- **Daily lives are identical**: every candidate's schedule and night movements are the same in
  every save until Ch 39 (the schedule rule above). The innocent librarian writes to a real cousin in
  a border town too, so letters are no difference.
- **Who does the deed, by save** (single source; character files cite this):

| Deed | Bound save | Innocent save |
|---|---|---|
| The cut page (Ch 5) | The librarian cuts it and hands it to the porter | The porter cuts it while collecting returns |
| The dead drop in the returns cart (`overdue`) | The librarian's | The porter's |
| The travel pass's seal (Ch 14) | The councillor seals it himself | The porter uses the open seal box on a post day |
| The intake ledger's torn pages (night shift) | The medic tears them out | The night patient (the smuggler) tears them out |
| The false floor (Ch 11) | The merchant built it | A carpenter in the east built it before the sale |

- **Why the page was cut that week (Ch 5).** The stipend registry had just flagged a new
  Kagari-reactive child (the player, S-114). Yūgure asked the voice for the page that names the
  twenty-seven's families, to know which Leaf families to test next.
- **Ch 37 timing.** Three days pass between the Ash Road report (37.0) and the blade's raid (37.3):
  the archive stays open while the keeper copies the list. Every candidate's post-Ch-28 channel
  reaches Yūgure's pickup at the east-road waystation within two days, equally in every rotation.
- **Yūgure's list** is kept in the voice's own notation. A cell's copy, captured in the Valley of
  Ash (Ch 35), holds sixteen years of entries (from ~Y-10), all in one notation and one hand: the
  voice's. (Why a Leaf
  notation indexes children from outside the Leaf: it is the voice's private habit of mind; they
  keep every child they report in the system they use every day.)
- **The four sources and their notations**, each shown to the player in the beta, in every save:

| Candidate | Source of names | Notation (shown in) | Private mark |
|---|---|---|---|
| `librarian` | The Academy aptitude scrolls, filed in the library | Shelf marks: `Leaf 7-iii` (Ch 5, shelving the scrolls) | A small brushed circle beside a gifted child |
| `medic` | The hospital intake ledger of rescued and orphaned children | Pulse counts in green ink: `p 88 / 112` (Ch 0, your own sample) | A tiny folded-crane stroke |
| `elder_councillor` | The orphan stipend registry | Stipend numbers: `S-114` (Ch 1, your own papers; you are S-114) | A hand-drawn pine-sprig flourish beside a name (not the seal stamp) |
| `merchant` | Their delivery book of orphanages and waystations | Road-stop shorthand: `E3 · two · bright` (Ch 11, the book in the cart) | A tick with a tail |

- **The red herring** in every save is the `elder_keeper`, who watches the player, guards a door and
  lies about knowing things. He is never the voice; his secret is the archive.
- **The Undercroft** (Night Watch) knew of "Nine" and of a voice from intercepted mail, but never
  learned who; they kept silent to use the knowledge, not to share it.
- **Journal documents** (`journal.documents`), each in the candidate's own hand (the shelving slip is
  the librarian's). Four scenes each add an unmissable document to the
  journal, showing the notation and the private mark, in every save: Ch 0.6 the medic's intake slip
  (your own reading, green ink, the crane stroke; the medic hands you a copy "for your records");
  Ch 1.2 your stipend papers (S-114, the pine seal and a hand-drawn pine-sprig flourish); Ch 5.1 the shelving slip (a shelf mark with a
  brushed circle beside a name); Ch 11.1 a torn page of the delivery book (`doc.delivery_page`; the
  merchant gives it to you to keep). The case board also pins the Ch 0 subtitle **"Nine. Up."** as a memory card, so a
  player who missed it can still connect the slip.
- **Thread Sight cannot solve it.** From Ch 24 the player sees bonds as threads, and a bonded
  person who hides something shows a **steady flicker** (one `hides:` bond flag, never line by line;
  it is not a lie detector). Each candidate carries exactly one `hides:` flag of the same kind until
  Ch 39/40, and none is ever a scripted thread exception before Ch 39. The limit ([WORLD.md](WORLD.md#thread-sight-and-the-mystery-a-principled-limit)):
  it reads only people bonded to the player at 6+, it shows *that* someone hides, never *what*, and
  all four candidates hide a true secret in every save (the librarian her Kagari family history;
  the medic their letters to the strangers who saved them; the councillor his signature on the Ash
  Road sealing; the merchant old debts and bandit smuggling). All four flicker the same. The hand
  (the porter) is never in the player's web, so the voice's tie to him never shows. The bound
  candidate's thread to the player reads as an ordinary two-way thread (never fraying or one-sided
  because of the treachery).
- **Held-back secrets.** Each candidate may share parts of their every-save secret as the bond grows,
  in every save alike, but keeps one piece back until Ch 39 or Ch 40, so the flicker never goes out
  early in any rotation:

| Candidate | Shared as the bond grows (every save) | Held back until Ch 39/40 (every save) |
|---|---|---|
| Librarian | Her Kagari family history (Ch 25.3 if at friendship 3) | What the cut page listed |
| Medic | That strangers saved them from a burning orphanage | The last reply in the crane jar (their outpost letters) |
| Councillor | That he signed the Ash Road sealing (after Ch 36) | His grandfather's vote |
| Merchant | Old debts and bandit smuggling years ago | The night at the waystation before Ch 14 |

- **Access routes.** The voice leaked three things. Every candidate, in every save, had a plausible
  route to all three, so reasoning from access convicts no one:

| Candidate | The finals' guard rotation (Ch 19) | That the archive would be open (Ch 37) | A channel after the porter falls (Ch 28) |
|---|---|---|---|
| Librarian | The Academy's exam-hall duty roster, filed in the library | The Sixth's clerk told the library (archive books were requested) | Letters to a "cousin" in a border town |
| Medic | The stadium triage posts list, issued with the guard posts | The Sixth's clerk told the hospital (a medic on standby) | Letters to the outposts |
| Councillor | The council's briefing | Told as an elder | Council post |
| Merchant | The vendor stall permits, which list the guard posts | Gate gossip from the Sixth's clerk's errands | The cart |

  None of the four leaked the Ch 0 raid: in every save that warning came from the hand (the porter
  loaded the raid squad's crates), so the raid points at no candidate.

  If the player asks the Fourth (crippled or taken saves) who sees the guard rotation, he says the
  same in every save, in one version: "Half the village, child. Medics, vendors, the council, the
  Academy." 

### The shared clue trail (identical in every save)

| Clue | Where | What the player sees | If bound | If innocent |
|---|---|---|---|---|
| `story.clue.medic.1` | Ch 0 | The medic takes a sample of your chakra "for the records" and writes it in green ink with a crane stroke | The reading went to Yūgure | They test every rescued child; it is hospital routine |
| `story.clue.councillor.1` | Ch 1 | Your stipend papers (S-114) were arranged by the councillor personally, pine seal on the corner | He kept the wick close and on file | The keeper asked him to; he did it as a favour and a kindness |
| `story.clue.medic.2` | Ch 3 | The medic drops by the evening of the flare "to check on you" | To report the flare | The instructor asked the medic to check, worried |
| `story.clue.librarian.1` | Ch 5 | The founding history's cut page; the edge is fresh | She cut it that morning and handed it to the porter | The porter cut it while collecting returns; she found it that morning |
| `story.clue.librarian.2` | Ch 5 | The librarian is nervous and lies that the page "has been gone for years" | She is afraid of being caught | She is afraid of what the page was: her own family's secret history. She lies to protect it |
| `story.clue.librarian.3` | Side: `district.b1.academy.overdue` | One overdue book, still out in the village before it is returned, holds a slip in an unknown cipher (Yūgure's): an incoming order in one fixed hand in every save, never a candidate's hand or mark. The player keeps the slip, so that one order never reaches the cart | A dead drop she used | The porter used the returns cart as a dead drop |
| `story.clue.merchant.1` | Ch 11 | The cart's false floor of chakra paper; the delivery book with its shorthand. In every save the merchant repairs the broken axle with their own tools (the tool marks the bound alibi later fails on) | They carry paper and names | They bought the cart second-hand from a carpenter in the east who built the floor; they did not know |
| `story.clue.merchant.2` | Ch 14 | The merchant slows the squad on the road, inventing reasons | To let the hearth slip past | A pair in road clothes with soot-marked wrists threatened them at the waystation the night before |
| `story.clue.councillor.2` | Ch 14 | The captured smuggler's travel pass bears the councillor's pine seal | He sealed it himself | His seal box sat open on his desk on post days, when the porter collected the council post; the porter used it |
| `story.clue.councillor.3` | Side: `event.b2.council_day` | From the gallery you see the councillor hand a sealed letter to the porter | A report | Ordinary council post |
| `story.clue.merchant.3` | Side: `district.b2.contraband` | The gate log shows the merchant's cart passed with no inspection, twice | They bribed the guard | The bored Hagane guards waved every regular through (the betting ring's guards) |
| `story.clue.medic.3` | Side: `district.b2.night_shift` | Pages are missing from the hospital's intake ledger after your night shift. The night plays identically in every save: you are sent on an errand to the herb store during the window, if this shift is the ledger night (a later shift finds the pages already gone, and nothing is missed during it), and nothing about the medic is seen | They tore them out | The night patient (the smuggler) tore them out (see the alibi below) |
| `story.clue.medic.4` | Side: `side.b3.hospital_supplies` | The diverted supplies' requisition is in green ink | Not theirs; the voice never touched it (a pure red herring in every save) | A forged requisition by an exam official; the trail clears them (SIDE_QUESTS bible entry) |

Every candidate has at least three beta clues; none is decisive.

### Where the trails diverge (Chunin and Jonin arcs)

**1. The slip (Ch 25).** In the hospital after the border post, all four candidates come to the
player, each for a natural reason: the medic treats you, the librarian brings books, the councillor
visits for the council (you are a Chunin on stipend files), the merchant sends a basket of fruit
and dried persimmons with a note. Each line is warm and parallel. **The bound candidate's line holds a detail only
Yūgure's reports contain: the player's nursery number.** Guards called the player "Nine" in Ch 0;
the player never says it to anyone (no dialogue option offers it before the reveal). The slip is
quiet and lands inside a kindness:

| Bound | The slip |
|---|---|
| Librarian | "Rest. Even the ninth flame of a fire needs tending." |
| Medic | "Your pulse is good. Better than eighty-eight, for a ninth—" (they stop, and say "for a Chunin") |
| Councillor | "The council is pleased. Number nine of the registry's children to make Chunin." (The registry has no such count; you are S-114) |
| Merchant | The note: "For the ninth of my favourite customers. Eat the persimmons first." |

Innocent candidates' parallel lines carry no number (the innocent medic: "Your pulse is good. Better
than eighty-eight, for a Chunin."), and no other line anywhere puts a count of nine near the player. A player who caught "Nine" in Ch 0 can solve
the case here. The journal records the line (`story.clue.slip.heard`), so the case board can recall
it.

**Ch 25.3, the gift's name** (identical in every save). If `friendship [librarian, 3]`, the
librarian comes that night with the song book, tells the player her family's heritage and names the
gift; else the keeper comes and names it. **Ch 31's council vote** (identical in every save): the
councillor abstains, "for the registry's neutrality".

**2. The hand's last words (Ch 28).** The caught porter cannot say the voice's name: a cinder seal in
his palm burns his memory out when he tries. What he manages: *"The voice keeps the names in its own
hand. Years in its own hand. All of them in its own hand."* This tells the player that Yūgure's list will be in the voice's
notation. Same line in every save.

**3. Alibis (Chunin side content and Ch 38).** Each innocent candidate has an alibi the player can
find; the bound candidate's alibi fails:

| Candidate | Alibi if innocent | Failing alibi if bound | Found in |
|---|---|---|---|
| Librarian | On the closed day `side.c.returned_book` follows, a book came back through the returns slot and was checked in on her desk ledger (she logs every return the moment she takes it from the cart, so the entry's date is when someone was inside the locked library). In every save she says, in the same words: "I was at the shrine all that day." The entry is dated the next morning, and the priest's visitor book has her in at dawn and out at dusk | The entry is dated that afternoon, and the visitor book shows her leaving at noon: she lied, and was at her desk | `side.c.returned_book` (Chunin side) or the case board |
| Medic | On the night the ledger pages vanished they were in surgery from dusk to dawn (the surgery roster, kept by `squad4_c`; a player whose night shift was the ledger night remembers being sent away during exactly that window) | The roster shows a twenty-minute gap inside the window | The case board (Ch 38.4) |
| Councillor | The pass's date (the pass is dated the day the squad sets out for Ch 13's border village (13.1); you are away from the village until 13.3 ends, so no sighting of him that day is possible in any save. It is a post day, and the mission desk never sends Ch 13 out on the council day (the first Moonday of the season)): he was at the daimyo's court that day (the court's repaired guest roll); his seal box sat on his desk, open on a post day | The repaired guest roll has no entry for him that day, and his clerk's log (the clerk logs every seal-box sign-out by habit) shows him signing the seal box out himself that date and sealing "a travel pass" | `side.c.court_roll` (Chunin side) or the case board |
| Merchant | They name the carpenter who sold the cart; a Chunin B-rank finds his abandoned shop full of false floors | The carpenter is real but the floor in their cart carries the merchant's own tool marks | `mission.b.false_floors` (Chunin B-rank) or the case board |

Each alibi's event happens on its date in every save, played or not: a book comes back through the library's returns slot on the library's first closed day after Ch 21, the day `side.c.returned_book` follows (never the overdue book, whose slip the player already holds; in an innocent save the porter, who holds a cart key, takes the order out that evening, and she logs the book the next morning), and the ledger pages vanish from the hospital on the ledger night: the night of your night shift if you work it on or before the night Ch 14 ends, otherwise the night Ch 14 ends (a shift worked later finds them already gone). At 38.4 the case board states the event (the library's closed-day return, with the librarian's recorded claim that she was at the shrine all that day, the hospital's note of the missing pages) before its record is checked, so a player who skipped `side.c.returned_book` or `night_shift` is never asked about an event they were not shown.

**4. The list (Ch 35, decoded Ch 38).** Yūgure's list, decoded, indexes years of children, all in
the bound candidate's notation and hand, and carries the private mark. The player compares it with
the documents in the journal (`journal.documents`: the intake slip, the stipend papers, the
shelving slip, the delivery-book page). Decisive.

### The case board and the accusation (Ch 38 to 39)

The case board (a journal page and a pinboard furniture piece in the apartment) collects every
clue, slip, alibi and document. To **accuse with proof** the player needs two of three: the slip,
the list's notation, a failed alibi. The board never assumes the slip was heard (the Ch 25.1 visits are optional), so the notation and the alibi alone are always enough. The player may also accuse any of the four sources without proof; the keeper is never among them (his card has no accuse action).

| Accusation | What happens |
|---|---|
| **The bound candidate, with proof** | The confrontation (below). The player chooses: **arrest** them openly, or **turn** them (they keep feeding Yūgure, now false news: in Ch 50 one district's array anchors are already broken, plus the candidate's own payoff, below). Turning needs `friendship [bound, 4]` or the candidate's own wish to make amends (librarian, medic) |
| **The bound candidate, without proof** | They deny it; the keeper refuses to act; two days later they try to run (a chase at the east gate, Ch 39b). Caught: arrested, no turning |
| **An innocent candidate** | The Sixth detains them on your word. `start_conflict` with them (`went_over_their_head` if you were close). The real voice, alarmed, tries to steal the archive key that night: the chase (Ch 39b). The innocent is freed; an apology quest (`bond.c.wrongly_accused.<candidate>`) can mend it |

Every path reaches the truth in Ch 39 and the same Ch 40. Agency changes the cost and the help you
get in the finale, never whether the story continues.

**Turned payoffs** (in every turned save, one district's anchors are already broken in Ch 50; and
each candidate adds their own):

| Turned | Payoff in Ch 51a |
|---|---|
| Librarian | Her false signals hold the first wave back from the wall an hour past dusk (Ch 51a still begins at the second dusk) |
| Medic | False casualty lists sent to Yūgure; the hospital is ready before the first wave |
| Councillor | False council orders; the west wall is ready where the hearths planned to break it |
| Merchant | False cargo: one wave arrives without its cinder bombs |

### The four reveals

**The voice owns the stadium.** Each reveal has one line about the finals' guard rotation, keyed
to `twist.fourth_fate`: what they were told it was for ("a show of strength; no one would be
hurt") and what they felt when the Fourth was hit on the stair (these are samples of the shape; the shipped lines
are the stadium lines in each candidate's file: falls: "I watched him fall on the
stair I had given them."; crippled: "I watched him carried down the stair I had given them, and I
went home."; taken: "I watched them lift him over the wall, and I told myself he'd come back.").
The councillor's "without blood" is the lie he was told and believed. `squad3_b` hears of it at
the Ch 40 council.

| Bound | The scene | What they say (the heart of it) | After |
|---|---|---|---|
| **Librarian** | In the library at night, among the aptitude scrolls; she has the cut page's copy in her sleeve | "My grandmother was one of the twenty-seven. She whispered our real name to me once and never again. He wrote to me for sixteen years like a cousin. He said he was finding the lost ones. I gave him children, and I told myself I was giving them home." She knew you were Nine before you came to the Leaf | Arrested: her family's secret history goes to the archive; she asks to teach the old songs to the restored clan from her cell. Turned: she sends the false signals, and in the epilogue the player as Hokage rules on her |
| **Medic** | The hospital roof at dawn; they have the green ink on their fingers | "They pulled me out of a burning orphanage when the Leaf was three days away. I owed them my life. I sent readings, sixteen years of them. Just numbers, I said. Then I treated your friend after the border post, and saw what she had done with what was put in her." (They mean the lost child, Ch 24; the medic treated the fallen friend in Ch 25.) "That was mine. I measured her." | Arrested, or turned; they ask to treat the lost child, whatever happens to them. (They learned what the strangers were at 21, when the leader's gatherers who had saved them at ~Y-24 came to collect the debt) |
| **Councillor** | His study, his seal box open | "My grandfather drafted the fourth clause at the founding and voted to end them ten years later. The Senju owe a clan its name. The village would never pay; he said he would make it pay without blood. I believed the part I wanted." He arranged your stipend to keep you safe *and* on file, and cannot say which he meant more | Arrested and stripped of the council seat; the Senju clan line's Heart step (`clan.senju.4`, which opens only after `story.ch39.done` in every save) becomes his house's reckoning. Turned: he keeps his seat as a mole, hating every day of it |
| **Merchant** | Their cart in the rain at the east gate, half packed to run | "It was paper. Then it was paper and names. Then once there were children under the floor, and they paid me three times over, and I told myself it was the last time." (They kept hiring the squad because they liked it, and being close kept them close to the news.) | Arrested; their delivery book helps the A-rank hunts. Turned: they run the false cargo |

The bound candidate's bond is never gated by the reveal: the player can be close to them. On the
reveal: `start_conflict` with `broke_secret` for the bound candidate (the betrayal is of the
player's trust); a player at level 7 or more with them gets an extra scene (Ch 39c, "Why you") in
which the candidate answers the question they once asked the player (see each character file).

### Innocents cleared

When a candidate is cleared (Ch 40), each gets a scene: the librarian gives her family's notebook to the
archive (she knows the old forms of the gift; her training line opens: `friendship [librarian, 7]`);
the medic asks to care for the lost child; the councillor votes to open the archive in public; the
merchant becomes the squad's informant on the roads. If the player suspected them aloud
(`story.suspected.<candidate>`), a `reconciled` moment.

### Fairness checks (per bound candidate)

| Bound | Can an attentive player solve it before Ch 38? | Can every player solve it at Ch 38? | Cheats? |
|---|---|---|---|
| Librarian | Yes: the slip ("ninth flame") at Ch 25; the shrine visitor book (`returned_book`) | Yes: shelf marks and brushed circles on the list | None: the circles were shown in Ch 5 |
| Medic | Yes: the slip at Ch 25 | Yes: green-ink pulse counts and cranes on the list; the roster's gap | None: the crane was shown on your own sample in Ch 0 |
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
| `fallen_parent`'s lost child | Truly died with the spouse after the ambush | Is you: the spouse fled with you to the spouse's sister in the persimmon house. The spouse had learned the watch-fire song from `fallen_parent` and sang it to you; the sister kept singing it after the spouse died of fever a year later. The sealed report (~Y-8) listed the spouse and child as "lost"; nobody in the Leaf ever learned of the persimmon house |
| The truth | At twenty-two, the second bore you (the father, a border-town civilian, died in a skirmish before you were born). She hid you with her sister's family in the persimmon house to keep you from the leader, who wanted a pure flame. When the cells took you at six, the leader told her you had died in the fire. She believed him | `fallen_parent` married a civilian of the border village and kept the child there, far from the village's eyes. After the Ash Road ambush the spouse fled with the child to the spouse's sister in the persimmon house. Yūgure found it two years later |
| Who holds the other charm half | The second, on a cord under her collar | The sensei, in the box with `fallen_parent`'s forehead protector (the box exists in both saves; only in B does it hold a charm half and an unsent letter) |
| Why the second spares you in the forest (Ch 16.3) and names you (Ch 19) | She feels the flame on day three; on the last night she hears the watch-fire song from your camp (16.7); she does not let herself believe | She feels a flame she has only felt once, in herself; she sees a child of the nurseries she swore to protect; her own son died in a nursery |
| Why the sensei suspects you (Ch 14) | Your flame is `fallen_parent`'s flame: the leaning campfire on their old missions. They suspect *what* you are | They suspect *who* you are; the persimmon detail (Ch 21) is a blow |
| The persimmon on the sill (Ch 27) | The second left it, having learned where you live | The sensei left it on the first day of the persimmon season (their teammate's favourite), as they leave a dried one, kept from the autumn before, at the memorial stone on the ambush's anniversary (Ch 21.3; the stone ritual happens in both saves) |
| The hint (Chunin, Ch 25) | The librarian or keeper names the charm and the song: someone has the other half; it is your parent's | Same |
| The reveal (Road to Hokage, Ch 48) | The second defects (Ch 48), comes to the persimmon house's ruins, and shows her half. The halves fit. She tells you first that the map in Ch 0 was hers. "I sang you that song. I didn't know you'd keep it. He told me you burned with the house." (her lines: ARCS/7 Ch 48, "The heart of it") | The Seventh (the sensei; why now: sensei.md, `twist.lineage = fallen`) takes you to the persimmon house's ruins and gives you the box: the forehead protector, the half charm. "I carried you over a ravine and didn't know. Then I suspected, and the report said "lost", and I was afraid to be wrong, so I never opened the box again." The sensei never saw your half before Ch 48 (it stays sewn in your sleeve) |
| Who carries the succession | The second's choice in the finale (she shields you); the Seventh names you successor as a teacher | The Seventh names you successor as the child of their teammate; the succession speech carries `fallen_parent`'s name |

### Fairness

- Every clue appears in both saves (the song, the charm, the sparing, the suspicion, the persimmon).
  In each save the explanations that point the wrong way stay true (the second really did lose a
  child; the sensei really did lose a teammate with the same flame).
- **Identical before Ch 48 in both lineages:** the sealed Ash Road report the player reads at
  Ch 37.0 lists `fallen_parent`'s spouse and child as "lost"; the Sixth hands the report to the
  sensei; the keeper gives the player a long look as he says the Ash Road Jonin's name. No one
  comments on the child before Ch 48. `twist.lineage` is read only at Ch 27 (the persimmon, no
  visible giver) and from Ch 48.
- **The second's defection.** A: she finds "Nine: her child. Keep from her." in the leader's records (what sent her there: her file, A track step 6).
  B: after the Valley of Ash rescue (Ch 35) she goes to the emptied caves herself; the hearth's
  day-book left there names the nursery where her son died, and she goes into the leader's notes
  looking for him.
- The decisive evidence (the matching half charm) is held back to the reveal in both. The story
  never lies to the player: the second never claims to be or not be the parent before Ch 48; the
  sensei never says "your parent" before Ch 48.

### What changes downstream

Nothing in this table takes effect before Ch 48 (the reveal-gate rule).

| | A | B |
|---|---|---|
| The second's fate scene (Ch 52 to 54) | She shields you as a mother; if she lives, the epilogue has her in the restored clan's hall | She shields you as a debt to her own son; if she lives, she keeps the old shrine |
| The sensei's guilt (spoken from Ch 48) | About their teammate, and about not seeing the flame | About the teammate *and* their child (you) |
| The memorial (Ch 41) | Identical in both lineages: 41.1 reads only `ans.sensei.fallen_name` (unset: both side by side) | The same. The lineage gives the name's place a second meaning only from Ch 48, in the Ch 55 speech ([fallen_parent.md](CHARACTERS/fallen_parent.md)) |
| The restored clan's head of house | You, with the second as elder if she lives | You |

---

## 3. `twist.fourth_fate`: what the finals cost the Fourth

| | **Falls** | **Crippled and abdicates** | **Taken** |
|---|---|---|---|
| Ch 19 | The attack begins at the opening lantern-lighting. He is in the stands, carrying Academy children down the east stair, when the leader strikes him there; he falls on the stair (the cinematic cutaway: his grandson's face, the smoke closing) | Hit in the same place by the leader's dark mirror, which tears half his chakra; he lives | Hit in the same place by a binding seal and carried off through the smoke by the leader's hearth; you see ash-violet scarves lift him over the wall |
| Ch 20 | An **Akimichi farewell feast**: the whole village eats his favourite dish in the street, his bowl set at an empty place; his grandson (`squad3_b`) or his daughter quotes your Ch 1 answer (`ans.hokage_4.want`; unset: "He said you came here hungry. Eat."). The Fifth named | The hospital; he abdicates from his bed and names the Fifth himself ("She is hard. The Leaf needs hard for a while") | The empty seat: the council names the Fifth "until he returns" |
| Ch 21 (Chunin opening) | A year later; his statue's unveiling in the Academy yard; the stipend continues in his name | A year later; he teaches the Academy's history class from a wheelchair. He is your mentor in the Chunin arc (an advisor the player can visit) | A year later: intel finally places him in a Yūgure hold; the opening mission, **The Empty Seat**, brings him home, hollowed by the leader's experiments. He returns too weak to rule and becomes a mentor (as the crippled path) |
| What it teaches the player | Loss, and the will he left | The cost of the dark mirror, seen in a man you love | The dark mirror's purpose: the leader is practising |
| Later beats | Ch 55: as the Eighth you extend his stipend, in his name, to every child brought home from the nurseries and the war, and make it law | Ch 49.3: "I felt this at the stadium"; Ch 51a: he sits with the Academy children again; Ch 55: he is at your inauguration as you extend his stipend and make it law | Ch 49.3: "I've felt this before. In their hold"; Ch 51a: he warns the Seventh; Ch 55: at your inauguration as you extend his stipend and make it law |

In every save the Fifth is named in Ch 20 and `world.hokage = 5`.

---

## Rotation test matrix

`quests.py --check` (and the story review) must pass with every combination: 4 × 2 × 3 = **24**
saves. The combinations that need care:

| Combination | Watch for |
|---|---|
| Traitor = medic, fate = crippled or taken | The medic treats the Fourth; the medic's reveal scene must not need the Fourth healthy |
| Traitor = councillor, lineage = B | The councillor signed the Ash Road sealing. At Ch 39 he says only "I signed the Ash Road away too. A Jonin's death." (the same line in A); "your parent" waits for a visit after Ch 48 (his cell if arrested; after the war if turned) |
| Traitor = merchant, lineage = A | The merchant's note "Eat the persimmons first" (the slip) touches the persimmon motif; in A the persimmon on the sill comes from the second, not the merchant. Keep them on different days (Ch 25 and Ch 27). The innocent merchants' notes send persimmons too, so the fruit is no tell |
| Traitor = librarian | After her arrest the gift's old forms are taught from her notebook in the archive (the keeper, then the house; librarian.md). Before Ch 39 she trains the player only at 25.5 (if she came in 25.3), identically in every save |
