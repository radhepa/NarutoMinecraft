"""Layered Nape: soft layers to the base of the neck, flicking outward at the ends, a long fringe
swept to one side to the brows and a short lock tucked before each ear."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Layered Nape", "gender": "unisex",
        "description": "Soft layers to the neck flicking out at the ends, long side-swept fringe, short ear locks."}


def build(g):
    scalp(g, 25280, side_rows=7, back_rows=8, sideburn=3, part=-2)
    ring_shell(g, 25281, side_rows=7, back_rows=8, ring_row=1)
    spike(g, "crown", (-.6, -7.8, .4), (20, 0, 12), ((3, 1), (2, 1)), 3, 25282)
    bangs(g, "fringe", [(-2.9, ((3, 2), (2, 1)), -16), (-1.0, ((3, 1), (2, 1)), -40),
                        (1.2, ((3, 1), (2, 1)), -46), (3.0, ((2, 2), (1, 1)), -20)], seed=25284)
    sidelocks(g, "ear", 6, seed=25288, x=4.35, z=-2.6, flare=6, width=2)
    back_fan(g, "nape", [(-3.1, ((3, 5), (2, 2), (1, 1)), 14, 6), (-1.0, ((3, 6), (2, 1)), 8, 6),
                         (1.0, ((3, 6), (2, 1)), -8, 6), (3.1, ((3, 5), (2, 2), (1, 1)), -14, 6)], seed=25292)
