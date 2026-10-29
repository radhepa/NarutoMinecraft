"""Rolled-Cuff Trousers: loose trousers rolled up to mid-calf, bare ankles over open-toe sandals and a
small kunai holster on the left thigh: the off-duty chunin in summer."""
from kit import leg_ring
from kit_field import holster, trousers
from kit_shinobi import sandals
from paint import k

META = {"name": "Rolled-Cuff Trousers", "gender": "unisex",
        "description": "Loose trousers rolled to mid-calf, bare ankles, a left thigh holster and sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32660, length=7, texture="weave")
    for ring in leg_ring(g, "roll", 6.6, "D", 3, (5, 2, 5), "weave"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, k("D", 4)), face.hline(0, face.w - 1, 1, k("D", 2))
    holster(g, "left", 32663)
    sandals(g)
