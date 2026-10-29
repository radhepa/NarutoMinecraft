"""Medicine Peddler's Kimono: the travelling seller's kasuri kimono hitched up short for the road,
a lacquered chest of little drawers strapped on the back, its brass pulls catching the light."""
from kit_kurama import wrap_front
from kit_market import kasuri, sash, sleeves
from paint import cap, k, solid, strip_fabric

META = {
    "name": "Medicine Peddler's Kimono",
    "gender": "unisex",
    "description": "Kasuri kimono hitched short for the road, a lacquered chest of little drawers strapped on the back.",
    "tags": ["civilian", "kimono", "wrap", "work"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 36480, 2)
    cap(body, "P", seed=36480)
    for face in body.sides:
        kasuri(face, k("S", 1), 36481 + face.x0)
    wrap_front(body.front, "S3", "P1", rows=8, start=1)
    sleeves(g, "P", "weave", 36482, rows=(0, 8))
    for side in ("right", "left"):
        kasuri(g.part(f"{side}_sleeve").strip, k("S", 1), 36484, rows=range(0, 8))
    sash(g, "sash", "K", 36486, y=8.6, height=2, base=3, knot="front")
    for x in (1, 6):
        jacket.front.vline(x, 0, 6, "L1")
        jacket.top.set(x, 3, "L1"), jacket.top.set(x, 2, "L1")
    box = g.piece("drawer_chest", "TORSO", (-3.5, 0, 0), (7, 9, 3), pivot=(0, .6, 2.3))
    solid(box, "K", "smooth", 36488, 3)
    box.top.fill("K4")
    for y in (0, 3, 6):
        box.back.hline(0, 6, y, "L2")
    for y in (1, 4, 7):
        box.back.set(3, y, "M4")
        box.back.hline(1, 2, y + 1, "K2"), box.back.hline(4, 5, y + 1, "K2")
