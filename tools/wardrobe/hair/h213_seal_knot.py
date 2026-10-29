"""Seal Knot: half up, half down: the top hair drawn back into a small knot at the crown, bound with
a paper seal tag, and the rest hanging straight to the shoulder blades; swept bangs and face locks."""
from anime import bangs, cel_box, curtain, ring_shell, sidelocks
from kit_uzumaki import wrap_tie
from paint import scalp

META = {"name": "Seal Knot", "gender": "unisex",
        "description": "Half-up knot bound with a seal tag, straight hair to the shoulder blades, swept bangs."}


def build(g):
    scalp(g, 2185, side_rows=7, back_rows=8, sideburn=4)
    ring_shell(g, 2186, side_rows=7, back_rows=8, ring_row=1)
    curtain(g, "curtain", (0, -4.6, 4.6), (-6, 0, 0), 9, 9, [(0, 3, 2), (3, 3, 3), (6, 3, 2)], seed=2187)
    knot = g.piece("knot", "HEAD", (-1.5, -3, -1.5), (3, 3, 3), pivot=(0, -7.2, 5.2), rotation=(30, 0, 0))
    cel_box(knot, 2188, 3, ring=None, top_delta=1)
    wrap_tie(g, "tag_band", (0, -7.2, 5.2), (30, 0, 0), (4, 1, 4), y=-1.6, key="S", tag=True)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 26), (-1.2, ((2, 2), (1, 1)), 26), (.4, ((2, 1), (1, 1)), 22),
                        (2.2, ((2, 2), (1, 1)), -12)], seed=2189)
    sidelocks(g, "frame", 11, seed=2190, x=4.3, z=-3.4, flare=3, width=2)
