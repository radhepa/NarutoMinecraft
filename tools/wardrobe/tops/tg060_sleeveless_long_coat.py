"""Sleeveless Long Coat: a knee-length sleeveless coat open at the front over a fitted top, split up
the back, a high turned collar and a wide belt cinching the waist: a jonin's travelling coat."""
from kit import belt, collar, flaps, side_panels
from paint import cap, fabric, strip_fabric

META = {
    "name": "Sleeveless Long Coat",
    "gender": "unisex",
    "description": "Knee-length open sleeveless coat over a fitted top, split back, high collar, wide belt.",
    "tags": ["shinobi", "jonin", "coat"],
    "rejects": ["skirt"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "plain", 33380, 2)
    cap(body, "S", seed=33380)
    strip_fabric(jacket, "P", "twill", 33381, 2)
    fabric(jacket.top, "P", "twill", 33381, 3)
    for y in range(12):
        for x in (3, 4):
            jacket.front.clear(x, y)
        jacket.front.set(2, y, "P3"), jacket.front.set(5, y, "P1")
    for side in ("right", "left"):
        g.part(f"{side}_arm").strip.hline(0, 15, 0, "S2")
        g.part(f"{side}_arm").strip.hline(0, 15, 1, "S1")
    band = belt(g, "belt", y=8.6, role="K", height=2, buckle="M")
    for face in flaps(g, "coat", 9, "P", "twill", 33383, width=9, hem="P1", top=11.4, slit=True):
        face.vline(0, 1, 8, "P1"), face.vline(8, 1, 8, "P3")
    side_panels(g, "coat_side", 8, "P", "twill", hem="P1", top=11.4)
    neck = collar(g, "collar", "P", "twill", height=2, y=-1.6)
    neck.front.hline(3, 5, 0, "P0"), neck.front.hline(3, 5, 1, "P0")
