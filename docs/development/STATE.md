# Development state

**Phase/task:** P03-5, the test map's rules
([ROADMAP.md 13.5](../../ROADMAP.md#p03--make-the-village-tangible)). P00 to P02 passed (13.3).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd; pushed to `origin/dev`.
The story checkout on the Desktop keeps its unfinished work; story review stays paused.

## P03 queue

1. Done: Shinobi Village (`village/`, mod id `narutominecraft`): VF residents wear the Leaf wardrobe.
2. Done: the test street (`leaf_block`) with ten residents in their own flats, by day and at night.
3. Done (partly): deterministic resident identity and appearance, surviving reload. Still open: the
   Core save seed and Classic/Varied mode choosing the cast, role identities for the bound cast (from P02).
4. Done: the street's tea house, notice board and training yard; adventure protection and builder mode.
5. Map rules (vanilla and VF generation off on the test map).
6. A resident count and a measured route for performance.

P02 (done): `PlayerRecord`, `SaveSeed`, `Seeds`, `Saved.forgiving`, owner sync, `checkLayers`.

## Evidence (29 October 2026, Windows 11, JDK 25.0.5)

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

P03-5: the test map's rules: vanilla structures, mobs and VF's own village generation stay off on the
Leaf test map, set once by `/narutominecraft street` rather than by the gametest's commands, and checked
by the street gametest. Then P03-6 (resident count, performance route), then P04's first errand.
