"""Elder Topknot: thinning hair combed straight back to a small stubby topknot on the crown, the
temples gone grey-thin, short sides: a retired Academy head."""
from anime import cel_box, spike
from kit_umino import combed_up, knot

META = {"name": "Elder Topknot", "gender": "unisex",
        "description": "Thinning hair combed back to a small stubby topknot on the crown, short sides."}


def build(g):
    combed_up(g, 18261, side_rows=3, back_rows=6, sideburn=3)
    knot(g, "knot", (0, -8.2, 1.6), rx=-70, size=(2, 1, 2))
    stub = g.piece("stub", "HEAD", (-1, -3, -1), (2, 3, 2), pivot=(0, -8.6, 1.8), rotation=(-30, 0, 0))
    cel_box(stub, 18263, base=2)
    spike(g, "stub_tip", (0, -10.8, 2.6), (-50, 0, 0), ((2, 1), (1, 1)), 2, 18265)
