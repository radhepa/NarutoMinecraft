"""Parted Curtain: straight hair parted in the middle and falling to either side of the brow like a
curtain drawn back, long locks framing the face to the jaw and a soft, even nape to the collar."""
from anime import back_fan, bangs, ring_shell, sidelocks
from paint import scalp

META = {"name": "Parted Curtain", "gender": "unisex",
        "description": "Centre-parted straight fringe drawn aside to the brows, jaw-length framing locks."}


def build(g):
    scalp(g, 25000, side_rows=7, back_rows=8, sideburn=3, part=0)
    ring_shell(g, 25001, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((3, 2), (2, 1), (1, 1)), 30), (-1.1, ((2, 2), (1, 1)), 44),
                        (1.1, ((2, 2), (1, 1)), -44), (2.9, ((3, 2), (2, 1), (1, 1)), -30)], seed=25002)
    sidelocks(g, "frame", 9, seed=25005, x=4.3, z=-3.3, flare=3, width=2)
    back_fan(g, "nape", [(-3.0, ((3, 6), (2, 1)), 4, 6), (0, ((3, 6), (2, 1)), 0, 6), (3.0, ((3, 6), (2, 1)), -4, 6)],
             seed=25008)
