"""Flat Top: short hair brushed straight up and cut dead level across the top in a hard square
block, the sides tapered close."""
from anime import cel_box
from kit_morino import clipped

META = {"name": "Flat Top", "gender": "unisex",
        "description": "Hair brushed up and cut dead level in a square block, close tapered sides."}


def build(g):
    clipped(g, 17021, side_rows=5, back_rows=6, base=2, stubble=False)
    block = g.piece("block", "HEAD", (-4, -10, -4), (8, 2, 8), inflate=.4)
    cel_box(block, 17022, ring=None, top_delta=1, clump=2)
    block.top.hline(0, 7, 0, "H3")
