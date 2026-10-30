# Development state

**Phase/task:** M3: finish the outstanding P05/P06 requirements, then P07, playing from the approved opening to
graduation without commands ([ROADMAP.md 13.4](../../ROADMAP.md#134-player-milestones-and-quality-gates)).
P00 to P02 passed (13.3); M2 passed 30 October 2026 (b2fc971 and earlier: this file at that commit).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd.

## Done since M2

- 5f21cc5: Hidden Leaf world preset. a36468c, 8bf6f40 (P06): chakra, hand signs, Academy techniques, guard, dodge.
- e92d2f6, f139632, d4e2ed2, 2348843 (P05): calendar, stipend, defeat wakes in flat 3a, chest and table, pets, the 29
  Beta 1 dishes, fatigue by the clock, Well Rested by comfort. Leaf worlds from before e92d2f6: recreate them.
- ed59bee, c4f4764 close P04. 8e873b3 (P05): the keeper's server-checked shop screen, weekly shelf and restocks.
- This file's commit (shop fixes): the training quest's keeper hands over the first tatami (quest action
  `give_item`); the screen is titled with the keeper's own shop, redraws after every click, and one rule says why a
  shop is shut; the gametest sends every take-out input at the window.

## Evidence (30 October 2026, JDK 25.0.5)

For the shop fixes: `./gradlew build`, `missions.py --check` and `:progression:runClientGameTest` passed
(`.local-dev/logs/p05shopfix-*.log`, screenshot `progression/build/run/clientGameTest/screenshots/0000_shop-screen.png`).

## Remaining

- P07: the opening and Academy campaign through graduation.
- P03: Varied's apartment roll, bound-cast role identities, Konoha loot tables and names.
- P05: hospital wake, level loss on death; the shop counter block, haggling, selling and orders.
- P06: animation, rebindable controls, full technique and stock coverage.

## Launch

`./gradlew :progression:runClient` (player `ShinobiTester`); Create World defaults to the Hidden Leaf. Game rule
`shinobi_core:varied_world` makes a Varied save. Pack: [PACK.md](PACK.md).

## Known shortcuts

One stand-in keeper sells for ten shops; the shop screen is a vanilla chest window, buying only, 45 lines; event
closings and keeper levels are ignored; the furniture shop is shut on day 1 (a Moonday), so the keeper gives the
first tatami; miso soup, soba and tamagoyaki are not sold, yakitori only on Market Day; quests run `set_flag`,
`give_ryo` and `give_item` only; the training fixture starts itself until P07; a dedicated server's default
level-type gets no map; fatigue has Story thresholds only; comfort ignores season, mess, plant and pet; undrawn dishes
show a stand-in sprite; a dead bound resident does not block a quest; the quest checker mirrors the street's plots.

## Blockers

P07 waits on the private story approval gate (ROADMAP 13.8); the story review is in progress.

## Next

Check the story gate, then P07's opening.
