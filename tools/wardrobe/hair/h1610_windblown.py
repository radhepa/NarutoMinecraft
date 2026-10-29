"""Windblown: the long-limbed messy look of a bodyguard who has been standing on a roof all day,
every lock at the back and sides blown out sideways in loose points, a scattered fringe."""
from anime import back_fan, bangs, ring_shell, sidelocks
from paint import scalp

META = {"name": "Windblown", "gender": "unisex",
        "description": "Messy collar-length hair blown out sideways in loose points, a scattered fringe."}


def build(g):
    scalp(g, 16520, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 16521, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.0, ((2, 3), (1, 1)), 30), (-1.5, ((2, 2), (1, 1)), 16), (0.3, ((2, 2),), -6),
                        (1.9, ((2, 2), (1, 1)), -20), (3.1, ((2, 3), (1, 1)), -34)], seed=16522)
    sidelocks(g, "frame", 7, seed=16530, x=4.3, z=-2.6, flare=16, width=2)
    back_fan(g, "fall", [(-3.4, ((3, 3), (2, 2), (1, 2)), 46, 10), (-1.4, ((3, 4), (2, 2), (1, 1)), 18, 8),
                         (1.4, ((3, 4), (2, 2), (1, 1)), -18, 8), (3.4, ((3, 3), (2, 2), (1, 2)), -46, 10)], seed=16540)
    sidelocks(g, "ear", 5, seed=16550, x=4.3, z=.6, flare=34, width=2)
