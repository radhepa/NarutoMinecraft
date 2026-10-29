"""Shin Guard Shorts: sturdy shorts with tall hardened-leather shin guards and knee caps strapped on
over bare legs, open sandals: the kit of a kicker who trains against trees."""
from kit import legs, leg_ring, waistband
from kit_rugged import shin_guard
from kit_shinobi import sandals
from paint import solid

META = {"name": "Shin Guard Shorts", "gender": "unisex",
        "description": "Sturdy shorts, tall leather shin guards with knee caps strapped over bare legs, sandals.",
        "tags": ["shinobi", "genin", "taijutsu"]}


def build(g):
    waistband(g, "K", "twill", 35420, 3)
    legs(g, "K", "twill", 35421, 3, rows=(0, 3), crease=False)
    for ring in leg_ring(g, "hem", 2.4, "K", 3, (5, 2, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 1, "K2")
    shin_guard(g, "shin_guard", "L", 35422, top=5.4, length=5, strap="K1", knee=True)
    sandals(g)
    belt = g.piece("waist_belt", "TORSO", (-4.6, 9.4, -2.6), (9, 1, 5), inflate=.1)
    solid(belt, "A", "weave", 35425, 2, edge=False)
