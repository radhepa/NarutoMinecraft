"""Messy Mop: a thick tousled mop that has never met a comb, short tufts sticking out every which way
over the crown and ears, a ragged fringe down to the brows and flicks at the nape."""
from anime import bangs, lock, ring_shell, spike
from paint import scalp

META = {"name": "Messy Mop", "gender": "unisex",
        "description": "Thick tousled mop, tufts sticking out every way, a ragged fringe to the brows, nape flicks."}

TUFT = ((3, 2), (2, 1), (1, 1))
SMALL = ((2, 2), (1, 1))
CROWN = [(-2.6, -2.4, TUFT, -34, -40), (-.4, -2.8, TUFT, -40, 10), (2.2, -2.0, TUFT, -30, 46), (0, -.2, TUFT, -8, -30),
         (2.6, .6, SMALL, 10, 60), (-2.8, 1.0, SMALL, 26, -56), (-.6, 2.0, TUFT, 40, 18), (1.8, 2.8, SMALL, 58, 30)]


def build(g):
    scalp(g, 31720, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 31721, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"tuft_{i}", (x, -7.8, z), (rx, 0, rz), segs, 3, 31722 + i)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 26), (-1.2, ((2, 2), (1, 1)), -12), (.6, ((2, 2), (1, 1)), 20),
                        (2.6, ((2, 2), (1, 1)), -24)], seed=31732)
    for side, sign in (("right", -1), ("left", 1)):
        for i, (y, rz) in enumerate(((-6.4, 70), (-4.6, 40))):
            lock(g, f"ear_tuft_{side}_{i}", (4.3 * sign, y, -.6 + i * 1.4), (0, 0, -rz * sign), SMALL, 2, 31736 + i + (sign > 0) * 3)
    for i, (x, rz) in enumerate(((-2.6, 34), (0, -6), (2.4, -38))):
        lock(g, f"nape_{i}", (x, -3.2, 4.3), (40, 0, rz), SMALL, 1, 31742 + i)
