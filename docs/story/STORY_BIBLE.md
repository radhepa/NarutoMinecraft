# Story bible

> **SPOILERS: for developers only.** This folder holds every twist of the Shinobi Modpack's story:
> identities, betrayals, the antagonist's goal and leader, the player's lineage, deaths and falls,
> reveal pacing and the seeds that pay off later. If you want to play the game unspoiled, stop
> reading here. [ROADMAP.md](../../ROADMAP.md) is spoiler-free.

The whole ~60-hour story, from a child in a cell to the Eighth Hokage. This file is the index and
holds the twist slots; the story itself is in the files below. All characters are original; named
canon characters appear only as cameos.

## The files

| File | What it holds |
|---|---|
| [WORLD.md](WORLD.md) | Conventions (roles, tokens, pronouns), the theme, the chronology before Y0, the Kagari, Yūgure and the Hollow Crown, the story rules of Kindling Bond, new places, tone |
| [ROTATIONS.md](ROTATIONS.md) | The three twist slots in full: every candidate's clue trail, innocent explanations, decisive evidence, reveals and fairness checks |
| [ARCS/1_cinders.md](ARCS/1_cinders.md) | The Academy, Ch 0 to 7 (Beta 1) |
| [ARCS/2_paper_trail.md](ARCS/2_paper_trail.md) | Genin, Ch 8 to 14 (Beta 2) |
| [ARCS/3_dusk_over_the_stadium.md](ARCS/3_dusk_over_the_stadium.md) | The Chunin Exams, Ch 15 to 20 (Beta 3) |
| [ARCS/4_embers.md](ARCS/4_embers.md) | Chunin, Ch 21 to 32 |
| [ARCS/5_ashes.md](ARCS/5_ashes.md) | Jonin, Ch 33 to 45 |
| [ARCS/6_night_watch.md](ARCS/6_night_watch.md) | ANBU branch (optional), N1 to N7 |
| [ARCS/7_last_bonfire.md](ARCS/7_last_bonfire.md) | Road to Hokage, Ch 46 to 55, and the epilogue |
| [ENSEMBLE.md](ENSEMBLE.md) | The class as four squads, the senior squad and five senseis: tiers, wants, flaws and where each moves the plot |
| [CHARACTERS/](CHARACTERS/) | One file per recurring character: arc, knowledge over time, endings, and their dialogue brief |
| [DIALOGUE_BRIEFS.md](DIALOGUE_BRIEFS.md) | Rules for every line, global spoiler gates, the questions characters ask the player |
| [SYSTEMS.md](SYSTEMS.md) | How the story uses missions, side quests, bonds, clans and combat; requests to each system |
| [FLAGS.md](FLAGS.md) | Every story flag: where it is set and read; the seeds table |
| [REVIEW_LOG.md](REVIEW_LOG.md) | The review rounds that locked the story |

## How to read this bible

