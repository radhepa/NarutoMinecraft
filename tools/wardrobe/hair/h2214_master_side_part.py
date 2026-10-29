"""Master's Side Part: the master builder's neat cut, combed into a deep side part on the left and
swept across and back, tidy above the ears and squared off at the nape."""
from anime import bangs, ring_shell, spike
from paint import k, scalp

META = {"name": "Master's Side Part", "gender": "unisex",
        "description": "A neat deep side part swept across and back, tidy above the ears, squared nape."}


def build(g):
    scalp(g, 22281, side_rows=4, back_rows=7, sideburn=2, part=5)
    hat = ring_shell(g, 22282, side_rows=4, back_rows=7, ring_row=1)
    hat.top.vline(5, 0, 7, k("H", 0))
    for i, (x, z, rx, rz) in enumerate(((1.6, -2.6, -40, 66), (-.6, -2.8, -44, 58), (-2.6, -2.0, -40, 40),
                                        (-.4, .4, -64, 36), (-2.4, 1.2, -66, 20))):
        spike(g, f"sweep_{i}", (x, -7.9, z), (rx, 0, rz), ((3, 2), (2, 2), (1, 1)), 2, 22284 + i)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 40), (-.8, ((3, 1), (2, 1)), 62), (1.4, ((2, 1),), 70)], seed=22292)
