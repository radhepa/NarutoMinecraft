"""Patrol Trousers: dark trousers bloused into tall soft boots laced up the shin, for night rounds
on wet streets and rooftops."""
from kit import footwear, legs, waistband
from paint import solid

META = {"name": "Patrol Trousers", "gender": "unisex",
        "description": "Dark trousers bloused into tall laced soft boots.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 34600)
    legs(g, "D", "twill", 34601, rows=(0, 5))
    footwear(g, "boot", top=6, role="K", base=2)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        pants = g.part(f"{side}_pants")
        for y in (7, 9):
            pants.front.hline(1, 2, y, "K3")
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 4.6, -2.5), (5, 2, 5))
        solid(puff, "D", "twill", 34603, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "D3")
