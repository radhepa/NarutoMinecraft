"""Low Tail: long hair with a fringe swept to one side above the brow, the length gathered low at the
nape in a cloth wrap and hanging in a long tail between the shoulder blades."""
from anime import bangs, lock, ring_shell, tie
from paint import scalp

META = {"name": "Low Tail", "gender": "unisex",
        "description": "Side-swept fringe, the length wrapped low at the nape into a long tail down the back."}


def build(g):
    scalp(g, 32845, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 32846, side_rows=5, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((3, 2), (2, 1)), 34), (-1.0, ((3, 2), (1, 1)), 38), (1.0, ((2, 1), (1, 1)), 30)],
          seed=32847)
    tie(g, "wrap", (0, -1.4, 4.7), (8, 0, 0), size=(3, 2, 2), key="D2")
    lock(g, "tail", (0, -.6, 4.9), (8, 0, 0), ((3, 4), (3, 4), (2, 3), (1, 2)), 2, 32850, ring=None, motion="sway")
