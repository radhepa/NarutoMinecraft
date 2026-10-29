"""Veiled Bob: a sleek chin-length bob, its long side-swept fringe drawn across the brow and down past
the outer corner of one eye like a fold of curtain, the hem cut straight and turned under."""
from anime import back_fan, bangs, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Veiled Bob", "gender": "unisex",
        "description": "Sleek chin-length bob, long side-swept fringe falling past one eye's outer corner."}


def build(g):
    scalp(g, 25060, side_rows=7, back_rows=8, sideburn=4, part=2)
    ring_shell(g, 25061, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((3, 2), (3, 1)), 30), (-1.0, ((3, 1), (2, 1)), 46), (1.0, ((3, 1), (2, 1)), 52)],
          seed=25062)
    lock(g, "sweep", (4.1, -7.9, -4.35), (-6, 0, 0), ((2, 4), (2, 2), (1, 1)), 1, 25065, ring=1)
    sidelocks(g, "side", 9, seed=25068, x=4.45, z=-1.4, flare=2, width=3, taper=False)
    sidelocks(g, "frame", 8, seed=25070, x=4.3, z=-3.4, flare=2, width=2, taper=False)
    back_fan(g, "nape", [(-3.0, ((3, 8),), 3, 3), (0, ((3, 8),), 0, 3), (3.0, ((3, 8),), -3, 3)], seed=25072)
