"""Gyoja Topknot: the old chief's hermit knot, everything combed up from a high brow into a small
knot bound with cord on the crown, the long back left to hang loose to the shoulders."""
from anime import cel_box, curtain, ring_shell, sidelocks, tie
from paint import scalp

META = {"name": "Gyoja Topknot", "gender": "unisex",
        "description": "Hair combed up into a small corded knot on the crown, the back hanging loose to the shoulders."}


def build(g):
    scalp(g, 23041, side_rows=6, back_rows=8, sideburn=3)
    hat = ring_shell(g, 23042, side_rows=6, back_rows=8, ring_row=1)
    for x in (1, 3, 5):
        hat.top.vline(x, 0, 7, "H1")
    knot = g.piece("knot", "HEAD", (-1.5, -3, -1.5), (3, 3, 3), pivot=(0, -7.7, .6), rotation=(-12, 0, 0))
    cel_box(knot, 23045, ring=0, top_delta=2)
    tie(g, "knot_cord", (0, -7.7, .6), (-12, 0, 0), size=(4, 1, 4), y=-1.2, key="S3")
    curtain(g, "back", (0, -4.2, 4.6), (12, 0, 0), 7, 6, hem=((0, 2, 2), (2, 3, 3), (5, 2, 2)), seed=23050)
    sidelocks(g, "temple", 5, seed=23055, x=4.35, z=-2.4, flare=3, width=1)
