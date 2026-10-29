# Arc 6 (optional): Night Watch (ANBU branch, N1 to N7)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**+~8 h** (about 4 h authored over 7 chapters, 4 h systemic: covert and S-rank missions, the mask's
night operations). Opens with the invitation at **level 35**, after Ch 38 (so the voice's case
is underway), any time before Ch 46. A player can return to regular duty at any time; the branch
can be finished during the Jonin arc or early in the Road to Hokage.

**What the arc is for.** The Leaf's shadow: the people who learned nothing from the archive,
because they never needed the truth told, only the gift caged. It is the best path to bring the
lost child home, and it tests the player's answer to the Kagari's oldest temptation from the
other side: not taking chakra, but letting someone else use you to take it.

**The Undercroft.** A hidden faction of retired ANBU under the Shimura house, led by
`undercroft_head` (an old Shimura woman, a former ANBU commander). Its belief: the Kagari gift is
the most dangerous weapon the Leaf ever buried, and the Leaf's mistake was destroying it instead of
keeping it. They want it caged and aimed at Yūgure. They have been watching the player since
Ch 31.

---

## N1: The Mask (35 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| N1.1 | The invitation | an ANBU captain (`anbu_captain`), the Seventh or Sixth | A masked visitor at your window at 2 a.m. The night infiltration test: reach the Hokage's desk unseen | teach | Accept / decline (declining closes the branch until re-offered next season) |
| N1.2 | The mask | `anbu_captain` | Choose a mask (an animal from a set); residents no longer recognise you while you wear it | teach | The mask (cosmetic) |

## N2: Covert (40 min)

Covert operations against Yūgure cells in the hills: a night raid, a cell's courier intercepted.
The ANBU captain teaches the rule of the mask: "Out here you have no name. Come home with it." A
captured courier carries a letter addressed to a cellar.

## N3: The Cellar (40 min)

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| N3.1 | The Shimura house | Shimura clan members | Follow the courier's letter to the Shimura house (if `clan.shimura.3` is done, a Shimura you helped opens the cellar door; else you break in) | plot | — |
| N3.2 | The Undercroft | `undercroft_head`, old ANBU | Under the cellar, a hall of old masks. The head greets you by your nursery number: "Nine. We have your reports too." (They intercepted Yūgure's mail for years; not the voice, but they knew of it) | plot | — |
| N3.3 | The offer | `undercroft_head` | "The Leaf burned the Kagari because it was afraid. We are not afraid. We are prepared. Join us, and no child will be taken again." | bond | Listen (pretend) / refuse / walk out (`ans.undercroft_head.offer`). Refusing or walking out: they let you go, and take the lost child the same week (N4 still happens) |

## N4: Caged (45 min)

The Undercroft has captured `lost_child` in the hills. In a sealed cell under the Shimura house
she sits with her stolen natures bound by seals. Their plan: use her hollowness as a **vessel**:
the dark mirror run backwards through her into Yūgure cells, draining them into her, and then
into a sealed jar the Undercroft keeps. The Leaf's own Hollow Crown, in miniature.

You see her through the bars, as in Ch 0, but from the other side. She knows you by the cord.

## N5: Orders (40 min)

The head orders you to kindle the girl as the vessel's spark: "Your gift can open her. We will do
the rest." The choice:

| Choice | What happens |
|---|---|
| **Pretend to obey** (`story.nightwatch.pretend`) | You go in to "prepare" her; you have one night |
| **Refuse** | They lock you out and plan to use a sealed descendant instead (genin_3, if `story.seed.genin_flame`); you must break in (N6 starts as a rescue of both) |

## N6: Giving (50 min)

The heart of the branch. You free her; the Undercroft's old ANBU fight you through the hall of
masks; in the deepest cell you do what the Kagari once did at watch-fires and what the dark mirror
reversed: you **give** her your own flame through the cord, until the stolen embers forced into
her have somewhere warm to go and leave. It costs you: you collapse, chakra empty, for a day.

She wakes as herself. Her first words are the ones she said through the bars in Ch 0, finished:
"So someone remembers I was here. You did." (`story.lost_child.home = nightwatch`; her bond starts
growing from 2.)

## N7: Daylight in the Cellar (30 min)

You bring the Undercroft to the Hokage. The head does not resist: "You will need us when he comes."
The choice of what to do with them:

| Choice | What happens |
|---|---|
| **Disband them** | The Undercroft's old masks go to the ANBU vault; the head is confined to her house (she appears in Ch 51 at the wall, fighting for the village anyway) |
| **Bring them under the Hokage** | They become a legitimate night unit; in Ch 50 they find twelve array anchors no one else could |
| **Expose them publicly** | The Shimura line's Heart step becomes a reckoning; the village's trust in the ANBU dips (a standing loss with `rank:anbu`); the head resigns |

If the branch is finished, Ch 47 becomes **The Warm Room** (her recovery) instead of her rescue.
