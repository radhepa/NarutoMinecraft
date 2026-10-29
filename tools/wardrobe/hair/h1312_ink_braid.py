"""Ink Braid: a calligrapher's hair, after Sai's ink and brush: sleek and centre parted, a light
fringe of points, the length drawn into one long braid down the back, tied off with a dark-red cord."""
from anime import bangs, braid, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Ink Braid", "gender": "unisex",
        "description": "Sleek centre-parted hair, a light pointed fringe, one long braid down the back with a red cord."}


def build(g):
    scalp(g, 13363, side_rows=6, back_rows=8, sideburn=3, part=3)
    ring_shell(g, 13364, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 20), (2.4, ((2, 2), (1, 1)), -20)], seed=13365)
    sidelocks(g, "frame", 7, seed=13366, x=4.3, z=-3.4, flare=2, width=1)
    tie(g, "braid_root", (0, -2.0, 4.6), (12, 0, 0), size=(3, 1, 2))
    end = braid(g, "braid", (0, -1.2, 4.7), (12, 0, 0), links=6, width=3, seed=13367)
    tie(g, "braid_cord", (0, -1.2, 4.7), (12, 0, 0), size=(2, 1, 2), y=end - 3, key="A2", motion="sway")
