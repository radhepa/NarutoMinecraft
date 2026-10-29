"""Masked Protector: the forehead protector on a leaf-green band worn with the clan's white fume
mask, the field medic's way of going into a gas-filled battlefield."""
from kit_shinobi import forehead_protector
from paint import k, solid

META = {"name": "Masked Protector", "gender": "unisex", "covers_mouth": True,
        "description": "Forehead protector on a green band, worn with the white pleated fume mask."}


def build(g):
    forehead_protector(g, band="D", seed=24811)
    mask = g.piece("fume_mask", "HEAD", (-4, -1.75, -4), (8, 2, 8), inflate=.25)
    solid(mask, "S", "weave", 24815, 3, edge=False)
    for face in mask.sides:
        face.hline(0, face.w - 1, 0, "D2")
    mask.front.hline(1, 6, 1, k("S", 2))
    mask.front.vline(3, 0, 1, "S4"), mask.front.set(4, 1, "S2")
