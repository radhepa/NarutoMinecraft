"""Akimichi Protector: the forehead protector on a band in the outfit's main color, its knot left with
long trailing tails that stream down the back like Choji's."""
from kit_shinobi import forehead_protector
from paint import solid

META = {"name": "Akimichi Protector", "gender": "unisex",
        "description": "Forehead protector on a band in the outfit's color, long tails streaming down the back."}


def build(g):
    forehead_protector(g, "P", seed=6980)
    for i, (x, rz) in enumerate(((-1.0, 18), (1.0, -14))):
        tail = g.piece(f"long_tail_{i}", "HEAD", (-.5, 0, 0), (1, 9, 1), pivot=(x, -6.6, 4.8), rotation=(14, 0, rz),
                       motion="sway")
        solid(tail, "P", "weave", 6989 + i, 2)
        tail.back.set(0, 8, "P1")
