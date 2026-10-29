"""Drawstring Trousers: loose ankle-length trousers gathered at the cuffs with drawstrings, a long
sash wound round the hips with one tail hanging to the knee, bare feet in open sandals."""
from kit import legs, leg_ring, waistband
from kit_rugged import baggy_legs
from kit_shinobi import sandals
from paint import solid

META = {"name": "Drawstring Trousers", "gender": "unisex",
        "description": "Loose ankle trousers gathered with drawstring cuffs, a long hip sash with a knee-length tail.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "S", "weave", 35460, 2)
    legs(g, "S", "weave", 35461, 2, rows=(0, 9), crease=False)
    baggy_legs(g, "loose", "S", 35462, top=.6, length=8, flare=1.5, width=5, texture="weave")
    for ring in leg_ring(g, "cuff", 8.8, "S", 1, (5, 1, 5), "weave"):
        for face in ring.sides:
            face.set(face.w // 2, 0, "K2")
    sandals(g)
    sash = g.piece("waist_sash", "TORSO", (-4.5, 9.0, -2.5), (9, 2, 5), inflate=.18)
    solid(sash, "A", "weave", 35464, 2, edge=False)
    for face in sash.sides:
        face.hline(0, face.w - 1, 0, "A3")
    tail = g.piece("waist_sash_tail", "TORSO", (-1, 0, 0), (2, 8, 1), pivot=(3.9, 10.4, -1.0), rotation=(0, 90, 6),
                   motion="flap_front")
    solid(tail, "A", "weave", 35465, 2)
    tail.front.hline(0, 1, 7, "A0"), tail.back.hline(0, 1, 7, "A0")
