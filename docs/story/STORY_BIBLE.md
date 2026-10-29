# Story bible

> **SPOILERS: for developers only.** This file holds every twist of the Shinobi Modpack's story:
> identities, betrayals, the antagonist's goal and leader, the player's lineage, deaths and falls,
> reveal pacing and the seeds that pay off later. If you want to play the game unspoiled, stop
> reading here. [ROADMAP.md](../../ROADMAP.md) is spoiler-free.

The whole ~60-hour story, laid out so the beta plants the right seeds and the data formats can hold
it. Only the beta's arcs are built now. All characters are original; named canon characters appear
only as cameos.

## How to read this bible

- **Names are rolled per save, in Classic and Varied alike.** Every character below is written as a
  role (`role:librarian`, `role:yugure_leader`). Names in parentheses are samples only. A save rolls
  each character's given name from the seeded name pools and their family name from their clan (a
  clan character keeps the clan's name) or from the `family_names` pool in
  `tools/wardrobe/population.json`. Looks, personalities and roles stay as designed.
- **The Hokage's names are rolled too; their looks are not.** Faces on the Rock, portraits and
  statues are baked into the map, so each Hokage's appearance, clan and era are fixed. Only the
  given name is rolled; a clan Hokage's family name is the clan's.
- **Some twists rotate per save.** A **twist slot** has two to four candidates. The `twists` stream
  of the save seed binds one at world creation, in both modes, and each candidate has its own clue
  trail. A player who knows one answer from another save cannot be sure of it in this one. All
  candidates' clues are authored; the bound candidate's clues are true, the others' get innocent
  explanations later.
- **All text uses tokens.** Quests and dialogue say `{name:role:sensei}`, `{given:role:rival}`,
  `{hokage:4}` or `{twist:traitor}`, never a literal name.

## Twist slots

| Slot | Candidates | Bound at | Revealed |
|---|---|---|---|
| `twist.traitor` (who inside the Leaf feeds Yūgure) | 4: the librarian, the medic, the council elder, the merchant | World creation | Jonin arc |
| `twist.lineage` (where your Kagari blood comes from) | 2: Yūgure's second, or a fallen Leaf shinobi | World creation | Chunin arc (a hint), road to Hokage (the truth) |
| `twist.fourth_fate` (what the finals' attack costs the Fourth Hokage) | 3: he falls; he is crippled and abdicates; he is taken by Yūgure | World creation | Ch 19 to 20 |

### The traitor

Whoever it is fed Yūgure the names of gifted orphans for years, and their help is why the prologue's
hideout held Leaf children. The **council elder who knows the Kagari truth** (`role:elder_keeper`)
is never the traitor: he looks suspicious on purpose and is the keeper of the archive's secret, an
ally once you earn his trust.

| Candidate | Motive | Clue trail (seeded in the beta) | If innocent |
|---|---|---|---|
| **The librarian** (`role:librarian`) | Her family kept the founding history; she wants the Kagari truth told, even by fire | Ch 5: the cut page's edge is fresh, and she is nervous; a side quest finds Yūgure's cipher in a returned book | Someone used her library as a dead drop; she cut the page to protect it |
| **The medic** (`role:medic`) | A Yūgure orphan herself, rescued years ago by the leader's people before the Leaf found her; she owes them | Ch 0: she takes a sample of your chakra "for the records"; Ch 3: she visits after the flare; the hospital ledger is missing pages | She tests every rescued orphan; the ledger was stolen from her |
| **The council elder** (`role:elder_councillor`) | His clan's guilt over the purge, turned into a wish to see the Kagari back | Ch 1: he arranged your stipend papers personally; Ch 14: his seal is on the smugglers' travel pass | His seal was stolen by a Yūgure infiltrator in his household |
| **The merchant** (`role:merchant`) | Debt; Yūgure pays well and he tells himself he only carries paper | Ch 11: the cart's false floor; Ch 14: he slows the squad down on the road | He was a dupe; he becomes the squad's informant |

## Yūgure

**Yūgure** (夕暮れ, "Dusk") is a band of missing-nin from across the five nations. They work in
**two-man cells** and wear **ash-violet cloaks marked with a sinking sun**. Their creed: *the
shinobi world must end at dusk so that a true dawn can come.*

- **Origin.** About twenty years before the story, the last survivor of the Kagari
  (`role:yugure_leader`, family name Kagari, given name rolled) gathered missing-nin whom
  the hidden villages had wronged: soldiers abandoned after wars, orphans used and discarded, clans
  broken by treaties.
- **What the members believe.** The **Last Bonfire**: a fire of gathered chakra that spreads through
  the hidden villages until none of them stands at dawn. It is the creed's promise, and it is a lie.
- **The true goal: the Hollow Crown.** The leader means to force-kindle every chakra in the Leaf,
  through the dark mirror of the Kagari gift, into one living wick of pure Kagari blood, and then
  take it from the wick: one person holding a whole village's chakra, the "true dawn" of a single
  ruler over every shinobi. You are the wick. When Yūgure's second learns the truth, they turn.
- **Method.** Cells smuggle chakra paper to test children for unusual chakra, buy and steal orphans,
  and plant agents in villages. Inside the Leaf they have one source: the traitor (`twist.traitor`).

## The Kagari

The **Kagari** (篝, "bonfire") were a Warring States clan. In the last war before the Leaf's founding
a Kagari bonfire burned a valley with both armies in it: chakra torn from every soldier at once.
When the Senju and the Uchiha made peace, the founding clans agreed the Kagari could not be allowed
to exist, and ended them. The Second Hokage sealed the records in an archive under the Rock and had
their names chiselled off the memorial stone; the Third knew and kept silent. One child survived,
hidden in the clan's shrine in the southern hills (the ruined shrine the prologue's chase runs
past), and grew up to lead Yūgure.

