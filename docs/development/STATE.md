# Development state

**Phase/task:** M3: finish the outstanding P05/P06 requirements, then P07, playing from the approved opening to
graduation without commands ([ROADMAP.md 13.4](../../ROADMAP.md#134-player-milestones-and-quality-gates)).
P00 to P02 passed (13.3); M2 passed 30 October 2026 (b2fc971 and earlier: this file at that commit).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd.

## Done since M2

- 5f21cc5: Hidden Leaf world preset. a36468c, 8bf6f40 (P06): chakra, hand signs, Academy techniques, guard, dodge.
- P05: calendar, stipend, flat, pets, dishes, fatigue, Well Rested (e92d2f6 to 2348843); the keeper's shop screen
  and its fixes (8e873b3 to e43e580). Leaf worlds from before e92d2f6: recreate them.
- 72c995b (P06 controls and animation): every combat key, the twelve signs included, is a vanilla key
  mapping under Shinobi in Options > Controls, rebindable and saved (COMBAT.md defaults; guard on right click). The
  twelve signs, transition, fizzle, push-palms, block and four dodges are keyed in `tools/combat/animations.py` and
  play on every player from the synced stance (clip and start tick).
- This file's commit (P06 review fixes): worn armour follows the poses; the wheel on J and substitution on N
  (G and X stay for the pouch and a quick slot); a weave or guard ends a one-shot clip.

## Evidence (30 October 2026, JDK 25.0.5)

`./gradlew build` and `:combat:runClientGameTest` passed (`.local-dev/logs/animfix-*.log`; `:progression:runClientGameTest`
at 72c995b: `p06anim-*.log`); screenshots in `combat/build/run/clientGameTest/screenshots/`: controls-shinobi,
academy-weaving, academy-cast, academy-dodge, academy-guard (in iron armour).

## Remaining

- P07: the opening and Academy campaign through graduation.
- P03: Varied's apartment roll, bound-cast role identities, Konoha loot tables and names.
- P05: hospital wake, level loss on death; the shop counter block, haggling, selling and orders.
- P06: full technique and stock coverage; the taijutsu combo with its clips; first-person arm poses.

## Launch

`./gradlew :progression:runClient` (player `ShinobiTester`); Create World defaults to the Hidden Leaf. Game rule
`shinobi_core:varied_world` makes a Varied save. Pack: [PACK.md](PACK.md).

## Known shortcuts

One stand-in keeper sells for ten shops, vanilla chest window, buying only; the furniture shop is shut on day 1, so
the keeper gives the first tatami; quests run `set_flag`, `give_ryo` and `give_item` only; the training fixture starts
itself until P07; fatigue has Story thresholds only; event closings and keeper levels are ignored; miso soup, soba and
tamagoyaki are not sold, yakitori only on Market Day; a dedicated server's default level-type gets no map; comfort
ignores season, mess, plant and pet; undrawn dishes show a stand-in sprite; a dead bound resident does not block a
quest; the quest checker mirrors the street's plots. Guard on right click works only with an empty hand (a held kunai
throws); signs 1 to 9 share the hotbar keys, which do not switch slots while weaving; the wheel (G) and Substitution (X)
keys are not in COMBAT.md and sit on the pouch and quick-slot keys; poses snap at a clip's start and show in third
person only. `tools/combat/build.py --check` flags a Minecraft class name in a client mixin as a story-bible term.

## Blockers

P07 waits on the private story approval gate (ROADMAP 13.8); the story review is in progress.

## Next

Check the story gate, then P07's opening.
