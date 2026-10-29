# Konoha: the build plan

How the Hidden Leaf gets built: the kit it is built from, every building and landmark with its
count and slice, every block it needs (vanilla first, custom only where vanilla cannot do it), the
process from layout file to zipped world, and what it costs. Read with [ROADMAP.md §6](ROADMAP.md#6-the-map)
(scale, border, what is pasted and what is built by hand, the district schedule) and
[CLANS.md](CLANS.md) (the 25 clans).

**No spoilers here.** Story locations are named neutrally ("the prologue hideout", "a hidden
room"). What they mean is in the developers-only story bible.

**Sources.** The Naruto wiki and image hosts are blocked from the build sessions, so the kit is
drawn from canon knowledge of the anime's Konoha. Anything marked *check against the art* must be
compared with reference images before it is built at scale.

**Machine-readable.** [`tools/konoha/blocks.json`](tools/konoha/blocks.json) (every custom block,
vanilla mapping and painting) and [`tools/konoha/buildings.json`](tools/konoha/buildings.json)
(every design program and building) are the source of truth. The tables and totals marked
*generated* below are written from them by `python3 tools/konoha/catalogue.py --write`.

## Contents

1. [The answer: how much it will be](#1-the-answer-how-much-it-will-be)
2. [Style guide: the Konoha kit](#2-style-guide-the-konoha-kit)
3. [Building catalogue](#3-building-catalogue)
4. [Block catalogue](#4-block-catalogue)
5. [Process](#5-process)
6. [Prototypes](#6-prototypes)
7. [Effort estimate](#7-effort-estimate)
8. [Registration notes for Phase 0](#8-registration-notes-for-phase-0)
9. [Open questions](#9-open-questions)

## 1. The answer: how much it will be

| | Count |
|---|---|
| Custom blocks | **175** blocks, **386** counting colour, wood, crest and sign variants separately; **684** new 16 px textures; 95 of them functional (doors, beds, seats, lights, containers, item displays, workstations, shop counters, boards). Includes the items session's 120 requests for stations, furniture, displays and shop interiors |
| Vanilla mappings | **54** needs met with vanilla blocks or combinations (roofs, walls, streets, the Rock, the forest), plus one Village Friends block reused (the easel) |
| Design programs | **31** Python programs (homes, apartments, shops, clan gates and houses, the wall, the forest's fence and trees, bridges, streets, training props, the Rock faces); 3 prototyped |
| Buildings | **110** homes, **15** apartment buildings, **55** shops, **75** clan builds, **30** landmarks, **8** training grounds, **704** Forest of Death pieces (660 trees, 44 gates), **142** wall modules |
| Agent effort | about **90 sessions** (~180 hours) for the whole village; **~81 sessions** (~162 hours) to the end of Beta 3 |
| Your hours in Minecraft | about **80 hours** to the end of Beta 3 (finishing the Rock, terrain and landmarks), **~105 hours** for the whole village; plus ~20 hours reviewing renders |

The detail behind each line is in sections 3, 4 and 7.

## 2. Style guide: the Konoha kit

Konoha is a hill town of plaster and tile under the Hokage Rock: boxy two- and three-storey
buildings in cream and terracotta plaster, low tile roofs in grey, green and orange-red, flat roofs
crowded with round water tanks, timber posts, shop fronts with awnings, noren and hanging signs,
paper lanterns, and utility poles with sagging wires along every street. Round towers and stacked
blocks break the skyline (*check the proportions against the art*).

### Shared palette

| Element | Blocks | Notes |
|---|---|---|
| Cream plaster | `smooth_sandstone`, trims and parapets in `cut_sandstone` | The kit's default wall (`kit.WALLS["cream"]`) |
| White plaster | `smooth_quartz`, trims in `calcite` | Hospital, offices, some homes |
| Terracotta plaster | `terracotta`, `white_terracotta`, `light_gray_terracotta` | Variety on residential streets |
| Orange-red walls | `smooth_red_sandstone`, `orange_terracotta`, `red_terracotta` | The Residence, the Academy (*check against the art*) |
| Floor bands | `terracotta`, `red_terracotta`, `brown_terracotta` | A stripe at every floor line, outside |
| Timber | `stripped_spruce_log`, `stripped_dark_oak_log`, `dark_oak_planks` | Corner posts, open shop fronts, galleries |
| Grey kawara | `deepslate_tile` stairs, slab, block + `grey_kawara_ridge` | Older houses, the shrine, clan halls |
| Green tile | `waxed_oxidized_cut_copper` stairs, slab, block + `green_kawara_ridge` | Homes; waxed so it never weathers |
| Orange tile | `waxed_cut_copper` stairs, slab, block + `orange_kawara_ridge` | Shops, the market street |
| Red tile | `red_nether_brick` stairs, slab, block + `red_kawara_ridge` | Temples and civic annexes (*check*) |
| Flat roof | `smooth_stone`, `smooth_stone_slab`, parapet in the wall's trim | With `water_tank` and `large_water_tank` |
| Base | `stone_bricks`, `cobblestone` | A raised floor one block above the street |
| Windows | `white_stained_glass_pane` (reads as paper), `glass_pane` for shops, `koshi_lattice` | |
| Streets | `dirt_path`, `coarse_dirt`, `packed_mud`, `gravel`; kerbs `cobblestone` | Mixed by street class by `roads.py` |

**Roof pitch.** Konoha's roofs are low. `kit.gable_roof(pitch="low")` climbs half a block a row in
alternating bottom and top slabs, the eave carries a lip of upside-down stairs, and the ridge gets a
kawara cap. Steep stairs roofs (`pitch="steep"`) are for shrines and clan halls only. A roof's span
with its overhang must be odd so the ridge has a centre row.

### By building type

| Type | Walls | Roof | Openings | Dressing |
|---|---|---|---|---|
| **Homes** | Cream, white or terracotta plaster on a stone base; timber corner posts; a band at the floor line | Low gable in green, grey or orange tile with a ridge cap; a small tiled canopy over the door | `koshi_door` entry, paper windows, `shoji_screen` and `fusuma_door` inside | Front garden behind a `bamboo_fence`, a `stone_lantern`, potted azalea, `laundry_line` on upper windows; tatami, futon, low table, tansu inside |
| **Apartment blocks** | Cream plaster, a band at every floor; timber gallery posts | Flat with a parapet, two or three `water_tank`s, a vent | Doors onto an outdoor gallery, stairs in the gallery's outer lane, paper windows | Fence railings, potted plants by doors, laundry lines, a `paper_lantern` by each flight |
| **Round towers** | Cream or white plaster, bands at every floor, windows in a ring | Flat, a `large_water_tank` on a steel stand | A central stair core | Balconies on the street side (*check against the art*) |
| **Shops** | Shop-house: plaster above, an open timber front below | Low gable in orange tile; deep street eave | Open bays with `noren` across the top, `awning` over, `koshi_lattice` upstairs | `shop_sign` on a bracket, `paper_lantern`s at the awning ends, benches out front; `shop_counter`, `produce_crate`, `flower_bucket`, `clothes_rack` inside |
| **Tea houses** | As shops, warmer timber | Orange or grey tile | Open front with `tea` noren | `tea_bench` with red felt, `wagasa` parasol, `tea_set`, `shogi_board`, a raised tatami room |
| **Ramen stand** | A small timber stall | Short orange eave over the counter | The counter open to the street, `ramen` noren | `ramen_counter`, `ramen_stool`s, `ramen_kitchen`, `large_red_paper_lantern`, `shop_board` |
| **Clan seats** | The clan's palette from its JSON (`clan_gate` maps P, S and A to plaster, timber and roof) | Grey kawara, steep, with `kawara_ridge_end` | A gate in a plaster compound wall | `clan_crest` on the gate, `clan_banner`s, the signature build (CLANS.md); Uchiha `crest_mural`s |
| **Academy** | Orange-red plaster (*check*), white trims | Low red or orange tile; a big 火 sign | Rows of glass windows; classroom doors are `shoji_door`s | The tree with a `tree_swing`, `target_post`s and `training_log`s in the yard; `academy_desk`, `blackboard`, `lectern` inside |
| **Hokage Residence** | Round, orange-red plaster (*check*) | A low round roof with 火 painted on it in `red_concrete` pixel art | A broad entrance; the Mission Desk inside | `leaf_crest` (large), `mission_desk`, `hokage_desk`, `paper_stack`, `scroll_shelf` archives |
| **Hospital** | White plaster, multi-storey | Flat, with tanks | Glass windows | `hospital_bed`, `hospital_curtain`, `iv_stand`, `medicine_cabinet`; a herb garden behind |
| **Shrine** | Timber and white plaster | Steep grey kawara with ridge ends | Torii (vanilla), open front | `shimenawa`, `shrine_bell`, `offering_box`, `ema_rack`, `komainu`, `stone_lantern`s, cherry trees |
| **Wall and gates** | A tall plaster face (`smooth_sandstone`, *check the colour*), `cut_sandstone` cornice, a stone footing | A walkway on top | Main gate: two tall doors in `green_terracotta` with あん in `red_concrete`, *check against the art* | Watch towers every ~125 blocks; the guard booth |
| **Bridges** | Timber decks on stone piers | — | — | Railings; `bridge_finial` caps on arched bridges |
| **Streets** | — | — | — | `utility_pole` every 12 blocks with `power_wire`, `street_lamp`s, `street_sign`s, `notice_board`s, trees |

## 3. Building catalogue

Every building and landmark, how it is built, and the slice that needs it. "Program" means a
design program pasted at fixed spots; "one-off + hand finish" means a landmark drafted once in
Python (a one-off program, never repeated) and finished by hand in the map world; "hand" means
built in the map world. Footprints are in blocks, x by z.

### Totals by slice

*Generated.*

<!-- gen:building-totals -->
| Group | Phase 0 | Beta 1 | Beta 2 | Beta 3 | Later | Total |
|---|---:|---:|---:|---:|---:|---:|
| Homes | 8 | 38 | 28 | 6 | 30 | 110 |
| Apartment buildings | 1 | 6 | 3 | 0 | 5 | 15 |
| Shops | 1 | 18 | 17 | 4 | 15 | 55 |
| Clan builds | 0 | 31 | 40 | 0 | 4 | 75 |
| Landmarks | 0 | 10 | 13 | 2 | 5 | 30 |
| Training grounds | 0 | 0 | 3 | 0 | 5 | 8 |
| Forest of Death | 0 | 0 | 0 | 704 | 0 | 704 |
| Wall | 0 | 16 | 25 | 23 | 78 | 142 |
| Street pieces (bridges, trees, poles) | 13 | 182 | 142 | 40 | 202 | 579 |
| Streets (km, laid by roads.py) | 0.15 | 2.4 | 2.0 | 0.8 | 3.0 | 8.35 |

Design programs: **31** (6 homes, 3 apartment buildings, 5 shops, 3 clan builds, 2 wall, 4 forest of death, 4 street pieces (bridges, trees, poles), 1 training grounds, 1 story, 2 landmarks), 3 of them prototyped.
<!-- /gen:building-totals -->

Housing check: 110 homes at about 1.6 residents, 15 apartment buildings at about 70% of their
flats, the clan seats' 39 nobles and the shopkeepers upstairs make about 300 residents for the
whole village and about 220 by the end of Beta 3 (ROADMAP §6: about 300 and about 200).

### Every building

*Generated.*

<!-- gen:buildings -->
#### Homes

| Building | Built from | Footprint | P0 | B1 | B2 | B3 | Later | Total | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| Two-storey plaster home | program `home_plaster_2f` | 11 x 11 | 5 | 14 | 8 | 2 | 10 | 39 | 2 to 3 residents; wall, roof and mirror rolled per plot |
| Single-storey home | program `home_plaster_1f` | 11 x 9 | 3 | 8 | 6 | 2 | 8 | 27 | 1 to 2 residents |
| Townhouse (one unit of a row) | program `machiya_row` | 5 x 11 a unit |  | 8 | 4 | 2 | 6 | 20 | Rows of 3 to 4 units on the market and residential streets |
| Corner house | program `home_corner` | 11 x 11 |  | 4 | 2 |  | 4 | 10 | Street corners |
| Garden house | program `home_garden` | 15 x 15 |  | 4 | 4 |  | 2 | 10 | Elders, well-off families; the Haruno house is one |
| Riverside house | program `home_riverside` | 9 x 13 |  |  | 4 |  |  | 4 | The riverside district |

#### Apartment buildings

| Building | Built from | Footprint | P0 | B1 | B2 | B3 | Later | Total | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| Leaf apartment block | program `leaf_block` | 35 x 15 | 1 | 3 | 1 |  | 1 | 6 | 12 flats (10 x 8 inside: main room, kitchenette, bathroom, genkan, closet, balcony); the player's block (flat 3a) and two more candidate blocks in Beta 1 |
| Round apartment tower | program `apartment_tower` | 13 x 13 |  | 1 |  |  | 2 | 3 | 12 flats; the skyline's round towers (check against the art) |
| Shops with flats above | program `shop_apartment` | 13 x 11 |  | 2 | 2 |  | 2 | 6 | 4 flats over 2 shops; the Beta 2 ones include the village inn, which lodges the foreign teams in Beta 3 |

#### Shops

| Building | Built from | Footprint | P0 | B1 | B2 | B3 | Later | Total | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| Small shop-house | program `shop_tea_house` | 11 x 11 | 1 | 3 | 3 |  | 3 | 10 | Tea houses (two rivals on one corner), dango, sweets, the test street's shop |
| Shop-house | program `shop_house` | 11 x 11 |  | 7 | 8 |  | 4 | 19 | Grocer, haruno store, the barber and market fillers (B1); scrolls, pawn, tools, tailor, medicine, metalworker, bookshop (B2) |
| Large store | program `shop_large` + hand dressing | 17 x 13 |  | 2 | 3 |  | 2 | 7 | The furniture shop and its showroom, and the weapon shop with its forge room (B1); the post office (B2); two warehouses by the market (B2) |
| Market stall row | program `market_stall` | 13 x 5 |  | 6 | 2 | 4 | 4 | 16 | Vegetables, fish, rice; exam-week stalls in B3 |
| Restaurant | program `restaurant` | 15 x 13 |  |  | 1 |  | 2 | 3 | The barbecue house (B2), an izakaya |

#### Clan builds

| Building | Built from | Footprint | P0 | B1 | B2 | B3 | Later | Total | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| Clan gate and wall | program `clan_gate` | varies |  | 15 |  |  |  | 15 | All 15 noble quarters in Beta 1, crest and palette from the clan JSON |
| Clan hall or clan home | one-off + hand finish | varies |  | 15 |  |  |  | 15 | 8 great clans' main halls and the 7 smaller clans' homes |
| Clan member's house | program `clan_house` | 11 x 11 |  |  | 16 |  |  | 16 | 1 to 3 per great compound |
| Clan signature features | hand | varies |  | 1 | 14 |  |  | 15 | Inuzuka kennels and clinic (B1, pets); deer forest, koi pond and dojo, greenhouse, shrines, studio, grove, moon platform (B2) |
| Minor clan mark | pasted variant + hand | varies |  |  | 10 |  |  | 10 | Carpenters' yard and a sealed shrine room by hand; a dojo and a metalworker's shop from programs; the rest homes dressed for the family |
| Vacant estate | one-off + hand finish | 40 x 40 |  |  |  |  | 4 | 4 | Sealed walled estates for player clans |

#### Landmarks

| Building | Built from | Footprint | P0 | B1 | B2 | B3 | Later | Total | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| Hokage Rock with four faces | sculpt + hand | ~200 x 60, 70 tall |  | 1 |  |  |  | 1 | rock_faces.py sculpts the faces, the user finishes; a hidden room's door at its foot |
| Hokage Residence | one-off + hand finish | ~33 round |  | 1 |  |  |  | 1 | Round, 火 on the roof; exterior and ground floor in B1, the Mission Desk and council gallery dressed in B2 |
| Ninja Academy | one-off + hand finish | ~48 x 32 |  | 1 |  |  |  | 1 | Classrooms, yard with target posts, library, workshop, the tree with the swing; exam hall dressed in B3 |
| Hospital | one-off + hand finish | ~32 x 24 |  | 1 |  |  |  | 1 | Wards, the wake room, the herb garden behind |
| Shrine | one-off + hand finish | ~30 x 40 |  | 1 |  |  |  | 1 | Torii, bell, offering box, wish plaques, komainu, toro |
| Main gate and guard booth | one-off + hand finish | ~30 x 12, 20 tall |  | 1 |  |  |  | 1 | あん on the doors |
| Ramen stand | one-off + hand finish | 7 x 6 |  | 1 |  |  |  | 1 | A VF tavern by bounds |
| Prologue hills: the hideout and a ruined shrine | hand | ~120 x 120 |  | 1 |  |  |  | 1 | South of the wall, inside the border |
| Jonin standby station | program `shop_house` variant + hand dressing | 11 x 11 |  |  | 1 |  |  | 1 | Beside the Residence; 6 workplace seats (jonin, day); opens to the player at Jonin |
| Gate barracks | program `leaf_block` variant | 14 x 11 |  | 1 |  |  |  | 1 | By the main gate: 6 bunks for the gate guards, the Shiranui neighbourhood next to it |
| Village park | hand | ~40 x 40 |  | 1 |  |  |  | 1 | Trees, a pond, benches; missions' park and pet hideouts |
| Potter's kiln yard | one-off + hand finish | 15 x 15 |  |  | 1 |  |  | 1 | A potter family's climbing kiln and drying racks; a potter's stall on the market street |
| Farmstead outside the gate | program `farm` + hand terrain | ~40 x 30 |  |  | 2 |  |  | 2 | Farmhouse, barn, pen and fields; an orchard and a woodlot nearby |
| Smithy and forge | one-off + hand finish | 11 x 11 |  |  | 1 |  |  | 1 | Behind the weapon shop |
| Bath house | one-off + hand finish | 17 x 15 |  |  | 1 |  |  | 1 |  |
| Ino-Shika-Cho memorial | hand | 9 x 9 |  |  | 1 |  |  | 1 | By the Nara forest |
| Ferry landing | hand | 9 x 7 |  |  | 1 |  |  | 1 | With the site of the future bridge |
| East road waystation | one-off + hand finish | 21 x 21 |  |  | 1 |  |  | 1 | With the roadside inn and its cellar; the east road's bridge, ford, bend, reeds and hill pass are terrain anchors |
| Bandit camp | camp program + hand | ~30 x 30 |  |  | 3 |  |  | 3 | Outside the wall |
| Border village (first far region) | pasted homes + hand | ~120 x 120 |  |  | 1 |  |  | 1 | Its own region, with a few outlying buildings |
| Forest of Death tower | one-off + hand finish | ~33 x 33, 40 tall |  |  |  | 1 |  | 1 | The preliminaries' arena inside |
| Chunin Exam stadium | one-off + hand finish | ~96 round |  |  |  | 1 |  | 1 | 64-block floor, ~150 seats, the Kage box |
| Police HQ, ANBU HQ, three more gates | one-off + hand finish | varies |  |  |  |  | 5 | 5 | Later arcs; their story locations are added as the arcs are written |

#### Training grounds

| Building | Built from | Footprint | P0 | B1 | B2 | B3 | Later | Total | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| Training Ground 3 | hand | ~60 x 60 |  |  | 1 |  |  | 1 | Three stumps, the memorial stone, the river |
| Training ground (pasted props) | program `training_ground` + hand terrain | ~50 x 50 |  |  | 2 |  | 5 | 7 | The lake ground and the cliff ground in B2; outer grounds later |

#### Forest of Death

| Building | Built from | Footprint | P0 | B1 | B2 | B3 | Later | Total | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| Forest of Death giant tree | program `giant_tree` | 4-7 thick |  |  |  | 260 |  | 260 | Seeded, four forms |
| Understorey tree | program `forest_tree` | 2-3 thick |  |  |  | 400 |  | 400 | Between the giants |
| Forest of Death gate | program `fod_gate` | 7 x 3 |  |  |  | 44 |  | 44 | On a fence swept along the forest's circle |

#### Wall

| Building | Built from | Footprint | P0 | B1 | B2 | B3 | Later | Total | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| Wall segment (16 blocks of the swept wall) | program `wall_segment` | 16 x 5, 14 tall |  | 14 | 22 | 20 | 70 | 126 | ~2,010 blocks of wall |
| Wall watch tower | program `wall_tower` | 9 x 9 |  | 2 | 3 | 3 | 8 | 16 |  |

#### Street pieces (bridges, trees, poles)

| Building | Built from | Footprint | P0 | B1 | B2 | B3 | Later | Total | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| Bridge | program `bridge` | varies |  | 2 | 2 |  | 2 | 6 | Flat bridges first, arched from B2 |
| Street and garden tree | program `village_tree` | varies |  | 60 | 40 |  | 50 | 150 |  |
| Utility pole (placed by roads.py) | roads.py | 1 x 1 | 13 | 120 | 100 | 40 | 150 | 423 | Every 12 blocks on main and ring streets |
<!-- /gen:buildings -->

### Markers

Blueprints and `layout.json` carry the markers the village systems read. Ranks and routines key on
`job`; a marker may pin `rank` when a role needs it, otherwise the rank comes from the job.

| Marker | Fields | Read by |
|---|---|---|
| `resident` | `group` (`any`, `civilian`, `clanless`, a clan id), `job`, optional `rank` | Village: residents from markers |
| `workplace` | `job`, `slots`, `shift` (`day`, `night`, `rotation`), optional `rank_min` | Routines: where a job is done |
| `bed`, `house_plaque` | position, facing | VF homes |
| `seat` | facing | VF Seat |
| `tavern_bounds` | `to` | The VF tavern hook |
| `door_anchor`, `candidate_flat` | `note` | Paste tool, quests |

Rank-bound workplaces: the Mission Desk (Residence ground floor, 3 slots, rotation, chunin; B2), the
jonin standby station (6, day, jonin; B2), the main gate's booth (2, day, chunin) and the gate
barracks (6 bunks; B1), the wall towers' night watch (1 each, night; 2 towers in B1), Academy
classrooms (5 teachers, day, chunin; B1), the hospital (6 medics, day and night, chunin and
special jonin; B1), the police HQ and ANBU HQ (later). Workers live in ordinary homes and flats.

### Shop sites

The items session's shops, with the building each goes in. Its slices come from
`data/items/shops.tsv` (branch `items`); the weapon shop moves to Beta 1 (a Beta 1 side quest is
there; it sells practice gear until Genin). Each shop's noren is `<trade>_noren` (`shop_noren` group);
shop displays show the shop's stock lines in order, with the slot counts the items session set.

| Shop | Building | Slice |
|---|---|---|
| `ichiraku` | Ramen stand (landmark) | Beta 1 |
| `grocer`, `haruno_store` | `shop_house` | Beta 1 |
| `fishmonger` | `market_stall` | Beta 1 |
| `tea_house`, `tea_house_rival` | Two `shop_tea_house` on one corner, one with the green awning | Beta 1, Beta 2 |
| `flower_shop` | `shop_house` front of the Yamanaka compound | Beta 1 |
| `furniture_shop` | `shop_large` with the showroom | Beta 1 |
| `weapon_shop` | `shop_large` with a forge room (forge, anvil, whetstone wheel, quench trough) | Beta 1 |
| `academy_supply` | The Academy workshop (public workbench) | Beta 1 |
| `inuzuka_clinic`, `cat_shelter` | Inuzuka compound; `shop_house` next to it | Beta 1 |
| `hospital_dispensary`, `pharmacy` | The hospital (herb room: apothecary table); `shop_house` by the hospital (Suzuran) | Beta 1 |
| `shrine_office` | The shrine | Beta 1 |
| `market_day_stalls` | `market_stall` rows on the market street | Beta 1 |
| `dango_stand`, `senbei_shop` | `shop_tea_house`; the senbei shop in the Uchiha quarter | Beta 2 |
| `barbecue_house` | `restaurant` | Beta 2 |
| `tool_shop`, `scroll_shop`, `tailor`, `pawn_shop` | `shop_house` (the scroll shop's calligraphy desk, the tailor's table) | Beta 2 |
| `kinoshita_yard` | Kinoshita mark (public workbench) | Beta 2 |
| `hagane_metalworks` | `shop_house` beside the forge | Beta 2 |
| `bath_house` | Bath house (landmark) | Beta 2 |
| `painters_studio` | Kurama clan home (VF easel) | Beta 2 |
| `festival_stalls` | `festival_stall` blocks on the main street | Beta 2 |
| `exam_stalls` | `market_stall` rows by the stadium | Beta 3 |
| `barber` | `shop_house` on the market street (barber chair, dresser mirror) | Beta 1 |
| `bookshop` | `shop_house` | Beta 2 |

Gathering anchors (right-click spots on a respawn timer, no breaking) the items session places
through `layout.json`: `gather:herb_garden` (behind the hospital), `gather:bamboo_grove` (by the
shrine), `gather:river` and `gather:river_bend` (iron sand, the riverside), `gather:cliff_nest` (the
cliff training ground), `gather:forest_floor` (the outer woods), `gather:forest_of_death`.

### Mission anchors

The missions session's anchors (`adventure/data/shinobi_adventure/missions/needs.json`, 133 of
them, 88 for Beta 1 and 2) are placed by `layout.json`. A dotted tag is one named place; an undotted
tag is generic and gets 4 to 8 instances spread over the districts. Beta anchors:

| Anchors | Where | Slice |
|---|---|---|
| `academy.grounds`, `academy.yard`, `academy.library` | Academy | Beta 1 |
| `residence.mission_desk`, `residence.records` | Residence ground floor (records: the archive room behind the desk) | Beta 2 |
| `gate.main`, `gate.travel_desk`, `gate.stores` | Main gate: the travel desk in the guard booth, a storehouse beside the barracks | Beta 1 |
| `hospital.desk`, `hospital.ward` | Hospital | Beta 1 |
| `shrine.steps`, `shrine.hall`, `shrine.roof` | Shrine | Beta 1 |
| `bathhouse`, `bathhouse.boiler` | Bath house (the boiler room at the back) | Beta 2 |
| `market.stall`, `market.grocer`, `market.tea`, `market.oil`, `market.fish` | Market street: `market_stall` rows, the grocer, the tea house, an oil seller's `shop_house`, the fishmonger | Beta 1 |
| `clan.nara.forest`, `clan.aburame.garden`, `clan.yamanaka.shop` | Clan quarters | Beta 2 |
| `main_street`, `alley.back`, `residential_lane`, `rooftop_route`, `dog_route`, `street_lamp`, `street_drain`, `poster_board` | Streets, by `roads.py` (lamps, drains and boards as street furniture) | Beta 1 |
| `client_home`, `client_roof`, `client_garden`, `vacant_home`, `hiding_spot`, `pet_hideout`, `overgrown_lot` | Homes and lots in every residential district (vacant homes are homes with no resident marker) | Beta 1 |
| `shop_storeroom`, `warehouse`, `office`, `festival_store`, `restaurant`, `barbecue_house`, `inn` | Shops' back rooms; two warehouses (`shop_large`); an office (`shop_house`); the festival goods store; the barbecue house; the village inn (`shop_apartment`, Beta 2) | Beta 1 to 2 |
| `park` | The village park | Beta 1 |
| `dojo`, `carpenters_yard`, `kiln_yard` | Dojo program; the Kinoshita yard; the potter's kiln yard | Beta 2 |
| `training_ground`, `riverbank`, `river_jetty`, `herb_garden`, `herb_slope` | Training grounds; the riverside (the ferry landing's jetty); behind the hospital; the slope below the Rock | Beta 2 |
| `farm_field`, `farm_barn`, `farm_pen`, `orchard`, `woodlot`, `forest_edge` | Two farmsteads and an orchard outside the gate, the woodlot and woods beyond | Beta 2 |
| `outside.*` (bandit camp and lookout, beehives, boar wallow, forest trail, hollow, ravine, training ground, wolf den, woodcutter path) | The hills and woods outside the wall, inside the border | Beta 2 |
| `road.*` (bridge, campsite, east bend, east waystation, ford, hill pass, inn cellar, reeds, thieves' den) | The east road and its waystation inn | Beta 2 |
| `border.*` (back room, healer, marker, market, outpost, pawnshop, post, square, stream) | The border village region | Beta 2 |

The later anchors (`capital.*`, `foreign.*`, `fort.*`, `pass.*`, `pilgrim.*`, `coast.*`, `far.*`,
`siege.*` and the rest) belong to far regions and later arcs and are placed when those are built.

### Story locations (neutral)

Where the story needs a place, it is part of a building above:

| Slice | Place | In |
|---|---|---|
| Beta 1 | The prologue hideout; a ruined shrine in the southern hills | Prologue hills |
| Beta 1 | A hidden room's door | Hokage Rock (`sealed_stone_door`) |
| Beta 1 | The library and its archive | Academy |
| Beta 1 | The shrine's wish plaques | Shrine (`ema_rack`) |
| Beta 2 | The memorial stone | Training Ground 3 (`memorial_stone`) |
| Beta 2 | Outlying buildings of the first far region | Border village region |
| Beta 2 | The council gallery | Hokage Residence |
| Beta 2 | A sealed shrine room | Tsuchigumo mark |
| Beta 2 | The post office | `shop_large` |
| Later | A hidden room in a clan home; the later arcs' places | Added as the arcs are written |

### Design programs

*Generated.*

<!-- gen:programs -->
| Program | Makes | First | Status |
|---|---|---|---|
| `home_plaster_2f` | Two-storey plaster home | Phase 0 | prototype |
| `home_plaster_1f` | Single-storey home with an engawa | Phase 0 | planned |
| `machiya_row` | Row of 3 to 4 narrow townhouses | Beta 1 | planned |
| `home_corner` | L-shaped corner house | Beta 1 | planned |
| `home_garden` | Larger house in a walled garden | Beta 1 | planned |
| `home_riverside` | Riverside house with a veranda over the bank | Beta 2 | planned |
| `leaf_block` | Leaf apartment block: walk-up, 2 to 4 storeys, three flats a landing (HOME.md flat plan) | Phase 0 | prototype |
| `apartment_tower` | Round apartment tower, 4 to 6 storeys, large tank on top | Beta 1 | planned |
| `shop_apartment` | Shops on the ground floor, flats above (also the inns) | Beta 1 | planned |
| `shop_tea_house` | Small shop-house with an open front, awning and noren | Phase 0 | prototype |
| `shop_house` | Two-storey shop-house with a display front | Beta 1 | planned |
| `shop_large` | Wide store with a showroom (furniture, weapons, post office) | Beta 1 | planned |
| `market_stall` | Row of open market stalls | Beta 1 | planned |
| `restaurant` | Restaurant with a dining hall (barbecue house, izakaya) | Beta 2 | planned |
| `clan_gate` | Clan gate with its stretch of compound wall, crest and palette from the clan JSON | Beta 1 | planned |
| `clan_house` | A clan member's house in the clan's palette | Beta 2 | planned |
| `dojo` | Small dojo (Namiashi, the Gekko's hall, training halls) | Beta 2 | planned |
| `wall` | Village wall: a profile swept along the wall's circle in 16-block segments | Beta 1 | planned |
| `wall_tower` | Watch tower on the wall | Beta 1 | planned |
| `fod_fence` | Forest of Death fence swept along its circle | Beta 3 | planned |
| `fod_gate` | Forest of Death numbered gate | Beta 3 | planned |
| `giant_tree` | Giant tree, 4 to 7 thick and 60 to 90 tall, four forms (straight, arched roots, hollow, leaning) | Beta 3 | planned |
| `forest_tree` | Understorey tree for the forest and the outer woods | Beta 3 | planned |
| `village_tree` | Street and garden trees: cherry, pine, maple | Beta 1 | planned |
| `bridge_flat` | Flat timber bridge | Beta 1 | planned |
| `bridge_arched` | Arched bridge with giboshi posts | Beta 2 | planned |
| `training_props` | Training-ground prop sets: target lines, post rows, log circles | Beta 1 | planned |
| `roads` | roads.py: streets, kerbs, poles and wires, lamps from layout.json polylines | Phase 0 | planned |
| `camp` | Camp kit: tents, fire, crates (bandit camps, forest camps) | Beta 2 | planned |
| `rock_faces` | rock_faces.py: the Hokage Rock faces as voxel sculpts from depth maps | Beta 1 | planned |
| `farm` | Farmhouse, barn, pen and field plots | Beta 2 | planned |
<!-- /gen:programs -->

## 4. Block catalogue

**Vanilla first.** A custom block exists only where vanilla cannot make the piece at the kit's
scale: round tanks and lanterns, thin paper and cloth, signs and crests with text, and anything
that must work (sliding doors, futons, seats, stations, shelves that show their goods). Everything
else is a mapping below.

**Shared with the items session** (branch `items`, `data/items/block_requests.json`). Items owns
each furniture piece's item, price and source, the station screens and recipes, and what a display
shows; this catalogue owns the block: id, model, collision and states. Where both had a piece, the
items ids won (`tansu_chest`, `folding_screen`, `andon_lamp`, `bench_red_cloth`, `festival_stall`,
...); `tatami` stays (asked of items instead of `tatami_mat`); `potted_fern` is vanilla; the easel is
VF's `easel_canvas`. One `keepsake` stand shows any of the 40 keepsakes, and the 26 displays share
one item-rendering block entity.

### Totals

*Generated.* Variants count separately (a red and a white lantern are two blocks in game); a
block's slice is the first slice that needs any of its variants.

<!-- gen:block-summary -->
| Group | Blocks | With variants | Textures | Functional |
|---|---:|---:|---:|---:|
| Roofs | 5 | 15 | 37 | 0 |
| Facades and shop fronts | 10 | 71 | 102 | 3 |
| Crests and banners | 4 | 58 | 99 | 0 |
| Interior fittings | 5 | 13 | 26 | 2 |
| Story pieces | 2 | 4 | 7 | 1 |
| Lanterns | 2 | 7 | 16 | 2 |
| Streets | 8 | 22 | 30 | 2 |
| Festival | 5 | 9 | 17 | 3 |
| Shrine | 6 | 8 | 16 | 4 |
| Furniture (the Leaf set) | 39 | 79 | 137 | 19 |
| Training | 6 | 7 | 13 | 4 |
| Academy, Residence, hospital, stadium | 15 | 20 | 45 | 7 |
| Shops and food | 27 | 27 | 50 | 13 |
| Gardens | 2 | 3 | 4 | 0 |
| Clan signatures | 3 | 6 | 6 | 0 |
| Crafting stations | 9 | 10 | 26 | 8 |
| Displays (item-rendering) | 27 | 27 | 53 | 27 |
| **All custom blocks** | **175** | **386** | **684** | **95** |

| By slice (new that slice) | Phase 0 | Beta 1 | Beta 2 | Beta 2.5 | Beta 3 | Later | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| Custom blocks (first needed) | 11 | 112 | 46 | 0 | 3 | 3 | 175 |
| Custom block variants | 21 | 203 | 142 | 0 | 11 | 9 | 386 |
| Vanilla mappings | 23 | 15 | 10 | 0 | 5 | 1 | 54 |

Complexity: 92 simple, 71 medium and 12 complex blocks (259, 108 and 19 with variants). Prototyped now: 11 blocks, 21 with variants.
<!-- /gen:block-summary -->

### Vanilla mappings

*Generated.*

<!-- gen:vanilla -->
| Need | Vanilla blocks | Use | First |
|---|---|---|---|
| Cream plaster walls | smooth_sandstone; cut_sandstone for trims and parapets | The kit's main wall | Phase 0 |
| White plaster walls | smooth_quartz; calcite for trims | Hospital, shrine offices, some homes | Beta 1 |
| Terracotta plaster walls | terracotta, white_terracotta (pale pink), light_gray_terracotta | Homes and shops for variety | Phase 0 |
| Orange-red walls | smooth_red_sandstone, orange_terracotta, red_terracotta | The Residence and Academy (check against the art) | Beta 1 |
| Floor-line bands | terracotta, red_terracotta, brown_terracotta | The horizontal stripe at each floor | Phase 0 |
| Timber posts and beams | stripped_spruce_log, stripped_dark_oak_log, dark_oak_planks | Corner posts, open fronts | Phase 0 |
| Floors | spruce_planks, oak_planks; packed_mud for earth-floored shops; polished_andesite for entries | Inside every building | Phase 0 |
| Grey kawara roof | deepslate_tile_stairs, deepslate_tile_slab, deepslate_tiles | Low pitch in alternating slabs, steep in stairs | Phase 0 |
| Green tile roof | waxed_oxidized_cut_copper stairs, slab, block | Waxed so it never weathers | Phase 0 |
| Orange tile roof | waxed_cut_copper stairs, slab, block | Waxed | Phase 0 |
| Red tile roof | red_nether_brick stairs, slab, block | Temples and the Residence's annex (check) | Beta 1 |
| Flat roofs | smooth_stone, smooth_stone_slab; parapet in cut_sandstone | Apartments, the hospital | Phase 0 |
| Foundations | stone_bricks, cobblestone, mossy_stone_bricks | Raised floors | Phase 0 |
| Paper windows | white_stained_glass_pane | Reads as shoji from outside | Phase 0 |
| Glass windows | glass_pane | Shops, the hospital | Phase 0 |
| Barred windows | iron_bars | The Morino house, cells | Beta 2 |
| Railings | spruce_fence, dark_oak_fence | Galleries, balconies; dark_oak_fence as a coarse lattice until koshi_lattice lands | Phase 0 |
| Swinging doors (placeholders) | spruce_door, dark_oak_door | Replaced by koshi_door and shoji_door in Beta 1 | Phase 0 |
| Shutters | spruce_trapdoor | Until amado lands | Phase 0 |
| Streets | dirt_path, coarse_dirt, packed_mud, gravel | roads.py mixes them by street class | Phase 0 |
| Kerbs and steps | cobblestone, stone_brick_slab, smooth_stone_slab | Street edges, house steps | Phase 0 |
| Stone-paved squares | polished_andesite, stone_bricks, smooth_stone | In front of the Residence and the Academy | Beta 1 |
| Gardens | grass_block, moss_block, azalea, flowering_azalea, ferns, flower_pot | Front gardens | Phase 0 |
| Bamboo | bamboo, bamboo_block, bamboo_fence (takegaki fence) | Fences, groves | Phase 0 |
| Cherry trees | cherry_log, cherry_leaves | Streets and the shrine | Beta 1 |
| Stepping stones | smooth_stone_slab, andesite | Gardens and the shrine | Beta 1 |
| Koi pond | water, lily_pad, tropical fish | Hyuga estate, gardens | Beta 2 |
| Torii | red_concrete pillars and tie beam, black_concrete kasagi with deepslate_tile_stairs for the upturned ends | Check the vermilion against the art | Beta 1 |
| Purification basin | cauldron with water, bamboo, stone | The shrine's temizuya | Beta 1 |
| Hokage Rock | stone, andesite, tuff, calcite; deepslate in the deep creases | Sculpted by rock_faces.py, finished by hand | Beta 1 |
| Village wall | smooth_sandstone face, cut_sandstone cornice, stone_bricks footing | Swept by wall.py (check the colour against the art) | Beta 1 |
| Main gate doors | green_terracotta with あん in red_concrete pixel art; dark_oak frame | Check the green and the lettering against the art | Beta 1 |
| Residence roof mark | red_concrete pixel art of 火 on the roof | Hand-placed from a pixel stencil | Beta 1 |
| Stadium | stone_bricks, smooth_sandstone, smooth_stone_slab benches | Seats are VF Seat markers on slabs | Beta 3 |
| Giant trees | jungle_log and dark_oak_log trunks, mangrove_roots, rooted_dirt, moss_block | Trunks from trees.py | Beta 3 |
| Forest canopy | dark_oak_leaves, jungle_leaves, vines, moss_carpet, glow_lichen | trees.py | Beta 3 |
| Forest fence | iron_bars and chain on stone_brick posts | fences.py along the circle | Beta 3 |
| Tower | stone_bricks, smooth_stone, polished_andesite | Hand-built | Beta 3 |
| Training grounds | oak_log stumps, hay_block, water, stone cliffs | Props from training_props.py | Beta 2 |
| Camps | campfire, barrel, white_wool and spruce tents, hay_block | Bandit camps | Beta 2 |
| Hideout | deepslate_bricks, iron_bars cells, soul_lantern, chain | The prologue hideout | Beta 1 |
| Kitchens | smoker, cauldron, barrel; Hearth & Harvest cooking pot | Homes and shops | Phase 0 |
| Storage | chest, barrel, bookshelf, chiseled_bookshelf | Until tansu and scroll_shelf land | Phase 0 |
| Western beds | bed (any colour) | Some flats keep a western bed, as the player's first flat does | Phase 0 |
| Iron lanterns | lantern, soul_lantern | Back lanes, the hideout | Phase 0 |
| Hives | bee_nest, beehive, honeycomb_block | The Aburame garden walls | Beta 2 |
| Greenhouse | glass, flower pots, flowers | The Yamanaka greenhouse | Beta 2 |
| Kennels' run | spruce_fence, hay_block, coarse_dirt | The Inuzuka run | Beta 1 |
| Smithy dressing | anvil, grindstone, blast_furnace, chain, lava under glass | Around the custom forge | Beta 2 |
| Bath house | water, smooth_stone, spruce; campfire under a slab for steam | Hand-built | Beta 2 |
| Memorials | polished_blackstone, chiseled_stone_bricks | The Ino-Shika-Cho memorial with clan crest plaques | Beta 2 |
| Statues of the Hokage | stone, andesite, calcite | Sculpted like the Rock faces at small scale | Later |
| Potted fern | potted_fern | The items catalogue's potted_fern is the vanilla block | Beta 1 |
| Easel and canvas | Village Friends easel_canvas | Reused from VF for the painters' studio | Beta 2 |
<!-- /gen:vanilla -->

### Custom blocks

*Generated.* ★ marks the prototypes in this branch. "Tex" counts the group's new textures.

<!-- gen:block-table -->
#### Roofs

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Kawara ridge cap** ★<br>`kawara_ridge` | The rounded ridge tiles along every roof peak, which stairs and slabs cannot make | `grey_kawara_ridge` Grey (deepslate tile roofs); `green_kawara_ridge` Green (oxidized copper roofs); `orange_kawara_ridge` Orange (cut copper roofs); `red_kawara_ridge` Red (red nether brick roofs) (Beta 1) | decor | simple | 12 | Phase 0 |
| **Onigawara ridge end**<br>`kawara_ridge_end` | The ornamental end tile that closes each ridge at the gables | `grey_kawara_ridge_end` Grey; `green_kawara_ridge_end` Green; `orange_kawara_ridge_end` Orange; `red_kawara_ridge_end` Red | decor | medium | 8 | Beta 1 |
| **Kawara eave tiles**<br>`kawara_eave` | The round-ended tile course along an eave, the roof's front edge. Stair-shaped, placed in front of the first course; corners by the stair shape logic | `grey_kawara_eave` Grey; `green_kawara_eave` Green; `orange_kawara_eave` Orange; `red_kawara_eave` Red | decor | simple | 8 | Beta 1 |
| **Rooftop water tank** ★<br>`water_tank` | The round tank on flat roofs, one block wide, one to four tall (part: single, bottom, middle, top) | `water_tank` Painted steel; `water_tank_weathered` Weathered, rust-streaked (Beta 1) | decor | medium | 5 | Phase 0 |
| **Large water tank**<br>`large_water_tank` | A 2 x 2 tank for apartment towers and the hospital: four quarter blocks per course. Quarter-cylinder models (quadrant property); same textures style as water_tank | `large_water_tank` Painted steel | decor | complex | 4 | Beta 1 |

#### Facades and shop fronts

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Shop awning** ★<br>`awning` | Sloped canvas awning with a scalloped valance over shop fronts | `red_awning` Red and cream stripes; `green_awning` Green and cream stripes; `indigo_awning` Plain indigo; `blue_awning` Blue and white stripes (Beta 1); `orange_awning` Plain orange (Beta 1); `cream_awning` Plain cream (Beta 2) | decor | simple | 13 | Phase 0 |
| **Noren curtain** ★<br>`noren` | Split shop curtain across the top of a doorway; walk-through. Printed ones carry the shop's kanji | `indigo_noren` Plain indigo; `red_noren` Plain red; `white_noren` Plain white (Beta 1); `brown_noren` Plain brown (Beta 1); `black_noren` Plain black (Beta 2) | decor | simple | 6 | Phase 0 |
| **Hanging shop sign**<br>`shop_sign` | Vertical signboard (kanban), one block wide and two tall, hung from a bracket on the front. 16 x 32 text texture per sign; glyphs stamped by pixels.glyph and cleaned up by eye | 23: Ramen, Furniture 家具, Grocer 八百屋, Tea 茶, Flowers 花, Hospital 病院, Weapons 武器, Tools 道具, Barbecue 焼肉, Dango 団子, Scrolls 巻物, Pawn 質, Bath ゆ, Post 郵便, Medicine 薬, Fish 魚, Tailor 呉服, Keep out 立入禁止, Inn 宿, Sake 酒, Books 本, Barber 床屋, Photographs 写真 | decor | simple | 24 | Beta 1 |
| **Fascia signboard**<br>`shop_board` | Horizontal name board over a landmark's entrance, three blocks wide (part: left, middle, right). Check every landmark's sign against the art | 8: Ramen stand name, Hospital, Ninja Academy, Library 書庫, Mission Desk 任務受付, Bath house 銭湯, Post office 郵便局, Police HQ | decor | simple | 24 | Beta 1 |
| **Koshi lattice**<br>`koshi_lattice` | Fine vertical timber lattice for machiya windows and shop fronts; connects like a pane | `light_koshi_lattice` Light cypress; `dark_koshi_lattice` Dark timber | decor | simple | 2 | Beta 1 |
| **Lattice entry door**<br>`koshi_door` | The sliding lattice-and-glass front door of homes and shops | `koshi_door` Light cypress; `dark_koshi_door` Dark timber | door (shoji_door) | medium | 4 | Beta 1 |
| **Amado shutter**<br>`amado` | Wooden storm shutter that closes a window or veranda at night | `amado` Light; `dark_amado` Dark | toggle (Trapdoor logic) | simple | 2 | Beta 2 |
| **Round window**<br>`marumado` | Round lattice window (2 x 2, four parts) for tea rooms and the shrine | `marumado` Lattice | decor | medium | 4 | Beta 2 |
| **Bamboo blind**<br>`bamboo_blind` | Sudare: roll-up blind for verandas and windows; rolled or down | `bamboo_blind` Bamboo | toggle | simple | 2 | Beta 1 |
| **Shop noren** ★<br>`shop_noren` | A shop's noren with its name or trade painted | 21: Tea (茶), Ramen (麺), Flowers (花), Bath house (ゆ), Barbecue (焼), Dango (団子), Sake (酒), Scrolls (巻), Sweets (甘), Inn (宿), Grocer 八百屋, Fish 魚, Weapons 武器, Tools 道具, Furniture 家具, Tailor 呉服, Pawn 質, Medicine 薬, Books 本, General store 雑貨, Barber 床屋 | decor | simple | 21 | Phase 0 |

#### Crests and banners

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Leaf crest plaque**<br>`leaf_crest` | The Hidden Leaf mark on gates, the Academy, the Residence and protectors' racks | `leaf_crest_stone` Carved stone, one block; `leaf_crest_painted` Painted wood, one block; `leaf_crest_large` Large 3 x 3 relief (9 parts) | decor | simple | 11 | Beta 1 |
| **Clan crest plaque**<br>`clan_crest` | A clan's crest on its gate and hall, one block, wall-mounted. Crests from the clan JSON and glyphs.py, the same ones the wardrobe stamps; a player clan's crest is a runtime decal on a blank plaque (later) | 25: Senju, Uzumaki, Uchiha, Hyuga, Nara, Akimichi, Yamanaka, Inuzuka, Sarutobi, Aburame, Hatake, Kurama, Shimura, Yuhi, Gekko, Shiranui, Morino, Umino, Haruno, Namiashi, Hagane, Kinoshita, Tsuchigumo, Suzuran, Tobari | decor | simple | 26 | Beta 1 |
| **Clan banner**<br>`clan_banner` | A hanging cloth banner, one wide and two tall, in the clan's palette with its crest | 26: Hidden Leaf, Senju, Uzumaki, Uchiha, Hyuga, Nara, Akimichi, Yamanaka, Inuzuka, Sarutobi, Aburame, Hatake, Kurama, Shimura, Yuhi, Gekko, Shiranui, Morino, Umino, Haruno, Namiashi, Hagane, Kinoshita, Tsuchigumo, Suzuran, Tobari | decor | simple | 26 | Beta 1 |
| **Crest mural**<br>`crest_mural` | A crest painted large on a wall, 3 x 3 blocks (9 parts): the Uchiha fan on the compound's walls | `uchiha_crest_mural` Uchiha fan; `uzumaki_crest_mural` Uzumaki spiral; `leaf_crest_mural` Hidden Leaf; `police_crest_mural` Military Police (Later) | decor | simple | 36 | Beta 2 |

#### Interior fittings

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Shoji screen** ★<br>`shoji_screen` | Fixed paper wall panel on a kumiko lattice, two blocks tall | `shoji_screen` Light cypress; `dark_shoji_screen` Dark timber | decor | simple | 8 | Phase 0 |
| **Shoji sliding door**<br>`shoji_door` | Sliding paper door, two blocks tall; opens by sliding over its neighbour, not swinging. Shares the shoji_screen textures | `shoji_door` Light cypress; `dark_shoji_door` Dark timber | door (Door block logic with a sliding open model) | medium | 2 | Beta 1 |
| **Fusuma sliding door**<br>`fusuma_door` | Opaque painted sliding door between rooms | `fusuma_door` Plain cream; `fusuma_door_wave` Wave pattern (seigaiha); `fusuma_door_pine` Pine (Beta 2); `fusuma_door_crane` Cranes (Beta 2); `fusuma_door_mountain` Mountains (Beta 2) | door (shoji_door) | medium | 10 | Beta 1 |
| **Ranma transom**<br>`ranma` | Carved transom panel above sliding doors | `wave_ranma` Waves; `cloud_ranma` Clouds | decor | simple | 2 | Beta 2 |
| **Tatami** ★<br>`tatami` | Rush floor mat, 2 px, the border down its long sides (axis) | `tatami` Fresh; `aged_tatami` Aged gold | decor | simple | 4 | Phase 0 |

#### Story pieces

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Paper seal tag**<br>`seal_tag` | A paper tag pasted on a wall or door. Decal like a vanilla glow lichen face; the explosive tag is also the thrown item's texture | `seal_tag_seal` Seal 封; `seal_tag_explosive` Explosive tag 起爆 (Beta 2); `seal_tag_ward` Ward 護符 (Beta 2) | decor | simple | 3 | Beta 1 |
| **Sealed stone door**<br>`sealed_stone_door` | A 3 x 3 stone slab door hung with seal tags, at the foot of the Rock (a hidden room) | `sealed_stone_door` Stone | story_door (Opens by a quest action, never by hand) | complex | 4 | Beta 1 |

#### Lanterns

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Paper lantern** ★<br>`paper_lantern` | Chochin: ribbed paper lantern hanging from a cord or standing | `red_paper_lantern` Red; `white_paper_lantern` White with a red band; `festival_paper_lantern` Festival 祭 (Beta 2); `large_red_paper_lantern` Large red (the ramen stand) (Beta 1) | light | medium | 9 | Phase 0 |
| **Stone lantern** ★<br>`stone_lantern` | Toro: granite lantern, two blocks tall (half: lower, upper) | `stone_lantern` Granite; `mossy_stone_lantern` Mossy; `charred_stone_lantern` Charred (a ruined shrine) (Beta 1) | light | complex | 7 | Phase 0 |

#### Streets

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Utility pole** ★<br>`utility_pole` | Creosoted wooden pole (part: pole, top with crossarm and insulators, top with transformer). Placed by roads.py every 12 blocks | `utility_pole` Wood | decor | medium | 3 | Phase 0 |
| **Power wire** ★<br>`power_wire` | Two strands between pole crossarms (axis, sag 0 to 2). Placed by roads.py between poles | `power_wire` Black | decor | simple | 1 | Phase 0 |
| **Street lamp**<br>`street_lamp` | Wooden post with a paper lamp box, two blocks tall | `street_lamp` Wood; `dark_street_lamp` Dark wood | light | medium | 4 | Beta 1 |
| **Direction sign**<br>`street_sign` | A post with arrow boards naming places | 10: Academy, Hokage Residence, Hospital, Market, Main gate, Shrine, Training grounds, Riverside, Bath house, Stadium | decor | simple | 11 | Beta 1 |
| **Notice board**<br>`notice_board` | A roofed Konoha notice board | `village_notice_board` Village notices; `mission_notice_board` Mission board (Beta 2) | quest_board (VF quest/Board, a new model) | medium | 4 | Beta 1 |
| **Post box**<br>`post_box` | The red letter box outside the post office | `post_box` Red | decor | simple | 2 | Beta 2 |
| **Bridge post finial**<br>`bridge_finial` | Onion-shaped giboshi cap on bridge railing posts | `bronze_bridge_finial` Bronze; `red_bridge_finial` Vermilion | decor | medium | 2 | Beta 2 |
| **Laundry line**<br>`laundry_line` | A line on a balcony with washing or an airing futon (axis) | `laundry_line_clothes` Washing; `laundry_line_futon` Airing futon; `laundry_line_empty` Empty | decor | simple | 3 | Beta 1 |

#### Festival

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Lantern garland**<br>`lantern_garland` | A string of small paper lanterns between poles (axis, sag) | `red_lantern_garland` Red; `mixed_lantern_garland` Red and white | light | simple | 2 | Beta 2 |
| **Mask display**<br>`mask_display` | Board of festival masks | `mask_display` Wood | decor | simple | 1 | Beta 2 |
| **Taiko drum**<br>`taiko` | Drum on a stand | `taiko` Lacquer | interact (Plays a beat) | medium | 2 | Beta 2 |
| **Festival stall**<br>`festival_stall` | Yatai: a two-block food stall with a roof (part: left, right); the trade is its noren | `takoyaki_festival_stall` Takoyaki; `candy_apple_festival_stall` Candy apples; `masks_festival_stall` Masks; `yakitori_festival_stall` Yakitori (Beta 3) | decor | complex | 10 | Beta 2 |
| **Goldfish pool**<br>`goldfish_pool` | Tub of goldfish for the scooping game | `goldfish_pool` Blue tub | interact (Festival game) | medium | 2 | Beta 2 |

#### Shrine

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Shimenawa rope**<br>`shimenawa` | Twisted straw rope with zigzag paper shide (axis; part: end, middle) | `shimenawa` Thick; `thin_shimenawa` Thin | decor | medium | 4 | Beta 1 |
| **Shrine bell**<br>`shrine_bell` | Suzu bell on a rope at the shrine front | `shrine_bell` Bronze | interact (Rings and counts a visit (New Year)) | medium | 2 | Beta 1 |
| **Offering box**<br>`offering_box` | Slatted saisen box under the bell | `offering_box` Wood | interact (Takes a ryo note: a prayer, a small luck buff) | medium | 2 | Beta 1 |
| **Wish plaque rack**<br>`ema_rack` | Rack of wooden ema wish plaques (fill: empty, some, full) | `ema_rack` Wood | interact (Opens a wish to read (the shrine district quest)) | medium | 3 | Beta 1 |
| **Komainu guardian**<br>`komainu` | Stone guardian lion-dog on a plinth, two blocks tall | `komainu_a` Open mouth; `komainu_un` Closed mouth | decor | complex | 4 | Beta 1 |
| **Fortune rack**<br>`omikuji_rack` | Frame of tied fortune slips | `omikuji_rack` Wood | interact | simple | 1 | Beta 2 |

#### Furniture (the Leaf set)

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Zabuton cushion**<br>`zabuton` | Floor cushion to sit on | `indigo_zabuton` Indigo; `red_zabuton` Red; `green_zabuton` Green; `brown_zabuton` Brown; `purple_zabuton` Purple; `cream_zabuton` Cream | seat (VF tavern Seat) | simple | 6 | Beta 1 |
| **Kotatsu**<br>`kotatsu` | Heated low table under a quilt | `red_kotatsu` Red; `indigo_kotatsu` Indigo; `green_kotatsu` Green; `brown_kotatsu` Brown | seat (VF Seat on all four sides) | medium | 9 | Beta 2 |
| **Pet bed**<br>`pet_bed` | A round bed for a pup or a cat | `red_pet_bed` Red; `blue_pet_bed` Blue; `green_pet_bed` Green | pet_bed (VF Pets sleep spot) | simple | 4 | Beta 1 |
| **Shoe cabinet**<br>`getabako` | The low shoe cabinet at a home's entry | `getabako` Wood | container | simple | 2 | Beta 1 |
| **Tea set**<br>`tea_set` | Teapot and cups on a tray, placed on a table | `tea_set` Clay | decor | simple | 1 | Beta 1 |
| **Shogi board**<br>`shogi_board` | A shogi board on legs, pieces set | `shogi_board` Kaya wood | decor | simple | 2 | Beta 1 |
| **Hibachi brazier**<br>`hibachi` | Ceramic charcoal brazier | `hibachi` Ceramic | light | medium | 2 | Beta 2 |
| **Wooden bath**<br>`ofuro` | Square hinoki bath tub | `ofuro` Hinoki | seat (VF Seat (soak)) | medium | 2 | Beta 2 |
| **Bedroll**<br>`bedroll` | A camping bedroll for the forest nights | `green_bedroll` Green; `brown_bedroll` Brown | bed (BedBlock that is removed on waking) | simple | 2 | Beta 3 |
| **Futon**<br>`futon` | Floor bed, two blocks long | 7: Indigo, Red, Green, White, Brown, Pink, Deluxe, thick quilt | bed (vanilla BedBlock: VF homes count it, sleep clears fatigue) | medium | 15 | Beta 1 |
| **Low table**<br>`low_table` | Chabudai | `low_table` Round, light; `dark_low_table` Round, dark; `long_low_table` Long, light | decor | simple | 3 | Beta 1 |
| **Low desk**<br>`low_desk` | A floor desk for study | `low_desk` Wood | decor | simple | 2 | Beta 1 |
| **Zaisu**<br>`zaisu` | Legless floor chair | `zaisu` Wood and cushion | seat (VF Seat) | simple | 2 | Beta 1 |
| **Rug**<br>`rug` | A woven floor rug, carpet-thin | `indigo_rug` Indigo; `red_rug` Red; `green_rug` Green; `cream_rug` Cream | decor | simple | 4 | Beta 1 |
| **Folding screen**<br>`folding_screen` | Byobu, two blocks wide | `folding_screen` Plain; `gold_folding_screen` Gold clouds (Beta 2); `pine_folding_screen` Pine (Beta 2); `crane_folding_screen` Cranes (Beta 2) | decor | medium | 8 | Beta 1 |
| **Scroll shelf**<br>`scroll_shelf` | Shelves of rolled scrolls; 9 slots | `scroll_shelf` Open shelf; `archive_scroll_shelf` Archive boxes (library) | container (9-slot inventory) | medium | 4 | Beta 1 |
| **Tansu chest**<br>`tansu_chest` | Chest of drawers with iron fittings; 27 slots | `tansu_chest` Light; `dark_tansu_chest` Dark; `step_tansu` Step tansu, climbable | container (27-slot inventory) | medium | 9 | Beta 1 |
| **Bookcase**<br>`bookcase` | A tall bookcase; 18 slots | `bookcase` Wood | container | simple | 2 | Beta 1 |
| **Wardrobe cabinet**<br>`wardrobe_cabinet` | Opens the wardrobe (outfits you own) | `wardrobe_cabinet` Wood | interact (Wardrobe screen by Items) | medium | 2 | Beta 1 |
| **Dresser with mirror**<br>`dresser_mirror` | Kyodai mirror stand | `dresser_mirror` Lacquer | decor | medium | 2 | Beta 1 |
| **Andon lamp**<br>`andon_lamp` | Paper floor lamp | `andon_lamp` Cream paper; `red_andon_lamp` Red paper | light | medium | 4 | Beta 1 |
| **Potted bonsai**<br>`potted_bonsai` | A bonsai tree in a tray | `potted_bonsai` Pine; `maple_potted_bonsai` Maple | decor | medium | 4 | Beta 1 |
| **Bamboo vase**<br>`bamboo_vase` | A cut-bamboo vase with a stem | `bamboo_vase` Bamboo | decor | simple | 1 | Beta 1 |
| **Ikebana**<br>`ikebana` | A flower arrangement in a low dish | `ikebana` Seasonal | decor | simple | 1 | Beta 1 |
| **Hanging scroll**<br>`hanging_scroll` | Kakejiku, one wide and two tall. Was planned as painting variants; a block so furnish mode places it | `hanging_scroll_fire` 火; `hanging_scroll_shinobi` 忍; `hanging_scroll_harmony` 和; `hanging_scroll_landscape` Landscape; `hanging_scroll_crane` Crane; `hanging_scroll_leaf` Hidden Leaf | decor | simple | 12 | Beta 1 |
| **Poster**<br>`poster` | A printed poster or a framed painting, 1 x 1 or 2 x 2 | `poster_academy` Academy; `poster_festival` Leaf Festival (Beta 2); `poster_wanted` Wanted (Beta 2); `poster_exams` Chunin Exams (Beta 3); `poster_village` A painting of the village; `poster_lake` A painting of the lake (Beta 2) | decor | simple | 12 | Beta 1 |
| **Wall clock**<br>`wall_clock` | A pendulum wall clock | `wall_clock` Wood | decor | medium | 2 | Beta 1 |
| **Calendar scroll**<br>`calendar_scroll` | A wall calendar showing the season and day | `calendar_scroll` Paper | interact (Shows VF Calendar) | simple | 1 | Beta 1 |
| **Wind chime**<br>`wind_chime` | Furin glass chime | `wind_chime` Glass | decor | simple | 1 | Beta 2 |
| **Mailbox**<br>`mailbox` | A home's letter box by the door | `mailbox` Wood | interact (Letters by Items) | simple | 2 | Beta 1 |
| **Kamidana**<br>`kamidana` | A small household shrine shelf | `kamidana` Wood | decor | medium | 2 | Beta 1 |
| **Memorial altar**<br>`memorial_altar` | Butsudan, a family memorial cabinet | `memorial_altar` Lacquer | decor | medium | 2 | Beta 1 |
| **Incense burner**<br>`incense_burner` | Bronze burner with a curl of smoke | `incense_burner` Bronze | decor | simple | 1 | Beta 1 |
| **Weapon rack**<br>`weapon_rack` | Standing rack showing up to 4 tools | `weapon_rack` Wood | display (Block entity, 4 slots, rendered) | complex | 2 | Beta 1 |
| **Pet bowl**<br>`pet_bowl` | Food and water bowls | `pet_bowl` Ceramic | interact (VF Pets feeding) | simple | 1 | Beta 1 |
| **Cat tower**<br>`cat_tower` | Posts and perches for a cat | `cat_tower` Wood and rope | decor | medium | 2 | Beta 1 |
| **Goldfish bowl**<br>`goldfish_bowl` | A glass bowl with a goldfish | `goldfish_bowl` Glass | decor | medium | 1 | Beta 2 |
| **Go board**<br>`go_board` | A go board on legs | `go_board` Kaya wood | decor | simple | 2 | Beta 1 |
| **Moving crate**<br>`moving_crate` | Packs furniture and chests with their contents for a move | `moving_crate` Wood | container (Keeps contents as an item) | simple | 1 | Later |

#### Training

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Training dummy**<br>`training_dummy` | Straw dummy on a post | `training_dummy` Straw | target (Combat hit counter) | medium | 2 | Beta 1 |
| **Training log**<br>`training_log` | A rope-bound stump or a tall log for strikes | `training_log_stump` Stump; `training_log_tall` Tall log | target | simple | 4 | Beta 1 |
| **Climb marks**<br>`kunai_mark` | Kunai cut marks on a trunk, for tree walking | `kunai_mark` Cut | decor | simple | 1 | Beta 2 |
| **Memorial stone**<br>`memorial_stone` | The polished kunai-shaped memorial stone, three blocks tall (part). Engraved names as a texture; check its shape and size against the art | `memorial_stone` Polished stone | decor | complex | 3 | Beta 2 |
| **Target board**<br>`target_board` | Wall-mounted ring target that shows stuck kunai | `target_board` Wood | target (Combat hit target) | medium | 1 | Beta 1 |
| **Target post**<br>`target_post` | Ring target on a post | `target_post` Wood | target (Combat hit target) | medium | 2 | Beta 1 |

#### Academy, Residence, hospital, stadium

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Academy desk**<br>`academy_desk` | Long tiered classroom desk with its bench (part: left, middle, right) | `academy_desk` Wood | seat (VF Seat) | medium | 2 | Beta 1 |
| **Blackboard**<br>`blackboard` | Wall board, three wide (part); a blank, a hand-sign chart or an exam face | `blackboard` Blank; `blackboard_signs` Hand signs chart; `blackboard_exam` Exam (Beta 3) | decor | simple | 9 | Beta 1 |
| **Teacher's desk**<br>`lectern` | The teacher's desk at the front of a classroom | `lectern` Wood | decor | simple | 2 | Beta 1 |
| **Tree swing**<br>`tree_swing` | A plank swing on ropes, hung from a branch (the Academy tree) | `tree_swing` Wood | seat (VF Seat with a swing clip) | medium | 2 | Beta 1 |
| **Paper stack**<br>`paper_stack` | Stacks of papers or scrolls for desks | `paper_stack_papers` Papers; `paper_stack_scrolls` Scrolls; `paper_stack_missions` Mission scrolls (Beta 2) | decor | simple | 3 | Beta 1 |
| **Hokage's desk**<br>`hokage_desk` | The broad desk of the Hokage's office | `hokage_desk` Dark wood | decor | medium | 3 | Beta 1 |
| **Mission desk**<br>`mission_desk` | The long desk of the Mission Desk (part: left, middle, right) | `mission_desk` Wood | interact (Opens the Mission Desk board (Progression)) | medium | 3 | Beta 2 |
| **Hospital bed**<br>`hospital_bed` | Metal-frame bed with white sheets | `hospital_bed` White | bed (BedBlock that is not a home bed: the hospital wake point) | medium | 3 | Beta 1 |
| **Hospital curtain**<br>`hospital_curtain` | Privacy curtain on a ceiling rail (axis) | `hospital_curtain` Pale green | decor | simple | 1 | Beta 1 |
| **IV stand**<br>`iv_stand` | Drip stand | `iv_stand` Steel | decor | simple | 1 | Beta 1 |
| **Medicine cabinet**<br>`medicine_cabinet` | Glass-fronted cabinet of bottles | `medicine_cabinet` White | container | medium | 2 | Beta 1 |
| **Clinic table**<br>`vet_table` | Examination table of the Inuzuka clinic | `vet_table` Steel | decor | simple | 1 | Beta 1 |
| **Kennel**<br>`kennel` | A dog house | `kennel` Wood; `inuzuka_kennel` Inuzuka red (Beta 2) | pet_bed (VF Pets) | medium | 4 | Beta 1 |
| **Kage seat**<br>`kage_seat` | The high-backed seat of the stadium's Kage box | `kage_seat` Lacquer | seat (VF Seat) | complex | 3 | Beta 3 |
| **Bracket board**<br>`bracket_board` | The finals' tournament board, 3 x 2 (part) | `bracket_board` Wood | decor | simple | 6 | Beta 3 |

#### Shops and food

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Ramen counter**<br>`ramen_counter` | The ramen stand's lacquered bar counter (part: straight, end) | `ramen_counter` Lacquer and wood | decor | medium | 3 | Beta 1 |
| **Ramen stool**<br>`ramen_stool` | Round stool at the counter | `ramen_stool` Red top | seat (VF tavern Seat) | simple | 1 | Beta 1 |
| **Shop counter**<br>`shop_counter` | Straight and corner; the keeper stands behind; right-click opens the shop | `shop_counter` Shop counter | interact (Shop screen by Items) | simple | 2 | Beta 1 |
| **Menu board**<br>`menu_board` | Right-click shows prices | `menu_board` Menu board | interact (Prices by Items) | simple | 2 | Beta 1 |
| **Noodle kitchen**<br>`noodle_kitchen` | The ramen stand's stock pot and noodle station, with steam | `noodle_kitchen` Noodle kitchen | station (VF tavern kitchen anchor) | medium | 3 | Beta 1 |
| **Rice sack pile**<br>`rice_sack_pile` | Stacked rice sacks | `rice_sack_pile` Rice sack pile | decor | simple | 1 | Beta 1 |
| **Market stall**<br>`market_stall` | A stall counter with a cloth canopy (two blocks) | `market_stall` Market stall | decor | medium | 3 | Beta 1 |
| **Dango grill**<br>`dango_grill` | Charcoal grill with skewers | `dango_grill` Dango grill | decor | medium | 2 | Beta 2 |
| **Red-cloth bench**<br>`bench_red_cloth` | Tea house bench with a red felt cloth | `bench_red_cloth` Red-cloth bench | seat (VF Seat) | simple | 2 | Beta 1 |
| **Parasol**<br>`parasol` | Wagasa over a bench, two blocks tall | `parasol` Parasol | decor | medium | 2 | Beta 1 |
| **Tea counter**<br>`tea_counter` | The tea house's serving counter with kettles | `tea_counter` Tea counter | decor | medium | 2 | Beta 1 |
| **Barbecue table**<br>`barbecue_table` | Sunken grill, seats on both sides | `barbecue_table` Barbecue table | seat (VF Seat both sides) | medium | 3 | Beta 2 |
| **Bench**<br>`bench_seat` | Plain wooden bench | `bench_seat` Bench | seat (VF Seat) | simple | 1 | Beta 1 |
| **Catalogue lectern**<br>`catalogue_lectern` | The furniture shop's order book | `catalogue_lectern` Catalogue lectern | interact (Shop screen by Items) | simple | 2 | Beta 1 |
| **Lumber rack**<br>`lumber_rack` | Planks and beams on a rack (Kinoshita yard) | `lumber_rack` Lumber rack | decor | simple | 1 | Beta 2 |
| **Fitting screen**<br>`fitting_screen` | The tailor's changing screen | `fitting_screen` Fitting screen | decor | simple | 1 | Beta 2 |
| **Pawn counter grille**<br>`pawn_counter_grille` | The pawn shop's grilled window; opens the pawn screen | `pawn_counter_grille` Pawn counter grille | interact (Pawn screen by Items) | medium | 2 | Beta 2 |
| **Bath counter**<br>`bath_counter` | The bath house's raised attendant's booth | `bath_counter` Bath counter | decor | medium | 2 | Beta 2 |
| **Locker shelf**<br>`locker_shelf` | Baskets for clothes at the bath house | `locker_shelf` Locker shelf | decor | simple | 1 | Beta 2 |
| **Wash stool**<br>`wash_stool` | Low wooden stool by the taps | `wash_stool` Wash stool | seat (VF Seat) | simple | 1 | Beta 2 |
| **Medicine drawer wall**<br>`medicine_drawer_wall` | A wall of small herb drawers | `medicine_drawer_wall` Medicine drawer wall | decor | simple | 1 | Beta 1 |
| **Herb drying rack**<br>`herb_drying_rack` | Bundles of herbs on a rack (Suzuran, the pharmacy) | `herb_drying_rack` Herb drying rack | decor | simple | 2 | Beta 1 |
| **Hospital counter**<br>`hospital_counter` | Reception and dispensary counter | `hospital_counter` Hospital counter | interact (Dispensary by Items) | simple | 2 | Beta 1 |
| **Senbei grill**<br>`cracker_grill` | Rice cracker grill | `cracker_grill` Senbei grill | decor | medium | 2 | Beta 2 |
| **Target game booth**<br>`target_game_booth` | The festival throwing game | `target_game_booth` Target game booth | interact (Festival game) | medium | 2 | Beta 2 |
| **Arranging table**<br>`arranging_table` | The flower shop's work table | `arranging_table` Arranging table | decor | simple | 2 | Beta 1 |
| **Barber chair**<br>`barber_chair` | The barber's chair; right-click opens restyle | `barber_chair` Barber chair | seat (VF Seat; restyle screen by Items and the creator) | medium | 2 | Beta 1 |

#### Gardens

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Shishi-odoshi**<br>`shishi_odoshi` | Bamboo deer-scarer over a stone basin | `shishi_odoshi` Bamboo | decor | medium | 2 | Beta 2 |
| **Raked gravel**<br>`raked_gravel` | Karesansui gravel in raked lines or ripples (axis) | `raked_gravel_lines` Lines; `raked_gravel_ripples` Ripples | decor | simple | 2 | Beta 2 |

#### Clan signatures

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Sealing mask**<br>`sealing_mask` | A wall-hung mask of the Uzumaki hall | `sealing_mask_fox` Fox; `sealing_mask_demon` Demon; `sealing_mask_elder` Elder | decor | medium | 3 | Beta 2 |
| **Insect jar**<br>`insect_jar` | Glass jars of insects (Aburame) | `insect_jar_beetle` Beetles; `insect_jar_firefly` Fireflies | decor | simple | 2 | Beta 2 |
| **Sawhorse**<br>`sawhorse` | Carpenter's sawhorse with a plank (Kinoshita) | `sawhorse` Wood | decor | simple | 1 | Beta 2 |

#### Crafting stations

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Shinobi workbench**<br>`workbench` | Crafting station for tags, smoke bombs and furniture (Academy workshop, Kinoshita yard, homes) | `workbench` Wood | workstation (VF tools/workstations pattern; screen by Items) | complex | 4 | Beta 1 |
| **Forge**<br>`forge` | The smithy's hearth with bellows, two blocks wide, glows; and the home forge with its anvil in one block | `forge` Smithy hearth; `small_forge` Home forge and anvil (Beta 2) | workstation (Screen by Items) | complex | 8 | Beta 1 |
| **Smithy anvil**<br>`anvil` | The weapon shop's anvil, where the smithing screen opens | `anvil` Iron on a stump | workstation (Screen by Items) | medium | 2 | Beta 1 |
| **Whetstone wheel**<br>`whetstone_wheel` | Treadle whetstone for repair and sharpening | `whetstone_wheel` Stone and wood | workstation (Screen by Items) | medium | 2 | Beta 1 |
| **Quench trough**<br>`quench_trough` | Water trough by the forge | `quench_trough` Wood | decor | simple | 1 | Beta 1 |
| **Apothecary table**<br>`apothecary_table` | Mortar, scales and jars: pills and poultices (pharmacy, hospital herb room, homes) | `apothecary_table` Wood | workstation (Screen by Items) | medium | 3 | Beta 1 |
| **Sealing desk**<br>`sealing_desk` | A low desk with brush, ink and tag paper for seals (homes) | `sealing_desk` Wood | workstation (Screen by Items) | medium | 2 | Beta 2 |
| **Calligraphy desk**<br>`calligraphy_desk` | The scroll shop's public sealing desk | `calligraphy_desk` Lacquer | workstation (Screen by Items) | medium | 2 | Beta 2 |
| **Tailor's table**<br>`tailor_table` | Cutting table with cloth and shears (tailor, homes) | `tailor_table` Wood | workstation (Screen by Items) | medium | 2 | Beta 2 |

#### Displays (item-rendering)

| Block | Purpose | Variants (slice) | Function | Model | Tex | First |
|---|---|---|---|---|---:|---|
| **Keepsake stand**<br>`keepsake` | A small stand that shows one of the 40 keepsakes | `keepsake` Keepsake stand | display, 1 slot (Item display block entity (one renderer for all)) | medium | 2 | Beta 1 |
| **Display shelf**<br>`display_shelf` | Home shelf showing 6 items | `display_shelf` Display shelf | display (Item display block entity (one renderer for all)) | medium | 2 | Beta 1 |
| **Goods shelf**<br>`goods_shelf` | Shop shelving | `goods_shelf` Goods shelf | display, 6 slots (Item display block entity (one renderer for all)) | medium | 2 | Beta 1 |
| **General store shelf**<br>`general_store_shelf` | Tall store shelving | `general_store_shelf` General store shelf | display, 9 slots (Item display block entity (one renderer for all)) | medium | 2 | Beta 1 |
| **Crate display**<br>`crate_display` | Stacked crates of goods | `crate_display` Crate display | display, 4 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 1 |
| **Produce crate**<br>`produce_crate_display` | Tilted crate of vegetables or fruit | `produce_crate_display` Produce crate | display, 4 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 1 |
| **Fish on ice**<br>`fish_ice_display` | The fishmonger's ice tray | `fish_ice_display` Fish on ice | display, 4 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 1 |
| **Glass case**<br>`glass_case` | Counter-height glass case; also the home display case | `glass_case` Glass case | display, 4 slots (Item display block entity (one renderer for all)) | medium | 2 | Beta 1 |
| **Weapon display wall**<br>`weapon_display_wall` | Wall board of blades and tools | `weapon_display_wall` Weapon display wall | display, 6 slots (Item display block entity (one renderer for all)) | medium | 2 | Beta 1 |
| **Pouch hooks**<br>`pouch_hooks` | Hooks of pouches and holsters | `pouch_hooks` Pouch hooks | display, 4 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 1 |
| **Scroll rack**<br>`scroll_rack` | Pigeonholes of scrolls | `scroll_rack` Scroll rack | display, 9 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 2 |
| **Scroll display case**<br>`scroll_display_case` | A glass case for rare scrolls | `scroll_display_case` Scroll display case | display, 1 slot (Item display block entity (one renderer for all)) | medium | 2 | Beta 2 |
| **Flower bucket stand**<br>`flower_bucket_stand` | Tiered buckets of cut flowers | `flower_bucket_stand` Flower bucket stand | display, 6 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 1 |
| **Flower pot tiers**<br>`flower_pot_tiers` | Stepped shelf of potted plants | `flower_pot_tiers` Flower pot tiers | display, 6 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 1 |
| **Showroom plinth**<br>`showroom_plinth` | Shows one furniture piece in the showroom | `showroom_plinth` Showroom plinth | display, 1 slot (Item display block entity (one renderer for all)) | complex | 2 | Beta 1 |
| **Bolt shelf**<br>`bolt_shelf` | Bolts of cloth | `bolt_shelf` Bolt shelf | display, 6 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 2 |
| **Mannequin**<br>`mannequin` | Wears one wardrobe outfit on the resident model | `mannequin` Mannequin | display, 1 slot (Item display block entity (one renderer for all)) | complex | 2 | Beta 2 |
| **Curio shelf**<br>`curio_shelf` | The pawn shop's shelf of oddments; also the home curio cabinet | `curio_shelf` Curio shelf | display, 12 slots (Item display block entity (one renderer for all)) | medium | 2 | Beta 2 |
| **Tall bookshelf**<br>`bookshelf_tall` | Bookshop shelving | `bookshelf_tall` Tall bookshelf | display, 9 slots (Item display block entity (one renderer for all)) | simple | 2 | Later |
| **Book table**<br>`book_display_table` | A table of books face up | `book_display_table` Book table | display, 4 slots (Item display block entity (one renderer for all)) | simple | 2 | Later |
| **Pet supply shelf**<br>`pet_supply_shelf` | The clinic's shelf | `pet_supply_shelf` Pet supply shelf | display, 6 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 1 |
| **Metal stock rack**<br>`metal_stock_rack` | Bars and blanks at the metalworks | `metal_stock_rack` Metal stock rack | display, 6 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 2 |
| **Charm stall**<br>`charm_stall` | Shrine charms and fortunes | `charm_stall` Charm stall | display, 3 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 1 |
| **Paint display**<br>`paint_display` | Paints and brushes at the studio | `paint_display` Paint display | display, 6 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 2 |
| **Jar shelf**<br>`jar_shelf` | Jars of herbs and medicines | `jar_shelf` Jar shelf | display, 6 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 1 |
| **Prize shelf**<br>`prize_shelf` | Festival game prizes | `prize_shelf` Prize shelf | display, 6 slots (Item display block entity (one renderer for all)) | simple | 2 | Beta 2 |
| **Wall mount**<br>`wall_mount` | A wall bracket showing one item | `wall_mount` Wall mount | display, 1 slot (Item display block entity (one renderer for all)) | simple | 1 | Beta 1 |
<!-- /gen:block-table -->

## 5. Process

The ROADMAP §6 pipeline, made concrete. Everything that can be text is text in this repository;
the map world is the last step, and every hand build is exported back to files so the world is
never the only copy.

### The pieces

| Piece | What it is | Who |
|---|---|---|
| `tools/konoha/blocks.py` | Custom blocks in Python: textures, models, blockstates, item models into `src/main/resources/assets/narutominecraft/` (VF `tools/tavern/furniture.py` style) | Agent |
| `tools/konoha/kit.py` | The building kit: `Plan`, walls, bands, low and steep gable roofs, flat roofs, tanks, shoji, doors; the palettes of section 2 | Agent |
| `tools/konoha/buildings/*.py` | Design programs; each writes a blueprint to `tools/konoha/blueprints/` with markers (House Plaque, beds, residents, seats, tavern bounds, door anchor) | Agent |
| VF's compiler | `tools/create_village_structures.py` turns blueprints into structure NBT | Agent runs it |
| `tools/konoha/layout.json` | Every district: polygon, streets as polylines with a class, plots with a design, rotation, mirror and variant rolls, landmark positions, anchors, resident markers, candidate flats, vacant estates | Agent drafts, you approve the plan view |
| `tools/konoha/layout.py` | `--check` (every plot fits, every home has a plaque and beds, every marker is inside a building, anchors resolve, no overlaps) and `--plan` (a top-down PNG of the village from the layout) | Agent |
| `tools/konoha/roads.py` | Streets from the layout's polylines: surface by class, kerbs, poles every 12 blocks with wires, lamps, signs; writes street blueprints per district | Agent |
| `tools/konoha/sweep.py` | Curved runs swept along a circle or polyline: the village wall (a 16-block profile), clan compound walls, the forest's fence | Agent |
| `tools/konoha/rock_faces.py` | The Hokage Rock: each face as a depth map (a 24-block-tall grey image) voxelised into stone, andesite, tuff and calcite by depth and slope, into a blueprint per face | Agent drafts, you finish in game |
| `/shinobi paste <district>` | Dev command (builder mode only): pastes a district's blueprints at their fixed spots from the layout; re-pasting one district never touches another; `--dry` outlines the plots with particles | Agent writes (Phase 0), you run |
| `/shinobi export <name> <from> <to>` | Saves a hand-built region as structure NBT into `src/main/resources/data/narutominecraft/structure/konoha/landmarks/`, so hand work is versioned in git and re-pasteable | Agent writes, you run |
| `/shinobi check` | In-game `layout.py --check`: lists plaques without a home, homes without beds, markers in walls; glows each problem | Agent writes, you run |
| `render_kit.py` | Preview renders of blocks, buildings, cutaways and streets into `docs/renders/konoha/` | Agent, you review |

### Order of work

| # | Step | Who | Slice |
|---|---|---|---|
| 1 | Prototype kit, 3 programs and renders (this branch); you approve the look | Agent, then you | Now |
| 2 | Master world: empty generator, border, VF and vanilla worldgen off, builder mode; WorldEdit (or Axiom) for builder mode | Agent sets up; you install and open it | Phase 0 |
| 3 | Block registration from `blocks.json`, the Phase 0 blocks in game; you check each in a test world | Agent, then you | Phase 0 |
| 4 | `layout.json` for the test street, `/shinobi paste`, `/shinobi check`, `/shinobi export`; VF's compiler for NBT | Agent | Phase 0 |
| 5 | Paste the test street; ten residents walk, sleep and trade (ROADMAP §9 exit criteria) | You run it, agent fixes | Phase 0 |
| 6 | Beta 1 blocks (61 groups) and programs (home variants, towers, shops, clan gates, wall, trees, bridges, training props) with renders | Agent; you review renders | Beta 1 |
| 7 | Village layout: the whole village planned now (all districts as polygons and plots, ROADMAP: "laid out now, built after the beta"); you approve the plan PNG | Agent, then you | Beta 1 |
| 8 | **Hokage Rock**: terrain massing by `sweep.py`/heightmap, faces by `rock_faces.py`; then you sculpt and smooth each face in game | Agent drafts; **you finish** | Beta 1 |
| 9 | Landmark drafts as one-off programs (Residence, Academy, hospital, shrine, gate, ramen stand, prologue hideout and ruined shrine, 15 clan halls); paste; **you finish each by hand** and `/shinobi export` it | Agent drafts; **you finish** | Beta 1 |
| 10 | Paste the Beta 1 districts; **you shape the terrain** between them (hills, the river banks, gardens) and walk every street | **You**, agent fixes | Beta 1 |
| 11 | `/shinobi check` clean; markers and anchors verified; the world zipped by the release job | Agent, you sign off | Beta 1 |
| 12 | Beta 2 blocks, programs and landmarks (training grounds, smithy, bath house, camps, the border village, clan quarters filled out); **you finish landmarks and terrain** | Agent drafts; **you finish** | Beta 2 |
| 13 | Beta 3: the forest (trees by program, fence by sweep, gates), tower and stadium; **you shape the forest floor and river and finish the tower and stadium** | Agent drafts; **you finish** | Beta 3 |
| 14 | Later districts, gates, the full wall, vacant estates | As above | Later |

### What needs you at your PC

| Step | Why it needs you | What helps | Hours |
|---|---|---|---|
| Phase 0: install builder tools, paste and walk the test street | Only you run the client | `/shinobi paste`, `/shinobi check` | 2 |
| Hokage Rock: four faces | Faces need an eye in the game's light, not a render | `rock_faces.py` gets each face to ~80%; WorldEdit smooth and erode brushes; `/shinobi export rock` after each session; a face can be re-pasted from its blueprint to start over | 10 |
| Hokage Rock: blending the cliff into the terrain and the village's fan | Terrain reads only in game | Heightmap massing pasted first | 3 |
| Prologue hills terrain | Same | A heightmap draft | 3 |
| Beta 1 landmark finishing (8) | Interiors, lighting, the last 10% of detail | One-off drafts; the kit's blocks; renders to compare | 12 |
| Clan halls finishing (15) | Each clan's signature feature | Drafts from the clan JSON palette | 7.5 |
| Beta 1 terrain between districts, the park, walking every street | Paths, slopes, sightlines to the Rock | `--plan` PNG, `/shinobi check` | 6 |
| Beta 2 training grounds terrain (Ground 3, the lake, the cliff) | Terrain | Props by program | 5 |
| Beta 2 landmark finishing (6) and clan quarter dressing (15) | Detail | Drafts | 12 |
| Beta 2 border village, farmsteads and the east road's terrain, walk-through | Terrain | Pasted homes and farms | 8 |
| Beta 3 forest floor and river, tower and stadium finishing, walk-through | Terrain, scale | Trees and fence pasted first | 12 |
| **To the end of Beta 3** | | | **~80** |
| Later districts, gates, estates | | | ~25 |

If you would rather build the landmarks yourself from scratch, add about 60 hours to the beta; the
recommended path is agent drafts and your finishing.

## 6. Prototypes

This branch holds the first working slice of the pipeline, to calibrate the estimate and show the
look.

- **Blocks** (`tools/konoha/blocks.py`, `pixels.py`): 11 blocks (the noren count as two: plain and shop), 21 with variants, 50 textures, 32
  models: `shoji_screen`, `tatami`, `paper_lantern`, `stone_lantern`, `noren`, `water_tank`,
  `kawara_ridge`, `utility_pole` and `power_wire`, `awning`. Compiled into
  `src/main/resources/assets/narutominecraft/{blockstates,models/block/konoha,textures/block/konoha,items}`.
  `python3 tools/konoha/blocks.py --check` validates them against `blocks.json`.
- **Design programs** (`tools/konoha/kit.py`, `buildings/`): a two-storey home, a tea house with an
  awning, noren and lanterns, and the twelve-flat Leaf apartment block (the home session's flat plan,
  `blueprints/leaf_block.homes.json` with its homes.json rows) with a gallery, external stairs and
  rooftop tanks. Each writes `tools/konoha/blueprints/<id>.json` with its markers.
- **Renders** (`tools/konoha/render_kit.py` with `preview.py`, drawing through the wardrobe's
  rasterizer, the VF preview renderer): custom blocks are drawn from the compiled assets; vanilla
  blocks are procedural stand-ins in their average colours (good for massing and palette, not
  texture detail).

| Render | Shows |
|---|---|
| [blocks.png](docs/renders/konoha/blocks.png), [blocks/](docs/renders/konoha/blocks/) | Every prototype block, assembled, and a close-up of each |
| [home_plaster_2f.png](docs/renders/konoha/home_plaster_2f.png), [cutaway](docs/renders/konoha/home_plaster_2f_cutaway.png) | The home, front and back; both floors |
| [shop_tea_house.png](docs/renders/konoha/shop_tea_house.png), [cutaway](docs/renders/konoha/shop_tea_house_cutaway.png) | The tea house; the shop floor and the owner's rooms |
| [leaf_block.png](docs/renders/konoha/leaf_block.png), [cutaway](docs/renders/konoha/leaf_block_cutaway.png) | The Leaf apartment block; the ground and third-floor flats |
| [street.png](docs/renders/konoha/street.png) | All three on one street with poles, wires, lanterns and a tree |

```
python3 tools/konoha/blocks.py --check
for f in tools/konoha/buildings/*.py; do python3 "$f"; done
python3 tools/konoha/render_kit.py
python3 tools/konoha/catalogue.py --write
```

Fixed after looking at the renders: the camera (it first looked from below), a roof pitch that was
too steep for Konoha (now the low slab roof), the awning's slope and frame, a rounder paper
lantern, softer ridge joints, a legible ramen glyph, wires that meet the insulators, and the
apartment's ground-floor walkway and stair steps.

## 7. Effort estimate

### Calibration

The prototype set (10 blocks with 21 variants and 50 textures, the preview renderer, the building
kit, three design programs, the street scene and their fixes) took about **one third of a working
session**. A session here means a focused agent session of about two hours including renders,
review and fixes; your review of its renders is on top (about 15 minutes a session). Rates taken
from it, with margin for in-game fixes the renders cannot show:

| Work | Rate |
|---|---|
| Simple blocks | ~12 a session |
| Medium blocks | ~8 a session |
| Complex blocks | ~3 a session |
| Text and crest variants (signs, noren, crests, banners) | ~60 a session, then a cleanup pass by eye |
| Design programs once the kit exists | ~3 a session |
| One-off landmark drafts | 0.5 to 2 sessions each |

### Sessions

| Work | Phase 0 | Beta 1 | Beta 2 | Beta 3 | Later | Total |
|---|---:|---:|---:|---:|---:|---:|
| Block models and textures (164 blocks left, 365 variants, 634 textures) | 0.5 | 12 | 6 | 1 | 1 | **20.5** |
| Java registration and block behaviour (the display block entity, seats, beds, containers, station hooks for Items' screens) | 2 | 6 | 4 | 1 | — | **13** |
| Design programs (28 left) and `roads.py`, `sweep.py`, `rock_faces.py` | 1.5 | 7 | 3 | 3 | — | **14.5** |
| Paste tooling, `layout.py`, layout files | 6 | 3 | 2 | 1 | 2 | **14** |
| One-off landmark drafts | — | 12 | 6 | 4 | 6 | **28** |
| **Total** | **10** | **40** | **21** | **10** | **9** | **~90** (~180 h) |

### Your hours

| | Phase 0 | Beta 1 | Beta 2 | Beta 3 | Later | Total |
|---|---:|---:|---:|---:|---:|---:|
| Building and terrain in Minecraft (section 5) | 2 | 41.5 | 25 | 12 | 25 | **~105** |
| Reviewing renders | 2.5 | 8 | 4 | 2.5 | 2 | ~19 |

## 8. Registration notes for Phase 0

No mod code exists yet, so this branch ships assets and renders only. When Phase 0 registers the
blocks:

- **One generic registration from `blocks.json`.** Each variant id becomes a block with its
  properties read from the blockstate file (`facing`, `axis`, `half`, `part`, `sag`); shape families
  share a few classes: decor (a VoxelShape from the model's elements), two-block (`half`, placed
  like a door), multi-part (`part` left/middle/right or quadrants), pane-like (`koshi_lattice`),
  no-collision (`noren`, `power_wire`, `lantern_garland`), and columns whose `part` updates from
  neighbours (`water_tank`, `utility_pole`).
- **Light.** Lanterns 13, toro 12, andon 10, street lamps 13; model elements already carry
  `light_emission` so the paper glows.
- **Behaviour reuses VF.** Seats (`zabuton`, `tea_bench`, `ramen_stool`, `academy_desk`,
  `kotatsu`, `tree_swing`, `kage_seat`, `ofuro`) spawn VF's tavern `Seat`; `futon` and
  `bedroll` are vanilla `BedBlock`s so VF homes count them and sleep clears fatigue; the
  `hospital_bed` is a bed that is never a home bed; `notice_board` is VF's quest board with a new
  model; `workbench` and `forge` follow VF's `tools/workstations/`; `ramen_kitchen` anchors the
  tavern kitchen.
- **Sliding doors.** `shoji_door`, `fusuma_door` and `koshi_door` are door blocks whose open state
  slides the panel over the neighbouring block instead of swinging.
- **Tags.** Every piece a player may place at home is tagged `shinobi_life:furniture` (ROADMAP §7);
  a `#narutominecraft:konoha` tag and a Konoha creative tab hold the rest for builder mode.
- **Namespace.** Assets are under `narutominecraft` today; when the pack splits into its mods, the
  furniture moves with Shinobi Life and the architecture with the map's mod (one rename in
  `blocks.py`).
- **Check in game.** The awning's 22.5° element rotation (its front must drop), the wire height
  at the insulators, and the glyphs at 16 px.

## 9. Open questions

1. **Village Friends' pipeline was not readable from this session** (adding the VF repository was
   refused), so `kit.Plan.blueprint` writes a provisional format (palette characters in layers,
   plus markers) and `preview.py` stands in for VF's renderer. Next step: read VF's
   `BUILDING_EDITING.md`, `tools/village_design/`, `tools/village_blueprints/`,
   `create_village_structures.py`, `standalone_templates.json`, `TAVERN.md`, `tools/tavern/`,
   `tools/workstations/`, `tools/hearth/` and `HOMES.md`, then switch `Plan.blueprint` to VF's
   format and `blocks.py` to `furniture.py`'s helpers. The designs themselves do not change.
2. **Check against the art:** the water tanks' size and colour, the round towers, the wall's colour
   and height, the main gate's doors and lettering, the Residence's and the Academy's colours, the
   hospital, the torii's vermilion, the memorial stone's shape.
3. **Builder tools for 26.3:** whether WorldEdit (Fabric) or Axiom has a 26.3 build; if neither,
   the agent adds brush commands (smooth, erode, fill) to builder mode.
4. **Who finishes the landmarks:** the plan assumes agent drafts and your finishing (~80 hours to
   Beta 3); building them yourself from scratch is about 60 hours more.
5. **The Hokage faces' designs:** `rock_faces.py` needs one depth map per face, drawn from each
   Hokage's look in the story's design notes; you approve them as renders before they are carved.
