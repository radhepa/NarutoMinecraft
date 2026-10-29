"""Rough Crop: short hair hacked off with a kunai, sticking out in uneven tufts all over, a few
short points at the brow and a ragged edge at the nape."""
from anime import bangs, lock, ring_shell, spike
from paint import scalp

META = {"name": "Rough Crop", "gender": "unisex",
        "description": "Short hair hacked off unevenly in tufts all over, short brow points, a ragged nape."}

TUFTS = [(-2.6, -2.0, 14, -30), (0, -2.2, 18, 6), (2.4, -1.8, 10, 34), (-3.0, 1.0, -22, -40), (-.6, .4, -10, -8),
         (1.6, .8, -18, 22), (3.0, 1.4, -26, 44), (-1.6, 2.8, -40, -16), (1.2, 2.8, -44, 14)]


def build(g):
    scalp(g, 35780, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 35781, side_rows=4, back_rows=6, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(TUFTS):
        segs = ((3, 2), (2, 1), (1, 1)) if i % 2 else ((2, 2), (1, 1))
        spike(g, f"tuft_{i}", (x, -7.8, z), (rx, 0, rz), segs, 2, 35782 + i)
    bangs(g, "brow_point", [(-2.4, ((2, 2), (1, 1)), 16), (0, ((2, 1), (1, 1)), -4), (2.2, ((2, 2), (1, 1)), -20)],
          seed=35792)
    for i, (x, rz) in enumerate(((-2.4, 14), (0, -4), (2.4, -16))):
        lock(g, f"nape_{i}", (x, -2.8, 4.3), (30, 0, rz), ((2, 2), (1, 1)), 1, 35795 + i)
