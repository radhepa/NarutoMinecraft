# Konoha district sheets

One sheet per district of the [master plan](MASTER_PLAN.md). Footprints are the draft's
(`master_layout.json`: x, z of the north-west corner, then width by depth). A **Fabric** line counts
the district's everyday lots (`tools/konoha/master.py`, `FILL`), built from the signed-off building
families (K4) and pasted in K5. Batches are in [BATCHES.md](BATCHES.md). Spoiler-free.

## The Rock and the ridge

- **Bounds** x -262..312, z -320..-222. The ridge is the village's north wall.
- **Holds** the four faces (x -43..156, z -266..-227 in plan, carved into the face's upper third);
  the falls at x about -160; the old quarry cut into the face at the west end; forest on top, never
  built (canon keeps the plateau wild in this era).
- **Story** the sealed door (Rock Walk, x 128); the east stair's top landing and lookout.
- **Batch** K11 (massing and face drafts; the owner finishes the faces).

## The Foot

- **Bounds** x -110..204, z -221..-176. Faces Rock Road (z -172).
- **Built** the Hokage Residence (x 33-81).
- **Planned** Senju compound (-15, -215, 48 × 40) west of the Residence, its hall around a living
  tree; Uzumaki memorial compound (-60, -212, 40 × 36); Shimura clan home (-105, -212, 24 × 24), near
  the cliff; Sarutobi clan home (82, -200, 24 × 24) east of the Residence; courier office
  (110, -190, `shop_house`); jonin standby station (124, -190, `shop_house` variant, B2); the stair
  plaza and the east stair (172, -221, 30 × 40); Rock Walk along the cliff foot.
- **Fabric** 8 shop-houses east of the stair plaza (x 136..170).
- **People** clan families (Senju, Uzumaki few, Sarutobi, Shimura); couriers (4).
- **Anchors** `residence.mission_desk`, `residence.records`, the council gallery (B2).
- **Batch** K9 (clan gates and halls, courier office), K11 (Rock Walk, stair).

## Shrine Hill

- **Bounds** x 150..204, z -168..-104, east of the Academy.
- **Planned** the shrine (152, -140, 50 × 36, raised 6): torii at the foot on Academy Street, steps,
  hall, bell, offering box, wish plaques, komainu; the woods and bamboo grove behind it up to Rock Road
  (`gather:bamboo_grove`).
- **People** the shrine keeper.
- **Anchors** `shrine.steps`, `shrine.hall`, `shrine.roof`.
- **Batch** K9.

## Central Leaf

- **Bounds** x 61..204, z -98..-37, between Academy Street and the Leaf Street blocks.
- **Planned** Hyuga compound (64, -96, 48 × 34): two halves, main and branch house, a dojo and a koi
  pond; garden houses (116, -96, block of 2 `home_garden`); Yuhi grove (160, -96): a house among old
  trees; Hatake clan home (120, -60): a lone worn house with kennels.
- **Fabric** 26 lots south of the compounds (11 shop-houses, 15 townhouses); Leaf Street east
  (x 74..115, z -36..14) 18 townhouses.
- **People** Hyuga (4 to 6), two elder households, small clans.
- **Batch** K9 (Hyuga, garden houses), K13 (Yuhi, Hatake).

## Hospital Hill

- **Bounds** x -140..53, z -168..-47.
- **Planned** Hospital (-70, -130, 56 × 50) on a +4 terrace: five storeys of white plaster, glass,
  flat roof with tanks, wards and the desk, the wake room; herb garden and the Suzuran herbalists'
  houses (-135, -130, block) behind it (`gather:herb_garden`); pharmacy (-12, -132, `shop_house`);
  Yamanaka compound (13, -90, 40 × 36) with the flower shop fronting Main Street and the greenhouse
  behind.
- **Fabric** 77 lots: shop-houses along Rock Road, homes on the hill's lanes (z -80..-47) and on the
  lane east of the pharmacy.
- **People** medics (6, day and night), herbalists, the Yamanaka, families.
- **Anchors** `hospital.desk`, `hospital.ward`, `herb_garden`, `clan.yamanaka.shop`.
- **Batch** K8.

## Academy

- **Bounds** x 61..148, z -168..-104, at the Rock's foot across Rock Road from the Residence (canon).
- **Built** the Academy with its yard and swing tree, today at z -120..-57; K5 moves the plot to
  (61, -168) and its anchors with it.
- **Planned** teachers' houses (Umino, 120, -165, block of 3 homes) beside it.
- **Fabric** 4 homes south of the teachers' houses.
- **People** teachers (5, day).
- **Anchors** `academy.grounds`, `academy.yard`, `academy.library` (placed).
- **Batch** K9 (the teachers' houses with the Central Leaf work); the exam hall in K16.

## Leaf Street

- **Bounds** x -45..53, z -45..22. **Built**: the Leaf Block (the player's flat 3a), the tea house,
  the training yard, Sakura Lane's 14 homes.
- **Next** the facade pass with the building families (K4).

## Apartment Blocks

- **Bounds** x -140..-46, z -45..40, on Sakura Lane and Leaf Street west.
- **Planned** three Leaf apartment blocks (-100, -45 / -24 / -1, 35 × 15 each), one round apartment
  tower (-62, -24, 13 × 13, six storeys, a large tank on top); a district well.
- **Fabric** 9 walk-ups west of the blocks and round the tower.
- **People** clanless shinobi and young families (about 45); the Varied candidate flats.
- **Batch** K10.

## Main Street

- **Bounds** x 36..78, z -175..176, the frontages on both sides of the axis.
- **Built** Ichiraku, the grocer, the furniture shop, the weapon shop.
- **Rules** continuous frontage, every ground floor a shop, keepers living above; a 3-wide passage
  about every 42 blocks; poles, lamps and the notice board at the Leaf Street crossroads.
- **Fabric** 20 shop-house lots filling the gaps on both sides.
- **Batch** K5 (the fabric), each district's batch for its landmarks.

## Civilian Market

- **Bounds** x -140..53, z 23..100, on Market Street (z 62).
- **Planned** Akimichi compound (-110, 26, 48 × 30): a kitchen hall and storehouse; the barbecue house
  (-60, 26, `restaurant`); the market's shops (the barber, the haruno store, the oil
  seller, a courier box, as shop-house lots); stall rows north and south of Market Street (-42, 52 and 67,
  six `market_stall` each); the market well (the coldest).
- **Fabric** 68 lots: shop-houses north of the stalls, townhouse rows south of them (z 73..98), homes
  west of the Akimichi.
- **People** civilians (about 40): stallholders, the barber, families in the townhouses.
- **Anchors** `market.stall`, `market.grocer`, `market.oil`, `market.fish`, `shop_storeroom`, `warehouse`.
- **Batch** K7.

## Shop Row

- **Bounds** x 61..115, z 20..125, east of Main Street on Shop Lane.
- **Built** the furniture and weapon shops.
- **Planned** smithy and forge (75, 42, B2); bath house (88, 26, B2) with the boiler room and the mural
  wall; the rival tea houses on the Shop Lane corner (61, 66, two `shop_tea_house`); the village inn on
  Main Street.
- **Fabric** 21 lots south of Shop Lane and round the bath house: the scroll shop, tool shop, tailor,
  pawn shop and bookshop among the shop-houses.
- **Anchors** `market.tea`, `bathhouse`, `bathhouse.boiler`, `inn`, `office`.
- **Batch** K7 (tea houses), K15 (bath house, inn, smithy).

## South Residential

- **Bounds** x -140..53, z 101..168, on South Lane (z 104) and Haruno Lane (z 137).
- **Planned** the village park (-140, 107, 42 × 60) on the river: trees, a pond, benches, pet hideouts.
- **Fabric** 44 home lots in four rows on South Lane and Haruno Lane, the Haruno house among them.
- **People** civilian families (about 40).
- **Anchors** `client_home`, `client_garden`, `vacant_home`, `pet_hideout`, `park`, `residential_lane`.
- **Batch** K10.

## Inuzuka and the gate quarter

- **Bounds** x 61..200, z 126..168.
- **Planned** Inuzuka compound and clinic (64, 126, 48 × 40): kennels, the open run, the veterinary
  clinic; the cat shelter (114, 128, `shop_house`); gate storehouse (130, 135); gate barracks (130, 152,
  six bunks); Shiranui house (148, 152) with its senbon target wall.
- **Fabric** 14 lots east of the Shiranui house (townhouses and homes).
- **People** the Inuzuka, gate guards, families (about 25).
- **Anchors** `gate.stores`; the clinic's pet shop.
- **Batch** K7 (the Inuzuka compound and clinic, the cat shelter), K14 (barracks, storehouse, Shiranui).

## East Quarters

- **Bounds** x 116..200, z -37..125, on Artists' Lane (x 150), Leaf Street east and Shop Lane.
- **Planned** Kurama studio (155, -35) on Artists' Lane; two more round towers (K10).
- **Fabric** 85 lots: artists' townhouses below the studio, homes west of Artists' Lane, shop-houses
  and townhouses on Shop Lane east, homes to the south.
- **People** families, artists, small clans (about 30).
- **Batch** K13.

## Nara forest

- **Bounds** x 210..296, z -221..-40, against the ridge and the east wall.
- **Planned** Nara compound (214, -165, 48 × 40): a plain house and the clan's workrooms; the deer forest
  (214, -218, and the woods south of the compound) with clearings and deer; the Ino-Shika-Cho memorial
  (270, -110).
- **Anchors** `clan.nara.forest`, `forest_edge`.
- **Batch** K13.

## Stadium grounds and training lanes

- **Stadium** (212, -32, 94 across): the Chunin Exam arena (K13).
- **Training lanes** (x 210..306, z 70..168): Gekko dojo with its moon platform (214, 72), Namiashi
  dojo (242, 72), the inner training field (214, 100) (K15).

## West bank

- **Bounds** x -262..-166, z -221..168, across the river from the centre, raised 2.
- **Planned** the Uchiha quarter (x -258..-190, z -200..-72, walled): the gate and main hall
  (-240, -200), the shrine, the senbei shop, the police HQ in its far corner; the old quarry
  (-250, -221) and the Tsuchigumo stone houses (-181, -200) at its mouth; the Morino house (-258, -66)
  with barred windows; the Aburame clan home (-230, -66) with insect gardens; a vacant estate (-258, 46).
- **Fabric** 81 lots: the Uchiha quarter's homes inside its wall (z -172..-78), the Tobari lanes'
  shuttered townhouses and homes (z -40..35), the riverside houses on Uchiha Road (verandas over the bank).
- **Anchors** `riverbank`, `river_jetty`, `gather:river`, `clan.aburame.garden`, `hiding_spot`.
- **Batch** K12 (river, bridges, ferry, the Uchiha wall, gate, hall, shrine and shop, Aburame, Morino).

## The river

- Falls at x about -160 from the ridge; channel x -170..-150 (stone banks, steps to the water) to
  z 70; the ferry reach (z 70-135, up to 40 wide) with the island (one pine, many ducks) and the ferry
  landings; leaves by a water gate in the south-west wall toward Training Ground 3 and the lake.
- **Batch** K6 (terrain: the channel and water), K12 (bridges, landings, the island).

## Main Gate and wall

- **Built** the gate (x 37-77) and ten wall modules (x -43..157).
- **Planned** the rest of the south front (x -200..-44 and 158..220), the diagonals and sides, a
  watch tower at every corner of the ring (8) and between (to 16), the water gate; the guard booth
  with the travel desk; the dusk and dawn gate swap.
- **Anchors** `gate.main`, `gate.travel_desk`.
- **Batch** K14 (gate quarter), K13 (the ring's east), K12 (the ring's west).

## Outside the wall

| Place | Where | Batch |
|---|---|---|
| Prologue hills: the hideout, a ruined shrine | South, x -210..30, z 200..335 | K14 |
| Training Ground 3 (three stumps, the memorial stone, the river, forest on both banks) | South-west, downstream of the water gate | K16 |
| The lake ground and the cliff ground | South-west and west | K16 |
| Farmsteads, orchard, woodlot | South-east, outside the gate | Later (the outside world) |
| The east road, its bridge, ford, bend, campsite and waystation | From the gate eastwards | Later (the outside world) |
| Bandit camps | In the outer hills | Later (the outside world) |
| The Forest of Death (384 across), its fence, 44 gates and the tower | East of the wall | K16 |
