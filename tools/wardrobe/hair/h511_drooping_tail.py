"""Drooping Tail: a long-haired Nara's tail, tied high on the crown in the clan's spiky burst but
long enough that the weight of it droops down the back of the head to a fan of points."""
from anime import bangs, lock, sidelocks
from kit_nara import pulled_back
from anime import tie

META = {"name": "Drooping Tail", "gender": "unisex",
        "description": "Tied high in a spiky burst, the long tail drooping down the back to a fan of points."}


def build(g):
    pulled_back(g, 5601, side_rows=4, back_rows=7, sideburn=2)
    pivot = (0, -7.6, 4.4)
    tie(g, "tie", pivot, (-20, 0, 0), (3, 2, 3), y=-1)
    lock(g, "tail", pivot, (24, 0, 0), ((4, 3), (4, 3), (3, 3)), 3, 5610, ring=None, motion="sway", y0=.5)
    for i, rz in enumerate((-34, -12, 12, 34)):
        lock(g, f"fan_{i}", (0, -7.6 + 9 * .91, 4.4 + 9 * .41), (24, 0, rz), ((2, 2), (1, 2)), 2, 5630 + i * 5,
             ring=None, motion="sway")
    for i, (rx, rz) in enumerate(((-40, -20), (-40, 20), (-60, 0))):
        lock(g, f"burst_{i}", pivot, (180 + rx, 0, rz), ((2, 2), (1, 1)), 2, 5650 + i * 5, ring=None)
    sidelocks(g, "frame", 6, seed=5670, x=4.35, z=-3.0, flare=5, width=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 22), (2.9, ((2, 2), (1, 1)), -22)], seed=5680)
