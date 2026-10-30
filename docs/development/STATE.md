# Development state

**Phase/task:** M3: finish the outstanding P05/P06 requirements, then P07, playing from the approved opening to
graduation without commands ([ROADMAP.md 13.4](../../ROADMAP.md#134-player-milestones-and-quality-gates)).
P00 to P02 passed (13.3); M2 passed 30 October 2026 (b2fc971). **Branch/base:** `dev`, from `main` e9238bd.

## Done since M2

- P05 (e92d2f6 to e43e580): calendar, stipend, flat, pets, dishes, fatigue, Well Rested, the keeper's shop screen.
  Leaf worlds from before e92d2f6: recreate them.
- P06 (a36468c to c90629e): chakra, signs, the six Academy techniques, guard, dodge, rebindable keys (Options >
  Controls > Shinobi), keyed clips on every player's model; winning the first-day spar teaches the techniques
  (`teach_technique`, 2a9a9df); smoke bomb, ninja wire and roof hopping (c90629e).
- 1104995: the keeper also sells the weapon shop's and Academy counter's stock; smoke bombs and wire craft.
- This file's commit (P07, paused): the story engine (scene and choose steps, chaining, cast steps, `set_rank`,
  `/shinobi answer <quest> <step> <option>`) and chapters 0 to 7 as quests; 0 to 2 client-tested, 3 to 7 checked by
  `missions.py --check` only. The owner asked on 30 October 2026 to build Konoha first, then return to the story.

## Evidence (30 October 2026, JDK 25.0.5)

`./gradlew build`, `:combat:runClientGameTest` (`.local-dev/logs/tools-*.log`) and `:progression:runClientGameTest`
(`story37-gt.log`: chapters 0 to 2 in Classic and Varied, chapter 3 starts) passed; screenshots under each module's
`build/run/clientGameTest/`.

## Remaining

- Konoha (owner's order): the Beta 1 districts of ROADMAP §6 from `tools/konoha/layout.json`.
- P07: chapters 3 to 7 in a client (Classic and Varied); story stand-ins swapped for the real Konoha places.
- P03: Varied's apartment roll, bound-cast role identities, Konoha loot tables and names.
- P05: hospital wake, level loss on death; the shop counter block, haggling, selling and orders.
- P06: mentors and lessons; first-person arm poses; air and dash taijutsu clips.

## Launch

`./gradlew :progression:runClient` (player `ShinobiTester`); Create World defaults to the Hidden Leaf. Game rule
`shinobi_core:varied_world` makes a Varied save. Pack: [PACK.md](PACK.md).

## Known shortcuts

One stand-in keeper sells for twelve shops (vanilla chest window, buying only, 45 lines); the keeper gives the first
tatami; a chapter that fails to start on a map is not retried; the training fixture starts itself; fatigue has Story thresholds only; comfort ignores season, mess, plant and pet; undrawn items use stand-in
sprites. Guard needs an empty hand; signs share the hotbar keys while weaving; poses snap and show in third person
only. Release clears vanilla nausea, blindness, darkness; First Aid has no downed state; every player roof-hops; any
tripwire trips mobs; tool numbers are fixed in `Tools`; the workbench is the vanilla crafting table.

## Blockers

None. The private story gate (ROADMAP 13.8) was approved by the owner on 30 October 2026 for the beta build (an
override after review round 28, not a locked pass; `story` branch, not merged into `main`).

## Next

Konoha K1: `layout.json` with `layout.py --check`/`--plan`, the map pasted from it (rotated plots, streets), then one
district per increment.
