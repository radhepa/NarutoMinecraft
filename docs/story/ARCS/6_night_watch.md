# Arc 6 (optional): Night Watch (ANBU branch, N1 to N7)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**+~8 h**: about 4.7 h authored over 7 chapters (280 min) and about 3.3 h systemic (covert and
S-rank missions, the mask's night operations).

**When it plays.**

| Part | Gate |
|---|---|
| N1 to N2 (the invitation, covert work) | Level 35 and `story.ch39.done` (the voice's case is closed, so the Undercroft's knowledge of "Nine" can never be mistaken for evidence), no bad deed in the last season (ROADMAP §11) |
| N3 onward (the cellar) | `story.ch44.done` (the lost child has been seen hunting in Ch 44) |
| Ch 47 | Waits until the branch is finished or declined. Entering Ch 47 with the branch half played (the player chose to move on at the registry) closes it through the Ch 47 path: the Undercroft's orders reach the shrine instead (squad5_c at the shrine) |

A player can return to regular duty at any time. A player turned down for the invitation (a bad
deed) still meets the Undercroft's story through Ch 47.

**What the arc is for.** The Leaf's shadow: the people who learned nothing from the archive,
because they never needed the truth told, only the gift caged. It is the best path to bring the
lost child home, and it tests the player's answer to the Kagari's oldest temptation from the
other side: not taking chakra, but letting someone else use you to take it.

**The Undercroft.** The heirs of the **sealing team that sealed the twenty-seven** in the Quiet
Ending: a mixed-clan oath society of old ANBU and sealers, sworn in as children by their parents
and grandparents, who never stopped believing the gift must be sealed and used. A Shimura elder
shelters them in the hall under the Shimura house, so the Shimura are complicit, not the faction.
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

Covert operations against Yūgure hearths in the hills: a night raid, a hearth's courier
intercepted. The ANBU captain teaches the rule of the mask: "Out here you have no name. Come home
with it." Among the masks on the raid is one that counts coins under its breath: `squad5_c`, who
says nothing to you.

## N3: The Cellar (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| N3.1 | The Shimura house | Shimura clan members | The ash-violet strip from Ch 44 and a courier's letter both lead to the Shimura house (if `clan.shimura.3` is done, a Shimura you helped opens the cellar door; else you break in) | plot | — |
| N3.2 | The Undercroft | `undercroft_head`, old ANBU and sealers | Under the cellar, a hall of old masks and older seals. The head greets you by your nursery number: "Nine. We have your reports too." (They intercepted Yūgure's mail for years; they never knew the voice) | plot | — |
| N3.3 | The offer | `undercroft_head` | "My grandmother sealed twenty-seven children so this village could sleep. The Leaf has decided to feel sorry about it. We are not sorry. We are prepared. Join us, and no child will be taken again." | bond | Listen (pretend) / refuse / walk out (`ans.undercroft_head.offer`). Refusing or walking out: they let you go, and take the lost child the same week (N4 still happens) |

## N4: Caged (45 min)

The Undercroft has captured `lost_child` in the hills. In a sealed cell under the Shimura house she
sits with her stolen natures bound by the same kind of seal the sealing team once laid on the
twenty-seven. Their plan: use her hollowness as a **vessel**: the dark mirror run backwards through
her into Yūgure hearths, draining them into her, and then into a sealed jar the Undercroft keeps.
The Leaf's own Hollow Crown, in miniature.

You see her through the bars, as in Ch 0, but from the other side. She knows you by the cord.
`squad5_c` guards the cell; he will not look at you.

## N5: Orders (40 min)

The head orders you to kindle the girl as the vessel's spark: "Your gift can open her. We will do
the rest." The choice:

| Choice | What happens |
|---|---|
| **Pretend to obey** (`story.nightwatch.pretend`) | You go in to "prepare" her; you have one night |
| **Refuse** | They lock you out and plan to use a sealed descendant instead (genin_3, if `story.seed.genin_flame`); you must break in (N6 starts as a rescue of both) |

## N6: Giving (50 min)

The heart of the branch. You free her; the Undercroft's old masks fight you through the hall. At
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
"So someone remembers I was here. You did." (Variants by `ans.lost_child.cell` in her file;
`story.lost_child.home = nightwatch`; her bond starts growing from 2.)

## N7: Daylight in the Cellar (30 min)

You bring the Undercroft to the Hokage. The head does not resist: "You will need us when he comes."
The choice of what to do with them (`story.nightwatch.undercroft`):

| Choice | What happens |
|---|---|
| **Disband them** (`disbanded`) | The old masks and seals go to the ANBU vault; the head is confined to her house (she appears in Ch 51a at the wall, fighting for the village anyway) |
| **Bring them under the Hokage** (`sworn`) | They become a legitimate night unit; in Ch 50 they find twelve array anchors no one else could (they know cinder seals: their grandparents' craft, turned inside out) |
| **Expose them publicly** (`exposed`) | The Shimura line's Heart step becomes a reckoning for the elder who sheltered them; the village's trust in the ANBU dips (a standing loss with `rank:anbu`); the head resigns |

If the branch is finished, Ch 47 becomes **Home Fires** (her recovery) instead of her rescue.
