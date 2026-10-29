"""Long Spikes: thick spikes swept straight back from the brow and streaming past the nape in long
tapering points, and rough points at the temples."""
from anime import bangs, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Long Spikes", "gender": "unisex",
        "description": "Thick spikes swept back from the brow, streaming past the nape in long tapering points."}

LONG = ((4, 3), (3, 3), (2, 3), (1, 2))
# Swept-back spikes: (x, y, z, segments, lean back, splay)
SWEEP = [(-2.4, -7.6, -1.6, LONG, 80, 8), (0, -8.0, -2.0, ((4, 4), (3, 3), (2, 3), (1, 2)), 84, 0),
         (2.4, -7.6, -1.6, LONG, 80, -8), (-3.4, -6.6, 1.0, LONG, 70, 14), (3.4, -6.6, 1.0, LONG, 70, -14),
         (-1.4, -7.6, 1.8, LONG, 64, 4), (1.4, -7.6, 1.8, LONG, 64, -4), (0, -5.4, 3.8, LONG, 44, 0),
         (-2.6, -4.4, 3.8, ((3, 3), (2, 3), (1, 2)), 36, 12), (2.6, -4.4, 3.8, ((3, 3), (2, 3), (1, 2)), 36, -12)]


def build(g):
    scalp(g, 35620, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 35621, side_rows=5, back_rows=8, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(SWEEP):
        lock(g, f"sweep_{i}", (x, y, z), (rx, 0, rz), segs, 2, 35622 + i, ring=0)
    bangs(g, "brow_point", [(-3.0, ((2, 2), (1, 1)), 30), (3.0, ((2, 2), (1, 1)), -30)], seed=35635)
    sidelocks(g, "temple", 5, seed=35637, x=4.4, z=-2.6, flare=22, width=2)
