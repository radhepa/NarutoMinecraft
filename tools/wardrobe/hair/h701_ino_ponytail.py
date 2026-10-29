"""Ino Ponytail: the Yamanaka kunoichi's long platinum tail tied high on the crown and falling to the
hips, a heavy fringe swept across the brow to the wearer's right that stops on the eye line, and one
long lock sliding past the right cheek to the collarbone."""
from anime import cel_box, lock, ring_shell, tie
from paint import scalp

META = {"name": "Ino Ponytail", "gender": "unisex",
        "description": "Long high ponytail to the hips, a fringe swept over the right brow, a long cheek lock."}

# The swoop: every fringe lock leans to the wearer's right (-x) and ends above the eyes.
SWOOP = [(3.0, ((2, 2), (1, 1)), 10), (1.8, ((3, 2), (2, 2), (1, 1)), 56), (.2, ((3, 2), (2, 2), (1, 1)), 60),
         (-1.6, ((3, 2), (2, 2)), 50)]
TAIL = ((4, 3), (4, 4), (4, 4), (3, 4), (3, 3), (2, 3), (1, 2))


def build(g):
    scalp(g, 7001, side_rows=5, back_rows=7, sideburn=3)
    ring_shell(g, 7002, side_rows=4, back_rows=6, ring_row=1)
    for i, (x, segs, rz) in enumerate(SWOOP):
        lock(g, f"swoop_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 7010 + i * 13, ring=0)
    lock(g, "veil", (-4.7, -7.9, -3.4), (0, 0, 4), ((2, 4), (2, 4), (1, 2)), 1, 7040)
    lock(g, "frame_left", (4.5, -7.6, -3.3), (0, 0, -3), ((1, 6), (1, 1)), 1, 7045)
    tie(g, "tie", (0, -7.2, 4.4), (0, 0, 0), (3, 2, 3), y=-1)
    root = g.piece("tail_root", "HEAD", (-2, -2, 0), (4, 3, 3), pivot=(0, -7.4, 5.0), rotation=(20, 0, 0))
    cel_box(root, 7050, base=2)
    lock(g, "ponytail", (0, -7.4, 6.2), (16, 0, 0), TAIL, 3, 7060, ring=None, motion="sway")
