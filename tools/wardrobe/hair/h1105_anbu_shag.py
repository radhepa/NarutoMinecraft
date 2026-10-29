"""ANBU Shag: Kakashi in his ANBU years, the slanting spikes grown out shaggy, longer points over the
brow, ragged locks over the ears and a spiky nape grown down to the collar."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "ANBU Shag", "gender": "unisex",
        "description": "Slanting spikes grown out shaggy: longer brow points, ragged side locks, a spiky nape to the collar."}

BIG = ((4, 3), (3, 2), (2, 2), (1, 2))
MID = ((3, 2), (2, 2), (1, 2))
CROWN = [(-2.4, -2.4, MID, -20, 24), (.2, -2.6, BIG, -16, 32), (2.6, -2.0, MID, -12, 50),
         (-2.6, .6, BIG, 6, 26), (.2, .6, BIG, 8, 34), (2.8, .8, MID, 10, 50),
         (-1.4, 3.0, MID, 34, 30), (1.6, 3.0, MID, 34, 42)]


def build(g):
    scalp(g, 11401, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 11402, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 11410 + i)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 20), (-1.0, ((2, 2), (1, 1)), 14), (.8, ((2, 2), (1, 1)), 8),
                        (2.6, ((2, 2), (1, 1)), -6)], seed=11430)
    sidelocks(g, "frame", 7, seed=11440, x=4.35, z=-3.2, flare=10, width=2)
    sidelocks(g, "sidelock", 6, seed=11445, x=4.45, z=-.6, flare=16, width=2)
    back_fan(g, "nape", [(-3.0, ((2, 4), (1, 2)), 18, 14), (-1.0, ((2, 5), (1, 2)), 6, 12),
                         (1.0, ((2, 5), (1, 2)), -6, 12), (3.0, ((2, 4), (1, 2)), -18, 14)], seed=11450)
