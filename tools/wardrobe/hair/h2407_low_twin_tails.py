"""Low Twin Tails: two long tails gathered low behind the ears and tied with plain white cords,
falling down the back past the shoulder blades, the way the Sannin medic wore hers, and a fringe
swept apart from the centre to show the brow."""
from anime import bangs, lock, ring_shell, tie
from paint import scalp

META = {"name": "Low Twin Tails", "gender": "unisex",
        "description": "Two long tails tied low behind the ears with white cords, fringe swept apart at the centre."}

TAIL = ((3, 3), (3, 3), (3, 3), (2, 3), (1, 2))


def build(g):
    scalp(g, 24181, side_rows=6, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 24182, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.1, ((2, 3), (1, 1)), 8), (-1.4, ((2, 2), (1, 1)), 40), (1.4, ((2, 2), (1, 1)), -40),
                        (3.1, ((2, 3), (1, 1)), -8)], seed=24185)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (2.4 * sign, -2.4, 4.4)
        tie(g, f"tie_{side}", pivot, (10, 0, -6 * sign), (3, 1, 2), key="S4")
        lock(g, f"tail_{side}", pivot, (10, 0, -6 * sign), TAIL, 2, 24190 + (sign > 0) * 9, ring=None, motion="sway",
             y0=1)
