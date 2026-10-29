# `role:sensei` (also `role:captain`)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Backstory:
> [WORLD.md](../WORLD.md). Rotations: [ROTATIONS.md](../ROTATIONS.md).

## At a glance

| | |
|---|---|
| Role | `role:captain` in Ch 0 to 7, `role:sensei` from Ch 8 (one character, two role ids bound to the same resident); the **Seventh Hokage** from Ch 42 (`{hokage:7}` resolves to them) |
| Look | Classic: curated (a quiet clanless Jonin with an old burn scar down the neck and left forearm). Varied: rolled, but **the burn scar is always added** (a mark the story needs) |
| Pronouns | Rolled with the look in Varied: *they* here; dialogue uses `{they:sensei}`, `{them:sensei}`, `{their:sensei}` |
| Clan | Classic: clanless. Varied: rolled from shinobi groups (the story never depends on it) |
| Rank | Jonin → Hokage (Ch 42) |
| Archetype | Classic: **reserved** (warmth -.2, discipline .3, openness -.8). Varied: rolled; the arc reads the same with any archetype, only the voice changes |
| Values | Freedom, honesty (Classic); in every save the story treats **loyalty to the dead** as theirs |
| Peeves | Nosiness, rudeness (Classic) |
| Dream | Classic: *protect the village*; the true one, unspoken: *not to lose another student the way they lost a teammate* |
| First / last | Ch 0 (the raid) / Ch 55 (the succession) and the epilogue |

## Arc

**Wants.** To keep the child they carried over the ravine alive and whole. Underneath, to undo the
Ash Road: to have pulled `fallen_parent` out of that fire.

**Fears.** That the fire which killed their teammate lives in the child; that they will be too slow
again; that the village they serve buried their teammate's death on purpose (it did, and they
signed the report).

**Secrets.**
- They signed the sealed Ash Road report that called the ambush bandits (Ch 36 reveals it was
  Yūgure; they did not know then, but they chose not to ask).
- They know the watch-fire song from `fallen_parent`, who hummed it on missions (Ch 18).
- They saw a campfire lean toward their old team. They recognise your flame (Ch 14).
- *Lineage B only:* they keep a box with `fallen_parent`'s forehead protector and half a watch-fire
  charm. They do not know the child had the other half until Ch 48.
- They leave a persimmon at the memorial stone every year on the Ash Road anniversary.

**What they know and when.**

| Knowledge | From |
|---|---|
| The player is a nursery child, "Nine" to the guards | Never told; they read only the raid's list of children (numbers were not on it). They never say "Nine" |
| The child points toward the lost girl (if `ans.captain.ch0 = point`) | Ch 0: their first failure with you; they never stop looking for her |
| The bell flicker | Ch 8 (they see it, say nothing) |
| Chakra paper chars near the player | Ch 11 (if shown) or Ch 14 |
| The persimmon tree (if `story.lineage.persimmon_told`) | Ch 14 |
| The watch-fire song in the player's mouth | Ch 16 (heard from the tower report) / Ch 18 (if sung) |
| The word "Kagari" was said to the player | Ch 19 (they were there with a kunai at her throat) |
| The flame is the same as `fallen_parent`'s | Ch 24 to 25 (certain) |
| The Ash Road was Yūgure, and why | Ch 36 |
| The Quiet Ending, the twenty-seven | Ch 36 to 37 |
| The Hollow Crown | Ch 49 |
| *Lineage B:* the player is their teammate's child | Ch 48 (the charm halves fit) |
| *Lineage A:* the second is the player's mother | Ch 48 to 49 (from the player, or the council) |

**How they change.**

