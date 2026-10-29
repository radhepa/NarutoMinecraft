"""Long High Tail: everything gathered into one long tail tied high on the back of the crown with a
sea-blue cloth wrap, falling past the shoulder blades to the small of the back, a long side-swept
fringe ending at the brow."""
from anime import bangs, sidelocks, tie
from kit_umino import combed_up, falling_tail, knot

META = {"name": "Long High Tail", "gender": "unisex",
        "description": "One long tail tied high with a cloth wrap, falling to the small of the back, a side fringe."}

TAIL = ((4, 3), (4, 4), (3, 4), (3, 4), (2, 3), (1, 2))


def build(g):
    combed_up(g, 18141, side_rows=5, back_rows=7, sideburn=3)
    bangs(g, "fringe", [(-2.8, ((3, 2), (2, 2), (1, 1)), 34), (-.6, ((3, 2), (2, 1)), 36), (1.6, ((2, 1), (1, 1)), 24)],
          seed=18143)
    sidelocks(g, "frame", 6, seed=18145, x=4.35, z=-3.4, flare=2, width=1)
    knot(g, "tail", (0, -7.2, 4.4), rx=0)
    tie(g, "wrap", (0, -7.4, 5.4), (16, 0, 0), (4, 2, 4), y=0, key="A2")
    falling_tail(g, "tail", (0, -7.4, 5.8), TAIL, rx=16, seed=18147)
