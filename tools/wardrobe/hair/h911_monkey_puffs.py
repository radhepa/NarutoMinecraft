"""Monkey Puffs: an invention after Enma's round ears. Short hair with a ragged fringe, the sides
gathered into two round puffs tied above the ears, so the head reads like a little monkey's."""
from anime import bangs, cel_box, ring_shell, spike, tie
from paint import scalp

META = {"name": "Monkey Puffs", "gender": "unisex",
        "description": "Short hair, ragged fringe and two round puffs tied above the ears."}


def build(g):
    scalp(g, 9611, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 9612, side_rows=5, back_rows=7, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-1.0, ((2, 2), (1, 1)), 8), (1.0, ((2, 2), (1, 1)), -8),
                        (2.8, ((2, 2), (1, 1)), -18)], seed=9620)
    for side, sign in (("right", -1), ("left", 1)):
        pivot = (4.3 * sign, -7.2, .8)
        tie(g, f"bun_tie_{side}", pivot, (0, 0, -90 * sign), (3, 1, 3), y=-.5, key="A2")
        puff = g.piece(f"bun_{side}", "HEAD", (-1.5, -1.5, -1.5), (3, 3, 3), pivot=(5.6 * sign, -7.6, .8))
        cel_box(puff, 9630 + (sign > 0), top_delta=1)
        for i, (rx, rz) in enumerate(((-30, 30 * sign), (20, 50 * sign))):
            spike(g, f"bun_{side}_tuft_{i}", (5.8 * sign, -9.0, .8), (rx, 0, rz), ((2, 1), (1, 1)), 1, 9640 + i)
    for i, (x, rz) in enumerate(((-2.0, -16), (0.0, 0), (2.0, 16))):
        spike(g, f"back_{i}", (x, -5.0, 3.8), (-110, 0, rz), ((3, 2), (2, 1), (1, 1)), 2, 9650 + i * 3)
