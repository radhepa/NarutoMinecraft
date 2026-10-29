"""Chin Bob: a straight bob cut level at the chin all round, a little fuller at the back, the
fringe parted to one side and tucked behind the left ear."""
from anime import bangs, cel_box, ring_shell
from paint import scalp

META = {"name": "Chin Bob", "gender": "unisex",
        "description": "Straight level chin bob, fuller at the back, a side-parted fringe tucked behind one ear."}


def build(g):
    scalp(g, 33935, side_rows=8, back_rows=8, sideburn=0, part=5)
    ring_shell(g, 33936, side_rows=8, back_rows=8, ring_row=1)
    back = g.piece("back", "HEAD", (-4.5, 0, -1), (9, 7, 2), pivot=(0, -7.6, 4.5), rotation=(-5, 0, 0))
    cel_box(back, 33937, ring=1)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-.5, 0, -3.5), (1, 8, 7), pivot=(4.6 * sign, -8, .4))
        cel_box(panel, 33938 + (sign > 0), ring=1)
    g.part("hat").left.vline(5, 1, 4, "H1")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-1.1, ((3, 2), (2, 1)), 28), (.8, ((3, 2), (1, 1)), 36),
                        (2.6, ((2, 1),), 50)], seed=33940)
