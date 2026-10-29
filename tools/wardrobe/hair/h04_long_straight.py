"""Long Straight: sleek straight hair to the shoulder blades, parted bangs that leave the forehead
clear, long face-framing locks to the collarbone and a glossy sheen ring.

The length is one solid curtain down the back with a pointed, uneven hem, plus a side panel over
each ear, so the hair reads as a sheet rather than separate strands."""
from anime import bangs, cel_box, ring_shell, sidelocks
from paint import scalp

META = {"name": "Long Straight", "gender": "female",
        "description": "Straight hair to the shoulder blades, parted bangs, long face-framing locks."}

# The back curtain hangs from behind the crown; its hem is three points of different lengths.
CURTAIN_PIVOT, CURTAIN_TILT = (0, -6.0, 4.6), (-8, 0, 0)
HEM = [(-4.5, 3, 3), (-1.5, 3, 2), (1.5, 3, 3)]   # (x, width, length) below the sheet


def build(g):
    scalp(g, 501, side_rows=6, back_rows=8, sideburn=4)
    ring_shell(g, 502, side_rows=7, back_rows=8, ring_row=1)
    sheet = g.piece("curtain", "HEAD", (-4.5, 0, -.5), (9, 12, 1), pivot=CURTAIN_PIVOT, rotation=CURTAIN_TILT, motion="sway")
    cel_box(sheet, 510, ring=1)
    for i, (x, w, length) in enumerate(HEM):
        tip = g.piece(f"curtain_tip_{i}", "HEAD", (x, 12, -.5), (w, length - 1, 1), pivot=CURTAIN_PIVOT,
                      rotation=CURTAIN_TILT, motion="sway")
        cel_box(tip, 511 + i, top_delta=0)
        point = g.piece(f"curtain_point_{i}", "HEAD", (x + 1, 11 + length, -.5), (1, 1, 1), pivot=CURTAIN_PIVOT,
                        rotation=CURTAIN_TILT, motion="sway")
        cel_box(point, 515 + i, top_delta=0)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3), (1, 9, 7), pivot=(4.6 * sign, -7, .6))
        cel_box(panel, 520 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 16), (-1.2, ((2, 1), (1, 1)), 30),
                        (1.2, ((2, 1), (1, 1)), -30), (2.6, ((2, 2), (1, 1)), -16)], seed=530)
    sidelocks(g, "frame", 10, seed=540, x=4.3, z=-3.4, flare=3, width=2)
