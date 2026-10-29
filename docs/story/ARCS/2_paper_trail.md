# Arc 2: Paper Trail (Genin, Ch 8 to 14, Beta 2)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**~8 h** (4 h authored, 4 h systemic: about 12 board D-ranks, 3 board C-ranks, training and the clan
lesson), about 24 in-game days. Child stage. Levels 5 to 15.

**What the arc is for.** Make the squad a family, and give the player's world a shape outside the
wall: roads, border villages, a word for the enemy. The mystery moves from "something is wrong" to
"someone is moving children and paper, and one of them knows what I am". The arc ends with the
first sight of the two shadows and a sensei who has started to look at the player differently.

---

## Ch 8: Three and a Bell (35 min)

*Teaches: squad commands, parry, teamwork.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 8.1 | Assignment | `instructor`, class | Squads read out: you, `teammate_a`, `teammate_b`, under the Jonin who carried you out of the hills. The rival is put with `classmate_c` and `classmate_d` under another Jonin and pretends not to care | plot, bond | — |
| 8.2 | The sensei | `sensei` | Training Ground 3 at dawn. The sensei is late on purpose, eats an apple, and says almost nothing: "Two bells. Three of you. Noon." | life | — |
| 8.3 | The test | `sensei`, the squad | You only pass if a teammate gets a bell too. Alone, it is impossible; together (squad commands: a feint, a trap, a timed rush), it is hard. As you and a teammate grab the bells together, a faint flame flickers between your hands; the sensei sees it and says nothing | plot, teach, seed (`story.seed.bell_flicker`), bond (`shared_moment bond.bells` with whoever grabs with you) | Who you grab with: the player picks the moment; whoever is beside you (the teammate you gave the command to). Giving away your own bell so both teammates pass is allowed (`ans.player.bell_given`): the sensei passes all three and remembers it |
| 8.4 | Lunch | `sensei` | The sensei shares their lunch and asks one question: "When I give an order you think is wrong, what will you do?" | bond | Obey and trust you / Ask why first / Do what's right and take the blame (`ans.sensei.orders`). Ch 24 (the order to fall back) and the Seventh's speech (Ch 42) read it |

---

## Ch 9: Small Jobs (15 min)

*Teaches: board missions, mission pay, failure on death.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 9.1 | The Mission Desk | `sensei`, a desk Chunin | The board opens. The first D-rank: a grocer's goat that eats laundry has escaped into the market | teach, life | — |
| 9.2 | The goat | squad | A comic chase; `teammate_b`'s pup makes it worse | life, bond (`mission_together`) | — |

After Ch 9 the board, `Dogs and Bugs` and the market's price war open (second side wave).

---

## Ch 10: Climbing Trees (25 min)

*Teaches: tree walking, wall-running, chakra jump, roof hopping.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 10.1 | Tree walking | `sensei`, squad | Climb a tree with chakra feet; mark your height with a kunai. Each teammate's struggle shows who they are (a careful climber, a reckless one) | teach | — |
| 10.2 | The stone | `sensei` | Evening, the memorial stone. The sensei stands at one name, just beside a long chiselled gap where names were cut away | seed (`story.seed.chiselled_names`, `story.seed.fallen_name`) | Ask about the gap / ask about the name / stand with them in silence (`ans.sensei.stone`). Gap: "Names someone decided to forget." Name: "A teammate. The best of us." Silence: they say, after a while, "Thank you," and you gain trust (`stood_by_them`) |

---

## Ch 11: Paper Trail (45 min)

*Teaches: escort, defeat, inspect, camping, bond.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 11.1 | The merchant | `merchant` | The first story C-rank: escort a cheerful, talkative merchant east. They keep a delivery book of every stop, in their own shorthand (`E3 · two · bright`, with a tailed tick), and show it off | seed (source notation), life | — |
| 11.2 | Bandits | squad | Bandits on the road; one of them, a smuggler, escapes wounded | teach | — |
| 11.3 | The false floor | squad, `merchant` | A broken axle shows a false floor full of chakra paper. When you pick up a sheet it chars faintly ash-violet at the edges; your teammates' sheets do not. The merchant swears they did not know | clue (`story.clue.merchant.1`), seed (`story.seed.cargo_found`, `story.seed.paper_chars`) | Hide the charred sheet / show the sensei / show a teammate (`ans.player.paper`). Showing the sensei: sensei trust +, and their suspicion (Ch 14) comes a scene earlier |
| 11.4 | The campfire | `teammate_a` (needs `friendship [teammate_a, 5]`) | On watch, teammate_a confesses they are afraid of being invisible: everyone looks past them. Then they ask you | bond (`shared_moment bond.teammate_a.campfire`, `heart_to_heart`) | "What are *you* afraid of?" Being taken again / Being alone / Being nobody / Fire (`ans.teammate_a.your_fear`). teammate_a remembers; in Ch 24 their line, falling, answers it ("You won't be alone. I'm right—") |
| 11.5 | Report | `sensei` | The sensei asks for the report and then: "Anything else?" | bond | Tell about the charred paper / don't (if not already shown) |

---

## Ch 12: Still Water (30 min)

