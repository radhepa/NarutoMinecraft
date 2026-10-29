"""Field Trousers: straight dark trousers with patched knees in the clan colour, ankle wraps, a
leather belt with a kunai holster on the right thigh and dark sandals."""
from kit import belt
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Field Trousers", "gender": "unisex",
        "description": "Straight dark trousers, coloured knee patches, ankle wraps, holster, dark sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 1730, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 1730, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 1731 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "twill", 1731, 2)
        leg.front.rect(0, 4, 4, 2, "P2"), leg.front.hline(0, 3, 4, "P3")
        for x in range(leg.strip.w):
            leg.strip.set(x, 9, "S3" if x % 3 else "S2")
    sandals(g)
    belt(g, "waist_belt", y=9.2, role="L", height=1, buckle="M", inflate=.3)
    strap = g.piece("holster_strap", "RIGHT_LEG", (-2.45, 1.0, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 1733, 2)
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, .8, -1.0))
    solid(holster, "K", "leather", 1734, 3)
    holster.right.set(0, 0, "M3")
