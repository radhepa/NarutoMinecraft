# How the story uses the systems

> **SPOILERS: for developers only.** Part of the [story bible](STORY_BIBLE.md).

From the Chunin arc on, the main path is about half authored chapters and half systemic play
(ROADMAP §1, §8); the beta leans authored (Beta 1 about 70/30, Beta 3 about 83/17). This file says what the systemic half carries for the plot, so that missions, bonds,
side quests, clans and combat are part of the story and not filler between it.

## 1. Missions

| Stretch | Story-tied missions | What they carry |
|---|---|---|
| Genin | Board D-ranks (~12), C-ranks (~3) | Squad experiences for the bond gates; the C-rank `mission.c.escort_merchant` may roll the merchant as client (more time with a traitor candidate; done as `chain.merchant`) |
| Chunin | Board B-ranks (~5, 35 to 45 min each) with **trail drops** (`trail_drop {chance, pool}` on `mission.b.missing_nin_hunt`, `spy_in_town`, `fortress_infiltration`, `supply_sabotage`, `allied_courier`, `road_watch`, `false_floors`; pools `journal:trail.roads`, `journal:trail.workshop`): each has the chance its template sets (25 to 50 percent in the catalogue) of a Yūgure trace (a sinking-sun mark, chakra paper, a cell's cache) | `mission.b.false_floors` (the merchant's alibi or failed alibi) exists; three story B-ranks are requests (below). Each trace adds a line to the journal's *Yūgure* page; one trace or more before Ch 27 unlocks an extra line from the second in 27.3 |
| Chunin | Leading NPC Genin on missions | Reads `squad_cohesion` |
| Jonin | A-rank **cell hunts** in far regions | `mission.a.cell_hunt` (rolled region): captured cell members give pieces of the Hollow Crown's shape (they don't know it; they repeat orders: "Mark the doors. Bring the paper.") that make Ch 49 recognisable |
| Jonin | Your Genin team's D- and C-ranks | Your own teaching; the genin's bonds; genin_3's flame (`story.seed.genin_flame`) |
| ANBU | Covert and S-rank | The Undercroft's trail (N2) |
| Road to Hokage | S-ranks clearing the last hearths, from Ch 46 until Ch 51a begins (`story.cells_cleared`) | Each one cleared removes a wave from the Ch 51a assault, down to a floor (ARCS/7 Ch 51a, "The waves") |

Mission failure never blocks the story; it costs standing, as in the beta. A required objective lost
in a story fight (Ch 14's runner, Ch 19's east stair) restarts that fight from its checkpoint;
there is no failed-outcome flag.

**Done (missions session):** B-rank templates with a `trail_drop` field, `mission.b.false_floors`,
the A-rank `mission.a.cell_hunt` with a far-region slot, `mission.c.lead_genin`, and `chain.merchant` (the merchant cast as client on `mission.c.escort_merchant` and `caravan_guard`, with a camp-talk step after Ch 14).

**Requests (missions session):** these are not in `tools/missions/catalogue/` yet.
- Three story-flagged B-ranks with trail drops: `mission.b.paper_cache` (a cell's cache of chakra
  paper), `mission.b.cell_watch` (watching a waystation a hearth uses) and `mission.b.nursery_rumour`
  (a rumour of children kept on a border farm).
- A mission trail drop that lands also adds 1 to `story.trail.count` (today it only adds the journal line). Side-quest steps called trail drops in §2 (`clan.tsuchigumo.3`, Snowbound) add nothing to it.
- `chain.merchant`'s story states: after Ch 40 an innocent merchant's chain becomes the informant chain; it ends after an arrest and is suspended for a turned merchant ([merchant.md](CHARACTERS/merchant.md)).
- An S-rank template for the Road to Hokage, `mission.s.clear_hearth`, whose success raises the
  counter `story.cells_cleared` by one.
- Simulation inputs: the story's day counts and gates (WORLD.md "Elapsed time and ages"; FLAGS.md
  gates), in place of the simulation's Chunin from day 60 and Jonin from day 140.

## 2. Side quests

