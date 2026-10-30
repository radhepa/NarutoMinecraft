# Development state

**Phase/task:** P03-2, the test street and ten living residents
([ROADMAP.md 13.5](../../ROADMAP.md#p03--make-the-village-tangible)). P00 to P02 passed (13.3).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd; pushed to `origin/dev`.
The story checkout on the Desktop keeps its unfinished work; story review stays paused.

## P03 queue

1. Done: Shinobi Village (`village/`, mod id `narutominecraft`): VF residents wear the Leaf wardrobe.
2. A small test street and its markers; ten residents with homes and routines.
3. Role identities for the bound cast (moved from P02).
4. Map rules (vanilla and VF generation off on the test map).
5. A resident count and a measured route for performance.

P02 (done): `PlayerRecord`, `SaveSeed`, `Seeds`, `Saved.forgiving`, owner sync, `checkLayers`.

## Evidence (29 October 2026, Windows 11, JDK 25.0.5)

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

P03-2: register the Konoha decor blocks, paste the `leaf_block` blueprint on a flat test map with a VF
village marker and its twelve House Plaques, and spawn ten residents at its markers; a client gametest
shows each resident with its own flat and bed, walking by day and asleep at night.
