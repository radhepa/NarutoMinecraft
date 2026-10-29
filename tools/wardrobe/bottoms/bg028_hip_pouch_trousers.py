"""Hip-Pouch Trousers: field trousers with a belt carrying a pouch on each hip and one at the back,
bloused into shin wraps over open-toe sandals."""
from kit import belt
from kit_field import blouse, pocket, trousers
from kit_shinobi import sandals, wraps

META = {"name": "Hip-Pouch Trousers", "gender": "unisex",
        "description": "Bloused trousers with a belt of hip and back pouches, shin wraps and sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32540)
    wraps(g)
    sandals(g)
    blouse(g, "D", 32543)
    belt(g, "waist_belt", y=9.4, role="L", height=1, buckle="M", inflate=.12)
    for i, (x, z, ry) in enumerate(((-4.6, 0, 90), (4.6, 0, -90), (0, 2.6, 180))):
        pocket(g, f"waist_pouch_{i}", (x, 9.8, z), (4, 4, 2), "L", 32545 + i, rotation=(0, ry, 0), snap="M3", scale=.65)
