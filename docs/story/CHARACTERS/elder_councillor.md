# `role:elder_councillor`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). A
> `twist.traitor` candidate: read [ROTATIONS.md](../ROTATIONS.md) §1 first.

## At a glance

| | |
|---|---|
| Role | `role:elder_councillor`, the council elder who keeps the orphan stipend registry |
| Look | Fixed: a broad, upright man in his late sixties, white hair tied back Senju-style, a neat short beard, green-and-brown council robes, a seal box of dark wood carried by a cord; his personal seal is a pine sprig |
| Pronouns | He / him |
| Clan | Senju (a cadet household); family name Senju |
| Rank | Jonin (retired), elder of the council |
| Archetype | `steadfast` (warmth .3, bold .2, pride 0, discipline .5, open 0) |
| Values | duty, loyalty (to the village, to his clan's name) |
| Peeves | lateness, dishonesty |
| Dream | "honor their clan": to pay back what the Senju owe |
| First appearance | Ch 1 |
| Last appearance | Ch 55 (the ruling if bound; a guest at the inauguration if innocent) |

## Arc

### Common to every save

- His grandfather, a Senju scribe, drafted the First's **fourth clause** inviting the Kagari at the
  founding, and ten years later voted with the council for the Quiet Ending. The family has known for three
  generations; it is the household's private shame and why the councillor took the registry: he
  wanted to look after orphans.
- He keeps the orphan stipend registry. Every orphan has a number: the player is **S-114**. His
  personal pine-sprig seal goes on papers he handles himself.
- He arranged the player's stipend personally **because the keeper asked him to** (Ch 1). That is
  true in every save.
- With the keeper, he **signed the sealing of the Ash Road report** (~Y-8). He told himself an
  inquiry would set the clans on each other.
- He sends council letters through the porter, like every elder. On post days his seal box sits
  open on his desk while the porter collects the post (true in every save).
- He sits in the council briefings that set the finals' guard rotation (one of the routes by which
  a rotation could leak, true in every save).
- **His every-save secret**: he signed the Ash Road sealing that buried a Jonin's death (the
  signature itself comes out in Ch 37.0, when the report is read).
- **His held-back piece:** his grandfather's vote. He keeps it until Ch 39 (bound) or Ch 40
  (innocent), in every save.

