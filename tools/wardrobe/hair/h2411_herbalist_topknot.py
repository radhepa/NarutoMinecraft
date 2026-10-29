"""Herbalist Topknot: the old herb-masters' style, hair drawn up smooth from every side into a tight
topknot on the crown bound with a green cord, a short sprig of bells pinned through it, and a
clean hairline."""
from anime import cel_box, ring_shell, tie
from kit_suzuran import bell_charm
from paint import scalp

META = {"name": "Herbalist Topknot", "gender": "unisex",
        "description": "Hair drawn up smooth into a tight crown topknot with a green cord and a bell sprig."}


def build(g):
    scalp(g, 24281, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 24282, side_rows=3, back_rows=6, ring_row=1)
    knot = g.piece("knot", "HEAD", (-1.5, -3, -1.5), (3, 3, 3), pivot=(0, -8.2, .8))
    cel_box(knot, 24285, ring=0)
    tuft = g.piece("tuft", "HEAD", (-1, -2, -1), (2, 2, 2), pivot=(0, -11.2, 1.0), rotation=(-20, 0, 0))
    cel_box(tuft, 24286, top_delta=1)
    tie(g, "cord", (0, -8.2, .8), (0, 0, 0), (4, 1, 4), y=-1.4, key="D2")
    bell_charm(g, "sprig", (-1.6, -10.4, -.6), rotation=(0, 0, -20))
