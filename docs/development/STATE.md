# Development state

**Phase/task:** P02-1, one player record and seed survive a full save/reload
([ROADMAP.md 13.5](../../ROADMAP.md#p02--make-state-reliable)). P00 and P01 passed (13.3).
**Branch/base:** `dev` in `C:\Users\minal\NarutoMinecraft-dev`, from `main` e9238bd; pushed to `origin/dev`.
The story checkout on the Desktop keeps its unfinished work; story review stays paused.

## P02 queue

1. Core player record (versioned) with a save seed, kept on the server; survives quit/reload.
2. Independent random streams from the seed; deterministic-stream tests.
3. Missing/invalid data and schema-version handling; a versioned test save.
4. Minimal client sync of the record.
5. Prove lower mods do not import higher mods.

## Evidence (29 October 2026, Windows 11, JDK 25.0.5)

- `./gradlew build`: passed, 373 engine tests, 0 failures (dev `4ad03db`).
- `./gradlew :core:runClientGameTest -Ppack`: passed; Core 0.1.0, VF 2.29.1, Fabric API, Minecraft 26.3.
- Not checked: importing the `.mrpack` into a real launcher (Loom's production client crashes natively here).
- Open from P01: the first/third-person animation spike, due before P06 combat content.

## Launch

`./gradlew :core:runClient` (player `ShinobiTester`). Pack: [PACK.md](PACK.md).

## Blockers

None.

## Next

P02-1: the player record and seed in Core, with a client gametest that saves, reloads and compares.
