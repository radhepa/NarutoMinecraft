"""Half-Up Bells: shoulder-length hair with the top half gathered into a small knot at the back of
the crown, a bell sprig tied in with it, and the rest left loose to the shoulders over a gently
pointed hem, with a light fringe."""
from anime import bangs, cel_box, curtain, ring_shell, sidelocks, tie
from kit_suzuran import bell_charm
from paint import scalp

META = {"name": "Half-Up Bells", "gender": "unisex",
        "description": "Top half tied in a small crown knot with a bell sprig, the rest loose to the shoulders."}


def build(g):
    scalp(g, 24381, side_rows=7, back_rows=8, sideburn=0)
    ring_shell(g, 24382, side_rows=6, back_rows=8, ring_row=1)
    knot = g.piece("knot", "HEAD", (-1.5, -1.5, -1), (3, 3, 2), pivot=(0, -7.4, 5.0))
    cel_box(knot, 24385, ring=0)
    tie(g, "cord", (0, -7.4, 5.0), (90, 0, 0), (3, 1, 3), y=-.5, key="D2")
    bell_charm(g, "sprig", (1.0, -7.4, 6.2), rotation=(0, 180, 30))
    curtain(g, "loose", (0, -6.0, 4.5), (6, 0, 0), 9, 6, hem=((0, 3, 2), (3, 3, 3), (6, 3, 2)), seed=24390)
    sidelocks(g, "frame", 6, seed=24395, flare=3)
    bangs(g, "fringe", [(-2.4, ((3, 2), (1, 1)), 20), (0, ((3, 2), (1, 1)), 0), (2.4, ((3, 2), (1, 1)), -20)],
          seed=24400)
