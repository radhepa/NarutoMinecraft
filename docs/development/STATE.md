# Development state

**Phase/task:** Konoha, the owner's order of 30 October 2026: the whole village of KONOHA_BUILD.md, district by
district (ROADMAP §6: Beta 1, then Beta 2, Beta 3 and Later), before more quest or systems work. M3's story (P07) is
paused at 6fc02a7. **Branch/base:** `dev`, from `main` e9238bd. Names and dialogue belong to the `names` branch: don't
edit name pools, name rolling or dialogue pools on `dev`.

## Done

- P05/P06 (e92d2f6 to c90629e), P07 engine and chapters 0 to 7 as quests (6fc02a7; 0 to 2 client-tested).
- Konoha K1 (this commit): `tools/konoha/layout.json` (`layout.py --check`/`--plan`) drives the paste: 3 streets,
  30 built plots, 31 planned, rotated and mirrored. Leaf Street, Sakura Lane (14 homes), Main Street, and canon first
  versions of the Ninja Academy, the Hokage Residence and the main gate with its wall. Quest places are saved as
  anchors (`TestStreet.PLACES`, the same list as layout.py ANCHORS and missions.py STREET_ANCHORS).

## Evidence (30 October 2026, JDK 25.0.5)

`./gradlew build` passed; `layout.py --check` ok; `missions.py --check` ok. `:village:runClientGameTest` passed
(`.local-dev/logs/konoha-landmarks-gt.log`): 25 residents, 26 plaques, paste 19.2 s, 23 of 25 asleep in their own
beds, the day route 4.6 to 8.8 ms per tick, the night route 3.1 to 3.6. Screenshots: `village/build/run/clientGameTest/screenshots/*konoha-*`;
renders: `docs/renders/konoha/`.

## Remaining

- Konoha Beta 1: shops (Ichiraku, grocer, furniture, weapon shop, Inuzuka clinic) and the market, the hospital,
  the shrine, the apartment blocks and the south homes, Hokage Rock, the clan gates and halls, the prologue hills,
  about 200 residents. Then Beta 2, Beta 3 and Later.
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

Konoha K2: the Main Street shops and the market district, one design per building in `tools/konoha/buildings/`.
