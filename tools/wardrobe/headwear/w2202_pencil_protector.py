"""Pencil Protector: the Leaf forehead protector on an indigo band, worn the builder's way with a
flat carpenter's pencil tucked behind the right ear and the band's tails knotted short at the back."""
from kit_shinobi import forehead_protector
from paint import solid

META = {"name": "Pencil Protector", "gender": "unisex",
        "description": "Leaf forehead protector on an indigo band, a carpenter's pencil tucked behind the right ear."}


def build(g):
    forehead_protector(g, band="D", seed=22761)
    pencil = g.piece("pencil", "HEAD", (-.5, -3.5, -.5), (1, 7, 1), pivot=(-4.6, -5.0, 0.2), rotation=(64, 0, 0),
                     scale=(.75, .75, .75))
    solid(pencil, "A", "smooth", 22762, 3, edge=False)
    pencil.top.fill("K1"), pencil.bottom.fill("S3")
    for face in pencil.sides:
        face.set(0, 0, "S3")