| Arc | Change |
|---|---|
| 1 Cinders | A rescuer who keeps their distance: carries you out, then hands you to the instructor and the village |
| 2 Paper Trail | Becomes your teacher by refusing to teach in words; starts to suspect (Ch 14) and decides to stay close rather than report |
| 3 Dusk | Protects you openly for the first time (the kunai at the second's throat); the warning "Don't say it" |
| 4 Embers | Breaks their own rule of distance: trains a forbidden gift at night, against the Fifth's watch |
| 5 Ashes | Learns their own signature buried their teammate's truth; cries once (if you follow them, Ch 36); accepts the hat because the village must be led by someone who was wrong and admits it |
| 6 Night Watch | As Hokage (or under the Sixth), the authority you bring the Undercroft to; their choice follows yours |
| 7 Last Bonfire | Leads the war; tells the truth in lineage B; names you successor and stops trying to carry everything |

**Endings and variants.**

| Slot / choice | Effect on them |
|---|---|
| `twist.lineage = fallen` | The Ch 48 walk and box; their succession speech names `fallen_parent` as your parent |
| `twist.lineage = second` | Ch 48 is the second's scene; they learn after. Their guilt stays about the teammate and about not seeing the flame. Their speech names the second (alive or remembered) |
| `twist.fourth_fate` | Falls: they carry the Fourth's coffin. Crippled or taken: they consult him as Hokage |
| `twist.traitor = councillor` | The councillor co-signed the Ash Road sealing; their scene in Ch 39 adds one line of cold anger |
| `ans.sensei.orders` | Their inaugural speech (Ch 42) and the order to fall back (Ch 24) |
| Sensei trust under 50 at Ch 25 | Training comes from the keeper or librarian; the sensei stays distant until Ch 36 and says "I should have been the one" |
| `ans.player.archive_follow = sensei` | The Rock scene: they cry, then ask you to call them by their given name when no one is listening |

## Dialogue brief

### Voice

Short sentences. Answers questions with questions or with silence. Never praises in public; praises
in private with one word ("Good."). Eats an apple when they want to look relaxed and are not.
Says your name rarely, so it lands. Calls the Hokage "the old man" / "the boss" only in private.
Never says "I'm sorry" until Ch 48; never explains the scar until Ch 36; never says "Kagari" before
you do.

Voice samples, not shipped lines:
- "Two bells. Three of you. Noon."
- "That's twice now the paper's done that near you. Where were you born, {given:player}?"
- "Keep your fire low until you need it."
- "...Good."
- (Ch 25) "I've seen that fire before. Once. I couldn't keep it lit."
- (as Hokage) "I'll still be around to complain. Go on."

### Topics they care about

| Topic (level) | What they say |
|---|---|
| Small talk (0) | Weather and food in two words; deflects with a question about your training |
| Training (1) | Their real love: exact, practical, specific to your last fight |
| Their hobby (2) | Whittling (shavings in their pockets); later they whittle a small watch-fire basket |
| Their family (4) | "Had a team. That's family enough." |
| Your story (4) | They listen without interrupting and remember every detail |
| Their values (5) | "Come back with everyone. Then the mission." |
| Their advice (5) | Practical and blunt; for grief: "Eat something. Then cry. In that order." |
| Their dream (6) | Before Ch 36: "To be bored. Old and bored." After: "That nobody signs a lie for me again." |
| What worries them (7) | You. Said plainly once, then never again |

### Never reveal before

| Fact | Not before |
|---|---|
| Their teammate had "your fire" | Ch 25 (`story.kindling.awakened`) |
| The song is their teammate's song | Ch 25; before, they only react (turn away) |
| The Ash Road was Yūgure; they signed the sealed report | Ch 36 |
| The persimmon at the stone is for their teammate (they may leave it in view in Ch 21; the reason only at Ch 21.3 as "They loved these") | Ch 21 |
| The box and the charm half (lineage B only) | Ch 48; never in lineage A saves |
| "Your parent" (either lineage) | Ch 48 |
| The second's name or identity | Ch 26 (her face) / Ch 48 to 49 |
| Anything about the Quiet Ending | Ch 36 |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes them |
|---|---|---|---|---|---|---|
| `ans.captain.ch0` | Ch 0.4 (the raid) | (not a question: the look) | run / hide / point | — | Ch 24 ("You pointed, that night. I sent two people. I should have gone myself") if point | Point: they carry the lost girl as their own failure and ask after her in Ch 44 |
| `ans.sensei.orders` | Ch 8.4 | "When I give an order you think is wrong, what will you do?" | obey / ask / right | Obey: their discipline; Ask: their honesty; Right: their freedom (and their fear) | Ch 24.3; Ch 42 inaugural speech | Shapes how the Seventh commands: obey → strict; ask → explains orders; right → "Do it right" |
| `ans.sensei.stone` | Ch 10.2 | (at the memorial stone) | gap / name / silence | Silence honours them (`stood_by_them`) | Ch 21.3, Ch 41 ("You stood there with me once") | Silence: they open up one beat earlier at Ch 25 |
| `ans.sensei.ash_road` | Ch 13.2 | (at the waystation) | ask / dont | Asking gently is fine; never prying here | Ch 36.6 | Asked: at Ch 36 they say "You asked me once. Here's the answer" |
| `ans.sensei.born` | Ch 14.4 | "Where were you born?" | truth (the tree, the camps) / dont_know / why | Honesty | Ch 21.3, Ch 48 | Truth: sets up the persimmon blow; why: they respect it and answer "Because I'm afraid for you" |
| `ans.sensei.song` | Ch 18.1 | (asks about the hummed song) | sing / dont_know / dream | — | Ch 25.4, Ch 48 | Sing: they know it is their teammate's; they hum it back in Ch 53 |
| `ans.sensei.kagari_word` | Ch 20.5 | "Don't say it to anyone. Not yet." | promise / ask / silent | Promise kept through Ch 22: `kept_promise` | Ch 22.2 | Promise kept: their trust passes 50 earlier (secret training) |
| `ans.sensei.know` | Ch 25.4 | "Do you want to know what you are? Even if it changes how you see yourself?" | everything / need / no | Everything: their honesty; No: their freedom ("Good answer too") | Ch 36 (how much they bring you), Ch 53 line | Everything: they bring you to the archive with them in Ch 36 |
| `ans.sensei.apple` | Level 4, a training hangout | "Why do you think I'm always eating something when I'm worried?" | to look calm / to have something to do with my hands / you're just hungry | — (filler with a function: shows they know you see them) | Ch 49 war council: they hold an apple and don't eat it | — |
| `ans.sensei.hat` | Ch 42, before the succession (level 6) | "Should someone who signed a lie be Hokage?" | yes, because you know the cost / no, but you're the best we have / only if you say it out loud | Honesty | Ch 42 speech: they confess the signature in public if "say it out loud" | Changes the Seventh's first act: a public confession, or a quiet one to the council |
| `ans.sensei.successor` | Ch 54.4 | "Do you want it? Honestly." | yes / not yet / only if you stay near | — | Ch 55.2 | "Only if you stay near": they become your advisor in the post-game |

### What their lines are for

- **Plot:** the rescue, the bell test, the suspicion, the recommendation, the warning, the secret
  training, the archive, the war council, the succession.
- **Clue (lineage):** the song reaction, the persimmon, the stone. Must read identically in both
  lineages until Ch 48.
- **Bond:** their trust meter gates training (Ch 25); their sparse praise is the reward.
- **Teach:** squad commands (Ch 8), tree walking (Ch 10), water walking (Ch 12), the exam technique
  (Ch 18), Kindling (Ch 25 onward).
- **Life:** apples, late arrivals, paying at the barbecue house under protest.
- **Pools:** greetings per arc (captain: formal; sensei: clipped; Hokage: tired and warm);
  quarrel pools (cold shoulder = they assign you to the dullest D-ranks); a `bond.seen.disobeyed_orders`
  reaction that reads `ans.sensei.orders`.

### Variants

- **Varied archetypes:** keep the clipped surface for every archetype; a warmhearted roll speaks more
  but still dodges the scar; a fiery roll is loud in training and silent at the stone. The scar and
  the apple habit stay in every save.
- **Lineage A vs B:** identical through Ch 47. In A, Ch 48 is not theirs; their Ch 49 line: "She
  saved you twice. I can work with that."
- **Trust under 50 (Ch 25):** a "distant" pool through the Chunin arc.

## New flags

- `ans.sensei.apple` (to_look_calm, hands, hungry)
- `ans.sensei.hat` (yes_cost, best_we_have, out_loud)
- `ans.sensei.successor` (yes, not_yet, stay_near)
