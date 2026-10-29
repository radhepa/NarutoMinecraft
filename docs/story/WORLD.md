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
- **Full names, Given Family.** Everyone but the Hokage has a family name; `{name:<role>}` renders
  "Given Family". A clan member carries the clan's name; anyone outside the 25 clans carries an
  ordinary family name that never matches a clan (`family_names` in `population.json`), and their
  character file says **no clan** plainly. The renamed Kagari descendants carry their adoptive
  families' names. Honorifics stay natural ("{family:sensei_4}-sensei", "Lord Fourth"); Hokage
  are named by given name only.
- **The ensemble** (the four squads of the player's class, the senior squad and five senseis) is in
  [ENSEMBLE.md](ENSEMBLE.md). Their looks are curated in Classic and rolled in Varied, so they are
  *they* in dialogue tokens too.
- **`role:fallen_parent`** is the sensei's dead teammate. Their gender is rolled per save from the
  `names` stream (they have no fixed look: they appear only in a painted portrait, drawn in shadow,
  and in memory).
- **Flags** are listed in [FLAGS.md](FLAGS.md). Twist slots are in [ROTATIONS.md](ROTATIONS.md).

## The theme in one line

**A fire you take burns out; a fire you share keeps everyone warm.** Every strand of the story is
a version of it: Kindling Bond against the dark mirror, a village that keeps its fire by keeping
its people against a village that once kept its peace by erasing them, a squad that passes the cord
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
| ~Y-13 | `fallen_parent`, a Leaf Jonin and grandchild of a renamed child, serves on a team with the future sensei and `sensei_3`. Their gift is sealed but flickers in danger: a campfire that leans toward the team | The sensei (without knowing what it was) |
| ~Y-12 | **The player is born.** Who the parent is, is `twist.lineage` ([ROTATIONS.md](ROTATIONS.md)). In every save the baby ends up in a border village, in a house with a persimmon tree, with a family who sing it the Kagari watch-fire song | — |
| ~Y-10 | **The voice** begins: someone inside the Leaf starts sending Yūgure the names and readings of gifted children (`twist.traitor`, [ROTATIONS.md](ROTATIONS.md)), the same in every save. Messages go out by **the first hand**, an old east-road carter (no clan, an ordinary name) | The voice |
| ~Y-8 | **The Ash Road ambush.** A Yūgure cell carrying chakra paper (which chars ash-violet near Kagari chakra) ambushes the three-person team of `fallen_parent`, the future sensei and `sensei_3`, to test `fallen_parent`. The sensei sends `sensei_3` back for help, then goes back in; `fallen_parent` dies; the sensei is burned trying to pull them out (the scar). `fallen_parent` had a young child with a civilian spouse in a border village; after the ambush the report lists the spouse and child as "lost" (in lineage A they truly died; in lineage B the child is the player, see [ROTATIONS.md](ROTATIONS.md) §2). Persimmons were `fallen_parent`'s favourite fruit; the sensei leaves one at the memorial stone every year. The elders, the keeper among them, record it as a bandit ambush and seal the report: an open inquiry would have asked why Yūgure wanted that Jonin | The keeper, the councillor (who signed the sealing) |
| ~Y-6 | The old carter dies in a road accident; **the porter** (a nursery child, sixteen) is sent into the Leaf and takes over as the hand. Yūgure finds the persimmon house. The family is killed or scattered; the child (six) is taken to Yūgure's **nurseries**, camps where gifted children are tested, named by number and trained. The player becomes **"Nine"** (the cells themselves are unnumbered; only the player and Yūgure ever know the name) | — |
| Y-6 to Y0 | Six years in the nurseries. The player's flame is the strongest any test has shown, and it does not grow: a wick raised in a cage stays small, because the gift grows with bonds. The leader keeps the child's existence from his own second | The leader, the voice (the reports), the porter |
| Y0 | The prologue. The hideout in the southern hills, by the ruined Kagari shrine. That night the leader takes a strong girl's chakra (`lost_child`) to test the dark mirror on a Kagari-sensitive child. The Leaf raids the camp the same night: the keeper had received an anonymous map. **The map came from the second**, who learned the hideout was emptying children and could not bear it. The porter loaded the raid squad's supply crates, so **the hand** warned the leader the raid was coming, and he **let it happen**: "Let the Leaf raise my fire." | The second; the leader |

### Elapsed time and ages

Two time skips: one year after the Chunin Exams, and **four years** before the Jonin trial. The
player is 12 at Y0. Lines spoken in later arcs count years from this table.

| Point | Year | Player's age | Stage |
|---|---|---|---|
| Ch 0 (prologue) | Y0 | 12 | Child |
| Ch 8 (team assignment) | Y0 + about a month | 12 | Child |
| Ch 20 (end of the beta) | Y0 + about two months | 12 | Child |
| Ch 21 (first skip) | Y+1 | 13 | Teen |
| Ch 32 (end of the Chunin arc) | Y+2 | 14 | Teen |
| Ch 33 (second skip, four years) | Y+6 | 18 | Adult |
| Ch 45 | Y+7 | 19 | Adult |
| Ch 55 (the Eighth) | Y+8 | 20 | Adult |

Useful spans: the Ash Road ambush is 9 years past at Ch 21 and 14 at Ch 37; the player was taken
from the persimmon house 13 years before Ch 48; the voice has been active about **sixteen years** by
Ch 35 to 39 ("sixteen years" wherever a candidate speaks the span). Every candidate was an adult
at ~Y-10 (the medic, born ~Y-31, was a new hospital orderly of 21). No count of "nine" is ever
spoken near the player except the name itself ("ten months", never "nine").

## The Kagari

The **Kagari** (篝, "bonfire") were a Warring States clan of watch-fire keepers. In camp, a Kagari
would sit at the fire with soldiers who trusted them, and the fire would "lean" toward the bonded:
the Kagari could push their chakra into a comrade's and make the comrade's own technique burn past its limits, by consent. Their crest is
a watch-fire basket (篝籠) of four crossed staves holding a flame. Their songs survive as one
lullaby, **the watch-fire song**, sung in the families of the renamed children without anyone
knowing why. The Kagari gift is a **bloodline gift**, sealed for three generations; it surfaces in the
player and is gated by bonds, not by clan membership. ROADMAP's rule that kekkei genkai come only
through clans holds for the clans; the Kagari are the one exception the story reveals.

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
strong at its height. They wear no uniform: members travel in ordinary road clothes, and their sign
is a **sinking sun drawn in soot on the inside of the wrist**. They work in **hearths**: cells of
three or more, each tied to a nursery. When they mean to be seen (the stadium, the border post)
they tie **ash-violet scarves** over their faces; ash-violet is the colour charred chakra paper
turns. The second and the blade are the exception: a pair, "the only pair he ever allowed".

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
  **the hand** (`porter`, since Y-6; an old carter before him) and **the voice** (`twist.traitor`).
  The voice's sources reach border children too: the library files the border outposts' entrance
  tests with the aptitude scrolls; the stipend registry lists the border-village orphans the Leaf
  sponsors; the hospital ledger logs every rescued child; the merchant's book logs every stop. The
  candidates' daily schedules and night movements are identical in every save until Ch 39.
- **The marks**: the sinking sun scratched on walls is a hearth's sign, and in the Leaf it is also an
  **anchor of the array**: a cinder seal laid under the scratch. Over six years in the Leaf the porter laid
  eighty-one of them across the village under crates, sills and doorsteps. The one on the player's
  door (Ch 4) marks the wick's home.

### The leader's plan, beat by beat

| When | What he does | Why |
|---|---|---|
| Ch 0 | Warned by the hand of the raid (the porter loaded its supply crates), he lets the Leaf take Nine, and watches from the ridge | The flame would not grow in a cage; the gift grows with bonds. "Let the Leaf raise my fire." That same night he tests the dark mirror on the lost child |
| Ch 4 | The porter lays an anchor under the wick's door | The array must know where the wick lives |
| Ch 13 | A stranger approaches `teammate_b` | To put eyes inside Nine's squad; b's parent is one of his |
| Ch 19 | The stadium attack: test the Leaf's defences, strike the Hokage (the Fourth's fate), and order the second to "find the strongest flame and tell me how it burns" | A test of the second's loyalty: he already knows. Nobody is ordered to take the player. She names it aloud instead |
| Ch 23 | The testers' free schools go on | The paper still hunts for other wicks, in case this one fails |
| Ch 24 | The lost child raids the border post, ordered to wound and never kill the wick; he watches from a ridge (24.7) | To wake the gift by making a friend fall |
| Ch 30 | The Tobari cinder bombs | A test: does the Leaf turn on its own when frightened? Its answer feeds his plan to strike when it is divided |
| Ch 37.3 | The blade's raid on the archive for the Hearthstone | The array's heart; it fails |
| Ch 44 | A sentence sent through the lost child's stolen voices: "Grow, little flame. I like your friends." | He wants the web to grow: the wider it is, the more there is to take |
| Ch 51b | His voice comes through the array as the player climbs the Rock | He needs the wick at the heart |
| Ch 52 | The array lit; the dark mirror offered | The Hollow Crown |

