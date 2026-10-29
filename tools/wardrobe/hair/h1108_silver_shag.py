"""Silver Shag: a loose shag of short silver spikes standing out all round the head, as if never
combed since the Academy, ragged points over the brow and ears."""
from anime import bangs, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Silver Shag", "gender": "unisex",
        "description": "Short silver spikes standing out all round the head, ragged brow points and ear tufts."}

S = ((3, 2), (2, 1), (1, 1))
M = ((3, 2), (2, 2), (1, 1))
# Spikes radiating from the crown in every direction, a little tipped to the wearer's left.
CROWN = [(-2.6, -2.6, M, -36, -30), (0, -2.8, M, -40, 6), (2.6, -2.6, M, -34, 40),
         (-3.0, 0, S, 0, -54), (3.0, 0, S, 0, 60), (-1.4, 0, M, 4, -10), (1.4, 0, M, 6, 20),
         (-2.4, 2.8, M, 44, -30), (0, 3.0, M, 50, 6), (2.4, 2.8, M, 44, 40)]


def build(g):
    scalp(g, 11701, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 11702, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.6, z), (rx, 0, rz), segs, 3, 11710 + i)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 26), (-1.0, ((2, 2), (1, 1)), 10), (.9, ((2, 2), (1, 1)), -10),
                        (2.7, ((2, 2), (1, 1)), -26)], seed=11730)
    sidelocks(g, "tuft", 5, seed=11740, x=4.4, z=-2.0, flare=22, width=2)
    sidelocks(g, "back_tuft", 4, seed=11745, x=4.4, z=1.6, flare=28, width=2)
    for i, (x, rz, rx) in enumerate(((-2.8, 30, 44), (0, 0, 52), (2.8, -30, 44))):
        lock(g, f"nape_{i}", (x, -3.4, 4.3), (rx, 0, rz), ((2, 2), (1, 1)), 1, 11750 + i * 5)
