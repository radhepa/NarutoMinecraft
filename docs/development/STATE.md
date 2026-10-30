# Development state

**Phase/task:** P04-3, flags, conditions and actions, and one branch
([ROADMAP.md 13.5](../../ROADMAP.md#p04--prove-a-complete-gameplay-loop)). P00 to P03 passed (13.3).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd; pushed to `origin/dev`.
The story checkout on the Desktop keeps its unfinished work; story review stays paused.

## P03 queue

1. Done: Shinobi Village (`village/`, mod id `narutominecraft`): VF residents wear the Leaf wardrobe.
2. Done: the test street (`leaf_block`) with ten residents in their own flats, by day and at night.
3. Done (partly): deterministic resident identity and appearance, surviving reload. Still open: the
   Core save seed and Classic/Varied mode choosing the cast, role identities for the bound cast (from P02).
4. Done: the street's tea house, notice board and training yard; adventure protection and builder mode.
5. Done: the Leaf map's rules (no monsters, raids, traders, TNT, arrows or fire spread).
6. Done: 11 residents on the street (ten flats and the tea house keeper) and the performance route.
   Open from 3 and 2, folded into later work as M2 needs them: Classic/Varied from the Core save seed,
   role identities, loot tables and names for the Konoha blocks.

## P04 queue

1. Done: a quest runtime and persistent journal: accept and complete one objective (`go` to an anchor).
2. Done: roles and map anchors, with clear errors when one is missing.
3. Flags, conditions and actions, and one branch.
4. Ryo through the Life wallet; one-time rewards.
5. A trade at the tea house.
6. Reload at each boundary, failure and retry.
7. The quest checker reports authoring errors (extend `tools/missions/missions.py`).

P02 (done): `PlayerRecord`, `SaveSeed`, `Seeds`, `Saved.forgiving`, owner sync, `checkLayers`.

## Evidence (29 October 2026, Windows 11, JDK 25.0.5)

- P04-2 `./gradlew build`: passed; `:progression:runClientGameTest` passed: the street binds its residents by
  marker role and job (`ShinobiVillage.ROLES`, saved with the level); the test errand casts the tea house keeper
  (`resident` by job) and the yard (`anchor` by tag) when accepted and keeps the cast in the journal; using the
  keeper through the client completes the `talk` step, then the yard the `go` step; a test quest whose anchor the
  map lacks is refused, naming the slot; roles survive reopening. Unit tests: casting and its errors, the checker's
  new refusals, the journal codec and saves from before the cast. Ponytail review: no tick crash on an old save's
  missing cast, one talk per click (main hand only), a talk step must name a resident slot. Open: under 5 s of
  server lag the keeper click failed twice in seven runs, retried clicks included (not reproduced since).

- P04-1 `./gradlew build`: passed; `:progression:runClientGameTest` passed: the new Shinobi Progression mod
  (`progression/`, `shinobi_progression`) loads quests from `data/*/quests/` through the mission engine's
  `Template`, the test errand is accepted with `/shinobi quest accept`, completes at the street's training yard
  (`go` to `anchor:training`), and the journal and the street's anchors survive reopening; a done quest cannot
  be taken again. Ponytail review: no crash on a step removed from the data (left in the journal until P04-6),
  reload with `/reload`, a broken quest file names itself, wrong-typed fields and `go` without a place are
  refused (unit-tested in `Quests`). Not yet: the pack does not ship Progression; journal commands are
  operator-only.

- P03-6 `./gradlew build`: passed; `:village:runClientGameTest` passed with the performance route: three stops
  (tea house, apartment block, yard), five seconds each, 11 residents. Baseline, server ms per tick on average:
  day 5.6 to 7.7, night 2.5 to 2.6; client 119 fps by day, 30 at night (the test client's frame cap, not load).
  Ponytail review: logged as a record, not a gate (an average, and shared CI runners are noisy).

- P03-5 `./gradlew build`: passed; `:village:runClientGameTest` passed: building the street turns off monster,
  patrol, phantom and trader spawns, raids, TNT and projectile block damage, and fire spread (`TestStreet.OFF`),
  and the gametest checks them; residents still walk and 9 of 11 sleep in their own beds. VF's generation needs
  no switch: the test map is flat with structures off. Ponytail review: mob griefing stays on (VF's farmers
  harvest and residents pick up items through it); a fire never goes out with spread off, so `StreetGuard` stops
  flint and steel and fire charges. Not yet: buckets, explosions of mobs a player places (shortcut).

- P03-4 `./gradlew build`: passed; `:village:runClientGameTest` passed: the street pastes the tea house
  (keeper upstairs, its own plaque and bed) and the new `training_yard` (targets, hay, VF's notice board)
  beside `leaf_block`; VF reads 12 houses with a bed each; all 11 residents keep their beds, 11 walk by day,
  9 sleep at 2 am (screenshot `test-street-yard`). `StreetGuard`: a survival player cannot break or build on
  the street or make a flat private; `/narutominecraft builder` can. Ponytail review: closed the plaque
  eviction, kept doors and beds usable with a block in hand, covered reshaping tools, checked every village
  holding a spot. The tea house needed its stair head walled and capped (VF floods room to room). Not yet:
  buckets, fire and explosions (shortcut: protection by village name until the map's regions).

- P03-3 `./gradlew build`: passed, 386 tests; `:village:runClientGameTest` passed: each resident's UUID
  comes from the world seed and its marker, so VF draws the same profile, name and look for it; ten
  different residents; reopening the save finds all ten with the same names, looks and flats. Building a
  second street on the same seed fails clearly instead of spawning duplicates. Not yet: the Core save seed
  and Classic/Varied mode (shortcut: the world seed); Leaf names and palettes.

- P03-2 `./gradlew build`: passed, 386 tests; `:village:runClientGameTest` passed: the 21 Konoha blocks
  register, `leaf_block` pastes on a flat map, VF reads 11 plaqued flats with a bed each, all ten residents
  keep the flat they were placed in, at least one walks by day and 8 or more sleep in their own beds at
  2 am (screenshot `test-street-day`). Two mixins (`LeafFlats`, unit-tested): VF fills plaqued houses in
  its own order, so residents landed in flats on other floors they could not path to. `/narutominecraft
  street` builds it in game (operators, empty ground). Ponytail review: scoped the bed seeding to Leaf
  flats and residents at home, a clear error without room for a plaque or on a village, one-character
  palette keys. Not yet: loot tables and names for the Konoha blocks; why up to two residents stay up at 2 am.

- P03-1 `./gradlew build`: passed, 385 tests; `:village:runClientGameTest` passed: four residents wear
  Leaf outfits (screenshot `leaf-residents`); `:core:runClientGameTest -Ppack` loads Core, Village and VF.
  A mixin hands VF a Leaf catalog; garments ship in VF's namespace. Ponytail review: fixed the CI VF build
  (`gradlew` not executable), the pack check's mod set and PACK.md. Not yet: Leaf palettes (VF's ten
  palette ids for now) and the population draw (every profession wears every collection).

- P02-4/5 `./gradlew build` and `:core:runClientGameTest`: passed, 383 tests; the client receives the
  changed record; `checkLayers` passes and fails on a planted Core-imports-Life file.
- P02-3 `./gradlew build :core:runClientGameTest`: passed, 383 tests (373 engine + 10 Core), 0 failures;
  reload gametest passed. Ponytail review: fixed a save blocked by a decode-only check, merged SaveSeed's codecs.
- P02-1 `./gradlew :core:runClientGameTest`: passed. `StateGameTest` creates a world, checks the new
  record and seed, changes both, quits, reopens the save and reads them back unchanged.
- P01 `./gradlew :core:runClientGameTest -Ppack`: passed; Core 0.1.0, VF 2.29.1, Fabric API, Minecraft 26.3.
- Not checked: the record surviving death (`copyOnDeath` is set, untested).
- Not checked: importing the `.mrpack` into a real launcher (Loom's production client crashes natively here).
- Graph not refreshed: local graphify 0.9.76 is older than the committed graph.
- Open from P01: the first/third-person animation spike, due before P06 combat content.

## Launch

`./gradlew :village:runClient` (Village + VF; player `ShinobiTester`), or `:core:runClient`. Pack: [PACK.md](PACK.md).

## Blockers

None.

## Next

P04-3: flags set by step actions and read by conditions, and the errand follows one `branch` (the shortcut in
`Journal.advance`); a gametest takes the branch and the flag survives reopening.
