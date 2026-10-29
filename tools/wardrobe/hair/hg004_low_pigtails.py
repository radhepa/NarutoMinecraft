"""Low Pigtails: hair parted down the middle and gathered into two bunches just below the ears, tied with
cloth ties and falling forward over the shoulders, with a soft parted fringe."""
from anime import bangs, lock, ring_shell, tie
from paint import scalp

META = {"name": "Low Pigtails", "gender": "female",
        "description": "Centre-parted hair in two low bunches below the ears, tied and falling over the shoulders."}

TAIL = ((3, 3), (3, 2), (2, 2), (1, 1))


def build(g):
    scalp(g, 31790, side_rows=7, back_rows=8, sideburn=3, part=3)
    hat = ring_shell(g, 31791, side_rows=6, back_rows=8, ring_row=1)
    hat.back.vline(3, 0, 7, "H1")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 24), (-1.2, ((2, 2), (1, 1)), 30), (1.2, ((2, 2), (1, 1)), -30),
                        (2.8, ((2, 2), (1, 1)), -24)], seed=31792)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (4.7 * sign, -2.0, -.6)
        rot = (-34, 0, -12 * sign)
        tie(g, f"tie_{side}", pivot, rot, (3, 1, 3), key="A2")
        lock(g, f"tail_{side}", pivot, rot, TAIL, 3, 31796 + (sign > 0) * 7, ring=None, motion="sway", y0=1)
