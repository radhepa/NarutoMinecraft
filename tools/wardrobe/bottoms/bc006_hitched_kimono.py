"""Hitched Kimono: a kimono skirt pulled up and tucked into the sash at the back for running
errands, showing close dark leggings, cloth gaiters and straw sandals underneath."""
from kit import flaps
from kit_market import kyahan, straw_sandals
from paint import fabric, k, strip_fabric

META = {"name": "Hitched Kimono", "gender": "unisex",
        "description": "Kimono skirt tucked up at the back over dark leggings, cloth gaiters and straw sandals.",
        "tags": ["civilian", "kimono", "skirt", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36590, 2, 9, 11)
    fabric(body.bottom, "P", "weave", 36590, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 36591 + (side == "left"), 3, 0, 9)
        fabric(leg.top, "K", "twill", 36591, 3)
    front, back = flaps(g, "skirt", 4, "P", "weave", 36593, width=9, hem=k("P", 1), top=11.2)
    front.vline(5, 1, 3, k("P", 3))
    back.hline(0, 8, 0, k("P", 1)), back.hline(0, 8, 1, k("P", 3))
    kyahan(g, "S", rows=(5, 9), seed=36595, tie=k("D", 2))
    straw_sandals(g)
