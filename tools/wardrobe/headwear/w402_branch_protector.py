"""Branch Protector: the forehead protector worn the branch-house way, its plate tied over a white
under-wrap so no edge of the seal shows, with long cloth tails down the back."""
from kit_shinobi import forehead_protector
from paint import solid

META = {"name": "Branch Protector", "gender": "unisex",
        "description": "Forehead protector over a white under-wrap, long tails down the back."}


def build(g):
    under = g.piece("under_wrap", "HEAD", (-4, -8.3, -4), (8, 1, 8), inflate=.5)
    solid(under, "S", "weave", 4986, 3, edge=False)
    forehead_protector(g, "D", seed=4987)
    for i, (x, rz) in enumerate(((-.7, 8), (.7, -6))):
        tail = g.piece(f"long_tail_{i}", "HEAD", (-.5, 0, 0), (1, 7, 1), pivot=(x, -6.2, 5.0), rotation=(10, 0, rz),
                       motion="sway")
        solid(tail, "D", "weave", 4990 + i, 2)
