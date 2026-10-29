"""Sai Sleek: Sai's short, straight, ink-black hair: smooth and close to the head, a neat fringe
brushed down to the brows in fine points and the sides trimmed over the tops of the ears."""
from anime import bangs, cel_box, ring_shell
from paint import scalp

META = {"name": "Sai Sleek", "gender": "unisex",
        "description": "Short straight sleek hair, a neat pointed fringe to the brows, trimmed sides."}


def build(g):
    scalp(g, 13066, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 13067, side_rows=5, back_rows=7, ring_row=1)
    crown = g.piece("crown", "HEAD", (-4.5, -8.5, -4.5), (9, 1, 9))
    cel_box(crown, 13067, ring=0, clump=4)
    for side, x in (("right", -4.55), ("left", 3.55)):
        wall = g.piece(f"side_{side}", "HEAD", (x, -7.6, -4.2), (1, 4, 8))
        cel_box(wall, 13068 + (x > 0), ring=0, clump=4)
    back = g.piece("back", "HEAD", (-4.5, -7.6, 3.55), (9, 5, 1))
    cel_box(back, 13069, ring=1, clump=4)
    bangs(g, "fringe", [(-3.4, ((2, 3), (1, 1)), 4), (-1.5, ((2, 2), (1, 1)), 4), (0, ((2, 2), (1, 1)), 0),
                        (1.5, ((2, 2), (1, 1)), -4), (3.4, ((2, 3), (1, 1)), -4)], seed=13072)
