# `role:rival`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Arcs:
> [ARCS/](../ARCS/). Rules: [WORLD.md](../WORLD.md).

## At a glance

| | |
|---|---|
| Name | Given Family (`{name:role:rival}`); Classic family name Uchiha, given name rolled |
| Role | `role:rival`: classmate on Squad 2 (with `classmate_c`, `classmate_d`, under `sensei_2`), rival to ally |
| Look | Classic: curated (an Uchiha: dark hair, high collar, the fan crest; arms always crossed). Varied: rolled |
| Pronouns | Rolled: *they*; tokens in dialogue |
| Clan (Classic) | Uchiha (a minor household of the police quarter) |
| Rank | Academy → Genin → Chunin (Ch 20, alongside you) → Jonin (Ch 33, the paired trial) → the Seventh's captain |
| Archetype | Classic: **proud** (warmth -.4, boldness .5, pride .9, discipline .6, openness -.6) |
| Values | strength, family |
| Peeves | bragging, nosiness |
| Dream | "Surpass a rival" (you), which becomes "be someone their family can't look past" and ends as "protect the village" |
| First / last | Ch 1 ("Another one from nowhere") / Ch 55 (epilogue) |

**Role-fixed in every save:** proud; wants to surpass you; on another squad; the Ch 2 spar, the
Ch 19 finals bout, scheduled last and never fought (the attack starts at the opening lantern-lighting;
"You owe me a match" pays it in the epilogue); they drag you clear in Ch 19 if both teammates are
under 4; their awakening in the Ch 29 spar with you;
the Ch 29 spar; the Jonin trial pair (Ch 33); the family ceremony (Ch 43); the flame in Ch 53.

## Arc

**Wants.** To be strongest; underneath, to be *seen* by a family that looked past them. Nobody from
their family came to their Academy graduation (Ch 7.3b: they leave before the speech ends — the rival
stands alone after the speech).

**Fears.** Being ordinary. Needing anyone. That strength given (by blood, by a gift, by friends) is
worth more than strength earned, which would make their whole life a mistake.

**Secrets.**
- Their household is cold and exacting; a sibling is the favourite (`side.b3.rivals_sibling` is the
  younger sibling who wants secret training: a crack in the family that the player can widen kindly).
- They watch your bouts more than their own.
- From Ch 29: they are afraid your gift makes their effort meaningless.

**What they know and when.**

