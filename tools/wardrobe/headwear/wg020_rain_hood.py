"""Rain Hood: an oiled cloth hood pulled up against the weather, a stiff peak over the brow and a
cape of the same cloth falling over the back of the neck; hides the hair beneath."""
from paint import fabric, solid

META = {"name": "Rain Hood", "gender": "unisex", "hides_hair": ["*"],
        "description": "Oiled hood pulled up with a stiff peak over the brow and a neck cape at the back."}


def streaks(face):
    for x in range(1, face.w, 3):
        face.vline(x, 1, face.h - 1, "P3")
    face.hline(0, face.w - 1, face.h - 1, "P1")


def build(g):
    crown = g.piece("hood_crown", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.75)
    solid(crown, "P", "smooth", 35930, 2, edge=False)
    fabric(crown.top, "P", "smooth", 35930, 3)
    back = g.piece("hood_back", "HEAD", (-4, -6, 3), (8, 8, 1), inflate=.75)
    solid(back, "P", "smooth", 35931, 2)
    streaks(back.back)
    for side, x in (("right", -4), ("left", 3)):
        panel = g.piece(f"hood_{side}", "HEAD", (x, -6, -2.6), (1, 8, 6), inflate=.75)
        solid(panel, "P", "smooth", 35932 + (side == "left"), 2)
        streaks(panel.right if side == "right" else panel.left)
    peak = g.piece("hood_peak", "HEAD", (-5, -9.0, -5.6), (10, 1, 3))
    solid(peak, "P", "smooth", 35934, 3, edge=False)
    peak.front.fill("P1")
    for side, x in (("right", -5.0), ("left", 4.0)):
        edge = g.piece(f"hood_edge_{side}", "HEAD", (0, -8.2, -5.2), (1, 7, 2), pivot=(x, 0, 0))
        solid(edge, "P", "smooth", 35935 + (side == "left"), 1)
    cape = g.piece("hood_cape", "HEAD", (-5, 0, -1), (10, 3, 6), pivot=(0, -.6, 1.4))
    solid(cape, "P", "smooth", 35937, 2)
    streaks(cape.back)
