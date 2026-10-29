"""Sagari Shorts: dark knee shorts under a thick folded mawashi band with a fringe of stiff sagari
cords hanging in front, bandaged shins and open-toe sandals: a sumo wrestler's waist on a shinobi."""
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Sagari Shorts", "gender": "unisex",
        "description": "Dark knee shorts, a thick mawashi band with sagari cords, bandaged shins, sandals.",
        "tags": ["shinobi", "akimichi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "rib", 6943, 2, 9, 11)
    fabric(body.bottom, "K", "rib", 6943, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "weave", 6944 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "K", "weave", 6944, 2)
        leg.strip.hline(0, leg.strip.w - 1, 4, "K3")
    wraps(g, 5, 9)
    sandals(g)
    band = g.piece("waist_mawashi", "TORSO", (-4.5, 9.2, -2.5), (9, 3, 5), inflate=.5)
    solid(band, "A", "rib", 6946, 2, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 0, "A3"), face.hline(0, face.w - 1, 2, "A1")
    for i, x in enumerate((-2.4, -1.2, 0, 1.2, 2.4)):
        cord = g.piece(f"waist_sagari_{i}", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(x, 12.2, -3.2), motion="flap_front")
        solid(cord, "A", "smooth", 6947 + i, 2)
