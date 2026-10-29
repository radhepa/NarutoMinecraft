"""Child's Cut: the rounded cut mothers give at home, short all round with a straight fringe
trimmed at the brows, the nape cut close and one stubborn tuft standing up on the crown."""
from anime import bangs, lock, ring_shell
from paint import scalp

META = {"name": "Child's Cut", "gender": "unisex",
        "description": "Rounded home cut, straight fringe at the brows, close nape and one tuft standing up on the crown."}


def build(g):
    scalp(g, 37985, side_rows=5, back_rows=7, sideburn=1)
    ring_shell(g, 37986, side_rows=4, back_rows=6, ring_row=1)
    bangs(g, "fringe", [(-3.0, ((2, 2),), 6), (-1.0, ((2, 2),), 2), (1.0, ((2, 2),), -2), (3.0, ((2, 2),), -6)],
          seed=37987)
    lock(g, "tuft", (.6, -8.4, .4), (160, 0, -12), ((2, 2), (1, 1)), 1, 37988)
