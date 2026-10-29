"""Hatake Cloth Mask: the clan's cloth face mask worn on its own, off duty: navy knit pulled up over
the nose and running down into the collar."""
from kit_hatake import face_mask

META = {"name": "Hatake Cloth Mask", "gender": "unisex", "covers_mouth": True,
        "description": "A navy knit mask over the nose and mouth, running down into the collar."}


def build(g):
    face_mask(g, seed=11975)
