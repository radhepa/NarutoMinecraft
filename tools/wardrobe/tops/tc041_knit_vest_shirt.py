"""Knit Vest and Shirt: the archive clerk's and the older schoolboy's look, a long-sleeved white
shirt with pointed collar tips under a V-necked knit vest with ribbed edges."""
from kit_household import arm_cloth
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Knit Vest and Shirt",
    "gender": "unisex",
    "description": "White long-sleeved shirt with pointed collar tips under a ribbed V-neck knit vest.",
    "tags": ["civilian", "casual"],
}

V = [(2, 0), (3, 0), (4, 0), (5, 0), (3, 1), (4, 1), (3, 2), (4, 2), (4, 3)]


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "plain", 37300, 3)
    cap(body, "S", seed=37300, base=3)
    body.front.vline(3, 0, 11, "S2")
    strip_fabric(jacket, "P", "knit", 37301, 2, 0, 11)
    fabric(jacket.top, "P", "knit", 37301, 3)
    for x, y in V:
        jacket.front.set(x, y, None)
    for x, y in ((1, 0), (2, 1), (2, 2), (3, 3), (6, 0), (5, 1), (5, 2), (4, 4)):
        jacket.front.set(x, y, "P1")
    strip_fabric(jacket, "P", "rib", 37302, 1, 10, 11)
    for arm in arm_cloth(g, "S", "plain", 37303, rows=(0, 9), base=3, overlay=False):
        arm.strip.hline(0, arm.strip.w - 1, 9, "S2")
    for side, x, rz in (("right", -1.4, 24), ("left", 1.4, -24)):
        tip = g.piece(f"collar_{side}", "TORSO", (-1, 0, 0), (2, 2, 1), pivot=(x, -.2, -2.7), rotation=(0, 0, rz))
        solid(tip, "S", "plain", 37306 + (side == "left"), 4, edge=False)
