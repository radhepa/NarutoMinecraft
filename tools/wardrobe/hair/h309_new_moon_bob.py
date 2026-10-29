"""New Moon Bob: Sarada's chin-length bob, straight black hair cut level with the jaw, a fringe swept
off to the left and long pointed locks framing the face."""
from anime import bangs, cel_box, ring_shell, sidelocks
from paint import scalp

META = {"name": "New Moon Bob", "gender": "unisex", "description": "A chin-length bob, side-swept fringe and pointed framing locks."}


def build(g):
    scalp(g, 3401, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 3402, side_rows=7, back_rows=8, ring_row=1)
    back = g.piece("bob_back", "HEAD", (-5, 0, -1), (10, 9, 2), pivot=(0, -7.6, 4.6), rotation=(-4, 0, 0))
    cel_box(back, 3405, ring=1)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"bob_{side}", "HEAD", (-1, 0, -4), (2, 8, 8), pivot=(4.7 * sign, -7.6, .6))
        cel_box(panel, 3410 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-2.8, ((3, 2), (2, 1)), 38), (-.6, ((3, 2), (1, 1)), 40), (1.6, ((2, 2), (1, 1)), 30),
                        (3.0, ((2, 2), (1, 1)), -10)], seed=3415)
    sidelocks(g, "frame", 9, seed=3420, x=4.3, z=-3.6, flare=1, width=2)
