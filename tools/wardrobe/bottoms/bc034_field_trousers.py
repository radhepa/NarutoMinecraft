"""Field Trousers: the farmer's and the gardener's fitted cotton trousers, the shins bound in
buttoned cloth gaiters and the feet in straw waraji tied at the ankle."""
from kit_household import trouser_legs, waist, waraji
from paint import solid

META = {"name": "Field Trousers", "gender": "unisex",
        "description": "Fitted cotton trousers with buttoned cloth gaiters on the shins, straw waraji.",
        "tags": ["civilian", "work", "trousers"]}


def build(g):
    waist(g, "K", "twill", 37628, band="K3")
    trouser_legs(g, "K", "twill", 37629, rows=(0, 9))
    waraji(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        gaiter = g.piece(f"{side}_gaiter", bone, (-2.5, 5.4, -2.5), (5, 4, 5))
        solid(gaiter, "D", "weave", 37631 + (side == "left"), 2)
        for face in gaiter.sides:
            face.hline(0, face.w - 1, 0, "D3")
        outer = gaiter.right if side == "right" else gaiter.left
        outer.vline(2, 0, 3, "D1")
        for y in (1, 3):
            outer.set(2, y, "M3")
