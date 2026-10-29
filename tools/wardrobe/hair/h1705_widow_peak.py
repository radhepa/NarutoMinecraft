"""Widow's Peak: combed straight back from a sharp point on the brow, the temples bare and the
sides swept close behind the ears."""
from kit_morino import combed_back, nape_hem

META = {"name": "Widow's Peak", "gender": "unisex",
        "description": "Combed straight back from a sharp point on the brow, bare temples, close sides."}


def build(g):
    hat = combed_back(g, 17041, side_rows=3, back_rows=6, sideburn=0)
    nape_hem(g, 17045, y=-2.0)
    head = g.part("head")
    for x in (0, 1, 6, 7):
        head.front.clear(x, 0), head.front.clear(x, 1)
    hat.front.set(3, 1, "H2"), hat.front.set(4, 1, "H2")
    hat.front.set(3, 2, "H1"), hat.front.set(4, 2, "H1")
