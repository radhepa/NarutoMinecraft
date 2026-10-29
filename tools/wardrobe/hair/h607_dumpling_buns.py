"""Dumpling Buns: two round buns high on either side of the crown like a pair of dumplings, tied
with a red cord, spiky bangs and short spiked ends at the nape."""
from anime import bangs, cel_box, ring_shell, sidelocks, tie
from kit_akimichi import flick
from paint import scalp

META = {"name": "Dumpling Buns", "gender": "unisex",
        "description": "Two round buns high on the crown tied with red cord, spiky bangs and nape."}


def build(g):
    scalp(g, 6601, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 6602, side_rows=6, back_rows=7, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        bun = g.piece(f"bun_{side}", "HEAD", (-2.5, -4.5, -2.5), (5, 4, 5), pivot=(2.6 * sign, -7.9, 1.0),
                      rotation=(0, 0, 16 * sign))
        cel_box(bun, 6610 + (sign > 0), ring=1)
        crown = g.piece(f"bun_{side}_top", "HEAD", (-1.5, -5.5, -1.5), (3, 1, 3), pivot=(2.6 * sign, -7.9, 1.0),
                        rotation=(0, 0, 16 * sign))
        cel_box(crown, 6612 + (sign > 0), top_delta=2)
        tie(g, f"bun_tie_{side}", (2.6 * sign, -7.9, 1.0), (0, 0, 16 * sign), size=(5, 1, 5), y=-.8, key="A2")
    for i, (x, rz) in enumerate(((-2.4, 30), (-.8, 10), (.8, -10), (2.4, -30))):
        flick(g, f"nape_{i}", (x, -2.6, 4.1), (34, 0, rz), ((2, 2), (1, 1)), 1, 6620 + i)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 20), (-.6, ((2, 2), (1, 1)), 6), (1.6, ((2, 2), (1, 1)), -14)], seed=6630)
    sidelocks(g, "frame", 7, seed=6640, x=4.3, z=-3.4, flare=6, width=2)
