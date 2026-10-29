# `role:sensei` (also `role:captain`)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Backstory:
> [WORLD.md](../WORLD.md). Rotations: [ROTATIONS.md](../ROTATIONS.md).

## At a glance

| | |
|---|---|
| Role | `role:captain` in Ch 0 to 7, `role:sensei` from Ch 8 (one character, two role ids bound to the same resident); the **Seventh Hokage** from Ch 42 (`{hokage:7}` resolves to them) |
| Look | Classic: curated (a quiet Jonin of no clan with an old burn scar down the neck and left forearm). Varied: rolled, but **the burn scar is always added** (a mark the story needs) |
| Pronouns | Rolled with the look in Varied: *they* here; dialogue uses `{they:sensei}`, `{them:sensei}`, `{their:sensei}` |
| Name | Given Family (rolled); Classic: **no clan**, an ordinary family name that never matches a clan. Varied: rolled from shinobi groups (the story never depends on the clan). Called "{family:sensei}-sensei" by the squad; "Lord Seventh" from Ch 42 |
| Nature | **Fire** (a fire user who was burned on the Ash Road; they still teach fire) |
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
again; that the village they serve buried their teammate's death on purpose (it did, and their
name is on the report).

**Secrets.**
- They signed the Ash Road **field report**, which told the truth as they saw it: a trained cell,
  chakra paper, after `fallen_parent`. The elders rewrote it above their name as a bandit ambush and
  sealed it. Years later they saw the rewrite and said nothing, to keep their post. That silence is
  their guilt (Ch 37.0) and the Ch 42 council's objection.
- They know the watch-fire song from `fallen_parent`, who hummed it on missions (Ch 18).
- They saw a campfire lean toward their old team. They recognise your flame (Ch 14).
- They keep a box with `fallen_parent`'s forehead protector (every save). *Lineage B only:* it also
  holds half a watch-fire charm and an unsent letter; they do not know the child had the other half
  until Ch 48.
- `fallen_parent` had a young child, reported "lost" with the spouse after the ambush. The sensei
  never speaks of it before Ch 48 (in A the child truly died; in B it is you).
