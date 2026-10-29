"""Bandaged Shorts: dark training shorts to mid-thigh, bandages bound over both knees, a thigh
holster on the right leg and navy open-toe sandals."""
from kit_shinobi import sandals
from kit_yuhi import bandage_turns
from paint import fabric, solid, strip_fabric

META = {"name": "Bandaged Shorts", "gender": "unisex",
        "description": "Dark mid-thigh shorts, bandaged knees, a right thigh holster, navy sandals.",
        "tags": ["shinobi", "wrap"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 14940, 2, 9, 11)
    fabric(body.bottom, "K", "twill", 14940, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 14941 + (side == "left"), 2, 0, 3)
        fabric(leg.top, "K", "twill", 14941, 2)
        leg.strip.hline(0, leg.strip.w - 1, 3, "K3")
        bandage_turns(leg.strip, 0, 5, leg.strip.w - 1, 7, "S", 3)
    sandals(g)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.1, 1.0, -1.0))
    solid(holster, "K", "leather", 14943, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
