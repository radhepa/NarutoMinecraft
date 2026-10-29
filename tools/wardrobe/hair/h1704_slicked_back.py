"""Slicked Back: oiled flat and combed hard back from the brow, the ends curling out in a short
ridge at the nape."""
from anime import lock
from kit_morino import combed_back

META = {"name": "Slicked Back", "gender": "unisex",
        "description": "Oiled flat and combed hard back off the brow, a short ridge of ends at the nape."}


def build(g):
    combed_back(g, 17031, side_rows=4, back_rows=7)
    for i, x in enumerate((-3.0, -1.0, 1.0, 3.0)):
        lock(g, f"nape_{i}", (x, -1.6, 4.4), (10, 0, 0), ((2, 1), (1, 1)), 1, 17035 + i * 3, ring=None)
