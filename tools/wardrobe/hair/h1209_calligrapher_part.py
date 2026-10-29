"""Calligrapher's Part: a short, neat cut with a sharp side part, the fringe brushed across the brow in
one smooth sweep and the sides and nape kept close: the tidy look of a clan scribe."""
from anime import lock, ring_shell
from kit_kurama import part_line, side_fringe
from paint import scalp

META = {"name": "Calligrapher's Part", "gender": "unisex",
        "description": "Short and neat, a sharp side part, the top swept across in one stroke, close sides."}


def build(g):
    scalp(g, 12320, side_rows=4, back_rows=6, sideburn=2, part=2)
    ring_shell(g, 12321, side_rows=3, back_rows=5, ring_row=1)
    part_line(g, 2)
    side_fringe(g, "fringe", 12340, specs=[(-2.8, ((2, 2), (1, 1)), 30), (-.8, ((3, 2),), 40), (1.4, ((3, 1), (2, 1)), 44),
                                           (3.2, ((2, 2), (1, 1)), 20)])
    for i, x in enumerate((-2.4, 0, 2.4)):
        lock(g, f"nape_{i}", (x, -2.6, 4.3), (16, 0, 0), ((2, 1), (1, 1)), 1, 12352 + i)
