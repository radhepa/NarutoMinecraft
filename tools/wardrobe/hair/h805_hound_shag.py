"""Hound Shag: a thick layered shag grown out to the neck, choppy layers stepping down the back of
the head, uneven locks over the ears and a messy fringe that just reaches the brows."""
from anime import back_fan, bangs, ring_shell, sidelocks
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Hound Shag", "gender": "unisex",
        "description": "Thick choppy layers to the neck, uneven locks over the ears, a messy fringe."}

TOP = ((3, 2), (2, 1), (1, 1))
CROWN = [(-2.0, -1.6, TOP, 8, -30), (.4, -2.0, TOP, 12, 8), (2.4, -1.2, TOP, 4, 34), (-1.0, 1.4, TOP, -30, -14),
         (1.6, 1.6, TOP, -32, 18)]
LAYERS = [(-3.4, ((2, 3), (2, 2), (1, 1)), 22, 18), (-1.7, ((3, 4), (2, 2), (1, 1)), 8, 12),
          (0, ((3, 3), (2, 3), (1, 1)), -2, 10), (1.7, ((3, 4), (2, 2), (1, 1)), -8, 12),
          (3.4, ((2, 3), (2, 2), (1, 1)), -22, 18)]


def build(g):
    scalp(g, 8121, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 8122, side_rows=6, back_rows=8, ring_row=1)
    burst(g, "crown_tuft", CROWN, 8123)
    back_fan(g, "nape", LAYERS, seed=8126, motion="sway")
    bangs(g, "fringe", [(-2.9, ((2, 3), (1, 1)), 18), (-1.4, ((2, 2), (1, 1)), 12), (0, ((2, 2), (1, 1)), -4),
                        (1.5, ((2, 2), (1, 1)), -14), (2.9, ((2, 3), (1, 1)), -20)], seed=8132)
    sidelocks(g, "sidelock", 6, seed=8136, x=4.4, z=-2.6, flare=10, width=2)
    sidelocks(g, "earlock", 5, seed=8139, x=4.5, z=.6, flare=16, width=2)
