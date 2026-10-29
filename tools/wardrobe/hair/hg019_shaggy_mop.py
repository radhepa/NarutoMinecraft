"""Shaggy Mop: layered hair grown out and left uneven, choppy ends over the ears and down the nape,
a parted fringe that falls to the brow at the sides and stays short over the eyes."""
from anime import back_fan, bangs, ring_shell, sidelocks
from paint import scalp

META = {"name": "Shaggy Mop", "gender": "unisex",
        "description": "Layered uneven hair, choppy ends over the ears and nape, a parted fringe to the brow."}


def build(g):
    scalp(g, 32950, side_rows=7, back_rows=8, sideburn=3)
    ring_shell(g, 32951, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 14), (-1.3, ((2, 2), (1, 1)), 24), (1.3, ((2, 2), (1, 1)), -24),
                        (2.9, ((2, 2), (1, 1)), -14)], seed=32952)
    sidelocks(g, "ear", 5, seed=32957, x=4.45, z=-1.0, flare=10, width=2)
    back_fan(g, "nape", [(-2.8, ((3, 2), (2, 2), (1, 1)), 18, 14), (0, ((3, 3), (2, 2), (1, 1)), 0, 10),
                         (2.8, ((3, 2), (2, 2), (1, 1)), -18, 14)], seed=32959, z=4.4)
