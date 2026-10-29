# Naruto Minecraft

A Minecraft mod of the Hidden Leaf, built on the Village Friends resident model. The wardrobe is
authored in Python under `tools/wardrobe/` and compiled into `src/main/resources/`. Read
[README.md](README.md) for the village and [CLANS.md](CLANS.md) for building a clan. The friendship
system is [BONDS.md](BONDS.md) (time together: [LIFE_TOGETHER.md](LIFE_TOGETHER.md)); its engine is the pure Java module `life/bonds` (JDK 25:
`./gradlew :life:bonds:test`, `./gradlew :life:bonds:simulate` for the pacing tables). Missions are
[MISSIONS.md](MISSIONS.md): templates authored in `tools/missions/` (`python tools/missions/missions.py --doc`,
`--check`) and the pure Java generator `progression/missions` (`./gradlew :progression:missions:test`,
`:progression:missions:simulate`).
The home is [docs/HOME.md](docs/HOME.md); its engine is `life/home`, on top of the bond engine
(`./gradlew :life:home:test`, `./gradlew :life:home:simulate`).

## Commits

- Author every commit as `radhepa <radherpatel7@gmail.com>`:
  `git -c user.name=radhepa -c user.email=radherpatel7@gmail.com commit -m "..."`.
- No co-author, session or tool trailers, and no model names, in commits, branch names or files.

## graphify

This project has a knowledge graph at graphify-out/. `.graphifyignore` leaves out compiled assets,
renders and the one-file-per-piece wardrobe modules.

- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists.
  Use `graphify path "<A>" "<B>"` and `graphify explain "<concept>"` for focused questions.
- After modifying code, run `graphify update .` (AST-only, no API cost) and commit graphify-out/.
- graphify may not be installed in a fresh session: `pip install graphifyy` (two y's).
