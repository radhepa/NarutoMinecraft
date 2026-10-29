"""Elder Topknot: a council elder's hair, combed straight back from a high clear brow and gathered
into a small wound topknot on the crown, tied with a dark cord; the sides lie flat over the ears."""
from anime import cel_box, ring_shell, tie
from paint import scalp

META = {"name": "Elder Topknot", "gender": "unisex",
        "description": "Combed straight back from a high brow into a small wound topknot on the crown."}


def build(g):
    scalp(g, 13165, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 13166, side_rows=5, back_rows=7, ring_row=2)
    tie(g, "knot_cord", (0, -8.2, 1.2), (0, 0, 0), size=(3, 1, 3), key="K2")
    knot = g.piece("knot", "HEAD", (-1.5, -3, -1.5), (3, 3, 3), pivot=(0, -8.2, 1.2), rotation=(-12, 0, 0))
    cel_box(knot, 13166, ring=0, clump=2)
    tip = g.piece("knot_tip", "HEAD", (-1, -4, -1), (2, 1, 2), pivot=(0, -8.2, 1.2), rotation=(-12, 0, 0))
    cel_box(tip, 13167, base=3, top_delta=0)
