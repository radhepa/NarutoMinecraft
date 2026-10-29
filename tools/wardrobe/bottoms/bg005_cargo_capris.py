"""Cargo Capris: twill capris cut off below the knee, a big flapped pocket on each thigh and a strap
cinching each cuff, with shin wraps and open-toe sandals."""
from kit_academy import leg_cloth, shin_wraps, waist
from kit_shinobi import sandals
from paint import solid

META = {"name": "Cargo Capris", "gender": "unisex",
        "description": "Below-knee twill capris, flapped thigh pockets, strapped cuffs, shin wraps and sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = waist(g, "L", "twill", 31460, band="L1")
    body.front.set(3, 9, "M3"), body.front.set(4, 9, "M3")
    leg_cloth(g, "L", "twill", 31461, (0, 7))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        leg.strip.hline(0, leg.strip.w - 1, 7, "L1"), leg.strip.hline(0, leg.strip.w - 1, 6, "K2")
    shin_wraps(g, 8, 9)
    sandals(g)
    for side, bone, x in (("right", "RIGHT_LEG", -3.0), ("left", "LEFT_LEG", 2.0)):
        pocket = g.piece(f"{side}_cargo", bone, (0, 0, 0), (1, 3, 3), pivot=(x, 1.6, -1.5))
        solid(pocket, "L", "twill", 31463, 3)
        outer = pocket.right if side == "right" else pocket.left
        outer.hline(0, 2, 0, "L1"), outer.set(1, 1, "M3")
