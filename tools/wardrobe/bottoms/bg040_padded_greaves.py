"""Padded Greaves: field trousers with quilted greaves laced round the shins from knee to ankle, a
thigh holster on the left and open-toe sandals: the front-line jonin's legs."""
from kit import leg_ring
from kit_field import holster, trousers
from kit_shinobi import sandals
from paint import k

META = {"name": "Padded Greaves", "gender": "unisex",
        "description": "Trousers with quilted greaves laced from knee to ankle, a left thigh holster and sandals.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32780, length=5)
    sandals(g)
    for ring in leg_ring(g, "greave", 4.6, "P", 2, (5, 5, 5), "quilt", inflate=.05):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, k("P", 3)), face.hline(0, face.w - 1, 4, k("P", 1))
        ring.back.vline(2, 1, 3, k("L", 2))
    holster(g, "left", 32784)
