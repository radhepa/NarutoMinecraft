"""Top Knot: all the hair drawn up tight from the brow and the nape into a neat knot on the crown,
bound with a dark cord, short at the temples: an instructor's or a guard's no-nonsense knot."""
from anime import ring_shell, tie
from kit_kurama import bun
from kit_nara import pulled_back

META = {"name": "Top Knot", "gender": "unisex",
        "description": "Hair drawn tight from brow and nape into a corded knot on the crown."}


def build(g):
    pulled_back(g, 34810, side_rows=4, back_rows=7, sideburn=2)
    bun(g, "crown_knot", (0, -9.4, .6), size=4, seed=34812)
    tie(g, "crown_cord", (0, -8.6, .6), size=(3, 1, 3), y=-.4, key="K1")
