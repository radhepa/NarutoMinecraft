"""Shorts Over Leggings: cut-off shorts layered over full-length dark leggings, a kunai holster on the
thigh and open-toe sandals: the genin who wants pockets and freedom both."""
from kit_academy import holster, leg_cloth, turned_hem, waist
from kit_shinobi import sandals
from paint import strip_fabric

META = {"name": "Shorts Over Leggings", "gender": "unisex",
        "description": "Cut-off shorts over full-length dark leggings, a thigh holster and open-toe sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "D", "twill", 31565)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "rib", 31566, 1, 0, 9)
        leg.strip.hline(0, leg.strip.w - 1, 9, "K0")
    for side in ("right", "left"):
        pants = g.part(f"{side}_pants")
        strip_fabric(pants, "D", "twill", 31567 + (side == "left"), 2, 0, 3)
        pants.strip.hline(0, pants.strip.w - 1, 3, "D1")
    leg_cloth(g, "D", "twill", 31569, (0, 0))
    turned_hem(g, "hem", 3.6, "D", 31570, height=1, base=3)
    sandals(g)
    holster(g, 31572, y=4.4, strap=None)
