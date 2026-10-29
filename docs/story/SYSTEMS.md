# How the story uses the systems

> **SPOILERS: for developers only.** Part of the [story bible](STORY_BIBLE.md).

The main path is about half authored chapters and half systemic play in every stretch (ROADMAP
§1, §8). This file says what the systemic half carries for the plot, so that missions, bonds,
side quests, clans and combat are part of the story and not filler between it.

## 1. Missions

| Stretch | Story-tied missions | What they carry |
|---|---|---|
| Genin | Board D-ranks (~12), C-ranks (~3) | Squad experiences for the bond gates; one C-rank template (`mission.c.east_delivery`) may roll the merchant as client (more time with a traitor candidate) |
| Chunin | B-ranks (~10) with **trail drops** (missions session: `trail_drop {chance, pool}` on `mission.b.missing_nin_hunt`, `spy_in_town`, `fortress_infiltration`, `supply_sabotage`, `allied_courier`, `road_watch`; pools `journal:trail.roads`, `journal:trail.workshop`): each story-flagged B-rank has a 1-in-3 chance of a Yūgure trace (a sinking-sun mark, chakra paper, a cell's cache) | `mission.b.paper_cache`, `mission.b.cell_watch`, `mission.b.false_floors` (the merchant's alibi or failed alibi), `mission.b.nursery_rumour`. Each trace adds a line to the journal's *Yūgure* page; three traces before Ch 27 unlock an extra line from the second in 27.3 |
| Chunin | Leading NPC Genin on missions | Reads `squad_cohesion` |
| Jonin | A-rank **cell hunts** in far regions | `mission.a.cell_hunt` (rolled region): captured cell members give pieces of the Hollow Crown's shape (they don't know it; they repeat orders: "Mark the doors. Bring the paper.") that make Ch 49 recognisable |
| Jonin | Your Genin team's D- and C-ranks | Your own teaching; the genin's bonds; genin_3's flame (`story.seed.genin_flame`) |
| ANBU | Covert and S-rank | The Undercroft's trail (N2) |
| Road to Hokage | S-ranks clearing the last hearths, between Ch 46 and Ch 48 (`story.cells_cleared`) | Each one cleared removes a wave from the Ch 51a assault |

Mission failure never blocks the story; it costs standing, as in the beta.

**Requests (missions session):** B-rank templates with a `trail_drop` field (a chance and a
pool of journal lines); an A-rank `cell_hunt` template with a far-region slot; a "lead your Genin"
companion mode from the Jonin arc.

## 2. Side quests

The side quests SIDE_QUESTS.md lists keep their premises; these are their story ties (truths in
the bible's side quest secrets).

| Quest | Ties into |
|---|---|
| `district.b1.academy.overdue` | `story.clue.librarian.3` (the cipher slip) |
| `event.b2.council_day` | `story.clue.councillor.3`; introduces the council for Ch 31 and Ch 40 |
| `district.b2.contraband` | `story.clue.merchant.3` |
| `district.b2.night_shift` | Sets `story.seed.night_patient` (Ch 23) and `story.clue.medic.3`; nothing about the medic is seen; identical in every save (the alibi is only the roster at Ch 38) |
| `side.b2.pawned_scroll` | `story.seed.second_page`: a second cut page; the keeper buys it from you in the Jonin arc (trust +) |
| `side.b2.lost_letters` | `story.seed.unknown_family`: a letter to a family that no longer exists, one of the twenty-seven's old names (Ch 37 makes it land) |
| `side.b3.lost_genin` | The foreign Genin (Ch 15, 16) |
| `side.b3.hospital_supplies` | `story.clue.medic.4`, a pure red herring in every save |
| `clan.tobari.3` | Ch 30 shortcut; the Tobari deserter who taught Yūgure the smothering technique |
| `clan.shimura.3` | Opens the Night Watch's cellar (N3) |
| `clan.kurama.3` | The hidden painting of the shrine before it burned, brought out in Ch 40 |
| `clan.tsuchigumo.3` | A Yūgure scout seeking their seal: a trail drop in the Chunin arc |
| `clan.uzumaki.3` | The sealing expert who helps break the archive's old seals in Ch 36 if present (otherwise the keeper's keys alone) |
| `clan.hatake.4` | The keepsake's heir is the last Hatake; if no Hatake lives in the save, it goes to the house's caretaker and its old ninken, who choose whom to follow |
| `clan.senju.4` | If the councillor is the voice, the founders' shrine dispute becomes his house's reckoning |
| `clan.<id>.5` (Legacy) | Ch 50: a clan whose Legacy step is done opens its quarter's anchors and sends fighters to Ch 51a |
| `filler.lake_lanterns` | If `story.seed.flare`, the lantern leans toward you (an echo) |
| Snowbound (Chunin, later) | A courier carrying Yūgure paper unknowingly: a trail drop |
| The Puppet Theatre (Jonin, later) | A gifted orphan hidden from a Yūgure recruiter; can join your restored house later |
| The Forger's Ink (Jonin, later) | Gated to `story.ch39.done`; the ink of the voice's household, consistent with `twist.traitor` |

