"""Shinobi Bike Shorts: Sakura's dark green fitted shorts to above the knee, a kunai holster strapped
round the right thigh, a hip pouch at the back and navy open-toe sandals."""
from kit import pouch
from kit_shinobi import sandals
from paint import fabric, k, solid, strip_fabric

META = {"name": "Shinobi Bike Shorts", "gender": "unisex",
        "description": "Fitted dark green shorts above the knee, kunai holster on the right thigh, back pouch, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "smooth", 19710, 2, 9, 11)
    fabric(body.bottom, "D", "smooth", 19710, 1)
    body.strip.hline(0, body.strip.w - 1, 9, k("D", 3))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "smooth", 19711 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "smooth", 19711, 2)
        leg.strip.hline(0, leg.strip.w - 1, 4, k("D", 1))
    sandals(g)
    holster = g.piece("holster", "RIGHT_LEG", (-2.3, 1.6, -2.3), (5, 2, 5), inflate=.05)
    solid(holster, "K", "leather", 19713, 2, edge=False)
    case = g.piece("holster_case", "RIGHT_LEG", (-1, 0, -1), (2, 3, 2), pivot=(-2.4, 1.4, 0))
    solid(case, "K", "leather", 19714, 2)
    case.right.set(0, 0, k("M", 3))
    pouch(g, "waist_pouch", (0, 9.6, 2.4), size=(3, 2, 1), role="L", flap=k("M", 3))
