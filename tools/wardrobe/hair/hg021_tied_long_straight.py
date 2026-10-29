"""Tied Long Straight: straight hair parted at the centre and falling to the waist, gathered loosely
near the ends with a cloth tie, the fringe parted off the brow and long locks framing the face."""
from anime import bangs, cel_box, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Tied Long Straight", "gender": "female",
        "description": "Waist-length straight hair parted at the centre, tied loosely near the ends."}

PIVOT, TILT = (0, -6.2, 4.6), (-6, 0, 0)


def build(g):
    scalp(g, 33800, side_rows=7, back_rows=8, sideburn=3, part=3)
    ring_shell(g, 33801, side_rows=7, back_rows=8, ring_row=1)
    sheet = g.piece("length", "HEAD", (-4, 0, -.5), (8, 11, 1), pivot=PIVOT, rotation=TILT, motion="sway")
    cel_box(sheet, 33802, ring=1)
    gathered = g.piece("length_gathered", "HEAD", (-2, 11, -.5), (4, 6, 1), pivot=PIVOT, rotation=TILT, motion="sway")
    cel_box(gathered, 33803, top_delta=0)
    point = g.piece("length_point", "HEAD", (-1, 17, -.5), (2, 1, 1), pivot=PIVOT, rotation=TILT, motion="sway")
    cel_box(point, 33804, top_delta=0)
    tie(g, "tie", PIVOT, TILT, (5, 1, 2), y=11.2, key="A2", motion="sway")
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3), (1, 9, 7), pivot=(4.6 * sign, -7.2, .6))
        cel_box(panel, 33805 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 22), (-1.1, ((2, 1), (1, 1)), 34), (1.1, ((2, 1), (1, 1)), -34),
                        (2.7, ((2, 2), (1, 1)), -22)], seed=33807)
    sidelocks(g, "frame", 11, seed=33811, x=4.3, z=-3.4, flare=2, width=2)
