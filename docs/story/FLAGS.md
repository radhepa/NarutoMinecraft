# Story flags

> **SPOILERS: for developers only.** Part of the [story bible](STORY_BIBLE.md).

Every flag the story sets, where it is set and where it is read. `story/seeds.json` is generated
from the **Seeds** table; `quests.py --check` warns about a seed never read or a read never set.
Flags are player scope unless they start with `world.`.

## Chapter flags

Every main chapter sets `story.ch<N>.done` when it ends (`story.chN1.done` to `story.chN7.done` for
the Night Watch; `story.ch51a.done` and `story.ch51b.done` for the two halves of the war; Ch 51 is
done when both are). Gates in the character briefs use them ("never before `story.ch36.done`").

## Gates that order the chapters

| Gate | Condition |
|---|---|
| Night Watch N1 to N2 | Level 35, `story.ch39.done`, no bad deed in the last season |
| Night Watch N3 onward | `story.ch44.done` |
| Ch 47 | The Night Watch finished (`story.chN7.done`) or declined or never offered; entering Ch 47 with the branch half played closes it through Ch 47 |
| Ch 49 | Level 47 |
| Ch 55 | Plays directly after Ch 54. Finishing Ch 53 applies a **level-50 floor** and the deed `saved_the_village` (lived by every resident), which lifts the village to Hero and every district and clan quarter to Good Neighbor, so ROADMAP's Hokage requirement is met by the story |

## Twist slots (bound at world creation)

| Flag | Values | Read in |
|---|---|---|
| `twist.traitor` | `librarian`, `medic`, `councillor`, `merchant` | Ch 25 (the slip), Chunin alibis, Ch 35 to 40, Ch 50 and 51a (turned), Ch 55 (ruling) |
| `twist.lineage` | `second`, `fallen` | Ch 21, 27, 48, 52 to 55 |
| `twist.fourth_fate` | `falls`, `crippled`, `taken` | Ch 19 to 21, 49, 51, 55 |

## Seeds (set in the beta, paid later)

