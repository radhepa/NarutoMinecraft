"""Fountain Tail: hair gathered right on top of the crown and tied tight, the tail springing up from
the tie and spilling back down behind the head to the shoulder blades like a fountain, a short fringe
swept to one side."""
from anime import bangs, lock
from kit_umino import combed_up, falling_tail, knot

META = {"name": "Fountain Tail", "gender": "unisex",
        "description": "Tied on top of the crown, the tail springing up and spilling down the back, a side-swept fringe."}


def build(g):
    combed_up(g, 18021, side_rows=5, back_rows=7, sideburn=2)
    bangs(g, "fringe", [(-2.6, ((3, 2), (2, 1)), 34), (-.6, ((2, 2), (1, 1)), 30), (1.6, ((2, 1), (1, 1)), 20)],
          seed=18025)
    knot(g, "crown", (0, -8.6, 1.8), rx=-60)
    lock(g, "spring", (0, -9.2, 2.4), (150, 0, 0), ((4, 2), (3, 2)), 3, 18030, ring=None)
    falling_tail(g, "tail", (0, -10.6, 4.6), ((4, 3), (4, 3), (3, 3), (2, 3), (1, 2)), rx=32, seed=18035)
