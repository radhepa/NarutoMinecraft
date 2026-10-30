# Konoha build techniques and palettes

How every Konoha building is made from here on: proportions true to a 1.8 m player, wall gradients
mapped to `kit.WALLS`, depth, roofs, fronts, light, streets, terrain, trees, and lived-in interiors
for every home type. Part of the [master plan](MASTER_PLAN.md). Blocks are vanilla plus the
Konoha set (`KonohaBlocks.java`); where a Leaf-set furniture block is planned (KONOHA_BUILD.md,
Interior fittings), the kit helper places a vanilla stand-in now and swaps to the block later in one
place.

Tags: **[canon]** stated by a source (listed at the end); **[art]** from the series' look, to check
against reference art before treating as canon.

## 1. Proportions

One block is one metre. The player is 1.8 blocks tall, so doors, rooms and furniture keep real sizes.

| Thing | Size | Notes |
|---|---|---|
| Door | 1 × 2 | Opens onto a level landing, never straight onto a stair (villager pathing) |
| Clear ceiling | 3 blocks inside | Japanese homes 2.2 to 2.4 m [canon]; 3 keeps lanterns and jumps clear |
| Storey | 4 floor to floor (homes), 5 (shops, halls, the Academy) | The floor slab is the fourth block |
| Window | 1 wide × 1 or 2 high, sill at 1 above the floor | Set one block back from the wall face (§3) |
| Tatami | 1 × 2 blocks [canon: 88 × 176 cm] | `narutominecraft:tatami` is a 2 px mat laid ON the floor, seams staggered, never a four-corner cross |
| Rooms | 4.5 mats = 3 × 3; 6 mats = 3 × 4; 8 mats = 4 × 4 [canon] | Bedrooms 6 mats, a master or living room 8 |
| Genkan | 2 × 1 (flat), 2 × 2 (house) | Half a block below the house floor; the shoe cabinet beside it |
| Corridor | 1 wide in homes, 2 in public buildings | Two blocks of headroom over every stair step |
| Stair | 1 wide in homes, 3 in public; a landing every 6 to 8 steps | A partition and a door close a stair well (VF floods rooms door to door) |
| Street | main 7 (5 carriageway + kerbs), lane 5, alley 3 | `layout.json` widths |
| Plot | home 11 × 11 to 13 × 13; shop-house 6 to 11 wide, 11 to 15 deep | A third of a home plot is garden |

## 2. Walls: gradients and palettes

Rules [canon, Conquest gradient guide]: step only between neighbouring values; cluster the accent
blocks in irregular clumps (never rows, columns or salt-and-pepper splatter); darken under windows
and where rain runs; squint to judge. Buildings are "mainly yellow" [canon], so cream is the default.

| `kit.WALLS` | Field (about 85%) | Clusters (about 15%) | Under sills | Footing (1 course) | Grime band (street faces, 1 course above the footing) |
|---|---|---|---|---|---|
| `cream` | smooth_sandstone | cut_sandstone, sandstone | sandstone | stone_bricks, tuff, polished_andesite | sandstone with a little smooth_red_sandstone |
| `white` | calcite 70 / smooth_quartz 30 on large walls; smooth_quartz on small | calcite | polished_diorite | diorite then andesite | polished_diorite |
| `terracotta` | terracotta | brown_terracotta low, white_terracotta high (sun-bleached) | brown_terracotta | stone_bricks | brown_terracotta |
| `plaster_orange` | smooth_red_sandstone | red_sandstone, cut_red_sandstone | red_sandstone | stone_bricks | terracotta |
| machiya, Uchiha (new) | calcite above the 1.5-block line | | | dark_oak_planks or stripped_dark_oak_log boards below the line (koshikabe) | |

The kit gets one helper, `plaster(x0, y0, z0, x1, y1, z1, style, seed)`, that lays a palette's field
with seeded clusters, the sill darkening and the footing, so every building gets the same treatment
from a single call. Seeded, so a re-run gives the same wall.

## 3. Depth

Each step adds a shadow line. A flat wall with holes cut in it is the commonest flaw of the K1
buildings; every face from K4 on has at least the first four.

1. **Frame.** Posts (`style["post"]`) at the corners and every 3 to 5 blocks, one block proud of the
   plaster; or plaster set one block back between posts.
