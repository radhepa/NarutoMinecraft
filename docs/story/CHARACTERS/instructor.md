# `role:instructor`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

## At a glance

| | |
|---|---|
| Role | The Chunin from the rescue; your Academy instructor; later head of the Academy |
| Look | Classic: curated (a cheerful clanless Chunin, sleeves rolled, chalk on everything). Varied: rolled |
| Pronouns | *they*; dialogue uses `{they:instructor}` and the rest |
| Clan | Classic: clanless (an Umino in a save that rolls them so, by chance) |
| Rank | Chunin → Academy head (Jonin arc) |
| Archetype | Classic: **warmhearted** (warmth .8, openness .5) |
| Values | Kindness, family |
| Peeves | Cruelty, neglect |
| Dream | *Be a great teacher* |
| First / last | Ch 0 (the raid, scooping up two children) / Ch 55 (the face question, one last time) |

## Arc

**Wants.** That every child they teach becomes someone, and that no child is ever looked at the way
the nursery children were: as a reading on a slip of paper.

**Fears.** That cheerfulness is all they have, and that one day it will not be enough to keep a
room of children calm (Ch 51 is that day, and it is).

**Secrets.** Small and human:
- **Why they hushed the flare (Ch 3).** Plain protectiveness, not orders. At the raid they saw the
  children counted and slipped like stock; in the village they had already seen the keeper watching
  the new orphan from the Hokage's shoulder. When your chakra flared, they decided no one would
  turn you into a reading again while they were in the room: "Nice control, both of you! Next
  pair!" That evening, worried, they asked the medic to check on you (the innocent explanation of
  `story.clue.medic.2` in every save; in the medic-bound save the medic was glad of the excuse).
- They failed the Jonin exam twice and chose the Academy; they tell it as a joke and it is not one.
- They keep a list of every child they ever taught, with one good thing about each.

**What they know and when.**

| Knowledge | From |
|---|---|
| The flare (they saw it) | Ch 3 |
| The keeper watches you | Ch 1 (they noticed) |
| "Kagari" | Ch 31 (the rumour), Ch 40 (the council) |
| The Quiet Ending | Ch 40 (public) |
| The player's gift in full | Ch 31 or when the player tells them |

**How they change.**

| Arc | Change |
|---|---|
| 1 Cinders | Your first adult in the village: ramen, enrolment, the forehead protector |
| 2 Paper Trail | Hands you to your sensei and pretends not to mind; visits the squad with buns |
| 3 Dusk | Evacuates the Academy children in Ch 19 (seen from the east stair) |
| 4 Embers | Quietly defies the Fifth's curfew to run night lessons for nursery-rescued children |
| 5 Ashes | Becomes Academy head; asks you to teach a class; hears the council and adds the twenty-seven to the history lessons |
| 7 Last Bonfire | Holds the Academy in the assault (Ch 51.2); asks the face question at your carving |

**Endings and variants.**

| | |
|---|---|
| `twist.fourth_fate = crippled/taken` | They share the Academy with the Fourth (who teaches history); comic and tender scenes together |
| `twist.fourth_fate = falls` | They speak at the statue's unveiling (Ch 21) |
| `ans.instructor.face` | Ch 42 and Ch 55 callbacks |
| `ans.player.ramen` | They order it for you whenever they pay |

## Dialogue brief

### Voice

Bright, fast, lots of exclamation points that they half-mean; specific praise ("Your left foot!
Did you see your left foot?"). Teaches with stories and food. Lowers their voice when something is
serious, and children notice. Never mocks a child; never says "you failed", says "not yet". Never
speaks about the raid in front of other children.

Voice samples, not shipped lines:
- "The Academy isn't a test, {given:player}. It's a place. You get to have a place."
- "Nice control, both of you! Next pair!"
- "That's not dust. Okay, it's a little bit not dust."
- "Rows of two! Who wants to see a really big clone?"
- "Whose face would you put up there, if you could pick anyone?"

### Topics they care about

| Topic | What they say |
|---|---|
| Food (1) | Ramen orders as personality tests |
| Their hobby (2) | The list of good things about every pupil; they let you read your own entry at level 6 |
| Their family (4) | A big civilian family in the market; their mother sells pickles and thinks shinobi are silly |
| Their values (5) | "Every kid's worth the whole effort. Every one." |
| Advice (5) | Warm and practical; about the rival: "Lonely people bite. Feed them anyway" |
| Their dream (6) | To run the Academy so well that nobody remembers a child was ever a number |
| Worries (7) | That they hushed the flare and should have asked you instead (said at Ch 31) |

### Never reveal before

| Fact | Not before |
|---|---|
| Why they hushed the flare | Ch 31 (after the gift is public), or level 7 |
| That they asked the medic to visit | Ch 25 (in the medic-innocent save this clears the medic softly; in the medic-bound save the line exists too and stays true) |
| The Jonin exam failures | Level 5 |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes them |
|---|---|---|---|---|---|---|
| `ans.player.ramen` | Ch 1.4 | "Miso or salt?" | miso / salt / pork_bone / yours | — (life) | Forever: the cook calls it; the instructor orders it | — |
| `ans.instructor.face` | Ch 5.3 | "Whose face would you put up there, if you could pick anyone?" | captain / forgotten / mine / yours | Any answer is warm; "yours" makes them laugh and cry | Ch 42.3, Ch 55.4 | "Forgotten": they add the twenty-seven to the curriculum before anyone asks |
| `ans.instructor.not_yet` | Level 3, after a failed lesson (Ch 6 study night or a training hangout) | "When you fail at something, what do you tell yourself?" | not yet / try harder / nothing, I just do it again | Kindness | Ch 7.1 (the retry line uses your words) | — |
| `ans.instructor.number` | Level 5, Ch 21 to 31 (the night lessons) | "Some of these kids only answer to numbers. Should I make them use their names?" | yes, names are theirs / let them choose when / use both until they're ready | Kindness, freedom | Ch 35.4 (how the Valley children are greeted) | Shapes how the Leaf receives nursery children for the rest of the game |
| `ans.instructor.teach` | Ch 40, level 6 | "Would you teach a class here? One class. On the twenty-seven." | yes / not yet / only if a descendant teaches with me | — | Jonin systemic (a class you can teach once a week) | "Descendant": genin_3 or the librarian teaches with you |
| `ans.instructor.list` | Level 7 | They let you read your entry on their list. "Is it right? Did I get you right?" | yes / it's kinder than me / add something (you choose a word) | — | Ch 55 epilogue: the word is on the Academy's wall | — |

### What their lines are for

- **Teach:** almost all Academy tutorials speak through them (Ch 1 to 7): every tutorial line is
  also a small bond line.
- **Bond:** the first adult who is simply kind; their list is a running reward.
- **Plot:** the hush (Ch 3), the medic request, the Academy in Ch 51.
- **Life:** comedy with the Fourth (if alive), the pickle-selling mother, the ramen.
- **Pools:** Academy-era greetings (teacher), later greetings (proud ex-teacher who still calls you
  by your Academy nickname), war greetings (steady, low voice).

### Variants

- Varied archetypes keep the "believes in everyone" spine. A stern roll shows it through drills and
  a single nod; a playful roll through games.
- Clanless or clan: if rolled into a clan, their family scenes move to that quarter.

## New flags

- `ans.instructor.not_yet` (not_yet, harder, again)
- `ans.instructor.number` (names, choose, both)
- `ans.instructor.teach` (yes, not_yet, with_descendant)
- `ans.instructor.list` (yes, kinder, add_word)
