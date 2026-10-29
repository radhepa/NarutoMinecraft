# Arc 3: Dusk over the Stadium (Chunin Exams, Ch 15 to 20, Beta 3)

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

**~3 h** (2.5 h authored, 0.5 h systemic in the training break). Child stage. Levels 15 to 18.
The beta ends with promotion, not a time skip.

**What the arc is for.** A tournament that becomes an invasion. The player should feel strong (the
squad works, the jutsu land), then small (the attack is bigger than them), then named (a stranger
knows what they are). The end of the beta leaves three hooks: a name (Kagari), a cost (the
Fourth), and a new Hokage who does not trust them.

**The foreign team is real and innocent**: three Genin of a small village with two adult escorts.
The escorts are `yugure_second` and `yugure_blade`, openly adults, travelling under false papers.
`foreign_genin` is one of the real Genin; their escorts vanish before the finals and leave the
three of them stranded. No one is disguised as a Genin.

---

## Ch 15: Ink (20 min)

*Teaches: stealth objectives, choice.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 15.1 | The hall | proctors, all candidates (your class's squads, the senior squad, the foreign team; their two escorts at the back wall) | An **observation test**. The proctors stage small events in the hall while everyone writes: a dropped scroll, a fake scuffle in the third row, a stranger at the window, a proctor who leaves with the wrong coat. The paper asks one question: "What did you notice?" Watching without being caught watching is the skill | teach | How you watch: openly / under Transformation as a proctor's runner / with a clone in the rafters / through a teammate's signal (teammate_a's small genjutsu points your eyes) (judged later; each has a judging tag) |
| 15.2 | What you noticed | the proctor | The answers are judged on what was really there. One thing nobody staged: the foreign team's tall escort at the back wall has hands burned like a smith's (ember chakra scars) | seed, clue | What you wrote about the foreign team: the escort's burned hands / the other escort writes left-handed and never sets down his sword case / their Genin keep looking back at the escorts, uneasy / nothing (`ans.player.foreign_team`). Any true answer earns the proctor's nod; the sensei remembers it |
| 15.3 | Lost Genin | `foreign_genin` (side `side.b3.lost_genin`) | The night before, a foreign Genin was lost in the village; if you helped them, they whisper in the hall: "Our escorts aren't from our village. They just had the papers" | clue (optional) | — |

---

## Ch 16: The Forest (60 min)

*Teaches: survival, bedroll camping, On Duty, tree-hopping fights.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 16.1 | The gate | squad | One scroll of a pair; five in-game days to reach the tower with both. Escorts and senseis wait outside the fence (the two foreign escorts are seen leaving the fence line early, "to fetch supplies") | teach, clue | — |
| 16.2 | Stalked | another team | Day two: a rival village's team shadows you; their traps are good | plot | — |
| 16.2b | The truce | `squad3_a`, `squad3_b`, `squad3_c` | Day two, night: the trio's camp and yours meet at the river. `squad3_a` has a plan for both squads against the traps; it works until it doesn't, and you improvise the rest together | plot, bond (`mission_together` with the trio) | She asks: "Do we split up or stay together? You decide, I'll plan either." Split / together / your call, it's your plan (`ans.squad3_a.forest`) |
| 16.3 | Spared | `yugure_second` | Day three: the other team's trap drops you into a ravine; you are about to be finished when a burning kunai pins your attacker's sleeve. The tall escort from the hall stands on a branch inside the fence, where no escort should be ("looking for my team"), looks at you a moment too long, and leaves. Ember chakra glows on her hands | plot, seed (`story.seed.second_spared`) | — |
| 16.4 | The lost Genin | `foreign_genin` | Day three, evening: you find `foreign_genin` alone and lost, looking for escorts who left the forest early. Their teammates are somewhere ahead | clue, bond | Take them to their team (an hour lost; a `helped_resident` deed) / point the way and go on |
| 16.6 | The night watch | `teammate_a`, `teammate_b` | Each night one teammate shares your watch. Their fears (bond quests `bond.b3.teammate_a`, `.b` at level 5). On the last night you hum the song from your dream without meaning to, and the campfire **leans toward your squad** (only if `squad_cohesion 50`) | bond (`shared_moment bond.night_watch`), seed (`story.seed.campfire_leans`) | — |
| 16.7 | The listener | `yugure_second` (offscreen) | Beyond the firelight, the song stops someone in the trees. (The camera shows a branch sway; nothing more) | seed | — |
| 16.8 | The voice on the bridge | `teammate_b` | If `teammate_approached` is kept or followed: teammate_b says the tall escort's voice is the stranger's from the bridge | clue | Tell the sensei at the tower / keep it between you (`ans.teammate_b.forest_voice`) |
| 16.9 | The tower | squad | Reach the tower with both scrolls | plot | — |