| Flag | Set | Paid off |
|---|---|---|
| `story.seed.half_charm` (item `half_charm`) | Ch 0.1 | Ch 25 (named), Ch 48 (the halves fit) |
| `story.seed.lost_child_cord` | Ch 0.2 | Ch 24, Ch 44, N4 to N6, Ch 47, Ch 55 |
| `story.seed.camp_number` | Ch 0.2 | Ch 25 (the slip), N3 |
| `story.seed.ruined_shrine` | Ch 0.5 | Ch 46 |
| `story.seed.watcher` | Ch 0.8 | Ch 52 |
| `story.clue.medic.1` | Ch 0.6 | Ch 38 |
| `story.seed.stipend` | Ch 1.2 | Ch 19 to 20, Ch 55 (extended in the Fourth's name to every child brought home, and made law). The stipend itself (30 ryo every morning) continues for the whole game |
| `story.seed.keeper_noticed` | Ch 1.2 | Ch 32, Ch 36 |
| `story.clue.councillor.1` | Ch 1.2 | Ch 38 |
| `story.seed.flare` | Ch 3.2 | Ch 24, `filler.lake_lanterns` |
| `story.clue.medic.2` | Ch 3.5 | Ch 38 |
| `story.seed.door_mark` | Ch 4.1 | Ch 49 |
| `story.seed.sealed_door` | Ch 4.3 | Ch 36 |
| `story.seed.missing_page` | Ch 5.2 | Ch 37 |
| `story.clue.librarian.1`, `.2` | Ch 5.2 | Ch 38 |
| `story.seed.blank_spots` | Ch 5.3 | Ch 32, 42, 55 |
| `story.seed.watchfire_song` | Ch 6.3 | Ch 16, 18, 25, 48, 52, 53 |
| `story.seed.cord_flicker` (was `bell_flicker`) | Ch 8.3 | Ch 24 |
| `story.seed.chiselled_names` | Ch 10.2 | Ch 41 |
| `story.seed.fallen_name` | Ch 10.2 | Ch 21, 41, 48 |
| `story.seed.cargo_found` | Ch 11.3 | Ch 23 |
| `story.seed.paper_chars` | Ch 11.3 | Ch 14, 23 |
| `story.clue.merchant.1` | Ch 11.3 | Ch 38 |
| `story.seed.ash_road` | Ch 13.2 | Ch 21, 24, 36 |
| `story.seed.teammate_approached` | Ch 13.4 | Ch 16, 26 |
| `story.clue.merchant.2`, `story.clue.councillor.2` | Ch 14 | Ch 38 |
| `story.ch14.done`, `story.ch14.recommended` | Ch 14 | Ch 15 (rank requirement), 27 |
| `story.seed.sensei_knows` | Ch 14.4 | Ch 25 |
| `story.lineage.persimmon_told` | Ch 14.4 | Ch 21.3 |
| `story.seed.second_spared` | Ch 16.3 | Ch 48 |
| `story.seed.campfire_leans` | Ch 16.6 | Ch 53 |
| `story.ch19.named` | Ch 19.5 | Ch 22, 48 |
| `world.hokage` | Ch 20 (5), Ch 32 (6), Ch 42 (7), Ch 55 (8) | Everywhere |
| `story.seed.fifth_hard_line` | Ch 20.2 | Ch 22, 30, 31 |
| `story.seed.night_patient` | `district.b2.night_shift` | Ch 23 |
| `story.seed.second_page` | `side.b2.pawned_scroll` | Jonin (the keeper) |
| `story.seed.unknown_family` | `side.b2.lost_letters` | Ch 37 |
| `story.clue.librarian.3`, `.merchant.3`, `.councillor.3`, `.medic.3`, `.medic.4` | Side quests (ROTATIONS §1) | Ch 38 |

## Later arcs

| Flag | Set | Read |
|---|---|---|
| `story.seed.leader_practising` | Ch 21.2c | Ch 49 |
| `story.kindling.awakened` | Ch 24.5 | Kindling Bond everywhere |
| `story.clue.slip.heard` | Ch 25.1 | Ch 38 |
| `story.lineage.hint` | Ch 25.3 | Ch 48 |
| `story.teammate_b.path` (`stayed`, `nearly`, `left`) | Ch 26 | Ch 32, 51a |
| `story.teammate_b.parent_alive` | Ch 26 | Ch 51a |
| `story.seed.candle` | Ch 27.3 | Ch 49 |
| `story.seed.porter_ledger` | Ch 28.5 | Ch 49, 50 |
| `story.seed.genin_flame` | Ch 34.3 | N5, Ch 44 |
| `story.clue.list_found` | Ch 35.3 | Ch 38 |
| `story.archive.opened` | Ch 36 | Ch 46 |
| `story.accused` | Ch 38.6 | Ch 39, 40 |
| `story.suspected.<candidate>` | Ch 5 and later accusations | Ch 40 |
| `story.traitor.fate` (`arrested`, `turned`) | Ch 39.2 | Ch 50, 51a, 55 |
| `story.seed.second_doubts` | Ch 41.4 | Ch 48 |
| `story.seed.lost_child_breaking` | Ch 44.2 | N3, Ch 47 |
| `story.squad5_c.stand` (`stood_down`, `fought`) | N6 or Ch 47 | Ch 51a, his file |
| `story.nightwatch.pretend` | N5 | N6 |
| `story.nightwatch.undercroft` (`disbanded`, `sworn`, `exposed`) | N7 | Ch 50, 51a |
| `story.lost_child.home` (`nightwatch`, `shrine`) | N6 or Ch 47 | Ch 53, 55 |
| `story.clan.choice` (`kagari`, `own`, `rekindled_own`, `enshrined`, `kin_of_host`, `left_host`) | Ch 46 | Ch 50, 55 |
| `story.hollow_crown.known` | Ch 49 | Ch 50 |
| `story.array.unbroken` (0 to 81) | Ch 50 | Ch 51a to 53 |
| `story.cells_cleared` (a counter) | S-ranks between Ch 46 and 48 | Ch 51a (each removes a wave) |
| `story.trail.count` (a counter) | B-rank trail drops (Chunin) | Ch 27.3 (three or more: an extra line from the second) |
| `story.merchant.camp_talks` (a counter) | `chain.merchant` camp step (after Ch 14) | The merchant's lines; after Ch 40 the informant chain |
| `story.finale.reached` | Ch 52.3 | Ch 55 epilogue line |
| `story.finale.offered_leader` | Ch 53.6 | Ch 54.3 |
| `story.traitor.ruling` | Ch 55.3 | Epilogue |
| `story.suspected.keeper` | Any accusation of the keeper (Ch 4 to 38) | Ch 36 (his dry line) |
| `story.lost_child.family_known` | Ch 38 (the decoded list names her family) | Her file; Ch 47, 55 |
| `bond_flag parent_sorry` on `yugure_b_parent` | Ch 51a.4 (when `ans.teammate_b.ask = sorry` and the parent apologises) | Ch 51a.4 branch |
| `story.second.lives` | Ch 53.5: the web at "strong" or above, or `friendship [yugure_second, 4]`, or `friendship [squad4_c, 6]` with `ans.squad4_c.second` not "someone else first" | Ch 54, 55 |
| `story.blade.custody` | Ch 52 (he lives) | Ch 54, 55 |

## Acts the story asks of the bond engine

| Act | What it is | Used in |
|---|---|---|
| `offered_flame` | A person (or a clan or district, by standing) below level 6 freely offers their flame; the only way someone under Spark kindles toward the player | Ch 31.2, Ch 53.2 (clans and districts), the red cord |
| `gave_flame` | The player relit someone's flame (big, kept) | N6, Ch 47 |
| `shielded_with_life` | Someone took the dark mirror for the player (big, kept) | Ch 52.4 |

**Story floor.** A scripted gift scene treats its scripted target as at the tier it needs (Ch 24:
Spark; Ch 31: Flame), whatever the level.

**`thread_floor`: the only scripted Thread Sight exceptions.** Thread Sight shows a thread only for
people bonded to the player at 6+ (between two others, only when both are). The flicker is a steady
state from one `hides:` bond flag, never a lie detector. The exceptions, each a `thread_floor`:

| Exception | Where |
|---|---|
| The red cord's grey thread to the lost child | Ch 24.6, N6, Ch 47 |
| The second's one-sided thread toward the player | From Ch 27; fraying from Ch 49 to 52; held by the player in Ch 53.5 |
| teammate_b's fraying thread before the bridge (every branch) | Ch 26 |
| The blade's thread to the second | Ch 52 only |

The porter and every traitor candidate are never exceptions before Ch 39. The leader has no
threads.

**The bond web's sizes are data.** `BondWeb.score` ([BONDS.md](../../BONDS.md) §11) maps to three tiers,
calibrated by the bonds session's simulation (at 60 h: reckless 4 to 10, typical 34 to 40, devoted
42 to 50): **a small fire** (under 20), **strong** (from 20), **the whole village** (from 41). The
thresholds live in the datapack. Story conditions read the tier (`bond_web_tier strong`), never a
raw number.

