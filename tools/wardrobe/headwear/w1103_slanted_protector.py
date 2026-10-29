"""Slanted Protector: the forehead protector tied aslant, dipping over the left brow, a fold of the band
hanging at the temple; the bare-faced Hatake way to wear it."""
from kit_hatake import slanted_protector

META = {"name": "Slanted Protector", "gender": "unisex",
        "description": "Forehead protector tied aslant over the left brow, a fold of band at the temple."}


def build(g):
    slanted_protector(g, seed=11981)
