"""Florist Trousers: easy dark trousers for the shop floor, rolled to a cuff above the ankle in
cream, a tie belt and navy open-toe sandals."""
from kit import belt, leg_ring, legs
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Florist Trousers", "gender": "unisex",
        "description": "Easy dark trousers rolled to a cream cuff above the ankle, tie belt, navy sandals.",
        "tags": ["florist"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 7470, 2, 9, 11)
    fabric(body.bottom, "D", "weave", 7470, 1)
    legs(g, "D", "weave", 7471, 2, rows=(0, 8))
    for ring in leg_ring(g, "cuff", 8.0, "S", 3, (4, 2, 4), "weave", inflate=.25):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "S4"), face.hline(0, face.w - 1, 1, "S2")
    belt(g, "waist_tie", y=9.0, role="S", height=1, buckle=None, inflate=.15)
    sandals(g)
