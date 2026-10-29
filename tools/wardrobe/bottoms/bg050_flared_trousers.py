"""Flared Trousers: loose trousers that widen toward the ankle and are gathered there by cloth
bands, a wide sash with a knot at the back, open-toe sandals."""
from kit import leg_ring, legs, waistband
from kit_kunoichi import obi
from kit_shinobi import sandals

META = {"name": "Flared Trousers", "gender": "unisex",
        "description": "Loose trousers widening to gathered ankle bands, a wide back-knotted sash, sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "P", "weave", 33580)
    legs(g, "P", "weave", 33581, rows=(0, 9), crease=False)
    sandals(g)
    for side in ("right", "left"):
        pants = g.part(f"{side}_pants")
        for face in pants.sides:
            for y in range(4, 9):
                face.set(1, y, "P1")
            face.hline(0, face.w - 1, 8, "P2")
    for ring in leg_ring(g, "ankle_band", 8.4, "S", 3, (5, 1, 5), "weave"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "S2")
    obi(g, "waist_sash", y=9.0, role="S", height=2, knot="back", seed=33584)
