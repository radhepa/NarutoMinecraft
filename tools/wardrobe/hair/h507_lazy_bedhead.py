"""Lazy Bedhead: no tie today. The hair left loose falls in a stiff, spiky mop to the jaw, flat on
top where it was slept on and splayed out at the sides and nape."""
from anime import bangs, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Lazy Bedhead", "gender": "unisex",
        "description": "Hair left untied: a stiff spiky mop to the jaw, flat on top, splayed at the sides and nape."}

# Nape and side points: (x, y, z, segments, rx, rz)
SPLAY = [(-3.0, -4.0, 4.3, ((2, 3), (1, 2)), 30, 34), (-1.0, -4.0, 4.4, ((2, 4), (1, 2)), 26, 10),
         (1.0, -4.0, 4.4, ((2, 4), (1, 2)), 26, -10), (3.0, -4.0, 4.3, ((2, 3), (1, 2)), 30, -34),
         (-4.3, -5.0, 2.0, ((1, 3), (1, 2)), 0, 40), (4.3, -5.0, 2.0, ((1, 3), (1, 2)), 0, -40)]


def build(g):
    scalp(g, 5301, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 5302, side_rows=7, back_rows=8, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(SPLAY):
        lock(g, f"splay_{i}", (x, y, z), (rx, 0, rz), segs, 1, 5310 + i * 5, ring=None)
    sidelocks(g, "frame", 7, seed=5340, x=4.35, z=-3.2, flare=10, width=2)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 26), (-1.2, ((2, 2), (1, 1)), 10), (1.0, ((2, 2), (1, 1)), -14),
                        (2.8, ((2, 2), (1, 1)), -28)], seed=5350)
