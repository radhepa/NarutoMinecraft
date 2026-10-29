"""Iruka Tail: the Umino signature. Dark hair combed straight up and back off the brow, tied high on
the back of the crown in a short stiff brush of a ponytail that stands out behind the head and
flicks up at the ends, short sideburns at the temples."""
from kit_umino import brush_tail, combed_up, knot

META = {"name": "Iruka Tail", "gender": "unisex",
        "description": "Combed up and back, tied high in a short stiff brush of a tail standing out behind the head."}

LONG = ((3, 3), (3, 2), (2, 2), (1, 2))
MID = ((3, 2), (2, 2), (1, 2))
# (segments, rx, rz): rx 90 stands straight out behind, more lifts the brush up and back.
LOCKS = [(LONG, 108, 0), (LONG, 100, -24), (LONG, 100, 24), (MID, 84, -36), (MID, 84, 36), (LONG, 122, -12),
         (LONG, 122, 12), (MID, 78, 0)]
UP = [(((2, 3), (1, 2)), -64, -20), (((2, 3), (1, 2)), -60, 22)]


def build(g):
    combed_up(g, 18001, side_rows=4, back_rows=6, sideburn=3)
    knot(g, "tail", (0, -7.4, 4.4), rx=-30)
    brush_tail(g, "tail", (0, -7.8, 5.6), LOCKS, seed=18010, up=UP)
