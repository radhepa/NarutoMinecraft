"""Side Part: a neat, short regulation cut parted hard on the left and combed flat, the sides
trimmed above the ears."""
from kit_morino import nape_hem
from paint import scalp, shell


META = {"name": "Side Part", "gender": "unisex",
        "description": "Short regulation cut with a hard left part, combed flat, trimmed above the ears."}


def build(g):
    nape_hem(g, 17095, y=-2.6)
    scalp(g, 17091, side_rows=4, back_rows=6, sideburn=1, part=5)
    shell(g, 17092, side_rows=3, back_rows=5, sheen=1, front=[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)])
    g.part("hat").top.vline(5, 0, 7, "H0")
