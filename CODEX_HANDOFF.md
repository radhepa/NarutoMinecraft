# Codex handoff: Leaf names and dialogue

Branch `names`, worktree `C:\Users\minal\NarutoMinecraft-names`, cut from `dev` at `6fc02a7` (30 October 2026).
A separate agent is building the Konoha map on `dev` in `C:\Users\minal\NarutoMinecraft-dev` at the same time.
Your work merges into `dev` later.

## The job

1. **New Japanese names for every Leaf resident and shinobi.** This is the main task.
2. **Dialogue.** Write it once the names are done, or alongside them.

## 1. Names

### Today

- Residents are spawned by `village/src/main/java/dev/shinobi/village/TestStreet.java`, in the `"resident"` marker case. It sets only a UUID, and Village Friends (VF) picks the look and name from it.
- VF's names come from its own pools, `ResidentNames` in the read-only VF source at `C:\Users\minal\NarutoMinecraft-deps\village-friends-2.29.1\src\main\java\dev\villagefriends\ResidentNames.java`.
  - VF loads them from the data resource `data/villagefriends/villagefriends/names.json`, using a reload listener named `villagefriends:resident_names`.
  - The schema is `Data(version, pools[], surnames[], restrictedSurnames[], restrictedSurnameComplexions[])`, and each pool is `Pool(id, weight, complexions[], male[], female[], unisex[], surnames[])`.
  - A name may not contain spaces and may be at most 64 characters.
  - `ResidentNames.corrected(...)` renames a stored name that no longer fits the pool. This means existing residents get renamed when the pool changes, which is what we want.
- So every Leaf resident currently carries a borrowed, Western-style VF name. The owner wants brand-new Japanese names instead.

### The plan

The plan is already designed in ROADMAP.md, section "Names rolled per save" (search for that heading). Its rules also cover the player's surname.

- **Given names:** a new pool, `names/given.json` in Shinobi Village, with original Japanese given names by gender: male, female and unisex.
  - The path the tools expect is `village/src/main/resources/data/narutominecraft/names/given.json`. `tools/dialogue/dialogue.py` (`family_names()`) already reads it to reject literal names in text.
- **Family names:**
  - A clan member carries the clan's name, from the clan files in `data/combat/clans/` and the clan loader.
  - Clanless shinobi and civilians draw from `family_names` in `tools/wardrobe/population.json`.
  - That list has 50 common surnames. Replace or extend it with a larger, varied set.
  - The character creator picks the player's surname from the same pool (`village/look/.../Names.java`), so keep them consistent.
- **Name order:** given name first, then family name, such as "Shigure Nara". Honorifics keep their shape.
- **Leaf residents must stop using VF's pools.** The simplest route to try first is to ship our own `data/villagefriends/villagefriends/names.json` from Shinobi Village, with Japanese pools.
  - Prove in a real client that it wins over VF's copy.
  - If mod resource order makes it lose, ship it in the world datapack instead, or use a mixin or event in our mod.
  - Clan-quarter residents must carry their clan's surname. That likely needs a small hook where we spawn them, or a mixin on the name lookup.
- **Rolled per save:** names come from the save's `names` seed stream, and stay stable within a save.

### Rules for the names

- The names must be original. Do not reuse names of canon Naruto characters, which the dialogue compiler's canon check rejects.
- Use real, natural Japanese names in romaji, without macrons, such as Haruto, Aoi or Ren.
- Size the pools for about 300 residents with few duplicates. Aim for at least 150 given names per gender bucket.
- Text never contains a name. It uses only the tokens `{name:<ref>}`, `{given:<ref>}`, `{family:<ref>}`, `{hokage:<n>}` and `{player}`. See `village/dialogue/.../Names.java` and `Tokens.java`.

### Done when

- A new Hidden Leaf world shows only Japanese names, given name first, on residents' name tags and in dialogue and the journal.
- Clan residents carry their clan's name.
- Names stay the same after a reload.
- A JUnit or gametest check covers the pool loading and the clan surname.
- A client screenshot shows several named residents.

## 2. Dialogue

Read DIALOGUE.md first, especially sections 9 (mass production), 12 (story-gated pools) and 13 (what waits).

- The compiler and checker is `tools/dialogue/dialogue.py`. The bank currently holds about 15,800 pieces.
- The owner approved the story for the beta build on 30 October 2026. That unblocks the cast's voices, which DIALOGUE.md section 13 lists as waiting:
  - role-tagged greetings, topics, hangouts and life events;
  - their questions, 10 to 15 each;
  - the `player_ally` and `rival` barks beyond the pilot;
  - mission banter by role;
  - the story-gated pools.
- The briefs are on the `story` branch. Bring the approved story docs in first, as their own commit: `git checkout story -- docs/story`. Then use `docs/story/DIALOGUE_BRIEFS.md` and `docs/story/STORY_BIBLE.md`.
- Story-gated lines go only in `docs/story/dialogue/`. The compiler enforces where spoiler terms may appear.
- Lines use name tokens, never names.

## Rules (the owner's, the same for every agent)

- **Lean changes.** Make the smallest complete change, reuse existing tools and code, and add no abstractions nobody asked for. Mark any known limit with a `shortcut: <limit>, <when to upgrade>` comment.
- **Village Friends is read-only.** Never edit or push anything in `C:\Users\minal\NarutoMinecraft-deps\village-friends-2.29.1` or VF's GitHub repository. Change VF behaviour only through data, mixins or events in our mods.
- **Stay out of the map code.** Don't touch `tools/konoha/`, the map, the world preset, `LeafFlats`, or `TestStreet`'s plaque and bed code: the map agent owns those. If you must touch the resident spawn in `TestStreet`, keep it to a few lines and say so in the commit message.
- **Commits:**
  - Commit as `git -c user.name=radhepa -c user.email=radherpatel7@gmail.com commit -m "..."`.
  - Add no co-author, session or tool trailers, and no AI or model names, in commits, branches or files.
  - Commit to `names` only. Do not push, and do not merge into `dev` or `main`.
