"""Half-Moon Knot: the top half of shoulder-length hair gathered into a small flat knot at the back of
the crown, the rest left down over the nape, a centre-parted fringe drawn aside."""
from anime import back_fan, bangs, cel_box, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Half-Moon Knot", "gender": "unisex",
        "description": "Half-up flat knot at the back of the crown, the rest down to the shoulders, parted fringe."}


def build(g):
    scalp(g, 25240, side_rows=7, back_rows=8, sideburn=3, part=0)
    ring_shell(g, 25241, side_rows=7, back_rows=8, ring_row=1)
    knot = g.piece("knot", "HEAD", (-2, -1.5, 0), (4, 3, 2), pivot=(0, -6.6, 4.3), rotation=(-20, 0, 0))
    cel_box(knot, 25242, ring=1)
    tie(g, "knot_cord", (0, -6.6, 4.3), (-20, 0, 0), size=(2, 3, 1), y=-1.5, key="K2")
    bangs(g, "fringe", [(-2.7, ((3, 2), (2, 1)), 34), (-1.0, ((2, 1), (1, 1)), 46),
                        (1.0, ((2, 1), (1, 1)), -46), (2.7, ((3, 2), (2, 1)), -34)], seed=25244)
    sidelocks(g, "frame", 8, seed=25248, x=4.3, z=-3.3, flare=3, width=2)
    back_fan(g, "nape", [(-3.0, ((3, 7), (2, 1), (1, 1)), 6, 4), (0, ((3, 8), (2, 1)), 0, 4),
                         (3.0, ((3, 7), (2, 1), (1, 1)), -6, 4)], seed=25252)
