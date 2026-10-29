"""Merchant Topknot: hair drawn up from close-cut sides into a short folded topknot on the crown,
tied with a cloth cord, the brow left clear and short sideburns."""
from anime import cel_box, ring_shell, tie
from paint import scalp

META = {"name": "Merchant Topknot", "gender": "unisex",
        "description": "Close sides drawn up into a short folded topknot on the crown, tied with a cord."}


def build(g):
    scalp(g, 19401, side_rows=4, back_rows=6, sideburn=3)
    ring_shell(g, 19402, side_rows=3, back_rows=5, ring_row=1)
    base = g.piece("knot_base", "HEAD", (-1.5, -2, -1.5), (3, 2, 3), pivot=(0, -8.0, .6))
    cel_box(base, 19405, base=2)
    tie(g, "cord", (0, -9.4, .6), (0, 0, 0), (3, 1, 3), y=-.5, key="A2")
    fold = g.piece("knot_fold", "HEAD", (-1, -1, -3), (2, 2, 4), pivot=(0, -10.0, 1.2), rotation=(-20, 0, 0))
    cel_box(fold, 19407, base=2, ring=0)
