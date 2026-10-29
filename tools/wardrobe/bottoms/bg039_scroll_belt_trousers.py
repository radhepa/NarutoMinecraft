"""Scroll-Belt Trousers: field trousers under a broad belt carrying a sealing scroll across the back and a
shuriken pouch on the right hip, bloused into shin wraps over open-toe sandals."""
from kit import belt
from kit_field import blouse, pocket, trousers
from kit_shinobi import sandals, wraps
from paint import k, solid

META = {"name": "Scroll-Belt Trousers", "gender": "unisex",
        "description": "Bloused trousers, a broad belt with a back scroll and a hip shuriken pouch, shin wraps.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32760)
    wraps(g)
    sandals(g)
    blouse(g, "D", 32763)
    belt(g, "waist_belt", y=9.2, role="L", height=2, buckle="M", inflate=.14)
    scroll = g.piece("waist_scroll", "TORSO", (-5, -1, -1), (10, 2, 2), pivot=(0, 9.6, 3.2))
    solid(scroll, "S", "plain", 32765, 3, edge=False)
    for face in scroll.sides:
        face.vline(0, 0, 1, k("A", 2)), face.vline(face.w - 1, 0, 1, k("A", 2))
    scroll.right.fill("A1"), scroll.left.fill("A1")
    pocket(g, "waist_shuriken_pouch", (-4.7, 9.6, 0), (3, 3, 2), "K", 32766, rotation=(0, 90, 0), snap="M3", scale=.8)
