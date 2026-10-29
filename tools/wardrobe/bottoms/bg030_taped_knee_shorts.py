"""Taped Knee Shorts: knee-length field shorts with a hemmed cuff, the knees taped below it, bare shins
and open-toe sandals, a holster on the right thigh: the genin's summer kit."""
from kit import leg_ring
from kit_field import holster, tape, trousers
from kit_shinobi import sandals
from paint import k

META = {"name": "Taped Knee Shorts", "gender": "unisex",
        "description": "Knee-length shorts with a cuffed hem, taped knees, bare shins, a thigh holster and sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    trousers(g, "D", 32580, length=4)
    for ring in leg_ring(g, "hem", 4.0, "D", 2, (5, 1, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, k("D", 3))
    for side in ("right", "left"):
        tape(g.part(f"{side}_leg"), (5, 6))
    holster(g, "right", 32584)
    sandals(g)
