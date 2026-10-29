"""Patched Monpe: an old pair of field monpe gone soft with wear, darned at both knees with squares
of other cloth, gathered at the ankle over split-toe jika-tabi."""
from kit_market import gathered_ankles, jika_tabi, patch
from paint import fabric, strip_fabric

META = {"name": "Patched Monpe", "gender": "unisex",
        "description": "Worn field monpe darned at the knees, gathered at the ankle over jika-tabi.",
        "tags": ["civilian", "trousers", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "L", "weave", 36695, 2, 9, 11)
    fabric(body.bottom, "L", "weave", 36695, 1)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "L", "weave", 36696 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "L", "weave", 36696, 2)
        strip_fabric(pants, "L", "weave", 36698 + (side == "left"), 2, 0, 6)
        if side == "right":
            patch(pants.front, 0, 3, 3, 2, "D", 2, stitch="S3")
        else:
            patch(pants.front, 1, 2, 3, 3, "S", 1, stitch="L1")
    gathered_ankles(g, "ankle", "L", 36700, y=7.0)
    jika_tabi(g, "K", top=8, seed=36702)
