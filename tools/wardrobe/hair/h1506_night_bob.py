"""Night Bob: a heavy straight bob cut level with the jaw all the way round, a soft parted fringe
at the brows and the ends turned slightly under."""
from anime import bangs, cel_box, ring_shell
from paint import scalp

META = {"name": "Night Bob", "gender": "unisex",
        "description": "Straight jaw-length bob, ends turned under, a soft parted fringe at the brows."}


def build(g):
    scalp(g, 15150, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 15151, side_rows=8, back_rows=8, ring_row=1)
    back = g.piece("bob_back", "HEAD", (-4.5, 0, -.5), (9, 9, 1), pivot=(0, -7.6, 4.6))
    cel_box(back, 15152, ring=1)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"bob_{side}", "HEAD", (-.5, 0, -4), (1, 9, 9), pivot=(4.6 * sign, -7.6, .5))
        cel_box(panel, 15155 + (sign > 0), ring=1)
        curl = g.piece(f"bob_{side}_end", "HEAD", (-1, 0, -4), (2, 1, 9), pivot=(4.4 * sign, 1.4, .5))
        cel_box(curl, 15158 + (sign > 0), base=1, top_delta=0)
    curl = g.piece("bob_back_end", "HEAD", (-4.5, 0, -1.5), (9, 1, 2), pivot=(0, 1.4, 4.4))
    cel_box(curl, 15160, base=1, top_delta=0)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 10), (-1.0, ((2, 2), (1, 1)), 14),
                        (1.0, ((2, 2), (1, 1)), -14), (2.8, ((2, 2), (1, 1)), -10)], seed=15165)
