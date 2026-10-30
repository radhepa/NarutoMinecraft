# The pack and a test world

The pack manifest lives in `pack/` ([ROADMAP.md](../../ROADMAP.md), "The pack: separate mods"). It builds a
Modrinth `.mrpack`: Minecraft 26.3, Fabric Loader 0.19.5 and Fabric API 0.161.0+26.3 by version and hash,
with Village Friends 2.29.1 and the Shinobi mods (Core, Village, Life, Combat, Progression) as jars inside the pack (none has a download yet). The
world is not part of the pack.

## Build the pack

1. Build Village Friends 2.29.1. It has no release, so build commit `ccd1a2c` with JDK 25 (its `gradlew` is
   not executable, so run it with `sh`). Shinobi Village compiles against this jar, so the root `./gradlew build`
   needs it too:

   ```bash
   git clone https://github.com/radhepa/Village-Friends-Minecraft-Mod village-friends-2.29.1
   cd village-friends-2.29.1 && git checkout ccd1a2c6cae176549dfb5d038bf4ebc6cbaac631 && sh ./gradlew :jar
   ```

   Copy `build/libs/village-friends-2.29.1.jar` to `build/deps/` in this repository, or pass
   `-Pvf_jar=<path>`. The pack refuses a jar whose SHA-256 differs from `vf_sha256` in `gradle.properties`.
2. `./gradlew :pack:mrpack` writes `pack/build/pack/shinobi-modpack-0.1.0.mrpack`.
3. `./gradlew :core:runClientGameTest -Ppack` checks the pack's mod set: a real client loads the five
   Shinobi mods, Village Friends (the pinned jar) and Fabric API, opens a new world and saves screenshots to
   `core/build/run/clientGameTest/screenshots/`.

## Install it for a test world

Keep testing in its own instance, never in your everyday Minecraft folder.

1. In a launcher that imports `.mrpack` files (the Modrinth App: *Add instance → From file*; Prism
   Launcher: *Add Instance → Import*), import `shinobi-modpack-0.1.0.mrpack`. The launcher downloads
   Minecraft, Fabric Loader and Fabric API and makes a new instance with its own `mods` and `saves`.
2. Launch the instance. *Singleplayer → Create New World*, name it `Shinobi Test`.
3. For a newer build, import the new `.mrpack` as a new instance. To remove a test setup, delete its
   instance; your other worlds are untouched.
