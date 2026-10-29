"""Bell Bob: a rounded bob that swells over the ears and curls in at the jaw like the mouth of a
lily-of-the-valley bell, a soft straight fringe to the brows and a bell sprig pinned at the left
temple."""
from anime import bangs, cel_box, ring_shell
from kit_suzuran import bell_charm
from paint import scalp

META = {"name": "Bell Bob", "gender": "unisex",
        "description": "Rounded bob curling in at the jaw like a bell, straight fringe, a bell sprig pin."}


def build(g):
    scalp(g, 24001, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 24002, side_rows=7, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        swell = g.piece(f"swell_{side}", "HEAD", (-1, 0, -3.5), (2, 6, 7), pivot=(4.6 * sign, -7.6, .4))
        cel_box(swell, 24010 + (sign > 0), ring=1)
        curl = g.piece(f"curl_{side}", "HEAD", (-1, 0, -3), (1, 2, 6), pivot=(4.6 * sign - .5 * sign, -1.7, .6))
        cel_box(curl, 24012 + (sign > 0), top_delta=0)
    back = g.piece("back", "HEAD", (-5, 0, -1), (10, 7, 2), pivot=(0, -7.6, 4.6))
    cel_box(back, 24014, ring=1)
    curl = g.piece("back_curl", "HEAD", (-4.5, 0, -1), (9, 1, 1), pivot=(0, -.7, 4.4))
    cel_box(curl, 24015, top_delta=0)
    bangs(g, "fringe", [(-3.0, ((2, 2), (2, 1)), 6), (-1.0, ((2, 3),), 2), (1.0, ((2, 3),), -2),
                        (3.0, ((2, 2), (2, 1)), -6)], seed=24020)
    bell_charm(g, "pin", (4.9, -7.0, -2.4), rotation=(0, -90, 20))
