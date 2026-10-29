"""Pleated Skirt: a box-pleated cotton skirt to mid-calf from the newer shops in town, with white
socks and straw zori."""
from kit import flaps, side_panels
from kit_market import straw_sandals
from paint import fabric, k, strip_fabric

META = {"name": "Pleated Skirt", "gender": "unisex",
        "description": "Box-pleated cotton skirt to mid-calf, white socks and straw zori.",
        "tags": ["civilian", "skirt", "casual"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 36830, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, k("D", 3))
    fabric(body.bottom, "D", "weave", 36830, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "S", "plain", 36831, 3, 7, 9)
    for face in flaps(g, "skirt", 8, "D", "weave", 36832, width=9, hem=k("D", 1), top=11.2):
        for x in range(1, 9, 2):
            face.vline(x, 1, 7, k("D", 1))
    side_panels(g, "skirt_side", 8, "D", "weave", hem=k("D", 1), top=11.2)
    straw_sandals(g)
