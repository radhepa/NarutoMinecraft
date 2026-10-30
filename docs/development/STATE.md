# Development state

**Phase/task:** M3 (P07, with the outstanding P05/P06 requirements first): play from the approved opening to
graduation without commands ([ROADMAP.md 13.4](../../ROADMAP.md#134-player-milestones-and-quality-gates)).
M2 passed 30 October 2026. P00 to P02 passed (13.3); P03 and P04 queues done except the items below.
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd; pushed to `origin/dev`.
M2 evidence is for the commit "M2: the training spar, furnishing, sleep and the session proof" (see `git log`).
The story checkout on the Desktop keeps its unfinished work; story review is paused unless the M3 brief runs it.
Older evidence (P01 to P05-1): this file at commit b2fc971.

## M2 (Early P05 + P06): done

Creator on first join; the noncanonical `training.test.first_day` quest starts itself and names each step
("Next: ..."): walk to the yard, win a spar (new mod Shinobi Combat, `combat/`: each attack taken by the server
through Academy taijutsu's combo machine and stamina, combat-core damage, crit particles, sound, hit overlay,
"Spar won!" title, +30 ryo; the partner strikes back, a loss ends the bout and the next hit starts another),
talk to the keeper and buy a tatami, place it in flat 3a (the guard lets only furnishings down in that room),
sleep in that room's bed at night; reload keeps look, quest, wallet and tatami.

## Evidence (30 October 2026, Windows 11, JDK 25.0.5)

- `./gradlew build`: passed (log `.local-dev/logs/m2-build.log`).
- `:progression:runClientGameTest`: passed, `SessionGameTest` drives the whole M2 session through real client
  clicks and attacks; screenshots `progression/build/run/clientGameTest/screenshots/0000_session-creator` to
  `0005_session-reopened` (log `m2-progression-gametest.log`). `:village:runClientGameTest` and
  `:core:runClientGameTest -Ppack` (all five Shinobi mods, VF, Fabric API) passed.
- `:pack:mrpack` bundles Core, Village, Life, Combat and Progression with nested engines.
- Ponytail review: 0 blockers; fixed: only furnishings are placeable in the room, a click onto an existing floor
  mat does not finish the furnish step, no second partner before the yard's entities load, unknown step types
  and a spar without a place are refused (tests), a map that cannot cast the quest is not retried every tick,
  the quest waits for the flat anchor (older street saves), only the room's bed counts, spectators cannot spar.
  Marked shortcuts: hit lands on input, partner never guards or moves, sneak-attack is the heavy input; the
  training fixture starts itself until P07; the keeper also sells the furniture shop.

## Remaining from earlier phases

- P04-6: failure and retry at each quest boundary (the spar loss and retry exist, untested).
- P04-7: the quest checker (extend `tools/missions/missions.py`).
- P03: Varied's apartment roll (flat 3a in both modes), role identities for the bound cast, Konoha block loot tables and names.
- P05/P06 beyond M2: fatigue and the rest of the ordinary day, chakra, signs, techniques, guard/movement,
  animation, rebindable controls, pets, full stock and technique coverage (ROADMAP 13.4, 13.5).

## Launch

`./gradlew :progression:runClient` (every Shinobi mod + VF; player `ShinobiTester`). Create World defaults to the
Hidden Leaf preset (void); the first start pastes the test street, its border and the spawn on the street. Game rule
`shinobi_core:varied_world` (Create World, Game Rules) makes a Varied save. `/narutominecraft street` still builds the
street for operators. Pack: [PACK.md](PACK.md).

## Blockers

P07 needs the private story approval gate (ROADMAP 13.8, `STORY_CHECK_HANDOFF.md` in the Desktop checkout).

## Next

M3: check the story gate, then finish the outstanding P05/P06 requirements, then P07's opening and Academy
campaign through graduation without commands.
