"""Scarecrow Mask: Kakashi's way of wearing his face: the forehead protector slanted down over the
left brow and a navy cloth mask pulled up over the nose and mouth."""
from kit_hatake import face_mask, slanted_protector

META = {"name": "Scarecrow Mask", "gender": "unisex", "covers_mouth": True,
        "description": "Forehead protector slanted over the left brow, a navy cloth mask over nose and mouth."}


def build(g):
    slanted_protector(g)
    face_mask(g)
