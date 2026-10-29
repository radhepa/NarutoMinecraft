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
Ch 19 finals bout interrupted by the attack (and they cover you if both teammates are under 4);
the Ch 29 spar; the Jonin trial pair (Ch 33); the family ceremony (Ch 43); the flame in Ch 53.

## Arc

**Wants.** To be strongest; underneath, to be *seen* by a family that looked past them. Nobody from
their family came to their Academy graduation (Ch 7: a beat the player can notice — the rival
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
| You lost the finals bout to the smoke, not to them | Ch 19 (they never let it go) |
| The rumour of your fire | Ch 29 |
| What the gift is (that it needs consent) | Ch 29 (if you tell them) or Ch 40 |
| Kagari | Ch 40 |
| The Hollow Crown | Ch 49 (as the Seventh's captain) |

**How they change.**

| Arc | Change |
|---|---|
| Cinders | Contempt for "nobodies", then a crack: you fell like someone who'd been fighting longer |
| Paper Trail | Rivalry as their only way to talk to you |
| Dusk | The finals bout: their best, stolen by the attack; they may cover you |
| Embers | Hurt pride at the gift; asks what's left when the people are gone (Ch 29) |
| Ashes | Fights better beside you (Ch 33); lets you see their family (Ch 43) |
| Last Bonfire | Offers their flame (Ch 53): the proudest person in the village choosing to give |

**Endings and variants.**
- **Ch 19 cover:** with both teammates under level 4, the rival takes the blade meant for you
  (`saved_by_them`). Their Ch 20 line: "Don't thank me. I want our match back."
- **Ch 51b, fixed in every save:** on the Rock's stair the rival holds the way against the strongest
  hearth so you can climb: "Go. You owe me a match." They are badly hurt and live; the match is
  paid in the epilogue (`ans.rival.spar_last`).
- **Ch 29 answer** (`ans.rival.theirs`) decides their Ch 53 line: *my memory of them* → "Then
  remember me. Take it."; *nothing, so I won't let them go* → "Then don't let go."; *me, the person
  they chose to trust* → "You said I'd be what's left. Then take it." (ARCS/7 already uses this
  last line; the others are the alternates.) **Unset** (Ch 29 skipped): "I'm not giving you this
  because I lost. Take it."
- **Ch 43** (`ans.rival.why_came`) adds the second half of the Ch 53 line: *you'd have come for me*
  → "You were right. I came."; *I wanted to* → "I wanted to."; *you asked* → "You didn't even ask."; **unset** (Ch 43 skipped):
  no second half
- If you **never go** to the ceremony (Ch 43), they still kindle at 6+, without the second half.
- **Romance** (teen and up): a rival romance is slow (pride); the confession is a challenge ("Spar
  me. If I win, you hear something."). Never in the child stage.
- **Thread Sight on them** (from Ch 24, level 6+): their thread is thin, taut and bright, like
  wire; it flickers when they hide being hurt (the Ch 43 family, a loss to you). Ch 29's spar is
  their first look at the gift: they ask if you can see what they think; you can't, and say so.
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

- **Child:** clipped, cutting, few words; "Hmph" is allowed once a chapter, no more; questions
  disguised as insults.
- **Teen:** the same clipped voice with more vocabulary; compliments that sound like complaints
  ("That was barely adequate. Again.").
- **Adult:** dry, loyal, still competitive about trivial things (who orders faster at Ichiraku);
  says "we" exactly once (Ch 53).
- **Never:** says thank you plainly before Ch 43; cries in front of you; brags about their clan
  (peeve); asks personal questions directly (peeve: nosiness) — they ask sideways.
- **Tics:** crossed arms; "Again." after any spar; keeps score of everything aloud.

Voice samples, not shipped lines:
- (child, Ch 1) "Another one from nowhere."
- (child, Ch 2) "Who taught you to fall like that? Nobody falls like that here."
- (teen, Ch 29) "Is it yours, or theirs?"
- (teen, Ch 20) "Don't thank me. I want our match back."
- (adult, Ch 43) "Why did you come?"
- (adult, Ch 53) "You said I'd be what's left. Then take it."

### Topics they care about

| Depth | Topics |
|---|---|
| 0 to 2 | Training, technique, the score, who's strongest in the year |
| 3 to 4 | Their clan's expectations; the sibling; the police quarter |
| 5 | Values: strength earned; family as duty |
| 6 | The dream as it changes |
| 7 | Worries: being ordinary; that giving makes you weak |
| Shared memory | The Ch 2 spar, the stolen finals, the Rock spar (Ch 29), the trial (Ch 33) |

### Never reveal before

| Secret / fact | Gate |
|---|---|
| Nobody came to their graduation | Ch 43 (said); seen in Ch 7.3b, where the player can go to them or let them be |
| The sibling's secret training | `side.b3.rivals_sibling` (the sibling tells you, not the rival) |
| The fear about gifts | Ch 29 |
| Any warmth toward you in words | Ch 43 |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes them |
|---|---|---|---|---|---|---|
| `ans.rival.fall` | Ch 2.3 | "Who taught you to fall like that?" | the truth, the camps / nobody / you'll have to beat it out of me | truth earns respect; *nobody* reads as bragging-adjacent (they don't believe you); the dare raises rivalry | Ch 20, Ch 43 ("You told me about the camps when we were eleven. I never told anyone.") | Truth: the first crack; dare: a pure rivalry track |
| `ans.rival.theirs` | Ch 29.3 | "If your strength comes from other people, what's left when they're gone?" | my memory of them / nothing, so I won't let them go / me, the person they chose to trust | strength (all three answer it); *the person they chose* honours it most for the proud | Ch 53 flame line | How they come to see strength |
| `ans.rival.why_came` | Ch 43.2 | "Why did you come?" | because you'd have come for me / because I wanted to / because you asked | family | Ch 53 second half | They admit the bond (or not) |
| `ans.rival.score` (new) | Genin, after a spar (L2) | "Keep score with me. Every spar until we're Jonin. Deal?" | deal / only if I keep the book / no, I'd rather just train with you | rivalry vs warmth | Ch 33 (they read the final tally after the trial) | *no*: the rival is stung, then trains with you weekly (a ritual) |
| `ans.rival.sibling` (new) | Ch 18, after `side.b3.rivals_sibling` | "You trained my sibling. Behind my back." | they asked me / they'll be better than both of us / you should've trained them | family | Ch 43 (the sibling attends the ceremony, or not) | *you should've*: the rival trains the sibling; the sibling comes to Ch 43 |
| `ans.rival.finals` (new) | Ch 20.4 or Chunin talk (L3) | "Who would have won the finals?" | you / me / we'll never know, so let's find out | pride | Ch 33 trial line; epilogue spar | *let's find out*: a ritual spar on the Rock each year |
| `ans.rival.clan` (new) | Ch 40 aftermath (L6) | "My clan's elder forged it. Do I carry that?" | no, you weren't born / yes, we all carry the village's / carry it by making it right | family, honesty | Ch 40 council break; Ch 51 (they fight beside the Kagari house's members) | Whether they stand up in the council |
| `ans.rival.ordinary` (new) | Jonin, level 7 (worries) | "What if I'm just... ordinary? Good, but ordinary." | then be the best ordinary there is / you're not / ordinary people held the wall in the war | honesty | Ch 51 wall scene (if "ordinary people" — they say it to the defenders) | Settles their fear |
| `ans.rival.graduation` | Ch 7.3b | (the rival alone after the speech; nobody came for them) | go to them / let them be | *go*: they snap "What?", then don't leave; respect for leaving them their pride if *let go* | Ch 43.1 ("You came over at graduation. I hated it. I've thought about it every year." / "You left me alone at graduation. That was the kindest thing anyone did that day.") | Whether the Ch 43 invitation is a return of a favour or a first reach |
| `ans.rival.forest` (new) | Ch 16, after the ravine glimpse (L3) | "You saw my eyes. Don't tell anyone until I show them." | I won't / you should be proud of them / they suit you | honesty, pride | Ch 19 finals (they reveal them with a glance at you) | *won't*: trust +; *proud*: they're annoyed and pleased |
| `ans.rival.team` (new) | Genin, after `sensei_2`'s teasing (L3) | "Is your sensei as embarrassing as mine?" | worse / mine eats apples to look mysterious / yours is great, actually | playful (filler) | A running joke; Ch 42 (sensei_2 at the Seventh's naming, and the rival's line) | Small: their softening toward their own sensei |
| `ans.rival.give_up` (new) | Ch 31 aftermath (L5) | "You stood up in front of the whole council for a clan that isn't yours. Why?" | because they were right / because no one stood up for mine / because I could | loyalty, family | Ch 40 (the rival stands in the council for the truth) | Teaches them public courage |
| `ans.rival.spar_last` (new) | Ch 50, before Dusk (L6) | "If we live through tomorrow, you owe me a real finals." | deal / we'll call it a draw forever / you'll win | rivalry | Ch 55 epilogue: the finals rematch on the Rock, and its result (or none) | The last image of the rivalry |
| `ans.rival.hokage` (new) | Ch 54 | "You'll be Hokage. I'd have liked it to be me." | it should have been both of us / you'll be my right hand / you'll surpass me yet | pride | Ch 55 epilogue (their post: captain of the guard's training, or the Academy's hardest teacher) | Their post-game role |

### What their lines are for

- **Functions:** bond, rivalry (the spar pools and the score), mirror (strength earned vs given:
  the thematic opponent of the gift who becomes its proudest giver), comedy (pettiness at
  Ichiraku), a plot body in battles (Ch 19, 33, 51).
- **States:** rivalry is not dislike (BONDS §2): greeting pools by *rivalry* height as well as level.
  Quarrel: proud and slow to heal; they never apologise first (a `making_up` pool where they
  "happen" to train at your ground).
- **Pools:** greetings by level, rivalry and state; spar banter (before/after, win/lose); topics;
  hangouts: sparring, training, rooftop race, shogi; highlights (the first win, the trial).

### Variants

**Archetype skins (Varied).** Role-fixed: pride, the score, another squad, the family that looked
past them, the Ch 53 flame. A Varied rival rolled as gentle or warm keeps a proud *stance* in the
rival role (pride is lifted to at least .5 for the role) but the cover changes:

| Archetype group | Their pride shows as | Ch 43 family beat |
|---|---|---|
| Proud, stern, meticulous (Classic) | Contempt, scorekeeping | A clan ceremony nobody in the family invited friends to |
| Fiery, bold, adventurous | Loud challenges, showing off | A family dinner where they're compared to a sibling |
| Reserved, thoughtful, curious | Quiet superiority, books | A family that sends a letter instead of coming |
| Warm, playful, gentle | Joking competition that hides hurt | A household too busy (a shop, a clinic) to notice |

Clan: an Uchiha rival awakens the Sharingan in the Forest of Death (Ch 16.5), glimpsed by the player
across the ravine as two red points in the dark; they never mention it until the finals; a
rival of another clan shows that clan's first-tier art; a clanless rival's pride is in being
self-taught.

## New flags

- `ans.rival.graduation` (went / let_go)
- `ans.rival.forest` (wont_tell / proud / suit)
- `ans.rival.team` (worse / apples / great)
- `ans.rival.give_up` (right / no_one / could)
- `ans.rival.spar_last` (deal / draw / you_win)
- `ans.rival.score` (deal / keep_book / just_train)
- `ans.rival.sibling` (they_asked / better / should_have)
- `ans.rival.finals` (you / me / find_out)
- `ans.rival.clan` (not_born / carry / make_right)
- `ans.rival.ordinary` (best_ordinary / not / held_wall)
- `ans.rival.hokage` (both / right_hand / surpass)
- Option ids for existing: `.fall`: `truth`, `nobody`, `dare`; `.theirs`: `memory`, `hold_on`,
  `chosen`; `.why_came`: `youd_come`, `wanted`, `asked`
