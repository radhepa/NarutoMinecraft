"""Topknot: the sides and back cut short, the long top gathered into a tight knot on the crown and
tied with a cord, a couple of short ends sticking up out of it."""
from anime import cel_box, ring_shell, spike, tie
from paint import scalp

META = {"name": "Topknot", "gender": "unisex",
        "description": "Short sides and back, the top gathered into a tight cord-tied knot on the crown."}


def build(g):
    scalp(g, 32895, side_rows=3, back_rows=6, sideburn=1)
    ring_shell(g, 32896, side_rows=2, back_rows=4, ring_row=1)
    knot = g.piece("knot", "HEAD", (-1.5, -3, -1.5), (3, 3, 3), pivot=(0, -8.4, .8), rotation=(-12, 0, 0))
    cel_box(knot, 32897, ring=0)
    tie(g, "cord", (0, -8.4, .8), (-12, 0, 0), size=(4, 1, 4), y=-.6, key="A2")
    for i, (x, rz) in enumerate(((-.5, -26), (.6, 22))):
        spike(g, f"end_{i}", (x, -11.2, .2), (-20, 0, rz), ((2, 1), (1, 1)), 1, 32898 + i)