- **Names are rolled per save, in Classic and Varied alike.** Every character is written as a role
  (`role:librarian`, `role:yugure_leader`). A save rolls each character's given name from the
  seeded name pools and their family name from their clan (a clan character keeps the clan's name)
  or from the `family_names` pool in `tools/wardrobe/population.json`. Looks, personalities and
  roles stay as designed.
- **The Hokage's names are rolled too; their looks are not.** Faces on the Rock, portraits and
  statues are baked into the map, so each Hokage's appearance, clan and era are fixed.
- **Some twists rotate per save** (below). All candidates' clues are authored; the bound
  candidate's clues are true, the others' have innocent explanations.
- **All text uses tokens** (`{name:role:sensei}`, `{hokage:4}`, `{twist:traitor}`), never a literal
  name; pronouns of rolled-look roles are tokens too ([WORLD.md](WORLD.md#conventions)).

## Keys read by tools

Lines other sessions' checkers parse. Keep the key names stable.

- **creator.reserved_family_names**: Kagari

## Twist slots

| Slot | Candidates | Bound at | Revealed |
|---|---|---|---|
| `twist.traitor` (the voice inside the Leaf that feeds Yūgure) | 4: the librarian, the medic, the councillor, the merchant | World creation | Diverges from Ch 25; solvable at the case board (Ch 38); revealed Ch 39 |
| `twist.lineage` (whose child you are) | 2: Yūgure's second is your mother; the sensei's fallen teammate was your parent | World creation | A hint in Ch 25; the truth in Ch 48 |
| `twist.fourth_fate` (what the finals' attack costs the Fourth Hokage) | 3: he falls; he is crippled and abdicates; he is taken by Yūgure | World creation | Ch 19 to 21 |

Fixed in every save: **the hand** inside the Leaf is the porter; the keeper is a red herring and
never the voice; the leader is never your relative. Details: [ROTATIONS.md](ROTATIONS.md).

## The story in one page

An orphan known only as **Nine** wakes in a cell of a Yūgure nursery. A girl in the next cell pushes
a red cord through the bars before she is dragged away. The Leaf raids the camp (on a map someone in
Yūgure sent them); a quiet Jonin carries the child out; the Fourth Hokage gives them a stipend, a
flat and a bowl of ramen.

The Academy and the Genin years are a life: classmates, a squad, a sensei, missions, a pet. Under
them, small wrong things: a medic who records a chakra sample, a flare that takes on a partner's
nature, a sinking sun scratched on a door, a cut page in the library, chakra paper that chars
violet in the player's hand, a stranger who tells a teammate their lost parent is alive, two
shadows with soot-marked wrists and one word, **Yūgure**. At the Chunin Exams Yūgure attacks the
stadium at the opening lantern-lighting, before a single bout is fought; a burning woman, one of a
foreign team's adult escorts, stops in front of the player and says **"Kagari"**; the Fourth falls, is
crippled or is taken; the Fifth, a hard Hyuga, distrusts the player's blood.

As a Chunin the player's gift wakes: at a burning border post, the hollowed girl from the next cell
attacks, a teammate falls protecting the player, and their fire answers. The gift has an old name,
Kindling. Someone inside the Leaf is feeding Yūgure; the player catches the hand (the kind porter)
but not the voice. Fear of unusual chakra breaks the Fifth.

As a Jonin the player opens the archive under the Rock with the keeper and the Sixth: the Kagari
were invited to found the Leaf and were ended instead, their twenty-seven children renamed and
scattered through the village. The player solves who the voice is, makes the truth public, and
sees their own sensei become the Seventh. Optionally, as ANBU, they stop the Leaf's own shadow from
using the hollowed girl as a weapon, and bring her home by giving her their flame.

On the road to Hokage the player restores the Kagari (or founds a clan), learns whose child they
are, and learns Yūgure's real goal: not the Last Bonfire of the creed but the **Hollow Crown**, the
whole Leaf's chakra forced through the player as a wick and taken by the leader, the last Kagari
child of the purge, ageless on stolen chakra. On the Rock, offered the dark mirror, the player
refuses; every bond they made kindles toward them by choice, first the red cord; a fire given
freely cannot be taken, and the leader's own mirror turns on him. The Seventh names the player
successor. Their face is carved as the Eighth, and their first act extends the Fourth's stipend to
every child brought home and makes it law.

## Reveal pacing

| By the end of | The player knows | The player suspects |
|---|---|---|
| Academy (beta) | Someone who marks doors with a sinking sun took you and is watching you | Your chakra is strange; the keeper knows something; someone cut a page |
| Genin (beta) | The name **Yūgure**; it smuggles chakra paper and orphans; the paper chars near you | The sensei knows what you are; someone in the Leaf helps them |
| Chunin Exams (beta) | Yūgure attacked the Leaf; a woman of theirs called you **Kagari** | Kagari is a clan, and you are of it |
| Chunin | Your gift is Kindling (you see bonds as threads and can kindle a friend past their limits), a Kagari gift; the paper hunts your bloodline; the porter was the hand; there is a voice; teammate_b's parent is with Yūgure; the charm half is a parent's pair | The Leaf erased the Kagari; who the voice is (an attentive player knows) |
| Jonin | The Quiet Ending, the archive, the twenty-seven, the Third's silence; who the voice is | Yūgure wants something worse than the creed |
| Road to Hokage | Your lineage; the Hollow Crown, and that you are its wick | — |

## The Hokage line

Looks, clans and eras are fixed (baked into the map); given names are rolled per save. Faces one to
four are on the Rock at the start; the Fifth and Sixth are fixed carvings placed at story beats
(Ch 32, Ch 42); the Seventh's and your Eighth's faces are built from your sensei's and your looks.

| # | Clan | Look (fixed) | Era | What they left behind |
|---|---|---|---|---|
| 1 | Senju | Broad, long dark hair, a calm founder's face | The founding | The charter with its fourth clause, the memorial stone |
| 2 | Uchiha | Lean, sharp-featured, a high collar | The first generation | The Academy, the ANBU, the Chunin Exams; the Quiet Ending, the sealed archive and the chiselled names |
| 3 | Sarutobi | A woman with a long braid and a kind, lined face | Thirty years of peace | The clan council, the Will of Fire lantern walk, the keeper's oath, and a letter in the archive "for whoever comes asking" |
| 4 | Akimichi | A big, warm man with a broad smile | Sitting when you arrive | The orphan's stipend (it runs the whole game; the Eighth extends it and makes it law); his fate at the finals is `twist.fourth_fate` |
| 5 | Hyuga | A severe woman, pale eyes, hair tied high | After the finals; the Chunin years | Curfews and a sensor corps; steps down after the Tobari crisis (Ch 31) |
| 6 | Yamanaka | A soft-spoken man with long pale hair | The Jonin years | Opens the archive, makes the Quiet Ending public, raises the Kagari memorial, resigns (Ch 42) |
| 7 | The sensei | The sensei's own look | The road to Hokage | Leads the Leaf through the war with Yūgure; names you successor |
| 8 | You | Your look | — | — |

## Recurring characters

| Role | Fixed look | First appears | Through the story | File |
|---|---|---|---|---|
| `captain` / `sensei` | Classic: yes; Varied: rolled | Ch 0 | Rescues you, trains you, suspects what you are, becomes the Seventh | [sensei](CHARACTERS/sensei.md) |
| `instructor` | Classic: yes; Varied: rolled | Ch 0 | Your Academy teacher; believes in everyone; holds the Academy in the war | [instructor](CHARACTERS/instructor.md) |
| `medic` | Classic: yes; Varied: rolled | Ch 0 | A traitor candidate | [medic](CHARACTERS/medic.md) |
| `hokage_4` | Yes (man) | Ch 1 | The stipend; his fate rotates | [hokage_4](CHARACTERS/hokage_4.md) |
| `elder_keeper` | Yes (man) | Ch 1 | Keeper of the archive; a red herring; an ally; dies at the door (Ch 51b) | [elder_keeper](CHARACTERS/elder_keeper.md) |
| `elder_councillor` | Yes (man, Senju) | Ch 1 | A traitor candidate | [elder_councillor](CHARACTERS/elder_councillor.md) |
| `porter` | Yes (young man) | Ch 1 | The hand, in every save; caught Ch 28 | [porter](CHARACTERS/porter.md) |
| `librarian` | Yes (woman) | Ch 5 | A Kagari descendant; a traitor candidate; if innocent, trains the gift | [librarian](CHARACTERS/librarian.md) |
| `teammate_a`, `teammate_b` | Classic: yes; Varied: rolled | Ch 1 | Your squad | [a](CHARACTERS/teammate_a.md), [b](CHARACTERS/teammate_b.md) |
| `classmate_c`, `classmate_d` | Classic: yes; Varied: rolled | Ch 1 | The rival's squad; the memorial's carvers; your guard | [classmates](CHARACTERS/classmates.md) |
| `rival` | Classic: yes; Varied: rolled | Ch 1 | Rival to ally; offers their flame at the end | [rival](CHARACTERS/rival.md) |
| `merchant` | Classic: yes; Varied: rolled | Ch 11 | A traitor candidate | [merchant](CHARACTERS/merchant.md) |
| `lost_child` | Yes (girl) | Ch 0 | The girl in the next cell; hollowed; comes home | [lost_child](CHARACTERS/lost_child.md) |
| `yugure_second` | Yes (woman) | Ch 13 (the stranger), Ch 16 | An ember user; names you Kagari; a lineage candidate; defects | [yugure_second](CHARACTERS/yugure_second.md) |
| `yugure_blade` | Yes (man) | Ch 14 | Her partner, an ink-and-dusk swordsman; your recurring duel; turns in Ch 51b, fights beside you on the Rock, lives in custody | [yugure_blade](CHARACTERS/yugure_blade.md) |
| `yugure_leader` | Yes (man) | Ch 0 (the watcher) | The last Kagari child of the purge | [yugure_leader](CHARACTERS/yugure_leader.md) |
| `hokage_5`, `hokage_6` | Yes | Ch 20, Ch 32 | The hard line; the truth told | [5](CHARACTERS/hokage_5.md), [6](CHARACTERS/hokage_6.md) |
| `fallen_parent` | No look (memory only) | Ch 10 (a name) | The sensei's teammate; a lineage candidate | [fallen_parent](CHARACTERS/fallen_parent.md) |
| The ensemble: `sensei_2..5`, `squad3_*`, `squad4_*`, `squad5_*` | Mixed | Ch 1 to 8 | Four squads of your class, a senior squad and their senseis ([ENSEMBLE.md](ENSEMBLE.md)) | [senseis](CHARACTERS/senseis.md), [squad3](CHARACTERS/squad3.md), [squad4](CHARACTERS/squad4.md), [squad5](CHARACTERS/squad5.md) |
| Minor: `ramen_cook`, `undercroft_head`, `anbu_captain`, `genin_1..3`, `yugure_b_parent`, `foreign_genin`, `elder_hyuga` | Mixed | Various | — | [minor](CHARACTERS/minor.md) |

## The arcs

| Stretch | Arc | Chapters | Hours | Status |
|---|---|---|---|---|
| Academy | **Cinders** | 0 to 7 | ~4 | Beta 1 |
| Genin | **Paper Trail** | 8 to 14 | ~8 | Beta 2 |
| Chunin Exams | **Dusk over the Stadium** | 15 to 20 | ~3 | Beta 3 |
| Chunin | **Embers** | 21 to 32 | ~13 | Later |
| Jonin | **Ashes** | 33 to 45 | ~17 | Later |
| ANBU (optional) | **Night Watch** | N1 to N7 | +~8 | Later |
| Road to Hokage | **The Last Bonfire** | 46 to 55 | ~15 | Later |

## Spoilers behind the roadmap's neutral wording

| Roadmap says | The truth |
|---|---|
| The prologue's hideout | A Yūgure nursery; the guards wear road clothes with a sinking sun drawn in soot inside the wrist, and ash-violet scarves |
| The ruined shrine in the prologue hills | The Kagari clan shrine, burned in the Quiet Ending; the old Kagari land, where the player can restore the clan |
| The sealed door at the foot of the Rock | The archive of the Quiet Ending, with the Hearthstone |
| The memorial stone at Training Ground 3 | Names chiselled off: the Kagari dead |
| A story-unlocked clan option at the registry | Restoring the Kagari under their old name and crest, with Kindling Bond as the clan art |
| Kindling Bond, unlocked by a story moment after the beta | The Kagari gift; the dark mirror is taking chakra by force |
| Rotating story roles bound by the `twists` stream | `twist.traitor`, `twist.lineage`, `twist.fourth_fate` |
| The Chunin Exams finals | Yūgure attacks the stadium; the second names you Kagari; the Fourth's fate; the Fifth named |
| The antagonist organization, its scouts and cells | Yūgure and its hearths (cells of three or more, each tied to a nursery) |
| The Shimura clan home | A stranger has been using its cellar as a mail drop; the trail leads to the Undercroft, the heirs of the sealing team of the Quiet Ending, in a derelict sealing hall under the old quarry (the ANBU branch) |

## Side quest secrets

Solutions, culprits and story ties for [SIDE_QUESTS.md](../../SIDE_QUESTS.md), keyed by quest id.
Side quests stay optional; several plant or echo the main path's seeds ([SYSTEMS.md](SYSTEMS.md) §2).

### Filler arcs

| Quest | The truth |
|---|---|
| `filler.ramen_thief` | The thief is the old neighbour's cat from `district.b1.neighbours.3` and its whole litter, let in at night by the cook's own grandson, who feeds them because the fish stall closed. Catching the culprit means choosing: scold the boy, or get the stall reopened (which also finishes the neighbour's quest). Free ramen either way |
| `filler.lake_lanterns` | The ghost light is a retired Tobari lantern-keeper who walks the lake every night to tend a lantern for a son lost on a mission; the "ghost" moves because he water-walks. The finale is helping him set the lantern down for good. If `story.seed.flare` is set, the lantern's flame leans toward you as you pass |
| `filler.dogs_and_bugs` | Neither: the beetle crawled into the Kinoshita yard's timber and was built into a new shrine bench. Both clans were wrong, and laughing about it together is the finale (a large relation boost between the Inuzuka and Aburame) |
| `filler.silent_bell` | A swallow's nest inside the bell; the chicks fledge if you wait a week, or you can move the nest (the priest prefers waiting). A Tsuchigumo shrine-keeper knew all along and was testing whether you would listen |
| A Hundred Masks (later) | A Kurama apprentice's runaway illusion copies the faces of people the apprentice admires; yours among them |
| Snowbound (later) | Every traveller's secret is harmless except one: a courier carrying Yūgure's chakra paper, unaware of what it is |
| The Puppet Theatre (later) | The puppeteer's mute assistant is a gifted orphan with chakra strings; the theatre is hiding them from a Yūgure recruiter |
| The Forger's Ink (later) | Opens only after `story.ch39.done`. The forgeries use the ink of the voice's household (consistent with `twist.traitor`); the quest closes the voice's last channel |

### District quests and one-offs

| Quest | The truth |
|---|---|
| `district.b2.price_war` | Both tea houses buy from the same supplier, who sets them against each other to sell more; uniting them against him ends the war |
| `district.b2.ferryman` | The ferryman cannot swim; his last season is about teaching a child the river before he hangs up the pole. The new bridge is named after him if you finish it |
| `district.b2.night_shift` | One of the three patients is the Yūgure smuggler who escaped wounded in Ch 11, silent; the night ends with him slipping out, and pages are missing from the intake ledger. Whether the medic left their station that night is the medic's alibi or failed alibi (ROTATIONS §1). Sets `story.seed.night_patient` (the tester of Ch 23) |
| `district.b2.unbeatable_post` | The post is a sealed Uzumaki training post that hardens under chakra; it falls only to plain taijutsu with no chakra at all |
| `district.b1.academy.overdue` | One book holds a slip in Yūgure's cipher: `story.clue.librarian.3` |
| `district.b2.contraband` | The gate log shows the merchant's cart passed twice uninspected: `story.clue.merchant.3` (the bored guards waved every regular through) |
| `side.b2.pawned_scroll` | The scroll is real: a page of an old Academy textbook with the same cut as the missing page (Ch 5); the pawnbroker does not know who sold it (the porter). Sets `story.seed.second_page` |
| `side.b2.lost_letters` | One letter is addressed to a family that no longer exists in the census: one of the twenty-seven's old names. Returning it to the shrine sets `story.seed.unknown_family` |
| `side.b3.lost_genin` | The foreign Genin is one of a real, innocent foreign team whose two adult escorts (the second and the blade, under false papers) keep slipping away at night; the Genin knows only that the escorts are new (Ch 15 to 16) |
| `side.b3.stall_thief` | A Yūgure scout testing the village's guards before the finals; you can catch them but not hold them |
| `side.b3.hospital_supplies` | Diverted by a forged requisition in green ink, by an exam official selling supplies: `story.clue.medic.4`. A pure red herring in every save; the voice never touched it |
| `event.b2.council_day` | From the gallery you see the councillor hand a sealed letter to the porter: `story.clue.councillor.3` |
| `event.b3.betting_ring` | Run by the Hagane gate guards out of boredom; your odds improve if you finished `district.b2.contraband` |

### Mission secrets

Story ties of board missions ([SYSTEMS.md](SYSTEMS.md) §1). The board's premises stay neutral.

| Mission | The truth |
|---|---|
| `main.ch9.small_jobs`, `main.ch11.paper_trail`, `main.ch13.far_village`, `main.ch14.second_escort` | The story chapters (see the arc files) |
| `mission.c.escort_merchant`, `mission.c.caravan_guard` (`chain.merchant`, after Ch 14) | More time with a traitor candidate. One neutral camp step, identical in every save (`story.merchant.camp_talks`). No candidate-specific clues before Ch 39. After Ch 40 an innocent merchant's chain becomes the informant chain |
| `mission.b.*` with a `trail_drop` (Chunin) | Yūgure traces for the journal's *Yūgure* page |
| `mission.b.false_floors` | The merchant's alibi (the carpenter's abandoned shop) or failed alibi (the tool marks) |
| `mission.a.cell_hunt` (Jonin) | Cell members repeat orders whose meaning only Ch 49 reveals ("Mark the doors. Bring the paper.") |

### Boss secrets

Story fights in the combat session's boss files (`data/combat/bosses/<id>.json`, `"story": "bible:<id>"`). Public files carry only neutral loadouts.

| Boss id | Chapter | Who and what | Secret mechanic |
|---|---|---|---|
| `combat:boss.ch14.road_ambush` | Ch 14.2 to 14.3 | A Yūgure hearth of three (road clothes, ash-violet scarves) holds the river crossing while the smuggler runs; the second and the blade cross ahead and never fight | **Cut bridge:** at a set time the blade's one stroke cuts the rope bridge behind them (an ink line that blocks pursuit); capturing the smuggler is the objective that sets `story.ch14.done` |
| `combat:boss.ch16.forest_team` | Ch 16.3 | A hostile exam team of another village springs a ravine trap | **Ember interrupt:** at low player health a burning kunai pins the attacker (the second, "looking for her team"), ending the fight |
| `combat:boss.ch19.stadium_cell` | Ch 19.2 to 19.6 | Yūgure hearths in the stands at the opening lantern-lighting | Protect objective: the Academy children down the east stair; the Fourth is hit on the stair by a scripted strike (`twist.fourth_fate`); a collapsing tier at 19.4 |
| `combat:boss.ch19.finals` | — | The rival bout is scheduled last and **never fought** in the story (the attack comes first). The file can stay for NPC exam seasons | — |
| `combat:boss.chunin.story_1` | Ch 24 | `lost_child`, hollowed, at the border post | **Hollow:** flat AI, no flinch, cycles three stolen natures; ordered to wound, never kill, the player; phase 2 begins when a friend falls (scripted kindle, story floor); ends when she sees the cord |
| `combat:boss.chunin.story_2` | Ch 31.1 | A Yūgure hearth in the storm drain under the wall | **Smothered:** no sound cues; the player's first Ember Link (story floor) lets them see through allies' eyes |
| `combat:boss.jonin.story_1` | Ch 37.3 | `yugure_blade` in the archive (loadout `combat:enemy.lone_duellist`) | Protect the stone basket (the Hearthstone); ink lines in the air deny areas; he retreats wounded |
| `combat:boss.jonin.story_2` | Ch 35 | The nursery hearth's leader in the Valley of Ash | Avoidable: squad3_a's no-fight plan skips most of it; the children's cells are protect objectives |
| `combat:boss.anbu.story_1` | N6 | The Undercroft's old masks, then `squad5_c` | Sealing traps; `squad5_c` can be talked down mid-fight (`ans.squad5_c.offer`), ending it |
| `combat:boss.road.story_1` | Ch 51b | `yugure_blade`, last duel, on the rooftops (loadout `combat:enemy.lone_duellist`) | His best; ends on the player's answer (`ans.yugure_blade.why`), after which he turns |
| `combat:boss.road.story_2` | Ch 47 | The hearths hunting the deserting `lost_child` at the shrine | Defend the stone basket and her; then the relighting (a scripted thread floor) |
| `combat:boss.road.final` | Ch 52 to 53 | `yugure_leader` on the Rock | **Dark mirror:** a drain beam the player breaks by line of sight; unbroken anchors (`story.array.unbroken`) add hollow fighters; **every fire:** in the last phase the player's power grows with each flame given (the bond web tiers); the fight ends when his mirror turns on him |

### Clan lines

| Quest | The truth |
|---|---|
| `clan.kurama.3` | The missing painting shows the Kagari shrine before it burned; a Kurama painter (one of the twenty-seven's adoptive family) made it and was punished |
| `clan.tsuchigumo.3` | The intruder at the sealed shrine room is a Yūgure scout looking for the clan's natural-energy seal |
| `clan.shimura.3` | A Shimura found a stranger using their cellar as a mail drop for sealed letters and wants it gone quietly; helping catches the Undercroft's courier, which opens the Night Watch's N3. The Shimura have no part in the Undercroft |
| `clan.tobari.3` | What moves on the wall unheard is a Yūgure cell using a sound-smothering technique learned from a Tobari deserter (Ch 30 to 31) |
| `clan.hatake.4` | The keepsake's heir is the sensei if no Hatake lives in the save; otherwise the last Hatake |
| `clan.uzumaki.3` | The scattered Uzumaki is genuine, and a sealing expert who helps with the archive's seals (Ch 36) |
| `clan.senju.4` | If `twist.traitor = councillor`, the founders' shrine dispute becomes his house's reckoning |

## Bonds in the story

How the plot drives the bond engine ([BONDS.md](../../BONDS.md)), by beat. Everything is data:
quest actions and conditions on roles, never code. Questions and answers: [DIALOGUE_BRIEFS.md](DIALOGUE_BRIEFS.md) §4.

| Beat | Role | Bond data |
|---|---|---|
| Ch 0, the rescue | `captain` | `bond_event saved_by_them` |
| Ch 0, the red cord | `lost_child` | Bond created at level 2 with `bond_flag red_cord`; it does not grow while she is gone; it starts growing when she comes home (N6 or Ch 47) |
| Ch 3, the flare | `teammate_a` | `bond_event trained_together`; flavor only, never a Kindling grant |
| Ch 6, a classmate confides | `teammate_b` | Keep it (`kept_secret`) or tell the instructor (`broke_secret`) |
| Ch 8, the cord test (three watch-fire tags on one red cord, taken together) | the squad | `shared_moment bond.cord_test` |
| Ch 11, the campfire | `teammate_a` | Needs `friendship [teammate_a, 5]`; `shared_moment`, `heart_to_heart` |
| Ch 13, the stranger | `teammate_b`, `sensei` | Tell the sensei: `went_over_their_head` with b, `kept_promise` with the sensei. Keep: `kept_secret` with b. Go: `stood_by_them` and a `reckless_charge` the sensei hears of |
| Ch 14, the suspicion | `sensei` | `bond_meter [sensei, trust, 50]` gates the secret training (Ch 25) |
| Ch 16, the night watch | teammates | `shared_moment bond.night_watch`; the campfire leans only with `squad_cohesion 50` |
| Ch 19, the attack | teammates or the rival | The teammate at the higher level drags you out of a collapsing tier of the stands (`saved_by_them`; no wound); both under 4: the rival |
| Ch 24, the first kindling | the teammate at the highest level, 6 or more; else the sensei | `saved_by_them`; their own technique kindled past its limits; `story.kindling.awakened`. Story floor: the scripted target counts as Spark in this scene |
| Ch 26, b's road | `teammate_b` | `bond_meter [teammate_b, trust]`: 60+ stays, 30 to 59 nearly joins (`return_to_squad`), under 30 leaves (`remove_from_squad story`) |
| Ch 36, the keeper's door | `elder_keeper` | `bond_meter [elder_keeper, trust, 60]` and `friendship [elder_keeper, 6]`: he opens it himself |
| Ch 39, the voice | `twist.traitor` | Never gated by the reveal. `start_conflict` with `broke_secret`; turning needs `friendship 4`; at 7, "Why you" |
| Ch 40, the cleared | innocent candidates | `shared_moment`; `reconciled` if suspected aloud |
| Ch 46, your house | descendants, friends | Recruitment (BONDS §10) |
| N6 / Ch 47, giving flame | `lost_child` | `gave_flame` (requested act); her bond grows from 2 |
| Ch 50, the doors | clans and districts | `standing` gates per quarter |
| Ch 53, every fire | everyone at 6+ | The watch-fire's size is `BondWeb.score` ([BONDS.md](../../BONDS.md) §11), in three tiers: a small fire (under 20), strong (from 20), the whole village (from 41). The thresholds are data, calibrated by the bonds session's simulation (60 h: reckless 4 to 10, typical 34 to 40, devoted 42 to 50) |
| Ch 52, the blade | `yugure_blade` | His one thread to the second burns bright for this scene only (`thread_floor`); he lives (`story.blade.custody`) |
| Ch 53, the spoken flames | `lost_child`, `sensei`, spouse, the friend who fell in Ch 24, the other teammate, `rival` | Fixed order; the red cord and the sensei kindle first in every save at any level (the lonely floor; the sensei's flame overrides a falling-out); then faces without spoken lines |
| Ch 53, the second | `yugure_second` | Lives in any of three ways: the web at "strong" (score 20 or more); `friendship [yugure_second, 4]`; or `friendship [squad4_c, 6]` with `ans.squad4_c.second` not "someone else first". Resolved before the leader's end (53.5) |
| The librarian teaches the gift's old forms | `librarian` | Before Ch 39, identical in every save: `friendship [librarian, 7]` and `story.kindling.awakened` (lore and practice: the songs, keeping the flame, the ember mark). After Ch 40 only if innocent |
| The merchant turns informant (innocent) | `merchant` | `friendship [merchant, 6]` after Ch 40 |
