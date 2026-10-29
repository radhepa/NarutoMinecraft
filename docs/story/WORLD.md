# The world behind the story

> **SPOILERS: for developers only.** Part of the [story bible](STORY_BIBLE.md).

What happened before the player wakes in a cell, what each faction wants, and the rules the plot
keeps. Every arc file and character file builds on this one; when they disagree, this file wins
and the other is a bug.

## Conventions

- **Roles, not names.** Characters are written by role (`role:sensei`). Text uses tokens:
  `{name:<role>}`, `{given:<role>}`, `{family:<role>}`, `{hokage:<n>}`, `{player}`.
- **Pronouns.** Characters with a **fixed look** have a fixed gender, written here: the Hokage
  (1 man, 2 man, 3 woman, 4 man, 5 woman, 6 man), `elder_keeper` (man), `elder_councillor` (man),
  `librarian` (woman), `lost_child` (girl), `yugure_second` (woman), `yugure_blade` (man),
  `yugure_leader` (man), `porter` (young man), `undercroft_head` (woman), `fallen_parent` (rolled,
  see below). Characters whose look is **rolled in Varied** (the sensei, instructor, medic, the
  four classmates, rival, merchant, the Jonin-arc Genin) have a rolled gender, so the story files
  call them *they* and dialogue uses pronoun tokens (`{they:<role>}`, `{them:<role>}`,
  `{their:<role>}`, requested from the dialogue and character-creation sessions). The player's
  gender comes from the creator screen and is always a token.
- **`role:fallen_parent`** is the sensei's dead teammate. Their gender is rolled per save from the
  `names` stream (they have no fixed look: they appear only in a painted portrait, drawn in shadow,
  and in memory).
- **Flags** are listed in [FLAGS.md](FLAGS.md). Twist slots are in [ROTATIONS.md](ROTATIONS.md).

## The theme in one line

**A fire you take burns out; a fire you share keeps everyone warm.** Every strand of the story is
a version of it: Kindling Bond against the dark mirror, a village that keeps its fire by keeping
its people against a village that once kept its peace by erasing them, a squad that passes the bell
test only together, a leader who wants to hold everything and a player who wins by being held.

Three questions the story asks the player, again and again, through choices and through the
characters' questions:

1. **What do you owe the people who wronged you?** (The leader, the second, teammate_b's parent,
   the village itself.)
2. **Is it enough to know the truth, or must it be said aloud?** (The keeper, the librarian, the
   archive, the traitor.)
3. **Are you what you were born, or what you choose?** (Kagari blood, the camps' number, the rival,
   the lost child.)

## Chronology

Years count back from the prologue (Y0). A year of the village calendar is 112 days, but the
story counts in ordinary years.

| When | What happened | Who knows at Y0 |
|---|---|---|
| ~Y-82 | **The Valley of Ash.** In the last war before the founding, the Kagari clan head ends a battle by tearing the chakra out of every soldier in a valley, Senju and Uchiha alike, with the dark mirror. Thousands are left hollow; most die within days. The Kagari themselves are horrified; the clan splits | Everyone knows the battle; almost no one knows it was a Kagari |
| ~Y-80 | **The founding.** The First Hokage (Senju) writes the founding charter with a **fourth clause** inviting the Kagari into the village as a founding clan: their watch-fire tradition (kindling allies in war camps, by consent) had saved his soldiers for years, and he blamed the valley on one man | The charter's public copy is missing the clause |
| ~Y-72 | The First dies. The Second Hokage (Uchiha) takes office | — |
| ~Y-70 | **The Quiet Ending.** A report (forged by a frightened Uchiha elder, never proven) says the Kagari plan a second bonfire. The Second and the clan council order the Kagari ended. Adults who resist at the clan shrine in the southern hills are killed; the shrine burns. **Twenty-seven children** are taken, their gift sealed by a sealing team, and adopted into Leaf families under new names. The names of the Kagari dead are chiselled off the memorial stone at Training Ground 3. The records, the forged report, the **renaming list** and the clan's relic, the **Hearthstone** (an ember that has burned since the clan began), are sealed in an archive under the Rock | The archive's keepers |
| ~Y-70 | **One child escapes**: a boy of nine, hidden in the shrine's ash pit. He lives in the burned hills, then in the wars of other nations, and survives by learning the dark mirror from the clan's forbidden scroll | Only himself |
| ~Y-58 | The Third Hokage (Sarutobi) takes office, learns of the Quiet Ending, and keeps the silence for the peace. Thirty years of peace | — |
| ~Y-40 | The Third takes a last student, a young archivist (`elder_keeper`), and swears him to keep the archive and its silence | The keeper |
| ~Y-30 | The Third writes a letter and seals it in the archive: "for whoever comes asking" | No one has read it |
| ~Y-28 | The Fourth Hokage (Akimichi) takes office. The keeper never tells him the archive's full contents | — |
| ~Y-25 | The surviving boy, now ageless on taken chakra, gathers soldiers abandoned after wars, orphans used and discarded and clans broken by treaties | — |
| ~Y-20 | **Yūgure** is founded (see below) | — |
| ~Y-15 | The keeper notices descendants of the renamed children showing chakra the sealing should have smothered. The seal is weakening over the generations | The keeper |
| ~Y-13 | `fallen_parent`, a Leaf Jonin and grandchild of a renamed child, serves on a team with the future sensei. Their gift is sealed but flickers in danger: a campfire that leans toward the team | The sensei (without knowing what it was) |
| ~Y-12 | **The player is born.** Who the parent is, is `twist.lineage` ([ROTATIONS.md](ROTATIONS.md)). In every save the baby ends up in a border village, in a house with a persimmon tree, with a family who sing it the Kagari watch-fire song | — |
| ~Y-8 | **The Ash Road ambush.** A Yūgure cell carrying chakra paper (which chars ash-violet near Kagari chakra) ambushes the sensei's team to test `fallen_parent`. The parent dies; the sensei is burned trying to pull them out (the scar). The elders, the keeper among them, record it as a bandit ambush and seal the report: an open inquiry would have asked why Yūgure wanted that Jonin | The keeper, the councillor (who signed the sealing) |
| ~Y-6 | Yūgure finds the persimmon house. The family is killed or scattered; the child (six) is taken to Yūgure's **nurseries**, camps where gifted children are tested, numbered and trained. The player becomes **"Nine"** | — |
| Y-6 to Y0 | Six years in the nurseries. The player's flame is the strongest any test has shown. The leader keeps the child's existence from his own second | The leader, the traitor (the reports), the porter |
| Y0 | The prologue. The hideout in the southern hills, by the ruined Kagari shrine. That night the leader takes a strong girl's chakra (`lost_child`) to test the dark mirror on a Kagari-sensitive child. The Leaf raids the camp the same night: the keeper had received an anonymous map. **The map came from the second**, who learned the hideout was emptying children and could not bear it | The second |

