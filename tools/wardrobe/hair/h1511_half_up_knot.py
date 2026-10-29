"""Half-Up Knot: shoulder-length hair with the top section gathered into a small round knot at the
back of the crown, the rest left to fall straight; face-framing locks to the jaw."""
from anime import bangs, cel_box, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Half-Up Knot", "gender": "unisex",
        "description": "Shoulder-length hair, the top gathered into a small knot at the back, jaw-length locks."}


def build(g):
    scalp(g, 15280, side_rows=7, back_rows=8, sideburn=4)
    ring_shell(g, 15281, side_rows=7, back_rows=8, ring_row=1)
    back = g.piece("back", "HEAD", (-4.5, 0, -.5), (9, 10, 1), pivot=(0, -6.0, 4.6), rotation=(-4, 0, 0), motion="sway")
    cel_box(back, 15282, ring=None)
    for i, x in enumerate((-3.5, 0, 3.5)):
        tip = g.piece(f"back_tip_{i}", "HEAD", (x - 1, 10, -.5), (2, 1, 1), pivot=(0, -6.0, 4.6), rotation=(-4, 0, 0),
                      motion="sway")
        cel_box(tip, 15284 + i, top_delta=0)
    knot = g.piece("knot", "HEAD", (-2, -2, 0), (4, 3, 3), pivot=(0, -6.6, 5.0))
    cel_box(knot, 15288, ring=1)
    tie(g, "knot_tie", (0, -6.6, 4.9), size=(5, 1, 1), y=.6, key="D2")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 14), (-1.0, ((2, 1), (1, 1)), 24), (1.0, ((2, 1), (1, 1)), -24),
                        (2.8, ((2, 2), (1, 1)), -14)], seed=15290)
    sidelocks(g, "frame", 8, seed=15295, x=4.3, z=-3.4, flare=3, width=2)
