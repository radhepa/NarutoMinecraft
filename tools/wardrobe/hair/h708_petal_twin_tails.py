"""Petal Twin Tails: two low tails gathered behind the ears and bound with blossom ties, falling over
the shoulders to the chest, a soft centre-parted fringe and smooth sides."""
from anime import bangs, lock, ring_shell, tie
from kit_yamanaka import flower
from paint import scalp

META = {"name": "Petal Twin Tails", "gender": "unisex",
        "description": "Two low tails behind the ears with blossom ties, centre-parted fringe."}


def build(g):
    scalp(g, 7701, side_rows=6, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 7702, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 22), (-1.2, ((2, 2), (1, 1)), 30), (1.2, ((2, 2), (1, 1)), -30),
                        (2.8, ((2, 2), (1, 1)), -22)], seed=7710)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (4.4 * sign, -3.4, 2.2)
        tie(g, f"tie_{side}", pivot, (10, 0, -10 * sign), (2, 1, 2), key="A2")
        flower(g, f"bloom_{side}", (4.4 * sign + .9 * sign, -3.4, 2.2), rotation=(0, -90 * sign, 0))
        lock(g, f"tail_{side}", pivot, (10, 0, -10 * sign), ((3, 3), (3, 3), (2, 3), (1, 2)), 2, 7720 + (sign > 0) * 9,
             ring=None, motion="sway", y0=1)
