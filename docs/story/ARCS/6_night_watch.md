# Arc 6 (optional): Night Watch (ANBU branch, N1 to N7)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**+~8 h**: about 4.7 h authored over 7 chapters (280 min) and about 3.3 h systemic (covert and
S-rank missions, the mask's night operations).

**When it plays.**

| Part | Gate |
|---|---|
| N1 to N2 (the invitation, covert work) | Level 35 and `story.ch39.done` (the voice's case is closed, so the Undercroft's knowledge of "Nine" can never be mistaken for evidence), no bad deed in the last season (ROADMAP §11) |
| N3 onward (the quarry) | `story.ch44.done` (the lost child has been seen hunting in Ch 44), and one of four ways in: the ash-violet strip from Ch 44 (if you followed her), the N2.3 courier letters (if you kept one), `clan.shimura.3` (the mail drop), or the ANBU captain's order to look into the letters, given after Ch 44 (always available) |
| Ch 47 | Waits until the branch is finished or declined. At the Ch 46 registry a prompt asks whether to finish the night work first or go on. Going on closes the branch through the Ch 47 path: the Undercroft's orders reach the shrine instead (`squad5_c` at the shrine) |
| After Ch 47 | Once `story.ch47.done` is set, the branch is never offered again |

A player can return to regular duty at any time. A player turned down for the invitation (a bad
deed) still meets the Undercroft's story through Ch 47.

**What the arc is for.** The Leaf's shadow: the people who learned nothing from the archive,
because they never needed the truth told, only the gift caged. It is the best path to bring the
lost child home, and it tests the player's answer to the Kagari's oldest temptation from the
other side: not taking chakra, but letting someone else use you to take it.

**The Undercroft.** The heirs of the **sealing team that sealed the twenty-seven** in the Quiet
Ending: a mixed-clan oath society of old ANBU and sealers, sworn in as children by their parents
and grandparents, who never stopped believing the gift must be sealed and used. They meet in the
sealing team's own derelict **sealing hall under the old quarry**, sealed off since the Quiet
Ending. The Shimura have no part in it; a Shimura is among those who expose it (`clan.shimura.3`:
a stranger has been using a Shimura cellar as a mail drop for sealed letters).
They are led by `undercroft_head`, the sealing team leader's granddaughter (no clan; an ordinary
family name), a former ANBU commander. Their belief: the Leaf's mistake was not sealing the Kagari
but failing to keep the gift for itself. They want it caged and aimed at Yūgure. They have been
watching the player since Ch 31.

---

## N1: The Mask (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| N1.1 | The invitation | an ANBU captain (`anbu_captain`), the Seventh or Sixth | A masked visitor at your window at 2 a.m. The night infiltration test: reach the Hokage's desk unseen | teach | Accept / decline (declining closes the branch until re-offered next season) |
| N1.2 | The mask | `anbu_captain` | Choose a mask (an animal from a set); residents no longer recognise you while you wear it | teach | The mask (cosmetic) |

## N2: Covert (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| N2.1 | The rule of the mask | `anbu_captain` | On the wall at midnight: "Out here you have no name. Come home with it." | teach | — |
| N2.2 | The raid | ANBU squad, `squad5_c` | A night raid on a Yūgure hearth in the hills (stealth, detection by sight and sound). Among the masks is one that counts coins under its breath: `squad5_c`, who says nothing to you | teach, plot | Take the hearth silently / loud (stealth record) |
| N2.3 | The courier | a courier | A courier intercepted on the ridge carries sealed letters with no Yūgure mark: a strange seal, old and Leaf-made | plot, seed (the Undercroft) | Report the letters to the captain / keep one (`ans.anbu_captain.letter`) |

## N3: The Cellar (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| N3.1 | The way in | Shimura clan members, `anbu_captain` | By whichever way opened it: the ash-violet strip from Ch 44 points to the old quarry; the kept courier letters and the captain's order lead to a Shimura cellar used as a mail drop (if `clan.shimura.3` is done, the Shimura you helped is waiting and shows you the drop; else you stake it out), and the courier who comes for the letters leads you to the old quarry | plot | — |
| N3.2 | The Undercroft | `undercroft_head`, old ANBU and sealers | Behind a sealed quarry face, the sealing team's derelict hall: old masks, older seals, the brushes that sealed twenty-seven children. The head greets you by your nursery number: "Nine. We have your reports too." (They intercepted Yūgure's mail for years; they never knew the voice) | plot | — |
| N3.3 | The offer | `undercroft_head` | "My grandmother sealed twenty-seven children so this village could sleep. The Leaf has decided to feel sorry about it. We are not sorry. We are prepared. Join us, and no child will be taken again." | bond | Listen (pretend) / refuse / walk out (`ans.undercroft_head.offer`). Refusing or walking out: they let you go, and take the lost child the same week (N4 still happens) |