## The Kagari

The **Kagari** (篝, "bonfire") were a Warring States clan of watch-fire keepers. In camp, a Kagari
would sit at the fire with soldiers who trusted them, and the fire would "lean" toward the bonded:
the Kagari could borrow a comrade's nature or a technique for a moment, by consent. Their crest is
a watch-fire basket (篝籠) of four crossed staves holding a flame. Their songs survive as one
lullaby, **the watch-fire song**, sung in the families of the renamed children without anyone
knowing why.

**The renamed children.** Twenty-seven, adopted into Leaf families of every kind: a few into clans
(a Senju household, a Sarutobi household, a Kurama household of painters, two Tobari households),
most into clanless shinobi and civilian homes. Their gift was sealed. Three generations later
there are a few hundred quiet descendants in the Leaf, most with no trace of the gift; a handful
whose sealed flame flickers. In the story:

| Descendant | Line | What it means |
|---|---|---|
| The player | Strongest flame in generations; the seal is gone | The wick |
| `fallen_parent` | A renamed child's grandchild; sealed flame that flickered | Killed for it |
| `librarian` | A renamed child's granddaughter; her family kept the true history in secret | A traitor candidate's motive; or an ally who knows the old forms |
| `yugure_second` | Descended from a renamed child who left the Leaf for a border town two generations ago; her flame broke its seal as ember chakra | Why the leader made her his second |
| `lost_child` | Distant descendant; strong reaction to the chakra paper | Why she was in the nursery, and why the leader chose her for his test |
| Others | Families across the village, unaware | Your restored clan can find them (Road to Hokage) |

The founding charter's public copy and the Academy's founding history each lost a page. The
library's history book page was cut on the morning of Ch 5 (see [ROTATIONS.md](ROTATIONS.md) for
who did it in each save). The archive keeps the originals.

## Yūgure

**Yūgure** (夕暮れ, "Dusk") is a band of missing-nin from across the five nations, about two hundred
strong at its height, in **two-man cells**, in **ash-violet cloaks marked with a sinking sun**.

- **The creed** (what members believe): *the shinobi world must end at dusk so that a true dawn can
  come.* The **Last Bonfire** is a fire of gathered chakra that will spread through the hidden
  villages until none of them stands, so no village can use and discard children again. Most
  members are sincere. Many were the children villages used.
- **The truth** (what the leader wants): the **Hollow Crown**. Not the end of every village, but
  every chakra of one village, forced through a Kagari wick and taken from the wick by the leader:
  one person holding a whole village's strength, ruler over every shinobi, never again able to be
  erased. He has told no one. His second learns it in the Road to Hokage and turns.
- **What they do**: smuggle chakra paper to find children whose chakra chars it; buy and steal those
  children for the nurseries; recruit the bitter; plant agents in villages. In the Leaf they have
  **the hand** (`porter`) and **the voice** (`twist.traitor`).
- **The marks**: the sinking sun scratched on walls is a cell's sign, and in the Leaf it is also an
  **anchor of the array**: a cinder seal laid under the scratch. Over six years the porter laid
  eighty-one of them across the village under crates, sills and doorsteps. The one on the player's
  door (Ch 4) marks the wick's home.

