# `role:teammate_a`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Arcs:
> [ARCS/](../ARCS/). Rules: [WORLD.md](../WORLD.md).

## At a glance

| | |
|---|---|
| Name | Given Family (`{name:role:teammate_a}`); Classic family name Kurama (the clan's name), given name rolled |
| Role | `role:teammate_a`: classmate (Ch 1), your paired-exercise partner (Ch 3), squadmate (Ch 8 on) |
| Look | Classic: curated (a Kurama, ink-stained fingers, a brush behind the ear). Varied: rolled from the four classmates |
| Pronouns | Rolled: *they* here; dialogue uses `{they:role:teammate_a}`, `{them:…}`, `{their:…}` |
| Clan (Classic) | Kurama (a household of genjutsu painters) |
| Rank | Academy → Genin (Ch 7) → Chunin (Ch 20) → Jonin (Ch 33); a sensor captain or a painter-shinobi by Ch 30's choice |
| Archetype | Classic: **shy** (warmth .5, boldness -.7, pride -.4, discipline .2, openness -.6) |
| Values | creativity, kindness |
| Peeves | rudeness, nosiness |
| Dream | Classic: "master their art": to paint the village as it really is, so nobody looking at it can be looked past |
| First / last | Ch 1 (drawing in a margin) / Ch 55 (the epilogue: the mural, or a portrait of the new Hokage) |

## Arc

**Wants.** To be *seen* without having to stand up and shout. To make something that makes
people stop.

**Fears.** Being invisible (everyone looks past them); freezing when it matters and someone getting
hurt because of it (Ch 16). Later: being made into a tool (the sensor corps, their family's plans).

**Secrets.**
- They felt the flare in Ch 3 from the inside: "a warm room". They have never felt anything like
  it and have been quietly drawing it ever since: a small room with a fire in it fills the back of
  their sketchbook. (Shown to the player at level 6, or after Ch 25.)
- Their family wants them to give up painting for "real" genjutsu (the Classic Kurama household;
  in Varied, the family's version of it, see Variants).
- From Ch 24 (if they are the one who fell): they were terrified, and moved anyway. They will tell
  only you.

**What they know and when.**

| Knowledge | When |
|---|---|
| Your chakra did something strange in the exercise | Ch 3 (`story.seed.flare`) |
| It is a secret between you | Ch 3, if `ans.teammate_a.flare` = yes or dont_tell (`bond_flag flare_secret`) |
| The cord flicker was the same thing | Ch 8, the cord test (`story.seed.cord_flicker`; they saw it; they say so only if the flare is shared: the line is in [ARCS/2_paper_trail.md](../ARCS/2_paper_trail.md) 8.3) |
| The paper chars around you | Ch 11 if you showed them (they say so at 14.3); Ch 23 if you let the squad hear the tester (`bond_flag knows_flame`) |
| Your gift is real and has a name | Ch 25 (if they fell, they saw it; otherwise the squad learns at Ch 25) |
| Kagari, the archive, the purge | Ch 40 (with the village) |
| Your lineage | Ch 48, if you tell them (a talk topic opens: "your parent") |

**How they change.**

| Arc | Change |
|---|---|
| Cinders | Hides behind the sketchbook; the flare gives them a secret worth keeping, and a friend to keep it with |
| Paper Trail | Shows a painting in public for the first time (bond quest 1); says aloud what they're afraid of (the campfire) |
| Dusk | Fears freezing; asks if you'd forgive them |
| Embers | Does not freeze (Ch 24, if they fall); chooses (or is pushed into) the sensor corps (Ch 30) |
| Ashes | Paints the Kagari memorial mural (Ch 41): the first time their work is the village's |
| Last Bonfire | Hides the war's work in paint (Ch 50, 51a.5); kindles toward you without being asked (Ch 53); their line answers the fear you told them in Ch 11 |

**Endings and variants.**
- **Who fell in Ch 24.** If teammate_a fell: they lie hurt in the burning post; your Thread Sight
  opens and the first thread you ever see is theirs, bright and steady. You push your chakra into
  them; they rise for one moment and cast their *own* painted genjutsu past its limits: it swallows
  the whole post, and the hollow girl stands inside a painting of the border post as it was before
  it burned, long enough for the two of you to finish the fight together. Their Ch 24.4 fall line is
  taken from the **Ch 24 line table** below (the arc cites it). They gain
  a permanent `saved_by_them` memory toward you and a `trained_together` streak in the secret
  training. If someone else fell: they arrive at the hospital last and say they should have been
  faster.
- **Ch 24 line table** (teammate_a falls; first matching row wins). In every save they shout "Get down!"
  as they step in front of you, the one time they ever shout; the fall line follows:

  | Priority | Reads | Fall line (24.4) | If `bond_flag knows_flame` (Ch 23), add |
  |---|---|---|---|
  | 1 | `ans.teammate_a.your_fear` = taken | "Nobody's taking you—" | "I knew. Since the school. Do it." |
  | 1 | `your_fear` = alone | "You won't be alone—" | same |
  | 1 | `your_fear` = nobody | "You're not nobody, you're—" | same |
  | 1 | `your_fear` = fire | "It's not that kind of fire—" | same |
  | 2 | `ans.teammate_a.freeze` set (any) | "I didn't freeze. See? I didn't—" | same |
  | 3 | unset (neither) | "I'm right here—" | same |

  Ch 25.2: "That was the warm room again" (flare shared) / "I knew it would be you. I didn't know it
  would feel like that" (`knows_flame`, not shared) / "So that's what it was" (neither).
- **Ch 53 line table** (teammate_a speaks in slot 4 if they fell in Ch 24, or if the sensei fell and a is the higher
  teammate; else slot 5; once only, per the speaking rule in DIALOGUE_BRIEFS; one line;
  the arc cites this table):

  | Reads `ans.teammate_a.your_fear` | Line |
  |---|---|
  | alone | "You told me once you were afraid of being alone. Look how many of us there are." |
  | taken | "Nobody takes you. We give." |
  | nobody | "Nobody? Look how many of us know your name." |
  | fire | "This is the good kind." |
  | unset | "Here. All of it. It's yours." |

- **Fixed main-path beats (every save):** in Ch 50 their painted genjutsu hides the anchor-breakers'
  work from Yūgure's watchers (a street that looks untouched while you dig); in Ch 51a.5 it hides the
  second line squad3_a builds behind the broken gate, long enough for it to hold.
- **A falling-out with teammate_a** is mended by the story at the Ch 41 unveiling if the player comes
  (`mend`; they hand you the corner of the cloth without a word). If the player stays away, or a falling-out begins after
  Ch 41, it is mended at Ch 49.5, where they bring their genjutsu plan to you, not to the Seventh (`mend`).
  Both mends also carry `return_to_squad` if the falling-out took them out of the squad: a mended
  teammate_a is back in the squad, and their squad lines return.
- **If teammate_a is out of the squad** (a falling-out, or a low bond; a low-bond departure has no story mend, only the systemic return quest: neglect has a cost, and slot 5 of the Ch 53 rule records it): a stand-in from
  Squad 2 (classmate_c, else classmate_d) takes their squad lines in Ch 31 (the drain's story floor links everyone present, the stand-in included), Ch 35, Ch 45 and Ch 50. Whether they speak in Ch 53.2 follows
  slot 5 of the speaking rule in DIALOGUE_BRIEFS (with the squad hold, SYSTEMS.md §3).
- **Thread Sight on them** (from Ch 24, level 6+): a steady flicker while they carry a `hides:`
  bond flag (never line by line, never a lie detector): `hides:warm_room` (the drawings, until shown), `hides:corps` (Ch 30, until they ask you),
  `hides:portrait` (romance, until the confession). You see *that*, never *what*; asking before they
  offer is prying.
- **Unison technique (Blaze tier, Ember Link): "Ink Dawn".** You hold the squad's shared flame
  while they paint; your ember-gold chakra becomes their paint, and the genjutsu they cast is a
  sunrise over the whole field that every enemy inside sees as their own home burning down to dusk,
  then dawn. Enemies stop to watch it; allies see only warm light. It is the one illusion they ever
  make that is about hope.
- **Ch 30 corps choice** (`ans.teammate_a.corps`): *join if you want* → they ask for time and choose
  painting first, corps second (a part-time sensor; Ch 50 they find anchors by feel). *Don't let them
  choose for you* → they refuse the corps; a quarrel with their family (a life event: "a quarrel
  with family", comfortable to comfort) and a painter-shinobi path. *Join and keep your eyes open for
  us* → a sensor captain by Ch 33; in Ch 38 they stand the sensor watch over the case-board room.
- **The mural (Ch 41)** reads `ans.teammate_a.paint`: *are* → the Kagari faces as the archive
  describes them, burned shrine and all; *should* → the same faces at the Leaf's festivals, as if
  they had never left; *both* → two panels, and they ask you which goes on the left. It reads
  `ans.teammate_a.show`: *brave* → they unveil it; *foolish* → they ask you to; *both* → they hold the
  cloth with you. **Unset**, each flag on its own: `paint` unset → both panels, and they ask
  you which goes on the left; `show` unset → they unveil it, with you beside them. This list is the one
  statement of the mural's reads (ARCS/5 41.2 points here).
- **Romance** (teen and up, if chemistry allows): dating moves the painting hangout to *their*
  studio; the confession (level 8) is a painting of you they never finished in public (the Kurama
  custom: "a painted eye is never finished in public"). If you date them, `teammate_b` gets the
  squad-dinner scene (ARCS/5_ashes.md).
- **A falling-out** (any route BONDS.md §9 allows, until the squad hold from Ch 49's end): they leave
  the squad (BONDS §7); they still paint the memorial and do not invite you, but the unveiling is
  public, and coming anyway mends it (41.2).

## Dialogue brief

### Voice

- **Child (Beta):** quiet, short sentences that trail off; starts with "Um" or a small apology;
  describes feelings as pictures ("like a warm room", "like ink in water"); goes silent instead of
  arguing. Brave only in what they draw.
- **Teen (Chunin):** still soft but finishes sentences; dry, private jokes aimed only at you; talks
  about colour and light when nervous.
- **Adult (Jonin+):** calm, precise, sometimes startlingly direct; still frames everything in
  images; teaches children to paint at the memorial.
- **Never:** shouts (except once: Ch 24, "Get down!"); boasts; mocks anyone's work; says "I'm
  fine" when they aren't, to you (they say "I'm... it's a grey day").
- **Tics:** apologises before disagreeing; wipes ink on their sleeve; counts colours under their
  breath.

Voice samples, not shipped lines:
- (child) "Um. Sorry. Did you feel that too? It was like you were inside my chakra. Like a warm room."
- (child, campfire) "Everyone looks past me. Like I'm a wall with nothing painted on it."
- (teen, Ch 30) "They want me to read people for the corps. I'd rather paint them. Is that selfish?"
- (teen, after Ch 24) "I didn't freeze. I want you to know that. I was so scared, and I didn't."
- (adult, Ch 41) "{player}. Hold the other corner. If they hate it, they hate it with both of us."
- (adult, Ch 53) see the Ch 53 line table.

### Topics they care about

| Depth (level) | Topics |
|---|---|
| 0 to 2 | Paint, colours, the light on the Rock, what the instructor said; the weather as colours |
| 3 to 4 | Their family's expectations; the Kurama studios; other people's art (they are generous) |
| 5 | Values: being kind about other people's work; the difference between seeing and looking |
| 6 | Their dream; the warm-room drawings |
| 7 | Worries: being used, freezing, that you'll leave them behind when you're strong |
| Shared memory | The overlook painting (B1), the tea-house painting (B2.1), the campfire |

### Never reveal before

| Secret / fact | Gate |
|---|---|
| That the flare felt like "inside" your chakra | Ch 3 (they ask; never volunteered to others) |
| The warm-room drawings | `friendship 6` or `story.kindling.awakened` |
| Their fear of being invisible | Ch 11 campfire (`friendship 5`); or level 7 topic |
| Anything about your gift to anyone else | Never, unless the player broke the flare secret first |
| The word "Kagari" | Ch 40 (they don't know it before) |
| What a Thread Sight flicker on them means | Never told by the game; only by their own later confession |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes them |
|---|---|---|---|---|---|---|
| `ans.teammate_a.flare` | Ch 3.4 | "Did you feel that too?" | yes / no (you imagined it) / don't tell anyone | yes, dont_tell honour honesty and trust; *no* tests it (a small `rude`-sized sting for the shy) | Ch 8.3 cord flicker line; Ch 25.2 "warm room" (if they were the friend who fell) | Sharing makes them your keeper of secrets; denial makes them doubt their own senses until Ch 24 |
| `ans.teammate_a.paint` | B1 bond quest (L2) | "Should a painting show things as they are, or as they should be?" | are / should / both | creativity either way | Ch 41 mural | Their style for life: realist, hopeful, or both |
| `ans.teammate_a.your_fear` | Ch 11 campfire (L5) | "What are *you* afraid of?" | being taken again / being alone / being nobody / fire | Your honesty (any answer is a `heart_to_heart`) | Ch 24 fall line; Ch 53 flame line | They become the friend who guards against *your* fear: watches doors (taken), always comes (alone), names you to others (nobody), learns water/earth safety (fire) |
| `ans.teammate_a.show` | B2 bond 1 (L4) | "Is it brave to let people see what you made, or just foolish?" | brave / foolish / both | creativity, kindness | Ch 41 unveiling | Whether they stand in front of their own work |
| `ans.teammate_a.family` | B2 bond 2 (L5) | "If your family wanted you to be someone else, would you?" | yes, for them / no / I'd try to be both | family vs freedom (the shy value kindness: no answer offends) | Ch 30 corps choice | Frames how they hear the corps offer |
| `ans.teammate_a.freeze` | Ch 16 night watch (L5) | "If I froze, and you got hurt, would you forgive me?" | always / there's nothing to forgive / I'd be angry, but yes | honesty valued; *angry but yes* earns respect (+) | Ch 24 if they fall: "I didn't freeze"; Ch 25 | *always*: they relax; *nothing to forgive*: they cry a little; *angry but yes*: they train harder, and say so |
| `ans.teammate_a.corps` | Ch 30.3 | "The corps wants me. What should I do?" | join if you want / don't let them choose for you / join, and keep your eyes open for us | freedom or loyalty | Ch 33 rank, Ch 38 sensor watch, Ch 50 anchors | Their career (see Variants) |
| `ans.teammate_a.colour` (new) | Hangout: painting at the overlook (L3, any arc) | "If you were a colour, which one?" | the red of the cord / ash-grey / the green of the Leaf / whatever you'd paint me | creativity (filler with a payoff) | Their portrait of you (Ch 55 epilogue, or the confession painting) uses it | Small: sets your colour in their art |
| `ans.teammate_a.seen` (new) | Chunin, level 6 talk (dream) | "Do you think I'd still be me if nobody ever saw my paintings?" | yes, you paint for you / no, art needs eyes / I'd see them | creativity / kindness | Ch 41: whether they sign the mural | *yes*: unsigned mural; *no*: signed large; *I'd see them*: signed small, with a mark only you know |
| `ans.teammate_a.used` (new) | Jonin, level 7 (worries), after Ch 36 | "The founders used a whole clan's gift and then erased it. Are we using you, when we fight beside you?" | no, I'm choosing / sometimes, and that's all right / yes, so watch me | honesty, kindness | Ch 55.5 epilogue line ("You said you were choosing. I watched. You were.") | Settles their fear of being a tool by seeing you choose |
| `ans.teammate_a.squad` (new) | Ch 8, after the cord test (three watch-fire tags on one plain hemp cord) (L3) | "Why did you hand me the cord's end? You could have tried alone." | because we pass together / because you were there / because you'd have done it for me | kindness, loyalty | Ch 16 night watch (they say they've thought about it since) | Their first belief that they're chosen, not just near |
| `ans.teammate_a.hurt` (new) | Life event after Ch 24 (injured; comfort at L5) | "My hand shakes when I hold the brush now. Should I stop for a while?" | rest, the brush will wait / paint the shaking / paint with your other hand, I'll hold the paper | creativity | Ch 41 (the mural has a shaky line they kept, or doesn't) | How they carry the injury |
| `ans.teammate_a.secret_kept` (new) | Chunin, level 7 (after Thread Sight sees their flicker) | "You can see I'm hiding something, can't you. Do you want to know?" | only when you want to tell me / yes / I already know it's about me | honesty, privacy (asking "yes" is pried if under 7) | Romance confession, or the warm-room sketchbook shown | Teaches them that hiding from you is allowed |
| `ans.teammate_a.after` (new) | Road to Hokage, Ch 46 hangout at the shrine | "When this is over, will you still have time to sit for a portrait?" | always / only if you paint me tired / I'll make time | kindness | Ch 55 epilogue: the portrait | The epilogue portrait's pose |

### What their lines are for

- **Functions:** bond (questions above), callback (warm room, campfire, mural), clue-adjacent (they
  are the one who notices the cord flicker and the warm feeling: the player's mirror for the gift),
  tutorial (genjutsu basics for a Classic Kurama: the Ch 12 clan lesson for a clanless player whose
  closest classmate they are), comfort (they are the gentlest voice after Ch 24 and Ch 51).
- **States:** quarrel (`bond.greet.cold_shoulder.shy`: they avoid eye contact and talk to their
  brush); the cold shoulder after a broken flare secret is the worst one they have; jealousy (if you
  favour b) comes out as a drawing of the squad with themself very small.
- **Phases:** child (shy, apologetic) → teen (dry humour) → adult (calm, direct). After Ch 24 they
  call you by `{given:player}` instead of `{name:player}`.
- **Pools needed:** greetings by level and state; talk topics (above) in their voice; hangout lines
  for painting, library, stargazing, dango; 3 highlights (the overlook, the tea-house painting
  hung, the night they painted you into a genjutsu); life events (a painting sold, a family quarrel,
  injured after Ch 24); the four ask lines (Ch 3, B1, B2, Ch 16).

### Variants

**Archetype skins (Varied).** Role-fixed traits in every save: your Ch 3 partner; the Ch 11
campfire speaker; the sensor-corps offer in Ch 30; the memorial work in Ch 41 (painted, carved,
written or sung by skin). The skin swaps the craft and the quest objects:

| Archetype group | Craft / dream | B1 quest (high place) | B2 quests | Ch 41 memorial work |
|---|---|---|---|---|
| Creative, gentle, shy, imaginative | Painting (Classic) | Paint the village from the overlook | Hang the painting; a painted genjutsu | The mural |
| Bold, fiery, adventurous, playful | A song or a story (the storyteller) | Sing to the village from the Rock top | Perform at the tea house; a story told to the squad at night | A song at the unveiling, written into the stone's plaque |
| Disciplined, stern, meticulous, proud | Calligraphy, records, maps | Map the village from the Rock | A calligraphy scroll mocked, hung anyway; a "perfect form" their family demands | The names, brushed onto the stone before carving |
| Warm, steadfast, protective, thoughtful | Cooking or gardening | A picnic on the overlook for the class | A dish at the festival; the family wants them in the clan trade | A memorial garden of persimmon saplings |

The campfire fear stays "being invisible" in every skin; their questions keep their ids and change
only nouns (painting → song, map, dish).

**Classic vs Varied clan.** A Classic Kurama: genjutsu, the studio, the Kurama clan line overlaps
(their family is a minor voice in `clan.kurama.*`). A Varied teammate_a of another clan or none: the
family pressure is that clan's (a Hyuga main-house duty, an Akimichi kitchen, a civilian shop).

**Romance.** Only from the teen stage. Dating replaces the Ch 41 "hold the other corner" line with
"hold my hand while they look". Never in the child stage (the bond engine refuses romantic acts).

## New flags

- `ans.teammate_a.squad` (together / there / for_me)
- `ans.teammate_a.hurt` (rest / paint_shaking / other_hand)
- `ans.teammate_a.secret_kept` (when_ready / yes / about_me)
- `ans.teammate_a.colour` (red / grey / green / your_choice)
- `ans.teammate_a.seen` (for_self / needs_eyes / i_see)
- `ans.teammate_a.used` (choosing / sometimes / watch_me)
- `ans.teammate_a.after` (always / tired / make_time)
- `ans.teammate_a.family` option ids: `for_them`, `no`, `both`; **unset** (B2 quest skipped): at Ch 30 they ask without a reference to it and lean toward joining
- `hides:warm_room`, `hides:corps`, `hides:portrait` (bond flags on teammate_a)
- `ans.teammate_a.flare` option ids: `yes`, `no`, `dont_tell`
- `ans.teammate_a.paint`: `are`, `should`, `both`; `.show`: `brave`, `foolish`, `both`;
  `.your_fear`: `taken`, `alone`, `nobody`, `fire`; `.freeze`: `always`, `nothing`, `angry_yes`;
  `.corps`: `if_you_want`, `dont_let_them`, `eyes_open`
