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
Combat is [docs/COMBAT.md](docs/COMBAT.md): data authored in `tools/combat/` (`python3 tools/combat/build.py --check`)
and the pure Java module `combat/core` (`./gradlew :combat:core:test`, `:combat:core:simulate`, `:combat:core:trace`).

## Commits

- Author every commit as `radhepa <radherpatel7@gmail.com>`:
  `git -c user.name=radhepa -c user.email=radherpatel7@gmail.com commit -m "..."`.
- No co-author, session or tool trailers, and no model names, in commits, branch names or files.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## Focused workflow

- Apply Ponytail 5 in full mode for this project: the smallest complete change, reuse existing tools and code, and concise responses. The official `ponytail@ponytail` plugin is enabled in project settings.
- Read the active handoff before continuing interrupted work. For the story review, use `STORY_CHECK_HANDOFF.md`; all plot details and review findings stay under `docs/story/`. Owner-facing responses contain status, scores and checks only.
- Start repository questions with a narrow `graphify query "<question>" --budget 1200`. Follow its source references and read only the needed passages. A graph is navigation, not proof: inspect new or stale sources directly and refresh after the revision batch.
- Do not repeatedly dump the full graph, report, story folder or whole repository. Cache the source locations and decisions already established in the current task. Give parallel reviewers distinct lenses and bounded source lists when independent review is authorized.
- Validate each coherent revision batch with the required handoff checks. Reuse matching passing results; rerun checks when edits, failures or unresolved risks justify them. Do not omit required validation to save tokens.
- Keep routine replies to the outcome, actual changes and verification. End with one brief line for anything not checked or a material risk; never invent tool use, review scores or measured savings.
