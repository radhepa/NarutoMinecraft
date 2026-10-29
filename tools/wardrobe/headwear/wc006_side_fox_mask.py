"""Side Fox Mask: a painted paper fox mask from a festival stall, white with red brows and cheek
flicks, pointed ears and a little snout, pushed round to the side of the head on a red cord the
way children and festival-goers wear them, so the face stays clear."""
from kit_household import HALF
from glyphs import stamp
from paint import fabric, solid

META = {"name": "Side Fox Mask", "gender": "unisex",
        "description": "White festival fox mask with red markings worn on the side of the head on a red cord."}

LEGEND = {"4": "S4", "3": "S3", "2": "S2", "A": "A2", "a": "A3", "K": "K0"}
FOX = ["4444444444",
       "3333333333",
       "3aA3333Aa3",
       "3333333333",
       "3KK3333KK3",
       "33KK33KK33",
       "3333333333",
       "3A333333A3",
       "3AA3333AA3",
       "3333KK3333",
       "3333333333",
       "2222222222"]
SIDE = dict(pivot=(5.35, -7.6, .4), rotation=(0, -90, 6))


def build(g):
    plate = g.piece("mask", "HEAD", (-5, 0, -1), (10, 12, 1), scale=HALF, **SIDE)
    for f in plate.faces:
        fabric(f, "S", "plain", 37900, 3)
    stamp(plate.front, FOX, 0, 0, LEGEND)
    snout = g.piece("mask_snout", "HEAD", (-1.5, 6, -3), (3, 3, 2), scale=HALF, **SIDE)
    solid(snout, "S", "plain", 37901, 3, edge=False)
    snout.front.hline(0, 2, 0, "K0"), snout.top.hline(0, 2, 0, "A2")
    for i, x in enumerate((-3.5, 2.0)):
        ear = g.piece(f"mask_ear_{i}", "HEAD", (x, -3, -1), (2, 3, 1), scale=HALF, **SIDE)
        solid(ear, "S", "plain", 37902 + i, 3, edge=False)
        ear.front.set(0 if i == 0 else 1, 1, "A2"), ear.front.set(0 if i == 0 else 1, 2, "A2")
    back = g.piece("cord_back", "HEAD", (-4.5, 0, 0), (9, 1, 1), pivot=(0, -6.4, 4.25))
    side = g.piece("cord_side", "HEAD", (0, 0, -4.5), (1, 1, 9), pivot=(-4.3, -6.4, 0), rotation=(0, 0, 0))
    for cord in (back, side):
        solid(cord, "A", "weave", 37904, 2, edge=False)
