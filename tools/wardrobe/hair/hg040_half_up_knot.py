"""Half-Up Knot: hair to the shoulders, the top half drawn back from the face into a small knot at
the back of the crown and the rest left falling to the collar, face-framing locks at the temples:
the Academy instructor's favourite."""
from anime import curtain, ring_shell, sidelocks
from kit_kurama import bun
from paint import scalp

META = {"name": "Half-Up Knot", "gender": "unisex",
        "description": "Shoulder-length hair, the top half drawn into a small knot at the back of the crown."}


def build(g):
    scalp(g, 34930, side_rows=7, back_rows=8, sideburn=4)
    ring_shell(g, 34931, side_rows=7, back_rows=8, ring_row=1)
    bun(g, "half_knot", (0, -8.2, 4.6), size=3, seed=34932, rotation=(30, 0, 0))
    curtain(g, "fall", (0, -4.4, 4.6), (-4, 0, 0), 8, 6, [(0, 3, 2), (3, 2, 2), (5, 3, 2)], seed=34935)
    sidelocks(g, "frame", 8, seed=34940, x=4.3, z=-3.4, flare=3, width=2)
