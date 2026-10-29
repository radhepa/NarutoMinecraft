"""Quiet Tufts: short, soft hair that sticks up in a few small tufts however it is combed, a light
fringe of short points and wisps curling at the nape and over the ears."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Quiet Tufts", "gender": "unisex",
        "description": "Short soft hair with a few small tufts, a light fringe of points, nape wisps."}

TUFT = ((2, 2), (1, 1))


def build(g):
    scalp(g, 25220, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 25221, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.2, -1.8, -10, -28), (.2, -.6, 6, 10), (2.4, -2.0, -8, 30),
                                        (-1.0, 2.0, 24, -14), (1.6, 2.4, 26, 22))):
        spike(g, f"tuft_{i}", (x, -7.8, z), (rx, 0, rz), TUFT, 2, 25222 + i)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 20), (-1.0, ((2, 1), (1, 1)), 6), (.8, ((2, 2),), -8),
                        (2.7, ((2, 2), (1, 1)), -22)], seed=25228)
    sidelocks(g, "ear", 4, seed=25232, x=4.4, z=-1.6, flare=14, width=1)
    back_fan(g, "nape", [(-2.4, ((2, 3), (1, 1)), 24, 18), (0, ((2, 3), (1, 1)), 0, 14), (2.4, ((2, 3), (1, 1)), -24, 18)],
             seed=25235)
