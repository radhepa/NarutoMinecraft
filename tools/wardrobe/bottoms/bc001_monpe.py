"""Monpe: the loose kasuri work trousers of the fields and the market, roomy through the thigh and
gathered tight at the ankle, tied at the waist, over straw sandals."""
from kit_market import gathered_ankles, kasuri, straw_sandals
from paint import fabric, k, solid, strip_fabric

META = {"name": "Monpe", "gender": "unisex",
        "description": "Loose kasuri work trousers gathered at the ankle, tied at the waist, straw sandals.",
        "tags": ["civilian", "trousers", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 36515, 2, 9, 11)
    fabric(body.bottom, "D", "weave", 36515, 1)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "D", "weave", 36516 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "weave", 36516, 2)
        strip_fabric(pants, "D", "weave", 36518 + (side == "left"), 2, 0, 7)
        kasuri(pants.strip, k("S", 1), 36520 + (side == "left"), rows=range(0, 8))
    gathered_ankles(g, "ankle", "D", 36522, y=8.0)
    tie = g.piece("waist_tie", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(-2.2, 9.6, -2.6), rotation=(0, 0, 8), motion="sway")
    solid(tie, "D", "weave", 36524, 3)
    straw_sandals(g)
