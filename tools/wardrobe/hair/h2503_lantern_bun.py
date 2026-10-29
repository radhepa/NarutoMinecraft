"""Lantern Bun: hair drawn up into a round bun on the crown, bound with an amber cord the way the
lantern-keepers tie the paper lanterns, a short side fringe and wisps left loose before the ears."""
from anime import bangs, cel_box, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Lantern Bun", "gender": "unisex",
        "description": "Round bun high on the crown bound with an amber cord, side fringe, loose wisps."}


def build(g):
    scalp(g, 25040, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 25041, side_rows=6, back_rows=8, ring_row=1)
    bun = g.piece("bun", "HEAD", (-2, -4, -2), (4, 4, 4), pivot=(0, -7.6, 1.6), rotation=(-12, 0, 0))
    cel_box(bun, 25042, ring=1)
    tie(g, "bun_cord", (0, -7.6, 1.6), (-12, 0, 0), size=(5, 1, 5), y=-.6, key="A2")
    knot = g.piece("bun_knot", "HEAD", (-1, -1.5, -1), (2, 2, 2), pivot=(0, -11.4, 2.4), rotation=(-12, 0, 0))
    cel_box(knot, 25043, base=3, top_delta=0)
    bangs(g, "fringe", [(-2.8, ((3, 2), (2, 1), (1, 1)), 26), (-.8, ((3, 1), (2, 1)), 40), (2.6, ((2, 2), (1, 1)), -16)],
          seed=25044)
    sidelocks(g, "wisp", 7, seed=25047, x=4.35, z=-3.0, flare=5, width=1)