**Bond quests `bond.b3.teammate_a` and `bond.b3.teammate_b` (night watch, level 5):**

| Who | Their fear | Their question |
|---|---|---|
| teammate_a | That one day they will freeze when it matters and someone will be hurt because of it | "If I froze, and you got hurt, would you forgive me?" (`ans.teammate_a.freeze`: always, there's nothing to forgive, I'd be angry but yes). Ch 24: if they are the one who falls, they did not freeze, and they say so |
| teammate_b | That they are their parent: someone who leaves | "Promise me something. If I ever start walking away, drag me back." (`ans.teammate_b.drag_back`: promise, no—you won't leave, I'll walk with you instead). The Chunin arc's return scene quotes it |

---

## Ch 17: The Tower (20 min)

*Teaches: duels, judged performance.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 17.1 | Preliminaries | proctors, all | One-on-one bouts. Yours is against `classmate_d` (careful, protective, a kenjutsu prodigy). The rival wins theirs in seconds and looks to see if you watched. `squad5_c` wins his faster and does not look at anyone. `squad4_a` beats `squad4_b`, who demands a rematch at volume | teach, bond (`spar_won`/`spar_lost` with classmate_d) | Fight; a yield is allowed |
| 17.2 | The bracket | proctors, the foreign team | The finals bracket goes up: your last bout of the day is against the `rival`, scheduled to close the finals. The foreign Genin win through, and their escorts are not in the gallery to see it | plot, clue | — |

---

## Ch 18: Six Days (30 min)

*Teaches: training, crafting, side quests; the exam reward technique.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 18.1 | The reward | `sensei` | Six days compressed. The sensei teaches one C-rank technique fitted to your nature. On the last day they ask about the song you hummed in the forest | bond, teach | Sing it / say you don't know it / say it's from a dream (`ans.sensei.song`). Singing it: the sensei turns away for a moment. They know it (they heard it from `fallen_parent` on missions) |
| 18.2 | Festival | the village, `sensei_2` | Exam-week stalls; the betting booth, where `sensei_2` is seen placing a bet on the finals against his own squad ("I'm hedging. It's called strategy"), and your sensei writes it down for him; a rival's younger sibling training in secret (side quests) | life | — |
| 18.3 | The Fourth's visit | `hokage_4` | The Fourth stops by Training Ground 3 with a bag of buns: "Don't win for me. Win for you." | bond | — |

---

## Ch 19: Dusk over the Stadium (35 min)

