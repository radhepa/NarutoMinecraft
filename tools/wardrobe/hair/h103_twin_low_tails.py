"""Twin Low Tails: Tsunade's cut. A fringe parted in the middle with long locks framing the face to
the jaw, and the length gathered into two low tails tied at the nape, hanging to the waist."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Twin Low Tails", "gender": "female",
        "description": "Centre-parted fringe, jaw-length framing locks, two low tails tied at the nape to the waist."}

TAIL = ((2, 4), (2, 4), (3, 4), (2, 3), (1, 2))


def build(g):
    scalp(g, 1064, side_rows=6, back_rows=8, sideburn=4, part=3)
    ring_shell(g, 1065, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 12), (-1.8, ((2, 2), (1, 1)), 18),
                        (1.8, ((2, 2), (1, 1)), -18), (3.0, ((2, 2), (1, 1)), -10)], seed=1079)
    sidelocks(g, "frame", 9, seed=1084, x=4.3, z=-3.4, flare=4, width=2)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (2.2 * sign, -1.4, 4.6)
        tie(g, f"tie_{side}", pivot, (-5, 0, -4 * sign), (3, 1, 3))
        lock(g, f"tail_{side}", pivot, (-5, 0, -4 * sign), TAIL, 2, 1089 + (sign > 0) * 9, ring=None, motion="sway",
             y0=1)
