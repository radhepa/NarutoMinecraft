"""Crescent Topknot: the silver hair drawn up from close sides into a knot on the crown, the ends
bursting out of it in a crescent of spikes slanting to the wearer's left, two points on the brow."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Crescent Topknot", "gender": "unisex",
        "description": "Close sides drawn up into a crown knot that bursts into a crescent of slanting spikes."}

BURST = [(-1.2, ((3, 2), (2, 2), (1, 1)), -6, -20), (0, ((3, 3), (2, 2), (1, 2)), -4, 14), (1.2, ((3, 2), (2, 2), (1, 2)), 0, 44),
         (.6, ((2, 2), (1, 2)), 18, 70), (-.6, ((2, 2), (1, 1)), -24, -46)]


def build(g):
    scalp(g, 11801, side_rows=4, back_rows=7, sideburn=1)
    ring_shell(g, 11802, side_rows=3, back_rows=6, ring_row=1)
    knot = g.piece("crown_knot", "HEAD", (-2, -2, -2), (4, 2, 4), pivot=(0, -8.2, .4))
    cel_box(knot, 11810, base=2)
    band = g.piece("crown_tie", "HEAD", (-1.5, -1, -1.5), (3, 1, 3), pivot=(0, -10.0, .4))
    cel_box(band, 11811, base=0, top_delta=0)
    for i, (x, segs, rx, rz) in enumerate(BURST):
        spike(g, f"crown_spike_{i}", (x, -10.8, .4), (rx, 0, rz), segs, 2, 11820 + i)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 28), (2.6, ((2, 2), (1, 1)), -28)], seed=11830)
    sidelocks(g, "sidelock", 4, seed=11840, x=4.4, z=-2.6, flare=6, width=1)
