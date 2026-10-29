"""Braided Fang: slanting silver spikes on the crown, the long back hair worked into one tight braid
that falls down the spine and ends in a small tuft: a kunoichi's version of the White Fang's tail."""
from anime import bangs, braid, ring_shell, sidelocks, spike, tie
from paint import scalp

META = {"name": "Braided Fang", "gender": "unisex",
        "description": "Slanting crown spikes, a pointed fringe and one long braid down the spine."}

MID = ((3, 2), (2, 2), (1, 1))
CROWN = [(-2.2, -2.2, MID, -16, 24), (.4, -2.4, ((3, 3), (2, 2), (1, 1)), -12, 34), (2.6, -1.8, MID, -8, 50),
         (-1.6, .8, MID, 16, 28), (1.4, 1.0, MID, 18, 42)]


def build(g):
    scalp(g, 12401, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 12402, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 12410 + i)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 18), (-.9, ((2, 2), (1, 1)), 10), (.9, ((2, 2), (1, 1)), -4),
                        (2.7, ((2, 2), (1, 1)), -16)], seed=12430)
    sidelocks(g, "frame", 8, seed=12440, x=4.3, z=-3.4, flare=5, width=2)
    tie(g, "tie", (0, -3.6, 4.4), (10, 0, 0), size=(3, 1, 3), key="D2")
    braid(g, "braid", (0, -3.6, 4.6), (10, 0, 0), links=6, width=3, seed=12450, y0=1.0)
