# Development state

**Phase:** P01, make it boot ([card](phases/P01.md)). P00 is complete ([card](phases/P00.md)).
**Branch:** `dev` in the worktree `C:\Users\minal\NarutoMinecraft-dev`, based on `main` e9238bd.
The story checkout on the Desktop is untouched; story review stays paused.

## Done: P01 increment 1, Core boots

Shinobi Core (`core/`, mod id `shinobi_core`) is a Fabric mod that depends on Fabric API only. Its client
game test opens the real client, checks the loaded mods, creates a world and saves two screenshots.

Changed paths: `core/`, `settings.gradle` (Fabric plugin repository, `include 'core'`), `gradle.properties`
(version pins, 2 GB Gradle heap), `.gitignore` (`run/`), `CLAUDE.md` (pointer), `docs/development/`.

## Evidence (29 October 2026, Windows 11, JDK 25.0.5)

- `./gradlew :core:build`: passed.
- `./gradlew :core:runClientGameTest`: passed in 1 min 10 s. The log lists `shinobi_core 0.1.0`,
  `fabric-api`, `minecraft 26.3`, `fabricloader 0.19.5` and prints `Shinobi Core loaded`. Screenshots:
  `core/build/run/clientGameTest/screenshots/0000_core_title.png`, `0001_core_world.png`.
- `./gradlew test`: 357 engine tests, 0 failures.
- Village Friends 2.29.1 (VF `main` ccd1a2c, no tag or Maven artifact) builds with the same pins:
  `C:\Users\minal\NarutoMinecraft-deps\village-friends-2.29.1`, jar SHA-256 `13706bf9…c49e69e`.
- Not checked: the authoring tool checks (no tool or data changes).
- Graph not refreshed: local graphify is 0.9.76, the committed graph is 0.9.97; an update rewrites ~690
  cache files. Refresh once graphify is upgraded.

## Launch

From the worktree: `./gradlew :core:runClient` (player `ShinobiTester`, run folder `core/run/`).

## Blockers

None.

## Next

P01 increment 2: the minimal pack manifest (`pack/`) pinning Minecraft, Loader, Fabric API, VF 2.29.1
(jar built from ccd1a2c, by hash) and Shinobi Core, plus the separate test-world install procedure.
Then the first/third-person player-animation spike. Village, Life, Combat and Progression assemblies
arrive with their first features.
