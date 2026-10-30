# Konoha build batches

The ordered build list for the [master plan](MASTER_PLAN.md). One bounded batch at a time; each
leaves the village pasting, tested and pushed. K1 and K2 are done (STATE.md). Coordinates and
footprints are in [DISTRICTS.md](DISTRICTS.md); how to build in [TECHNIQUES.md](TECHNIQUES.md).

## Every batch's checks

1. Designs: `python tools/konoha/buildings/<file>.py` for each touched design; renders of the touched
   buildings (`render_kit.building_sheet`), looked at before paste. Revert renders of untouched
   buildings (they churn bytes).
2. `python tools/konoha/layout.py --check` (and `--plan` when plots change).
3. Full build: `./gradlew build --max-workers=1` (log in `.local-dev/logs/`).
4. Client gametest (`:village:runClientGameTest`): residents and plaques counted, beds, at least n − 2
   asleep in their own beds at 2 am, the performance routes, the `konoha-*` screenshots looked at.
   `TestStreetGameTest`'s counts updated when plots change.
5. A review of the change (Ponytail lens), its fixes, then STATE.md and a commit to `dev`.

## Beta 1

| Batch | Scope | Done when |
|---|---|---|
| **K3 Interiors** | Kit furnishing helpers (TECHNIQUES §10.1). Lived-in interiors in every resident home already built: `home_plaster_2f` (all three palettes, Sakura Lane's 14), the Leaf Block's resident flats by household (1a, 4b, the others; 3a and the Varied candidates keep their open floor), the keepers' rooms above the grocer, the furniture and weapon shops, Ichiraku and the tea house | Renders show every room furnished to its programme; the walk line from each door to its bed is clear; the gametest's sleep count holds (n − 2) |
| **K4 Facade pass** | The kit's `plaster` gradient helper and the depth rules (TECHNIQUES §2 to §5) applied to every built design: posts, floor bands, recessed windows with sills and lintels, base steps, eaves with soffits and rafter ends, machiya fronts on the shop-houses, hidden light, no bare torches; the Academy's and the Residence's silhouettes checked against reference art; the gate's doors filling the opening, the wall's boards warmer, the Residence's round forecourt (MASTER_PLAN §8); the teal and blue roof palettes | Renders side by side with K2's show depth on every face; the gametest passes unchanged |
| **K5 Layout merge** | `docs/konoha/master_layout.json` merged into `tools/konoha/layout.json`: the master's streets and planned footprints replace the old planned plots; the **Academy moves to the Rock's foot** (61, -168) with its anchors; the street paste covers the new streets; the world border stays 660 until the outside is built | `layout.py --check` passes with 0 overlaps; `--plan` matches `master_plan.png`; the gametest finds the Academy anchors at the new site |
| **K6 Terrain and trees** | A terrain pass pasted before the plots, and the tree budget (TECHNIQUES §9) along the built streets: the river's channel and water, the falls' pool, the hospital terrace (+4), Shrine Hill (+6), the west bank (+2), the Rock's massing as a rough cliff; the street gradients (TECHNIQUES §7); it replaces the first-start grass fill | The core stays at y 64 and every built plot pastes unchanged; the start time is no worse than today's (about 20 s fill) |
| **K7 Market and Inuzuka** | Market Street: stall rows, the market shop-houses (barber, store, oil seller), the townhouse rows (`machiya_row`), the Akimichi compound; the rival tea houses on Shop Lane; the Inuzuka compound and its clinic, the cat shelter; their residents and keepers | Each stall and shop has its keeper; the market anchors resolve; about 50 more residents sleep |
| **K8 Hospital Hill** | The hospital on its terrace (five storeys, wards, the desk, roof tanks), the herb garden and herbalists' houses, the pharmacy, the Yamanaka compound and flower shop, the hill homes | The hospital anchors resolve; medics keep day and night shifts |
| **K9 The Foot and Central Leaf** | Clan gates and halls: Senju, Uzumaki memorial, Sarutobi, Shimura; the courier office; the Hyuga compound; the garden houses; Shrine Hill (torii, steps, hall, bell, plaques); the teachers' houses | Clan crests on the gates; the shrine anchors resolve |
| **K10 Housing** | The three apartment blocks and the round tower; the round-building family's drum house; the south homes (both blocks) and the park; `home_plaster_1f`, corner and garden house designs | About 85 more residents sleep; the rooftop route runs across the blocks |
| **K11 The Rock** | The Rock to about y 170 (MASTER_PLAN §4's sightline), its face, ledges and forest top; the four faces drafted (the owner finishes them); Rock Walk and the sealed door; the east stair and its lookout | The faces read from the main gate; the stair climbs with landings every 6 steps |
| **K12 The west bank** | The bridges (Rock Road's, the old bridge, Leaf Street's, the footbridge), the ferry landings and the island; the Uchiha wall, gate and main hall; the Aburame and Morino homes; the wall ring's west | Crossings walkable both ways; the ferry anchors resolve |
| **K13 The east** | The east quarters' homes, Kurama studio, Hatake and Yuhi homes; the Nara compound and deer forest, the memorial; the wall ring's east | The ring closes on the east side |
| **K14 The gate quarter and the prologue hills** | The barracks (six bunks: the gate's guards), the gate storehouse, the Shiranui house, the gate homes; the wall's south front completed with towers and the water gate; the prologue hills outside with the hideout and the ruined shrine | Guards man the gate; the prologue's places resolve; about 200 residents in all |

## After Beta 1

- **Beta 2:** the rest of the clan quarters (the Uchiha's homes and senbei shop, the minor clans),
  Shop Row's remaining shops, the bath house and the inn, the smithy, the training lanes' dojos, the
  outside (Training Ground 3, the lake and cliff grounds, farms, the east road and its waystation,
  bandit camps); the world border grows to about 1,200.
- **Beta 3:** the Chunin Exam stadium, the Forest of Death's fence, gates and tower.
- **Later:** the police HQ, two more round towers, festival dressing.
