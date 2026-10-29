"""Layered Flick: collar-length hair cut in layers whose ends flick outward all round, a soft fringe
parted at the brow and the ears half covered: easy, lively and worn by anyone in the clan."""
from anime import back_fan, bangs, ring_shell, sidelocks
from paint import scalp

META = {"name": "Layered Flick", "gender": "unisex",
        "description": "Collar-length layers flicking outward at the ends, soft parted fringe, ears half covered."}

FLICK = ((3, 4), (2, 2), (1, 1))
BACK = [(-3.0, FLICK, 16, 12), (-1.0, ((3, 5), (2, 2), (1, 1)), 12, 14), (1.0, ((3, 5), (2, 2), (1, 1)), -12, 14),
        (3.0, FLICK, -16, 12)]


def build(g):
    scalp(g, 1384, side_rows=7, back_rows=8, sideburn=3, part=5)
    ring_shell(g, 1385, side_rows=6, back_rows=8, ring_row=1)
    back_fan(g, "layer", BACK, seed=1389, z=4.3)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 20), (-1.0, ((2, 2), (1, 1)), 34), (1.6, ((2, 2), (1, 1)), -20),
                        (3.0, ((2, 2), (1, 1)), -10)], seed=1399)
    sidelocks(g, "frame", 7, seed=1404, x=4.4, z=-3.0, flare=8, width=2)
    sidelocks(g, "ear", 6, seed=1409, x=4.5, z=.4, flare=12, width=3)
