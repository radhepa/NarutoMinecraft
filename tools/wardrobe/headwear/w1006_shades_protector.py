"""Shades and Protector: the forehead protector tied over the brow and the clan's round dark
shades below it, as Shino wears them on missions."""
from kit_aburame import lenses
from kit_shinobi import forehead_protector

META = {"name": "Shades and Protector", "gender": "unisex", "covers_face": True,
        "description": "Forehead protector over round dark shades."}


def build(g):
    forehead_protector(g, seed=10951)
    lenses(g, "K", "M", "round")
