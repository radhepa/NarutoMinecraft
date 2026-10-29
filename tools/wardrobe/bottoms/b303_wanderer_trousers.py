"""Wanderer Trousers: dark trousers to the ankle under a navy cloth hung from the waist to the knee
front and back, tied with a cord, over navy sandals."""
from kit import flaps
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Wanderer Trousers", "gender": "unisex",
        "description": "Dark ankle trousers under a navy waist cloth to the knee, navy sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 3970, 2, 9, 11)
    fabric(body.bottom, "K", "twill", 3970, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 3971 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "K", "twill", 3971, 2)
        leg.strip.hline(0, leg.strip.w - 1, 9, "K3")
    sandals(g)
    for face in flaps(g, "waist_cloth", 7, "D", "weave", 3973, width=8, hem="D1", top=10.4, front_z=-2.9, back_z=1.9):
        face.vline(2, 1, 6, "D1"), face.vline(5, 1, 6, "D1")
    cord = g.piece("waist_cord", "TORSO", (-4.6, 0, -2.6), (9, 1, 5), pivot=(0, 9.6, 0), inflate=.35)
    solid(cord, "D", "weave", 3975, 3, edge=False)
