# Development state

**Phase/task:** M3: finish the outstanding P05/P06 requirements, then P07, playing from the approved opening to
graduation without commands ([ROADMAP.md 13.4](../../ROADMAP.md#134-player-milestones-and-quality-gates)).
P00 to P02 passed (13.3); M2 passed 30 October 2026 (b2fc971 and earlier: this file at that commit).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd.

## Done since M2

- 5f21cc5: a new world is the Hidden Leaf preset; its first start pastes the street, border and spawn.
- a36468c, 8bf6f40 (P06): chakra, hand signs, Academy techniques, guard and dodge.
- e92d2f6, f139632 (P05): calendar, 30 ryo stipend from day 2 (one per skipped day), Tired at 01:00 cleared by a bed,
  a defeat wakes in flat 3a (if the map has it and the spot is free) minus thrown tools, the flat's chest and table,
  pet adoption. Leaf worlds created before e92d2f6 lack keep_inventory, the chest and the table: recreate them.
- The commit "P04: ..." (this file's commit) closes P04: a lost spar keeps the quest at its spar, reward unpaid
  (P04-6); a step missing its quest, step, anchor or resident waits blocked with one warning and shows so in
  `/shinobi journal`; `missions.py --quests` (also in `--check`) checks every quest file (P04-7, MISSIONS.md).

## Evidence (30 October 2026, JDK 25.0.5)

`./gradlew build` passed (`.local-dev/logs/p04-build.log`); `python tools/missions/missions.py --check` passed.
`:progression:runClientGameTest` passed (`p04-progression-gametest.log`): `SessionGameTest` loses a spar, retries,
wins and is paid once across a reload, and a two-day clock jump pays two stipends; `ErrandGameTest` blocks a step
whose anchor is gone. `:village:` and `:combat:runClientGameTest` passed at e92d2f6 (`p05-day-*-gametest.log`).

## Remaining

- P07: the opening and Academy campaign through graduation.
- P03: Varied's apartment roll, role identities for the bound cast, Konoha loot tables and names.
- P05: Exhausted/Collapse/Well Rested, hospital wake, level loss on death, dish buffs, weekly stock and hours, a
  shop screen.
- P06: animation, rebindable controls, full technique and stock coverage.

## Launch

`./gradlew :progression:runClient` (player `ShinobiTester`). A new world needs no command: Create World defaults to
the Hidden Leaf. Game rule `shinobi_core:varied_world` makes a Varied save. Pack: [PACK.md](PACK.md).

## Known shortcuts

The tea house keeper sells the furniture, tea and adoption lines; the training fixture starts itself until P07; a
dedicated server's default level-type gets no map; one fatigue stage; a dead but still bound resident does not block a
quest; the quest checker mirrors the street's plots from `TestStreet`.

## Blockers

P07 waits on the private story approval gate (ROADMAP 13.8); the story review is in progress.

## Next

Check the story gate, then P07's opening.
