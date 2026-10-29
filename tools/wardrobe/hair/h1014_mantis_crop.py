"""Mantis Crop: a field cut kept almost to the scalp, with one short triangular point swept up at
the front like a mantis's head: nothing for an insect swarm to catch on."""
from anime import ring_shell, spike
from paint import scalp

META = {"name": "Mantis Crop", "gender": "unisex",
        "description": "Hair cut almost to the scalp, one short triangular point swept up at the front."}


def build(g):
    scalp(g, 10441, side_rows=2, back_rows=5, sideburn=1)
    ring_shell(g, 10442, side_rows=1, back_rows=4, ring_row=0)
    spike(g, "point", (0, -7.8, -2.6), (-32, 0, 0), ((5, 1), (3, 2), (1, 2)), 3, 10450)
    for i, x in enumerate((-2.6, 2.6)):
        spike(g, f"wing_{i}", (x, -7.8, -1.6), (-50, 0, x * 10), ((2, 1), (1, 1)), 2, 10455 + i)
