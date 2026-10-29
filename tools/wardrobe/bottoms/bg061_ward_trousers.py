"""Ward Trousers: the medical corps' straight trousers, pressed and plain, with split-toe socks and
straw sandals for the hospital's wooden floors."""
from kit import legs, waistband
from kit_hyuga import tabi
from paint import solid

META = {"name": "Ward Trousers", "gender": "unisex",
        "description": "Straight pressed trousers, split-toe socks and straw sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 34400)
    legs(g, "D", "twill", 34401, rows=(0, 8))
    tabi(g, "S", "K1", "D2")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        cuff = g.piece(f"{side}_cuff", bone, (-2.5, 8.0, -2.5), (5, 1, 5))
        solid(cuff, "D", "twill", 34403, 2, edge=False)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 0, "D1")