## N4: Caged (45 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| N4.1 | Taken | the Undercroft, `lost_child` | News: the Undercroft has captured `lost_child` in the hills (whatever you answered in N3) | plot | — |
| N4.2 | The cell | `lost_child`, `squad5_c` | In a sealed cell in the quarry hall she sits with her stolen natures bound by the same kind of seal the sealing team once laid on the twenty-seven. You see her through the bars, as in Ch 0, but from the other side. She knows you by the cord. `squad5_c` guards the cell; he will not look at you | plot, bond | Speak to her through the bars / speak to `squad5_c` (`ans.squad5_c.free`, his file) |
| N4.3 | The jar | `undercroft_head` | The head shows you **the jar**: a sealed stone jar the sealing team made. The plan: make the girl its mouth, run the dark mirror backwards through her into Yūgure hearths, draining them into her and on into the jar. The Leaf's own Hollow Crown, in miniature | plot | — |

## N5: Orders (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| N5.1 | The order | `undercroft_head` | "Your gift can open her. Kindle her, and we will do the rest." | plot | **Pretend to obey** (`story.nightwatch.pretend`): you go in to "prepare" her; you have one night / **Refuse**: they lock you out |
| N5.2 | The fallback | `undercroft_head`, `genin_3` | If you refused and you reported genin_3's flicker (`ans.player.genin_flame = reported`), the Undercroft takes genin_3 as their fallback mouth for the jar; N6 starts as a rescue of both. Otherwise they will wait for you to break | plot | — |
| N5.3 | The night | `anbu_captain` | The ANBU captain finds you on the wall and says only: "Masks come off at home. Remember where yours is." (If you kept a letter in N2, they know.) | bond | Tell the captain everything / go alone (`ans.anbu_captain.alone`) |

## N6: Giving (50 min)

The heart of the branch. You free her; the Undercroft's old masks fight you through the hall (if
you told the ANBU captain everything, `ans.anbu_captain.alone = told`, masks of the Hokage's own hold
the quarry mouth and the fight is shorter; alone or unset, you fight it all). At
the deepest cell `squad5_c` is the last mask between you and her. You can fight him, or talk him
down: ask him "What did they promise you?" (`ans.squad5_c.offer`). Talked down, he opens the cell
himself and walks out of the Undercroft with you: **a betrayal, or not** (`story.squad5_c.stand =
stood_down`). Fought, he is beaten and leaves the ANBU (`fought`); he returns in Ch 51a at the
wall either way.

In the cell you do what the Kagari once did at watch-fires and what the dark mirror reversed: you
kindle her own flame back alive through the one grey thread along the cord, until the stolen embers
forced into her have nothing to hold on to and leave. It costs you: you collapse, chakra empty, for
a day.

She wakes as herself. Her first words are the ones she said through the bars in Ch 0, finished:
"Someone remembers I was here. You did." (Variants by `ans.lost_child.cell` in her file;
`story.lost_child.home = nightwatch`; her bond starts growing from 2.)

Afterwards, in the hospital, `squad4_c` finds that the last stolen embers in her still carry the
leader's voice (the one that spoke through her in Ch 44.3) and quiets them with a Suzuran herb
seal, one night at a time.

## N7: Daylight in the Cellar (30 min)

You bring the Undercroft to the Hokage. The head does not resist: "You will need us when he comes."
The choice of what to do with them (`story.nightwatch.undercroft`):

| Choice | What happens |
|---|---|
| **Disband them** (`disbanded`) | The old masks, the seals and the jar go to the ANBU vault, the quarry hall is sealed for good; the head is confined to her house (she appears in Ch 51a at the wall, fighting for the village anyway) |
| **Bring them under the Hokage** (`sworn`) | They become a legitimate night unit; in Ch 50 they find twelve array anchors no one else could (they know cinder seals: their grandparents' craft, turned inside out) |
| **Expose them publicly** (`exposed`) | The Shimura who found the mail drop testifies with you; the village's trust in the ANBU dips (a standing loss with `rank:anbu`); the head resigns |

If the branch is finished, Ch 47 becomes **Home Fires** (her recovery) instead of her rescue.
