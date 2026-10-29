"""Proctor's Cut: Hayate Gekko's short brown hair, a little too long for a soldier, falling in loose
uneven strands over the brow and to the collar at the back, short points over the cheekbones. Flat
enough on the crown that a bandana ties down over it."""
from anime import back_fan, bangs, ring_shell, sidelocks
from paint import scalp

META = {"name": "Proctor's Cut", "gender": "unisex",
        "description": "Short brown hair in loose uneven strands to the brow, cheek points, collar-length nape."}


def build(g):
    scalp(g, 15010, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 15011, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.0, ((2, 3), (1, 1)), 14), (-1.5, ((2, 2), (1, 1)), 6), (0.2, ((2, 2), (1, 1)), -8),
                        (1.8, ((2, 2), (1, 1)), -16), (3.1, ((2, 3), (1, 1)), -10)], seed=15020)
    sidelocks(g, "cheek", 5, seed=15030, x=4.3, z=-3.2, flare=6, width=2)
    back_fan(g, "nape", [(-2.7, ((3, 2), (2, 1), (1, 1)), 14, 12), (0, ((3, 3), (2, 1), (1, 1)), 0, 10),
                         (2.7, ((3, 2), (2, 1), (1, 1)), -14, 12)], seed=15040)
