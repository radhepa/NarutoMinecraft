"""Burrow Shag: shaggy layered hair, choppy over the ears and the nape, tousled like it was slept in
a mountain cave, with short wisps at the brow edges."""
from anime import back_fan, bangs, ring_shell, sidelocks
from paint import scalp

META = {"name": "Burrow Shag", "gender": "unisex",
        "description": "Shaggy choppy layers over the ears and nape, short wisps at the brow edges."}


def build(g):
    scalp(g, 23281, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 23282, side_rows=5, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.2, ((2, 3), (1, 1)), 16), (-.8, ((2, 2), (1, 1)), -10), (1.2, ((2, 2), (1, 1)), 14),
                        (3.2, ((2, 3), (1, 1)), -16)], seed=23285)
    back_fan(g, "shag", [(-3.2, ((2, 3), (1, 1)), 26, 22), (-1.6, ((2, 4), (1, 1)), 10, 16), (0, ((3, 4), (1, 2)), 0, 18),
                         (1.6, ((2, 4), (1, 1)), -10, 16), (3.2, ((2, 3), (1, 1)), -26, 22)], seed=23290)
    sidelocks(g, "frame", 5, seed=23295, x=4.4, z=-2.6, flare=10, width=2)
