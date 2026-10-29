"""Jinbei Shorts: the knee shorts of a summer jinbei, loose crepe with a narrow stripe and an
elastic waist, worn barefoot in wooden geta on the veranda and at the festival."""
from kit_household import geta, stripes, trouser_legs, waist
from paint import solid

META = {"name": "Jinbei Shorts", "gender": "unisex",
        "description": "Loose striped crepe knee shorts with an elastic waist, wooden geta.",
        "tags": ["civilian", "casual", "shorts"]}


def build(g):
    body = waist(g, "P", "plain", 37580, band="P1")
    stripes(body.strip, "P3", every=3, rows=range(9, 12))
    for leg in trouser_legs(g, "P", "plain", 37581, rows=(0, 4)):
        stripes(leg.strip, "P3", every=3, rows=range(0, 5))
    geta(g, strap="A2")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        hem = g.piece(f"{side}_hem", bone, (-2.5, 3.2, -2.5), (5, 2, 5))
        solid(hem, "P", "plain", 37583, 2)
        for face in hem.sides:
            stripes(face, "P3", every=3)
            face.hline(0, face.w - 1, 1, "P1")
