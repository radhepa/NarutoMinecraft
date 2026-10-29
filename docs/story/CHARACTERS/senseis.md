# The other senseis: `role:sensei_2`, `role:sensei_3`, `role:sensei_4`, `role:sensei_5`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Ensemble plan:
> [ENSEMBLE.md](../ENSEMBLE.md). The player's own sensei: [sensei.md](sensei.md).

Four Jonin who teach the rest of the class and the senior squad. Each has a history with the
player's sensei, a squad of their own, and at least one beat that moves the main plot. All four
have **rolled looks in Varied** (so *they* here and pronoun tokens in dialogue); the Classic
curation gives each a fixed look and gender, stated below.

**Unset answers.** Every main-path read of an `ans.*` flag in this file has an `unset` branch: the
unset line given in its row, or else the character's line for that beat without the callback
("You said ___" is dropped, nothing else changes).

**How the five relate** (the "staff room"):

| | sensei | sensei_2 | sensei_3 | sensei_4 | sensei_5 |
|---|---|---|---|---|---|
| **sensei** | — | Contest-rival since the Academy; the tally | The Ash Road team; unspoken since | Colleagues; respect, no warmth | Their old sealing teacher |
| **sensei_2** | "Best of three. Again." | — | Teases her gently; the only one who makes her laugh | Calls him "the Baker" to his face | Their teacher; still afraid of him |
| **sensei_3** | Won't look at them at festivals | Lets him tease her | — | Shares a bench at the hospital some nights | Their teacher; visits him on his birthday |
| **sensei_4** | Thinks they keep too many secrets | Thinks he isn't serious; is wrong | Brings her bread | — | Their teacher in binding seals |
| **sensei_5** | "My quiet one." | "My loud one, who pretends to be quiet." | "My sad one." | "My baker." | — |

---

## `role:sensei_2`

### At a glance

