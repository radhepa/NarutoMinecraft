"""Back Braid: hair pulled into one long, firm braid down the middle of the back, tied off with a
white cord above a small tuft, with a soft side-parted fringe and smooth sides."""
from anime import braid, cel_box, lock, ring_shell, tie
from kit_kurama import side_fringe
from paint import scalp

META = {"name": "Back Braid", "gender": "unisex",
        "description": "One long braid down the middle of the back with a white cord, soft side-parted fringe."}


def build(g):
    scalp(g, 24351, side_rows=5, back_rows=8, sideburn=2, part=2)
    ring_shell(g, 24352, side_rows=4, back_rows=8, ring_row=1)
    side_fringe(g, "fringe", 24355, side=1)
    root = g.piece("root", "HEAD", (-2, 0, -1), (4, 2, 2), pivot=(0, -4.6, 4.4))
    cel_box(root, 24360)
    end = braid(g, "braid", (0, -2.8, 5.0), (8, 0, 0), links=7, width=3, seed=24365)
    tie(g, "cord", (0, -2.8, 5.0), (8, 0, 0), (3, 1, 3), y=end - 3, key="S4", motion="sway")
    lock(g, "temple", (4.4, -7.4, -3.0), (0, 0, -6), ((1, 4), (1, 1)), 1, 24370)
