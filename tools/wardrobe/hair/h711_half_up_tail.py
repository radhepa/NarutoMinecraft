"""Half-Up Tail: the top of the hair caught in a small tail at the back of the crown, the rest let
down in a straight sheet to the shoulder blades, a side-swept fringe and long framing locks."""
from anime import bangs, curtain, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Half-Up Tail", "gender": "unisex",
        "description": "A small crown tail over hair let down to the shoulder blades, side-swept fringe."}


def build(g):
    scalp(g, 7951, side_rows=7, back_rows=8, sideburn=3)
    ring_shell(g, 7952, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "sheet", (0, -5.6, 4.5), (-6, 0, 0), 9, 11, hem=[(0, 3, 2), (3, 3, 3), (6, 3, 2)], seed=7960)
    tie(g, "tie", (0, -6.8, 4.9), (0, 0, 0), (3, 2, 2), y=-1, key="A2")
    lock(g, "crown_tail", (0, -6.8, 5.8), (10, 0, 0), ((3, 3), (2, 3), (1, 2)), 2, 7970, ring=None, motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 18), (-1.0, ((3, 2), (2, 1)), 42), (1.0, ((3, 2), (1, 1)), 46),
                        (2.8, ((2, 2), (1, 1)), -14)], seed=7980)
    sidelocks(g, "frame", 9, seed=7990, x=4.4, z=-3.4, flare=3, width=2)
