"""Infiltration Hood: a close dark hood that covers every hair and frames the face, its edge bound
in a narrow band at the brow and the cloth gathered at the nape: for night work."""
from paint import fabric, solid

META = {"name": "Infiltration Hood", "gender": "unisex", "hides_hair": ["*"],
        "description": "A close dark hood covering the hair, a bound edge at the brow, gathered at the nape."}


def build(g):
    cap = g.piece("hood", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.7)
    solid(cap, "K", "smooth", 33996, 3, edge=False)
    fabric(cap.top, "K", "smooth", 33996, 3)
    cap.front.hline(0, 7, 1, "P2")
    back = g.piece("hood_back", "HEAD", (-4, -6, 3), (8, 7, 1), inflate=.7)
    solid(back, "K", "smooth", 33997, 3)
    for name, x in (("right", -4.0), ("left", 3.0)):
        side = g.piece(f"hood_{name}", "HEAD", (x, -6, -3.4), (1, 7, 7), inflate=.7)
        solid(side, "K", "smooth", 33998, 3)
        (side.right if name == "right" else side.left).vline(0, 0, 6, "P2")
    gather = g.piece("hood_gather", "HEAD", (-2, 0, 0), (4, 2, 1), pivot=(0, .2, 4.4))
    solid(gather, "K", "smooth", 33999, 2)