| Knowledge | When |
|---|---|
| You came from "the camps" | Ch 2, if `ans.rival.fall` = truth |
| Your finals bout was never fought | Ch 19 (they never let it go: "You owe me a match.") |
| The rumour of your fire | Ch 29 |
| What the gift is (that it needs consent) | Ch 29 (if you tell them) or Ch 40 |
| Kagari | Ch 40 |
| The Hollow Crown | Ch 49 (as the Seventh's captain) |

**How they change.**

| Arc | Change |
|---|---|
| Cinders | Contempt for "nobodies", then a crack: you fell like someone who'd been fighting longer |
| Paper Trail | Rivalry as their only way to talk to you |
| Dusk | The finals bout they trained for, never fought; they may drag you clear |
| Embers | Hurt pride at the gift; asks what's left when the people are gone (Ch 29) |
| Ashes | Fights better beside you (Ch 33); lets you see their family (Ch 43) |
| Last Bonfire | Offers their flame (Ch 53): the proudest person in the village choosing to give |

**Endings and variants.**
- **Ch 19 cover:** with both teammates under level 4, the rival drags you out of a collapsing tier
  of the stands (`saved_by_them`; no wound). Their Ch 20 line: "Don't thank me. You owe me a match."
- **Ch 51b, fixed in every save:** the rival fights up the Rock's stair beside you; near the top
  they see the trio pinned on the steps below (a hearth's strongest has them cornered), and turn
  back: "Go. You owe me a match." They are badly hurt and live; the match is paid in the epilogue
  (`ans.rival.spar_last`). The `ans.rival.ordinary` answer is read here, as they turn (see the
  question row).
- **Ch 53 line table** (the rival speaks in slot 6; one line built from two reads; the arc cites
  this table). First half by `ans.rival.theirs` (Ch 29):

  | `ans.rival.theirs` | First half |
  |---|---|
  | memory | "Then remember me." |
  | hold_on | "Then don't let go." |
  | chosen | "You said I'd be what's left." |
  | unset | "Take it. Don't say anything." (the whole line; no second half) |

  Second half by `ans.rival.why_came` (Ch 43), only if the first half is set: *youd_come* "You were
  right. I came. Take it."; *wanted* "I wanted to. Take it."; *asked* "You didn't even ask. Take
  it."; unset: "Take it."
- If you **never go** to the ceremony (Ch 43), they still kindle at 6+, with the unset second half.
- **Romance** (teen and up): a rival romance is slow (pride); the confession is a challenge ("Spar
  me. If I win, you hear something."). Never in the child stage.
- **Thread Sight on them** (from Ch 24, level 6+): their thread is thin, taut and bright, like
  wire; it holds a steady flicker while they carry `hides:family` (the empty seats at graduation,
  until Ch 43). Ch 29's spar is their awakening and their first look at the gift: they ask if you
  can see what they think; you can't, and say so.
- **Unison technique (Blaze tier, Ember Link): "Twin Strike".** The only unison built from two
  people refusing to be outdone: each of you attacks a beat after the other, and each blow is
  Kindled by the other's flame, so the chain only ends when one of you yields (neither does).
  Classic: the Sharingan reads the enemy's guard and your thread marks the gap. It works only at
  rivalry 30 or more: it needs the rivalry, not just the friendship.
- **Their sensei and squad:** Squad 2 under `sensei_2`, who teases your sensei as a self-declared
  rival; the rival is embarrassed by their sensei and quietly copies them.
- **Clan.** A Classic Uchiha rival's clan reacts to Ch 40 (their head protests the forgery); the
  rival breaks with their clan's line publicly at the council if `friendship 7` ("A dead elder lied.
  We'll carry it anyway").

## Dialogue brief

### Voice

- **Child:** clipped, cutting, few words; questions disguised as insults.
- **Teen:** the same clipped voice with more vocabulary; compliments that sound like complaints
  ("That was barely adequate. Is that all?").
- **Adult:** dry, loyal, still competitive about trivial things (who orders faster at Ichiraku);
  rarely says "we".
- **Never:** says thank you plainly before Ch 43; cries in front of you; brags about their clan
  (peeve); asks personal questions directly (peeve: nosiness) — they ask sideways.
- **Tics:** taps two fingers on their clan crest (Classic; a Varied rival taps their family mark)
  when thinking; crossed arms; challenges and questions dressed as insults ("Is that all?", "You call
  that a fall?"); never keeps score (that is `sensei_2`'s habit, and the rival hates it).

Voice samples, not shipped lines:
- (child, Ch 1) "Another one from nowhere."
- (child, Ch 2) "Who taught you to fall like that? Nobody falls like that here."
- (teen, Ch 29) "Is it yours, or theirs?"
- (teen, Ch 20) "Don't thank me. You owe me a match."
- (adult, Ch 43) "Why did you come?"
- (adult, Ch 51b, turning back on the stair) "Go. You owe me a match."

### Topics they care about

| Depth | Topics |
|---|---|
| 0 to 2 | Training, technique, who's strongest in the year, challenges |
| 3 to 4 | Their clan's expectations; the sibling; the police quarter |
| 5 | Values: strength earned; family as duty |
| 6 | The dream as it changes |
| 7 | Worries: being ordinary; that giving makes you weak |
| Shared memory | The Ch 2 spar, the finals that never happened, the Rock spar (Ch 29), the trial (Ch 33) |

### Never reveal before

| Secret / fact | Gate |
|---|---|
| Nobody came to their graduation | Ch 43 (said); seen in Ch 7.3b (they leave before the speech ends; the player can follow or let them be) |
| The sibling's secret training | `side.b3.rivals_sibling` (the sibling tells you, not the rival) |
| The fear about gifts | Ch 29 |
| Any warmth toward you in words | Ch 43 |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes them |
|---|---|---|---|---|---|---|
| `ans.rival.fall` | Ch 2.3 | "Who taught you to fall like that?" | the truth, the camps / nobody / you'll have to beat it out of me | truth earns respect; *nobody* reads as bragging-adjacent (they don't believe you); the dare raises rivalry | Ch 20, Ch 43 ("You told me about the camps when we were eleven. I never told anyone.") | Truth: the first crack; dare: a pure rivalry track |
| `ans.rival.theirs` | Ch 29.3 | "If your strength comes from other people, what's left when they're gone?" | my memory of them / nothing, so I won't let them go / me, the person they chose to trust | strength (all three answer it); *the person they chose* honours it most for the proud | Ch 53 flame line | How they come to see strength |
| `ans.rival.why_came` | Ch 43.2 | "Why did you come?" | because you'd have come for me / because I wanted to / because you asked | family | Ch 53 second half | They admit the bond (or not) |
| `ans.rival.score` (new) | Genin, after a spar (L2) | "My sensei keeps a tally against yours. Pathetic. Do you think counting makes anyone better?" | no, only trying does / it helps some people / your sensei's just lonely | rivalry vs warmth | Ch 33 (their trial line: "I didn't count. I just didn't lose."); Ch 54 (sensei_2's notebook: the rival keeps it) | *lonely*: they soften toward sensei_2 and keep the notebook after Ch 54 |
| `ans.rival.sibling` (new) | Ch 18, after `side.b3.rivals_sibling` | "You trained my sibling. Behind my back." | they asked me / they'll be better than both of us / you should've trained them | family | Ch 43 (the sibling attends the ceremony, or not) | *you should've*: the rival trains the sibling; the sibling comes to Ch 43 |
| `ans.rival.finals` (new) | Ch 20.4 or Chunin talk (L3) | "We never fought. Who would have won?" | you / me / we'll never know, so let's find out | pride | Ch 33 trial line; epilogue spar | *let's find out*: a ritual spar on the Rock each year |
| `ans.rival.clan` (new) | Ch 40 aftermath (L6) | "My clan's elder forged it. Do I carry that?" | no, you weren't born / yes, we all carry the village's / carry it by making it right | family, honesty | Ch 40 council break; Ch 51b (on the stair they fight beside the Kagari house's members) | Whether they stand up in the council |
| `ans.rival.ordinary` (new) | Jonin, level 7 (worries) | "What if I'm just... ordinary? Good, but ordinary." | then be the best ordinary there is / you're not / ordinary people held the wall in the war | honesty | Ch 51b stair, as they turn back: *best ordinary* "Best ordinary there is. Watch."; *not* "You said I'm not. Prove it by going."; *held_wall* "Ordinary people hold stairs too."; unset: no extra line | Settles their fear |
| `ans.rival.graduation` | Ch 7.3b | (nobody came for the rival; they slip away before the Fourth's speech ends; you can follow to the water pump) | go to them / let them be | *go*: they snap "What?", then don't leave; respect for leaving them their pride if *let go* | Ch 43.1 ("You came over at graduation. I hated it. I've thought about it every year." / "You left me alone at graduation. That was the kindest thing anyone did that day.") | Whether the Ch 43 invitation is a return of a favour or a first reach |
| `ans.rival.forest` (new) | Ch 29, after their awakening in the spar (L4) | "You saw it. Don't tell anyone until I show them." | I won't / you should be proud of it / it suits you | honesty, pride | Ch 33 trial (they show it to the examiners with a glance at you) | *won't*: trust +; *proud*: they're annoyed and pleased |
| `ans.rival.team` (new) | Genin, after `sensei_2`'s teasing (L3) | "Is your sensei as embarrassing as mine?" | worse / mine eats apples to look mysterious / yours is great, actually | playful (filler) | A running joke; Ch 42 (sensei_2 at the Seventh's naming, and the rival's line) | Small: their softening toward their own sensei |
| `ans.rival.give_up` (new) | Ch 31 aftermath (L5) | "You stood up in front of the whole council for a clan that isn't yours. Why?" | because they were right / because no one stood up for mine / because I could | loyalty, family | Ch 40 (the rival stands in the council for the truth) | Teaches them public courage |
| `ans.rival.spar_last` (new) | Ch 50, before Dusk (L6) | "If we live through tomorrow, you owe me a real finals." | deal / we'll call it a draw forever / you'll win | rivalry | Ch 55 epilogue: the finals rematch on the Rock, and its result (or none) | The last image of the rivalry |
| `ans.rival.hokage` (new) | Ch 54 | "You'll be Hokage. I'd have liked it to be me." | it should have been both of us / you'll be my right hand / you'll surpass me yet | pride | Ch 55 epilogue (their post: captain of the guard's training, or the Academy's hardest teacher) | Their post-game role |

### What their lines are for

- **Functions:** bond, rivalry (the spar pools and the challenges), mirror (strength earned vs given:
  the thematic opponent of the gift who becomes its proudest giver), comedy (pettiness at
  Ichiraku), a plot body in battles (Ch 19, 33, 51).
- **States:** rivalry is not dislike (BONDS §2): greeting pools by *rivalry* height as well as level.
  Quarrel: proud and slow to heal; they never apologise first (a `making_up` pool where they
  "happen" to train at your ground).
- **Pools:** greetings by level, rivalry and state; spar banter (before/after, win/lose); topics;
  hangouts: sparring, training, rooftop race, shogi; highlights (the first win, the trial).

### Variants

**Archetype skins (Varied).** Role-fixed: pride, the challenges, another squad, the family that looked
past them, the Ch 53 flame. A Varied rival rolled as gentle or warm keeps a proud *stance* in the
rival role (pride is lifted to at least .5 for the role) but the cover changes:

| Archetype group | Their pride shows as | Ch 43 family beat |
|---|---|---|
| Proud, stern, meticulous (Classic) | Contempt, cutting challenges | A clan ceremony nobody in the family invited friends to |
| Fiery, bold, adventurous | Loud challenges, showing off | A family dinner where they're compared to a sibling |
| Reserved, thoughtful, curious | Quiet superiority, books | A family that sends a letter instead of coming |
| Warm, playful, gentle | Joking competition that hides hurt | A household too busy (a shop, a clinic) to notice |

Clan: an Uchiha rival awakens the Sharingan's first tomoe in the Ch 29 spar with you (a Varied rival:
their clan art's first real strength); a
rival of another clan shows that clan's first-tier art; a clanless rival's pride is in being
self-taught.

## New flags

- `ans.rival.graduation` (went / let_go)
- `ans.rival.forest` (wont_tell / proud / suit; asked in Ch 29)
- `ans.rival.team` (worse / apples / great)
- `ans.rival.give_up` (right / no_one / could)
- `ans.rival.spar_last` (deal / draw / you_win)
- `ans.rival.score` (trying / helps_some / lonely)
- `hides:family` (bond flag on the rival until Ch 43)
- `ans.rival.sibling` (they_asked / better / should_have)
- `ans.rival.finals` (you / me / find_out)
- `ans.rival.clan` (not_born / carry / make_right)
- `ans.rival.ordinary` (best_ordinary / not / held_wall)
- `ans.rival.hokage` (both / right_hand / surpass)
- Option ids for existing: `.fall`: `truth`, `nobody`, `dare`; `.theirs`: `memory`, `hold_on`,
  `chosen`; `.why_came`: `youd_come`, `wanted`, `asked`
