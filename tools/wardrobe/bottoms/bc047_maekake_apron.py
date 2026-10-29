"""Maekake Apron: the heavy indigo-style apron of the kitchen and the garden, tied over dark
trousers with a broad white band at the hem and a large white circle mark at the front, worn with
cloth shoes."""
from kit_household import cloth_shoes, trouser_legs, waist
from paint import fabric, solid

META = {"name": "Maekake Apron", "gender": "unisex",
        "description": "Heavy apron with a white hem band and circle mark over dark trousers, cloth shoes.",
        "tags": ["civilian", "work", "trousers"]}

RING = [(1, 0), (2, 0), (0, 1), (3, 1), (0, 2), (3, 2), (1, 3), (2, 3)]


def build(g):
    waist(g, "K", "twill", 37836)
    trouser_legs(g, "K", "twill", 37837, rows=(0, 9))
    cloth_shoes(g, "K", 1)
    apron = g.piece("apron", "TORSO", (-4.5, 0, 0), (9, 10, 1), pivot=(0, 9.4, -2.9), motion="flap_front")
    solid(apron, "D", "weave", 37839, 2)
    fabric(apron.front, "D", "weave", 37839, 2)
    apron.front.hline(0, 8, 0, "D3")
    apron.front.hline(0, 8, 8, "S3"), apron.front.hline(0, 8, 9, "D1")
    for x, y in RING:
        apron.front.set(3 + x, 2 + y, "S3")
    band = g.piece("waist_apron_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.2, 0), inflate=.2)
    solid(band, "D", "weave", 37840, 3, edge=False)
