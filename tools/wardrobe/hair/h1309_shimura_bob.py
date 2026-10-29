"""Shimura Bob: straight dark hair cut in a blunt line at the jaw all round, a straight fringe to
the brows, an ordinary village look among the clan's grey and ink."""
from anime import bangs, cel_box, ring_shell
from paint import scalp

META = {"name": "Shimura Bob", "gender": "unisex", "description": "Blunt jaw-length bob, a straight fringe to the brows."}


def build(g):
    scalp(g, 13264, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 13265, side_rows=8, back_rows=8, ring_row=1)
    for side, x in (("right", -4.7), ("left", 3.7)):
        wall = g.piece(f"side_{side}", "HEAD", (x, -7.8, -3.6), (1, 9, 8))
        cel_box(wall, 13265 + (x > 0), ring=1, clump=3)
    back = g.piece("back", "HEAD", (-4.5, -7.8, 3.7), (9, 9, 1))
    cel_box(back, 13267, ring=1, clump=3)
    front = g.piece("fringe_bar", "HEAD", (-4.5, -8.4, -4.6), (9, 2, 1))
    cel_box(front, 13267, ring=0, clump=3)
    bangs(g, "fringe", [(-2.4, ((2, 2),), 0), (-.8, ((2, 2),), 0), (.8, ((2, 2),), 0), (2.4, ((2, 2),), 0)], seed=13270)
