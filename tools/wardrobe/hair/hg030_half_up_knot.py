"""Half-Up Knot: the top half of the hair gathered into a small knot high at the back of the crown,
the rest falling straight past the shoulders, a light fringe and loose locks by the ears."""
from anime import bangs, cel_box, ring_shell, sidelocks
from kit_kunoichi import round_bun
from paint import scalp

META = {"name": "Half-Up Knot", "gender": "unisex",
        "description": "A small knot high at the back of the crown, the rest straight past the shoulders."}


def build(g):
    scalp(g, 33960, side_rows=7, back_rows=8, sideburn=2)
    ring_shell(g, 33961, side_rows=7, back_rows=8, ring_row=1)
    round_bun(g, "knot", (0, -7.6, 3.4), (-30, 0, 0), size=3, seed=33962, tie_key="A2")
    sheet = g.piece("length", "HEAD", (-4, 0, -.5), (8, 8, 1), pivot=(0, -5.4, 4.6), rotation=(-6, 0, 0), motion="sway")
    cel_box(sheet, 33964, ring=None)
    for i, x in enumerate((-2.5, .5)):
        tip = g.piece(f"length_tip_{i}", "HEAD", (x - .5, 8, -.5), (3, 2, 1), pivot=(0, -5.4, 4.6), rotation=(-6, 0, 0),
                      motion="sway")
        cel_box(tip, 33965 + i, top_delta=0)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -2.5), (1, 8, 6), pivot=(4.6 * sign, -7.0, .7))
        cel_box(panel, 33967 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 14), (-.9, ((2, 1), (1, 1)), 26), (.9, ((2, 1), (1, 1)), -26),
                        (2.6, ((2, 2), (1, 1)), -14)], seed=33969)
    sidelocks(g, "frame", 8, seed=33973, x=4.3, z=-3.4, flare=3, width=1)
