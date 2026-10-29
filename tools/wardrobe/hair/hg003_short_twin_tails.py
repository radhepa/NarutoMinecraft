"""Short Twin Tails: chin-length hair with a full fringe, the back gathered into two short perky tails
tied high on either side of the head with bright cloth ties, flicking out and down."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Short Twin Tails", "gender": "female",
        "description": "Chin-length hair, a full fringe and two short perky tails tied high on each side."}

TAIL = ((3, 2), (2, 2), (2, 1), (1, 1))


def build(g):
    scalp(g, 31770, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 31771, side_rows=6, back_rows=7, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-1.0, ((2, 2), (1, 1)), 6), (1.0, ((2, 2), (1, 1)), -6),
                        (2.8, ((2, 2), (1, 1)), -18)], seed=31772)
    sidelocks(g, "frame", 5, seed=31776, x=4.3, z=-3.2, flare=4, width=2)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (4.6 * sign, -6.8, 1.8)
        rot = (18, 0, -34 * sign)
        tie(g, f"tie_{side}", pivot, rot, (3, 1, 3), key="A2")
        lock(g, f"tail_{side}", pivot, rot, TAIL, 2, 31780 + (sign > 0) * 7, ring=None, motion="sway", y0=1)
