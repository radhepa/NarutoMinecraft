"""Drop-Holster Trousers: field trousers bloused into shin wraps, a long holster riding low on the right
thigh on two straps and hung from the belt by a leather drop strap."""
from kit_field import blouse, holster, trousers
from kit_shinobi import sandals, wraps
from paint import solid

META = {"name": "Drop-Holster Trousers", "gender": "unisex",
        "description": "Bloused trousers, shin wraps and a low drop-leg holster hung from the belt, sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32420)
    wraps(g)
    sandals(g)
    blouse(g, "D", 32423)
    holster(g, "right", 32425, y=2.2, tied=True)
    drop = g.piece("waist_drop_strap", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(-3.9, 10.2, -1.0))
    solid(drop, "L", "leather", 32429, 2, edge=False)