- They leave a persimmon at the memorial stone every year on the Ash Road anniversary.
- The Ash Road team was three: the sensei, `fallen_parent` and `sensei_3` (Classic: a Yuhi genjutsu
  user). `sensei_3` survived uninjured because the sensei ordered her back to signal for help; the
  two have never talked about that night (until Ch 37: "fourteen years"). Among the other senseis:
  `sensei_2` (Classic: Shiranui) has challenged the sensei to senbon footwork contests on guard
  rotations since the Academy (threading senbon through the lantern rings on the wall walk, the
  timed relay of the gate's bell). The tally is lopsided: at Ch 8 **sensei_2 trails 38 to 211** and
  keeps the notebook; by Ch 42 it is 51 to 289, and the new Seventh says "You win this one too" and
  loses on purpose (51 to 290). In Ch 51b sensei_2 dies holding the main gate, the player and the
  Seventh beside him; his last words are always "Did I win?" and the Seventh answers "You won." In
  Ch 54 his notebook's last line is read: "Held the gate longer than you would have. 52 to 290.
  Mine." `sensei_5` (Uzumaki) taught the sensei sealing once: old teacher,
  quiet student. `sensei_4` (Morino) is a colleague. Their own lines are in the ensemble's files.
- They never see the player's half charm before Ch 48: it stays sewn in the sleeve. From Ch 25 their
  thread carries a steady flicker (`hides:the_box`) from Ch 25 to Ch 48 in **both** lineages (they hide the box in
  both); only in lineage B is the reason explained, at Ch 48.

**What they know and when.**

| Knowledge | From |
|---|---|
| The player is a nursery child, "Nine" to the guards | Never told; they read only the raid's list of children (numbers were not on it). They never say "Nine" |
| The child points toward the lost girl (if `ans.sensei.ch0 = point`) | Ch 0: their first failure with you; they never stop looking for her |
| The cord flicker | Ch 8 (they see it at the cord test, say nothing) |
| Chakra paper chars near the player | Ch 11 (if shown) or Ch 14 |
| The persimmon tree (if `story.lineage.persimmon_told`) | Ch 14 |
| The watch-fire song in the player's mouth | Ch 16 (heard from the tower report) / Ch 18 (if sung) |
| The word "Kagari" was said to the player | Ch 19 (they were there with a kunai at her throat) |
| The flame is the same as `fallen_parent`'s | Ch 24 to 25 (certain: they see the ember-gold chakra and the mark on your palm) |
| You can see bonds (Thread Sight): the sensei shows as a thread to you, with a steady flicker while they hide something | Ch 25 (you tell them, or they guess). From then on, when you ask about what they hide, they say "I can't tell you yet" instead of deflecting: they know you can see that they are hiding |
| The Ash Road was Yūgure, and why | Ch 37.0 (the report opens Ch 37 on its own night) |
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
| 5 Ashes | Receives the Ash Road report from the Sixth at Ch 37.0 (both lineages); learns their own signature buried their teammate's truth; cries once (if you follow them, Ch 37.0); accepts the hat as the bridge the Sixth hands it to ("The one who opens the archive shouldn't be the one who builds on it") and says plainly they were always the bridge |
| 6 Night Watch | As Hokage (or under the Sixth), the authority you bring the Undercroft to; their choice follows yours |
| 7 Last Bonfire | Leads the war; argues against you climbing the Rock (Ch 49, 51b) and lets you choose; holds the gate, then the Rock's foot, in 51a/51b; tells the truth in lineage B; names you successor and stops trying to carry everything |

**Endings and variants.**

| Slot / choice | Effect on them |
|---|---|
| `twist.lineage = fallen` | The Ch 48 walk and box; their succession speech names `fallen_parent` as your parent |
| `twist.lineage = second` | Ch 48 is the second's scene; they learn after. Their guilt stays about the teammate and about not seeing the flame. Their speech names the second (alive or remembered) |
| `twist.fourth_fate` | Falls: at the Akimichi farewell feast (Ch 20) they sit by the empty place with his bowl and eat in silence. Crippled or taken: they consult him as Hokage |
| `twist.traitor = councillor` | The councillor co-signed the Ash Road rewrite; their Ch 39 scene adds one line of cold anger after his "I signed the Ash Road away too. A Jonin's death." |
| `ans.sensei.orders` | Their inaugural speech (Ch 42) and the order to fall back (Ch 24) |
| Sensei trust under 50 at Ch 25 | Training comes from the keeper or librarian; the sensei stays distant until Ch 37 and says "I should have been the one" |
| `ans.player.archive_follow = sensei` | The Rock scene: they cry, then ask you to call them by their given name when no one is listening |

## Dialogue brief

### Voice

Short sentences. Answers questions with questions or with silence. Never praises in public; praises
in private with one word ("Good."). Eats an apple when they want to look relaxed and are not.
Says your name rarely, so it lands. Calls the Hokage "the boss" only in private (never "the old man").
Never says "I'm sorry" until Ch 48; never explains the scar until Ch 37; never says "Kagari" before
you do.

Voice samples, not shipped lines:
- "One cord. Three tags. Sundown."
- "That's twice now the paper's done that near you. Where were you born, {given:player}?"
- "Keep your fire low until you need it."
- "...Good."
- (Ch 25) "I've seen that fire before. Once. I couldn't keep it lit."
- (Ch 48, lineage B only) "I carried you over a ravine and didn't know. Then I suspected, and the
  report said the persimmon house burned with everyone in it, and I was afraid to be wrong, so I
  never opened the box."
- (Ch 32.4) "Jonin, then. All of you. Four years."
- (training) "Don't push harder. Push *into* me. Let me do the rest."
- (as Hokage) "I'll still be around to complain. Go on."
- (Ch 1.2, to the Fourth, about the anonymous map that found the hideout) "The map was good. Unsigned."
- (Ch 42) "I was always the bridge. Somebody has to be. Then somebody walks over it."
- (Ch 49 and 51b, arguing against the player going up the Rock) "It'll pick you wherever you stand. I know. I still don't want you up there."

### Topics they care about

| Topic (level) | What they say |
|---|---|
| Small talk (0) | Weather and food in two words; deflects with a question about your training |
| Training (1) | Their real love: exact, practical, specific to your last fight |
| Their hobby (2) | Whittling (shavings in their pockets); later they whittle a small watch-fire basket |
| Their family (4) | "Had a team. That's family enough." (At level 6: "Three of us. One's on the stone. One won't look at me at festivals." That is `sensei_3`) |
| Your story (4) | They listen without interrupting and remember every detail |
| Their values (5) | "Come back with everyone. Then the mission." |
| Their advice (5) | Practical and blunt; for grief: "Eat something. Then cry. In that order." |
| Their dream (6) | Before Ch 37: "To be bored. Old and bored." After: "That nobody signs a lie for me again." |
| What worries them (7) | You. Said plainly once, then never again |

### Never reveal before

| Fact | Not before |
|---|---|
| Their teammate had "your fire" | Ch 25 (`story.kindling.awakened`) |
| That `sensei_3` was the third on the Ash Road team | Ch 25 (the fact); what happened between them, Ch 37 |
| The song is their teammate's song | Ch 25; before, they only react (turn away) |
| The Ash Road was Yūgure; they signed the sealed report | Ch 37 |
| The persimmon at the stone is for their teammate (they may leave it in view in Ch 21; the reason only at Ch 21.3 as "They loved these") | Ch 21 |
| The box (shown) | Ch 48 in both saves; the charm half and letter exist only in lineage B |
| That `fallen_parent` had a child | Ch 48, both saves |
| "Your parent" (either lineage) | Ch 48 |
| The second's name or identity | Ch 26 (her face) / Ch 48 to 49 |
| Anything about the Quiet Ending | Ch 36 |
| The player's half charm (they never see it) | Ch 48 |
| Their lineage-B heart line | Ch 48, lineage B only |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | Changes them |
|---|---|---|---|---|---|---|
| `ans.sensei.ch0` | Ch 0.4 (the raid) | (not a question: the look) | run / hide / point | — | Ch 24 ("You pointed, that night. I sent two people. I should have gone myself") if point; the lost child's return (N6 or Ch 47): if point, the sensei comes to see her and says "You pointed. I was too slow. You weren't." (unset/run/hide: "She's home. That's all that matters.") | Point: they carry the lost girl as their own failure and ask after her in Ch 44 |
| `ans.sensei.orders` | Ch 8.4 | "When I give an order you think is wrong, what will you do?" | obey / ask / right | Obey: their discipline; Ask: their honesty; Right: their freedom (and their fear) | Ch 24.3; Ch 42 inaugural speech | Shapes how the Seventh commands: obey → strict; ask → explains orders; right → "Do it right" |
| `ans.sensei.stone` | Ch 10.2 | (at the memorial stone) | gap / name / silence | Silence honours them (`stood_by_them`) | Ch 21.3, Ch 41 ("You stood there with me once") | Silence: they open up one beat earlier at Ch 25 |
| `ans.sensei.ash_road` | Ch 13.2 | (at the waystation) | ask / dont | Asking gently is fine; never prying here | Ch 37.0 | Asked: at Ch 37 they say "You asked me once. Here's the answer" |
| `ans.sensei.born` | Ch 14.4 | "Where were you born?" | truth (the tree, the camps) / dont_know / why | Honesty | Ch 21.3, Ch 48 | Truth: sets up the persimmon blow; why: they respect it and answer "Because I'm afraid for you" |
| `ans.sensei.song` | Ch 18.1 | (asks about the hummed song) | sing / dont_know / dream | — | Ch 25.4, Ch 48 | Sing: they know it is their teammate's; at the Ch 48 ruins (lineage B) or the Ch 41 stone (lineage A and B alike before Ch 48: they hum one line, nothing more) |
| `ans.sensei.kagari_word` | Ch 20.5 | "Don't say it to anyone. Not yet." | promise / ask / silent | Promise kept through Ch 22: `kept_promise` | Ch 22.2 | Promise kept: their trust passes 50 earlier (secret training) |
| `ans.sensei.know` | Ch 25.4 | "Do you want to know what you are? Even if it changes how you see yourself?" | everything / need / no | Everything: their honesty; No: their freedom ("Good answer too") | Ch 36 to 37 (how much they bring you) | Everything: they bring you to the archive in Ch 36 and to the report in Ch 37 |
| `ans.sensei.apple` | Level 4, a training hangout | "Why do you think I'm always eating something when I'm worried?" | to look calm / to have something to do with my hands / you're just hungry | — (filler with a function: shows they know you see them) | Ch 49 war council: they hold an apple and don't eat it | — |
| `ans.sensei.hat` | Ch 42, before the succession (level 6) | "Should someone who kept quiet about a rewritten report be Hokage?" | yes, because you know the cost / no, but you're the best we have / only if you say it out loud | Honesty | Ch 42 speech: they confess the signature in public if "say it out loud" | Changes the Seventh's first act: a public confession, or a quiet one to the council |
| `ans.sensei.successor` | Ch 54.4 | "Do you want it? Honestly." | yes / not yet / only if you stay near | — | Ch 55.2 | "Only if you stay near": they become your advisor in the post-game |
| `ans.sensei.burned` | Ch 18.1, level 4 (fire training) | "I'm a fire user who got burned by fire. Should I still be teaching you to make it?" | yes, you know what it costs / no, teach something safer / only if you show me the scar | Honesty, their fear | Ch 24.5 (if they fall, the sensei's fire becomes a wall of flame and they say "You said I should still teach it") and Ch 37 (the scar's story) | "Show me the scar": they explain it one arc early at level 7 (the fact of the burn, not the Ash Road truth) |
| `ans.sensei.fear_squad` | Ch 16 tower or Ch 18 training, level 4 | "Which of you three do I worry about most?" | me / teammate_a / teammate_b / all of us the same | Honesty (they answer truthfully whatever you say) | Ch 24.4 (the one they named is the one they look for first when the fire leans) | Changes the order they check on you all in Ch 19 and Ch 51 |
| `ans.sensei.revenge` | Ch 37.0 (if you follow them to the Rock), else Ch 38 | "Should I find the ones who did the Ash Road, before anything else?" | yes, they owe it / no, the living first / only if they're still killing | Loyalty to the dead against duty | Ch 49 war council and Ch 51a (whether the Seventh personally hunts hearths before the assault) | "The living first": the Seventh's war plan protects the Academy before striking cells |
| `ans.sensei.sensei_3` | Ch 25 to 31, level 6, a training hangout | "There was a third of us that night. I sent them back. Should I have?" | yes, one of you lived / no, you needed them / ask them, not me | Honesty | Ch 41 (the memorial: they stand next to `sensei_3`, or apart) | "Ask them": they finally talk to `sensei_3` (ensemble scene) |

**Ch 53: the sensei's flame line (the only table for it; ARCS cites it).** The sensei is always the
second speaker, after the cord; their flame overrides a falling-out (a falling-out with the sensei
is mended by story at Ch 25.4). If the sensei is the one who fell in Ch 24, slot 4 is skipped.

| Condition | Line |
|---|---|
| Base (`ans.sensei.orders` unset) | "Hold on. We're nearly out." |
| `ans.sensei.orders = obey` | "Hold on. That's an order. We're nearly out." |
| `ans.sensei.orders = ask` | "Hold on. You want to know why? Because we're nearly out." |
| `ans.sensei.orders = right` | "Hold on. Do it right. We're nearly out." |
| `story.finale.reached` (any of the above) | The cord's flame arrives grey-edged first; the sensei's line gains a first sentence: "I saw you reach. You let go. That's the whole job." |

**Unset answers.** Every main-path read of an `ans.sensei.*` flag has an `unset` branch with a
neutral line (for example Ch 42 with `orders` unset: "My students taught me to explain my orders.
I'll try"; Ch 22 with `kagari_word` unset: the sensei simply stands behind you).

### What their lines are for

- **Plot:** the rescue, the cord test, the suspicion, the recommendation, the warning, the secret
  training, the archive, the war council, the succession.
- **Clue (lineage):** the song reaction, the persimmon, the stone. Must read identically in both
  lineages until Ch 48.
- **Bond:** their trust meter gates training (Ch 25); their sparse praise is the reward.
- **Teach:** squad commands (Ch 8), tree walking (Ch 10), water walking (Ch 12), the exam technique
  (Ch 18), the gift (Ch 25 onward): Thread Sight first, then Kindle (they let you push your chakra
  into their own technique, so it goes past its limits; the sensei's trademark technique, kindled,
  is the Ch 25 training's first success), then Ember Link drills with the squad. Their way of putting
  it: "You don't take anything. You make the other person more."
- **Life:** apples, sensei_2's contests (always lost, always gracious about it), paying at the barbecue house under protest.
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
- `ans.sensei.burned` (yes_cost, safer, show_scar)
- `ans.sensei.fear_squad` (player, teammate_a, teammate_b, all)
- `ans.sensei.revenge` (owed, living_first, still_killing)
- `ans.sensei.sensei_3` (yes, no, ask_them)