The side quests SIDE_QUESTS.md lists keep their premises; these are their story ties (truths in
the bible's side quest secrets). A tie that names a chapter pays only if the quest is done before that
chapter plays; done later, the quest keeps its plain truth and no story tie (the steps held by the
requests below are the exceptions, since they cannot be done early).

| Quest | Ties into |
|---|---|
| `district.b1.academy.overdue` | `story.clue.librarian.3` (the cipher slip) |
| `event.b2.council_day` | `story.clue.councillor.3`; introduces the council for Ch 31 and Ch 40 |
| `district.b2.contraband` | `story.clue.merchant.3` |
| `district.b2.night_shift` | Sets `story.seed.night_patient` (Ch 23) and `story.clue.medic.3`; nothing about the medic is seen; identical in every save (the alibi is only the roster at Ch 38; the pages vanish in every save, played or not, on the ledger night: the night of your night shift if you work it on or before the night Ch 14 ends, otherwise the night Ch 14 ends: [ROTATIONS.md](ROTATIONS.md) §1, item 3). The shift's three parts play on one night. The smuggler slips out on the ledger night in every save; a shift worked after it finds his bed empty and the pages already gone (no errand window, nothing missed during it), and sets `story.clue.medic.3` but not `story.seed.night_patient`, so Ch 23's tester is a stranger. |
| `side.b2.pawned_scroll` | `story.seed.second_page`: a second cut page; the keeper buys it from you in the Jonin arc (trust +) |
| `side.b2.lost_letters` | `story.seed.unknown_family`: a letter to a family that no longer exists, one of the twenty-seven's old names (Ch 37 makes it land) |
| `side.b3.lost_genin` | The foreign Genin (Ch 15, 16). It opens on the evening Ch 15's requirements are first all met (`story.ch14.done`, `story.ch14.recommended`, level 15) and plays that evening; Ch 15 begins the next morning (by `time_skip` to its date if that is still ahead), so the 15.3 tie can pay |
| `side.b3.hospital_supplies` | `story.clue.medic.4`, a pure red herring in every save |
| `clan.tobari.3` | Ch 30 shortcut; the Tobari deserter who taught Yūgure the smothering technique |
| `clan.shimura.3` | Step 3 opens only after `story.ch44.done`, in every save (request below), so the Undercroft's courier is never caught before N3 can follow it. Exposes the cellar mail drop; the letters go to the ANBU captain unopened (the Shimura custom: a carrier never opens a sealed letter); following its courier leads to the old quarry (N3) |
| `clan.kurama.3` | Step 3 opens only after `story.ch39.done`, in every save (request below), so it plays in Ch 40.4's wave and never shows the shrine or the twenty-seven before the archive opens them (Ch 36 to 37). The hidden painting of the shrine before it burned, brought out in Ch 40 |
| `clan.tsuchigumo.3` | A Yūgure scout seeking their seal: a trail drop in the Chunin arc |
| `clan.uzumaki.3` | The sealing expert who helps break the archive's old seals in Ch 36 if present (otherwise the keeper's keys alone) |
| `clan.hatake.4` | The keepsake's heir is the last Hatake; if no Hatake lives in the save, it goes to the house's caretaker and its old ninken, who choose whom to follow |
| `clan.senju.4` | Step 4 opens only after `story.ch39.done`, in every save (request below). If the councillor is the voice, the founders' shrine dispute becomes his house's reckoning |
| `clan.<id>.5` (Legacy) | Ch 50: a clan whose Legacy step is done opens its quarter's anchors and sends fighters to Ch 51a |
| `filler.lake_lanterns` | If `story.seed.flare`, the lantern leans toward you (an echo) |
| Snowbound (Chunin, later) | A courier carrying Yūgure paper unknowingly: a trail drop |
| The Puppet Theatre (Jonin, later) | A gifted orphan hidden from a Yūgure recruiter; can join your restored house later |
| The Forger's Ink (Jonin, later) | Gated to `story.ch39.done`; the ink of the voice's household, consistent with `twist.traitor` |

