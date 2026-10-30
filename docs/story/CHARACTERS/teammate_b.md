# `role:teammate_b`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Arcs:
> [ARCS/](../ARCS/). Rules: [WORLD.md](../WORLD.md).

## At a glance

| | |
|---|---|
| Name | Given Family (`{name:role:teammate_b}`). **No clan.** Family name drawn from the ordinary `family_names` pool (never a clan's name), shared with the grandmother and the absent parent |
| Role | `role:teammate_b`: classmate (Ch 1), squadmate (Ch 8 on); the one Yūgure tries to recruit |
| Look | Classic: curated (clanless, scuffed jacket with a pup in it, a too-big forehead protector that was their parent's). Varied: rolled from the four classmates |
| Pronouns | Rolled: *they*; dialogue uses `{they:role:teammate_b}` and the rest |
| Clan (Classic) | No clan; raised by a grandmother in the shinobi apartment blocks |
| Rank | Academy → Genin → Chunin → Jonin (a frontline captain) |
| Archetype | Classic: **fiery** (warmth .6, boldness .9, pride .4, discipline -.5, openness .8) |
| Values | courage, loyalty |
| Peeves | cowardice, neglect |
| Dream | Classic: "find where they belong" (said aloud as "be the best shinobi in the Leaf", which is not the real one) |
| Pet | A stray pup (Classic: a scruffy brown ninken-mix; it grows up through the story) |
| First / last | Ch 1 (late, with the pup) / Ch 55 (epilogue: with or without their parent) |

**Role-fixed in every save:** a parent who walked out of the village when b was small and joined
Yūgure (`role:yugure_b_parent`); the stranger on the bridge (Ch 13); the Ch 26 branch; meeting the
parent in Ch 51; a pet.

## Arc

**Wants.** To matter to someone enough that they would never leave. To be loud enough to fill the
space a parent left.

**Fears.** That they *are* their parent: someone who walks away (Ch 16: "If I ever start walking
away, drag me back"). Being left behind by the squad.

**Why Yūgure wanted b.** Not for b's chakra: b has no Kagari blood. The leader wanted a way into
Nine's squad: eyes on the wick as it grows, and a door for later. b's parent, a hearth member for
years, was the bait; the second was given the job (Ch 13) and hated it. She says so in Ch 49 if b
asks her (`ans.teammate_b.stranger_face` = ask or come_with): "He didn't want you. He wanted to stand
next to your friend. I used your parent's name to do it." (Her one apology to b is a separate beat,
`ans.yugure_second.b_sorry` in her file.) b's anger at being *used for someone
else* is the last push of their arc: they were never the point, and they choose to be anyway.

**Secrets.**
- Their parent left; the village says "missing-nin" (told to you in Ch 6; `ans.teammate_b.parent_first`).
- They keep the parent's old forehead protector (shown in B2 bond quest 2).
- From Ch 13: the stranger said the parent is alive (secret or not by the Ch 13 choice).
- From Ch 26: the parent is with Yūgure (`story.teammate_b.parent_alive`). b is ashamed of it
  and tells no one but you (and the sensei, on the *stayed* path).

**What they know and when.**

| Knowledge | When |
|---|---|
| Their parent "is alive" | Ch 13 (`story.seed.teammate_approached`) |
| The stranger's voice is the woman in the forest | Ch 16.8 (if kept or followed) |
| Your gift | Ch 23 (if you let the squad hear) or Ch 25 |
| Their parent is in Yūgure | Ch 26 (every branch) |
| The stranger is Yūgure's second | Ch 26 (stayed: they see her face) or Ch 49 |
| Kagari, the purge | Ch 40 |
| The second knew their parent | Ch 49 (the second tells them, if asked) |

**How they change.**

| Arc | Change |
|---|---|
| Cinders | All noise; trusts you with the one quiet thing they have (Ch 6) |
| Paper Trail | Learns to listen in a squad; the stranger finds their crack (Ch 13) |
| Dusk | Says the fear aloud (Ch 16); covers you at the stadium if their bond is the higher |
| Embers | Walks to the edge (Ch 26) and stays, nearly goes, or goes; learns the truth about the parent |
| Ashes | A captain who never leaves a teammate; quieter; good with the Valley children |
| Last Bonfire | Faces the parent (Ch 51) with your question and decides what they owe them |

**Endings and variants.**
- **Any departure from Ch 8 on** (a falling-out or a low bond): b is replaced by a stand-in lent by
  `sensei_2` (classmate_c, else classmate_d). If b has already left by Ch 13, the stranger approaches
  them anyway (outside the squad, b is easier to reach), and Ch 26 plays as *left*.
- **The well rule (Ch 26 *nearly*):** b turns back on the spot only if you made the `drag_back`
  promise and their trust is 45 or more; `ans.teammate_b.grandma` (any answer; **unset** adds
  nothing) adds 10 trust before the bridge. Otherwise the chase, the fight and the talk-down.
- **Ch 51a:** b holds the market street with `squad4_b` and the dogs; the parent comes there.
- **A falling-out with b** is mended by the story at the Ch 49.5 return, or at 51a.4 if the player
  chose "at the war" there, whatever their stance before the parent (`mend`).
- **If teammate_b is out of the squad** (a falling-out, the *left* path, or a low bond): a stand-in from
  Squad 2 (classmate_c, else classmate_d) takes their squad lines in Ch 31 (the drain's story floor
  links everyone present, ARCS/4 31.1), Ch 35, Ch 45 and Ch 50. Whether they speak in Ch 53.2 follows
  slot 5 of the speaking rule in DIALOGUE_BRIEFS (with the squad hold, SYSTEMS.md §3).
- **Ch 53 line table** (b speaks in slot 4 if they fell in Ch 24, or if the sensei fell and b is the higher
  teammate; else slot 5; once only, per the speaking rule in DIALOGUE_BRIEFS; one line; the arc
  cites this table):

  | Reads `ans.teammate_b.drag_back` | Line |
  |---|---|
  | promise | "You promised to drag me back. Now I'm dragging you. Take it!" |
  | wont_leave | "Told you I wouldn't leave. Take it!" |
  | walk_with | "We're walking together. That's the deal. Take it!" |
  | unset | "Later's not goodbye. Take it!" |

- **Ch 13 → Ch 26 path** (`story.teammate_b.path`):
  - *stayed* (trust 60+): b brings you the second note; together you trap the bridge. Ever after b
    says "we" about every danger. Ch 51: steady, asks the question calmly.
  - *nearly* (30 to 59): the walk to the well, the ash-violet scarf in their hands, your drag-back line. A
    `reconciled`-weight moment when they come back. Ch 51: shaky; they look at you before they speak.
  - *left* (under 30): b quits the squad (`remove_from_squad story`), trains alone, sleeps badly.
    Their return quest (Ch 32) needs `friendship 4`; if never done, b comes back at Ch 49.5 when the
    second's truth makes Yūgure impossible, and the player takes b back then or at the war (51a.4), as
    for any falling-out. This path only shades b's manner there. Ch 51: guarded, slow to meet your eyes.
- **Ch 51a parent scene** (the parent in road clothes, a sinking sun in soot on the inside of the
  wrist, an ash-violet scarf pulled down) reads `ans.teammate_b.ask` (the question b asks; **unset**:
  b asks "why") and
  `ans.teammate_b.come_back` (**unset**: "only if sorry"): *yes* → b brings the parent in (epilogue: an awkward dinner at the
  grandmother's); *only if sorry* → the parent must say it; the parent says it only if b's ask was
  "are you sorry" (which sets `bond_flag parent_sorry`), else they walk away; *no* → b lets them go and does not
  look back (epilogue: b at the bridge, alone, at peace). The parent lives in all three.
  `ans.teammate_b.parent_good` colours b's last line ("I'm going to be better than you" / "I'm
  already better than you" / "I don't need to be anything to you").
- **Ch 24** if b fell: "Told you. Drag me back—" (reads `ans.teammate_b.drag_back`). Thread Sight
  opens on them; you push your chakra into them; they rise for one moment with the pup, and their
  own fang technique (Classic: a spinning pup-and-partner rush) goes past its limits into a storm
  that tears the post's smoke away and drives the hollow girl back. Ch 25: "Did you SEE that? That
  was me! ...It was me, right? You just made it bigger." If b already knew (`bond_flag knows_flame`,
  Ch 23): at 24.4 "Do the thing! The fire thing!", and at 25.2 "Knew it. Knew it since the school."
  The fall line itself reads `ans.teammate_b.drag_back` (**unset**: "Don't you dare walk off—").
- **Thread Sight on them** (from Ch 24, level 6+): the thread frays toward the bridge on the nights
  they go there: a scripted `thread_floor` before the bridge in Ch 26, in every branch (squad4_b also
  tells you b has been at the bridge). A steady flicker while they carry `hides:notes` (the
  stranger's notes, Ch 26 *nearly*, until the well).
  On the *left* path it thins to one strand that never quite breaks.
- **Unison technique (Blaze tier, Ember Link): "Pack Fire".** You, b and the pup move as one flame:
  three ember-gold rushes from three sides, the pup leading, landing at once; the pup's bark sets
  the timing. Unique because it needs the pup: if the pup is home, it doesn't exist.
- **Their rival-friend:** `squad4_b`, the loud Inuzuka with the big ninken, from Squad 4. The two
  compete over everything (whose dog is braver, who eats more at the barbecue house), and squad4_b
  is the one person b admits to missing on the *left* path.
- **Romance** (teen and up): b confesses loudly, in public, at a festival (a deed the village hears).
  Dating a teammate triggers the other's squad-dinner scene.

## Dialogue brief

### Voice

- **Child:** loud, fast, exclamation marks, invents nicknames for everyone (for you: from your
  ramen order in Ch 1, e.g. "Miso"), talks to the pup as if it votes. Turns everything into a
  challenge. Goes very quiet when the parent comes up.
- **Teen:** still loud with others; with you, sudden honest silences. Swears by the pup.
- **Adult:** a captain's voice: short orders, a grin after. Uses "we" for everything.
- **Never:** says "goodbye" (they say "later"); admits being scared before Ch 16; speaks ill of the
  grandmother; calls the parent "mother", "father" or any such word before Ch 51 (they say "them" or "my parent").
- **Tics:** taps the forehead protector; feeds the pup off their own plate; counts to three before
  doing something stupid ("One—" and goes on one).

Voice samples, not shipped lines:
- (child, Ch 6) "Everyone says missing-nin. Whatever. Don't tell anyone, okay? Okay. Good."
- (child, Ch 16) "Promise me something. If I ever start walking away, drag me back. Even if I bite."
- (teen, Ch 26, nearly) "They said my parent asked for me. Nobody's ever asked for me."
- (teen, after) "We. It's *we* now. You're stuck with it."
- (adult, Ch 51) "I've got one question for you. {given:player} gave it to me years ago."
- (adult, epilogue) "Later. Not goodbye. I never say goodbye, you know that."

### Topics they care about

| Depth | Topics |
|---|---|
| 0 to 2 | The pup, food, beating the rival, rooftop races, who's strongest |
| 3 to 4 | The grandmother; the bridge; the parent as "them" |
| 5 | Values: you don't leave people; cowards; loyalty as a promise you keep with your feet |
| 6 | The real dream: belonging somewhere nobody can walk out of |
| 7 | Worries: that they are their parent; that the squad would be better without them |
| Shared memory | The runaway pup at the well (B1), the clinic night (B2.1), the Rock race (B2.2), the bridge |

### Never reveal before

| Secret / fact | Gate |
|---|---|
| The parent left the village | Ch 6 (to you only) |
| The stranger's offer | Ch 13 (to you if `friendship 4`, else you witness it) |
| The parent's forehead protector | B2 bond 2 (`friendship 5`) |
| The fear of being a leaver | Ch 16 night watch, or level 7 |
| Parent in Yūgure | Ch 26 |
| Anything the second told them | After Ch 49 |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes them |
|---|---|---|---|---|---|---|
| `ans.teammate_b.parent_first` | Ch 6.2 | (after the confidence) — the player's reply | promise / it isn't your fault / what were they like? | loyalty (promise), kindness (not your fault), *what were they like* tests (pried-adjacent, but they answer: "They laughed loud. Like me.") | Ch 26 (they repeat your words to the stranger); Ch 51 | Sets what they cling to: your promise, their innocence, or a memory of laughter |
| `ans.teammate_b.come_back` | B1 bond (L2) | "Do you think people who leave can ever come back?" | yes / only if they're sorry / no | courage, loyalty | Ch 51a.4; endings | Their verdict on the parent |
| `ans.teammate_b.parent_good` | B2 bond 1 (L4) | "Do you think I'd be a good parent? Someday. Better than mine?" | yes / you already care like one (the pup) / you don't have to be anything like them | family | Ch 51 last line to the parent; epilogue (b with a child, post-game) | Their sense of what they're not |
| `ans.teammate_b.ask` | B2 bond 2 (L5) | "If you could ask them one thing, what would it be?" | why / are you sorry / do you remember me | courage | Ch 51a: b asks it (**unset**: why) | The parent's answer (why: Yūgure's creed, the village failed them; sorry: yes, and `parent_sorry` is set; remember: they name the pup's predecessor, a dog b had at three) |
| `ans.teammate_b.drag_back` | Ch 16 night watch (L5) | "If I ever start walking away, drag me back." | I promise / no — you won't leave / I'll walk with you instead | loyalty (promise and walk-with both honour it) | Ch 24 fall line; Ch 26 *nearly* line ("You promised"); Ch 32 return (set: "You were supposed to drag me back. You took your time."; unset: only "You took your time.") | *promise*: they test it; *you won't leave*: they believe it, and it holds them on the *nearly* path; *walk with you*: they laugh and never forget it |
| `ans.teammate_b.forest_voice` | Ch 16.8 | "That's the voice from the bridge. Do we tell sensei?" | tell sensei / keep it between us | duty vs loyalty | Ch 26 (the sensei is ready, if told: `stayed` gets a sensei ambush) | Whether they trust adults with it |
| `ans.teammate_b.pup_name` (new) | Ch 2 or first talk (L1) | "The pup needs a real name. You pick." | a food / a jutsu sound / your name for them / "Pup" | playful | Every scene the pup is in; Ch 51 (the parent asks its name) | Filler with payoff: the pup's name token `{pet:role:teammate_b}` |
| `ans.teammate_b.loud` (new) | Genin hangout, rooftop race (L3) | "Am I too loud? Grandma says I'm too loud." | yes, and don't stop / sometimes / you're as loud as you need | freedom, kindness | Ch 33 (captain's voice) | Whether they learn quiet or keep the noise as theirs |
| `ans.teammate_b.cloak` (new) | Ch 26 *nearly* or *left* return | "What would you have done if I'd tied it on?" (the scarf) | come after you / let you go / tie one on too, to drag you out | loyalty | Ch 51 (if the parent offers b a scarf again, b answers with yours) | |
| `ans.teammate_b.parent_hate` (new) | Jonin, level 7 talk (worries), after Ch 40 | "The village erased a whole clan and called it peace. Maybe my parent wasn't wrong to leave." | they weren't wrong to be angry / they were wrong to leave you / both | honesty | Ch 51 parent scene (b quotes you) | Lets b grant the parent's grievance without excusing them |
| `ans.teammate_b.squad4` (new) | Genin, after a squad4_b brawl (L3) | "squad4_b says their dog's braver than mine. Settle it." | yours / theirs / have a race and find out | playful, filler with payoff | Ch 33 (a race at the Jonin promotion), Ch 51 (the two dogs side by side) | A rivalry that keeps b anchored to the village |
| `ans.teammate_b.grandma` (new) | Life event: the grandmother sick (L4, before Ch 26) | "If she goes, I've got nobody. Don't say I've got you, that's cheesy." | you've got me anyway / you've got the squad / you've got the pup, at least | family | Ch 26: any answer adds 10 trust before the bridge (the well rule); **unset**: nothing | Who b counts as family |
| `ans.teammate_b.stranger_face` (new) | Ch 49, after the second's truth (L6); not asked if b's return waits for the war (49.5), since she never sees b before Dusk (`ans.yugure_second.b_sorry`) | "She knew my parent. Should I ask her about them, or is that like forgiving her?" | ask her, knowing isn't forgiving / don't, it's hers to offer / I'll come with you | honesty | Ch 51 (b knows the parent's side, or not, before the meeting; unasked or unset: not) | Prepares b for Ch 51 |
| `ans.teammate_b.after` (new) | Ch 54 Morning | "So. Now what?" | ramen / sleep for a week / go see your grandmother | warm, filler | Epilogue | Last shared ritual |

### What their lines are for

- **Functions:** bond (the questions), plot (the Yūgure recruitment line: the story's most personal
  view of what Yūgure offers and why it works), comic relief (the pup, the noise), courage beats
  (Ch 19, 24, 51).
- **States:** quarrel (fiery: loud then sulky; cold shoulder means they train alone at the bridge);
  jealousy (they say it outright: "You like a better than me"); the *left* path greeting pool is
  its own (`bond.greet.departed.teammate_b`: curt, sad, never cruel).
- **Phases:** child (loud) → teen (loud with honest silences) → adult (captain's we).
- **Pools needed:** greetings by level, state and path; topics in their voice; hangouts: ramen,
  rooftop race, sparring, walking a pet, snowball fight; highlights (the goat chase, the pup at the
  clinic, the Rock race win/loss); life events (the pup's growth, the grandmother sick, injured
  after Ch 24, the parent news).

### Variants

**Archetype skins (Varied).** Role-fixed: the absent parent in Yūgure, the stranger, the pup (or
another pet), the leaver fear. The skin changes how b *covers* the wound:

| Archetype group | Cover | B1 quest | B2 quests | Ch 26 *nearly* tell |
|---|---|---|---|---|
| Bold, fiery, adventurous, playful (Classic) | Noise and dares | The pup runs off to the old well | Clinic night; Rock race | They run to the bridge |
| Disciplined, stern, meticulous, proud | Rules and perfection ("I'll never break one") | The pet escapes during a drill they were "in charge of" | A rule they break for the pet; the protector polished every night | They walk, at an exact time, as if obeying an order |
| Warm, gentle, steadfast, protective | Taking care of everyone else | The pet is lost while they helped a neighbour | A night carrying a sick stray; cooking the parent's dish | They leave a note for the grandmother first |
| Reserved, shy, thoughtful, curious | Silence and questions | The pet follows a scent to the well; they won't say why they know the well | A library search for the parent's mission records; the protector | They go without a word; you notice the empty seat |

**Romance.** Teen and up. On the *nearly* path, a romance confession cannot happen until Ch 32's
reconciliation; on *left*, until the return quest.

## New flags

- `ans.teammate_b.pup_name` (food / jutsu / player_choice / pup) and the token `{pet:role:teammate_b}` (request to dialogue session)
- `ans.teammate_b.squad4` (yours / theirs / race)
- `ans.teammate_b.grandma` (me / squad / pup; unset: no trust bonus)
- `hides:notes` (bond flag on teammate_b, Ch 26 *nearly* until the well)
- `ans.teammate_b.stranger_face` (ask / wait / come_with)
- `ans.teammate_b.loud` (dont_stop / sometimes / as_needed)
- `ans.teammate_b.cloak` (come_after / let_go / drag_out)
- `ans.teammate_b.parent_hate` (angry_ok / wrong_to_leave / both)
- `ans.teammate_b.after` (ramen / sleep / grandmother)
- `bond_flag parent_sorry` on `yugure_b_parent` (set in Ch 51a.4: the parent apologises only if b's ask was "are you sorry")
- Option ids for existing flags: `.parent_first`: `promise`, `not_fault`, `what_like`;
  `.come_back`: `yes`, `if_sorry`, `no`; `.parent_good`: `yes`, `already`, `not_them`;
  `.ask`: `why`, `sorry`, `remember`; `.drag_back`: `promise`, `wont_leave`, `walk_with`;
  `.forest_voice`: `tell`, `keep`
