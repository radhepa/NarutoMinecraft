# `role:classmate_c` and `role:classmate_d`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Arcs:
> [ARCS/](../ARCS/). Rules: [WORLD.md](../WORLD.md).

The two classmates who end up on the rival's squad: Squad 2, under `sensei_2`. Smaller arcs than the teammates, but each has a
through-line the finale pays off: **c makes things that last; d stands where it matters.**

## At a glance

| | `role:classmate_c` | `role:classmate_d` |
|---|---|---|
| Name | Given Family; Classic family name Kinoshita | Given Family; Classic family name Gekko |
| Look | Classic: curated (a Kinoshita carpenter's child, sawdust in the hair, a pencil behind the ear). Varied: rolled | Classic: curated (a Gekko: pale, tired eyes, a wooden practice sword, straight back). Varied: rolled |
| Pronouns | Rolled: *they*, tokens | Rolled: *they*, tokens |
| Clan (Classic) | Kinoshita (minor; carpenters and builders) | Gekko (noble; swordsmen of the Crescent Moon) |
| Rank | Genin → Chunin (Ch 20 or the next season) → a builder-shinobi (engineering corps) | Genin → Chunin → Jonin → the Hokage's guard (Ch 55) |
| Archetype | **thoughtful** | **protective** |
| Values | knowledge, honesty | loyalty, family |
| Peeves | rudeness, bragging | recklessness, cruelty |
| Dream | "build something lasting" | "protect the village" |
| Family | A big, loud carpenter family; the Ch 6 study night is at their table | A quiet sword family; an older sibling in the Hokage's guard |
| First / last | Ch 1 (lends you a pencil) / Ch 55 (the clan hall door in the epilogue) | Ch 1 (wooden sword) / Ch 55 (takes the post as your guard) |

## Arc

### Squad 2

Both are on the rival's Squad 2 under `sensei_2` (Classic: a cool, teasing Shiranui who calls
your sensei their rival). c is the squad's peacemaker, d its shield; sensei_2's teasing of your
sensei gives c and d a running joke with you ("Our sensei says yours eats apples to look
mysterious").

### classmate_c

- **Wants:** to make something that outlives them; to be useful without being in charge.
- **Fears:** waste (a thing built badly, a life spent on nothing); arguments (they go quiet).
- **Secret:** they are better at maths than anyone at the Academy and hide it so the rival won't
  make it a contest.
- **Knows:** your gift at Ch 40 with the village; the renamed families at Ch 40 (their family
  carves the memorial in Ch 41).
- **Changes:** Cinders: hosts the study night, the first table you ever sat at as a guest (6.1).
  Paper Trail: on the rival's squad, the peacemaker. Embers: builds the Tobari quarter's barricades
  down after the crisis (Ch 31, a cameo). Ashes: re-carves the memorial with their family (Ch 41).
  Last Bonfire: builds your clan hall's door (Ch 46), holds the Residence steps beside d in Ch 51a,
  and rebuilds the market after the war (Ch 54).
- **Ending:** the epilogue's last workshop scene: they teach your house's children to plane wood.

### classmate_d

- **Wants:** to stand in front of the people they love; to be worthy of the family's sword.
- **Fears:** being too slow (an older sibling was injured because d hesitated as a child: their
  secret); recklessness in others.
- **Secret:** the sibling's injury (told at level 7).
- **Knows:** your gift at Ch 25 (they visit the hospital after Ch 24 with the rival's squad) or
  Ch 40.
- **Changes:** Cinders: dawn kata alone (B1 bond quest). Paper Trail: the rival squad's shield.
  Dusk: your preliminaries opponent (Ch 17); careful, protective even in a bout. Embers: guards the
  council chamber during Ch 31. Ashes: a Jonin. Last Bonfire: holds the Residence steps in Ch 51a with classmate_c (sensei_2 sent Squad 2 to the
  stair and the Residence);
  takes the post of your guard in Ch 55, quoting your answer.
- **Ending:** standing beside (or in front of) the Eighth, by your answer.

## Dialogue brief

### Voice

| | classmate_c | classmate_d |
|---|---|---|
| Child | Slow, careful, explains things with measurements ("That beam's two hands too short"); asks "why" a lot | Formal, short, polite; says "Understood"; worries aloud about others' safety |
| Teen | Dry humour about the rival; mild, firm disagreements | Calmer; teases you about recklessness |
| Adult | A builder's patience; talks in "we'll need" | Soldierly, warm under it; "I've got your left" |
| Never | Raises their voice; brags (peeve) | Mocks anyone; charges in without a plan |
| Tics | Taps surfaces to test them; carries a pencil everywhere | Adjusts their sword before speaking; checks exits |

Voice samples, not shipped lines:
- (c, child, Ch 6) "Sit, sit. Mum cooks for twelve whether there's twelve or not."
- (c, adult, Ch 46) "I carved what you said. Took me three weeks. Don't cry on the wood."
- (d, child, B1) "You came. Good. Watch my left foot. Tell me if it's slow."
- (d, teen, Ch 17) "I won't go easy. That would be rude."
- (d, adult, Ch 55) "You asked me once if it's braver to stand in front or beside. I've decided."

### Topics

| Depth | classmate_c | classmate_d |
|---|---|---|
| 0 to 2 | Wood, tools, the Academy's leaky roof, food at their house | Swords, footwork, the moon-viewing platform |
| 3 to 4 | The family yard; the rival squad's fights | The sibling in the guard; the Gekko and Namiashi rivalry |
| 5 | Honest work; things built to last | Loyalty; who you protect first |
| 6 | The dream: a building that outlives them | The dream: the guard |
| 7 | Worry: that wars waste everything they build | The secret: the sibling's injury |

### Never reveal before

| Secret / fact | Gate |
|---|---|
| c's hidden maths | Level 5 (or a shogi hangout) |
| d's sibling's injury | Level 7 |
| Anything about your gift (they don't know) | Ch 25 (d) / Ch 40 (c) |

### Questions for the player

| Id | Who, when | Question | Options | Remembered / changes |
|---|---|---|---|---|
| `ans.classmate_c.make` | c, B1 bond (L2) | "What would you make for someone you've never met?" | a door that's always open / a bowl / a name plate / a bed | Carved into your clan hall's door (Ch 46; **unset**: a plain watch-fire basket in the lintel, and c says "I didn't know what you'd want, so I made what I'd want"). The options echo the porter's door, the ramen bowl, the chiselled names and the first home |
| `ans.classmate_c.last` (new) | c, Genin hangout (L4) | "What's the oldest thing you've ever touched?" | the memorial stone / the cord / my charm / the Rock | Ch 41: they show you the oldest stone they carve |
| `ans.classmate_c.argue` (new) | c, Chunin (L5), after the rival squad quarrels | "When friends fight, do you take a side or hold the ladder?" | take a side / hold the ladder / walk away until they cool | How c mediates in Ch 40's aftermath wave (a scene in `side.j.roots`) |
| `ans.classmate_c.rebuild` (new) | c, Ch 54 | "Rebuild it like it was, or better?" | like it was / better / ask the people who live there | The market's new look in the epilogue |
| `ans.classmate_c.table` (new) | c, Ch 6 study night (L1) | "Is it weird, eating with a family this loud?" | it's nice / it's a lot / I've never had one | family | Ch 46 (they invite your house to dinner) | They make you a standing place at the table |
| `ans.classmate_c.squad2` (new) | c, Genin (L3) | "How do I keep the rival and d from fighting?" | feed them / give them the same enemy / let them, then fix it | knowledge, kindness | Ch 33 (they keep the peace at the trial), epilogue | Their way of leading |
| `ans.classmate_c.war` (new) | c, Ch 50 or the war's eve (L5) | "Everything I built might burn when they come. Was it worth building?" | yes / build it again after / that's why it matters | building | Ch 54 rebuild (`ans.classmate_c.rebuild` reads it too) | Their resolve |
| `ans.classmate_d.guard` (new) | d, Chunin (L4) | "My sibling says the guard is boring. Is it wrong to want boring?" | no, boring means everyone's safe / a little / you'll never be bored next to me | loyalty | Ch 55 guard post line | Confirms the dream |
| `ans.classmate_d.sensei2` (new) | d, Genin (L3) | "Our sensei teases yours constantly. Should I stop them?" | no, it's how they say they like each other / yes / join in | playful | Ch 42 (d laughs at sensei_2's speech) | Small: lightness |
| `ans.classmate_d.night` (new) | d, the war's eve (L6) | "If I fall, who do I tell first?" | your sibling / me / no one, you won't fall | family, protective | Ch 51b.2, as the crossing passes the Residence steps (d holds them with c; if *no one*, they joke about it mid-fight; **unset**: they say nothing and hold) | Their courage under fear |
| `ans.classmate_d.stand` | d, B1 bond (L2) | "Is it braver to stand in front of someone or beside them?" | in front / beside / behind, to catch them | Ch 55.3: their post as your guard, in that position (**unset**: beside), and their line |
| `ans.classmate_d.hesitate` (new) | d, Ch 17 after the bout | "I hesitated, once. Did you see?" | yes / no / hesitating isn't the same as failing | Their Chunin promotion speech; their training ritual with you |
| `ans.classmate_d.reckless` (new) | d, after Ch 24 (L5) | "Your sensei said fall back. Staying: is it brave or stupid?" | brave / stupid / both, and I'd do it again | Ch 51b.2, the Residence steps (as the crossing passes: *brave* d covers your left without asking; *stupid* they argue first, then cover it; *again* they laugh and say "so would I"; unset: they cover it) |
| `ans.classmate_d.sibling` (new) | d, level 7 (Jonin) | "Should I tell my sibling I've blamed myself all these years?" | yes / no, carry it / tell them you're grateful instead | An epilogue scene with the sibling |

### What their lines are for

- **Functions:** a wider circle (classmates count toward the bond web's breadth), set-up and payoff
  (the door, the guard post), texture (family life the player never had, at c's table), a sparring
  partner (d), memorial builders (c).
- **States:** they are rarely in quarrels; their pools need jealousy only if you were their closest
  and joined another squad (a short `felt_overlooked` line at Ch 8).
- **Pools:** greetings by level; topics; hangouts (c: library, shogi, market; d: training, moon
  viewing, shrine); one highlight each.

### Variants

**Archetype skins (Varied).** Role-fixed: c is the maker who hosts the Ch 6 study night and
carves/builds (Ch 41, 46); d is the protector who fights you in Ch 17 and guards you in Ch 55. If
Varied rolls c as non-craft, the craft becomes the family trade of their roll (a smith's child
forges the door's hinges; a florist's child plants the memorial garden; a clanless shinobi's child
carves anyway, badly, and the carving is loved). If d is rolled as non-sword, their art is their
clan's or a staff/taijutsu; the guard post stays.

**Romance.** Either may become a romance from the teen stage; it changes their B-rank and Jonin
hangout lines and gives them the spouse slot of Ch 53 if married (their line is in DIALOGUE_BRIEFS, "The Ch 53
speaking rule"). Never in the child stage.

**Squad changes.** If any teammate leaves from Ch 8 on (Ch 26 *left*, a falling-out, a low bond),
the stand-in squadmate is `classmate_c` (or `classmate_d` if c is unavailable), lent from Squad 2 by `sensei_2` with a great show of
reluctance: their bond gains `mission_together` fast, and their lines
for the Embers chapters need a squad pool (`bond.squad.standin.<role>`).

**Unison techniques (Blaze tier, light):** c and you: "Raised Beam" (c's earth or wood frame
Kindled into a bridge or wall in seconds; a rescue technique); d and you: "Crescent and Ember"
(the Gekko three-way strike with your ember-gold flame filling the clones' blades).

## New flags

- `ans.classmate_c.table` (nice / a_lot / never_had)
- `ans.classmate_c.squad2` (feed / same_enemy / let_them)
- `ans.classmate_c.war` (yes / again / matters)
- `ans.classmate_d.guard` (safe / little / never_bored)
- `ans.classmate_d.sensei2` (no / yes / join)
- `ans.classmate_d.night` (sibling / me / no_one)
- `ans.classmate_c.make` (door / bowl / name_plate / bed)
- `ans.classmate_c.last` (stone / cord / charm / rock)
- `ans.classmate_c.argue` (side / ladder / walk_away)
- `ans.classmate_c.rebuild` (as_was / better / ask)
- `ans.classmate_d.stand` (front / beside / behind)
- `ans.classmate_d.hesitate` (yes / no / not_failing)
- `ans.classmate_d.reckless` (brave / stupid / again)
- `ans.classmate_d.sibling` (tell / carry / grateful)