**New story side quests** (spoiler-zone premises; neutral premises to send the roadmap session):

| Id | Stretch | Premise (neutral) | Truth |
|---|---|---|---|
| `side.c.returned_book` | Chunin | A library book keeps being returned on days the library is closed | The librarian's alibi or failed alibi |
| `side.c.court_roll` | Chunin | A clerk from the daimyo's court is stuck in the village with a damaged guest roll | The councillor's alibi or failed alibi |
| `side.c.sensor_shadow` | Chunin | The young sensor assigned to you would like, very much, to have a single day off | squad4_a's bond line |
| `side.c.third_time` | Chunin | A loud Genin and his enormous dog are taking the Chunin Exams for the third time | squad4_b's promotion at last (fan favourite) |
| `side.j.roots` | Jonin | Families come asking the archive where they came from | The descendants after Ch 40 |
| `bond.c.wrongly_accused.<candidate>` | Jonin | Make amends to someone you wronged | After a wrong accusation |

## 3. Bonds

The bond engine ([BONDS.md](../../BONDS.md), [LIFE_TOGETHER.md](../../LIFE_TOGETHER.md)) is the story's spine:

- **Gates** decide which scenes play: the Ch 11 campfire (`friendship [teammate_a, 5]`), the Ch 24
  fall (the highest teammate at 6+), the secret training (`bond_meter [sensei, trust, 50]`), the
  keeper's door (`trust 60`, `friendship 6`), turning the voice (`friendship [bound, 4]`), the
  second's life (the web at the "strong" tier, `friendship [yugure_second, 4]`, or `friendship [squad4_c, 6]`), the finale's size (the web's tier), and the Ch 53 flame order (the cord, the sensei, the spouse, the friend who fell, the other teammate, the rival; then faces).
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
  shrine visits) adds lines to the finale.
- **Life events** for story characters are authored, not rolled, at story beats (the teammate's
  injury after Ch 24, b's parent news after Ch 26, the keeper's illness hint before Ch 51), so
  comforting them can earn the moments the gates ask for.
- **A teammate who leaves.** Any teammate who leaves from Ch 8 on (a falling-out, a low bond) is
  replaced by a stand-in lent by `sensei_2` (classmate_c, else classmate_d). If b has already left
  by Ch 13, the stranger approaches b anyway (easier to reach outside the squad) and Ch 26 plays as
  *left*. The story mends a falling-out at Ch 25 for the friend who fell and at Ch 25.4 for the
  sensei; in Ch 53 the sensei's flame overrides a falling-out.
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
finale reading the six fixed speakers in order (the cord, the sensei, the spouse, the friend who fell in Ch 24, the other teammate, the rival), then everyone else at 6+ as faces (ARCS/7 53.2).

## 3b. Rank gates (the failure rule)

The main path never stalls on a failed rank gate:

| Gate | If the player fails |
|---|---|
| Graduation (Ch 7) | A failed part is retaken the next day |
| The Chunin Exams (Ch 20) | A player not promoted makes Chunin at the next season's exam inside the Ch 21 time skip (a vignette; a different line from the sensei) |
| The Jonin trial (Ch 33) | The arc's chapter missions count toward the mission requirements and the trial bout counts as the A-rank; level 30 still applies, and the chapter waits for it |
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
| **The crossing**: Ember Mark jumps between Blaze friends, else a guided rooftop run | Ch 51b |

## 6. The Hokage requirement (wording for the roadmap)

The succession (Ch 55) needs level 50, **Hero standing with the village**, and **at least Good
Neighbor in every district and clan quarter**; defending the village in the last arc counts as a
great deed in every community. The roadmap session has the neutral wording for ROADMAP §11.
