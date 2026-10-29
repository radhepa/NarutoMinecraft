# `role:elder_keeper`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Backstory:
> [WORLD.md](../WORLD.md). Twist slots: [ROTATIONS.md](../ROTATIONS.md).

## At a glance

| | |
|---|---|
| Role | `role:elder_keeper`, the council elder who keeps the archive under the Rock |
| Look | Fixed: a tall, thin old man (~60), shaved head, a long grey archivist's coat with ink-stained cuffs, a ring of old iron keys on a cord at his belt, one cloudy eye |
| Pronouns | He / him |
| Clan | No clan (an archivist's family with an ordinary family name from the pool; Given Family order) |
| Rank | Jonin (retired), elder of the council |
| Archetype | `stern` (warmth −.1, bold .3, pride .4, discipline .9, open −.5) |
| Values | duty, loyalty (to the Third's oath; slowly, to the truth) |
| Peeves | recklessness, lateness |
| Dream | "protect the village" as he was taught; under it, to be forgiven for keeping quiet |
| First appearance | Ch 1 (at the Fourth's shoulder) |
| Last appearance | Ch 51b (at the archive door, overwhelmed, he hands the player the keys and dies); remembered Ch 54, Ch 55 |

## Arc

**Wants.** To keep the oath he swore to the Third at twenty: the archive stays shut, the peace stays
whole. Underneath, from the moment he sees the player's flare (Ch 3), he wants something he cannot
admit: for someone to make him open it.

**Fears.** That the truth told carelessly will set the clans on each other and Yūgure will walk in
through the crack. That he is a coward who called it duty. That the child he watches will become
what the Valley of Ash made of one Kagari.

**Secrets.**
- He knows the Quiet Ending in full: the fourth clause, the forged report, the renaming list, the
  Hearthstone. He has known for forty years.
- He signed the sealing of the Ash Road report (~Y-8), with the councillor, hiding that Yūgure
  killed `fallen_parent` for their blood.
- He received the anonymous map that led to the raid in Ch 0 (from the second; he never learned who).
  He chose the captain for the raid.
- He asked the councillor to arrange the player's stipend personally (this is true in every save;
  in the councillor-bound save the councillor had his own reasons too).
- He noticed the renamed descendants' flames returning (~Y-15) and has kept a private list of
  flickers. The player's name went on it the night of Ch 3.

**What he knows and when.**

| When | Knows |
|---|---|
| Ch 0 | That an unsigned map put children in a Yūgure camp near the old shrine. Suspects Kagari blood in the camp |
| Ch 1 | Sees the player; suspects nothing yet beyond "a nursery child" |
| Ch 3 | Sees the flare through the window: knows the player is a Kagari descendant with an unsealed flame |
| Ch 4 | Knows someone tried the archive door (he was checking the seals that night). Does not know who |
| Ch 19 | Hears "Kagari" was said. Knows Yūgure knows what the player is |
| Ch 28 | Knows of the porter and the voice; suspects every candidate, including himself as a suspect in others' eyes |
| Ch 35 to 36 | With the list, gives up the silence. With the Classic Uzumaki sealing master (`role:sensei_5`) he breaks the archive's old seals |
| Ch 51b | Knows the leader wants the Hearthstone; holds the door alone until he is overwhelmed |

**How he changes.**

| Arc | He is |
|---|---|
| Cinders (beta) | A shadow: watching, warning, lying badly. The player's first suspect if they think like a detective |
| Paper Trail | Absent except as a figure at council; he appears at the memorial stone once at night (Ch 10, after the sensei leaves, if the player lingers) |
| Dusk over the Stadium | Near the Hokage's seat when the attack begins, then at the archive door all night while the village burns: he guards the door, not the people, and knows it |
| Embers | Begins to speak, one fact at a time. Names the gift if the librarian cannot (Ch 25). Asks to walk with the player (Ch 32, at trust 40) |
| Ashes | Opens the archive (Ch 36), reads the Third's letter aloud (the chapter ends on it), reads the Ash Road report on its own night (Ch 37.0), decodes the cipher (Ch 38; the matching is the player's, at the case board with `role:sensei_4`, who never gives answers), stands beside the player at the council (Ch 40) |
| The Last Bonfire | Grants the old ground's records for the restored house (Ch 46). Holds the door alone in Ch 51b; overwhelmed by the time the player reaches it, he hands them the keys and dies |

**Ending.** In Ch 51b (after the gate, the crossing and the blade's last duel) the player reaches the
archive door. The keeper has held it alone against a Yūgure hearth and is overwhelmed; the hearth has
the Hearthstone. He presses the archive keys into the player's hand and says one last line, the only
version: "Someone has to keep it open now. Not closed. Open." If `ans.elder_keeper.forgive` is set, he
adds one sentence before it ("You said once they speak. I spoke." / "Let them help." / "It wasn't
yours to give. Thank you for not giving it."). He dies there. His keys hang in the restored house's
hall (or the archive, if the player founded their own clan). In the epilogue the archive has a new
keeper the player chose (Ch 55: the librarian if innocent and free, the descendant genin_3, or the
cleared councillor).

**The red herring, on purpose.** He looks like the voice in the beta: he watches too closely (Ch 1),
he is at the window (Ch 3), he is at the door the figure vanished by (Ch 4), he lies ("No one comes
here"). Every one of these has its true reason above. He is **never** the voice in any save, and
the case board (Ch 38) never lets the player accuse him: his name is not among the four sources.
A player who suspected him aloud (`story.suspected.keeper`, from talking to the sensei or the
instructor in the Chunin arc) gets a dry line in Ch 36: "You thought it was me. Good. So did I, some
nights."

## Thread Sight and the keeper

From Ch 24 the player can see bonds as threads of light. If the keeper is bonded to the player at
6 or more and the player probes him before Ch 36, his thread shows the steady flicker of someone hiding
something (`hides:archive`; he is). It is never a lie detector. This deepens the red herring honestly: the flicker says *that*, never
*what*, and the four candidates flicker too ([ROTATIONS.md](../ROTATIONS.md)). After Ch 36 his
flicker is gone; a player who watched it vanish gets his line: "There. Nothing left in me to hide."

## Dialogue brief

### Voice

- **Register:** formal, clipped, old-fashioned; full sentences with no wasted words; no contractions
  in the beta, a few creep in once he trusts the player.
- **Habits:** answers questions with instructions ("Go home."); touches his key ring when lying or
  afraid; calls the player "child" until Ch 33 (Jonin), then by their given name, never by title.
- **Tics:** counts things under his breath (seals, steps, years). Quotes the Third without naming her
  ("Someone wiser than me said...").
- **Never says:** "Kagari" before Ch 36; anything kind in front of others before Ch 32; "I'm sorry"
  until the Third's letter has been read (Ch 36), and then he says it once, plainly.

*Voice samples, not shipped lines:*

- (Ch 4) "Go home, child. This door is not for you, and neither is the night."
- (Ch 25, naming the gift) "Your fire has an old name. I was told it once by a woman who made me
  promise never to say it. I am breaking that promise because you are lying in a hospital."
- (Ch 32) "Come to me when you are a Jonin. I will show you a door. Be on time."
- (Ch 36) "Forty years I have been the only one who knew this, {given:player}. It is not a thing
  a man should know alone."
- (Ch 51b, his one last line) "Someone has to keep it open now. Not closed. Open."

### Topics they care about

| Depth | Topics |
|---|---|
| Levels 0 to 2 | Punctuality; the village's records; whether you are where you should be at night |
| 3 to 4 | The Third (as "my teacher"); old handwriting; the memorial stone and who visits it |
| 5 to 6 | Duty against conscience; what a secret costs the one who keeps it; the Ash Road (only from Ch 37.0) |
| 7+ | His fear that he is a coward; what the archive should become; who should keep it after him |

### Never reveal before

| Secret | Gate |
|---|---|
| That he received the Ch 0 map | `story.ch36.done` |
| The word "Kagari" | `story.ch36.done` (he uses "your fire" or "the old name" before) |
| What is behind the door | `story.ch36.done` |
| The fourth clause, the forged report, the renaming list, the Hearthstone | `story.ch36.done` |
| That he signed the Ash Road sealing | Ch 37.0 (the report's own night, after the archive chapter) |
| That he asked the councillor to arrange the stipend | `story.ch36.done`; in a councillor-bound save he tells it in Ch 39 as part of the reveal |
| His list of flickers (descendants) | `story.ch37.done` |
| Which candidate he suspects | Never: he refuses to guess aloud ("I have been wrong about people for forty years") |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | How it changes him |
|---|---|---|---|---|---|---|
| `ans.elder_keeper.door` | Ch 4 | (Player asks; his reaction is the beat) | What's behind it / Someone was here / leave | "Someone was here" tests his honesty and frightens him (he lies) | Ch 36: "You told me someone had been at my door. You were right, and I said no one comes here." | "Someone was here" makes him check the seals every night after; in Ch 36 he credits the player with the first warning |
| `ans.elder_keeper.late` | Ch 32 (the walk, trust 40) | "Is it worse to tell a truth too early, or too late?" | Too early: it hurts people unready / Too late: the hurt grows in the dark / Never is the worst | Too late honours conscience over duty; too early honours his old duty | Ch 36: he quotes it opening the door | "Too late" or "never" and he opens the archive himself in Ch 36 even below the trust gate (if trust ≥ 50) |
| `ans.elder_keeper.oath` | Ch 33 (after the trial, a level-5 talk) | "If you swore an oath to someone you loved, and the oath was wrong, would you keep it?" | Keep it; an oath is an oath / Break it and tell them why / Keep it until it hurts someone, then break it | Tests duty against honesty | Ch 37.0: "You said until it hurts someone. It hurt someone on the Ash Road". Unset: he reads the report without comment | Shapes which line he reads the Third's letter with (relief / shame / grief) |
| `ans.elder_keeper.who_keeps` | Ch 38 (case board, level 6) | "When I am gone, who should keep the archive?" | Nobody; open it / Someone who will read it aloud / You, as long as you can | Tests his fear of his own end | Ch 55: the archive's next keeper (the player picks); unset default: the Seventh appoints the librarian if innocent and free, else genin_3 | "Nobody" makes him leave the archive door unlocked in his will |
| `ans.elder_keeper.forgive` | Ch 40 (after the council, level 6) | "Should the village forgive the people who kept quiet?" | Yes, once they speak / No, but it should let them help / It's not my forgiveness to give | Asks for himself without saying so | Ch 51b: the one-sentence addition before his last line (see Ending); unset: no addition | The answer is the last thing he asks about |
| `ans.elder_keeper.third` | Ch 36 (after the letter) | "She asked whoever reads it to say it for her. Will you?" | Yes, all of it / Yes, but my way / Say it with me | Duty handed on | Ch 40 testimony line; unset: he speaks second | "Say it with me" makes him stand and speak first at the council (40.2) |
| `ans.elder_keeper.valley` | Ch 36 (the Valley of Ash, scene 36.5) | "One man did that. Should his whole clan have paid?" | No, never / No, but I understand why they were afraid / The village should pay now | Tests the player's view of collective guilt | Ch 54 (the leader's name): he is dead, but his notes on the archive desk quote it | Feeds the player's council testimony options |
| `ans.elder_keeper.night` | After Ch 4 (level 1, if met at the door) | "Why were you out so late? Children sleep." | I couldn't sleep / I was chasing someone / Why were *you* out? | Tests the player's honesty; the last answer tests him | Ch 32 walk: "You asked me why I was out. I was guarding a door from you" | "Why were you" makes him avoid the player for the rest of the beta (a stronger red herring) |
| `ans.elder_keeper.stone` | Paper Trail, level 2 (at the memorial stone at night, after Ch 10) | "Do you know why names go on stone?" | So they're remembered / so they can't be changed / so someone has to look at them | Duty; the third option is his guilt | Ch 41 re-carving: he stands by the gap and repeats your answer | "Can't be changed": in Ch 41 he says "I was wrong; they can. That's worse, and better" |
| `ans.elder_keeper.afraid` | After Ch 19 (level 2, at the archive door the morning after the attack) | "Were you afraid, in the stadium?" | Yes / No / Only for my friends | Small confession invited; he admits he stayed at the door | Ch 37.0, after the Ash Road report: "I asked if you were afraid. I'll tell you: I was, the whole night, at a door." Unset: he says only the second half | "Only for my friends": he begins to trust the player (trust +) |
| `ans.elder_keeper.teacher` | Embers, level 4 | "Who taught you the most? Not the most jutsu. The most." | My sensei / the camps / my friends / you, maybe | His past: the Third; "you, maybe" disarms him | Ch 36 (before the letter): "She taught me the most. Mostly what not to do" | "You": he gives the player his old archive ledger pen (a keepsake) |

### What their lines are for

- **Functions:** red herring (beta), warning (beta), exposition of the backstory (Ch 36 to 38),
  conscience made visible (Chunin to Jonin), farewell (Ch 51b).
- **Mood states:** `guarded` (until trust 40), `testing` (40 to 59), `confiding` (60+ or after Ch 36),
  `grieving` (after Ch 40).
- **Pools:** `npc.elder_keeper.greet.<state>`, `talk.q.elder_keeper.<topic>`, the `bond.greet.level.*`
  overrides (he never says the warm generic lines).

### Variants

- Identical in Classic and Varied (fixed look, fixed role); name rolled.
- `twist.traitor`: he is never bound. In a councillor-bound save his betrayal by an old colleague is a
  second blow in Ch 39 ("I asked him to keep you safe. He kept you on file"). In a librarian-bound
  save he names the gift alone in Ch 25 and teaches what the archive keeps of how the Kagari kept the flame (the watch-fire practices, the songs), never the abilities themselves.
- `twist.lineage = fallen`: in 37.0 he says the Ash Road dead Jonin's name and looks at the player
  a moment too long; he suspects, and says nothing (the reveal is the Seventh's).
- Ch 36's opening reads `bond_meter [elder_keeper, trust, 60]` and `friendship [elder_keeper, 6]`.

## New flags

`ans.elder_keeper.late`, `ans.elder_keeper.oath`, `ans.elder_keeper.who_keeps`,
`ans.elder_keeper.forgive`, `ans.elder_keeper.third`, `ans.elder_keeper.valley`,
`story.suspected.keeper`, `story.ch36.done`, `story.ch37.done`. Also: `ans.elder_keeper.night`, `ans.elder_keeper.stone`, `ans.elder_keeper.afraid`, `ans.elder_keeper.teacher`.

Every main-path read of an `ans.elder_keeper.*` flag has an `unset` branch (a neutral line).