2. **Floor band.** A stripped log or a `dark_oak_slab` line proud of the wall at every floor.
3. **Windows recessed.** Glass or shoji one block back from the face; a bottom slab sill below, an
   upside-down stair lintel above; spruce trapdoors open as shutters, or a lattice (§5).
4. **Base step.** The footing course steps out half a block with a `stone_brick_slab` cap.
5. **Eaves.** Overhang 1 on homes and shop-houses, 2 on halls, temples, the Academy and the Residence;
   upside-down stairs or top slabs as the soffit; fences or dark oak trapdoors as rafter ends under the
   eave edge.
6. **Roof clutter.** On flat roofs: `narutominecraft:water_tank` on a four-leg fence frame (two or
   three a block, canon's skyline [canon: hospital tanks; art: everywhere]), iron_bars or chain pipes
   down the walls, lightning_rod antennas, a parapet of stone_brick_wall or a smooth_quartz_slab cap.

## 4. Roofs

| Roof | Where | How |
|---|---|---|
| Low gable (kirizuma) | Homes | `kit.gable_roof(pitch="low")`: alternating bottom and top slabs (about 22°). Odd widths centre the ridge |
| Curved (sori) | Halls, the shrine, clan gates, the Academy wings | First one or two courses at the eave as slabs, then stairs toward the ridge; an eave lip one course below the first row, one block out |
| Hip-and-gable (irimoya) | The Academy wings, clan halls, the Hyuga gate, the shrine, the Uchiha hall | A hip on all four sides to about two thirds of the height, then a small gable set one block in on the short ends, faced with planks or a trapdoor lattice |
| Hip (yosemune) | Shops, the tea houses | Four slopes to a short ridge |
| Pent (hisashi) | Every machiya front | A one-deep slab or stair skirt roof at the first-floor line, the full width of the shop front |
| Flat with parapet | Apartment blocks, the hospital, many town buildings [art] | A one-block parapet, tanks and pipes on top |

**Round buildings** (drum houses, round shops, tiered towers): a cylinder of radius 4 to 8 with posts
every 4 blocks round the face, each tier one block narrower than the one below, every tier capped by a
one-block skirt roof stepping out two blocks; a flat top with a tank, or a low cone. About one building
in twelve, in every district, so the round tower is a family, not a single landmark.

Ridges: one row capped with the kawara ridge block; each end gets a raised cap (onigawara: a wall
block and a slab, or the ridge block's end piece). Over about 15 × 15, split the roof into sections.
Colours keep the KONOHA_BUILD.md rule: **grey** (deepslate tile) for homes and the Uchiha quarter,
**green** (oxidised copper) for public buildings and the Academy, **orange** (cut copper) for shops
and the Residence's accents, and two new palettes for town buildings and round towers: **teal**
(weathered cut copper) and **blue** (light blue and cyan terracotta, with prismarine bricks for the
deeper course).

## 5. Fronts

- **Machiya front** (the market, Main Street's shop-houses, the Uchiha quarter): koshi lattice of
  spruce or dark oak fences (or open trapdoors) one block in front of glass or shoji on the ground
  floor; mushiko slats (iron_bars) in a low upper floor; a hisashi pent roof; bamboo inuyarai leaning
  at the wall base.
- **Shop opening:** noren over the door (`red_noren`, `indigo_noren`, `ramen_noren`, `tea_noren`), an
  awning (`red/green/indigo_awning`), a vertical sign board on the post beside the door, a paper lantern
  at the door.
- **Homes:** the door under a small one-deep porch roof, a stone step, a potted plant; the plaque
  beside the door.

## 6. Light

- **Hidden:** `minecraft:light[level=10..15]` inside eaves, under counters, in ceilings and behind
  shoji, so rooms glow without a torch in sight. The kit already passes any block state through.
- **Visible:** lanterns on chains under shop eaves every 4 to 6 blocks; paper lanterns at doors;
  stone lanterns at shrines, gardens and clan gates; a lit shoji (a light block behind it).
- **Rule:** no bare torches anywhere in the village.

## 7. Streets

| Street | Centre | Edges | Kerb | Extras |
|---|---|---|---|---|
| Main Street, Rock Road, Market Street, East Avenue | packed_mud and dirt_path | coarse_dirt and gravel in clusters | one row of polished_andesite or a stone_brick_slab | A one-wide gutter half a block down, covered by iron_bars or trapdoors at doors; utility poles every 12 blocks on alternate sides, wires sagging one block mid-span |
| Lanes | dirt_path | coarse_dirt | none | Lamps at crossings |
| Back alleys | gravel | moss at the walls | none | smooth_stone_slab stepping stones |

Gradient chain [canon]: grass, dirt_path, coarse_dirt, gravel, andesite or cobble, polished stone,
stone_bricks; cleaner in the centre, rougher at the edges. Squares at main crossings get a notice
board, a well, a tree and a lamp.

## 8. Terrain

- **Retaining walls (ishigaki):** cobblestone, stone, andesite and tuff mixed, battered one in per
  four up (stairs on the slope), capped with a stone_brick_slab row.
- **Stairs on slopes:** stone brick or spruce, a landing every 6 to 8 steps, fence or wall rails;
  slab ramps where the rise is one in two.
- **Terraces:** 3 to 5 blocks between levels (the hospital +4, the shrine +6 in two flights).
- **The river:** water two below the street, a stone-brick channel with steps down; reeds outside the
  wall.

## 9. Trees and gardens

Konoha is a leaf village: big broadleaf trees (dark oak and oak, custom canopies 15 to 25 high)
between buildings; cloud-pruned pines (spruce logs, flat leaf pads) in clan gardens; cherry
sparingly at the shrine, the Academy and the river; bamboo in clan gardens; azalea hedges; moss
carpet, ferns and short grass at wall bases. Every home plot keeps a third as garden: a tree or a
pine, a stone lantern, stepping stones from the gate.

**Tree budget.** Seen from the Rock the village should read as roofs in a forest. A big broadleaf every
15 to 20 blocks along every street (in the kerb line or a front garden, never on the carriageway);
one or two per home plot; a grove of three to five in every square, clan garden and park; the
Academy's swing tree and the shrine's woods as the largest. A tree is never closer than 2 blocks to a
wall, so canopies frame the roofs instead of hiding them.

## 10. Interiors

Every home a resident sleeps in gets a lived-in layout (the owner's feedback: today only tatami, a
bed, a chest, a low table and a lamp). **Player homes stay open**: the Classic flat (3a) and the
Varied candidate flats keep their open floor, because the player furnishes them (docs/HOME.md);
they get the fixed kitchen and bath fittings only.

### 10.1 Furnishing recipes (vanilla stand-ins)

The kit's helpers (`tools/konoha/kit.py`, K3); `f` is the way the piece faces, into the room.

| Piece | Kit helper | Blocks (stand-in) |
|---|---|---|
| Stove | `stove(x, y, z, f)` | a smoker, an iron_trapdoor hood two above |
| Fridge | `fridge(x, y, z)` | white_concrete two high |
| Counter, cupboards | `counter(x, y, z, f, cupboard=True)` | a barrel, an open spruce trapdoor two above as the wall cupboard |
| Low table (chabudai) | `low_table(x, y, z)` | a spruce bottom slab |
| Tansu | `tansu(x, y, z, f, top=None)` | a barrel, a pot or plant on top |
| Butsudan | `butsudan(x, y, z)` | stripped dark oak wood, three candles on top |
| Desk | `desk(x, y, z)` | a spruce top slab, a lantern on it |
| Toilet | `toilet(x, y, z)` | a hopper, a birch trapdoor lid |

Set directly in the designs: the sink (water_cauldron[level=3] in the counter run), the basin (an
empty cauldron), zabuton (carpets round the table), the TV (black_concrete on a spruce top slab),
shelves and the bookshelf beside a desk, plants (potted plants, decorated pots). Later pieces, with the Leaf set or
the batch that needs them: the genkan step, kotatsu, oshiire, tokonoma, kamidana, the tub, the
washer, the laundry pole, the shop counter, hidden light (`minecraft:light`).

Item frames and paintings are entities; the blueprint format carries blocks and markers only, so the
recipes use none. Clutter comes from blocks: pots, candles, books (chiseled bookshelves), banners,
decorated pots, carpet offcuts by the door.

### 10.2 Rules every interior keeps (villager pathing)

- The door opens onto a level, empty landing; two blocks of headroom over every stair step.
- A one-wide walk line from the door to every bed, the stove and the resident marker, free of
  furniture taller than a carpet or a trapdoor laid flat.
- Beds stay where their `bed` markers are; a moved bed moves its marker.
- No furniture on the house plaque, the mailbox or any anchor marker block.
- The House Plaque hangs outside on a solid wall, never on air: beside a home's door, on the gallery
  beside a flat's door, on a shop's front at its keeper's floor. The cell two behind it is room air:
  Village Friends floods the house from there.
- Low pieces (carpet, trapdoor tables, slabs) in the walk line; tall pieces against the walls.

### 10.3 Room programmes by home type

**Family house, two storeys** (`home_plaster_2f`, 7 × 5 inside per floor; Sakura Lane, the south
streets). Too small for a bath: the household uses the bath house (Shop Row), as small Japanese homes
did; the toilet and basin sit by the genkan.

- Ground floor: genkan (2 × 2) with the shoe cabinet and the stair start; LDK (living, dining,
  kitchen, about 5 × 4): a kitchen run along a wall (fridge, counter, sink, stove, counter, cupboards
  over), a dining table for four, the TV corner with cushions; a washitsu (6 mats) with a tokonoma, a
  butsudan and an oshiire; a washroom (washer and basin) opening to the bath (a 2 × 1 tub); a toilet
  under the stair.
- Upper floor: two bedrooms (6 mats each) with an oshiire or a tansu, a child's desk in one; a
  landing with a shelf; the balcony across the front with a laundry pole.

**One-storey house** (`home_plaster_1f`, planned): the ground floor above with the second bedroom in
place of the washitsu's tokonoma wall.

**Leaf Block flat** (10 × 8 inside: main room 6 × 6, kitchenette 3 × 4, bath 3 × 3, genkan, closet)
by household:

| Flat | Household | Main room |
|---|---|---|
| 1a | The landlady | Kotatsu and cushions, a tansu, a butsudan and kamidana, plants on every sill, a TV |
| 4b | Family with a child | Futon bed for the parents, a child's desk with books, toys (a decorated pot, a banner), a low dining table |
| Other resident flats | Single shinobi | Bed, a grindstone and a tool rack of open trapdoors, a desk with scrolls, a training dummy on the balcony |
| Other resident flats | Civilian worker | Bed, a low table and cushions, a tansu, a TV, laundry on the balcony |
| Other resident flats | Elder | Futon, a kotatsu, a butsudan, a tokonoma, bonsai pots |
| 3a, Varied candidates | The player | Kitchen and bath fittings only; the floor stays open |

The kitchenette gets fridge, sink, stove and a counter in every flat; the bath gets a tub, a toilet
and a basin.

**Keepers above their shops** (the grocer, the furniture shop, the weapon shop, Ichiraku's cook, the
tea house): one washitsu-bedroom (6 mats, a futon bed, an oshiire, a tansu), a small kitchen, and a
trade touch (ledgers and a desk for the grocer, offcuts and a workbench for the furniture maker, a
grindstone for the weapon smith, a stock of bowls for the cook, tea canisters for the tea house).

**Clan halls** (K9 onward): a formal room (8 mats or more) with a tokonoma and the clan banner, an
engawa round a garden, a family room with a kotatsu, the kitchen, bedrooms off a corridor.

**Barracks** (K14): six bunks (beds two high on a spruce frame), a locker of barrels per bunk, a
table, a duty board.

## Sources

Gathered in the research pass of the master plan; Narutopedia was reached through search snippets
only. Canon: Baidu Baike (Hidden Leaf Village: area, shape, colour), NaruSaku Wiki and the Wikipedia
2007 mirror (the gate's あん, four gates), Narutopedia (Hokage Rock, Residence, Academy, Uchiha Clan,
Naka River, Forest of Death). Technique: Conquest Reforged gradient guide; Minecraft Wiki roof
construction guidelines and furniture tutorial; 4netplayers and Sportskeeda path guides; the Cal Poly
minka guide. Interiors: e-housing.jp, Tofugu (washitsu), japan-experience (house lexicon), the tatami
size tables. Full notes, every link and the access caveats: [RESEARCH.md](RESEARCH.md).
