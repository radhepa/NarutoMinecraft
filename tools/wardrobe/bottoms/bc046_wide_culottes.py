"""Wide Culottes: breezy wide-legged trousers cut to the mid-calf, so they swing like a skirt,
with a smocked waist and thong sandals."""
from kit_household import trouser_legs, waist, zori
from paint import solid

META = {"name": "Wide Culottes", "gender": "unisex",
        "description": "Wide-legged mid-calf culottes with a smocked waist, thong sandals.",
        "tags": ["civilian", "casual", "trousers"]}


def build(g):
    body = waist(g, "D", "plain", 37820)
    for x in range(0, body.strip.w, 2):
        body.strip.set(x, 9, "D1")
    trouser_legs(g, "D", "plain", 37821, rows=(0, 7), base=1)
    zori(g, sock="L3", strap="L1", sole="L2")
    for side, sign, bone in (("right", -1, "RIGHT_LEG"), ("left", 1, "LEFT_LEG")):
        leg = g.piece(f"{side}_wide", bone, (-2.5, 0, -2.6), (5, 8, 5), pivot=(0, .3, 0), rotation=(0, 0, -6 * sign),
                      inflate=.14, motion="none")
        solid(leg, "D", "plain", 37823 + (sign > 0), 2)
        for face in leg.sides:
            face.vline(1, 2, 6, "D1"), face.vline(3, 3, 6, "D1")
            face.hline(0, face.w - 1, 7, "D1")
        leg.bottom.fill("D0")
