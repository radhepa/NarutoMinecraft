"""Night Curtain: Yugao Uzuki's hair, a straight sheet to the waist with a side-swept fringe that
clears the eyes, long locks framing the face to the collarbone and a pointed, uneven hem."""
from anime import bangs, curtain, ring_shell, sidelocks
from paint import scalp

META = {"name": "Night Curtain", "gender": "female",
        "description": "Straight hair to the waist, side-swept fringe, long face-framing locks."}


def build(g):
    scalp(g, 15080, side_rows=7, back_rows=8, sideburn=4)
    ring_shell(g, 15081, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -6.2, 4.6), (-4, 0, 0), 9, 18, hem=[(0, 2, 3), (2, 3, 2), (5, 2, 3), (7, 2, 2)], seed=15082)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3), (1, 10, 7), pivot=(4.6 * sign, -7, .6), motion="sway")
        from anime import cel_box
        cel_box(panel, 15090 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-3.0, ((3, 2), (2, 1), (1, 1)), 28), (-1.2, ((3, 2), (2, 1)), 40),
                        (0.9, ((3, 1), (2, 1)), 48), (2.8, ((2, 2), (1, 1)), -14)], seed=15095)
    sidelocks(g, "frame", 11, seed=15100, x=4.3, z=-3.4, flare=3, width=2)
