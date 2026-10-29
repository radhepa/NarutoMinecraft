"""Paddy Trousers: old trousers rolled high above the knee for planting out the rice, the bare
shins and feet splashed with paddy mud, straw sandals tied on."""
from kit_kurama import splatter
from kit_market import rolled_cuffs, straw_sandals
from paint import fabric, strip_fabric

META = {"name": "Paddy Trousers", "gender": "unisex",
        "description": "Trousers rolled above the knee, mud-splashed bare shins, straw sandals.",
        "tags": ["civilian", "trousers", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 36860, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 36860, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 36861 + (side == "left"), 2, 0, 2)
        fabric(leg.top, "D", "twill", 36861, 2)
        splatter(leg.strip, 36863 + (side == "left"), keys=("L1", "L2", "L0"), density=.18, rows=range(5, 10))
        leg.strip.hline(0, leg.strip.w - 1, 9, "L1")
    rolled_cuffs(g, "cuff", 2.4, "D", 36865)
    straw_sandals(g)
