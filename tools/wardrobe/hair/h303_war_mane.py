"""War Mane: Madara's enormous wild mane, a jagged black sheet to the small of the back that flares
out past the shoulders, spiky crown, and one long bang hanging down the right cheek."""
from anime import cel_box, curtain, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "War Mane", "gender": "unisex", "extras_height": 224,
        "description": "A huge spiky mane to the small of the back, flaring wide, and a long bang down one cheek."}

HEM = [(0, 3, 4), (2, 3, 3), (4, 3, 5), (6, 3, 3), (8, 3, 4), (10, 2, 3)]
# Flaring outer locks: (x, y, z, segments, rx, rz)
FLARE = [(-4.6, -6.0, 2.0, ((3, 5), (2, 4), (1, 2)), 8, 28), (4.6, -6.0, 2.0, ((3, 5), (2, 4), (1, 2)), 8, -28),
         (-4.4, -4.0, 3.6, ((3, 5), (2, 3), (1, 2)), 16, 40), (4.4, -4.0, 3.6, ((3, 5), (2, 3), (1, 2)), 16, -40),
         (-3.0, -2.0, 4.8, ((3, 4), (2, 3), (1, 2)), 22, 22), (3.0, -2.0, 4.8, ((3, 4), (2, 3), (1, 2)), 22, -22)]


def build(g):
    scalp(g, 3081, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 3082, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "mane", (0, -6.4, 4.9), (-6, 0, 0), 12, 13, HEM, seed=3085, depth=2)
    for i, (x, y, z, segs, rx, rz) in enumerate(FLARE):
        lock(g, f"mane_flare_{i}", (x, y, z), (rx, 0, rz), segs, 2, 3090 + i * 3, motion="sway")
    for i, (x, z, rx, rz) in enumerate(((-2.6, -2.4, -20, -24), (0, -2.0, -16, 6), (2.6, -2.2, -18, 26),
                                        (-2.0, .8, 4, -30), (1.8, .8, 4, 30), (0, 2.6, 24, 0))):
        spike(g, f"crown_spike_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 2), (2, 2), (1, 1)), 3, 3110 + i)
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"side_{side}", "HEAD", (-1, 0, -3), (2, 9, 7), pivot=(4.9 * sign, -7.2, .8), rotation=(0, 0, -6 * sign))
        cel_box(panel, 3120 + (sign > 0), ring=1)
    # The long bang falls down the right cheek, outside the eye.
    lock(g, "bang_long", (-4.35, -8.0, -3.8), (-2, 0, 3), ((2, 5), (2, 4), (1, 2)), 1, 3125)
    lock(g, "bang_short", (4.35, -8.0, -3.8), (-2, 0, -8), ((2, 5), (1, 2)), 1, 3128)
    for i, (x, rz) in enumerate(((-1.8, 26), (.4, -6), (2.2, -24))):
        lock(g, f"fringe_{i}", (x, -8.6, -4.3), (-14, 0, rz), ((2, 2), (1, 1)), 1, 3130 + i * 3, ring=0)
