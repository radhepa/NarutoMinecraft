# Development state

**Phase/task:** M3: finish the outstanding P05/P06 requirements, then P07, playing from the approved opening to
graduation without commands ([ROADMAP.md 13.4](../../ROADMAP.md#134-player-milestones-and-quality-gates)).
P00 to P02 passed (13.3); M2 passed 30 October 2026 (b2fc971 and earlier: this file at that commit).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd.

## Done since M2

- 5f21cc5: new worlds are the Hidden Leaf preset (street, border, spawn).
- a36468c, 8bf6f40 (P06): chakra, hand signs, Academy techniques, guard and dodge.
- e92d2f6, f139632, d4e2ed2 (P05): calendar, stipend, defeat wakes in flat 3a, the flat's chest and table, pet adoption,
  the 29 Beta 1 dishes. Leaf worlds from before e92d2f6: recreate them.
- ed59bee, c4f4764 close P04: failure and retry, blocked steps, recasting, the quest checker.
- 2348843 (P05 fixes): fatigue by the clock (Tired 01:00, Exhausted 03:00 with damage -20%, collapse 06:00
  waking at noon); only a whole night's sleep or a defeat clears it; Well Rested by the flat's comfort; ramen restores
  chakra; the strongest dish buff stays.
- This file's commit (P05 shops): using the shop keeper opens a server-checked shop screen (a chest window) listing
  each open shop's lines with price and stock; a click buys after checking hours, stock, wallet and pack space. The
  week's shelf comes from life/economy Stock (save seed, mode, rank), restocks on each line's interval and survives
  reopening; a shut shop gets a polite line and no screen. The keeper keeps the tea house, furniture shop, Ichiraku,
  dango stand, grocer, fishmonger, Haruno store, Market Day stalls, clinic and shelter, each at its own hours.

## Evidence (30 October 2026, JDK 25.0.5)

`./gradlew build`, `missions.py --check`, `:progression:` and `:village:runClientGameTest` passed
(`.local-dev/logs/p04fix-*.log`); for the P05 fixes, `./gradlew build` and `:progression:runClientGameTest`
(`p05eatfix-*.log`); for the shops, `./gradlew build` and `:progression:runClientGameTest` (`p05shop-*.log`,
screenshot `progression/build/run/clientGameTest/screenshots/0000_shop-screen.png`).

## Remaining

- P07: the opening and Academy campaign through graduation.
- P03: Varied's apartment roll, bound-cast role identities, Konoha loot tables and names.
- P05: hospital wake, level loss on death; the shop counter block, haggling, selling and orders.
- P06: animation, rebindable controls, full technique and stock coverage.

## Launch

`./gradlew :progression:runClient` (player `ShinobiTester`); Create World defaults to the Hidden Leaf. Game rule
`shinobi_core:varied_world` makes a Varied save. Pack: [PACK.md](PACK.md).

## Known shortcuts

One stand-in keeper sells for ten shops; the shop screen is a vanilla chest window, buying only, 45 lines, and a
keeper with an open shop shows no talk window; event closings and keeper levels are ignored (newcomer prices); the
furniture shop is shut on day 1 (a Moonday), so the training fixture's furnish step hands over a tatami; cooked-only
dishes (miso soup, soba, tamagoyaki) are not sold, and yakitori only on Market Day; the training fixture starts itself until P07; a dedicated
server's default level-type gets no map; fatigue has Story thresholds only, a Darkness pulse for the darkened edge, no
short chakra jumps; comfort ignores season, mess, plant and pet; undrawn dishes show a stand-in sprite; a dead bound
resident does not block a quest; the quest checker mirrors the street's plots.

## Blockers

P07 waits on the private story approval gate (ROADMAP 13.8); the story review is in progress.

## Next

Check the story gate, then P07's opening.
