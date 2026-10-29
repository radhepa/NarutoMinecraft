# `role:teammate_a`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Arcs:
> [ARCS/](../ARCS/). Rules: [WORLD.md](../WORLD.md).

## At a glance

| | |
|---|---|
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
| The bell flicker was the same thing | Ch 8 (they saw it; they say so only if the flare is shared) |
| The paper chars around you | Ch 11 if you showed a teammate; Ch 23 if you let the squad hear the tester (`bond_flag knows_flame`) |
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
| Last Bonfire | Kindles toward you without being asked (Ch 53); their line answers the fear you told them in Ch 11 |

**Endings and variants.**
- **Who fell in Ch 24.** If teammate_a fell: their Ch 25 line is "That was the warm room again" (if
  the flare was shared) or "So that's what it was" (if not); they gain a permanent `saved_by_them`
  memory toward you and a `trained_together` streak in the secret training. If someone else fell:
  they arrive at the hospital last and say they should have been faster.
- **Ch 30 corps choice** (`ans.teammate_a.corps`): *join if you want* → they ask for time and choose
  painting first, corps second (a part-time sensor; Ch 50 they find anchors by feel). *Don't let them
  choose for you* → they refuse the corps; a quarrel with their family (a life event: "a quarrel
  with family", comfortable to comfort) and a painter-shinobi path. *Join and keep your eyes open for
  us* → a sensor captain by Ch 33; in Ch 38 they bring you the sensor logs that fix one alibi's time.
- **The mural (Ch 41)** reads `ans.teammate_a.paint`: *are* → the Kagari faces as the archive
  describes them, burned shrine and all; *should* → the same faces at the Leaf's festivals, as if
  they had never left; *both* → two panels, and they ask you which goes on the left. It reads
  `ans.teammate_a.show`: *brave* → they unveil it; *foolish* → they ask you to; *both* → they hold the
  cloth with you.
- **Romance** (teen and up, if chemistry allows): dating moves the painting hangout to *their*
  studio; the confession (level 8) is a painting of you they never finished in public (the Kurama
  custom: "a painted eye is never finished in public"). If you date them, `teammate_b` gets the
  squad-dinner scene (ARCS/5_ashes.md).
- **A falling-out** (only if the player broke the flare secret and more): they leave the squad
  (BONDS §7); they still paint the memorial, and do not invite you to the unveiling.

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
- (adult, Ch 53) "You told me once you were afraid of being alone. Look how many of us there are."

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

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes them |
|---|---|---|---|---|---|---|
| `ans.teammate_a.flare` | Ch 3.4 | "Did you feel that too?" | yes / no (you imagined it) / don't tell anyone | yes, dont_tell honour honesty and trust; *no* tests it (a small `rude`-sized sting for the shy) | Ch 8 bell flicker line; Ch 24 "warm room"; Ch 25.2 | Sharing makes them your keeper of secrets; denial makes them doubt their own senses until Ch 24 |
| `ans.teammate_a.paint` | B1 bond quest (L3) | "Should a painting show things as they are, or as they should be?" | are / should / both | creativity either way | Ch 41 mural | Their style for life: realist, hopeful, or both |
| `ans.teammate_a.your_fear` | Ch 11 campfire (L5) | "What are *you* afraid of?" | being taken again / being alone / being nobody / fire | Your honesty (any answer is a `heart_to_heart`) | Ch 24 fall line; Ch 53 flame line | They become the friend who guards against *your* fear: watches doors (taken), always comes (alone), names you to others (nobody), learns water/earth safety (fire) |
| `ans.teammate_a.show` | B2 bond 1 (L4) | "Is it brave to let people see what you made, or just foolish?" | brave / foolish / both | creativity, kindness | Ch 41 unveiling | Whether they stand in front of their own work |
| `ans.teammate_a.family` | B2 bond 2 (L5) | "If your family wanted you to be someone else, would you?" | yes, for them / no / I'd try to be both | family vs freedom (the shy value kindness: no answer offends) | Ch 30 corps choice | Frames how they hear the corps offer |
| `ans.teammate_a.freeze` | Ch 16 night watch (L5) | "If I froze, and you got hurt, would you forgive me?" | always / there's nothing to forgive / I'd be angry, but yes | honesty valued; *angry but yes* earns respect (+) | Ch 24 if they fall: "I didn't freeze"; Ch 25 | *always*: they relax; *nothing to forgive*: they cry a little; *angry but yes*: they train harder, and say so |
| `ans.teammate_a.corps` | Ch 30.3 | "The corps wants me. What should I do?" | join if you want / don't let them choose for you / join, and keep your eyes open for us | freedom or loyalty | Ch 33 rank, Ch 38 sensor logs, Ch 50 anchors | Their career (see Variants) |
| `ans.teammate_a.colour` (new) | Hangout: painting at the overlook (L3, any arc) | "If you were a colour, which one?" | the red of the cord / ash-grey / the green of the Leaf / whatever you'd paint me | creativity (filler with a payoff) | Their portrait of you (Ch 55 epilogue, or the confession painting) uses it | Small: sets your colour in their art |
| `ans.teammate_a.seen` (new) | Chunin, level 6 talk (dream) | "Do you think I'd still be me if nobody ever saw my paintings?" | yes, you paint for you / no, art needs eyes / I'd see them | creativity / kindness | Ch 41: whether they sign the mural | *yes*: unsigned mural; *no*: signed large; *I'd see them*: signed small, with a mark only you know |
| `ans.teammate_a.used` (new) | Jonin, level 7 (worries), after Ch 36 | "The founders used a whole clan's gift and then erased it. Are we using you, when we fight beside you?" | no, I'm choosing / sometimes, and that's all right / yes, so watch me | honesty, kindness | Ch 53 (their flame line: "You said you were choosing. So am I.") / an epilogue line | Settles their fear of being a tool by seeing you choose |
| `ans.teammate_a.after` (new) | Road to Hokage, Ch 46 hangout at the shrine | "When this is over, will you still have time to sit for a portrait?" | always / only if you paint me tired / I'll make time | kindness | Ch 55 epilogue: the portrait | The epilogue portrait's pose |

### What their lines are for

- **Functions:** bond (questions above), callback (warm room, campfire, mural), clue-adjacent (they
  are the one who notices the bell flicker and the warm feeling: the player's mirror for the gift),
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

- `ans.teammate_a.colour` (red / grey / green / your_choice)
- `ans.teammate_a.seen` (for_self / needs_eyes / i_see)
- `ans.teammate_a.used` (choosing / sometimes / watch_me)
- `ans.teammate_a.after` (always / tired / make_time)
- `ans.teammate_a.family` option ids: `for_them`, `no`, `both`
- `ans.teammate_a.flare` option ids: `yes`, `no`, `dont_tell`
- `ans.teammate_a.paint`: `are`, `should`, `both`; `.show`: `brave`, `foolish`, `both`;
  `.your_fear`: `taken`, `alone`, `nobody`, `fire`; `.freeze`: `always`, `nothing`, `angry_yes`;
  `.corps`: `if_you_want`, `dont_let_them`, `eyes_open`
