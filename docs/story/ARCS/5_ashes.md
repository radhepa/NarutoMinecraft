# Arc 5: Ashes (Jonin, Ch 33 to 45, later)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**~17 h** main path: about 8.6 h authored over 13 chapters (515 min) and about 8.4 h systemic
main-path play: A-rank cell hunts (~4 h), D- and C-ranks leading your own Genin team (~2.5 h), the
third-nature trial (~1 h) and training (~1 h). Side quests (clan lines' Heart steps and the rest)
and romance to marriage sit outside the main-path hours, as ROADMAP §1 counts them. Opens with the
second time skip: **four years later** (Y+6), the player is 18 and an adult (1.0 scale). The arc
runs about a year of story time (to Y+7). Levels 30 to 42. The optional ANBU branch
([6_night_watch.md](6_night_watch.md)) opens at level 35 after Ch 39; its middle (N3 on) waits for
Ch 44.

**Where the systemic play sits.** A-rank hunts and Genin missions fill the gaps between Ch 34 and
35, Ch 37 and 38 (so Ch 36 to 41 is not one unbroken run of reveals), and Ch 42 and 44.

**What the arc is for.** The truth comes out, and the player is the one who must say it aloud. The
village's founding crime, the voice inside, the names under the chisel. The player becomes a
teacher (their own Genin), a witness (the archive), a detective (the case board) and a judge
(the accusation). The arc ends with the Leaf having faced itself, a new memorial, a new Hokage who
is the player's own sensei, and a warning that Yūgure wants something worse than the creed.

---

## Ch 33: The Trial (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 33.1 | Four years | Player, squad | Adult now, 18. Montage vignettes of the class grown up: the squad as Chunin captains, the rival's rise, `squad3_b` running his mother's grill on rest days, `squad5_a` campaigning (cheerfully, uninvited) to be the next Hokage, `squad5_c` gone into the ANBU, `squad4_b` finally a Chunin, a wedding or two in the village | plot (`time_skip`) | — |
| 33.2 | The bout | `rival`, two examiners | The Jonin trial bout: you and the rival as a pair against two examiners. The rival hates needing you and fights better beside you than anyone | teach, bond | — |
| 33.3 | The review | `hokage_6`, the council | The council review. The `elder_hyuga` asks about "the rumour of your blood" (Ch 31 was seen by half a quarter), and reads back how you testified at the Tobari council (`ans.player.testify`: for the Tobari → "You spoke for a quarter against a Hokage"; against the lockdown → "You spoke against a lawful order"; for the Fifth's right to fear → "You granted her fear and still opposed her"; unset → "You testified, I am told"). The Sixth stops him. Then asks you, gently, one question | plot, bond | "What is a Hokage for?" To protect the village / To protect the people the village forgets / To carry what no one else should (`ans.hokage_6.for`). The Sixth's resignation (Ch 42) answers it |
| 33.4 | Jonin | squad, `sensei` | Promotion. The sensei gives you their old Jonin vest's spare patch | plot (`promote jonin`), bond | — |

---

## Ch 34: Three Small Shadows (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 34.1 | Your team | `genin_1`, `genin_2`, `genin_3` | You are given three Genin (rolled). If you freed the boy in the third cell (Ch 0), `genin_1` is him, grown: "You don't remember me. You opened my door" | plot, bond | — |
| 34.2 | Your test | the Genin | Design their test: the bells on one cord (as your sensei did) / a test of your own (a choice of three: a rescue drill, a stolen scroll, a night watch) (`ans.player.own_test`). Your sensei watches from a tree, eating an apple. If you once gave your own bell away (`ans.player.bell_given`), the sensei tells your Genin the story before the test: "Your teacher once handed theirs away. Don't expect the same from them." Each test choice opens a different first bond quest for the Genin (`bond.j.genin.<own_test>`) | teach, bond | — |
| 34.3 | The flicker | `genin_3` | In the test, `genin_3`'s chakra flickers warm when they help a teammate. A sealed flame, faint. A descendant | seed (`story.seed.genin_flame`) | Tell them / watch over them quietly / report it to the sensor corps (`ans.player.genin_flame`). Reporting it: the Sixth thanks you and does nothing; the genin hears of it and trusts you less |

Your Genin team is a systemic companion group for the rest of the game (D- and C-ranks you lead,
small bond quests; see [SYSTEMS.md](../SYSTEMS.md)).

---

## Ch 35: Far Fires (50 min)

*A story A-rank in the Valley of Ash.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 35.1 | The valley | squad (your old one, as Jonin), the sensei, the trio (`squad3_a`, `squad3_b`, `squad3_c`), `squad4_b` (lent for his nose) | The Valley of Ash: grey grass, old armour, nothing grows above knee height. "They say both armies just lay down here," the sensei says | plot, seed (the Valley's story, told in Ch 36) | — |
| 35.2 | The nursery | a Yūgure nursery in the caves; `squad3_a`, `squad4_b` | `squad4_b` and his ninken smell out the caves' back entrance; `squad3_a`'s plan gets every child out before the hearth wakes, without a fight if you follow it (a fight if you don't). Children in numbered cells. Among them, the boy from the empty bed (Ch 13), seven years older, who remembers your squad's voices outside the waystation | plot, bond | Follow squad3_a's plan / go loud (the fight is the same hearth either way) |
| 35.3 | The list | the hearth's leader | In the hearth leader's chest, Yūgure's list: years of children, all in one hand, in cipher | clue (`story.clue.list_found`) | — |
| 35.4 | Home | the children | Leading twenty children home along the Ash Road; a night at camp where they ask you what the Leaf is like | bond, life | How you describe the Leaf: a place that feeds you / a place that's trying / a place you choose (`ans.player.leaf_is`). One of them repeats it at the memorial (Ch 41) |

---

## Ch 36: The Keeper's Door (45 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 36.1 | The door | `elder_keeper`, `hokage_6`, `sensei_5` | If `bond_meter [elder_keeper, trust, 60]` and `friendship [elder_keeper, 6]`: the keeper comes for you at night himself: "I said I would show you a door." Else the Sixth orders the archive opened after Ch 35's list, and the keeper obeys like a man going to his execution | plot, bond | — |
| 36.2 | The archive | the keeper, the Sixth | `sensei_5` and the keeper break the door's old seals together (the `clan.uzumaki.3` expert helps if present). Under the Rock: shelves, sealed boxes, and in the centre a stone watch-fire basket holding an ember that has burned for a century: **the Hearthstone**. It leans toward you | plot | — |
| 36.3 | The charter | the keeper | The founding charter's fourth clause: the Kagari invited as a founding clan, in the First's hand | plot | — |
| 36.4 | The order | the keeper | The Second's order for the Quiet Ending, and the report it rested on. The keeper: "It was forged. I've known for forty years" | plot | — |
| 36.5 | The Valley | the keeper | What happened in the Valley of Ash: one Kagari's dark mirror, and a whole clan blamed | plot, teach (the dark mirror, named) | — |
| 36.6 | The letter | the keeper, the Sixth, Player | The last box: the Third's letter. The keeper hands it to you to read aloud, standing at the Hearthstone: "For whoever comes asking. We ended a clan for a peace we could have kept with them. I kept quiet for thirty years and called it wisdom. It was not. If you are reading this, say it for me." The chapter ends on the silence after it | plot | — |

---

## Ch 37: Names (45 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 37.0 | The Ash Road | the keeper, the `sensei`, `sensei_3` | The next night, its own scene: the sealed report of the Ash Road ambush. Yūgure, not bandits, after `fallen_parent`'s blood. The keeper's signature and the councillor's; the sensei's own field report, rewritten above their name. The sensei reads it standing up and walks out without a word. `sensei_3` stays, reads it twice, and says the thing she has never said: "They sent me back so I'd live. I've been angry at them for fourteen years for it" | plot, bond | Follow the sensei / stay with the keeper and `sensei_3` (`ans.player.archive_follow`). Following: the sensei on the Rock, the first time you see them cry; staying: the keeper tells you why he kept silent ("Because she asked me to. And because I was afraid"), and `sensei_3` goes up the Rock after the sensei herself |
| 37.1 | Twenty-seven | the keeper | The renaming list: twenty-seven children, their old names and new families. The keeper traces three lines for you: the `librarian`'s grandmother; `fallen_parent`'s grandmother; and one who left the Leaf for a border town two generations ago (the `yugure_second`'s line) | plot | — |
| 37.2 | Everyone | Player | The realisation: the Kagari never ended. They were scattered through the Leaf. Your genin_3 is on the list's branches | plot | — |
| 37.3 | The blade | `yugure_blade` | That night the swordsman breaks into the archive (word that it would be open had gone round the Sixth's clerk's errands, to the hospital, the library, the council and the gate; the voice passed it on): he wants the Hearthstone. Duel three, among the shelves; you must protect the basket while he cuts ink into the air. He retreats wounded, without it | plot, teach | Let him go when he's beaten / try to capture him (he escapes either way; capture attempt shows his honour: he warns you of a trap) (`ans.yugure_blade.archive`) |
| 37.4 | Who knew | the keeper | "Only a few people were meant to know the archive would be open." (The keeper, the Sixth, you, and the places the Sixth's clerk ran errands to: the hospital, the library, the council, the gate. Every candidate had a route; a dead end that points only at "someone inside") | clue | — |

---

## Ch 38: The Case Board (40 min)

The detective chapter. Pace: the player's own.

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 38.1 | The board | Player, `sensei_4` | The case board (journal page and pinboard furniture) collects every clue, slip and alibi so far. `sensei_4` sits with you through it: he asks good questions ("What would they have to know to write that?") and never gives an answer | teach | — |
| 38.2 | Decoding | the keeper | With the porter's words ("in its own hand"), the cipher breaks: the list is indexed in one notation and one hand across years | clue | — |
| 38.3 | Matching | Player | Compare the list with the documents in the journal (`journal.documents`): the green-ink intake slip from Ch 0, the S-114 papers from Ch 1, the shelving slip from Ch 5, the delivery-book page from Ch 11 | clue | — |
| 38.4 | Alibis | Player, witnesses | Check any alibis not yet checked (the shrine book; the surgery roster, kept by `squad4_c`; the court roll; the carpenter's shop) | clue | — |
| 38.5 | The slip | Player | The journal recalls the Ch 25 hospital lines if `story.clue.slip.heard`, pinned beside the Ch 0 memory card "Nine. Up." `sensei_4` on Thread Sight: "A flicker isn't proof. I hide bread from my squad." | clue | — |
| 38.6 | Decide | Player | Accuse with proof (two of three), or accuse without | plot | Who (`story.accused = <candidate>`) |

---

## Ch 39: The Voice (45 min)

The reveal ([ROTATIONS.md](../ROTATIONS.md) §1: the four scenes, the accusation table).

| # | Scene | What happens |
|---|---|---|
| 39.1 | The confrontation | The bound candidate's scene (library at night, hospital roof at dawn, the councillor's study, the cart in the rain) |
| 39.2 | The choice | Arrest or turn (turning needs `friendship [bound, 4]` or the candidate's own wish) (`story.traitor.fate`: arrested, turned) |
| 39.3 | The arrest | `sensei_4` makes the arrest in every outcome but turning; the village sees a Morino take a respected person away, and for once nobody whispers about his clan |
| 39b | The chase (if accused without proof, or an innocent was accused) | The voice tries to steal the archive key at night; a chase to the east gate; arrested |
| 39c | Why you (if `friendship [bound, 7]`) | The candidate answers the question they once asked you, in light of what they did |

---

## Ch 40: Daylight (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 40.1 | Before the council | `hokage_6`, Player | The Sixth asks you how much to say | bond | Everything / Everything but the renamed families' names / Let each family decide whether to be named (`ans.hokage_6.names`; table below) |
| 40.2 | The council | the clan heads, the village | The Sixth makes the Quiet Ending public, with you as witness. The Senju head bows to the floor; the Uchiha head protests that a dead elder's forgery is not his clan's crime; the elder_hyuga walks out, and his grand-niece `squad4_a` does not follow him; `squad5_a`, whose clan's Hokage kept the silence for thirty years, stands up in the gallery and sits down again without a word | plot, mood (`mood_event village grieving`) | Your testimony: for the dead / for the living descendants / against the silence (`ans.player.council_testimony`) |
| 40.2b | Faith | `squad5_a` | That night, on the Rock under the Third's face, `squad5_a` asks you the question he can't ask anyone in his family | bond | "Does it still count, the Will of Fire, if the one who taught it to us kept this quiet?" It counts more now / It never counted / It counts if we say it out loud (`ans.squad5_a.will`). He stands with the Seventh in Ch 42 either way; the answer is his speech when he becomes your Commander (Ch 55) |
| 40.3 | The cleared | the innocent candidates | Each cleared candidate's scene (ROTATIONS §1) | bond | — |
| 40.4 | The village | residents | A side-quest wave: families learning their roots (`side.j.roots`, shaped by `ans.hokage_6.names` and `ans.player.council_testimony`), old friends quarrelling over blame, a Kurama painter bringing out a hidden painting of the shrine (`clan.kurama.3`) | life, systems | — |

**What `ans.hokage_6.names` decides:**

| Answer | How descendants learn | Ch 46.3: who comes to the shrine | `side.j.roots` wave |
|---|---|---|---|
| Everything (or unset) | The list is read at the council; every family learns at once | Many, some angry; two families refuse to be named and leave the village quarter for a season | Large and loud: quarrels over blame, two estrangement hooks |
| Everything but the names | The families are told privately by the archive | Few at first; more each in-game week | Small and private: one family at a time asks the archive |
| Let each family decide | Each family is asked; some say no | The willing only, and they come proud | Medium: the families who said yes host a gathering |

**What `ans.player.council_testimony` decides:** the dedication carved on the memorial stone in Ch
41 ("For the dead" / "For the living, who carry them" / "So that it is said"; unset: "For the
Kagari"), and the first family who comes to the archive in `side.j.roots` (a family of the dead, a
living descendant, or an old Leaf family who kept silent).

---

## Ch 41: The Memorial (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 41.1 | Re-carving | `classmate_c`, the village | The chiselled gap on the memorial stone is re-carved with the Kagari dead's names and a dedication chosen by your council testimony; `fallen_parent`'s name is moved beside them. classmate_c's family does the carving | plot | — |
| 41.2 | The mural | `teammate_a` | teammate_a's mural beside the stone, painted from your answer in Beta 1 (`ans.teammate_a.paint`) and unveiled by them or by you (`ans.teammate_a.show`) | bond (`supported_dream` if you helped) | — |
| 41.3 | The children | the Valley children | One of the rescued children repeats what you told them the Leaf is (`ans.player.leaf_is`) | bond | — |
| 41.4 | At night | `yugure_second` | At the stone at night, a woman in plain road clothes traces a name (her line's). The second. No fight. The first real conversation | plot, bond | She asks: "What will you do with that fire when they come for it?" Give it / Keep it / Share it, the way it's meant (`ans.yugure_second.fire`). She says: "He says the Bonfire will free everyone. Lately I wonder what it needs to burn." (`story.seed.second_doubts`) |

---

## Ch 42: The Sixth's Last Order (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 42.1 | Resignation | `hokage_6` | The Sixth resigns to take responsibility for the Leaf's buried crime: "A Hokage is for..." (answers `ans.hokage_6.for`) | plot | — |
| 42.2 | The Seventh | `sensei`, the council, `squad5_a`, `sensei_2`, the village | The council balks: the sensei's own field report of the Ash Road was rewritten above their name and they signed it; the `elder_hyuga` says a Hokage who signed a lie cannot ask the village to tell the truth. `sensei_2` kneels first. Then `squad5_a`, the Sarutobi heir whose clan's Hokage kept the silence, stands up in the gallery: "I'm with them. Because they're the one who'll say it was wrong." The vote carries. New Year: the sensei is named Seventh Hokage. Their speech quotes your Ch 8 answer about wrong orders (`ans.sensei.orders`; unset: "One of my students once told me nothing at all, and did the right thing anyway") and, if you once gave your own bell away (`ans.player.bell_given`), "and one of them once gave away their bell" | plot (`set_hokage 7`, `carve_face 6`), bond | — |
| 42.3 | The face | the Rock | The Seventh's face begins to be carved. The instructor's Ch 5 question is called back (`ans.instructor.face`) | bond | — |

---

## Ch 43: The Rival's Door (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 43.1 | The ceremony | `rival`, their family | The rival's clan (or family) ceremony honouring their promotion. No one in their family came to their Academy graduation; they ask you to stand with them now, without saying why | bond | Go / don't (going: `stood_by_them`, a permanent moment if friendship 6) |
| 43.2 | After | `rival` | On the roof after: "Why did you come?" | bond | Because you'd have come for me / Because I wanted to / Because you asked (`ans.rival.why_came`). Ch 53 |

---

## Ch 44: Hollow Echo (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 44.1 | Reports | the Seventh | Yūgure hearths found emptied in the hills: someone pale is hunting them | plot | — |
| 44.2 | Her | `lost_child`, `squad3_c`, your Genin | On an A-rank with your Genin (and `squad3_c`, lent to you as a sensor), she appears. She could kill the Genin; she stops when genin_3's flame flickers, and when she sees the cord. `squad3_c` hears what's in her: "There are a dozen people in there. She's at the bottom." "Too many voices in here," she says, touching her chest. "One of them is yours." | plot, seed (`story.seed.lost_child_breaking`) | — |
| 44.3 | His voice | `lost_child` | Before she goes, her flat voice changes to a gentle one that is not hers, and carries one sentence from the leader: **"Grow, little flame. I like your friends."** Then she is herself again, frightened of it | plot (the leader on screen through her) | — |
| 44.4 | The second hunter | `squad5_c` | A masked ANBU arrives with orders to take her alive: `squad5_c`. She is gone before either of you reaches her. He will not say whose orders | plot, seed | Follow her / stay with the Genin (`ans.lost_child.echo`). Following: she leaves a strip of ash-violet scarf tied to a branch, pointing toward the Shimura house: the Night Watch's lead into its middle chapters (N3) |

---

## Ch 45: The Road Opens (30 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 45.1 | Level 42 | the Seventh | The Seventh asks you to stand at their side: "Whatever's coming, I'd like you where I can see you." The road to Hokage opens | plot | — |
| 45.2 | The squad | squad | Ichiraku. The cook sets down your order without asking, as for seven years | bond, life | — |

---

## Romance and marriage (systemic, with story beats)

From the teen stage (Ch 21) any eligible bond can date at level 7 and confess at level 8; marriage
needs adults and level 10 (BONDS.md §10). Story beats that read it:

- **The squad and romance.** If you date a teammate, the other teammate gets a scene (`jealous` or a
  blessing, by personality) in the next squad dinner.
- **The wedding** at the shrine is an event chapter (`event.wedding.player`) whenever it happens; the
  squad, the sensei (as Hokage, if after Ch 42) and anyone at level 6+ attend.
- **The finale reads it.** A spouse is the strongest flame in Ch 53; their line comes first.
