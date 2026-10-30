#!/usr/bin/env python3
"""The Konoha master layout (docs/konoha/MASTER_PLAN.md): keeps every built plot and street, re-cuts the districts,
adds the street network, the landmarks' footprints and the dense fabric between them as lots (FILL), checks
overlaps and renders the plan. Writes docs/konoha/master_layout.json and master_plan.png; batch K5 merges it.

  python tools/konoha/master.py
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import layout as L  # noqa: E402

lay = L.load()
built = [p for p in lay["plots"] if not p.get("planned")]
keep_streets = lay["streets"]

def rect(x0, z0, x1, z1): return [[x0, z0], [x1, z0], [x1, z1], [x0, z1]]

D = [  # id, name, polygon
 ("ridge", "Hokage Rock and the ridge", [[-262, -320], [312, -320], [312, -222], [-262, -222]]),
 ("foot", "The Foot (Residence)", rect(-110, -221, 204, -176)),
 ("central", "Central Leaf", rect(61, -98, 204, -37)),
 ("hospital", "Hospital Hill", rect(-140, -168, 53, -47)),
 ("academy", "Academy", rect(61, -168, 148, -104)),
 ("shrine", "Shrine Hill", rect(150, -168, 204, -104)),
 ("leaf_street", "Leaf Street", rect(-45, -45, 53, 22)),
 ("leaf_east", "Leaf Street east", rect(74, -36, 115, 14)),
 ("apartments", "Apartment Blocks", rect(-140, -45, -46, 40)),
 ("main_street", "Main Street", rect(36, -175, 78, 176)),
 ("market", "Civilian Market", rect(-140, 23, 53, 100)),
 ("shops", "Shop Row", rect(61, 20, 115, 125)),
 ("south", "South Residential", rect(-140, 101, 53, 168)),
 ("inuzuka", "Inuzuka and the gate quarter", rect(61, 126, 200, 168)),
 ("east", "East Quarters", rect(116, -37, 200, 125)),
 ("nara", "Nara forest", [[210, -221], [296, -221], [296, -40], [210, -40]]),
 ("stadium", "Stadium grounds", rect(210, -35, 306, 66)),
 ("southeast", "Training lanes", rect(210, 70, 306, 168)),
 ("west_bank", "West bank (Uchiha, riverside)", [[-262, -221], [-166, -221], [-166, 168], [-196, 168], [-262, 95]]),
 ("river", "The river", [[-170, -224], [-150, -224], [-150, 70], [-152, 135], [-175, 150], [-230, 150], [-236, 138], [-190, 128], [-166, 70]]),
 ("gate", "Main Gate and wall", rect(-200, 173, 220, 190)),
 ("prologue_hills", "Prologue Hills (outside)", rect(-210, 200, 30, 335)),
]
WALL = [[-200, 183], [-275, 90], [-275, -110], [-250, -222], [275, -222], [310, -110], [310, 90], [220, 183]]

S = [  # id, name, class, width, from, to
 ("rock_road", "Rock Road", "main", 7, [-140, -172], [204, -172]),
 ("academy_street", "Academy Street", "lane", 5, [61, -101], [204, -101]),
 ("hospital_road", "Hospital Road", "lane", 5, [-140, -138], [53, -138]),
 ("sakura_lane_w", "Sakura Lane (west)", "lane", 5, [-140, -28], [-45, -28]),
 ("leaf_street_w", "Leaf Street (west)", "lane", 5, [-140, 17], [-45, 17]),
 ("leaf_street_e", "Leaf Street (east)", "lane", 5, [61, 17], [203, 17]),
 ("market_street", "Market Street", "main", 7, [-140, 62], [53, 62]),
 ("shop_lane", "Shop Lane", "lane", 5, [61, 62], [204, 62]),
 ("south_lane", "South Lane", "lane", 5, [-140, 104], [53, 104]),
 ("haruno_lane", "Haruno Lane", "lane", 5, [-95, 137], [53, 137]),
 ("wall_lane", "Wall Lane", "lane", 5, [-196, 170], [215, 170]),
 ("river_road", "River Road", "lane", 5, [-143, -168], [-143, 168]),
 ("east_avenue", "East Avenue", "main", 7, [207, -168], [207, 168]),
 ("artists_lane", "Artists' Lane", "lane", 5, [150, -98], [150, 60]),
 ("uchiha_road", "Uchiha Road", "lane", 5, [-185, -200], [-185, 60]),
]

P = [  # id, name, district, x, z, w, d
 # the Rock
 ("hokage_faces", "Hokage Rock: the four faces", "ridge", -43, -266, 200, 40),
 ("archive_door", "Sealed door at the foot", "ridge", 128, -225, 3, 3),
 # the Foot
 ("senju", "Senju compound", "foot", -15, -215, 48, 40),
 ("uzumaki", "Uzumaki memorial compound", "foot", -60, -212, 40, 36),
 ("shimura", "Shimura clan home", "foot", -105, -212, 24, 24),
 ("sarutobi", "Sarutobi clan home", "foot", 82, -200, 24, 24),
 ("courier", "Courier office", "foot", 110, -190, 11, 11),
 ("jonin_station", "Jonin standby station", "foot", 124, -190, 11, 11),
 ("rock_stair", "The Rock's east stair and plaza", "foot", 172, -221, 30, 40),
 ("rock_walk", "Rock Walk (foot path)", "foot", -105, -221, 270, 3),
 # central
 ("hyuga", "Hyuga compound", "central", 64, -96, 48, 34),
 ("central_homes", "Garden houses", "central", 116, -96, 30, 30),
 ("shrine", "Shrine Hill", "shrine", 152, -140, 50, 36),
 # hospital hill
 ("hospital", "Hospital", "hospital", -70, -130, 56, 50),
 ("herb_garden", "Herb garden and Suzuran houses", "hospital", -135, -130, 60, 50),
 ("pharmacy", "Pharmacy", "hospital", -12, -132, 11, 11),
 ("yamanaka", "Yamanaka compound and flower shop", "hospital", 13, -90, 40, 36),
 # academy
 ("umino", "Teachers' houses (Umino)", "academy", 120, -165, 28, 30),
 # apartments
 ("apartment_2", "Apartment block", "apartments", -100, -45, 35, 15),
 ("apartment_3", "Apartment block", "apartments", -100, -24, 35, 15),
 ("apartment_4", "Apartment block", "apartments", -100, -1, 35, 15),
 ("tower_1", "Round apartment tower", "apartments", -62, -24, 13, 13),
 # market
 ("akimichi", "Akimichi compound", "market", -110, 26, 48, 30),
 ("barbecue", "Barbecue house", "market", -60, 26, 15, 13),
 ("stalls_n", "Market stalls (north row)", "market", -42, 52, 78, 5),
 ("stalls_s", "Market stalls (south row)", "market", -42, 67, 78, 5),
 # shops
 ("smithy", "Smithy and forge", "shops", 75, 42, 11, 11),
 ("tea_corner", "Rival tea houses", "shops", 61, 66, 26, 11),
 ("bath_house", "Bath house", "shops", 88, 26, 17, 15),
 # south
 ("park", "Village park", "south", -140, 107, 42, 60),
 # inuzuka and the gate quarter
 ("inuzuka", "Inuzuka compound and clinic", "inuzuka", 64, 126, 48, 40),
 ("cat_shelter", "Cat shelter", "inuzuka", 114, 128, 11, 11),
 ("barracks", "Gate barracks", "inuzuka", 130, 152, 14, 11),
 ("gate_stores", "Gate storehouse", "inuzuka", 130, 135, 14, 11),
 ("shiranui", "Shiranui house", "inuzuka", 148, 152, 11, 11),
 # east quarters
 ("hatake", "Hatake clan home", "central", 120, -60, 24, 22),
 ("yuhi", "Yuhi grove", "central", 160, -96, 30, 30),
 ("kurama", "Kurama studio (artists' lane)", "east", 155, -35, 24, 24),
 # the Nara forest
 ("nara", "Nara compound", "nara", 214, -165, 48, 40),
 ("deer_forest", "Deer forest", "nara", 214, -218, 80, 50),
 ("memorial", "Ino-Shika-Cho memorial", "nara", 270, -110, 9, 9),
 # stadium and training lanes
 ("stadium", "Chunin Exam stadium", "stadium", 212, -32, 94, 94),
 ("gekko", "Gekko dojo", "southeast", 214, 72, 24, 24),
 ("namiashi", "Namiashi dojo", "southeast", 242, 72, 20, 20),
 ("inner_field", "Inner training field", "southeast", 214, 100, 90, 64),
 # west bank
 ("uchiha_hall", "Uchiha gate and main hall", "west_bank", -240, -200, 36, 24),
 ("quarry", "The old quarry", "west_bank", -250, -221, 70, 18),
 ("tsuchigumo", "Tsuchigumo stone houses", "west_bank", -181, -200, 10, 24),
 ("morino", "Morino house", "west_bank", -258, -66, 24, 24),
 ("aburame", "Aburame clan home", "west_bank", -230, -66, 24, 24),
 ("vacant_sw", "Vacant estate", "west_bank", -258, 46, 40, 40),
 # the river
 ("ferry", "Ferry landings and the island", "river", -170, 95, 20, 20),
 # outside
 ("hideout", "Hideout", "prologue_hills", -180, 230, 40, 30),
 ("ruined_shrine", "Ruined shrine", "prologue_hills", -90, 300, 20, 20),
]

# The dense fabric: urban blocks cut into bands, each band a row of lots, a back alley or a lane.
# axis "x": rows run east-west and bands stack south from z0; axis "z": rows run north-south, bands stack east from x0.
# Band tokens: S shop-houses, T townhouses (machiya), H homes, W walk-ups (flat roofs, 3-5 storeys) with their depth;
# A a back alley, L a lane (odd widths). A lot that would overlap a landmark, a built plot or a street is skipped.
FILL = [  # id, district, x0, z0, x1, z1, axis, bands (earlier blocks win: Main Street's frontage first)
 ("ms_west", "main_street", 41, -47, 53, 168, "z", "S13"),
 ("ms_east", "main_street", 61, -37, 73, 168, "z", "S13"),
 ("h_rock", "hospital", -140, -168, 53, -143, "x", "S12 A3 H11"),
 ("h_hill", "hospital", -140, -80, 10, -47, "x", "L5 H12 A3 H11 L3"),
 ("h_lane", "hospital", -12, -120, 10, -82, "z", "H11 A3 H9"),
 ("h_east", "hospital", 14, -134, 53, -93, "x", "S12 A3 H12 L5 H10"),
 ("c_south", "leaf_east", 74, -36, 115, 7, "x", "T12 A3 T12 L5 T12"),
 ("a_east", "academy", 120, -134, 147, -108, "x", "H12 A3 H12"),
 ("c_west", "central", 61, -60, 115, -38, "x", "S10 A3 T10"),
 ("c_east", "central", 145, -65, 203, -39, "x", "T12 A3 S12"),
 ("ap_n", "apartments", -140, -45, -104, -33, "x", "W13"),
 ("ap_s", "apartments", -140, -25, -104, 12, "x", "W15 A3 W15 L5"),
 ("ap_tn", "apartments", -62, -45, -46, -33, "x", "W13"),
 ("ap_ts", "apartments", -62, -10, -46, 14, "x", "W12 A3 W10"),
 ("m_north", "market", -42, 23, 53, 50, "x", "L3 S11 A3 S11"),
 ("m_south", "market", -140, 73, 53, 98, "x", "T12 A3 T11"),
 ("m_west", "market", -140, 23, -112, 49, "x", "H12 A3 H12"),
 ("s_row", "shops", 61, 79, 115, 122, "x", "S12 A3 S12 L5 T12"),
 ("s_mid", "shops", 88, 42, 115, 53, "x", "S12"),
 ("s_bath", "shops", 106, 21, 115, 40, "z", "S10"),
 ("so_n", "south", -95, 107, 53, 132, "x", "H12 A3 H11"),
 ("so_s", "south", -95, 140, 53, 166, "x", "H12 A3 H12"),
 ("g_east", "inuzuka", 160, 126, 200, 166, "x", "T12 A3 H12 L3 H11"),
 ("e_north", "east", 116, -37, 147, 14, "x", "H12 A3 H12 L3 H11 A3 H8"),
 ("e_artists", "east", 154, -10, 203, 13, "x", "T11 A3 T10"),
 ("e_mid", "east", 116, 20, 147, 59, "x", "S12 A3 H12 L3 H10"),
 ("e_market", "east", 154, 20, 203, 59, "x", "S12 A3 S12 L3 T10"),
 ("e_south", "east", 116, 65, 203, 122, "x", "S12 A3 H12 L5 H12 A3 H11"),
 ("w_tobari", "west_bank", -258, -40, -190, 35, "x", "T12 A3 T12 L5 H12 A3 H12 L5 H12"),
 ("w_river", "west_bank", -182, -40, -171, 59, "z", "H12"),
 ("w_uchiha", "west_bank", -258, -172, -190, -78, "x", "L5 H12 A3 H12 L5 H12 A3 H12 L5 H12 A3 H11"),
 ("f_east", "foot", 136, -205, 170, -179, "x", "S12 A3 S12"),
]
KINDS = {  # lot widths along the row (cycled), the gap between lots, a name
 "S": ((8, 7, 10, 9, 7, 11, 8), 0, "Shop-house"),
 "T": ((6, 7, 6, 8, 7), 0, "Townhouse"),
 "H": ((9, 10, 8, 11, 9), 1, "Home"),
 "W": ((13, 15, 12, 14), 2, "Walk-up"),
}
PASSAGE = 42   # a three-wide passage crosses each block about this often along its rows


def fill(fixed, streets):
    """Lots and their alleys, lanes and passages for every FILL block, clear of `fixed` rects and every street."""
    lots, new, fixed = [], [], list(fixed)

    def rect(axis, run0, run1, c0, c1):
        return (run0, c0, run1, c1) if axis == "x" else (c0, run0, c1, run1)

    def street(sid, name, cls, width, axis, mid, a, b):
        ends = ([a, mid], [b, mid]) if axis == "x" else ([mid, a], [mid, b])
        new.append({"id": sid, "name": name, "class": cls, "width": width, "from": ends[0], "to": ends[1]})

    for bid, dist, x0, z0, x1, z1, axis, bands in FILL:
        run0, run1, c = (x0, x1, z0) if axis == "x" else (z0, z1, x0)
        cend = z1 if axis == "x" else x1
        # passages first, where they cross no landmark (they run across the bands, so on the other axis)
        prects = []
        for i, q in enumerate(range(run0 + PASSAGE, run1 - 14, PASSAGE)):
            r = rect(axis, q, q + 2, c, cend)
            if not any(L.overlap(r, o) for o in fixed):
                prects.append(r)
                street(f"{bid}_p{i}", "Passage", "alley", 3, "z" if axis == "x" else "x", q + 1, c, cend)
        k = 0
        for tok in bands.split():
            t, n = tok[0], int(tok[1:])
            if t in "AL":   # the band's free stretches, at least 10 long
                start = None
                for q in range(run0, run1 + 2):
                    ok = q <= run1 and not any(L.overlap(rect(axis, q, q, c, c + n - 1), o) for o in fixed)
                    if ok and start is None:
                        start = q
                    if not ok and start is not None:
                        if q - start >= 10:
                            street(f"{bid}_{t.lower()}{k}", "Back alley" if t == "A" else "Lane",
                                   "alley" if t == "A" else "lane", n, axis, c + n // 2, start, q - 1)
                            k += 1
                        start = None
            else:
                widths, gap, name = KINDS[t]
                block = fixed + prects + [L.street_rect(s) for s in streets + new]
                q, i = run0, 0
                while q <= run1:
                    w = widths[i % len(widths)]
                    if q + w - 1 > run1:
                        break
                    r = rect(axis, q, q + w - 1, c, c + n - 1)
                    if any(L.overlap(r, o) for o in block):
                        q += 1
                        continue
                    fixed.append(r)
                    lots.append({"id": f"{bid}_{len(lots)}", "name": name, "district": dist, "planned": True, "lot": t,
                                 "at": [r[0], 0, r[1]], "size": [r[2] - r[0] + 1, r[3] - r[1] + 1]})
                    q, i = q + w + gap, i + 1
            c += n
        assert c - 1 <= cend, (bid, c - 1, cend)
    return lots, new


district_ids = {d[0] for d in D}
plots = [dict(p, district=p["district"] if p["district"] in district_ids else ("leaf_street" if p["district"] == "leaf_street" else p["district"])) for p in built]
for p in plots:  # built plots keep their place (the Academy moves to the Rock's foot, canon); re-file their districts
    if p["id"] == "academy": p["at"] = [61, 0, -168]
    p["district"] = {"residence": "foot", "gate": "gate", "shops": "shops", "market": "market", "academy": "academy"}.get(p["district"], p["district"])
for pid, name, dist, x, z, w, d in P:
    plots.append({"id": pid, "name": name, "district": dist, "planned": True, "at": [x, 0, z], "size": [w, d]})
streets = keep_streets + [{"id": i, "name": n, "class": c, "width": w, "from": a, "to": b} for i, n, c, w, a, b in S]
lots, alleys = fill([L.footprint(p) for p in plots], streets)
plots += lots
streets += alleys
out = {"format": "konoha-layout/1", "notes": "Master plan draft (docs/konoha/MASTER_PLAN.md); batch K5 merges it into tools/konoha/layout.json.",
       "map": lay["map"], "spawn": lay["spawn"], "border": {"x": 18.5, "z": 7.5, "size": 680}, "wall": WALL,
       "districts": [{"id": i, "name": n, "polygon": poly} for i, n, poly in D], "streets": streets, "plots": plots}

# overlaps: plots against plots and streets (streets may cross streets)
rects = {p["id"]: L.footprint(p) for p in plots}
srects = {s["id"]: L.street_rect(s) for s in streets}
bad = []
ids = list(rects)
for i, a in enumerate(ids):
    for b in ids[i + 1:]:
        if L.overlap(rects[a], rects[b]): bad.append((a, b))
    for s, r in srects.items():
        if L.overlap(rects[a], r) and a not in ("rock_walk",): bad.append((a, s))
for a, b in bad: print("overlap", a, b, rects[a], rects.get(b) or srects[b])
(ROOT / "docs/konoha").mkdir(exist_ok=True)
(ROOT / "docs/konoha/master_layout.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")

# render: the layout plan, then the wall ring and the river on top
from PIL import ImageDraw
L.SCALE = 2
png = L.plan(dict(out, plots=[p for p in plots if "lot" not in p]), ROOT / "docs/konoha/master_plan.png")
from PIL import Image
img = Image.open(png)
dr = ImageDraw.Draw(img, "RGBA")
b = out["border"]; ox, oz = b["x"] - b["size"] / 2, b["z"] - b["size"] / 2
pt = lambda x, z: ((x - ox) * 2, (z - oz) * 2)
river = next(d for d in D if d[0] == "river")[2]
dr.polygon([pt(*q) for q in river], fill=(60, 110, 200, 200))
dr.line([pt(*q) for q in WALL + WALL[:1]], fill=(120, 90, 60, 255), width=8)
for q in WALL: dr.ellipse([pt(*q)[0] - 9, pt(*q)[1] - 9, pt(*q)[0] + 9, pt(*q)[1] + 9], fill=(90, 70, 50, 255))
LOT = {"S": (190, 110, 80), "T": (200, 170, 120), "H": (235, 220, 180), "W": (150, 160, 185)}
for p in lots:
    r = L.footprint(p)
    dr.rectangle([pt(r[0], r[1]), (pt(r[2] + 1, r[3] + 1)[0] - 1, pt(r[2] + 1, r[3] + 1)[1] - 1)],
                 fill=LOT[p["lot"]] + (255,), outline=(60, 50, 40, 255))
# the view axis: gate to the faces
dr.line([pt(57, 183), pt(57, -260)], fill=(255, 255, 255, 120), width=2)
img.save(png)
print("plots", len(plots), "lots", {t: sum(p.get("lot") == t for p in plots) for t in KINDS},
      "streets", len(streets), "bad", len(bad))
