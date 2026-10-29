"""Shawl Kimono: a grandmother's winter dress, a fine-striped everyday kimono with a narrow obi and
a hand-knitted shawl laid over the shoulders, its two ends falling down the front."""
from kit_household import overlap, sash, stripes, wide_sleeves
from paint import cap, solid, strip_fabric

META = {
    "name": "Shawl Kimono",
    "gender": "unisex",
    "description": "Fine-striped kimono with a narrow obi and a knitted shawl over the shoulders, ends down the front.",
    "tags": ["civilian", "kimono", "wrap"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 37360, 2)
    cap(body, "P", texture="weave", seed=37360)
    stripes(body.strip, "P1", every=2)
    overlap(body.front, "S3", "P0", rows=8, under="S4")
    wide_sleeves(g, "sleeve", "P", "weave", 37361, top=2.6, length=7, hem="P0",
                 pattern=lambda f, rows=None: stripes(f, "P1", every=2, rows=rows), arm_rows=9)
    sash(g, "obi", "D", y=7.8, height=2, knot="back", seed=37366)
    wrap = g.piece("shawl", "TORSO", (-5, 0, -3), (10, 2, 6), pivot=(0, -.6, 0), inflate=.1)
    solid(wrap, "S", "knit", 37369, 2)
    wrap.top.rect(3, 2, 4, 2, "S0")
    back = g.piece("shawl_back", "TORSO", (-4.5, 0, 0), (9, 4, 1), pivot=(0, 1.4, 2.4))
    solid(back, "S", "knit", 37370, 2)
    back.back.hline(0, 8, 3, "S1")
    for side, x in (("right", -2.4), ("left", 2.4)):
        end = g.piece(f"shawl_end_{side}", "TORSO", (-1, 0, 0), (2, 6, 1), pivot=(x, 1.2, -3.1), motion="sway")
        solid(end, "S", "knit", 37371 + (side == "left"), 2)
        end.front.hline(0, 1, 5, "S1")
