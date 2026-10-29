"""Wild Spikes: a mass of short, heavy spikes thrown every which way as if never combed, points over
the ears and at the nape and a ragged row of short points along the hairline."""
from anime import bangs, lock, ring_shell, spike
from paint import scalp

META = {"name": "Wild Spikes", "gender": "unisex",
        "description": "Short heavy spikes in every direction, points over the ears and nape, a ragged hairline."}

TUFT = ((3, 2), (2, 2), (1, 1))
SMALL = ((2, 2), (1, 1))
CROWN = [(-2.6, -2.2, TUFT, 10, -40), (0, -2.6, TUFT, 18, -6), (2.6, -2.0, TUFT, 8, 38),
         (-2.8, .6, TUFT, -20, -48), (-.4, .4, TUFT, -14, 12), (2.4, .8, TUFT, -22, 44),
         (-1.4, 2.8, SMALL, -46, -24), (1.4, 2.8, SMALL, -44, 28)]


def build(g):
    scalp(g, 32860, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 32861, side_rows=4, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_{i}", (x, -7.7, z), (rx, 0, rz), segs, 2, 32862 + i)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 24), (-.6, ((2, 1), (1, 1)), -16), (1.4, ((2, 1), (1, 1)), 20),
                        (2.9, ((2, 2), (1, 1)), -26)], seed=32870)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"ear_{side}", (4.4 * sign, -5.6, -.4), (0, 0, -40 * sign), ((2, 2), (1, 2)), 2, 32871 + (sign > 0))
    for i, (x, rz) in enumerate(((-2.6, 36), (0, 0), (2.6, -36))):
        lock(g, f"nape_{i}", (x, -3.0, 4.3), (48, 0, rz), ((2, 2), (1, 2)), 1, 32873 + i)
