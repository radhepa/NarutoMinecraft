"""Twin High Tails: hair parted down the middle and tied in two tails high on either side of the
crown, each standing out and drooping to the shoulders in stiff points, a short straight fringe."""
from anime import bangs
from kit_umino import combed_up, knot
from anime import lock

META = {"name": "Twin High Tails", "gender": "female",
        "description": "Two tails tied high on either side of the crown, drooping to the shoulders in points."}

TAIL = ((3, 3), (3, 2), (2, 2), (1, 2))


def build(g):
    combed_up(g, 18101, side_rows=5, back_rows=7, sideburn=2, streaks=False)
    g.part("head").top.vline(3, 0, 7, "H0")
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 12), (-.8, ((2, 2), (1, 1)), 4), (.8, ((2, 2), (1, 1)), -4),
                        (2.4, ((2, 2), (1, 1)), -12)], seed=18103)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (3.0 * sign, -7.8, 2.4)
        knot(g, f"tail_{side}", pivot, rx=-20)
        lock(g, f"tail_{side}", (3.6 * sign, -8.2, 2.8), (16, 0, -26 * sign), TAIL, 2, 18110 + (sign > 0) * 9, ring=None,
             motion="sway")
