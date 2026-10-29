"""Low Tail: the Nara matriarch's hair. A side-swept fringe and chin-length locks framing the
face, the rest gathered at the nape in a short tail that splits into stiff points."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Low Tail", "gender": "unisex",
        "description": "Side-swept fringe, chin-length framing locks, a short spiky tail low at the nape."}


def build(g):
    scalp(g, 5151, side_rows=7, back_rows=8, sideburn=1, part=5)
    ring_shell(g, 5152, side_rows=7, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 34), (-1.2, ((3, 2), (2, 1)), 40), (1.0, ((2, 2), (1, 1)), 30),
                        (3.0, ((2, 2), (1, 1)), -12)], seed=5160)
    sidelocks(g, "frame", 8, seed=5170, x=4.35, z=-3.0, flare=4, width=2)
    tie(g, "tie", (0, -2.6, 4.6), (20, 0, 0), (3, 2, 2))
    for i, (segs, rz) in enumerate(((((3, 3), (3, 2), (2, 2), (1, 1)), 0), (((2, 3), (2, 2), (1, 1)), 30),
                                    (((2, 3), (2, 2), (1, 1)), -30))):
        lock(g, f"tail_{i}", (0, -1.6, 4.9), (30, 0, rz), segs, 2, 5180 + i * 5, ring=None, motion="sway")
