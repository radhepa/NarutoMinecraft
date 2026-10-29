"""High and Tight: the sides and back clipped to stubble, a short flat pad left on top of the crown
and squared off at the brow."""
from anime import cel_box
from kit_morino import clipped

META = {"name": "High and Tight", "gender": "unisex",
        "description": "Stubble sides and back with a short flat pad on top, squared at the brow."}


def build(g):
    clipped(g, 17011, side_rows=4, back_rows=6)
    pad = g.piece("pad", "HEAD", (-3, -8.8, -3.6), (6, 1, 6), inflate=.2)
    cel_box(pad, 17012, ring=None, top_delta=1)
