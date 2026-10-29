# Story check handoff

For whoever finishes the story check and lock. This file is **spoiler-free**: the owner will play
the game and must not learn the twists, identities, fates or reveal timing. Every story detail
lives under `docs/story/`. Read those files yourself; never repeat their contents anywhere else.

## Where things stand

- **Repository:** `radhepa/NarutoMinecraft`. Every system is designed and merged into `main`:
  bonds, economy, home, roster and ranks, missions, items, the character creator, dialogue,
  combat and the Konoha build plan. Main is green: 357 JUnit tests, and every checker below passes.
- **Story:** on branch `story`, not yet on `main`. Only `docs/story/` differs from main.
  - **Rounds:** three review rounds have run, and none has passed yet.
  - **Round 3:** its revisions are committed (`099baed`), and the log entry for it is `bfc9b7e`.
  - **Round 4 (partial):** a partial pass followed, with fixes committed at `1e408d2`, the head of
    `story`. Its scores were a 7, b 7, c 8, d 8, e 8, f 7, but its reports were never written into
    `REVIEW_LOG.md`, so its blocking issues are lost.
- **Next step:** run a fresh, full round 4 on `1e408d2`. Log it as round 4, and note the partial
  pass's scores in that entry.

## Read first

1. `docs/story/STORY_BIBLE.md`: the index. It links the arcs, characters, ensemble, flags,
   rotations, world, systems and dialogue briefs.
2. `docs/story/REVIEW_LOG.md`: the rubric, every round's scores and blocking issues, and what
   changed after each round.
3. `ROADMAP.md` §1 and §8: the beta's chapters and hours, and the 60-hour budget the story must fit.

## The review process

Use the rubric that is already in `REVIEW_LOG.md`, and keep the earlier rounds' conventions.

- **Reviewers:** six fresh, independent reviewers each round, one per lens. Give each the story
  files and the rubric, but no opinion of what is good.
- **Lenses:**
  - (a) structure and pacing;
  - (b) characters and motivation;
  - (c) mystery fairness, across every rotation and slot;
  - (d) Naruto tone and canon (it should feel like the anime without copying it);
  - (e) player agency and how well it fits the systems;
  - (f) emotional payoff.
- **Scoring:** each lens scores 1 to 10 and lists blocking issues with their locations.
- **Pass rule:** a round passes when every lens scores 8 or more with no blocking issues.
- **Each round:**
  1. Run the six lenses.
  2. Log the round in `REVIEW_LOG.md`.
  3. Revise.
  4. Commit.
  5. Run the next round.
- **Round 4 focus:** check first that round 3's blocking issues are really fixed. The "What
  changed after round 3" list in the log is the claim to verify.

## Cross-system checks

The story must agree with the merged designs on `main`. Earlier rounds found mismatches here.

| Check against | What must agree |
|---|---|
| `docs/story/SYSTEMS.md` vs `MISSIONS.md`, `BONDS.md`, `SIDE_QUESTS.md`, `CLANS.md` | Every story-tied mission, bond beat, side quest and clan hook exists in those designs, or is listed as a request to that system |
| `docs/COMBAT.md`, `data/combat/` | Story bosses and fights use combat's boss ids, phase counts and squad sizes |
| `docs/RANKS.md`, `tools/roster/` | Named characters, ranks, teams and the Academy class match the roster |
| `DIALOGUE.md`, `docs/story/DIALOGUE_BRIEFS.md` | Voice briefs match the dialogue engine's conventions and tokens |
| `KONOHA_BUILD.md` | Story locations exist in the build plan, described neutrally there |
| `ITEMS.md`, `docs/HOME.md` | Money, gifts, keepsakes and the flat match those designs |

## Owner decisions the story must respect

These are settled. Do not reopen them.

- **The player:** always a clanless orphan. There is no clan-born start.
- **Money:**
  - No rent.
  - The Academy stipend is 30 ryo a day for the whole game, plus 100 ryo on day 1.
  - No story beat may assume the stipend stops.
- **Storage:** vanilla chests and barrels. There is no collection book.
- **Names:**
  - Given name first, then family name.
  - Every character has a last name.
  - Clanless characters are marked "no clan".
- **The week:** Moonday, Fireday, Waterday, Woodday, Metalday, Earthday, Sunday. Sunday is market
  day. The dialogue compiler rejects Monday through Saturday.
- **Kindling Bond:** the approved redesign in `BONDS.md`. None of it ships in the beta.
- **Dialogue:**
  - Unused talk is banked for up to 3 days per person.
  - "We already talked" lines are not marked.
  - Spending is global.
  - A close friend may ask each opinion question once.
  - Invented lore is kept.

## Checkers

Run these from the repository root after every change. All must pass before the lock.

```
python3 tools/dialogue/dialogue.py --check      # also lints story-bible terms leaking into public pools
python3 tools/combat/build.py --check           # also scans combat data for story-bible terms
python3 tools/missions/missions.py --check
python3 tools/roster/roster.py --check
python3 tools/items/items.py --check
python3 tools/creator/creator.py --check
python3 tools/konoha/catalogue.py --check
python3 tools/wardrobe/wardrobe.py --check
./gradlew test                                  # JDK 25
```

**About the spoiler lint:**
- `dialogue.py` treats as spoiler terms any proper nouns that `STORY_BIBLE.md` bolds and no
  public doc uses, plus everything in `docs/story/dialogue/spoiler_terms.txt`.
- When you add a new secret name, bold it in the bible or add it to `spoiler_terms.txt`.
- Bold list labels that end in a full stop or colon are ignored.

## Rules

- **Spoilers:**
  - They stay in `docs/story/` only.
  - Never put them in commit messages, branch names, public docs or anything said to the owner.
  - Use neutral commit messages, such as "Story: review round 4 revisions".
- **Commits:**
  - Author every commit as `radhepa <radherpatel7@gmail.com>`:
    `git -c user.name=radhepa -c user.email=radherpatel7@gmail.com commit -m "..."`.
  - No co-author, tool or session trailers, and no model or assistant names in commits,
    branch names or files.
- **Public docs:** any edit outside `docs/story/` (ROADMAP, SIDE_QUESTS and so on) must stay
  neutral.
- **Reports to the owner:** give scores and progress only, never story content.

## Locking and merging

1. When a round passes, add it to `REVIEW_LOG.md` and mark the story **locked** in `STORY_BIBLE.md`.
2. Bring `main` into `story`, then run every checker and the tests.
3. Squash-merge `story` into `main` as radhepa, with a neutral message such as "Story: locked".
   - Squash, don't merge: one old merge commit on `story` (`920a237`) has the wrong author, and
     squashing keeps it out of main's history.
4. Refresh the knowledge graph, `graphify update .` (`pip install graphifyy` if it is missing),
   then commit `graphify-out/` and push `main`.
5. Tell the owner, spoiler-free: "the story is locked and on main".

## Waiting on the lock

This is for the build team; nothing here is part of the story check.

- **Dialogue:** cast voices, story-gated pools (`docs/story/dialogue/`) and the story bosses'
  phase lines, written from `DIALOGUE_BRIEFS.md`.
- **Combat:** a final pass that the story bosses in `data/combat/` match the locked chapters.
- **Missions:** a final pass over the story-tied missions (`docs/story/SYSTEMS.md`).
