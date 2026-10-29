"""Shaggy Nape: short spiky hair on top with layered locks left long at the nape, hanging ragged to
the collar, and a few short points at the brow. A younger brother's cut."""
from anime import back_fan, bangs, ring_shell, spike
from paint import scalp

META = {"name": "Shaggy Nape", "gender": "unisex",
        "description": "Short spiky crown, long ragged layers at the nape to the collar, short brow points."}

S = ((3, 2), (2, 1), (1, 1))
CROWN = [(-2.4, -2.0, S, -18, -24), (.2, -2.4, S, -22, 6), (2.6, -1.8, S, -14, 28), (-1.4, 1.0, S, 20, -16),
         (1.6, 1.2, S, 22, 18)]
NAPE = [(-3.2, ((2, 3), (1, 2)), 20, 14), (-1.6, ((3, 3), (2, 2), (1, 1)), 8, 10), (0, ((3, 4), (2, 2), (1, 1)), 0, 8),
        (1.6, ((3, 3), (2, 2), (1, 1)), -8, 10), (3.2, ((2, 3), (1, 2)), -20, 14)]


def build(g):
    scalp(g, 1352, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 1353, side_rows=5, back_rows=8, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_spike_{i}", (x, -7.8, z), (rx, 0, rz), segs, 3, 1357 + i)
    back_fan(g, "nape", [(x, s, rz, rx) for x, s, rz, rx in NAPE], seed=1362, z=4.3)
    for i, (x, rz) in enumerate(((-4.3, 10), (4.3, -10))):
        back_fan(g, f"side_{i}", [(x, ((2, 4), (1, 2)), rz, 0)], seed=1372 + i, z=0.5)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 16), (0, ((2, 1), (1, 1)), 0), (2.4, ((2, 2), (1, 1)), -16)], seed=1377)
