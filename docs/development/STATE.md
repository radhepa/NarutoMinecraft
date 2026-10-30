# Development state

**Phase/task:** P02-3, missing/invalid data and schema versions
([ROADMAP.md 13.5](../../ROADMAP.md#p02--make-state-reliable)). P00 and P01 passed (13.3); P02-1 and P02-2 done.
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd; pushed to `origin/dev`.
The story checkout on the Desktop keeps its unfinished work; story review stays paused.

## P02 queue

1. Done: `PlayerRecord` (versioned; rank, level, age stage, clan, difficulty) as a player attachment kept
   through death, and `SaveSeed` (seed, mode) on the overworld, set from the world seed on first start.
2. Done: `core/.../Seeds.java`, the owner copy of the engines' identical seed streams, and
   `SaveSeed.stream(domain, key)`. `SeedsTest` checks equal seeds, independence and the engines' numbers.
3. Missing/invalid data and schema-version handling; a versioned test save.
4. Minimal client sync of the record.
5. Prove lower mods do not import higher mods.

## Evidence (29 October 2026, Windows 11, JDK 25.0.5)

- P02-2 `./gradlew build`: passed, 377 tests (373 engine + 4 Core), 0 failures.
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

P02-3: decide what a record with a newer `version`, a missing field or an unknown id does on load (keep
the save, log a clear error, never wipe it), with Core unit tests and a small versioned test save.
