"""Hanzubon: knee-length cotton shorts with a drawstring, what the errand children and the young
runners wear all summer, with simple straw zori."""
from kit_market import straw_sandals
from paint import fabric, k, solid, strip_fabric

META = {"name": "Hanzubon", "gender": "unisex",
        "description": "Knee-length drawstring cotton shorts with straw zori.",
        "tags": ["civilian", "shorts", "casual"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "L", "twill", 36650, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, k("L", 3))
    fabric(body.bottom, "L", "twill", 36650, 1)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "L", "twill", 36651 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "L", "twill", 36651, 2)
        strip_fabric(pants, "L", "twill", 36653 + (side == "left"), 2, 0, 4)
        pants.strip.hline(0, pants.strip.w - 1, 4, k("L", 1))
    knot = g.piece("waist_string", "TORSO", (-.5, 0, -.5), (1, 2, 1), pivot=(0, 9.4, -2.5), scale=(.6, 1, .6), motion="sway")
    solid(knot, "S", "weave", 36655, 3)
    straw_sandals(g)