**Thread Sight.** From Ch 24, if he is bonded to the player at 6 or more and the player probes him,
his thread flickers: he is hiding something. He is, in every save (the Ash Road signature, and his
grandfather's vote), so the flicker cannot single out the voice and never says what. It **never goes out
before Ch 39 or 40** (after Ch 37.0 the signature is known, but the grandfather's vote is still held
back). Bound, his thread to the player reads as a normal two-way thread. His tie to the porter is
never visible.

### If innocent

- **Wants:** to protect the village's peace and, if it ever comes, to be there when the Senju pay
  what they owe.
- **Fears:** that he is his grandfather: a man who wrote the right thing and voted the wrong one.
- **Secret:** the family's shame, and the Ash Road signature.
- **The pass** (`story.clue.councillor.2`): the porter used the open seal box on a post day.
- **The letter to the porter** (`story.clue.councillor.3`): ordinary council post.
- **The slip scene (Ch 25.1):** "The council is pleased. Another of the registry's children made
  Chunin. Your number is on my wall now, with the others who did." (He means S-114.)
- **The alibi** (`side.c.court_roll`, or the case board): his clerk's log marks the pass's date as a
  post day with the seal box left open on his desk, and the court's repaired guest roll shows him at
  the daimyo's court that day.
- **Ch 36 to 37:** he is not there. He hears of the archive the next day and asks the Sixth to let
  him read the fourth clause in his grandfather's hand (every save).
- **Ch 40 cleared:** at the council he moves to make the Quiet Ending public and votes first, then
  tells the room his held-back piece (his grandfather drafted the clause and voted to end them) and
  owns his Ash Road signature in the open. To the player, privately, if lineage B and
  after Ch 48: "I signed away the truth of your parent's death."
- **Road to Hokage:** he supports the restoration at the registry (Ch 46: he waives the founding fee
  "on behalf of a debt"); in Ch 50 he opens the Senju quarter's anchors himself.
- **Ending:** keeps his seat; at Ch 55 he hands the player the registry's first new page: the
  stipend extended and made law in the Fourth's name. A possible archive keeper.

### If bound (the voice)

- **Wants:** the Kagari restored and the Senju debt paid, and he no longer believes the village will
  pay it. The leader proposed a pact: names of descendants and gifted orphans for a promise to
  restore the clan "without blood".
- **Fears:** that he believed the part he wanted; that he kept the player close for the leader as much
  as for the keeper, and cannot tell which he meant more.
- **Secret:** since about Y-10, registry numbers sent through the porter; the finals' guard rotation
  from the council briefing (Ch 19); the news, spread by the Sixth's clerk to the council, that the
  archive would be open (Ch 37); and after the porter fell (Ch 28), reports in his own council post.
- **The pass:** he sealed it.
- **Ch 36 to 37:** identical to the innocent track (he asks to read the fourth clause).
- **The letter to the porter:** a report.
- **The slip scene (Ch 25.1):** "The council is pleased. Number nine of the registry's children to make
  Chunin." (The registry keeps no such count, and you are S-114.)
- **The failed alibi:** his clerk's log shows him signing the seal box out himself and sealing a
  travel pass on that date; the guest roll shows he left court early.
- **Ch 38:** the list is indexed by S-numbers with pine marks.
- **Ch 39 reveal:** his study, the seal box open. "My grandfather drafted the fourth clause and then
  voted to end them. The Senju owe a clan its name. The village would never pay; he said he would
  make it pay without blood. I believed the part I wanted." In lineage B he adds only: "I signed the Ash
  Road away too. A Jonin's death, and a child's." (Nothing more until after Ch 48.)
- **Fate:** *arrested*: stripped of his seat; the Senju line's Heart step (`clan.senju.4`) becomes his
  house's reckoning. *Turned* (needs `friendship [elder_councillor, 4]`): he keeps his seat as a mole
  and feeds the leader a false finals-style rotation for the assault; Ch 51's west wall is ready.
  Ch 55's ruling: pardon (he serves the registry he betrayed), exile, or service (he records every
  descendant's restored name).

### How he changes

| Arc | Innocent | Bound |
|---|---|---|
| Cinders to Embers | Kind, formal, proud of "his" orphans; at council day hands post to the porter; directs the stadium's evacuation; visits the player in hospital (Ch 25.1); at the Tobari council (Ch 31) **abstains "for the registry's neutrality"** | Identical, except the Ch 25.1 slip line and the alibi result |
| Ashes | Cleared; confesses his signature; votes first | Revealed |
| Last Bonfire | Pays the debt in public | In a cell, or a mole who hates every day of it |

Nothing else differs before Ch 39.

## Dialogue brief

### Voice

- **Register:** courtly and warm, a council speaker's cadence; uses "we" for the village and the clan.
- **Habits:** taps the seal box when thinking; calls the player by their registry number once, in
  Ch 1, then by their given name forever ("A number is for the files"). In the bound track that
  habit is what makes the Ch 25 slip stand out.
- **Tics:** says "in good order" when anything is settled.
- **Never says:** "Kagari" before Ch 39 (bound) or Ch 40 (innocent); "nine" except the bound slip.

*Voice samples, not shipped lines:*

- (Ch 1) "Stipend S-114. I saw to it myself. A number is for the files; you'll have a name with me."
- (council day) "The council hears both clans. That is all a council is: a room where you must hear."
- (Ch 31, every save) "The registry serves every child in this village. I abstain, for its neutrality."
- (Ch 40, innocent) "My grandfather wrote the clause that invited them. Then he voted to end them. I
  have his handwriting on my wall. Today I would like to finish his sentence."

### Topics they care about

| Depth | Topics |
|---|---|
| 0 to 2 | The stipend, your flat, whether you are eating; the Senju founders' shrine |
| 3 to 4 | Council procedure; the clans' quarrels; his household's garden |
| 5 to 6 | Duty to the dead; his grandfather (as "a scribe who served the First") |
| 7+ | Debt between clans; whether a law can be wrong; his signature (after Ch 37.0, both tracks; he is ashamed, and says less than he knows) |

### Never reveal before

| Secret | Gate |
|---|---|
| The fourth clause and his grandfather's vote | Ch 40 (innocent), Ch 39 (bound) |
| The Ash Road signature | Ch 37.0 (the report is read); he owns it aloud Ch 39 or 40 |
| That the keeper asked him to arrange the stipend | After Ch 37.0 |
| The council briefing as a leak route | `twist.traitor = elder_councillor` and Ch 39 |
| The pact with the leader | `twist.traitor = elder_councillor` and Ch 39 |
| The number nine | Only the bound Ch 25.1 slip |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes him | Bound answer in Ch 39c |
|---|---|---|---|---|---|---|---|
| `ans.elder_councillor.stipend` | Ch 7 (graduation, level 1) | "You are a shinobi now, and the stipend is still yours. Was it enough, these weeks?" | It was a home / It was barely enough / It should never end for anyone | Duty | Ch 55: the restored stipend's terms | "Never end": he proposes a stipend for every Academy orphan until Chunin (innocent, Ch 40; the player can enact it in Ch 55) | "You said it was a home. I was keeping you on file in it." |
| `ans.elder_councillor.debt` | Level 4 | "Does a grandchild owe for a grandparent's wrong?" | Yes / No, but they can choose to pay / Only if they keep the profits | His heart | Ch 39 or 40 | "Choose to pay" is the line he quotes at the council | "You said one can choose to pay. I chose a way that cost other people." |
| `ans.elder_councillor.law` | Council day (Ch 12+), level 3 | "Are laws for the village or for the people in it?" | The village / the people / the people the village forgets | Duty against kindness | Ch 31 (his abstention speech, every save) | "The people the village forgets": his abstention adds "and a registry that forgets anyone is no registry" (both tracks). Unset: the plain line | — |
| `ans.elder_councillor.sign` | Level 5 (Chunin) | "Would you put your seal on something you weren't sure of, if everyone you respected asked you to?" | No / Yes, and carry it / Yes, and read it aloud first | Tests his signature | Ch 37.0 to 40 | "Read it aloud first" becomes his rule as a councillor after Ch 40 | "I did, and I didn't read it aloud." |
| `ans.elder_councillor.fear` | Ch 31 (after the testimony, level 5) | "What should a council fear most?" | Its enemies / its own people / being wrong out loud | Duty | Ch 40 | "Being wrong out loud": he is the first to stand in Ch 40 | "I feared being wrong out loud. So I was wrong in letters." |
| `ans.elder_councillor.pine` | Level 2 | "Do you know why my seal is a pine? Guess." | It lives a long time / it stays green / you like pine nuts | Life (filler with a payoff) | Ch 55: he answers it ("Pines grow where the old trees burned.") | — | — |
| `ans.elder_councillor.vote` | Ch 40 (innocent, before the council) | "If I stand up first, will you stand second?" | Yes / I'll stand first / Stand alone; it's yours to do | Loyalty | Ch 40.2 staging | Who speaks first at the council | — |
| `ans.elder_councillor.flat` | After Ch 1 (level 1) | "Is the flat in good order? Anything broken, anything missing?" | It's perfect / the door sticks (fixed already) / it's lonely | Duty, kindness; "lonely" is a small confession | Ch 25 hospital visit line (both tracks): he asks about the flat again | "Lonely": he sends a potted pine for the sill (a furniture keepsake) | — |
| `ans.elder_councillor.change` | Paper Trail, after council day (level 3) | "If you sat on the council, what would you change first?" | The stipend / who gets heard / nothing, I'd listen first | Duty | Ch 40: he recalls it voting | "Who gets heard": the Chunin testimony rule (Ch 31) is his proposal, credited to the player | — |
| `ans.elder_councillor.proud` | Level 4 | "Is there someone you'd want to be proud of you? Living or not." | The captain / the girl from the cell / my parents, whoever they were / no one | Family; opens his grandfather story | Ch 39 or 40 | — | — |
| `ans.elder_councillor.clans` | Embers, level 5 (after Ch 30) | "Which part of the village do you think the council hears least?" | The minor clans / the civilians / the orphans / the Tobari, this month | Duty against fear | Ch 31 | "The Tobari": before abstaining he asks the Fifth to hear the Tobari first (both tracks) | — |

### What their lines are for

- **Functions:** clue carrier (beta, identical), politics (council, Ch 31, Ch 40), the clans' debt
  (theme), sympathy for the bound reveal, a public ally (innocent).
- **Mood states:** `formal` (default), `fatherly` (level 5+), `troubled` (after Ch 31, both tracks),
  `ashamed` (after Ch 37.0, both tracks), `confessed` (after Ch 39/40). No mood differs before Ch 39.
- Every main-path read of an `ans.elder_councillor.*` flag has an `unset` branch.
- **Pools:** `npc.elder_councillor.*`, `talk.q.elder_councillor.<topic>`,
  `story.ch25.visit.elder_councillor.<bound|innocent>`.

### Variants

- Identical in Classic and Varied; name rolled, family name Senju.
- `twist.traitor = elder_councillor`: the bound track. Note the rotation matrix's watch item: with
  `twist.lineage = fallen`, the reveal adds only "I signed the Ash Road away too. A Jonin's death, and a
  child's."
- The player is always a clanless orphan: his Ch 1 kindness is to a stranger in every save.

## New flags

`ans.elder_councillor.stipend`, `ans.elder_councillor.debt`, `ans.elder_councillor.law`,
`ans.elder_councillor.sign`, `ans.elder_councillor.fear`, `ans.elder_councillor.pine`,
`ans.elder_councillor.vote`, `ans.elder_councillor.flat`, `ans.elder_councillor.change`, `ans.elder_councillor.proud`, `ans.elder_councillor.clans`.
