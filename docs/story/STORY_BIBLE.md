# Story bible

> **SPOILERS: for developers only.** This file holds every twist of the Shinobi Modpack's story:
> identities, betrayals, the antagonist's goal and leader, the player's lineage, deaths and falls,
> reveal pacing and the seeds that pay off later. If you want to play the game unspoiled, stop
> reading here. [ROADMAP.md](../../ROADMAP.md) is spoiler-free.

The whole ~60-hour story, laid out so the beta plants the right seeds and the data formats can hold
it. Only the beta's arcs are built now. All characters are original; named canon characters appear
only as cameos. Quests refer to characters by role ([ROADMAP.md, section 5](../../ROADMAP.md#5-data-formats-built-for-the-whole-story)):
the Classic cast binds the roles to the characters in the roadmap's Classic table, and Varied saves
roll them; the fixed characters below are the same in every save.

## Yūgure

**Yūgure** (夕暮れ, "Dusk") is a band of missing-nin from across the five nations. They work in
**two-man cells** and wear **ash-violet cloaks marked with a sinking sun**. Their creed: *the
shinobi world must end at dusk so that a true dawn can come.*

- **Origin.** About twenty years before the story, **Kagari Seiren**, the last survivor of the
  Kagari, gathered missing-nin whom the hidden villages had wronged: soldiers abandoned after wars,
  orphans used and discarded, clans broken by treaties. Each had a grievance; Seiren gave them a
  purpose.
- **Goal.** The **Last Bonfire**: the Kagari gift turned to force. Chakra torn from hundreds of
  captives is gathered into one fire that spreads through the hidden villages, so that none of them
  stands at dawn. It needs a Kagari bloodline as its wick. Orphans with unusual chakra are its fuel
  and its soldiers. You are the wick.
- **Method.** Cells smuggle chakra paper to test children for unusual chakra, buy and steal
  orphans, and plant agents in villages. Inside the Leaf they have one source: the elder.

## The Kagari

The **Kagari** (篝, "bonfire") were a Warring States clan whose chakra flared, gathered and spread
like flame. In the last war before the Leaf's founding a Kagari bonfire burned a valley with both
armies in it. When the Senju and the Uchiha made peace, the founding clans agreed the Kagari could
not be allowed to exist, and ended them. The Second Hokage sealed the records in an archive under
the Rock and had their names chiselled off the memorial stone; the Third knew and kept silent.
One child, Seiren, survived, hidden in the clan's shrine in the southern hills, the burnt shrine
the prologue's chase runs past.

The Kagari were feared for the dark side of their gift: a Kagari can take chakra by force. The
bonfire that burned the valley was chakra torn from both armies at once. That is what the founders
ended, and what Seiren has made of the clan's gift ([Kindling Bond](#kindling-bond)).

## Kindling Bond

*Decided.* The Kagari ability is **Kindling Bond** (篝火の縁).

- **What it does.** Kagari chakra resonates with the people a Kagari is bonded to. You can kindle a
  bonded ally's chakra nature or one of their techniques and borrow it briefly: a few casts of their
  nature's jutsu, or one use of their signature technique, after which the flame goes out and needs
  time to rekindle.
- **Bonds decide what you can borrow.** Each bonded character offers what they know. Deeper bonds
  unlock more: friendship level 6 lets you borrow their nature, level 8 one of their techniques,
  level 10 (or a teammate, your sensei, your spouse) both and longer. A spouse's bond is the
  strongest. This is one of the ways the player gains more elemental natures: a nature borrowed
  often enough through a bond can be learned for good with a master's trial.
- **How it looks.** A bond-flame, a small watch-fire (*Kagari-bi*), flickers between you and the
  ally whose chakra you borrow, and your chakra takes their nature's colour while it burns.
- **The dark mirror.** Taking chakra by force instead of borrowing it through a bond: no bond, no
  consent, and the victim is left hollow. It is how Seiren grew strong, why Akari came back empty,
  how the Last Bonfire burns, and why the founders feared the clan. The player can never use it;
  the story offers the temptation once, in the last arc.
- **In the systems.** Shinobi Combat adds a `kindle` effect type (borrow a nature or technique from
  a bonded character for a time); Shinobi Life's friendship and romance levels are its bond levels;
  Core's natures list gains a "borrowed" source; Progression unlocks it with a story flag
  (`story.kindling.awakened`).
- **In the beta: foreshadowing only.** Three flickers, none controllable:
  - Ch 3: in a paired chakra exercise your chakra flares and, for a moment, takes on your partner's
    nature (water beads on a scorched post); the instructor hushes it up.
  - Ch 8: when you and a teammate grab the bells together, a faint flame flickers between your
    hands. Nobody else sees it.
  - Ch 16: on the forest night watch, the campfire leans toward your squad when they are near you.
- **The first real kindling** is a big moment of the Chunin arc: during Akari's raid on the border
  post, a teammate falls protecting you and you kindle their nature to finish the fight. From then
  on it is a skill you train in secret with Fumiko and the sensei.

## You and Seiren

Seiren's daughter fled Yūgure to live quietly in a border town, and died when you were small.
Yūgure found you and took you to the hideout where the Leaf squad found you. **Seiren is your
grandparent**: the leader of Yūgure wants you back as heir and as wick. A clan-born player's other
parent was of that clan; a clanless player's Kagari blood is all they have. Later, the
player clan choice lets you restore the Kagari under their old name and crest, or
found a new clan.

## Reveal pacing

| By the end of | The player knows | The player suspects |
|---|---|---|
| Academy (beta) | Someone in a sinking-sun cloak took you and is watching you | Your chakra is strange; the elder knows something |
| Genin (beta) | The name **Yūgure**; it smuggles chakra paper and orphans | The sensei knows what you are |
| Chunin Exams (beta) | Yūgure attacked the Leaf; a Yūgure member called you **Kagari** | Kagari is a clan, and you are of it |
| Chunin | Yūgure's two-man cells and creed; Akari is one of them; your bond-flame is a Kagari gift, Kindling Bond | The Leaf erased the Kagari |
| Jonin | The Kagari purge, the Second's archive, the Third's silence; the elder is the traitor | Who leads Yūgure |
| Road to Hokage | Seiren is the last Kagari, your grandparent; the Last Bonfire is the gift turned to force, and it needs you | — |

## The Hokage line

Four faces are on the Rock when you arrive; three more are carved during the story; yours is the
Eighth. All are original characters with custom faces.

| # | Hokage | Era | What they left behind |
|---|---|---|---|
| 1 | **Senju Tsugumori**, the Founder | The founding | The wall, the founding charter (with its missing page), the memorial stone, and the agreement that ended the Kagari |
| 2 | **Uchiha Reiga**, the Builder | The first generation | The Academy, the ANBU, the Chunin Exams, and the sealed archive under the Rock with the chiselled names: the rule of silence |
| 3 | **Sarutobi Kaede**, the Long Peace | Thirty years of peace | The clan council, the Will of Fire lantern walk, and a letter in the archive "for whoever comes asking" |
| 4 | **Akimichi Gōzan**, the Kind One | Sitting when you arrive | The orphan's stipend that pays for your apartment; he dies defending the stadium in the Chunin Exam attack (the beta's Chunin Exams) |
| 5 | **Hyuga Sayo**, the Hard Line | Named at the end of the beta; the Chunin years | Border watch posts, curfews and a sensor corps; she distrusts your blood. She steps down when her hard line brings a clan quarter to the edge of revolt |
| 6 | **Yamanaka Ren**, the Listener | The Jonin years | Opens the archive with you, makes the Kagari purge public, raises a memorial to the Kagari, and resigns to take responsibility for the Leaf's buried crime |
| 7 | **The sensei** (`role:sensei`; Classic: Ōtori Kaname), the Bridge | The road to Hokage | The captain who rescued you leads the village through the war with Yūgure and names you successor |
| 8 | **You** | — | — |

## Recurring characters

| Character | Fixed or role | First appears | Through the story |
|---|---|---|---|
| **Akimichi Gōzan**, the Fourth Hokage | Fixed | Ch 1 | Warm, protective; his stipend is why you have a home; dies in Ch 19 |
| **Elder Mibu Tatsuhide** | Fixed | Ch 1 | His clan took part in the purge. Guilt turned into treason: he fed Yūgure the names of gifted orphans, believing Seiren only wanted the Kagari back, not the villages burned. Unmasked in the Jonin years |
| **Fumiko**, the Academy librarian | Fixed | Ch 5 | Keeps the cut page of the founding history; an ally who helps you train Kindling Bond in the Chunin years |
| **Akari**, the girl left behind | Fixed | Ch 0 | Seiren took her chakra by force; she returns in the Chunin years as a hollow Yūgure operative; a bond (and your kindling) can bring her back on the ANBU branch or in the road to Hokage |
| **Hotaru** | Fixed | Ch 16 | Yūgure, an ember user, Seiren's second; names you Kagari in Ch 19; doubts the Last Bonfire; defects in the road to Hokage and leads you to Seiren |
| **Usuzumi** | Fixed | Ch 14 (one of the two shadows) | Hotaru's partner, an ink-and-dusk swordsman; your recurring duel |
| **Kagari Seiren** | Fixed | Ch 0 (the watching figure) | The leader of Yūgure, your grandparent |
| The **sensei** | Role | Ch 0 | Rescues you, trains you, suspects what you are (Ch 14), becomes the Seventh Hokage |
| The **instructor** and **medic** | Roles | Ch 0 | Mentors through the whole story; the medic runs the hospital in the war |
| **teammate_a**, **teammate_b** | Roles | Ch 1 | Your squad; *teammate_b*'s choice after the stranger (Ch 13) decides whether they stay, leave, or nearly join Yūgure in the Chunin years |
| The **rival** | Role | Ch 1 | Rival to ally; fights beside you in the war |
| **Kenta**, the merchant | Role | Ch 11 | Keeps hiring the squad; an unwitting carrier for Yūgure's chakra paper, later an informant |

## The arcs

| Stretch | Arc | Hours | Major beats | Status |
|---|---|---|---|---|
| Academy | **Cinders** | ~4 | The rescue; the apartment; the flare; the sinking sun on your door; the missing page; graduation | Beta 1 |
| Genin | **Paper Trail** | ~8 | The squad and the bell test; tree and water walking; chakra paper in Kenta's cart; the empty bed in the border village; the stranger and *teammate_b*; "Yūgure" | Beta 2 |
| Chunin Exams | **Dusk over the Stadium** | ~3 | The written test; the forest and the false team; the tower; the attack; "Kagari"; the Fourth's fall; the Fifth; promotion | Beta 3 |
| Chunin | **Embers** | ~13 | Opens with the first time skip: a year later, a teen. The Fifth's curfews and suspicion; Akari returns in a raid on a border post and, when a teammate falls, the first real kindling (Kindling Bond awakens); you train it in secret with Fumiko and the sensei; B-rank missions on Yūgure's trail; *teammate_b*'s choice pays off; you can found a clan; a Yūgure strike sets a clan quarter against the Fifth, who steps down; the Sixth is named | Later |
| Jonin | **Ashes** | ~17 | Three years later, an adult and a Jonin. Your own Genin team; A-rank hunts for cells in far regions; the Sixth opens the archive with you: the Third's letter and the missing page reveal the Kagari purge; Elder Mibu is unmasked as the traitor; the truth is made public and the Kagari get a memorial; the Sixth resigns and the sensei becomes the Seventh; romance can lead to marriage | Later |
| ANBU (optional) | **Night Watch** | +~8 | Masks and covert operations against Yūgure's cells; the Shimura storyline (a hidden faction that wants to use you as a weapon); the best path to bring Akari home | Later |
| Road to Hokage | **The Last Bonfire** | ~15 | Restore the Kagari on their old land by the burnt shrine, or found your own clan; Hotaru defects and leads you to Seiren, your grandparent; Yūgure lights the Last Bonfire at the Leaf; Seiren offers you the dark mirror and you refuse; every bond you built in the village kindles into one watch-fire against the Bonfire; you face Seiren; the Seventh names you successor; the inauguration and your face as the Eighth | Later |

## Threads seeded in the beta

Every thread the beta plants, the flag that records it (declared in `story/seeds.json`), and where
it pays off.

| Seed | Planted in | Flag | Pays off in |
|---|---|---|---|
| Akari and the red cord | Ch 0 | `story.seed.akari_cord` | Chunin (she returns), ANBU or road to Hokage (she can come home); the cord is a key item |
| The burnt shrine in the hills | Ch 0 | `story.seed.burnt_shrine` | Road to Hokage: the old Kagari land, where you can restore the clan (one of the vacant estates) |
| The watching figure in a sinking-sun cloak | Ch 0, Ch 4 | `story.seed.watcher` | Road to Hokage: it was Seiren |
| The elder's long look | Ch 1, Ch 3 | `story.seed.elder_noticed` | Jonin: the traitor |
| The Fourth's orphan stipend | Ch 1 | `story.seed.stipend` | Ch 19 (his fall) and Hokage: you can restore the stipend as the Eighth |
| The flare that takes a partner's nature | Ch 3 | `story.ch3.flare_seen` | Chunin: Kindling Bond awakens |
| The flicker between you and a teammate at the bells | Ch 8 | `story.seed.bell_flicker` | Chunin: the first real kindling with a teammate |
| The campfire leaning toward your squad | Ch 16 | `story.seed.campfire_leans` | Road to Hokage: every bond kindles into one watch-fire |
| The sealed door at the foot of the Rock | Ch 4 | `story.seed.sealed_door` | Jonin: the Second's archive |
| The missing page | Ch 5 | `story.seed.missing_page` | Jonin: the Kagari purge |
| The blank spots on the Rock | Ch 5 | `story.seed.blank_spots` | Every new Hokage, and the Eighth |
| The chiselled names on the memorial stone | Ch 10 | `story.seed.chiselled_names` | Jonin: the Kagari memorial |
| Chakra paper in Kenta's cart | Ch 11 | `story.seed.chakra_paper` | Chunin: Yūgure's testing network; Kenta as informant |
| The stranger and *teammate_b* | Ch 13 | `story.seed.teammate_approached` (and your choice) | Chunin: *teammate_b* stays, leaves or nearly joins Yūgure |
| The two shadows (Usuzumi and partner) | Ch 14 | `story.ch14.yugure_named` | Chunin and Jonin duels with Usuzumi |
| The sensei's suspicion | Ch 14 | `story.seed.sensei_knows` | Chunin: the sensei trains your fire in secret |
| Hotaru says "Kagari" | Ch 19 | `story.ch19.kagari_named` | Road to Hokage: Hotaru defects |
| The Fourth's fall, the Fifth's hard line | Ch 19 to 20 | `world.hokage` | Chunin: the Fifth steps down |

## Beta 1: the opening and the Academy (~4 h)

About 2.8 hours of authored chapters and 1.2 hours of systemic play (lessons between chapters,
jobs, furnishing, adopting a pet, friends), over about 12 in-game days.

| Ch | Title | Time | What happens | Teaches | Seeds |
|---|---|---|---|---|---|
| 0 | Cinders | 20 min | The creator screen. You wake in a cell of a Yūgure hideout in the hills, among other children. A girl in the next cell, **Akari**, pushes a red cord through the bars before guards in ash-violet cloaks drag her away. You slip out and hide; the Leaf squad (*captain*, *instructor*, *medic*) raids the camp; a chase through the forest past a burnt shrine; the *captain* carries you over a ravine; a cloaked figure with a sinking sun watches you go | Looking, sneaking, following, dodging, sprinting, climbing | Akari and the red cord; the burnt shrine (old Kagari ground); the sinking sun |
| 1 | A Key and a Bowl | 20 min | The gate at night, the Rock's four faces, the Fourth Hokage **Akimichi Gōzan**, the orphan's apartment and stipend. **Elder Mibu Tatsuhide** watches from the Hokage's side. Next morning: Ichiraku with the *instructor*, enrolment, the four classmates and the *rival* | The HUD, ryo, shops, the apartment, talking, VF friendship | The elder's look; the Fourth's orphan stipend (his legacy) |
| 2 | Forms | 20 min | First lessons: taijutsu forms and throwing at targets; a spar with the *rival* | Combo, heavy, dodge, block, practice kunai and shuriken | — |
| 3 | The Leaf on Your Brow | 25 min | The chakra lesson (a leaf stuck to your forehead) unlocks the chakra bar. In a paired chakra exercise your chakra flares and, for a moment, takes on your partner's nature: water beads on a scorched post. The *instructor* hushes it up; the elder is at the window | Chakra, meditation, hand signs (typed or radial) | `story.ch3.flare_seen`: Kindling Bond, foreshadowed |
| 4 | Sinking Sun | 25 min | A sinking-sun mark scratched on your door at night. You chase a figure across the rooftops until it vanishes at the foot of the Rock, by a sealed stone door | Night, fatigue, roof running, the cost of staying up | The sealed door (the Second's archive); Yūgure inside the walls |
| 5 | The Missing Page | 15 min | A library chore for **Fumiko** the librarian: the founding history has a page cut out. The *instructor*'s tour of the Rock: four faces, four blank spots, "one day yours, maybe" | Errands, the journal, inspecting | The missing page (the Kagari purge); the blank spots |
| 6 | Exam Eve | 20 min | A study night at a classmate's home: Transformation, Substitution and the Clone with your classmates; you dream of Akari | Clone, Transformation, Substitution; bond quests | Classmates' families and ties; Akari |
| 7 | Graduation | 25 min | The quiz, the throwing test and the clone test; the forehead protector; the Fourth's speech; the stipend ends | The exam flow, promotion | — |

## Beta 2: Genin life (~8 h)

About 4 hours of authored chapters and 4 hours of systemic play: about 12 board D-ranks (~2 h),
3 board C-ranks (~1.5 h), training and your clan's lesson (~0.5 h), over about 24 in-game days.

| Ch | Title | Time | What happens | Teaches | Seeds |
|---|---|---|---|---|---|
| 8 | Three and a Bell | 35 min | Team assignment: *teammate_a*, *teammate_b* and you, under the *captain*, now your *sensei*. The bell test at Training Ground 3: you only pass if a teammate gets a bell too. As you and a teammate grab the bells together, a faint flame flickers between your hands | Squad commands, parry, teamwork | `story.seed.bell_flicker` |
| 9 | Small Jobs | 15 min | The Mission Desk; the squad's first D-rank; the board opens | Board missions, mission pay, failure on death | — |
| 10 | Climbing Trees | 25 min | Tree walking at Training Ground 3. By the memorial stone the *sensei* stops at a place where names were chiselled off | Tree walking, wall-running, chakra jump, roof hopping | The chiselled names (Kagari dead) |
| 11 | Paper Trail | 45 min | First story C-rank: escort the merchant **Kenta** east. Bandits on the road; a false floor in his cart hides chakra paper bound for the border; a campfire talk with *teammate_a* | Escort, defeat, inspect, camping, bond | `story.seed.chakra_paper` (Yūgure's testing network) |
| 12 | Still Water | 30 min | Water walking on the lake; the nature ceremony (choose your first nature); your clan's elder teaches the clan technique, or a friendly clan teaches a clanless player a lesser one | Water-walking, natures, the first elemental jutsu, the clan technique, the scroll shop | — |
| 13 | The Empty Bed | 45 min | The first far region: a border village whose orphan has vanished. The trail ends at an abandoned waystation marked with a sinking sun. Back home, a stranger approaches *teammate_b* | Travel, investigation, ninken tracking | `story.seed.teammate_approached` (a teammate's later choice) |
| 14 | Two Shadows | 50 min | Escorting Kenta again, a two-man team in ash-violet cloaks slips past the squad. You capture their smuggler, who says one word: **Yūgure**. The *sensei* starts to suspect what you are and recommends the squad for the Chunin Exams | Two-man cell enemies, smoke and paper bombs | `story.ch14.yugure_named`; the sensei's suspicion |

## Beta 3: the Chunin Exams (~3 h)

About 2.5 hours authored and 0.5 hours systemic (the training break). The beta ends with the promotion, not a time skip. The exams are also a
calendar event that runs with NPC teams every season.

| Ch | Title | Time | What happens | Teaches | Seeds |
|---|---|---|---|---|---|
| 15 | Ink | 20 min | The written test in an Academy hall: ten impossible questions; the real test is gathering answers unseen (Byakugan, Transformation, a clone in the rafters, a bribe in dialogue). A foreign team sits two rows ahead | Stealth objectives, choice | The foreign team |
| 16 | The Forest | 60 min | The Forest of Death: one scroll of a pair and five in-game days (nights at camp) to reach the tower with both. The foreign team is Yūgure in disguise and stalks you; an Uchiha player's Sharingan awakens in a moment of danger; on the night watch the campfire leans toward your squad | Survival, bedroll camping, On Duty, tree-hopping fights | Hotaru (a member of the foreign team); `story.seed.campfire_leans` |
| 17 | The Tower | 20 min | One-on-one preliminaries in the tower's arena | Duels, judged performance | — |
| 18 | One Month | 30 min | The training break, compressed to six days: the *sensei* teaches your exam reward technique; festival crowds and stalls | Systemic: training, crafting, side quests | — |
| 19 | Dusk over the Stadium | 40 min | The finals before the whole village. Yūgure attacks: smoke, fire, two-man cells in the stands. In the chaos **Hotaru** stops in front of you and says the name **Kagari**. The Fourth Hokage falls defending the stadium | Defence, protect objectives, the cinematic camera | `story.ch19.kagari_named`; `world.hokage = 4 → 5` |
| 20 | Embers | 10 min | The funeral. **Hyuga Sayo** is named the Fifth Hokage. Promotion results (judged on how you fought). The squad's evening at Ichiraku, and the *sensei*'s warning that Yūgure will come again. End of the beta: you are still a child, and the time skip opens the Chunin arc later | Promotion | The Fifth's hard line |

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
| The burnt shrine in the prologue hills | The Kagari clan shrine where Seiren hid as a child; the old Kagari land, later one of the vacant estates, where the player can restore the clan |
| The sealed door at the foot of the Rock | The Second Hokage's archive of the Kagari records |
| The memorial stone at Training Ground 3 | Names chiselled off: the Kagari dead |
| A story-unlocked clan option at the registry | Restoring the Kagari under their old name and crest, with Kindling Bond as the clan art |
| Kindling Bond, unlocked by a story moment after the beta | The Kagari gift; the dark mirror is taking chakra by force |
| The Chunin Exams finals | Yūgure attacks the stadium; Hotaru names you Kagari; the Fourth Hokage falls; Hyuga Sayo is named the Fifth (`world.hokage = 5`, her face carved after the beta) |
| The antagonist organization, its scouts and cells | Yūgure and its two-man cells |
| The Shimura clan home's cellar | The entrance to the hidden faction of the ANBU branch's story |
| Rare milestones for the fourth and fifth natures | Kindling Bond borrowing, and the Hokage's archive |
