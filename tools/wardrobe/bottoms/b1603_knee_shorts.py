"""Knee Shorts: dusky shorts to the knee with turned-up cuffs, bandaged shins and sandals, a small
needle pouch on the right hip: for academy students and genin."""
from kit import pouch
from kit_shinobi import bandage, sandals
from paint import fabric, strip_fabric

META = {"name": "Knee Shorts", "gender": "unisex",
        "description": "Dusky knee shorts with turned cuffs, bandaged shins, a needle pouch on the hip, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 16876, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "twill", 16876, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 16877 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "twill", 16877, 2)
        leg.strip.hline(0, leg.strip.w - 1, 4, "D3"), leg.strip.hline(0, leg.strip.w - 1, 5, "D1")
        bandage(leg.strip, 0, 7, leg.strip.w - 1, 9)
    sandals(g)
    pouch(g, "waist_pouch", (-3.6, 10.0, -1.0), size=(2, 2, 2), role="L")
