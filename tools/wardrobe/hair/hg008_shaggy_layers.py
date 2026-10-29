"""Shaggy Layers: choppy layered hair to the nape, every layer flicking out at the tips over the ears and
down the back, with a long uneven fringe that stops at the brows."""
from anime import bangs, lock, ring_shell
from paint import scalp

META = {"name": "Shaggy Layers", "gender": "unisex",
        "description": "Choppy layers to the nape flicking out at the tips, a long uneven fringe to the brows."}

FLICK = ((2, 2), (2, 1), (1, 1))


def build(g):
    scalp(g, 31880, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 31881, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 16), (-1.4, ((2, 2), (1, 1)), 4), (.2, ((2, 2), (1, 1)), -8),
                        (1.8, ((2, 2), (1, 1)), 10), (3.0, ((2, 2), (1, 1)), -18)], seed=31882)
    n = 0
    for side, sign in (("right", -1), ("left", 1)):
        for z, y, rz in ((-2.6, -6.6, 22), (-.4, -6.0, 34), (1.8, -6.4, 28), (-1.4, -3.8, 48), (1.0, -3.6, 52)):
            lock(g, f"layer_{side}_{n}", (4.3 * sign, y, z), (0, 0, -rz * sign), FLICK, 2, 31888 + n * 3)
            n += 1
    for i, (x, y, rx, rz) in enumerate(((-2.6, -6.4, 18, 14), (0, -6.6, 16, -4), (2.6, -6.4, 18, -16),
                                        (-1.6, -3.4, 40, 30), (1.6, -3.4, 40, -30), (0, -3.0, 46, 4))):
        lock(g, f"back_layer_{i}", (x, y, 4.3), (rx, 0, rz), FLICK, 2, 31920 + i * 3)
