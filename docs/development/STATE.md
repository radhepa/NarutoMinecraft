# Development state

**Phase/task:** M3: finish the outstanding P05/P06 requirements, then P07, playing from the approved opening to
graduation without commands ([ROADMAP.md 13.4](../../ROADMAP.md#134-player-milestones-and-quality-gates)).
P00 to P02 passed (13.3); M2 passed 30 October 2026 (b2fc971 and earlier: this file at that commit).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd.

## Done since M2

- 5f21cc5: a new world is the Hidden Leaf preset; its first start pastes the street, border and spawn.
- a36468c, 8bf6f40 (P06): chakra, hand signs, Academy techniques, guard and dodge.
- e92d2f6, f139632 (P05): calendar, daily stipend, Tired, a defeat wakes in flat 3a, the flat's chest and table, pet
  adoption. Leaf worlds created before e92d2f6 lack keep_inventory, the chest and the table: recreate them.
- ed59bee, c4f4764 close P04: failure and retry, blocked steps, recasting, `missions.py --check` for quests.
- This file's commit (P05): the 29 Beta 1 Leaf dishes are edible items from the item data with their buffs (ramen and
  dango speed chakra regen, tea puts the night's fatigue off an hour, a meal halves its slowdown); the keeper sells the
  tea house's at catalogue prices. Rest stages: Tired, then Exhausted on a second night awake, a collapse on the third
  that wakes the player in the flat; a whole night in the flat's bed from before midnight gives Well Rested until noon.

## Evidence (30 October 2026, JDK 25.0.5)

`./gradlew build`, `missions.py --check`, `:progression:` and `:village:runClientGameTest` passed
(`.local-dev/logs/p04fix-*.log`); for the dishes and rest stages, `./gradlew build` and `:progression:runClientGameTest`
(`p05eat-*.log`).

## Remaining

- P07: the opening and Academy campaign through graduation.
- P03: Varied's apartment roll, role identities for the bound cast, Konoha loot tables and names.
- P05: hospital wake, level loss on death, weekly stock and hours, a shop screen.
- P06: animation, rebindable controls, full technique and stock coverage.

## Launch

`./gradlew :progression:runClient` (player `ShinobiTester`); Create World defaults to the Hidden Leaf. Game rule
`shinobi_core:varied_world` makes a Varied save. Pack: [PACK.md](PACK.md).

## Known shortcuts

The tea house keeper sells the furniture, tea and adoption lines (no keeper yet for Ichiraku, dango or grocer dishes);
the training fixture starts itself until P07; a dedicated server's default level-type gets no map; fatigue advances a
stage a night (not the clock thresholds), without Exhausted's damage penalty, and a collapse keeps the clock; Well
Rested ignores comfort; ramen speeds regen rather than restoring chakra; undrawn dishes show a base sprite or a vanilla
food; a dead but still bound resident does not block a quest; the quest checker mirrors the street's plots.

## Blockers

P07 waits on the private story approval gate (ROADMAP 13.8); the story review is in progress.

## Next

Check the story gate, then P07's opening.