- **Files:** use UTF-8 with LF line endings. Generated-file checks compare exact bytes.
- **Spoilers:** reports to the owner give status, scores and checks only, never story content. Commit messages stay neutral.
- **Low RAM.** The machine has 16 GB, and the map agent runs client gametests. Run one client gametest at a time, and none while a `java` process from `NarutoMinecraft-dev` is running a client.

## Tools and checks

- **Java:** JDK 25 at `C:\Users\minal\AppData\Local\Programs\NarutoMinecraft\jdk-25.0.5+8`. Set `JAVA_HOME` to it.
- **Python:** `C:\Users\minal\OneDrive\Desktop\NarutoMinecraft\.venv\Scripts\python.exe` (3.13).
- **After each coherent change:**
  - `./gradlew build`, which builds every module and runs the JUnit tests.
  - `python tools/dialogue/dialogue.py`, the dialogue compile and its checks.
  - `python tools/missions/missions.py --check` and `python tools/combat/build.py --check`, if you touched their data.
- **Client proof:** `./gradlew :village:runClientGameTest` or `./gradlew :progression:runClientGameTest`. Look at the screenshots under `<module>/build/run/clientGameTest/screenshots/`.
- **Navigation:** `graphify query "<question>" --budget 1200` from the repository root, before grepping.

## When you finish

Update this file's status section below with the following, spoiler-free:
- what changed;
- the checks that passed;
- the screenshots;
- anything left.

Then tell the owner the branch is ready to merge.

## Status

Completed on 30 October 2026. The `names` branch is ready for a local merge into `dev`; nothing was pushed or merged.

### What changed

- Imported the approved `docs/story` documents from `story` as their own commit before writing dialogue.
- Added Japanese given-name pools: 223 male, 230 female and 185 unisex entries, without canon names or authored-word
  collisions. Expanded the ordinary family pool to 215 surnames and regenerated the creator's identical pool.
- Added a small mod-side hook after VF creates a resident profile. It rolls given-first names from the actual save's
  `names` stream in Classic and Varied, saves them on the resident and migrates settled residents' home/ledger names.
  Clan markers take their surname from the compiled clan registry shared with the creator. VF's source was not edited.
- Used the hook rather than a VF pool override: VF's validator requires its regional pool categories, its legacy-name
  correction does not migrate every stored name, and a UUID-only pool draw cannot vary Classic names by the save seed.
- The only TestStreet changes are the resident comment and one `LeafNames.marker(v, marker)` call after its UUID is set.
  Keep that call before `addFreshEntity` when reconciling the map branch's resident-spawn changes. No plaque, bed,
  map, preset, LeafFlats or `tools/konoha` code was changed.
- Added beta voices for 28 recurring roles, ten supplementary questions per role, 560 answer callbacks and 280
  asks-back replies, plus role combat/command barks, mission banter and gated public chapter reactions. Sources stay
  under `docs/story/dialogue`. No plot outcomes or scripted answer flags were invented.
- The compiled bank now has 17,448 pieces: 16,556 lines in 4,636 pools, 302 exchanges and 590 questions.
- Fixed story-tag matching: `story` indexes the source; the explicit `when` condition opens it. The compiler now
  refuses a gated source missing either, and generated dialogue is always UTF-8 with LF. Updated the code graph.

### Checks passed

- JDK 25 `gradlew build`: 400 JUnit tests, zero failures/errors across 67 suites. The tests include pool loading,
  all clan surnames, the shared player family pool, save-seed stability, a 300-resident duplicate-rate check,
  role selection, real reveal gates and answer memory after a ledger round trip.
- `python tools/dialogue/test_dialogue.py`: four authoring regression checks.
- `python tools/dialogue/dialogue.py` and `--check --report`: current generated bank, no duplicate/near-duplicate,
  name, spoiler, pronoun or child-safety violations; all 1,371 required bond pools present; zero new orphan bond keys.
- `python tools/creator/creator.py --check`, `python tools/missions/missions.py --check` and
  `python tools/combat/build.py --check`.
- `gradlew build :village:runClientGameTest`: real client checks for migration, male/female/nonbinary names, clan
  surnames, dialogue/ledger names and unchanged names after closing and reopening the save. Existing village,
  street and creator client tests also passed. Client runs waited for the map worktree's client slot.
- `git diff --check` and LF byte checks. Full local logs are in `build/names-*.log`.

### Screenshot

- [Four named residents, including clan residents](docs/renders/names/leaf-japanese-names.png), captured by the client
  test and visually checked. The original is `village/build/run/clientGameTest/screenshots/0008_leaf-japanese-names.png`.

### Remaining planned integration

- The new authored bank's live Context/condition/ledger/menu bridge remains Phase 0 work from DIALOGUE section 13;
  the current client uses VF's conversation UI. Names already work in that UI and its journal/ledger data.
- Later-arc scenes, exact scripted/bond-quest questions and full Varied voice/craft skins follow the approved
  briefs' work order after beta play and the remaining cast bindings. The shortcut and upgrade point are recorded
  in `docs/story/dialogue/README.md`. The current beta batch uses the curated role registers.
- The graph refresh is AST-only; its existing Gradle-parser warnings remain. No map-branch merge was attempted.
