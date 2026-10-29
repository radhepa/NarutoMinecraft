"""Herb Shorts: dark knee shorts for working the gardens, a leather pouch strapped to the right
thigh with a sprig of leaves poking out, white wraps on the shins and sandals."""
from kit import belt, legs
from kit_shinobi import sandals, wraps
from kit_suzuran import herb_pouch
from paint import fabric, solid, strip_fabric

META = {"name": "Herb Shorts", "gender": "unisex",
        "description": "Dark knee shorts, a herb pouch strapped to the right thigh, white shin wraps, sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 24721, 3, 9, 11)
    fabric(body.bottom, "K", "twill", 24721, 2)
    for leg in legs(g, "K", "twill", 24722, 3, rows=(0, 4)):
        leg.strip.hline(0, leg.strip.w - 1, 4, "K1")
    wraps(g, 6, 9)
    belt(g, "waist_belt", y=9.0, role="L", height=1, buckle="M")
    strap = g.piece("thigh_strap", "RIGHT_LEG", (-2.45, 1.4, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", 24723, 2, edge=False)
    herb_pouch(g, "thigh_pouch", (-2.6, 1.0, -.2), bone="RIGHT_LEG", rotation=(0, 90, 0), size=(3, 3, 1))
    sandals(g)
