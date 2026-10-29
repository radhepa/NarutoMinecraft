"""Twin Scroll Braids: a centre part and soft brow-length bangs, the length divided behind each ear
into a braid that hangs forward over the shoulder like a pair of scroll cords, tied off with cloth."""
from anime import bangs, braid, cel_box, ring_shell, tie
from paint import scalp

META = {"name": "Twin Scroll Braids", "gender": "female",
        "description": "Centre part, soft bangs, a braid forward over each shoulder tied with cloth."}


def build(g):
    scalp(g, 12360, side_rows=7, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 12361, side_rows=7, back_rows=8, ring_row=1)
    for side, sign in (("right", -1), ("left", 1)):
        root = g.piece(f"root_{side}", "HEAD", (-1, 0, -2), (2, 8, 4), pivot=(4.4 * sign, -7.6, -1.6))
        cel_box(root, 12364 + (sign > 0), ring=1)
        braid(g, f"braid_{side}", (4.6 * sign, .4, -2.9), (0, 0, -3 * sign), links=5, width=2, seed=12370 + (sign > 0) * 20)
        tie(g, f"cloth_{side}", (4.6 * sign, .4, -2.9), (0, 0, -3 * sign), size=(3, 1, 3), y=8.6, key="A2")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 10), (-1.4, ((2, 2),), 18), (0, ((2, 1), (1, 1)), 0),
                        (1.4, ((2, 2),), -18), (2.8, ((2, 2), (1, 1)), -10)], seed=12400)
