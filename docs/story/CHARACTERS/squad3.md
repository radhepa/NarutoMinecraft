# Squad 3: `role:squad3_a`, `role:squad3_b`, `role:squad3_c`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Ensemble plan:
> [ENSEMBLE.md](../ENSEMBLE.md).

Squad 3 graduates with the player in Ch 7 and is taught by `sensei_3` (Classic: Yuhi, genjutsu; the
Ash Road team's survivor). In Classic it is a Nara, an Akimichi and a Yamanaka: the old three-clan
alliance (SIDE_QUESTS §4.2) in a new generation, and none of them is the canon version of their
clan. The squad's running dynamic: **a planner who cannot improvise, a heart who thinks he must be
someone else, and a reader of people who trusts nobody**. Together they work; that is the joke and
the point.

All three are rolled-look roles: in Varied their gender, look and clan are rolled by the class
weights, and dialogue uses pronoun tokens (`{they:squad3_a}`). The ★ role traits from ENSEMBLE.md
stay fixed in every save: squad3_b is **the Fourth's grandson** (his clan is the Fourth's, so
`squad3_b` is always Akimichi), squad3_c is **a sensor** (always Yamanaka: the Sixth's nephew).
**squad3_b and squad3_c have fixed clans in every save** (Akimichi and Yamanaka), because their Hokage relatives have fixed looks and clans; only their looks and genders roll. squad3_a's clan is the only one Varied may change (see Variants).

---

## `role:squad3_a`: the planner

### At a glance

| | |
|---|---|
| Role | Squad 3's strategist; the player's shogi rival |
| Name | Placeholder: **Shiori Nara** (Given Family, rolled per save) |
| Look | Classic: curated (a tight high ponytail that keeps coming loose, ink on her fingers, a notebook on a cord). Varied: rolled |
| Pronouns | Classic: she. Varied: rolled; tokens |
| Clan | Classic: Nara |
| Specialty | Shadow binding; traps; planning ten moves ahead. Style: never where the fight is; always where it will be |
| Rank | Academy → genin (Ch 7) → Chunin at the next season's exams (the time skip) → Jonin early in the Jonin arc (after the player) |
| Archetype | meticulous (BONDS §5) |
| Values / peeves | duty, knowledge / lateness, recklessness |
| Dream | Master their art (a plan with no hole in it) |
| Tier | Story-driving |
| First / last | Ch 1 (enrolment) / Ch 55 (the epilogue: she plans the Eighth's first festival) |

### Arc

- **Wants:** never to be the reason a plan fails.
- **Fears:** the moment the plan meets something it did not imagine. She freezes, and people get
  hurt while she recalculates.
- **Secret (small, every save):** she failed the Academy's practical once, as a younger student,
  because a dog ran onto the field and she stopped moving. She repeated the year. Nobody in this
  class knows (she is a year older than she says).
- **Knows, and when:** nothing of the twists. Learns of the gift from the rumours after Ch 31; of the
  archive after Ch 40 like everyone; of the Hollow Crown in Ch 49 (she is on the war council because
  she is the best planner the Leaf has).

| Arc | How she changes |
|---|---|
| Cinders | The girl who answers every question and asks the instructor for extra homework; challenges the player to shogi after Ch 2 |
| Paper Trail | Plans for her squad and hates that squad3_b improvises; shogi with the player becomes a ritual |
| Dusk | **Ch 16**: the forest truce. Her plan (a decoy scroll and a shadow trap) saves Squad 1 and Squad 3 from the foreign team's traps. In Ch 19 her plan for the stands collapses in the smoke and she freezes; squad3_b drags her out |
| Embers | Promoted in the skip. Writes every plan twice. Starts to ask the player about improvising |
| Ashes | **Ch 35**: with your old squad and hers in the Valley of Ash (squad4_b lent to the A-rank; his nose finds the nursery's back entrance), her plan gets twenty children out and home without a fight |
| Last Bonfire | **Ch 50**: plans the hunt for the eighty-one anchors (districts, clans, standing, who opens which door). **Ch 51a**: the gate's first line breaks and her plan breaks with it. For the first time she improvises: she builds the second line at the gate out of whatever is left, with nothing written down (the market street is teammate_b's and squad4_b's). In 51b sensei_2 dies holding that gate; her line is what he held. After the war she keeps one blank page in every notebook |

**Endings.** She becomes the Eighth's strategist. If the player answered her improvising question
(`ans.squad3_a.improvise`) with "you will", she says it back on the gate: "You said I would."

### Relationships

- **squad3_b:** she organises him; he feeds her. They bicker like siblings. She is the first one he
  tells when the Fourth's fate lands.
- **squad3_c:** the only person whose reading of people she trusts more than her own plans, and she
  tells him so once, which he does not believe.
- **sensei_3:** the sensei who keeps telling her a good illusion has gaps on purpose.
- **The player:** shogi rival. She never says the player is better; she keeps the score in her
  notebook.
- **squad4_a:** two disciplined girls who get on in silence; they study together at the library.

### Dialogue brief

**Voice.** Quick, precise, in lists. Counts things aloud ("Three problems. One: ..."). Says "Wait.
Wait." when she freezes. Never says "I don't know"; says "I don't know *yet*". Child: earnest and a
little bossy. Teen: dry. Adult: still lists, but she lets other people finish their sentences.

*Voice samples, not shipped lines:*
- "Three problems. One: we're lost. Two: they're not. Three: {given:squad3_b} ate the map."
- "Again. You won because I hesitated, and I won't hesitate twice."
- "Wait. Wait. That wasn't in the—" (beat) "...Fine. New plan. I'll write it after."
- "{player}, you never plan, and it works. I need to know why before it stops working."
- (adult) "I kept a page blank. In case."

**Topics by depth.**

| Depth | What she says |
|---|---|
| Small talk, training (0 to 1) | Shogi openings, the weather as tactics |
| Hobby (2) | Shogi problems she sets herself; she will give you one to solve |
| Family (4) | A family of strategists who expect brilliance and say "hm" when they get it |
| Values (5) | "A plan is a promise you make to everyone in it." |
| Advice (5) | Gives it in numbered points |
| Dream (6) | A plan with no hole in it; she knows it's impossible |
| Worries (7) | The repeated year: the dog on the field |

**Never reveal before.**

| Fact | Gate |
|---|---|
| Her repeated year | Level 7 (`worries`) |
| Anything about the gift | After Ch 31 (rumour), only as rumour |
| The array or Hollow Crown | Ch 49 |

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | How it changes her |
|---|---|---|---|---|---|---|
| `ans.squad3_a.shogi` | After Ch 2, first shogi game (`side.b1.shogi` or a hangout) | "Do you play to win or to not lose?" | win, not_lose, "to see what you'll do" (watch) | Win tests her caution; not_lose honours duty; watch intrigues her | Every shogi greeting; Ch 50's plan has a "{player} gambit" if win | She starts opening aggressively against you |
| `ans.squad3_a.forest` | Ch 16.2b, the truce | "Do we split up or stay together? You decide, I'll plan either." | split, together, "your call, it's your plan" (yours) | Yours honours her and also makes her freeze a second | Ch 51: on the gate she says "You let me choose in the forest. I'm choosing" | together: Squad 3 trusts Squad 1 for good; yours: she grows faster |
| `ans.squad3_a.froze` | Ch 20 or the first hangout after Ch 19 (level 3) | "I froze in the stands. Did you see?" | "I saw, and it's all right", "I didn't see" (a kind lie), "Then plan for freezing" | Plan honours knowledge; the lie violates honesty if she finds out (squad3_b saw you watching) | Ch 51 if "plan for freezing": she has a written plan for her own freeze, and uses it | Planning for freezing is her turning point |
| `ans.squad3_a.improvise` | Embers, level 5 (Asking their advice, reversed) | "How do you decide when there's no time?" | "I don't, I just move", "I trust whoever's beside me", "I already decided who I am, so the rest is easy" | All three teach her something different | Ch 51 improvisation line quotes it | Shapes how she improvises: alone, with others, or from values |
| `ans.squad3_a.children` | Ch 35, the night camp | "Twenty children and a road. If it goes wrong, who do we save first?" | the youngest, the closest, "nobody first: we plan so we don't choose" | None is right; tests duty and kindness | Ch 50: her anchor plan's priorities follow it | Her war plan orders districts by your answer |
| `ans.squad3_a.worry` | Level 7 (worries) | "Would you trust a plan from someone who froze once and repeated a whole year?" | yes, "only if they planned for it", "I'd trust them more" | "More" honours her completely | Ch 55: she shows you the blank page | `supported_dream` if "more" |
| `ans.squad3_a.hokage` | Road to Hokage, level 6+ | "When you're Hokage, will you want a strategist who tells you no?" | yes, "only in private", "you'll tell me no anyway" | Yes honours honesty | Ch 55: she accepts the strategist's post with your words | She becomes the Eighth's strategist (if answered at all; otherwise she runs the Academy's tactics class) |
| `ans.squad3_a.homework` | Cinders, level 1 (small talk in the Academy yard) | "Did you finish the reading? All of it? Even the footnotes?" | "all of it", "most of it", "there was reading?" | Knowledge; "there was reading?" breaks a peeve gently and makes her laugh despite herself | Ch 7 exam eve: she offers you her notes (most / none) or asks for yours (all) | Small: who studies with whom at the Ch 6 table |
| `ans.squad3_a.squad` | Paper Trail, level 3 (a tea-house shogi game) | "My squad never follows the plan. Do I change the plan or change the squad?" | "change the plan", "change how you tell them", "keep both, add a backup" | Duty against kindness | Ch 16.2b: her plan has a part for squad3_b's improvising ("change how you tell them") | Her squad's cohesion lines in Ch 19 |
| `ans.squad3_a.loss` | After Ch 19, level 4 (the first hangout after the attack) | "We lost people in the stands I'd counted. Do you count people, in a fight?" | "every one", "only mine", "I don't count, I just go" | Duty, loyalty; "just go" scares and fascinates her | Ch 50: the anchor plan counts residents by your answer (every district / squads first / no headcount) | Shades her war plan's priorities with `children` |
| `ans.squad3_a.sensei` | Embers, level 5 | "Our sensei says a good illusion has gaps on purpose. Does a good plan?" | "yes", "no, close every gap", "leave one for someone you trust" | Creativity against discipline | Ch 51: the gap she leaves in the market trap is for you ("one for someone you trust") | Feeds the blank page |

**What her lines are for.** Plot (Ch 16, Ch 50, Ch 51 plans), teach (she explains clan standing and
the anchor map as a strategy board in Ch 50: the player's checklist in character), bond (shogi
ritual), filler (shogi trash talk, deadlines). Mood states: normal, frozen (short, repeated
"wait"), quarrel (she schedules the reconciliation). Pools: greetings by arc, shogi win/loss lines,
a "freeze" pool for combat.

**Variants.** Varied may roll her any clan of the class weights; the ★ trait is **the planner who
freezes**. Skins: a Nara or Sarutobi (shogi and shadow/fire traps), a clanless one (a scroll-shop
child with scroll traps), a Hyuga or Aburame (formation tactics). The Ch 16 truce, Ch 50 plan and
Ch 51 improvisation stay.

**Unison technique (Blaze).** *Shadow Ember Snare*: her shadow binding carries the player's ember
along it; anything it catches is pinned and marked for the whole linked squad.

**Thread Sight.** Her thread to squad3_b is the steadiest on the map; to the player, it brightens
after every shogi game she loses.

---

## `role:squad3_b`: the grandson

### At a glance

| | |
|---|---|
| Role | The Fourth Hokage's grandson; Squad 3's heart and wall |
| Name | Placeholder: **Daichi Akimichi** |
| Look | Classic: curated (broad, soft-spoken, an apron under his flak jacket from Chunin on). Varied: rolled look, clan fixed |
| Pronouns | Classic: he. Varied: rolled; tokens |
| Clan | Akimichi (★ fixed: the Fourth's clan) |
| Specialty | Expansion and the rolling charge; cooking (buffs from his dishes) |
| Rank | Academy → genin → Chunin in the time skip → Jonin in the Jonin arc |
| Archetype | warmhearted |
| Values / peeves | kindness, family / cruelty, neglect |
| Dream | Open a shop (a barbecue house of his own) *and* be a shinobi |
| Tier | Story-driving |
| First / last | Ch 1 / Ch 55 (stands beside the player when the stipend is extended and made law) |

### Arc

- **Wants:** to be a chef and a shinobi both, and not his grandfather's shadow.
- **Fears:** that he is not enough of either: not the shinobi his grandfather was, not the cook his
  mother is.
- **Secret (small):** he wants the kitchen as much as the flak jacket, and has never told his
  grandfather he means to have both. (He will never get to tell him in the *falls* variant.)
- **Knows, and when:** the Fourth tells his family more than he tells the village. squad3_b knows
  the stipend was his grandfather's own idea, paid partly from his own pocket in the first years
  (he tells the player at level 4). In *taken*, he knows from his grandfather (Ch 21) that "they
  practised on me"; he never knows why until Ch 49.

| Arc | How he changes |
|---|---|
| Cinders | Brings food to everything. **Ch 6**: arrives at the study night with a pot from the barbecue house; when classmate_c's parent thanks "the Hokage's grandson", he goes quiet |
| Paper Trail | Serves the squad dinner after Ch 14 at his mother's barbecue house; his expansion is clumsy |
| Dusk | **Ch 19**: he holds the east stair beside the player; when the Fourth is hit he runs the wrong way, toward the Kage box. What he sees is `twist.fourth_fate` (below) |
| Embers | By the variant (below) |
| Ashes | Ch 35: carries children two at a time. Ch 40: says out loud that his grandfather never knew about the archive, and asks the player if that makes it better or worse |
| Last Bonfire | **Ch 51a**: holds the Academy door with the instructor and sensei_3 (expanded to fill the doorway for an hour). Ch 55: restores the stipend with the player in his grandfather's name |

**By `twist.fourth_fate`:**

| | Falls | Crippled | Taken |
|---|---|---|---|
| Ch 19 | Sees his grandfather fall on the arena floor covering the Academy children's evacuation (the cinematic cutaway); the player's squad pulls him back from the floor | Reaches the box as the dark mirror tears into his grandfather; carries him out | Sees the ash-violet scarves lift his grandfather over the wall; tries to follow and is knocked flat |
| Ch 20 | **The Akimichi farewell feast**: the whole village eats the Fourth's favourite dish in the street, his bowl set at an empty place. squad3_b cooks because he cannot speak, then speaks once: he quotes what the Fourth asked the player (`ans.hokage_4.want`: "He asked {player} what they wanted to be. They said..."; unset: "He asked everyone what they wanted to be. He never asked me. I'd have said: both.") | At the hospital he sleeps in the chair | He refuses to leave the Kage box until the sensei carries him home |
| Ch 21 | At the statue: tells the player he was going to quit; now he cannot | His grandfather's caretaker; learns to cook soft food; tells his grandfather he wants the kitchen, and is told "Then why are you still here?" | **Insists on joining the Empty Seat rescue**, which `sensei_2` leads; he is the one who carries his grandfather out |
| Endings | Opens the barbecue house's second room as a ramen-and-grill named for the Fourth; stays a Jonin | Cooks for his grandfather every night; a Jonin who runs a kitchen | Both, and his grandfather eats there every night |

### Relationships

- **squad3_a and squad3_c:** see above; he is the glue.
- **sensei_3:** brings her lunch, because she forgets to eat.
- **teammate_b:** competitive eaters.
- **The player:** the first classmate who invites the player home (Ch 6 and a dinner at level 5).
  He knows the player's stipend number is on his grandfather's list.
- **The Fourth's daughter (`hokage_4_daughter`):** his mother. Her jokes are his jokes.

### Dialogue brief

**Voice.** Slow, warm, food metaphors he does not notice he is using. Says "It's fine, it's fine"
when it isn't. Never insults anyone's appetite. Child: shy, mumbling. Teen: steadier, a joker with
the squad. Adult: a host's voice.

*Voice samples, not shipped lines:*
- "Here. You looked like someone who forgot breakfast."
- "Everyone says Grandpa this, Grandpa that. He can't even cut onions without crying."
- "It's fine. It's fine. (beat) It's not fine."
- (crippled) "He wanted it soft and salty. Like when Grandma made it."
- (adult) "Sit. Eat. Then tell me what we're doing."

**Topics by depth.**

| Depth | What he says |
|---|---|
| Food (1) | Everything; he asks your order and remembers it |
| Hobby (2) | Recipes; he trades one for one of yours |
| Family (4) | His mother's grill, his grandfather's stipend, his late grandmother |
| Values (5) | "Nobody eats alone at my table." |
| Dream (6) | His own shop, *and* the flak jacket |
| Worries (7) | That he chose the kitchen and his grandfather's fate punished him for it (all variants) |

**Never reveal before.**

| Fact | Gate |
|---|---|
| The Fourth's fate | Ch 19 |
| "They practised on me" (taken) | Ch 21 |
| Why they practised | Ch 49 |
| The stipend's private origin | Level 4 |

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | How it changes him |
|---|---|---|---|---|---|---|
| `ans.squad3_b.order` | Ch 6 or first meal together | "What's your favourite thing to eat? Not ramen. Everyone says ramen." | something from before the camps (a persimmon), "anything someone made for me", "I never had a favourite" | Kindness, family | He cooks it for you on your birthday every year | The persimmon answer is a seed his mother uses in Ch 21 ("Who taught you persimmons?") without meaning anything |
| `ans.squad3_b.grandson` | Ch 8 to 14, level 3 | "Do you think people only like me because of my grandfather?" | "I like you because you fed me", "maybe, so make them like you for you", "I didn't know who he was" | Honesty | Ch 21 (falls): "You said they'd like me for me. Do they?" | "for you" pushes him toward the kitchen sooner |
| `ans.squad3_b.quit` | Ch 21, level 5 | "If I quit and cooked instead, would that be running away?" | "no, it's choosing", "not if you finish what you started", "do both" | Freedom against duty | His ending (above): choose → the kitchen first; finish → Jonin first; both → both | Decides his ending |
| `ans.squad3_b.archive` | Ch 40 | "He never knew. Is that better or worse?" | better, worse, "it means you get to decide what he'd have done" | — | Ch 55: what he says at the stipend's restoration | Shapes his Ch 55 speech |
| `ans.squad3_b.door` | Ch 50, before the war | "If the Academy door falls, I fall with it. Is that stupid?" | "yes, run", "no, but I'll come", "it won't fall, I'll send help" (an Ember Mark promise if Blaze with him) | Courage, loyalty | Ch 51: if "I'll come" and the player arrives, a `saved_life`; if "help", an ally appears | Changes who arrives at the Academy in Ch 51 |
| `ans.squad3_b.recipe` | Road to Hokage, level 7 | "Grandpa's recipe has one ingredient missing. Do I guess or leave the gap?" | guess, "leave it, it's his", "add yours" | Creativity, family | Ch 55's dish | The dish at the Eighth's inauguration |
| `ans.squad3_b.third_helping` | Cinders, level 1 (lunch in the yard) | "Do you want the last dumpling? You have to say yes, it's rude otherwise." | "yes", "split it", "you have it" | Family custom ("never refuse"); "you have it" is kind but against custom, and he is delighted and scandalised | He always saves you the last one at the squad dinner (Ch 14.6) | Filler that becomes a ritual |
| `ans.squad3_b.mother` | Paper Trail, level 4 (the barbecue house) | "Mum says I cook like Grandpa fights. Is that a compliment?" | "yes", "it depends how he fights", "ask her" | Family; "ask her" sends you to `hokage_4_daughter` | Her taste question (minor.md) opens with it | Small |
| `ans.squad3_b.funeral` | Ch 20 (falls) / hospital (crippled) / the empty box (taken), level 3+ | Falls: "Should I cook at the feast? Or is that weird?" Crippled: "Should I tell him I'm scared?" Taken: "Is it wrong to eat when he might be hungry?" | Falls: cook / sit with your mother / both. Crippled: tell him / be brave for him / tell me first. Taken: eat / eat for him / save him a bowl every night | Grief, family | Ch 21 by variant: the funeral dish, the hospital confession, or the saved bowls he gives his grandfather after the Empty Seat | His grief takes the shape of your answer |
| `ans.squad3_b.expansion` | Embers, level 4 (a training hangout) | "I hate growing big. Everyone stares. Do I use it anyway?" | "use it, they can stare", "only when it protects someone", "make it yours, not the clan's" | Courage, family | Ch 51: he expands in the Academy doorway and says why | — |
| `ans.squad3_b.player_food` | Ashes, level 6 (dinner at his home) | "You never talk about what you ate in the camps. You don't have to. Do you want to?" | "yes" (a heart-to-heart), "not yet", "they fed us ash bread" | Openness; a real moment if "yes" at level 6 (`heart_to_heart`) | He never serves ash-coloured bread again; Ch 55's dish avoids it | Deepens the bond; "not yet" he asks once more at level 8 |

**What his lines are for.** Plot (the Fourth's fate seen from family), bond (feeding the player is
how he says everything), life and filler (food), teach (dish buffs in his kitchen hangout). Mood
states: by fate variant from Ch 19; grief pool (falls) for Ch 20 to 21; caretaker pool (crippled,
taken). Pools: greetings by variant, food lines, a "host" pool for the barbecue hangout.

**Variants.** Clan fixed (Akimichi), look rolled. Fate variants above.

**Unison technique (Blaze).** *Hearth Boulder*: his rolling charge wrapped in the player's ember,
leaving a trail of fire that heals allies who stand in it (his kindness made literal).

**Thread Sight.** In *falls*, his thread to the empty statue is the only thread the player ever sees
running to someone who is gone (a grief thread: grey, unfrayed).

---

## `role:squad3_c`: the reader

### At a glance

| | |
|---|---|
| Role | A sensor; the Sixth's nephew; the one who flags the player |
| Name | Placeholder: **Ren Yamanaka** |
| Look | Classic: curated (pale hair cut short, half-closed eyes, a flower behind one ear his aunt puts there every morning). Varied: rolled look, clan fixed |
| Pronouns | Classic: he. Varied: rolled; tokens |
| Clan | Yamanaka (★ fixed: the Sixth's nephew) |
| Specialty | Sensing (range grows with rank), mind techniques; quiet hands. Style: finds you before you find him |
| Rank | Academy → genin → Chunin in the time skip (joins the sensor corps) → sensor captain in the Jonin arc |
| Archetype | reserved |
| Values / peeves | honesty, freedom / nosiness, rudeness |
| Dream | Find where they belong (a person he does not have to read) |
| Tier | Story-driving |
| First / last | Ch 1 / Ch 55 |

### Arc

- **Wants:** to be sure of people.
- **Fears:** that everyone is lying and he is the only one who can tell; and, worse, that he cannot
  tell after all.
- **Secret:** in Ch 3 he felt the player's chakra move into their partner's and has thought about
  it for a year when he flags it in Ch 22. He did not flag it in Ch 3 because his uncle told him
  "children's chakra is strange". Flagging it in Ch 22 was his choice, and he is ashamed of the
  relief he felt.
- **Knows, and when:** that the player's chakra is anomalous (Ch 3, as a feeling; Ch 22, as a
  reading). The Kagari word only after Ch 31 as rumour. In Ch 44 he can read the lost child's
  "too many voices". In Ch 49 he can feel the array's anchors once he knows what they are.

| Arc | How he changes |
|---|---|
| Cinders | **Ch 3**: after the flare he says to the player, not unkindly, "Your chakra just moved into theirs." No one else hears |
| Paper Trail | Watches everyone; good on tracking missions; his mind technique is weak because he will not commit to it |
| Dusk | Ch 19: senses the hearths in the stands a second before the smoke and is not believed |
| Embers | **Ch 22**: the sensor who flags the player "Anomalous". He seeks the player out that night (if level 2+) to say he is sorry, or does not (below). Through Ch 31 he watches the Fifth's sweeps and starts to hate them |
| Ashes | Ch 40: his uncle the Sixth makes the archive public; he admits he flagged a Kagari descendant before anyone knew the word. **Ch 44**: on an A-rank with the player's Genin he reads the lost child: "There are a dozen people in there. She's at the bottom." |
| Last Bonfire | **Ch 49 to 50**: with the porter's ledger and the player's description he can feel cinder seals under floors; he finds the anchors the ledger missed. Ch 53: his flame is the first sensor's flame the player ever feels: a cool, exact light |

**Endings.** A sensor captain who trusts at least one person without reading them (the player,
if `ans.squad3_c.read` was "then don't"), or one who reads everyone and is lonely (if never
answered).

### Relationships

- **squad3_a, squad3_b:** the only two people he stopped reading years ago.
- **The Sixth (`hokage_6`), his uncle:** gentle with him; told him once that a sensor's first duty is
  to doubt his own reading. He tries.
- **squad4_a:** the two sensors of the Fifth's watch on the player. She follows; he flags. They
  argue about it until Ch 31.
- **The player:** guilt, then respect. From Ch 31 he is the one who tells the player, quietly, when
  a sweep is coming.

### Dialogue brief

**Voice.** Short. Observational. Answers questions you didn't ask ("You're angry. Not at me.").
Never says "I think"; says "I read". When he is unsure he goes silent instead of guessing. Child:
eerie. Teen: blunt. Adult: gentle, and still blunt.

*Voice samples, not shipped lines:*
- "Your chakra just moved into theirs."
- "You're lying. It's fine. Everyone does. I just hear it."
- (Ch 22, after) "I flagged you. I'd do it again. I'm sorry anyway."
- "My aunt puts a flower here every morning. It means 'come home'. She doesn't know I know."
- (Ch 44) "There are a dozen people in there. She's at the bottom."

**Topics by depth.**

| Depth | What he says |
|---|---|
| Small talk (0) | Mostly silence; reads your mood back to you |
| Hobby (2) | The language of flowers (the Yamanaka line) |
| Village news (3) | Knows it all, says little |
| Family (4) | The flower shop, the uncle who will be Hokage, the aunt with the flowers |
| Values (5) | "Doubt your own reading first." |
| Worries (7) | That he will never stop reading people long enough to have a friend |

**Never reveal before.**

| Fact | Gate |
|---|---|
| What he felt in Ch 3 (beyond the one line) | Ch 22 |
| That he flagged the player | Ch 22 (he admits it the same night or never) |
| "Kagari" in his mouth | After Ch 40 |
| The voices in the lost child | Ch 44 |

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | How it changes him |
|---|---|---|---|---|---|---|
| `ans.squad3_c.moved` | Ch 3.3, a reply to his line | (He doesn't ask; he waits.) The player may answer "What do you mean?", "Don't tell anyone", or walk away | ask, hush, walk | Hush makes him complicit; ask honours honesty | Ch 22: "You asked me what I meant. I still don't know." / "You told me not to tell. I'm telling." / nothing | Changes his Ch 22 apology |
| `ans.squad3_c.flagged` | Ch 22.1, that night | "I flagged you. Are you going to hate me?" | "yes", "no, you did your job", "ask me when I know what I am" | Honesty; duty | Ch 31: he warns you of the sweep only if "no" or "ask me" | "yes" starts a quarrel he lets run its course |
| `ans.squad3_c.read` | Embers, level 5 | "Do you want me to stop reading you? I can try." | "yes", "no, I've got nothing to hide", "then don't, and just ask me" | "Then don't" honours freedom deeply; "nothing to hide" makes him smile (he can hear that it's untrue, and likes you for it) | His ending | "then don't" is the turning point of his arc |
| `ans.squad3_c.flower` | Hobby talk, level 3 | "If you were a flower, what would you be saying?" | "come home", "I'm still here", "don't look at me" | Creativity | His aunt starts putting that flower in the player's window in the Jonin arc | — |
| `ans.squad3_c.voices` | Ch 44, after | "Should I tell the Hokage what I read in her?" | "yes", "only that she's breaking free", "no, it's hers to tell" | Duty against privacy | N3 and Ch 47: what the Undercroft knows depends on his report (if "yes", they learn faster) | — |
| `ans.squad3_c.anchors` | Ch 50 | "I can feel them now. All of them. It hurts. Do I keep going?" | "keep going", "rest, we'll find them", "I'll link with you" (Ember Link if Flame) | — | Ch 50: "link" finds ten more anchors | Ember Link with him is his first unread trust |
| `ans.squad3_c.lie` | Paper Trail, level 2 | "Tell me something true and something false. I'll say which." | true first, false first, "two true things" | Honesty; "two true things" stumps him, the first time anyone has | He tries the game again at level 6 and loses on purpose | Filler that becomes trust |
| `ans.squad3_c.stands` | After Ch 19, level 3 | "I felt them in the stands before the smoke. Nobody listened. Should I have shouted?" | "yes, always shout", "you couldn't have known it was real", "next time, tell me" | Duty, loyalty | Ch 22: "next time, tell me" makes him warn you about the sweep before it reaches you | — |
| `ans.squad3_c.uncle` | Ashes, after Ch 32, level 4 | "My uncle is Hokage now. People are nicer to me. Can I believe any of them?" | "believe the ones who were nice before", "read them and decide", "believe me" | Honesty | Ch 40: whether he stands beside his uncle at the council or watches from the back | — |
| `ans.squad3_c.purge` | After Ch 40, level 5 | "I flagged you for being what my village killed. What do I owe you?" | "nothing", "remember it", "help me find the others like me" | Duty, kindness | Ch 46: "help me" makes him the sensor who finds descendants for your house | His recruitment role |
| `ans.squad3_c.quiet` | Road to Hokage, level 7 (stargazing on the Rock) | "Do you ever want everyone to stop being so loud inside?" | "yes", "no, I like the noise", "with you it's quiet" | Openness; the last is a real moment at level 7 | His Ch 53 flame line | — |

**What his lines are for.** Clue and seed (Ch 3, Ch 22), plot (Ch 44, Ch 49 to 50), bond (guilt to
trust), life (flowers). Mood states: before Ch 22, after Ch 22 (guilt), after `ans.squad3_c.read`.

**Variants.** Clan fixed (Yamanaka), look rolled.

**Unison technique (Blaze).** *Lantern Net*: his sensing spread through the player's threads, so
every bonded ally becomes a sensor point; for a moment the linked squad sees the whole battlefield.

**Thread Sight.** His threads are many and thin: he is tied to almost everyone a little and to
almost no one much. They thicken toward the player after `ans.squad3_c.read`.

---

## New flags

- `ans.squad3_a.shogi` (win, not_lose, watch)
- `ans.squad3_a.forest` (split, together, yours)
- `ans.squad3_a.froze` (all_right, didnt_see, plan)
- `ans.squad3_a.improvise` (move, beside, decided)
- `ans.squad3_a.children` (youngest, closest, plan)
- `ans.squad3_a.worry` (yes, planned, more)
- `ans.squad3_a.hokage` (yes, private, anyway)
- `ans.squad3_b.order` (persimmon, made_for_me, none)
- `ans.squad3_b.grandson` (fed_me, for_you, didnt_know)
- `ans.squad3_b.quit` (choosing, finish, both)
- `ans.squad3_b.archive` (better, worse, decide)
- `ans.squad3_b.door` (run, come, help)
- `ans.squad3_b.recipe` (guess, leave, add)
- `ans.squad3_c.moved` (ask, hush, walk)
- `ans.squad3_c.flagged` (yes, no, ask_later)
- `ans.squad3_c.read` (yes, nothing_to_hide, dont)
- `ans.squad3_c.flower` (come_home, still_here, dont_look)
- `ans.squad3_c.voices` (yes, breaking_free, hers)
- `ans.squad3_c.anchors` (keep, rest, link)
- `ans.squad3_a.homework` (all, most, what_reading)
- `ans.squad3_a.squad` (plan, tell, backup)
- `ans.squad3_a.loss` (every, mine, go)
- `ans.squad3_a.sensei` (yes, close, trusted_gap)
- `ans.squad3_b.third_helping` (yes, split, you)
- `ans.squad3_b.mother` (yes, depends, ask_her)
- `ans.squad3_b.funeral` (by fate: cook, sit, both / tell, brave, tell_me / eat, for_him, save_bowl)
- `ans.squad3_b.expansion` (stare, protect, yours)
- `ans.squad3_b.player_food` (yes, not_yet, ash_bread)
- `ans.squad3_c.lie` (true_first, false_first, two_true)
- `ans.squad3_c.stands` (shout, couldnt_know, tell_me)
- `ans.squad3_c.uncle` (before, read, me)
- `ans.squad3_c.purge` (nothing, remember, help)
- `ans.squad3_c.quiet` (yes, noise, with_you)
