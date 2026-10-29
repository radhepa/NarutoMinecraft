"""Courier Protector: the forehead protector as the messenger corps tie it, the band knotted with
long tails that stream out behind a runner."""
from kit_shinobi import forehead_protector
from paint import solid

META = {"name": "Courier Protector", "gender": "unisex",
        "description": "Forehead protector knotted with long streaming tails."}


def build(g):
    forehead_protector(g, "A", seed=34990)
    for i, (x, rz) in enumerate(((-.8, 20), (.8, -16))):
        tail = g.piece(f"long_tail_{i}", "HEAD", (-.5, 0, 0), (1, 9, 1), pivot=(x, -6.6, 5.0), rotation=(48, 0, rz),
                       motion="sway")
        solid(tail, "A", "weave", 34996 + i, 2)
        tail.back.set(0, 8, "A1")
