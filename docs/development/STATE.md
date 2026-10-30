# Development state

**Phase/task:** P02-2, independent random streams from the save seed
([ROADMAP.md 13.5](../../ROADMAP.md#p02--make-state-reliable)). P00 and P01 passed (13.3); P02-1 done.
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd; pushed to `origin/dev`.
The story checkout on the Desktop keeps its unfinished work; story review stays paused.

## P02 queue

1. Done: `PlayerRecord` (versioned; rank, level, age stage, clan, difficulty) as a player attachment kept
   through death, and `SaveSeed` (seed, mode) on the overworld, set from the world seed on first start.
2. Independent random streams from the seed; deterministic-stream tests.
3. Missing/invalid data and schema-version handling; a versioned test save.
4. Minimal client sync of the record.
5. Prove lower mods do not import higher mods.

## Evidence (29 October 2026, Windows 11, JDK 25.0.5)

- P02-1 `./gradlew :core:runClientGameTest`: passed. `StateGameTest` creates a world, checks the new
  record and seed, changes both, quits, reopens the save and reads them back unchanged.
- `./gradlew build`: passed, 373 engine tests, 0 failures (engine results cached, inputs unchanged).
- P01 `./gradlew :core:runClientGameTest -Ppack`: passed; Core 0.1.0, VF 2.29.1, Fabric API, Minecraft 26.3.
- Not checked: the record surviving death (`copyOnDeath` is set, untested).
- Graph not refreshed: local graphify 0.9.76 is older than the committed graph.
- Not checked: importing the `.mrpack` into a real launcher (Loom's production client crashes natively here).
- Open from P01: the first/third-person animation spike, due before P06 combat content.

## Launch

`./gradlew :core:runClient` (player `ShinobiTester`). Pack: [PACK.md](PACK.md).

## Blockers

None.

## Next

P02-2: Core's `stream(domain, key) = SplitMix64(hash64(saveSeed, domain, key))` (ROADMAP.md, "One seed,
many streams"), reusing an existing engine's SplitMix64/hash64 if one fits, with unit tests that equal
seeds give equal streams and different domains stay independent.
