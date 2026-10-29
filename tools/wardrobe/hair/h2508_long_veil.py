"""Long Veil: straight hair falling in one dark sheet to the middle of the back like a night curtain
let down, a straight-cut fringe to the brows and long locks before the ears to the collarbone."""
from anime import bangs, cel_box, curtain, ring_shell, sidelocks
from paint import scalp

META = {"name": "Long Veil", "gender": "unisex",
        "description": "Straight sheet to mid-back, a straight-cut brow fringe, locks to the collarbone."}


def build(g):
    scalp(g, 25140, side_rows=7, back_rows=8, sideburn=4)
    ring_shell(g, 25141, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "veil", (0, -6.0, 4.6), (-5, 0, 0), 9, 14, hem=[(0, 3, 1), (3, 3, 1), (6, 3, 1)], seed=25142)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -2), (1, 9, 6), pivot=(4.6 * sign, -7, 1.0), motion="sway")
        cel_box(panel, 25146 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-3.0, ((2, 2),), 4), (-1.0, ((2, 2),), 0), (1.0, ((2, 2),), 0), (3.0, ((2, 2),), -4)],
          seed=25150)
    sidelocks(g, "frame", 11, seed=25155, x=4.3, z=-3.4, flare=1, width=2, taper=False)
