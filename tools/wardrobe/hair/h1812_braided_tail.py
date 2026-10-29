"""Braided Tail: hair tied high on the back of the crown and plaited into a single braid that hangs to
the shoulder blades, a short fringe parted to the side and short sideburns."""
from anime import bangs, braid
from kit_umino import combed_up, knot

META = {"name": "Braided Tail", "gender": "unisex",
        "description": "Tied high on the crown and plaited into one braid to the shoulder blades, a side fringe."}


def build(g):
    combed_up(g, 18241, side_rows=5, back_rows=7, sideburn=3)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 26), (-.8, ((2, 2), (1, 1)), 22), (2.8, ((1, 2), (1, 1)), -10)],
          seed=18243)
    knot(g, "tail", (0, -7.2, 4.4), rx=0)
    braid(g, "braid", (0, -6.4, 5.4), (14, 0, 0), links=6, width=3, seed=18245)