*Teaches: water-walking, natures, the first elemental jutsu, the clan technique, the scroll shop.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 12.1 | The lake | `sensei`, squad | Water walking; teammate_b falls in eleven times | teach, life | — |
| 12.2 | The ceremony | a nature master | Chakra paper again (ordinary paper): your first nature is chosen. The master notes, puzzled, that your paper "warmed" before it showed your nature | teach, seed | Choose your first nature |
| 12.3 | The clan lesson | your clan's elder, or a friendly clan's teacher | A clan-born player's homecoming: kin you never met, and the clan's first technique. A clanless player learns a lesser technique from the clan of their closest classmate's family | teach, bond | — |

After Ch 12: Lanterns on the Lake, the hospital night shift, the clan welcomes (wave 1), the council
day (third side wave).

---

## Ch 13: The Empty Bed (45 min)

*Teaches: travel, investigation, ninken tracking.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 13.1 | The border village | squad, a village head, a foster mother | The first far region. An orphan boy has vanished from his bed; the window was opened from outside. His bed smells of soot | plot, teach | — |
| 13.2 | The trail | squad, a ninken (yours or teammate_b's pup) | Tracking across the hills to an abandoned waystation on the Ash Road with a sinking sun scratched on its gate. The sensei goes very quiet here and touches their scar | plot, seed (`story.seed.ash_road`) | Ask the sensei what happened here / don't (`ans.sensei.ash_road`). Asking: "A long time ago, I lost someone here." No more |
| 13.3 | Too late | squad | Inside: a child's sandal, warm ashes, chakra paper scraps. The boy is gone (he is found in the Valley of Ash nursery in Ch 35, alive) | plot | — |
| 13.4 | The stranger | `teammate_b`, a stranger in a traveller's hat (`yugure_second`, unrecognised) | Back home, on the old bridge at dusk, a stranger stops teammate_b: "I knew your parent. They're alive. Come alone in three days, and I'll tell you where." You see it from the bridge's end, or teammate_b tells you that night (if `friendship [teammate_b, 4]`) | plot, seed (`story.seed.teammate_approached`) | **Tell the sensei** / **keep the secret** / **go with them** (`story.seed.teammate_approached`: told, kept, followed). Bond data as in the bible's bond table. Go: on the night, the stranger sees two of you, does not come out, and leaves a note in the bridge rail: "Next time, alone." teammate_b keeps the note |

---

## Ch 14: Two Shadows (50 min)

*Teaches: two-man cell enemies, smoke and paper bombs.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 14.1 | East again | `merchant`, squad | The merchant hires the squad again, and this time slows them down: a lame horse that isn't lame, a forgotten bag, a long lunch | clue (`story.clue.merchant.2`) | Push them on / let them set the pace (no effect on the bound answer; a pushed merchant later says "you were right to hurry") |
| 14.2 | The shadows | `yugure_second`, `yugure_blade` (cloaked), a smuggler | At the river crossing, two figures in ash-violet cloaks with a sinking sun slip across the water ahead of you. The swordsman cuts the rope bridge behind them with one stroke that leaves an ink-dark line in the air. Their smuggler is left behind | plot, seed (`story.ch14.done`) | — |
| 14.3 | The smuggler | squad | Smoke and paper bombs; you capture the smuggler. He says one word, as if it should frighten you: **"Yūgure."** In his coat, a travel pass sealed with a pine-sprig seal | plot, clue (`story.clue.councillor.2`) | — |
| 14.4 | The suspicion | `sensei` | That night the sensei finds you alone. They have seen paper char near you twice now. "Where were you born?" | seed (`story.seed.sensei_knows`), bond | The truth as you know it: a house with a tree, then the camps / "I don't know" / "Why does it matter?" (`ans.sensei.born`). If you mention the tree, the sensei asks "What kind of tree?" and you can say persimmon (sets `story.lineage.persimmon_told`): in lineage B it lands hard (Ch 21 calls it back) |
| 14.5 | The recommendation | `sensei` | Back at the Desk, the sensei recommends the squad for the Chunin Exams. To you, privately: "Keep your fire low until you need it." | plot (`story.ch14.recommended`) | — |
| 14.6 | Squad dinner | squad, `sensei` | The barbecue house: the sensei pays, under protest; teammate_b eats everything | bond (`meal_together` with all; `shared_moment bond.squad_dinner`) | — |

---

## Beta 2 bond quests (two per teammate)

| Quest | Who | Beat | Question | Pays off |
|---|---|---|---|---|
| `bond.b2.teammate_a.1` | teammate_a (level 4) | A painting they were proud of is laughed at by older Genin; help them hang it anyway at the tea house | "Is it brave to let people see what you made, or just foolish?" (`ans.teammate_a.show`: brave, foolish, both) | Ch 41: they unveil the memorial mural in public, or ask *you* to unveil it (foolish) |
| `bond.b2.teammate_a.2` | teammate_a (level 5) | Their family wants them to give up painting for genjutsu; they paint a genjutsu instead, with you inside it | "If your family wanted you to be someone else, would you?" (`ans.teammate_a.family`) | Their Chunin-arc choice to join the sensor corps or not (Ch 30) |
| `bond.b2.teammate_b.1` | teammate_b (level 4) | The pup is sick; carry it to the Inuzuka clinic at night | "Do you think I'd be a good parent? I mean someday. Better than mine?" (`ans.teammate_b.parent_good`) | Ch 51: when b faces their parent |
| `bond.b2.teammate_b.2` | teammate_b (level 5) | A rooftop race to the Rock's top; at the top they show you their parent's old forehead protector | "If you could ask them one thing, what would it be?" (`ans.teammate_b.ask`: why, are you sorry, do you remember me) | Ch 51: the question b asks their parent is yours |