## Kindling Bond

*Decided.* The Kagari gift is **Kindling Bond** (篝火の縁).

- **What it does.** Kagari chakra resonates with the people a Kagari is bonded to. You can kindle a
  bonded ally's chakra nature or one of their techniques and borrow it briefly: a few casts of their
  nature's jutsu, or one use of their signature technique, after which the flame needs time to
  rekindle.
- **Bonds decide what you can borrow.** Friendship level 6 lets you borrow an ally's nature, level 8
  one of their techniques, level 10 (or a teammate, your sensei, your spouse) both and for longer.
  A nature borrowed often enough can be learned for good with a master's trial.
- **How it looks.** A bond-flame, a small watch-fire (*Kagari-bi*), flickers between you and the
  ally, and your chakra takes their nature's colour while it burns.
- **The dark mirror.** Taking chakra by force instead of borrowing it through a bond: no bond, no
  consent, and the victim is left hollow. It is how the leader grew strong, why the lost child
  comes back empty, what the Hollow Crown is built on, and why the founders feared the clan. The
  player can never use it; the story offers the temptation once, in the last arc.
- **In the systems.** A `kindle` combat effect, friendship and romance levels as bond levels, a
  "borrowed" nature source, and the unlock flag `story.kindling.awakened`.
- **In the beta: foreshadowing only.** Ch 3: in a paired chakra exercise your chakra flares and, for
  a moment, takes on your partner's nature. Ch 8: a faint flame flickers between you and a teammate
  at the bells. Ch 16: on the forest night watch, the campfire leans toward your squad.
- **The first real kindling** is a big moment of the Chunin arc: in the lost child's raid on a
  border post, a teammate falls protecting you and you kindle their nature to finish the fight.

## Your lineage

The leader is **not** your relative in any save. You carry Kagari blood through `twist.lineage`:

| Candidate | The truth | How it lands |
|---|---|---|
| **Yūgure's second** (`role:yugure_second`) is your parent | They hid you as a baby with a border family to keep you from the leader, and lost you when Yūgure's cells found you anyway | At the finals they recognise you and say "Kagari"; in the road to Hokage they defect to protect you, and the reveal is theirs to make |
| **A fallen Leaf shinobi** of hidden Kagari descent was your parent | Killed on a mission the village buried; your sensei was their teammate and has carried the guilt | The sensei's suspicion in Ch 14 is recognition; the reveal comes from the sensei, and the Seventh's succession carries it |

A clan-born player's other parent was of that clan; a clanless player's Kagari blood is all they
have. Later, the player clan registry lets you restore the Kagari under their old name and crest
(with Kindling Bond as the clan art), or found a new clan.

## Reveal pacing

