"""Tide Spikes: short red spikes all swept back from the brow like a breaking wave, rising highest
at the crown and curling out at the nape, with a few short points over the forehead."""
from anime import bangs, lock, ring_shell, spike
from paint import scalp

META = {"name": "Tide Spikes", "gender": "unisex",
        "description": "Short spikes swept back like a breaking wave, short points over the brow."}

WAVE = ((4, 3), (3, 2), (2, 2), (1, 1))
CROWN = [(-2.4, -2.8, ((4, 2), (3, 2), (1, 1)), -58, -16), (0, -3.0, ((4, 2), (3, 2), (1, 1)), -60, 0),
         (2.4, -2.8, ((4, 2), (3, 2), (1, 1)), -58, 16), (-2.6, -.2, WAVE, -72, -18), (0, -.4, WAVE, -76, 0),
         (2.6, -.2, WAVE, -72, 18), (-1.4, 2.4, WAVE, -86, -10), (1.4, 2.4, WAVE, -86, 10)]


def build(g):
    scalp(g, 2070, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 2071, side_rows=4, back_rows=6, ring_row=1)
    for i, (x, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crest_{i}", (x, -7.7, z), (rx, 0, rz), segs, 3, 2072 + i)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 24), (0, ((2, 1), (1, 1)), 0), (2.4, ((2, 2), (1, 1)), -24)], seed=2081)
    for side, sign in (("right", -1), ("left", 1)):
        for i, (y, z) in enumerate(((-6.6, -1.6), (-5.6, .8))):
            lock(g, f"side_{side}_{i}", (4.3 * sign, y, z), (20, 0, -60 * sign), ((2, 2), (1, 1)), 1, 2083 + i, ring=0)
    for i, (x, rz) in enumerate(((-2.6, 40), (0, 0), (2.6, -40))):
        lock(g, f"nape_{i}", (x, -3.0, 4.3), (62, 0, rz), ((2, 2), (1, 2)), 1, 2088 + i * 3, ring=None)
