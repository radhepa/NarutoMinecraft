# Development state

**Phase/task:** M3: finish the outstanding P05/P06 requirements, then P07, playing from the approved opening to
graduation without commands ([ROADMAP.md 13.4](../../ROADMAP.md#134-player-milestones-and-quality-gates)).
P00 to P02 passed (13.3); M2 passed 30 October 2026 (b2fc971 and earlier: this file at that commit).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd.

## Done since M2

- 5f21cc5: Hidden Leaf world preset. a36468c, 8bf6f40 (P06): chakra, hand signs, Academy techniques, guard, dodge.
- P05: calendar, stipend, flat, pets, dishes, fatigue, Well Rested (e92d2f6 to 2348843); the keeper's shop screen
  and its fixes (8e873b3 to e43e580). Leaf worlds from before e92d2f6: recreate them.
- 72c995b to 5c7bde0 (P06): rebindable combat keys under Shinobi in Options > Controls (COMBAT.md defaults); sign,
  block, dodge and Academy taijutsu clips on every player's model; worn armour follows the poses.
- 5a74294 (P06): the rest of the Academy techniques. Release (woven Ram) clears nausea, blindness and
  darkness; Rope Escape (passive) moves 40% faster through cobwebs; Field First Aid (crouch, empty hand, use on a
  hurt ally) heals after 3 s, and moving off, standing up or a landed hit stops it.
- 2a9a9df: the quest action `teach_technique` (ROADMAP 5); winning the first-day spar teaches the six
  Academy techniques, so they need no command.
- This file's commit (P06): the Academy tools and roof hopping. A thrown smoke bomb bursts: mobs within 4 lose
  their target, others are blinded, a thrower inside goes invisible for 6 s; ninja wire strings a tripwire that
  holds a mob down 2 s; a sprint jump off leaves, logs, stairs or slabs costs a chakra point and pushes on (keyed clip).

## Evidence (30 October 2026, JDK 25.0.5)

`./gradlew build` and `:combat:runClientGameTest` passed (`.local-dev/logs/tools-build3.log`, `tools-combat-gt5.log`; screenshot academy-smoke); `:progression:runClientGameTest` at 2a9a9df (`teach-*.log`);
and earlier shots in
`combat/build/run/clientGameTest/screenshots/`.

## Remaining

- P07: the opening and Academy campaign through graduation.
- P03: Varied's apartment roll, bound-cast role identities, Konoha loot tables and names.
- P05: hospital wake, level loss on death; the shop counter block, haggling, selling and orders.
- P06: mentors and lessons (the first-day spar teaches all six at once); stock coverage (the tools and practice weapons are not sold yet); first-person arm poses; air and dash taijutsu clips.

## Launch

`./gradlew :progression:runClient` (player `ShinobiTester`); Create World defaults to the Hidden Leaf. Game rule
`shinobi_core:varied_world` makes a Varied save. Pack: [PACK.md](PACK.md).

## Known shortcuts

One stand-in keeper sells for ten shops, vanilla chest window, buying only; the furniture shop is shut on day 1, so
the keeper gives the first tatami; quests run `set_flag`, `give_ryo`, `give_item` and `teach_technique` only; the training fixture starts
itself until P07; fatigue has Story thresholds only; event closings and keeper levels are ignored; miso soup, soba and
tamagoyaki are not sold, yakitori only on Market Day; a dedicated server's default level-type gets no map; comfort
ignores season, mess, plant and pet; undrawn dishes show a stand-in sprite; a dead bound resident does not block a
quest; the quest checker mirrors the street's plots. Guard on right click works only with an empty hand (a held kunai
throws); signs 1 to 9 share the hotbar keys, which do not switch slots while weaving; poses snap at a clip's start and
show in third person only; the heavy plays its release without the windup. Release's
genjutsu are vanilla nausea, blindness and darkness; First Aid has no bleeding or downed state to treat; Rope Escape
loosens cobwebs only. Every player roof-hops (no lesson); any tripwire trips mobs, one wire per item, no tether or
binding; the smoke bomb's numbers are fixed in `Tools` (weapons/tools.json is not loaded).

## Blockers

P07 waits on the private story approval gate (ROADMAP 13.8); the story review is in progress.

## Next

Check the story gate, then P07's opening.
