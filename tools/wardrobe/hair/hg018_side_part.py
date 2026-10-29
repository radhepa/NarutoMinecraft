"""Side Part: a neat short cut parted on the left, the top combed across to the right in a soft wave
that stops above the brow, the sides tidy over the ears."""
from anime import bangs, ring_shell
from paint import scalp

META = {"name": "Side Part", "gender": "unisex",
        "description": "Neat short cut parted on the left, the top combed across in a soft wave above the brow."}


def build(g):
    scalp(g, 32910, side_rows=4, back_rows=7, sideburn=2, part=5)
    ring_shell(g, 32911, side_rows=3, back_rows=6, ring_row=1)
    bangs(g, "sweep", [(1.6, ((3, 1), (2, 1)), 70), (0.0, ((3, 1), (2, 1)), 72), (-1.8, ((3, 1), (2, 1)), 74),
                       (-3.4, ((2, 2), (1, 1)), 30)], seed=32912)
