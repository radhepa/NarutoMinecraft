"""Wrapped Shorts: loose knee-length shorts with a frayed hem, the calves wound in bandage from knee
to ankle and plain open sandals: the lightest kit for running the forest roads."""
from kit import legs, leg_ring, waistband
from kit_rugged import leg_wraps
from kit_shinobi import sandals
from paint import solid

META = {"name": "Wrapped Shorts", "gender": "unisex",
        "description": "Loose knee shorts with a frayed hem, calves wound in bandage, open sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waistband(g, "P", "weave", 35360, 2)
    legs(g, "P", "weave", 35361, 2, rows=(0, 4), crease=False)
    for ring in leg_ring(g, "hem", 3.4, "P", 2, (5, 2, 5), "weave"):
        for face in ring.sides:
            for x in range(face.w):
                face.set(x, 1, "P1" if x % 2 else "P0")
    leg_wraps(g, 5, 10)
    sandals(g)
    tie = g.piece("waist_tie", "TORSO", (-4.5, 9.4, -2.5), (9, 1, 5), inflate=.12)
    solid(tie, "L", "weave", 35363, 2, edge=False)
