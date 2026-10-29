"""Receding Crop: an older interrogator's cut, the hairline gone back high at both temples and the
rest clipped short and grizzled."""
from kit_morino import nape_hem
from paint import scalp, shell


META = {"name": "Receding Crop", "gender": "unisex",
        "description": "Hairline gone back high at both temples, the rest clipped short."}


def build(g):
    nape_hem(g, 17155, y=-2.6)
    scalp(g, 17151, side_rows=4, back_rows=6, sideburn=1, shadow=False)
    shell(g, 17152, side_rows=2, back_rows=5, sheen=None)
    head, hat = g.part("head"), g.part("hat")
    for x in range(8):
        head.front.clear(x, 0)
    # Bare temples: the front of the crown cleared in an M.
    for x, rows in ((0, 3), (1, 3), (2, 2), (3, 1), (4, 1), (5, 2), (6, 3), (7, 3)):
        for y in range(rows):
            head.top.clear(x, 7 - y), hat.top.clear(x, 7 - y)
    for x in range(8):
        hat.front.clear(x, 0)
