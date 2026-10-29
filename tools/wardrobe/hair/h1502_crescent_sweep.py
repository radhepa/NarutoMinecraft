"""Crescent Sweep: short hair with the whole fringe combed one way in a curving arc across the brow,
like a new moon lying on its side; close sides and a tapered nape."""
from anime import bangs, lock, ring_shell
from paint import scalp

META = {"name": "Crescent Sweep", "gender": "unisex",
        "description": "Short hair, the fringe swept one way in a curved arc across the brow, tapered nape."}


def build(g):
    scalp(g, 15050, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 15051, side_rows=4, back_rows=6, ring_row=1)
    # Every fringe lock leans to the wearer's left, the outer ones longest, so the edge curves.
    bangs(g, "sweep", [(-3.2, ((3, 2), (2, 1), (1, 1)), -38), (-1.4, ((3, 2), (2, 1)), -52),
                       (0.6, ((3, 1), (2, 1)), -62), (2.6, ((2, 2), (1, 2)), -30)], seed=15060)
    lock(g, "swept_side", (4.3, -7.4, -2.6), (0, 0, -10), ((2, 4), (1, 2)), 1, 15070)
    for i, (x, rz) in enumerate(((-2.4, 14), (0, 0), (2.4, -14))):
        lock(g, f"nape_{i}", (x, -6.8, 4.3), (8, 0, rz), ((3, 4), (2, 1), (1, 1)), 1, 15075 + i)
