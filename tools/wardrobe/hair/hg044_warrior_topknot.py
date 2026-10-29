"""Warrior Top-Knot: hair drawn up tight from every side into a knot on the crown, bound with a cord
and spraying out in a short brush of spikes; a few loose strands at the temples."""
from anime import cel_box, lock, ring_shell, spike
from kit_rugged import knot_bun
from paint import scalp

META = {"name": "Warrior Top-Knot", "gender": "unisex",
        "description": "Hair drawn up tight into a corded knot on the crown with a short brush of spikes, loose temple strands."}


def build(g):
    scalp(g, 35680, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 35681, side_rows=5, back_rows=7, ring_row=2)
    knot_bun(g, "knot", (0, -7.9, .8), (-14, 0, 0), (3, 2, 3), 35682)
    cord = g.piece("knot_cord", "HEAD", (-1.5, -1, -1.5), (3, 1, 3), pivot=(0, -7.7, .8), rotation=(-14, 0, 0), inflate=.15)
    cel_box(cord, 35683, base=0, top_delta=0)
    for i, (rx, rz, segs) in enumerate(((-30, -26, ((2, 2), (1, 2))), (-36, 0, ((3, 2), (2, 2), (1, 1))),
                                        (-30, 26, ((2, 2), (1, 2))), (-58, -12, ((2, 3), (1, 2))),
                                        (-58, 12, ((2, 3), (1, 2))))):
        spike(g, f"brush_{i}", (0, -9.6, 1.2), (rx, 0, rz), segs, 2, 35684 + i * 2)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"strand_{side}", (4.3 * sign, -7.4, -2.9), (0, 0, -6 * sign), ((1, 4), (1, 2)), 1, 35695 + (sign > 0))
