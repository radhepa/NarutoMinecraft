"""Raven Feathers: layered blue-black hair cut in long pointed feathers, two tiers folding down the
back like a crow's closed wings, feathered side locks and a short fringe."""
from anime import bangs, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Raven Feathers", "gender": "unisex",
        "description": "Long pointed layers folding down the back in two tiers like wings, feathered side locks."}

# Feathers: (x, y, z, rx, rz, segments)
UPPER = [(-3.2, -7.4, 4.3, 30, 30), (-1.1, -7.6, 4.5, 36, 10), (1.1, -7.6, 4.5, 36, -10), (3.2, -7.4, 4.3, 30, -30)]
LOWER = [(-3.0, -4.6, 4.8, 14, 22), (-1.0, -4.8, 5.0, 18, 8), (1.0, -4.8, 5.0, 18, -8), (3.0, -4.6, 4.8, 14, -22)]


def build(g):
    scalp(g, 3701, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 3702, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, y, z, rx, rz) in enumerate(UPPER):
        lock(g, f"feather_upper_{i}", (x, y, z), (rx, 0, rz), ((2, 4), (1, 2)), 1, 3710 + i * 4)
    for i, (x, y, z, rx, rz) in enumerate(LOWER):
        lock(g, f"feather_lower_{i}", (x, y, z), (rx, 0, rz), ((3, 5), (2, 2), (1, 2)), 1, 3730 + i * 4, motion="sway")
    for side, sign in (("right", -1), ("left", 1)):
        for j, (z, flare, n) in enumerate(((-1.4, 18, 6), (1.2, 26, 5))):
            lock(g, f"side_feather_{side}_{j}", (4.45 * sign, -6.8, z), (0, 0, -flare * sign), ((2, n - 2), (1, 2)), 1,
                 3750 + j * 3 + (sign > 0))
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 30), (-.6, ((2, 2), (1, 1)), 18), (1.4, ((2, 2), (1, 1)), -16),
                        (2.9, ((2, 2), (1, 1)), -30)], seed=3770)
    sidelocks(g, "frame", 9, seed=3780, x=4.3, z=-3.5, flare=4, width=2)
