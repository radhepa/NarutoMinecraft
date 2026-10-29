"""Crag Swept: hair swept straight back from the brow and cut to break into stony points over the
nape, like a ridge of crags."""
from anime import back_fan, ring_shell
from paint import scalp

META = {"name": "Crag Swept", "gender": "unisex",
        "description": "Hair swept straight back from the brow, breaking into stony points over the nape."}


def build(g):
    scalp(g, 23241, side_rows=5, back_rows=8, sideburn=2)
    hat = ring_shell(g, 23242, side_rows=4, back_rows=7, ring_row=1)
    for x in (1, 4, 6):
        hat.top.vline(x, 0, 7, "H1")
    back_fan(g, "crag", [(-3.0, ((2, 3), (1, 2)), 18, 34), (-1.2, ((3, 4), (2, 2), (1, 1)), 6, 30),
                         (1.2, ((3, 4), (2, 2), (1, 1)), -6, 30), (3.0, ((2, 3), (1, 2)), -18, 34)], seed=23245)
