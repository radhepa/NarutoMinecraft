# `role:lost_child`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Arcs:
> [ARCS/](../ARCS/). Rules: [WORLD.md](../WORLD.md).

## At a glance

| | |
|---|---|
| Role | `role:lost_child`: the girl in the next cell (Ch 0); hollowed by the leader; Yūgure's weapon (Ch 24); deserter (Ch 44); home (N6 or Ch 47) |
| Look | **Fixed** in every save: a thin girl with a cropped dark fringe and a scar through one eyebrow; as hollow: chalk-pale, eyes flat grey, the ash-violet cloak; at home: colour returns slowly over the Road to Hokage |
| Pronouns | She / her (fixed look) |
| Name | Given Family. Her given name is rolled; her **family name** is unknown to her (and to the Leaf) until Yūgure's list is decoded (Ch 38): the nursery recorded it when she was taken. Until then the medic's records say "unknown" |
| Clan | **No clan**; a distant Kagari descendant (her chakra charred the paper) |
| Age | The player's age, a few months older |
| Archetype (after return) | Rolled from **reserved** at first, moving toward **curious** as she heals (the bond engine's personality is set to reserved at her return; her answers to your questions nudge it, see below) |
| Values (after return) | freedom, honesty → plus whatever the player helps her choose |
| Peeves | being touched without warning; being called by a number |
| Dream | At return: none ("I don't have one"); she chooses one in Ch 47/the Warm Room |
| Bond | Created at level 2 in Ch 0 with `bond_flag red_cord`; frozen while she is gone; grows from 2 after her return |
| First / last | Ch 0 / Ch 55 (the last image: a red cord tied on the stone watch-fire basket) |

## Arc

**Wants.** In Ch 0: that someone remembers she was there. Hollow: nothing (that is the horror). At
home: to find out what she likes, who she would have been, and to be called by her name.

**Fears.** Being forgotten (Ch 0). As hollow, there is only an echo of fear: being taken again. At
home: that the stolen voices are still in her; that she hurt people (she did: the border post, the
Yūgure cells in Ch 44).

**Secrets.**
- In the nursery she was "Seven". She heard the guards call you "Nine" (she never uses it: she
  hated hers).
- The leader took her chakra the night of Ch 0 to test the dark mirror on a Kagari-sensitive child;
  then cells forced stolen embers into her to make a weapon. She remembers the leader's song.
- In Ch 44 she was already hunting Yūgure cells on her own: the cord was pulling her back.
- She remembers the hideout's layout and two of the leader's hiding places (useful in Ch 49 and the
  S-ranks before Ch 51, if she is home by then).

**What she knows and when.**

| Knowledge | When |
|---|---|
| Your nursery number | Ch 0 (never said) |
| The leader's song, and that he is Kagari | Ch 0 (she tells you after her return, if asked about him) |
| That you kept the cord | Ch 24 (`bond_flag saw_cord`) |
| Yūgure's hideouts in the hills | Ch 24 on (said after return) |
| What the Undercroft wanted from her | N4 (if Night Watch) |
| The Hollow Crown | Ch 49 (as a listener; she understands it better than anyone: "That's what he did to me, but for everyone") |

**How she changes.**

| Phase | Change |
|---|---|
| Ch 0 | Brave, whispering, gives away the only thing she has |
| Ch 24 | Hollow; stops at the cord |
| Ch 44 | Breaking: "Too many voices in here. One of them is yours." |
| N6 / Ch 47 | Her own extinguished flame kindled back alive by you, through the cord's thread; home, empty and new; says Ch 0's words finished |
| Road to Hokage | Learns what she likes; asks the questions she never asked; kindles toward you in Ch 53 |
| Epilogue | Chooses a life (by her answers): the shrine's keeper, a medic's apprentice, a shinobi of your house, or a traveller who writes |

**Endings and variants.**
- **Home by Night Watch (N6)**: the fullest version; Ch 47 is *The Warm Room*. She is home by Ch 49
  and helps map the hills.
- **Home by the shrine (Ch 47)**: shorter recovery; she still asks the questions, compressed into
  Ch 47 to Ch 54.
- **Ch 0 words** (`ans.lost_child.cell`) return in Ch 24 and N6/Ch 47: *remember* → "You
  remembered"; *find* → "You found me. You said you would."; *silent* → "Someone remembers. You did."
- **Ch 44** (`ans.lost_child.echo`): *follow* opens the Night Watch lead (the cloth strip to the
  Shimura house); *protect* keeps your Genin safe and she says nothing more.
- **Ch 53**: if home and at `friendship 6`, her flame comes before the instructor's: "So someone
  remembers." If home but under 6, she watches, and in the epilogue says she wishes she had.
- She **cannot die** in the story after her return; before it, she always escapes.

## Dialogue brief

### Voice

- **Ch 0 (child):** a whisper, fast, practical, fierce. No self-pity. "Here." not "Please take this."
- **Hollow (Ch 24, 44):** flat, toneless, repeats phrases others said near her (the leader's "little
  flame", a guard's "Up.", a child crying "Mama") and sometimes *your* Ch 0 words. Never her own
  sentence until the cord. This is a deliberate effect: her hollow pool is built from other
  characters' lines.
- **Home (teen or adult, depending on when):** slow, plain words, long pauses; asks a lot of
  questions; literal (jokes take her a beat); laughs suddenly and is surprised by it. Grows warmer
  and quicker over the arc.
- **Never:** says her nursery number; lies; says "I'm fine" (she says what she feels, flatly: "I am
  frightened").
- **Tics:** touches her bare wrist where the cord used to be (the cord stays with you until
  `ans.lost_child.cord` in Ch 54); counts the doors in every room.

Voice samples, not shipped lines:
- (Ch 0) "They're taking me tonight. Here. So someone remembers I was here."
- (hollow, Ch 24) "Up. Little flame. Up. ...I'll remember."
- (Ch 44) "Too many voices in here. One of them is yours."
- (home) "What's this called? Ramen. Do I like ramen? ...I think I like ramen."
- (home, later) "{player}. Say my name again. I want to hear it in your voice."
- (Ch 53) "So someone remembers. Take it. It's mine to give."

### Topics she cares about (after return)

| Depth | Topics |
|---|---|
| 0 to 2 | Names of things, food, the weather ("Is rain always this loud?"), the village's sounds |
| 3 to 4 | The nursery (only if she starts it); the other children; your life in the years she missed |
| 5 | Values: being honest even when it's ugly; being free to leave a room |
| 6 | The dream she chooses |
| 7 | Worries: the voices; what she did to the border post; the leader |
| Shared memory | The cell, the cord, the shrine fire, her first bowl of ramen |

### Never reveal before

| Secret / fact | Gate |
|---|---|
| Her own name, spoken by her | Her return (before it, others say it: the medic's records in Ch 25 list her as "unknown"; the name token is first used by her) |
| Her nursery number | Never |
| What the leader did, in detail | After return, level 5, and only if you ask (pried before it) |
| The leader's hiding places | After return (Ch 49 or before) |
| That she hunted cells in Ch 44 | After return |

### Questions for the player

She asks the questions she never got to ask anyone. Most come after her return (N6/the Warm Room,
or compressed into Ch 47 to 54). Her answers to *you* (the player's choices) shape what she becomes.

| Id | When | Question | Options | Honours / tests | Remembered | Changes her |
|---|---|---|---|---|---|---|
| `ans.lost_child.cell` | Ch 0.2 | (your reply to the cord) | I'll remember / I'll find you / say nothing | honesty | Ch 24, N6/Ch 47 | Her first words to you at home |
| `ans.lost_child.echo` | Ch 44.2 | (your reaction) | follow her / protect the Genin | — | Night Watch lead | — |
| `ans.lost_child.name` (new) | Home, first day | "Did you know my name? Before?" | no, I'm sorry / I asked the medic / I called you "the girl with the cord" | honesty | Every greeting after: she uses the name you gave her back to you ("Cord-keeper", if the last) | Small; how she names you |
| `ans.lost_child.what_like` (new) | Home, first week (L2) | "What do people *like*? How do you know?" | you try things / you watch what makes you forget the time / you ask a friend | freedom, curiosity | Her personality shift: *try* → adventurous; *forget time* → imaginative; *ask a friend* → warmhearted (`Personality` nudged 0.2 toward it) | Her archetype drifts |
| `ans.lost_child.voices` (new) | Home, L3 | "Some nights I still hear the voices. Will they go?" | yes, in time / maybe not, and you'll learn to live with them / I'll sit with you until they do | honesty, kindness | Ch 53 (if *I'll sit*: "You sat with me. I'll stand with you.") | Her nights: a ritual (`ritual` stargazing on the Rock) if *I'll sit* |
| `ans.lost_child.blame` (new) | Home, L5 | "I hurt people at the border post. Your friend. Do they hate me?" | no / ask them yourself / yes, and that's theirs to give up | honesty | A scene with the teammate who fell in Ch 24 (if *ask them*: a reconciliation between them, a `reconciled` moment for both) | Whether she faces it |
| `ans.lost_child.leader` (new) | After Ch 49, L5 | "He sang to me. The same song you know. Was he ever good?" | once, before they burned his home / no / maybe that's not the question | honesty | Ch 54 leader's name choice (she says her view) | Her mercy or her hardness |
| `ans.lost_child.dream` (new) | Ch 47 or later, L6 | "I think I want something. Is it allowed, to want things this late?" | yes: what is it? / it's never late / you can want many things | freedom | Epilogue: she chooses between shrine keeper (if she spent time at the shrine), medic's apprentice (if her bond with the medic is 4+), shinobi of your house, traveller | Her dream is set |
| `ans.lost_child.cord` (new) | Ch 54 Morning | "Do you still have it? The cord?" | give it back / keep it / tie it on the shrine basket together | — | The epilogue's last image (the basket is the default; *give back*: she wears it; *keep*: you do) | The last image |

### What her lines are for

- **Functions:** the story's emotional frame (first image, last image), horror (the hollow voice:
  what the dark mirror does), mercy and recovery (the gift rekindling a flame that went out), clue (the hideouts,
  the leader's song), and the theme's question 3 (are you what you were made, or what you choose?).
- **States:** hollow (no bond pool; the echo pool), deserter (Ch 44, terse, frightened), home
  (recovering: a staged greeting pool by weeks since return, not just level).
- **Pools needed:** the echo pool (built from other characters' lines with permission tags);
  home greetings by recovery stage and level; topics; hangouts (shrine visit, stargazing, market
  stroll, ramen); life events (first snow, a nightmare, a small proud moment, choosing a dream).

### Variants

- She has a **fixed** look and role; no archetype skin. Her post-return personality is driven by the
  player's answers (`ans.lost_child.what_like`).
- **Age at return:** if home through Night Watch during the Jonin arc, she is an adult; if home in
  Ch 47, also an adult. Her voice is an adult who missed a childhood: plain, curious.
- **Romance:** possible only after return, as adults, and only after her `ans.lost_child.dream` is
  answered (she must have chosen something for herself first). Gated by level 7 and the usual
  chemistry.

### Thread Sight and her

- **Hollow (Ch 24, Ch 44):** when your Thread Sight opens in Ch 24, she has no threads at all, to
  anyone: except one, grey and thin, from your wrist to hers, along the red cord. It is the only
  reason the kindling of her flame is possible later.
- **The return (N6 / Ch 47):** you do not give her chakra to keep; you push your flame along that
  one thread until her own extinguished flame catches again, and the stolen embers forced into her
  have nowhere to stay. Her thread turns from grey to her own colour (a pale copper).
- **After:** her threads to other people appear one by one, a visible measure of her recovery
  (the medic, the teammate who fell, your house). A flicker on her thread means she is hiding a
  bad night (the voices); she tells you if you wait.

## New flags

- `story.lost_child.family_known` (Ch 38, from the decoded list)
- `ans.lost_child.name` (didnt_know / asked_medic / cord_girl)
- `ans.lost_child.what_like` (try / forget_time / ask_friend)
- `ans.lost_child.voices` (in_time / live_with / sit_with)
- `ans.lost_child.blame` (no / ask_them / theirs)
- `ans.lost_child.leader` (once / no / not_the_question)
- `ans.lost_child.dream` (what_is_it / never_late / many)
- `ans.lost_child.cord` (give_back / keep / basket)
- Option ids for existing: `.cell`: `remember`, `find`, `silent`; `.echo`: `follow`, `protect`
