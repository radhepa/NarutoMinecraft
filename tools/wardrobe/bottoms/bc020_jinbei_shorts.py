"""Jinbei Shorts: the loose kasuri shorts that go with a jinbei, cut above the knee with a
drawstring, for summer evenings at the stall, with wooden geta."""
from kit_market import geta, kasuri
from paint import fabric, k, solid, strip_fabric

META = {"name": "Jinbei Shorts", "gender": "unisex",
        "description": "Loose kasuri shorts cut above the knee with a drawstring, wooden geta.",
        "tags": ["civilian", "shorts", "casual"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36800, 2, 9, 11)
    fabric(body.bottom, "P", "weave", 36800, 1)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "P", "weave", 36801, 2, 0, 3)
        fabric(leg.top, "P", "weave", 36801, 2)
        strip_fabric(pants, "P", "weave", 36802 + (side == "left"), 2, 0, 3)
        kasuri(pants.strip, k("S", 2), 36804, rows=range(0, 3))
        pants.strip.hline(0, pants.strip.w - 1, 3, k("P", 1))
    knot = g.piece("waist_string", "TORSO", (-.5, 0, -.5), (1, 2, 1), pivot=(0, 9.4, -2.5), scale=(.6, 1, .6), motion="sway")
    solid(knot, "K", "weave", 36806, 3)
    geta(g)