### The Hollow Crown, step by step

1. **The array**: eighty-one cinder seals around the village (laid by the porter).
2. **The heart**: the Hearthstone, the Kagari relic sealed in the archive under the Rock. Only it
   can join the array into one fire.
3. **The wick**: a Kagari of strong flame at the heart. The array forces every chakra in its reach
   into the wick (force-kindling: the dark mirror at the scale of a village).
4. **The taking**: the leader takes the gathered fire from the wick with the dark mirror. The wick
   and everyone in the array are left hollow.

What defeats it (Ch 52 to 53): a fire freely given cannot be taken. When the player's bonds kindle
toward the player by their own will, the gathered fire is no longer the array's; it answers the
wick, and it will not burn for a taker. The leader's own mirror turns on him.

## Kindling Bond in the story

The ability list is being redesigned (working proposal: perceive bonds, kindle allies, a link, a
mark to travel to or call bonded allies, an ultimate that scales with the bond web; tiers Spark,
Flame, Blaze, Bonfire). **The story depends only on these rules**, which any final design must keep:

1. **It needs a bond, and the bond's consent.** It works through people who trust you; it fails with
   strangers, enemies and anyone in a falling-out.
2. **It shares, never takes.** A kindled ally loses nothing.
3. **It is visible.** A small watch-fire flame between you and the ally (*Kagari-bi*).
4. **It can give as well as borrow.** Pouring your own flame into someone is possible (the lost
   child's return), and costly.
5. **It grows with the web.** The more people (and the more kinds of people) who would kindle for
   you, the greater it is. Its ultimate is the whole village choosing you.
6. **The dark mirror is its shadow**: taking chakra by force. The player never gets it; it is offered
   once (Ch 52), and refusing is the climax.

**Story milestones of the gift** (mapped to the proposed tiers where they line up; if the ability
list changes, the milestone moves with the nearest ability):

| Milestone | Where | Proposed tier |
|---|---|---|
| Foreshadowing: the flare, the flicker, the leaning campfire | Ch 3, Ch 8, Ch 16 | — |
| **Awakening**: the first real kindling, a fallen teammate's nature | Ch 24 | Spark |
| The gift named and trained in secret | Ch 25 to Ch 29 | Spark |
| The gift seen in the open; the first time someone kindles *toward* you | Ch 31 | Flame |
| Giving flame: the lost child's return | Night Watch N6 or Ch 47 | Blaze |
| The Bonfire: every bond in the village | Ch 53 | Bonfire |

## The Leaf's people in power

| Body | Who | Stance |
|---|---|---|
| The Hokage | Four at the start; three more change hands in the story | — |
| The elder council | Three elders: the `elder_keeper` (archive), the `elder_councillor` (registry and stipends), and a Hyuga elder (`elder_hyuga`, the Fifth's uncle, a minor role) | Sealed the Ash Road report; the keeper and councillor know parts of the truth |
| The sensor corps | Hyuga and Yamanaka sensors | Under the Fifth: watches "anomalous chakra" |
| The Undercroft | A hidden faction of retired ANBU under the Shimura house | Believes the Kagari gift must be caged and used (Night Watch) |

## Places the story adds

| Place | Where | First seen | Notes |
|---|---|---|---|
| The southern hills hideout and the ruined Kagari shrine | Prologue hills | Ch 0 | Burned shrine, a stone watch-fire basket still standing; later the old Kagari land (one of the vacant estates' plots, by the hills) |
| The sealed door at the foot of the Rock | Under the Rock | Ch 4 | The archive: records, the renaming list, the Third's letter, the Hearthstone |
| The memorial stone, Training Ground 3 | Ground 3 | Ch 10 | Chiselled gap; `fallen_parent`'s name just beside it |
| The Ash Road waystation | East road | Ch 13 | Where the Ash Road ambush happened eight years ago, and where the trail of the empty bed ends |
| The border village with the persimmon tree | A far region | Ch 21 (the player's memory), Ch 48 (visit) | The house of the player's early childhood, burned |
| The border post at the Ash Road | A far region | Ch 24 | The lost child's raid |
| The Valley of Ash | A far region | Ch 35 | The old battlefield; a Yūgure nursery in its caves |
| The Undercroft | Under the Shimura house | Night Watch | Its cellar door is the Shimura line's secret |

## Tone

- **Like the anime, not copied from it.** Earnest friendship and rivalry, a sensei who teaches more
  by example than by speeches, goofy filler and food, villains with real grief, sacrifice that
  is earned, and a village worth protecting. No catchphrases, jutsu names or scenes lifted from
  canon; canon clans and places appear as the setting the mod already uses.
- **Child stage is safe.** No romance, no gore. Deaths happen off-screen or in the cinematic camera's
  cutaway; the hollow are pale and quiet, not mutilated.
- **Earned speeches.** A speech about bonds lands only after the player has lived the bonds it
  names. Dialogue in big moments reads flags and memories so the speech is about *this* save.
- **Humour stays.** Even the Last Bonfire arc keeps a ramen night and a squabble.
