"""Rain Shag: a short, overgrown shag of separate pointed locks falling every which way, over the
ears and down to the nape, with a ragged fringe at the brows."""
from anime import back_fan, bangs, lock, ring_shell
from paint import scalp

META = {"name": "Rain Shag", "gender": "unisex",
        "description": "Short overgrown shag in loose pointed locks over the ears and nape, ragged fringe."}

NAPE = [(-3.2, ((2, 3), (1, 2)), 18, 14), (-1.1, ((2, 4), (1, 2)), 6, 8), (1.1, ((2, 4), (1, 1)), -8, 10),
        (3.2, ((2, 3), (1, 2)), -18, 14)]


def build(g):
    scalp(g, 2192, side_rows=6, back_rows=8, sideburn=1)
    ring_shell(g, 2193, side_rows=5, back_rows=7, ring_row=1)
    back_fan(g, "nape", NAPE, seed=2194)
    for side, sign in (("right", -1), ("left", 1)):
        for i, (z, n, rz, rx) in enumerate(((-2.6, 5, 16, -6), (-.4, 6, 24, 6), (1.8, 5, 30, 14))):
            lock(g, f"side_{side}_{i}", (4.3 * sign, -7.6, z), (rx, 0, -rz * sign), ((2, n - 2), (1, 2)), 1,
                 2195 + i + (sign > 0) * 3, ring=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 24), (-1.6, ((2, 2), (1, 1)), -6), (-.1, ((2, 2), (1, 1)), 12),
                        (1.5, ((2, 2), (1, 1)), -14), (2.9, ((2, 2), (1, 1)), -26)], seed=2201)
    for i, (x, z, rz, rx) in enumerate(((-2.0, -1.0, 30, -30), (1.6, .6, -36, 20), (0, 2.6, 8, 40))):
        lock(g, f"cowlick_{i}", (x, -7.9, z), (rx + 180, 0, rz), ((2, 2), (1, 1)), 1, 2204 + i, ring=None)
