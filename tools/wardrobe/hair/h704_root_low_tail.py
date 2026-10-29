"""Root Low Tail: straight hair with a blunt centre-parted fringe at the brows, smooth sides tucked
behind the ears and the length gathered at the nape in a short tail bound with a dark cloth wrap,
the plain way a Root operative keeps it."""
from anime import bangs, lock, ring_shell, tie
from paint import scalp

META = {"name": "Root Low Tail", "gender": "unisex",
        "description": "Blunt centre-parted fringe, smooth sides, a short nape tail in a dark cloth wrap."}


def build(g):
    scalp(g, 7301, side_rows=7, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 7302, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 3),), 8), (-1.3, ((2, 2),), 4), (1.3, ((2, 2),), -4), (2.9, ((2, 3),), -8)], seed=7310)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"side_{side}", (4.45 * sign, -7.4, -1.6), (0, 0, -3 * sign), ((2, 6), (1, 1)), 3, 7320 + (sign > 0))
    tie(g, "wrap", (0, -1.4, 4.4), (-8, 0, 0), (3, 2, 2), y=-.5, key="K2")
    lock(g, "tail", (0, -.2, 4.6), (-12, 0, 0), ((3, 3), (2, 3), (1, 2)), 2, 7330, ring=None, motion="sway")
