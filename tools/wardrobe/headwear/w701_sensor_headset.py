"""Sensor Headset: the Yamanaka sensor corps' headset, a slim band over the crown joining two ear
cups lit in aqua, and a short antenna rising from the left cup to carry the mind-link."""
from paint import solid

META = {"name": "Sensor Headset", "gender": "unisex",
        "description": "Slim crown band joining aqua-lit ear cups, a short antenna on the left."}


def build(g):
    for side, sign in (("right", -1), ("left", 1)):
        cup = g.piece(f"{side}_cup", "HEAD", (-1, -1.5, -1.5), (2, 3, 3), pivot=(5.0 * sign, -3.8, .4))
        solid(cup, "K", "smooth", 7710 + (sign > 0), 2)
        outer = cup.left if sign > 0 else cup.right
        outer.fill("M2"), outer.set(1, 1, "A3")
        arm = g.piece(f"{side}_arm", "HEAD", (-.5, -4, -.5), (1, 4, 1), pivot=(5.1 * sign, -5.2, .4))
        solid(arm, "M", "plain", 7712, 3)
    band = g.piece("band", "HEAD", (-5.5, -1, -.5), (11, 1, 1), pivot=(0, -9.0, .4))
    solid(band, "M", "plain", 7713, 3)
    band.top.hline(4, 6, 0, "A3")
    antenna = g.piece("antenna", "HEAD", (-.5, -5, -.5), (1, 5, 1), pivot=(5.4, -4.6, 1.6), rotation=(-16, 0, -14))
    solid(antenna, "K", "smooth", 7714, 2)
    tip = g.piece("antenna_tip", "HEAD", (-.5, -6, -.5), (1, 1, 1), pivot=(5.4, -4.6, 1.6), rotation=(-16, 0, -14))
    solid(tip, "A", "plain", 7715, 3, edge=False)
