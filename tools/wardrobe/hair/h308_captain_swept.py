"""Captain Swept: Fugaku's stern swept-back cut, the hair combed straight back off a high brow into a
layered back, short dark side locks before the ears and no fringe."""
from anime import lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Captain Swept", "gender": "unisex", "description": "Combed straight back off the brow, layered at the back, short side locks."}

# Locks lying back over the crown: (x, z, segments, rx)
TOP = [(-2.6, -3.4, ((3, 4), (2, 3)), 96), (0, -3.6, ((3, 4), (2, 3)), 98),
       (2.6, -3.4, ((3, 4), (2, 3)), 96)]


def build(g):
    scalp(g, 3361, side_rows=4, back_rows=8, sideburn=2, shadow=False)
    ring_shell(g, 3362, side_rows=4, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx) in enumerate(TOP):
        lock(g, f"crown_comb_{i}", (x, -8.3, z), (rx, 0, 0), segs, 1, 3370 + i * 4, ring=0)
    for i, (x, rz) in enumerate(((-3.0, 18), (-1.0, 6), (1.0, -6), (3.0, -18))):
        lock(g, f"back_{i}", (x, -6.6, 4.4), (24, 0, rz), ((2, 3), (1, 2)), 1, 3385 + i * 3)
    sidelocks(g, "sidelock", 6, seed=3395, x=4.4, z=-3.0, flare=6, width=2)
