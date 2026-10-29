"""Tide Protector: the leaf forehead protector on a deep teal band, worn the ordinary way."""
from kit_shinobi import forehead_protector

META = {"name": "Tide Protector", "gender": "unisex",
        "description": "The leaf forehead protector on a deep teal band."}


def build(g):
    forehead_protector(g, band="P", seed=20821)
