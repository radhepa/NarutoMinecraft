# Development state

**Phase:** P01, make it boot ([card](phases/P01.md)). P00 is complete ([card](phases/P00.md)).
**Branch:** `dev` in the worktree `C:\Users\minal\NarutoMinecraft-dev`, based on `main` e9238bd.
The story checkout on the Desktop is untouched; story review stays paused.

## Done

- Increment 1: Shinobi Core (`core/`, mod id `shinobi_core`) boots in a real client with Fabric API.
- Audit fixes 1–18 in the engines and tools (mission desk, combat, life, bonds, dialogue, look); combat
  `--check` writes nothing; generated files are LF; CI in `.github/workflows/check.yml` (not yet run on GitHub).
- Increment 2: the pack manifest in `pack/` and the install procedure in [PACK.md](PACK.md). Changed
  paths: `pack/`, `build.gradle` (Loom declared once), `core/build.gradle` (`-Ppack`), `settings.gradle`,
  `gradle.properties` (VF and Fabric API pins), `docs/development/`.

## Evidence (29 October 2026, Windows 11, JDK 25.0.5)

- `./gradlew build`: passed, 373 engine tests, 0 failures.
- All authoring checks passed, including font checks; they leave the tree unchanged.
- `./gradlew :pack:mrpack`: `pack/build/pack/shinobi-modpack-0.1.0.mrpack`. Fabric API's SHA-1 and
  SHA-512 match Modrinth version `bNnaTiuM`; the VF jar matches `vf_sha256`.
- `./gradlew :core:runClientGameTest -Ppack`: passed. The log lists `shinobi_core 0.1.0`,
  `villagefriends 2.29.1`, `fabric-api`, Minecraft 26.3; it opened a world (screenshots saved).
- Not checked: importing the `.mrpack` into a real launcher. Loom's production-client task crashed
  natively (0xC0000005) on this PC while loading fonts, even without VF, so it was not kept.
- Graph not refreshed: local graphify 0.9.76 is older than the committed graph (0.9.97).

## Launch

`./gradlew :core:runClient` (player `ShinobiTester`). Pack: see [PACK.md](PACK.md).

## Blockers

None.

## Next

The first/third-person player-animation spike (P01). Village, Life, Combat and Progression assemblies
arrive with their first features.