| By the end of | The player knows | The player suspects |
|---|---|---|
| Academy (beta) | Someone in a sinking-sun cloak took you and is watching you | Your chakra is strange; someone at the Hokage's side knows something |
| Genin (beta) | The name **Yūgure**; it smuggles chakra paper and orphans | The sensei knows what you are |
| Chunin Exams (beta) | Yūgure attacked the Leaf; one of them called you **Kagari** | Kagari is a clan, and you are of it |
| Chunin | Yūgure's cells and creed; the lost child is one of them; your bond-flame is a Kagari gift | The Leaf erased the Kagari; someone inside helps Yūgure |
| Jonin | The purge, the archive, the Third's silence; who the traitor is (this save's candidate) | What Yūgure really wants |
| Road to Hokage | Your lineage (this save's candidate); the Hollow Crown, and that you are its wick | — |

## The Hokage line

Looks, clans and eras are fixed (baked into the map's faces, portraits and statues); given names
are rolled per save. Faces one to four are on the Rock at the start; the Fifth and Sixth are fixed
carvings placed at story beats; the Seventh's and your Eighth's faces are built from your looks.

| # | Clan | Look (fixed) | Era | What they left behind |
|---|---|---|---|---|
| 1 | Senju | Broad, long dark hair, a calm founder's face | The founding | The wall, the founding charter (with its missing page), the memorial stone, and the agreement that ended the Kagari |
| 2 | Uchiha | Lean, sharp-featured, a high collar | The first generation | The Academy, the ANBU, the Chunin Exams, the sealed archive under the Rock and the chiselled names: the rule of silence |
| 3 | Sarutobi | A woman with a long braid and a kind, lined face | Thirty years of peace | The clan council, the Will of Fire lantern walk, and a letter in the archive "for whoever comes asking" |
| 4 | Akimichi | A big, warm man with a broad smile | Sitting when you arrive | The orphan's stipend that pays for your apartment; his fate at the finals is `twist.fourth_fate` |
| 5 | Hyuga | A severe woman, pale eyes, hair tied high | Named after the finals; the Chunin years | Border watch posts, curfews and a sensor corps; she distrusts your blood. She steps down when her hard line brings a clan quarter to the edge of revolt |
| 6 | Yamanaka | A soft-spoken man with long pale hair | The Jonin years | Opens the archive with you, makes the purge public, raises a memorial to the Kagari, and resigns to take responsibility for the Leaf's buried crime |
| 7 | The sensei's (`role:sensei`) | The sensei's own look | The road to Hokage | The captain who rescued you leads the village through the war with Yūgure and names you successor |
| 8 | You | Your look | — | — |

**The Fourth's fate (`twist.fourth_fate`).** *He falls* defending the stadium (a funeral in Ch 20);
*he is crippled* and abdicates (he becomes a mentor in the Chunin arc); or *he is taken* by Yūgure
(a rescue mission opens the Chunin arc, and he returns too weak to rule). In every save the Fifth is
named in Ch 20 and `world.hokage = 5`.

## Recurring characters

| Role | Sample name | Fixed look | First appears | Through the story |
|---|---|---|---|---|
| `role:hokage_4` | (rolled) Akimichi | Yes | Ch 1 | Warm and protective; his stipend is why you have a home |
| `role:elder_keeper` | (rolled) | Yes | Ch 1 | Watches you too closely; knows the Kagari truth and guards the archive; never the traitor; an ally in the Jonin arc |
| `role:elder_councillor` | (rolled) | Yes | Ch 1 | A traitor candidate |
| `role:librarian` | (rolled) | Yes | Ch 5 | Keeps the founding history; a traitor candidate; helps you train Kindling Bond if innocent |
| `role:lost_child` | (rolled) | Yes | Ch 0 | The girl in the next cell who gives you a red cord; the leader takes her chakra by force; she returns hollow in the Chunin arc; a bond (and your kindling) can bring her back on the ANBU branch or in the road to Hokage |
| `role:yugure_second` | (rolled) | Yes | Ch 16 | An ember user; names you Kagari at the finals; a lineage candidate; defects when they learn of the Hollow Crown |
| `role:yugure_blade` | (rolled) | Yes | Ch 14 | Yūgure's second's partner, an ink-and-dusk swordsman; your recurring duel |
| `role:yugure_leader` | (rolled) Kagari | Yes | Ch 0 (the watching figure) | The last survivor of the Kagari, the leader of Yūgure |
| `role:sensei` | (rolled) | Classic: yes; Varied: rolled | Ch 0 | Rescues you, trains you, suspects what you are, becomes the Seventh Hokage; a lineage candidate's teammate |
| `role:instructor`, `role:medic` | (rolled) | Classic: yes; Varied: rolled | Ch 0 | Mentors; the medic is a traitor candidate |
| `role:teammate_a`, `role:teammate_b` | (rolled) | Classic: yes; Varied: rolled | Ch 1 | Your squad; *teammate_b*'s choice after the stranger (Ch 13) decides whether they stay, leave, or nearly join Yūgure in the Chunin arc |
| `role:rival` | (rolled) | Classic: yes; Varied: rolled | Ch 1 | Rival to ally; fights beside you in the war |
| `role:merchant` | (rolled) | Classic: yes; Varied: rolled | Ch 11 | Keeps hiring the squad; a traitor candidate, otherwise a dupe turned informant |

## The arcs

| Stretch | Arc | Hours | Major beats | Status |
|---|---|---|---|---|
| Academy | **Cinders** | ~4 | The rescue; the apartment; the flare; the sinking sun on your door; the missing page; the first traitor clues; graduation | Beta 1 |
| Genin | **Paper Trail** | ~8 | The squad and the bell test; tree and water walking; chakra paper in the merchant's cart; the empty bed in the border village; the stranger and *teammate_b*; "Yūgure" | Beta 2 |
| Chunin Exams | **Dusk over the Stadium** | ~3 | The written test; the forest and the false team; the tower; the attack; "Kagari"; the Fourth's fate; the Fifth named; promotion | Beta 3 |
| Chunin | **Embers** | ~13 | The first time skip: a year later, a teen. The Fifth's curfews and suspicion; B-rank missions on Yūgure's trail; the lost child's raid on a border post and the first real kindling; training Kindling Bond in secret; *teammate_b*'s choice pays off; the traitor's trail tightens; you can found a clan; a Yūgure strike sets a clan quarter against the Fifth, who steps down; the Sixth is named | Later |
| Jonin | **Ashes** | ~17 | Three years later, an adult and a Jonin. Your own Genin team; A-rank hunts for cells in far regions; the Sixth and the keeper open the archive with you: the purge revealed; the traitor unmasked (this save's candidate); the truth made public and the Kagari memorial; the Sixth resigns and the sensei becomes the Seventh; romance can lead to marriage | Later |
| ANBU (optional) | **Night Watch** | +~8 | Covert operations against Yūgure's cells; the Shimura storyline (a hidden faction that wants to use you as a weapon); the best path to bring the lost child home | Later |
| Road to Hokage | **The Last Bonfire** | ~15 | Restore the Kagari on their old land by the ruined shrine, or found your own clan; your lineage revealed (this save's candidate); Yūgure's second turns and leads you to the leader; the Last Bonfire is lit and shown to be the Hollow Crown; the leader offers you the dark mirror and you refuse; every bond in the village kindles into one watch-fire; the leader falls; the Seventh names you successor; your face as the Eighth | Later |

## Threads seeded in the beta

| Seed | Planted in | Flag | Pays off in |
|---|---|---|---|
| The lost child and the red cord | Ch 0 | `story.seed.lost_child_cord` | Chunin (she returns), ANBU or road to Hokage (she can come home); the cord is a key item |
| The ruined shrine in the hills | Ch 0 | `story.seed.ruined_shrine` | Road to Hokage: the old Kagari land, where you can restore the clan (one of the vacant estates) |
| The watching figure in a sinking-sun cloak | Ch 0, Ch 4 | `story.seed.watcher` | Road to Hokage: the leader |
| The keeper's long look | Ch 1, Ch 3 | `story.seed.keeper_noticed` | Jonin: the keeper, a false lead turned ally |
| The traitor clue trail (four candidates, one true) | Ch 0, 1, 3, 5, 11, 14 and side quests | `story.clue.<candidate>.<n>` | Jonin: the traitor |
| The Fourth's orphan stipend | Ch 1 | `story.seed.stipend` | Ch 19 to 20 (his fate) and Hokage: you can restore the stipend as the Eighth |
| The flare that takes a partner's nature | Ch 3 | `story.ch3.done` (with `story.seed.flare`) | Chunin: Kindling Bond awakens |
| The sealed door at the foot of the Rock | Ch 4 | `story.seed.sealed_door` | Jonin: the Second's archive |
| The missing page | Ch 5 | `story.seed.missing_page` | Jonin: the purge (and a traitor clue if the librarian is bound) |
| The blank space on the Rock | Ch 5 | `story.seed.blank_spots` | Every new Hokage, and the Eighth |
| The flicker at the bells | Ch 8 | `story.seed.bell_flicker` | Chunin: the first real kindling with a teammate |
| The chiselled names on the memorial stone | Ch 10 | `story.seed.chiselled_names` | Jonin: the Kagari memorial |
| Chakra paper in the merchant's cart | Ch 11 | `story.seed.cargo_found` | Chunin: Yūgure's testing network |
| The stranger and *teammate_b* | Ch 13 | `story.seed.teammate_approached` (and your choice) | Chunin: *teammate_b* stays, leaves or nearly joins Yūgure |
| The two shadows | Ch 14 | `story.ch14.done` | Chunin and Jonin duels with Yūgure's blade |
| The sensei's suspicion | Ch 14 | `story.seed.sensei_knows` | Chunin: the sensei trains your gift in secret; the fallen-shinobi lineage |
| The campfire leaning toward your squad | Ch 16 | `story.seed.campfire_leans` | Road to Hokage: every bond kindles into one watch-fire |
| Yūgure's second says "Kagari" | Ch 19 | `story.ch19.named` | Road to Hokage: they defect; the second's lineage |
| The Fourth's fate, the Fifth's hard line | Ch 19 to 20 | `world.hokage`, `twist.fourth_fate` | Chunin: the Fifth steps down |
## Beta 1: the opening and the Academy (~4 h)

About 2.8 hours of authored chapters and 1.2 hours of systemic play (lessons between chapters,
jobs, furnishing, adopting a pet, friends), over about 12 in-game days.

| Ch | Working title | Time | What happens | Teaches | Seeds |
|---|---|---|---|---|---|
| 0 | Cinders | 20 min | The creator screen. You wake in a cell of a Yūgure hideout in the hills, among other children. A girl in the next cell (*lost_child*) pushes a red cord through the bars before guards in ash-violet cloaks drag her away. You slip out and hide; the Leaf squad (*captain*, *instructor*, *medic*) raids the camp; a chase through the forest past a ruined shrine; the *medic* takes a sample of your chakra "for the records"; the *captain* carries you over a ravine; a cloaked figure with a sinking sun watches you go | Looking, sneaking, following, dodging, sprinting, climbing | The lost child and the red cord; the ruined shrine (old Kagari ground); the sinking sun; a traitor clue (medic) |
| 1 | A Key and a Bowl | 20 min | The gate at night, the Rock's four faces, the Fourth Hokage (*hokage_4*), the orphan's apartment and stipend, with papers the *elder_councillor* arranged personally. The *elder_keeper* watches you from the Hokage's side. Next morning: Ichiraku with the *instructor*, enrolment, the four classmates and the *rival* | The HUD, ryo, shops, the apartment, talking, VF friendship | The keeper's look; the Fourth's stipend; a traitor clue (councillor) |
| 2 | Forms | 20 min | First lessons: taijutsu forms and throwing at targets; a spar with the *rival* | Combo, heavy, dodge, block, practice kunai and shuriken | — |
| 3 | The Leaf on Your Brow | 25 min | The chakra lesson (a leaf stuck to your forehead) unlocks the chakra bar. In a paired chakra exercise your chakra flares and, for a moment, takes on your partner's nature: water beads on a scorched post. The *instructor* hushes it up; the *elder_keeper* is at the window; that evening the *medic* drops by "to check on you" | Chakra, meditation, hand signs (typed or radial) | `story.seed.flare`: Kindling Bond, foreshadowed; a traitor clue (medic) |
| 4 | Sinking Sun | 25 min | A sinking-sun mark scratched on your door at night. You chase a figure across the rooftops until it vanishes at the foot of the Rock, by a sealed stone door | Night, fatigue, roof running, the cost of staying up | The sealed door (the Second's archive); Yūgure inside the walls |
| 5 | The Missing Page | 15 min | A library chore for the *librarian*: the founding history has a page cut out, its edge fresh, and she is nervous. The *instructor*'s tour of the Rock: four faces, four blank spots, "one day yours, maybe" | Errands, the journal, inspecting | The missing page (the Kagari purge); the blank spots; a traitor clue (librarian) |
| 6 | Exam Eve | 20 min | A study night at a classmate's home: Transformation, Substitution and the Clone with your classmates; you dream of the girl in the next cell | Clone, Transformation, Substitution; bond quests | Classmates' families and ties; the lost child |
| 7 | Graduation | 25 min | The quiz, the throwing test and the clone test; the forehead protector; the Fourth's speech; the stipend ends | The exam flow, promotion | — |

## Beta 2: Genin life (~8 h)

About 4 hours of authored chapters and 4 hours of systemic play: about 12 board D-ranks (~2 h),
3 board C-ranks (~1.5 h), training and your clan's lesson (~0.5 h), over about 24 in-game days.

| Ch | Working title | Time | What happens | Teaches | Seeds |
|---|---|---|---|---|---|
| 8 | Three and a Bell | 35 min | Team assignment: *teammate_a*, *teammate_b* and you, under the *captain*, now your *sensei*. The bell test at Training Ground 3: you only pass if a teammate gets a bell too. As you and a teammate grab the bells together, a faint flame flickers between your hands | Squad commands, parry, teamwork | `story.seed.bell_flicker` |
| 9 | Small Jobs | 15 min | The Mission Desk; the squad's first D-rank; the board opens | Board missions, mission pay, failure on death | — |
| 10 | Climbing Trees | 25 min | Tree walking at Training Ground 3. By the memorial stone the *sensei* stops at a place where names were chiselled off | Tree walking, wall-running, chakra jump, roof hopping | The chiselled names (Kagari dead) |
| 11 | Paper Trail | 45 min | First story C-rank: escort the *merchant* east. Bandits on the road; a false floor in his cart hides chakra paper bound for the border; a campfire talk with *teammate_a* | Escort, defeat, inspect, camping, bond | `story.seed.cargo_found` (Yūgure's testing network); a traitor clue (merchant) |
| 12 | Still Water | 30 min | Water walking on the lake; the nature ceremony (choose your first nature); your clan's elder teaches the clan technique, or a friendly clan teaches a clanless player a lesser one | Water-walking, natures, the first elemental jutsu, the clan technique, the scroll shop | — |
| 13 | The Empty Bed | 45 min | The first far region: a border village whose orphan has vanished. The trail ends at an abandoned waystation marked with a sinking sun. Back home, a stranger approaches *teammate_b* | Travel, investigation, ninken tracking | `story.seed.teammate_approached` (a teammate's later choice) |
| 14 | Two Shadows | 50 min | Escorting the *merchant* again (he keeps slowing the squad down), a two-man team in ash-violet cloaks slips past. You capture their smuggler, who says one word, **Yūgure**, and carries a travel pass with the *elder_councillor*'s seal. The *sensei* starts to suspect what you are and recommends the squad for the Chunin Exams | Two-man cell enemies, smoke and paper bombs | `story.ch14.done`; the sensei's suspicion; traitor clues (merchant, councillor) |

## Beta 3: the Chunin Exams (~3 h)

About 2.5 hours authored and 0.5 hours systemic (the training break). The beta ends with the promotion, not a time skip. The exams are also a
calendar event that runs with NPC teams every season.

| Ch | Working title | Time | What happens | Teaches | Seeds |
|---|---|---|---|---|---|
| 15 | Ink | 20 min | The written test in an Academy hall: ten impossible questions; the real test is gathering answers unseen (Byakugan, Transformation, a clone in the rafters, a bribe in dialogue). A foreign team sits two rows ahead | Stealth objectives, choice | The foreign team |
| 16 | The Forest | 60 min | The Forest of Death: one scroll of a pair and five in-game days (nights at camp) to reach the tower with both. The foreign team is Yūgure in disguise and stalks you; an Uchiha player's Sharingan awakens in a moment of danger; on the night watch the campfire leans toward your squad | Survival, bedroll camping, On Duty, tree-hopping fights | *yugure_second* (a member of the foreign team); `story.seed.campfire_leans` |
| 17 | The Tower | 20 min | One-on-one preliminaries in the tower's arena | Duels, judged performance | — |
| 18 | One Month | 30 min | The training break, compressed to six days: the *sensei* teaches your exam reward technique; festival crowds and stalls | Systemic: training, crafting, side quests | — |
| 19 | Dusk over the Stadium | 40 min | The finals before the whole village. Yūgure attacks: smoke, fire, two-man cells in the stands. In the chaos *yugure_second* stops in front of you and says the name **Kagari**. The Fourth Hokage's fate (`twist.fourth_fate`): he falls, is crippled, or is taken | Defence, protect objectives, the cinematic camera | `story.ch19.named`; `world.hokage = 4 → 5` |
| 20 | Embers | 10 min | The funeral, the abdication or the empty seat (by `twist.fourth_fate`). The Fifth Hokage (*hokage_5*, Hyuga) is named. Promotion results (judged on how you fought). The squad's evening at Ichiraku, and the *sensei*'s warning that Yūgure will come again. End of the beta: you are still a child, and the time skip opens the Chunin arc later | Promotion | The Fifth's hard line |

## The squad bonding arc (spoilers)

Bond quests (`kind: bond`) carry the squad through the beta, gated by friendship:

| When | Bond beat |
|---|---|
| Beta 1, Ch 6 | Study night: you learn each classmate's family and what they want to become |
| Beta 1 | Two bond quests per classmate (for example *teammate_a*'s painting of the village from the Rock; *teammate_b*'s runaway pup) |
| Beta 2, Ch 8 | The bell test: pass together or not at all |
| Beta 2, Ch 11 | The campfire with *teammate_a* |
| Beta 2 | Two bond quests per teammate, and a squad dinner at the barbecue house after Ch 14 |
| Beta 2, Ch 13 | *teammate_b* and the stranger: tell the *sensei*, keep the secret, or follow them (a flag later arcs read) |
| Beta 3, Ch 16 | The night watch in the forest: each teammate's fear |
| Beta 3, Ch 19 | Your teammates cover you in the attack; low friendship changes who does |

## Spoilers behind the roadmap's neutral wording

| Roadmap says | The truth |
|---|---|
| The prologue's hideout | A Yūgure hideout; the guards wear ash-violet cloaks with a sinking sun |
| The ruined shrine in the prologue hills | The Kagari clan shrine where the leader hid as a child; the old Kagari land, later one of the vacant estates, where the player can restore the clan |
| The sealed door at the foot of the Rock | The Second Hokage's archive of the Kagari records |
| The memorial stone at Training Ground 3 | Names chiselled off: the Kagari dead |
| A story-unlocked clan option at the registry | Restoring the Kagari under their old name and crest, with Kindling Bond as the clan art |
| Kindling Bond, unlocked by a story moment after the beta | The Kagari gift; the dark mirror is taking chakra by force |
| Rotating story roles bound by the `twists` stream | `twist.traitor`, `twist.lineage`, `twist.fourth_fate` |
| The Chunin Exams finals | Yūgure attacks the stadium; *yugure_second* names you Kagari; the Fourth's fate; the Fifth named (`world.hokage = 5`) |
| The antagonist organization, its scouts and cells | Yūgure and its two-man cells |
| The Shimura clan home | Its cellar is the entrance to the hidden faction of the ANBU branch's story |

## Side quest secrets

Solutions, culprits and story ties for [SIDE_QUESTS.md](../../SIDE_QUESTS.md), keyed by quest id.
Side quests stay optional: none of these is required for the main path, but several plant or echo
its seeds.

### Filler arcs

| Quest | The truth |
|---|---|
| `filler.ramen_thief` | The thief is the old neighbour's cat from `district.b1.neighbours.3` and its whole litter, let in at night by the cook's own grandson, who feeds them because the fish stall closed. Catching the culprit means choosing: scold the boy, or get the stall reopened (which also finishes the neighbour's quest). Free ramen either way |
| `filler.lake_lanterns` | The ghost light is a retired Tobari lantern-keeper who walks the lake every night to tend a lantern for a son lost on a mission; the "ghost" moves because he water-walks. The finale is helping him set the lantern down for good. If `story.seed.flare` is set, the lantern's flame leans toward you as you pass (a Kindling Bond echo) |
| `filler.dogs_and_bugs` | Neither: the beetle crawled into the Kinoshita yard's timber and was built into a new shrine bench. Both clans were wrong, and laughing about it together is the finale (a large relation boost between the Inuzuka and Aburame) |
| `filler.silent_bell` | A swallow's nest inside the bell; the chicks fledge if you wait a week, or you can move the nest (the priest prefers waiting). A Tsuchigumo shrine-keeper knew all along and was testing whether you would listen |
| A Hundred Masks (later) | A Kurama apprentice's runaway illusion copies the faces of people the apprentice admires; yours among them |
| Snowbound (later) | Every traveller's secret is harmless except one: a courier carrying Yūgure's chakra paper, unaware of what it is |
| The Puppet Theatre (later) | The puppeteer's mute assistant is a gifted orphan with chakra strings; the theatre is hiding them from a recruiter (a Yūgure cell, if the Chunin arc is done) |
| The Forger's Ink (later) | The forgeries use the ink of the bound traitor candidate's household; if the bound candidate is innocent, the ink was stolen from them (a clue trail cameo, consistent with `twist.traitor`) |

### District quests and one-offs

| Quest | The truth |
|---|---|
| `district.b2.price_war` | Both tea houses buy from the same supplier, who sets them against each other to sell more; uniting them against him ends the war |
| `district.b2.ferryman` | The ferryman cannot swim; his last season is about teaching a child the river before he hangs up the pole. The new bridge is named after him if you finish it |
| `district.b2.night_shift` | One of the three patients is a Yūgure smuggler from Ch 11, injured and silent; the night ends with him slipping out. Sets `story.seed.night_patient` (pays off in the Chunin arc) |
| `district.b2.unbeatable_post` | The post is a sealed Uzumaki training post that hardens under chakra; it falls only to plain taijutsu with no chakra at all |
| `side.b2.pawned_scroll` | The scroll is real: a page of an old Academy textbook with the same cut as the missing page (Ch 5); the pawnbroker does not know who sold it. Sets `story.seed.second_page` |
| `side.b2.lost_letters` | One letter is addressed to a family that no longer exists in the census; returning it to the shrine sets `story.seed.unknown_family` (a quiet Kagari echo) |
| `side.b3.stall_thief` | A member of the disguised foreign team, testing the village's guards; you can catch them but not hold them |
| `side.b3.hospital_supplies` | Diverted by an exam official for a foreign team; if `twist.traitor` is the medic, the trail touches her too (a clue), otherwise it clears her name |
| `event.b3.betting_ring` | Run by the Hagane gate guards out of boredom; your odds improve if you finished `district.b2.contraband` |

### Clan lines

| Quest | The truth |
|---|---|
| `clan.kurama.3` | The missing painting shows the ruined shrine in the southern hills as it was before it burned; the Kurama hid it because a painter of their house was punished for making it |
| `clan.tsuchigumo.3` | The intruder at the sealed shrine room is a Yūgure scout looking for the clan's natural-energy seal |
| `clan.shimura.3` | The unexplained matter belongs to the hidden faction of the ANBU branch's story; helping opens that branch's first contact |
| `clan.tobari.3` | What moves on the wall unheard is a Yūgure cell using a sound-smothering technique learned from a Tobari deserter |
| `clan.hatake.4` | The keepsake's heir is the *sensei* if no Hatake lives in the save; otherwise the last Hatake |
| `clan.uzumaki.3` | The scattered Uzumaki is genuine, and a sealing expert who later helps restore a Kagari seal (Road to Hokage) |

## Bonds in the story (spoilers)

How the plot drives the bond engine ([BONDS.md](../../BONDS.md)), by role. Everything here is data:
quest actions and conditions on roles, never code.

| Beat | Role | Bond data |
|---|---|---|
| Ch 0, the rescue | *captain* (later *sensei*) | `bond_event saved_by_them` (a permanent moment: they carried you out) |
| Ch 0, the red cord | *lost_child* | A bond created at level 2 with `bond_flag red_cord`; it does not grow while she is gone (no contact) and is the hook for bringing her back |
| Ch 3, the flare | *teammate_a* (the paired exercise) | `bond_event trained_together`; the flare is flavor only, never a Kindling grant |
| Ch 6, a classmate confides | *teammate_b* | A choice: `kept_secret` or `broke_secret` (a permanent moment, or a quarrel) |
| Ch 8, the bells | *teammate_a*, *teammate_b* | `shared_moment bond.bells` for whoever grabs a bell with you |
| Ch 11, the campfire | *teammate_a* | Branch on `friendship [teammate_a, 5]`; `shared_moment` and `heart_to_heart` |
| Ch 13, the stranger and *teammate_b* | *teammate_b*, *sensei* | Tell the *sensei*: `went_over_their_head` with *teammate_b*, `kept_promise` with the *sensei*. Keep the secret: `kept_secret` with *teammate_b*, `story.seed.teammate_approached = "kept"`. Follow them: `stood_by_them` and a `reckless_charge` the *sensei* hears of. The Chunin arc reads the flag and `bond_meter [teammate_b, trust]`: at 60 or more they stay, under 30 they leave (`remove_from_squad story`), between they nearly join Yūgure and a return quest (`squad_can_return` is bypassed by `return_to_squad`) brings them home |
| Ch 14, the suspicion | *sensei* | The *sensei*'s trust gates the secret training of the Chunin arc: `bond_meter [sensei, trust, 50]` |
| Ch 16, the night watch | *teammate_a*, *teammate_b* | `shared_moment bond.night_watch` for teammates not quarrelling with you; the campfire leans toward the squad only if `squad_cohesion 50` |
| Ch 19, the attack | *teammate_a*, *teammate_b* | Whoever has the higher level covers you (`saved_by_them`); with both under 4, the *rival* does |
| Chunin arc, the first real kindling | the teammate who falls | The teammate with the highest level who is at 6 or more; if neither is, the *sensei*. Their nature is the one kindled; `set_flag story.kindling.awakened` |
| Chunin to Jonin, the traitor's trail | `twist.traitor` | The bound candidate's bond is never gated by the reveal: the player can be close to them. On the reveal, `start_conflict` with `broke_secret` for the bound candidate (a falling-out for most players); the innocent candidates get `shared_moment` scenes when their names are cleared |
| Road to Hokage, every bond kindles | everyone at level 6 or more | The final watch-fire counts bonds at 6+ (the village you befriended is the fire); `standing` Hero everywhere is the Hokage requirement |
| The lost child comes home | *lost_child* | Needs `friendship [lost_child, 2]` kept from Ch 0 and the ANBU or road-to-Hokage quest; her bond then starts growing |
| The finale's watch-fire | the whole village | The fire's size is `BondWeb.score`: every bond at 6 or more, deeper bonds worth more, and each clan, district and rank it reaches adds one. Thresholds (data, tuned in playtests): a small fire at 15 (the squad and a few friends), a strong one at 40, the whole village at 70. A thin web still wins the fight; a wide one changes the scene and the epilogue |
| The keeper becomes an ally | *elder_keeper* | `bond_meter [elder_keeper, trust, 60]` and `friendship [elder_keeper, 6]` open his archive quests; he starts wary (stern, private) so trust is earned through kept promises and kept secrets, not gifts |
| The librarian trains the gift, if innocent | *librarian* | Only when `twist.traitor` is not the librarian: `friendship [librarian, 7]` and `kindling_uses` on any bond of 6+ open her training line |
| The merchant turns informant, if innocent | *merchant* | Only when `twist.traitor` is not the merchant: `friendship [merchant, 6]` after the Ch 14 road, plus `standing ["district:market", "good_neighbor"]` |
| Traitor candidates and friendship | every `twist.traitor` candidate | **The bound answer never depends on friendship**: it is fixed by the `twists` stream at world creation. Friendship only changes how the clue trail plays (who confides in you, who lies to your face, who you can bring along). Innocent candidates the player is close to become allies when cleared (`shared_moment` plus a permanent `reconciled` if the player suspected them aloud) |
| The Ch 13 choice in the society | *teammate_b* | Keeping the secret plants no deed; telling the *sensei* is a `deed` the squad hears of (teammate_a learns it within days through the squad tie, so teammate_a's dialogue can react before the player tells them) |
