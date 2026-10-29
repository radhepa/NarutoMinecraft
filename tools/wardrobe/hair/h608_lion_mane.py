"""Lion Mane: a big round mane of spikes swept back from the face and bristling out on every side,
the points around the jaw and nape flaring wide like a lion's ruff."""
import math

from anime import bangs, ring_shell, spike
from kit_akimichi import flick
from paint import scalp

META = {"name": "Lion Mane", "gender": "unisex",
        "description": "Spikes swept back from the face and bristling out all round in a wide ruff."}


def build(g):
    scalp(g, 6701, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 6702, side_rows=7, back_rows=8, ring_row=1)
    # The ruff: rings of outward spikes at three heights, from the temples round the back.
    for r, (y, n, length) in enumerate(((-6.8, 7, 3), (-4.6, 7, 4), (-2.4, 5, 3))):
        for i in range(n):
            t = i / (n - 1)
            ang = -110 + 220 * t          # degrees round the head, 0 behind it
            a = math.radians(ang)
            x, z = 4.0 * math.sin(a), 4.0 * math.cos(a)
            rx, rz = 80 * math.cos(a), -80 * math.sin(a)
            flick(g, f"ruff_{r}_{i}", (x, y, z), (rx, 0, rz), ((3, 2), (2, length - 1), (1, 1)), 2, 6710 + r * 10 + i)
    for i, (x, z, rx, rz) in enumerate(((-2.4, -2.0, -40, -20), (0, -2.4, -48, 0), (2.4, -2.0, -40, 20))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 2), (2, 2), (1, 1)), 2, 6740 + i)
    bangs(g, "fringe", [(-2.2, ((2, 2), (1, 1)), 28), (2.2, ((2, 2), (1, 1)), -28)], seed=6750)