| | |
|---|---|
| Role | Squad 2's Jonin (the `rival`, `classmate_c`, `classmate_d`); the Fifth's **Jonin Commander** (Ch 22 to 31) |
| Name | Given Family, rolled. Classic: a **Shiranui** (the clan's name as family name) |
| Look | Classic: curated: a lean man in a guard's flak vest, hair tied back, a senbon always turning between two fingers, a small battered notebook in the vest pocket. Varied: rolled |
| Pronouns | Classic: he. Varied: rolled; dialogue uses `{they:sensei_2}` |
| Specialty and style | Senbon at speed: needle volleys that pin sleeves and shadows; a guard's footwork; never wastes a step |
| Rank | Jonin; Jonin Commander from Ch 22; a Jonin of the Seventh's guard from Ch 42 |
| Archetype | Classic: **playful** with a guard's discipline (warmth .5, boldness .3, discipline -.2 in manner, .5 on duty) |
| Values | Freedom, loyalty |
| Peeves | Laziness, recklessness (other people's) |
| Dream | To win one contest that matters |
| Tier | Story-driving |
| First / last | Ch 8 (assignment) / Ch 51b (the main gate); his notebook in Ch 54 |

### Arc

**Wants.** To beat the player's sensei at something that counts. The real want under it: to have
been on the Ash Road with them.

**Fears.** That if anything is taken seriously it can hurt him. That he was spared the Ash Road by
luck and has never earned it.

**Secrets.** He asked to go on the Ash Road mission and was turned down (the roster was full). He
has blamed himself, a little, ever since. He keeps the contest tally in a notebook because
it is the only way he knows to say that the sensei still matters to him.

**What he knows and when.**

| Knowledge | From |
|---|---|
| The Ash Road was a disaster his rival survived | Before Y0 |
| The player is "the kid they carried out" | Ch 8 |
| "Kagari" was said at the stadium | Ch 20 (as a senior Jonin) |
| The player's chakra is "anomalous" (the corps' report) | Ch 22, as Commander |
| The Tobari are innocent | Ch 31, with everyone |
| The Quiet Ending | Ch 40 (public) |
| The Hollow Crown | Ch 49 (the war council) |

**How he changes.**

| Arc | Change |
|---|---|
| 2 Paper Trail | The comic rival: in the Academy hall right after assignment (Ch 8.1) he challenges the player's sensei, in front of both squads, to that week's contest (threading senbon through the lantern rings on the wall walk, one run each, at dusk). He loses, writes it down, and shows the squads the page: **38 to 211**. "I'm catching up." |
| 3 Dusk | Ch 18.2: in the training break he is caught betting on the finals against his own squad ("It's called hedging. Sunshine, don't look at me like that."). Ch 19: on duty at the Hokage's seat when the attack begins at the opening lantern-lighting; he fights his way toward the east stair as the Fourth's fate plays out there, too late. Afterwards he stops joking for a week |
| 4 Embers | Leads the Empty Seat rescue (Ch 21c). The Fifth makes him Jonin Commander: he enforces a curfew he hates, strictly and fairly, teasing the player while writing their name in the night log. At the Tobari council (Ch 31.3) he puts down the Commander's armband in front of his own Hokage: "I'm with the kid." The first serious thing he has ever said in public |
| 5 Ashes | One of the two examiners in the player's Jonin trial (Ch 33.2). Kneels first to the Seventh (Ch 42), the tally now 51 to 289: "You win this one too. Don't get used to it." He writes 51 to 290 |
| 7 Last Bonfire | Holds the main gate in the war (Ch 51a) until the evacuation is through, and dies there as the Seventh and the player reach him (Ch 51b, the first stop on the player's route); "You won" |

**His ending (every save, main path).** In Ch 51a he holds the main gate with a handful of Chunin
against the leader's strongest hearths until the evacuation is through (he has already sent his own
squad away: the rival to the Rock's stair, c and d to the Residence steps). squad5_b and the
Tobari smother the lanes beside the gate; squad3_a builds the second line behind it when it breaks. In Ch 51b the player's route to the Rock passes
the gate: the player is with the Seventh when they reach him. He is dying, and he always asks:
**"Did I win?"** "You won," the Seventh says: the only contest they ever conceded. In Ch 54 the
Seventh finds the notebook; the last line, written at the gate in a lull, is: *"Held the gate
longer than you would have. 52 to 290. Mine."* If `ans.sensei_2.on_purpose` is `counts`, the
Seventh reads it aloud and laughs, the first time anyone has heard them laugh; if `doesnt`, they
write "Counts." under it; `secret` or unset, they close the notebook and keep it.

### Relationships

- **The player's sensei:** the tally (a running joke through every arc; numbers in his greetings).
- **His squad:** he calls the rival "Sunshine" because they never smile; c "the Architect"; d
  "the Wall". He is a better teacher than he lets anyone see: the rival's growth into an ally is
  half his work (he makes the rival fight beside people).
- **The Fifth:** loyal, then honest; she respects him more for Ch 31.

### Dialogue brief

**Voice.** Dry, quick, teasing; never raises his voice; turns everything into a bet; calls people
by nicknames; switches to plain, short sentences when it is serious, and that switch is the tell.
Never says "I'm proud of you"; says "Not bad" and writes it in the notebook. Never jokes about the
Ash Road.

Voice samples, not shipped lines:
- "Best of three. Again. Loser buys."
- "Curfew's ten. It's ten-oh-two. I'm writing 'ten-oh-one'. You owe me."
- "You want to know a secret? They're terrible at losing. Have been since we were eight."
- (Ch 31, plain) "No. Not like this. I'll say it to her face."
- (Ch 51a, to his squad) "Stair. Residence. Go. That's an order. I'm winning this one."
- (Ch 51b, dying) "Did I win?"

**Topics.**

| Topic (level) | What he says |
|---|---|
| Small talk (0) | A bet about the weather |
| Training (1) | Speed and footwork; challenges you to a race |
| Hobby (2) | The tally (lopsided, proudly: a few dozen wins in twenty years, and climbing), and the contests he invents on guard rotations: lantern rings, the gate-bell relay, the wall walk in the rain |
| Family (4) | A big Shiranui family of guards; "I'm the one who doesn't stand still" |
| Values (5) | "Be fun to lose to. Be impossible to beat when it matters." |
| Advice (5) | "If it can hurt you, laugh at it first. Then deal with it." (After Ch 31: "Or don't laugh. Sometimes don't.") |
| Dream (6) | "One win that counts." |
| Worries (7) | "That I'll be the one who wasn't there. Again." |

**Never reveal before.**

| Fact | Not before |
|---|---|
| He asked to be on the Ash Road mission | Level 7 and Ch 37.0 (when the report is opened) |
| Anything about the player's chakra beyond "anomalous" | Ch 31 |
| The war plan, the anchors | Ch 49 |

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | Changes him |
|---|---|---|---|---|---|---|
| `ans.sensei_2.laugh` | Ch 8 or a hangout at level 2 | "Your sensei. Do they ever laugh? Be honest." | Never / Only when they think no one's looking / You'd have to make them | Freedom (playful truth) | Ch 54: the notebook scene | "Make them": he keeps trying, and the tally gains a column called "Made them laugh: 0" |
| `ans.sensei_2.liked_right` | Ch 22 to 30, during a curfew check | "Is it better to be liked or to be right?" | Liked / Right / Both, if you work at it | Loyalty vs honesty | Ch 31: he quotes you before he speaks against the lockdown | "Right": he speaks first and alone. "Liked": he waits until you testify, then stands with you. "Both": he brings the Hagane and Tobari together before speaking |
| `ans.sensei_2.curfew_friend` | Ch 28 (the stake-out night pass) | "Would you break curfew for a friend?" | Yes / I'd ask for a pass first / Depends on the friend | Rules vs loyalty | Ch 28: he signs the pass, or catches you and lets you go | Shapes his night log: "yes" earns a wink and a forged time |
| `ans.sensei_2.on_purpose` | Ch 42 (after he kneels) | "If I lost a contest on purpose, would it still count?" | It counts / It doesn't / Only if they never find out | Freedom, loyalty | Ch 51b and Ch 54 (the last line of the tally) | "Counts": the Seventh laughs reading it. "Doesn't": the Seventh says "It counts" anyway |
| `ans.sensei_2.wasnt_there` | Level 7 hangout, Jonin arc | "Ever been somewhere you weren't, in your head? Some night you should've been at?" | Yes, the night they took the girl / No / Every day | Honesty | Ch 51a: his last order to his squad quotes it ("Not this time") | Opens his Ash Road confession |
| `ans.sensei_2.nickname` | Any hangout, level 3 | "Everybody gets a nickname. What's yours going to be?" | Pick from three he offers ("Matchstick", "Stray", "Trouble") / refuse | Playfulness | He uses it forever; it is the last word in the notebook's margin | — |
| `ans.sensei_2.contest` | Level 2, on his guard rotation | "Name a contest. Anything on this wall. I'll beat you at it." | Senbon through the lantern rings / The gate-bell relay / Who can make my sensei talk first | Freedom | His greetings keep your running score (he loses to you too, cheerfully); the third becomes a joint campaign (he and you vs the sensei) | Opens a ritual on his rotation |
| `ans.sensei_2.armband` | Ch 31 (after the council) | "I just put down the best job I ever hated. Was that stupid?" | No, it was right / A little, and right / You'll get it back | Loyalty vs duty | Ch 42: when the Seventh offers him the armband back, he takes it if you said "get it back", else he asks to stay at the gate | Where he serves in the war (Ch 51: the gate either way) |
| `ans.sensei_2.squad` | Level 5, Chunin arc | "My Sunshine still doesn't smile. Should I make them, or leave them be?" | Make them / Leave them be / Make them fight beside someone | His teaching | The rival's Ch 43 ceremony: he is there (make them), absent with a note (leave), or brings the whole squad (fight beside); unset: he is there, at the back, saying nothing | The rival's ally arc moves a little faster with "fight beside" |
| `ans.sensei_2.tally_end` | Level 6 | "What happens to the tally when one of us is gone?" | It stops / The other one keeps it / Someone new picks it up | Loyalty | Ch 54: the Seventh keeps the notebook (other one), closes it (stops), or gives it to you (someone new; you inherit a contest line in the epilogue) | — |
| `ans.sensei_2.serious` | Level 7, Jonin arc | "Ever wish I'd be serious? Honest." | No, you're right as you are / Sometimes / You are serious, you just hide it | Honesty | Ch 51b: a second line after "Did I win?" and "You won" (never instead of them) | As you are: a last joke ("Write it down"); sometimes: nothing more; hide it: a plain line ("Tell them I was there"); unset: nothing more |
| `ans.sensei_2.gate` | Ch 49 (the war council) | "Someone has to hold the main gate. Who'd you pick?" | You / My sensei / Whoever volunteers / Nobody alone | Duty | Ch 51b (at the gate): "You said me. Good pick." / "Nobody alone. So I brought a handful."; other answers and unset: no extra line | — |

**What his lines are for.** Comedy that carries feeling (life, bond); the curfew system's teacher
(teach, Ch 22 to 31: passes, night logs); the Ch 31 turn (plot); the war's first sacrifice
(plot, bond). Pools: greetings with a tally number (per arc), curfew lines (on duty), a quiet
pool after Ch 19 and after Ch 31, the Ch 18.2 betting lines, war lines.

**Unison technique (Blaze, with the player).** *Needle Rain of Embers*: his senbon volley, kindled,
becomes a rain of ember-gold needles that pin a whole cell's shadows at once.

**Variants.** Varied: any archetype; keep the tally and the switch to plain speech when serious.
`twist.fourth_fate = taken`: he leads the Empty Seat (Ch 21c) and carries the Fourth out himself.

**New flags.** `ans.sensei_2.laugh` (never, unseen, make_them), `ans.sensei_2.liked_right`
(liked, right, both), `ans.sensei_2.curfew_friend` (yes, pass, depends),
`ans.sensei_2.on_purpose` (counts, doesnt, secret), `ans.sensei_2.wasnt_there` (girl_night, no,
every_day), `ans.sensei_2.nickname` (matchstick, stray, trouble, none), `ans.sensei_2.contest`
(rings, bell, make_talk), `ans.sensei_2.armband` (right, little, get_back), `ans.sensei_2.squad`
(make, leave, fight_beside), `ans.sensei_2.tally_end` (stops, keeps, someone_new),
`ans.sensei_2.serious` (as_you_are, sometimes, hide_it), `ans.sensei_2.gate` (you, sensei,
volunteers, nobody_alone).

---

## `role:sensei_3`

### At a glance

| | |
|---|---|
| Role | Squad 3's Jonin (`squad3_a`, `squad3_b`, `squad3_c`); the Ash Road team's survivor |
| Name | Given Family, rolled. Classic: a **Yuhi** |
| Look | Classic: curated: a tall woman with grey eyes and short-cropped dark hair, a leaf-pattern scarf, always a little apart. Varied: rolled |
| Pronouns | Classic: she. Varied: rolled; dialogue uses `{they:sensei_3}` |
| Specialty and style | The Yuhi grove genjutsu: a fall of leaves that hides, misdirects and quiets everyone inside it; a short blade for close work |
| Rank | Jonin throughout |
| Archetype | Classic: **gentle**, with grief (warmth .7, boldness -.4, pride -.5) |
| Values | Kindness, family (her squad as family) |
| Peeves | Cruelty, rudeness |
| Dream | To be forgiven by the one person who never blamed her |
| Tier | Story-driving |
| First / last | Ch 8 / epilogue |

### Arc

**Wants.** Forgiveness, from the player's sensei, for leaving the Ash Road alive. They never
blamed her; that is the problem: there is nothing to forgive, so she cannot be forgiven.

**Fears.** Being spared again while someone else stays.

**Secrets.** On the Ash Road the sensei ordered her back to signal for help. She went. She has
replayed the choice to disobey every night since. She remembers `fallen_parent`'s laugh
and the watch-fire song. She does not know the ambush was Yūgure until Ch 37.0.

**What she knows and when.**

| Knowledge | From |
|---|---|
| The Ash Road ambush, as "bandits" | Before Y0 |
| The song (from `fallen_parent`) | Before Y0; she hears the player hum it in the forest report (Ch 16) and says nothing |
| The player has `fallen_parent`'s fire | Ch 25 (the sensei tells her, the first words between them in years) |
| The Ash Road was Yūgure | Ch 37.0 |
| The Hollow Crown | Ch 49 |

She never speaks of `fallen_parent`'s home life or family before Ch 48.

**How she changes.**

| Arc | Change |
|---|---|
| 2 Paper Trail | Ch 10: at the memorial stone at dusk with the player's sensei; they stand two metres apart and do not speak. The player sees it |
| 3 Dusk | In the forest, she is a proctor at a tower gate; she lets the player's squad rest an hour longer than the rules allow (a kindness the player can notice) |
| 4 Embers | Ch 25.3b: she seeks out the player once: "If you're what I think, {they:sensei} will tell you about a road someday. When that day comes, remember I was sent away. I didn't run." |
| 5 Ashes | Ch 37.0 (the Ash Road report's own night): stays when the sensei walks out, reads the report twice, and says the thing she has never said: "They sent me back so I'd live. I've been angry at them for fourteen years for it." Later, on the Rock, the two finally talk (onscreen if the player followed the sensei, told by her afterwards if the player stayed). She asks the sensei to blame her; they refuse, then say "I was angry you went. I was glad you lived." It is enough |
| 7 Last Bonfire | Ch 51a, at the Academy with the instructor and squad3_b: her falling-leaf genjutsu hides the Academy's evacuation, a whole grove over the streets; she stays behind in the illusion until the last child is out. She is spared again, and this time she lets herself be |

**Endings.** She lives. Epilogue: she and the sensei leave persimmons at the stone together.

### Relationships

- **The player's sensei:** fourteen years of silence, ended in Ch 37.
- **sensei_2:** the only person who makes her laugh; she knows why he keeps the tally.
- **Her squad:** she teaches the trio as a family, not a formation; squad3_a's freeze is a mirror of
  her own Ash Road moment, and she says so after the war (Ch 54).

### Dialogue brief

**Voice.** Soft, careful, complete sentences; she asks about the other person before answering
about herself; images from gardens and trees. When hurt, she becomes very polite. Never says
"bandits" after Ch 37.0; never says "I'm fine" and means it.

Voice samples, not shipped lines:
- "Sit. You can stand later; everyone stands later."
- "Illusions don't lie. They show you what you were already afraid of."
- (Ch 25.3b) "If you're what I think, {they:sensei} will tell you about a road someday. When that day comes, remember I was sent away. I didn't run."
- (Ch 51a, at the Academy) "Go on. I'll keep the leaves falling. I'm good at staying, it turns out."
- (to her squad) "A plan is a garden. Some of it dies. You plant again."

**Topics.**

| Topic (level) | What she says |
|---|---|
| Small talk (0) | Flowers in season; asks how you slept |
| Training (1) | Genjutsu release, gently; "the trick is to notice" |
| Hobby (2) | Pressing flowers; she gives one to anyone at level 3 |
| Family (4) | Her squad first; the Yuhi grove second |
| Values (5) | "Kindness costs. Pay it anyway." |
| Advice (5) | On regret: "Say it to the person. Even if they're on the stone." |
| Dream (6) | Before Ch 37.0: "To stop dreaming the same road." After: "To be bored with him, at festivals." |
| Worries (7) | Her squad; squad3_a most |

**Never reveal before.**

| Fact | Not before |
|---|---|
| She was the third on the Ash Road | Ch 25 (by the sensei) |
| She left on the sensei's order | Ch 25 (her own line) |
| The ambush was Yūgure | Ch 37.0 |
| Anything about `fallen_parent`'s spouse, child or home | Ch 48 |

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | Changes her |
|---|---|---|---|---|---|---|
| `ans.sensei_3.spared` | Ch 25.3b (her visit, after her line about the road) | (The player's reply to "I was sent away. I didn't run.") | I know you didn't / Ask what road / Say nothing | Her guilt | Ch 37.0: "You said you knew I didn't. You were right." / "You asked what road. This one." / she hands you the report without a word; unset: as "say nothing" | The arc's definition (Ch 25.3b) |
| `ans.sensei_3.saved_choice` | Level 5 hangout (Chunin) | "Would you rather be the one who's saved, or the one who stays?" | Saved, so I can come back / The one who stays / Neither: we all leave together | Her guilt | Ch 51a: "You said ___. I'm choosing the other one, this once" or "You said together. Then go, I'll be right behind"; unset: "Go on. I'm good at staying" | Decides how she frames her stay in Ch 51a |
| `ans.sensei_3.coward` | Level 5 hangout (Chunin) | "Is it cowardice to obey an order to run?" | No, it's trust / Sometimes / Yes, but forgivable | Kindness to herself | Ch 37.0: she quotes you to the sensei | "No": she can ask for forgiveness at last. "Yes, but": she asks to be blamed first |
| `ans.sensei_3.illusion` | Level 3 hangout (flower pressing) | "If an illusion made someone happy, would you break it?" | Yes, truth first / No / Only if they asked | Honesty vs kindness | Ch 40 (the council): "We've all lived in a nice illusion" | Her stance on making the Quiet Ending public |
| `ans.sensei_3.flower` | Level 3 | "Which flower should I press for you?" | Persimmon blossom / Rose / A weed from the training ground | Kindness | She gives it; it is in your apartment as a keepsake | — |
| `ans.sensei_3.say_it` | Ch 41 (at the memorial) | "Is there anyone on this stone you'd say something to?" | The girl's family / My parent, whoever they were / Nobody yet | Grief | Ch 54: she stands with you at the stone and says it with you | — |
| `ans.sensei_3.squad` | Level 6, Jonin arc | "If one of mine froze, and someone got hurt, would you tell them it wasn't their fault?" | Yes / No, I'd tell them it's how they learn / I'd tell them I froze once too | Kindness | Ch 54: what she says to squad3_a about the night the gate fell (she was at the Academy); unset: "You built a line out of nothing. That's all anyone can do" | squad3_a's growth line |
| `ans.sensei_3.festival` | Level 2, the Leaf Festival (Beta 2) | "Do you like festivals, or do you like watching them?" | Being in them / Watching / Watching with someone | Kindness | Her greetings at every festival after; Ch 54's epilogue festival ("With someone, you said. I'm trying it") | Seeds her "bored with him, at festivals" dream |
| `ans.sensei_3.angry` | Ch 37.0, after her line | "Is it wrong to be angry at someone for saving you?" | No / Yes, but it's human / Tell them, then decide | Honesty with herself | The Rock talk: what she says first to the sensei | "Tell them" makes the Rock talk happen the same night, not weeks later |
| `ans.sensei_3.genjutsu` | Level 3 (a training hangout) | "If I put you in a genjutsu of your happiest day, what would I see?" | The cord test / A bowl of ramen / A house with a tree / I don't have one yet | Openness | Ch 51a: the leaves she spreads over the Academy show a glimpse of your answer as you pass | "Don't have one yet": she makes one for you in the epilogue (a pressed-flower card) |
| `ans.sensei_3.trio` | Level 4, Genin arc | "My three argue about who matters most in a team. What do you think?" | The planner / The one who holds the line / The one who keeps everyone talking | Family | Ch 51a: she says it to squad3_b at the Academy door as the evacuation starts, and sends it to squad3_a and squad3_c by the Academy's runner; unset: "Hold on to each other" | — |
| `ans.sensei_3.persimmon` | Ch 21.3 (the anniversary; she watches from the path) | "He leaves one every year. Should I leave one too?" | Yes / Leave it with them, together / Leave something of your own | Grief | Epilogue: the two leave persimmons together (together), she leaves a pressed flower (own), or she leaves her own the next year (yes) | — |

**What her lines are for.** The Ash Road's living witness (seed, plot); a gentle adult for the
player in the Chunin years (bond); the trio's teacher (ensemble). Pools: greetings by arc; a
polite-hurt pool (festivals, before Ch 36); the forest proctor lines (Ch 16).

**Unison technique (Blaze).** *Grove of Embers*: her falling-leaf genjutsu, kindled, becomes a fall of
ember-lit leaves over a whole district, hiding everyone the player is bonded to.

**Variants.** Varied: any genjutsu-capable shinobi; the Ash Road role is fixed.
`twist.lineage = fallen`: in Ch 48 aftermath she says, "They talked about a child once. I never
asked." `= second`: she says nothing new.

**New flags.** `ans.sensei_3.spared` (knew, ask_road, nothing; the arc's), `ans.sensei_3.saved_choice` (saved, stay, together), `ans.sensei_3.coward` (trust,
sometimes, forgivable), `ans.sensei_3.illusion` (break, keep, if_asked), `ans.sensei_3.flower`
(persimmon, rose, weed), `ans.sensei_3.say_it` (girl_family, my_parent, nobody),
`ans.sensei_3.squad` (not_fault, learn, froze_too), `ans.sensei_3.festival` (in_them, watching,
with_someone), `ans.sensei_3.angry` (no, human, tell_them), `ans.sensei_3.genjutsu` (cord, ramen,
tree_house, none_yet), `ans.sensei_3.trio` (planner, line, talker), `ans.sensei_3.persimmon` (yes,
together, own).

---

## `role:sensei_4`

### At a glance

| | |
|---|---|
| Role | Squad 4's Jonin (`squad4_a`, `squad4_b`, `squad4_c`); the Leaf's interrogator in the story's key captures |
| Name | Given Family, rolled. Classic: a **Morino** |
| Look | Classic: curated: a very large man in a long dark greatcoat, a shaved head with old scars, flour on his cuffs. Varied: rolled |
| Pronouns | Classic: he. Varied: rolled; dialogue uses `{they:sensei_4}` |
| Specialty and style | Interrogation, binding wire, pressure: he fights slowly and never misses a grab |
| Rank | Jonin throughout |
| Archetype | Classic: **stern** at work, **warmhearted** at home (two pools) |
| Values | Honesty, duty |
| Peeves | Dishonesty, cruelty |
| Dream | To be trusted, not feared |
| Tier | Story-driving |
| First / last | Ch 8 / Ch 55 |

### Arc

**Wants.** To be trusted. The village crosses the street from the Morino.

**Fears.** That he is what they think: a man who sees the worst in people first. (He usually is
right, and it costs him.)

**Secrets.** He bakes bread every morning for the hospital and his squad and has never told anyone
it was him. He once got a confession from an innocent man (years ago) and has never trusted a
confession since.

**What he knows and when.**

| Knowledge | From |
|---|---|
| "Yūgure" (the smuggler's only word) | Ch 14 |
| The paper looks for "the old fire" | Ch 23 (the tester) |
| A voice inside; "in its own hand" | Ch 28 (he hears the porter) |
| Each candidate's alibi status | Only what the player brings to the case board (Ch 38) |
| The voice | Ch 39 |

He never knows the bound answer before the player does; he never suggests a name.

**How he changes.**

| Arc | Change |
|---|---|
| 2 Paper Trail | Ch 14: interrogates the smuggler for a night and gets one word. "That word was the most frightened thing I've ever heard a man say." |
| 4 Embers | Ch 23: the tester. Ch 28: reaches the porter first and tries to hold the cinder seal in his palm back with a binding; fails; stays with him until the medic comes and is visibly shaken |
| 5 Ashes | Ch 38: sits with the player at the case board; asks good questions, never gives answers; distrusts Thread Sight ("A flicker isn't proof. Everyone hides something. I hide bread."). Ch 39: makes the arrest. If the player accused without proof, he warns once ("Are you sure? Then sign it.") |
| 7 Last Bonfire | Ch 51a: runs the hospital with squad4_c and the medic through the war (triage, the door, the bread) |

**Endings.** He lives. If the player thanks him for the bread (`ans.sensei_4.bread = thanked`
after Ch 39), the village learns it was him; in the epilogue a line of children waits at his door.

### Relationships

- **His squad:** squad4_a (fairness), squad4_b (noise), squad4_c (quiet); he is gentle with all three
  and terrifying to everyone else.
- **sensei_2:** "the Baker" to his face; respects him more than he admits.
- **The medic:** works beside them at the hospital; in `twist.traitor = medic` saves, the arrest is
  the hardest thing he does.

### Dialogue brief

**Voice.** Slow, low, few words; asks questions he already knows the answer to, to see how you
answer; never threatens, just waits. At home (and with his squad), suddenly warm: "Eat. You're
thin." Never guesses aloud. Never says "I know you're lying"; says "Try again."

Voice samples, not shipped lines:
- "Sit. Take your time. I have all night. I brought bread."
- "Try again."
- "A flicker isn't proof. Everyone hides something."
- (case board) "What would have to be true for this to be them? Now: what would have to be true for it not to be?"
- (Ch 39) "I'll do it. It's my job to be the one they hate."

**Topics.**

| Topic (level) | What he says |
|---|---|
| Small talk (0) | One word answers |
| Training (1) | "Listen more than you talk. Then listen again." |
| Hobby (2) | Denies baking (at level 5 admits it) |
| Family (4) | The Morino house: "Bars on the windows so the neighbours feel safe. Inside, we have a cat." |
| Values (5) | "The truth is heavy. Carry it anyway, and don't drop it on people." |
| Advice (5) | On suspicion: "Write down why. If you can't, you don't suspect them, you just dislike them." |
| Dream (6) | "A street where people don't cross over." |
| Worries (7) | The innocent man he broke; you, at the case board |

**Never reveal before.**

| Fact | Not before |
|---|---|
| Any opinion on who the voice is | Never (he only asks questions) |
| The porter's words, to anyone but the player | Ch 38 |
| The bread | Level 5 |

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | Changes him |
|---|---|---|---|---|---|---|
| `ans.sensei_4.see_first` | Ch 14 or level 2 | "When you look at me, what do you see first?" | The coat / The scars / The flour on your cuffs | Honesty | Level 5: "You saw the flour. Nobody sees the flour." | "Flour" opens his warm pool early |
| `ans.sensei_4.worse` | Ch 28 (after the porter) | "Which is worse: trusting a liar, or doubting an honest man?" | Trusting a liar / Doubting an honest man / Doing either without checking | Honesty, duty | Ch 38: his opening question at the case board | Sets how hard he presses you on proof before the accusation |
| `ans.sensei_4.confess` | Level 3 hangout | "What would you confess to, if I asked nicely?" | Eating the cook's last egg / Breaking curfew / Nothing, ask harder | Humour | A running joke in his greetings | — |
| `ans.sensei_4.second_chance` | Ch 40 (after the reveal) | "Do people deserve a second chance after they've lied to you?" | Yes / If they tell the truth now / No | Duty vs kindness | Ch 55: his line about your ruling on the voice | — |
| `ans.sensei_4.bread` | Level 5 (he admits it) | "Don't tell anyone." | Promise / Tell them anyway / Ask to learn | Trust | Epilogue: the line of children | "Learn": a baking hangout opens |
| `ans.sensei_4.feared` | Level 6, Jonin arc | "Would you rather be feared and right, or trusted and wrong?" | Feared and right / Trusted and wrong / Neither, I'd work harder | His dream | Ch 51a: at the hospital he says which he chose (unset: "Neither. Bread.") | — |
| `ans.sensei_4.smuggler` | Ch 14 (after the night's questioning) | "One word in a whole night. Was I too hard, or not hard enough?" | Too hard / Not hard enough / Fear doesn't talk | Honesty | Ch 23 (the tester): he questions harder, gentler, or offers the tester food first | Sets his method in Ch 23 |
| `ans.sensei_4.porter` | Ch 28 (after the seal) | "I had my hands on that seal. Could I have done anything?" | No / Faster, maybe / You stayed with him; that was something | Duty | Ch 38: he keeps the porter's words pinned at the top of the board | "Stayed with him": he visits the porter at the shrine in the epilogue |
| `ans.sensei_4.flicker` | Ch 38 (if you mention Thread Sight) | "Your threads show who's hiding something. Does that make them guilty?" | No, everyone hides something / It makes them worth asking / Yes | Honesty | Ch 39 (a wrong accusation): "You said ___. Remember it now." | "Yes": he presses harder for paper proof before the arrest |
| `ans.sensei_4.squad_noise` | Level 3, Genin arc | "My dog boy is loud, my Hyuga is quiet and my herbalist hides in the greenhouse. How do I make them a squad?" | Feed them / Give them one problem none can solve alone / Let them fight it out | Family | squad4's Chunin-arc bond beats (a shared meal, a joint mission, a sparring brawl) | — |
| `ans.sensei_4.sign` | Ch 39 (before any accusation) | "When you sign this, it's your name on it. Still sure?" | Yes / Give me a day / Sign it with me | Duty | Ch 40: the council hears whose names are on the arrest | "With me": both names on the warrant; his clan's standing rises with yours |

**What his lines are for.** The interrogations and the case board (clue: he frames, never solves);
the fairness of the mystery made visible (he refuses to treat a flicker as evidence); his squad's
father figure; comedy in the warm pool. Pools: stern and warm greetings; case-board prompts
(generic, rotation-free); arrest lines per candidate (written with the reveals).

**Unison technique (Blaze).** *Iron Hearth*: his binding wire, kindled, becomes a cage of ember
light that holds a target without hurting it.

**Variants.** Varied: any steady, stern shinobi. Rotations: his Ch 39 arrest lines differ by
`twist.traitor`; the medic's is the hardest.

**New flags.** `ans.sensei_4.see_first` (coat, scars, flour), `ans.sensei_4.worse` (trust_liar,
doubt_honest, unchecked), `ans.sensei_4.confess` (egg, curfew, nothing), `ans.sensei_4.second_chance`
(yes, if_truth, no), `ans.sensei_4.bread` (promise, tell, learn), `ans.sensei_4.feared` (feared,
trusted, neither), `ans.sensei_4.smuggler` (too_hard, not_enough, fear), `ans.sensei_4.porter` (no,
faster, stayed), `ans.sensei_4.flicker` (everyone, worth_asking, yes), `ans.sensei_4.squad_noise`
(feed, one_problem, fight), `ans.sensei_4.sign` (yes, a_day, with_me).

---

## `role:sensei_5`

### At a glance

| | |
|---|---|
| Role | The senior squad's Jonin (`squad5_a`, `squad5_b`, `squad5_c`); the Leaf's old sealing master |
| Name | Given Family, rolled. Classic: an **Uzumaki** |
| Look | Classic: curated: an old man (about seventy) with a long white braid that was once red, round spectacles, a coat of sealing brushes, a loud laugh. Varied: rolled (always old) |
| Pronouns | Classic: he. Varied: rolled; dialogue uses `{they:sensei_5}` |
| Specialty and style | Sealing: barriers, binding chains, seals that hold or break; fights by drawing faster than people move |
| Rank | Jonin (refuses to retire) |
| Archetype | Classic: **warmhearted**, talkative (warmth .8, openness .5, discipline -.1) |
| Values | Family, knowledge |
| Peeves | Neglect, laziness |
| Dream | To pass on everything before he goes |
| Tier | Story-driving |
| First / last | Ch 7 (with the senior squad at graduation) / epilogue |

### Arc

**Wants.** To teach everything he knows before he dies, to someone who will listen.

**Fears.** That he talked his whole life and nobody heard the important part. That he once
didn't ask a question he should have.

**Secrets.** Forty years ago the Third asked him to inspect "a very old seal under the Rock". He
renewed it and did not ask what it held. He has wondered ever since. He taught half the Jonin of
the Leaf (the player's sensei, sensei_2, sensei_3 as Academy guest-teacher), and calls them by
pet names.

**What he knows and when.**

| Knowledge | From |
|---|---|
| A seal under the Rock, renewed for the Third | Before Y0 |
| What it guarded (the archive) | Ch 36 |
| Cinder seals: what they are | Ch 28 (he examines the one burned into the porter's palm) and Ch 49 (the array) |
| The Hollow Crown | Ch 49 |

**How he changes.**

| Arc | Change |
|---|---|
| 1 Cinders | Ch 7: watches the graduation with his senior squad, loudly commenting |
| 3 Dusk | Ch 19: seals the stadium's gates so the evacuation can run, shouting instructions at everyone |
| 4 Embers | Ch 28: reads the burned palm seal: "Whoever drew this has been drawing for a very long time." (A seed: the leader's age) |
| 5 Ashes | Ch 36: breaks the archive's old seals with the keeper: "I put my hand on this door forty years ago and I didn't ask. I'm asking now." |
| 7 Last Bonfire | Ch 50: teaches the village to break cinder seals (systemic: a technique scroll and a lesson every district needs); Ch 52: holds the array's last anchor on the Rock shut with his own chakra while the player faces the leader. He survives, drained, and spends the epilogue teaching squad5_b, who finally talks back |

His growth: from talking to listening. The silent squad5_b is his lesson.

### Relationships

- **His senior squad:** squad5_a (hope), squad5_b (silence he has to learn to hear), squad5_c
  (talent he cannot hold).
- **The other senseis:** his pet names; he scolds them like students.
- **The Uzumaki line:** if `clan.uzumaki.3` is done, the scattered Uzumaki is his great-niece and
  helps him in Ch 36.

### Dialogue brief

**Voice.** Loud, warm, long sentences with digressions; tells a story to answer a yes-or-no
question; laughs at his own jokes; then, rarely, one quiet line that is the point. Never says
"I'm too old." Never says anything he hasn't checked twice about seals.

Voice samples, not shipped lines:
- "Ha! A seal is a promise with good handwriting. Sit, sit, this will take an hour."
- "My quiet one, my loud one, my sad one, and my baker. And now you. What are you?"
- "Whoever drew this has been drawing for a very long time."
- "I put my hand on this door forty years ago and I didn't ask. I'm asking now."
- (Ch 52, quiet) "Go on. I've got this one. I've had it for forty years."

**Topics.**

| Topic (level) | What he says |
|---|---|
| Small talk (0) | A story about the weather in a year you've never heard of |
| Training (1) | Sealing basics; brush grip |
| Hobby (2) | Calligraphy; he will teach you to write your name properly |
| Family (4) | The Uzumaki: "Few of us left, all of us loud" |
| Values (5) | "Ask the question. Even if the answer is heavy." |
| Advice (5) | "Listen to the quiet ones. They've been waiting." (He is learning it himself) |
| Dream (6) | "One student who'll hold everything I drop." |
| Worries (7) | The door he didn't ask about |

**Never reveal before.**

| Fact | Not before |
|---|---|
| He renewed the seal under the Rock | Ch 36 (at level 7, in the Jonin arc, he can hint "I once sealed something I didn't understand") |
| The leader's age read from the seal | Said at Ch 28 as a strange fact; never connected aloud before Ch 49 |
| The array | Ch 49 |

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | Changes him |
|---|---|---|---|---|---|---|
| `ans.sensei_5.carve` | Level 3 hangout (calligraphy) | "If you had to write one word on a seal that must hold forever, what would it be?" | Home / Remember / Together / Open | Knowledge, family | Ch 52: he writes your word on the last anchor's seal as he holds it | — |
| `ans.sensei_5.ask` | Ch 36 (at the door) | "Should I have asked, back then?" | Yes / You trusted her; that's not nothing / You're asking now | Knowledge vs loyalty | Ch 52: his last line | "Yes": he takes the blame aloud at the council (Ch 40) |
| `ans.sensei_5.teach_one` | Level 5, Chunin arc | "If you could only teach one person everything you know, who would you pick?" | A friend / A stranger who needs it / Someone like me / Nobody, I'd teach everyone a little | Family | Ch 50: how he runs the village seal lessons (one student, or all) | "Everyone": Ch 50 finds more anchors (district lessons count double) |
| `ans.sensei_5.quiet` | Level 4 | "My quiet one never talks to me. What am I doing wrong?" | Talking / Nothing, wait / Ask her something and stop | His growth | Epilogue: squad5_b's first long answer to him | Starts his learning-to-listen arc early |
| `ans.sensei_5.name` | Level 2 (writing lesson) | "Shall I teach you to write your name? Or the name you'd like?" | My name / A name I don't know yet / Kagari (only offered after Ch 40) | Identity | Your name scroll keepsake reads it; Ch 46 the clan hall's first seal is in his hand | — |
| `ans.sensei_5.gates` | Ch 20 (after the attack) | "I sealed the gates behind the children. If someone had been on the wrong side, should I have waited?" | Yes / No, the children first / You'd have found a way | Duty vs kindness | Ch 52: on the anchor, "This time nobody's on the wrong side" | — |
| `ans.sensei_5.seal_read` | Ch 28 (he reads the palm seal) | "A lifetime of practice in that seal. Longer than mine. Who draws like that for so long?" | Someone who never stopped / Someone very old / Someone who isn't old | Knowledge | Ch 49: "You said ___. You were right." | A seed only; never answered before Ch 49 |
| `ans.sensei_5.loud` | Level 3 | "Am I too loud? Everyone says so and then nobody says it again." | Yes / Never stop / Only in the library | Honesty | His volume in the archive (Ch 36) and his rare quiet lines | "Yes": he tries whispering, badly, for a week (comic pool) |
| `ans.sensei_5.third` | Level 6, Jonin arc | "I knew the Third. Do you want to know what she was like, or would you rather she stayed a face on the Rock?" | Tell me / A face is enough / Tell me after the archive | Knowledge | Ch 36: he tells, or keeps quiet as the letter is read, or tells you on the way out | "Tell me": the Third's letter lands harder (his line: "That's her handwriting. She always pressed too hard") |
| `ans.sensei_5.last_lesson` | Ch 50 (after the seal lessons) | "If this was my last lesson, what should it have been?" | How to break a seal / How to make one hold / How to listen / Nothing, you'll teach more | Family | Ch 52: his line on the anchor; epilogue: what he teaches squad5_b | "How to listen": his epilogue scene is listening to squad5_b's paragraph |
| `ans.sensei_5.brush` | Epilogue gate (Ch 54) | "Who gets my brushes when I'm done with them?" | Me / squad5_b / The Academy / You're not done | Family | Epilogue | — |

**What his lines are for.** Sealing exposition in character (teach); the archive's last lock and
the array's breaking (plot); warmth and comedy (life); a long-life perspective on the Third's era
(seed, world). Pools: loud greetings; quiet lines (rare, after Ch 36); lesson lines (Ch 50).

**Unison technique (Blaze).** *Spiral Hearth*: his binding chains, kindled, become a spiral of
ember chains that seal an area against chakra drain (the counter to the dark mirror's pull for a
moment; Ch 52 dressing).

**Variants.** Varied: any old sealing specialist. If the Uzumaki line is not done, his great-niece
does not appear.

**New flags.** `ans.sensei_5.carve` (home, remember, together, open), `ans.sensei_5.ask` (yes,
trusted, asking_now), `ans.sensei_5.teach_one` (friend, stranger, like_me, everyone),
`ans.sensei_5.quiet` (talking, wait, ask), `ans.sensei_5.name` (mine, unknown, kagari),
`ans.sensei_5.gates` (wait, children_first, found_a_way), `ans.sensei_5.seal_read` (never_stopped,
very_old, not_old), `ans.sensei_5.loud` (yes, never_stop, library), `ans.sensei_5.third` (tell,
face, after), `ans.sensei_5.last_lesson` (break, hold, listen, not_last), `ans.sensei_5.brush` (me,
squad5_b, academy, not_done).
