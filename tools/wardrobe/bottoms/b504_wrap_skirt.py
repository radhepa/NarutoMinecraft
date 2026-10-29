"""Wrap Skirt: a calf-length wrap skirt over dark leggings, the overlap slit at the front, with soft
flat sandals: worn with the household's wrap blouses and aprons."""
from kit import flaps
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Wrap Skirt", "gender": "female",
        "description": "Calf-length wrap skirt slit at the front over dark leggings, flat sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 5631, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "weave", 5631, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 5632 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "K", "smooth", 5632, 2)
    sandals(g)
    front, back = flaps(g, "skirt", 9, "D", "weave", 5633, hem="D1", top=11.2)
    front.vline(5, 1, 8, "D0"), front.vline(6, 1, 8, "D3")
    for name, x in (("right", -5.0), ("left", 4.0)):
        panel = g.piece(f"skirt_{name}", "TORSO", (0, 0, -2), (1, 9, 4), pivot=(x, 11.2, 0))
        strip_fabric(panel, "D", "weave", 5634, 2)
        fabric(panel.top, "D", "weave", 5634, 3), fabric(panel.bottom, "D", "weave", 5634, 1)
        panel.strip.hline(0, panel.strip.w - 1, 8, "D1")
