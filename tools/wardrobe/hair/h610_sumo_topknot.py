"""Sumo Topknot: the wrestler's chonmage, the hair oiled smooth and drawn up from every side into a
tie at the back of the crown, the knot folded forward to lie along the top of the head."""
from anime import cel_box, ring_shell, tie
from paint import scalp

META = {"name": "Sumo Topknot", "gender": "unisex",
        "description": "Oiled hair drawn up into a chonmage: a knot folded forward along the crown."}


def build(g):
    scalp(g, 6901, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 6902, side_rows=5, back_rows=8, ring_row=1)
    root = g.piece("knot_root", "HEAD", (-1.5, -2, -1.5), (3, 2, 3), pivot=(0, -7.8, 2.6))
    cel_box(root, 6910, ring=0)
    tie(g, "knot_tie", (0, -9.9, 2.6), size=(3, 1, 3), key="S3")
    # The folded knot: a flat paddle lying forward on the crown, its end fanning slightly.
    fold = g.piece("knot_fold", "HEAD", (-1.5, -1, -6), (3, 2, 6), pivot=(0, -9.7, 3.2), rotation=(6, 0, 0))
    cel_box(fold, 6920, ring=0, top_delta=2)
    end = g.piece("knot_end", "HEAD", (-2, -1.2, -7.5), (4, 2, 2), pivot=(0, -9.7, 3.2), rotation=(6, 0, 0))
    cel_box(end, 6925, top_delta=1)
