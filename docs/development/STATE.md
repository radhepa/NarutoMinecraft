# Development state

**Phase/task:** M3: finish the outstanding P05/P06 requirements, then P07, playing from the approved opening to
graduation without commands ([ROADMAP.md 13.4](../../ROADMAP.md#134-player-milestones-and-quality-gates)).
P00 to P02 passed (13.3); M2 passed 30 October 2026 (b2fc971 and earlier: this file at that commit).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd.

## Done since M2

- 5f21cc5: a new world is the Hidden Leaf preset; its first start pastes the street, border and spawn.
- a36468c, 8bf6f40 (P06): chakra, hand signs, Academy techniques, guard and dodge.
- The commit "P05: the ordinary day" (this file's commit): calendar ("Day N, Weekday" title, `Daily.day/weekday`),
  30 ryo stipend from day 2 (day 1 is the 100 ryo purse, economy.json `stipend.from_day`), Tired at 01:00 awake
  (Slowness I, chakra regen x0.75) cleared by a bed, a defeat wakes in flat 3a with the pack minus thrown tools
  (keep_inventory on the map), chest and crafting table in the flat, kitten/pup adoption from the keeper.

## Evidence (30 October 2026, JDK 25.0.5)

`./gradlew build` passed (`.local-dev/logs/p05-day-build.log`). `:progression:runClientGameTest` passed: `SessionGameTest`
adds stipend days 2 and 3, fatigue and recovery, chest and table, death wake, a tamed kitten (screenshots
`0006_session-chest` to `0008_session-kitten`; log `p05-day-progression-gametest.log`). `:village:` and
`:combat:runClientGameTest` passed (`p05-day-village-gametest.log`, `p05-day-combat-gametest.log`).

## Remaining

- P07: the opening and Academy campaign through graduation.
- P04-6: failure and retry at each quest boundary. P04-7: the quest checker (`tools/missions/missions.py`).
- P03: Varied's apartment roll, role identities for the bound cast, Konoha loot tables and names.
- P05: Exhausted/Collapse/Well Rested, hospital wake (no hospital on the map), level loss on death (no levels yet),
  dish items and their buffs, weekly stock and hours, a shop screen.
- P06: animation, rebindable controls, full technique and stock coverage.

## Launch

`./gradlew :progression:runClient` (player `ShinobiTester`). A new world needs no command: Create World defaults to
the Hidden Leaf. Game rule `shinobi_core:varied_world` makes a Varied save. Pack: [PACK.md](PACK.md).

## Known shortcuts

The tea house keeper sells the furniture, tea and adoption lines; the training fixture starts itself until P07; a
dedicated server's default level-type gets no map; one fatigue stage.

## Blockers

P07 waits on the private story approval gate (ROADMAP 13.8); the story review is in progress.

## Next

Check the story gate, then P07's opening.
