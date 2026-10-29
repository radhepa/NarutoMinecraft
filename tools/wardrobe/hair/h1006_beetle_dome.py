"""Beetle Dome: a smooth, glossy cap of hair cut round like a beetle's shell, the hem level with
the ears and split into short points at the nape, the fringe stopping at the brows."""
from anime import bangs, cel_box, ring_shell
from paint import scalp

META = {"name": "Beetle Dome", "gender": "unisex",
        "description": "A smooth round cap of hair to the ears, pointed at the nape, brow-length fringe."}


def build(g):
    scalp(g, 10161, side_rows=6, back_rows=8, sideburn=1)
    ring_shell(g, 10162, side_rows=6, back_rows=8, ring_row=1)
    # The shell: a raised dome over the crown and a seam down the middle like wing cases.
    dome = g.piece("dome", "HEAD", (-4, -9, -4), (8, 1, 8), inflate=.55)
    cel_box(dome, 10170, ring=None, top_delta=2)
    dome.top.vline(3, 1, 7, "H1"), dome.top.vline(4, 1, 7, "H1")
    for i, x in enumerate((-3.0, -1.0, 1.0, 3.0)):
        tip = g.piece(f"nape_point_{i}", "HEAD", (-1, 0, -.5), (2, 2, 1), pivot=(x, -.4, 4.6), rotation=(8, 0, 0))
        cel_box(tip, 10175 + i, top_delta=0)
    bangs(g, "fringe", [(-3.2, ((2, 3), (1, 1)), 8), (-1.2, ((2, 2),), 4), (1.2, ((2, 2),), -4),
                        (3.2, ((2, 3), (1, 1)), -8)], seed=10180)
