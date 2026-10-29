"""Tracker Wraps: close trousers wound in cloth strips from the knee to the ankle so nothing snags
in the brush, a pouch on the right thigh and soft split-toe boots."""
from kit import footwear, legs, waistband
from kit_yamanaka import wrapped
from paint import solid

META = {"name": "Tracker Wraps", "gender": "unisex",
        "description": "Close trousers wrapped from knee to ankle, a thigh pouch, soft split-toe boots.",
        "tags": ["shinobi", "wrap"]}


def build(g):
    waistband(g, "D", "twill", 34520)
    for leg in legs(g, "D", "twill", 34521, rows=(0, 5), crease=False):
        wrapped(leg.strip, 0, 6, leg.strip.w - 1, 9, "S")
    footwear(g, "boot", top=10, role="K", base=2)
    for side in ("right", "left"):
        g.part(f"{side}_leg").front.vline(1 if side == "right" else 2, 10, 11, "K0")
    strap = g.piece("thigh_strap", "RIGHT_LEG", (-2.45, 1.4, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 34523, 2, edge=False)
    pouch = g.piece("thigh_pouch", "RIGHT_LEG", (0, 0, 0), (1, 3, 3), pivot=(-3.0, 1.0, -1.5))
    solid(pouch, "L", "leather", 34524, 2)
    pouch.right.hline(0, 2, 0, "L3")