*Teaches: defence, protect objectives, the cinematic camera.* No blood in the child stage.

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 19.1 | The lanterns | the village, the Fourth at the Hokage's seat | The whole village in the stands at dusk for the finals' opening: the Fourth lights the first lantern and the lights run around the stadium's rim. Your bout with the rival is the last on the card | plot, life | — |
| 19.2 | Dusk | Yūgure hearths | As the last lantern catches, smoke bombs in the stands, fire, and hearths of Yūgure fighters among the spectators, ash-violet scarves pulled up over their faces; the guard rotation had a gap exactly where they came in (the voice's work). No bout is ever fought; the rival, beside you at the fighters' gate, says "This doesn't count" | plot | — |
| 19.3 | Hold the stair | squad, `sensei`, `sensei_5`, `squad5_c`, `yugure_blade` | Protect the east stair while the Academy children are evacuated. The sensei fights the blade on the arena floor (ink-dark cuts in the air), and `squad5_c` jumps down to fight beside them and takes a cut (a scar later). `sensei_5` seals the stadium's gates behind the children | teach, plot | — |
| 19.4 | Covered | the higher-level teammate (or the rival) | A tier of the stands gives way under you; a friend drags you out before it falls (`saved_by_them` with the teammate at the higher level; with both under 4, the rival) | bond | — |
| 19.5 | "Kagari" | `yugure_second` | Her order was to find the strongest flame in the stadium and tell the leader how it burns (a test of her: he already knows; nobody is ordered to take the player). She steps out of the smoke in front of you, scarf down, ember chakra lighting her face, a hand raised toward you as if to feel the heat, and stops. A held beat: the noise of the stadium drops away, and she says one word aloud, quietly, as if it hurt: **"Kagari."** Then the sensei's kunai is at her throat and the blade pulls her away | plot, seed (`story.ch19.named`) | — |
| 19.6 | The east stair | `hokage_4`, `squad3_b`, `sensei_2`, `yugure_leader` (unseen) | The Fourth has left the Hokage's seat to carry two Academy children down the east stair himself, past your squad; his grandson `squad3_b` is on that stair. There he is hit, in every fate (`twist.fourth_fate`, [ROTATIONS.md](../ROTATIONS.md) §3): *falls*: he dies there, shown through the cinematic cutaway; *crippled*: the dark mirror tears half his chakra; *taken*: the leader's hearth carries him off from the stair over the wall. `sensei_2` gets the children out | plot (`world.hokage = 4 → 5`) | — |

---

## Ch 20: Embers (15 min)

*Teaches: promotion.*

| # | Scene | Who | What happens | For | Choices |
|---|---|---|---|---|---|
| 20.1 | After | the village, `squad3_b`, the Fourth's daughter | By `twist.fourth_fate`: *falls*: the **Akimichi farewell feast**: the whole village eats his favourite dish in the street, his bowl set at an empty place; `squad3_b` (or his mother) says what the Fourth told them about you, quoting `ans.hokage_4.want` (unset: "He said you came here hungry. Eat."). *Crippled*: the hospital, where he abdicates from his bed. *Taken*: the empty Hokage's seat, and `squad3_b` refusing to leave the east stair | plot, bond | Sit at the feast beside `squad3_b` / carry the bowl to the empty place (*falls* only; `ans.player.feast`: sat, carried; the bowl comes back to you in Ch 21.2a) |
| 20.2 | The Fifth | `hokage_5`, the council | The Fifth Hokage, a severe Hyuga woman, is named. Her first order: curfews and a sensor watch. Her eyes find you in the crowd and stay | plot, seed (`story.seed.fifth_hard_line`) | — |
| 20.3 | Results | proctors, `sensei` | Promotion results, judged on what you noticed, how you fought in the forest and the tower, and how you protected the stair. On Story difficulty the player is promoted if they held the stair; the judging changes the speech and the rank-up's standing; the proctor's note reads your Ch 15 answer (`ans.player.foreign_team`: "You saw her hands," "You saw the sword case," "You saw their Genin were afraid," or, unset or nothing, "Next time, look harder"). Promoted with you: the `rival`, `squad5_c`, `squad4_a`, and one of your teammates (the stronger, by the roster); the rest of the class makes Chunin next season ([ENSEMBLE.md](../ENSEMBLE.md)) | plot (`promote chunin`) | — |
| 20.4 | Ichiraku | squad, `rival` (if they come) | The squad's evening at Ichiraku. Nobody talks about it, then everybody does. Your order is set down without asking. If the rival comes: "You still owe me a match" | bond | Whoever covered you: thank them now / later (thanking now: a `kept_promise`-sized warmth and a line they remember) |
| 20.5 | The warning | `sensei` | Walking you home: "That word she said. Don't say it to anyone. Not yet. They'll come again." | seed | Promise / ask what it means / say nothing (`ans.sensei.kagari_word`). Promising sets `kept_promise` when you keep it through Ch 22 (the Fifth's interrogation) |

**End of the beta.** The time skip opens the Chunin arc later.
