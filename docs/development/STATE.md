# Development state

**Resumed (owner, 30 October 2026):** plan the whole village before building more. Done: [docs/konoha/](../konoha/README.md)
(master plan, district sheets, techniques, batch list K3 to K14).
**Phase/task:** Konoha, the owner's order of 30 October 2026: the whole village of KONOHA_BUILD.md, district by
district (ROADMAP §6: Beta 1, then Beta 2, Beta 3 and Later), before more quest or systems work. M3's story (P07) is
paused at 6fc02a7. **Branch/base:** `dev`, from `main` e9238bd. Names and dialogue are the merged `names` work: leave
them alone. Each resident a batch spawns calls `LeafNames.marker(v, marker)` after `setUUID`, before `addFreshEntity`.

## Done

- P05/P06 (e92d2f6 to c90629e), P07 engine and chapters 0 to 7 as quests (6fc02a7; 0 to 2 client-tested).
- Konoha K1 (442a511): `tools/konoha/layout.json` (`layout.py --check`/`--plan`) drives the paste: 3 streets,
  30 built plots, 31 planned, rotated and mirrored. Leaf Street, Sakura Lane (14 homes), Main Street, and canon first
  versions of the Ninja Academy, the Hokage Residence and the main gate with its wall. Quest places are saved as
  anchors (`TestStreet.PLACES`, the same list as layout.py ANCHORS and missions.py STREET_ANCHORS).
- Konoha K2 (this commit): Main Street's shops, each with a keeper living upstairs: Ichiraku, the grocer
  (`shop_house.py`), the furniture and weapon shops (`shop_large.py`), the tea house reworked. Stairs climb in a
  closed well from a level landing behind a door; tatami lies on the floor, level with the bed. Each keeper sells
  its own shop (`ShinobiProgression.SHOPS`). `LeafFlats.CLAIMS` gives a placed resident back the bed it stands by
  once, if VF handed beds out first (`LeafFlatsTest`).
- `names` merged (63110e1, owner-approved): resident names and dialogue.

## Villager track (branch `claude/villagers-eeb914`, for `dev`)

- Hidden Leaf UI: VF's talk window, journal and ledger and the shop window in washi paper, ink, green and orange with
  scroll rods and the leaf crest (`LeafUi`, screen mixins); the chat is replaced by `LeafChat`, a message scroll of
  cards with speaker name plates, a letter-by-letter reveal and answer cards, plus a wooden "Speak" bar.
- Player eyes: `PlayerEyes` draws VF's face planes (eyes, brows, blush, mouth) on the player, in the world and the
  creator's preview.
- Keyed clips: the ninja run (sprinting; residents running too), the ready stance (still with a kunai or shuriken),
  meditation (2 s crouched still), the victory cheer and the spar bow; spar partners bow, stand ready and cheer
  (VF residents through `ResidentModelMixin`).
- Evidence: `./gradlew build`; the three client gametests passed. Screenshots `leaf-eyes`, `leaf-talk`,
  `leaf-ledger`, `leaf-chat`, `leaf-chat-open` (village), `academy-ready`, `academy-ninja-run`, `academy-meditate`
  (combat), `shop-screen`, `session-won` (progression); the tests check each clip and the answer card's click.

## Evidence (30 October 2026, JDK 25.0.5)

`./gradlew build` passed (`.local-dev/logs/k2-build.log`); `layout.py --check` ok (34 plots built).
`:village:runClientGameTest` passed (`.local-dev/logs/k2-gt.log`): 29 residents, 30 plaques, paste 18.4 s, 27 of 29
asleep in their own beds. After the merge: build, `dialogue.py`, `creator.py`, `missions.py` and `layout.py --check`
passed; the client gametest with `LeafNamesGameTest` passed (`.local-dev/logs/merge-gt.log`): 27 of 29 asleep, the
day route 8.8 to 13.4 ms per tick, the night route 4.8 to 5.0. Screenshots: `village/build/run/clientGameTest/screenshots/*konoha-*`;
renders: `docs/renders/konoha/`.

## Remaining

- Konoha Beta 1: batches K3 to K14 of [BATCHES.md](../konoha/BATCHES.md), about 200 residents. Then Beta 2,
  Beta 3 and Later.
- P07: chapters 3 to 7 in a client; story stand-ins swapped for the real places.
- P03, P05, P06 leftovers as before (Varied's roll, the shop counter block, mentors, first-person poses).

## Launch

`./gradlew :progression:runClient` (player `ShinobiTester`); Create World defaults to the Hidden Leaf. Pack:
[PACK.md](PACK.md).

## Known shortcuts

The first-start grass fill walks the whole border block by block (about 20 s). The gate has no guards yet (no
barracks beds). One stand-in keeper sells for twelve shops. Guard needs an empty hand. Poses show in third person
only. On low RAM, run gametests with `JAVA_TOOL_OPTIONS=-Xmx3g` and `--max-workers=1`.

## Blockers

None.

## Next

K3 interiors ([BATCHES.md](../konoha/BATCHES.md)): kit furnishing helpers, lived-in rooms in every built resident
home (Sakura Lane, the Leaf Block's resident flats, the keepers above the shops). Then K4 facade pass, K5 layout
merge (the Academy moves to the Rock's foot), K6 terrain, K7 to K14 by district.