**Requests (side-quest session):** hold Senju Heart step 4 (`clan.senju.4`) until `story.ch39.done`
in every save, whatever the rotation, so it never branches on `twist.traitor` before Ch 39; the
same gate as The Forger's Ink. Hold Shimura Trust step 3 (`clan.shimura.3`) until `story.ch44.done`
in every save, so its courier is caught only when the Night Watch's N3 can follow him; before then
the Shimura line waits at step 2. Hold Kurama Trust step 3 (`clan.kurama.3`) until
`story.ch39.done` in every save, so the painting comes out in Ch 40.4's wave, after the archive's
truth.

**New story side quests** (spoiler-zone premises; neutral premises to send the roadmap session):

| Id | Stretch | Premise (neutral) | Truth |
|---|---|---|---|
| `side.c.returned_book` | Chunin | A library book keeps being returned on days the library is closed | The librarian's alibi or failed alibi |
| `side.c.court_roll` | Chunin | A clerk from the daimyo's court is stuck in the village with a damaged guest roll | The councillor's alibi or failed alibi |
| `side.c.sensor_shadow` | Chunin | The young sensor assigned to you would like, very much, to have a single day off | squad4_a's bond line |
| `side.c.third_time` | Chunin | A loud Genin and his enormous dog are taking the Chunin Exams for the third time | squad4_b's promotion at last (fan favourite) |
| `side.j.roots` | Jonin | Families come asking the archive where they came from | The descendants after Ch 40 |
| `bond.c.wrongly_accused.<candidate>` | Jonin | Make amends to someone you wronged | After a wrong accusation |
| `bond.teammate_b.return` | Chunin | A friend who quit is training alone at night; get them to talk to you | b's return at Ch 32.3, or at the next dawn if done later and before Ch 49 (*left* path only; needs `friendship [teammate_b, 4]`; ARCS/4 32.3) |
| `bond.j.genin.<own_test>` | Jonin | Your new Genin want a second go at the test you set them; run it again, your way | The Genin's first bond quest: its opening errand is the test you chose at Ch 34.2 (cord, rescue, scroll, night watch) |

## 3. Bonds

The bond engine ([BONDS.md](../../BONDS.md), [LIFE_TOGETHER.md](../../LIFE_TOGETHER.md)) is the story's spine:

