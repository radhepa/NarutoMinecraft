"""Porter's Shorts: short close cotton shorts for hauling loads up the hill roads, the shins
wrapped in indigo gaiters tied at the knee, straw sandals bound at the ankle."""
from kit_market import kyahan, straw_sandals
from paint import fabric, k, strip_fabric

META = {"name": "Porter's Shorts", "gender": "unisex",
        "description": "Short close cotton shorts, indigo gaiters tied at the knee, bound straw sandals.",
        "tags": ["civilian", "shorts", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 36680, 2, 9, 11)
    fabric(body.bottom, "S", "weave", 36680, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "S", "weave", 36681 + (side == "left"), 2, 0, 2)
        fabric(leg.top, "S", "weave", 36681, 2)
        leg.strip.hline(0, leg.strip.w - 1, 2, k("S", 1))
    kyahan(g, "D", rows=(4, 9), seed=36683, tie="S3")
    straw_sandals(g)
