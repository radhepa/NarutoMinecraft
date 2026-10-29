"""Field Hood: a soft hood pulled up over the head against wind and rain, open at the face, its brim
stiffened over the brow and a drawcord in the accent colour hanging at the throat."""
from paint import k, solid

META = {"name": "Field Hood", "gender": "unisex", "hides_hair": ["*"],
        "description": "Soft hood pulled up, open at the face, a stiff brim and an accent drawcord."}


def build(g):
    crown = g.piece("hood_crown", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.7)
    solid(crown, "P", "smooth", 32984, 2, edge=False)
    crown.top.vline(4, 0, 7, k("P", 1))
    for side, x in (("right", -4.75), ("left", 3.75)):
        cheek = g.piece(f"hood_{side}", "HEAD", (0, -6, -4), (1, 7, 8), pivot=(x, 0, 0), inflate=.7)
        solid(cheek, "P", "smooth", 32985, 2)
        cheek.front.vline(0, 0, 5, k("P", 3))
    back = g.piece("hood_back", "HEAD", (-4, -5, 3), (8, 6, 1), inflate=.7)
    solid(back, "P", "smooth", 32986, 2)
    back.back.vline(4, 0, 5, k("P", 1))
    brim = g.piece("hood_brim", "HEAD", (-4.5, -8.5, -5.2), (9, 1, 2), rotation=(-6, 0, 0))
    solid(brim, "P", "smooth", 32987, 3, edge=False)
    brim.front.hline(0, 8, 0, k("P", 3))
    for i, x in enumerate((-3.4, 3.4)):
        cord = g.piece(f"cord_{i}", "HEAD", (-.5, 0, -.5), (1, 3, 1), pivot=(x, .4, -4.2), scale=(.5, 1, .5), motion="sway")
        solid(cord, "A", "plain", 32988 + i, 2)
