"""Wharf Trousers: plain cotton trousers rolled to the knee for the boat landing and the wet stone
of the fish market, bare shins and wooden geta."""
from kit_market import geta, rolled_cuffs
from paint import fabric, k, solid, strip_fabric

META = {"name": "Wharf Trousers", "gender": "unisex",
        "description": "Plain cotton trousers rolled to the knee, bare shins, wooden geta.",
        "tags": ["civilian", "trousers", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 36560, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 36560, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 36561 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "twill", 36561, 2)
    rolled_cuffs(g, "cuff", 4.0, "D", 36563)
    belt = g.piece("waist_cord", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.0, 0), inflate=.16)
    solid(belt, "L", "weave", 36565, 2, edge=False)
    geta(g)
