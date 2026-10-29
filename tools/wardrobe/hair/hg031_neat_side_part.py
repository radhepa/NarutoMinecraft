"""Neat Side Part: short hair combed from a clean side part, the fringe swept across the brow and
away from the eyes, trimmed close over the ears and at the nape: the look of a ward doctor or a
records officer, and it greys well."""
from anime import ring_shell
from kit_kurama import part_line, side_fringe
from paint import scalp

META = {"name": "Neat Side Part", "gender": "unisex",
        "description": "Short hair from a clean side part, fringe swept off the brow, trimmed ears and nape."}


def build(g):
    scalp(g, 34800, side_rows=4, back_rows=6, sideburn=2, part=2)
    ring_shell(g, 34801, side_rows=3, back_rows=6, ring_row=1)
    part_line(g, 2)
    side_fringe(g, "fringe", 34802, side=1, specs=[(-2.6, ((2, 1),), 50), (-.8, ((3, 1), (2, 1)), 62),
                                                   (1.2, ((3, 1), (2, 1)), 66), (3.2, ((2, 2), (1, 1)), 30)])
