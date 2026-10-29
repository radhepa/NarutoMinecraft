"""Sensor Trousers: loose, soft trousers gathered into ties at the ankle, for sitting still for hours
and then moving at once, with plain open-toe sandals."""
from kit import leg_ring, legs, waistband
from kit_shinobi import sandals
from paint import k

META = {"name": "Sensor Trousers", "gender": "unisex",
        "description": "Loose soft trousers gathered into ankle ties, open-toe sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "weave", 34540)
    legs(g, "D", "weave", 34541, rows=(0, 9), crease=False)
    sandals(g)
    for ring in leg_ring(g, "ankle_gather", 7.6, "D", 2, size=(5, 2, 5), inflate=.12):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, k("D", 3))
            for x in range(0, face.w, 2):
                face.set(x, 1, k("D", 1))
    leg_ring(g, "ankle_tie", 9.4, "S", 3, size=(5, 1, 5), inflate=.05)
