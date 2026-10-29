"""Momohiki Gaiters: close-fitting indigo momohiki work trousers, cream kyahan gaiters tied over the
shins and dark split-toe jika-tabi hooked up the ankle."""
from kit import waistband
from kit_kinoshita import kyahan, tabi
from paint import fabric, strip_fabric

META = {"name": "Momohiki Gaiters", "gender": "unisex",
        "description": "Snug indigo work trousers, cream gaiters over the shins and dark split-toe tabi.",
        "tags": ["shinobi", "kinoshita"]}


def build(g):
    waistband(g, "D", "twill", 22621)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 22622 + (side == "left"), 2, 0, 8)
        fabric(leg.top, "D", "twill", 22622, 2)
        leg.front.vline(1 if side == "right" else 2, 0, 4, "D1")
    kyahan(g, top=4, bottom=8)
    tabi(g, top=9)
