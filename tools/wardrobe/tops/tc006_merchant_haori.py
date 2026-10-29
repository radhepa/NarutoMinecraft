"""Merchant's Haori: the shop owner's short haori over a striped kosode, the front held by a pale
braided himo tie, the sleeves hanging square, and an abacus tucked in the obi at the hip."""
from kit import flaps
from kit_kurama import kimono_sleeves, wrap_front
from kit_market import stripes
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Merchant's Haori",
    "gender": "unisex",
    "description": "Short haori with a braided tie over a striped kosode, square hanging sleeves, an abacus at the hip.",
    "tags": ["civilian", "coat", "kimono", "wrap"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 36120, 2)
    cap(body, "S", seed=36120)
    for face in body.sides:
        stripes(face, k("P", 1), 2, offset=1)
    wrap_front(body.front, "S4", None, rows=8, start=2)
    strip_fabric(jacket, "P", "weave", 36121, 2)
    fabric(jacket.top, "P", "weave", 36121, 3)
    fabric(jacket.bottom, "P", "weave", 36121, 1)
    for y in range(12):
        for x in range(2, 6):
            jacket.front.clear(x, y)
        jacket.front.set(1, y, "P3"), jacket.front.set(6, y, "P3")
    # The himo: two braided cords meeting in a knot at the breastbone.
    jacket.front.set(2, 4, "S3"), jacket.front.set(5, 4, "S3"), jacket.front.set(3, 5, "S4"), jacket.front.set(4, 5, "S4")
    jacket.front.set(3, 6, "S2"), jacket.front.set(4, 7, "S2")
    kimono_sleeves(g, "P", "weave", 36122, length=8, top=-2.3, bell=False)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 36124, 2, 0, 7)
    for face in flaps(g, "haori_hem", 3, "P", "weave", 36126, width=9, top=11.0, front_z=-3.0, back_z=2.0, slit=True):
        face.hline(0, 8, 2, "P1")
    obi = g.piece("obi", "TORSO", (-4.5, 0, -2.5), (9, 2, 5), pivot=(0, 8.4, 0), inflate=.12)
    solid(obi, "K", "weave", 36128, 3, edge=False)
    abacus = g.piece("abacus", "TORSO", (-.5, 0, -2), (1, 3, 4), pivot=(-4.9, 7.6, -.4), rotation=(0, 0, 8))
    solid(abacus, "L", "smooth", 36129, 2)
    for face in (abacus.right, abacus.left):
        for y in range(3):
            for x in range(0, 4, 2):
                face.set(x, y, "K1")
            face.set(1 + y % 2, y, "L4")
