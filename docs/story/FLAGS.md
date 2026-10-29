# Story flags

> **SPOILERS: for developers only.** Part of the [story bible](STORY_BIBLE.md).

Every flag the story sets, where it is set and where it is read. `story/seeds.json` is generated
from the **Seeds** table; `quests.py --check` warns about a seed never read or a read never set.
Flags are player scope unless they start with `world.`.

## Chapter flags

Every main chapter sets `story.ch<N>.done` when it ends (`story.chN1.done` to `story.chN7.done` for
the Night Watch). Gates in the character briefs use them ("never before `story.ch36.done`").

## Twist slots (bound at world creation)

| Flag | Values | Read in |
|---|---|---|
| `twist.traitor` | `librarian`, `medic`, `councillor`, `merchant` | Ch 25 (the slip), Chunin alibis, Ch 35 to 40, Ch 51 (turned), Ch 55 (ruling) |
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
| `story.seed.bell_flicker` | Ch 8.3 | Ch 24 |
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
| `story.teammate_b.path` (`stayed`, `nearly`, `left`) | Ch 26 | Ch 32, 51 |
| `story.teammate_b.parent_alive` | Ch 26 | Ch 51 |
| `story.seed.candle` | Ch 27.3 | Ch 49 |
| `story.seed.porter_ledger` | Ch 28.5 | Ch 49, 50 |
| `story.seed.genin_flame` | Ch 34.3 | N5, Ch 44 |
| `story.clue.list_found` | Ch 35.3 | Ch 38 |
| `story.archive.opened` | Ch 36 | Ch 46 |
| `story.accused` | Ch 38.6 | Ch 39, 40 |
| `story.suspected.<candidate>` | Ch 5 and later accusations | Ch 40 |
| `story.traitor.fate` (`arrested`, `turned`) | Ch 39.2 | Ch 50, 51, 55 |
| `story.seed.second_doubts` | Ch 41.4 | Ch 48 |
| `story.seed.lost_child_breaking` | Ch 44.2 | N3, Ch 47 |
| `story.nightwatch.pretend` | N5 | N6 |
| `story.nightwatch.undercroft` (`disbanded`, `sworn`, `exposed`) | N7 | Ch 50, 51 |
| `story.lost_child.home` (`nightwatch`, `shrine`) | N6 or Ch 47 | Ch 53, 55 |
| `story.clan.choice` (`kagari`, `own`) | Ch 46 | Ch 50, 55 |
| `story.hollow_crown.known` | Ch 49 | Ch 50 |
| `story.array.unbroken` (0 to 81) | Ch 50 | Ch 51 to 53 |
| `story.finale.reached` | Ch 52.3 | Ch 55 epilogue line |
| `story.finale.offered_leader` | Ch 53.5 | Ch 54.3 |
| `story.second.lives` | Ch 53.6 | Ch 54, 55 |
| `story.traitor.ruling` | Ch 55.3 | Epilogue |
| `story.suspected.keeper` | Any accusation of the keeper (Ch 4 to 38) | Ch 36 (his dry line) |
| `story.lost_child.family_known` | Ch 38 (the decoded list names her family) | Her file; Ch 47, 55 |
| `bond_flag parent_sorry` on `yugure_b_parent` | Ch 51.3 (when `ans.teammate_b.ask = sorry` and the parent apologises) | Ch 51.3 branch |
| `story.second.lives` also by `friendship [squad4_c, 6]` | Ch 53.6 | Ch 54, 55 |

## Tokens the story needs

`{they:<role>}`, `{them:<role>}`, `{their:<role>}`, `{theirs:<role>}`, `{themself:<role>}` and verb
helpers for rolled-look roles and the player; `{pet:role:teammate_b}` and `{pet:role:squad4_b}` (pet
names the player can choose).

## Answers (`ans.*`)

Player-scope string flags: `ans.<role>.<topic> = <option>`. The question tables in each
[character file](CHARACTERS/) are the source of truth for their options and payoffs; the arc
files show where each is asked. Naming: `ans.player.*` are the player's own choices that are not
answers to one character (how you describe the Leaf, your ramen order, your speech).

Every `ans.*` flag must be read at least once after it is set (a callback line, a branch, or an
epilogue line). `quests.py --check` treats `ans.*` like seeds.

The full list lives in the character files' "Questions for the player" tables and their "New
flags" sections; [DIALOGUE_BRIEFS.md](DIALOGUE_BRIEFS.md) collects them by chapter.
