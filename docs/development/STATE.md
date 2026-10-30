# Development state

**Phase/task:** P02-4, minimal client sync of the player record
([ROADMAP.md 13.5](../../ROADMAP.md#p02--make-state-reliable)). P00 and P01 passed (13.3); P02-1 to P02-3 done.
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd; pushed to `origin/dev`.
The story checkout on the Desktop keeps its unfinished work; story review stays paused.

## P02 queue

1. Done: `PlayerRecord` (versioned; rank, level, age stage, clan, difficulty) as a player attachment kept
   through death, and `SaveSeed` (seed, mode) on the overworld, set from the world seed on first start.
2. Done: `core/.../Seeds.java`, the owner copy of the engines' identical seed streams, and
   `SaveSeed.stream(domain, key)`. `SeedsTest` checks equal seeds, independence and the engines' numbers.
3. Done: `Saved.forgiving` reads a damaged or newer record leniently (known fields kept, the rest
   defaulted, an error logged) instead of Fabric dropping it; version-1 test saves in `core/src/test/resources/saves/v1/`.
   An unreadable seed still falls back to the world seed in Classic.
4. Minimal client sync of the record.
5. Prove lower mods do not import higher mods.

## Evidence (29 October 2026, Windows 11, JDK 25.0.5)

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

`./gradlew :core:runClient` (player `ShinobiTester`). Pack: [PACK.md](PACK.md).

## Blockers

None.

## Next

P02-4: sync the player record to its owner (Fabric attachment `syncWith`, owner only), checked in a
client gametest that reads the record on the client after the server changes it.