He never calls the player kin; he calls them "little flame".

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

*Approved design.* The Kagari gift is **Kindling Bond**: power that flows outward, through people.
It grows with how many people the player has truly bonded with and how deep those bonds go. At its
height it is as strong as the great eye techniques, but it is not an eye: its sign is an **ember
mark** on the palm (later the chest), threads of light, and ember-gold chakra. Nothing is ever
copied or borrowed.

| Power | What it does | Tier (friendship level) |
|---|---|---|
| **Thread Sight** | Always on. Bonds appear as threads of light: who is tied to whom, how strongly, which ties fray or run one way. Bonded allies are sensed anywhere on the map. A bonded person who is hiding something shows a flicker in their thread | Spark (6) |
| **Kindle** | Push your chakra into a bonded ally so *their own* technique goes past its limits: a fireball becomes a firestorm, healing becomes a revival, a sensor's range covers the village. They do it, bigger | Spark (small kindles), Flame (8: full) |
| **Ember Link** | Bind the squad into one flame: a shared chakra pool, damage spread across the squad, seeing through a linked ally's eyes. **Unison techniques**, unique to each pairing | Flame (8); unison at Blaze |
| **Ember Mark** | An ember left in a deeply bonded ally: travel to their side, or call them to yours, across any distance | Blaze (10, or a spouse) |
| **Bonfire** | The ultimate: every bond at once. Its strength is the whole bond web; a player who befriended half the village burns like a sun, a loner holds a candle | Bonfire (the bond web) |

