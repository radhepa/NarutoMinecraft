# Naruto Minecraft

A Minecraft mod of the Hidden Leaf, built on the Village Friends resident model. The wardrobe is
authored in Python under `tools/wardrobe/` and compiled into `src/main/resources/`. Read
[README.md](README.md) for the village and [CLANS.md](CLANS.md) for building a clan.

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