- **Gates** decide which scenes play: the Ch 11 campfire (`friendship [teammate_a, 5]`), the Ch 24
  fall (the highest teammate at 6+), the secret training (`bond_meter [sensei, trust, 50]`), the
  keeper's door (`trust 60`, `friendship 6`), turning the voice (`friendship [bound, 4]`), the
  second's life (the web at the "strong" tier, `friendship [yugure_second, 4]`, or `friendship [squad4_c, 6]` with `ans.squad4_c.second` not "someone else first"; FLAGS `story.second.lives`), the finale's size (the web's tier), and the Ch 53 flame order (the cord, the sensei, the spouse, the friend who fell, the other teammate, the rival; then faces).
- **Moments** are the story's beats: every chapter's bond scene is a `shared_moment` keyed by quest id.
- **Questions and answers.** Every major character asks the player questions (opinions, values,
  advice, their past, small confessions). Answers are player-scope flags `ans.<role>.<topic>`
  ([FLAGS.md](FLAGS.md)), read later by dialogue and quests. Each question's options are written to
  honour or test the character's values, so the bond engine's reaction (`Reaction.react`) also moves
  the meters: the *reaction* is the systemic effect; the *flag* is the story memory. There are no
  "right" answers: each changes who the character becomes, and none locks the player out of the
  main path.
- **Time together.** Hangouts and rituals are where most questions are asked: a question is a
  conversation topic that opens at its level and plays in a hangout or a talk (`talk.q.<role>.<topic>`).
  A ritual with a story character (the squad's ramen, the rival's rooftop race, the lost child's
  shrine visits) adds a remembered moment among the Ch 53 faces (ARCS/7 53.2); it is not a flame line.
- **Life events** for story characters are authored, not rolled, at story beats (the teammate's
  injury after Ch 24, b's parent news after Ch 26, the keeper's illness hint before Ch 51), so
  comforting them can earn the moments the gates ask for.
- **A teammate who leaves.** Any teammate who leaves from Ch 8 on (a falling-out, a low bond) is
  replaced by a stand-in lent by `sensei_2` (classmate_c, else classmate_d). If b has already left
  by Ch 13, the stranger approaches b anyway (easier to reach outside the squad) and Ch 26 plays as
  *left*. The story mends a falling-out with a `mend` act at: Ch 25.4 (the sensei); Ch 41.2 (teammate_a,
  at the unveiling, which is public, so the player can go uninvited); Ch 49.4 (the sensei, if a falling-out with them
  stands at Ch 49); Ch 49.5 (teammate_b, unless the player chose "at the war", and teammate_a if a falling-out with them
  stands at Ch 49); Ch 51a.4 (teammate_b, if the player chose "at the war" at 49.5, in every such save; standing with b only colours it). Every story `mend` of a teammate whose
  falling-out took them out of the squad also carries `return_to_squad`. In Ch 53 the
  sensei's flame overrides a falling-out. A teammate in a falling-out has their bond held low and leaves the squad under
  BONDS §7, so they are never the friend who falls in Ch 24.
- **The squad hold.** From the end of Ch 49 to the end of Ch 55, no quarrel with a teammate or the
  sensei hardens into a falling-out (a third strike, a severity-60 betrayal or a quarrel left 28 days
  stays a quarrel), and a low bond takes no teammate out of the squad. So no falling-out stands at the
  finale, and the only teammate who can be out of the squad at Ch 53 is a teammate_a who left on a low
  bond and never did the return quest (DIALOGUE_BRIEFS, "The Ch 53 speaking rule", item 5). In the
  post-game the normal BONDS.md rules apply again.
- **Unset answers.** Every main-path read of an `ans.*` flag has an `unset` default
  ([FLAGS.md](FLAGS.md)).
- **The village talks.** Big beats are deeds everyone hears: the stadium (Ch 19), the border post
  (Ch 24), the testimony (Ch 31), the council (Ch 40), the war (Ch 51a and 51b). Residents' greetings react.

**Done (bonds session):** BONDS.md §11 now uses the approved powers. The request was to replace BONDS.md §11's table
(nature casts, technique uses, "borrow", a "borrowed" natures source, a 12-use trial that makes a
nature yours) with the approved powers in [WORLD.md](WORLD.md#kindling-bond-in-the-story): Thread
Sight, Kindle, Ember Link, Ember Mark and Bonfire on the tiers Spark 6, Flame 8, Blaze 10 or a
spouse, Bonfire the web. Natures come by resonance: fighting beside someone often enough lets their
trial teach you their nature, never a copy. Count `kindle` uses for the resonance trial, not for
borrowing. Thread Sight's mystery limit (reads only bonds at 6+, shows that someone hides, never
what) is a rule of the engine, not of the story.

**Other requests (bonds session):** the Kindling tiers read friendship levels as approved (Spark 6, Flame 8, Blaze 10 or a spouse, Bonfire the web); answer flags (`ans.*`) as player-scope string flags, readable by a
`flag` condition with a value; authored life events for story roles at story beats; an act
`gave_flame` (big, kept; the lost child's return) and `shielded_with_life` (the second); the
finale reading the six fixed speakers in order (the cord, the sensei, the spouse, the friend who fell in Ch 24, the other teammate, the rival), then everyone else at 6+ as faces (ARCS/7 53.2); a story hold between two flags (for example `squad_hold [roles, from_flag, to_flag]`) under which a quarrel with the named roles cannot become a falling-out and a low bond cannot remove them from the squad (§3, "The squad hold": from `story.ch49.done` to `story.ch55.done`); a scripted thread between two named roles, with a `to` field and a `bright` style (FLAGS.md, the blade's thread to the second at Ch 52.5).

## 3b. Rank gates (the failure rule)

The main path never stalls on a failed rank gate:

| Gate | If the player fails |
|---|---|
| Graduation (Ch 7) | A failed part is retaken the next day |
| The Chunin Exams (Ch 20) | A player not promoted makes Chunin at the next season's exam inside the Ch 21 time skip (a vignette; a different line from the sensei) |
| The Jonin trial (Ch 33) | The arc's chapter missions count toward the mission requirements, leading NPC Genin counts toward the three squad missions, the trial bout counts as the A-rank, and the A-rank jutsu is waived on the story path (one learned by then counts); level 30 still applies, and the chapter waits for it |
| The Hokage (Ch 55) | Met by Ch 53.7's level floor and `saved_the_village` |

## 4. Clans

- **The player is a clanless orphan** (a user decision "for now"; clan-born play may return later). Clans reach the player as hosts and teachers: a lesser technique from the clan of the closest classmate who has a clan (Ch 12), welcome quests, invitations at high friendship (BONDS §10), and the Legacy steps.
- **Clan politics in the plot**: the Tobari crisis (Ch 30 to 31) is a clan story told through the
  bond engine's relations (`clan_relation tobari hagane`, moods); the council (Ch 40) moves every
  founding clan's relation with the village; the Legacy steps decide who stands with you in Ch 51a.
- **Your house**: restored Kagari or your own clan (Ch 46), recruited from descendants and friends.

## 5. Combat

Requests to the combat session, by story need (docs/COMBAT.md is being written; these are needs,
not mechanics):

| Need | Where |
|---|---|
| **The cord test** (`ch8.cord_test`): the sensei's own habits, no canon test beats (request in §7) | Ch 8 |
| **Hearth** AI: a cell of three or more in road clothes that covers each other and retreats together; ash-violet scarves when they mean to be seen. The second and the blade are the one pair | Ch 14 onward |
| **The blade**: a kenjutsu duellist whose cuts leave short-lived ink lines in the air (area denial) | Ch 14 (one cut), 27, 37, 51b |
| **Ember chakra**: the second's burning kunai and ember palms | Ch 16, 19, 27 |
| **The hollow**: an enemy with flat AI and several stolen natures (cycles through them), who does not flinch | Ch 24 (the lost child), Ch 52 to 53 (hollow fighters) |
| **Smothered fights**: no sound cues | Ch 31 |
| **Kindling Bond** (approved design, [WORLD.md](WORLD.md#kindling-bond-in-the-story)): Thread Sight from Ch 24 (with the mystery limit: reads only bonds at 6+; the flicker is a steady `hides:` state, never a lie detector; the only exceptions are the `thread_floor` list in FLAGS.md); a Kindle that makes an ally's own technique exceed its limits (Ch 24's scripted kindle must work on any teammate's or the sensei's signature technique); Ember Link in a dark, soundless fight (Ch 31); Ember Mark travel across the village (Ch 51); the Bonfire (Ch 53) | Ch 24 onward |
| **Unison techniques** for the player with each close character (ideas in each character file) | Jonin arc onward |
| **The dark mirror** as an enemy attack: a drain beam the player must break line of sight from | Ch 52 |
| **The finale**: a fight where the player's power grows with each flame given (data: the bond web) | Ch 53 |
| **Protect objectives** with evacuating residents | Ch 19, 51a |
| **The Dusk assault**: waves across the wall and the gate, fewer for each hearth cleared, with a floor that always comes (the counts: ARCS/7 Ch 51a, "The waves") | Ch 51a |
| **The crossing**: Ember Mark jumps between Blaze friends, else a guided rooftop run | Ch 51b |

## 6. The Hokage requirement (wording for the roadmap)

The succession (Ch 55) needs level 50, **Hero standing with the village**, and **at least Good
Neighbor in every district and clan quarter**; defending the village in the last arc counts as a
great deed in every community. The roadmap session has the neutral wording for ROADMAP §11.

## 7. Requests to other sessions (open)

These live outside `docs/story/`, so the story asks for them in neutral words. Each must be done
before the lock's final cross-system pass.

| To | Request (neutral wording) | Why the story needs it |
|---|---|---|
| Combat (`data/combat/bosses/ch8.cord_test.json`) | Rename phase 1 for the sensei's own habit ("Watching the cord", keeping the 90% dodge). The timer runs to sundown (ARCS/2 8.2), not noon. Replace the phase 2 punish with "a sweep and pin on the one who did not help; the one who helped gets a free tag touch". No named canon technique in the file. Rename the combo `combat:squad.bell_grab` (`data/combat/combos/squad.json`) to a cord id. Then `build.py --check` | The fight must not restage a canon test beat for beat (WORLD.md, Tone) |
| Public docs: `docs/RANKS.md` (the Beta 2 rows), `BONDS.md` (the squad bonding arc list and the moments list), `ITEMS.md` (the key item) | "The bell test" becomes "the cord test"; "holds the bells" becomes "holds the cord"; "self-declared rival" becomes "old contest partner"; the key item is "the cord test's tag" (`cord_tag`), without the claim that the roadmap names a bell | The public docs must match the story and the roadmap, which already say the cord test |
| Roadmap (§8, Ch 19 "Teaches") | Duels are taught in Ch 17 (the preliminaries); Ch 19 teaches protect objectives and the cinematic camera | ARCS/3 Ch 17 and Ch 19 |
| Roadmap (§11 event calendar) | The player's own Chunin Exams run on story dates (a written test, five Forest days, a tower day of preliminaries, a six-day break, the finals), apart from the calendar's NPC exam week; every story-gated date may `time_skip` forward to it, and one already passed is held on the day its chapter begins | WORLD.md "The calendar rule" and its dated table |
| Side quests (`SIDE_QUESTS.md`) | Add `bond.c.wrongly_accused.<candidate>`, `bond.teammate_b.return` and `bond.j.genin.<own_test>` with the neutral premises in §2 | They are story quests not yet in the side-quest design |
| Bonds (`BONDS.md` §8, its standing tables and the succession list) | The Hokage standing gate reads "Hero with the village and at least Good Neighbor in every district and clan quarter", as §15 and the roadmap (§11) already do | Ch 55.1 and §6 use that gate; the Ch 53.7 lift meets it |
| Bonds (`BONDS.md` §1 and §15) | A condition `bond_web_tier <small/strong/whole_village>` that reads `BondWeb.score` against the datapack's thresholds | FLAGS.md and Ch 53.3 read the tier, never a raw score |
| Combat (`docs/COMBAT.md`, the Bonfire paragraph; `data/combat/bosses/road.final.json`, the every_fire phase) | The finale's three fire tiers (and their damage multipliers) read `bond_web_tier`, the same tier the story stages, not the Bonfire strength (`Kindling.bonfire().strength()`, BONDS §11) | Ch 53.3, 53.5 and the epilogue size are staged on `BondWeb.score`; the fight must match the fire the player sees |
| Missions (`tools/missions/catalogue/later_ranks.py`) | `mission.a.cell_hunt` fights `combat:group.cell_trio` instead of `combat:group.cell_pair` | Yūgure travels in hearths of three or more; the second and the blade are the one pair (§5) |
| Missions (`tools/missions/`) | The open missions requests in §1 ("Requests (missions session)") | They are tracked there; the lock's cross-system pass checks them with this table |
| Side quests (`SIDE_QUESTS.md`, clan lines) | The open side-quest requests in §2 (hold `clan.senju.4` until `story.ch39.done`; hold `clan.shimura.3` until `story.ch44.done`; hold `clan.kurama.3` until `story.ch39.done`) | Rotation fairness: the quest must not branch on the voice before Ch 39 (ROTATIONS.md); the Undercroft's courier is never caught before N3; the painting never shows the Kagari past before Ch 36 to 37 |
| Bonds (`BONDS.md`) | The open requests in §3 ("Other requests (bonds session)") | They are tracked there; the lock's cross-system pass checks them with this table |
| Roster (`life/roster` `Season`) | Label the second skip "Four years later", and model the Ch 45 gate at level 42 and the Ch 48 gate at level 45 | WORLD.md "Elapsed time and ages"; ARCS/7 |
| Side quests (`SIDE_QUESTS.md`) | Open `side.b3.lost_genin` on the evening Ch 15's requirements are first all met (after Ch 14, recommended, level 15), the evening before the exam, not at Ch 15 | The 15.3 tie pays only if the quest can be done before Ch 15 plays |
