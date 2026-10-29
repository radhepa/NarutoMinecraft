# `role:librarian`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). A
> `twist.traitor` candidate: read [ROTATIONS.md](../ROTATIONS.md) §1 first.

## At a glance

| | |
|---|---|
| Role | `role:librarian`, keeper of the Academy library |
| Look | Fixed: a slight woman in her forties, ink-dark hair in a low knot held by two brushes, round spectacles, a grey-green library apron over a plain kimono, a faded red thread around one finger (a habit, not a Yūgure tally) |
| Pronouns | She / her |
| Clan | No clan; an ordinary family name from the pool (the renamed family's Leaf name). She is a renamed Kagari child's granddaughter, and she knows |
| Rank | Chunin (retired from the field at 25 after an injury; walks with a slight limp) |
| Archetype | `thoughtful` (warmth .2, bold −.2, pride 0, discipline .4, open −.2) |
| Values | knowledge, honesty (which she betrays daily by keeping her family's secret) |
| Peeves | rudeness, bragging |
| Dream | "build something lasting": a history of the Leaf that leaves no one out |
| First appearance | Ch 5 |
| Last appearance | Ch 55 (the ruling if bound; the archive or the restored house's song teacher if innocent) |

## Arc

### Common to every save

- Her grandmother was one of the twenty-seven renamed children. Once, at the end of her life, she
  whispered the family's true name (Kagari) and the watch-fire song to the girl, and made her
  swear never to repeat either. The librarian's family kept a hidden notebook: a true history
  of the Quiet Ending as the grandmother remembered it, and the song with its old words.
- She files the Academy aptitude scrolls by shelf mark (`Leaf 7-iii`) and puts a small brushed circle
  beside a child who "might need a little more". She means it kindly in every save. The library
  also files the border outposts' entrance tests with the aptitude scrolls, so border children are
  on her shelves too. The library also
  files the Academy's exam-hall duty rosters, which list the finals' guard posts (one of the routes
  by which a rotation could leak, true in every save).
- She is nervous by nature around authority and around the founding history.
- She writes to a cousin in a border town; in every save the letters go by the ordinary post. (In
  an innocent save the cousin is real; in a bound save the leader's letters come under the same
  cousin's name. Letters are not a movement difference.)
- The fresh-cut page (Ch 5) listed the families who adopted the twenty-seven, under a chapter
  heading about "the settling of the southern hills". It went to Yūgure through the porter in every
  save. It was cut that week because the stipend registry had just flagged a new Kagari-reactive
  child (the player), and the voice was asked to send the page that names the twenty-seven's
  families. Who cut it is the rotation. **She knows what the page listed** (it matches her family
  notebook) in every save.
- **Her every-save secret:** she is a Kagari descendant whose family kept the true history.
- **Her held-back piece:** what the cut page listed. She shares her heritage at Ch 25.3 (if she comes)
  but keeps this until Ch 39 (bound) or Ch 40 (innocent), in every save.

**Thread Sight.** From Ch 24, if she is bonded to the player at 6 or more and the player probes her,
her thread flickers: she is hiding something. In every save she is (her heritage, and after Ch 25.3
the page's contents), so the flicker shows in every rotation, never says what, and **never goes out
before Ch 39 or 40**. Bound, her thread to the player reads as a normal two-way thread. Her tie to the
porter is never visible (the porter is never at 6+ with the player). Her flag is `hides:family_history`.
The flicker is one steady state from a single `hides:` bond flag, never line by line, and it
is not a lie detector: it means *hiding*, nothing more. Each of the four candidates carries exactly
one `hides:` flag of the same kind, from the start of the game until Ch 39/40, in every save. Their
daily schedules and night movements are identical in every save until Ch 39.

### Everything before Ch 39 is identical in both tracks

| Beat | What plays (every save) |
|---|---|
| Ch 5 | The shelving, the circles, the cut page, the lie ("gone for years"), `ans.librarian.forget` |
| `overdue` | The cipher slip in a returned book (`story.clue.librarian.3`) |
| Paper Trail, Dusk | Book recommendations; water at the stadium evacuation |
| Ch 25.1 | A hospital visit with books. **The only line that differs is the slip line** (below) |
| Ch 25.3 | If `friendship [librarian, 3]`: she comes at night with the family notebook, tells the player her family's heritage, sings the song (or offers to, `ans.librarian.song`), shows the drawing of a watch-fire charm and names the gift: Kindling. She asks the player to tell no one where the notebook came from (`bond_flag notebook_secret`; keeping it is a `kept_secret` moment). Else the keeper comes instead. Identical in both tracks |
| Embers | Warm, a little guarded; at level 7 she deflects questions about the page ("Some pages are better read by the right person"). Identical |
| `side.c.returned_book` | **The alibi result differs** (below) |
| Ch 38 | She is not at the case board in any save (she is a suspect, and the player works it with `role:sensei_4`) |

### If innocent

- **Wants:** to keep her family safe and her grandmother's promise; later, to have the truth told by
  someone braver than her.
- **Fears:** being found out; that her silence makes her complicit.
- **The page:** the porter, collecting returns, cut it that morning. She found it at opening time
  and recognised what was gone. Her lie ("gone for years") protects her family's connection to it.
- **The cipher slip:** the porter used the returns cart as a dead drop. She has never seen the cipher.
- **The slip scene (Ch 25.1):** "Rest. Even the smallest flame of a fire needs tending." (No number.)
- **The alibi** (`side.c.returned_book`): the cipher book of `overdue` was returned on the library's
  closed day; she was at the shrine all day (the priest's visitor book shows her in at dawn and out at
  dusk, helping repaint plaques).
- **Ch 40 cleared:** she tells the player what the cut page listed (the adopting families, which
  match the archive's renaming list), gives the family notebook to the archive and stands up at the
  council to say her grandmother's real name aloud. Her training line opens
  (`friendship [librarian, 7]` and the gift awakened): the old forms of the gift, taught from the
  notebook: the watch-fire songs, how the Kagari kept the flame low in peace, how they sat at camp
  fires with the bonded, and the meaning of the ember mark. Lore and practice that deepen Thread
  Sight and Kindle; she teaches no ability of her own.
- **Road to Hokage:** she joins the restored house if the player restores the Kagari and asks (she
  says yes if `friendship 6`). She teaches the song to the new members. In the finale she is a face among the
  flames, with one short line only if she is at level 9 or more.
- **Ending:** keeper of the archive if the player chooses her in Ch 55, or the restored house's
  historian.

### If bound (the voice)

- **Wants:** the truth told and the Kagari restored, "even by fire". For sixteen years the leader wrote to
  her like a cousin, signing as "a fellow keeper of memory", and told her he was finding the lost
  ones before the Leaf could seal them too.
- **Fears:** that he lied; that the children she circled went to nurseries; that the player was one
  of them (she knew, from his letters, before the player came to the Leaf).
- **Secret:** since about Y-10 (by an old east-road carter until Y-6, through the porter since) she
  sent him the shelf marks and circled names of gifted children; the
  exam-hall duty roster for the finals (Ch 19's gap); the news, from the Sixth's clerk, that the
  archive would be open (Ch 37); and, after the porter fell (Ch 28), her own "cousin" letters by the
  ordinary post.
- **The page:** she cut it that morning and gave it to the porter in the returns cart. Her lie is the
  same lie, for a worse reason.
- **The cipher slip:** she used the returns cart as her dead drop.
- **Ch 25.3:** she comes exactly as in the innocent track (if friendship 3). Her heritage is true; the
  gift's name is true; she tells no lie in the scene. What she does not say is that she will write
  to him about it.
- **The slip scene (Ch 25.1):** "Rest. Even the ninth flame of a fire needs tending." She hears
  herself and smooths her apron.
- **The failed alibi:** the shrine's visitor book shows her leaving at noon on the closed day.
- **Ch 38:** the list's notation is shelf marks with brushed circles.
- **Ch 39 reveal:** the library at night, among the aptitude scrolls; the cut page's copy in her
  sleeve. "My grandmother was one of the twenty-seven. She whispered our real name to me once and
  never again. He wrote to me for sixteen years like a cousin. He said he was finding the lost ones. I gave
  him children, and I told myself I was giving them home." The stadium (keyed to `twist.fourth_fate`):
  "I sent him a duty roster. He said the finals would be a show of strength; no one would be hurt."
  *Falls*: "Then the Fourth went down on the stair with children in his arms." / *crippled*: "Then I
  saw him carried past the library in a chair." / *taken*: "Then his seat was empty for a year, and I
  shelved the news." The page, at last: "It listed the
  families. I gave him the families."
- **Fate:** *arrested*: the notebook goes to the archive; she asks to teach the old songs to the
  restored house from her cell (allowed if the player asks the Seventh). *Turned* (she wishes to make
  amends, so turning does not need friendship 4): she keeps writing to the leader, now false news,
  and her false signals delay the assault by an hour; Ch 51a opens with one district's anchors already
  broken (as in every turned save). Either way, Ch 55's ruling: pardon (she
  keeps the archive under watch), exile (she leaves her notebook to the house), or service (she
  teaches the song to every new member, for life).

### How she changes

| Arc | Innocent | Bound |
|---|---|---|
| Cinders to Embers | Nervous, kind; breaks her grandmother's promise for the player (25.3) | Identical (only the Ch 25.1 slip line and the alibi result differ) |
| Ashes | Cleared; tells the page; speaks her name aloud | Revealed; confesses |
| Last Bonfire | Teaches the house its song | Imprisoned or turned; in the finale (turned) her false signals buy an hour |

## Dialogue brief

### Voice

- **Register:** soft, precise, bookish; long sentences she cuts short when nervous.
- **Habits:** corrects grammar under her breath; quotes books by shelf mark ("as 4-ii says");
  pushes up her spectacles before saying something true.
- **Tics:** twists the red thread on her finger when the founding history comes up.
- **Never says:** "Kagari" before Ch 25.3 (and then only alone with the player), in every save;
  what the cut page listed before Ch 39/40; the number nine except in the bound Ch 25.1 slip.

*Voice samples, not shipped lines:*

- (Ch 5) "The circles are mine. Children who might need a little more. Don't tell them; they'd want
  to know what 'more' means, and I don't always know."
- (Ch 5) "That page has been gone for years." (Same line in both tracks.)
- (Ch 25.3, both tracks) "My grandmother sang this to me. She made me promise never to sing it to
  anyone. I think she meant: never to anyone who wouldn't understand."
- (Ch 40, innocent) "My grandmother's name was not the one on her grave. I'd like to say the real
  one. Once, out loud, in a room full of people."
- (Ch 39, bound) "I gave him children, and I told myself I was giving them home."

### Topics they care about

| Depth | Topics |
|---|---|
| 0 to 2 | Books, overdue books, quiet in the library, the Academy's history lessons |
| 3 to 4 | Who writes history; handwriting; her limp (a mission at 25, "a fall, not a fight") |
| 5 to 6 | Lies told to protect people; her grandmother (without the secret) |
| 7+ (both tracks, before Ch 39) | Her family's name (after 25.3); the song's words; whether forgetting is ever kind. Deflects questions about the cut page |

### Never reveal before

| Secret | Gate |
|---|---|
| Her heritage (descendant) | Ch 25.3 and `friendship 3`, alone, in every save; else Ch 39/40 |
| The family notebook | Ch 25.3 (if she comes), every save |
| What the cut page listed | Ch 39 (bound) or Ch 40 (innocent): her held-back piece |
| The duty roster as a leak route | `twist.traitor = librarian` and Ch 39 |
| The letters from "a fellow keeper of memory" | `twist.traitor = librarian` and Ch 39 |
| That she knew the player was a nursery child before Ch 5 | `twist.traitor = librarian` and Ch 39 |
| The number nine | Only the bound Ch 25.1 slip line |
| The alibi details | Only through `side.c.returned_book` or the case board |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes her | Bound answer in Ch 39c |
|---|---|---|---|---|---|---|---|
| `ans.librarian.forget` | Ch 5 | "Do you think some things are better forgotten?" | Yes, if remembering only hurts / No, forgetting is how it happens again / It depends who chose to forget | "No" honours knowledge; "who chose" is her own question | Innocent: Ch 40 ("You said forgetting is how it happens again. I'm done forgetting"). Bound: Ch 39c. Unset: a neutral line about the page | "No" or "who chose": at 25.3 she brings the song's words written out for the player to keep (both tracks; the gate stays `friendship 3`) | "You said it depends who chose. I let him choose for me." |
| `ans.librarian.book` | After Ch 5, level 2 | "What kind of story do you want me to find you?" | Heroes / true things / something sad / anything with food in it | Light; sets her book gifts | Her book gifts all game; a callback when she sends a book to the hospital (Ch 25) | Picks the Ch 25 books | — |
| `ans.librarian.history` | Level 4 | "Who should write history: the people who won, or the people who remember?" | The ones who remember / both, side by side / whoever's honest | Knowledge, honesty | Ch 40's speech; her history of the Leaf's preface (epilogue) | Innocent: her history's shape. Bound: the reason she gives in 39c | "I thought he was the one who remembered." |
| `ans.librarian.lie` | Level 5 | "Have you ever lied to protect someone?" | Yes, and I'd do it again / Yes, and I regret it / No | Tests honesty; she is asking about herself | Ch 39 or 40 | "Again": she trusts the player with the notebook sooner. "Regret": she confesses (bound) without the chase if accused with only one proof | "You said you'd do it again. So would I. That's the worst thing I know about myself." |
| `ans.librarian.name` | Level 6 | "If you found out your family had another name once, would you take it back?" | Yes / No, I'm who I've become / I'd carry both | The heart of her and of the player's future | Ch 46 (the house's founding) | "Both": she proposes the restored house keep the renamed families' Leaf names beside the old one | "He said I could have it back. I wanted it so much I didn't ask the price." |
| `ans.librarian.fire` | Level 7 (Chunin) | "Is it ever right to burn something to make people see it?" | Never / Only your own things / Sometimes nothing else works | Tests her secret creed ("even by fire") | Bound: Ch 39 opens with it. Innocent: Ch 51a (she saves the library's histories from the fire) | If "sometimes", she worries for the player and warns the keeper to check the archive door (both tracks) | "You said never. You were right and I wasn't listening." |
| `ans.librarian.song` | Ch 25.3 if she comes; else level 6 (Ch 26 to 32). Same in both tracks | "Will you sing it for me? Just once, so I know it's real." | Sing / Not yet / Teach me the words first | Kindness | Innocent: she sings with the player at the memorial (Ch 41). Bound: she sings it alone in her cell (heard in Ch 54) | — | "I asked you to sing it so I could tell him how it sounded. I didn't. I kept that one." |
| `ans.librarian.read` | Ch 5 (level 0) | "Can you read well? Some children from... far away never had the chance." | Yes / a little / they taught us numbers, not words | Kindness; "numbers" is the nurseries (identical line in both tracks) | Her book gifts are pitched to the answer; Ch 39 (bound): "You told me they taught you numbers. I knew which number" | "A little": she starts a reading hour the player can attend (life, studied_together) | — |
| `ans.librarian.shelf` | Level 2 | "If someone wrote a book about you, which shelf would it go on?" | Adventures / history / the lost-and-found box / it isn't written yet | Imagination | Epilogue: her history of the Leaf (innocent) or a bound copy she sends from her cell (bound) shelves the player's chapter there | — | — |
| `ans.librarian.circle` | Level 3 (after Ch 7) | "If someone had put a little circle by your name, meaning 'needs more', would you want to know?" | Yes / no / only if they'd help | Honesty; identical in both tracks before Ch 39 | Innocent: she shows the player their own aptitude scroll, with a circle (Ch 40). Bound: Ch 39, the circle beside your own shelf mark on the list | — | — |
| `ans.librarian.who_sang` | Level 4 (Paper Trail) | "Who sang to you when you were small? Everyone has someone." | I don't remember / someone in a house with a tree / no one | Her own grandmother; a small confession back ("Mine did. Once") | Ch 25.3 (both tracks): she starts with it. Bound: Ch 39c adds the answer column | "A tree": she goes very still (both tracks; a fair tell of her heritage, not of the voice) | — |

### What their lines are for

- **Functions:** clue carrier (beta, both tracks identical), lore (the song, the gift's name, the
  twenty-seven), heart of the mystery's sympathy (the bound reveal), ally and teacher (innocent).
- **Mood states:** `nervous` (default), `warm` (level 5+), `confiding` (after 25.3, both tracks),
  `freed` (innocent, after Ch 40), `confessed` (bound, after Ch 39). No mood differs before Ch 39.
- **Pools:** `npc.librarian.*`, `talk.q.librarian.<topic>`, `story.ch25.visit.librarian.<bound|innocent>`.

### Variants

- Identical in Classic and Varied (fixed role and look); name rolled.
- `twist.traitor = librarian`: the bound track. Otherwise innocent.
- `twist.lineage`: no change to her.
- Ch 25.3 reads only `friendship [librarian, 3]`, never the rotation: below it, the keeper comes in
  every save. After a bound reveal, the old forms are taught from her notebook in the archive (by the
  keeper, then the house).
- Every main-path read of an `ans.librarian.*` flag has an `unset` branch (a neutral line).

## New flags

`ans.librarian.book`, `ans.librarian.history`, `ans.librarian.lie`, `ans.librarian.name`,
`ans.librarian.fire`, `ans.librarian.song`, `bond_flag notebook_secret`, `story.ch25.done`, `ans.librarian.read`, `ans.librarian.shelf`, `ans.librarian.circle`, `ans.librarian.who_sang`.
