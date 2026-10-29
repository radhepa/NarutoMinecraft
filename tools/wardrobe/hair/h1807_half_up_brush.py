"""Half-Up Brush: straight hair left down to the jaw at the sides and back, the top half gathered into
a small stiff brush tied on the crown, a few fringe points at the brows."""
from anime import bangs, curtain, sidelocks
from kit_umino import brush_tail, combed_up, knot

META = {"name": "Half-Up Brush", "gender": "unisex",
        "description": "Jaw-length hair left down, the top half tied in a small stiff brush on the crown."}

BRUSH = [(((2, 2), (1, 2)), 120, 0), (((2, 2), (1, 2)), 104, -24), (((2, 2), (1, 2)), 104, 24)]


def build(g):
    combed_up(g, 18121, side_rows=7, back_rows=8, sideburn=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 18), (2.6, ((2, 2), (1, 1)), -18)], seed=18123)
    sidelocks(g, "side", 7, seed=18125, x=4.4, z=-1.8, flare=4, width=2)
    curtain(g, "fall", (0, -6.4, 4.5), (6, 0, 0), 8, 4, hem=[(0, 2, 2), (3, 2, 2), (6, 2, 2)], seed=18127)
    knot(g, "brush", (0, -8.2, 2.8), rx=-50, size=(2, 1, 2))
    brush_tail(g, "brush", (0, -8.8, 3.6), BRUSH, seed=18130)
