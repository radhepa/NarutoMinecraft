"""Long Low Tail: the elder sister's way, long brown hair parted off-centre with a rough fringe,
two long face-framing locks to the collarbone and the length tied low at the nape in a tail that
ends in ragged points."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Long Low Tail", "gender": "unisex",
        "description": "Long hair with a rough fringe, long framing locks and a low ponytail with ragged ends."}


def build(g):
    scalp(g, 8061, side_rows=6, back_rows=8, sideburn=4, part=5)
    ring_shell(g, 8062, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 22), (-1.2, ((2, 2), (1, 1)), 16), (.6, ((2, 1), (1, 1)), 10),
                        (2.6, ((2, 2), (1, 1)), -20)], seed=8069)
    sidelocks(g, "frame", 11, seed=8072, x=4.3, z=-3.4, flare=3, width=2)
    tie(g, "tie", (0, -1.2, 4.7), size=(3, 1, 2), key="A2")
    lock(g, "ponytail", (0, -.4, 4.8), (12, 0, 0), ((3, 4), (3, 4), (3, 3), (2, 2), (1, 2)), 2, 8072, ring=None,
         motion="sway")
