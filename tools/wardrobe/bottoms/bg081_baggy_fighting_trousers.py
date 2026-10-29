"""Baggy Fighting Trousers: wide, loose trousers that billow out over the thighs and shins, gathered
at the ankle with cloth wraps over straw sandals, a broad cloth sash knotted at the hip: room to
kick high and land soft."""
from kit import legs, waistband
from kit_rugged import baggy_legs, leg_wraps, straw_sandals
from paint import solid

META = {"name": "Baggy Fighting Trousers", "gender": "unisex",
        "description": "Wide billowing trousers gathered at the ankle with wraps, straw sandals, a knotted hip sash.",
        "tags": ["shinobi", "taijutsu"]}


def build(g):
    waistband(g, "P", "twill", 35310, 2)
    legs(g, "P", "twill", 35311, 2, rows=(0, 8), crease=False)
    baggy_legs(g, "baggy", "P", 35312, top=.4, length=9, flare=3)
    leg_wraps(g, 9, 10)
    straw_sandals(g)
    sash = g.piece("waist_sash", "TORSO", (-4.5, 9.3, -2.5), (9, 2, 5), inflate=.15)
    solid(sash, "A", "weave", 35314, 2, edge=False)
    for face in sash.sides:
        face.hline(0, face.w - 1, 0, "A3")
    end = g.piece("waist_sash_end", "TORSO", (-.5, 0, -.5), (2, 4, 1), pivot=(-3.4, 10.6, -2.9), rotation=(0, 0, 8),
                  motion="flap_front")
    solid(end, "A", "weave", 35315, 2)
