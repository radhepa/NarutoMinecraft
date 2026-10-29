"""Masked Protector: the forehead protector worn with a navy cloth mask pulled up over the nose and
mouth, wound once around the neck: the jonin who gives nothing away."""
from kit_shinobi import forehead_protector
from paint import solid

META = {"name": "Masked Protector", "gender": "unisex", "covers_mouth": True,
        "description": "Forehead protector with a navy cloth mask over the nose and mouth."}


def build(g):
    forehead_protector(g)
    mask = g.piece("face_mask", "HEAD", (-4, -1.75, -4), (8, 2, 8), inflate=.25)
    solid(mask, "D", "knit", 341, 2, edge=False)
    mask.front.vline(3, 0, 1, "D3"), mask.front.vline(4, 0, 1, "D1")
    for face in mask.sides:
        face.hline(0, face.w - 1, 0, "D3")
