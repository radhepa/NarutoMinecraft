"""Field Shorts: khaki knee shorts with deep side pockets, pale wraps from the knee to the ankle and
open-toe sandals: the clan's lighter summer kit."""
from kit import legs, waistband
from kit_shinobi import sandals, wraps
from paint import solid

META = {"name": "Field Shorts", "gender": "unisex",
        "description": "Khaki knee shorts with side pockets, pale shin wraps, open-toe sandals.", "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 10811)
    legs(g, "D", "twill", 10812, rows=(0, 4))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        leg.strip.hline(0, leg.strip.w - 1, 4, "D1")
        outer = leg.right if side == "right" else leg.left
        outer.hline(0, 3, 1, "D3"), outer.vline(0, 1, 3, "D1")
    wraps(g, 5, 9)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        hem = g.piece(f"{side}_hem", bone, (-2.3, 3.6, -2.3), (4, 1, 4), inflate=.2)
        solid(hem, "D", "twill", 10815, 2)