**Scripted thread form** (bonds session): `{"thread": {"who": "role:x", "floor": "spark", "style":
"one_sided" | "fraying", "until": "<story flag>"}}`; it shows only after `story.kindling.awakened`.

## Journal documents and other ids

`doc.ledger_sample` (Ch 0), `doc.stipend_papers` (Ch 1), `doc.shelving_slip` (Ch 5),
`doc.delivery_page` (Ch 11): journal documents the case board (Ch 38) compares. `ans.player.feast`
(Ch 20, falls variant). `shared_moment bond.squad5_c.porter` (Ch 28.5). Act `saved_the_village`
(end of Ch 53; a lived deed worth 90 that forgives earlier bad deeds, so every finisher reaches Hero with the village). `world.roster.<role>.gone` (set when a role leaves the roster:
neutral aliases read by the ranks session): `hokage_4` at Ch 20 if `twist.fourth_fate = falls`; the bound candidate at Ch 39 if arrested; `sensei_2` and `elder_keeper` at Ch 51b.

## Tokens the story needs

`{they:<role>}`, `{them:<role>}`, `{their:<role>}`, `{theirs:<role>}`, `{themself:<role>}` and verb
helpers for rolled-look roles and the player; `{pet:role:teammate_b}` and `{pet:role:squad4_b}` (pet
names the player can choose).

## Answers (`ans.*`)

Player-scope string flags: `ans.<role>.<topic> = <option>`. The question tables in each
[character file](CHARACTERS/) are the source of truth for their options and payoffs; the arc
files show where each is asked. Naming: `ans.player.*` are the player's own choices that are not
answers to one character (how you describe the Leaf, your ramen order, your speech).

**Renamed in round 2:** `ans.player.bell_given` → `ans.player.cord_given` (`handed` / `together`);
`story.seed.bell_flicker` → `story.seed.cord_flicker`; the keepsake `bell` → `cord_tag`; the speech
choice "the bell" → "the cord tag". `ans.sensei_3.spared` keeps the Ch 25.3b definition; the
senseis.md question that used that id is `ans.sensei_3.saved_choice`.

Every `ans.*` flag must be read at least once after it is set (a callback line, a branch, or an
epilogue line). `quests.py --check` treats `ans.*` like seeds.

**Unset defaults.** Many questions are asked only at a bond level, in a bond quest or in a
hangout, so a player can reach a scene that reads an answer they were never asked. **Every read of
an `ans.*` flag in a main-path scene lists an `unset` branch**: a neutral default line that does
not assume an answer (examples: Ch 51a.4 b asks "Why?" and `come_back` defaults to "only if
sorry"; Ch 55.3 classmate_d says "Beside you, then."). The arc files and character files give the
unset line beside each read; `quests.py --check` rejects a main-path read with no `unset` branch.

The full list lives in the character files' "Questions for the player" tables and their "New
flags" sections. The index by chapter is generated from those tables (`quests.py --questions`);
[DIALOGUE_BRIEFS.md](DIALOGUE_BRIEFS.md) §4 explains where questions are asked.
