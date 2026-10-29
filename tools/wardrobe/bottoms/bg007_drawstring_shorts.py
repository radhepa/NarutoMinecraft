"""Drawstring Shorts: short running shorts cut above the knee with notched side vents and a white
drawstring, a kunai holster over a thigh wrap and open-toe sandals."""
from kit_academy import holster, leg_cloth, waist
from kit_shinobi import sandals
from paint import k

META = {"name": "Drawstring Shorts", "gender": "unisex",
        "description": "Above-knee running shorts with side vents and a drawstring, thigh holster and sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = waist(g, "P", "plain", 31490)
    body.front.set(3, 10, "S3"), body.front.set(4, 10, "S3"), body.front.set(3, 11, "S3")
    for side, leg in zip(("right", "left"), leg_cloth(g, "P", "plain", 31491, (0, 3))):
        leg.strip.hline(0, leg.strip.w - 1, 3, "S3")
        outer = leg.right if side == "right" else leg.left
        outer.set(1, 3, None), outer.set(2, 3, None), outer.set(1, 2, k("P", 1)), outer.set(2, 2, k("P", 1))
    sandals(g)
    holster(g, 31493, y=4.0)
