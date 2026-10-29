"""Windswept Tail: a high tail caught by the sea wind, streaming out sideways off the back of the
crown, loose fringe locks blown the same way."""
from anime import bangs, lock
from kit_umino import combed_up, knot

META = {"name": "Windswept Tail", "gender": "unisex",
        "description": "A high tail streaming sideways in the wind, loose fringe locks blown the same way."}

TAIL = ((4, 3), (3, 3), (3, 3), (2, 2), (1, 2))


def build(g):
    combed_up(g, 18301, side_rows=5, back_rows=7, sideburn=2)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 40), (-1.0, ((3, 2), (1, 1)), 44), (1.0, ((2, 2), (1, 1)), 40)],
          seed=18303)
    knot(g, "tail", (0, -7.4, 4.4), rx=-10)
    lock(g, "tail", (.4, -7.6, 5.4), (60, 0, 62), TAIL, 3, 18305, ring=None, motion="sway")
    lock(g, "tail_wisp", (.4, -7.6, 5.4), (80, 0, 40), ((2, 3), (1, 3)), 1, 18310, ring=None)
