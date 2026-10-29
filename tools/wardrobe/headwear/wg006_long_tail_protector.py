"""Long-Tail Protector: the forehead protector on a long dark band, the knot tied high at the back and
its two ends trailing down past the shoulders, lifting with every step."""
from kit_shinobi import forehead_protector
from paint import k, solid

META = {"name": "Long-Tail Protector", "gender": "unisex",
        "description": "Forehead protector on a long band, knotted high with two ends trailing past the shoulders."}


def build(g):
    forehead_protector(g, "K", seed=32975)
    for i, (x, rz) in enumerate(((-.7, 12), (.7, -8))):
        tail = g.piece(f"long_tail_{i}", "HEAD", (-.5, 0, 0), (1, 9, 1), pivot=(x, -6.4, 5.0), rotation=(26, 0, rz),
                       motion="sway")
        solid(tail, "K", "weave", 32981 + i, 2)
        tail.back.set(0, 8, k("K", 1))