**Costs.** While linked you feel your allies' pain. Overuse burns your own chakra and stamina. A
quarrel dims that person's flame; a falling-out puts it out. With strangers it does nothing.
**Natures** come by resonance: fight beside someone often enough and their trial can teach you
their nature. You never copy it.

### The rules the story keeps

1. **It needs a bond, and the bond's consent.** It works through people who trust you; it fails with
   strangers, enemies and anyone in a falling-out.
2. **It gives, never takes.** A kindled ally loses nothing and gains. Pouring your flame into
   someone can relight theirs (the lost child's return), and it costs you.
3. **It grows with the web.** Its ultimate is the whole village choosing you.
4. **The dark mirror is its shadow**: taking chakra by force, without a bond. The player never gets
   it; it is offered once (Ch 52), and refusing is the climax.

### Story floors

The gift must play in every save, including a lonely one:

- **Scripted scenes.** A scripted gift scene treats its scripted target as at the tier it needs
  (Ch 24: Spark; Ch 31: Flame), whatever their level. Ch 31's link binds everyone at 6+ plus a
  scripted pair link with the friend who fell in Ch 24.
- **`offered_flame`.** A person below level 6 can kindle toward the player only by freely offering
  their flame (an act, recorded as a permanent moment). It is how `squad5_b`'s grandmother kindles in
  Ch 31, how whole clans and districts kindle in Ch 53, and how the red cord kindles.
- **The crossing (Ch 51b).** Ember Mark jumps only to friends at Blaze; otherwise the player crosses
  the burning village on the rooftops, guided by `squad4_a`'s Byakugan. Fewer Blaze friends, a
  longer run.
- **The lonely finale.** The red cord is always the first flame: the lost child always comes home by
  Ch 47, and `bond_flag red_cord` kindles at any level ("Take it. It's mine to give."). The sensei
  always gives theirs second (`saved_by_them`, Ch 0; it overrides even a falling-out). Ch 53's order
  is fixed: the cord, the sensei, the spouse, the friend who fell in Ch 24, the other teammate, the
  rival, then faces without spoken lines (others by level, clans, districts). Below the web's lowest
  threshold the Bonfire is an honest small fire (two or three flames on a quiet Rock), and it still
  wins: a fire freely given cannot be taken, however small. The thresholds are data, calibrated by
  the bonds session's simulation of `BondWeb.score` ([BONDS.md](../../BONDS.md) §11). The epilogue
  has a matching lonely tier: "You carried this with very few hands. Let more in now."
- **The second and the blade at the end.** The blade turns in Ch 51b and lives (taken into custody;
  in the epilogue he asks to guard the shrine or the second's grave). The second's fate resolves in
  Ch 53.5, before the leader's end in 53.6.

### Thread Sight and the mystery (one engine rule)

Thread Sight could solve the voice's case in a glance; it does not, because one rule holds in every
save and every rotation:

1. **It reads only your own web.** A person shows a thread only if they are bonded to you at level 6
   or more. A thread between two *other* people shows only when both are bonded to you at 6+.
   Strangers, enemies and acquaintances are dark.
2. **A flicker is a steady state, never a lie detector.** It comes from one `hides:` bond flag: the
   thread flickers for as long as the person keeps something from you, the same in every scene,
   whatever they say line by line. It shows *that*, never *what*. Each of the four traitor
   candidates carries exactly one `hides:` flag of the same kind until Ch 39 or 40 in every save
   (the librarian her family history, keeping back what the cut page listed; the medic their
   letters to the strangers who once saved them, keeping back the last reply in their crane jar; the
   councillor his signature on the Ash Road sealing, keeping back his grandfather's vote; the
   merchant old debts and bandit smuggling, keeping back the night at the waystation). All four
   flicker the same; the bound candidate's thread to the player is an ordinary two-way thread. The
   flicker narrows nothing.
3. **The hand is never in your web.** The porter is never at 6+ before Ch 28, and after it his
   memory is burned, so the voice's tie to the hand is never visible.
4. **Scripted exceptions** (`thread_floor`, the only ones): the red cord's grey thread (Ch 24.6, N6,
   Ch 47); a one-sided thread *toward* the player from the second (from Ch 27; fraying from Ch 49 to
   Ch 52); teammate_b's fraying thread before the bridge (Ch 26, every branch); the blade's thread to
   the second, **only in Ch 52**. The porter and every traitor candidate are never exceptions before
   Ch 39. The leader has **no threads at all**: eighty years without one bond.
5. **Only two things may differ between rotations before Ch 39**: the Ch 25.1 slip line, and the
   results of the four alibi checks (Chunin side content and Ch 38). Every other scene, vote,
   schedule and question plays identically in every save ([ROTATIONS.md](ROTATIONS.md) §1).

The keeper flickers too, honestly (he hides the archive) until Ch 36.

### Story milestones of the gift

| Milestone | Where | Tier |
|---|---|---|
| Foreshadowing: the flare, the flicker on the cord, the leaning campfire | Ch 3, Ch 8, Ch 16 | — |
| **Awakening.** At the border post a friend falls for you; the threads appear; you kindle them and they rise once and cast their own technique past its limits | Ch 24 | Spark (story floor) |
| The gift named, its old forms learned, trained in secret: Thread Sight drills, small kindles | Ch 25 to Ch 29 | Spark |
| The gift in the open: the squad linked as one flame in the drain; a near-stranger offers their flame (`offered_flame`) | Ch 31 | Flame (story floor) |
| Unison techniques with the closest bonds; the first Ember Mark (spouse or a level-10 friend) | Jonin arc, systemic | Blaze |
| Relighting a flame: the lost child's return | Night Watch N6 or Ch 47 | Blaze (the cord) |
| Ember Marks across the burning village: travel to the friends who need you | Ch 51b | Blaze (else the rooftop run) |
| The Bonfire: every bond in the village | Ch 53 | Bonfire |

## The Leaf's people in power

| Body | Who | Stance |
|---|---|---|
| The Hokage | Four at the start; three more change hands in the story | — |
| The elder council | Three elders: the `elder_keeper` (archive), the `elder_councillor` (registry and stipends), and a Hyuga elder (`elder_hyuga`, the Fifth's uncle, a minor role) | Sealed the Ash Road report; the keeper and councillor know parts of the truth |
| The sensor corps | Hyuga and Yamanaka sensors | Under the Fifth: watches "anomalous chakra" |
| The Undercroft | The heirs of the sealing team that sealed the twenty-seven in the Quiet Ending: a mixed-clan oath society of old ANBU and sealers, led by the sealing team leader's granddaughter (`undercroft_head`, no clan), meeting in the sealing team's derelict hall under the old quarry. The Shimura have no part in it (a Shimura helps expose it) | Believes the gift must stay sealed, and be used: their sealed **jar**, and a plan to make the lost child its mouth (Night Watch) |

## Places the story adds

| Place | Where | First seen | Notes |
|---|---|---|---|
| The southern hills hideout and the ruined Kagari shrine | Prologue hills | Ch 0 | Burned shrine, a stone watch-fire basket still standing; later the old Kagari land (one of the vacant estates' plots, by the hills) |
| The sealed door at the foot of the Rock | Under the Rock | Ch 4 | The archive: records, the renaming list, the Third's letter, the Hearthstone |
| The memorial stone, Training Ground 3 | Ground 3 | Ch 10 | Chiselled gap; `fallen_parent`'s name just beside it |
| The Ash Road waystation | East road | Ch 13 | Where the Ash Road ambush happened eight years before, and where the trail of the empty bed ends |
| The border village with the persimmon tree | A far region | Ch 21 (the player's memory), Ch 48 (visit) | The house of the player's early childhood, burned |
| The border post at the Ash Road | A far region | Ch 24 | The lost child's raid |
| The Valley of Ash | A far region | Ch 35 | The old battlefield; a Yūgure nursery in its caves |
| The Undercroft | The sealing team's derelict hall under the old quarry | Night Watch | Found through `clan.shimura.3`: a Shimura discovers a stranger using their cellar as a mail drop for sealed letters, and the courier leads to the quarry |

## Tone

- **Like the anime, not copied from it.** Earnest friendship and rivalry, a sensei who teaches more
  by example than by speeches, goofy filler and food, villains with real grief, sacrifice that
  is earned, and a village worth protecting.
- **Allowed from canon:** clan kekkei genkai and clan art names (ROADMAP §11); Academy basics
  (Clone, Transformation, Substitution, tree and water walking); canon places the map uses
  (Ichiraku, the Hokage Rock, the Forest of Death, Training Ground 3); "the Will of Fire" only as the
  Sarutobi lantern-walk custom and in characters' questions about it, never as a slogan.
- **Forbidden:** canon characters' signature techniques by name in story scenes, canon catchphrases
  and verbal tics, canon exam gimmicks, canon scenes restaged.
- **Child stage is safe.** No romance, no gore, no blood (a cut is "a cut, a scar later"). Deaths happen off-screen or in the cinematic camera's
  cutaway; the hollow are pale and quiet, not mutilated.
- **Earned speeches.** A speech about bonds lands only after the player has lived the bonds it
  names. Dialogue in big moments reads flags and memories so the speech is about *this* save.
- **Humour stays.** Even the Last Bonfire arc keeps a ramen night and a squabble (the pre-war
  squad dinner in Ch 50).
