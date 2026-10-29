"""Ember Crest: the sides kept short and a tall crest of spikes running from the brow back over the
crown like a flame, its points leaning back, with spiky tufts at the nape."""
from anime import bangs, ring_shell, spike
from kit_akimichi import flick
from paint import scalp

META = {"name": "Ember Crest", "gender": "unisex",
        "description": "Short sides and a tall crest of back-leaning spikes from brow to crown, spiky nape."}

# The crest, front to back: (z, segments, tilt x)
CREST = [(-3.0, ((4, 3), (3, 2), (2, 2), (1, 1)), -18), (-1.0, ((4, 4), (3, 2), (2, 2), (1, 1)), -30),
         (1.0, ((4, 4), (3, 3), (2, 2), (1, 1)), -44), (3.0, ((4, 3), (3, 2), (2, 1), (1, 1)), -62)]


def build(g):
    scalp(g, 6136, side_rows=3, back_rows=7, sideburn=2)
    ring_shell(g, 6136, side_rows=3, back_rows=6, ring_row=1)
    for i, (z, segs, rx) in enumerate(CREST):
        spike(g, f"crest_{i}", (0, -7.8, z), (rx, 0, 0), segs, 3, 6142 + i)
    for i, (x, rz) in enumerate(((-2.4, -26), (2.4, 26))):
        spike(g, f"crest_side_{i}", (x, -7.8, .4), (-36, 0, rz), ((3, 2), (2, 2), (1, 1)), 2, 6149 + i)
    for i, (x, rz) in enumerate(((-2.2, 26), (0, 0), (2.2, -26))):
        flick(g, f"nape_{i}", (x, -2.8, 4.1), (48, 0, rz), ((2, 2), (1, 2)), 1, 6156 + i)
    bangs(g, "fringe", [(-1.0, ((2, 2), (1, 1)), 16), (1.2, ((2, 2), (1, 1)), -16)], seed=6163)
